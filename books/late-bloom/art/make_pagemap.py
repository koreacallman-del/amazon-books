"""페이지 배치표 생성 — manuscript-v8.docx → v8-page-map.md

  python3 make_pagemap.py

원고의 페이지 구분을 기준으로 "몇 쪽에 어떤 글이 놓이는지"를 뽑는다.
build.py와 make_ebook.py가 이 파일에서 본문을 읽으므로, 원고가 바뀌면
이것부터 다시 돌린다.

페이지 구분은 두 가지를 본다.
  1) 명시적 페이지 나눔  <w:br w:type="page"/>
  2) 워드가 마지막으로 렌더하며 남긴 경계  <w:lastRenderedPageBreak/>

저자가 워드에서 편집하면 명시적 나눔이 빈 문단으로 바뀌는 일이 잦다.
그때는 2)가 실제 쪽 배분을 알려주는 유일한 단서다. 1)이 있으면 1)을 쓰고,
없으면 2)로 넘어간다. 어느 쪽이든 저자가 워드에서 본 쪽 배분과 같아진다.
"""

import os
import re
import zipfile

from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
SRC = os.path.join(BOOK, "manuscript-v8.docx")
DST = os.path.join(BOOK, "v8-page-map.md")


def split_pages(path):
    """(쪽 목록, 사용한 구분 방식)"""
    raw = zipfile.ZipFile(path).read("word/document.xml")
    root = etree.fromstring(raw)
    body = root.find(W + "body")

    explicit = raw.count(b'w:type="page"')
    mode = "명시적 페이지 나눔" if explicit else "워드 렌더 경계"
    marker = f"{W}br" if explicit else f"{W}lastRenderedPageBreak"

    pages = [[]]
    for para in body.iter(W + "p"):
        line = []
        for run in para.iter(W + "r"):
            broke = False
            for el in run.iter(marker):
                if marker.endswith("br"):
                    broke = el.get(W + "type") == "page"
                else:
                    broke = True
                if broke:
                    break
            if broke:
                pages.append([])
            txt = "".join(t.text or "" for t in run.iter(W + "t"))
            if txt:
                line.append(txt)
        s = "".join(line).strip()
        if s:
            pages[-1].append(s)
    return pages, mode


def main():
    pages, mode = split_pages(SRC)
    lines = [l for pg in pages for l in pg]
    ko = len(re.findall(r"[가-힣]", "".join(lines)))

    out = [
        "# 「시계가 멈춘 마을」 v8 — 페이지별 텍스트 배치 (정본)",
        "",
        f"총 {len(pages)}페이지 · 한글 {ko:,}자 · "
        f"페이지당 평균 {ko / len(pages):.0f}자 · 판형 8.5×8.5in",
        "용도: 일러스트 작업 기준표. 각 페이지의 텍스트가 그 페이지의 '한 장면'이다.",
        "",
        f"※ 이 파일은 `art/make_pagemap.py`가 manuscript-v8.docx에서 생성한다. "
        f"쪽 구분은 **{mode}** 기준. 직접 고치지 말 것 — 원고를 고치고 다시 돌릴 것.",
        "",
    ]
    for i, pg in enumerate(pages, 1):
        out.append(f"--- p.{i} ---")
        out.extend(pg if pg else ["(빈 페이지)"])

    with open(DST, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    empty = sum(1 for pg in pages if not pg)
    print(f"완료 → {DST}")
    print(f"  {len(pages)}쪽 · 한글 {ko:,}자 · 줄 {len(lines)} · 빈 쪽 {empty}")
    print(f"  쪽 구분: {mode}")
    return len(pages)


if __name__ == "__main__":
    n = main()
    if n != 133:
        print(f"\n⚠ 페이지 수가 133이 아닙니다 ({n}쪽). "
              f"삽화 122장 대응이 어긋나므로 확인이 필요합니다.")

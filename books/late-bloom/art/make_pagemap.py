"""페이지 배치표 생성 — manuscript-v8.docx → v8-page-map.md

  python3 make_pagemap.py

원고의 페이지 나눔을 기준으로 "몇 쪽에 어떤 글이 놓이는지"를 뽑는다.
build.py가 이 파일에서 본문을 읽으므로, 원고가 바뀌면 이것부터 다시 돌린다.
"""

import os
import re

from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
SRC = os.path.join(BOOK, "manuscript-v8.docx")
DST = os.path.join(BOOK, "v8-page-map.md")


def split_pages(path):
    doc = Document(path)
    pages = [[]]
    for p in doc.paragraphs:
        broke = "<w:br" in p._p.xml and 'w:type="page"' in p._p.xml
        t = p.text.strip()
        if broke:
            pages.append([])
        if t:
            pages[-1].append(t)
    return pages


def main():
    pages = split_pages(SRC)
    lines = [l for pg in pages for l in pg]
    ko = len(re.findall(r"[가-힣]", "".join(lines)))

    out = [
        "# 「시계가 멈춘 마을」 v8 — 페이지별 텍스트 배치 (정본)",
        "",
        f"총 {len(pages)}페이지 · 한글 {ko:,}자 · "
        f"페이지당 평균 {ko / len(pages):.0f}자 · 판형 8.5×8.5in",
        "용도: 일러스트 작업 기준표. 각 페이지의 텍스트가 그 페이지의 '한 장면'이다.",
        "",
        "※ 이 파일은 `art/make_pagemap.py`가 manuscript-v8.docx에서 생성한다. "
        "직접 고치지 말 것 — 원고를 고치고 다시 돌릴 것.",
        "",
    ]
    for i, pg in enumerate(pages, 1):
        out.append(f"--- p.{i} ---")
        out.extend(pg if pg else ["(빈 페이지)"])

    with open(DST, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    empty = sum(1 for pg in pages if not pg)
    print(f"완료 → {DST}")
    print(f"  {len(pages)}쪽 · 한글 {ko:,}자 · 텍스트 줄 {len(lines)} · 빈 쪽 {empty}")
    return len(pages)


if __name__ == "__main__":
    n = main()
    if n != 133:
        print(f"\n⚠ 페이지 수가 133이 아닙니다 ({n}쪽). "
              f"art/pages.py의 조판표는 133쪽 기준이므로 맞춰야 합니다.")

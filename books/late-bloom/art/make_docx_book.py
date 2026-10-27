"""워드 편집본 생성 — 「시계가 멈춘 마을」 (삽화판)

  python3 make_docx_book.py

그림은 페이지 배경(글 뒤)으로 깔고, 글은 편집 가능한 텍스트로 올린다.
저자가 워드에서 문장을 직접 고칠 수 있어야 하므로 글자를 그림에 굽지 않는다.
조판 수치는 make_ebook.py(전자책 PDF)와 같게 맞춘다. 두 산출물이 어긋나면
저자가 워드에서 고친 결과와 PDF가 달라진다.

산출물: out/시계가-멈춘-마을_워드편집본.docx (8.5×8.5in, 133쪽)
"""

import io
import os

from PIL import Image
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from build import load_texts, OUT
from make_ebook import (image_map, edge_color, CHAPTER_PAGES, NO_IMAGE,
                        IMG_W, IMG_TOP, TEXT_Y, BODY, LEAD,
                        DENSE_N, DENSE_BODY, DENSE_LEAD, PT, TRIM)

HERE = os.path.dirname(os.path.abspath(__file__))
TRIM_IN = 8.5
DPI = 170                  # 편집용. 인쇄 제출은 PDF를 쓴다
JPEG_Q = 86
FONT_NAME = "나눔명조"      # 없으면 워드가 바탕/명조 계열로 대체한다


def jpeg_bytes(path, cache={}):
    if path in cache:
        return cache[path]
    im = Image.open(path).convert("RGB")
    target = round(IMG_W / PT * DPI)
    if im.width > target:
        r = target / im.width
        im = im.resize((target, round(im.height * r)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=JPEG_Q, optimize=True)
    cache[path] = buf.getvalue()
    return cache[path]


def send_behind(run, left_in, top_in, w_in, h_in):
    """인라인 그림을 지정한 자리에 고정된 '글 뒤' 배경으로 바꾼다."""
    inline = run._r.find(qn("w:drawing"))[0]
    anchor = OxmlElement("wp:anchor")
    for k, v in (("distT", "0"), ("distB", "0"), ("distL", "0"),
                 ("distR", "0"), ("simplePos", "0"), ("relativeHeight", "1"),
                 ("behindDoc", "1"), ("locked", "0"), ("layoutInCell", "1"),
                 ("allowOverlap", "1")):
        anchor.set(k, v)
    sp = OxmlElement("wp:simplePos"); sp.set("x", "0"); sp.set("y", "0")
    anchor.append(sp)
    for tag, off in (("wp:positionH", Inches(left_in)),
                     ("wp:positionV", Inches(top_in))):
        pos = OxmlElement(tag)
        pos.set("relativeFrom", "page")
        o = OxmlElement("wp:posOffset"); o.text = str(int(off))
        pos.append(o)
        anchor.append(pos)
    ext = OxmlElement("wp:extent")
    ext.set("cx", str(int(Inches(w_in)))); ext.set("cy", str(int(Inches(h_in))))
    anchor.append(ext)
    ee = OxmlElement("wp:effectExtent")
    for k in ("l", "t", "r", "b"):
        ee.set(k, "0")
    anchor.append(ee)
    anchor.append(OxmlElement("wp:wrapNone"))
    for tag in ("wp:docPr", "wp:cNvGraphicFramePr"):
        el = inline.find(qn(tag))
        if el is not None:
            anchor.append(el)
    graphic = inline.find(qn("a:graphic"))
    anchor.append(graphic if graphic is not None else inline[-1])
    parent = inline.getparent()
    parent.remove(inline)
    parent.append(anchor)


def page_shade(doc_body_para, rgb):
    """문단 배경색 — 쪽 전체 바탕 역할."""
    pPr = doc_body_para._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "%02X%02X%02X" % rgb)
    pPr.append(shd)


def set_font(run, name, size_pt, rgb=(0x1C, 0x1A, 0x17), bold=False):
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(*rgb)
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:eastAsia", "w:ascii", "w:hAnsi"):
        rf.set(qn(a), name)


def build():
    texts = load_texts()
    pages, found = image_map()

    d = Document()
    sec = d.sections[0]
    sec.page_width = Inches(TRIM_IN)
    sec.page_height = Inches(TRIM_IN)
    for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(sec, side, Inches(0))
    sec.header_distance = Inches(0)
    sec.footer_distance = Inches(0)

    st = d.styles["Normal"]
    st.font.size = Pt(BODY)
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.space_before = Pt(0)

    # PDF와 같은 자리 (inch)
    img_top_in = IMG_TOP / PT
    text_top_in = (TRIM - TEXT_Y) / PT - 0.16     # 첫 줄 윗선

    for n in range(1, 134):
        img = pages.get(n)
        lines = texts.get(n, [])

        p = d.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = Pt(1)
        if img:
            iw, ih = Image.open(img).size
            w_in = IMG_W / PT
            h_in = w_in * ih / iw
            run = p.add_run()
            run.add_picture(io.BytesIO(jpeg_bytes(img)), width=Inches(w_in))
            send_behind(run, (TRIM_IN - w_in) / 2, img_top_in, w_in, h_in)

        if lines:
            if n == 1:
                tops, sizes = 3.3, [(28, True), (15, False)]
            elif n == 133:
                tops, sizes = 1.0, [(17, True), (11.5, False)]
            elif n in CHAPTER_PAGES:
                tops, sizes = 3.6, [(19, True)]
            else:
                tops, sizes = text_top_in, [(BODY, False)]

            dense = (n not in NO_IMAGE and
                     sum(len(l) for l in lines) > 150)
            size = DENSE_BODY if dense else sizes[-1][0]
            lead = DENSE_LEAD if dense else LEAD
            centered = n == 1 or n in CHAPTER_PAGES

            for i, s in enumerate(lines):
                tp = d.add_paragraph()
                tp.paragraph_format.space_before = (
                    Inches(tops) if i == 0 else Pt(0))
                tp.paragraph_format.space_after = Pt(0)
                head = (n == 1 and i == 0) or (n == 133 and i == 0) or \
                       (n in CHAPTER_PAGES)
                sz, bold = sizes[0] if head else (size, False)
                tp.paragraph_format.line_spacing = Pt(
                    sz * 1.55 if head else lead)
                if centered or (n == 133 and i == 0):
                    tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    tp.paragraph_format.left_indent = Inches(0.8)
                    tp.paragraph_format.right_indent = Inches(0.8)
                else:
                    tp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    tp.paragraph_format.left_indent = Inches(1.07)
                    tp.paragraph_format.right_indent = Inches(0.75)
                r = tp.add_run(s)
                set_font(r, FONT_NAME, sz,
                         (0x5C, 0x55, 0x4E) if (n == 1 and i) else
                         (0x1C, 0x1A, 0x17), bold)

        if n < 133:
            d.add_page_break()

    path = os.path.join(OUT, "시계가-멈춘-마을_워드편집본.docx")
    d.save(path)
    return path, len(pages)


if __name__ == "__main__":
    path, n_img = build()
    mb = os.path.getsize(path) / 1024 / 1024
    print(f"완료 → {path}")
    print(f"  133쪽 · 삽화 {n_img}장 · {mb:.1f} MB · {DPI}dpi")
    print("  글은 워드에서 직접 수정할 수 있습니다. 그림은 배경으로 고정됩니다.")

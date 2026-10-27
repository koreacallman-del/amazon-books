"""전자책 PDF 생성 — 「시계가 멈춘 마을」

  python3 make_ebook.py

전자책은 제본이 없다. 책등 여백이 필요 없고, 인쇄 300dpi 제약도 없다.
그래서 그림을 인쇄본(5.1in)보다 크게(7.3in) 쓴다.

페이지 바탕은 그 쪽 그림의 모서리 색을 뽑아 깐다. 그림과 바탕이 같은
크림색이 되어 그림의 네모 테두리가 사라지고 한 장처럼 보인다.

산출물: out/시계가-멈춘-마을_전자책.pdf (8.5×8.5in, 133쪽)
"""

import glob
import io
import os
import re

from PIL import Image
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from build import load_texts, OUT

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
ART = os.path.join(BOOK, "illustrations")

PT = 72.0
TRIM = 8.5 * PT                 # 정사각 페이지
IMG_W = 7.3 * PT                # 전자책은 크게 — 인쇄본은 5.1in
SIDE = 0.62 * PT                # 글 좌우 여백

# 나눔명조. reportlab 내장 한국어 CID 폰트는 한글 폭 계산이 부정확해서
# 가운데 정렬이 틀어지고 자간이 벌어진다. TTF를 직접 심는다.
FONT = "NanumMyeongjo"
FONT_B = "NanumMyeongjo-Bold"
FONT_DIR = os.path.join(HERE, "fonts")

# 그림이 없는 11쪽
CHAPTER_PAGES = {2, 22, 36, 53, 69, 78, 88, 99, 120}
NO_IMAGE = {1, 133} | CHAPTER_PAGES


def image_map():
    """파일명 앞 숫자로 001~122를 뽑아, 그림 없는 쪽을 건너뛰며 쪽에 붙인다."""
    found = {}
    for p in glob.glob(os.path.join(ART, "*.png")):
        m = re.match(r"^(\d{3})", os.path.basename(p)) or \
            re.search(r"illustration-(\d{3})", p)
        if m:
            found[int(m.group(1))] = p
    targets = [n for n in range(1, 134) if n not in NO_IMAGE]
    return {pg: found[i] for i, pg in enumerate(targets, 1) if i in found}, found


def paper_of(path, cache={}):
    """그림 가장자리 색 = 그 쪽의 바탕색."""
    if path in cache:
        return cache[path]
    r, g, b = edge_color(Image.open(path).convert("RGB"))
    cache[path] = Color(r / 255, g / 255, b / 255)
    return cache[path]


DEFAULT_PAPER = Color(253 / 255, 248 / 255, 238 / 255)

JPEG_Q = 88          # 전자책용. 화면에서 열화가 보이지 않는 선
MAX_PX = 1536        # 원본 그대로. 7.3in에 넣으면 약 210dpi
FEATHER = 40         # 그림 가장자리를 바탕색으로 풀어주는 폭(px)

# 조판 기준 — 전부 고정값이다. 쪽마다 달라지면 책장을 넘길 때 글이 뛴다.
IMG_TOP = 78.0                   # 그림 위 여백
TEXT_Y = 150.0                   # 본문 첫 줄 기준선 (쪽 아래에서)
BODY = 14.0                      # 본문 크기 — 폰에서 읽히는 하한
LEAD = 23.0
DENSE_N = 6                      # 이 줄 수 이상이면 촘촘하게
DENSE_BODY, DENSE_LEAD = 12.5, 20.0


def edge_color(im):
    """가장자리 띠의 평균색. 모서리 한 점보다 정확하다.

    그림 안쪽은 종이 결과 비네팅 때문에 변 중간 밝기가 모서리와 다르다.
    모서리 한 점으로 바탕을 맞추면 네모 윤곽이 희미하게 남는다.
    """
    w, h = im.size
    b = max(4, min(w, h) // 120)
    px = []
    for strip in (im.crop((0, 0, w, b)), im.crop((0, h - b, w, h)),
                  im.crop((0, 0, b, h)), im.crop((w - b, 0, w, h))):
        s = strip.resize((1, 1), Image.LANCZOS)
        px.append(s.getpixel((0, 0)))
    return tuple(sum(c[i] for c in px) // len(px) for i in range(3))


def feather_mask(size, px):
    """가장자리에서 안쪽으로 서서히 불투명해지는 마스크."""
    w, h = size
    m = Image.new("L", size, 255)
    draw_px = m.load()
    for i in range(px):
        v = int(255 * (i + 1) / (px + 1))
        for x in range(w):
            draw_px[x, i] = min(draw_px[x, i], v)
            draw_px[x, h - 1 - i] = min(draw_px[x, h - 1 - i], v)
        for y in range(h):
            draw_px[i, y] = min(draw_px[i, y], v)
            draw_px[w - 1 - i, y] = min(draw_px[w - 1 - i, y], v)
    return m


def as_jpeg(path, cache={}):
    """PNG를 JPEG로 바꾸고 가장자리를 바탕색으로 풀어 메모리에 올린다.

    PNG는 무손실이라 그대로 넣으면 133쪽이 288MB가 된다. 전자책은 화면에서
    보는 것이므로 그 용량이 의미가 없고, 배송비와 내려받기 시간만 늘린다.
    """
    if path in cache:
        return cache[path]
    im = Image.open(path).convert("RGB")
    if max(im.size) > MAX_PX:
        r = MAX_PX / max(im.size)
        im = im.resize((round(im.width * r), round(im.height * r)),
                       Image.LANCZOS)
    bg = Image.new("RGB", im.size, edge_color(im))
    bg.paste(im, (0, 0), feather_mask(im.size, FEATHER))
    buf = io.BytesIO()
    bg.save(buf, "JPEG", quality=JPEG_Q, optimize=True, progressive=True)
    buf.seek(0)
    cache[path] = ImageReader(buf)
    return cache[path]


def wrap(c, text, width, size, font):
    """글자 단위 줄바꿈. 한국어는 단어 경계가 덜 중요하다."""
    out, cur = [], ""
    for ch in text:
        if c.stringWidth(cur + ch, font, size) > width and cur:
            out.append(cur)
            cur = ch
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def draw_text(c, lines, top_y, size, lead, center=False, font=None):
    font = font or FONT
    c.setFillColorRGB(0.11, 0.10, 0.09)
    y = top_y
    for ln in lines:
        for seg in wrap(c, ln, TRIM - SIDE * 2 - 0.9 * PT, size, font):
            if center:
                c.drawCentredString(TRIM / 2, y, seg)
            else:
                c.drawString(SIDE + 0.45 * PT, y, seg)
            y -= lead
    return y


def build():
    pdfmetrics.registerFont(TTFont(FONT, os.path.join(FONT_DIR, "NanumMyeongjo.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_B, os.path.join(FONT_DIR, "NanumMyeongjo-Bold.ttf")))
    texts = load_texts()
    pages, found = image_map()

    path = os.path.join(OUT, "시계가-멈춘-마을_전자책.pdf")
    c = rl_canvas.Canvas(path, pagesize=(TRIM, TRIM))
    c.setTitle("시계가 멈춘 마을")
    c.setAuthor("곽 훈 안토니오")

    for n in range(1, 134):
        img = pages.get(n)
        c.setFillColor(paper_of(img) if img else DEFAULT_PAPER)
        c.rect(0, 0, TRIM, TRIM, stroke=0, fill=1)
        lines = texts.get(n, [])

        if n == 1:                                   # 표제지
            c.setFont(FONT_B, 34)
            draw_text(c, lines[:1], TRIM * 0.57, 34, 44, center=True, font=FONT_B)
            c.setFont(FONT, 17)
            c.setFillColorRGB(0.36, 0.33, 0.30)
            draw_text(c, lines[1:], TRIM * 0.46, 17, 24, center=True)

        elif n == 133:                               # 작가의 말
            c.setFont(FONT_B, 19)
            draw_text(c, lines[:1], TRIM - 1.7 * PT, 19, 28, center=True, font=FONT_B)
            c.setFont(FONT, 12)
            draw_text(c, lines[1:], TRIM - 3.0 * PT, 12, 19.5)

        elif n in CHAPTER_PAGES:                     # 장 제목
            c.setFont(FONT_B, 22)
            draw_text(c, lines, TRIM * 0.52, 22, 32, center=True, font=FONT_B)

        else:
            iw, ih = Image.open(img).size
            w = IMG_W
            h = w * ih / iw
            # 그림 위치와 글 높이를 쪽마다 고정한다. 책장을 넘길 때 글이
            # 같은 자리에 있어야 책처럼 읽힌다.
            c.drawImage(as_jpeg(img), (TRIM - w) / 2, TRIM - IMG_TOP - h,
                        w, h, mask=None)
            if lines:
                # 저자가 워드에서 문장을 합쳐 한 줄이 84자까지 나온다.
                # 자동 줄바꿈 뒤의 실제 줄 수로 크기를 정해야 넘치지 않는다.
                width = TRIM - SIDE * 2 - 0.9 * PT
                n_wrapped = sum(len(wrap(c, ln, width, BODY, FONT))
                                for ln in lines)
                dense = n_wrapped >= DENSE_N
                size = DENSE_BODY if dense else BODY
                lead = DENSE_LEAD if dense else LEAD
                c.setFont(FONT, size)
                draw_text(c, lines, TEXT_Y, size, lead)

        c.showPage()

    c.save()
    return path, pages, found


if __name__ == "__main__":
    path, pages, found = build()
    mb = os.path.getsize(path) / 1024 / 1024
    print(f"완료 → {path}  ({mb:.1f} MB · 133쪽)")
    print(f"그림 배치: {len(pages)}쪽 / 원본 {len(found)}장")
    miss = [n for n in range(1, 134) if n not in pages and n not in NO_IMAGE]
    print(f"그림 없는 쪽: {sorted(NO_IMAGE)}")
    if miss:
        print(f"⚠ 그림이 비어버린 쪽: {miss}")

"""133장 생성기 — SVG · PDF · 프루프

  python3 build.py

산출물:
  out/svg/p001.svg …            낱장
  out/late-bloom-interior.pdf   인쇄용 (8.5×8.5in, 134p)
  out/proof.html                전체 열람용
"""

import os
import re
import math

import ink
import objects
from ink import (INK, INK_SOFT, GOLD, PAPER, HAIR, FINE, GUTTER, OUTER,
                 line, curve, to_svg, to_pdf)
from pages import P, GOLD_PAGES, CHAPTER_PAGES

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")

# 선의 온도 — 부마다 달라진다
COLD, THAW, GOLDZ, WARM = range(4)


def zone_of(n):
    if n <= 32:
        return COLD
    if n <= 64:
        return THAW
    if n <= 119:
        return GOLDZ
    return WARM


def page_text(n, texts):
    return texts.get(n, [])


def load_texts():
    """v8-page-map.md에서 페이지별 본문을 읽는다."""
    path = os.path.join(BOOK, "v8-page-map.md")
    out, cur = {}, None
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"^--- p\.(\d+) ---", ln.strip())
        if m:
            cur = int(m.group(1))
            out[cur] = []
            continue
        s = ln.strip()
        if cur and s and not s.startswith("(빈 페이지)") and not s.startswith("#") \
                and not s.startswith("총 ") and not s.startswith("용도"):
            out[cur].append(s)
    return out


def spine_side(n):
    """1쪽이 오른쪽 면이므로 홀수는 책등 왼쪽, 짝수는 오른쪽."""
    return "left" if n % 2 else "right"


def main_line(n):
    """책 전체를 관통하는 주선. 홀수에서 나간 높이로 짝수에 들어온다."""
    if n in CHAPTER_PAGES:
        return []
    z = zone_of(n)
    color = {COLD: INK_SOFT, THAW: INK_SOFT, GOLDZ: GOLD, WARM: GOLD}[z]
    op = {COLD: 0.30, THAW: 0.34, GOLDZ: 0.32, WARM: 0.42}[z]
    y = 84 + 5.5 * math.sin(n * 0.42)
    if n % 2:
        return [line(62, y + 1.4, 100, y, HAIR, color, n * 7, 0.10, 4, op)]
    return [line(0, y, 38, y + 1.2, HAIR, color, n * 7 + 1, 0.10, 4, op)]


def chapter_line(n):
    """장 제목 페이지 — 사물 없이 선 하나와 여백."""
    z = zone_of(n)
    color = GOLD if z >= GOLDZ else INK_SOFT
    idx = sorted(CHAPTER_PAGES).index(n)
    if n == 2:
        return [line(22, 74, 78, 30, FINE, color, 201, 0.14, 6, 0.55)]
    if n == 120:
        return [line(24, 34, 76, 70, FINE, color, 220, 0.14, 6, 0.6)]
    y = 40 + idx * 3.2
    return [curve([(18, y + 10), (40, y), (62, y + 6), (82, y - 4)],
                  FINE, color, 200 + n, 0.16, opacity=0.5)]


def compose(n, texts):
    """한 페이지의 획과 글을 만든다.

    주선은 의도적으로 판면 밖으로 나간다(다음 장으로 이어짐). 안전영역
    검사 대상이 아니므로 사물과 분리해서 돌려준다.
    """
    items, tpos = P[n]
    gold = n in GOLD_PAGES
    bleed = chapter_line(n) if n in CHAPTER_PAGES else main_line(n)
    strokes = []

    for fn_name, x, y, s, kw in items:
        fn = getattr(objects, fn_name)
        kwargs = dict(kw)
        if "gold" in fn.__code__.co_varnames[:fn.__code__.co_argcount]:
            kwargs.setdefault("gold", gold)
        seed_name = "seed" if "seed" in fn.__code__.co_varnames[:fn.__code__.co_argcount] else None
        if seed_name:
            kwargs.setdefault("seed", n * 13 + len(strokes))
        strokes += fn(x, y, s, **kwargs)

    lines = page_text(n, texts)
    out_text = []
    if lines:
        big = (n == 1)
        size = 5.0 if big else 3.35
        lead = 6.6 if big else 6.0
        if tpos == "top":
            y0 = 24
        elif tpos == "mid":
            y0 = 48 - (len(lines) - 1) * lead / 2
        else:
            y0 = 100 - OUTER - 6 - (len(lines) - 1) * lead
        # 텍스트도 책등을 피한다
        x = 50 if (big or tpos == "mid") else (
            GUTTER + 12 if n % 2 else OUTER + 9)
        anchor = "middle" if (big or tpos == "mid") else "start"
        for i, s in enumerate(lines):
            esc = (s.replace("&", "&amp;").replace("<", "&lt;")
                   .replace(">", "&gt;"))
            out_text.append({
                "x": x, "y": y0 + i * lead, "s": esc,
                "size": size if i == 0 or not big else size * 0.62,
                "anchor": anchor,
                "color": INK if i == 0 or not big else INK_SOFT,
            })
    return bleed, strokes, out_text


def _xs(d):
    """경로에서 실제 x좌표만 뽑는다. 원호(a)의 반지름·플래그는 좌표가 아니다."""
    toks = re.findall(r"[MLCZAaz]|-?\d*\.?\d+", d)
    xs, i, cmd, cur = [], 0, None, 0.0
    while i < len(toks):
        t = toks[i]
        if t in "MLCZAaz":
            cmd, i = t, i + 1
            continue
        if cmd in ("M", "L"):
            xs.append(float(toks[i])); cur = float(toks[i]); i += 2
        elif cmd == "C":
            for k in (0, 2, 4):
                xs.append(float(toks[i + k]))
            cur = float(toks[i + 4]); i += 6
        elif cmd in ("A", "a"):
            dx = float(toks[i + 5])
            cur = cur + dx if cmd == "a" else dx
            xs.append(cur); i += 7
        else:
            i += 1
    return xs


def check(n, strokes):
    """책등 안전영역 침범 검사."""
    lo, hi = ((GUTTER, 100 - OUTER) if spine_side(n) == "left"
              else (OUTER, 100 - GUTTER))
    bad = 0
    for s in strokes:
        if s.bleed:
            continue
        r = s.width / 2 if s.width else 0
        for x in _xs(s.d):
            if x - r < lo - 0.01 or x + r > hi + 0.01:
                bad += 1
                break
    return bad


def build():
    os.makedirs(os.path.join(OUT, "svg"), exist_ok=True)
    texts = load_texts()
    pdf_pages, proof, warn = [], [], []

    for n in range(1, 134):
        bleed, content, tx = compose(n, texts)
        bad = check(n, content)
        if bad:
            warn.append((n, bad))
        strokes = bleed + content
        svg = to_svg(strokes, tx, spine_side(n))
        with open(os.path.join(OUT, "svg", f"p{n:03d}.svg"), "w",
                  encoding="utf-8") as f:
            f.write(svg)
        pdf_pages.append((strokes, tx))
        proof.append((n, svg))

    # 인쇄는 짝수 페이지. 133 → 134 (판권면 자리)
    pdf_pages.append(([], []))
    to_pdf(pdf_pages, os.path.join(OUT, "late-bloom-interior.pdf"))

    write_proof(proof, texts)
    return warn


def write_proof(proof, texts):
    gold = sorted(GOLD_PAGES)
    cards = []
    for n, svg in proof:
        tags = []
        if n in CHAPTER_PAGES:
            tags.append("장 제목")
        if n in GOLD_PAGES:
            tags.append("금빛")
        has_hand = any(k in str(P[n][0]) for k in
                       ("hand_", "palm_open", "two_hands", "fist"))
        if has_hand:
            tags.append("손")
        tag_html = "".join(f'<i>{t}</i>' for t in tags)
        cards.append(
            f'<figure id="p{n}"><div class="sheet">{svg}</div>'
            f'<figcaption><b>{n}</b>{tag_html}</figcaption></figure>')

    html = f"""<title>시계가 멈춘 마을 전장</title>
<style>
:root{{--bg:#E8E6E0;--bg2:#DEDCD4;--edge:#C9C6BC;--fg:#4A4B46;--dim:#767771;
--head:#23241F;--mark:#6B7A5E;
--serif:'Nanum Myeongjo',serif;--sans:'IBM Plex Sans KR',system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
--bg:#22241F;--bg2:#2B2E28;--edge:#3C4037;--fg:#C4C7BD;--dim:#8E9288;
--head:#EFF0E9;--mark:#9CB08A;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#22241F;--bg2:#2B2E28;--edge:#3C4037;
--fg:#C4C7BD;--dim:#8E9288;--head:#EFF0E9;--mark:#9CB08A;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--sans);margin:0}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 20px;padding-block:36px 60px}}
h1{{font-family:var(--serif);color:var(--head);font-size:clamp(1.5rem,4vw,2.1rem);
margin:0 0 10px;font-weight:700;text-wrap:balance}}
.lede{{max-width:64ch;line-height:1.7;font-size:.94rem;margin:0 0 18px}}
.stats{{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0 0 26px}}
.stats li{{font-size:.72rem;letter-spacing:.05em;text-transform:uppercase;
color:var(--dim);border:1px solid var(--edge);background:var(--bg2);
padding:5px 9px;border-radius:2px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:18px}}
figure{{margin:0;min-width:0}}
.sheet{{border:1px solid var(--edge);box-shadow:0 3px 10px rgba(0,0,0,.12);
background:{PAPER};aspect-ratio:1;overflow:hidden}}
.sheet svg{{display:block;width:100%;height:auto}}
figcaption{{display:flex;align-items:center;gap:6px;flex-wrap:wrap;
margin-top:6px;font-size:.72rem;color:var(--dim)}}
figcaption b{{font-family:var(--serif);color:var(--head);font-size:.86rem;
font-variant-numeric:tabular-nums}}
figcaption i{{font-style:normal;font-size:.62rem;letter-spacing:.04em;
color:var(--mark);border:1px solid var(--edge);padding:1px 5px;border-radius:2px}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&family=IBM+Plex+Sans+KR:wght@400;500&display=swap">
<div class="wrap">
<h1>시계가 멈춘 마을 — 전장 133쪽</h1>
<p class="lede">작화 엔진으로 생성한 본문 전체입니다. 133장이 같은 선 규칙·같은 먹색·같은
금색을 씁니다. 사물 75종, 손은 43쪽에만, 금빛은 30쪽에만 들어갑니다.
벡터이므로 인쇄 해상도에서 선이 깨지지 않습니다.</p>
<ul class="stats"><li>133쪽</li><li>사물 75종</li><li>손 43쪽</li>
<li>금빛 30쪽</li><li>8.5×8.5in</li><li>먹 + 금 1색</li></ul>
<div class="grid">{''.join(cards)}</div>
</div>"""
    with open(os.path.join(OUT, "proof.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    warn = build()
    print(f"생성 완료 → {OUT}")
    if warn:
        print(f"⚠ 책등 안전영역 확인 필요: {len(warn)}쪽")
        for n, b in warn[:12]:
            print(f"   p.{n} ({b}획)")
    else:
        print("책등 안전영역: 133쪽 전부 통과")

"""작화 엔진 — 「시계가 멈춘 마을」

좌표계는 0~100 정사각. 최종 판형 8.5×8.5in에 비례 매핑된다.
모든 그림은 여기 정의된 프리미티브만 사용한다. 그래야 133장이 흔들리지 않는다.

선에 미세한 떨림(tremble)을 준다. 기계적인 직선은 인쇄물에서 차갑게 보이기 때문이다.
떨림은 페이지 번호로 시드를 고정해서, 몇 번 생성해도 같은 그림이 나온다.
"""

import math

# ── 재료 ────────────────────────────────────────────────────────────────
PAPER = "#F6F1E6"      # 크림 종이
INK = "#1C1A17"        # 먹 — 순흑이 아닌 따뜻한 검정
INK_SOFT = "#56504A"   # 옅은 먹 (배경 요소, 담선)
GOLD = "#A8822F"       # 금 — 채도 낮은 앤티크 골드

# 선 굵기 (0~100 좌표 기준)
HAIR = 0.24
FINE = 0.30
THIN = 0.42
MED = 0.62
BOLD = 0.88

# 인쇄 안전 영역
GUTTER = 4.4           # 책등 쪽 0.375in
OUTER = 2.9            # 바깥·위·아래 0.25in


class Stroke:
    """렌더러에 전달되는 단일 획.

    bleed=True는 판면 밖으로 의도적으로 나가는 획(다음 장으로 이어지는 주선,
    화면 밖에서 들어오는 담벼락 등). 책등 안전영역 검사에서 제외된다.
    """
    __slots__ = ("d", "color", "width", "opacity", "dash", "fill", "cap",
                 "bleed")

    def __init__(self, d, color=INK, width=THIN, opacity=1.0,
                 dash=None, fill="none", cap="round", bleed=False):
        self.d = d
        self.color = color
        self.width = width
        self.opacity = opacity
        self.dash = dash
        self.fill = fill
        self.cap = cap
        self.bleed = bleed


class _Rng:
    """결정적 난수. 같은 시드면 항상 같은 그림."""

    def __init__(self, seed):
        self.s = (seed * 1103515245 + 12345) & 0x7FFFFFFF

    def next(self):
        self.s = (self.s * 1103515245 + 12345) & 0x7FFFFFFF
        return self.s / 0x7FFFFFFF

    def sym(self, amp):
        return (self.next() * 2 - 1) * amp


def _fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ── 경로 생성 ───────────────────────────────────────────────────────────

def _catmull(pts, closed=False):
    """점들을 지나는 매끄러운 베지에 경로."""
    if len(pts) < 2:
        return ""
    if len(pts) == 2:
        (x0, y0), (x1, y1) = pts
        return f"M{_fmt(x0)} {_fmt(y0)} L{_fmt(x1)} {_fmt(y1)}"

    p = list(pts)
    if closed:
        p = [pts[-1]] + list(pts) + [pts[0], pts[1]]
    else:
        p = [pts[0]] + list(pts) + [pts[-1]]

    d = f"M{_fmt(p[1][0])} {_fmt(p[1][1])}"
    for i in range(1, len(p) - 2):
        x0, y0 = p[i - 1]
        x1, y1 = p[i]
        x2, y2 = p[i + 1]
        x3, y3 = p[i + 2]
        c1x, c1y = x1 + (x2 - x0) / 6.0, y1 + (y2 - y0) / 6.0
        c2x, c2y = x2 - (x3 - x1) / 6.0, y2 - (y3 - y1) / 6.0
        d += (f" C{_fmt(c1x)} {_fmt(c1y)} {_fmt(c2x)} {_fmt(c2y)}"
              f" {_fmt(x2)} {_fmt(y2)}")
    if closed:
        d += " Z"
    return d


def tremble(pts, seed, amp=0.13):
    """점들을 미세하게 흔든다. 손으로 그린 느낌."""
    r = _Rng(seed)
    return [(x + r.sym(amp), y + r.sym(amp)) for x, y in pts]


def line(x1, y1, x2, y2, w=THIN, color=INK, seed=1, amp=0.10,
         seg=5, opacity=1.0):
    """미세하게 떨리는 직선."""
    pts = []
    for i in range(seg + 1):
        t = i / seg
        pts.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
    inner = tremble(pts[1:-1], seed, amp)
    pts = [pts[0]] + inner + [pts[-1]]
    return Stroke(_catmull(pts), color, w, opacity)


def curve(pts, w=THIN, color=INK, seed=0, amp=0.0, closed=False,
          opacity=1.0, fill="none", dash=None):
    """점들을 지나는 곡선."""
    if amp:
        pts = tremble(pts, seed, amp)
    return Stroke(_catmull(pts, closed), color, w, opacity, dash, fill)


def arc(cx, cy, r, a0, a1, w=THIN, color=INK, seed=0, amp=0.0,
        steps=None, opacity=1.0):
    """중심 (cx,cy), 반지름 r, a0~a1도(12시=0, 시계방향)."""
    span = abs(a1 - a0)
    steps = steps or max(8, int(span / 9))
    pts = []
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps - 90)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return curve(pts, w, color, seed, amp, opacity=opacity)


def ring(cx, cy, r, w=THIN, color=INK, gap=None, seed=0, amp=0.0):
    """원. gap=(시작도, 끝도)를 주면 그 구간이 끊긴다."""
    if gap is None:
        return arc(cx, cy, r, 0, 360, w, color, seed, amp)
    g0, g1 = gap
    return arc(cx, cy, r, g1, g0 + 360, w, color, seed, amp)


def dot(cx, cy, r, color=INK, opacity=1.0):
    d = (f"M{_fmt(cx - r)} {_fmt(cy)} a{_fmt(r)} {_fmt(r)} 0 1 0 {_fmt(r * 2)} 0"
         f" a{_fmt(r)} {_fmt(r)} 0 1 0 {_fmt(-r * 2)} 0 Z")
    return Stroke(d, color, 0, opacity, None, color)


def crack(x, y, length, angle=90, seed=3, w=HAIR, color=INK,
          steps=5, spread=0.55, opacity=0.85):
    """실금. 지그재그로 갈라지는 가는 선."""
    r = _Rng(seed)
    a = math.radians(angle - 90)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    pts = []
    for i in range(steps + 1):
        t = i / steps
        off = r.sym(spread) * (1 - abs(t - 0.5) * 0.7)
        pts.append((x + ux * length * t + px * off,
                    y + uy * length * t + py * off))
    return Stroke(_catmull(pts), color, w, opacity)


def hatch(x, y, w_box, h_box, n=6, angle=60, w=HAIR, color=INK,
          seed=5, opacity=0.7):
    """평행 빗금. 어두움·무게를 나타낸다."""
    out = []
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    for i in range(n):
        t = (i + 0.5) / n
        sx = x + w_box * t
        sy = y
        ln = min(h_box, w_box)
        out.append(line(sx, sy, sx + dx * ln * 0.55, sy + dy * ln * 0.55,
                        w, color, seed + i, 0.06, 3, opacity))
    return out


def weave(cx, cy, rx, ry, n=9, seed=7, w=FINE, color=INK):
    """엮인 질감 — 둥지, 바구니. 짧은 호가 교차한다."""
    out = []
    out.append(curve([(cx - rx, cy - ry * 0.5), (cx - rx * 0.75, cy + ry * 0.55),
                      (cx, cy + ry), (cx + rx * 0.75, cy + ry * 0.55),
                      (cx + rx, cy - ry * 0.5)], THIN, color, seed, 0.10))
    for i in range(n):
        t = (i + 0.5) / n
        sx = cx - rx + rx * 2 * t
        depth = ry * (1 - abs(t - 0.5) * 1.1)
        out.append(curve([(sx, cy - ry * 0.45),
                          (sx + (0.5 - t) * rx * 0.28, cy + depth * 0.45),
                          (sx + (0.5 - t) * rx * 0.55, cy + depth * 0.92)],
                         w * 0.8, color, seed + 11 + i, 0.08, opacity=0.9))
    for k, f in ((0.62, 0.55), (0.86, 0.78)):
        out.append(curve([(cx - rx * (1 - k * 0.25), cy + ry * f * 0.5),
                          (cx, cy + ry * f),
                          (cx + rx * (1 - k * 0.25), cy + ry * f * 0.5)],
                         HAIR, color, seed + 40 + int(k * 100), 0.07,
                         opacity=0.65))
    return out


def silhouette(pts, color=INK, opacity=0.92, seed=0, amp=0.08):
    """눈 없는 붓 실루엣 — 새, 고양이. 면으로 채운다."""
    if amp:
        pts = tremble(pts, seed, amp)
    return Stroke(_catmull(pts, closed=True), color, 0, opacity, None, color)


def thread(x1, y1, x2, y2, color=GOLD, w=0.5, seed=9, amp=0.16, seg=7):
    """실땀 — 끊어진 것이 이어지는 자리. 점선."""
    s = line(x1, y1, x2, y2, w, color, seed, amp, seg)
    s.dash = "2.4 1.9"
    return s


# ── 렌더러 ──────────────────────────────────────────────────────────────

def to_svg(strokes, texts=(), guide_side=None, size=520, show_guide=False):
    """SVG 문자열. guide_side는 'left'(홀수) 또는 'right'(짝수)."""
    parts = [f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" '
             f'xmlns="http://www.w3.org/2000/svg">',
             f'<rect width="100" height="100" fill="{PAPER}"/>']
    for s in strokes:
        attrs = [f'd="{s.d}"', f'fill="{s.fill}"']
        if s.width:
            attrs += [f'stroke="{s.color}"', f'stroke-width="{_fmt(s.width)}"',
                      f'stroke-linecap="{s.cap}"', 'stroke-linejoin="round"']
        if s.opacity < 1:
            attrs.append(f'opacity="{_fmt(s.opacity)}"')
        if s.dash:
            attrs.append(f'stroke-dasharray="{s.dash}"')
        parts.append("<path " + " ".join(attrs) + "/>")
    for t in texts:
        anchor = t.get("anchor", "start")
        parts.append(
            f'<text x="{_fmt(t["x"])}" y="{_fmt(t["y"])}" '
            f'text-anchor="{anchor}" font-size="{_fmt(t.get("size", 3.4))}" '
            f'fill="{t.get("color", INK)}" '
            f'font-family="Nanum Myeongjo, serif">{t["s"]}</text>')
    if show_guide and guide_side:
        gx = GUTTER if guide_side == "left" else 100 - GUTTER
        parts.append(f'<path d="M{_fmt(gx)} 0 L{_fmt(gx)} 100" stroke="#C0392B" '
                     f'stroke-width="0.35" stroke-dasharray="2 1.6" '
                     f'fill="none" opacity="0.5"/>')
    parts.append("</svg>")
    return "".join(parts)


def _svg_path_to_pdf(canvas, d, scale, h):
    """SVG 경로를 reportlab 경로로 옮긴다. M/L/C/Z/a만 쓴다."""
    import re
    toks = re.findall(r"[MLCZAaz]|-?\d*\.?\d+", d)
    p = canvas.beginPath()
    i = 0
    cmd = None
    cur = (0, 0)
    start = (0, 0)

    def pt(x, y):
        return x * scale, h - y * scale

    while i < len(toks):
        t = toks[i]
        if t in "MLCZAaz":
            cmd = t
            i += 1
            if cmd in "Zz":
                p.close()
                cur = start
            continue
        if cmd == "M":
            x, y = float(toks[i]), float(toks[i + 1]); i += 2
            p.moveTo(*pt(x, y)); cur = (x, y); start = (x, y)
        elif cmd == "L":
            x, y = float(toks[i]), float(toks[i + 1]); i += 2
            p.lineTo(*pt(x, y)); cur = (x, y)
        elif cmd == "C":
            x1, y1, x2, y2, x, y = (float(toks[i + k]) for k in range(6)); i += 6
            p.curveTo(*pt(x1, y1), *pt(x2, y2), *pt(x, y)); cur = (x, y)
        elif cmd in "Aa":
            # dot()이 쓰는 원호만 처리: 반원 두 개 → 원
            rx, ry = float(toks[i]), float(toks[i + 1])
            dx, dy = float(toks[i + 5]), float(toks[i + 6]); i += 7
            nx, ny = (cur[0] + dx, cur[1] + dy) if cmd == "a" else (dx, dy)
            mx, my = (cur[0] + nx) / 2, (cur[1] + ny) / 2
            p.curveTo(*pt(cur[0], cur[1] - ry * 1.33), *pt(nx, ny - ry * 1.33),
                      *pt(nx, ny)) if abs(dy) < 0.01 else p.lineTo(*pt(nx, ny))
            cur = (nx, ny)
        else:
            i += 1
    return p


def to_pdf(pages, path, trim_in=8.5, bleed_in=0.0):
    """페이지 목록을 인쇄용 PDF로. pages = [(strokes, texts), ...]"""
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib.colors import HexColor

    pt_per_in = 72.0
    w = (trim_in + bleed_in) * pt_per_in
    h = (trim_in + bleed_in * 2) * pt_per_in
    scale = trim_in * pt_per_in / 100.0
    c = rl_canvas.Canvas(path, pagesize=(w, h))

    for strokes, texts in pages:
        c.setFillColor(HexColor(PAPER))
        c.rect(0, 0, w, h, stroke=0, fill=1)
        for s in strokes:
            p = _svg_path_to_pdf(c, s.d, scale, h)
            c.saveState()
            if s.opacity < 1:
                c.setFillAlpha(s.opacity); c.setStrokeAlpha(s.opacity)
            if s.fill != "none":
                c.setFillColor(HexColor(s.fill))
            if s.width:
                c.setStrokeColor(HexColor(s.color))
                c.setLineWidth(s.width * scale)
                c.setLineCap(1); c.setLineJoin(1)
                if s.dash:
                    c.setDash([float(v) * scale for v in s.dash.split()])
            c.drawPath(p, stroke=1 if s.width else 0,
                       fill=1 if s.fill != "none" else 0)
            c.restoreState()
        c.showPage()
    c.save()
    return path

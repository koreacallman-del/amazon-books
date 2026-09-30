"""사물 카탈로그 — 「시계가 멈춘 마을」

각 함수는 (cx, cy) 중심에 사물 하나를 그려 Stroke 목록을 돌려준다.
s는 크기 배율. seed는 떨림 고정용. gold=True면 그 사물의 핵심부가 금빛이 된다.

원칙: 한 사물은 3~12획. 장면을 그리지 않는다. 배경을 그리지 않는다.
새·고양이는 눈 없는 붓 실루엣으로만 (저자 결정).
"""

import math
from ink import (Stroke, line, curve, arc, ring, dot, crack, hatch, weave,
                 silhouette, thread, INK, INK_SOFT, GOLD, HAIR, FINE, THIN,
                 MED, BOLD)


def _c(color, gold):
    return GOLD if gold else color


# ── 1부. 멈춘 것들 ──────────────────────────────────────────────────────

def clock_hands(cx, cy, s=1.0, seed=1, gold=False):
    """문자판 없이 6시에 멈춘 바늘 두 개."""
    k = _c(INK, gold)
    return [line(cx, cy, cx, cy - 23 * s, 0.9, k, seed, 0.09),
            line(cx, cy, cx, cy + 13.5 * s, 1.9, k, seed + 1, 0.09),
            crack(cx - 2.4, cy - 10.8 * s, 4 * s, 108, seed + 2),
            dot(cx, cy, 1.15 * s, k)]


def dial(cx, cy, s=1.0, seed=2, gold=False):
    """숫자 없이 눈금 점만. 테두리 한 곳이 끊긴다."""
    k = _c(INK, gold)
    r = 20 * s
    out = [ring(cx, cy, r, MED, k, gap=(352, 8), seed=seed, amp=0.09),
           line(cx, cy, cx, cy - 15.5 * s, 0.75, k, seed + 1, 0.07),
           line(cx, cy, cx, cy + 9 * s, 1.6, k, seed + 2, 0.07),
           dot(cx, cy, 1.0 * s, k)]
    for i in range(12):
        if i == 0:
            continue
        a = math.radians(i * 30 - 90)
        rr = 0.5 if i % 3 == 0 else 0.38
        out.append(dot(cx + r * 0.87 * math.cos(a),
                       cy + r * 0.87 * math.sin(a), rr * s, k))
    return out


def planner(cx, cy, s=1.0, seed=3, gold=False):
    """일정표 — 빈틈없이 채워진 칸들."""
    k = _c(INK, gold)
    w, h = 16 * s, 20 * s
    out = [curve([(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2),
                  (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)],
                 THIN, k, seed, 0.10, closed=True)]
    for i in range(1, 7):
        y = cy - h / 2 + h * i / 7
        out.append(line(cx - w / 2, y, cx + w / 2, y, HAIR, k, seed + i,
                        0.06, 3, 0.55))
    for i in range(6):
        y = cy - h / 2 + h * (i + 0.5) / 7
        out.append(line(cx - w * 0.36, y, cx + w * 0.30, y, HAIR, k,
                        seed + 20 + i, 0.09, 4, 0.8))
    return out


def phone(cx, cy, s=1.0, seed=4, gold=False, lit=False, face_down=False):
    """전화기. lit이면 화면에 금빛 점."""
    k = INK
    w, h = 7.5 * s, 14 * s
    out = [curve([(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2),
                  (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)],
                 THIN, k, seed, 0.09, closed=True)]
    if face_down:
        out += hatch(cx - w * 0.3, cy - h * 0.3, w * 0.6, h * 0.5, 4, 62,
                     HAIR, k, seed + 5, 0.45)
    else:
        out.append(line(cx - w * 0.28, cy - h * 0.34, cx + w * 0.28,
                        cy - h * 0.34, HAIR, k, seed + 3, 0.06, 3, 0.5))
    if lit:
        out.append(dot(cx, cy, 0.9 * s, GOLD))
    return out


def door_handle(cx, cy, s=1.0, seed=5, gold=False):
    """문손잡이 + 문틀 수직선."""
    k = _c(INK, gold)
    return [line(cx + 6 * s, cy - 16 * s, cx + 6 * s, cy + 16 * s, THIN, k,
                 seed, 0.10),
            curve([(cx + 6 * s, cy - 1.2 * s), (cx - 1 * s, cy - 1.6 * s),
                   (cx - 5 * s, cy + 0.4 * s)], MED, k, seed + 1, 0.10),
            curve([(cx - 5 * s, cy + 0.4 * s), (cx - 6.2 * s, cy + 2.4 * s)],
                  MED, k, seed + 2, 0.08),
            dot(cx + 6 * s, cy - 1.2 * s, 0.7 * s, k)]


def empty_bowl(cx, cy, s=1.0, seed=6, gold=False):
    """빈 그릇 — 안쪽은 종이 그대로."""
    k = _c(INK, gold)
    r = 9 * s
    return [curve([(cx - r, cy - r * 0.32), (cx - r * 0.82, cy + r * 0.55),
                   (cx, cy + r * 0.82), (cx + r * 0.82, cy + r * 0.55),
                   (cx + r, cy - r * 0.32)], THIN, k, seed, 0.10),
            curve([(cx - r * 1.05, cy - r * 0.34), (cx, cy - r * 0.46),
                   (cx + r * 1.05, cy - r * 0.34)], FINE, k, seed + 1, 0.08),
            line(cx - r * 0.42, cy + r * 0.86, cx + r * 0.42, cy + r * 0.86,
                 HAIR, k, seed + 2, 0.05, 3, 0.5)]


def briefcase(cx, cy, s=1.0, seed=7, gold=False, empty=False):
    """서류가방. empty면 옆으로 눕고 입이 벌어진다."""
    k = _c(INK, gold)
    w, h = 18 * s, 11 * s
    out = [curve([(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2),
                  (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)],
                 THIN, k, seed, 0.10, closed=True),
           curve([(cx - 3.2 * s, cy - h / 2), (cx - 2.6 * s, cy - h / 2 - 3.4 * s),
                  (cx, cy - h / 2 - 4.1 * s), (cx + 2.6 * s, cy - h / 2 - 3.4 * s),
                  (cx + 3.2 * s, cy - h / 2)], FINE, k, seed + 1, 0.09)]
    if empty:
        out.append(curve([(cx - w * 0.34, cy - h / 2),
                          (cx, cy - h * 0.18),
                          (cx + w * 0.34, cy - h / 2)], HAIR, k, seed + 2,
                         0.08, opacity=0.6))
    else:
        out.append(line(cx - w * 0.30, cy - h * 0.02, cx + w * 0.30,
                        cy - h * 0.02, HAIR, k, seed + 2, 0.06, 3, 0.55))
    return out


def worn_heel(cx, cy, s=1.0, seed=8, gold=False):
    """닳은 구두 굽 — 한쪽만 기울어 마모됨."""
    k = _c(INK, gold)
    return [curve([(cx - 7 * s, cy - 2 * s), (cx + 6 * s, cy - 2.6 * s),
                   (cx + 7 * s, cy + 1.2 * s), (cx - 5.6 * s, cy + 2.4 * s)],
                  THIN, k, seed, 0.10, closed=True),
            line(cx + 2.6 * s, cy + 2.1 * s, cx + 6.6 * s, cy + 3.6 * s,
                 FINE, k, seed + 1, 0.10),
            line(cx - 5.6 * s, cy + 2.4 * s, cx + 2.6 * s, cy + 2.1 * s,
                 HAIR, k, seed + 2, 0.06, 3, 0.55)]


def coat_hem(cx, cy, s=1.0, seed=9, gold=False):
    """외투 자락 — 바람에 한쪽만 들림."""
    k = _c(INK, gold)
    return [curve([(cx - 8 * s, cy - 12 * s), (cx - 7 * s, cy + 2 * s),
                   (cx - 4 * s, cy + 9 * s), (cx + 3 * s, cy + 7 * s),
                   (cx + 8 * s, cy + 1 * s)], THIN, k, seed, 0.12),
            curve([(cx - 3.4 * s, cy - 11 * s), (cx - 2 * s, cy - 1 * s),
                   (cx + 0.6 * s, cy + 5.4 * s)], FINE, k, seed + 1, 0.10,
                  opacity=0.7),
            curve([(cx + 3 * s, cy + 7 * s), (cx + 6.4 * s, cy + 8.6 * s)],
                  HAIR, k, seed + 2, 0.08, opacity=0.6)]


def leaf(cx, cy, s=1.0, seed=10, gold=False, shadow=False):
    """나뭇잎 하나. shadow면 아래에 나란한 그림자 선."""
    k = _c(INK, gold)
    out = [curve([(cx - 5.4 * s, cy), (cx - 1.6 * s, cy - 3.4 * s),
                  (cx + 4.4 * s, cy - 1.2 * s), (cx + 1.2 * s, cy + 3 * s),
                  (cx - 4 * s, cy + 1.8 * s)], FINE, k, seed, 0.09,
                 closed=True),
           curve([(cx - 4.6 * s, cy + 0.6 * s), (cx + 2.6 * s, cy - 0.6 * s)],
                 HAIR, k, seed + 1, 0.06, opacity=0.65)]
    if shadow:
        out.append(curve([(cx - 4.4 * s, cy + 5.6 * s),
                          (cx + 3.2 * s, cy + 4.6 * s)],
                         HAIR, INK_SOFT, seed + 2, 0.07, opacity=0.5))
    return out


def wall_corner(cx, cy, s=1.0, seed=11, gold=False):
    """벽 모퉁이 — 직각으로 꺾이는 선."""
    k = _c(INK, gold)
    return [line(cx, cy - 18 * s, cx, cy + 2 * s, THIN, k, seed, 0.09),
            line(cx, cy + 2 * s, cx + 20 * s, cy + 2.6 * s, THIN, k,
                 seed + 1, 0.09),
            crack(cx - 0.4, cy - 9 * s, 5 * s, 96, seed + 2, opacity=0.6)]


def grass(cx, cy, s=1.0, seed=12, gold=False, n=3):
    """풀 — 갈라진 틈에서 올라온 몇 줄기."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        off = (i - (n - 1) / 2) * 1.5 * s
        lean = off * 0.5
        out.append(curve([(cx + off, cy), (cx + off + lean * 0.5, cy - 3.4 * s),
                          (cx + off + lean, cy - 6.2 * s)],
                         FINE, k, seed + i, 0.09))
    return out


def footprints(cx, cy, s=1.0, seed=13, gold=False, n=5):
    """발자국 — 점점이 이어지다 끊긴다."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        x = cx - 14 * s + 28 * s * t
        y = cy + (1.6 if i % 2 else -1.6) * s
        out.append(dot(x, y, (0.62 - 0.07 * i) * s, k, max(0.25, 1 - 0.17 * i)))
    return out


def broken_stone(cx, cy, s=1.0, seed=14, gold=False):
    """깨진 돌."""
    k = _c(INK, gold)
    return [curve([(cx - 7 * s, cy + 2.6 * s), (cx - 5 * s, cy - 2.6 * s),
                   (cx + 1 * s, cy - 3.4 * s), (cx + 6.4 * s, cy - 0.6 * s),
                   (cx + 5 * s, cy + 3 * s)], THIN, k, seed, 0.11,
                  closed=True),
            crack(cx - 1.4 * s, cy - 3.2 * s, 6 * s, 172, seed + 1, FINE),
            line(cx - 7 * s, cy + 2.6 * s, cx + 5 * s, cy + 3 * s, HAIR, k,
                 seed + 2, 0.06, 3, 0.5)]


def signpost(cx, cy, s=1.0, seed=15, gold=False, back=False):
    """이정표. back이면 뒷면(글씨 없음)."""
    k = _c(INK, gold)
    out = [line(cx, cy + 14 * s, cx, cy - 6 * s, THIN, k, seed, 0.09),
           curve([(cx - 10 * s, cy - 6.6 * s), (cx + 10 * s, cy - 7.4 * s),
                  (cx + 10 * s, cy - 12 * s), (cx - 10 * s, cy - 11.2 * s)],
                 THIN, k, seed + 1, 0.10, closed=True)]
    if not back:
        for i in range(2):
            y = cy - 10.6 * s + i * 2.3 * s
            out.append(line(cx - 7 * s, y, cx + (2.4 - i * 5) * s, y, HAIR, k,
                            seed + 10 + i, 0.09, 4, 0.55 - i * 0.2))
    return out


def compass(cx, cy, s=1.0, seed=16, gold=False):
    """나침반 — 바늘이 돌고 있다."""
    k = _c(INK, gold)
    r = 8 * s
    return [ring(cx, cy, r, THIN, k, seed=seed, amp=0.09),
            line(cx - r * 0.6, cy + r * 0.5, cx + r * 0.62, cy - r * 0.46,
                 FINE, k, seed + 1, 0.08),
            dot(cx, cy, 0.6 * s, k),
            arc(cx, cy, r * 0.74, 200, 320, HAIR, k, seed + 2, 0.06,
                opacity=0.5)]


def screwdriver(cx, cy, s=1.0, seed=17, gold=False, down=False):
    """드라이버. down이면 눕혀져 있다."""
    k = _c(INK, gold)
    if down:
        return [curve([(cx - 9 * s, cy), (cx - 2 * s, cy - 0.5 * s)], MED, k,
                      seed, 0.09),
                line(cx - 2 * s, cy - 0.5 * s, cx + 8 * s, cy - 0.9 * s, THIN,
                     k, seed + 1, 0.08),
                line(cx + 8 * s, cy - 0.9 * s, cx + 9.6 * s, cy - 0.9 * s,
                     MED, k, seed + 2, 0.05, 2)]
    return [curve([(cx, cy + 9 * s), (cx + 0.4 * s, cy + 2 * s)], MED, k, seed,
                  0.09),
            line(cx + 0.4 * s, cy + 2 * s, cx, cy - 8 * s, THIN, k, seed + 1,
                 0.08),
            line(cx - 0.9 * s, cy - 8 * s, cx + 0.9 * s, cy - 8 * s, MED, k,
                 seed + 2, 0.05, 2)]


def mainspring(cx, cy, s=1.0, seed=18, gold=False, loose=False):
    """태엽 — 감긴 나선. loose면 풀려 있다."""
    k = _c(INK, gold)
    pts = []
    turns = 2.2 if loose else 3.4
    steps = 60
    for i in range(steps + 1):
        t = i / steps
        a = t * turns * 2 * math.pi
        r = (1.4 + t * (8.4 if loose else 5.6)) * s
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a) * 0.96))
    return [curve(pts, FINE if loose else THIN, k, seed, 0.06)]


def gear(cx, cy, s=1.0, seed=19, gold=False, teeth=9):
    """톱니바퀴 하나."""
    k = _c(INK, gold)
    r = 7 * s
    out = [ring(cx, cy, r, THIN, k, seed=seed, amp=0.07),
           ring(cx, cy, r * 0.32, FINE, k, seed=seed + 1, amp=0.06)]
    for i in range(teeth):
        a = math.radians(i * 360 / teeth)
        out.append(line(cx + r * math.cos(a), cy + r * math.sin(a),
                        cx + r * 1.26 * math.cos(a), cy + r * 1.26 * math.sin(a),
                        FINE, k, seed + 5 + i, 0.05, 2))
    return out


def pocket_watch(cx, cy, s=1.0, seed=20, gold=False, n=1):
    """회중시계. n개를 나란히."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        x = cx + (i - (n - 1) / 2) * 13 * s
        r = 5.4 * s
        out += [ring(x, cy, r, THIN, k, seed=seed + i, amp=0.08),
                line(x, cy, x, cy - r * 0.68, HAIR, k, seed + 10 + i, 0.06, 3),
                line(x, cy, x + r * 0.42, cy + r * 0.3, HAIR, k,
                     seed + 20 + i, 0.06, 3),
                curve([(x - 1 * s, cy - r), (x, cy - r - 1.8 * s),
                       (x + 1 * s, cy - r)], FINE, k, seed + 30 + i, 0.07)]
    return out


def wind_key(cx, cy, s=1.0, seed=21, gold=False):
    """태엽 열쇠."""
    k = _c(INK, gold)
    return [ring(cx, cy - 4.4 * s, 3.2 * s, THIN, k, seed=seed, amp=0.08),
            line(cx, cy - 1.2 * s, cx, cy + 6.4 * s, THIN, k, seed + 1, 0.08),
            line(cx, cy + 6.4 * s, cx + 2.6 * s, cy + 6.4 * s, FINE, k,
                 seed + 2, 0.06, 2),
            line(cx, cy + 4 * s, cx + 1.8 * s, cy + 4 * s, FINE, k, seed + 3,
                 0.06, 2)]


def empty_chair(cx, cy, s=1.0, seed=22, gold=False, n=1):
    """빈 의자. n=2면 두 개 나란히."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        x = cx + (i - (n - 1) / 2) * 15 * s
        out += [line(x - 5 * s, cy, x + 5 * s, cy - 0.3 * s, THIN, k,
                     seed + i, 0.09),
                line(x + 5 * s, cy - 0.3 * s, x + 5.4 * s, cy - 11 * s, THIN,
                     k, seed + 10 + i, 0.09),
                line(x - 4.4 * s, cy, x - 4.6 * s, cy + 8 * s, FINE, k,
                     seed + 20 + i, 0.08),
                line(x + 4.6 * s, cy - 0.2 * s, x + 4.8 * s, cy + 8 * s, FINE,
                     k, seed + 30 + i, 0.08),
                line(x + 1.4 * s, cy - 9.4 * s, x + 5.2 * s, cy - 9.6 * s,
                     HAIR, k, seed + 40 + i, 0.07, 3, 0.6)]
    return out


def cloth_scrap(cx, cy, s=1.0, seed=23, gold=False):
    """천 조각 — 한쪽이 찢겨 있다."""
    k = _c(INK, gold)
    r = _c(INK, gold)
    pts = [(cx - 7 * s, cy - 4 * s), (cx + 6 * s, cy - 5 * s),
           (cx + 7 * s, cy + 3 * s), (cx + 1 * s, cy + 2 * s),
           (cx - 2 * s, cy + 5 * s), (cx - 6.4 * s, cy + 2.6 * s)]
    out = [curve(pts, FINE, r, seed, 0.14, closed=True)]
    for i in range(3):
        y = cy - 2.4 * s + i * 2.4 * s
        out.append(line(cx - 5.4 * s, y, cx + 4.6 * s, y - 0.4 * s, HAIR, k,
                        seed + 5 + i, 0.08, 3, 0.45))
    return out


# ── 2부. 보내고 기다리는 것들 ───────────────────────────────────────────

def bell(cx, cy, s=1.0, seed=24, gold=False, silent=True):
    """종. silent면 소리선이 없다."""
    k = _c(INK, gold)
    out = [curve([(cx - 6 * s, cy + 5 * s), (cx - 5 * s, cy - 2 * s),
                   (cx, cy - 7 * s), (cx + 5 * s, cy - 2 * s),
                   (cx + 6 * s, cy + 5 * s)], THIN, k, seed, 0.10),
           line(cx - 6.6 * s, cy + 5 * s, cx + 6.6 * s, cy + 5 * s, FINE, k,
                seed + 1, 0.07),
           curve([(cx - 0.8 * s, cy - 7 * s), (cx, cy - 9.4 * s),
                  (cx + 0.8 * s, cy - 7 * s)], FINE, k, seed + 2, 0.07),
           dot(cx, cy + 6.6 * s, 0.9 * s, k)]
    if not silent:
        out += [arc(cx, cy, 11 * s, 40, 78, HAIR, k, seed + 3, 0.05,
                    opacity=0.5),
                arc(cx, cy, 11 * s, 282, 320, HAIR, k, seed + 4, 0.05,
                    opacity=0.5)]
    return out


def nest(cx, cy, s=1.0, seed=25, gold=False, wall=True):
    """빈 둥지. 안쪽은 종이 그대로 비운다."""
    out = weave(cx, cy, 20 * s, 11 * s, 9, seed, FINE, _c(INK, gold))
    if wall:
        w = line(0, cy + 3 * s, cx - 23 * s, cy + 3 * s, 0.45,
                 INK_SOFT, seed + 60, 0.06, 3)
        w.bleed = True   # 담벼락은 화면 밖에서 이어져 들어온다
        out.insert(0, w)
    return out


def bird_sil(cx, cy, s=1.0, seed=26, gold=False, flying=True):
    """새 — 눈 없는 붓 실루엣 (저자 결정)."""
    k = _c(INK, gold)
    if flying:
        pts = [(cx - 7 * s, cy + 1 * s), (cx - 2 * s, cy - 2.6 * s),
               (cx + 3 * s, cy - 1.4 * s), (cx + 7.4 * s, cy + 1.6 * s),
               (cx + 2 * s, cy + 1.4 * s), (cx - 1.6 * s, cy + 3 * s),
               (cx - 4.6 * s, cy + 2.4 * s)]
    else:
        pts = [(cx - 6 * s, cy + 2.4 * s), (cx - 4.4 * s, cy - 2 * s),
               (cx - 0.6 * s, cy - 4 * s), (cx + 3.6 * s, cy - 2.2 * s),
               (cx + 6.6 * s, cy + 1.4 * s), (cx + 1.6 * s, cy + 3.4 * s),
               (cx - 3 * s, cy + 3.4 * s)]
    return [silhouette(pts, k, 0.9, seed, 0.09)]


def eggshell(cx, cy, s=1.0, seed=27, gold=False):
    """알껍질 — 반쪽만 남았다."""
    k = _c(INK, gold)
    return [curve([(cx - 5 * s, cy), (cx - 4.2 * s, cy + 3.4 * s),
                   (cx, cy + 4.8 * s), (cx + 4.2 * s, cy + 3.4 * s),
                   (cx + 5 * s, cy)], THIN, k, seed, 0.10),
            curve([(cx - 5 * s, cy), (cx - 2.6 * s, cy - 1.2 * s),
                   (cx - 0.6 * s, cy + 0.4 * s), (cx + 2 * s, cy - 1.4 * s),
                   (cx + 5 * s, cy)], FINE, k, seed + 1, 0.13)]


def sneaker(cx, cy, s=1.0, seed=28, gold=False):
    """운동화 한 짝 — 떠난 아이의 것."""
    k = _c(INK, gold)
    return [curve([(cx - 8 * s, cy + 2.6 * s), (cx - 7.4 * s, cy - 1.4 * s),
                   (cx - 2 * s, cy - 3 * s), (cx + 2.6 * s, cy - 1 * s),
                   (cx + 8 * s, cy + 0.6 * s), (cx + 7.6 * s, cy + 3 * s)],
                  THIN, k, seed, 0.10),
            line(cx - 8 * s, cy + 3 * s, cx + 7.6 * s, cy + 3.2 * s, FINE, k,
                 seed + 1, 0.07),
            curve([(cx - 5.4 * s, cy - 1.6 * s), (cx - 2.6 * s, cy + 0.4 * s)],
                  HAIR, k, seed + 2, 0.07, opacity=0.6),
            curve([(cx - 3.6 * s, cy - 2.4 * s), (cx - 1 * s, cy - 0.4 * s)],
                  HAIR, k, seed + 3, 0.07, opacity=0.6)]


def feather(cx, cy, s=1.0, seed=29, gold=False):
    """깃털 하나 — 남겨진 흔적."""
    k = _c(INK, gold)
    out = [curve([(cx, cy - 7 * s), (cx + 0.6 * s, cy), (cx - 0.4 * s,
                  cy + 7 * s)], FINE, k, seed, 0.08)]
    for i in range(7):
        t = i / 6
        y = cy - 6 * s + 11 * s * t
        w = 3.4 * s * (1 - abs(t - 0.35) * 0.9)
        out.append(line(cx + 0.3 * s, y, cx - w, y + 1.2 * s, HAIR, k,
                        seed + 5 + i, 0.06, 2, 0.75))
        out.append(line(cx + 0.3 * s, y, cx + w, y + 1.2 * s, HAIR, k,
                        seed + 15 + i, 0.06, 2, 0.75))
    return out


def waterdrop(cx, cy, s=1.0, seed=30, gold=False, n=1):
    """물방울. 경계를 넘는 물줄기에 쓴다."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        y = cy + i * 4.6 * s
        r = (1.5 - i * 0.16) * s
        out.append(curve([(cx, y - r * 1.9), (cx + r, y), (cx, y + r * 1.1),
                          (cx - r, y)], FINE, k, seed + i, 0.06, closed=True))
    return out


def name_tag(cx, cy, s=1.0, seed=31, gold=False):
    """이름 막대 — 화면 속 이름, 꽃밭의 이름표."""
    k = _c(INK, gold)
    return [curve([(cx - 9 * s, cy - 2.2 * s), (cx + 9 * s, cy - 2.4 * s),
                   (cx + 9 * s, cy + 2.2 * s), (cx - 9 * s, cy + 2.4 * s)],
                  FINE, k, seed, 0.09, closed=True),
            line(cx - 6 * s, cy, cx + 4.4 * s, cy - 0.2 * s, THIN, k,
                 seed + 1, 0.09, 4, 0.85)]


def dry_and_bloom(cx, cy, s=1.0, seed=32, gold=False):
    """핀 꽃 한 송이 + 마른 줄기 한 대. 반쪽 꽃밭."""
    k = INK
    out = [curve([(cx - 6 * s, cy + 9 * s), (cx - 5.4 * s, cy + 1 * s),
                  (cx - 6 * s, cy - 4 * s)], FINE, k, seed, 0.10)]
    for i in range(5):
        a = math.radians(i * 72 - 90)
        out.append(curve([(cx - 6 * s, cy - 4 * s),
                          (cx - 6 * s + 2.4 * s * math.cos(a),
                           cy - 4 * s + 2.4 * s * math.sin(a))],
                         HAIR, _c(k, gold), seed + 5 + i, 0.07))
    out += [line(cx + 6 * s, cy + 9 * s, cx + 5.6 * s, cy + 2.4 * s, FINE, k,
                 seed + 20, 0.09),
            line(cx + 5.6 * s, cy + 2.4 * s, cx + 7 * s, cy - 2 * s, FINE, k,
                 seed + 21, 0.09),
            line(cx + 6.4 * s, cy + 5 * s, cx + 9 * s, cy + 3 * s, HAIR, k,
                 seed + 22, 0.08, 2, 0.7)]
    return out


def watering_can(cx, cy, s=1.0, seed=33, gold=False, tilted=True):
    """물뿌리개. tilted면 기울어 물이 떨어진다."""
    k = _c(INK, gold)
    t = -14 if tilted else 0
    a = math.radians(t)
    def R(px, py):
        return (cx + (px * math.cos(a) - py * math.sin(a)),
                cy + (px * math.sin(a) + py * math.cos(a)))
    body = [R(-6 * s, -5 * s), R(6 * s, -5.4 * s), R(5.4 * s, 5 * s),
            R(-5.4 * s, 5 * s)]
    out = [curve(body, THIN, k, seed, 0.10, closed=True),
           curve([R(-6 * s, -4 * s), R(-11 * s, -7.4 * s),
                  R(-13 * s, -9.6 * s)], THIN, k, seed + 1, 0.09),
           curve([R(-12.4 * s, -10.4 * s), R(-14.6 * s, -9 * s)], FINE, k,
                 seed + 2, 0.07),
           curve([R(1 * s, -5.2 * s), R(3.6 * s, -9.4 * s),
                  R(7 * s, -8.2 * s)], FINE, k, seed + 3, 0.08)]
    if tilted:
        out += waterdrop(R(-14 * s, -8 * s)[0], R(-14 * s, -8 * s)[1] + 4 * s,
                         s, seed + 10, gold, 3)
    return out


def calendar(cx, cy, s=1.0, seed=34, gold=False):
    """달력 — 한 칸만 비어 있다."""
    k = _c(INK, gold)
    w, h = 18 * s, 15 * s
    out = [curve([(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2),
                  (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)],
                 THIN, k, seed, 0.09, closed=True)]
    for i in range(1, 4):
        y = cy - h / 2 + h * i / 4
        out.append(line(cx - w / 2, y, cx + w / 2, y, HAIR, k, seed + i, 0.05,
                        3, 0.4))
    for i in range(1, 5):
        x = cx - w / 2 + w * i / 5
        out.append(line(x, cy - h / 2, x, cy + h / 2, HAIR, k, seed + 10 + i,
                        0.05, 3, 0.4))
    for r in range(4):
        for c in range(5):
            if r == 2 and c == 3:
                continue
            x = cx - w / 2 + w * (c + 0.5) / 5
            y = cy - h / 2 + h * (r + 0.55) / 4
            out.append(dot(x, y, 0.3 * s, k, 0.55))
    return out


def note(cx, cy, s=1.0, seed=35, gold=False):
    """쪽지 — 접힌 자리가 남은 종이."""
    k = _c(INK, gold)
    return [curve([(cx - 7 * s, cy - 5 * s), (cx + 7 * s, cy - 5.4 * s),
                   (cx + 6.4 * s, cy + 5 * s), (cx - 6.6 * s, cy + 5.2 * s)],
                  FINE, k, seed, 0.10, closed=True),
            line(cx - 7 * s, cy, cx + 6.8 * s, cy - 0.3 * s, HAIR, k, seed + 1,
                 0.08, 4, 0.5),
            line(cx - 4.6 * s, cy - 2.4 * s, cx + 3.4 * s, cy - 2.6 * s, HAIR,
                 k, seed + 2, 0.07, 3, 0.7),
            line(cx - 4.6 * s, cy + 2.4 * s, cx + 1 * s, cy + 2.2 * s, HAIR,
                 k, seed + 3, 0.07, 3, 0.7)]


def cut_thread(cx, cy, s=1.0, seed=36, gold=False, gap=6.0):
    """끊어진 실. gap이 좁아지면 이어지는 중."""
    k = _c(INK, gold)
    g = gap * s
    return [curve([(cx - 14 * s, cy - 1.4 * s), (cx - 8 * s, cy + 0.6 * s),
                   (cx - g / 2, cy)], FINE, k, seed, 0.12),
            curve([(cx + g / 2, cy), (cx + 8 * s, cy - 0.8 * s),
                   (cx + 14 * s, cy + 1 * s)], FINE, k, seed + 1, 0.12)]


def bud(cx, cy, s=1.0, seed=37, gold=False):
    """봉오리 — 아직 열리지 않았다."""
    k = _c(INK, gold)
    return [line(cx, cy + 8 * s, cx + 0.4 * s, cy + 1 * s, FINE, INK, seed,
                 0.09),
            curve([(cx + 0.4 * s, cy + 1 * s), (cx - 2 * s, cy - 2.4 * s),
                   (cx, cy - 5.6 * s), (cx + 2.2 * s, cy - 2.2 * s),
                   (cx + 0.4 * s, cy + 1 * s)], FINE, k, seed + 1, 0.08),
            curve([(cx + 0.4 * s, cy + 3.4 * s), (cx + 3.6 * s, cy + 2 * s)],
                  HAIR, INK, seed + 2, 0.08, opacity=0.7)]


def roots(cx, cy, s=1.0, seed=38, gold=False):
    """뿌리 — 보이지 않던 것."""
    k = _c(INK, gold)
    out = [line(cx, cy - 8 * s, cx, cy, THIN, INK, seed, 0.09)]
    for i, (dx, dy, w) in enumerate([(-7, 7, FINE), (-3, 9, FINE),
                                     (2, 9.4, FINE), (6.6, 7.4, FINE),
                                     (-9.6, 4, HAIR), (9.4, 4.4, HAIR)]):
        out.append(curve([(cx, cy), (cx + dx * 0.5 * s, cy + dy * 0.45 * s),
                          (cx + dx * s, cy + dy * s)], w, k, seed + 5 + i,
                         0.10))
    return out


def sprout(cx, cy, s=1.0, seed=39, gold=True):
    """싹 — 마른 줄기에서 솟는다. 책 전체의 전환점(p.67)."""
    return [line(cx, cy + 27 * s, cx + 0.4 * s, cy + 13 * s, 0.85, INK, seed,
                 0.09),
            line(cx + 0.4 * s, cy + 13 * s, cx - 1.4 * s, cy + 5.5 * s, 0.8,
                 INK, seed + 1, 0.09),
            line(cx - 1.4 * s, cy + 5.5 * s, cx - 0.1 * s, cy, 0.7, INK,
                 seed + 2, 0.08),
            line(cx + 0.3 * s, cy + 10 * s, cx + 4.5 * s, cy + 6.2 * s, 0.4,
                 INK, seed + 3, 0.08, 3, 0.8),
            curve([(cx - 0.1 * s, cy), (cx + 0.2 * s, cy - 6 * s),
                   (cx - 0.4 * s, cy - 14.5 * s)], 0.7,
                  GOLD if gold else INK, seed + 4, 0.07),
            curve([(cx - 0.3 * s, cy - 9.5 * s), (cx - 3.5 * s, cy - 10.6 * s),
                   (cx - 6.2 * s, cy - 12.8 * s), (cx - 7.1 * s, cy - 15.6 * s),
                   (cx - 3.8 * s, cy - 16 * s), (cx - 1.2 * s, cy - 14.2 * s),
                   (cx - 0.3 * s, cy - 11.4 * s)], 0.55,
                 GOLD if gold else INK, seed + 5, 0.07),
            curve([(cx - 0.2 * s, cy - 6.5 * s), (cx + 3 * s, cy - 7.2 * s),
                   (cx + 5.9 * s, cy - 9 * s), (cx + 7.1 * s, cy - 11.7 * s),
                   (cx + 3.8 * s, cy - 12.3 * s), (cx + 1 * s, cy - 10.8 * s),
                   (cx - 0.2 * s, cy - 8.1 * s)], 0.55,
                  GOLD if gold else INK, seed + 6, 0.07)]


# ── 3부. 금이 가고 꺼진 것들 ────────────────────────────────────────────

def jar(cx, cy, s=1.0, seed=40, gold=False, stitched=False):
    """항아리. stitched면 금 간 자리가 금실로 이어진다."""
    k = INK
    out = [curve([(cx - 9 * s, cy - 8 * s), (cx - 11 * s, cy),
                  (cx - 8.4 * s, cy + 8 * s), (cx, cy + 10 * s),
                  (cx + 8.4 * s, cy + 8 * s), (cx + 11 * s, cy),
                  (cx + 9 * s, cy - 8 * s)], THIN, k, seed, 0.11),
           curve([(cx - 9 * s, cy - 8 * s), (cx - 6 * s, cy - 9.6 * s),
                  (cx, cy - 10 * s), (cx + 6 * s, cy - 9.6 * s),
                  (cx + 9 * s, cy - 8 * s)], FINE, k, seed + 1, 0.09)]
    gc = GOLD if (gold or stitched) else INK
    out.append(crack(cx - 2 * s, cy - 9 * s, 14 * s, 172, seed + 2,
                     FINE, gc, 6, 0.9, 0.95))
    out.append(crack(cx + 5 * s, cy - 6 * s, 9 * s, 196, seed + 3,
                     HAIR, gc, 5, 0.7, 0.8))
    if stitched:
        for i in range(3):
            y = cy - 5 * s + i * 4 * s
            out.append(thread(cx - 4.4 * s, y, cx + 1.2 * s, y - 0.6 * s,
                              GOLD, 0.42, seed + 20 + i, 0.12, 4))
    return out


def shard(cx, cy, s=1.0, seed=41, gold=False):
    """깨진 조각 + 금실땀."""
    out = [curve([(cx - 6 * s, cy + 3 * s), (cx - 3 * s, cy - 4 * s),
                  (cx + 4 * s, cy - 2.6 * s), (cx + 6 * s, cy + 3.4 * s)],
                 FINE, INK, seed, 0.11)]
    out.append(thread(cx - 4 * s, cy + 0.6 * s, cx + 4.4 * s, cy + 0.2 * s,
                      GOLD, 0.45, seed + 1, 0.14, 5))
    return out


def knuckles(cx, cy, s=1.0, seed=42, gold=False):
    """손등의 주름 — 손 자체를 그리지 않고 주름만."""
    k = _c(INK, gold)
    out = []
    for i in range(5):
        y = cy - 5 * s + i * 2.6 * s
        w = 9 * s * (1 - abs(i - 2) * 0.13)
        out.append(curve([(cx - w, y), (cx, y - 1.1 * s), (cx + w, y + 0.3 * s)],
                         HAIR if i % 2 else FINE, k, seed + i, 0.10,
                         opacity=0.85 - i * 0.05))
    return out


def wildflower(cx, cy, s=1.0, seed=43, gold=False, n=2):
    """들꽃 — 아무도 심지 않은 것."""
    k = _c(INK, gold)
    out = []
    for j in range(n):
        x = cx + (j - (n - 1) / 2) * 6 * s
        h = (7 + j * 1.6) * s
        out.append(curve([(x, cy + h), (x + 0.6 * s, cy + h * 0.4),
                          (x - 0.4 * s, cy)], HAIR, INK, seed + j, 0.09))
        for i in range(4):
            a = math.radians(i * 90 - 45)
            out.append(curve([(x - 0.4 * s, cy),
                              (x - 0.4 * s + 1.9 * s * math.cos(a),
                               cy + 1.9 * s * math.sin(a))],
                             HAIR, k, seed + 10 + j * 4 + i, 0.06))
    return out


def bulb(cx, cy, s=1.0, seed=44, gold=False, lit=False):
    """전구. lit이면 금빛 빛살이 퍼진다."""
    k = INK
    out = [curve([(cx - 4.4 * s, cy + 1 * s), (cx - 4.6 * s, cy - 3 * s),
                  (cx, cy - 6 * s), (cx + 4.6 * s, cy - 3 * s),
                  (cx + 4.4 * s, cy + 1 * s), (cx + 2.4 * s, cy + 3 * s),
                  (cx - 2.4 * s, cy + 3 * s)], THIN, k, seed, 0.09,
                 closed=True),
           line(cx - 2.6 * s, cy + 3.8 * s, cx + 2.6 * s, cy + 3.8 * s, FINE,
                k, seed + 1, 0.06, 3),
           line(cx - 2.4 * s, cy + 5.2 * s, cx + 2.4 * s, cy + 5.2 * s, FINE,
                k, seed + 2, 0.06, 3),
           line(cx, cy + 5.6 * s, cx, cy + 7.4 * s, FINE, k, seed + 3, 0.06, 3)]
    if lit:
        out.append(curve([(cx - 1.6 * s, cy + 2.4 * s), (cx - 0.6 * s, cy - 1 * s),
                          (cx + 0.8 * s, cy + 1.4 * s),
                          (cx + 1.6 * s, cy - 2 * s)], FINE, GOLD, seed + 4,
                         0.08))
        for i in range(8):
            a = math.radians(i * 45 - 90)
            out.append(line(cx + 7 * s * math.cos(a), cy - 1.5 * s + 7 * s * math.sin(a),
                            cx + 11 * s * math.cos(a), cy - 1.5 * s + 11 * s * math.sin(a),
                            HAIR, GOLD, seed + 20 + i, 0.06, 2, 0.75))
    else:
        out += hatch(cx - 3 * s, cy - 4.4 * s, 6 * s, 6 * s, 5, 62, HAIR, k,
                     seed + 5, 0.5)
    return out


def broom(cx, cy, s=1.0, seed=45, gold=False):
    """빗자루 — 세워둔 채."""
    k = _c(INK, gold)
    out = [line(cx, cy - 12 * s, cx + 0.6 * s, cy + 4 * s, THIN, k, seed,
                0.09)]
    for i in range(7):
        t = (i - 3) / 3
        out.append(line(cx + 0.6 * s, cy + 4 * s, cx + 0.6 * s + t * 3.4 * s,
                        cy + 10 * s, HAIR, k, seed + 5 + i, 0.09, 3, 0.8))
    return out


def lamp_post(cx, cy, s=1.0, seed=46, gold=False, lit=False):
    """가로등 기둥 — 살짝 기울어져 있다."""
    k = INK
    out = [line(cx, cy + 16 * s, cx + 1.2 * s, cy - 8 * s, THIN, k, seed,
                0.10),
           curve([(cx + 1.2 * s, cy - 8 * s), (cx + 1.6 * s, cy - 11 * s),
                  (cx + 4 * s, cy - 12 * s)], FINE, k, seed + 1, 0.08)]
    out += bulb(cx + 5 * s, cy - 14 * s, s * 0.8, seed + 5, gold, lit)
    return out


def switch(cx, cy, s=1.0, seed=47, gold=False, up=False):
    """스위치. up이면 올려져 있다."""
    k = _c(INK, gold)
    out = [curve([(cx - 3 * s, cy - 4.4 * s), (cx + 3 * s, cy - 4.4 * s),
                  (cx + 3 * s, cy + 4.4 * s), (cx - 3 * s, cy + 4.4 * s)],
                 FINE, INK, seed, 0.08, closed=True)]
    y = cy - 2 * s if up else cy + 2 * s
    out.append(line(cx - 1.4 * s, y, cx + 1.4 * s, y, MED,
                    GOLD if (up and not gold) else k, seed + 1, 0.06, 2))
    if up:
        out += hatch(cx - 1, cy - 8 * s, 2 * s, 2 * s, 2, 90, HAIR, GOLD,
                     seed + 2, 0.6)
    return out


def cat_sil(cx, cy, s=1.0, seed=48, gold=False):
    """고양이 — 눈 없는 붓 실루엣 (저자 결정)."""
    k = _c(INK, gold)
    pts = [(cx - 8 * s, cy + 3 * s), (cx - 7.4 * s, cy - 1 * s),
           (cx - 6 * s, cy - 2.4 * s), (cx - 6.6 * s, cy - 4.6 * s),
           (cx - 4.6 * s, cy - 3 * s), (cx - 2.6 * s, cy - 3.4 * s),
           (cx + 1 * s, cy - 1.6 * s), (cx + 5 * s, cy + 0.6 * s),
           (cx + 7.6 * s, cy - 2 * s), (cx + 8 * s, cy + 1 * s),
           (cx + 5.6 * s, cy + 3.2 * s), (cx - 1 * s, cy + 3.6 * s)]
    return [silhouette(pts, k, 0.9, seed, 0.10)]


# ── 4부. 심고 세는 것들 ─────────────────────────────────────────────────

def soil_patch(cx, cy, s=1.0, seed=49, gold=False):
    """흙 한 뙈기 — 담벼락과 길 사이 좁은 땅."""
    k = _c(INK_SOFT, gold)
    out = [curve([(cx - 16 * s, cy), (cx - 8 * s, cy - 1.2 * s),
                  (cx + 4 * s, cy - 0.6 * s), (cx + 16 * s, cy + 0.4 * s)],
                 FINE, k, seed, 0.14)]
    for i in range(6):
        x = cx - 13 * s + i * 5.2 * s
        out.append(line(x, cy + 1.4 * s, x + 1.6 * s, cy + 3 * s, HAIR, k,
                        seed + 5 + i, 0.10, 2, 0.5))
    return out


def fist(cx, cy, s=1.0, seed=50, gold=False):
    """꼭 쥔 주먹 — 안에 무엇이 있는지 보이지 않는다."""
    k = _c(INK, gold)
    return [curve([(cx - 7 * s, cy + 2 * s), (cx - 7.4 * s, cy - 3 * s),
                   (cx - 3 * s, cy - 6.4 * s), (cx + 3.4 * s, cy - 6 * s),
                   (cx + 7.4 * s, cy - 2.4 * s), (cx + 7 * s, cy + 2.6 * s),
                   (cx + 2 * s, cy + 5 * s), (cx - 4 * s, cy + 4.6 * s)],
                  0.68, k, seed, 0.11, closed=True),
            curve([(cx - 5 * s, cy - 3.4 * s), (cx + 5.4 * s, cy - 3 * s)],
                  HAIR, k, seed + 1, 0.09, opacity=0.7),
            curve([(cx - 4.4 * s, cy + 0.4 * s), (cx + 5 * s, cy + 0.8 * s)],
                  HAIR, k, seed + 2, 0.09, opacity=0.65),
            line(cx - 1.4 * s, cy - 5.6 * s, cx - 1.6 * s, cy - 2.8 * s, HAIR,
                 k, seed + 3, 0.06, 2, 0.5),
            line(cx + 2.4 * s, cy - 5.4 * s, cx + 2.2 * s, cy - 2.6 * s, HAIR,
                 k, seed + 4, 0.06, 2, 0.5)]


def seed_obj(cx, cy, s=1.0, seed=51, gold=True):
    """씨앗 하나 — 극소. 금빛 점."""
    return [dot(cx, cy, 1.25 * s, GOLD if gold else INK)]


def tree_rings(cx, cy, s=1.0, seed=52, gold=False, n=5):
    """나이테 — 중심이 한쪽으로 치우쳐 있다."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        r = (2.4 + i * 2.6) * s
        out.append(ring(cx - i * 0.5 * s, cy, r, HAIR if i else FINE, k,
                        seed=seed + i, amp=0.13))
    return out


def shade(cx, cy, s=1.0, seed=53, gold=False):
    """그늘 — 나무는 그리지 않고 그늘만."""
    return [curve([(cx - 15 * s, cy), (cx - 8 * s, cy + 2.6 * s),
                   (cx + 2 * s, cy + 3.2 * s), (cx + 13 * s, cy + 1 * s)],
                  FINE, INK_SOFT, seed, 0.16, opacity=0.55)] + \
        hatch(cx - 13 * s, cy + 1 * s, 26 * s, 5 * s, 9, 68, HAIR, INK_SOFT,
              seed + 5, 0.32)


def furrow(cx, cy, s=1.0, seed=54, gold=False):
    """고랑 — 누군가 갈아둔 자리."""
    k = _c(INK, gold)
    out = []
    for i in range(4):
        y = cy - 4 * s + i * 3 * s
        out.append(curve([(cx - 16 * s, y), (cx, y + 0.8 * s),
                          (cx + 16 * s, y - 0.4 * s)], HAIR if i % 2 else FINE,
                         k, seed + i, 0.12, opacity=0.8))
    return out


def stone_steps(cx, cy, s=1.0, seed=55, gold=False, n=4):
    """돌계단 — 위쪽이 보이지 않는다."""
    k = _c(INK, gold)
    out = []
    for i in range(n):
        x = cx - 10 * s + i * 5 * s
        y = cy + 8 * s - i * 4 * s
        out += [line(x, y, x + 6.4 * s, y - 0.4 * s, FINE, k, seed + i, 0.08),
                line(x + 6.4 * s, y - 0.4 * s, x + 6.6 * s, y - 3.6 * s, HAIR,
                     k, seed + 10 + i, 0.07, 2, 0.7)]
    return out


def star(cx, cy, s=1.0, seed=56, gold=True, n=1):
    """별. n>1이면 여러 개."""
    out = []
    from ink import _Rng
    rr = _Rng(seed)
    for i in range(n):
        if n == 1:
            x, y, rad = cx, cy, 1.15 * s
        else:
            x = cx + rr.sym(17 * s)
            y = cy + rr.sym(12 * s)
            rad = (0.42 + rr.next() * 0.62) * s
        out.append(dot(x, y, rad, GOLD if gold else INK,
                       0.7 + (0.3 if n == 1 else rr.next() * 0.3)))
    return out


def town_map(cx, cy, s=1.0, seed=57, gold=False):
    """지도 — 걸어온 마을이 선 몇 개로."""
    k = _c(INK_SOFT, gold)
    return [line(cx - 13 * s, cy + 6 * s, cx + 2 * s, cy + 5 * s, HAIR, k,
                 seed, 0.12, 4, 0.7),
            line(cx + 2 * s, cy + 5 * s, cx + 6 * s, cy - 3 * s, HAIR, k,
                 seed + 1, 0.12, 4, 0.7),
            line(cx + 6 * s, cy - 3 * s, cx + 13 * s, cy - 6 * s, HAIR, k,
                 seed + 2, 0.12, 4, 0.7),
            dot(cx - 13 * s, cy + 6 * s, 0.45 * s, k, 0.8),
            dot(cx + 13 * s, cy - 6 * s, 0.45 * s, GOLD if gold else k, 0.9)]


def key(cx, cy, s=1.0, seed=58, gold=False):
    """열쇠 — 오래 쓰지 않은 것."""
    k = _c(INK, gold)
    return [ring(cx - 6 * s, cy, 3 * s, FINE, k, seed=seed, amp=0.08),
            line(cx - 3 * s, cy, cx + 7 * s, cy - 0.3 * s, THIN, k, seed + 1,
                 0.08),
            line(cx + 4.4 * s, cy, cx + 4.4 * s, cy + 2.6 * s, FINE, k,
                 seed + 2, 0.06, 2),
            line(cx + 6.8 * s, cy, cx + 6.8 * s, cy + 1.8 * s, FINE, k,
                 seed + 3, 0.06, 2)]


def phone_signal(cx, cy, s=1.0, seed=59, gold=True):
    """전화기 + 접촉점에서 퍼지는 신호. p.116 — 금빛 최대."""
    out = phone(cx, cy, s, seed, False, lit=False)
    out.append(dot(cx, cy - 1 * s, 0.85 * s, GOLD))
    for i in range(4):
        out.append(arc(cx, cy - 1 * s, (6 + i * 5.5) * s, 38, 142, HAIR, GOLD,
                       seed + 10 + i, 0.07, opacity=0.8 - i * 0.16))
        out.append(arc(cx, cy - 1 * s, (6 + i * 5.5) * s, 218, 322, HAIR, GOLD,
                       seed + 20 + i, 0.07, opacity=0.8 - i * 0.16))
    return out


# ── 5부. 나란히 ─────────────────────────────────────────────────────────

def glasses(cx, cy, s=1.0, seed=60, gold=False):
    """안경 — 벗어놓은 채."""
    k = _c(INK, gold)
    return [ring(cx - 6 * s, cy, 4 * s, FINE, k, seed=seed, amp=0.08),
            ring(cx + 6 * s, cy, 4 * s, FINE, k, seed=seed + 1, amp=0.08),
            curve([(cx - 2 * s, cy - 0.6 * s), (cx, cy - 1.6 * s),
                   (cx + 2 * s, cy - 0.6 * s)], HAIR, k, seed + 2, 0.07),
            curve([(cx - 10 * s, cy - 0.6 * s), (cx - 14 * s, cy + 1.6 * s)],
                  HAIR, k, seed + 3, 0.09),
            curve([(cx + 10 * s, cy - 0.6 * s), (cx + 14 * s, cy + 1.6 * s)],
                  HAIR, k, seed + 4, 0.09)]


def iron_gate(cx, cy, s=1.0, seed=61, gold=False, open_=False):
    """철문. open_이면 한쪽이 열려 있다."""
    k = _c(INK, gold)
    out = [line(cx - 11 * s, cy - 12 * s, cx - 11 * s, cy + 12 * s, THIN, k,
                seed, 0.08)]
    n = 5
    for i in range(n):
        x = cx - 11 * s + (i + 1) * 4.4 * s
        if open_ and i >= 3:
            x = cx - 11 * s + (i + 1) * 4.4 * s + 3.4 * s
        out.append(line(x, cy - 11 * s, x, cy + 11 * s, HAIR, k, seed + 5 + i,
                        0.08, 4, 0.8))
    out.append(line(cx - 11 * s, cy - 4 * s, cx + 12 * s, cy - 4.4 * s, HAIR,
                    k, seed + 20, 0.07, 4, 0.6))
    return out


def bench(cx, cy, s=1.0, seed=62, gold=False, overlap=False):
    """벤치 널판. overlap이면 예전 벤치가 겹쳐 보인다."""
    k = _c(INK, gold)
    out = [line(cx - 20 * s, cy, cx + 20 * s, cy, 0.5, INK_SOFT, seed, 0.07),
           line(cx - 20 * s, cy + 3.2 * s, cx + 20 * s, cy + 3.2 * s, 0.28,
                INK_SOFT, seed + 1, 0.07, 4, 0.6)]
    if overlap:
        out.append(line(cx - 18 * s, cy - 4 * s, cx + 18 * s, cy - 4.4 * s,
                        HAIR, INK_SOFT, seed + 2, 0.09, 4, 0.35))
    return out


def wristwatch(cx, cy, s=1.0, seed=63, gold=False, moving=True):
    """손목시계 — 다시 가고 있다."""
    k = _c(INK, gold)
    out = [ring(cx, cy, 5 * s, THIN, k, seed=seed, amp=0.08),
           curve([(cx - 5 * s, cy - 2 * s), (cx - 8.6 * s, cy - 5 * s)], FINE,
                 k, seed + 1, 0.08),
           curve([(cx + 5 * s, cy + 2 * s), (cx + 8.6 * s, cy + 5 * s)], FINE,
                 k, seed + 2, 0.08),
           dot(cx, cy, 0.5 * s, k)]
    if moving:
        out += [line(cx, cy, cx + 1.8 * s, cy - 3 * s, HAIR, GOLD if gold else k,
                     seed + 3, 0.06, 2),
                line(cx, cy, cx - 2.4 * s, cy + 1.4 * s, HAIR, k, seed + 4,
                     0.06, 2)]
    else:
        out += [line(cx, cy, cx, cy - 3.2 * s, HAIR, k, seed + 3, 0.06, 2),
                line(cx, cy, cx, cy + 2 * s, FINE, k, seed + 4, 0.06, 2)]
    return out


def shoes_pair(cx, cy, s=1.0, seed=64, gold=False):
    """구두 한 켤레 — 나란히 벗어놓았다."""
    k = _c(INK, gold)
    out = []
    for i in (-1, 1):
        x = cx + i * 5.4 * s
        out += [curve([(x - 3.4 * s, cy + 2.4 * s), (x - 3 * s, cy - 1.6 * s),
                       (x, cy - 3 * s), (x + 3 * s, cy - 1 * s),
                       (x + 3.4 * s, cy + 2.4 * s)], FINE, k,
                      seed + (i + 1) * 5, 0.09),
                line(x - 3.6 * s, cy + 2.8 * s, x + 3.6 * s, cy + 2.8 * s,
                     HAIR, k, seed + (i + 1) * 5 + 1, 0.06, 3, 0.7)]
    return out


def flower_line(cx, cy, s=1.0, seed=65, gold=True, n=4):
    """꽃이 핀 선 — p.132. 사물이 사라지고 선만 남는다."""
    k = GOLD if gold else INK
    base = [(cx - 30 * s, cy + 6 * s), (cx - 14 * s, cy + 2 * s),
            (cx + 4 * s, cy - 3 * s), (cx + 22 * s, cy - 10 * s)]
    out = [curve(base, 0.72, k, seed, 0.09)]
    from ink import _Rng
    rr = _Rng(seed + 3)
    for i in range(n):
        t = (i + 0.7) / (n + 0.4)
        bx = base[0][0] + (base[-1][0] - base[0][0]) * t
        by = base[0][1] + (base[-1][1] - base[0][1]) * t - 2.2 * s
        out.append(line(bx, by + 2.4 * s, bx + rr.sym(0.8), by - 1.4 * s, HAIR,
                        k, seed + 10 + i, 0.07, 2, 0.9))
        for j in range(5):
            a = math.radians(j * 72 - 90 + rr.sym(12))
            rad = (1.5 + rr.next() * 0.5) * s
            out.append(curve([(bx, by - 1.4 * s),
                              (bx + rad * math.cos(a),
                               by - 1.4 * s + rad * math.sin(a))],
                             HAIR, k, seed + 40 + i * 5 + j, 0.05))
    return out


def single_flower(cx, cy, s=1.0, seed=66, gold=True):
    """꽃 한 송이 — p.133 마지막."""
    k = GOLD if gold else INK
    out = [line(cx, cy + 9 * s, cx + 0.4 * s, cy + 1.6 * s, FINE, k, seed,
                0.08)]
    for i in range(6):
        a = math.radians(i * 60 - 90)
        out.append(curve([(cx + 0.4 * s, cy + 1.6 * s),
                          (cx + 0.4 * s + 1.4 * s * math.cos(a) * 0.6,
                           cy + 1.6 * s + 1.4 * s * math.sin(a) * 0.6),
                          (cx + 0.4 * s + 2.6 * s * math.cos(a),
                           cy + 1.6 * s + 2.6 * s * math.sin(a))],
                         HAIR, k, seed + 5 + i, 0.06))
    out.append(dot(cx + 0.4 * s, cy + 1.6 * s, 0.5 * s, k))
    return out


# ── 손 (43페이지에만) ───────────────────────────────────────────────────

def palm_open(cx, cy, s=1.0, seed=70, gold=False, hold=None):
    """펼친 손바닥. hold='gold'면 손바닥 위에 금빛 점."""
    k = INK
    out = [curve([(cx - 22 * s, cy + 12 * s), (cx - 24.5 * s, cy + 4 * s),
                  (cx - 18.5 * s, cy - 6.5 * s), (cx - 9 * s, cy - 8.6 * s)],
                 0.7, k, seed, 0.10),
           curve([(cx - 9 * s, cy - 8.6 * s), (cx - 3 * s, cy - 13.1 * s),
                  (cx + 0.5 * s, cy - 13.1 * s)], 0.62, k, seed + 1, 0.09),
           curve([(cx + 0.5 * s, cy - 13.1 * s), (cx + 8.5 * s, cy - 13.6 * s),
                  (cx + 11.5 * s, cy - 9.6 * s)], 0.62, k, seed + 2, 0.09),
           curve([(cx + 11.5 * s, cy - 9.6 * s), (cx + 19.5 * s, cy - 11.2 * s),
                  (cx + 23.5 * s, cy - 5.4 * s), (cx + 20.5 * s, cy + 5 * s)],
                 0.7, k, seed + 3, 0.10),
           curve([(cx + 20.5 * s, cy + 5 * s), (cx + 10 * s, cy + 16.2 * s),
                  (cx - 10 * s, cy + 16.4 * s), (cx - 22 * s, cy + 12 * s)],
                 0.75, k, seed + 4, 0.10),
           curve([(cx - 18.5 * s, cy - 6.5 * s), (cx - 27.5 * s, cy - 11 * s),
                  (cx - 34.5 * s, cy - 6 * s), (cx - 29.5 * s, cy + 1.2 * s),
                  (cx - 22 * s, cy + 2.4 * s)], 0.62, k, seed + 5, 0.10),
           curve([(cx - 13 * s, cy + 1 * s), (cx, cy + 4 * s),
                  (cx + 10 * s, cy + 1 * s)], HAIR, k, seed + 6, 0.10, 0.75),
           curve([(cx - 11 * s, cy + 7 * s), (cx + 1 * s, cy + 9.4 * s),
                  (cx + 9.5 * s, cy + 6 * s)], HAIR, k, seed + 7, 0.10, 0.7),
           curve([(cx - 16 * s, cy - 2 * s), (cx - 13.5 * s, cy + 5 * s),
                  (cx - 13.5 * s, cy + 11 * s)], HAIR, k, seed + 8, 0.10, 0.7)]
    for i, x in enumerate((-6, 1, 8)):
        out.append(line(cx + x * s, cy - 11.4 * s, cx + (x + 0.5) * s,
                        cy - 7.4 * s, HAIR, k, seed + 20 + i, 0.06, 2, 0.55))
    if hold:
        out.append(dot(cx, cy - 0.5 * s, 1.25 * s, GOLD))
    return out


def hand_rest(cx, cy, s=1.0, seed=71, gold=False, flip=False):
    """벤치에 얹은 손등. flip이면 좌우 반전."""
    k = INK
    m = -1 if flip else 1
    out = [curve([(cx - 10 * s * m, cy + 9.8 * s),
                  (cx - 11 * s * m, cy + 2.5 * s),
                  (cx - 8.5 * s * m, cy - 3 * s),
                  (cx - 3.5 * s * m, cy - 4.6 * s),
                  (cx + 2 * s * m, cy - 3.4 * s),
                  (cx + 8 * s * m, cy + 0.6 * s),
                  (cx + 10 * s * m, cy + 9.8 * s)], 0.68, k, seed, 0.10)]
    for i, (fx, fy) in enumerate(((-5.7, 1.6), (-1, -2.2), (3.8, -1.6))):
        out.append(curve([(cx + fx * s * m, cy + 9.8 * s),
                          (cx + (fx + 0.4) * s * m, cy + 4.6 * s),
                          (cx + (fx + 1.5) * s * m, cy + fy * s)],
                         HAIR, k, seed + 5 + i, 0.09, 0.7))
    out.append(curve([(cx - 7.5 * s * m, cy + 1.5 * s),
                      (cx, cy - 0.2 * s),
                      (cx + 6.5 * s * m, cy + 1 * s)], HAIR, k, seed + 20,
                     0.09, 0.6))
    return out


def two_hands(cx, cy, s=1.0, seed=72, gold=True):
    """두 손 — 한 뼘 간격, 닿지 않는다. 금빛 실땀이 잇는다. p.126."""
    out = bench(cx, cy + 8 * s, s, seed)
    out += hand_rest(cx - 22 * s, cy, s, seed + 10)
    out += hand_rest(cx + 22 * s, cy, s, seed + 30, flip=True)
    if gold:
        out.append(thread(cx - 10 * s, cy + 9.6 * s, cx + 10 * s, cy + 9.6 * s,
                          GOLD, 0.55, seed + 50, 0.14, 7))
    return out


def hand_grip(cx, cy, s=1.0, seed=73, gold=False, obj=None):
    """무엇을 쥔 손 — 손가락 관절이 보인다."""
    k = INK
    out = [curve([(cx - 9 * s, cy + 7 * s), (cx - 10.4 * s, cy + 0.6 * s),
                  (cx - 6.4 * s, cy - 4.4 * s), (cx - 0.4 * s, cy - 5.6 * s),
                  (cx + 6 * s, cy - 3.4 * s), (cx + 9.4 * s, cy + 1.6 * s),
                  (cx + 8 * s, cy + 7.4 * s), (cx - 2 * s, cy + 9.4 * s)],
                 0.68, k, seed, 0.11, closed=True)]
    for i in range(3):
        x = cx - 5.4 * s + i * 4.4 * s
        out.append(curve([(x, cy - 4.8 * s), (x + 0.6 * s, cy - 1 * s),
                          (x - 0.2 * s, cy + 2.6 * s)], HAIR, k, seed + 5 + i,
                         0.09, 0.65))
    out.append(curve([(cx - 8 * s, cy - 1.4 * s), (cx + 7.6 * s, cy - 0.6 * s)],
                     HAIR, k, seed + 20, 0.09, 0.6))
    return out


def hand_press(cx, cy, s=1.0, seed=74, gold=False):
    """검지로 누르는 순간 — 접촉점이 정확하다. p.116."""
    k = INK
    return [curve([(cx - 4 * s, cy + 13 * s), (cx - 5.4 * s, cy + 5 * s),
                   (cx - 3.4 * s, cy - 1.6 * s), (cx - 0.6 * s, cy - 4.2 * s)],
                  0.68, k, seed, 0.10),
            curve([(cx - 0.6 * s, cy - 4.2 * s), (cx + 2 * s, cy - 4.6 * s),
                   (cx + 4 * s, cy - 1.4 * s), (cx + 5 * s, cy + 5 * s),
                   (cx + 6 * s, cy + 13 * s)], 0.68, k, seed + 1, 0.10),
            curve([(cx - 2.4 * s, cy + 3 * s), (cx + 3.4 * s, cy + 3.4 * s)],
                  HAIR, k, seed + 2, 0.08, 0.6),
            curve([(cx - 3 * s, cy + 8 * s), (cx + 4.4 * s, cy + 8.4 * s)],
                  HAIR, k, seed + 3, 0.08, 0.55),
            curve([(cx - 1.2 * s, cy - 3.2 * s), (cx + 2.6 * s, cy - 2.8 * s)],
                  HAIR, k, seed + 4, 0.07, 0.5)]


def hand_release(cx, cy, s=1.0, seed=75, gold=False):
    """놓는 손 — 손가락이 막 벌어진다."""
    k = INK
    out = [curve([(cx - 10 * s, cy + 8 * s), (cx - 11.4 * s, cy + 1 * s),
                  (cx - 7 * s, cy - 4 * s), (cx, cy - 5 * s),
                  (cx + 7 * s, cy - 3 * s), (cx + 10.4 * s, cy + 2 * s),
                  (cx + 9 * s, cy + 8.4 * s)], 0.68, k, seed, 0.11)]
    for i, (x, dx) in enumerate(((-6, -2.6), (-1.4, -0.6), (3.4, 1.6),
                                 (7.4, 3.4))):
        out.append(curve([(x * s + cx, cy - 4.6 * s),
                          ((x + dx * 0.5) * s + cx, cy - 8 * s),
                          ((x + dx) * s + cx, cy - 11.4 * s)],
                         FINE, k, seed + 5 + i, 0.10, 0.9))
    out.append(curve([(cx - 8.6 * s, cy + 1.6 * s), (cx + 8.4 * s, cy + 2.4 * s)],
                     HAIR, k, seed + 20, 0.09, 0.6))
    return out


def hand_touch(cx, cy, s=1.0, seed=76, gold=False):
    """쓸어주는 손 — 손끝만 닿는다."""
    k = INK
    return [curve([(cx - 13 * s, cy + 9 * s), (cx - 14 * s, cy + 2 * s),
                   (cx - 9 * s, cy - 3 * s), (cx - 2 * s, cy - 4.4 * s)],
                  0.68, k, seed, 0.10),
            curve([(cx - 2 * s, cy - 4.4 * s), (cx + 5 * s, cy - 3 * s),
                   (cx + 10.4 * s, cy + 0.6 * s), (cx + 13 * s, cy + 4 * s)],
                  0.62, k, seed + 1, 0.10),
            curve([(cx + 13 * s, cy + 4 * s), (cx + 9 * s, cy + 8 * s),
                   (cx - 2 * s, cy + 10.4 * s), (cx - 13 * s, cy + 9 * s)],
                  0.7, k, seed + 2, 0.10),
            curve([(cx - 10 * s, cy + 1.6 * s), (cx + 2 * s, cy + 4 * s),
                   (cx + 10 * s, cy + 3 * s)], HAIR, k, seed + 3, 0.10, 0.65),
            curve([(cx - 6 * s, cy - 3.6 * s), (cx - 5 * s, cy + 0.6 * s)],
                  HAIR, k, seed + 4, 0.07, 0.5),
            curve([(cx + 1 * s, cy - 4 * s), (cx + 2 * s, cy + 0.4 * s)],
                  HAIR, k, seed + 5, 0.07, 0.5)]


def hand_point(cx, cy, s=1.0, seed=77, gold=False):
    """가리키는 손 — 검지만 뻗었다."""
    k = INK
    return [curve([(cx - 8 * s, cy + 9 * s), (cx - 9.4 * s, cy + 2.6 * s),
                   (cx - 6 * s, cy - 1.4 * s), (cx - 1.4 * s, cy - 2.4 * s)],
                  0.68, k, seed, 0.10),
            curve([(cx - 1.4 * s, cy - 2.4 * s), (cx + 1 * s, cy - 8 * s),
                   (cx + 2.6 * s, cy - 14.4 * s)], 0.62, k, seed + 1, 0.09),
            curve([(cx + 2.6 * s, cy - 14.4 * s), (cx + 4.6 * s, cy - 13.6 * s),
                   (cx + 4 * s, cy - 7 * s), (cx + 5.4 * s, cy - 1.6 * s)],
                  0.62, k, seed + 2, 0.09),
            curve([(cx + 5.4 * s, cy - 1.6 * s), (cx + 8.4 * s, cy + 2.6 * s),
                   (cx + 7 * s, cy + 9.4 * s), (cx - 8 * s, cy + 9 * s)],
                  0.7, k, seed + 3, 0.10),
            curve([(cx - 6 * s, cy + 2 * s), (cx + 5.4 * s, cy + 3 * s)],
                  HAIR, k, seed + 4, 0.09, 0.6)]


def hand_limp(cx, cy, s=1.0, seed=78, gold=False):
    """힘없이 늘어진 손."""
    k = INK
    out = [curve([(cx - 6 * s, cy - 10 * s), (cx - 7.4 * s, cy - 2 * s),
                  (cx - 5 * s, cy + 3.4 * s), (cx, cy + 5.4 * s),
                  (cx + 5.4 * s, cy + 4 * s), (cx + 8 * s, cy - 1.4 * s),
                  (cx + 7 * s, cy - 10 * s)], 0.68, k, seed, 0.11)]
    for i, x in enumerate((-3.4, 0.6, 4.4)):
        out.append(curve([(cx + x * s, cy + 4.6 * s),
                          (cx + (x + 0.6) * s, cy + 8.4 * s),
                          (cx + (x + 1.4) * s, cy + 11.4 * s)],
                         FINE, k, seed + 5 + i, 0.10, 0.85))
    return out


HANDS = {
    "palm": palm_open, "rest": hand_rest, "grip": hand_grip,
    "press": hand_press, "release": hand_release, "touch": hand_touch,
    "point": hand_point, "limp": hand_limp, "two": two_hands, "fist": fist,
}

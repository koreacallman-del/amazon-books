"""133페이지 조판 — 「시계가 멈춘 마을」

각 페이지: (사물함수, x, y, 배율, 추가인자)의 목록.
좌표는 0~100. 홀수 페이지는 책등이 왼쪽, 짝수는 오른쪽이므로
사물은 x 30~70 구간에 두어 양쪽 모두 안전하게 한다 (예외는 개별 확인).

금빛: 저자 결정에 따라 30페이지로 한정 (초안 41 → 30).
손: 43페이지. 나머지는 사물과 여백만.
"""

# 금빛이 들어가는 30페이지 — 이 목록이 유일한 기준이다
GOLD_PAGES = {
    65, 66, 67, 68, 69,                    # 싹 — 첫 금빛
    71, 72, 73, 74, 75, 76, 77,            # 항아리 — 금빛 밀도 최고
    86, 87,                                # 가로등이 켜짐
    91, 97,                                # 씨앗
    103, 105, 107, 108, 110, 118,          # 별
    113,                                   # 땅 위의 금빛 점
    115, 116, 117, 119,                    # 전화
    126,                                   # 두 손 사이의 실
    132, 133,                              # 꽃이 핀 선 · 마지막 꽃
}

# 텍스트를 놓을 자리 — 사물 반대편
TEXT_TOP, TEXT_BOTTOM, TEXT_MID = "top", "bottom", "mid"

# (사물, x, y, 배율, kwargs, 텍스트자리)
P = {}


def _(n, items, text=TEXT_BOTTOM):
    P[n] = (items, text)


# ── 1부. 멈춘 것들 (p.1~35) ─────────────────────────────────────────────
_(1,  [("clock_hands", 50, 40, 1.0, {})], TEXT_BOTTOM)
_(2,  [], TEXT_MID)                                    # 장 제목 — 선과 여백만
_(3,  [("planner", 50, 42, 1.0, {})])
_(4,  [("planner", 50, 42, 1.0, {})], TEXT_BOTTOM)
_(5,  [("hand_grip", 50, 58, 1.0, {}), ("phone", 50, 42, 0.9, {})], TEXT_TOP)
_(6,  [("phone", 50, 48, 1.0, {"face_down": True})], TEXT_BOTTOM)
_(7,  [("hand_grip", 44, 50, 0.95, {}), ("door_handle", 54, 46, 1.0, {})], TEXT_BOTTOM)
_(8,  [("hand_grip", 44, 50, 0.95, {}), ("door_handle", 54, 46, 1.0, {})], TEXT_TOP)
_(9,  [("empty_bowl", 50, 52, 1.1, {})], TEXT_TOP)
_(10, [("hand_grip", 40, 40, 0.9, {}), ("briefcase", 52, 56, 1.0, {})], TEXT_TOP)
_(11, [("worn_heel", 50, 50, 1.2, {})], TEXT_BOTTOM)
_(12, [("coat_hem", 52, 48, 1.1, {})], TEXT_BOTTOM)
_(13, [("leaf", 50, 46, 1.3, {})], TEXT_BOTTOM)
_(14, [("leaf", 54, 50, 1.3, {})], TEXT_TOP)
_(15, [("hand_touch", 40, 56, 0.9, {}), ("wall_corner", 56, 44, 1.0, {})], TEXT_TOP)
_(16, [("grass", 50, 58, 1.4, {"n": 4})], TEXT_TOP)
_(17, [("hand_grip", 50, 58, 0.95, {}), ("phone", 50, 42, 0.9, {})], TEXT_TOP)
_(18, [("footprints", 50, 52, 1.1, {})], TEXT_BOTTOM)
_(19, [("hand_touch", 40, 56, 0.9, {}), ("broken_stone", 56, 44, 1.1, {})], TEXT_TOP)
_(20, [("hand_touch", 40, 60, 0.85, {}), ("signpost", 54, 44, 1.0, {})], TEXT_BOTTOM)
_(21, [("compass", 50, 46, 1.2, {})], TEXT_BOTTOM)
_(22, [], TEXT_MID)
_(23, [("dial", 50, 42, 1.0, {})], TEXT_BOTTOM)
_(24, [("dial", 50, 44, 1.0, {})], TEXT_BOTTOM)
_(25, [("hand_grip", 44, 58, 0.9, {}), ("screwdriver", 54, 44, 1.0, {})], TEXT_TOP)
_(26, [("mainspring", 50, 46, 1.0, {"loose": True})], TEXT_BOTTOM)
_(27, [("gear", 43, 46, 1.0, {}), ("gear", 57, 46, 0.85, {})], TEXT_BOTTOM)
_(28, [("pocket_watch", 50, 44, 1.0, {"n": 3})], TEXT_BOTTOM)
_(29, [("wind_key", 50, 46, 1.2, {})], TEXT_BOTTOM)
_(30, [("hand_grip", 50, 60, 0.9, {}), ("phone", 50, 44, 0.9, {"face_down": True})], TEXT_TOP)
_(31, [("empty_chair", 50, 48, 1.1, {})], TEXT_BOTTOM)
_(32, [("cloth_scrap", 52, 44, 1.2, {})], TEXT_BOTTOM)
_(33, [("hand_release", 48, 40, 0.95, {}), ("screwdriver", 52, 58, 1.0, {"down": True})], TEXT_BOTTOM)
_(34, [("screwdriver", 50, 62, 1.0, {"down": True})], TEXT_TOP)
_(35, [("clock_hands", 46, 44, 0.85, {}), ("grass", 62, 56, 0.9, {"n": 3})], TEXT_BOTTOM)

# ── 2부. 보내고 기다리는 것들 (p.36~69) ─────────────────────────────────
_(36, [], TEXT_MID)
_(37, [("bell", 50, 46, 1.1, {})], TEXT_BOTTOM)
_(38, [("nest", 50, 46, 1.0, {})], TEXT_BOTTOM)
_(39, [("bird_sil", 50, 48, 1.2, {"flying": False})], TEXT_BOTTOM)
_(40, [("eggshell", 50, 50, 1.3, {})], TEXT_TOP)
_(41, [("bird_sil", 62, 30, 0.55, {})], TEXT_BOTTOM)
_(42, [("bird_sil", 50, 46, 1.1, {"flying": False})], TEXT_BOTTOM)
_(43, [("sneaker", 50, 52, 1.0, {})], TEXT_TOP)
_(44, [("hand_grip", 50, 60, 0.9, {}), ("phone", 50, 44, 0.9, {})], TEXT_TOP)
_(45, [("phone", 50, 48, 1.0, {})], TEXT_BOTTOM)
_(46, [("nest", 50, 48, 0.9, {})], TEXT_TOP)
_(47, [("bird_sil", 50, 46, 1.15, {"flying": False})], TEXT_BOTTOM)
_(48, [("feather", 54, 44, 1.1, {})], TEXT_BOTTOM)
_(49, [("palm_open", 50, 56, 0.85, {}), ("feather", 50, 44, 0.8, {})], TEXT_TOP)
_(50, [("waterdrop", 50, 44, 1.6, {})], TEXT_BOTTOM)
_(51, [("hand_point", 42, 58, 0.85, {}), ("name_tag", 54, 44, 1.0, {})], TEXT_TOP)
_(52, [("name_tag", 50, 46, 1.0, {})], TEXT_BOTTOM)
_(53, [], TEXT_MID)
_(54, [("dry_and_bloom", 50, 46, 1.2, {})], TEXT_BOTTOM)
_(55, [("hand_grip", 38, 42, 0.85, {}), ("watering_can", 56, 50, 1.0, {"tilted": False})], TEXT_BOTTOM)
_(56, [("calendar", 50, 44, 1.0, {})], TEXT_BOTTOM)
_(57, [("hand_grip", 40, 58, 0.85, {}), ("note", 54, 44, 1.1, {})], TEXT_TOP)
_(58, [("note", 46, 48, 0.9, {}), ("note", 54, 52, 0.9, {})], TEXT_TOP)
_(59, [("empty_chair", 50, 48, 1.0, {"n": 2})], TEXT_BOTTOM)
_(60, [("hand_touch", 40, 58, 0.85, {}), ("cut_thread", 56, 44, 1.0, {"gap": 9})], TEXT_TOP)
_(61, [("hand_touch", 38, 58, 0.8, {}), ("bud", 56, 46, 1.1, {})], TEXT_TOP)
_(62, [("roots", 50, 48, 1.1, {})], TEXT_TOP)
_(63, [("bud", 46, 44, 1.0, {}), ("roots", 56, 60, 0.7, {})], TEXT_TOP)
_(64, [("hand_grip", 38, 40, 0.85, {}), ("watering_can", 56, 50, 1.0, {"tilted": True})], TEXT_BOTTOM)
_(65, [("watering_can", 54, 40, 1.0, {"tilted": True}), ("soil_patch", 50, 68, 1.0, {})], TEXT_TOP)
_(66, [("soil_patch", 50, 60, 1.0, {}), ("bud", 50, 54, 0.7, {})], TEXT_TOP)
_(67, [("sprout", 50, 50, 1.0, {})], TEXT_TOP)
_(68, [("palm_open", 50, 62, 0.8, {}), ("sprout", 50, 42, 0.6, {})], TEXT_TOP)
_(69, [], TEXT_MID)

# ── 3부. 금이 가고 꺼진 것들 (p.70~87) ──────────────────────────────────
_(70, [("jar", 50, 48, 1.1, {})], TEXT_BOTTOM)
_(71, [("shard", 50, 46, 1.3, {})], TEXT_BOTTOM)
_(72, [("hand_touch", 38, 58, 0.85, {}), ("jar", 56, 46, 0.9, {})], TEXT_TOP)
_(73, [("hand_touch", 38, 58, 0.8, {}), ("shard", 56, 46, 1.1, {})], TEXT_TOP)
_(74, [("jar", 50, 48, 1.2, {"stitched": True})], TEXT_TOP)
_(75, [("knuckles", 50, 48, 1.3, {})], TEXT_BOTTOM)
_(76, [("jar", 50, 54, 1.0, {"stitched": True}), ("waterdrop", 50, 32, 1.0, {"n": 3})], TEXT_TOP)
_(77, [("jar", 50, 52, 1.0, {"stitched": True})], TEXT_TOP)
_(78, [], TEXT_MID)
_(79, [("wildflower", 50, 52, 1.2, {})], TEXT_TOP)
_(80, [("bulb", 50, 42, 1.1, {}), ("grass", 50, 64, 0.9, {"n": 3})], TEXT_BOTTOM)
_(81, [("broom", 52, 46, 1.1, {})], TEXT_BOTTOM)
_(82, [("note", 50, 46, 1.2, {})], TEXT_BOTTOM)
_(83, [("lamp_post", 48, 46, 1.0, {})], TEXT_BOTTOM)
_(84, [("cat_sil", 52, 46, 1.2, {})], TEXT_BOTTOM)
_(85, [("hand_point", 40, 58, 0.85, {}), ("switch", 56, 46, 1.2, {})], TEXT_TOP)
_(86, [("hand_point", 38, 60, 0.85, {}), ("switch", 54, 46, 1.2, {"up": True})], TEXT_TOP)
_(87, [("bulb", 50, 42, 1.1, {"lit": True}), ("grass", 50, 66, 0.9, {"n": 3})], TEXT_BOTTOM)

# ── 4부. 심고 세는 것들 (p.88~119) ──────────────────────────────────────
_(88, [], TEXT_MID)
_(89, [("soil_patch", 50, 52, 1.0, {})], TEXT_TOP)
_(90, [("fist", 50, 50, 1.2, {})], TEXT_BOTTOM)
_(91, [("palm_open", 50, 56, 0.95, {"hold": "gold"})], TEXT_TOP)
_(92, [("seed_obj", 50, 50, 1.0, {})], TEXT_TOP)
_(93, [("hand_release", 50, 42, 0.9, {}), ("soil_patch", 50, 66, 0.8, {})], TEXT_TOP)
_(94, [("hand_touch", 38, 58, 0.8, {}), ("tree_rings", 56, 46, 1.0, {})], TEXT_TOP)
_(95, [("shade", 50, 52, 1.0, {})], TEXT_TOP)
_(96, [("hand_point", 40, 40, 0.85, {}), ("furrow", 52, 62, 1.0, {})], TEXT_TOP)
_(97, [("hand_release", 42, 40, 0.85, {}), ("furrow", 52, 62, 1.0, {}),
       ("seed_obj", 52, 60, 0.9, {})], TEXT_TOP)
_(98, [("soil_patch", 50, 58, 1.0, {})], TEXT_TOP)
_(99, [], TEXT_MID)
_(100, [("stone_steps", 50, 48, 1.1, {})], TEXT_BOTTOM)
_(101, [("clock_hands", 24, 46, 0.30, {}), ("nest", 37, 46, 0.26, {"wall": False}),
        ("bud", 50, 46, 0.55, {}), ("jar", 63, 46, 0.34, {}),
        ("bulb", 76, 46, 0.55, {})], TEXT_BOTTOM)   # 예외: 아이콘 5개 (저자 허용)
_(102, [("soil_patch", 50, 52, 0.9, {}), ("shade", 50, 62, 0.8, {})], TEXT_TOP)
_(103, [("star", 54, 34, 1.4, {})], TEXT_BOTTOM)
_(104, [("hand_point", 44, 62, 0.85, {}), ("star", 58, 32, 1.2, {})], TEXT_BOTTOM)
_(105, [("star", 46, 32, 1.1, {}), ("star", 60, 40, 0.9, {})], TEXT_BOTTOM)
_(106, [("hand_grip", 40, 58, 0.85, {}), ("town_map", 56, 44, 1.0, {})], TEXT_TOP)
_(107, [("star", 50, 38, 1.0, {"n": 3})], TEXT_BOTTOM)
_(108, [("star", 54, 26, 1.2, {})], TEXT_BOTTOM)
_(109, [("star", 50, 40, 1.0, {"n": 5})], TEXT_BOTTOM)
_(110, [("star", 50, 34, 1.3, {})], TEXT_BOTTOM)
_(111, [("briefcase", 50, 52, 1.0, {})], TEXT_TOP)
_(112, [("hand_grip", 40, 58, 0.85, {}), ("key", 56, 44, 1.1, {})], TEXT_TOP)
_(113, [("seed_obj", 50, 56, 1.0, {}), ("soil_patch", 50, 60, 0.8, {})], TEXT_TOP)
_(114, [("hand_grip", 50, 60, 0.9, {}), ("phone", 50, 44, 0.95, {})], TEXT_TOP)
_(115, [("hand_point", 42, 58, 0.85, {}), ("name_tag", 54, 44, 1.0, {})], TEXT_TOP)
_(116, [("hand_press", 50, 62, 0.95, {}), ("phone_signal", 50, 40, 1.0, {})], TEXT_TOP)
_(117, [("hand_grip", 44, 56, 0.9, {}), ("phone", 50, 42, 0.95, {"lit": True})], TEXT_TOP)
_(118, [("star", 46, 32, 1.1, {}), ("star", 60, 38, 1.0, {})], TEXT_BOTTOM)
_(119, [("phone", 50, 50, 1.0, {"lit": True})], TEXT_TOP)

# ── 5부. 나란히 (p.120~133) ─────────────────────────────────────────────
_(120, [], TEXT_MID)
_(121, [("signpost", 50, 46, 1.0, {"back": True})], TEXT_BOTTOM)
_(122, [("glasses", 50, 50, 1.1, {})], TEXT_BOTTOM)
_(123, [("hand_touch", 36, 56, 0.8, {}), ("iron_gate", 58, 46, 0.9, {"open_": True})], TEXT_TOP)
_(124, [("bench", 50, 50, 1.0, {"overlap": True})], TEXT_TOP)
_(125, [("hand_touch", 38, 58, 0.8, {}), ("cut_thread", 56, 44, 1.0, {"gap": 2.4})], TEXT_TOP)
_(126, [("two_hands", 50, 54, 0.92, {})], TEXT_TOP)
_(127, [("wristwatch", 50, 50, 1.2, {"moving": True})], TEXT_TOP)
_(128, [("leaf", 50, 44, 1.2, {"shadow": True})], TEXT_BOTTOM)
_(129, [("clock_hands", 50, 44, 0.9, {}), ("leaf", 53, 40, 0.8, {})], TEXT_BOTTOM)
_(130, [("shoes_pair", 50, 52, 1.1, {})], TEXT_TOP)
_(131, [("hand_release", 40, 40, 0.85, {}), ("briefcase", 54, 58, 1.0, {"empty": True})], TEXT_TOP)
_(132, [("flower_line", 50, 48, 1.0, {})], TEXT_TOP)
_(133, [("single_flower", 50, 52, 1.4, {})], TEXT_TOP)

# 장 제목 페이지 — 사물 없이 주선만 지나간다
CHAPTER_PAGES = {2, 22, 36, 53, 69, 78, 88, 99, 120}

assert len(P) == 133, f"페이지 수 오류: {len(P)}"
assert len(GOLD_PAGES) == 30, f"금빛 페이지 수 오류: {len(GOLD_PAGES)}"

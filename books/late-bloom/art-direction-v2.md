# 「시계가 멈춘 마을」 페이지별 아트 디렉션 v2 (사물 + 여백 + 선)

작성: designer · 기준 원고: `v8-page-map.md` (133페이지, 정본) · 규격: `illustration-spec.md`
판형 8.5×8.5in 정사각 · 인쇄: 표준 컬러(먹 + 포인트 금빛 1색) · 이미지는 프롬프트만 작성(생성 안 함)
기존안 `art-direction.md`(손과 선 v1)는 수정하지 않고 그대로 둠. 비교용.

콘셉트 한 줄: **각 페이지는 그 페이지의 사물 하나와 여백. 손은 쥐고·놓고·만지고·누르는 순간에만. 선은 책 전체를 잇는다.**

---

## 0. 전체 스타일 가이드

### 0-1. 고정 시스템 (양보 불가)
- 종이: 크림/아이보리, 미세한 종이결. 133장 전부 동일.
- 잉크: **먹 단색 + 금빛 1색.** 그 외 색 금지. 금빛은 얇은 선·작은 점으로만 (면 채움, 그라데이션, 반짝이는 금속 질감 금지 — 금박이 종이에 앉은 무광 느낌).
- 이유: (a) 133장이 한 권으로 보이려면 시스템이 하나여야 함 (b) 표준 컬러 범위를 벗어나면 권당 인쇄비가 $9.71로 뛰어 정가 $19가 됨.
- AI로 만들 때 스타일이 흔들리면 책이 싸 보임 → **0-8의 "스타일 고정 시험"을 먼저 하고, 통과한 뒤에 133장을 생성.**

### 0-2. 사물 원칙 (가장 중요)
- 한 페이지 = 사물 하나 + 여백 70% 이상. 배경·바닥 그림자·하늘·인물 전신·얼굴 없음.
- "생각하게 하는 느낌"은 무엇을 그리느냐가 아니라 무엇을 안 그리느냐에서 나온다. 사물은 작게, 정확하게, 페이지 한쪽에.
- 사물 크기: 대부분 폭 12~35%. 감정이 무거운 페이지일수록 더 작게, 여백을 더 크게 (p.34, p.83이 가장 큼).
- "사물 하나"의 해석: 한 켤레(구두·운동화), 두 의자, 두 별처럼 짝을 이루는 것은 하나로 본다. 다음 페이지만 예외적으로 서로 다른 사물이 둘 이상 나온다.
  - p.80, p.87: 전구 + 풀 한 포기 (지시문의 예시 구도)
  - p.86: 전구 + 스위치 + 고양이 눈 (원고가 셋을 한 페이지에 적음)
  - **p.101: 작은 아이콘 5개 일렬.** 원고가 5개를 나열하는 페이지라서. 장면이 아니라 "목록"으로 처리.
- **텍스트 자리**: 여백의 일부는 글이 앉을 자리다. 사물이 상단이면 글은 하단, 사물이 하단이면 글은 상단. 표의 "구도" 칸이 사물의 위치를 정하면 글은 그 반대쪽. 글이 긴 페이지(p.43, 83, 122, 133)는 사물을 더 작게.

### 0-3. 책등 안전영역 (홀짝 규칙)
- 1쪽이 오른쪽 면이므로 **홀수 페이지는 책등이 왼쪽, 짝수 페이지는 책등이 오른쪽.** 즉 바깥쪽(펼치는 쪽)은 홀수=오른쪽, 짝수=왼쪽.
- 기존안(v1)에는 이 방향이 홀짝과 맞지 않는 곳이 있었음(예: p.7 "왼쪽 가장자리=바깥쪽"). v2는 표에서 바깥쪽을 홀짝에 맞춰 적음.
- 규격상 안쪽 여백은 0.375in(폭의 4.4%). 여유를 두어 **모든 요소를 프레임 가장자리에서 6% 이상** 띄움 (선이 일부러 바깥 가장자리로 나가는 경우만 예외).
- 사물이 책등 쪽으로 걸치는 구도 없음. 금빛 파동(p.116)도 프레임 안에서 사라지게 그림.
- 선은 스프레드 중앙(책등)을 가로지르지 않는다.

### 0-4. 선의 재질 — 3종 (기존안 계승)
| 재질 | 무엇 | 쓰이는 곳 |
|---|---|---|
| **먹선** | 시간·거리·단절 | 책 전체 바탕. 금빛이 나와도 먹선은 남는다 |
| **금박(금빛)** | 치유·자각의 순간과 그 잔광 | 0-6 목록 (41페이지) |
| **실(바느질선)** | 끊어진 것이 이어짐 | p.60(끊어진 실), 73, 74(항아리를 금실땀으로 이음), 117, 118(전화가 이어짐), 125, 126(재회). 총 7페이지 |

### 0-5. 선의 온도 — 책 전체를 잇는 연결 요소
모든 페이지에 최소 한 획의 선이 있다 (사물 자체가 선이거나, 사물 옆의 바닥선·궤적·바람선·균열).
| 구간 | 온도 | 선의 성격 |
|---|---|---|
| p.1~32 | **냉** | 가늘고 곧고 각진 먹선. 직각, 균열, 끊김 |
| p.33~64 | **해빙** | 직선이 처음으로 느슨해지고 곡선이 나란히 등장. 아직 먹선 |
| p.65~119 | **금** | 금빛이 나타나고 확산. 먹선과 공존. p.106만 의도적으로 냉으로 되돌아감 |
| p.120~133 | **온** | 선이 조금 굵고 둥글어지고 끝이 부드러움. 금빛이 안정 |

**이음 규칙 (기본값)**: 홀수 쪽의 바닥선·궤적선은 바깥(오른쪽)으로 나가고, 다음 짝수 쪽에서 바깥(왼쪽)으로 같은 높이에서 들어온다. 한 장(leaf)을 넘길 때 선이 이어져 보이는 장치다. 짝수→홀수(책등을 마주 보는 면)는 이어지지 않고 각자 프레임 안에서 끝난다. 표에서 이 규칙과 다르면 "선의 상태" 칸에 예외를 적었다. (편집 도구에서 연결선만 별도 레이어로 얹는 방법도 가능. 0-8 참조)
**주선(主線)**: p.2 「들어가는 길」의 선 한 줄이 시작이고, p.120에서 되돌아오고, **p.132에서 꽃이 핀다.** 이 선이 이 책의 등뼈.

### 0-6. 금빛을 쓰는 페이지 (총 41쪽, 30.8%)
- 2부: p.65 66 67 68 69 (5)
- 3부: p.71 72 73 74 75 76 77 86 87 (9)
- 4부: p.91 101(항아리·전구만) 103 104 107 108 109 110 112 113 114 115 116 117 118 119 (16)
- 5부: p.120 121 122 124 125 126 127 128 129 132 133 (11)
- 그 외 92쪽은 순수 먹. 가장 밝은 금빛은 p.86(가로등)과 p.116(전화). p.66~67의 싹은 책에서 처음으로 금빛이 사물 전체를 차지하는 곳.
- p.105(별을 세다 멈춤)에서는 금빛이 잠시 꺼지고 p.107에서 돌아온다. p.130·131은 금 없이 굵은 먹선으로 아낀다.

### 0-7. 손 (총 43쪽 / 133쪽 = 32.3%, 목표 30~40% 충족)
- 등장 규칙: 쥐고·놓고·만지고·누르는 순간에만. 나머지는 사물과 여백.
- 손은 **한 페이지에 하나.** 예외는 p.126 단 한 곳(손 둘). 이후 p.127~133에는 손이 없거나 하나(p.131)뿐이다.
- 60대의 손: 마디 굵고 힘줄·검버섯, 손톱 짧고 뭉툭. 항상 손목에서 잘린 클로즈업. 팔뚝·몸통·얼굴 없음. 매끈하거나 젊게 그리지 않는다.
- 손이 없는 존재(새·고양이·항아리·꽃)에는 손을 그리지 않는다.
- 손 등장 페이지:
  - 1부(11): p.5 7 8 10 15 17 19 20 25 30 33
  - 2부(10): p.44 49 51 55 57 60 61 64 65 68
  - 3부(5): p.72 73 75 85 86
  - 4부(13): p.90 91 93 94 96 97 104 106 112 114 115 116 117
  - 5부(4): p.123 125 126(둘) 131
- 부별 비율: 1부 31% · 2부 29% · 3부 28% · 4부 41% · 5부 29%. 4부가 가장 높은 이유는 씨앗(심음)과 전화(누름)라는 손의 동작이 몰려 있기 때문.
- 손이 연속 4쪽 이상 이어지는 곳은 p.114~117(전화 클라이맥스) 한 곳뿐.

### 0-8. 제작 순서 (초보자용)
1. **스타일 고정 시험 (필수)**: 아래 7쪽을 먼저 생성한다 — p.1, 33, 67, 86, 101, 116, 126. 종이 색·먹선 굵기·금빛 질감이 같은 책으로 보이는지 확인. 하나라도 튀면 접두어를 고치고 7쪽을 다시. 통과한 뒤에야 나머지 126쪽 생성.
2. 같은 도구·같은 모델·같은 접두어로 전부 생성. 중간에 모델을 바꾸지 않는다. (가능하면 첫 통과 이미지를 참조 이미지로 계속 넣는다)
3. 생성 후 종이색 통일: 편집 도구에서 배경을 하나의 크림색(예: #F6F0E0 근방)으로 맞춘다. 이미지 안에 글자가 들어갔으면 폐기.
4. 텍스트는 편집 도구(Canva 등)에서 얹는다. 사물의 반대쪽 여백에.
5. 짝수 쪽은 책등이 오른쪽이므로 사물이 오른쪽에 치우치지 않았는지 확인.
6. **AI로 생성한 이미지는 KDP 등록 시 "AI-generated images"로 공시해야 한다** (kdp-rules.md). 본문 텍스트가 사람 저작이어도 이미지가 AI면 별개로 공시. 아마존 공식 정책상 상품 페이지에는 표시되지 않음. `notes.md` 기록은 편집장이 처리.

### 0-9. 아동서로 보이지 않게
정사각 판형이라 위험이 실재한다. 지킬 것: 귀여운 캐릭터 없음 · 채도 없음(먹+무광 금) · 둥근 장난감 같은 형태 금지 · 새와 고양이는 눈·표정 없는 붓 실루엣 · 손은 늙은 손 · 사물은 실제 크기감과 마모(닳은 구두, 낡은 열쇠). 폰트는 편집 도구에서 성인용 세리프.

---

## 1부. 멈춘 것들 — p.1 ~ p.35 (35쪽)
「들어가는 길」 + 「첫 번째 만남 — 멈춘 시계탑」. 선: 냉 (직선·직각·균열 → 33쪽부터 처음으로 느슨해짐). 손 11쪽.

| p. | 텍스트 | 그 페이지의 사물 | 손 유무 및 동작 | 선의 상태 | 구도·여백 | 영문 프롬프트 |
|---|---|---|---|---|---|---|
| 1 | 시계가 멈춘 마을 / 늦게 피는 꽃이 오래 간다 | 6시에서 멈춘 시계 바늘 두 개 (문자판 없이 바늘만) | 손 없음 | 먹·냉. 바늘 자체가 선. 긴 바늘에 실금 한 가닥 | 사물 상단 중앙(폭 30%), 하단은 제목 자리. 여백 90% | Two thin black ink clock hands frozen at six o'clock with no dial, floating small in the upper center of the page, sharp cold linework with one hairline crack running through the longer hand. |
| 2 | 들어가는 길 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹·냉. **주선의 시작.** 왼쪽 바깥에서 들어와 화면 3분의 2 지점에서 끝나는 가는 직선 한 줄 | 선은 하단 3분의 1 높이. 여백 97% | A single hairline black ink line entering from the left edge and stopping two-thirds of the way across a vast empty cream page, nothing else. |
| 3 | 어른들은 바쁘다는 말을 참 좋아한다 / 얼굴이 밝아진다 / 등이 펴진다 | 빽빽하게 칸이 찬 일정표 한 장 (글자 없이 격자와 낙서 자국만) | 손 없음 | 먹·냉. 촘촘한 수평·수직 직선 격자. 격자 한 줄이 바깥(오른쪽)으로 나감 | 상단 중앙 폭 35%. 여백 85% | A small single page of a daily planner densely packed with tight rigid grid lines and abstract scribble marks with no legible writing, placed small in the upper center, one straight line leaving the page to the right. |
| 4 | 바쁘지 않느냐고 물으면 / 어디를 봐야 할지 모른다 | 텅 빈 일정표 한 장 (같은 크기, 격자가 성기게 끊김) | 손 없음 | 먹·냉. 격자선이 몇 줄만 남고 끊김. 왼쪽 바깥에서 선이 들어와 일정표 앞에서 멈춤 | 상단 중앙 폭 35% (p.3과 같은 자리). 여백 92% | The same small planner page now almost empty, only a few faint broken grid lines remaining, small in the upper center, a hairline entering from the left edge and stopping short of it. |
| 5 | 그 사람에게도 전화기가 하나 있었다 / 울리면 일어났고 / 두 번 울리면 뛰어갔고 | 전화기 (브랜드 없는 단순한 막대형 휴대전화) | 손 1 — 전화기를 꽉 움켜쥠. 책 전체에서 가장 팽팽한 쥠 | 먹·냉. 전화기에서 위로 뻗는 팽팽한 직선이 오른쪽 바깥으로 나감 | 사물 하단 중앙 폭 28%. 글은 상단. 여백 85% | A weathered elderly hand gripping a plain generic candy-bar mobile phone tightly, knuckles taut, cropped at the wrist, small at lower center, one taut straight black line rising from the phone and running off the right edge. |
| 6 | 울리지 않으면 앉아서 기다렸다 / 요즘 전화기는 울리지 않았다 / 쉬라는 거지 | 화면을 아래로 엎어 놓은 전화기 | 손 없음 (p.5의 손이 떠난 뒤) | 먹·냉. 힘이 빠져 살짝 처진 수평선이 왼쪽에서 들어와 전화기에서 끝남 | 하단 폭 25%, 위쪽 전부 비움. 여백 90% | A plain mobile phone lying face-down seen from above, small and low on the page, a limp slightly sagging hairline entering from the left edge and ending at it, black ink only. |
| 7 | 삼십 년 동안 같은 곳에 갔다 / 아침에 문을 열고 / 저녁에 문을 닫았다 | 낡은 문손잡이 (놋 레버형) | 손 1 — 손잡이를 쥠 | 먹·냉. 뒤에 수직 문틀선 한 획 (이음 규칙 예외: 수직선) | 중앙 하단 폭 22%. 여백 88% | A weathered elderly hand gripping an old brass lever door handle, cropped at the wrist, one straight vertical hairline behind it suggesting a door edge, small at lower center. |
| 8 | 삼십 년 삶이었다 / 문을 열어도 아무도 들어오지 않았다 | 반쯤 열린 문의 가장자리와 문틈 (빈 틈이 핵심) | 손 1 — 문을 열어 붙든 채 멈춘 손 (기다림) | 먹·냉. 수직선 끝에 작은 균열 하나 (예외: 수직선) | 중앙 폭 22%, 문틈은 빈 종이 그대로. 여백 88% | A weathered hand holding open the edge of a door left ajar, the narrow gap between door and frame left as blank paper, one vertical hairline with a tiny crack at its top end, small and centered. |
| 9 | 빈 방에 매일 들어가는 것은 / 빈 그릇을 식탁에 올리는 것과 같았다 | 빈 그릇 하나 (굽 낮은 사발) | 손 없음 | 먹·냉. 테두리 원선이 한 곳 끊김. 아래 바닥선이 오른쪽으로 나감 | 하단 중앙 폭 25%. 여백 90% | A single empty bowl seen from slightly above, thin black ink outline with a tiny gap in the rim, small and low, one hairline beneath it running off the right edge. |
| 10 | 그날도 걷고 있었다 / 매일 걷는 길이었다 / 같은 길인데 다른 길 같았다 | 낡은 서류가방 (모서리 닳은 가죽) | 손 1 — 손잡이를 쥐고 걷는 손 (매일의 쥠) | 먹·냉. 가방 아래 짧은 수평선이 왼쪽에서 들어옴 | 중앙 폭 25%, 가방은 손에 매달려 있음. 여백 85% | A worn leather briefcase hanging from an elderly hand that grips its handle, cropped at the wrist, no body, small at center, a short hairline entering from the left edge beneath it. |
| 11 | 길이 바뀐 게 아니라 / 걷는 사람이 바뀌고 있었을 것이다 | 굽이 한쪽만 닳은 구두 (밑창이 위로 뒤집힘) | 손 없음 | 먹·냉. 닳은 굽 자국이 이 책에서 처음으로 살짝 휜 곡선. 바닥선이 오른쪽으로 나감 | 하단 중앙 폭 22%. 여백 88% | A single leather dress shoe turned sole-up on the page, its heel worn down unevenly on one side, fine black ink, small and low, one thin line beneath it running off the right edge. |
| 12 | 사람들이 옆을 지나갔다 / 앞만 보고, 빠르게 / 지금은 아무도 나를 스치지 않았다 | 스쳐 지나가는 외투 자락 한 조각 (사람 없이 옷자락만) | 손 없음 | 먹·냉. 빠른 사선 세 획이 바깥(왼쪽)으로 사라지고, 그 뒤로 획이 없는 빈 공간 | 바깥쪽(좌) 상단에서 사라짐. 중앙~안쪽은 텅 빔. 여백 90% | A few quick diagonal black ink strokes of a passing coat hem sweeping away toward the left edge, no person, the rest of the page left as empty paper. |
| 13 | 강물 위에 떠 있는 나뭇잎처럼 / 물살에 밀려나고 있었다 | 물에 뜬 나뭇잎 한 장 | 손 없음 | 먹·냉. 물결 한 줄 위에 잎. 물결이 오른쪽으로 나감 | 중앙 폭 15% (잎). 여백 90% | A single fallen leaf floating on one thin wavy ink line of water, drifting toward the right edge, small on an empty cream page. |
| 14 | 밀려나는 것을 나이가 들었다고 부르기도 한다 / 물살이 빨라진 것뿐이었다 | 물살에 기울어진 같은 나뭇잎 | 손 없음 | 먹·냉. 물결 간격이 p.13보다 확연히 촘촘하고 빠름. 왼쪽에서 들어옴 | 중앙 폭 15%. 여백 90% | The same single leaf tilted steeply on one wavy ink line whose curves are tighter and faster than before, entering from the left edge, small and centered. |
| 15 | 밀려나듯 걷다가 / 한 번도 꺾어보지 않은 모퉁이 앞에 섰다 / 삼십 년 동안 매일 지나쳤다 | 담벼락 모퉁이 (직각으로 꺾이는 벽 모서리 한 줄) | 손 1 — 모서리를 짚음 | 먹·냉. **책에서 처음 나오는 직각.** 수평선이 직각으로 위로 꺾임 (예외: 꺾임) | 중앙 폭 25%. 여백 88% | A weathered elderly hand resting flat against the sharp corner of a wall where one straight black ink line turns at a hard right angle, cropped at the wrist, small and centered. |
| 16 | 모퉁이 안쪽으로 좁은 길이 보였다 / 바람이 그쪽에서 불어왔다 / 어딘가로 부르는 것 같기도 하고 | 바람에 한 방향으로 휘는 풀 한 포기 | 손 없음 | 먹·냉. 풀줄기 곡선과 그 뒤로 가는 바람선 세 가닥 | 하단 중앙 폭 12%, 높이 20%. 여백 90% | A single clump of grass bending sharply in one direction under three faint wind lines, black ink, small at lower center. |
| 17 | 어딘가로 밀어내는 것 같기도 했다 / 전화기를 꺼내 보았다. 조용했다 / 모퉁이를 꺾었다 | 화면이 꺼진 전화기 | 손 1 — 꺼낸 전화기를 쥐고 내려다봄 | 먹·냉. p.15와 같은 직각 선이 그대로 이어져 오른쪽으로 나감 | 하단 중앙. 여백 85% | A weathered hand holding a dark silent mobile phone, cropped at the wrist, small at lower center, beside it a thin black line that bends at a right angle and runs off the right edge. |
| 18 | 뒤를 돌아보니 / 큰길이 벌써 흐려져 있었다 | 뒤로 갈수록 옅어지는 발자국 네 개 | 손 없음 | 먹·냉. 발자국이 곧 선. 가까운 것은 진하고 마지막은 종이에 거의 묻힘 | 사선으로 배치, 폭 30%. 여백 88% | Four black ink footprints in a diagonal trail, the nearest one crisp and dark, each further one fainter until the last is almost blank paper, nothing else on the page. |
| 19 | 좁은 골목이 이어졌다 / 낮은 지붕, 오래된 담벼락, 갈라진 길 | 금이 간 돌벽돌 한 장 | 손 1 — 손끝으로 금을 따라 훑음 | 먹·냉. 지그재그 균열선. 이 책에서 가장 날카로운 선 | 중앙 폭 25%. 여백 85% | A weathered elderly hand tracing its fingertips along a jagged crack in a single old stone block, cropped at the wrist, sharp cold black ink lines, small and centered. |
| 20 | 골목 끝에 이정표가 하나 서 있었다 / 글씨가 반쯤 지워져 있었다 / 시계가 멈춘 마을 | 낡은 이정표 (기둥 + 작은 나무 팻말, 글씨는 긁힌 자국뿐) | 손 1 — 지워진 자리를 손끝으로 더듬음 | 먹·냉. 기둥 수직선이 위로 갈수록 흐려짐 (예외: 수직선) | 하단 중앙, 높이 35%. 글은 상단. 여백 85% | A weathered wooden signpost with one small board whose markings are only worn scratches and no readable letters, a hand feeling the board with its fingertips, cropped, the top of the post fading away, small and low. |
| 21 | 아무 데도 갈 곳이 없을 때 / 비로소 어디든 갈 수 있다 | 바늘이 풀려 어디도 가리키지 않는 나침반 | 손 없음 | 먹·냉. 나침반에서 곧은 헤어라인 한 줄이 오른쪽 바깥으로 | 중앙 폭 22%. 여백 90% | A plain round pocket compass drawn in black ink, its needle hanging loose and pointing nowhere in particular, small at center, one straight hairline leaving it toward the right edge. |
| 22 | 첫 번째 만남 — 멈춘 시계탑 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹·냉. 짧은 수평선 위에 서 있는 가장 가는 수직선 하나 (시계탑을 암시) | 바깥쪽(좌) 하단, 높이 25%. 여백 97% | A single tall hairline vertical black ink line standing on a short horizontal line, small in the lower left area of a vast empty cream page, nothing else. |
| 23 | 마을 한가운데에 시계탑이 서 있었다 / 바늘이 멈춰 있었다 / 여섯 시에서 | 시계 문자판 (숫자 없이 눈금 점만) + 6시 바늘 | 손 없음 | 먹·냉. 문자판 원선이 한 곳 끊김 | 상단 중앙 폭 30%. 여백 85% | A round clock face drawn in thin black ink with tiny tick dots and no numerals, both hands stopped at six o'clock, one small gap broken in the rim, small in the upper center. |
| 24 | 아침 여섯 시인지 밤 여섯 시인지는 알 수 없었다 / 멈춘 시계에게는 아침과 밤의 구별이 없다 | 세로선으로 반 가른 문자판 (반쪽은 빈 종이, 반쪽은 빗금) | 손 없음 | 먹·냉. 가운데 세로선 하나, 한쪽만 촘촘한 빗금 | 상단 중앙 폭 30%. 여백 85% | A round clock face split by one vertical line, the left half empty paper and the right half filled with dense fine hatching, hands at six o'clock, small in the upper center, black ink only. |
| 25 | 한 사람이 손에 도구를 들고만 서 있었다 | 시계 수리용 작은 드라이버 | 손 1 — 도구를 곧게 쥐고 굳어 있음 | 먹·냉. 도구가 그대로 수직 직선 (예외: 수직선) | 중앙 하단 폭 15%. 여백 88% | A weathered elderly hand holding a slim watchmaker's screwdriver upright and perfectly still, cropped at the wrist, one straight rigid black ink line, small at lower center. |
| 26 | "시계가 아픈 건가요?" / "이 시계는 아픈 게 아니에요." / "갈 곳을 잃은 거예요." | 풀려버린 태엽 (납작한 나선 스프링) | 손 없음 | 먹·냉. 나선의 바깥 끝이 풀려 벌어짐. 왼쪽에서 들어온 선이 나선에서 끝남 | 중앙 폭 22%. 여백 90% | A loosened watch mainspring drawn as a flat spiral of fine black ink line, its outer end uncoiled and sprung open, small at center, a hairline entering from the left edge. |
| 27 | "갈 곳이 없으면 바늘도 서는 거예요." / 나는 바늘이 아니라 시계였다 / 시계가 왜 서겠어 | 맞물린 채 굳은 톱니바퀴 두 개 | 손 없음 | 먹·냉. 각진 톱니선. 바닥선이 오른쪽으로 | 하단 중앙 폭 25%. 여백 88% | Two small interlocking cogwheels seized in place, crisp angular black ink line, small at lower center. |
| 28 | 걷다가 멈춘 사람, / 문을 열다가 멈춘 사람, / 웃다가 멈춘 사람 | 서로 다른 시각에 멈춘 회중시계 세 개 (일렬) | 손 없음 | 먹·냉. 시계 사이를 잇는 선이 매번 끊김 | 중앙, 세 개 합쳐 폭 45%. 여백 85% | Three small pocket watches in a row, each stopped at a different time, joined by one thin black line that breaks between each watch, small at center. |
| 29 | 시계가 멈추기 전에, / 이 사람들은 / 스스로 걸어본 적이 있었을까 | 태엽 감는 작은 열쇠 하나 | 손 없음 | 먹·냉. 열쇠 고리에서 나온 짧은 선이 허공에서 끝남 | 하단 중앙 폭 12%. 여백 92% | A single small watch winding key drawn in black ink, alone and low on an empty cream page, one very short line trailing from its bow ending in the air. |
| 30 | 주머니 속 전화기가 떠올랐다 / 꺼내 봤다. 화면이 꺼져 있었다 | 화면이 꺼진 전화기 (검은 화면은 촘촘한 빗금) | 손 1 — 전화기를 뒤집어 화면을 확인 | 먹·냉. 사각 테두리가 진함 | 중앙 폭 25%. 여백 85% | A hand turning over a dark silent mobile phone to check its screen, cropped at the wrist, the blank screen filled with fine hatching, small at center, cold black ink. |
| 31 | 전화기가 울리지 않으면 / 혼자 일어서 본 적이 있었을까 / 쓸데없는 생각이었다 | 빈 의자 (등받이 곧은 나무 의자 하나) | 손 없음 | 먹·냉. 의자 다리 아래 바닥선이 오른쪽으로 | 하단 중앙 폭 20%. 여백 88% | A single empty straight-backed wooden chair in thin black ink, small and low on the page, one hairline beneath its legs running off the right edge. |
| 32 | "하지만 바람은 시계가 없어도 불잖아요." / "시간은 원래 여기 있는 거잖아요." | 끈에 매달려 바람에 펄럭이는 천 조각 | 손 없음 | 먹·해빙 예고. 팽팽한 직선 끈 옆에 **처음으로 부드러운 곡선(천)이 나란히 놓임** | 상단 중앙, 천 폭 20%. 여백 88% | A single strip of cloth tied to a taut straight string and streaming sideways in the wind, the soft curve of the cloth contrasting the rigid line of the string, small in the upper center. |
| 33 | ★ 수리공이 도구를 내려놓았다 / 처음으로 내려놓았다 / 삼십 년 쥔 걸 지금 놓으면 | 놓이는 순간의 드라이버 | 손 1 — 손가락이 도구에서 막 떨어지는 순간 (놓음) | 먹·**해빙 시작.** 곧던 선이 처음으로 살짝 처짐 (예외: 처짐) | 하단 중앙 폭 20%, 여백을 크게. 여백 90% | A weathered elderly hand at the exact instant of letting go of a slim screwdriver, fingers just leaving it, cropped at the wrist, small at lower center, one once-rigid line beside it beginning to sag softly. |
| 34 | 그 삼십 년이 아무것도 아니게 되니까 / 바람이 불었다 / 한참을 서서 바람을 맞았다 | 바닥에 누워 있는 도구 하나 (손은 떠남) | 손 없음 | 먹·해빙. 바람 곡선 한 줄이 도구 위를 스침. 직선 자국은 아주 옅게 | 하단 바깥쪽(좌)에 아주 작게. **책 전체에서 가장 넓은 여백 95%** | A single tiny watchmaker's screwdriver lying on the ground, small at the lower left, one soft wind curve passing above it, everything else the most empty paper of the whole book. |
| 35 | 시계가 멈추기 전에는 / 바람이 부는 줄도 몰랐다 | p.1의 멈춘 바늘 두 개 + 그 옆을 지나는 바람 | 손 없음 | 먹·해빙. 부드러운 곡선이 바늘을 스쳐 오른쪽으로 흘러나감 → 2부로 이어짐 | 중앙 폭 20%. 여백 90% | The same two thin clock hands frozen at six o'clock, small at center, one soft curved wind line flowing past them and off the right edge, black ink only. |

---

## 2부. 보내고 기다리는 것들 — p.36 ~ p.69 (34쪽)
「두 번째 만남 — 돌아오지 않는 새」 + 「세 번째 만남 — 봄이 두 번 오는 꽃밭」. 선: 해빙 → p.65에서 첫 금빛. 손 10쪽. ★★ 책 전체의 전환점 p.67(싹).

| p. | 텍스트 | 그 페이지의 사물 | 손 유무 및 동작 | 선의 상태 | 구도·여백 | 영문 프롬프트 |
|---|---|---|---|---|---|---|
| 36 | 두 번째 만남 — 돌아오지 않는 새 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹·해빙. 짧은 수평선 위에 얹힌 아주 작은 열린 반원 (둥지를 암시) | 바깥쪽(좌) 하단 구석. 여백 97% | A tiny open half-circle line resting on a short horizontal line, in the lower left corner of a vast empty cream page, nothing else. |
| 37 | 시계가 멈춘 마을은 조용했다 / 바쁜 사람도 없으니 소리도 없었다 | 추가 멈춘 작은 놋종 | 손 없음 | 먹·해빙. 종을 매단 짧은 줄이 허공에서 끝남 | 상단 중앙 폭 15%. 여백 92% | A small hand bell hanging perfectly still with its clapper motionless, drawn in fine black ink, hung from a short cord that ends in the air, small in the upper center. |
| 38 | 담벼락 위에 잘 만든 둥지가 하나 있었다 / 그런데 텅 비어 있었다 | 빈 둥지 하나 (촘촘히 엮인 잔선) | 손 없음 | 먹·해빙. 둥지 안쪽은 종이 그대로 비움. 담선이 왼쪽에서 들어옴 | 하단 중앙 폭 25%, 위쪽은 텅 빈 하늘. 여백 88% | A single empty bird's nest woven from fine crisscrossing ink lines with its hollow left as blank paper, sitting on a short wall line entering from the left edge, empty sky above. |
| 39 | 어미 새인 듯 한 마리가 날개를 접고 앉아 있었다 / 하늘만 보고 있었다 | 날개를 접고 고개를 든 새 한 마리 (붓 실루엣, 눈 없음) | 손 없음 | 먹·해빙. 접힌 날개의 곡선 한 획 | 하단 폭 18%, 위쪽 하늘 전체 텅 빔. 여백 92% | A single small bird perched with folded wings and head tilted up, drawn as a spare ink brush silhouette without an eye or feather detail, low on a short wall line, empty sky above. |
| 40 | "누구를 기다리세요?" / "아이를." / "봄에 떠났어요." | 깨진 알껍질 반쪽 | 손 없음 | 먹·해빙. 둥근 테두리 한쪽이 톱니처럼 갈라짐 | 하단 중앙 폭 12%. 여백 92% | Half of a cracked eggshell resting open-side up, fine black ink, tiny and alone low on an empty cream page. |
| 41 | "지금은 가을이에요." / "내가 떠나라고 했어요." / "뒤돌아보지 마." | 멀리 날아가는 아주 작은 새 한 마리 | 손 없음 | 먹·해빙. 궤적선이 오른쪽 위 바깥으로 점점 가늘어지며 사라짐 | 바깥쪽(우) 상단 구석, 글은 하단. 여백 95% | A tiny bird silhouette flying away toward the upper right corner, a hairline flight arc thinning to nothing, the rest of the page empty. |
| 42 | "아이가 잘 배웠어요." / "한 번도 뒤돌아보지 않았어요." / "…당신은요?" | 목을 뒤로 돌려 이쪽을 보는 새 한 마리 | 손 없음 | 먹·해빙. 목의 곡선이 반대로 꺾이는 한 획 | 하단 중앙 폭 18%. 여백 90% | The same bird silhouette perched, its neck turned sharply back over its own shoulder, spare brushwork without eye detail, small and low, black ink only. |
| 43 | "뒤돌아본 적 있어요?" / 나도 아이에게 말했었다 / 열심히 해. 앞만 봐. 뒤돌아보지 마 (긴 글) | 발끝이 바깥쪽을 향한 운동화 한 켤레 | 손 없음 | 먹·해빙. 발끝에서 나온 직선이 가늘어지며 사라짐 (오른쪽) | 하단 바깥쪽(우), 폭 20%. 글이 길므로 위 3분의 2는 글 자리. 여백 90% | A pair of plain lace-up sneakers side by side seen from above with toes pointing to the right, small at the lower right, one thin straight line continuing from the toes and fading to nothing. |
| 44 | 가끔 전화기가 울렸다 / "잘 있어요?" "응." / "바빠요?" "응." | 진동으로 떨리는 전화기 | 손 1 — 전화기를 받쳐 든 손 | 먹·해빙. 진동을 나타내는 짧은 끊긴 획 두 쌍 (예외: 끊김) | 중앙 하단 폭 25%. 여백 85% | A hand holding a plain mobile phone that buzzes, two pairs of short broken vibration ticks beside it, cropped at the wrist, small at lower center. |
| 45 | 그게 전부였다 / 뒤돌아보면 내가 있는데 / 잘 키운 게 이런 건가 | 화면이 막 어두워진 전화기 | 손 없음 | 먹·해빙. 진동 획이 뚝 끊기고 그 자리에 빈 틈 | 하단 중앙 폭 22%. 여백 90% | A plain mobile phone lying still with its screen just gone dark, small and low, a gap of blank paper where vibration ticks once were. |
| 46 | "둥지는 움직이지 못하잖아요." / "하지만 소리는 갈 수 있잖아요." / "불러보세요. 이름을." | 빈 둥지 (p.38과 같음) | 손 없음 | 먹·해빙. 둥지 가장자리에서 가는 선 하나가 풀려 나와 오른쪽 바깥으로 | 하단 중앙 폭 22%. 여백 88% | The same empty woven nest in fine black ink, small and low, one thin line unspooling from its rim and curving off the right edge. |
| 47 | "바람은 어디든 가니까요." / 새가 고개를 들었다. 부리를 열었다 / 작지만 진짜 소리였다 | 부리를 벌린 새 (붓 실루엣) | 손 없음 | 먹·해빙. 부리에서 시작한 가는 곡선이 바람을 타고 오른쪽으로 | 하단 중앙 폭 18%. 여백 90% | A small bird silhouette with head lifted and beak open, spare ink brushwork, low on the page, one thin curved line leaving its beak and drifting off the right edge. |
| 48 | 그리운 소리는 작아도 멀리 간다 / 바람이 그 소리를 실어 갔다 | 바람에 실려 멀리 가는 깃털 한 장 | 손 없음 | 먹·해빙. 왼쪽에서 들어와 넓게 퍼지는 물결형 곡선 끝에 깃털 | 깃털은 중앙 오른쪽 (안쪽 6% 확보), 폭 8%. 여백 92% | A single tiny feather carried at the end of a wide softly widening wavy line that enters from the left edge, the feather small and right of center, black ink only. |
| 49 | 작은 소리가 돌아왔다 / 아이의 소리인지, / 바람의 메아리인지 | 손바닥에 내려앉는 깃털 (p.48의 깃털) | 손 1 — 오목하게 받는 손바닥 | 먹·해빙. 선이 위에서 내려와 손바닥에서 닫힘 (예외: 돌아옴, 프레임 안에서 끝남) | 하단 중앙 폭 25%. 여백 88% | A cupped elderly palm gently receiving a single tiny feather, cropped at the wrist, one thin curved line descending from above and ending in the palm, small at lower center. |
| 50 | 알 수는 없었다 / 하지만 새의 눈에 물이 고였다 / 부르는 것도 사랑이었다 | 매달린 물방울 한 방울 | 손 없음 | 먹·해빙. 가는 선 끝에 맺혀 떨어지기 직전 | 상단 중앙 폭 6%. 여백 95% | A single water droplet hanging from the tip of one hairline, about to fall, fine black ink, small in the upper center of an empty cream page. |
| 51 | 전화기를 꺼내 봤다 / 아이의 이름이 화면에 있었다 / 손가락이 가까이 갔다가 멈추었다 | 전화기 화면 속 이름 한 줄 (글자 없이 짧은 막대) | 손 1 — 검지가 화면 위에서 멈춤, 닿기 직전 (틈 남김) | 먹·해빙. 이름 막대와 손끝 사이의 미세한 틈 | 중앙 폭 28%. 여백 85% | A phone screen close-up showing one short horizontal bar like a written name and no letters, an index finger hovering just above it without touching, cropped at the wrist, a tiny visible gap between them. |
| 52 | 아직은 누르지 못했다 / 하지만 이름이 거기 있다는 것을 봤다 | 전화기 화면 속 이름 막대 (손가락이 물러난 뒤) | 손 없음 | 먹·해빙. p.51과 같은 크기의 이름 막대. 틈은 그대로 빈 종이 | 중앙 폭 28%. 여백 88% | The same phone screen with one short horizontal name bar and nothing else, no finger, an empty gap of paper above the bar, black ink only. |
| 53 | 세 번째 만남 — 봄이 두 번 오는 꽃밭 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹·해빙. 수직선 하나. 윗부분은 곡선으로 휘고 아랫부분은 곧고 뻣뻣함 | 바깥쪽(우) 하단 구석. 여백 97% | One thin vertical line whose upper half curves softly and lower half stays stiff and straight, small in the lower right corner of a vast empty cream page, nothing else. |
| 54 | 골목은 계속 이어졌다 / 꽃밭이 있었다 / 반은 피어 있고 반은 마른 꽃밭 | 활짝 핀 꽃 한 송이 + 마른 줄기 한 대 (나란히) | 손 없음 | 먹·해빙. 왼쪽 줄기는 부드러운 곡선, 오른쪽 줄기는 뻣뻣하게 꺾인 선 | 하단 중앙 폭 25%. 여백 85% | One blooming flower on a soft curved stem standing beside one dry withered stem drawn with stiff broken lines, small and low at center, fine black ink only. |
| 55 | "왜 반쪽만 마른 거예요?" / "한 사람은 매일 물을 주었고," / "한 사람은 내일 주겠다고 했어요." | 물뿌리개 (주둥이에서 물이 나오지 않음) | 손 1 — 손잡이를 쥠, 기울이지 않음 | 먹·해빙. 주둥이 끝에서 나온 곧은 선이 중간에 끊김 (물 없음) | 중앙 하단 폭 28%. 여백 85% | A weathered elderly hand gripping the handle of a plain metal watering can held upright, cropped at the wrist, no water falling, one short straight line from the spout that breaks off, small at lower center. |
| 56 | "삼십 년 동안 내일이었어요." / "내일은 오지 않는 날이에요." / 내일. 내일. 내일 | 뜯겨 나가는 달력 한 장 (칸만, 숫자 없음) | 손 없음 | 먹·해빙. 뜯긴 가장자리가 톱니선 | 상단 중앙 폭 22%. 여백 88% | A single torn-off calendar page drawn as an empty grid with no numerals, its torn edge zigzagged, small in the upper center, black ink only. |
| 57 | 나에게도 내일이라는 먼 날이 있었다 / 같이 걷자. 내일 / 바빴다 | 접힌 쪽지 한 장 | 손 1 — 쪽지를 집어 내밀다 멈춤 (건네지 못함) | 먹·해빙. 쪽지에서 뻗은 선이 도중에 꺾여 되돌아옴 (예외: 되돌아옴) | 하단 중앙 폭 22%. 여백 88% | Elderly fingers pinching a small folded note held out and stopped midway, cropped at the wrist, one thin line from the note extending outward then bending back on itself, small at lower center. |
| 58 | 정말 바빴다 / 삼십 년 동안 내일을 모으면 / 한 번도가 된다 | 뜯어낸 달력 종이 더미 (어긋나게 쌓임) | 손 없음 | 먹·해빙. 짧은 수평선이 겹겹이 쌓이되 이어지지 않음 | 하단 중앙 폭 22%. 여백 88% | A small crooked stack of torn-off calendar pages seen from the side, layers of short unconnected horizontal ink lines, low at center, black ink only. |
| 59 | 한 번도 걷지 않았다 / 한 번도 보러 가지 않았다 / 한 번도 앉아서 얘기하지 않았다 | 마주 보게 놓였지만 빈 의자 두 개 | 손 없음 | 먹·해빙. 두 의자 사이 바닥선이 한 곳 끊김 (틈 하나) | 중앙 하단, 합쳐 폭 35%. 여백 88% | Two empty wooden chairs facing each other with a gap between them, thin black ink, small and low at center, the ground line broken once in the gap. |
| 60 | 가장 가까운 사람에게 / 가장 먼 말을 했다 / 바빴다는 말이 이제는 변명처럼 들렸다 | 끊어진 실 한 가닥 (양 끝이 멀리 벌어짐) | 손 1 — 한쪽 실 끝을 쥠 (다른 쪽 끝은 멀리 떠 있음) | **먹실**(끊어진 상태). 두 끝의 간격이 이 책에서 가장 멀다. p.125에서 이 간격이 좁아진다 | 손은 바깥쪽(좌), 다른 끝은 오른쪽 중앙(안쪽 여백 확보). 여백 88% | A weathered hand pinching one end of a cut black thread, cropped at the wrist, the other end hanging far away across the page with a wide empty gap between the two ends, small and low. |
| 61 | "물을 주면 다시 피나요?" / "첫 번째 봄처럼은 안 피어요." / "조용하고 작게." | 마른 줄기 끝의 아주 작은 새 눈(봉오리) | 손 1 — 검지 끝이 봉오리에 닿을 듯 말 듯 | 먹·해빙. 꺾인 마른 선 끝이 살짝 곡선으로 시작 | 중앙 하단 폭 22%. 여백 88% | A dry broken stem ending in one tiny bud, an elderly fingertip hovering just beside it without touching, cropped at the wrist, the tip of the stem beginning a faint new curve, black ink only. |
| 62 | "그게 두 번째 봄이에요." / "삼십 년을 안 줘도 죽지 않은 뿌리예요." / "마르고 나서야 이 뿌리가 보였어요." | 땅 선 아래로 뻗은 뿌리 (위는 마른 그루터기만) | 손 없음 | 먹·해빙. 땅 선 한 줄, 그 아래로 뿌리가 곡선으로 퍼짐 | 중앙 폭 30%. 여백 82% | A short dry stump above one horizontal ground line and a branching root system spreading in graceful curves below it, fine black ink, small at center. |
| 63 | "보이는 꽃은 시들어도" / "보이지 않는 뿌리는 살아 있었어요." / "중요한 것은 늘 보이지 않는 법이니까요." | 고개 숙인 시든 꽃 한 송이 + 거의 안 보이는 점선 뿌리 | 손 없음 | 먹·해빙. 위는 선명한 마른 선, 아래 뿌리는 점선으로 종이에 거의 묻힘 | 중앙 폭 25%. 여백 85% | A single drooping withered flower in crisp black ink above a ground line, its roots below drawn only as extremely faint dotted lines almost invisible on the paper. |
| 64 | "좀 들어주시겠어요?" / "손목이 예전 같지 않아서요." | 물뿌리개 (막 기울려는) | 손 1 — 물뿌리개 밑을 받쳐 듦 (다른 손은 프레임 밖) | 먹·해빙. 주둥이가 처음으로 사선 각도 | 중앙 폭 28%. 여백 85% | An elderly hand supporting the base of a watering can that is just beginning to tilt, cropped at the wrist, the spout forming a diagonal line, small at center. |
| 65 | ★ 내가 기울였다 / 물이 마른 흙에 스며들었다 / 흙이 숨을 쉬기 시작했다 | 기울어진 물뿌리개에서 떨어지는 물 한 줄 + 마른 흙 선 | 손 1 — 물뿌리개를 완전히 기울임 (물이 쏟아지는 순간) | 먹 + **금(책 최초).** 물줄기는 먹선, 흙에 닿는 지점에서만 금빛이 처음 번짐 | 물뿌리개 상단 중앙, 흙선 60% 높이. 글은 하단. 여백 85% | An elderly hand fully tilting a watering can at the upper center, one thin black line of water falling to a dry ground line below, and only where the water meets the soil a tiny first touch of warm gold blooming. |
| 66 | "두 번째 봄은 첫 번째보다 늦게 와요." / "하지만 더 오래 가요." / "빨리 핀 꽃은 빨리 지지만," | 젖은 흙 위의 작은 봉긋 (싹이 뚫기 직전) | 손 없음 | 금. 봉긋 위에 금빛 점 하나 + 먹 흙선 | 하단 중앙 폭 12%. 여백 92% | A tiny rounded mound on a short ground line in black ink with one small warm gold dot at its top, a seed about to break through, small and low on an empty page. |
| 67 | ★★ "늦게 핀 꽃은 오래 가니까요." / 삼십 년 동안 첫 번째 봄만 알았다 / 두 번째 봄이 있다는 걸 | 마른 줄기에서 솟은 싹 한 줄기 (잎 둘) | 손 없음 (싹 하나만. 책 전체의 중심 이미지) | **금.** 싹 전체가 금빛 선. 아래 마른 줄기는 먹선으로 남음 (금이 먹을 덮지 않음) | 중앙 하단, 싹 높이 30%. 글은 상단. 여백 88% | A single new sprout with two small leaves rising from a dry black ink stem, the sprout drawn entirely in fine warm gold line, alone at the lower center of a vast empty cream page, the pivotal image of the book. |
| 68 | 아무도 알려주지 않았다 / 오늘 집에 가면 내일이라고 말하지 않을 것이다 / 물을 주기에 늦은 날은 없다 | 작은 싹 하나 + 위에서 내려오는 물 한 줄 | 손 1 — 물뿌리개를 싹 위에서 살짝 기울임 | 금. 싹은 금빛, 물줄기는 가는 먹선이 금빛 끝에서 닿음 | 물뿌리개 상단, 싹 하단, 사이는 물줄기. 글은 중간 띠. 여백 85% | An elderly hand tilting a small watering can slightly at the top, one thin black line of water falling to a small sprout drawn in warm gold at the bottom, cropped at the wrist, small. |
| 69 | 오늘이 아니면 내일도 없으니까. / 네 번째 만남 — 깨진 항아리 (제목 병기, 선만) | 없음 — 선과 여백만 | 손 없음 | 금. 금빛 헤어라인 한 줄이 오른쪽 바깥으로 나가다 중간에서 가는 균열 한 줄로 갈라짐 (3부 예고) | 하단 3분의 1 높이. 여백 96% | One warm gold hairline running across a vast empty cream page toward the right edge and splitting midway into a single tiny black crack, nothing else. |

---

## 3부. 금이 가고 꺼진 것들 — p.70 ~ p.87 (18쪽)
「네 번째 만남 — 깨진 항아리」 + 「다섯 번째 만남 — 꺼진 가로등」. 선: 금(먹과 공존) + 실땀. 금빛이 본격 사용되는 부(18쪽 중 9쪽). 손 5쪽.

| p. | 텍스트 | 그 페이지의 사물 | 손 유무 및 동작 | 선의 상태 | 구도·여백 | 영문 프롬프트 |
|---|---|---|---|---|---|---|
| 70 | 골목을 걷다가 낮은 담 너머로 / 작은 마당이 보였다 / 의자 옆에 항아리가 놓여 있었다 | 금이 여기저기 간 항아리 (아직 검은 균열) | 손 없음 | 먹·해빙. 균열이 검은 가는 선. 항아리 아래 바닥선 왼쪽에서 들어옴 | 하단 중앙 폭 28%. 여백 85% | A single round ceramic jar covered in thin black ink crack lines, small and low on a short ground line entering from the left edge, empty space above. |
| 71 | 금이 여기저기 가 있었다 / 금이 간 자리가 / 금빛으로 빛나고 있었다 | 균열 한 줄 (항아리 표면 일부의 클로즈업) | 손 없음 | **금.** 균열 한 가닥이 검은 선에서 금빛으로 바뀜. 먹 테두리는 남음 | 중앙 폭 30%. 여백 85% | A close-up fragment of a jar's curved surface in black ink with one crack line filled in warm gold, small at center on an empty cream page. |
| 72 | 의자에 앉은 사람이 / 금이 간 자리를 손으로 쓸어보고 있었다 | 항아리 어깨 부분과 금빛 금 | 손 1 — 손끝으로 금을 쓸어봄 | 금. 손가락이 지나간 자리에 금빛이 반짝임 | 중앙 폭 32%. 여백 82% | An elderly hand gently stroking its fingertips along a gold-filled crack on the shoulder of a jar, cropped at the wrist, the gold line glinting faintly under the fingers, small at center. |
| 73 | "버리지 않으셨네요." / "처음 깨졌을 때는 버리려고 했어요." / "그런데 금으로 이어 붙였더니" | 깨진 조각 두 개를 금실땀으로 이어 붙인 자리 | 손 1 — 두 조각을 맞대어 누름 | **실 + 금.** 갈라진 틈을 촘촘한 금빛 실땀이 잇는다 | 중앙 폭 28%. 여백 85% | An elderly hand pressing two broken pottery shards together, cropped at the wrist, the seam between them joined by tiny evenly spaced gold stitches like fine embroidery, small at center. |
| 74 | "깨진 자리가 무늬가 됐어요." / "이 항아리에서 가장 아름다운 곳이" / "가장 많이 다친 곳이에요." | 금빛 무늬가 전면에 퍼진 항아리 | 손 없음 | 실 + 금(전면). 금빛 균열선이 무늬처럼 항아리 전체에 | 중앙 폭 35%. 여백 80% | A single jar whose entire surface is covered in an intricate network of gold-filled cracks stitched like embroidery, outlined in fine black ink, small at center. |
| 75 | 이 몸에도 금이 가고 있었다 / 매끈한 게 잘 산 거라고 생각했다 / 아니었다 | 손등의 주름 (손 자체가 대상) | 손 1 — 손등을 내려다보듯 편 손 (책에서 손이 사물이 되는 유일한 페이지) | 금. 손금·주름 몇 줄이 항아리의 금과 같은 모양으로 금빛 | 중앙 폭 35%. 여백 78% | The back of a weathered elderly hand cropped at the wrist, its deep creases drawn in black ink and a few of them traced in fine warm gold like the gold-filled cracks of a jar, small at center. |
| 76 | "새 항아리는 매끈해요." / "이 항아리는 깨져봤어요." / "비를 맞아봤어요." | 금 간 항아리 입구 위로 떨어지는 빗방울 몇 점 | 손 없음 | 금. 금빛 균열 + 먹 빗방울 점선 | 중앙 폭 28%. 여백 85% | The upper part of a cracked jar with gold-filled cracks, a few small black ink raindrops falling toward its mouth, small at center. |
| 77 | "무거운 것을 담아봤어요." / 담 너머로 항아리가 보였다 / 금빛 무늬가 햇볕에 빛나고 있었다 | 낮은 담 위로 보이는 금빛 항아리 윗부분 | 손 없음 | 금. 이 부에서 가장 밝은 금빛. 균열의 금이 가는 광선처럼 몇 가닥 밖으로 번짐. 담은 수평선 하나 | 중앙 하단 폭 30%. 여백 82% | The top half of a gold-cracked jar peeking above one low wall line, a few fine warm gold rays radiating from its cracks, small at lower center, black ink otherwise. |
| 78 | 다섯 번째 만남 — 꺼진 가로등 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹. 가는 수직선 끝에 닫히지 않은 작은 빈 원 (가로등을 암시) | 바깥쪽(좌) 하단 구석. 여백 97% | One tall hairline vertical black line topped by a tiny unfilled circle, small in the lower left corner of a vast empty cream page, nothing else. |
| 79 | 걸음이 느려지고 있었다 / 보는 것이 많아지면 발이 느려진다 | 길가의 작은 들꽃 한 송이 | 손 없음 | 먹. 줄기 곡선이 부드러움. 바닥선이 오른쪽으로 | 하단 중앙 폭 10%. 여백 92% | A single small wildflower on a thin stem in fine black ink, tiny and low on the page, one short ground line running off the right edge. |
| 80 | 골목은 어두워지고 해는 기울고 있었다 / 골목 끝에 가로등이 하나 서 있었다 / 불이 꺼져 있었다 | 꺼진 전구 하나 + 그 아래 풀 한 포기 | 손 없음 | 먹. 전구 안 필라멘트에 촘촘한 빗금(어두움), 아래 풀은 곧음 | 전구 상단 중앙 폭 12%, 풀 하단 중앙 폭 5%, 글은 그 사이 띠. 여백 90% | One unlit light bulb drawn in black ink with dense hatching inside its glass, small in the upper center, and one tiny blade of grass at the bottom center, empty paper between them. |
| 81 | 가로등 근처 조그만 가게 앞에 / 누군가 등을 기대고 / 눈을 감고 앉아 있었다 | 벽에 기대 세워둔 낡은 빗자루 | 손 없음 | 먹. 벽 모서리 수직선 하나에 빗자루 사선 | 하단 중앙 폭 12%. 여백 88% | A worn straw broom leaning against one vertical wall edge line, thin black ink, small and low on the page. |
| 82 | "잠이 드신 건가요?" 노인이 눈을 떴다 / "아뇨. 기다리는 거예요." / "뭘요?" | 문에 걸린 팻말의 뒷면 (무늬 없음) | 손 없음 | 먹. 팻말을 매단 짧은 줄 | 상단 중앙 폭 15%. 여백 90% | A small blank shop sign hanging from a short cord with its back side showing, no letters, thin black ink, small in the upper center. |
| 83 | "이 골목을 걸어가는 사람을요." / "가게가 문을 닫고, 가로등도 꺼졌어요." / 나도 꺼진 가로등 같았다 (긴 글) | 꺼진 가로등 기둥 전체 (아주 가는 선) | 손 없음 | 먹. 기둥 수직선 + 머리의 빈 원. 정보량을 줄인 가장 단순한 선 | 하단 바깥쪽(우), 높이 22%. 상단은 글과 빈 밤. **여백 95%** | One very thin unlit streetlamp post with an empty circle at its top, tiny at the lower right of a vast empty cream page, black ink only. |
| 84 | 골목을 둘러봤다 / 빈 골목이었다 / 고양이가 담 위를 걷고 있었다 | 담 위를 걷는 고양이 (붓 실루엣, 눈 없음) | 손 없음 | 먹. 담 위 수평선 위를 걸음. 왼쪽에서 들어온 담선 | 하단 중앙 폭 22%. 여백 88% | A single small cat silhouette walking along a thin wall line, spare ink brushwork with no eye detail, tail up, small and low, wall line entering from the left edge. |
| 85 | "아무도 없는 건 아닌 것 같은데요." / "저건 손님 아닌가요." / "손님만 비추는 게 가로등인가요?" | 벽에 붙은 낡은 스위치 (꺼짐) | 손 1 — 검지로 스위치를 가리킴, 닿지 않음 | 먹. 손끝과 스위치 사이의 작은 틈 | 하단 중앙 폭 22%. 여백 88% | An old wall light switch in the off position, an elderly index finger pointing at it without touching, cropped at the wrist, thin black ink, small and low at center. |
| 86 | ★ 그 사람이 스위치를 올렸다 / 불이 켜졌다 / 고양이의 눈이 빛났다 | 스위치와 켜진 전구, 어둠 속 금빛 눈 두 점 | 손 1 — 스위치를 위로 올리는 접촉 순간 | **금(책 전체에서 가장 밝음).** 전구에서 12가닥 이내의 금빛 가는 방사선. 눈 두 점도 금 | 전구 상단 중앙, 손과 스위치 하단, 눈 두 점은 중간 왼쪽에 작게. 글은 중간 띠. 여백 82% | An elderly hand flipping a wall switch upward at the lower center, above it one light bulb now glowing with about a dozen fine warm gold hairline rays, and two tiny gold dots like cat eyes small at the left, cropped hand, black ink otherwise. |
| 87 | 손님은 오지 않았다 / 하지만 골목이 숨을 쉬기 시작했다 | 켜진 전구 + 그 아래 금빛 풀 한 포기 (p.80과 같은 구도) | 손 없음 | 금. 방사선이 짧고 부드럽게 잦아듦. 풀 끝에 금빛 | 전구 상단, 풀 하단 (p.80과 같은 위치). 여백 90% | The same one light bulb now lit with short soft warm gold rays at the upper center, and one tiny blade of grass at the bottom with a touch of gold at its tip, empty paper between them. |

---

## 4부. 심고 세는 것들 — p.88 ~ p.119 (32쪽)
「여섯 번째 만남 — 마지막 씨앗」 + 「마지막 만남 — 별을 세는 밤」. 선: 먹 → 금(별빛) → 실(전화가 이어짐). 손 13쪽. ★★ 두 번째 전환점 p.116(전화를 누름).

| p. | 텍스트 | 그 페이지의 사물 | 손 유무 및 동작 | 선의 상태 | 구도·여백 | 영문 프롬프트 |
|---|---|---|---|---|---|---|
| 88 | 여섯 번째 만남 — 마지막 씨앗 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹. 점 하나와 그쪽으로 뻗다 만 짧은 선 | 바깥쪽(좌) 하단 구석. 여백 97% | One tiny black ink dot with a short hairline reaching toward it and stopping just short, in the lower left corner of a vast empty cream page, nothing else. |
| 89 | 가로등 불빛을 뒤로하고 걷다보니, / 골목어귀에 좁은 텃밭이 있었다 / 사람 하나 겨우 쪼그려 앉을 만한 땅 | 좁은 흙 한 뙈기 (작은 직사각형 안에 고랑 빗금) | 손 없음 | 먹. 경계 사각형과 고랑 몇 줄 | 하단 중앙 폭 22%. 여백 88% | One small narrow rectangle of tilled soil drawn as a black ink outline with a few furrow lines inside, tiny and low at center. |
| 90 | 할머니가 쪼그려 앉아 있었다 / 손을 꼭 쥐고 있었다 / "뭘 들고 계세요?" | 꼭 쥔 주먹 | 손 1 — 무언가를 품은 채 펴지 않은 주먹 (노인의 손) | 먹. 주먹을 감싸듯 도는 짧은 곡선 | 중앙 하단 폭 22%. 여백 88% | A very old hand clenched into a small tight fist holding something unseen, cropped at the wrist, one short curved line wrapping around it, small at lower center. |
| 91 | 할머니가 천천히 손을 펼쳤다 / 작은 씨앗 하나가 손바닥 위에 있었다 | 씨앗 하나 (극소) | 손 1 — 손바닥을 펴 보임 | **금.** 씨앗 한 점만 금빛. 손금은 먹 | 하단 중앙, 손바닥 폭 30%. 여백 85% | An open weathered palm cropped at the wrist, its fine lines in black ink, at its center one impossibly tiny seed rendered as a single warm gold dot. |
| 92 | "마지막 씨앗이에요." / "심으면 더 이상 심을 게 없어요." / "그리고 이 좁은 데에 심어서" | 씨앗 하나 (혼자, 손 없이) | 손 없음 | 먹. 씨앗 둘레에 흐릿하게 맴도는 원 하나 (망설임) | 중앙 폭 5%. 여백 96% | One tiny seed in black ink alone at the center of a vast empty cream page, one faint uncertain circular line hovering loosely around it. |
| 93 | "뭐가 되겠어요." / 텃밭을 봤다. 좁았다 / 하지만 흙은 흙이었다 | 한 줌의 흙 (틈으로 흘러내림) | 손 1 — 흙 한 줌을 쥔 손 | 먹. 흙알갱이 짧은 획 | 하단 중앙 폭 28%. 여백 85% | An elderly hand holding a small handful of soil with grains falling between the fingers, cropped at the wrist, short irregular black ink marks for the soil, small and low. |
| 94 | "이 마을에 들어올 때 큰 나무를 봤어요." / "그 나무도 처음에는 이만한 자리에서 시작했을 거예요." / "씨앗은 밭의 크기를 모르니까요." | 그루터기 단면의 나이테 | 손 1 — 검지가 한가운데 작은 원(시작점)을 가리킴 | 먹. 동심원이 바깥으로 갈수록 성기게 | 중앙 폭 35%. 여백 78% | A cross-section of a tree stump showing concentric growth rings in fine black ink, one elderly index finger touching its tiny center ring, cropped at the wrist, small at center. |
| 95 | "그 나무를 심은 사람은 그늘을 봤을까요?" / "봤을 거예요." / 나도 볼 수 있을까 | 땅 위의 나뭇잎 그림자 얼룩 (그늘) | 손 없음 | 먹. 잎 모양 빗금 얼룩 몇 점 | 하단 중앙 폭 30%. 여백 88% | A small patch of dappled leaf-shaped shadow on the ground drawn as a few fine hatched leaf shapes, low at center, black ink only. |
| 96 | 그런 생각을 처음 했다 / "무릎이 안 굽혀져서요." / "좀 파주시겠어요?" | 흙 위에 파기 시작한 짧은 고랑 | 손 1 — 맨손으로 흙을 긁음 (도구 없음) | 먹. 고랑 시작선 | 하단 중앙 폭 25%. 여백 85% | An elderly bare hand with curled fingers scratching into soil, cropped at the wrist, one short furrow line just beginning beneath it, small and low. |
| 97 | 내가 흙을 팠다 / 할머니가 씨앗을 넣었다 / 흙은 같이 덮었다 | 씨앗이 들어가 닫히는 고랑 | 손 1 — 흙을 덮는 손 | 먹. 고랑선이 둥글게 닫힘 | 하단 중앙 폭 25%. 여백 85% | An elderly hand smoothing soil closed over a furrow, cropped at the wrist, the furrow line closing into a gentle curve, small and low at center, black ink only. |
| 98 | 씨앗은 이미 보이지 않았다 / 흙이 업고 있었다 / 바람은 불고 웃고 있었다 | 평평히 다져진 흙 위의 작은 봉긋 | 손 없음 | 먹. 가볍게 스치는 바람 곡선 한 줄 | 하단 중앙 폭 20%. 여백 90% | One small smooth mound of soil on a ground line with one light breezy curved line drifting above it, black ink only, small and low. |
| 99 | 마지막 만남 — 별을 세는 밤 (제목만) | 없음 — 선과 여백만 | 손 없음 | 먹. 완만한 능선 곡선 한 줄과 위쪽 작은 점 하나 | 곡선 하단, 점 상단 바깥쪽(우). 여백 97% | One long gentle curved line low on a vast empty cream page and one tiny dot high above it at the right, nothing else. |
| 100 | 할머니의 작은 텃밭을 지나니 골목이 끝났다 / 마을 끝에 작은 언덕이 있었다 / 올라서니 | 돌계단 세 칸 | 손 없음 | 먹. 각진 계단선이 위로 갈수록 부드러워짐. 오른쪽 위로 이어짐 | 하단 바깥쪽(우) 폭 28%. 여백 88% | Three worn stone steps rising toward the right drawn in fine black ink, the lines growing softer higher up, small at the lower right. |
| 101 | 걸어온 마을이 내려다보였다 / 멈춘 시계탑. 빈 둥지. 반쪽 꽃밭. 금빛 항아리. 켜진 가로등 | **예외 페이지.** 작은 아이콘 다섯이 일렬 — 시계 바늘, 빈 둥지, 마른 꽃대, 금 항아리, 전구 (각 폭 6~8%) | 손 없음 | 먹 + 금 소량 (항아리의 금 간 자리, 전구 광선만 금빛). 얇은 수평선 하나가 다섯을 꿰어 오른쪽으로 | 중앙 하단, 전체 폭 60%. 글은 상단. 여백 90% | Five tiny icons in a row along one thin horizontal line — two clock hands, an empty nest, a dry stem, a cracked jar with gold cracks, a small lit bulb with a few gold rays — each about six percent of the page width, black ink with gold only on the jar and bulb. |
| 102 | 씨앗이 묻힌 텃밭 / 해가 지고 있었다 / 그림자가 아주 길어졌다 / 해가 낮을 때 | 씨앗이 묻힌 작은 흙 봉긋 + 길게 늘어진 그림자 한 줄 | 손 없음 | 먹. 그림자가 과장되게 긴 대각선 한 줄, 안쪽 6% 앞에서 끝남 | 봉긋 하단 바깥쪽(좌), 그림자는 오른쪽 위로. 여백 92% | One small mound of soil at the lower left with one impossibly long thin diagonal shadow line stretching from it across the page and ending well before the right edge, black ink only. |
| 103 | 그림자는 가장 크다 / 언덕 꼭대기에 아이가 앉아 있었다 / 별이 하나 떴다 | 별 하나 (점 + 가는 십자 빛살) | 손 없음 | **금.** 별이 금빛 헤어라인. 아래에 먹 곡선(언덕) 한 획 | 상단 바깥쪽(우) 폭 6%, 글은 하단. **여백 96%** | One single small star rendered as a warm gold dot with fine cross-shaped gold hairlines at the upper right of a vast empty cream page, one soft black curve low at the bottom. |
| 104 | "별을 세는 거야?" / "네." / "왜?" "예쁘니까요." | 별 하나 | 손 1 — 검지 하나가 별을 가리키며 셈 (작게) | 금. 별과 손끝 사이 가는 금 점선 | 별 상단, 손 하단, 사이는 점선. 글은 중간 띠. 여백 92% | One small elderly hand with a single index finger raised toward one tiny warm gold star high above it, joined by a very faint dotted gold line, cropped at the wrist, small figure at the bottom of a vast empty page. |
| 105 | "세는 데 이유가 필요해요?" / 이유가 필요하지 / 그렇게 말하려다 멈추었다 | 별 두 개 | 손 없음 | 먹. 별 둘과 점선 모두 먹 (계산하려는 순간 금빛이 잠시 꺼짐). 점선이 중간에서 끊김 | 상단 중앙 폭 25%. 여백 92% | Two tiny stars in black ink at the upper center with a faint dotted line between them that stops halfway, empty paper below. |
| 106 | 걸을 때도 어디로 가는지 먼저 정했다 / 앉을 때도 왜 앉는지 먼저 생각했다 / 쉴 때도 이유를 찾았다 | 접힌 지도 한 장 (경로선만, 글자 없음) | 손 1 — 지도를 반듯이 눌러 펴는 손 | **먹·냉으로 의도적 회귀.** 1부 같은 각진 경로선 (계획하는 버릇의 차가움) | 중앙 폭 30%. 여백 82% | An elderly hand pressing flat a folded paper map that shows only a rigid angular route line and no lettering, cropped at the wrist, cold sharp black ink, small at center. |
| 107 | 이 아이는 이유 없이 별을 세고 있었다 / 예쁘니까 / 그게 전부였다 | 제멋대로 흩어진 작은 별 셋 | 손 없음 | 금. 별끼리 이어진 선이 없음 (계획 없음) | 상단에 흩어짐, 각 폭 4%. 여백 96% | Three tiny warm gold stars scattered loosely across the upper part of an empty cream page with no lines connecting them. |
| 108 | "저 별빛은 언제 떠난 빛이야?" / "오래전이요." / "몇 년, 몇십 년." | 별 하나 + 별에서 뻗어 내려오는 매우 긴 가는 선 | 손 없음 | 금. 별에서 화면 아래 바깥쪽까지 사선으로 뻗은 헤어라인 (거리) | 별 상단(안쪽 6% 확보), 선은 오른쪽 아래로. 여백 94% | One small warm gold star in the upper part of the page with one extremely long thin gold hairline running diagonally from it to the lower right, nothing else. |
| 109 | "그럼 지금 우리가 보는 빛은 옛날에 출발한 빛이네." / "네." | 사선을 따라 흐르는 작은 빛 알갱이 다섯 점 | 손 없음 | 금. 점 간격이 도착 쪽으로 갈수록 좁아짐 | 사선 배치, 폭 45%. 여백 94% | Five tiny warm gold light dots travelling in a diagonal line toward the lower left, spaced closer together as they arrive, on an empty cream page. |
| 110 | "그때 그 별은 알았을까." / "몰랐을 거예요." / "그냥 빛나고 있었을 거예요." | 방향 없이 빛나는 별 하나 | 손 없음 | 금. 짧은 빛살이 사방으로, 어디로도 향하지 않음 | 중앙 폭 8%. 여백 95% | One small warm gold star at the center of a vast empty cream page radiating very short fine gold hairlines in every direction, pointing nowhere in particular. |
| 111 | 삼십 년 동안 매일 걸었던 길 / 매일 만났던 사람들 / 매일 건넸던 손 / 그때는 그게 다인 줄 알았다 | 손잡이가 닳은 서류가방 (p.10과 같은 가방) | 손 없음 | 먹. 가방 아래 바닥선에 같은 짧은 획이 촘촘히 반복 (매일) | 하단 중앙 폭 22%. 여백 88% | The same worn leather briefcase with a scuffed handle, small and low at center, a ground line beneath it made of many identical short repeated ink ticks, black ink only. |
| 112 | 그때는 몰랐다. 그게 빛인 줄 / 알았다면 달랐을까 / … 알아도 그렇게 살았을 것이다 | 닳은 열쇠 하나 (삼십 년 쓴 가게 열쇠) | 손 1 — 열쇠를 쥐고 내려다봄 | 먹 + 금 옅게. 열쇠 날의 닳은 모서리에만 옅은 금 | 중앙 하단 폭 22%. 여백 88% | An elderly hand holding a single worn old key, cropped at the wrist, black ink line with a faint touch of warm gold along its worn edges, small at lower center. |
| 113 | 지금 여기 앉아 있는 것도 / 어딘가에서는 빛이 되고 있을까 | 땅 위의 작은 금빛 점 하나 (별이 아니라 "여기") | 손 없음 | 금. 점 둘레에 아주 가는 링 하나. 아래 짧은 먹 바닥선 | 하단 중앙 폭 5%. 여백 96% | One tiny warm gold dot with one very faint ring around it resting on a short black ground line, alone at the bottom center of a vast empty cream page. |
| 114 | 전화기를 꺼냈다 / 하루 종일 조용했다 / 울려야만 빛이 나는 게 아니었다 | 화면이 꺼진 전화기, 테두리에 금빛 | 손 1 — 전화기를 조용히 쥠 | 금. 전화기 테두리만 금 헤어라인. 화면은 빗금(꺼짐) | 중앙 하단 폭 25%. 여백 85% | An elderly hand holding a dark mobile phone whose screen is filled with fine hatching, its outline drawn in a thin warm gold line, cropped at the wrist, small at lower center. |
| 115 | 연락처를 열었다 / 지나친 이름이 있었다 / "전화하면 되잖아요?" | 전화기 화면 속 이름 막대 (p.51/52와 같은 구도) | 손 1 — 검지가 이름 위에서 멈춤 (p.51보다 틈이 좁음) | 금. 이름 막대가 금빛 (p.51의 먹과 대응) | 중앙 폭 28%. 여백 85% | A phone screen showing one short horizontal bar like a written name drawn in warm gold, an elderly index finger hovering very close above it, cropped at the wrist, the gap smaller than before. |
| 116 | ★★ 이번에는 눌렀다 / 신호음이 하나. / 둘. | 전화기 화면 위 한 점 + 퍼지는 신호 파동 | 손 1 — 검지가 화면을 정확히 누르는 접촉 순간 | **금(최대).** 접촉 지점에서 헤어라인 동심원이 번짐. 가장 바깥 원은 프레임 안에서 옅어져 사라짐 (책등 쪽 여백 유지) | 손·전화기 중앙 하단, 파동은 반지름 최대 폭 38%. 글은 최하단 띠. 여백 75% | An elderly index finger pressing firmly onto a phone screen at the exact moment of contact, cropped at the wrist, from that point thin warm gold concentric hairline circles ripple outward and fade before the page edges, nothing else. |
| 117 | 셋. / 멀리서 — 아주 멀리서 — / "여보세요?" | 귀 높이로 든 전화기 + 멀리 이어지는 금빛 실 | 손 1 — 전화기를 귀 높이로 듦 (얼굴 없음) | **실 + 금.** 전화기에서 출발한 금빛 실땀이 바깥(오른쪽) 위쪽의 아주 작은 점까지 이어짐 (연결) | 손 하단 중앙, 실 끝점은 오른쪽 상단. 여백 88% | An elderly hand raising a plain mobile phone to ear height, cropped at the wrist, a fine gold thread of tiny stitches running from the phone to a tiny distant dot in the upper right, small hand at the bottom. |
| 118 | 별이 하나 더 떴다 | 별 두 개 (p.103의 별 + 새로 뜬 별) | 손 없음 | **실 + 금.** 두 별 사이를 금빛 실땀 한 줄이 잇는 (p.105의 끊긴 점선과 대응) | 상단 중앙 폭 25%. 여백 94% | Two small warm gold stars at the upper center joined by one short line of tiny gold stitches, empty paper below. |
| 119 | 긴 말은 없었다 | 내려놓은 전화기 (화면이 옅게 밝음) | 손 없음 | 금. 전화기 위 짧은 곡선 한 획, 고요히 | 하단 중앙 폭 22%. 여백 92% | A plain mobile phone lying quietly with its screen faintly lit, one short calm curved warm gold line above it, small and low on an empty cream page. |

---

## 5부. 나란히 — p.120 ~ p.133 (14쪽)
「나가는 길」 + 공원 벤치 재회 + 「작가의 말」. 선: 온. **손은 p.126에서 둘, 그 뒤로는 사라지는 방향.** 손 4쪽. ★★★ p.126(손 둘), p.132(사물이 사라지고 꽃이 핀 선).

| p. | 텍스트 | 그 페이지의 사물 | 손 유무 및 동작 | 선의 상태 | 구도·여백 | 영문 프롬프트 |
|---|---|---|---|---|---|---|
| 120 | 나가는 길 (제목만) | 없음 — 선과 여백만 | 손 없음 | 금 + 먹, 온. p.2의 선과 같은 궤적이 돌아오되, 이번에는 부드럽게 휘고 금빛이 섞임 | 선은 하단 3분의 1 높이, 왼쪽에서 들어와 중앙에서 끝남. 여백 97% | One gently curving line blending black ink and warm gold entering from the left edge and ending near the center of a vast empty cream page, echoing an earlier straight line, nothing else. |
| 121 | 언덕을 내려왔다 / 마을을 빠져나왔다 / 이정표를 지났다 | 이정표 (p.20의 그 기둥, 뒤에서 본 모습) | 손 없음 | 금. p.20에서 지워졌던 자리가 금빛으로 채워짐 | 하단 중앙, 높이 35%. 여백 88% | The same old wooden signpost seen from behind, small and low on the page, the worn faded part of its board now traced in warm gold, black ink otherwise. |
| 122 | 시계가 멈춘 마을. 돌아보니 마을이 없었다 / 대신 낯익은 것들이 보였다 / 눈이 바뀌면 같은 길도 다른 길이 된다 (긴 글) | 접힌 안경 하나 | 손 없음 | 금. 렌즈 가장자리 한 줄만 금빛 | 하단 중앙 폭 22%. 글이 길므로 위쪽 전부 글 자리. 여백 90% | A single pair of folded eyeglasses lying on the page, thin black ink line with one lens rim traced in warm gold, small at lower center. |
| 123 | 집으로 가는 길에 공원이 있었다 / 매일 지나치던 공원 / 오늘은 들어갔다 | 열리는 철문 한 짝 (창살 세 개) | 손 1 — 문을 밀어 여는 손 | **온.** 먹선이 이 책에서 처음으로 굵고 끝이 둥글어짐 | 중앙 폭 28%, 문은 바깥쪽(우)으로 열림. 여백 85% | An elderly hand gently pushing open one iron park gate with three slim bars, the gate swinging toward the right, cropped at the wrist, soft round-ended black ink lines, small at center. |
| 124 | 벤치에 누군가 앉아 있었다 / 아주 오래전의 얼굴이 / 지금의 주름 위에 겹쳐 보였다 | 빈 벤치 (윤곽이 두 번 겹침 — 먹 하나, 금 하나, 살짝 어긋남) | 손 없음 | 온·금. 겹친 두 윤곽선 | 하단 중앙 폭 35%. 여백 85% | A single empty park bench drawn twice in slightly offset outlines, one in black ink and one in warm gold, small and low at center. |
| 125 | 이름을 불렀다 / 그 사람이 고개를 들었다 / 내 이름을 불렀다 | p.60의 끊어졌던 실의 두 끝이 거의 닿음 | 손 1 — 한쪽 실 끝을 쥐고 있음 | **실 + 금.** 실 끝 사이 간격이 p.60의 6분의 1 | 하단 중앙 폭 40%. 여백 88% | A weathered hand pinching one end of a thread whose other end hangs just a tiny gap away from it, cropped at the wrist, the thread rendered in warm gold stitches, small and low at center. |
| 126 | ★★★ 오래간만이었다 / 갈 곳이 없는 사람 둘이 / 나란히 앉는 것은 / 세상에서 가장 자연스러운 일이다 | 벤치 나무판의 모서리 + 두 손 사이의 금빛 실땀 | **손 2 — 책 전체에서 유일.** 나란히 놓인 두 손, 한 뼘 간격, 닿지 않음 | 실 + 금. 두 손 사이 바닥을 금빛 실땀 한 줄이 이음 (손이 닿는 대신 선이 잇는다) | 중앙 하단, 벤치 포함 폭 42%. 여백 80% | Two weathered elderly hands resting side by side on the edge of a wooden bench plank, cropped at the wrists, a hand's width apart and not touching, a short line of tiny warm gold stitches joining the space between them, small at lower center. |
| 127 | 전화기를 꺼내지 않았다 / 시간을 묻지 않았다 / 바람이 불었다 | 엎어 놓은 손목시계 | 손 없음 | 온·금. 바람 곡선이 시계 위를 스침 | 하단 중앙 폭 20%. 여백 90% | A wristwatch lying face-down on the page with its strap open, a soft warm gold wind curve passing above it, small and low, black ink otherwise. |
| 128 | 나뭇잎이 흔들렸다 / 그림자가 나란히 길어졌다 / "내일도 올 거야?" "갈 데가 있어야 안 오지." | 매달린 나뭇잎 한 장 + 나란한 긴 그림자 두 줄 | 손 없음 | 온·금. 평행한 두 금빛 선이 끝에서 살짝 가까워짐 | 잎 상단, 두 선 하단. 글은 중간 띠. 여백 88% | One hanging leaf at the upper center and below it two long parallel warm gold lines whose ends draw very slightly closer together, nothing else on the page. |
| 129 | 둘 다 웃었다 / 시계가 멈춘 마을은 멀리 있지 않았다 / 여기였다 | p.1의 6시에 멈춘 바늘 두 개 위에 나뭇잎 한 장이 얹힘 | 손 없음 | 금. p.1의 냉한 바늘이 같은 자리에서 금빛, 끝이 둥글어짐 (p.1의 대칭) | 상단 중앙 폭 30% (p.1과 같은 위치). 여백 90% | The same two clock hands frozen at six o'clock, now drawn in warm gold with softly rounded tips, one small leaf resting across them, small in the upper center. |
| 130 | 다만 바빠서 보이지 않았을 뿐 / 오래 달리면 왜 달리는지 잊는다 / 멈추면 비로소 묻는다 | 가지런히 벗어 놓은 구두 한 켤레 (p.11의 그 구두) | 손 없음 | 온. 먹선이 굵고 둥긂. 금 없음 (금을 아낌) | 하단 중앙 폭 28%. 여백 88% | One pair of worn leather dress shoes set neatly side by side seen from above, warm soft round-ended black ink lines, small and low at center. |
| 131 | 나는 누구였는가 / 이번에는 천천히 / 이번에는 곁을 보면서 | 열린 채 비어 있는 서류가방 (p.10의 그 가방) | 손 1 — 손잡이에서 손가락이 떨어지는 순간 (놓음). p.10과 대칭 | 온. 굵고 둥근 먹선. 금 없음 | 하단 중앙 폭 28%. 여백 85% | An elderly hand just releasing the handle of an open empty leather briefcase, cropped at the wrist, warm soft black ink lines, small and low at center. |
| 132 | ★★★ 더 이상 / 늦었다고 생각하지 않았다 / 두 번째 봄이 오고 있었다 | 없음 — 사물이 사라지고 꽃이 핀 선만 | 손 없음 | 금·온. p.2에서 시작한 주선이 굵고 둥근 곡선이 되어 위로 오르며, 위에 작은 꽃 3~5송이 (크기가 서로 다름). 왼쪽에서 들어와 오른쪽 안쪽 여백 앞에서 끝남 | 선은 하단 3분의 1에서 완만히 오름. **여백 90%** | One gently rising curved warm gold line entering from the left edge of a vast empty cream page, on it three to five small delicate flowers of different sizes in bloom, nothing else. |
| 133 | 작가의 말 (산문 전체) | 없음 — 마지막 꽃 한 송이만 | 손 없음 | 금. p.132의 선 끝이 조금 이어져 꽃이 활짝 핀 한 송이 | 하단 바깥쪽(우) 구석에 아주 작게. 글이 페이지 대부분. 여백 97% | One tiny fully bloomed flower on a very short warm gold line in the lower right corner of an otherwise empty cream page, nothing else. |

---

## 6. 공통 영문 프롬프트 접두어

최종 프롬프트 = **CORE** + (손 있는 페이지면 **HAND**) + (금빛 있는 페이지면 **GOLD**) + 표의 페이지 프롬프트.

**CORE**
```
Minimalist adult literary art-book illustration, fine black ink pen and brush linework on warm cream ivory paper with subtle paper grain, one single subject drawn small and precisely, at least 70 percent of the page left as empty paper, no background, no scenery, no ground shadow, no full figure, no face, black ink only, quiet sober mood for mature readers, not cute, not childlike, square 1:1 composition, keep every element at least 6 percent away from the frame edges except a thin line that deliberately runs off the outer edge, no text, no letters, no numbers.
```

**HAND** (손 등장 43쪽만)
```
Exactly one hand of a person in their sixties, close-up and cropped at the wrist, thick knuckles, visible tendons, age spots, short blunt nails, drawn in the same ink line as the object, never smooth or young, no arm, no body.
```
(p.126만: "Exactly two hands" 로 바꿔서 사용)

**GOLD** (금빛 41쪽만)
```
Add one accent of warm muted matte gold, used only as thin hairlines or tiny dots on the elements named in the prompt, like gold leaf on paper, not glossy, no metallic gradient, no glow fill.
```

**THREAD** (실 7쪽: p.60 73 74 117 118 125 126)
```
Thread rendered as tiny evenly spaced stitches like fine hand embroidery.
```

### 부정 프롬프트 (모든 페이지에 함께)
```
no children's book style, no cute cartoon characters, no rounded playful shapes, no bright saturated colors, no colors other than black and warm gold, no gradients, no watercolor wash, no photorealism, no background scenery, no ground shadow, no full body figures, no faces, no second hand, no arm, no smooth young hands, no clutter, no decorative border, no text, no letters, no numbers, no logos, no watermark
```
(p.126은 "no second hand" 를 "no third hand" 로 바꿔서 사용)

**표지**: 이 문서는 본문 133쪽만 다룬다. 표지는 본문 스타일 확정 후 별도 (`/cover`). 표지 후보는 p.1의 멈춘 바늘 또는 p.67의 싹이 본문 시스템과 그대로 이어진다.

---

## 7. 기존안(art-direction.md, 손과 선) 대비 달라진 점

| 항목 | v1 손과 선 | v2 사물 + 여백 + 선 |
|---|---|---|
| 페이지의 주인공 | 133쪽 전부 손 | **그 페이지 텍스트에 나오는 사물** (시계 바늘, 전화기, 문손잡이, 빈 그릇, 둥지, 물뿌리개, 항아리, 전구, 씨앗, 별, 벤치 등) |
| 손 | 133쪽(100%) | **43쪽(32.3%).** 쥐고·놓고·만지고·누르는 순간에만 |
| 원고의 강한 이미지 | 대부분 버림 (손이 시계·물뿌리개 등을 흉내만 냄) | 멈춘 시계, 빈 둥지, 반쪽 마른 꽃밭, 금빛 항아리, 꺼진 가로등, 흙에 묻히는 씨앗, 별, 벤치를 **사물로 복원** |
| 구도 원칙 | 손 + 선, 여백 70% | **사물 하나 + 여백 70% 이상.** 장면(배경·인물·하늘) 없음 |
| 반복 소진 | 같은 모티프 133회 | 사물이 부마다 바뀜. 반복은 의도된 메아리만 (p.1↔35↔129 바늘, p.10↔111↔131 서류가방, p.11↔130 구두, p.51↔52↔115 이름 막대, p.60↔125 끊어진 실, p.80↔87 전구와 풀, p.20↔121 이정표) |
| 선 | 페이지마다 손과 함께 | **책 전체를 잇는 주선.** p.2에서 시작해 p.120에서 돌아오고 p.132에서 꽃이 핀다. 냉→해빙→금→온 4단계와 홀짝 이음 규칙 |
| 선 재질 3종 | 먹선/금박/실 | 계승. 실은 7쪽으로 정리 (끊어진 실 p.60 → 이어짐 p.125·126의 호응 추가) |
| 금빛 | 약 30쪽 | 41쪽. 별(4부)이 금빛 사물로 들어와 늘었다. 5부는 14쪽 중 11쪽. p.130·131은 일부러 금 없이 굵은 먹으로 아낌 |
| 손이 둘 | p.126~132 내내 두 손 | **p.126 한 곳만.** 이후에는 손이 없거나 하나 (p.131 놓는 손) |
| 손이 사라짐 | p.132 (손이 투명해짐) | 손은 p.131이 마지막. **p.132는 사물마저 사라지고 꽃이 핀 선만** (사용자 지시 반영) |
| 장 제목 9쪽 | 손 없이 선 하나 | 동일하게 선과 여백만. 각 장의 사물을 선 한 획으로만 암시 |
| 책등 방향 | 홀짝과 맞지 않는 곳이 있었음 | 홀수=책등 왼쪽, 짝수=책등 오른쪽으로 통일, 바깥쪽 표기도 홀짝에 맞춤 |
| 프롬프트 접두어 | 모든 페이지에 "손 1개 + 선 1개" 고정 | 손·금빛·실을 모듈로 분리. 손 없는 페이지에 손이 끼어들지 않음 |

---

## 8. 저자 확인 필요
1. 새·고양이를 붓 실루엣으로 그릴지, 깃털·발자국 같은 흔적만 남길지 (p.39 41 42 47, p.84). 실루엣이 이야기는 더 잘 전달, 흔적만 그리면 아동서 위험이 더 낮음.
2. p.104의 별을 세는 손가락: 60대의 손 유지(일관성) vs 아이의 가는 손가락(원고에 더 충실하지만 아동서 느낌 위험).
3. p.67 싹: 손 없이 싹 하나(현재안) vs 손바닥 위에서 싹이 솟는 안.
4. p.101 아이콘 5개(사물 하나 원칙의 유일한 예외)를 허용할지.
5. p.69: 제목 전용으로 처리했으나 본문 한 줄("오늘이 아니면 내일도 없으니까.")이 함께 있음.
6. 금빛 41쪽(30.8%)을 유지할지, 30쪽대로 줄일지.
7. 스타일 고정 시험(0-8) 7쪽을 먼저 생성해 보고 진행할지.
8. `illustration-spec.md`는 여전히 "손과 선" 콘셉트를 유지하라고 적고 있음. 승인 후 갱신 필요 (이 작업에서는 수정하지 않음).

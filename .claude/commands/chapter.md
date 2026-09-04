---
description: 한 장 제작 — 사실 확인 → 초안 → 교정 → 보고. 인자: 책 폴더명 장번호
---
대상: $ARGUMENTS
1. 해당 책 폴더 전부 읽기. brief가 미확정이면 중단하고 /new-book 안내. 직전 장이 final이 아니면 중단하고 "직전 장을 먼저 확정해 주세요" 안내(사용자가 건너뛰겠다고 하면 notes에 기록 후 진행).
2. researcher 위임(A) → facts.md 갱신.
3. writer 위임(장 초안) → chapters/chNN.md (draft).
4. editor 위임(A·B·C) → reviewed + 변경 목록 + 모순 목록.
5. outline 상태 "교정", notes 기록.
6. 보고 형식으로. "확정"이라고 하면 status: final, outline final로 바꾸고 다음 장 안내. 수정 요청이면 writer에게 반영시킨 뒤 editor 재검토.

# 연구 로드맵 / 데이터 수집 계획

업데이트: 2026-11-14. 완료하지 않은 수집 작업은 **계획**으로만 기록합니다.

| 단계 | 작업 | 산출물 | 상태 | 완료 조건 |
|---|---|---|---|---|
| 1 | 연구계획서 전사·연구질문·변수 확정 | docs/research_proposal_transcription.md, docs/methodology.md | 완료 | 원본 연구 범위 유지 |
| 2 | 2009–2018 연도별 구단 최초 선발 인원 예비 데이터 정리 | data/raw, data/processed | 예비 집계 완료 | 자료별 원표 KBO 1차 자료로 교차검증 |
| 3 | 투표 마감일·투표 마감 전 경기 시점 찾기 | data/templates/standings_at_deadline.csv | 미수집 | 10개년 날짜+출처 및 기준 명시 |
| 4 | 연도×구단 승률·순위 수집 (마감 직전) | team standings dataset | 미수집 | 90개 구단×연도에 시점, 승률, 순위, 출처 기록 |
| 5 | 2014–2018 팬 득표 최종 원표·합산 명단 수집 | data/templates/fan_vs_weighted_position.csv | 미수집 | 리그×포지션 전수, 동률·예외 처리 |
| 6 | 구단별 관중 누계·집계 기준 확보 | data/templates/attendance_by_team.csv | 미수집 | 동일 시점 기준 및 원본 URL 기록 |
| 7 | 팬만 적용 시 가상 명단 vs 실제 합산 선발 비교 | scripts/ + results/ | 미분석 | 해마다 지표 비교, 변경 포지션과 팀 기록 |
| 8 | 성적·관중 변수 고려 및 감도 분석 | results/ | 미분석 | 주요 교란·규칙 차이·표본 수 한계 검토 |
| 9 | 논문 본문 10–12쪽 작성 및 발표 준비 | paper/ | 미작성 | 출처가 있는 모든 수치 재대조 |

## 우선순위

**1순위: 데이터 출처 검증 → 2순위: 팬 단독 vs 합산 결과 → 3순위: 당시 팀 승률·순위 → 4순위: 관중 자료 → 5순위: 논문.**

### 데이터 병합 키

- 구단×연도: `year + team_id` (예비 집계, 승률, 관중)
- 포지션별 비교: `year + league + position`
- 선택적으로 선수: `year + player_name + team_id + position` (동명이인 주의)

GitHub Issues를 열어 각 작업의 자료 출처·검증 상태·완료 조건을 기록합니다.

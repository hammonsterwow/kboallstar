# 연구 범위 확대안: 2009–2026

> 2026-11-14 제안·확인 사항. 사용자 연구계획서 원본(2009–2018)은 변경하지 않고 **추가 분석 범위**만 기록합니다. 기존 2009–2018 예비 집계도 그대로 유지하며, 신규 연도 원자료 확보 전까지 확장 분석 결과를 주장하지 않습니다.

## 확대 연구 질문

팬 투표 100%에서 팬 70% + 선수단 30%로 변경된 뒤 올스타 베스트 선발의 구단별 대표성이 어떻게 변화했는가? 그 경향이 2026년까지 유지되는가?

## 분석 기간·대상

| 구분 | 연도 | 선정 방식 | 주 분석 포함 | 근거 |
|---|---|---|---|---|
| 변경 전 | 2009–2013 (5개년) | 팬 투표 100% | 예 | 원 연구계획서 |
| 변경 후 1 | 2014–2019 (6개년) | 팬 70% + 선수단 30% | 예 | 2019 KBO 결과 원표 https://www.koreabaseball.com/Schedule/Allstar/News.aspx?bdSe=7446 |
| 팬 단독 특수 시기 | 2020 (1개년) | 팬 투표만, 실제 올스타전 없음 | 별도 분석 | https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=7845 |
| 팬 단독 특수 시기 | 2021 (1개년) | 팬 투표만, 실제 올스타전 없음 | 별도 분석 | https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=8124 |
| 변경 후 2 | 2022–2026 (5개년) | 팬 70% + 선수단 30% | 예 | 2022 KBO 투표 재개 https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=8384 |
| 최신 확인 | 2026 | 팬 70% + 선수단 30% | 예 | 최종 발표(2026-06-24) https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=12005 |

**주 분석: 총 16개년 (이전 5, 이후 11). 보조 분석: 2020–2021 (2개년). 전체 조사 범위: 18개년.**

## 왜 예외 시기를 별도로 다루는가

2020~2021년에는 올스타전 자체는 열리지 않았지만 KBO는 팬 투표를 시행하고 베스트12를 발표했습니다. 다만 선수단 투표를 실시하지 않았으며, 팬 참여·경기 진행 일정 모두 팬데믹 영향을 받았습니다. 따라서 2014년 이전의 통상적 팬 100%와 **동일한 처치집단으로 간주하지 않음**. 별도의 '코로나 특수 팬 단독' 집단으로 분류합니다.

## 분석 계획

1. 원계획의 구단별 최초 **투표 선발** 인원, 대표성 폭, 인원 표준편차를 2009–2026에 대해 계산. 감독 추천·부상 대체 인원은 포함하지 않음.
2. 2014–2019 및 2022–2026 각각의 연도에 대해 **동일 관측 팬 투표 단독 가상 명단 vs 실제 70:30 명단**을 리그·포지션별로 재구성하여 대표성 변화 계산. 이 비교는 규칙 비교이며 팬 행동의 반사실까지 추정하지 않음.
3. 2020–2021 팬 단독 결과는 별도 표로 기술하고 코로나 특수조건을 논의.
4. 투표 종료 전 마지막 완료 경기 기준 **구단 승률·순위**, 구단별 관중을 병합하고 당해 기준 시점·시즌 경기수와 출처 기록.
5. 구단 수·베스트 선발 정원·포지션 체계·투표 플랫폼 및 세부 자격 변경을 확인. 절대 표준편차뿐 아니라 대표성 비율, 정원 보정 지표(CV), 집중도(HHI)를 함께 제시.
6. 2026 최종 KBO 발표는 팬 투표 70%·선수단 투표 30%와 포지션별 득표 표를 제공하므로 원자료 수집 출발점으로 사용.
7. 도입 전 5개 연도, 도입 후 11개 연도는 **불균형한 표본**이며 연도별 시대적 변화와 팬덤 변동이 얽혀 있습니다. 단순 전후 평균 차이는 인과효과가 아님.

## 자료 스키마 확장

- `year` (2009~2026)
- `selection_rule`: `fan_100_pre2014` / `fan_70_players_30` / `fan_100_pandemic`
- `allstar_game_held`: true / false
- `fan_vote_close_datetime`, `as_of_game_date`
- `team_id`, `season_team_name`, `league`, `position`
- `fan_votes`, `player_votes`, `weighted_score`, `official_winner`
- `team_win_pct_at_cutoff`, `team_rank_at_cutoff`, `cumulative_attendance_at_cutoff`
- `source_url`, `verification_status`, `notes`

## 선행 자료 및 공식 링크

- [2019 KBO 최종 투표 자료](https://www.koreabaseball.com/Schedule/Allstar/News.aspx?bdSe=7446)
- [2020 KBO 팬 투표 베스트12](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=7845)
- [2021 KBO 팬 투표 베스트12](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=8124)
- [2022 선수단 투표 재개 공지](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=8384)
- [2023 KBO 베스트12](https://www.koreabaseball.com/Schedule/Allstar/Game/Main2023.aspx)
- [2024 KBO 베스트12](https://www.koreabaseball.com/Schedule/Allstar/Game/Main2024.aspx)
- [2025 KBO 베스트12](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=11553)
- [2026 KBO 최종 공식 발표·후보별 결과표](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=12005)

## 실행 작업

- [ ] 2009–2018 기존 예비 수치 공식 원본 검증
- [ ] 2019 및 2020–2026 최초 선발 구단별 자료 확장
- [ ] 2014–2019, 2022–2026 팬 단독 vs 합산 데이터 구축
- [ ] 18개년 투표 마감일과 기준일별 성적 수집
- [ ] 주요 비교 16개년 + 특수 기간 2개년 분리 분석
- [ ] 기존 10~12쪽 소논문 구조를 유지하되 자료량·논의 조정

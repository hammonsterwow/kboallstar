# 데이터 대장

## 현재 포함된 파일

| 경로 | 단위 | 상태 | 설명 |
|---|---|---|---|
| raw/allstar_initial_selections_preliminary_2009_2018.csv | 연도 × 구단 (wide) | **예비·검증 필요** | 기존 10개년 엑셀에서 전사한 최초 투표선발 인원, 출처 URL 포함 |
| processed/team_year_preliminary.csv | 구단 × 연도 (long) | **예비·검증 필요** | 회귀/시각화에 적합한 90행, 0명 팀 포함 |
| processed/yearly_metrics_preliminary.csv | 연도 (10행) | **예비·기술통계** | 대표성 비율·표준편차·CV·HHI |
| templates/standings_at_deadline.csv | 구단 × 연도 | **빈 템플릿** | 투표 종료 전 순위·승률·날짜 수집 |
| templates/fan_vs_weighted_position.csv | 연도 × 리그 × 포지션 | **빈 템플릿** | 팬 단독 1위 vs 최종 합산 1위 |
| templates/attendance_by_team.csv | 구단 × 연도 | **빈 템플릿** | 관중 통제변수 |

## 중요

- CSV의 `preliminary` 상태는 숫자를 외부 원문과 대조하지 않았다는 의미입니다.
- 0명인 참가 팀은 **0**, 미참가 팀은 **빈 칸**입니다. 절대 합치지 마세요.
- `HEROES`는 연도별 구단 공식 명칭과 다른 **분석용 고정 식별자**입니다. 최종 수집 때 연도별 공식 구단명을 별도 표로 보존하세요.
- 날짜/승률/관중/득표 템플릿의 빈 행은 '자료가 없다'는 뜻이지 '0'이라는 뜻이 아닙니다.
- 연도별 집계에 원본 링크를 남겼지만 일부는 보도 기사입니다. 가능하면 KBO 원표로 대체하고 원기사도 기록합니다.

### 기본 실행
```bash
python3 scripts/analyze_preliminary.py
```

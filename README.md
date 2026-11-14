# KBO All-Star Voting & Club Representation

**KBO 올스타 투표 방식 변화와 구단별 대표성 (2009–2018)**

> Status: **Research in progress / Preliminary data** (2026-11-14)
> 이 저장소의 10개년 집계는 **예비 분석**입니다. 원본 출처 재대조, 팬 투표 단독 명단 재구성, 통제변수 수집을 거친 뒤 최종 논문에 사용합니다.

## 2026년까지 연구 범위 확대 (2026-11-14)

**추가 연구 계획:** 전체 조사 2009–2026년. 주요 비교는 2009–2013 (팬 투표 100%, 5년) vs 2014–2019 및 2022–2026 (팬 70% + 선수단 30%, 11년)이며 2020–2021 팬 단독 투표는 코로나19 특수 사례로 별도 분석합니다.

- [확장 연구 설계 및 1차 공식 근거](docs/extension_2009_2026.md)
- [2019–2026 자료 수집 작업](https://github.com/hammonsterwow/kboallstar/issues/7)

**아래 2009–2018 수치는 기존 예비 연구 결과이며, 2026 확장 분석 결과가 아닙니다.** 연구계획서 원본 및 기존 예비 데이터는 변형하지 않습니다.

## 연구 질문

> 팬 투표 100% 방식에서 **팬 70% + 선수단 30%** 방식으로 전환한 이후, 투표로 최초 선발된 올스타의 **구단별 대표성**이 높아지고 편중이 완화되었는가?

- **독립변수:** 투표 방식 (2009–2013: 팬 100%, 2014–2018: 팬 70% + 선수단 30%)
- **종속변수 1:** 대표성의 폭 = 1명 이상 배출 구단 / 해당 연도 참가 구단
- **종속변수 2:** 구단별 선발 인원 모집단 표준편차 (선발 0명 팀 포함)
- **분석 대상:** 팬/합산 투표로 **최초 선발된 베스트 선수만**. 감독 추천·부상 대체 제외
- **보조 지표:** 변동계수(CV), HHI
- **추가 통제 검토:** 투표 마감 당시 승률·순위, 관중 규모, 참가 구단 수, 선발 정원
- **핵심 검증:** 2014–2018년 각 연도 **동일 후보군의 팬 단독 1위 명단**과 **합산 결과 명단** 비교

## 예비 결과 (확정 아님)

| 지표 | 2009–2013 | 2014–2018 |
|---|---:|---:|
| 평균 대표성의 폭 | 71.1% | 82.0% |
| 평균 구단별 선발 인원 표준편차 | 2.65명 | 2.10명 |
| 평균 HHI | 0.266 | 0.186 |

이 표는 연도별 **기술통계**이며, 제도 변경의 **인과효과를 입증하지 않습니다**. 2013년 NC, 2015년 KT 참가로 구단 수가 바뀌고 투표선발 정원도 20→22→24로 바뀝니다. 제도 변경에 따른 자기 구단 투표 제한도 별도로 검토해야 합니다.

## 저장소 구성

```text
README.md
docs/
  research_proposal_transcription.md   # 연구계획서 내용 전사 (개인정보 제외)
  methodology.md                       # 변수, 분석 설계, 한계
  paper_outline.md                     # 10~12쪽 논문 목차 초안
  research_roadmap.md                   # 단계별 계획·완료 기준
  research_log.md                       # 연구 결정 및 변경 기록
  literature.md                         # 선행연구 및 인용 검증 목록
data/
  README.md
  raw/allstar_initial_selections_preliminary_2009_2018.csv
  processed/team_year_preliminary.csv
  processed/yearly_metrics_preliminary.csv
  templates/standings_at_deadline.csv
  templates/fan_vs_weighted_position.csv
  templates/attendance_by_team.csv
sources/source_registry.csv
scripts/analyze_preliminary.py
.gitignore
```

### 재현 실행

Python 3 표준 라이브러리만 필요합니다.

```bash
python3 scripts/analyze_preliminary.py
```

실행 시 `results/`에 연도별 집계와 전후 요약이 만들어집니다. 원본 CSV는 수정하지 않습니다.

## 연구 자료와 검증 원칙

1. `data/raw/`의 현재 CSV는 **이전 예비 엑셀에서 전사한 값**입니다. 각 행에 해당 연도의 URL과 재검증 상태가 포함되어 있습니다.
2. 최종 선발 명단은 KBO 1차 자료를 우선 사용하고, 보도 자료는 보조·교차검증에 사용합니다.
3. 팬 단독·합산 비교를 할 때 **리그/포지션, 해당 연도의 선발 인원 규칙, 동일 후보 풀**을 유지합니다.
4. 투표 당시 구단 순위는 **팬 투표 마감 전 마지막으로 완료된 경기일** 기준으로 수집하고, 원본 순위 화면/URL·조회일을 남깁니다.
5. 관중 수는 팬 규모의 **대리변수(proxy)**이지 실제 투표 참여자 수가 아닙니다.
6. 기존 DOCX/PDF/XLSX 바이너리 파일은 이 초기 커밋에 포함하지 않았습니다. 연구계획서 내용과 예비 엑셀 데이터는 편집·버전관리가 쉬운 Markdown/CSV로 별도 전사했습니다.

## 연구 진행

[로드맵](docs/research_roadmap.md) · [연구계획서](docs/research_proposal_transcription.md) · [방법론](docs/methodology.md) · [원자료 출처 대장](sources/source_registry.csv) · [GitHub Issues](https://github.com/hammonsterwow/kboallstar/issues)

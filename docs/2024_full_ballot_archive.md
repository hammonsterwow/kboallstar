# 2024년 KBO 올스타 최종 후보 120명 득표수 전수 검증

## 원본
- 기존 50명 원표(유격수·외야수·DH)에 사용자가 추가로 보낸 70명 원표(선발/중간/마무리·포수·1B·2B·3B)를 합병했습니다.
- [KBO 공식 발표](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=10091), [사용자 제공 원표가 실린 기사](https://www.topstarnews.net/news/articleView.html?idxno=15507818).
- 전체 팬 3,227,578표, 선수단 322표, 2024년 6월 16일 투표 마감.

## 검증
- 120명 각각 **팬 득표, 선수단 득표, 공식 총점** 보존.
- 공식 총점 = 70 * 팬 득표 / 3,227,578 + 30 * 선수단 득표 / 322. **120명 전원 소수 둘째자리 반올림 범위 내 일치**.
- 기존 전사에서 재게시 숫자가 잘못됐던 드림 선발투수 **김광현 537,556표**, 나눔 3루수 **송성문 247,546표**를 사용자가 보낸 원본 이미지 및 점수로 확인하여 입력.
- 팬 100%와 실제 70:30 선발 변경 **5개**.

| 리그·포지션 | 팬 100% | 실제 70:30 |
|---|---|---|
| D CP | 김원중 (LOTTE) | 오승환 (SAMSUNG) |
| D 3B | 김영웅 (SAMSUNG) | 최정 (SK) |
| N SP | 양현종 (KIA) | 류현진 (HANWHA) |
| N C | 김태군 (KIA) | 박동원 (LG) |
| N OF | 소크라테스 (KIA) | 도슨 (HEROES) |

| 지표 | 팬 100% | 실제 70:30 |
|---|---:|---:|
| 대표 구단 | 7/10 | 8/10 |
| 표준편차 | 3.072458 | 2.244994 |
| HHI | 0.263889 | 0.187500 |

- 선발 24명, 실제 구단별: SK 2, DOOSAN 3, LOTTE 1, SAMSUNG 6, KIA 7, HEROES 2, LG 1, HANWHA 2, NC 0, KT 0.
- 50명 부분 CSV는 이력용으로 보존하고 아래 120명 전수 CSV를 새로운 정본으로 사용합니다.

## 산출물
- [120명 전체 최종 득표 CSV](../data/raw/2024_final_all_120_candidate_votes.csv)
- [포지션별 팬/합산 비교](../data/processed/2024_fan_only_vs_weighted_positions.csv)
- [구단별 선발 비교](../data/processed/2024_team_comparison.csv)

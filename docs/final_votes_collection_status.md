# 개인별 최종 득표수 수집 현황 (2009–2026)

업데이트: 2026-11-14. 이 문서는 **후보별 정확한 최종 득표수 저장 여부**만 집계합니다. 투표 선발 명단, 구단별 선발 인원, 선발자 역전 횟수 및 총투표수 확인과는 다른 작업입니다.

| 상태 | 연도 |
|---|---|
| 후보 전원 최종 득표수 입력 | **2009–2019** |
| 일부 후보 최종 득표수 입력 | **2024 (50/120), 2026 (24/120)** |
| 개인별 최종 득표수 데이터 미입력 | **2020–2023, 2025** |

즉 **완료 11개년 + 부분 2개년 + 미입력 5개년**입니다. 일부 연도 KBO 공식 문서에 원표가 *존재하는 것*과 저장소에 후보별로 *전사된 것*을 구분합니다.

### 2019년 최종 득표수 120명 전수 검증

- [2019년 KBO 공식 원표 120명 팬·선수단 득표 CSV](../data/raw/2019_final_all_120_candidate_votes.csv) 및 [검산 보고서](2019_full_ballot_archive.md).
- [2019년 KBO 공식 원문](https://www.koreabaseball.com/Schedule/Allstar/News.aspx?bdSe=7446) — 팬 1,215,445표·선수단 343표, 후보 120명.
- 팬 단독 대비 실제 70:30에서 드림 유격수 **이학주(삼성) → 김재호(두산)**, 드림 지명타자 **정의윤(SK) → 페르난데스(두산)** 두 자리 역전. 대표 구단 **6→7개**.
- [2019 포지션별 선발 비교](../data/processed/2019_fan_only_vs_weighted_seats.csv) · [2019 구단별 선발 인원](../data/processed/2019_team_comparison.csv).

### 2018년 최종 득표수 120명 전수 검증

- [2018 후보 전원 팬·선수단 득표 CSV](../data/raw/2018_final_all_120_candidate_votes.csv) 및 [검산 보고서](2018_full_ballot_archive.md).
- 원본 이미지: [선발투수~3루수](https://drive.google.com/file/d/1KAc-fGYYBwDlAAZdf5kKhvGSQK9k0xAT/view) · [유격수~지명타자](https://drive.google.com/file/d/1naOvfIi_3xOnpKY-SnrhXwFKDYzmqN-p/view).
- 팬 총 841,693표·선수단 352표로 환산점수 전 후보 검산. 나눔 6개 자리 변경으로 대표 구단 5→7개, 인원 표준편차 3.639→2.871.
- [2018 팬 단독 vs 실제 24자리 선발 비교](../data/processed/2018_fan_only_vs_weighted_seats.csv) 및 [구단별 선발 인원](../data/processed/2018_team_comparison.csv).

### 2016년 후보 120명 전수 검증

- [2016년 최종 120명 전체 팬·선수단 득표 CSV](../data/raw/2016_final_all_120_candidate_votes.csv) — 사용자 제공 최종 결과 이미지 2장에 기반해 전원 전사 및 공식 환산점수 검산.
- [2016년 팬 단독·실제 선발 비교](../data/processed/2016_fan_only_vs_weighted_seats.csv) / [구단별 선발 차이](../data/processed/2016_team_comparison.csv) / [검증 보고서](2016_full_ballot_archive.md).
- 드림 외야수 **박건우(두산) → 김문호(롯데)** 1건 역전; 팬 100% 6개 구단 → 실제 70:30 7개 구단 대표.
- [원본 이미지 1](https://drive.google.com/file/d/1BfUqunzbGxKzMKKNieUGSuyUYXtl0y1J/view) · [원본 이미지 2](https://drive.google.com/file/d/1pF9kAaFJNTtNkIRBmYyLy8NtyRiMKPim/view)

### 2017년 전수 확보 및 2024년 부분 확보

- [2017 최종 후보 120명 득표 및 선수단 득표·총점 CSV](../data/raw/2017_final_all_120_candidate_votes.csv) — [KBO 공식 최종 표](https://www.koreabaseball.com/Schedule/Allstar/News.aspx?bdSe=6667)에서 120명 전수 확인, 팬 2,123,872표·선수단 294표 환산 검산. 팬 단독 vs 70:30 24명 **전원 동일**. [상세 검증 기록](2017_full_ballot_archive.md).
- [2024 확인된 최종 후보 50명 CSV](../data/raw/2024_final_candidate_votes_partial_50.csv) — 사용자 제공 유격수·외야수·지명타자 원표만 전사. 공식 환산식 50명 검산. [원본 이미지](https://drive.google.com/file/d/1LWPamlAkdngyRbZTgGlroeQdFkGD8rqg/view), [부분 검증 기록](2024_partial_votes_archive.md). **전체 120명 중 나머지 70명의 득표는 미확보**.
- 2024 제공된 10개 선발 자리 중 나눔 외야수 1자리: 소크라테스(KIA) 팬 단독 우세, 실제 70:30에서는 도슨(키움) 당선. 나머지 미확보 포지션의 역전 결과는 이 50명 CSV만으로는 검증 불가.

### 2015년 신규 확보 자료

- [2015 후보 120명 전체 팬·선수단 득표수·총점 CSV](../data/raw/2015_final_all_120_candidate_votes.csv)
- [2015년 전체 최종 집계표 세 장의 원본 보관 내역 및 점수 검산](2015_full_ballot_archive.md)
- 팬 투표 2,337,036표, 선수단 346표로 120명 점수 재계산. 팬 단독 24명과 실제 70:30 24명 모두 동일(변경 0명), 최종 대표 구단 8/10.
- Google Drive 원본 이미지: [1](https://drive.google.com/file/d/1cH1UBifZC9YXbWvGw7usohkdDvsK6Kfy/view), [2](https://drive.google.com/file/d/1M3N7lpKgX5wv5BD5Oi6b_2APu0-nzObA/view), [3](https://drive.google.com/file/d/1rtq104kfVn4g-V9-f4ynAbRGZiqu_OaW/view).

### 2013년 신규 확보 자료

- [2013 후보 99명 최종 득표 CSV](../data/raw/2013_final_all_99_candidate_fan_votes.csv)
- 사용자 제공 [스타뉴스 게재 KBO 최종 집계표](https://www.starnewskorea.com/sports/2013/07/08/2013070809142484909) 및 [KBO 공식 최종 발표](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=5101)를 대조해 99명 전원 전사. [Google Drive 원본 이미지](https://drive.google.com/file/d/1KZV9tNuUbw1OzbQ-RVBdDwe3bioYaBhz/view).
- 총 유효투표 **2,217,846표**, 최다 득표 **봉중근(LG) 1,174,593표**, 실제 선발 **22명**. 웨스턴리그의 베스트11은 LG 선수 11명 독점.
- [2013년 최종 후보 득표 및 검증 기록](2013_final_vote_archive.md)

### 2012년 신규 확보 자료

- [2012 후보 80명 최종 득표 CSV](../data/raw/2012_final_all_80_candidate_fan_votes.csv)
- 사용자 제공 [최종 집계표 이미지](https://blog.naver.com/giddb83/161573002)를 80명 전수 전사. [Google Drive 보존 원본 PNG](https://drive.google.com/file/d/13bJlOSeuWsuF---281-orLE3dT3xVJz8/view).
- 총 유효투표 **1,721,475표**, 최다득표 **강민호(롯데) 892,727표**. 롯데 10명, KIA·LG 각 3명, 한화·넥센 각 2명 선발 검산.
- [2012 최종 득표 분석 및 출처 기록](2012_final_vote_archive.md)

### 2010년 신규 확보 자료

- [2010 후보 80명 최종 득표 CSV](../data/raw/2010_final_all_80_candidate_fan_votes.csv)
- 원본: [2010년 최종 집계표(사용자 제공 2장)](https://godlessjm.tistory.com/807). [원본 상단](https://drive.google.com/file/d/17WadeF6QjZxSYzZKslNrZOB3BgpzW291/view) / [원본 하단](https://drive.google.com/file/d/1SAZs8ibfkGpaY9xRhtHxM2tcJ6BFKeB8/view).
- 최다 득표 홍성흔(롯데) 818,269표, 다음 류현진(한화) 779,938표. 전체 80명 전사, 최초 선발 20명과 8개 구단 배분 검산 완료.
- 해당 표 이미지에 전체 유효투표수는 표시되어 있지 않아 별도 확인 이전까지 비워 두었습니다.

### 새로 입력한 자료

- [2011 팬 후보 80명 최종 득표 CSV](../data/raw/2011_final_all_80_candidate_fan_votes.csv)
  - 원문: [2011년 7월 11일 연합뉴스 최종 집계](https://go.seoul.co.kr/news/newsView.php?id=20110711800023).
  - 총 유효투표 1,623,576. 선수단 투표 해당 없음.
  - 리그별 각 10명, 총 20명 선발 결과가 삼성5 롯데4 SK1 KIA4 LG4 한화2 두산0 넥센0과 일치.
- [2009년 후보 80명 최종 득표수 전수 CSV](../data/raw/2009_final_all_80_candidate_fan_votes.csv)
  - **사용자가 직접 제공한 이미지 「2009 CJ마구마구 올스타전 베스트 10 인기투표 최종집계 결과」**에 실린 동·서군 80명 최종 득표수를 전수 전사하고 20명 선발 결과와 기존 구단별 인원을 대조했습니다. [조선일보 2009 최종 발표 기사](https://www.chosun.com/site/data/html_dir/2009/07/13/2009071300813.html)도 참고합니다.
  - 총 유효투표 1,401,532. 최종 후보 수 **80명 모두 숫자 확보**. 기존 부분 CSV의 김주찬 574,233 표기는 이미지에 따라 **574,603표로 정정**했습니다.
  - 80명 전수 이미지 원본을 기준으로 선발 20명 검산: 롯데 7, KIA 6, 두산 2, 히어로즈 2, SK·한화·LG 각 1, 삼성 0. 이전 10명 부분 CSV는 대조 이력용으로만 보존합니다.
  - 3~6차 **중간집계** 숫자는 최종값에 섞지 않음.

### 다음 데이터 채우는 방법

1. KBO 공식 최종 발표의 **후보 전원 득표표**를 찾기.
2. 연도/당시 리그/포지션/구단/선수명/정확한 팬 득표수/선수단 득표수(시행 당시만)/발표일/원문 URL 저장.
3. 리그별 선발 정원·외야수 3명 등을 감안해 동일 연도 실제 최초 선발과 재대조.
4. 한 연도의 후보 전원 및 공식 총 유효투표수·합산 산식까지 일치하면 `complete`로 변경.
5. 표의 중간 집계 여부/선발자 교체 여부/추천 선수 여부를 근거 없이 추정하지 말 것.

[연도별 CSV 상태 대장](../data/raw/final_individual_votes_completeness_2009_2026.csv)

> 후보 전체 표의 전사와 표에 인용된 제3자 보도 문장의 복사는 다릅니다. 저작물 본문을 옮기지 않고 선수명, 숫자, 정렬 키, 출처만 보관합니다.

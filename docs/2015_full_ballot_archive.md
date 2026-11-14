# KBO 2015년 올스타 팬/선수단 최종 득표 120명 전수표

최종 확인: 2026-11-14.

## 원본
- [KBO 공식 2015-07-06 최종 집계](https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=5974) — 팬 투표 총 2,337,036표, 선수단 총 346표, 120명 후보.
- [사용자가 제공한 2015 전체 득표표 이미지 3장](https://blog.naver.com/bjhplanner/220411489860?trackingCode=rss) — 각 후보 팬 득표·선수단 득표·총점.
- Google Drive 원본 이미지: [① 선발~1루수](https://drive.google.com/file/d/1cH1UBifZC9YXbWvGw7usohkdDvsK6Kfy/view), [② 2루수~유격수](https://drive.google.com/file/d/1M3N7lpKgX5wv5BD5Oi6b_2APu0-nzObA/view), [③ 외야수~지명타자](https://drive.google.com/file/d/1rtq104kfVn4g-V9-f4ynAbRGZiqu_OaW/view).

## 검증
- **120명 전원의 팬 득표·선수단 득표·공식 환산 점수** 전사 완료.
- 공식 점수 `70 × (개인 팬 득표 / 2,337,036) + 30 × (개인 선수단 득표 / 346)`과 **전 후보 120명 공식 점수**가 소수 둘째자리 반올림 오차 범위 이내 일치.
- 드림/나눔 각 12명(선발·중간·마무리투수, 포수, 1B·2B·3B·SS, 외야수 3명, DH).
- **팬 100% 가상 선발 24명과 실제 70:30 24명 동일(0명 변경).**
- 구단별 실제 선발: 삼성6, 한화4, 넥센3, NC3, SK2, 두산2, 롯데2, KIA2, LG0, KT0.
- 대표성 8/10=80%, 모집단 SD 1.685230, HHI 0.149306.

## CSV
- [전체 120명 팬·선수단·점수](../data/raw/2015_final_all_120_candidate_votes.csv)
- [포지션별 팬 전용과 실제 70:30 비교](../data/processed/2015_fan_only_vs_weighted_seats.csv)
- [개인별 득표 수집 상태](../data/raw/final_individual_votes_completeness_2009_2026.csv)

## 기존 연구 결과와 관계
2015년의 팬과 선수단이 일부 후보에 대해 다른 순위를 나타내더라도 최종 선발자 24명은 바뀌지 않았습니다. 제도 시행 후의 대표성 80%를 선수단 투표 도입으로 인한 선발 변경 효과로 오인하지 않도록 구분합니다. 기존 `2015_official_selected_24.csv`는 이전에 선발자만 정리한 이력 파일이고, 이번 **120명 CSV가 후보별 득표수 정본**입니다.

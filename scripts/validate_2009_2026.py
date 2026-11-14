#!/usr/bin/env python3
"""Validate KBO All-Star 2009–2026 annual, club and counterfactual outputs.

Source data:
  2009–2018 original preliminary CSV (historical primary-source audit still pending)
  2019–2026 official KBO yearly selected-club count CSV.
Comparison rules:
  fan-only roster = actual roster - KBO/press documented weighted-only winners
                                   + same-position fan-only winners.
The script checks internal consistency; it does not independently verify web sources.
"""
from pathlib import Path
from collections import defaultdict
import csv, math

ROOT=Path(__file__).resolve().parents[1]
TEAM_CODES=["SK","DOOSAN","LOTTE","SAMSUNG","KIA","HEROES","LG","HANWHA","NC","KT"]
TEAM_COLUMNS=["SK","두산","롯데","삼성","KIA","히어로즈·넥센","LG","한화","NC","KT"]

def read(path):
    with (ROOT/path).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

def source_counts(row):
    return {code:int(row[col]) for code,col in zip(TEAM_CODES,TEAM_COLUMNS) if row[col].strip()!=""}

def metrics(d):
    values=list(d.values())
    n=len(values); t=sum(values)
    assert n in (8,9,10) and t in (20,22,24)
    avg=t/n
    sd=math.sqrt(sum((v-avg)**2 for v in values)/n)
    return dict(n_teams=n,n_selections=t,represented=sum(v>0 for v in values),
        representation_rate=sum(v>0 for v in values)/n,
        population_sd=sd,cv=sd/avg,hhi=sum((v/t)**2 for v in values))

def check_metric(row,m):
    for k in ("n_teams","n_selections","represented"):
        assert int(row[k])==m[k], (row["year"],row.get("scenario"),k,row[k],m[k])
    for k in ("representation_rate","population_sd","cv","hhi"):
        assert abs(float(row[k])-m[k])<0.000002,(row["year"],row.get("scenario"),k)

def main():
    old=read("data/raw/allstar_initial_selections_preliminary_2009_2018.csv")
    new=read("data/raw/2019_2026_initial_team_counts_official.csv")
    source={int(r["year"]):source_counts(r) for r in old+new}
    assert set(source)==set(range(2009,2027))
    for y,d in source.items():
        assert len(d)==(8 if y<=2012 else 9 if y<=2014 else 10), y
        assert sum(d.values())==(20 if y<=2012 else 22 if y<=2014 else 24), y
    annual=read("data/processed/kbo_2009_2026_annual_representation.csv")
    assert len(annual)==18
    for row in annual:
        y=int(row["year"]); check_metric(row,metrics(source[y]))
        for k in TEAM_CODES:
            expected=source[y].get(k,"")
            assert str(row[k])==str(expected), (y,k)
    rev=read("data/processed/kbo_2014_2026_reversal_positions.csv")
    by_year=defaultdict(list)
    for r in rev:
        by_year[int(r["year"])].append(r)
    expected_years={2014,2015,2016,2017,2018,2019,2022,2023,2024,2025,2026}
    comparison=read("data/processed/kbo_2014_2026_fan_vs_weighted_metrics.csv")
    assert len(comparison)==22
    for row in comparison:
        y=int(row["year"])
        assert y in expected_years
        d=source[y].copy()
        if row["scenario"]=="fan_100_counterfactual":
            for r in by_year[y]:
                actual=r["actual_70_30_team"]; fan=r["fan_only_team"]
                assert d[actual]>0 and fan in d, (y,actual,fan)
                d[actual]-=1
                d[fan]+=1
        elif row["scenario"]!="actual_fan_70_player_30":
            raise ValueError("Unexpected scenario "+row["scenario"])
        check_metric(row,metrics(d))
        assert int(row["changed_selection_positions"])==len(by_year[y])
    print("Validation successful: 18 years, 22 scenario rows,",
        len(rev),"documented changed seats.")
    print("Note: validation of arithmetic is NOT a substitute for historical candidate-ballot verification.")

if __name__=="__main__":
    main()

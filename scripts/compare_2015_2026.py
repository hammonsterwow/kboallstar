#!/usr/bin/env python3
"""Recalculate 2015 actual and 2026 fan-only vs weighted representation.
2015 fan-only comparison deliberately left missing until 120 final candidate ballots verified.
"""
import csv,math
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
TEAMS=["DOOSAN","SAMSUNG","SSG","KT","KIA","HANWHA","LG","NC","LOTTE","KIWOOM"]
ALIAS={"SK":"SSG","NEXEN":"KIWOOM"}
def read(path):
    with (R/path).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def calc(team_ids):
    assert len(team_ids)==24
    c=Counter(team_ids)
    a=[c[t] for t in TEAMS]
    assert sum(a)==24
    sd=math.sqrt(sum((v-2.4)**2 for v in a)/10)
    return dict(represented=sum(v>0 for v in a),representativeness=sum(v>0 for v in a)/10,population_sd=sd,CV=sd/2.4,HHI=sum((v/24)**2 for v in a),counts=dict(zip(TEAMS,a)))
a=read("data/raw/2015_official_selected_24.csv")
b=read("data/raw/2026_official_selected_24.csv")
f=read("data/processed/2026_fan_only_vs_weighted.csv")
assert len(a)==len(b)==len(f)==24
for r in b:
    expected=70*int(r["fan_votes"])/4968276+30*int(r["players_votes"])/394
    assert abs(expected-float(r["weighted_score"]))<=0.015,r["player"]
assert sum(r["changed"]=="yes" for r in f)==6
c15=calc([ALIAS.get(r["club"],r["club"]) for r in a])
c26=calc([r["club"] for r in b])
cf26=calc([r["fan_club"] for r in f])
assert (c15["represented"],cf26["represented"],c26["represented"])==(8,6,8)
print("2015 actual:",c15)
print("2026 fan-only:",cf26)
print("2026 actual:",c26)
print("2026 changed seats: 6 / 24")
print("2015 fan-only: pending complete KBO 120-candidate source verification")

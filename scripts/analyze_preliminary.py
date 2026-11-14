#!/usr/bin/env python3
"""Recalculate PRELIMINARY KBO All-Star club-representation metrics.

Source: data/raw/allstar_initial_selections_preliminary_2009_2018.csv
No third-party Python dependencies. Run from any working directory.
This script verifies internal arithmetic, NOT the accuracy of historical source lists.
"""
from __future__ import annotations
import csv
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/raw/allstar_initial_selections_preliminary_2009_2018.csv"
OUT = ROOT / "results"
TEAM_COLS = ["SK","두산","롯데","삼성","KIA","히어로즈·넥센","LG","한화","NC","KT"]

def read_rows():
    with SRC.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            counts = [int(row[k]) for k in TEAM_COLS if row[k].strip() != ""]
            clubs = int(row["participating_clubs"])
            seats = int(row["initial_vote_seats"])
            if len(counts) != clubs:
                raise ValueError(f'{row["year"]}: clubs mismatch, {len(counts)} != {clubs}')
            if sum(counts) != seats:
                raise ValueError(f'{row["year"]}: total selections mismatch, {sum(counts)} != {seats}')
            if any(n < 0 for n in counts):
                raise ValueError(f'{row["year"]}: negative count')
            yield int(row["year"]), row["voting_rule"], clubs, seats, counts

def main():
    records = []
    for year, rule, clubs, seats, counts in read_rows():
        mean = seats/clubs
        sd = statistics.pstdev(counts)
        rep = sum(n > 0 for n in counts)/clubs
        hhi = sum((n/seats)**2 for n in counts)
        records.append({"year":year, "voting_rule":rule,
                        "clubs":clubs, "seats":seats,
                        "represented_clubs":sum(n>0 for n in counts),
                        "representation_rate":rep, "population_sd":sd,
                        "cv":sd/mean, "hhi":hhi})

    if len(records) != 10 or {r["year"] for r in records} != set(range(2009, 2019)):
        raise ValueError("Expected exactly the ten years 2009–2018")

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/"yearly_metrics.csv").open("w",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    groups = [("pre_2009_2013", [r for r in records if r["year"]<=2013]),
              ("post_2014_2018",[r for r in records if r["year"]>=2014])]
    with (OUT/"period_comparison.csv").open("w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["period","n_years","mean_representation_rate","mean_population_sd","mean_cv","mean_hhi"])
        for label, subset in groups:
            writer.writerow([label,len(subset)] +
              [statistics.mean(r[k] for r in subset) for k in
               ("representation_rate","population_sd","cv","hhi")])
    print("PRELIMINARY ONLY: source list verification and within-year fan-only comparison remain pending.")
    print(f"Wrote {OUT/'yearly_metrics.csv'} and {OUT/'period_comparison.csv'}")
    for label, subset in groups:
        print(label, "representativeness=",round(statistics.mean(r["representation_rate"] for r in subset),4),
              "sd=",round(statistics.mean(r["population_sd"] for r in subset),4))

if __name__=="__main__":
    main()

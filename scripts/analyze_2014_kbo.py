#!/usr/bin/env python3
"""Reproduce the 2014 KBO All-Star fan-only vs weighted ballot comparison.

Input: data/raw/2014_kbo_official_candidate_votes.csv
KBO source: https://www.koreabaseball.com/MediaNews/Notice/View.aspx?bdSe=5556
Standard-library Python only. No external dependencies.
This is an observed-ballot rule comparison, NOT a causal estimate.
"""
import csv
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/2014_kbo_official_candidate_votes.csv"
TEAMS = ("SAMSUNG", "DOOSAN", "LOTTE", "SK", "LG", "NEXEN", "NC", "KIA", "HANWHA")
POSITIONS = ("SP", "RP", "C", "1B", "2B", "3B", "SS", "OF", "DH")
FAN_BALLOTS = 1782008
PLAYER_BALLOTS = 291

def summarize(winners):
    counts = Counter(row["team_id"] for row in winners)
    vals = [counts[t] for t in TEAMS]  # Including zero-selected teams
    assert len(winners) == 22
    mean = 22 / len(TEAMS)
    sd = math.sqrt(sum((v - mean)**2 for v in vals) / len(TEAMS))
    return {
        "represented_clubs": sum(v > 0 for v in vals),
        "representation_rate": sum(v > 0 for v in vals) / len(TEAMS),
        "population_sd": sd,
        "cv": sd / mean,
        "hhi": sum((v/22)**2 for v in vals),
        "counts": counts,
    }

def main():
    with SOURCE.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 99
    assert sum(r["league"] == "E" for r in rows) == 44
    assert sum(r["league"] == "W" for r in rows) == 55

    for row in rows:
        row["fan_votes"] = int(row["fan_votes"])
        row["players_votes"] = int(row["players_votes"])
        row["official_weighted_score"] = float(row["official_weighted_score"])
        actual = 70 * row["fan_votes"] / FAN_BALLOTS + 30 * row["players_votes"] / PLAYER_BALLOTS
        assert abs(actual - row["official_weighted_score"]) <= 0.011, row["player"]

    fan_winners, weighted_winners = [], []
    for league in ("E", "W"):
        for pos in POSITIONS:
            candidates = [r for r in rows if r["league"] == league and r["position"] == pos]
            assert len(candidates) == (15 if (league == "W" and pos == "OF") else
                                       12 if (league == "E" and pos == "OF") else
                                       5 if league == "W" else 4)
            seats = 3 if pos == "OF" else 1
            fan_winners += sorted(candidates, key=lambda r: r["fan_votes"], reverse=True)[:seats]
            weighted_winners += sorted(candidates, key=lambda r: r["official_weighted_score"], reverse=True)[:seats]

    fan_ids = {(r["league"], r["position"], r["team_id"], r["player"]) for r in fan_winners}
    weighted_ids = {(r["league"], r["position"], r["team_id"], r["player"]) for r in weighted_winners}
    print("Candidates:", len(rows), "Seats:", len(fan_ids))
    print("Different selected player/position records:", len(fan_ids.symmetric_difference(weighted_ids)) // 2)
    print("Fan-only:", summarize(fan_winners))
    print("Weighted:", summarize(weighted_winners))
    assert fan_ids == weighted_ids, "Candidate lists do not match for 2014"
    assert summarize(weighted_winners)["counts"] == Counter({
        "SAMSUNG": 3, "DOOSAN": 4, "LOTTE": 2, "SK": 2,
        "LG": 1, "NEXEN": 3, "NC": 4, "KIA": 2, "HANWHA": 1
    })

if __name__ == "__main__":
    main()

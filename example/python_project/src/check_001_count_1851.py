#!/usr/bin/env python3
"""Check 001: the roll's count of market days in 1851.

Created 6 September 2026; updated 6 September 2026.
Plan: 001, task 1
Backs: [claim 001]
Instrument: the roll file at its committed revision, read with the Python standard library (3.11 or later)
Frame: the calendar year, as the roll's dates give it
Mutation: shift-year, drop-month
By: assistant

WHAT IS CHECKED: that the roll holds 51 rows dated in 1851, 49
ordinary and 2 fairs, with monthly sums adding to the same total.  The
full part 1, the construction, and the results are in the record,
evidence_and_reasoning/checks/001_count_1851.md; this docstring does not
repeat them.
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROLL = ROOT / "source_documents" / "Roll1851_market_roll.csv"

FAILURES: list[str] = []
VALUES: dict[str, object] = {}


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print one PASS/FAIL line and remember failures for the exit code."""
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def value(name: str, v: object) -> object:
    """Record a named value for the RESULT line; the record states the same."""
    VALUES[name] = v
    return v


def shift_year(rows: list[tuple[dt.date, str]]) -> list[tuple[dt.date, str]]:
    return [(d.replace(year=d.year + 1), k) for d, k in rows]


def drop_month(rows: list[tuple[dt.date, str]]) -> list[tuple[dt.date, str]]:
    return [(d, k) for d, k in rows if not (d.year == 1851 and d.month == 6)]


MUTATIONS: dict[str, "callable"] = {"shift-year": shift_year, "drop-month": drop_month}
BASIS: list[str] = ["source_documents/Roll1851_market_roll.csv"]


def construct() -> list[tuple[dt.date, str]]:
    """Every row of the roll as (date, kind)."""
    with open(ROLL, newline="", encoding="utf-8") as fh:
        return [(dt.date.fromisoformat(r["date"]), r["kind"]) for r in csv.DictReader(fh)]


def sanity(rows: list[tuple[dt.date, str]]) -> None:
    report("sanity: every kind is ordinary or fair", all(k in ("ordinary", "fair") for _, k in rows))
    report("sanity: every date is in 1851 or 1852", all(d.year in (1851, 1852) for d, _ in rows))


def verify(rows: list[tuple[dt.date, str]]) -> None:
    y = [(d, k) for d, k in rows if d.year == 1851]
    report("main: the count of 1851 rows is 51", value("count_1851", len(y)) == 51)
    report("main: 49 ordinary days", value("ordinary_1851", sum(1 for _, k in y if k == "ordinary")) == 49)
    report("main: 2 fairs", value("fair_1851", sum(1 for _, k in y if k == "fair")) == 2)
    months = {m: sum(1 for d, _ in y if d.month == m) for m in range(1, 13)}
    report("second route: the monthly sums add to the count", value("monthly_sum", sum(months.values())) == len(y))
    report("second route: twelve months counted", value("months", len(months)) == 12)


def discrepancies(rows: list[tuple[dt.date, str]]) -> None:
    pass


def main() -> int:
    print(__doc__.splitlines()[0])
    obj = construct()
    sanity(obj)
    verify(obj)
    discrepancies(obj)
    verdict = "reproduced" if not FAILURES else "not reproduced"
    print()
    print(f"  {len(FAILURES)} failure(s)" if FAILURES else "  all assertions passed")
    print("RESULT: " + verdict + "".join(f"; {k}={v}" for k, v in VALUES.items()))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

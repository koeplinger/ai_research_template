#!/usr/bin/env python3
"""Check 003: duplicated rows in the roll's 1851 entries (fails by design).

Created 6 September 2026; updated 6 September 2026.
Plan: 001, task 4
Backs: [claim 004]
Instrument: the roll file at its committed revision, read with the Python standard library (3.11 or later)
Frame: the calendar year, as the roll's dates give it
Mutation: duplicate-entry
By: assistant

WHAT IS CHECKED: that at least three rows of 1851 repeat an earlier row's
date and kind, which [claim 004] needs; the check reaches its failing
verdict, and the claim is ruled out.  The control plants one repeat in a
scratch list and shows it counted.  The full part 1, the construction,
and the results are in the record, evidence_and_reasoning/checks/003_duplicates.md;
this docstring does not repeat them.
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


def duplicate_entry(rows: list[tuple[dt.date, str]]) -> list[tuple[dt.date, str]]:
    first = [r for r in rows if r[0].year == 1851][:3]
    return rows + first


MUTATIONS: dict[str, "callable"] = {"duplicate-entry": duplicate_entry}
BASIS: list[str] = ["source_documents/Roll1851_market_roll.csv"]


def construct() -> list[tuple[dt.date, str]]:
    """Every row of the roll as (date, kind)."""
    with open(ROLL, newline="", encoding="utf-8") as fh:
        return [(dt.date.fromisoformat(r["date"]), r["kind"]) for r in csv.DictReader(fh)]


def count_duplicates(rows: list[tuple[dt.date, str]]) -> int:
    """The number of 1851 rows whose (date, kind) pair occurred earlier in the list."""
    seen, dup = set(), 0
    for r in rows:
        if r[0].year != 1851:
            continue
        if r in seen:
            dup += 1
        seen.add(r)
    return dup


def sanity(rows: list[tuple[dt.date, str]]) -> None:
    y = [r for r in rows if r[0].year == 1851]
    report("sanity: the rows of 1851 are 51 or more", value("rows_1851", len(y)) >= 51)
    distinct = list(dict.fromkeys(y))
    planted = distinct + distinct[:1]
    report("control: one 1851 row repeated in a scratch list of the distinct rows is counted as one duplicate",
           value("control_planted", count_duplicates(planted)) == 1)


def verify(rows: list[tuple[dt.date, str]]) -> None:
    report("main: at least three rows of 1851 duplicate an earlier row", value("duplicates_1851", count_duplicates(rows)) >= 3)


def discrepancies(rows: list[tuple[dt.date, str]]) -> None:
    if FAILURES:
        print(f"  the count of duplicated rows is {VALUES['duplicates_1851']}, not at least 3")


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

#!/usr/bin/env python3
"""Check 004: the weekdays of the roll's 1851 rows.

Created 6 September 2026; updated 6 September 2026.
Plan: 001, task 5
Backs: [claim 007]
Instrument: the roll file at its committed revision, read with the Python standard library (3.11 or later)
Frame: the calendar year, as the roll's dates give it; weekdays as the standard library's date arithmetic gives them
Mutation: shift-year, drop-month
By: assistant

WHAT IS CHECKED: that the 49 ordinary rows of 1851 fall on Tuesdays, the
2 fairs on Thursdays, the 51 rows on 51 distinct dates, and that 1851
has 52 Tuesdays of which three have no row.  The full part 1, the
construction, and the results are in the record,
evidence_and_reasoning/checks/004_weekdays.md; this docstring does not
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


def tuesdays_of_1851() -> list[dt.date]:
    """Every Tuesday of the calendar year 1851, by the standard library's weekday()."""
    first = dt.date(1851, 1, 1)
    return [first + dt.timedelta(i) for i in range(365) if (first + dt.timedelta(i)).weekday() == 1]


def sanity(rows: list[tuple[dt.date, str]]) -> None:
    y = [(d, k) for d, k in rows if d.year == 1851]
    report("sanity: the rows of 1851 number 51, as check 001 found", value("rows_1851", len(y)) == 51)
    report("sanity: every kind is ordinary or fair", all(k in ("ordinary", "fair") for _, k in y))
    report("sanity: the known case, 1 January 1851 is a Wednesday", dt.date(1851, 1, 1).weekday() == 2)


def verify(rows: list[tuple[dt.date, str]]) -> None:
    y = [(d, k) for d, k in rows if d.year == 1851]
    ordinary = [d for d, k in y if k == "ordinary"]
    fairs = [d for d, k in y if k == "fair"]
    on_tuesday = value("ordinary_on_tuesday", sum(1 for d in ordinary if d.weekday() == 1))
    report("main: 49 ordinary rows, every one a Tuesday", len(ordinary) == 49 and on_tuesday == 49)
    report("main: the two fairs fall on Thursdays",
           value("fair_weekdays", ",".join(d.strftime("%A") for d in fairs)) == "Thursday,Thursday")
    report("main: the rows of 1851 fall on distinct dates",
           value("distinct_dates_1851", len({d for d, _ in y})) == len(y) == 51)
    tuesdays = tuesdays_of_1851()
    report("main: 1851 has 52 Tuesdays", value("tuesdays_1851", len(tuesdays)) == 52)
    with_row = set(ordinary)
    report("control: the Tuesdays with an ordinary row are the 49 ordinary rows",
           value("tuesdays_with_row", sum(1 for t in tuesdays if t in with_row)) == 49)
    missing = [t for t in tuesdays if t not in with_row]
    report("negative: exactly three Tuesdays of 1851 have no row",
           value("tuesdays_without_row", ",".join(t.isoformat() for t in missing)) == "1851-02-04,1851-08-12,1851-12-30")


def discrepancies(rows: list[tuple[dt.date, str]]) -> None:
    if FAILURES:
        print(f"  {VALUES.get('ordinary_on_tuesday')} ordinary rows on Tuesdays; fairs on {VALUES.get('fair_weekdays')!r}; "
              f"Tuesdays without a row: {VALUES.get('tuesdays_without_row')!r}")


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

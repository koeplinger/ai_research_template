#!/usr/bin/env python3
"""Check 001: the roll's count of market days in 1851.

Created 20 November 2026; updated 20 November 2026.
Plan: 001, task 1
Backs: [claim 001]
Instrument: the held roll at its recorded checksum, read with the Python standard library, CPython 3.12.3
Frame: the calendar year, as the roll's dates give it, fixed by roll.in_year
Mutation: shift-year, drop-month, duplicate-entry, relabel-kind
By: assistant, model withheld from this shipped example

WHAT IS CHECKED: that the roll holds 51 rows dated 1851, 49 ordinary and 2
fairs, on 51 distinct days, every row counted being dated 1851 and no row
dated 1851 left out.  The full part 1, the construction, and the results
are in the record, evidence_and_reasoning/checks/001_count_1851.md; this
docstring does not repeat them.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import platform
import sys

import roll

FAILURES: list[str] = []
VALUES: dict[str, object] = {}
SUMS = roll.ROOT / "source_documents" / "Roll1851_market_roll_sha256.txt"


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


def _shift_year(rows):
    # A 29 February moves to 28 February, so that the shift alters dates and never stops the run.
    return [(d.replace(year=d.year + 1, day=min(d.day, 28) if (d.month, d.day) == (2, 29) else d.day), k) for d, k in rows]


def _drop_month(rows):
    return [(d, k) for d, k in rows if not (d.year == 1851 and d.month == 3)]


def _duplicate_entry(rows):
    return rows + [r for r in rows if roll.in_year(r[0], 1851)][:3]


def _relabel_kind(rows):
    i = next((i for i, (d, k) in enumerate(rows) if k == "fair" and roll.in_year(d, 1851)), None)
    return rows if i is None else rows[:i] + [(rows[i][0], "ordinary")] + rows[i + 1:]


MUTATIONS: dict[str, "callable"] = {
    "shift-year": _shift_year,
    "drop-month": _drop_month,
    "duplicate-entry": _duplicate_entry,
    "relabel-kind": _relabel_kind,
}

BASIS: list[str] = ["source_documents/Roll1851_market_roll/Roll1851_market_roll.csv",
                    "source_documents/Roll1851_market_roll_sha256.txt"]


def construct():
    """The roll's rows, as (date, kind) pairs in file order."""
    return roll.read_rows()


def two_years(rows) -> bool:
    return {d.year for d, _ in rows} <= {1851, 1852}


def known_kinds(rows) -> bool:
    return {k for _, k in rows} <= set(roll.KINDS)


def in_order(rows) -> bool:
    return [d for d, _ in rows] == sorted(d for d, _ in rows)


def count_1851(rows) -> tuple[int, int, int]:
    """The rows of 1851, in all and by kind: the count the claim states."""
    kept = [k for d, k in rows if roll.in_year(d, 1851)]
    return len(kept), kept.count("ordinary"), kept.count("fair")


def distinct_days(rows) -> int:
    """The distinct dates among the rows of 1851."""
    return len({d for d, _ in rows if roll.in_year(d, 1851)})


def by_month(rows) -> list[int]:
    """The reader's rows of 1851, month by month."""
    return [sum(1 for d, _ in rows if roll.in_year(d, 1851) and d.month == m) for m in range(1, 13)]


def lines_by_month() -> list[int]:
    """The held file's lines for each month of 1851, read as text, past the reader."""
    with open(roll.ROLL, encoding="utf-8", newline="") as fh:
        lines = fh.read().splitlines()[1:]
    return [sum(1 for line in lines if line.startswith(f"1851-{m:02d}-")) for m in range(1, 13)]


def is_listed(data: bytes, listed: dict) -> bool:
    """Whether these bytes are the file the checksum list names for the roll."""
    return listed.get(roll.ROLL.name) == hashlib.sha256(data).hexdigest()


def confirm_roll() -> bool:
    """Before the roll is parsed: it is the held file its checksum names, and the interpreter is stated."""
    data = roll.ROLL.read_bytes()
    listed = {line.split()[1]: line.split()[0] for line in SUMS.read_text(encoding="utf-8").splitlines() if line.strip()}
    ok = is_listed(data, listed)
    report("sanity: the roll is the file the checksum list names", ok, hashlib.sha256(data).hexdigest()[:16])
    report("control: bytes the list does not name fail that comparison", not is_listed(data + b"\n", listed))
    value("python", platform.python_version())
    print(f"  interpreter: {platform.python_implementation()} {platform.python_version()}")
    return ok


def sanity(rows) -> None:
    report("sanity: every row is dated 1851 or 1852", two_years(rows))
    report("control: a row dated 31 December 1850 fails that test", not two_years(rows + [(dt.date(1850, 12, 31), "ordinary")]))
    report("control: a row dated 1 January 1853 fails it too", not two_years(rows + [(dt.date(1853, 1, 1), "ordinary")]))
    report("sanity: every kind is ordinary or fair", known_kinds(rows))
    report("control: a row of another kind fails that test", not known_kinds(rows + [(dt.date(1851, 6, 3), "market")]))
    report("sanity: the rows are in date order", in_order(rows))
    report("control: two rows swapped fail that test", len(rows) < 2 or not in_order([rows[1], rows[0]] + rows[2:]))


def verify(rows) -> None:
    n, ordinary, fair = count_1851(rows)
    report("main: the roll holds 51 rows dated 1851", value("count_1851", n) == 51, str(n))
    report("main: 49 of them ordinary", value("ordinary_1851", ordinary) == 49)
    report("main: 2 of them fairs", value("fair_1851", fair) == 2)
    report("main: the 51 rows fall on 51 distinct days", value("days_1851", distinct_days(rows)) == n)
    report("control: a date held twice gives fewer days than rows",
           distinct_days(rows + [rows[0]]) < count_1851(rows + [rows[0]])[0])
    # The count's controls, through the same function: a row planted, and a
    # fair relabeled, each move the count as the claim says they would.
    first_fair = next((i for i, (d, k) in enumerate(rows) if k == "fair" and roll.in_year(d, 1851)), None)
    report("control: one row planted in 1851 is counted, 52", count_1851(rows + [(dt.date(1851, 6, 3), "ordinary")])[0] == n + 1)
    if first_fair is not None:
        relabeled = rows[:first_fair] + [(rows[first_fair][0], "ordinary")] + rows[first_fair + 1:]
        report("control: a fair relabeled ordinary splits 50 and 1", count_1851(relabeled)[1:] == (ordinary + 1, fair - 1))
    # The second route: the held file's lines, month by month, read past the
    # reader, agree with the reader's count in every month and in all.
    by_reader = by_month(rows)
    by_line = lines_by_month()
    value("monthly_1851", ",".join(str(c) for c in by_reader))
    report("second route: the file's lines agree, month by month", by_line == by_reader)
    first = next((r for r in rows if roll.in_year(r[0], 1851)), None)
    dropped = [r for r in rows if r != first]
    report("control: the first row of 1851 dropped from the reader's rows makes its month disagree",
           first is not None and by_month(dropped) != by_line)
    report("second route: and in all, so no row of 1851 is left out", sum(by_line) == n, f"{sum(by_line)} lines open with 1851-")
    report("one for many: every row counted is dated 1851", all(d.year == 1851 for d, _ in rows if roll.in_year(d, 1851)))
    # The year's boundary, pinned from both sides through the function the count uses.
    report("control: 1 January 1851 is in the year", roll.in_year(dt.date(1851, 1, 1), 1851))
    report("control: 31 December 1850 is not", not roll.in_year(dt.date(1850, 12, 31), 1851))
    report("control: 31 December 1851 is in the year", roll.in_year(dt.date(1851, 12, 31), 1851))
    report("control: 1 January 1852 is not", not roll.in_year(dt.date(1852, 1, 1), 1851))


def discrepancies(rows) -> None:
    for m, (a, b) in enumerate(zip(by_month(rows), lines_by_month()), 1):
        if a != b:
            print(f"  month {m}: {a} rows by the reader, {b} lines in the file")


def main() -> int:
    print(__doc__.splitlines()[0])
    if confirm_roll():
        obj = construct()
        sanity(obj)
        verify(obj)
        discrepancies(obj)
    else:
        print("  the roll is not the held file, and it is not parsed")
    verdict = "reproduced" if not FAILURES else "not reproduced"
    print()
    print(f"  {len(FAILURES)} failure(s)" if FAILURES else "  all assertions passed")
    print("RESULT: " + verdict + "".join(f"; {k}={v}" for k, v in VALUES.items()))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

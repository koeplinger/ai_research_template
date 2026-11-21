#!/usr/bin/env python3
"""Check 005: the weekdays of the roll's rows for 1851.

Created 20 November 2026; updated 20 November 2026.
Plan: 001, task 6
Backs: [claim 005]
Instrument: the held roll at its recorded checksum, read with the Python standard library, CPython 3.12.3
Frame: the calendar year, as the roll's dates give it, fixed by roll.in_year; a date's weekday, that of its ISO form on the Gregorian calendar
Mutation: shift-year, drop-month, duplicate-entry, relabel-kind
By: assistant, model withheld from this shipped example

WHAT IS CHECKED: that the roll's 49 ordinary rows of 1851 fall on
Tuesdays and its 2 fairs, of 15 May and 9 October, on Thursdays, no row
on any other weekday; and that of the year's 52 Tuesdays the roll holds a
row on 49, the three without one being 4 February, 12 August and 30
December.  The full part 1, the construction, and the results are in the
record, evidence_and_reasoning/checks/005_weekdays.md; this docstring does
not repeat them.
"""
from __future__ import annotations

import collections
import datetime as dt
import hashlib
import platform
import sys

import roll

FAILURES: list[str] = []
VALUES: dict[str, object] = {}
SUMS = roll.ROOT / "source_documents" / "Roll1851_market_roll_sha256.txt"
TUESDAY, THURSDAY = 1, 3    # as date.weekday() numbers them, Monday being 0
ONE_DAY = dt.timedelta(days=1)


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


def of_1851(rows) -> list:
    """The rows of 1851, in order, taken through in_year."""
    return [r for r in rows if roll.in_year(r[0], 1851)]


def weekday(d: dt.date) -> int:
    """A date's weekday by the date library, Monday being 0."""
    return d.weekday()


def zeller(d: dt.date) -> int:
    """A Gregorian date's weekday by Zeller's congruence, Monday being 0: a route past the date library."""
    y, m = (d.year - 1, d.month + 12) if d.month < 3 else (d.year, d.month)
    k, j = y % 100, y // 100
    return (d.day + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j + 5) % 7


def agrees(days, route=zeller) -> bool:
    """Whether a route gives the date library's weekday on every one of these days."""
    return all(weekday(d) == route(d) for d in days)


def pattern(rows) -> dict:
    """The rows of 1851, counted by kind and weekday."""
    return dict(collections.Counter((k, weekday(d)) for d, k in of_1851(rows)))


def has_shape(rows) -> bool:
    """The claim's first half: 49 ordinary rows on Tuesdays, 2 fairs on Thursdays, and no other row of 1851."""
    return pattern(rows) == {("ordinary", TUESDAY): 49, ("fair", THURSDAY): 2}


def fair_dates(rows) -> list[str]:
    """The month and day of each fair of 1851, in order."""
    return [d.strftime("%m-%d") for d, k in of_1851(rows) if k == "fair"]


def days_of(year: int) -> list[dt.date]:
    """Every day of a calendar year: the days of that year and the years on either side, taken through in_year."""
    start, end = dt.date(year - 1, 1, 1), dt.date(year + 1, 12, 31)
    return [d for d in (start + n * ONE_DAY for n in range((end - start).days + 1)) if roll.in_year(d, year)]


def tuesdays_of(year: int) -> list[dt.date]:
    """Every Tuesday of a calendar year."""
    return [d for d in days_of(year) if weekday(d) == TUESDAY]


def without_row(rows) -> list[dt.date]:
    """The Tuesdays of 1851 on which the rows hold nothing."""
    held = {d for d, _ in rows}
    return [d for d in tuesdays_of(1851) if d not in held]


def made_up():
    """A made-up roll of the claimed shape: the first 49 Tuesdays of 1851, ordinary, and two fairs on Thursdays."""
    return [(d, "ordinary") for d in tuesdays_of(1851)[:49]] + [(dt.date(1851, 5, 15), "fair"), (dt.date(1851, 10, 9), "fair")]


def holds_count(rows) -> bool:
    """Whether the roll holds the 51 rows of 1851 that check 001 counts."""
    return len(of_1851(rows)) == 51


def file_lines() -> list[str]:
    """The held file's lines, as text, its header first, read past the reader."""
    with open(roll.ROLL, encoding="utf-8", newline="") as fh:
        return [line.rstrip("\r\n") for line in fh]


def text_rows(lines) -> list[tuple[str, str]]:
    """The data lines opening 1851-, as (date, kind) text, split on commas, past the reader."""
    return [tuple(line.split(",", 2)[:2]) for line in lines[1:] if line.startswith("1851-")]


def matches_file(rows, lines) -> bool:
    """Whether the reader's rows of 1851 are the file's lines of 1851, row for row."""
    return [(d.isoformat(), k) for d, k in of_1851(rows)] == text_rows(lines)


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
    n = value("rows_1851", len(of_1851(rows)))
    report("sanity: the roll holds the 51 rows of 1851 that check 001 counts", holds_count(rows), str(n))
    report("control: 50 rows of 1851 fail that test", not holds_count(made_up()[:50]))
    report("control: 52 rows of 1851 fail it too", not holds_count(made_up() + made_up()[:1]))
    lines = file_lines()
    kept = of_1851(rows)
    first = next((line for line in lines[1:] if line.startswith("1851-")), "")
    report("sanity: the reader's rows of 1851 are the file's lines of 1851, row for row", matches_file(rows, lines))
    report("control: a row of 1851 the reader dropped fails that match", not matches_file(kept[1:], lines))
    misread = [(kept[0][0] + ONE_DAY, kept[0][1])] + kept[1:] if kept else kept
    report("control: a row of 1851 misread, the count kept, fails it", not matches_file(misread, lines))
    report("control: a line the file holds twice and the reader gives once fails it", not matches_file(rows, lines + [first]))
    edges = ["date,kind,remark", "1850-12-31,ordinary,", "1851-01-01,ordinary,", "1851-12-31,ordinary,", "1852-01-01,ordinary,"]
    report("control: the file's lines of 1851 are cut at the year's two ends", [r[0] for r in text_rows(edges)] == ["1851-01-01", "1851-12-31"])


def verify(rows) -> None:
    # The two routes to a weekday, each against dates known from outside the roll.
    for d, name, want in ((dt.date(1900, 1, 1), "1 January 1900, a Monday", 0),
                          (dt.date(2000, 1, 1), "1 January 2000, a Saturday", 5),
                          (dt.date(2000, 2, 29), "29 February 2000, a Tuesday", TUESDAY),
                          (dt.date(1970, 1, 1), "1 January 1970, a Thursday", THURSDAY)):
        report(f"control: both routes give {name}", (weekday(d), zeller(d)) == (want, want))
    year = days_of(1851)
    report("second route: Zeller's congruence gives the date library's weekday on every day of 1851", agrees(year), f"{len(year)} days")
    report("control: the days walked are the 365 of 1851, from 1 January to 31 December",
           (len(year), year[:1], year[-1:]) == (365, [dt.date(1851, 1, 1)], [dt.date(1851, 12, 31)]))
    report("control: a route one day out does not agree", not agrees(year, lambda d: zeller(d + ONE_DAY)))
    # The first half of the claim, and its controls on a made-up roll of the same shape.
    p = pattern(rows)
    ordinary_tue, fair_thu = p.get(("ordinary", TUESDAY), 0), p.get(("fair", THURSDAY), 0)
    value("ordinary_tuesday", ordinary_tue)
    value("fair_thursday", fair_thu)
    value("other_rows", sum(p.values()) - ordinary_tue - fair_thu)
    report("main: 49 ordinary rows on Tuesdays, 2 fairs on Thursdays, no row of 1851 on another day", has_shape(rows), str(sorted(p.items())))
    typical = made_up()
    report("control: a made-up roll of that shape passes the test", has_shape(typical))
    report("control: an ordinary row moved to a Wednesday fails it", not has_shape([(typical[0][0] + ONE_DAY, "ordinary")] + typical[1:]))
    report("control: a fair moved to a Friday fails it", not has_shape(typical[:-1] + [(typical[-1][0] + ONE_DAY, "fair")]))
    report("control: a fair relabeled ordinary fails it", not has_shape(typical[:-1] + [(typical[-1][0], "ordinary")]))
    report("control: 48 ordinary rows fail it", not has_shape(typical[1:]))
    report("control: 50 ordinary rows fail it", not has_shape(typical + [(d, "ordinary") for d in tuesdays_of(1851)[49:50]]))
    report("control: 1 fair fails it", not has_shape(typical[:-1]))
    report("control: 3 fairs fail it", not has_shape(typical + [(dt.date(1851, 7, 3), "fair")]))
    report("main: the fairs of 1851 are of 15 May and 9 October", value("fairs_1851", ",".join(fair_dates(rows))) == "05-15,10-09")
    report("control: a fair moved a day gives other dates", fair_dates(typical[:-1] + [(typical[-1][0] + ONE_DAY, "fair")]) != ["05-15", "10-09"])
    # The second half: the year's Tuesdays, pinned at both ends, and those with no row.
    tuesdays = tuesdays_of(1851)
    report("main: 1851 has 52 Tuesdays", value("tuesdays_1851", len(tuesdays)) == 52)
    report("control: 7 January 1851 is the first of them, and 31 December 1850, a Tuesday, is not one",
           tuesdays[:1] == [dt.date(1851, 1, 7)] and weekday(dt.date(1850, 12, 31)) == TUESDAY and dt.date(1850, 12, 31) not in tuesdays)
    report("control: 30 December 1851 is the last of them, and 6 January 1852, a Tuesday, is not one",
           tuesdays[-1:] == [dt.date(1851, 12, 30)] and weekday(dt.date(1852, 1, 6)) == TUESDAY and dt.date(1852, 1, 6) not in tuesdays)
    missing = without_row(rows)
    value("tuesdays_held", len(tuesdays) - len(missing))
    report("main: the Tuesdays without a row are 4 February, 12 August and 30 December",
           value("tuesdays_without_row", ",".join(d.strftime("%m-%d") for d in missing)) == "02-04,08-12,12-30")
    report("control: a row on any of the three takes it off the list",
           all(d not in without_row(rows + [(d, "ordinary")]) for d in (dt.date(1851, 2, 4), dt.date(1851, 8, 12), dt.date(1851, 12, 30))))
    report("control: a made-up roll holding one Tuesday more has one fewer without a row",
           len(without_row(typical + [(d, "ordinary") for d in tuesdays[49:50]])) == 2)
    report("control: a made-up roll holding one Tuesday fewer has one more without a row", len(without_row(typical[1:])) == 4)
    # The year's boundary, pinned from both sides through in_year, the function the reader's rows are taken by.
    report("control: 1 January 1851 is in the year", roll.in_year(dt.date(1851, 1, 1), 1851))
    report("control: 31 December 1850 is not", not roll.in_year(dt.date(1850, 12, 31), 1851))
    report("control: 31 December 1851 is in the year", roll.in_year(dt.date(1851, 12, 31), 1851))
    report("control: 1 January 1852 is not", not roll.in_year(dt.date(1852, 1, 1), 1851))


def discrepancies(rows) -> None:
    for d, k in of_1851(rows):
        if (k, weekday(d)) not in {("ordinary", TUESDAY), ("fair", THURSDAY)}:
            print(f"  {d.isoformat()}: {k} on a {d.strftime('%A')}")


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

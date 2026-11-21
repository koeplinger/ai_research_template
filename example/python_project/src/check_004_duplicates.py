#!/usr/bin/env python3
"""Check 004: duplicated rows among the roll's entries for 1851.

Created 20 November 2026; updated 20 November 2026.
Plan: 001, task 4
Backs: [claim 004]
Instrument: the held roll at its recorded checksum, read with the Python standard library, CPython 3.12.3
Frame: the calendar year, as the roll's dates give it, fixed by roll.in_year
Mutation: duplicate-entry
By: assistant, model withheld from this shipped example

WHAT IS CHECKED: that three of the roll's 51 rows dated 1851 repeat an
earlier row's date and kind, so that without them the roll's days of 1851
number the note's forty-eight, which the explanation under test needs.
The full part 1, the construction, and the results are in the record,
evidence_and_reasoning/checks/004_duplicates.md; this docstring does not
repeat them.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import io
import platform
import sys

import roll

FAILURES: list[str] = []
VALUES: dict[str, object] = {}
SUMS = roll.ROOT / "source_documents" / "Roll1851_market_roll_sha256.txt"
ROLL_COUNT = 51     # the roll's count for 1851, as [claim 001] states it; gated below against the roll's own rows
NOTE_FIGURE = 48    # the note's figure for 1851, as [claim 002] states it; taken as given, the note not being read here
NEEDED = ROLL_COUNT - NOTE_FIGURE    # the repeats the explanation needs, computed from the two


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


def _duplicate_entry(rows):
    return rows + [r for r in rows if roll.in_year(r[0], 1851)][:3]


MUTATIONS: dict[str, "callable"] = {
    "duplicate-entry": _duplicate_entry,
}

BASIS: list[str] = ["source_documents/Roll1851_market_roll/Roll1851_market_roll.csv",
                    "source_documents/Roll1851_market_roll_sha256.txt"]


def construct():
    """The roll's rows, as (date, kind) pairs in file order."""
    return roll.read_rows()


def of_1851(rows) -> list:
    """The rows of 1851, in order, taken through in_year."""
    return [r for r in rows if roll.in_year(r[0], 1851)]


def duplicates(rows) -> int:
    """The rows of 1851 whose (date, kind) pair has occurred earlier: a pair entered k times counts k - 1."""
    seen, n = set(), 0
    for r in of_1851(rows):
        n += r in seen
        seen.add(r)
    return n


def repeated_dates(rows) -> int:
    """The rows of 1851 whose date, whatever its kind, has occurred earlier."""
    days = [d for d, _ in of_1851(rows)]
    return len(days) - len(set(days))


def explains(rows) -> bool:
    """The gate: the needed rows of 1851 repeat an earlier row, and the days of 1851 number the note's figure."""
    return duplicates(rows) == NEEDED and len({d for d, _ in of_1851(rows)}) == NOTE_FIGURE


def holds_count(rows) -> bool:
    """Whether the roll holds the rows of 1851 that check 001 counts."""
    return len(of_1851(rows)) == ROLL_COUNT


def matches_file(rows, lines) -> bool:
    """Whether the reader's rows of 1851 are the file's lines of 1851, row for row."""
    return [(d.isoformat(), k) for d, k in of_1851(rows)] == text_rows(lines)


def planted(k: int):
    """A made-up roll of 51 rows of 1851, k of them repeats: 51 - k days from 1 January 1851, one
    ordinary row each, and the first k of those rows entered a second time."""
    days = [(dt.date(1851, 1, 1) + dt.timedelta(days=i), "ordinary") for i in range(51 - k)]
    return days + days[:k]


def file_lines() -> list[str]:
    """The held file's lines, as text, its header first, read past the reader."""
    with open(roll.ROLL, encoding="utf-8", newline="") as fh:
        return [line.rstrip("\r\n") for line in fh]


def text_rows(lines) -> list[tuple[str, str]]:
    """The data lines opening 1851-, as (date, kind) text, split on commas, past the reader."""
    return [tuple(line.split(",", 2)[:2]) for line in lines[1:] if line.startswith("1851-")]


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
    report(f"sanity: the roll holds the {ROLL_COUNT} rows of 1851 that check 001 counts", holds_count(rows), str(n))
    report("control: 50 rows of 1851 fail that test", not holds_count(planted(0)[:50]))
    report("control: 52 rows of 1851 fail it too", not holds_count(planted(0) + planted(0)[:1]))
    lines = file_lines()
    kept = of_1851(rows)
    first = next((line for line in lines[1:] if line.startswith("1851-")), "")
    report("sanity: the reader's rows of 1851 are the file's lines of 1851, row for row", matches_file(rows, lines))
    report("control: a row of 1851 the reader dropped fails that match", not matches_file(kept[1:], lines))
    misread = [(kept[0][0] + dt.timedelta(days=1), kept[0][1])] + kept[1:] if kept else kept
    report("control: a row of 1851 misread, the count kept, fails it", not matches_file(misread, lines))
    report("control: a line the file holds twice and the reader gives once fails it", not matches_file(rows, lines + [first]))


def verify(rows) -> None:
    value("needed", NEEDED)
    # The counting functions' controls, on made-up rolls.
    report("control: one planted repeat is counted as one", value("control_one", duplicates(planted(1))) == 1)
    report("control: three planted repeats are counted as three", value("control_three", duplicates(planted(3))) == 3)
    report("control: one row entered three times is counted as two repeats", duplicates(planted(1) + planted(1)[:1]) == 2)
    both_kinds = planted(0) + [(dt.date(1851, 1, 1), "fair")]
    report("control: a date entered again with the other kind is counted by its date, not by its date and kind",
           (repeated_dates(both_kinds), duplicates(both_kinds)) == (1, 0))
    # Through the reader: the file's text, each date and kind taken once, with
    # its first line of 1851 entered a second time, is read as one row more
    # and counted as one repeat.
    lines = file_lines()
    seen, once = set(), lines[:1]
    for line in lines[1:]:
        if tuple(line.split(",", 2)[:2]) not in seen:
            once.append(line)
            seen.add(tuple(line.split(",", 2)[:2]))
    first = next((line for line in once[1:] if line.startswith("1851-")), "")
    read_twice = roll.rows_from(io.StringIO("\r\n".join(once + [first]) + "\r\n", newline=""))
    report("control: a line of 1851 entered twice in the file's text is read as two rows and counted as one repeat",
           duplicates(read_twice) == 1 and len(of_1851(read_twice)) == len(text_rows(once)) + 1)
    # The gate, pinned from both sides on made-up rolls of 51 rows of 1851:
    # two repeats leave 49 days and fail it, three leave 48 and pass it, four
    # leave 47 and fail it. It holds both of its halves: four repeats on 48
    # days (52 rows) fail it, and so do three repeats leaving 47 days, one
    # date being held under both kinds. The main assertion is the gate itself.
    report("control: two planted repeats fail the gate", not explains(planted(2)))
    report("control: three planted repeats pass it", explains(planted(3)))
    report("control: four planted repeats fail it", not explains(planted(4)))
    report("control: four repeats on 48 days fail it", not explains(planted(3) + planted(3)[3:4]))
    days_47 = planted(0)[:47]
    report("control: three repeats leaving 47 days, one date under both kinds, fail it",
           not explains(days_47 + [(days_47[0][0], "fair")] + days_47[:3]))
    found = value("duplicates_1851", duplicates(rows))
    report(f"main: {NEEDED} rows of 1851 repeat an earlier row, leaving the note's {NOTE_FIGURE} days", explains(rows), f"{found} found")
    value("repeated_dates_1851", repeated_dates(rows))
    value("days_1851", len({d for d, _ in of_1851(rows)}))
    # The year's boundary, pinned from both sides through in_year, the function the reader's rows are taken by.
    report("control: 1 January 1851 is in the year", roll.in_year(dt.date(1851, 1, 1), 1851))
    report("control: 31 December 1850 is not", not roll.in_year(dt.date(1850, 12, 31), 1851))
    report("control: 31 December 1851 is in the year", roll.in_year(dt.date(1851, 12, 31), 1851))
    report("control: 1 January 1852 is not", not roll.in_year(dt.date(1852, 1, 1), 1851))


def discrepancies(rows) -> None:
    if not explains(rows):
        days = [d for d, _ in of_1851(rows)]
        print(f"  the explanation needs {NEEDED} repeated rows of 1851 and the roll holds {duplicates(rows)};"
              f" its {len(days)} rows of 1851 fall on {len(set(days))} distinct dates, where the note states {NOTE_FIGURE}")


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

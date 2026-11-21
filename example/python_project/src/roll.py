"""The market roll as rows: the one reader every check of the roll imports.

Created 20 November 2026; updated 20 November 2026.

The roll [Roll1851] is a CSV held under source_documents/, with three
columns, date, kind and remark: one row per day held, the date in ISO form,
the kind either ordinary or fair.  read_rows() returns its rows in file
order as (date, kind) pairs and refuses a line it cannot read as a row of
three fields, a blank line included, rather than skipping it.  A quoted
field is read as the csv module reads it, so that one left open runs on
into the lines after it; the held roll has no quotation mark, its checksum
is confirmed before a check parses it, and each check's second route,
reading the file's lines of 1851 past this reader, would show one of them
lost.  rows_from() does the reading, from any text stream
opened with newline="", so that a check can pass a planted text through
the reader.  in_year() fixes the
frame every count of the roll is stated in: a row belongs to a year when
its date falls in that calendar year, the year's boundary being imposed by
this project (evidence_and_reasoning/terminology.md).
"""
from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROLL = ROOT / "source_documents" / "Roll1851_market_roll" / "Roll1851_market_roll.csv"
KINDS = ("ordinary", "fair")


def read_rows(path: Path = ROLL) -> list[tuple[dt.date, str]]:
    """The roll's rows as (date, kind), in file order; a row that does not read raises an error."""
    with open(path, newline="", encoding="utf-8") as fh:
        return rows_from(fh)


def rows_from(stream) -> list[tuple[dt.date, str]]:
    """The rows of a roll read from a text stream opened with newline="", its header first."""
    reader = csv.reader(stream)
    header = next(reader, None)
    if header != ["date", "kind", "remark"]:
        raise ValueError(f"unexpected columns: {header}")
    out = []
    for row in reader:
        n = reader.line_num
        if len(row) != 3:
            raise ValueError(f"line {n}: {len(row)} fields, not 3")
        date, kind, _ = row
        if kind not in KINDS:
            raise ValueError(f"line {n}: unknown kind {kind!r}")
        out.append((dt.date.fromisoformat(date), kind))
    return out


def in_year(day: dt.date, year: int) -> bool:
    """Whether a date falls in the given calendar year: the frame of every count."""
    return day.year == year

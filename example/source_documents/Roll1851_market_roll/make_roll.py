"""The market roll of a fictional town, 1851 and 1852, written as CSV to standard output.

Every Tuesday of the two years is a market day, and so are two fair days
a year, less the Tuesdays the town's fictional council cancelled. The
roll records the days held: a cancelled Tuesday has no row, and the
reason it was cancelled is not recorded. Nothing here describes a real
place, and nothing in it is random, so every run prints the same bytes.
The file held beside this program is its output:

    python3 make_roll.py > Roll1851_market_roll.csv
"""
from __future__ import annotations

import csv
import datetime as dt
import sys

FAIRS = {dt.date(1851, 5, 15): "spring fair", dt.date(1851, 10, 9): "autumn fair",
         dt.date(1852, 5, 13): "spring fair", dt.date(1852, 10, 14): "autumn fair"}
CANCELLED = {dt.date(1851, 2, 4), dt.date(1851, 8, 12), dt.date(1851, 12, 30), dt.date(1852, 3, 2)}


def rows() -> list[dict[str, str]]:
    """One row per day held, in date order."""
    out = []
    day = dt.date(1851, 1, 1)
    while day.year <= 1852:
        if day.weekday() == 1 and day not in CANCELLED:
            out.append({"date": day.isoformat(), "kind": "ordinary", "remark": ""})
        if day in FAIRS:
            out.append({"date": day.isoformat(), "kind": "fair", "remark": FAIRS[day]})
        day += dt.timedelta(days=1)
    return out


def main() -> int:
    writer = csv.DictWriter(sys.stdout, fieldnames=["date", "kind", "remark"])
    writer.writeheader()
    writer.writerows(rows())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

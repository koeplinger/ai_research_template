"""The synthetic market roll: the market days of a fictional town in 1851 and 1852, written as a CSV.

Created 6 September 2026; updated 6 September 2026.

This example's source of record is synthetic by design.  The roll is
every Tuesday of the two years, plus two fair days a year, less the
Tuesdays the town's fictional council cancelled; nothing here describes
any real place.  The committed file source_documents/Roll1851_market_roll.csv
is the source of record for the example; this program is its provenance,
and running it again writes the same file, since nothing in it is random.

Usage
    python3 src/make_roll.py           write the roll to source_documents/
    python3 src/make_roll.py --print   print the rows instead
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "source_documents" / "Roll1851_market_roll.csv"
FAIRS = {dt.date(1851, 5, 15): "spring fair", dt.date(1851, 10, 9): "autumn fair",
         dt.date(1852, 5, 13): "spring fair", dt.date(1852, 10, 14): "autumn fair"}
CANCELLED = {dt.date(1851, 2, 4): "frost", dt.date(1851, 8, 12): "council order", dt.date(1851, 12, 30): "council order",
             dt.date(1852, 3, 2): "flood"}


def rows() -> list[dict[str, str]]:
    out = []
    day = dt.date(1851, 1, 1)
    while day.year <= 1852:
        if day.weekday() == 1 and day not in CANCELLED:
            out.append({"date": day.isoformat(), "kind": "ordinary", "note": ""})
        if day in FAIRS:
            out.append({"date": day.isoformat(), "kind": "fair", "note": FAIRS[day]})
        day += dt.timedelta(days=1)
    return sorted(out, key=lambda r: (r["date"], r["kind"]))


def main(argv: list[str]) -> int:
    data = rows()
    if argv == ["--print"]:
        for r in data:
            print(",".join(r.values()))
        return 0
    with open(TARGET, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["date", "kind", "note"])
        w.writeheader()
        w.writerows(data)
    print(f"wrote {len(data)} rows to {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

"""Tests of the roll's generator, the one foundation module.

Created 6 September 2026; updated 6 September 2026.
"""
import datetime as dt

import make_roll


def test_every_row_is_a_tuesday_or_a_fair():
    for r in make_roll.rows():
        day = dt.date.fromisoformat(r["date"])
        assert day.weekday() == 1 or r["kind"] == "fair"


def test_cancelled_tuesdays_are_absent():
    dates = {r["date"] for r in make_roll.rows() if r["kind"] == "ordinary"}
    for day in make_roll.CANCELLED:
        assert day.isoformat() not in dates


def test_rows_are_sorted_and_unique():
    rows = [(r["date"], r["kind"]) for r in make_roll.rows()]
    assert rows == sorted(rows)
    assert len(rows) == len(set(rows))

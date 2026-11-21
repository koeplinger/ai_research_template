"""Tests of the roll reader, src/roll.py.

Created 20 November 2026; updated 20 November 2026.

Each test of reading writes a small roll of its own to a temporary
folder, so that what it tests is the reader and not the held file.
"""
import datetime as dt
import io

import pytest

import roll


def write(tmp_path, text):
    p = tmp_path / "roll.csv"
    p.write_text(text, encoding="utf-8", newline="")
    return p


def test_reads_rows_in_file_order(tmp_path):
    p = write(tmp_path, "date,kind,remark\r\n1851-01-07,ordinary,\r\n1851-05-15,fair,spring fair\r\n")
    assert roll.read_rows(p) == [(dt.date(1851, 1, 7), "ordinary"), (dt.date(1851, 5, 15), "fair")]


def test_refuses_an_unknown_kind(tmp_path):
    p = write(tmp_path, "date,kind,remark\r\n1851-01-07,market,\r\n")
    with pytest.raises(ValueError):
        roll.read_rows(p)


def test_refuses_an_unreadable_date(tmp_path):
    p = write(tmp_path, "date,kind,remark\r\n1851-02-30,ordinary,\r\n")
    with pytest.raises(ValueError):
        roll.read_rows(p)


def test_refuses_unexpected_columns(tmp_path):
    p = write(tmp_path, "day,kind,remark\r\n1851-01-07,ordinary,\r\n")
    with pytest.raises(ValueError):
        roll.read_rows(p)


def test_reads_text_as_it_reads_the_file(tmp_path):
    text = "date,kind,remark\r\n1851-01-07,ordinary,\r\n1851-05-15,fair,spring fair\r\n"
    p = write(tmp_path, text)
    assert roll.rows_from(io.StringIO(text, newline="")) == roll.read_rows(p)


def test_keeps_a_line_entered_twice(tmp_path):
    p = write(tmp_path, "date,kind,remark\r\n1851-01-07,ordinary,\r\n1851-01-07,ordinary,\r\n")
    assert roll.read_rows(p) == [(dt.date(1851, 1, 7), "ordinary")] * 2


@pytest.mark.parametrize("line", ["", "1851-01-07,ordinary", "1851-01-07,ordinary,,1851-06-03"])
def test_refuses_a_line_that_is_not_three_fields(tmp_path, line):
    p = write(tmp_path, f"date,kind,remark\r\n1851-01-14,ordinary,\r\n{line}\r\n1851-01-21,ordinary,\r\n")
    with pytest.raises(ValueError, match="line 3"):
        roll.read_rows(p)


def test_a_refusal_names_the_file_line(tmp_path):
    p = write(tmp_path, "date,kind,remark\r\n1851-01-07,ordinary,\r\n1851-01-14,market,\r\n")
    with pytest.raises(ValueError, match="line 3: unknown kind"):
        roll.read_rows(p)


def test_the_year_boundary_from_both_sides():
    assert roll.in_year(dt.date(1851, 1, 1), 1851)
    assert roll.in_year(dt.date(1851, 12, 31), 1851)
    assert not roll.in_year(dt.date(1850, 12, 31), 1851)
    assert not roll.in_year(dt.date(1852, 1, 1), 1851)

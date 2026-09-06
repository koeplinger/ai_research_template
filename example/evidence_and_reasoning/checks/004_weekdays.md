# Check 004: the weekdays of the roll's 1851 rows

*Created 6 September 2026; updated 6 September 2026.*
Plan: 001, task 5
Backs: [claim 007]
Instrument: the roll file at its committed revision, read with the Python standard library (3.11 or later)
Mutation: shift-year, drop-month
Frame: the calendar year, as the roll's dates give it; weekdays as the standard library's date arithmetic gives them
By: assistant

## 1. What is checked

That the 49 ordinary rows of 1851 in the roll [Roll1851] fall on
Tuesdays and the 2 fairs on Thursdays [Roll1851, rows 19 and 40]; that
the 51 rows fall on 51 distinct dates; and that the calendar year 1851
has 52 Tuesdays, of which three have no row. Built on [check 001], whose
count of 51 rows this check takes as a sanity value.

## 2. Construction

The program `python_project/src/check_004_weekdays.py` reads every row
of the roll into a list of (date, kind); a row belongs to 1851 when
its date's year is 1851. The weekday of a date is the standard library's
`weekday()`, the Gregorian calendar's; the Tuesdays of 1851 are every
date of that year whose weekday is Tuesday, and a Tuesday has a row when
an ordinary row carries its date. Distinct dates are the set of the
rows' dates.

## 3. Sanity checks

The roll parses; the rows of 1851 number 51, as [check 001] found;
every kind is one of the two the registry entry names; the known case,
that 1 January 1851 is a Wednesday, holds.

## 4. Results

Run 6 September 2026, by assistant, CPython 3.12.3; re-run by the
assistant in the researcher's role.

rows_1851 = 51
ordinary_on_tuesday = 49
fair_weekdays = Thursday,Thursday
distinct_dates_1851 = 51
tuesdays_1851 = 52
tuesdays_with_row = 49
tuesdays_without_row = 1851-02-04,1851-08-12,1851-12-30

## 5. Discrepancies

None.

## 6. Verdict

Reproduced: the 49 ordinary rows are Tuesdays, the two fairs are
Thursdays, no date carries two rows, and three of the 52 Tuesdays of
1851 have no row, as [claim 007] states. Nothing further along this line
is needed. Second pass: the control assertion counts the Tuesdays with a
row by the calendar and reaches the same 49 as the count of ordinary
rows; the assistant, in the researcher's role, re-ran the program and
read the same line.

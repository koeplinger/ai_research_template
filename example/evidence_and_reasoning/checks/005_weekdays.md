# Check 005: the weekdays of the roll's rows for 1851

*Created 20 November 2026; updated 20 November 2026.*
Plan: 001, task 6
Backs: [claim 005]
Instrument: the held roll at its recorded checksum, read with the Python standard library, CPython 3.12.3
Mutation: shift-year, drop-month, duplicate-entry, relabel-kind
Frame: the calendar year, as the roll's dates give it, fixed by the roll reader's in_year; a date's weekday, that of its ISO form on the Gregorian calendar
By: assistant, model withheld from this shipped example

## 1. What is checked

That the roll's 49 ordinary rows of 1851 [Roll1851] fall on Tuesdays and
its 2 fairs, of 15 May and 9 October, on Thursdays, no row of 1851 on any
other weekday; and that of the 52 Tuesdays of 1851 the roll holds a row
on 49, the three without one being 4 February, 12 August, and 30
December. This is what [claim 005] states. Built on [check 001], whose
count of 51 rows this check gates again against the roll's own rows. A
date's weekday is that of its ISO form on the Gregorian calendar: the
roll writes its dates in that form, and the reading is imposed by this
project, the roll being made for it (`prompt_logs/005_sources.md`). The
program does not read the note.

## 2. Construction

The program `python_project/src/check_005_weekdays.py` first confirms
that the roll it will read is the held file whose SHA-256 checksum
`source_documents/Roll1851_market_roll_sha256.txt` lists, and prints the
interpreter it runs under; a roll that is not the held file is not parsed.
It then reads the roll through the project's reader as (date, kind)
pairs in file order, takes the rows of 1851 through `in_year`, and counts
them by kind and weekday, the date library giving the weekday. The
days of 1851 are found by walking that year and the years on either side
of it through `in_year`; its Tuesdays are those days on the weekday, and
those on which the roll holds no row are listed.

Two second routes. The held file's lines opening 1851-, split on their
commas, must be the reader's rows of 1851, row for row, so that a line
the reader merged, dropped, or misread shows as a disagreement. And
Zeller's congruence, a formula that uses no date library, must give the
date library's weekday on each day of 1851 so walked.

## 3. Sanity checks

Named in the program and reported by it, each with controls run through
the same function: the roll is the held file its checksum names (bytes
the list does not name fail that comparison); the roll holds the 51 rows
of 1851 that [check 001] counts (50 rows and 52 fail); the reader's rows
of 1851 are the file's lines of 1851, row for row (a row dropped, a row
misread with the count kept, and a line the file holds twice and the
reader gives once each fail), the lines of 1851 being cut at the year's
two ends. Both routes to a weekday give the weekday known from outside
the roll for 1 January 1900, a Monday, 1 January 2000, a Saturday, 29
February 2000, a Tuesday, and 1 January 1970, a Thursday; a route one day
out does not agree with the date library; and the days walked are the
365 of 1851, from 1 January to 31 December.

The claim's first half is tested on a made-up roll of the same shape,
which passes; an ordinary row moved to a Wednesday, a fair moved to a
Friday, a fair relabeled ordinary, 48 or 50 ordinary rows, and 1 or 3
fairs each fail, and a fair moved a day gives other fair dates. Its
second half is pinned at both ends of the
year: 7 January 1851 is the first Tuesday and 30 December 1851 the last,
and 31 December 1850 and 6 January 1852, both Tuesdays, are not among
them. A row on any of the three Tuesdays takes it off the list; a made-up
roll holding one Tuesday more has one fewer without a row, and one
holding one fewer has one more. The year's boundary is
pinned from both sides through `in_year`, the function the reader's rows
of 1851 are taken by: 1 January and 31 December 1851 are in the year, 31
December 1850 and 1 January 1852 are not.

## 4. Results

Run 20 November 2026, by assistant, model withheld from this shipped
example. Every assertion passed.

python = 3.12.3
rows_1851 = 51
ordinary_tuesday = 49
fair_thursday = 2
other_rows = 0
fairs_1851 = 05-15,10-09
tuesdays_1851 = 52
tuesdays_held = 49
tuesdays_without_row = 02-04,08-12,12-30

## 5. Discrepancies

None: the file's lines and the reader agree row for row, and the two
routes to a weekday agree on every day of 1851.

## 6. Verdict

Reproduced: the roll's 49 ordinary rows of 1851 fall on Tuesdays and its
2 fairs, of 15 May and 9 October, on Thursdays, and of the 52 Tuesdays of
1851 the three without a row are 4 February, 12 August, and 30 December,
as [claim 005] states. What to check next is what the note says of the
same days, which this check does not read.

Each named mutation was applied by the probe
(`tools/falsifiability_probe.py`), and the check failed under each. The
probe's matrix: the direct and the wrapped runs pass; shift-year,
drop-month, duplicate-entry and relabel-kind CAUGHT.
The probe's reader's table and the coverage audit, with the gaps each
found and their refuters' verdicts, are kept in
`prompt_logs/011_weekdays.md`.

Second pass: a reader without the first pass's reasoning, given the held
CSV alone, worked out the weekdays of the rows of 1851 by two methods of
its own, Zeller's congruence and a day count forward from 15 October
1582, each shown right on dates whose weekday it knew from outside the
file: 49 ordinary rows on Tuesdays and both fairs on Thursdays; 52
Tuesdays in 1851, the three without a row being 4 February, 12 August,
and 30 December. It agreed.

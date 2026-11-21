# Check 004: duplicated rows among the roll's entries for 1851

*Created 20 November 2026; updated 20 November 2026.*
Plan: 001, task 4
Backs: [claim 004]
Instrument: the held roll at its recorded checksum, read with the Python standard library, CPython 3.12.3
Mutation: duplicate-entry
Frame: the calendar year, as the roll's dates give it, fixed by the roll reader's in_year
By: assistant, model withheld from this shipped example

## 1. What is checked

That three of the roll's 51 rows dated 1851 [Roll1851] repeat an earlier
row's date and kind, so that without them the roll's days of 1851 number
the note's forty-eight: what [claim 004] needs, to explain the
difference of three between the roll's count [claim 001] and the note's
figure [claim 002]. Built on [check 001], whose count of 51 rows this
check gates again against the roll's own rows, and on [claim 002], whose
forty-eight it takes as given: the program does not read the note. The
difference of three takes the note's forty-eight to count what the
roll's 51 counts, each day once over the calendar year 1851: a premise
imposed by the explanation under test. [claim 002] claims nothing about
the convention under which the note counted, which plan 001 leaves to a
plan of its own.

## 2. Construction

The program `python_project/src/check_004_duplicates.py` first confirms
that the roll it will read is the held file whose SHA-256 checksum
`source_documents/Roll1851_market_roll_sha256.txt` lists, and prints the
interpreter it runs under; a roll that is not the held file is not parsed.
It then reads the roll through the project's reader as (date, kind)
pairs in file order, takes the rows of 1851 through `in_year`, and
counts those whose (date, kind) pair has occurred earlier: a pair
entered k times counts k - 1. The gate has two halves: three rows of
1851 repeat an earlier row, and the distinct dates of 1851 number the
note's figure. The 51 and the 48 are written into the program beside
the claims that state them, and the three is computed from them.

A second route, past the reader: the held file's lines opening 1851-,
split on their commas, must be the reader's rows of 1851, row for row,
so that a line the reader merged, dropped, or misread shows as a
disagreement.

## 3. Sanity checks

Named in the program and reported by it, each with controls run through
the same function: the roll is the held file its checksum names (bytes
the list does not name fail that comparison); the roll holds the 51
rows of 1851 that [check 001] counts (50 rows and 52 fail); the reader's
rows of 1851 are the file's lines of 1851, row for row (a row dropped, a
row misread with the count kept, and a line the file holds twice and the
reader gives once each fail). The counting functions' controls, on
made-up rolls: one repeat is counted as one, three as three, a row
entered three times as two, and a date entered again with the other kind
is counted by its date and not by its date and kind. Through the reader:
the file's text, each date and kind taken once, with its first line of
1851 entered a second time, is read as one row more and counted as one
repeat. The gate's controls, on made-up rolls: among 51 rows of 1851,
two repeats fail it, three pass it, and four fail it; four repeats on 48
days fail it, and so do three repeats leaving 47 days, one date being
held under both kinds. The main assertion is the gate itself, through
the same function. The year's boundary is pinned from both sides through
`in_year`, the function the reader's rows of 1851 are taken by: 1
January and 31 December 1851 are in the year, 31 December 1850 and 1
January 1852 are not. The second route's lines of 1851 are held to those
rows by the row-for-row match.

## 4. Results

Run 20 November 2026, by assistant, model withheld from this shipped
example. The sanity checks and the controls passed; the main assertion
failed, and the program exited 1.

python = 3.12.3
rows_1851 = 51
needed = 3
control_one = 1
control_three = 3
duplicates_1851 = 0
repeated_dates_1851 = 0
days_1851 = 51

## 5. Discrepancies

The explanation needs three repeated rows of 1851, and the count the
program prints is 0, neither one nor two: no row of 1851 repeats an
earlier row's date and kind, or even its date, and the 51 rows of 1851
fall on 51 distinct dates, where [claim 002] has the note state
forty-eight.

## 6. Verdict

Not reproduced: duplicated rows do not explain the difference between
the roll's count and the note's figure, and [claim 004], which needs
them, is ruled out by this check. The check could have passed: its
controls, run through the same functions as the main assertion, count
planted repeats exactly, and a made-up roll of 51 rows of 1851 with three
repeats passes the gate that two and four fail. The probe, which runs
the program's `main()`, does not judge a program whose direct run fails,
and says so; the verdict is read from this record. The named mutation
acts on the reader's rows and not on the file, so that the row-for-row
match would take it for a fault in the reader; the repeat the
explanation needs would be in the file's own text, and the control
through the reader plants one. The check was audited for coverage
twice, the second time after its revision, and its revisions were then
read against the gaps that survived: the first audit, with its probe
reader's table, is kept in `prompt_logs/008_tasks_3_and_4.md`, and the
rest in `prompt_logs/009_writeup_opened.md`, with the gaps found and
their refuters' verdicts. What to check next: the note's counting
convention, which plan 001 sets aside to a plan of its own.

Second pass: a reader without the first pass's reasoning, given the held
CSV alone, searched the whole file, and the rows of 1851 within it, for
a row that repeats an earlier row, by three keys of its own: the exact
text, the parsed date with the kind, trimmed and lower-cased, and the
date alone. It found none, in 1851 or in the whole file, with controls
that found planted repeats, among them a row of 1852 entered twice,
found when the whole file was searched and not when 1851 alone was. It
agreed. Its output, with its controls, is kept in
`prompt_logs/008_tasks_3_and_4.md`, under *The second pass for check
004*.

# Check 003: duplicated rows in the roll's 1851 entries

*Created 6 September 2026; updated 6 September 2026.*
Plan: 001, task 4
Backs: [claim 004]
Instrument: the roll file at its committed revision, read with the Python standard library (3.11 or later)
Mutation: duplicate-entry
Frame: the calendar year, as the roll's dates give it
By: assistant

## 1. What is checked

That at least three rows of 1851 in the roll [Roll1851] repeat an
earlier row's date and kind, which is what [claim 004] needs to explain
a difference of three from the note's figure [claim 002].

## 2. Construction

The program `python_project/src/check_003_duplicates.py` reads the rows
dated in 1851 and counts those whose (date, kind) pair has occurred
before in the file; the assertion is that this count is at least three.

## 3. Sanity checks

The roll parses; the rows of 1851 number at least 51 (51 on the roll as
shipped, as [check 001] found; more under the planted duplicate). The
control: one 1851 row repeated in a scratch list of the distinct rows is
counted as one duplicate.

## 4. Results

Run 6 September 2026, by assistant, CPython 3.12.3; re-run by the
assistant in the researcher's role.

rows_1851 = 51
control_planted = 1
duplicates_1851 = 0

## 5. Discrepancies

The assertion fails: the count of duplicated rows is 0, not at least 3.
The pattern is total: no row of 1851 repeats another.

## 6. Verdict

Not reproduced: duplicated rows do not explain the roll's excess
over the note, and [claim 004] is ruled out. What to check next is the
note's counting convention, plan 002. Under the bound mutation, three
1851 rows repeated, the count is 3 and the assertion passes, so the
mutation flips the verdict to reproduced; the probe does not judge a
program whose direct run fails, and this was recorded from a run of the
program's assertions on the mutated list. Second pass: the assistant, in
the researcher's role, re-ran the program and read the same line.

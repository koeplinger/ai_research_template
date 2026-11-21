# The rule for counting the roll's market days of 1851: 20 November 2026

*Created 20 November 2026; updated 20 November 2026.*

**Analytical note**: construction, sanity checks, and second pass recorded
(CHECK_METHODOLOGY.md section 8), serving [check 001].

## What was asked

What counts as a market day of 1851 in the roll, fixed before
[check 001] reads the roll, so that the rule of reading is not chosen
after the count is seen. The roll was made by a program whose rule is
known (`prompt_logs/005_sources.md`), so this note fixes the rule of
reading, not the outcome. No commit evidences its date, the project
being committed once at its end, so [check 001] carries no
`Pre-registered` stamp.

## What was found

What is fixed:

- A row of the roll [Roll1851] is a market day of 1851 when its date
  falls in the calendar year 1851 (the year's boundary,
  `evidence_and_reasoning/terminology.md`), whatever its kind: a fair is
  a day held.
- The count is the number of such rows. The kinds are counted apart, as
  the roll's own kind column gives them.
- A second path: the counts for each calendar month, summed, give the
  same total. A second route for completeness: the held file's lines
  that open with the year, read without the reader.
- The decision rule: the count is reported as it comes out, and no row
  is left out after the fact for any reason. The stopping rule: one run.

Second pass: the rule was read once more against the roll's head before
the run. It reads only the date and kind columns, and the remark column
decides nothing.

## What follows

[check 001] reads the roll under this rule.

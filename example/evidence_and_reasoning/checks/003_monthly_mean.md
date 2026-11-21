# Check 003: the mean number of market days a month in 1851, derived

*Created 20 November 2026; updated 20 November 2026.*
Plan: 001, task 3
Backs: [claim 003]
Instrument: a written derivation from the count [claim 001] states, cross-checked by the monthly counts [check 001] states
Mutation: drop-month
Frame: the calendar year and its twelve calendar months, as [check 001] fixes them
By: assistant, model withheld from this shipped example

## 1. What is checked

That the mean number of market days a month in 1851 is 51 divided by
12, which is 4.25, as [claim 003] states: from the count of
[claim 001], over the twelve calendar months of the year. The count is
taken as [claim 001] establishes it: whether the roll holds that count is
[check 001]'s to show, not this derivation's. Step 4 checks that the
numerator is the count of the year's twelve months, by the monthly counts
[check 001] gates against the file's own lines.

## 2. Construction

A written derivation, which any reader can follow:

1. Take the count of the roll's market days in 1851 from [claim 001]:
   51. The divisor is the year's twelve calendar months, imposed with
   the year's boundary, and must be the number of monthly counts step 4
   adds.
2. Divide: 51 / 12 = 4.25, exactly, since 12 x 4 = 48 and the remainder
   3 is 0.25 of 12.
3. Read the quotient back: 4.25 x 12 = 51, the count of step 1, which
   checks the division.
4. A second route to the numerator: add the twelve monthly counts that
   [check 001] states in its part 4, which its program gates, month by
   month, against the held file's own lines (its part 2); the sum must be
   the same 51.

## 3. Sanity checks

The mean lies between the least and the greatest monthly count, 3 and
5, both ends included.

## Executions

### 20 November 2026, by assistant, model withheld from this shipped example

Results: the count of [claim 001], 51; 51 / 12 = 17/4 = 4.25, exactly;
read back, 4.25 x 12 = 51, the count; the twelve monthly counts
[check 001] states in its part 4, 4, 3, 4, 5, 5, 4, 5, 3, 5, 5, 4 and 4,
sum to 51, the same count by its independent route; and the mean lies
between the least and greatest month, 3 and 5.

Discrepancies: none.

Verdict: proved: the mean number of market days a month in 1851 is
4.25.

The planted alteration, drop-month, on the project's side: March's 4
removed from a scratch copy of the transcribed monthly counts. Followed
again, step 4 summed them to 47, not 51, and flagged the disagreement:
it was caught.

Second pass, by a subagent of the assistant: a reader without the first
pass's reasoning, given the held CSV and the rule that a row is a day
held, counted the rows of 1851 month by month, twelve counts that sum to
51, and divided by the twelve months as an exact fraction: 51 / 12 = 17/4
= 4.25. It agreed. Its output is kept in
`prompt_logs/008_tasks_3_and_4.md`, under *The second pass for check
003*.

### 20 November 2026, by assistant, model withheld from this shipped example

The second execution, after the probe reader of round 008 found the first
plant on step 4's cross-check data rather than on the count the claim
takes: the plant moved to step 1, the procedure unchanged.

Results: as in the first execution: 51 / 12 = 17/4 = 4.25, read back to
51, the twelve monthly counts summing to 51.

Discrepancies: none.

Verdict: proved.

The planted alteration, drop-month, on the project's side: the count
step 1 takes, in a scratch copy, changed to 47, the count with March's
four rows removed. Steps 2 and 3 then gave 47/12, about 3.917, read back
to 47; step 4's twelve monthly counts summed to 51, not 47, and flagged
the numerator. It was caught, at step 4.

### 20 November 2026, by assistant, model withheld from this shipped example

The third execution, under the procedure as amended after the coverage
audit of round 016: the divisor held to the number of monthly counts, and
the sanity check's two ends stated.

Results: as in the first execution: 51 / 12 = 17/4 = 4.25, read back to
51, the twelve monthly counts summing to 51; the divisor, 12, is the
number of those counts; and 4.25 lies between 3 and 5.

Discrepancies: none.

Verdict: proved.

The planted alterations, on the project's side, in scratch copies: the
divisor changed to 11 and to 13, each flagged at step 1, there being
twelve monthly counts; and the quotient changed to 4.52, flagged at step
3, since 4.52 x 12 = 54.24, not 51. The sanity check, run from both of its
sides: a mean of 36/12 = 3 and one of 60/12 = 5 pass it, and 35/12 and
61/12 fail it.

The coverage audit of this procedure, with its gaps and their refuters'
verdicts, is kept in `prompt_logs/016_closure_checklist.md`.

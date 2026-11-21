# Plan 001: the roll's count for 1851 against the note's figure

*Created 20 November 2026; updated 21 November 2026.*
Status: CLOSED 21 November 2026, verdict CONFIRMED
Serves: H-A
Prerequisites: none

**Hypothesis plan.**

## The aspect, isolated

Whether the roll's count of market days for 1851 differs from the count
the note states for that year; where it does, what the roll alone can
decide about the difference; and what the roll's weekdays of 1851 hold
against what the note states of them. Not why the note's figure is what
it is, nor what the note means by its Tuesdays or its interruptions,
which the roll cannot decide, and not the count for 1852.

## Hypothesis

The roll's count of market days held in 1851, read under the calendar
year, differs from the count the note states for 1851 (H-A).

## Design

The roll [Roll1851] is the source of record for the count, read by a
program; the note [Note1851] is the source of record for the stated
figure, collated by a written procedure. The year's boundary is the
calendar year (imposed: a choice of this project, the roll being
synthetic). A market day is a row of the roll, whatever its kind
(imposed: the rule of reading, fixed in a protocol note before the count
is run, so that it is not chosen after the count is seen). The note's
figure is what the collation reads (derived). A difference is the
roll's count less the note's figure; its explanations are tested only
where the roll's own rows can decide them.

## Tasks

1. **Count the roll's rows for 1851** by a program that fails under a
   shifted year and under a dropped month; produces check 001 and
   claim 001.
2. **Collate the note's stated figure** against the note by a written
   procedure; produces check 002 and claim 002.
3. **Derive the mean number of market days a month** from the count, by
   a written derivation cross-checked by the program's monthly counts;
   produces check 003 and claim 003.
4. **Test duplicated rows as the explanation** of any difference, by a
   program; produces check 004 and claim 004.
5. **Write the write-up** under `paper/`, on the roll's count and
   weekdays against what the note states of them, reviewed before it is
   released; produces the write-up and its review.
6. **Read the roll's weekdays against what the note states of them**, by a
   program that reads each row's weekday, a date's weekday being that of
   its ISO form on the Gregorian calendar (imposed), and finds the
   Tuesdays of 1851 with no row; produces check 005 and claim 005. It is
   made before task 5's review, so that the review reads what it adds.

## Sanity checks

Every check holds when the tasks are done: each program re-run, the one
that fails by design read from its record, and each written procedure
not invalidated by what changed. The round check is clean; the indexes
are in step.

## Deliverables

Claims 001 to 005 and checks 001 to 005; the protocol note that fixes
the rule of reading; the tension rows any divergence from the note calls for; the
write-up under `paper/` and its review.

## Confirmation and refutation

CONFIRMED if check 001 reaches *reproduced* for a count of the roll's
1851 rows that differs from the figure check 002 finds the note to
state, its verdict *confirmed*. REFUTED if the two are equal. A plan
carried out as designed whose checks decide neither way (a count not
reproduced, or a figure not confirmed) closes INCONCLUSIVE; one whose
execution stopped closes ABANDONED.

## Out of scope

Why the note's figure is what it is, beyond the explanations the roll's
own rows can decide: the note's counting convention, set aside to a plan
of its own. What the note means by its Tuesdays or its interruptions,
which the roll cannot decide. The count for 1852.

## Execution status

| Task | State | Date | Note |
|---|---|---|---|
| 1 | done | 20 November 2026 | [check 001] reproduces 51 |
| 2 | done | 20 November 2026 | [check 002] confirms forty-eight |
| 3 | done | 20 November 2026 | [check 003] derives 4.25 |
| 4 | done | 20 November 2026 | [check 004] fails by design: no repeated row |
| 5 | done | 20 November 2026 | `paper/2026-11-20_market_days_1851.md`, reviewed, rebuilt on its review at prompt 014, and released at prompt 015; the weekdays put in at prompt 012, a deviation from the plan as engaged |
| 6 | done | 20 November 2026 | added at prompt 011, decision 3, a deviation from the plan as engaged; [check 005] reproduces the weekdays |

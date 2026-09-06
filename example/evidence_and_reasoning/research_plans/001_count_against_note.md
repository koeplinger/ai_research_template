# Plan 001: the roll's 1851 count against the note's

*Created 6 September 2026; updated 6 September 2026.*
Status: CLOSED 6 September 2026, verdict CONFIRMED
Serves: H-A
Prerequisites: none

**Hypothesis plan.**

## The aspect, isolated

Whether the roll's count of market days held in 1851 equals the
count the note states, and nothing else: not why the two might differ
beyond what the roll itself can rule out, and not the count for
1852. No other plan is engaged.

## Hypothesis

The roll's count of market days held in 1851, read under the
calendar year, differs from the count the note states for 1851 (H-A).

## Design

The roll [Roll1851] is the source of record for the count, read by a
program; the note [Note1] is the source of record for the stated figure,
collated by a written procedure. The year boundary is the calendar year
(imposed: a choice of the example, stated in the roll's own dates);
the count is of rows held, fairs included (derived from the roll's
`kind` column, which records both kinds as days held).

## Tasks

1. **Count the roll's 1851 rows by a program** that fails under a
   shifted year and under a dropped month; produces [check 001] and
   [claim 001].
2. **Collate the note's stated figure** against the note by a written
   procedure; produces [check 002] and [claim 002].
3. **Derive the monthly mean** from the count by arithmetic, cross-checked
   by the program's monthly sums; produces [claim 003].
4. **Rule out duplicated rows** as the explanation of any difference, by a
   program; produces [check 003] and [claim 004].
5. **Read the weekdays of the 1851 rows** by a program, and the Tuesdays
   of the year that have none; produces [check 004] and [claim 007].

## Sanity checks

Every check holds at closure: the three programs re-run (the one that
fails by design read from its record) and the procedure
not invalidated by what changed; the round check is clean; the indexes
are in step.

## Deliverables

Claims 001 to 004, checks 001 to 003, the tension row the difference
calls for, and a released note under `paper/`; from task 5, claim 007
and check 004, and the tension row the weekdays call for.

## Confirmation and refutation

CONFIRMED if the gated count of the roll's 1851 rows differs from the
note's collated figure; REFUTED if the two are equal. An outcome that
decides neither way (a count the program cannot reach, or a figure the
note does not state) closes ABANDONED with that outcome as its reason.

## Out of scope

The note's counting convention, and any explanation of the difference
that the roll alone cannot decide: plan 002 holds it.

## Execution status

| Task | State | Date | Note |
|---|---|---|---|
| 1 | done | 6 September 2026 | [check 001] passes; 51 rows |
| 2 | done | 6 September 2026 | [check 002] executed once; the note states 48 |
| 3 | done | 6 September 2026 | 4.25 a month, two routes agree |
| 4 | done | 6 September 2026 | [check 003]: no duplicated row |
| 5 | done | 6 September 2026 | [check 004]: Tuesdays and two Thursdays; three Tuesdays without a row; added while engaged, prompt 006 |

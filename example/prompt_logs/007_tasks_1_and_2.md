# Prompt 007: plan 001 engaged; tasks 1 and 2

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
Engage plan 001. Then do tasks 1 and 2: the count, and the note's
figure. Fix the rule of reading before the count is run.
--- PROMPT END ---

## What was done

Plan 001 engaged at the prompt's direction: its `Status:` line reads
ENGAGED 20 November 2026, and the plan index's status column ENGAGED.
The pinned environment was built at the project's root by the main
thread, `.venv`, from `python_project/requirements.txt`: CPython 3.12.3,
pytest 8.3.3.

**Task 1, the count.**

- The roll reader, `python_project/src/roll.py`, a foundation module the
  checks of the roll import, and its tests,
  `python_project/tests/test_roll.py`, five, all passing.
- Before any check read the roll, the rule of reading, in the analytical
  note `evidence_and_reasoning/notes/2026-11-20_counting_protocol.md`:
  a row of 1851 is a market day whatever its kind; one run; no row left
  out after the fact. It carries no `Plan:` line and is frozen on
  writing.
- [check 001], its record and its program, written, then probed:
  `tools/falsifiability_probe.py` applied each named mutation and the
  check failed under each. Run: it reproduces the count, 51 rows of
  1851, 49 ordinary and 2 fairs, on 51 distinct days. The concordance
  check, `tools/check_concordance.py`, finds the record and the program
  in agreement.
- [claim 001], written OPEN, backed by [check 001], its frame the
  calendar year.

**Task 2, the note's figure.**

- [check 002], a written procedure, its record and two executions. The
  note's figure is collated as written: "forty-eight", on page 1, with
  no count for 1852 on page 2. Its named alteration, alter-figure, was
  planted on the project's side, the held note never being edited, and
  was caught.
- [claim 002], written OPEN, backed by [check 002].

**The readers**, played by subagents that wrote nothing: two probe
readers, a coverage auditor of [check 001], and two second-pass readers
who had not seen the first pass, with a refuter for each gap or concern
they returned, 45 subagents in all; then a second coverage audit of the
revised [check 001], with 16 refuters, 17 more. The share of usage they
took is not known: the harness reports none. The tree was recorded by
the checksum of every file before each fan-out and compared after: no
file had changed.

What the readers found, and what was done about it:

- The two second passes agree with the first: a fresh count from the
  held CSV, 51 rows of 1851, 49 ordinary and 2 fairs; a fresh reading of
  page 1, "forty-eight", quoted word for word.
- The first probe reader and the first audit found [check 001] weaker
  than its record said: a second path to the total that could not fail,
  being the same count regrouped; the checksum and the interpreter
  stated and never read; no assertion that the 51 rows fall on 51 days;
  sanity tests never shown to fail; and every named mutation lowering
  the count, none raising it. The program and its record were revised:
  the checksum read against the checksum list; the interpreter printed;
  distinct days asserted; the second route made the file's own lines,
  month by month, read past the reader; a control for each sanity test;
  and duplicate-entry, already in the mutation set, named and bound. The
  reader's docstring still named the roll's third column *note*; it now
  names *remark*.
- The second audit found no MISMATCH. Its surviving gaps asked for five
  more controls, a test of the reader's refusal of a date it cannot
  read, and two sentences of the record narrowed; all were made. A
  control added then ended in an exception under two mutations, which
  the probe reported as ERROR rather than CAUGHT; it was rewritten to
  fail by assertion, and the probe again reads CAUGHT for all three.
- The probe reader of [check 002] found its procedure untested in four
  places: the Tuesday clause not transcribed in full, the absence of a
  count for 1852 without a positive control, the checksum step never
  shown to fail, and the page pinpoints never checked. The procedure was
  revised with a control for each, and its second execution records
  them.
- Both probe readers found dependencies that no mutation in the set
  alters: a row's kind, and a phrase of the note other than a figure.
  Amending the set is the researcher's: decision 3 below.

The audits, the probe readers' tables, the second passes, and every gap
with its refuter's verdict are below, as each returned them. The round
check: no finding.

**Brought, four decisions**, each with its options and the assistant's
recommendation after them:

1. **The register of [claim 001].** VERIFIED: a gated check that
   reproduced the count, probed under three mutations, twice audited,
   with a second pass that agreed. Options: (a) VERIFIED, `Verdict:
   reproduced`, `Verified-by: assistant, a re-count from the held CSV by
   a reader without the first pass's reasoning`; (b) leave it OPEN. The
   assistant recommends (a).
2. **The register of [claim 002].** ATTESTED: what the note says, at a
   locus, collated, with a second pass that agreed. Options: (a)
   ATTESTED, `Verdict: confirmed`, `Verified-by: assistant, a re-reading
   of page 1 by a reader without the first pass's reasoning`; (b)
   VERIFIED, on the same gated collation, still saying only what the
   note states; (c) leave it OPEN. The assistant recommends (a).
3. **Two names for the mutation set** (`CHECK_METHODOLOGY.md`, Slots, and
   `[vocab] mutations`): relabel-kind, one row's kind changed between
   ordinary and fair; and alter-wording, a phrase of a transcribed
   passage changed. Options: (a) both; (b) one; (c) neither. The
   assistant recommends (a), so that [check 001] and [check 002] can be
   shown to fail on the kind and on the note's wording.
4. **A tension row**, the roll against the note on the count, proposed
   while [claim 001] is the assistant's checked claim:
   `| T001 | the roll holds 51 market days in 1851, [claim 001] | the note
   states forty-eight market days for 1851, [Note1851, p. 1] | that the
   note's counting convention is unknown, set aside to a plan of its own
   | live |`. Options: (a) enter it as proposed; (b) reword it; (c) do
   not enter it. The assistant recommends (a), once decision 1 is
   ruled.

### The readers' output

#### The probe's reader for check 001, as first written

```
Check 001: python_project/src/check_001_count_1851.py (record: evidence_and_reasoning/checks/001_count_1851.md). It backs claim 001 (evidence_and_reasoning/claims/001_count_1851.md).
The mutation set (CHECK_METHODOLOGY.md, Slots, l.523) is shift-year, drop-month, duplicate-entry and alter-figure. The check names shift-year and drop-month (program l.9, record l.7, MUTATIONS l.51-54).

Dependency | Mutation that alters it | Named by the check | Matrix cell
---|---|---|---
The roll's rows, derived (claim l.16): the date each row bears | shift-year: every date moved one year later (program l.43-44), so the 1851 rows leave the year and the count goes to 0 | yes | CAUGHT
The roll's rows, derived: which rows are held | drop-month: the rows of March 1851 removed (program l.47-48), so the count goes from 51 to 47 | yes | CAUGHT
The roll's rows, derived: how many times a row is held | duplicate-entry: rows repeated | no | no cell (not run)
The roll's rows, derived: each row's kind, ordinary or fair, on which the 49 and the 2 rest (claim l.14-15; "the kinds are the roll's own", record l.30) | none. drop-month and duplicate-entry remove or repeat whole rows; nothing relabels a row | - | -
The year's boundary, the calendar year: imposed by the researcher's choice (claim l.16-18). It is also the claim's Frame (claim l.10), fixed by roll.in_year (program l.8; record l.8, l.27-29) | none | - | -
That a fair is a day held: imposed by the rule of reading (claim l.15-18), the convention the counting protocol fixed (record l.16-18) | none | - | -

The two unmutated runs (direct: passes, wrapped: passes) are the baseline each CAUGHT is read against. No row of the matrix is MISMATCH or NOT_COMPUTED.

Every dependency no mutation alters:
1. The year's boundary, which is also the Frame. shift-year moves the rows a whole year and does not touch in_year. Its CAUGHT shows that the count reads the rows' dates. It does not show where the count puts the start and end of 1851. The boundary has controls on both sides of both ends (program l.88-91): 1 January and 31 December 1851 are in the year, 31 December 1850 and 1 January 1852 are not. A control is not a mutation, though. Nothing in the set moves the edge (for example a year starting on 25 March, or every date moved one day across 31 December / 1 January), so the matrix has no cell for it.
2. The rule of reading. The program carries it only by not filtering the count by kind (program l.72). No mutation reads a fair as not held, which would bring the total to 49.
3. Each row's kind. No mutation relabels a row. The split assertions (program l.75-76) are the only ones that would catch a fair relabelled as ordinary with the total still 51, and no mutation in the set tests them that way.

Every named mutation that alters nothing the claim depends on (a misfiled robustness check): none.
- shift-year alters the dates of the 1851 rows.
- drop-month is glossed in Slots only as "one month's rows removed". The program pins it to March 1851 (l.48), which is inside the frame. Pinned to a month of 1852, it would alter nothing the claim depends on (the claim says nothing about 1852, claim l.23) and would be a misfiled robustness check.

The two set mutations the check does not name:
- alter-figure changes a figure in a transcribed passage. In this project that is the note (Slots l.521-522), which claim 001 disclaims (claim l.16, l.23-24). Check 001 is right to leave it out.
- duplicate-entry does alter the roll's rows. Without it, no planted mutation pushes the count up: both named mutations push it down, to 0 and to 47.

Written procedure: none here. Check 001 is a program with a printed verdict (CHECK_FORM, CHECK_METHODOLOGY.md l.521). Its alterations act on the rows that construct() returns (program l.43-61), and whether they were caught is read from the matrix, not from the record. The written procedure in the probe's NOTE is check 002 (evidence_and_reasoning/checks/002_collate_note.md). It is outside this one-check reading and was not read.

One unverified concern about a matrix cell: _shift_year (program l.44) raises ValueError on a row dated 29 February 1852, because 1853 has no 29 February (confirmed by an in-memory run). The sanity check allows rows dated 1852 (program l.66). The roll was not read here. If it holds such a row, the shift-year run ends in an exception, not a failed assertion, and the matrix's CAUGHT does not say which of the two it was.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The year's boundary, the calendar year (imposed), which is also the claim's Frame fixed by roll.in_year: no mutation in the set alters it. shift-year moves the rows, not in_year. The four boundary controls cover both sides of both ends but are controls, not mutations, so the matrix has no cell for a moved boundary. Refuter: narrowed.
2. The rule of reading (imposed convention: every 1851 row, fairs included, is a market day held): no mutation alters it. The program carries it only by not filtering the count by kind, and no mutation reads a fair as not held (total 49). Refuter: stands.
3. Each row's kind (derived; the kinds are the roll's own), on which the 49/2 split rests: no mutation relabels a row, so the split assertions are never tested against an alteration that keeps the total at 51. Refuter: stands.
4. Not a misfile, a concern: duplicate-entry alters the roll's rows (a row held more than once) but check 001 does not name it. No planted mutation pushes the count up; both named ones push it down (to 0 and to 47). Refuter: stands.
5. Unverified: _shift_year raises ValueError on a row dated 29 February 1852, and the sanity check allows rows dated 1852. The roll was not read, so the matrix's shift-year CAUGHT could be an exception, not a failed assertion. Refuter: narrowed.
```

#### The probe's reader for check 002, as first written

```
Check 002 (evidence_and_reasoning/checks/002_collate_note.md) is a written procedure that backs claim 002 (evidence_and_reasoning/claims/002_note_states_48.md). Its header names one mutation, alter-figure (check line 7). The claim's body classifies one input as derived, "what the note says, derived from its collation" (claim line 17), and classifies nothing as imposed. The table splits that one input into the parts that can each be false on their own. The mutation set and what each name does are at CHECK_METHODOLOGY.md line 63 and in the Slots row at line 523.

| Dependency | Mutation that alters it | Named by the check | Matrix cell |
|---|---|---|---|
| 1. Input, derived: the count the note gives at p. 1, "forty-eight" (claim 13-14) | alter-figure | yes | none; NOTE (written procedure). Executions: planted as "forty-seven" in a scratch copy of the claim's statement; caught (check 54-59) |
| 2. Input, derived: the year the same passage names, "1851" (claim 13; check 35-36) | alter-figure (1851 is a figure in the same transcribed passage) | yes | none; NOTE. Executions: not planted. The one plant changed the count, which is part of the same assertion |
| 3. Input, derived: "held on Tuesdays throughout the year with the customary interruptions at the turn of the year and in the depth of winter" (claim 14-16) | none. alter-figure changes a figure, and this clause has no figure. The other three mutations alter the roll | n/a | none; NOTE. Nothing planted |
| 4. Input, derived: "the roll shows no day held on any other day of the week" (claim 16-17). This is the note's own negative; the claim only says the note contains it, so collating it is a positive reading | none | n/a | none; NOTE. Nothing planted |
| 5. Input, not classified (it sits under "What is not claimed"): the note states no count for 1852 [Note1851, p. 2] (claim 23-24; check 15; step 3 at 28-29). This is a negative | none. No mutation in the set adds a count; alter-figure could change the year 1852 but not the absence | n/a | none; NOTE. Nothing planted |
| 6. Frame, the form consulted: source_documents/Note1851_market_days_note.md as held, at the SHA-256 its source-index row records (check 6; step 1 at 22-24; CHECK_METHODOLOGY.md 169) | none. No mutation swaps or alters the source. Step 1's checksum test fixes this frame | n/a | none; NOTE |
| 7. Frame, the page numbering: the page marks p. 1 and p. 2 that the claim's pinpoints cite (claim 13, 24; check 25, 28, 35-36) | none. No mutation moves a page mark or a pinpoint. The sanity check fixes this frame (two marks, in order; the paragraph under the first names 1851) | n/a | none; NOTE |

Three things are not dependencies and get no row:
- The roll itself. The claim says "nothing about whether forty-eight is right" (claim 22).
- The note author's counting convention, which the claim also disclaims (claim 22-23). With it goes the calendar in which the note counts 1851 and "the turn of the year". The claim repeats the note's labels without converting them, so nothing is compared across frames.
- The check's own rule that the count is transcribed in words (check 26-27, 36-37). The claim says nothing about how the note writes the number.

**Every dependency no mutation alters**
- **Row 3, the Tuesday statement with its interruptions.** The record also does not transcribe this clause. "held on Tuesdays" sits outside the quotation marks. "throughout the year" appears in the claim (14) and in the check's §1 (13), but nowhere in the transcription (check 43-48). The record still reports no discrepancy (check 50). From the record alone you cannot tell whether the note says "throughout the year".
- **Row 4, "no day held on any other day of the week".**
- **Row 5, the absence of an 1852 count.** This is also a negative with no positive control. Step 3 reads page 2 only, and the check names no control that the same reading would have to find, such as a planted case or a known positive (CHECK_METHODOLOGY.md 224-228). The record quotes the p. 2 sentence "A count of the market days of 1852 is left to a later note." (check 47-48). That sentence is evidence for the absence, but it is not a control.
- **Row 6, the held copy at its checksum.** An assertion fixes the frame, as §5 requires, but no planted alteration shows that this assertion can fail.
- **Row 7, the page marks.** The sanity check fixes them. No mutation in the set alters a pinpoint, although §5 allows a plant there (CHECK_METHODOLOGY.md 255-256). Steps 2 and 3 also pick their pages themselves and never say to check the claim's pinpoints against them.

**Every named mutation that alters nothing the claim depends on (a misfiled robustness check)**
- None. The check names only alter-figure, and it alters rows 1 and 2.
- shift-year, drop-month and duplicate-entry alter only the roll, which this claim disclaims. For this claim they would be robustness checks (CHECK_METHODOLOGY.md 266-272), and the check is right not to name them.
- The matrix has one row, [check 001], with shift-year and drop-month CAUGHT. That row belongs to another check and says nothing about claim 002.

**Where the alteration is planted, and what the record must say when it is caught**
- **Where:** on the project's side of the comparison. That means a scratch copy of claim 002's statement, quotation or pinpoint (CHECK_METHODOLOGY.md 249-257), and never the held note, for two reasons:
  - The note is never edited (check 54-55).
  - An altered copy of the note would fail step 1's checksum. The catch would then come from the checksum, not from reading p. 1.

  For alter-figure, the plant is a figure from the p. 1 passage as the claim states it: the count (row 1) or the year (row 2). The record did this, changing "forty-eight" to "forty-seven". A plant for rows 3 to 5 or row 7 would go on the same side, but no mutation in the set makes such a change.
- **What the record must say:** a dated entry under ## Executions that names who followed the procedure (CHECK_METHODOLOGY.md 55-59). It must give:
  - the mutation's name
  - where it was planted
  - the planted value
  - what the procedure read from the unaltered note at p. 1
  - that step 4 recorded the difference, so the alteration was caught

  The 20 November 2026 entry says all of these (check 54-59).
- **The matrix cannot show the catch.** For a written procedure, the tools report only a missing or unrecognized Mutation: line (CHECK_METHODOLOGY.md 496-499). The NOTE reports neither. Whether the alteration was caught is read from the Executions section, which records it. No MISMATCH or NOT_COMPUTED row concerns check 002.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. Dependency no mutation alters: the day-of-week statement, 'held on Tuesdays throughout the year with the customary interruptions at the turn of the year and in the depth of winter'. alter-figure changes only a figure, and this clause has none; the other three mutations alter the roll. Refuter: narrowed.
2. The record does not transcribe the Tuesday clause. 'held on Tuesdays' sits outside the quotation marks, and 'throughout the year', which the claim and the check's §1 both state, is missing from the transcription. The record still reports no discrepancy, so whether the note says 'throughout the year' cannot be read off the record. Refuter: stands.
3. Dependency no mutation alters: 'the roll shows no day held on any other day of the week'. Refuter: narrowed.
4. Dependency no mutation alters: the note states no count for 1852 [Note1851, p. 2]. No mutation in the set adds a count, and alter-figure could change only the year 1852, not the absence. Refuter: narrowed.
5. Negative without a control: the absence of an 1852 count rests on step 3's reading of page 2 alone, and no control is named that the same reading would have to find. The quoted p. 2 sentence deferring the count is evidence for the absence, not a control. Refuter: stands.
6. Dependency no mutation alters: the frame of the form consulted, source_documents/Note1851_market_days_note.md as held at its source-index SHA-256. Step 1's checksum test fixes it, but no planted alteration shows that this test can fail. Refuter: stands.
7. Dependency no mutation alters: the page-numbering frame, the page marks p. 1 and p. 2 that the claim's pinpoints cite. The sanity check fixes them, but no mutation in the set alters a pinpoint, and steps 2 and 3 pick their pages themselves without checking the claim's pinpoints against them. Refuter: stands.
```

#### The coverage audit of check 001, as first written

```
Paths: C = evidence_and_reasoning/claims/001_count_1851.md; R = evidence_and_reasoning/checks/001_count_1851.md; K = python_project/src/check_001_count_1851.py; L = python_project/src/roll.py (imported by K); S = source_documents/Roll1851_market_roll/Roll1851_market_roll.csv. Line numbers are file lines.
"Rerun": I ran K's main() in memory (python3 -B -I, CPython 3.12.3, nothing written). Result: 13 PASS, 0 FAIL, exit 0, and the RESULT values match R:48-52 exactly.
"In memory": rows changed in memory, then passed through K's own sanity() and verify().

| # | Assertion | Where stated | Class | Evidence |
|---|---|---|---|---|
| 1 | The roll holds 51 rows dated 1851; the count is the number of such rows | C:1, C:14; R:13, R:15-16, R:29-30, R:48; K:12 | GATED | K:74 "main: the roll holds 51 rows dated 1851" (n == 51). Rerun gives 51 (S:2-52). In memory it fails under shift-year (0), drop-month (47), one added row not in the roll (52), and with the fairs left out (49) |
| 2 | 49 of them are ordinary days | C:14; R:13-14, R:49; K:12 | GATED | K:75 "main: 49 of them ordinary". Rerun gives 49. Fails under shift-year (0), drop-month (45), and with the 1851-05-15 fair relabelled ordinary (50) |
| 3 | 2 of them are fairs | C:14-15; R:14, R:50; K:12 | GATED | K:76 "main: 2 of them fairs". Rerun gives 2 (S:20, S:41). Fails under shift-year (0), the relabelling (1) and fairs left out (0). Still passes under drop-month |
| 4 | An 1851 row is counted whatever its kind (the operational half of the rule of reading) | R:16-17; C:15-18 | GATED | K:72 filters on in_year only. K:74 needs 51 = 49 + 2, so a count without the fairs fails it (49, in memory) |
| 5 | Every row counted is dated 1851 | R:14; K:12-13 | GATED | K:85 "one for many: every row counted is dated 1851". It repeats in_year's own test (L:41), so it fails only if in_year changes (in memory, a 25 March year start fails it). It passes under both declared mutations |
| 6 | No row dated 1851 is left out; second route: the held file's lines that open with "1851-", read past the reader | R:15, R:31-33; K:13 | GATED | K:86 "one for many: no row dated 1851 is left out" (line count at K:83-84 == n). Rerun gives 51 lines. Fails under drop-month (51 vs 47), shift-year (51 vs 0) and one added row (51 vs 52) |
| 7 | A second path to the total: the twelve monthly counts, summed | R:30-31 | GATED | K:80 "second path: the twelve monthly counts add to the same total". It cannot fail: both sides filter with in_year and every date has a month from 1 to 12, so the sum equals n for any rows. 0 of 20,000 random date lists differ, and it still passes under both mutations (0 = 0, 47 = 47). It is not independent of #1 |
| 8 | monthly_1851 = 4,3,4,5,5,4,5,3,5,5,4,4 | R:51 | PRINTED_ONLY | value() at K:79, shown in the RESULT line (K:107). No condition tests the vector, only its sum (K:80). Rerun prints the same vector, which agrees with S (Feb S:6-8 and Aug S:32-34 hold 3 each) |
| 9 | monthly_sum = 51 | R:52 | GATED | K:80 (== n) together with K:74 (n == 51). Rerun gives 51 |
| 10 | Every assertion passed | R:46 | GATED | K:104-108 print "all assertions passed" and "RESULT: reproduced", and exit 0, only when no condition failed. The rerun agrees |
| 11 | A row belongs to 1851 when its date falls in the calendar year 1851; in_year fixes this, and the count uses it | C:10, C:16-17; R:8, R:27-29, R:39-40; K:8; L:9-11 | GATED | K:88-91, four controls through roll.in_year (L:39-41), the same function the count calls at K:72 and K:78. In memory, moving either edge of in_year by one day fails that edge's own control and nothing else, because S has no row closer to the edges than 1851-01-07, 1851-12-23 and 1852-01-06 |
| 12 | The dates are the roll's own, taken as written ("as the roll's dates give it") | C:10; R:8; K:8; L:6 | ATTESTED | S:1 column "date"; ISO dates at S:2-105, parsed by date.fromisoformat (L:35) |
| 13 | 1 January 1851 is in the year | R:40 | GATED | K:88 "control: 1 January 1851 is in the year". In memory it fails when in_year starts a day late |
| 14 | 31 December 1850 is not | R:41 | GATED | K:89 "control: 31 December 1850 is not". In memory it fails when in_year starts a day early |
| 15 | 31 December 1851 is in the year | R:40 | GATED | K:90 "control: 31 December 1851 is in the year". In memory it fails when in_year ends a day early |
| 16 | 1 January 1852 is not | R:41 | GATED | K:91 "control: 1 January 1852 is not". In memory it fails when in_year ends a day late |
| 17 | The calendar-year boundary is a choice imposed by the researcher (the project), set down in evidence_and_reasoning/terminology.md | C:16-18; R:28; L:10-11 | NOT_COMPUTED | A statement of convention. Nothing in K or L reads terminology.md. (The boundary itself is #11) |
| 18 | Each row counted is a market day held; a fair is a day held (rule of reading) | C:1, C:15-16, C:18; R:1, R:16-17; K:2 | NOT_COMPUTED | An imposed reading. Nothing in K reads or tests it |
| 19 | The 51 rows fall on 51 distinct days ("one row per day held"), so 51 rows are 51 market days and the 49 ordinary rows are 49 days | C:1, C:14; L:6 | NOT_COMPUTED | No condition tests that dates are distinct, and K:68 compares with sorted(), so a repeated date passes. S does have 51 distinct 1851 dates, but in memory, changing 1851-01-14 to 1851-01-07 (51 rows on 50 days) still gives "reproduced" |
| 20 | The rule of reading was fixed before this check read the roll | R:16-17 | NOT_COMPUTED | K records no order of events |
| 21 | The rule is set down in evidence_and_reasoning/notes/2026-11-20_counting_protocol.md | R:17-18 | NOT_COMPUTED | A pointer that nothing in K reads |
| 22 | The roll is synthetic, made by a program | C:22-23; R:18-19 | NOT_COMPUTED | S says nothing about its origin, and nothing in K reads such a statement |
| 23 | That program's rule is known | R:19 | NOT_COMPUTED | Nothing in K states or reads the rule |
| 24 | So the protocol fixes the rule of reading and not the outcome | R:19-20 | NOT_COMPUTED | K reads no protocol |
| 25 | What is read is the held roll at its recorded checksum | R:6; K:7 (path at K:56, L:20) | NOT_COMPUTED | No checksum is computed or compared in K or L, and no function reads BASIS (K:56). The sha256 of S now is 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3; the recorded value is outside the files I may read |
| 26 | The roll is read with the Python standard library | R:6; K:7 | PRINTED_ONLY | Computed by code that imports only the standard library and roll (K:18-23, L:13-17). Not printed, and nothing asserts it |
| 27 | The run used CPython 3.12.3 (run of 20 November 2026) | R:6, R:45-46; K:7 | NOT_COMPUTED | K prints neither the interpreter nor the date. sys is imported at K:21 and never used. (My rerun also happened to use CPython 3.12.3) |
| 28 | The program reads the roll through roll.py as (date, kind) pairs in file order | R:24-26; L:7-8 | PRINTED_ONLY | Computed: construct() returns roll.read_rows() (K:59-61, L:24-36). Not printed, and no condition tests file order (K:68 tests date order, which is different) |
| 29 | The reader refuses a row it cannot read rather than skipping it | R:26-27; L:8-9, L:25 | NOT_COMPUTED | The refusal branches (L:29-30, L:33-34, and fromisoformat at L:35) are never reached in K's run, and no control feeds the reader a bad row. In memory they do raise ValueError for kind "market", date 1851-02-30, a row with no kind, and a header naming "note" |
| 30 | The count is derived from the roll's rows and nothing else | C:16 | PRINTED_ONLY | Computed at K:59-61 and K:72-73. The RESULT line shows the value, not where it came from. K:86 ties the number to S's lines, but not its provenance |
| 31 | The kinds are the roll's own, ordinary and fair | R:30; L:7, L:21 | ATTESTED | S:1 column "kind": "ordinary" on 100 rows (e.g. S:2), "fair" at S:20, S:41, S:71, S:94 |
| 32 | Every row is dated 1851 or 1852 | R:37-38 | GATED | K:66 "sanity: every row is dated 1851 or 1852". Fails under shift-year (1853 appears) |
| 33 | Every kind is ordinary or fair | R:38 | GATED | K:67 "sanity: every kind is ordinary or fair". (The reader at L:33-34 would refuse such a row first) |
| 34 | The rows are in date order | R:38 | GATED | K:68 "sanity: the rows are in date order". In memory it fails when the first two rows are swapped. A repeated date passes |
| 35 | The check's mutations are shift-year and drop-month | R:7; K:9 | NOT_COMPUTED | Defined at K:43-54, but nothing in K applies them: main (K:98-108) never reads MUTATIONS, and R reports no mutation outcome. Applied in memory, each gives "not reproduced": shift-year fails K:66, K:74-76 and K:86; drop-month fails K:74-75 and K:86 |
| 36 | Discrepancies: none | R:56 | NOT_COMPUTED | discrepancies() (K:94-95) is only `pass`: it computes and reports nothing |

Left out of the table:
- The header bookkeeping (C:3-9; R:3-5, R:9; K:4-6, K:10): dates, Register, Kind, Verdict, Plan, Verified-by, Backs/Backed-by, By. It says nothing about the roll or the computation. Backs (R:5, K:6) matches Backed-by (C:9).
- C's "Evidence and route" (C:26) and R's "6. Verdict" (R:58) are empty and state nothing.
- C's "What is not claimed" (C:22-24) only sets scope; see list 1, item 11.

One more finding, outside the table (in the reader's docstring, not the record or claim): L:5-6 says the roll's three columns are "date, kind and note", but L:29 requires "remark", which is what S:1 has. The docstring and the code disagree (MISMATCH). In memory, a file laid out as the docstring says is refused with "unexpected columns". It does not affect the count.

List 1: negative assertions and their positive controls
1. No row dated 1851 is left out (#6, K:86). Control: drop-month (K:47-48), which removes the 4 March rows; in memory K:86 then fails (51 lines vs 47 counted), and shift-year also makes it fail (51 vs 0). But this control exists only as a declared mutation, which K does not apply and R does not report (#35).
2. No counted row lies outside 1851 (#5, K:85). Controls: K:89 and K:91 reject 31 December 1850 and 1 January 1852 through the same in_year the count uses. Also, S's 53 rows dated 1852 (S:53-105) are read and left out (104 read, 51 counted).
3. 31 December 1850 is not in the year (#14, K:89). Control: K:88 (1 January 1851 is), same function.
4. 1 January 1852 is not in the year (#16, K:91). Control: K:90 (31 December 1851 is), same function.
5. The reader does not skip a row it cannot read (#29). No control in K. GAP. (In memory the refusal does fire on every bad row I tried.)
6. Discrepancies: none (#36). No control, because discrepancies() does nothing. GAP.
7. Nothing but the roll's rows enters the count (#30, "and nothing else"). No control in K, and no declared mutation adds a row. GAP. (In memory, one added row not in the roll fails K:74, K:75 and K:86.)
8. No row lies outside 1851-1852 (#32, K:66). Control: shift-year, declared but not applied or reported; in memory K:66 fails on the 1853 rows it produces.
9. No row has a kind other than ordinary or fair (#33, K:67). No control, and no declared mutation changes a kind. GAP.
10. No row is out of date order (#34, K:68). No control, and no declared mutation reorders rows. GAP. (In memory, a swap fails K:68.)
11. "What is not claimed" (C:22-24): nothing about real markets, nothing about 1852, nothing about the convention of [Note1851]. These limit scope and assert nothing about the roll, so no control is owed. The one assertion inside them, that the roll is synthetic, is row #22.

List 2: quantities and their frames; boundaries and their controls
Quantities:
- 51 rows dated 1851 (#1). Frame: the calendar year 1851 as the roll's dates give it, fixed by in_year (#11, #12; C:10, R:8, K:8) and pinned by K:88-91. Population: the held roll S; nothing checks its recorded checksum (#25). Unit: rows. They count as "market days" only through #18 and #19, and both are NOT_COMPUTED.
- 49 ordinary (#2) and 2 fairs (#3). Same frame as #1, split by the roll's own kind labels (#31), which K:75-76 match as exact strings.
- monthly_1851 = 4,3,4,5,5,4,5,3,5,5,4,4 (#8). Frame: the calendar months of 1851, taken from each date's month inside in_year (K:78). R:31 calls them "the twelve monthly counts" and names no month edge, so the code fixes this frame, inside #11. The vector is PRINTED_ONLY and no gated assertion turns on a month edge (the sum at K:80 is the same whatever the edges), so no boundary controls are owed.
- monthly_sum = 51 (#9). Same frame as #1 (K:78 uses in_year).
- 51 lines of S that open with "1851-" (K:84, shown at K:86; route stated at R:31-33). Frame: the text prefix "1851-" on S's lines after the header. This states the year frame a second time, in text rather than through in_year.

Boundaries of gated assertions:
A. The calendar-year window of in_year (#1-#3, #5, #9, #11; counted at K:72 and K:78).
   - Lower end: last value that must pass is 1851-01-01 (K:88); first that must fail is 1850-12-31 (K:89).
   - Upper end: last value that must pass is 1851-12-31 (K:90); first that must fail is 1852-01-01 (K:91).
   - All four are written as literal dates, not computed from 1851, and run through roll.in_year, the function the count uses. Complete. In memory, each one-day shift of an edge is caught by its own control and by nothing else.
B. The text window of the second route (K:84, which feeds the gated K:86). K holds no controls. GAP. Owed:
   - Lower end: a line "1851-01-01,..." must be counted (pass); "1850-12-31,..." must not be (fail).
   - Upper end: "1851-12-31,..." must be counted; "1852-01-01,..." must not be.
   - (In memory, through K's verify on one-line files, the counts are 1, 0, 1, 0.)
C. The sanity window "1851 or 1852" (#32, K:66). K holds no controls. GAP. Owed:
   - Lower end: 1851-01-01 must pass; 1850-12-31 must fail.
   - Upper end: 1852-12-31 must pass; 1853-01-01 must fail.
   - (In memory, through K's sanity: PASS, FAIL, PASS, FAIL.)
D. The equalities (K:74-76 against 51, 49 and 2; K:80 and K:86, which compare two counts) have no threshold, cutoff, window end or minimum count, so no boundary controls are owed.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. NOT_COMPUTED: the record says the held roll is read at its recorded checksum, but the check computes and compares no checksum, and no function reads BASIS. The sha256 of the roll now is 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3; the recorded value is outside the files I may read. Refuter: narrowed.
2. NOT_COMPUTED: 'CPython 3.12.3' and the run date are stated, but the check prints neither; sys is imported and never used. Refuter: narrowed.
3. NOT_COMPUTED: that the 51 rows fall on 51 distinct days, which '51 market days' and '49 ordinary days' depend on. No condition tests that dates are distinct, and the date-order sanity check passes a repeated date. In memory, 51 rows on 50 days still give 'reproduced'. Refuter: stands.
4. NOT_COMPUTED: each row counted is a market day held, and a fair is a day held (rule of reading). This is an imposed reading that nothing in the check reads. Refuter: refuted.
5. NOT_COMPUTED: that the rule of reading was fixed before the check read the roll. Refuter: stands.
6. NOT_COMPUTED: that the rule is set down in evidence_and_reasoning/notes/2026-11-20_counting_protocol.md; nothing in the check reads that pointer. Refuter: refuted.
7. NOT_COMPUTED: that the roll is synthetic, made by a program; the roll itself says nothing about its origin. Refuter: narrowed.
8. NOT_COMPUTED: that the generating program's rule is known. Refuter: narrowed.
9. NOT_COMPUTED: that the protocol fixes the rule of reading and not the outcome. Refuter: stands.
10. NOT_COMPUTED: that the calendar-year boundary is a choice imposed by the researcher and set down in evidence_and_reasoning/terminology.md, which nothing reads. The boundary itself is gated by four controls. Refuter: refuted.
11. NOT_COMPUTED, and a negative without a positive control: 'the reader refuses a row it cannot read rather than skipping it'. The refusal branches are never reached in the check's run, and no control feeds the reader a bad row. Refuter: narrowed.
12. NOT_COMPUTED: the mutations shift-year and drop-month are defined, but nothing in the check applies them (main never reads MUTATIONS), and the record reports no mutation outcome. The positive controls for 'no row dated 1851 is left out' and 'every row is dated 1851 or 1852' depend on them. Applied in memory, each gives 'not reproduced'. Refuter: stands.
13. NOT_COMPUTED, and a negative without a positive control: 'Discrepancies: None.' has nothing behind it; discrepancies() is only pass. Refuter: stands.
14. Concern: the 'second path to the total' cannot fail on any input. Both sides filter with in_year and every date has a month from 1 to 12, so it is the same count regrouped and gives no independent support for 51 (0 of 20,000 random date lists differ; it passes under both mutations). Refuter: stands.
15. Negative without a positive control: that nothing but the roll's rows enters the count ('and nothing else'). No control and no declared mutation adds a row not in the roll; in memory, such a row fails K:74, K:75 and K:86. Refuter: narrowed.
16. Negative without a positive control: 'every kind is ordinary or fair' (no other kind). The sanity condition is never shown to fail. Refuter: narrowed.
17. Negative without a positive control: 'the rows are in date order' (no row out of order). No control or mutation reorders rows; in memory, a swap fails it. Refuter: stands.
18. A dependency no mutation alters: a row's kind. The 49/2 split is gated (relabelling the 1851-05-15 fair fails both conditions), but neither declared mutation changes a kind, and fair_1851 = 2 still passes under drop-month. Refuter: stands.
19. Boundary without both controls: the sanity window 'every row is dated 1851 or 1852' has no control at either end. Owed: 1851-01-01 pass / 1850-12-31 fail, and 1852-12-31 pass / 1853-01-01 fail. Refuter: narrowed.
20. Boundary without both controls: the second route's text test (lines that open with '1851-') feeds the gated 'no row dated 1851 is left out' but has no control at either end. Owed: '1851-01-01,...' counted / '1850-12-31,...' not counted, and '1851-12-31,...' counted / '1852-01-01,...' not counted. The four existing controls run through in_year only. Refuter: narrowed.
21. MISMATCH in the reader's docstring (outside the record and claim): it names the roll's third column 'note', but the code requires 'remark', which is what the roll has. A file laid out as the docstring says would be refused. It does not affect the count. Refuter: narrowed.
```

#### The second pass for check 001

```
Second-pass count of source_documents/Roll1851_market_roll/Roll1851_market_roll.csv (the only file I read)

RESULT: rows dated in calendar year 1851
- In all: 51
- Kind ordinary: 49
- Kind fair: 2 (line 20, 1851-05-15 "spring fair"; line 41, 1851-10-09 "autumn fair")

File counted: 2,334 bytes, sha256 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3. It has 105 lines: the header date,kind,remark and 104 data rows.

Rule: a row counts as 1851 when its date field is a valid zero-padded YYYY-MM-DD date, taken as written, from 1851-01-01 to 1851-12-31 inclusive. The kind is the kind column exactly as written.

HOW I COUNTED (three ways; all give 51 / 49 / 2)
1. By eye, month by month, from the file as read: Jan 4, Feb 3, Mar 4, Apr 5, May 4 + 1 fair, Jun 4, Jul 5, Aug 3, Sep 5, Oct 4 + 1 fair, Nov 4, Dec 4. The 1851 rows form one unbroken block, lines 2-52.
2. grep with every pattern anchored at the start of the line and none at the end. '^1851-' gives 51; '^1851-[0-9][0-9]-[0-9][0-9],ordinary,' gives 49; '^1851-[0-9][0-9]-[0-9][0-9],fair,' gives 2. '1851' anywhere on a line also gives 51, so no 1851 date sits in another column. As a control, an in-memory copy with "1851" planted in a remark raised that count to 52.
3. python3 -I -B -c, in memory only. I parsed the file with the csv module, checked each date against a strict YYYY-MM-DD pattern, converted it with datetime.date.fromisoformat, kept dates from 1851-01-01 to 1851-12-31 and tallied the kind: 51 = 49 + 2. Its month-by-month tally matches way 1 exactly. A variant without the csv module or date parsing also gives 51 / 49 / 2: it splits the raw text into lines, keeps lines starting '1851-' and takes the second comma field as the kind.

BOUNDARY CONTROLS
- Synthetic dates through the date test: 1850-12-31 is out, 1851-01-01 in, 1851-12-31 in, 1852-01-01 out. The prefix test gives the same results on the same four rows.
- Real rows at the end of the year: 1851-12-23 (line 52) is in and 1852-01-06 (line 53) is out.
- Start of the year: the first data row is 1851-01-07 (line 2). No row is dated before 1851, so only a synthetic date tests that edge from outside.

FRAME
- The 104 data rows split into 51 dated 1851 and 53 dated 1852 (51 ordinary and 2 fairs, on 1852-05-13 and 1852-10-14). No row falls outside 1851-1852. Across the whole file there are 100 ordinary rows and 4 fairs.
- The folder and the file are named for 1851, but 53 of the 104 rows are dated 1852. A whole-file count (104 / 100 / 4) is not the 1851 count.

DATA CHECKS (I trusted each check only after it caught a fault planted in an in-memory copy)
- Every row has exactly 3 fields. The kind is only ever 'ordinary' (100) or 'fair' (4), with no differences in case, spacing or spelling. Planted 'Ordinary', 'ordinary ' and 'faire' each showed up as a separate value.
- Every date is a valid zero-padded ISO date; planted 1851-02-30 and 1851-1-7 were both rejected. Each date is later than the one before, so no date is repeated; a copy with two rows swapped and a copy with one row repeated both failed this test.
- The file is ASCII only, with no BOM, quote characters, tabs or NUL bytes.
- Remarks are empty on all 100 ordinary rows. The fairs carry 'spring fair' or 'autumn fair'. All 100 ordinary rows fall on a Tuesday and all 4 fairs on a Thursday.

CONCERNS
(a) Every line ends in CRLF (105 CR, 105 LF). My counts do not depend on this: the patterns are anchored at the start of the line, the csv module handles CRLF, and the prefix variant reads only the first two fields. A pattern anchored at the end of the line does depend on it. ',ordinary,$' counts 100 rows with this shell's grep in its default mode (it reports itself as ugrep 7.8.4), 0 with the same grep under -P, and 0 with Python re. An early grep check of mine on row shape passed every row, because that grep's $ matched before the CR. Only a byte count, checked against a copy with CRLF added, showed the CRs.
(b) These are counts of rows in the file, not of markets held. 1851 has 52 Tuesdays, and 49 of them have an ordinary row. 1851-02-04, 1851-08-12 and 1851-12-30 have no row, and nothing in the file says why. Reading 49 as "ordinary market days held in 1851" would need a source other than this file.
(c) No real row lies just before the 1851-01-01 edge (see BOUNDARY CONTROLS). No row is dated before 1851, so this cannot change the count.

The methods agree on every count, and nothing was left uncomputed.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. Every line ends in CRLF. The reported counts do not depend on this, but a pattern anchored at the end of the line does: ',ordinary,$' counts 100 rows with this shell's grep (ugrep 7.8.4) in its default mode, and 0 under -P or with Python re. An early grep check on row shape passed every row despite the CR; only a byte count, checked against a planted CRLF copy, showed it. Refuter: narrowed.
2. What the count means: 49 counts ordinary rows, not market days held. 1851 has 52 Tuesdays; 1851-02-04, 1851-08-12 and 1851-12-30 have no row, and nothing in the file says why. Refuter: stands.
3. The file and its folder are named for 1851, but 53 of the 104 data rows are dated 1852. A whole-file count (104 rows: 100 ordinary, 4 fair) is not the 1851 count. Refuter: stands.
4. Boundary: no real row lies just before the 1851-01-01 edge, because no row is dated before 1851. Only a synthetic date (1850-12-31, excluded) tests that edge from outside. The year-end edge has real rows on both sides (line 52 in, line 53 out). This cannot change the count. Refuter: stands.
```

#### The second pass for check 002

```
The only file I read was source_documents/Note1851_market_days_note.md. Its sha256 is 5fb8eb5e76a7233097a77ce00ebab7b9a01e69ce51ffd791e49120309047d66b. It has 16 lines, all plain ASCII, with no carriage returns, tabs, trailing spaces or double spaces. "[p. 1]" is at line 6 and "[p. 2]" is at line 13. I wrote nothing.

1. Under [p. 1], the count for 1851
The count is written in words, "forty-eight", on line 8, with an ordinary ASCII hyphen. The file never gives this count in digits. The full sentence runs over lines 8–9 (the source breaks the line after "market"):
"The town's market roll for the year 1851 records forty-eight market days."

2. Under [p. 1], the days of the week
Lines 9–11 (the source breaks lines after "with the" and "depth of"):
"The market was held on Tuesdays throughout the year, with the customary interruptions at the turn of the year and in the depth of winter, and the roll shows no day held on any other day of the week."
Tuesday is the only day of the week the file names.

3. Under [p. 2], any count for 1852
No count is stated. Lines 15–16 (the source breaks the line after "A count of the"):
"The roll for 1852 is fuller, and it is not treated here. A count of the market days of 1852 is left to a later note."
How I checked this "no": I searched the whole file for digits and for number words. The search finds "forty-eight" on line 8, so it does catch a count written in words. Under [p. 2] (lines 13–16) it finds only the year "1852", twice, and the page mark itself. There are no number words there.

What the note leaves open
- Before the first page mark, lines 3–4 (in italics), the note calls itself "A fictional secondary source, written for this project." The forty-eight is the note's report of what "the town's market roll" records. I did not read the roll, so the count rests on the note alone.
- The note does not say how many "customary interruptions" there were or when they fell. So it does not say out of how many Tuesdays the forty-eight were held. For scale only, and not taken from the note: a calendar check run in memory gives 52 Tuesdays in 1851, from 7 January to 30 December, under both the Gregorian and the Julian calendar. If all forty-eight market days were Tuesdays, 4 Tuesdays had no market. The note does not state that 4.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The count depends only on this note. The note calls itself "A fictional secondary source, written for this project" and reports what "the town's market roll" records. The roll was not read because it is outside this task, so the forty-eight is not checked against it. Refuter: stands.
2. The note gives the number without the total it comes from. It gives "forty-eight" but not the number or dates of the "customary interruptions", nor how many Tuesdays 1851 had. A calendar check run in memory (not from the note) gives 52 Tuesdays in 1851 under both the Gregorian and the Julian calendar. That means 4 Tuesdays without a market, a number the note does not state or confirm. Refuter: narrowed.
3. This note has no count for 1852. Page 2 leaves it "to a later note". That later note was not read, and nothing in this note shows that it exists. Refuter: stands.
```

#### The coverage audit of check 001, after its revision

```
Abbreviations: l.N is line N of python_project/src/check_001_count_1851.py (the check). roll.py is python_project/src/roll.py. record is evidence_and_reasoning/checks/001_count_1851.md. claim is evidence_and_reasoning/claims/001_count_1851.md. CSV is source_documents/Roll1851_market_roll/Roll1851_market_roll.csv.

Run in memory (python3 -B, CPython 3.12.3), the check passes 19 of 19 conditions, exits 0, and prints exactly the values in record §4. The CSV's SHA-256 matches the listed one. No MISMATCH was found. The check's own run applies no mutation and exercises no refusal. A statement that only the probe, a log, a note or a test could back is classed NOT_COMPUTED. PRINTED_ONLY also covers a step the run carries out in code that no condition reports.

| # | Assertion | Where stated | Class | Evidence |
|---|---|---|---|---|
| 1 | The roll holds 51 rows dated 1851 | claim (title, Claim); record §1, §4, §6; check docstring | GATED | "main: the roll holds 51 rows dated 1851" (l.110); the rows are CSV lines 2–52 |
| 2 | 49 of them are ordinary | claim; record §1, §4, §6 | GATED | "main: 49 of them ordinary" (l.111) |
| 3 | 2 of them are fairs | claim; record §1, §4, §6 | GATED | "main: 2 of them fairs" (l.112) |
| 4 | The 51 rows fall on 51 distinct days, so they are 51 market days, not fewer | claim (title); record §1, §4, §6 | GATED | "main: the 51 rows fall on 51 distinct days" (l.114: len(days) == n, with n held at 51 by l.110) |
| 5 | By the rule of reading (imposed), each row of 1851 is a market day held, fairs included | claim; record §1 | GATED | count_1851 counts both kinds (l.84–85); with fairs dropped the count would be 49 and l.110 would fail |
| 6 | The count is derived from the roll's rows and nothing else | claim | GATED | l.98 (the file read is the held roll); l.118 (the count moves with the rows); l.128 (the count equals the file's own line count) |
| 7 | Frame: a row belongs to 1851 when its date falls in the calendar year 1851, as the roll's dates give it, fixed by roll.in_year | claim (Frame); record (Frame), §2; check docstring | GATED | Controls l.131–134, run through roll.in_year, which count_1851 calls (l.84) |
| 8 | That boundary is imposed by the researcher's choice (evidence_and_reasoning/terminology.md), not given by the roll | claim; record §2 | PRINTED_ONLY | Carried by the code: in_year is the project's own (roll.py l.39–41), and the run reads no period from the roll, whose header is date,kind,remark (CSV line 1). No condition reports it, and terminology.md is not read |
| 9 | The rule of reading was fixed in evidence_and_reasoning/notes/2026-11-20_counting_protocol.md before this check read the roll | claim ("the project fixed"); record §1 | NOT_COMPUTED | The check reads no note and records no order of events |
| 10 | The roll is synthetic, made by a program whose rule is recorded with it (prompt_logs/005_sources.md) | claim (What is not claimed); record §1 | NOT_COMPUTED | The check reads neither the program nor the log. The checksum list it parses names make_roll.py on its line 2, but the check uses only the roll's line (l.97–98) |
| 11 | So the protocol fixes the rule of reading and not the outcome | record §1 | NOT_COMPUTED | An inference from rows 9–10; nothing in the check bears on it |
| 12 | The roll the check reads is the held file at its recorded checksum | record (Instrument), §2; check docstring | GATED | "sanity: the roll is the file the checksum list names" (l.98). sha256sum gives 25f4a0fd…c63fd3, which is line 1 of source_documents/Roll1851_market_roll_sha256.txt |
| 13 | It is read with the Python standard library | record (Instrument); check docstring | PRINTED_ONLY | Carried by the imports (l.20–25; roll.py l.15–17); no condition reports it |
| 14 | The interpreter is CPython 3.12.3 | record (Instrument), §2, §4; check docstring | PRINTED_ONLY | Printed at l.100 and in the RESULT line (l.99, l.153); no condition compares it with 3.12.3. In memory: 3.12.3 |
| 15 | The check reads the roll through roll.read_rows, as (date, kind) pairs in file order | record §2 | PRINTED_ONLY | construct() (l.71) and read_rows (roll.py l.24–36); no condition tests file order (l.104 tests date order) |
| 16 | The reader refuses a row it cannot read rather than skipping it | record §2 | NOT_COMPUTED | The run exercises no refusal; the code that would refuse is roll.py l.29–35. In memory, a row of kind "market" raises "line 2: unknown kind 'market'". csv.DictReader skips a blank line silently, but a blank line is not a row |
| 17 | Those refusals are tested in python_project/tests/test_roll.py and are the control for the kinds check ("the reader refuses any other, as its tests show") | record §2, §3 | NOT_COMPUTED | The check neither runs nor reads those tests and prints no control after l.103, though §3 says each sanity check has "a control that must fail" |
| 18 | Every row is dated 1851 or 1852 | record §3 | GATED | "sanity: every row is dated 1851 or 1852" (l.101) |
| 19 | Control: a row dated 1853 fails that test | record §3 | GATED | l.102 (1853-01-04) |
| 20 | Every kind is ordinary or fair, the roll's own kinds | record §2, §3 | GATED | "sanity: every kind is ordinary or fair" (l.103); a row of any other kind stops the run earlier, uncaught, at roll.py l.34 |
| 21 | The rows are in date order | record §3 | GATED | "sanity: the rows are in date order" (l.104) |
| 22 | Control: two rows swapped fail that test | record §3 | GATED | l.105 |
| 23 | Control: one row planted in 1851 makes the count 52, through the same function | record §3 | GATED | l.118, via count_1851. It tests n + 1, which is 52 only because l.110 holds n at 51 |
| 24 | Control: a fair relabelled ordinary splits the count 50 and 1, through the same function | record §3 | GATED | l.121, via count_1851. It tests (ordinary + 1, fair − 1), which is (50, 1) only because l.111–112 hold 49 and 2. The total is not re-tested, and the control runs only if an 1851 fair exists (l.119) |
| 25 | 1 January 1851 is in the year | record §3 | GATED | l.131 |
| 26 | 31 December 1850 is not | record §3 | GATED | l.132 |
| 27 | 31 December 1851 is in the year | record §3 | GATED | l.133 |
| 28 | 1 January 1852 is not | record §3 | GATED | l.134 |
| 29 | The second route is independent of the reader: the file's lines, read as text, are counted month by month by the first eight characters of their date | record §2 | PRINTED_ONLY | lines_by_month (l.88–92) reads the file as text and never calls read_rows; "1851-MM-" is eight characters; no condition reports the independence |
| 30 | The file's lines agree with the reader in every month (Discrepancies: "None") | record §2, §5, §6 | GATED | "second route: the file's lines agree, month by month" (l.127); discrepancies() (l.137–141) printed nothing |
| 31 | They also agree in all | record §2, §6 | GATED | "second route: and in all, so no row of 1851 is left out" (l.128), which prints "51 lines open with 1851-" |
| 32 | No row dated 1851 is left out | record §1, §6; check docstring | GATED | l.127–128: a row the reader dropped would leave the file's lines higher in its month and in all |
| 33 | An added, a dropped, or a misread row shows there as a disagreement in its month | record §2 | NOT_COMPUTED | No control in the check passes a faulty row through the second route. In memory, added and dropped rows, and dates misread into another month or year, do disagree. A fair read as ordinary, or 1851-05-13 read as 1851-05-14, leaves every month equal: the first fails l.111–112, the second changes no stated figure |
| 34 | Every row counted is dated 1851 | record §1, §6; check docstring | GATED | "one for many: every row counted is dated 1851" (l.129), with l.132 and l.134 |
| 35 | Every assertion passed; verdict reproduced | record §4, §6 | GATED | "all assertions passed", "RESULT: reproduced" and exit 0 occur only when no condition fails (l.150–154). In memory: 19 of 19 PASS, exit 0 |
| 36 | monthly_1851 = 4,3,4,5,5,4,5,3,5,5,4,4 | record §4 | PRINTED_ONLY | In the RESULT line (l.126, l.153). l.127 tests that the two routes agree, not these figures; only their sum is held (l.128 with l.110). They equal the CSV month by month |
| 37 | The check's mutations are shift-year, drop-month and duplicate-entry | record (Mutation); check docstring | PRINTED_ONLY | MUTATIONS (l.59–63) holds exactly these three; the run applies none |
| 38 | The probe applied each mutation and the check failed under each; its matrix shows direct and wrapped runs passing and all three CAUGHT | record §6 | NOT_COMPUTED | main (l.144–154) applies no mutation, and tools/falsifiability_probe.py was not read. In memory, through main(): an identity-wrapped run exits 0 and each mutation exits 1 |
| 39 | shift-year, moving every date a year later, drove the count to 0 | record §6 | NOT_COMPUTED | Not in the run; in memory 0 (l.46–48) |
| 40 | drop-month, removing March 1851, drove the count to 47 | record §6 | NOT_COMPUTED | Not in the run; in memory 47 (l.51–52) |
| 41 | duplicate-entry, repeating three rows of 1851, drove the count to 54 | record §6 | NOT_COMPUTED | Not in the run; in memory 54 (l.55–56) |
| 42 | The reader's table, the coverage audit and the gaps, with their refuters' verdicts, are kept in prompt_logs/007_tasks_1_and_2.md | record §6 | NOT_COMPUTED | The check reads no log |
| 43 | A second-pass reader, given the CSV alone, counted 51 rows, 49 ordinary and 2 fairs, by three methods of its own, and agreed | record §6 | NOT_COMPUTED | The check records no second pass; the only pointer that may cover it is the log in row 42. Its figures equal rows 1–3 |
| 44 | The two fairs fall on 1851-05-15 and 1851-10-09 | record §6 | ATTESTED | CSV line 20 (1851-05-15,fair,spring fair) and CSV line 41 (1851-10-09,fair,autumn fair) |
| 45 | This check does not read the note's figure | record §6 | PRINTED_ONLY | The run opens only the roll (roll.py l.27; l.90; l.96) and the checksum list (l.97), the two files BASIS names (l.65–66) |

NEGATIVE ASSERTIONS AND THEIR POSITIVE CONTROLS

- N1. No row dated 1851 is left out (row 32); the "nothing else" in row 6 rests on the same gate. Gate: l.127–128. Control: none in the check. Nothing drops an 1851 row from the reader's rows to show l.127–128 failing. The probe's drop-month does that only outside the check, and the record reports only its count, 47, which l.110 fails on anyway. In memory, dropping 1851-05-13 fails both l.127 and l.128. GAP.
- N2. No month disagrees: "None" under Discrepancies (row 30). Gate: l.127, displayed by discrepancies() (l.137–141). Control: none in the check; this is the same hole as N1. In memory, moving 1851-05-13 to 1851-08-12, with the total unchanged, fails l.127 (and the date-order check) but no count gate. GAP (shared with N1).
- N3. No two of the 51 rows share a day (row 4). Gate: l.114. Control: none in the check. The planted row at l.118 is dated 1851-06-03, a date the roll already holds (CSV line 23), so it would serve, but it runs only through count_1851. duplicate-entry fails l.114 only outside the check, and the record reports only its count, 54. In memory, the rows plus that planted row fail l.114 (52 rows, 51 days). GAP.
- N4. No row outside 1851 is counted (row 34). Gate: l.129 and the in_year filter (l.84, l.113). Control: l.132 and l.134, through in_year. The roll's own 53 rows of 1852 (CSV lines 53–105) are also left out: 51 of 104 rows are counted. Present. l.129 applies in_year's own test again to rows in_year already selected, so it can fail only if in_year changes.
- N5. No row is dated outside 1851–1852 (row 18). Gate: l.101. Control: l.102 (1853-01-04). Present for the upper side only; the lower side has no control (see B2).
- N6. No kind other than ordinary or fair (row 20). Gate: l.103. Control: none in the check. The record's control is the reader's tests (row 17), which the check does not run. In memory, l.103's test is False with a row of kind "market", and read_rows refuses that row. GAP.
- N7. The reader skips no row (row 16). Gate: none in the check. Control: none in the check; the record cites the same tests. A skipped row would show in the second route, but that route has no control either (N1). GAP.
- N8. No row is out of date order (row 21). Gate: l.104. Control: l.105 (the first two rows swapped). Present. It would pass without testing anything if there were fewer than two rows (the guard at l.105), which does not matter at 104 rows.
- N9. 31 December 1850 and 1 January 1852 are not in the year (rows 26, 28). These are themselves controls, paired with the positive controls at l.131 and l.133. Present.
- Scope statements, which assert nothing about the roll and so need no control: the claim's "What is not claimed" (no real market, nothing about 1852, nothing about the note's convention) and row 45, which the code bears out.

QUANTITIES, THE ASSERTIONS THAT FIX THEIR FRAMES, AND BOUNDARY CONTROLS

- Q1. 51 rows dated 1851 (rows 1, 5). Frame: row 7. GATED (l.110) and turns on both ends of the year (B1).
  - Lower end: last value that must pass is 1 January 1851 (l.131); first that must fail is 31 December 1850 (l.132).
  - Upper end: last value that must pass is 31 December 1851 (l.133); first that must fail is 1 January 1852 (l.134).
  - All four are written as date literals, none is computed from 1851, and all run through roll.in_year, which count_1851 uses (l.84). Complete.
- Q2. 49 ordinary and 2 fairs (rows 2–3). Frame: row 7 plus row 20 (roll.KINDS, roll.py l.21). Year ends as in Q1. Complete.
- Q3. 51 distinct days (row 4). Frame: row 7 plus record §2 ("the days are the distinct dates among them"). Year ends as in Q1. Complete.
- Q4. 51 lines in all (row 31). Frame: row 29 (lines after the header that open with "1851-MM-", l.91–92). GATED (l.128) and turns on the year ends of the line route, but no last-pass or first-fail control is written out at either end. GAP (B3).
- Q5. monthly_1851 (row 36). Frame: the months of 1851, by date.month on in_year's rows (l.124) and by the "1851-MM-" prefix (row 29). The figures are PRINTED_ONLY, but the month-by-month agreement (l.127) is GATED and turns on both ends of each month in both routes. No control is written out at any month end. GAP (B3). In memory, lines_by_month puts 1851-01-01 in January, 1851-03-31 in March, 1851-04-01 in April and 1851-12-31 in December, and puts 1850-12-31 and 1852-01-01 in no month, so controls written this way would pass.
- Q6. 52, and the 50/1 split (rows 23–24). Frame: row 7 (the planted 1851-06-03 lies inside the year) plus the kinds. Not a boundary. Both are computed from the held values (n + 1; ordinary + 1 and fair − 1), so they are fixed only through l.110–112.
- Q7. 0, 47 and 54 (rows 39–41). Frame: row 7, applied to the rows the mutations change (l.46–56). Not computed by the run.
- Q8. The window "1851 or 1852" (row 18). Frame: the calendar years of the row dates (two_years, l.75). GATED (l.101) and turns on both ends of a two-year window (B2).
  - Upper end: the first-fail control is written as 4 January 1853 (l.102), not 1 January 1853, and there is no last-pass control at 31 December 1852.
  - Lower end: neither a last-pass control at 1 January 1851 nor a first-fail control at 31 December 1850 runs through two_years. The in_year controls at l.131–132 do not run through it.
  - GAP (B2). In memory, two_years gives True for 1851-01-01 and 1852-12-31, and False for 1850-12-31 and 1853-01-01.
- python = 3.12.3 (row 14) is a version, not a quantity with a frame. Every quantity has a frame.

Not classed: metadata and status fields (Created, Plan, By, Backs/Backed-by, Register OPEN, Kind, Verdict none, Verified-by unchecked). The claim's "Evidence and route" section is empty.

16 gaps, listed in gaps.
```

Its gaps, each with its refuter's verdict:

```
1. Row 9, NOT_COMPUTED: the record says the rule of reading was fixed in evidence_and_reasoning/notes/2026-11-20_counting_protocol.md before this check read the roll. The check reads no note and records no order of events. Refuter: narrowed.
2. Row 10, NOT_COMPUTED: the roll is said to be synthetic, made by a program whose rule is recorded with it (prompt_logs/005_sources.md). The check reads neither the program nor the log; it parses the checksum list, which names make_roll.py, but uses only the roll's line. Refuter: narrowed.
3. Row 11, NOT_COMPUTED: 'so the protocol fixes the rule of reading and not the outcome' is an inference that nothing in the check bears on. Refuter: refuted.
4. Row 16, NOT_COMPUTED, and negative N7 has no control in the check: 'the reader refuses a row it cannot read rather than skipping it'. The run never exercises a refusal (the code that would refuse is roll.py l.29-35; in memory an unknown kind raises ValueError), and the tests the record cites are not run by the check. Refuter: narrowed.
5. Row 17, NOT_COMPUTED, and negative N6 has no control in the check: the kinds sanity check (l.103) has no control line. The control the record offers is the reader's tests in python_project/tests/test_roll.py, which the check neither runs nor reads, although record §3 says each sanity check has 'a control that must fail'. Refuter: narrowed.
6. Row 33, NOT_COMPUTED and too broad: 'an added, a dropped, or a misread row shows there as a disagreement in its month'. No control in the check exercises the second route. In memory, a fair read as ordinary, or 1851-05-13 read as 1851-05-14, leaves every month equal; the first is caught by l.111-112, and the second changes no stated figure. Refuter: narrowed.
7. Row 38, NOT_COMPUTED: the record says the probe applied each named mutation and the check failed under each (matrix: direct and wrapped runs pass, three CAUGHT). The check's own run applies no mutation, and tools/falsifiability_probe.py was not read. Reproduced in memory: identity-wrapped run exits 0, each mutation exits 1. Refuter: narrowed.
8. Row 39, NOT_COMPUTED: shift-year drove the count to 0. The check's run does not compute it; reproduced in memory as 0. Refuter: stands.
9. Row 40, NOT_COMPUTED: drop-month drove the count to 47. The check's run does not compute it; reproduced in memory as 47. Refuter: stands.
10. Row 41, NOT_COMPUTED: duplicate-entry drove the count to 54. The check's run does not compute it; reproduced in memory as 54. Refuter: stands.
11. Row 42, NOT_COMPUTED: the reader's table, the coverage audit and the gaps, with their refuters' verdicts, are said to be kept in prompt_logs/007_tasks_1_and_2.md. The check reads no log. Refuter: stands.
12. Row 43, NOT_COMPUTED: a second-pass reader is said to have counted 51 rows, 49 ordinary and 2 fairs, by three methods, and agreed. The check records no second pass; only the log in row 42 might cover it. Refuter: stands.
13. Negatives N1 and N2 have no positive control. 'No row dated 1851 is left out' and 'None: the file's lines and the reader agree in every month' (and the 'nothing else' in the claim's derivation) rest on the second route, l.127-128, and nothing in the check shows that route failing on a dropped or moved row. The probe's drop-month exercises it only outside the check, and the record reports only the count 47, which l.110 fails on anyway. Refuter: stands.
14. Negative N3 has no positive control: the check never shows '51 rows on 51 distinct days' (l.114) failing on a repeated date. The planted row at l.118 (1851-06-03, a date already held on CSV line 23) would serve, but it runs only through count_1851. duplicate-entry fails l.114 only outside the check. Refuter: stands.
15. Boundary B2: the window 'every row is dated 1851 or 1852' (l.101) has neither control at its lower end (1851-01-01 must pass, 1850-12-31 must fail) and no last-pass control at its upper end (1852-12-31). Its one control is dated 1853-01-04, not 1853-01-01, the first date that must fail. Refuter: narrowed.
16. Boundary B3: the second route's windows have no controls. No month end in either route (date.month at l.124, prefix '1851-MM-' at l.92) and neither year end of the line route has a last-pass and first-fail pair, though l.127-128 depend on them. In memory, the line route places edge dates correctly, so controls written this way would pass. Refuter: narrowed.
```

## Corrections and departures

None of this round's own; the three departures entry 001 lists hold.

## Closing status

```
DONE: plan 001 engaged; tasks 1 and 2 done: the count, 51, and the note's figure, forty-eight; claims 001 and 002 written OPEN
WAITING ON YOU: four decisions: 1 the register of claim 001, 2 the register of claim 002, 3 two names for the mutation set, 4 tension row T001
```

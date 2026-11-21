# Prompt 009: three decisions; the write-up opened

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
1. (a). 2. (b): audit the revised check again, and if the audit holds,
claim 004 is RULED_OUT. 3. (a).

Then open the write-up, task 5. The three slots that waited for it:

- the deliverable: a short standalone note in markdown under paper/,
  released as the file itself, with a plain descriptive title, no
  version marker on the page, its Released stamp saying it is released,
  and nothing released with it but the text
- the paper's agent: we, also for a single author
- the voice: three rules of our own: the subject of a sentence is the
  roll, the note, or a count, never the data; every figure is stated
  with where it is read; nothing is said of any real market

Draft it.
--- PROMPT END ---

## What was done

The researcher ruled on the three decisions of round 008, and each was
applied:

- 1, "(a)": [claim 003] DERIVED, `Verdict: proved`, its `Verified-by:`
  the second pass's route, and its *Evidence and route* written.
- 2, "(b)": [check 004] audited for coverage a second time, after its
  revision in round 008. The assistant reads "if the audit holds" as: if
  no gap the audit names reaches the verdict. None does, as the account
  of the audit below shows, so [claim 004] RULED_OUT, `Verdict: not
  reproduced`, its `Verified-by:` the second pass's route, and its
  *Evidence and route* written; `CURRENT_STATE.md` says what is ruled
  out, and `evidence_and_reasoning/research_result.md` states it.
- 3, "(a)": F001 entered in `FINDINGS.md` as proposed;
  `evidence_and_reasoning/research_result.md` and `CURRENT_STATE.md` say
  what is established.

**Task 5, the write-up, opened** (`HOW_IT_FITS_TOGETHER.md`, *Opening a
write-up*). First the three slots that waited for it, each filled in the
researcher's words by the two moves of `GETTING_STARTED.md` §3, the
owner row and the sentence its token stood in:

- `{{DELIVERABLE}}`, owned by `DOCUMENT_GENRES.md`; the row of the
  conventions of `evidence_and_reasoning/editorial_standards.md` that
  points to it now names the form. Its machine half, the `[publication]`
  table of `tools/artifacts.toml`, stays disabled, the note not being
  built, and the bullet of `paper/README.md` on that table now says so.
- `{{PAPER_PRONOUN}}` and `{{VOICE}}`, owned by `editorial_standards.md`:
  the paper's agent in its conventions, and the voice rules in the owner
  row. The template's example voice record was deleted, as *Voice*
  directs where the row carries the rules itself.

The note was then drafted as `paper/2026-11-20_market_days_1851.md` and
indexed in `paper/README.md`; task 5 is in progress in the plan's ledger,
its review not yet made. What the draft asserts is in the record with
its register: the count [claim 001], the mean [claim 003], what the note
states [claim 002], and that no row repeats [claim 004]. The note has no
changelog, and no source of its own that is not released, so its claims
are reached through `FINDINGS.md` and
`evidence_and_reasoning/research_result.md`, and no claim, check, plan,
finding, or register is named on its page. It shows its evidence: the
roll's dates of 1851 by month, listed by a short program run once and
not kept, whose monthly counts are those [check 001] reports; and the
note's passage, quoted from its first page.

The assistant's reading, brought as decision 2 below: the first voice
rule fixes the subject of a sentence, and the paper's agent is we. The
draft reads the two together, so that a sentence may have we as its
subject, and any other subject is the roll, the note, or a count, never
the data. Every sentence of the draft keeps to that reading, and every
figure in it says where it is read.

**The audit**, played by subagents that wrote nothing: a fresh coverage
auditor of [check 004], given the check, its record, the claim it backs,
and the roll, and a refuter for each of the 13 gaps it named, 14
subagents in all. An audit of the wrong check was started first, from a
script of round 007 written for [check 001]; it was stopped after five
seconds, before its one auditor returned, and nothing from it was read.

The audit found no MISMATCH in what the check computes, and one in what
its record says: the record had the program confirm the roll's checksum
before reading the roll, and the program read it first. The refuters
refuted 2 of the gaps, narrowed 8, and let 3 stand. None reaches the
verdict: the roll holds no row of 1851 that repeats an earlier one.

The check was revised against what survived, and the revision was read
against the gaps by 7 readers who had not made it. They found it short
in places of its own: a control that could not fail, the second route's
year taken by its text while the record said every count went through
`in_year`, a sentence on the note's convention that nothing computed,
and a gate that a roll with four repeats would still pass. The check was
revised again and read by 3 fresh readers. They found the verdict sound
and a smaller set of faults: the gate counted date-and-kind pairs where
the claim speaks of days; the checksum's control tested an inequality of
its own; the row-for-row match had a control that reduced to a count;
the reader passed over a blank line and accepted a row with too many
fields; and several sentences of the two records said more than the
programs did. The check, [check 001], and the reader were revised a
third time, and read by 2 readers, who found all 16 points they were
given answered and two sentences of the reader's docstrings that said
too much, both corrected in their wording. 26 subagents in all;
the share of usage they took is not known: the harness reports none.
What the checks now do, gap by gap:

- **The gate's three.** The roll's 51 and the note's 48 are written into
  the program beside the claims that state them, and the three is
  computed from them and reported as a value. The 51 is gated against
  the roll's own rows; the 48 is taken as given from [claim 002], the
  note not being read here. The claim states as imposed the premise that
  the three rests on: that the note counts what the roll counts, each
  day once over the calendar year, about which [claim 002] claims
  nothing (gaps 1, 2, and 11).
- **The "because".** The gate tested at least three repeats, so a roll
  with four would have passed it, though four leave 47 days against the
  note's 48. The gate now has two halves: three rows of 1851 repeat an
  earlier row, and the distinct dates of 1851 number the note's figure.
  Its controls, on made-up rolls, fail at two repeats and at four among
  51 rows, pass at three, and fail at four repeats on 48 days and at
  three repeats leaving 47 days, one date held under both kinds. The
  main assertion is the gate itself. The claim now says three, so that
  without them the roll's days number forty-eight (gaps 3 and 12).
- **The checksum and the reading.** The program confirms the checksum
  before it reads the roll and reads nothing if the roll is not the held
  file. One function makes the comparison for the test and for its
  control, which bytes the list does not name fail. [check 001] had the
  same order under the same sentence of its record, and is corrected the
  same way; its results are unchanged, and the probe reads CAUGHT under
  all four of its mutations (gap 4).
- **The reader and the file.** The repeats were counted only in the
  reader's rows, so a reader that merged two identical lines would have
  hidden them. The reader's rows of 1851 must now be the file's lines of
  1851, split on their commas, row for row, with a control each for a
  row dropped, a row misread with the count kept, and a line the file
  holds twice and the reader gives once. A line of 1851 entered twice in
  the file's text is read through the reader, as one row more, and
  counted as one repeat. A date entered again with the other kind is
  counted by its date and not by its date and kind (gaps 6 and 10).
- **The reader itself.** It passed over a blank line and accepted a row
  of too many or too few fields. It now refuses each and names the
  file's line, and it reads from a text stream as it reads the file
  (`rows_from`). Its tests, 5 before this round, are 11.
- **[check 001]'s controls** now run through the functions its main
  assertions use, as its record says they do.
- **The second pass.** The record now says it searched the whole file,
  names its three keys as its output does, and names the control that
  bears on the rows of 1852, a row of 1852 entered twice; it points to
  that output (gaps 7 and 8).
- **The year's boundary.** Pinned from both sides through `in_year`, the
  function the reader's rows are taken by; the second route is held to
  the same rows by the row-for-row match (gap 13).
- **Left, each with its reason.** The 48 is not read here, the note being
  collated by [check 002]. The interpreter is printed and not compared,
  as in [check 001]. The checksum is taken on one read of the held file
  and the reader opens it again, a run not changing the held file. The
  named mutation acts on the reader's rows and not on the file, as the
  record now says. A quoted field left open is the one line the reader
  does not refuse: the roll holds no quotation mark, its docstring and
  [check 001]'s record say so, and each check's second route would show
  the lines lost.

The revised check fails as before, by design, and could pass: a roll
built in memory whose own lines hold three repeats among its 51 rows of
1851, on 48 days, passes every condition and reads reproduced; two
repeats, four, and three with one date under both kinds fail; a reader
that merges lines fails the row-for-row match; a roll that is not the
held file is not read; and every row mutation of the set, applied to the
reader's rows, runs to a verdict. The concordance check finds every
program in agreement with its record.

The audit, every gap with its refuter's verdict, and the readings of the
three revisions are below, as each returned them. The tree was recorded
by the checksum of every file before each fan-out and compared after:
through the audit, the files that differed were the main thread's own
edits, made while the auditor read (Corrections and departures); through
each reading of a revision, none. The round check: no finding.

This round edited two rulebooks, `DOCUMENT_GENRES.md` and
`editorial_standards.md`, so the documentation-sweep-owed reminder was
said once in the reply; the next sweep is the first step of the note's
release (`paper/README.md`, *Releasing a version*). Noticed and left for
that sweep: the examples of the `{{VOICE}}` owner row still name "the
example record above", which this round deleted.

**Brought, two decisions**, each with its options and the assistant's
recommendation after them:

1. **A second finding**, for `FINDINGS.md`: `| F002 | Repeated rows do
   not explain the roll's excess over the note's figure: no row of 1851
   repeats an earlier row's date and kind | [claim 004] | RULED_OUT |`.
   Options: (a) enter it as proposed; (b) reword it; (c) decline it. The
   assistant recommends (a).
2. **The first voice rule, read with the paper's agent.** Options: (a)
   as the draft reads it: a sentence may have we as its subject, and any
   other subject is the roll, the note, or a count; (b) as written, with
   no sentence whose subject is we, the agent appearing only as *our* or
   *us*; (c) the rule reworded. The assistant recommends (a).

The draft waits for the researcher's reading.

### The readers' output

#### The coverage audit of check 004, after its revision

```
Coverage audit, check 004 (duplicates)

Files read: python_project/src/check_004_duplicates.py ("check"; "l." means one of its lines unless another file is named), python_project/src/roll.py, evidence_and_reasoning/checks/004_duplicates.md ("record"; §1 to §6 are its own headings), evidence_and_reasoning/claims/004_duplicates_explain_gap.md ("claim"), source_documents/Roll1851_market_roll/Roll1851_market_roll.csv ("roll CSV") and source_documents/Roll1851_market_roll_sha256.txt. Nothing else was read and nothing was written.

I ran the check in memory (python3 -I -B). Its output matches record §4 exactly: both sanity checks and all four controls PASS, and the main assertion FAILs with "0 found". The result line is "RESULT: not reproduced; python=3.12.3; rows_1851=51; control_one=1; control_three=3; duplicates_1851=0", and the exit status is 1. Rows 1 to 6 are the claim's assertions; rows 7 to 30 are the record's.

| # | Assertion | Where stated | Class | Evidence |
|---|---|---|---|---|
| 1 | The roll holds 51 rows of 1851 (the roll's count for 1851, which check 001 also counts and this check uses as a sanity value) | claim, Claim ("[claim 001]"); record §1, §3, §4 (rows_1851 = 51); check l.92 | GATED | "sanity: the roll holds the 51 rows of 1851 that check 001 counts" (n == 51) passes with 51. The check counts this itself from the roll; it does not read check 001. Locus: roll CSV lines 2 to 52 (1851-01-07 to 1851-12-23). |
| 2 | The note's figure for 1851 is 48 | claim, Claim ("[claim 002]") and References ([Note1851]); record §1, §2 ("the note's 48"); check l.30 comment | NOT_COMPUTED | Nothing reads the note. BASIS (l.55-56) lists only the roll and its checksum list, and 48 appears only in the comment on l.30. |
| 3 | The roll's count is three more than the note's (51 less 48), so three repeats are "the least the explanation needs" | claim, Claim; record §1, §2, §3; check l.30 | NOT_COMPUTED | NEEDED = 3 is typed in as a literal. No line computes 51 - 48 or links NEEDED to the rows_1851 that the check computes. |
| 4 | At least three of the roll's rows of 1851 repeat an earlier row's date and kind | claim, Claim; record §1; check l.12-13 | GATED | "main: at least three rows of 1851 repeat an earlier row" (found >= NEEDED, l.104) reports FAIL with "0 found". The assertion is false for the held roll, and that is the check's finding. |
| 5 | The repeats are the reason the roll's count is higher than the note's (the claim's "because"): without them the roll would match the note's figure | claim, Claim | NOT_COMPUTED | Only the necessary count is tested (row 4). Nothing compares 51 - found with 48, and the gate has no upper limit: four planted repeats also pass explains() (run here). This does not affect the verdict, because the necessary count already fails. |
| 6 | So the roll counts some days more than once | claim, Claim | PRINTED_ONLY | discrepancies() prints "its 51 rows of 1851 fall on 51 distinct dates" (l.111-112), which contradicts it. No reported condition tests it either way. The record's opposite statement is row 22. |
| 7 | The roll that is read is the held file with the checksum the list gives | record header (Instrument), §2, §3; check l.7 | GATED | "sanity: the roll is the file the checksum list names" (l.88) passes (25f4a0fdf8374678). sha256sum of the roll CSV here gives 25f4a0fd...5c63fd3, the value on line 1 of source_documents/Roll1851_market_roll_sha256.txt. |
| 8 | The program checks the checksum first and then reads the roll ("first confirms ... It reads the roll ...") | record §2 | MISMATCH | The record says: check, then read. The code does the reverse: main() reads the roll in construct() (l.117) before sanity() computes its checksum (l.118). A roll that fails to parse raises ValueError before any checksum line prints. No effect on this run. |
| 9 | The check runs under CPython 3.12.3 and prints the interpreter | record header (Instrument), §2, §4 (python = 3.12.3); check l.7 | PRINTED_ONLY | Printed as "interpreter: CPython 3.12.3" (l.90) and python=3.12.3 in the RESULT line. Nothing compares it with 3.12.3. |
| 10 | The roll is read with the standard library, through the project's reader, as (date, kind) pairs in file order | record header (Instrument), §2 | PRINTED_ONLY | Done by construct() calling roll.read_rows (l.61; python_project/src/roll.py l.24-36), but no condition states it. A row that cannot be read raises an error outside any reported condition. The number of 1851 rows is covered by row 1, and no count here depends on order. |
| 11 | Frame: the calendar year as the roll's dates give it, set by roll.in_year | record header (Frame); check l.8 | PRINTED_ONLY | Used in every count (l.48, 68, 82, 91, 110; roll.py l.39-41 tests day.year == year), but no condition tests it. Neither end of the year has a control (List 2, B2). |
| 12 | The count is of rows of 1851 whose (date, kind) pair already appeared earlier in the list | record §2 | GATED | The controls in rows 14-15 run duplicates(), the same function the main assertion uses. A count that missed repeats, or that also counted first entries, would fail them. |
| 13 | That is, the rows beyond each pair's first entry (a pair entered k times adds k - 1) | record §2 | PRINTED_ONLY | Computed at l.69. The counting controls plant only single repeats of different rows, and a count of repeated pairs would pass them too, so nothing tests a pair entered three or more times. |
| 14 | One row of 1851 entered a second time in a copy of the distinct rows counts as one repeat: control_one = 1 | record §3, §4 | GATED | "control: one planted repeat is counted as one" (== 1, l.99) passes. |
| 15 | Three as three: control_three = 3 | record §3, §4 | GATED | "control: three planted repeats are counted as three" (== 3, l.100) passes. |
| 16 | The gate is that the count is at least three | record §2; check l.76, l.104 | GATED | Rows 17-18 test it from both sides inside explains() (l.76). The main condition repeats the comparison in its own line (l.104), which those controls never run (List 2, B1). |
| 17 | Two planted repeats fail the gate | record §3, §6 | GATED | "control: two planted repeats fail the gate" (not explains(planted(rows, 2)), l.101) passes. |
| 18 | Three planted repeats pass it | record §3, §6 | GATED | "control: three planted repeats pass it" (explains(planted(rows, 3)), l.102) passes. |
| 19 | The sanity checks and all four controls passed | record §4 | GATED | The six PASS lines. Any failure would print FAIL and be added to FAILURES. |
| 20 | The main assertion failed and the program exited 1 | record §4 | GATED | "[FAIL] main: ... -- 0 found". The exit status is 1 whenever FAILURES is not empty (l.125); it was 1 here. |
| 21 | No row of 1851 repeats an earlier row's date and kind: duplicates_1851 = 0, "none" | record §4, §5; §6 second pass (parsed date with kind) | PRINTED_ONLY | Shown as duplicates_1851=0 in the RESULT line and "0 found" (l.104). The main condition only tests >= 3, so it fails the same way at 0, 1 or 2. |
| 22 | The 51 rows of 1851 fall on 51 distinct dates, so no row of 1851 repeats an earlier row's date, even by date alone | record §5; §6 second pass (date alone) | PRINTED_ONLY | Printed by discrepancies() (l.110-112) but tested by no condition, and it has no positive control (List 1). |
| 23 | The result is total, not a near miss | record §5 | PRINTED_ONLY | Depends on the printed 0 (row 21). No condition tells 0 apart from 2. |
| 24 | Not reproduced: duplicated rows do not explain the difference, and claim 004 is ruled out by this check | record §6 | GATED | The main condition's FAIL produces "RESULT: not reproduced" and exit 1. With three or more repeats it would read PASS and "reproduced": the declared mutation duplicate-entry, applied here in memory, gives 3 repeats and passes l.104's comparison. Zero repeats can explain no positive difference, so this does not depend on rows 2-3. The claim's header still reads Verdict: none, Verified-by: unchecked. |
| 25 | The check could have passed: its controls, run through the same functions as the main assertion, count planted repeats exactly | record §6 | GATED | Rows 14-15 run duplicates(), as the main assertion does. The gate controls (rows 17-18) also go through explains(), which the main assertion never calls (List 2, B1). |
| 26 | The probe does not judge a program whose direct run fails, and says so; the verdict is read from this record (mutation: duplicate-entry) | record header (Mutation), §6; check l.9, l.51-53 | NOT_COMPUTED | Nothing in the check runs the probe or reads MUTATIONS. The mutation is declared but never applied. |
| 27 | Second pass: no row of 1851 repeats an earlier row by exact text | record §6 second pass | NOT_COMPUTED | The check compares only parsed (date, kind) pairs and never compares raw text. (Here: 51 lines of 1851, all distinct.) |
| 28 | Second pass: no repeats in the whole file, 1852 included, by any of the three keys | record §6 second pass | NOT_COMPUTED | duplicates() is called for 1851 only (l.103, 108), and nothing counts 1852. (Here: 104 rows, 104 distinct by each key.) |
| 29 | Second pass: a reader without the first pass's reasoning, given only the CSV, ran a control that found a planted repeat, and agreed | record §6 second pass | NOT_COMPUTED | That reader's procedure, control and result are not in the check, and the check does not print them. |
| 30 | Provenance: run on 20 November 2026 by the assistant; the coverage audit, the probe table, the gaps and the refuters' verdicts are kept in prompt_logs/008_tasks_3_and_4.md; plan 001 sets the note's counting convention aside | record header (By), §4, §6; claim, What is not claimed | NOT_COMPUTED | The check prints no date or author and reads neither that log nor plan 001. (The Plan, Backs and Backed-by fields agree across claim, record and check.) |

List 1: negative assertions and their positive controls
1. Row 21 (no repeat by date and kind, "none"). Controls: "one planted repeat is counted as one" and "three planted repeats are counted as three" (l.99-100). They run duplicates(), the main assertion's own function, on the distinct rows with repeats planted. Present.
2. Rows 20 and 24 (the main assertion fails; not reproduced; duplicated rows do not explain the difference; claim 004 ruled out). Control: "three planted repeats pass it" (l.102) shows the gate passes when three repeats are present. Present, though it runs through explains() rather than l.104 (List 2, B1).
3. Row 23 (not a near miss). Control: control_one shows that a single repeat is counted as 1, not 0. Present.
4. Row 22 (no row of 1851 repeats an earlier row's date, by date alone). No control. Nothing plants a repeated date into the distinct-date count (l.110-112). The planted controls only exercise duplicates(), whose (date, kind) key cannot see a date entered again with the other kind. Run here: adding (1851-01-07, fair) leaves duplicates() at 0, while the date count shows 52 rows on 51 dates. GAP.
5. Row 27 (no repeat by exact text). The record mentions the second reader's control, but the check has no control and no raw-text comparison of its own. GAP.
6. Row 28 (no repeats in the whole file). No control in the check, which counts 1851 only. GAP.
7. Row 26 (the probe does not judge a failing program). No control in the check, which runs no probe. GAP.
8. The claim's "What is not claimed" ("nothing about what does explain the difference"; "nothing about the note's counting convention"). These limit scope and assert no fact about the roll or the note, so no control applies. The second one leaves the note's frame open (List 2).

List 2: quantities and the assertions that fix their frames; boundaries and their controls
Quantities:
- rows_1851 = 51 (rows 1, 22): the rows dated in calendar year 1851 by roll.in_year, over the whole roll as roll.read_rows returns it. The frame is set by the record header "Frame" and check l.8 (roll.py l.9-11, l.39-41). Tested by an exact match (l.92), not a threshold. It depends on the year window (B2).
- duplicates_1851 = 0 (rows 4, 21): the rows of 1851 whose parsed (date, kind) pair already appeared earlier in file order among the rows of 1851. The frame is set by the same header and by record §2 (duplicates(), l.64-71). Tested by a minimum count (B1). It depends on the year window (B2).
- 51 distinct dates in 1851 (row 22): calendar year 1851 by in_year, counted by date alone (l.110-112); stated in record §5. Not tested by any condition.
- control_one = 1, control_three = 3, and the inputs to the two gate controls (rows 14-18): a sorted copy of the roll's distinct rows with the first k rows of 1851 entered again (planted(), l.79-82; record §3, "in a copy of the distinct rows"), counted by duplicates() for 1851. Tested by exact matches (l.99-100).
- The note's figure 48, and the difference of three it sets as NEEDED (rows 2, 3): no frame. The 51 is framed by in_year, but nothing fixes what the note counts or over which year. The claim sets the note's counting convention aside, and record §6 ("What to check next") puts it off. GAP.
- The second pass's whole-file count of 0 by three keys (rows 27-28): the frame is stated (whole file; exact text, parsed date with kind, date alone), but nothing in the check computes it.
- python = 3.12.3 and the checksum are identifiers, not quantities.

Boundaries:
- B1, the main gate: a minimum count of three (l.104; explains(), l.76).
  - Last value that must pass: 3 repeats, "control: three planted repeats pass it", explains(planted(rows, 3)), l.102.
  - First value that must fail: 2 repeats, "control: two planted repeats fail the gate", not explains(planted(rows, 2)), l.101.
  - Both are written-out literals; neither is computed from NEEDED.
  - But both run through explains(), which the main condition never calls: l.104 writes found >= NEEDED again in its own line. The controls therefore test a copy of the gate, not the code the verdict comes from. The two expressions agree today, so the verdict stands. GAP.
  - Notes: the two-repeat control records no count, though planted(rows, 2) holds exactly 2 repeats when run here. The gate has no upper limit, so 4 or more repeats also pass (row 5).
- B2, the calendar-year window from 1851-01-01 to 1851-12-31. rows_1851, the main count and the planted controls' choice of 1851 rows all depend on it (roll.in_year: day.year == year).
  - Controls it needs, written out and run through roll.in_year(d, 1851): at the start, 1851-01-01 must count and 1850-12-31 must not; at the end, 1851-12-31 must count and 1852-01-01 must not.
  - None of these is in the check. GAP.
  - Run here they give True, False, True, False. No row of this roll falls before 1851-01-07 or between 1851-12-23 and 1852-01-06, so neither end changes any count in this run.
- The checksum match (l.88) and the equalities at l.92, 99 and 100 are exact matches, not boundaries.
```

Its gaps, each with its refuter's verdict:

```
1. NOT_COMPUTED (row 2): the claim and record rely on the note's figure for 1851 being 48. Nothing in the check reads the note [Note1851]: BASIS lists only the roll and its checksum list, and 48 appears only in the comment on NEEDED. Refuter: narrowed.
2. NOT_COMPUTED (row 3): the roll's count is three more than the note's (51 less 48), which is where the gate's three comes from. NEEDED = 3 is typed in as a literal. Nothing computes 51 - 48 or links NEEDED to the rows_1851 the check computes itself. Refuter: narrowed.
3. NOT_COMPUTED (row 5): the claim's 'because', that the repeats are the reason the roll's count is higher. Only the necessary count (at least three) is tested. Nothing compares 51 - found with 48, and the gate has no upper limit (four planted repeats also pass explains()). This does not affect the verdict, because the necessary count already fails. Refuter: stands.
4. MISMATCH (row 8): record §2 says the program first checks the roll's checksum and then reads the roll. main() actually reads the roll in construct() (line 117) before sanity() computes its checksum (line 118), so a roll that failed to parse would raise an error before any checksum line printed. No effect on this run. Refuter: stands.
5. NOT_COMPUTED, and a negative with no control in the check (row 26): 'The probe does not judge a program whose direct run fails, and says so; the verdict is read from this record', together with the declared mutation duplicate-entry. Nothing in the check runs the probe or reads MUTATIONS; the mutation is declared but never applied. Refuter: refuted.
6. NOT_COMPUTED, and a negative whose control is not in the check (row 27): the second pass found no repeat of a row of 1851 by exact text. The check compares only parsed (date, kind) pairs and never raw text. The second reader's planted-repeat control is described in the record but is not run by the check. Refuter: narrowed.
7. NOT_COMPUTED, and a negative with no control (row 28): the second pass found no repeats 'in the whole file'. duplicates() is called for 1851 only. Nothing counts the 53 rows of 1852 or has a control for them. Refuter: narrowed.
8. NOT_COMPUTED (row 29): the second reader worked without the first pass's reasoning and from the CSV alone, ran a control that found a planted repeat, and agreed. None of this is in the check or printed by it. Refuter: narrowed.
9. NOT_COMPUTED (row 30): provenance. The record says the check was run on 20 November 2026 by the assistant, that the coverage audit, the probe table, the gaps and the refuters' verdicts are kept in prompt_logs/008_tasks_3_and_4.md, and that plan 001 sets the note's convention aside. The check prints no date or author and reads neither that log nor plan 001. Refuter: refuted.
10. Negative without a control (row 22): 'its 51 rows of 1851 fall on 51 distinct dates ... or even its date' (also the second pass's date-alone key). discrepancies() prints it but no condition tests it, and no control plants a repeated date into that count. The planted controls only use duplicates()'s (date, kind) key, which misses a date entered again with the other kind. Run here: adding (1851-01-07, fair) leaves duplicates() at 0 while the date count shows 52 rows on 51 dates. Refuter: narrowed.
11. Quantity without a frame (rows 2-3): the note's 48, and with it the difference of three that sets NEEDED. The 51 is framed by roll.in_year (the calendar year), but nothing fixes what the note counts or over which year, and the claim sets the note's counting convention aside. Refuter: narrowed.
12. Boundary whose controls do not run through the check's own code (B1, the main gate of at least three). Both controls exist as written-out literals: three planted repeats pass and two fail (lines 101-102). But they run through explains() (line 76), which the main condition never calls; line 104 writes found >= NEEDED again in its own line. The controls therefore test a copy of the gate, not the main condition's code. The record's 'run through the same functions as the main assertion' holds only for the counting controls. The expressions agree today, so the verdict stands. Refuter: narrowed.
13. Boundary without its controls (B2): the calendar-year window that every count depends on (rows_1851 == 51, the main count, and the planted controls' choice of 1851 rows). No control runs roll.in_year(d, 1851) at 1851-01-01 (must count) and 1850-12-31 (must not), or at 1851-12-31 (must count) and 1852-01-01 (must not). Run here they give True, False, True, False, and no row of this roll falls near either end, so no count changes in this run. Refuter: narrowed.
```

#### The first revision, read against the gaps that survived

The reader of the gate's figures (gaps 1, 2 and 11):

```
Gap 1: partly answered. Answered in part. The 3 is no longer a literal whose derivation lives only in a comment: line 32 computes NEEDED = ROLL_COUNT - NOTE_FIGURE. Section 1 now names a source for the 48 and says it is taken unread (record 16-18: '[check 002], whose collated forty-eight it takes as given: the program does not read the note'; program 31: 'collated by [check 002]; not read here'). That answers 'section 1 names no check for the 48'. Not answered: the 48 is still typed by hand (line 31), and BASIS (lines 57-58) still lists only the roll and its checksum list, with no file for the note, claim 002 or check 002. No condition compares NOTE_FIGURE with anything outside the program, while the 51 is gated against the roll's own count (line 134). Check 004 would still not notice if claim 002's figure were other than 48. In memory, editing NOTE_FIGURE to 47, 49, 50 or 51 does fail a gate control (lines 152-153), but only because those controls hard-code a three. That catches an edit to the program, not a change in claim 002 or the note. That check 002 'collated' the 48 is only asserted; nothing in the files read shows the 48 computed from the note. Rests on: python_project/src/check_004_duplicates.py lines 30-32, 57-58, 134, 152-153; evidence_and_reasoning/checks/004_duplicates.md lines 15-18; evidence_and_reasoning/claims/004_duplicates_explain_gap.md lines 10, 29; in-memory runs with NOTE_FIGURE set to 47, 49, 50 and 51

Gap 2: answered. NEEDED is no longer typed in. Line 32 computes it as ROLL_COUNT - NOTE_FIGURE, and ROLL_COUNT (line 30) is the same constant the sanity check compares with the computed rows_1851 (line 134). The gate's three and the sanity value of 51 are therefore one number in code. In memory, setting ROLL_COUNT to 52 made NEEDED 4 and failed the sanity check (rows_1851 = 51): a revised count now carries into the gate, and a roll that no longer holds 51 rows is caught. The record states the source (lines 37-39: the roll's 51 less the note's 48, with the three computed from them). The run reproduces section 4 exactly (rows_1851=51, control_one=1, control_three=3, duplicates_1851=0, repeated_lines_1851=0, repeated_dates_1851=0; exit 1). The prescribed direct run with -I stops at 'import roll', because -I keeps src off the import path, so main was run in memory with src added to the path. Residual, listed under new problems: the gate's controls and the mutation still hard-code the three, so a revised count reaches NEEDED and then fails a control. Rests on: python_project/src/check_004_duplicates.py lines 30-32, 78, 132-134, 200; evidence_and_reasoning/checks/004_duplicates.md lines 37-39, 73-79; in-memory runs as-is and with ROLL_COUNT = 52

Gap 11: partly answered. The record now says what the gate's three assumes and that the assumption depends on the convention set aside (lines 18-21: the note's forty-eight 'counts what the roll's 51 counts, each day once over the calendar year 1851, which the note does not say; its counting convention is left to a plan of its own'). That answers 'check 004 never says that its threshold depends on the counting convention'. Section 5 (lines 86-89) adds that the verdict would stand for any positive difference. Nothing shows the assumption holds. The program reads no note (line 31; BASIS 57-58). Claim 004 still asserts 'by three' (lines 14-15) while setting the convention out of scope (lines 21-23), and it does not state the assumption. The robustness sentence is not computed. The gate is evaluated only at NEEDED = 3, and the program cannot run at another difference without a gate control failing (in memory: a note figure of 47 fails 'three planted repeats pass it'; 49, 50 and 51 fail 'two planted repeats fail the gate'). Repeats are counted only inside calendar 1851 (line 66 default year=1851, line 92 prefix '1851-'). So nothing the program computes covers a convention that also moves the year frame, which is the 'over which year' half of the gap. Rests on: evidence_and_reasoning/checks/004_duplicates.md lines 18-21, 86-89, 104-105; evidence_and_reasoning/claims/004_duplicates_explain_gap.md lines 14-17, 21-23; python_project/src/check_004_duplicates.py lines 31, 57-58, 66, 92, 152-153; in-memory runs with NOTE_FIGURE set to 47, 49, 50 and 51

New problems:
1. The record's 'the three computed from them' is only half true, because the three is still typed into the program. The duplicate-entry mutation plants exactly [:3] (line 50). The gate's controls hard-code planted(rows, 2) and planted(rows, 3) (lines 152-153). The labels also type '51' (line 134) and 'three' (line 155). In memory, the derived NEEDED cannot carry a revised figure through the program. NOTE_FIGURE 47 fails 'control: three planted repeats pass it'. NOTE_FIGURE 49, 50 or 51 fails 'control: two planted repeats fail the gate'. ROLL_COUNT 52 fails both the sanity check and the three-repeats control, and the sanity label still reads 'the 51 rows'. At NEEDED 4 or 5 the mutation no longer passes the gate. Section 3 describes lines 152-153 only as controls that pin the gate from both sides. It does not say they are also the program's only check that the difference is three. NEEDED is never passed to value(), so the RESULT line, and with it section 4, is byte-identical at NOTE_FIGURE 47, 49, 50 and 51. The gate a run applied is printed only in the discrepancy line, and only when the gate fails. Where: python_project/src/check_004_duplicates.py lines 32, 50, 134, 152-153, 155, 200; evidence_and_reasoning/checks/004_duplicates.md lines 37-39, 57-59, 73-79
2. 'The verdict would be the same for any difference above zero, whatever count the note's convention gives' is prose, not a computed or reported condition. The 'above zero' part follows from duplicates_1851 = 0. But the program evaluates the gate only at 3 and cannot run at another difference without a control failing (previous item). 'Whatever count' overreaches for counts of 51 or more. In memory, at NOTE_FIGURE = 51 (NEEDED 0) the main assertion passes (0 >= 0), and the run fails only on the two-repeats control, because explains() (line 78) does not check that the difference is positive. Section 1 (line 20) makes the year frame part of the assumption. For a convention that also moves the frame, the sentence rests on rows the program never counts: repeats are counted only within calendar 1851 (line 66 default year=1851, line 92 prefix '1851-'). In memory, the whole file's 104 rows fall on 104 distinct dates, so the sentence happens to hold for this file. Check 004 does not compute that, and section 5 does not cite the second pass that reports it. Where: evidence_and_reasoning/checks/004_duplicates.md lines 86-89 (with line 20); python_project/src/check_004_duplicates.py lines 66, 78, 92
3. 'Which the note does not say' is a statement about the note's content. The record makes it although its program never reads the note (line 31 'not read here'; BASIS lines 57-58 list only the roll and its checksum list). It is not computed and cannot be checked from the check's basis. Claim 004 itself makes no statement about the convention (lines 21-23). Where: evidence_and_reasoning/checks/004_duplicates.md lines 20-21; python_project/src/check_004_duplicates.py lines 31, 57-58
4. The attribution of the 48 to [check 002] ('collated') is new and stated, not computed. No file of the note, claim 002 or check 002 is in BASIS, and no reported condition compares NOTE_FIGURE with any of them. The 51, by contrast, is gated against the roll's own count at line 134. Yet section 1 presents both numbers in the same way, as taken from earlier checks. Where: python_project/src/check_004_duplicates.py lines 30-31, 57-58, 134; evidence_and_reasoning/checks/004_duplicates.md lines 16-18
```

The reader of the explanation's "because" (gap 3):

```
Gap 3: partly answered. The record now says which half the gate tests. Section 1 says the gate tests 'at least three repeats' and that 'no more than three, so that the roll's distinct rows number the note's forty-eight exactly, is not tested'. The program's docstring and its comment on the gate controls also call three 'the least the explanation needs'. That is accurate to the program and answers 'whether the record says so'. But nothing computed changed: explains() is still duplicates(rows) >= NEEDED, it is still named explains() with the docstring 'enough repeated rows of 1851 to account for the difference', no value compares 51 - found with 48, and no reported condition tests an upper limit. In memory, explains(planted(rows, k)) is True for k = 4, 10 and 51. A 51-row roll of 1851 with four repeats (47 distinct against 48) or ten (41 distinct), run through main() with the checksum step bypassed, passes every assertion, prints no discrepancy line and ends 'RESULT: reproduced' with exit 0, the same as with exactly three. That is a counterfactual, since the checksum ties the run to the held roll, but it is the counterfactual section 6 invokes with 'The check could have passed', which it leaves unqualified. So the program still treats a pass of the necessary half as reproducing the claim, and the record does not say so. The record's reason for testing only that half is also wrong. It calls it 'the half of the explanation the roll can refuse', but the roll can refuse the other half from the same 51 and 48. A two-sided gate tried in memory (51 - found == 48) is False at four repeats and True at three. On the held roll it is False, like the one-sided gate, so computing it would have been cheap and would not change the verdict. What actually makes the upper half moot here is the result (0 found), which only the sentence's second clause gives. The gate's positive control, 'three planted repeats pass it', runs on planted(rows, 3), which holds 54 rows of 1851 and 51 distinct pairs (computed in memory), so the controls also test only the tested half. The verdict is unaffected: 0 repeats fails the necessary half, and section 6's 'not reproduced' rests on that alone. Run note: the prescribed 'python3 -B -I check_004_duplicates.py' stops at 'import roll' because -I keeps the script's folder off sys.path. Run through runpy with python_project/src on the path, it prints a RESULT line that matches section 4 (duplicates_1851=0, exit 1). Rests on: evidence_and_reasoning/checks/004_duplicates.md lines 13-16, 21-26, 56-59, 93-98; python_project/src/check_004_duplicates.py lines 12-13, 30-32, 76-78, 81-84, 150-155, 182-187, 197; evidence_and_reasoning/claims/004_duplicates_explain_gap.md lines 14-17; in-memory runs: explains(planted(rows, k)) for k = 2, 3, 4, 10, 51; main() on 51-row rolls of 1851 with 2, 3, 4 and 10 repeats (checksum step bypassed); a two-sided gate 51 - found == 48 on the held roll, the planted lists and the altered rolls

New problems:
1. It calls the tested half 'the half of the explanation the roll can refuse', which implies the untested half is beyond the roll's reach. It is not: both halves are read from the same roll count and the same note figure (program line 32 builds NEEDED from both). In memory, a 51-row roll of 1851 with four repeats fails a two-sided gate (51 - found == 48 is False) but passes the program's gate. What makes the other half moot here is the result (0 found), not a limit of the roll. Where: evidence_and_reasoning/checks/004_duplicates.md lines 21-23
2. The reason given for leaving the upper half untested ('since where fewer than three repeat the explanation fails whatever the other half') covers only the failing outcome, yet it sits in the section that says what is checked. In the passing outcome the program prints 'RESULT: reproduced' with exit 0 for four or ten repeats (in memory: 47 and 41 distinct against 48), and discrepancies() prints nothing when found exceeds NEEDED. The record never says that a pass would report 'reproduced' on the necessary half alone, and section 6's 'The check could have passed' is unqualified. Where: evidence_and_reasoning/checks/004_duplicates.md lines 24-26 and 95-98; python_project/src/check_004_duplicates.py lines 182-187 and 197
3. 'from both sides' and 'pinned from both sides' describe pinning the threshold between two and three, not an upper limit. No reported condition shows the gate passing at four, the case the gap names. The positive control at three also runs on planted(rows, 3), which holds 54 rows of 1851 and 51 distinct pairs (computed in memory, not by the program): there the three repeats leave 51, not 48. So 'three, the least the explanation needs, pass it' passes the gate on data the untested half would refuse, and the record does not say so. Where: evidence_and_reasoning/checks/004_duplicates.md lines 56-59; python_project/src/check_004_duplicates.py lines 150-153
```

The reader of the checksum and the reading (gap 4):

```
Gap 4: answered. The revision changes what runs, not just the wording. The checksum has moved out of sanity() into a new confirm_roll(), and main() now calls it before construct() in both checks: check 004 at line 192 then 193, check 001 at line 168 then 169. Neither sanity() touches the checksum any more (004 lines 132-140, 001 lines 114-121). Nothing reads the roll at import: roll.py only builds paths (lines 19-21). Part 2 of both records now states that order: 'first confirms ... It then reads' (004) and 'first confirms ... It reads' (001). Both runs print the checksum line and the interpreter line straight after the title, before any line that needs the reader's rows. I tried the gap's own case in memory: the reader's open was shadowed so read_rows raises ValueError("line 3: unknown kind 'market'"). The revised main() then prints the checksum line before the error in both checks: PASS 25f4a0fdf8374678 on the real bytes, FAIL f085c37150efe808 on altered bytes, followed by the interpreter line. The old order (construct, then confirm_roll) raises with no checksum line, as the gap said. Check 004 exits 1, with only the main assertion failing. Check 001 exits 0. Both RESULT lines match part 4 of their records, and sha256sum of the roll matches line 1 of the checksum list. The task's command (python3 -B -I check_004_duplicates.py) stops at 'import roll' with ModuleNotFoundError, because -I keeps the script's folder off sys.path. I therefore ran each program through runpy with '.' put on sys.path, which writes nothing. Rests on: python_project/src/check_004_duplicates.py:61-63,123-129,132-140,190-196; python_project/src/check_001_count_1851.py:75-77,105-111,114-121,166-172; python_project/src/roll.py:19-21,24-36; evidence_and_reasoning/checks/004_duplicates.md:30-34; evidence_and_reasoning/checks/001_count_1851.md:26-30; source_documents/Roll1851_market_roll_sha256.txt:1

New problems:
1. The revision presents the checksum as a confirmation made before the read: 'first confirms that the roll it will read is the held file' in both records' part 2, and 'Before the roll is read: it is the held file its checksum names' in the new confirm_roll() docstring. But the comparison only reports. main() goes on to read and evaluate the roll whatever it found. In memory, a parseable roll with one row's remark altered gets '[FAIL] sanity: the roll is the file the checksum list names -- 73a406b237258015', and both programs still read and score it to the end. Check 001 then exits 1 with 1 failure. Check 004 prints the same 'RESULT: not reproduced' line as the real run, with 2 failures in place of 1, so there a mismatch changes only the failure count. Nothing the program reports shows the comparison failing on bytes the list does not name. It does fail, as the experiment above shows, but that rests on my in-memory run, not on any reported condition. The missing control may predate the revision, since the old sanity() held the checksum; the earlier version is not among the files I may read. Where: python_project/src/check_004_duplicates.py:123-129,190-194; python_project/src/check_001_count_1851.py:105-111,166-170; evidence_and_reasoning/checks/004_duplicates.md:30-34; evidence_and_reasoning/checks/001_count_1851.md:26-30
2. Moving the checksum out of sanity() into confirm_roll(), which only main() calls, takes it out of the phase functions. A run that drives construct, sanity, verify and discrepancies directly now never computes it. In memory, a phase-only run prints no checksum line in either check, on the unmutated rows or under any named mutation. A construct() wrapper run through main() still prints the checksum first, before the read, and all four check-001 mutations still fail it (exit 1; the identity wrapper exits 0). Record 001 part 6 states 'the direct and the wrapped runs pass' from the probe (tools/falsifiability_probe.py), which is outside the files I may read. So I cannot tell whether its wrapped runs go through main(), which keeps the checksum, or through the phases, which would now skip it. Nor can I tell whether that matrix was made before or after this revision; the record does not say. Where: python_project/src/check_001_count_1851.py:105-121,166-170; python_project/src/check_004_duplicates.py:123-140,190-194; evidence_and_reasoning/checks/001_count_1851.md:85-88
```

The reader of the second route (gaps 6 and 10):

```
Gap 6: partly answered. Two parts of the surviving gap are now covered. First, the sanity now compares the reader's rows of 1851 with a count of the file's own lines (51 = 51), not only with the fixed 51. Second, the check has its own route from raw text to a counter (file_lines and repeated_lines). That route must agree with the reader and has a control planted in the file's text. So the negative no longer rests on the second reader's pass alone. I tested this in memory: I planted one identical line of 1851 in the raw text and gave it to a reader that merges identical rows. That reader fails the line-count sanity and both second-route agreements. The gap's central point is still open: no control in the check passes a repeated raw line through roll.read_rows() to duplicates(). Every planted repeat goes either into the reader's output (146-153) or into the text list (140, 165, 174), and read_rows only opens a path. The control offered for the reader side (138-140) never re-reads. It adds one line to the text count and compares it with the reader's count from the unplanted file, so it passes whenever the sanity above it passes. In memory: at 50 rows the sanity fails and the control passes; at 51 both pass; at 52 both fail. On the real file a merging reader still gives 0 and passes every reported condition, the new ones included. That is harmless now only because the text route also gives 0. In memory the real reader does carry a planted raw repeat through to duplicates() (count 1), but the check never shows this. The prescribed command `python3 -B -I check_004_duplicates.py` stops at `import roll` with ModuleNotFoundError, because -I keeps the script's folder off sys.path. Run in memory with that folder added, the output matches record section 4 and the program exits 1. Rests on: python_project/src/check_004_duplicates.py 87-100, 132-140, 146-153, 160-165; python_project/src/roll.py 24-36; evidence_and_reasoning/checks/004_duplicates.md 41-46, 50-54, 59-62, 69-79, 107-113

Gap 10: answered. The first pass now computes the date-alone count on both routes and tests that they agree (166-168). The text route's repeats by date must equal the reader's rows of 1851 less its distinct dates. The result is recorded as repeated_dates_1851 = 0 (record 79). The first pass also has its own planted control (169-174, PASS): a date of 1851 entered again with the other kind is found by date and not by date and kind. That is exactly the case the (date, kind) controls missed. Section 5 now reads the clause off that agreement instead of off discrepancies()'s print. Its '51 distinct dates' follows from rows_1851 = 51 and repeated_dates_1851 = 0 with the agreement passing. I tested this in memory. A line with the same date and the other kind, planted in the raw text, gives a date-alone count of 1 on both routes. A reader that merges rows of one date fails the line-count sanity and the date-alone agreement. A residual remains, but it does not reopen the clause. No reported control plants a repeated date into the reader-side count (len(days) - len(set(days)), line 168). Nor does one plant it into the distinct-date figure, which discrepancies() still prints only when the gate fails (185-187). So the clause's negative rests on the text route's controlled count; the reader's count agrees with it but has no control of its own. Rests on: python_project/src/check_004_duplicates.py 108-120, 166-174, 182-187; evidence_and_reasoning/checks/004_duplicates.md 59-62, 73-79, 83-86

New problems:
1. The record (63-64) and the program comment (175) say the year's boundary is pinned through in_year, 'the function every count uses'. Both headers (record 8, check 8) say the frame is fixed by in_year. The revision made this untrue. Four new counts set the year by the text prefix '1851-': the line count (136), the planted-line count (140) and both text-route counts (repeated_lines, prefix '1851-' at 92, applied at 96). None of the four boundary controls (176-179) goes through that prefix. In memory, changing repeated_lines' prefix to '18' or to '' leaves every reported condition unchanged on the real file. The prefix does matter: a repeated line of 1852 planted in the text counts 0 under '1851-' and 1 under '18'. No reported condition tests the second route's year frame, yet the record says it is pinned. Where: evidence_and_reasoning/checks/004_duplicates.md 8 and 62-65; python_project/src/check_004_duplicates.py 8, 92, 96, 136, 140, 175-179
2. The new control 'a line of 1851 entered twice in the file's text no longer matches the reader' never runs the reader on the planted text. It compares the count of the text's lines of 1851, plus one, with the reader's count from the unplanted file. Once the sanity at 135-137 passes, this reduces to count + 1 != count, so it cannot fail. It fails only when the reader gives exactly one row more than the file has lines, and then the sanity fails too. In memory: at 50 rows the sanity fails and the control passes; at 52 rows both fail. The record presents it as the control of the agreement between the reader and the lines. Section 2's sentence 'a repeated line the reader merged or dropped shows as a disagreement' is true when tested in memory. But no reported control that runs through roll.read_rows() shows it. Where: python_project/src/check_004_duplicates.py 138-140; evidence_and_reasoning/checks/004_duplicates.md 45-46 and 52-54
3. 'The reader gives one row for each of the file's lines of 1851' states a line-for-row match, but the program only checks that the two counts are equal. In memory, I used a reader that drops one row of 1851 and emits a date the file does not hold. It passes this sanity and every other reported condition; only the main assertion fails, as it does on the real file. This does not affect the repeat counts: a reader that drops one row and emits another twice fails both second-route agreements. But the line-for-row match the wording states is not computed. Where: python_project/src/check_004_duplicates.py 135-137; evidence_and_reasoning/checks/004_duplicates.md 43-44 and 52
```

The reader of the second pass (gaps 7 and 8):

```
Gap 7: partly answered. The only real gain is the new pointer. It leads to the log passage, where the second reader reports '0 for the whole file' (log 592), notes that dates rise strictly across all 104 rows (595), and has one control on a row outside 1851 (611: an extra 1852-05-13 fair counts 0 for 1851 and 1 for all years). The record itself still does neither thing the gap asked for. It still describes a search of 'the rows of 1851' (108) while reporting 'none ... in the whole file' (111-112), and it says nothing about how the 53 rows of 1852 were searched. The control it adds, 'one of them placed after the last row of 1852' (111), is log 603's copy of the 1851 row 1851-01-07. Under in_year that row belongs to 1851. In memory, using the check's own duplicates(), a search over the 1851 rows alone plus that copy gives 1, the same as a search over all rows. So this control cannot show that the 1852 rows were searched. The control that can show it (log 611) is not named. The clause was not cut back either, although the claim needs only 1851 (claims/004_duplicates_explain_gap.md 14-17). No program counts the 1852 rows. duplicates() uses year=1851 (66-73, 154). repeated_lines() uses the prefix '1851-' (92-100, 161-168). The only mention of 1852 is the boundary control (179). The RESULT line has no whole-file value. I ran the check in memory with src on sys.path, because under -I the instructed run stops at 'import roll'. The run matches record 73-79 and reports nothing about 1852. The clause itself is true: in memory there are 0 repeats by date and kind and 0 by date over all 104 rows. A repeat planted among the 1852 rows gives 0 under a count limited to 1851 and 1 under a whole-file count. That truth is computed nowhere in the project and is not stated as a method and control in the record. Rests on: evidence_and_reasoning/checks/004_duplicates.md:107-113, 73-79; prompt_logs/008_tasks_3_and_4.md:588, 592, 595, 603, 611; python_project/src/check_004_duplicates.py:49-50, 66-73, 81-84, 92-100, 154, 160-168, 179, 200; evidence_and_reasoning/claims/004_duplicates_explain_gap.md:14-17; in-memory runs of check_004 functions over source_documents/Roll1851_market_roll/Roll1851_market_roll.csv

Gap 8: answered. The record now says where the second pass is kept: 'Its output, with its controls, is kept in prompt_logs/008_tasks_3_and_4.md' (112-113). The log does hold it, under the only heading 'The second pass for check 004' (575), in a fenced block (577-618) containing: (a) its answer, 0 (578), which matches the check's duplicates_1851=0 in my run and in record 77; (b) the one file it read, at sha256 25f4a0fd...3fd3 (580), which matches sha256sum of the held CSV and line 1 of the checksum list; (c) its three keys (588-592), which match record 109-110; (d) its planted controls, which should be found, and negative controls, which should not (599-613); and (e) its statement that it read only that one file (617). Two small residues remain. First, the pointer names the file but not the heading, and the record says the same log also holds the first audit (100-102). Second, the passage holds the reader's output but not the brief it was given. So 'without the first pass's reasoning' rests on the reader's own statement that it read only the CSV (580, 617). These residues do not reopen the gap as narrowed, whose fix was a pointer. Rests on: evidence_and_reasoning/checks/004_duplicates.md:100-102, 107-113, 77; prompt_logs/008_tasks_3_and_4.md:575-618 (578, 580, 588-592, 599-613, 617); source_documents/Roll1851_market_roll_sha256.txt:1; sha256sum of source_documents/Roll1851_market_roll/Roll1851_market_roll.csv; check run RESULT duplicates_1851=0

New problems:
1. The added control, 'placed after the last row of 1852', is misleading where it stands. Next to 'in the whole file' it reads as the control for rows outside 1851, and it is not one. According to the log (prompt_logs/008_tasks_3_and_4.md:603) it is a copy of the 1851 row 1851-01-07. In memory, a search that never looks at 1852 finds it equally: 1 either way, and 0 for a count of 1852. The check's own planted() (python_project/src/check_004_duplicates.py:81-84) and its duplicate-entry mutation (line 50) already append their 1851 repeats after 1852-12-28, so this placement adds nothing about the rows of 1852. The log's control that does bear on them (line 611: an extra 1852-05-13 fair, 0 for 1851 and 1 for all years) goes unnamed. Where: evidence_and_reasoning/checks/004_duplicates.md:110-112
2. The revision keeps the whole-file clause and adds the three keys and the planted-repeat controls. All of these are the second reader's work: stated in the record, computed by no program, and covered by no reported condition. No PASS/FAIL line or RESULT value of check_004 touches the 53 rows of 1852. The clause is true (in memory: 0 repeats by date and kind and 0 by date over all 104 rows, with dates rising strictly), but its only support is the log passage (prompt_logs/008_tasks_3_and_4.md:588, 592, 595, 611). Where: evidence_and_reasoning/checks/004_duplicates.md:107-112; python_project/src/check_004_duplicates.py:66-73, 92-100, 154, 161-168, 200
3. Minor wording issues. The record says the reader 'searched ... for any that repeats the date and kind of an earlier row, by three keys ... and the date alone'. But the date-alone key tests a repeat of the date only, not of date and kind (log 591). Also, 'the parsed date with the kind' drops the log's 'trimmed and lower-cased' (log 590), which is what makes it differ from the exact-text key (log 613). Where: evidence_and_reasoning/checks/004_duplicates.md:108-110
```

The reader of the gate and the year's ends (gaps 12 and 13):

```
Gap 12: answered. The main line now passes explains(rows) itself as its condition (check line 155). Its comparison is therefore the one the two gate controls run (lines 152-153): same function, same operator, same NEEDED, with only the input different. value() is no longer in the gate's path: line 154 records duplicates(rows) only for the RESULT line and the '0 found' text. The record's statement that 'the main assertion is the gate itself, through the same function' (md 57-59, 95-98) is now true.

How I ran it: the given command, `python3 -B -I check_004_duplicates.py`, stops at `import roll` (line 25) with ModuleNotFoundError, because -I leaves the script's folder off sys.path. I ran the program through runpy with src on the path instead. That run reproduces the record's RESULT line and exit code 1.

In-memory experiments:
- A spy shows explains called three times, once on the constructed rows object itself.
- An explains that always returns True turns the main line to PASS and fails 'two planted repeats fail the gate'. One that always returns False fails 'three planted repeats pass it'.
- The operator mutants >, <, <= and !=, and NEEDED set to 2 or 4, are each failed by a gate control.
- A value() that returns 5 leaves the main line failing, with detail '5 found'. The mismatch is caught by the second-route assertion (161-162).
- The record's duplicate-entry mutation turns the main line to PASS with 3 found.

Two residues lie outside the gap as it survived and come from before this revision:
- An == in explains passes both gate controls, because no control plants more than three repeats. It cannot change this verdict: 0 == 3 is false, just as 0 >= 3 is.
- discrepancies() still writes the comparison again as found < NEEDED (line 184). It only decides whether the message prints and is not an assertion. Rests on: python_project/src/check_004_duplicates.py:25, 43-46, 76-78, 150-155, 161-162, 182-184; evidence_and_reasoning/checks/004_duplicates.md:56-59, 69-79, 95-98; in-memory runs: spy on explains, always-True/False explains, operator mutants >,<,<=,==,!=, NEEDED=2/4, value() returning 5, MUTATIONS['duplicate-entry'] applied to construct()

Gap 13: answered. Four controls now run roll.in_year at the ends of the year (check 176-179): 1 January and 31 December 1851 are in, 31 December 1850 and 1 January 1852 are out. That is the same function and the same year that rows_1851 (line 133) and the main count (duplicates, line 70, reached through explains) call. The record names the four (md 62-65) and states that the controls passed (69-71). My run reports all four PASS.

In memory I replaced in_year with five wrong windows: one dropping 1 Jan 1851, one taking 31 Dec 1850, one dropping 31 Dec 1851, one taking 1 Jan 1852, and one a week late at both ends. Each still gives rows_1851=51 and duplicates_1851=0. The data cannot tell, because the roll's rows of 1851 run from 1851-01-07 to 1851-12-23 and the next row is 1852-01-06 (CSV lines 2, 52, 53). Each window is failed by the control at its end, and only by that control.

The window's ends therefore no longer rest on reading roll.py line 41 or on an off-record run. The record's wider wording, that in_year is the function every count uses, is not true (see new problems), but that does not touch the two counts this gap names. Rests on: python_project/src/check_004_duplicates.py:66-73, 133-134, 175-179; python_project/src/roll.py:39-41; evidence_and_reasoning/checks/004_duplicates.md:62-65, 69-71; source_documents/Roll1851_market_roll/Roll1851_market_roll.csv:2, 52, 53; in-memory runs of five shifted in_year windows

New problems:
1. The new text says the year's boundary is pinned 'through in_year, the function every count uses'. Three of the check's counts do not use in_year: the sanity line count (line 136, reported as '51 lines'), and the second route's repeated_lines_1851 and repeated_dates_1851. The second route's counts come from repeated_lines (line 92, default prefix '1851-', called at 162 and 168), so all three pick 1851 by a text prefix. The year-end controls do not touch that prefix. For the second route's two counts, no reported condition checks the window at all.

In memory, I set repeated_lines' prefix to '185' (1851 and 1852) and then to '' (the whole file). Either way every condition except the main line still passes, and RESULT is unchanged (repeated_lines_1851=0, repeated_dates_1851=0). Only a prefix that leaves out 1851 entirely ('1852-') is caught, by the second route's planted controls. So the second route's agreement is not shown to be over the calendar year 1851. On this roll it holds just as well over the whole file. Where: evidence_and_reasoning/checks/004_duplicates.md:62-65; python_project/src/check_004_duplicates.py:175 (against lines 92, 136, 162, 168)
```

The reader of the revised record, as a coverage reader:

```
Row: GATED. Part 1 says 'That at least three of the roll's rows dated 1851 repeat an earlier row's date and kind' and 'The gate tests the half ... at least three repeats'; part 2 says 'The gate is that the count is at least three'. This is the main condition itself: explains(rows) = duplicates(rows) >= NEEDED, reported as 'main: at least three rows of 1851 repeat an earlier row'. On the run it FAILs with '0 found'. Rests on: evidence_and_reasoning/checks/004_duplicates.md:13-14,22-23,37; python_project/src/check_004_duplicates.py:66-78,154-155

Row: GATED. Part 1 says 'the difference of three'; part 2 says 'the roll's 51 less the note's 48 ... and the three computed from them'; part 5 says 'The gate needs at least three'. NEEDED = ROLL_COUNT - NOTE_FIGURE = 3, and the gate controls pin it from both sides. In memory, NEEDED=2 failed 'two planted repeats fail the gate' and NEEDED=4 failed 'three planted repeats pass it'. The discrepancy line prints it as 'the gate needs 3'. Rests on: evidence_and_reasoning/checks/004_duplicates.md:14-16,37-39,83; python_project/src/check_004_duplicates.py:30-32,78,152-153,186

Row: GATED. Part 1 says 'Built on [check 001], whose count of 51 rows this check takes as a sanity value'; part 3 says 'it holds the 51 rows of 1851 that [check 001] counts'. The condition rows_1851 == ROLL_COUNT PASSes with 51. The 51 is a constant written beside its claim citation, not read from check 001; claim 001 and check 001 were outside this reading. Rests on: evidence_and_reasoning/checks/004_duplicates.md:16-17,51; python_project/src/check_004_duplicates.py:30,133-134

Row: PRINTED_ONLY. Part 1 says '[check 002], whose collated forty-eight it takes as given: the program does not read the note'; part 2 says 'the note's 48, both written into the program beside the claims that state them'. This is true by inspection: NOTE_FIGURE = 48 is a constant used only in NEEDED, and the program opens only the roll and the checksum list. No condition compares 48 with the note, and 48 is never printed. Given 51, the gate controls fix 51 - 48 at 3, but not 48's agreement with the note. The statement is structural, so no condition could gate it. Rests on: evidence_and_reasoning/checks/004_duplicates.md:17-18,37-39; python_project/src/check_004_duplicates.py:29,31-32,89,125-126; python_project/src/roll.py:20,24-36

Row: NOT_COMPUTED. Part 1 says 'that the explanation would also need no more than three, so that the roll's distinct rows number the note's forty-eight exactly, is not tested'. That is accurate: no condition bounds the repeat count from above, and none compares a distinct-row count with 48. The record declares this gap itself, and the gap is moot while the lower half fails. Rests on: evidence_and_reasoning/checks/004_duplicates.md:23-26; python_project/src/check_004_duplicates.py:76-78,155

Row: GATED. Part 2 says the program 'first confirms that the roll it will read is the held file whose SHA-256 checksum ... lists'; part 3 says 'the roll is the held file its checksum names'. The condition compares the roll's SHA-256 with the list's entry for its file name and PASSes (25f4a0fdf8374678). It runs before construct() reads the rows. sha256sum of the CSV equals the first line of the list. Rests on: evidence_and_reasoning/checks/004_duplicates.md:30-32,50-51; python_project/src/check_004_duplicates.py:123-127,192-193; source_documents/Roll1851_market_roll_sha256.txt:1

Row: PRINTED_ONLY. Part 2 says 'and prints the interpreter it runs under'. The program prints 'interpreter: CPython 3.12.3' and records python=3.12.3. No condition asserts the version that the Instrument header line names. Rests on: evidence_and_reasoning/checks/004_duplicates.md:32-33; python_project/src/check_004_duplicates.py:128-129

Row: GATED. Part 2 says 'reads the roll through the project's reader as (date, kind) pairs in file order' and 'The reader must give one row for each of those lines'; part 3 says 'the reader gives one row for each of the file's lines of 1851'. construct() returns roll.read_rows(), and the condition in_file == n PASSes at 51 lines. The condition compares counts only. In memory, a reader that moved 1851-05-15 to 1851-05-16 passed every condition except the main, so 'one for each' is pinned as equal numbers, not line-for-line correspondence. No condition asserts file order, and the repeat count does not depend on it. Rests on: evidence_and_reasoning/checks/004_duplicates.md:33-34,43-44,52; python_project/src/check_004_duplicates.py:61-63,132-137; python_project/src/roll.py:24-36

Row: GATED. Part 2 says the program 'counts the rows of 1851 whose (date, kind) pair has occurred earlier in the list ... a pair entered k times counts k - 1'. duplicates() does exactly this. Its controls pin k=2 (one planted repeat counts 1), three pairs at k=2 (they count 3) and k=3 (one row entered three times counts 2), and all PASS. k - 1 is pinned only at k=2 and k=3. Rests on: evidence_and_reasoning/checks/004_duplicates.md:34-36; python_project/src/check_004_duplicates.py:66-73,146-149

Row: GATED. Part 2 says 'the held file's lines of 1851, read as text, are searched for a line whose date and kind, its first two fields, occur on an earlier line, and for one whose date alone does'. repeated_lines() with by_date_and_kind and with by_date gives repeated_lines_1851=0 and repeated_dates_1851=0. Each key has a planted control, and each count is compared with the reader's. The lines of 1851 are chosen by the text prefix '1851-', not by in_year; see the MISMATCH row. Rests on: evidence_and_reasoning/checks/004_duplicates.md:41-43; python_project/src/check_004_duplicates.py:87-110,160-174

Row: GATED. Part 2 says 'the two routes must agree on both counts'. Two reported conditions compare repeated_lines(lines, by_date_and_kind) with duplicates(rows), and repeated_lines(lines, by_date) with len(days) - len(set(days)). Both PASS. Rests on: evidence_and_reasoning/checks/004_duplicates.md:44-45; python_project/src/check_004_duplicates.py:161-162,166-168

Row: GATED. Part 2 says 'so that a repeated line the reader merged or dropped shows as a disagreement'. Two controls back it: 'a line of 1851 entered twice in the file's text no longer matches the reader' (on the count) and 'a line of 1851 entered twice in the file's text is found' (on the text repeat). In memory, a roll with three repeated lines, read by a reader that merges repeats, failed both sanity conditions and both route agreements. Rests on: evidence_and_reasoning/checks/004_duplicates.md:45-46; python_project/src/check_004_duplicates.py:137-140,161-165

Row: GATED. Part 3 says 'with a control: a line of 1851 entered twice in the file's text no longer matches the reader'. The reported control PASSes. It computes the file's count plus one against the reader's count, so it passes whenever the sanity before it passes. It shows only that the comparison sees one extra line and that the planted line is a line of 1851. Rests on: evidence_and_reasoning/checks/004_duplicates.md:52-54; python_project/src/check_004_duplicates.py:138-140

Row: GATED. Part 3 says 'one row of 1851 entered a second time in a copy of the distinct rows counts as one repeat, three as three, and one row entered three times as two'. These are three reported controls, all PASS (control_one=1, control_three=3). As stated, planted() builds on sorted(set(rows)), a copy of the distinct rows. Rests on: evidence_and_reasoning/checks/004_duplicates.md:54-56; python_project/src/check_004_duplicates.py:81-84,146-149

Row: GATED. Part 3 says 'two planted repeats fail it, and three, the least the explanation needs, pass it'; part 6 says 'three planted repeats pass the gate that two fail'. These are two reported controls, both PASS. Each fails if the threshold moves: in memory, NEEDED=2 failed one and NEEDED=4 failed the other. Rests on: evidence_and_reasoning/checks/004_duplicates.md:56-58,97-98; python_project/src/check_004_duplicates.py:152-153

Row: GATED. Part 3 says 'the main assertion is the gate itself, through the same function'; part 6 says 'its controls, run through the same functions as the main assertion'. The main condition calls explains(rows), the function the gate controls call, and explains() calls duplicates(), the function the counting controls call. This is true by inspection, and the main is a reported condition. Rests on: evidence_and_reasoning/checks/004_duplicates.md:58-59,95-97; python_project/src/check_004_duplicates.py:76-78,146-155

Row: GATED. Part 3 says 'The second route's controls, each planted on the file's lines taken once each: a line of 1851 entered twice is found'. The control takes first_of_each(lines, by_date_and_kind), adds one line of 1851, and asserts exactly 1 repeat. It PASSes. Rests on: evidence_and_reasoning/checks/004_duplicates.md:59-61; python_project/src/check_004_duplicates.py:113-120,163-165

Row: GATED. Part 3 says 'a date of 1851 entered again with the other kind is found by its date and not by its date and kind'. One condition, planted on first_of_each(lines, by_date), asserts the pair (count by date, count by date and kind) == (1, 0). It PASSes. The previous control is the positive counterpart of the negative half. Rests on: evidence_and_reasoning/checks/004_duplicates.md:61-62; python_project/src/check_004_duplicates.py:169-174

Row: GATED. Part 3 says 'The year's boundary is pinned from both sides through in_year ...: 1 January and 31 December 1851 are in the year, 31 December 1850 and 1 January 1852 are not'. These are four reported controls, all PASS, and the two negatives have the two positives as counterparts. Rests on: evidence_and_reasoning/checks/004_duplicates.md:62-65; python_project/src/check_004_duplicates.py:176-179; python_project/src/roll.py:39-41

Row: MISMATCH. Part 3, and the program's own comment, call in_year 'the function every count uses'. Only the reader-side counts use it: duplicates(), rows_1851, days, planted() and the discrepancy line. The file-side counts select 1851 by the text prefix '1851-': the sanity's in_file, its control, repeated_lines() (repeated_lines_1851, repeated_dates_1851 and both text controls), and the choice of each planted line. So the boundary controls do not reach the second route's frame. In memory, widening repeated_lines' default prefix from '1851-' to '18' (both years) left every line of output unchanged. Rests on: evidence_and_reasoning/checks/004_duplicates.md:62-64; python_project/src/check_004_duplicates.py:70,84,92,96,133,136,138,140,164,166,170,175,185

Row: PRINTED_ONLY. Part 5 says 'The gate needs at least three repeated rows of 1851 and the roll holds none'. duplicates_1851=0 is recorded and printed ('0 found', the RESULT line, the discrepancy line). The only condition on it is the main's >= 3, which fails alike for 0, 1 or 2: in memory, a roll with one repeat failed only the main. 'Fewer than three' is gated by that FAIL; 'none' is printed only. The planted controls give it positive counterparts. Rests on: evidence_and_reasoning/checks/004_duplicates.md:83-84; python_project/src/check_004_duplicates.py:146-149,154-155,183-187

Row: PRINTED_ONLY. Part 5 says 'the reader's rows and the file's own lines agree that no row of 1851 repeats an earlier row's date and kind'. The agreement is gated and PASSes. The shared value 0 (duplicates_1851 and repeated_lines_1851) is asserted by no condition beyond the main's >= 3. Both routes have positive controls on this key. Rests on: evidence_and_reasoning/checks/004_duplicates.md:84-85; python_project/src/check_004_duplicates.py:146-149,154-155,161-165

Row: PRINTED_ONLY. Part 5 says 'or even its date'. repeated_dates_1851=0 is printed, but the condition asserts only that the two routes agree. In memory, a roll with a date of 1851 entered again with the other kind gave repeated_dates_1851=1 on both routes and failed only the main. The text route's date key has a planted control; the reader-side date count, len(days) - len(set(days)), has none. Rests on: evidence_and_reasoning/checks/004_duplicates.md:85; python_project/src/check_004_duplicates.py:166-174,185-187

Row: PRINTED_ONLY. Part 5 says 'its 51 rows of 1851 falling on 51 distinct dates'. The 51 rows are gated by the sanity condition. The 51 distinct dates is len(set(days)), which the discrepancy line prints only when found < NEEDED, and no condition asserts it. Rests on: evidence_and_reasoning/checks/004_duplicates.md:85-86; python_project/src/check_004_duplicates.py:133-134,182-187

Row: PRINTED_ONLY. Part 5 says 'The pattern is total, not a near miss'. It is read from the printed 0 against the gate's 3, and no condition tells 0 from 1 or 2. Rests on: evidence_and_reasoning/checks/004_duplicates.md:86-87; python_project/src/check_004_duplicates.py:154-155,186

Row: NOT_COMPUTED. Part 5 says 'since no row repeats at all, the verdict would be the same for any difference above zero, whatever count the note's convention gives'. The program evaluates the gate only at NEEDED = 3. The generalisation follows by arithmetic from the printed, ungated 0, but nothing in the program computes it. 'No row repeats at all' covers only rows and lines of 1851, because the program never searches the 1852 rows. A convention that moved the year's boundary is therefore outside anything the program computed. Rests on: evidence_and_reasoning/checks/004_duplicates.md:87-89; python_project/src/check_004_duplicates.py:32,70,78,96

Row: GATED. Part 6 says 'Not reproduced: duplicated rows do not explain the difference ... and [claim 004], which needs them, is ruled out by this check'. The main condition FAILs and is the only failure (17 PASS, 1 FAIL); the RESULT line says not reproduced and the exit status is 1. The RESULT word is the same for any failure, so the ruling-out is read from the per-condition lines, not from the RESULT line alone. Rests on: evidence_and_reasoning/checks/004_duplicates.md:93-95; python_project/src/check_004_duplicates.py:155,197-201

Row: GATED. Part 6 says 'The check could have passed: its controls ... count planted repeats exactly, and three planted repeats pass the gate that two fail'. The stated grounds are reported controls, and all PASS. The program itself never shows all of its conditions passing on one roll. In memory, a roll of 51 rows of 1851 with three (date, kind) lines repeated, given its own checksum entry, passed all 18 conditions and printed 'reproduced' with exit 0, so the claim holds. With the held checksum list, only the held roll passes the checksum condition. Rests on: evidence_and_reasoning/checks/004_duplicates.md:95-98; python_project/src/check_004_duplicates.py:127,146-155

Row: GATED. Part 6 says 'The probe does not judge a program whose direct run fails'. What the probe does lies outside the program. The program's part is that its direct run fails: it exits 1 whenever any condition fails, here the main. Under the prescribed '-I' direct run it also exits 1, but at import, before any condition runs; see new_problems. Rests on: evidence_and_reasoning/checks/004_duplicates.md:98-99; python_project/src/check_004_duplicates.py:25,197-201

Row: NOT_COMPUTED. Part 6's second pass says a reader searched 'with controls that found planted repeats, one of them placed after the last row of 1852: none, in 1851 or in the whole file'. The record attributes this to a separate reader whose output is in prompt_logs/008_tasks_3_and_4.md, outside this reading. Nothing in this program searches the whole file or plants a repeat in 1852. Rests on: evidence_and_reasoning/checks/004_duplicates.md:107-113; python_project/src/check_004_duplicates.py:70,92-100

Row: GATED. Part 3 opens with 'Named in the program and reported by it:'. Each of the 16 checks part 3 lists is a reported condition. Together with part 2's two route agreements they match the program's 18 reported conditions one for one, and no reported condition goes undescribed. Rests on: evidence_and_reasoning/checks/004_duplicates.md:44-45,50-65; python_project/src/check_004_duplicates.py:127,134,137,139-140,146-179

New problems:
1. MISMATCH. Part 3, and the program's comment, call in_year 'the function every count uses', but the file-side counts select 1851 by the text prefix '1851-'. These are repeated_lines_1851, repeated_dates_1851, the sanity's in_file, its control and both text controls. The four boundary controls therefore pin only the reader route's frame. Widening repeated_lines' default prefix to '18' (both years) changed no line of the run's output, so no control pins the second route's frame. On the held roll this changes nothing: the two routes agree at 51 rows and neither year has a repeat. The fix is either to pass the text route's date field through roll.in_year and add a planted boundary line it must not count, or to narrow the wording to 'every count of the reader's rows'. Where: evidence_and_reasoning/checks/004_duplicates.md:62-64; python_project/src/check_004_duplicates.py:175 (claim) against :92,96,136,138,140,164,170 (prefix)
2. Could-never-pass. As the program stands, no reported condition is unsatisfiable: an in-memory roll of 51 rows of 1851 with three repeated lines, given its own checksum entry, passed all 18 conditions ('reproduced', exit 0). The program's registered mutation, duplicate-entry, is different. It appends rows to the reader's output but leaves the file text that the second route reads untouched. Under it, the condition 'the reader gives one row for each of the file's lines of 1851' can never pass for any roll that has rows of 1851, and both route agreements fail too, so the mutated check can never pass at all. On the held roll it turns the main to PASS (3 found) but fails four conditions: rows_1851=54, 54 rows against 51 lines, and both route agreements. On a roll of 48 rows of 1851 (51 after mutation) it still fails three. A probe that uses this mutation to show the check could pass will never see it pass. Where: python_project/src/check_004_duplicates.py:49-55,137,161-162,167-168; evidence_and_reasoning/checks/004_duplicates.md:7 (Mutation header)
3. The prescribed direct run, python3 -B -I check_004_duplicates.py from python_project/src, stops at 'import roll' with ModuleNotFoundError. The -I flag leaves the script's folder off sys.path, and the program does not add it. The exit status is 1, the same as a genuine 'not reproduced', so exit status alone cannot tell a run that never reached its conditions from one whose main assertion failed. The run for this reading was made with the folder inserted into sys.path, and it reproduced part 4's values exactly. Where: python_project/src/check_004_duplicates.py:25
4. NOT_COMPUTED. 'the verdict would be the same for any difference above zero, whatever count the note's convention gives' is an inference from duplicates_1851=0, a value no condition asserts; the main asserts only >= 3. The program evaluates the gate only at NEEDED=3 and searches only rows and lines of 1851. The inference holds for any positive difference within the calendar-year frame. A note convention that moved the year's boundary would need rows the program never examines (those of 1852). Where: evidence_and_reasoning/checks/004_duplicates.md:87-89
5. A negative with only a partial positive control: 'or even its date', and '51 rows of 1851 falling on 51 distinct dates'. It is computed on two sides, but only the text side's date key has a planted control. The reader-side count, len(days) - len(set(days)), is never shown counting a planted same-date row. The condition asserts only that the two sides agree, so the zero itself is printed, not gated. Where: evidence_and_reasoning/checks/004_duplicates.md:85-86; python_project/src/check_004_duplicates.py:166-168,185-187
6. NOT_COMPUTED by this program: the second pass's negative 'none, in 1851 or in the whole file', and its control 'placed after the last row of 1852'. Both are attributed to a separate reader whose output is in prompt_logs/008_tasks_3_and_4.md, which this reading could not open. The program's own search and controls stop at 1851. The whole-file negative, and part 5's 'no row repeats at all' if it is read as covering the whole roll, therefore rest on that log alone. Where: evidence_and_reasoning/checks/004_duplicates.md:107-113
7. NOT_COMPUTED, declared by the record itself: the upper half of the explanation is not tested, that is, no more than three repeats and distinct rows numbering 48. No condition bounds the count from above. The gap is moot while the lower half fails. Where: evidence_and_reasoning/checks/004_duplicates.md:23-26
8. A negative with no positive control in the program: 'which the note does not say', about the note's counting convention. It concerns the note, which the program by design does not read, so nothing here can control it. It rests on whoever read the note. Where: evidence_and_reasoning/checks/004_duplicates.md:18-21
```

#### The second revision, read by three fresh readers

The reader of check 004 and its record, as a coverage reader:

```
1. [UNTRUE; reaches the verdict] This is the designed failure, and the record reports it correctly as 'Not reproduced'. The claim says three of the roll's rows of 1851 repeat an earlier row's date and kind, so that without them the roll's days of 1851 number 48. That is untrue of the held roll: duplicates_1851=0, repeated_dates_1851=0, and its 51 rows of 1851 fall on 51 distinct dates. The main assertion fails ('0 found') and the program exits 1. Every control passes, run through the same functions: planted repeats are counted 1 as 1, 3 as 3, and a row entered three times as 2; a line repeated in the file's text is counted as 1; the gate fails 2 planted repeats, passes 3 and fails 4. Checked independently in memory, the CSV holds no repeat by exact text, by date and kind trimmed and lower-cased, or by date alone, in 1851 or in the whole file. sha256sum gives 25f4a0fd..., which matches the checksum list. The run gives exactly the values in part 4. Where: evidence_and_reasoning/claims/004_duplicates_explain_gap.md:14-17; python_project/src/check_004_duplicates.py:135-160; source_documents/Roll1851_market_roll/Roll1851_market_roll.csv:2-52; evidence_and_reasoning/checks/004_duplicates.md:82-94

2. [MISMATCH; does not reach the verdict] The record uses 'days' for two different counts. The gate (explains) counts the rows of 1851 less their (date, kind) repeats, which is the number of distinct (date, kind) pairs. Part 5 instead sets the note's forty-eight against distinct dates ('51 rows of 1851 fall on 51 distinct dates, where the note states forty-eight'), and part 1 assumes the note counts 'each day once'. On the held roll and on every planted roll each date has one kind, so the two counts agree and no reported condition tells them apart. Tested in memory: a roll of 51 rows of 1851 with three exact (date, kind) repeats plus one date entered under both kinds passes all 18 conditions and prints 'RESULT: reproduced'. Yet its 48 remaining rows fall on 47 distinct dates; repeated_dates_1851=4 is printed but nothing gates it. The held roll has 51 distinct dates and 51 distinct pairs, so the verdict is unaffected. Where: python_project/src/check_004_duplicates.py:87-89, 161, 169-173; evidence_and_reasoning/checks/004_duplicates.md:13-15, 20-21, 34-35, 82-85; evidence_and_reasoning/claims/004_duplicates_explain_gap.md:14-17

3. [MISMATCH; does not reach the verdict] Part 3, like the program's own comment at line 134, says the counting functions' controls run 'on made-up rolls of 51 rows of 1851'. Two of the four use 52 rows, as computed in memory: 'a row entered three times' is planted(1)+planted(1)[:1], and 'a date entered again with the other kind' is planted(0)+[(1851-01-01, fair)]. Only the one-repeat and three-repeat controls use 51 rows. The counting functions do not depend on the roll's size, so the controls still hold. Where: evidence_and_reasoning/checks/004_duplicates.md:51-54; python_project/src/check_004_duplicates.py:134, 137-139

4. [MISMATCH; does not reach the verdict] Part 3 says the sanity checks are reported 'each with a control', but the 51-row count check (line 125) has none of its own. The two controls beside the sanity checks cover only the checksum (116-117) and the row-for-row match (129). The count itself is borne out: it is a plain equality that would fail if the count were not 51, the row-for-row match holds it to the file's 51 lines opening 1851-, and in_year is pinned at both year boundaries (163-166). Only the wording 'each with a control' is not borne out. Where: evidence_and_reasoning/checks/004_duplicates.md:46-51; python_project/src/check_004_duplicates.py:123-129

5. [NO_CONTROL; does not reach the verdict] Part 2 says the second route makes 'a line the reader merged, dropped, or misread' show as a disagreement. The program's only control for that match drops one row (line 129); it plants no merged or misread line. In memory, each of these failed the row-for-row sanity check: an ISO week date (1851-W02-2, which Python 3.12 reads as 1851-01-07), a basic-form date (18510114), and a quoted remark spanning two lines. The statement is therefore true of the code, but the program does not demonstrate it. On the held roll the match passed with 51 rows on each side. Where: evidence_and_reasoning/checks/004_duplicates.md:39-42; python_project/src/check_004_duplicates.py:104-106, 126-129

6. [OTHER; does not reach the verdict] In memory, three repeats pass every condition and four fail the gate, but the gate on its own does not pin three. I tested rolls whose own lines hold three repeats among 51 rows of 1851, in the held file's CRLF line endings, with their checksum listed: repeats scattered, each next to its original, and the first line of 1851 entered three times. Each passed all 18 reported conditions and exited 0 with 'RESULT: reproduced'. So no condition is NEVER_PASSES, and part 6's 'the check could have passed' holds for the whole program, not only the gate. Four repeats among 51 rows fail the main assertion and nothing else, as do two, so the record's 'four leave 47 and fail it' is exact. The caveat is that the gate is rows less repeats, which is the count of distinct pairs, so added copies never move it. A roll of 48 distinct rows plus 4 repeats (52 rows) passes the gate, labelled '3 rows ... repeat' with '4 found', and fails only the 51-row check. The program's declared mutation duplicate-entry (lines 50-56) does not change the main assertion's result: on the held roll it gives 54 rows with 3 repeats, still 51 (fails), and on a passing roll 54 rows with 6 repeats, still 48 (passes). Only the 51-row check reacts. Exactly three repeats is pinned only by the gate and the 51-row check together. Where: python_project/src/check_004_duplicates.py:50-56, 87-89, 123-125, 156-160; evidence_and_reasoning/checks/004_duplicates.md:34-35, 57-60, 91-94

7. [NOT_COMPUTED; does not reach the verdict] The program does not compute the note's forty-eight. It is the constant NOTE_FIGURE = 48, and the program never reads the note. This covers part 5's 'where the note states forty-eight', the printed 'where the note states 48', and the claim's 'the note's figure [claim 002]'. Parts 1 and 2 of the record disclose this. It does not reach the verdict: the claim itself fixes the 48 and the three, and with zero repeats in the roll the claim is ruled out whatever figure the note states. Where: python_project/src/check_004_duplicates.py:32-33, 172-173; evidence_and_reasoning/checks/004_duplicates.md:18-19, 36-37, 84-85; evidence_and_reasoning/claims/004_duplicates_explain_gap.md:14-17

8. [OTHER; does not reach the verdict] The checksum control does not run altered bytes through the sanity check's comparison. It tests a separate inequality, listed value != sha256(roll + newline), which passes whenever the list names anything other than that one hash, or names nothing at all. In memory, with a list naming other bytes, the sanity check failed and the control still passed. So the control shows only that SHA-256 differs for altered bytes. The sanity check's own equality is plain, and sha256sum confirms the held roll matches the listed hash. Where: python_project/src/check_004_duplicates.py:109-120; evidence_and_reasoning/checks/004_duplicates.md:46-48; source_documents/Roll1851_market_roll_sha256.txt:1

9. [OTHER; does not reach the verdict] Some statements are not about what the program does and cannot be tested from the named files: the note's counting convention and plan 001's scope (part 1); the probe not judging a failing program; the two coverage audits; and what prompt_logs/008_tasks_3_and_4.md and prompt_logs/009_writeup_opened.md contain (part 6). One part of the second pass's report concerns the CSV and could be tested: that it holds no repeat by exact text, by date and kind trimmed and lower-cased, or by date alone, in 1851 or in the whole file. That is true: 0, 0 and 0 in each scope, over 51 and 104 data lines. Where: evidence_and_reasoning/checks/004_duplicates.md:19-23, 94-113

10. [OTHER; does not reach the verdict] The claim's own fields do not yet carry the record's verdict. They read Register OPEN, Verdict none and Verified-by unchecked, and the 'Evidence and route' section is empty. Meanwhile Backed-by names check 004, and the record says check 004 rules the claim out. The program bears on none of these fields. Where: evidence_and_reasoning/claims/004_duplicates_explain_gap.md:4-10, 26

```

The reader of the earlier points, one by one:

```
1. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 1 is still open. NOTE_FIGURE = 48 is still typed by hand. BASIS still names only the roll and its checksum list. No condition compares NOTE_FIGURE with claim 002, check 002 or the note, while the 51 is gated against the roll's own rows. So check 004 would still not notice if claim 002's figure were other than 48. Answered within the point: 'collated' and check 002 are gone, and record section 1 and the constant's comment now say the 48 is taken as given from claim 002 and the note is not read. It does not reach the verdict: with no repeats the gate fails for any figure but 51, and claim 004's own text says forty-eight. Where: python_project/src/check_004_duplicates.py:32, 58-59; evidence_and_reasoning/checks/004_duplicates.md:17-19

2. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 2 is still open, but narrower. Answered within it: the robustness sentence that nothing computed is gone, nothing is now claimed beyond calendar 1851, and record section 1 states the assumption and says the note is not read. Still open: claim 004 now lists 'whether the note's forty-eight counts what the roll's 51 counts' among what it does not claim. Yet its claim sentence says the roll's count exceeds the note's figure by three 'because' three rows repeat. That 'because' explains the gap only if the two figures count the same thing, which record section 1 says the three assumes. So the claim disowns the premise its explanation needs instead of stating it as a condition, and nothing read shows the premise holds. It does not reach the verdict: the claim's statement about the roll (three repeats) fails on the zero found, whatever the note's convention. Where: evidence_and_reasoning/claims/004_duplicates_explain_gap.md:14-17, 21-24; evidence_and_reasoning/checks/004_duplicates.md:19-23

3. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 8 is still open. Only main() calls confirm_roll(), and main() takes no mutation. A run that calls construct(), sanity(), verify() and discrepancies() directly computes no checksum and records no python value (tested in memory: neither appears). The record still does not say whether the probe's wrapped runs go through main(). Its new sentence says only that the probe does not judge a program whose direct run fails. It does not reach the verdict: the direct run passed the checksum. Where: python_project/src/check_004_duplicates.py:109-120, 176-184; evidence_and_reasoning/checks/004_duplicates.md:94-96

4. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 14 is still open, but narrower. Answered within it: repeated_dates() now has a planted control (a date entered again with the other kind counts 1 by date and 0 by date and kind). Still open: the roll's zero repeated dates and its 51 distinct dates are only printed, in the RESULT value and the discrepancy line, and no condition tests them. So the record's 'or even its date' and '51 distinct dates' rest on values that no assertion tells apart from 1 or 2. It does not reach the verdict, and the printed values match the record. Where: python_project/src/check_004_duplicates.py:138-139, 161, 169-173; evidence_and_reasoning/checks/004_duplicates.md:82-85

5. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 15 is still open. The registered mutation duplicate-entry is unchanged: it appends the first three rows of 1851 to the reader's output and leaves the file's text alone. Under it, three assertions fail (tested in memory): the count sanity (54 against 51), the new row-for-row sanity, and the main assertion (54 less 3 is 51, against 48). So the mutated check can never pass. The new row-for-row sanity makes this true of any mutation that changes the reader's rows of 1851; only a mutation of the file's text could pass. The record instead argues 'could have passed' from the gate's controls, and says the probe does not judge a program whose direct run fails. So the mutation does no work for this check, yet it stays registered. It does not reach the verdict. Where: python_project/src/check_004_duplicates.py:9, 50-56, 125-128, 160; evidence_and_reasoning/checks/004_duplicates.md:7, 91-96

6. [OPEN_POINT_STILL_OPEN; does not reach the verdict] Point 16 is still open. Record section 5 still says 'The pattern is total, not a near miss', read from duplicates_1851 = 0, which is only printed. The main assertion fails the same way for 0, 1 or 2 repeats (a control shows two fail the gate), and no condition tells 0 apart from them. It does not reach the verdict. Where: evidence_and_reasoning/checks/004_duplicates.md:85; python_project/src/check_004_duplicates.py:156, 159-160

7. [NO_CONTROL; does not reach the verdict] New: no control tests what makes the row-for-row sanity more than a count check. Its only control, as_text[1:] != text_rows(lines), drops a row, which only changes the count. Once the sanity passes it reduces to 50 != 51 and cannot fail, and the count comparison that point 11 faulted would have caught the same change. No control plants a misread that keeps the count, the case point 11 named, though record section 2 says a line 'merged, dropped, or misread shows as a disagreement'. The comparison itself does catch that case (tested in memory: the reader's rows with the first one dropped and 1851-12-30 added, still 51 rows, differ from the text rows). It does not reach the verdict. Where: python_project/src/check_004_duplicates.py:126-129; evidence_and_reasoning/checks/004_duplicates.md:39-42, 49-51

8. [UNTRUE; does not reach the verdict] New: the program comment and record section 3 say the counting functions' controls run 'on made-up rolls of 51 rows of 1851'. Two of the four do not. planted(1) + planted(1)[:1] (a row entered three times) and planted(0) plus a fair row on 1 January 1851 (a date entered again with the other kind) each hold 52 rows of 1851 (tested in memory). The counts they test do not depend on the roll's size. Where: python_project/src/check_004_duplicates.py:134, 137, 139; evidence_and_reasoning/checks/004_duplicates.md:51-54

9. [UNTRUE; does not reach the verdict] New: record section 3 opens 'Named in the program and reported by it, each with a control', but one of the sanity checks it lists, 'the roll holds the 51 rows of 1851 that [check 001] counts', has no control in the program. The only two controls in confirm_roll() and sanity() belong to the checksum comparison and the row-for-row match. Where: evidence_and_reasoning/checks/004_duplicates.md:46-49; python_project/src/check_004_duplicates.py:125

Answered:
- 3: NEEDED now reaches the RESULT line (needed=3), and the main line prints the gate applied (3 repeats, the note's 48) whether it passes or fails; the sanity label prints ROLL_COUNT. The gate controls' 2, 3 and 4 and planted()'s 51 are still literals, as the record states them, but a changed figure makes them fail, not pass (tested in memory with 47: two gate controls and the main assertion fail). The mutation's literal three is covered under point 15.
- 4: The record no longer speaks for the note's content. Section 1 now says only that claim 002 claims nothing about the convention and that the program does not read the note. Claim 002's own wording is outside the files I was allowed to read.
- 5: 'Collated' and check 002 are gone. Section 1 now separates the 51, gated again against the roll's own rows, from the 48, taken as given from claim 002.
- 6: explains() is now an equality (rows of 1851 less repeats == the note's figure). planted(k) gives 51 rows of 1851 with 51 - k distinct pairs, and controls show that two and four repeats fail and three pass (49, 47 and 48 days). The 'half the roll can refuse' sentence is gone.
- 7: main() reads the roll only when confirm_roll() passes, and a reported control shows the listed checksum does not match the roll's bytes with one byte added.
- 9: A control now passes the file's text through roll.rows_from (the parser read_rows calls), with each date and kind kept once and the first line of 1851 repeated. It requires 52 rows of 1851 and one repeat. A reader that merged the repeated line fails it (tested in memory).
- 10: The comment and the record now call in_year the function the reader's rows are taken by, not the one every count uses. They say the '1851-' prefix route is held to those rows by the row-for-row match, which is true on this file.
- 11: sanity() now compares the reader's rows of 1851 with the file's lines of 1851 as ordered (date text, kind text) lists. The case named, a row dropped and a date the file does not hold emitted, fails it (tested in memory). Its control is weak; see the NO_CONTROL finding.
- 12: The record now says the second-pass reader searched both the whole file and the rows of 1851 and found none in either. It also names the 1852 control (found over the whole file, not in 1851), as prompt_logs/008_tasks_3_and_4.md:611 has it.
- 13: The record now says 'a row that repeats an earlier row, by three keys', which fits the date-alone key, and it restores 'trimmed and lower-cased'. Nit: it now drops the log's 'parsed' from that key.
```

The reader of check 001, the reader, and its tests:

```
1. [NO_CONTROL; does not reach the verdict] The new checksum control does not test the comparison it claims to guard. Line 110 decides whether the roll is read, with ok = listed.get(roll.ROLL.name) == held. The control at lines 112-113 does not reuse that line: it makes its own comparison, listed.get(roll.ROLL.name) != sha256(data + b"\n"), so what it really tests is that hashlib gives a different digest for different bytes. Shown in memory: line 110 was changed to ok = bool(listed.get(roll.ROLL.name)), which only asks whether an entry exists, and a June row was appended to the bytes being hashed. The run then printed '[PASS] sanity: the roll is the file the checksum list names' and '[PASS] control: bytes the list does not name fail that comparison', and confirm_roll() returned True, so the altered roll would have been read. For contrast, breaking two_years() the same way made both of its controls FAIL, because those controls call two_years() itself. The record's part 3 wording ('bytes the list does not name fail the comparison') suggests the guarding comparison is exercised; it is not. A fix: put the comparison in one function and call it from both the sanity and the control, as known_kinds() and in_order() are called. The comparison as written is correct, and sha256sum of the roll gives 25f4a0fd...3fd3, the digest the list names. Where: python_project/src/check_001_count_1851.py:110-113; evidence_and_reasoning/checks/001_count_1851.md:50-51

2. [OTHER; does not reach the verdict] The guard works as the record says: in memory, with the checksummed bytes altered, read_rows() was never called and lines_by_month() never opened the roll. The run printed 'the roll is not the held file, and it is not read' and 'RESULT: not reproduced; python=3.12.3', and exited 1. But the checksum covers one read of the roll, not the bytes that are counted. confirm_roll() hashes roll.ROLL.read_bytes() (line 107). After that, construct() calls roll.read_rows(), which opens the file again by path (roll.py:27). lines_by_month() opens it twice more (line 100, called from verify at 148 and from discrepancies at 166). Spying on a normal run in memory confirmed this: one read_bytes by confirm_roll, then open(roll) by read_rows, then two opens by lines_by_month, none of them checked against the list. So part 2's 'first confirms that the roll it reads is the held file' holds only if the file does not change between the checksum and those reads. The new rows_from() could close the gap: decode the confirmed bytes once, count them with roll.rows_from(io.StringIO(text, newline='')), and have the second route split that same text. construct() does not do this. In memory, rows_from over the checksummed bytes equals read_rows() row for row (104 rows). Where: python_project/src/check_001_count_1851.py:107, 77, 100, 148, 166; python_project/src/roll.py:27; evidence_and_reasoning/checks/001_count_1851.md:26-29

3. [UNTRUE; does not reach the verdict] Two docstrings say rows_from() reads exactly as read_rows() reads the file: rows_from's own ('read as read_rows reads the file') and the module's ('rows_from() reads the same way from lines of text, so that a check can pass a planted text through the reader'). That holds only when the lines are split the way a file opened with newline='' splits them, at \r, \n and \r\n. The new test splits its text with str.splitlines (test_roll.py:47), which also breaks lines at \x0b, \x0c, \x1c-\x1e, \x85, U+2028 and U+2029, so the same text can read differently. In memory, with io.StringIO(t, newline='') standing in for the file: the text 'date,kind,remark\r\n1851-05-27,ordinary,note 1851-06-03,ordinary,\r\n' gave 1 row read as the file is read, but 2 rows through t.splitlines(keepends=True), the second an extra 1851-06-03. A remark holding NEL (\x85) or a form feed was accepted when read as the file is read, but refused when split ('line 3: unknown kind None'). Passing the planted text itself as one string, as the module docstring's wording suggests, is refused with 'unexpected columns: ['d']'. test_reads_text_as_it_reads_the_file tries only a plain text, where the two splits cannot differ, so it cannot catch this. read_rows() itself reads the held file as before, as far as can be told without the old source (the .git folder was out of bounds): the same open(path, newline='', encoding='utf-8'), with the file object handed to the same DictReader. On the held roll, read_rows() equals rows_from over StringIO, rows_from over splitlines with and without line ends, and a parse that does not use the csv module: 104 rows, first (1851-01-07, ordinary), last (1852-12-28, ordinary), 51 in 1851 (49 ordinary, 2 fairs), 53 in 1852. Check 001 does not call rows_from, and the held roll contains none of those characters. Where: python_project/src/roll.py:9-10, 32; python_project/tests/test_roll.py:44-47

4. [MISMATCH; does not reach the verdict] Record part 3 says 'The count's own controls run through the same functions' and names four controls. Two do: the planted row and the relabeled fair both go through count_1851(). The other two repeat the main test's code inline instead of reusing it. The distinct-days control (lines 136-137) builds its own set of days rather than the days set of line 134. The dropped-first-row control (lines 151-154) builds its own month counts rather than reusing by_reader from line 147. Shown in memory: with line 134's set changed to a list (so it counts rows, not days) and one date held twice, '[PASS] main: the 51 rows fall on 51 distinct days' and '[PASS] control: a date held twice gives fewer days than rows' both printed. So neither control would catch a fault in the main test it stands beside. This predates the three changes, and the new checksum control repeats the pattern (see the NO_CONTROL finding above). Where: evidence_and_reasoning/checks/001_count_1851.md:55-59; python_project/src/check_001_count_1851.py:134-137, 147, 151-154

5. [OTHER; does not reach the verdict] The reader 'refuses a row it cannot read, rather than skipping it', say the roll.py docstring and record part 2. That holds for the three refusals the tests try: unknown kind, unreadable date, unexpected columns. It fails for two shapes the tests do not try. csv.DictReader passes over a blank line without a word. A row with more fields than the header is accepted with the extra field dropped: '1851-01-07,ordinary,,1851-06-03' was read as (1851-01-07, ordinary). Also, the 'line {n}' in a refusal counts records, not file lines, so after a blank line a bad kind on file line 3 was reported as 'line 2: unknown kind 'market''. The refactor into rows_from() leaves all three as they were. Every line of the held roll has exactly three fields and none is blank, so none of this touches the count. Where: python_project/src/roll.py:7-9, 34-41; evidence_and_reasoning/checks/001_count_1851.md:32-33

6. [UNTRUE; does not reach the verdict] The test module's docstring says 'Each test writes a small roll of its own to a temporary folder, so that what it tests is the reader and not the held file'. test_the_year_boundary_from_both_sides writes no roll; it calls in_year directly. Accurate wording would be 'each test of reading'. The other six tests do write their own roll, and all 7 pass. Where: python_project/tests/test_roll.py:5-6, 55-59

```

#### The third revision, read by two readers

The reader of check 004, its record, and its claim:

```
Point 1: answered. The gate now also requires 48 distinct dates (check_004_duplicates.py line 90, control at 184-186). In memory, 51 rows with three repeats and one date under both kinds have 47 dates and fail; of the 51-row shapes tried, only 48 days with three exact repeats passes.

Point 2: answered. The gate requires exactly three repeats (line 90), so 48 distinct rows plus four repeats (52 rows) fail, in memory and as the control at line 183. A 52-row roll with three repeats and one date under both kinds still passes the gate alone, but fails the 51-row sanity check (line 140), so the run reports not reproduced (line 214).

Point 3: answered. Record lines 53-56 now say 'on made-up rolls' with no size, which covers the two 52-row rolls (program lines 158-159). The 'among 51 rows' wording at record lines 59-60 applies to planted(2), (3) and (4), which measured 51 rows each.

Point 4: answered. The 51-row count now runs through holds_count with controls at 50 and 52 rows (program lines 140-142, record lines 49-50). In memory both fail and the held roll passes.

Point 5: answered. The match now has controls for a misread that keeps the count and for a line held twice and given once (program lines 148-150, record lines 51-53). In memory, a real merge through the reader (a quote spanning two lines of 1851), a wrong date, a wrong kind, and two swapped rows each fail the match.

Point 6: answered. is_listed (lines 121-123) is now both the comparison confirm_roll returns and the function its control calls (lines 130-132). In memory, a lengthened or altered roll makes main() exit 1 without calling construct (lines 207-213).

Point 7: answered. Claim lines 17-19 state the premise as imposed and the explanation as tested under it, and lines 24-25 disclaim only that the premise holds. Record lines 20-22 say the same.

Point 8: answered. Record lines 99-101 now say the probe runs main(), and main() confirms the checksum before reading (program line 207). The probe is outside the files named, so its description is taken as written.

Point 9: answered. Record lines 86-90 now state the printed 0 and that no date repeats either, matching the run's duplicates_1851=0, repeated_dates_1851=0 and days_1851=51. A search of the check, record and claim finds neither 'total' nor 'near miss'.

Point 10: answered. Record lines 101-105 now say the mutation acts on the reader's rows, that the row-for-row match would take it for a reader fault, and that the control through the reader plants a repeat in the text (program lines 165-174). In memory the mutation gives 54 rows of 1851 and the match fails.

Point 11: answered. The RESULT line now carries days_1851=51 (program lines 190 and 217), as the run printed, and record line 82 states the same value.

New faults:
1. [does not reach the verdict] The read_rows docstring says a row that does not read raises ValueError. A field over 131,072 characters instead raises csv.Error, which is not a ValueError (tried in memory through rows_from). The run still stops on such a row, and the held roll has none. Where: python_project/src/roll.py line 28
```

The reader of check 001, the reader, and its tests:

```
Point 1: answered. python_project/src/check_001_count_1851.py now decides the read (line 124) and runs its control (line 126) through the one is_listed (lines 115-117). With that comparison weakened in memory to 'an entry exists', the control fails and the run exits 1; unweakened, check 001 passes and exits 0.

Point 2: answered. All four controls now call the functions the main tests use, count_1851, distinct_days and by_month (python_project/src/check_001_count_1851.py lines 149, 153, 156, 166), and faults injected into each failed a control while the main tests still passed. The one injected fault that survived is a distinct_days stuck at 51, because line 149 asks only for fewer days than rows; the record's statement that the controls run through the same functions still holds.

Point 3: answered. python_project/src/roll.py lines 10 and 34 now limit rows_from() to a stream opened with newline="", and python_project/tests/test_roll.py line 48 uses io.StringIO(text, newline=""). On nine planted texts that stream matched read_rows() every time, while str.splitlines differed on the three holding U+2028, U+0085, or form feed and vertical tab.

Point 4: answered. python_project/src/roll.py lines 41-43 now refuse blank, short and long rows and give the file's line: after a two-line record the refusal says line 4, where a record count says 3. The tests at python_project/tests/test_roll.py lines 56-66 use one-line records only and would pass under a record count too, so that behavior rests on the in-memory trial; all 11 tests pass.

Point 5: answered. python_project/tests/test_roll.py lines 5-6 now say 'Each test of reading' writes a roll. All eight reading tests call write, and the year-boundary test (lines 69-73) reads no roll.

New faults:
1. [does not reach the verdict] The reader is said to refuse a line it cannot read, a blank line included, rather than skip it, but a remark opening with a quote that never closes takes the lines after it into that remark, which is discarded. In memory, 1851-01-07,ordinary,"oops followed by an unknown kind, a non-row line, a blank line and a good row returned one row and no refusal. The held roll has no quote character, a planted one fails the checksum, and past that it fails the count and the second route. Where: python_project/src/roll.py lines 7-9, 28 and 35; evidence_and_reasoning/checks/001_count_1851.md lines 31-33
2. [does not reach the verdict] The docstring says a row that does not read raises ValueError, but a field over the csv module's 131072-character limit raises csv.Error, which is not a ValueError. The read still stops, and the held roll has no such field. Where: python_project/src/roll.py line 28
```

## Corrections and departures

- While the auditor read, the main thread filled the three slots, opened
  the write-up, and corrected two stale lines, in `DOCUMENT_GENRES.md`,
  `evidence_and_reasoning/editorial_standards.md`, `paper/README.md`,
  `paper/2026-11-20_market_days_1851.md`, the plan's ledger, and
  `CURRENT_STATE.md`. A change to the tree during a fan-out breaks the
  comparison the fan-out rests on, as round 008 recorded; none of these
  files was given to the auditor or to a refuter, and the comparison
  after the audit found no other file changed.
- An audit of the wrong check was started, and stopped before it returned
  (above).
- `CURRENT_STATE.md` said that plan 001's first two claims awaited their
  registers, which round 008 had given them, and the plan's ledger said
  the same of claims 001 and 002, and of claim 003 once this round gave
  it its register; both are corrected.
- The first and second revisions of [check 004] brought faults of their
  own, which their readers found and the next revision put right (above).
- This round ran over two sittings. At the end of the first, the
  project's folder was packed; at the start of the second it was
  restored, and the checksum of every file compared with those recorded:
  no file differed.
- Otherwise none of this round's own; the three departures entry 001
  lists hold.

## Closing status

```
DONE: decisions 1 to 3 of round 008 applied, claim 004 ruled out after a second audit; task 5 opened: three slots filled, the write-up drafted
WAITING ON YOU: the draft to read; two decisions: 1 finding F002, 2 the reading of the first voice rule
```

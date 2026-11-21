# Prompt 008: the four decisions; tasks 3 and 4

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
1. (a). 2. (a). 3. (a). 4. (a).

Then tasks 3 and 4: the mean, and duplicated rows.
--- PROMPT END ---

## What was done

The researcher ruled on the four decisions of round 007, each "(a)", and
each was applied:

- 1: [claim 001] VERIFIED, `Verdict: reproduced`, its `Verified-by:` the
  second pass's route, and its *Evidence and route* written.
- 2: [claim 002] ATTESTED, `Verdict: confirmed`, likewise.
- 3: the mutation set gains relabel-kind and alter-wording, in
  `CHECK_METHODOLOGY.md`'s Slots row and in the sentence that carries
  its value, and in `[vocab] mutations` in `tools/artifacts.toml`.
  [check 001] names and binds relabel-kind, and the probe reads CAUGHT
  under all four of its mutations; [check 002] names alter-wording, and
  its third execution planted it and caught it.
- 4: tension row T001 entered in
  `evidence_and_reasoning/public_record_tensions.md`, as proposed, with
  [claim 001]'s register.

This round edited a rulebook and the configuration, so the
documentation-sweep-owed reminder was said once in the reply; the
researcher's earlier word holds that the next sweep waits for the
write-up (prompt 005).

**Task 3, the mean.** [check 003], a written derivation: 51 / 12 = 17/4
= 4.25, read back to 51, and the twelve monthly counts [check 001] gates
against the file's own lines summing to the same 51. Executed twice, its
planted drop-month caught; [claim 003] written OPEN, formal, depending
on [claim 001].

**Task 4, duplicated rows.** [check 004], a program that fails by
design: the explanation under test needs at least three rows of 1851
repeating an earlier row, and the roll holds none. The probe does not
judge a failing program, and says so; the check's own controls show it
could have passed. [claim 004] written OPEN, depending on [claim 001]
and [claim 002]. The concordance check finds every program in agreement
with its record.

**The readers**, played by subagents that wrote nothing: four probe
readers, for [check 001] and [check 002] as amended and for
[check 003] and [check 004]; a coverage auditor of [check 004]; two
second-pass readers who had not seen the first pass; and a refuter for
each of the 59 gaps and concerns they returned, 66 subagents in all. The
share of usage they took is not known: the harness reports none. The
refuters refuted 8, narrowed 24, and let 27 stand.

What the readers found, and what was done about it:

- The two second passes agree with the first: the mean is 17/4 = 4.25,
  from the CSV alone; and no row of 1851 repeats an earlier row, by
  three keys of the reader's own, with a control that found a planted
  repeat.
- [check 004]'s audit found it weaker than its record: the checksum and
  the interpreter stated and never read; the roll's 51 typed in and not
  checked; the gate of three with no control at two; the discrepancy
  printed as fixed text; and the record's "could have passed" resting on
  a computation outside the program. Its probe reader found that a
  mutation it does not name ended the run in an exception. All were
  answered in the program and its record: the checksum and the
  interpreter read, the 51 gated, the gate pinned from both sides by
  planted repeats, two failing it and three passing it, the discrepancy
  computed, and every mutation of the set now runs to a verdict.
  [claim 004]'s wording now matches the check's, a row repeating an
  earlier row.
- [check 002]'s probe reader found its planted rewording tested on one
  word only, no wrong pinpoint ever planted, step 5's "word for word"
  never saying what a difference is, and the gloss's "transcribed
  passage" read as the claim's statement without saying so. The
  procedure now names step 5's four parts and its reading of the gloss,
  and records the step that flagged each plant; a fourth execution
  planted alter-wording on the interruptions and on the negation, and a
  wrong pinpoint, and caught all three. The sanity check now says the
  count in digits, not any figure, is a transcription error, since page
  1 writes the year in digits. [claim 002] now classifies its form
  consulted as imposed.
- [check 003]'s probe reader found its plant on the cross-check's data,
  not on the count the claim takes. The plant moved to step 1, and a
  second execution caught it at step 4. Its instrument line now names
  the count [claim 001] states, and its first part says the derivation
  takes that count as established. [claim 003] now cites the roll.
- Left, each with its reason: the year's boundary and the rule of
  reading, which no mutation alters, are pinned by [check 001]'s four
  boundary controls and gated by its count of each kind; the mutations
  [check 004] does not name are not run against a failing program, which
  the probe does not judge; the divisor of [check 003], twelve months,
  is imposed with the year's boundary; the probe's notice for a written
  procedure is the tool's wording, the same in every project.

The readers' output, as each returned it, is below. The tree was
recorded by the checksum of every file before the fan-out and compared
after: two files differed, [check 001]'s program and record, by a
correction the main thread made while the readers read, which Corrections
and departures records; reversing it gives back each file's checksum
exactly. The round check: no finding.

**Brought, three decisions**, each with its options and the assistant's
recommendation after them:

1. **The register of [claim 003].** DERIVED: a written derivation and an
   independent cross-check, both recorded, with a second pass that
   agreed. Options: (a) DERIVED, `Verdict: proved`, `Verified-by:
   assistant, a re-derivation from the held CSV by a reader without the
   first pass's reasoning`; (b) leave it OPEN. The assistant recommends
   (a).
2. **The register of [claim 004].** RULED_OUT: [check 004] fails as
   designed, and duplicated rows do not explain the difference. Its
   program was revised after its coverage audit. Options: (a) RULED_OUT
   now, `Verdict: not reproduced`, `Verified-by: assistant, a search of
   the held CSV for repeated rows by a reader without the first pass's
   reasoning`; (b) a second coverage audit of the revised check first,
   then RULED_OUT if it holds; (c) leave it OPEN. The assistant
   recommends (b), as for [claim 001].
3. **A first finding**, for `FINDINGS.md`: `| F001 | The roll holds 51
   market days in 1851, 49 ordinary and 2 fairs | [claim 001] | VERIFIED
   |`. Options: (a) enter it as proposed; (b) reword it; (c) decline it,
   entered as an accepted finding of the findings gate. The assistant
   recommends (a).

### The readers' output

#### The probe's reader for check 001

```
Check 001 is python_project/src/check_001_count_1851.py. It names four of the set's six mutations: shift-year, drop-month, duplicate-entry and relabel-kind (its Mutation line 9, the MUTATIONS dict at lines 64-69, and the record's line 7). The claim's body classifies three inputs. The count is derived "from the roll's rows and nothing else". The year's boundary is imposed by the researcher's choice. That a fair is a day held is imposed by the rule of reading.

| Dependency | Mutation that alters it | Named by the check | Matrix cell |
|---|---|---|---|
| Derived input (the count, from the roll's rows): the rows' dates, which put a row in 1851 | shift-year (every date a year later; no row left in 1851, count 0) | yes | CAUGHT |
| Derived input: every row of 1851 present, none left out | drop-month (the 4 rows of March 1851 removed; 47) | yes | CAUGHT |
| Derived input: each row held once, so 51 rows are 51 distinct days (the check asserts this; the title's "51 market days" needs it) | duplicate-entry (the first three rows of 1851 repeated; 54 rows on 51 days) | yes | CAUGHT |
| Derived input: the kinds as the roll gives them, 49 ordinary and 2 fairs | relabel-kind (the first fair of 1851 relabelled ordinary; 51 in all, split 50 and 1) | yes | CAUGHT |
| Imposed input: the year's boundary, the calendar year (the researcher's choice) | none | n/a | no cell |
| Imposed input: that a fair is a day held (the rule of reading) | none (relabel-kind changes a row's kind, not the rule) | n/a | no cell |
| Frame: the calendar year, as the roll's dates give it, fixed by roll.in_year (the claim says "fixed in [check 001]"). This is the same thing as the imposed boundary | none (shift-year moves the dates the frame reads, not the frame) | n/a | no cell |
| Convention: the rule of reading, "a row of 1851 is a market day whatever its kind" (record part 1, from the protocol note). It also covers each ordinary row being a day held | none | n/a | no cell |

Matrix, check 001: direct and wrapped both pass, so each CAUGHT comes from its mutation. The four CAUGHT cells match the record's part 6. I applied the check's own four mutation functions, in memory, to a stand-in roll built from the record's monthly figures (4,3,4,5,5,4,5,3,5,5,4,4). They give the record's counts: 0, 47, 54, and 51 split 50 and 1. relabel-kind trips only the split assertions (lines 123-124). The total, the distinct days, the date order and the month-by-month second route all still agree, as the record says: "a kind misread is caught by the count of each kind instead".

Dependencies no mutation alters

1. The year's boundary, which is also the frame. The set has no mutation that moves where the year begins or ends.
- shift-year moves every date a whole year and keeps each row's month and day (29 February aside). It changes which year the dates give, never where the boundary falls. It empties 1851, so its CAUGHT says nothing about the boundary.
- The four boundary controls (lines 149-152) pin in_year's code at 1 January and 31 December. They are controls, not an alteration of the imposed choice.
- Every MUTATIONS function maps the rows construct() returns to other rows, so as built no mutation can reach in_year.
- A boundary mutation, for example the year begun on another day, would be planted in memory in the year test the count goes through, roll.in_year. Three things would catch it: the second route, which counts lines by their "1851-" text without going through in_year; "every row counted is dated 1851"; and the boundary controls.

2. The rule of reading: a row of 1851, a fair included, is a market day held. relabel-kind alters a row's kind, not the rule, and under the rule no relabelling moves the total of 51.
- The program has no separate step for the rule. It exists only as count_1851 counting every kind (len(kept), lines 92-95), and the assertions speak of "rows", not of market days held.
- A mutation that stopped counting fairs as days held would be planted there. "51 rows dated 1851" (49) and "2 of them fairs" (0) would catch it.
- The set has no such mutation.

Named mutations that alter nothing the claim depends on

None.
- Each of the four alters the derived input, and each is aimed at rows of 1851, so none perturbs only what the claim disclaims ("nothing about 1852"). drop-month tests d.year == 1851 and month 3. duplicate-entry and relabel-kind select through in_year(..., 1851). shift-year moves 1851's rows out.
- One nuance: judged against the headline 51 market days, relabel-kind is a perturbation the claim says the total does not depend on (a row counts "whatever its kind"). Its CAUGHT rests on the 49/2 split alone. The claim states that split, so the mutation is filed correctly, but the cell supports the split, not the total.
- The set's other two, alter-figure and alter-wording, change the note's transcribed passages. The claim disclaims the note ("nothing about the counting convention of the note [Note1851]"), so for claim 001 they would be robustness checks, and the check rightly leaves them unnamed.

Written procedure

Does not apply. Check 001 is a program, the first CHECK_FORM in Slots.
- Its mutations act in memory on the (date, kind) rows construct() returns. The record's part 6 says the probe applied each one.
- A catch shows as the program's failing verdict ("RESULT: not reproduced", exit 1). The record's part 6 already states each CAUGHT and the count under each.
- The matrix's written procedures (checks 002 and 003) and check 004 are outside this reading.

Limits of this reading

Not opened, being outside the named files: python_project/src/roll.py, the roll's CSV, the counting protocol note, evidence_and_reasoning/terminology.md and tools/falsifiability_probe.py.
- That in_year is the calendar-year test rests on the boundary controls (passed, per the record) and on the frame lines.
- The counts under each mutation were checked against the record's own figures, not against the roll.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. No mutation in the set alters the imposed year boundary (the calendar year), which is also the claim's frame. shift-year moves dates a whole year, keeping each row's month and day, so it never moves the boundary. The four boundary controls pin in_year but are controls, not mutations. Every MUTATIONS function acts on the rows, so none can reach roll.in_year. Refuter: narrowed.
2. No mutation in the set alters the imposed rule of reading, that a row of 1851 (a fair included) is a market day held. relabel-kind changes a row's kind, not the rule, and leaves the total at 51. The program has no separate step for the rule beyond count_1851 counting every kind, and its assertions speak of rows, not of market days held. Refuter: narrowed.
3. relabel-kind's CAUGHT rests on the 49/2 split alone (lines 123-124). Against the headline 51 market days it is a perturbation the claim says the total does not depend on, so the cell supports the split, not the total. Refuter: refuted.
4. Reading limit: roll.py (in_year, read_rows, KINDS), the roll's CSV, the counting protocol note, terminology.md and the probe were outside the named files and not opened. That in_year is the calendar-year test rests on the check's boundary controls and frame lines. The counts under each mutation were confirmed only against the record's monthly figures, on a stand-in roll in memory. Refuter: narrowed.
```

#### The probe's reader for check 002

```
Check 002 (evidence_and_reasoning/checks/002_collate_note.md, a written procedure that is also its own record) backs claim 002 (evidence_and_reasoning/claims/002_note_states_48.md). The mutation set comes from CHECK_METHODOLOGY.md, Slots, {{MUTATION_SET}}. The check names two mutations: alter-figure and alter-wording. The probe's matrix has no row for check 002, only a NOTE that sends the reader to the record's Executions. So every Matrix cell below reads "no cell", followed by what the Executions say.

| Dependency | Mutation that alters it | Named by the check | Matrix cell |
|---|---|---|---|
| Derived input (the claim says "derived from its collation"): the count, "forty-eight" market days, p. 1 | alter-figure | yes | no cell. Executions 1 and 2: planted ("forty-eight" to "forty-seven" in a scratch copy of the claim's statement) and caught |
| Derived input: "held on Tuesdays throughout the year", p. 1 | alter-wording | yes | no cell. Execution 3: planted ("Tuesdays" to "Thursdays") and caught |
| Derived input: "with the customary interruptions at the turn of the year and in the depth of winter", p. 1 | alter-wording | yes | no cell. Never planted on this phrase |
| Derived input: "the roll shows no day held on any other day of the week", p. 1 | alter-wording | yes | no cell. Never planted, so flipping the negation is untested |
| Derived input: what the count is of, "the town's market roll", p. 1 | alter-wording | yes | no cell. Never planted |
| Derived input: no count is stated for 1852, p. 2. The claim puts this under "What is not claimed", but the check's §1 says it is something the claim says | alter-wording (make it state a count: "states no count" to "states fifty market days"); alter-figure only by changing its year, 1852 | yes | no cell. Never planted |
| Inputs the claim's body classifies as imposed | none are classified | n/a | n/a |
| Frame: the year of the count, 1851 ("the year 1851", p. 1) | alter-figure, because the year is a figure in the passage. shift-year does not alter it: it moves the roll's dates, not the note's | yes | no cell. alter-figure was planted only on the count |
| Frame: the source of record, source_documents/Note1851_market_days_note.md, at the SHA-256 checksum its row in the source index records | none | n/a | no cell. Guarded only by step 1 and its control |
| Frame: the page-mark pinpoints (p. 1 for the count and the days, p. 2 for 1852) | none | n/a | no cell. Guarded only by step 4 and the sanity check |
| Convention: the note writes its count in words, so a search for a count must find numbers in words as well as digits | none | n/a | no cell. Guarded only by the step-3 control |
| Convention: the claim restates page 1 in indirect speech, not word for word | none | n/a | no cell. No control |

How the claim classifies its inputs: the body classifies only one input, its statement, as "derived from its collation". It classifies nothing as imposed. Yet it rests on two imposed choices: the note chosen as source of record (at its checksum) and the page-mark frame.

DEPENDENCIES THAT NO MUTATION ALTERS
1. The source of record at its checksum. No mutation in the set swaps or alters the held source. Step 1's control (a scratch copy with one character changed gives a different checksum) shows the checksum is sensitive, but it is not a mutation.
2. The page-mark pinpoints. Step 4 confirms them and the sanity check requires two page marks in order. But no planted alteration shows that step 4 would catch a wrong pinpoint, for example the claim's "[Note1851, p. 1]" changed to "p. 2". alter-figure's gloss covers a figure in a transcribed passage, not a citation.
3. Numbers written in words. The step-3 control guards it: the same search over page 1 must find "forty-eight". Separately, the sanity check says "a figure in digits in the transcription is a transcription error". Read literally, that flags "1851", which page 1 writes in digits. It should say "the count".
4. Indirect speech. Step 5 says to compare "word for word" and to "record any difference". All three executions record "Discrepancies: none". Yet the claim's statement differs from the record's own transcription of page 1 in at least four places:
   - "for 1851" where the note has "for the year 1851"
   - "market days, held on Tuesdays" where the note has "market days. The market was held on Tuesdays"
   - the comma after "throughout the year" is dropped
   - "that" is added before "the roll shows"
   These are editorial changes. But the procedure never says which wording differences count, and whether alter-wording is caught depends on that unstated rule.

NAMED MUTATIONS THAT ALTER NOTHING THE CLAIM DEPENDS ON
None. alter-figure alters the count (and the year); alter-wording alters the days the market was held (and the other phrases). The other four mutations (shift-year, drop-month, duplicate-entry, relabel-kind) alter only the roll. The claim disclaims the roll: it "makes no claim that what it says is true" and says "Nothing about whether forty-eight is right". It also disclaims the note author's counting convention. Named against this claim, those four would be robustness checks filed as mutations. The check correctly names none of them.

WHERE TO PLANT THE ALTERATION, AND WHAT THE RECORD MUST SAY
Where to plant: not in the held note. The record says the note is never edited, and a changed copy of the note would be stopped at step 1 by its checksum. That tests the checksum, not the collation. Plant on the project's side, in a scratch copy of claim 002's text, then follow the procedure again against the held note. The gloss says the change goes in "a transcribed passage"; the record reads that as the claim's statement. That is the right place for a claim about what a source states, but the record should say it reads the gloss this way.
- alter-figure on the count: "forty-eight" to "forty-seven", flagged at step 5. Done (Executions 1 and 2).
- alter-figure on the year: "for 1851" to "for 1850", flagged at step 5 against "the year 1851" under page 1's mark. Not done.
- alter-wording on the days: "Tuesdays" to "Thursdays", flagged at step 5. Done (Execution 3).
- alter-wording on the interruptions and the negation: for example "in the depth of winter" to "at midsummer", and "shows no day held on any other day of the week" to "shows days held on other days of the week", each flagged at step 5. Not done.
- alter-wording on page 2: in "What is not claimed", "for which the note states no count" to "for which the note states fifty market days", flagged at step 3 (no count on page 2). Not done. Also, step 5 compares only with "the statement of [claim 002]", which does not contain this line. The procedure must say that this line is compared too.

What the record must say when the alteration is caught:
- the mutation's short name
- where it was planted: the scratch copy and which line of claim 002 was changed, with the held note untouched
- the exact change, before and after
- what the procedure read from the held note at that place, quoted, with its page mark
- the step that flagged the disagreement
- the word "caught". If it was missed, the record says "missed", and the verdict can no longer rest on this check.
Each named mutation is recorded under the execution that carries the verdict, or carried forward by name from an execution under the same procedure. Execution 3 does this for alter-figure, citing Execution 2. The current entries give everything except the step that flagged the disagreement; they say only "flagged the disagreement".

THE MATRIX
The probe prints no row for check 002, only a NOTE about "the planted alteration", singular. The check names two mutations, caught in different executions: alter-figure in Executions 1 and 2, alter-wording in Execution 3. Someone reading only the matrix sees neither result.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The year 1851, the count's frame, is altered by alter-figure, which the check names. But alter-figure was planted only on the count; no execution plants it on the year. Refuter: refuted.
2. alter-wording was planted only on 'Tuesdays'. It was never planted on the interruptions phrase, on the negation 'no day held on any other day of the week', or on 'the town's market roll'. Refuter: stands.
3. The page-2 dependency (no count stated for 1852) was never planted, and step 5 compares only with the claim's statement, which does not contain it. Refuter: narrowed.
4. Scope mismatch: the check's section 1 (and step 4) says the absence of a count for 1852 is something claim 002 says the note states. The claim puts it under 'What is not claimed', and its Evidence and route says the note was collated 'at page 1'. Refuter: refuted.
5. No mutation in the set alters the source of record (the held note at its recorded checksum). Only step 1 and its control guard it. Refuter: stands.
6. No mutation alters the page-mark pinpoints, and no planted wrong pinpoint ever tests step 4. Refuter: stands.
7. No mutation alters the numbers-in-words convention; only the step-3 control guards it. The sanity check's wording, 'a figure in digits in the transcription is a transcription error', would flag the year 1851, which page 1 writes in digits. It should say 'the count'. Refuter: narrowed.
8. Step 5 requires a word-for-word comparison that records any difference. Yet all three executions record 'Discrepancies: none', although the claim's statement differs from the page-1 transcription in at least four editorial places. The rule for which wording differences count is unstated, and whether alter-wording is caught depends on it. No mutation alters this convention. Refuter: narrowed.
9. The claim's body classifies one input as derived ('derived from its collation') and nothing as imposed, though the source of record at its checksum and the page-mark frame are imposed choices it rests on. Refuter: stands.
10. The record's entries for caught alterations do not name the procedure step that flagged the disagreement. Refuter: stands.
11. The gloss puts alter-figure and alter-wording in 'a transcribed passage'. The record plants them in a scratch copy of the claim's statement without saying that it reads the gloss this way. Refuter: stands.
12. The probe's matrix gives check 002 no row and no per-mutation cells, only a NOTE about one 'planted alteration', though the check names two mutations caught in different executions. Refuter: narrowed.
```

#### The probe's reader for check 003

```
Files read: evidence_and_reasoning/checks/003_monthly_mean.md (the check, a written procedure, with its record under Executions), evidence_and_reasoning/claims/003_monthly_mean.md (the claim), and the Slots table of CHECK_METHODOLOGY.md (the mutation set is at line 523). The check names one mutation in its header: `Mutation: drop-month`. The claim's "Evidence and route" section is empty, so I took its derived and imposed inputs from its Claim paragraph (lines 15 to 17).

| Dependency | Mutation that alters it | Named by the check | Matrix cell |
|---|---|---|---|
| Count, 51 (input, derived from [claim 001]) | drop-month. Removing one month's rows lowers the count by that month's figure. For March, 51 becomes 47 and the mean 47/12, about 3.917 | Yes, and it is the only one named | Check 003 has no cell. The probe's NOTE reads the result from the Executions, which say "caught", but that plant was on step 4's monthly counts, not on this count. Upstream, [check 001] drop-month: CAUGHT |
| Count, 51 | shift-year. The 1851 rows move into 1852, so the 1851 count becomes whatever the roll held for 1850 | No | Check 003 has no cell. Upstream, [check 001] shift-year: CAUGHT |
| Count, 51 | duplicate-entry, but only if [claim 001] counts rows rather than distinct dates. Claim 003 does not say which | No | Check 003 has no cell. Upstream, [check 001] duplicate-entry: CAUGHT |
| Count, 51 | relabel-kind, but only if [claim 001]'s count depends on a row's kind. Claim 003 does not say | No | Check 003 has no cell. Upstream, [check 001] relabel-kind: CAUGHT |
| Count, 51 | Neither alter-figure nor alter-wording. Both change the note's transcribed passage, and the count comes from the roll | n/a | n/a |
| Divisor, 12 calendar months (input, imposed with the year's boundary) | None. drop-month leaves it at 12 because it is imposed, not counted off the roll: the result is 47/12, not 47/11 (about 4.273, close to 4.25) | n/a | none |
| Frame: the calendar year 1851 and its twelve calendar months (fixed in [check 001]) | None changes the frame itself. shift-year moves the roll's dates across the year boundary, and that shows up as a change in the count | n/a | none |
| Convention (not stated): the mean is the count divided by 12, each month weighted alike whatever its length | None | n/a | none |
| Convention (taken over unstated from [claim 001]): what counts as a market day held, meaning which kinds count and whether a date entered twice counts once | None changes the rule. relabel-kind and duplicate-entry change the rows the rule sorts (rows 3 and 4) | n/a | none |

**Dependencies no mutation alters:** the imposed divisor, the frame, and both conventions. Every mutation in the set changes data, either rows of the roll or a transcribed passage of the note. None changes a structural choice, unlike the slot's own example "reverse one structural convention". So the claim's imposed input, its frame and its conventions are never exercised by any mutation. The derived count is exercised only upstream, where [check 001] catches all four roll mutations. Check 003 names drop-month alone.

**Named mutations that alter nothing the claim depends on:** by name, none. drop-month alters the derived count.

As planted, though, it altered nothing the claim depends on. The record says "March's 4 removed from a scratch copy of the transcribed monthly counts". That is step 4's input. It is not one month's rows removed from the roll, which is how the set defines drop-month. Nor is it the count that step 1 takes from [claim 001], which is the claim's input. Steps 1 to 3 never read the monthly counts, so with the plant in place they still give 51/12 = 4.25. Only step 4's cross-check sum moved, to 47.

So what was caught is a disagreement between the monthly counts in [check 001]'s part 4 and the 51 in [claim 001]. That is a transcription cross-check. It does not show the derivation responding to a changed count. The claim does not depend on the monthly counts: it says nothing "about how the market days spread across the months" and uses only the total. The mismatch starts in the check's Instrument line, which names "the held roll's monthly counts" as the derivation's data, while the claim names the count from [claim 001].

The plant is not a robustness check either, since it changed the sum and was caught. It is a consistency test filed as drop-month. alter-figure and alter-wording are not named, and they would be misfiled if they were, because they touch only the note, which the claim excludes.

**Where to plant it, and what the record must say:** plant drop-month on the claim's derived input. That is the count step 1 takes from [claim 001], on a scratch copy, lowered the way removing one month's rows lowers it: March's 4 market days, so 51 becomes 47. Leave the divisor at 12.

It can also be planted upstream, on a scratch copy of the roll with March's rows removed and [check 001]'s program run again. Then step 1 must read the re-run count. As written, step 1 copies the "51" printed in [claim 001], so the plant would never reach it. Step 4's "independent route" runs through the same program over the same rows, so a plant on the roll moves both routes to 47 together, and step 4 cannot catch it. The sanity check (the mean lies between the least and greatest month) also still passes at 3.917. In that case the only catch is the count and the quotient failing to match the procedure's own figures, 51 and 4.25.

When caught, the record should read along these lines:

"The planted alteration, drop-month: March's rows removed, so the count step 1 takes is 47, not 51 [on a scratch copy of that count / of the roll, with [check 001]'s program run again]; the divisor stays 12, imposed. Followed again, 47 / 12 = 47/12, about 3.917, read back 47, which is not the 4.25 claim 003 states [step-1 plant: and step 4's sum of the unaltered monthly counts, 51, disagreed with 47 / roll plant: step 4 agreed at 47, so the quotient is the only catch]: it was caught, at step [n]."

**Other concerns:**
- I computed the 1851 calendar in memory: it has 52 Tuesdays. The recorded monthly counts are one above the Tuesday count in May and October and one below in February, August and December. So the 51 includes days other than the weekly Tuesday, perhaps fairs. If it counts both kinds, relabel-kind leaves 51 unchanged and alters nothing claim 003 depends on. This is an inference only, because I did not read [claim 001].
- The matrix shows [check 004] (python_project/src/check_004_duplicates.py) failing its direct run. I did not read it. If the failure means the shipped roll holds a repeated row, then whether the 51 counts rows or distinct dates is a real question for this claim, not just something a mutation tests.
- The claim's References cite only [Note1851], the note the claim says it states nothing about. Its actual source, [claim 001], appears only under Depends-on.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The drop-month alteration was planted on step 4's transcribed monthly counts. That is not the roll's rows (how the set defines drop-month), and not the count step 1 takes from [claim 001] (the claim's derived input). Steps 1 to 3 still give 51/12 = 4.25, so 'caught' shows a transcription cross-check working, not the derivation responding to a changed count. Refuter: stands.
2. The probe reads check 003's result from its Executions, so it will count drop-month as caught for check 003 even though the plant altered nothing the claim depends on. Refuter: stands.
3. The check's Instrument line names the held roll's monthly counts as the derivation's data, while the claim names the count from [claim 001] as its derived input. That mismatch led to the plant landing on the cross-check input instead of the claim's input. Refuter: narrowed.
4. Step 4's 'independent route' runs through [check 001]'s program over the same rows, so a drop-month planted on the roll moves both routes to 47 and step 4 cannot catch it. Step 1 copies the printed 51, so a plant on the roll reaches it only if step 1 reads a re-run count. The catch must then be stated as a mismatch with the procedure's own 51 and 4.25. The sanity check still passes at 47/12, about 3.917. Refuter: narrowed.
5. No mutation in the set alters the imposed divisor (twelve calendar months), the frame (calendar year 1851 and its months), the averaging convention (count divided by 12, months weighted alike) or the counting convention. The set holds only data alterations, so these dependencies are never exercised. Refuter: narrowed.
6. Claim 003 does not state its counting convention (which kinds count; whether a repeated date counts once), so whether duplicate-entry and relabel-kind change the 51 depends on [claim 001], which I did not read. The 1851 calendar (52 Tuesdays; May and October one above, February, August and December one below) suggests the 51 includes days other than the weekly Tuesday. If so, relabel-kind would leave it unchanged. Refuter: narrowed.
7. [check 004], the duplicates program, fails its direct run. I did not read it. If the shipped roll holds a repeated row, whether the 51 counts rows or distinct dates is a real question for claim 003. Refuter: refuted.
8. The claim's References cite only [Note1851], the note the claim says it states nothing about. Its actual source, [claim 001], appears only under Depends-on. Refuter: narrowed.
9. The claim's Evidence and route section is empty, so the derived and imposed classification had to be read from the Claim paragraph. Refuter: stands.
```

#### The probe's reader for check 004

```
Check 004 is a program, python_project/src/check_004_duplicates.py. Its record is evidence_and_reasoning/checks/004_duplicates.md and it backs evidence_and_reasoning/claims/004_duplicates_explain_gap.md. It names one mutation, duplicate-entry (program line 9, record line 7, and the MUTATIONS table at program lines 47-49). The probe's row for it: direct FAILS (exited 1); duplicate-entry not judged; 1 run, so no wrapped run and no mutated run.

The claim's body classifies no input as derived or imposed, because its "Evidence and route" section is empty (claim line 25). I read the dependencies from three places: the claim's statement (claim lines 14-17), its Depends-on line (claims 001 and 002) and the check's Frame line. The classifications in brackets are my reading, not the claim's.

| # | Dependency | Mutation that alters it | Named by the check | Matrix cell |
|---|---|---|---|---|
| 1 | Input: the roll's count for 1851, 51 rows [derived; claim 001] | shift-year (moves the rows out of 1851); drop-month (removes a month's rows); duplicate-entry (51 becomes 54 as this check plants it). relabel-kind leaves the number of rows unchanged. | duplicate-entry. It is named for row 4 but alters this too, and the check's sanity test "at least 51" (program line 71) accepts 54. | check 004: duplicate-entry not judged; shift-year and drop-month have no cell. Check 001's row (the check the record builds on): shift-year, drop-month and duplicate-entry all CAUGHT. |
| 2 | Input: the note's figure for 1851 [derived; claim 002]. It is 48 by the claim's own arithmetic. | alter-figure | no | check 004: none, because it never reads the note. The figure is the job of the note's collation, evidence_and_reasoning/checks/002_collate_note.md. That is a written procedure with no matrix row; per the probe's NOTE, whether it caught its alteration is read from its Executions (not read here). |
| 3 | Input: the gap of three [derived from rows 1 and 2 in the claim, but written into the check as the literal 3 at program line 82] | Every mutation that alters row 1 or row 2: shift-year, drop-month, duplicate-entry, alter-figure. None of them changes the check's threshold. | duplicate-entry alters it (54 against 48 is a gap of six), but the check still asks for 3. | check 004: duplicate-entry not judged; nothing else was run. |
| 4 | Input: the roll's rows dated 1851 as (date, kind) pairs, and how many repeat an earlier row. This is what the claim asserts. [derived; the held roll read through the project's reader] | duplicate-entry (plants three repeats; it is the set's alteration aimed at this); relabel-kind (can make or remove one repeat, and only where a date carries two rows); drop-month (can only remove repeats); shift-year (swaps in the rows dated 1850, if there are any) | duplicate-entry: yes. The others: no. | check 004: direct FAILS (exited 1); duplicate-entry not judged. Only the record's prose (lines 58-60) says this mutation makes the main assertion pass. |
| 5 | Frame: the calendar year 1851 as the roll's dates give it, fixed by roll.in_year [imposed] | shift-year | no | check 004: none. Check 001's row: shift-year CAUGHT. |
| 6 | Convention: a row of 1851 is a repeat when both its date and its kind match an earlier row; the first occurrence is not counted [imposed by the claim's wording; program lines 59-66] | None changes the rule. relabel-kind changes the kind the rule reads. shift-year moves every date together, so it neither makes nor breaks a pair. | no | none |
| 7 | Convention: the roll's count counts rows, so a repeated row counts one day twice ("so that the roll counts some days more than once") [imposed, through claim 001] | None. duplicate-entry uses this convention but does not change it. | no | none |
| 8 | Convention, unstated: the note's figure counts each day once, so the roll's repeats are its excess over the note. The claim's "because" needs this, yet the claim puts "the note's counting convention" out of scope (claim lines 21-23). [imposed, unstated] | None. alter-wording changes a phrase of a transcribed passage, but claim 004 reads no wording of the note. | no | none |

**Dependencies no mutation alters**
- Row 6, the repeat rule. A date-only rule, for example, is not in the set.
- Row 7, the convention that the roll's count counts rows.
- Row 8, the note counting each day once. The record itself names this as what to check next (record lines 62-63).

Row 3 is a near case. Four mutations change the gap, but none of them reaches check 004, where the gap is the literal 3 and the count is the literal 51 (program lines 71 and 82). A change to the gap can only be caught by the checks behind claims 001 and 002. Of the roll-side mutations the check does not name, drop-month and relabel-kind cannot change this failing verdict: drop-month can only remove repeats, and relabel-kind adds at most one. shift-year could change it only if the roll held at least 51 rows dated 1850 with three repeats among them.

**Named mutations that alter nothing the claim depends on (a robustness check misfiled)**
None. The one named mutation, duplicate-entry, alters row 4, the very thing the claim asserts, and through it rows 1 and 3. alter-wording, which the check does not name, alters none of claim 004's own dependencies as far as the files I read show.

**Written procedure**
Not applicable: check 004 is a program, and its mutation is applied in memory to the rows that construct() returns (program lines 42-49). The one dependency that only a written procedure can guard is row 2, the note's figure, under alter-figure. That belongs to check 002, which this task did not let me read. From the Slots glosses alone (CHECK_METHODOLOGY.md, Slots, the CHECK_FORM and MUTATION_SET rows):
- **Where to plant it:** a changed figure in the transcribed passage that the collation reads against the note at its page marks.
- **What the record must say when it is caught:** its Executions must hold one dated execution for that reading. That execution should name the planted change (which figure, at which page mark, the original and planted values) and state that the collation found the transcription disagreeing with the note there.

**Further concerns**
- (a) The figures the claim takes from claims 001 and 002 are literals in the check: "at least 51" (line 71) and "at least three" (line 82). Under the check's own duplicate-entry, the roll's count becomes 54, a gap of six over the note's figure, and the check still passes with three repeats. So the "could have passed" run shows only that the counter finds planted repeats. It does not show a roll in which repeats explain the gap; that would need three of the 51 rows to be repeats, leaving 48 distinct pairs. The negative verdict stands, because at least three repeats is a necessary condition of the claim.
- (b) The mutation's outcome rests on prose. The record says it was "computed by applying the mutation to the roll's rows in memory" (record lines 58-60). Its Results section gives no value or date for that run, main() never applies MUTATIONS, and the probe's cell is "not judged". I re-ran the program's logic in memory on made-up rows, not the roll. Whenever the 51 rows of 1851 are distinct pairs, it agrees with the record: 54 rows, 3 repeats, the controls unchanged, every assertion passing, exit 0.
- (c) The claim's header has not been updated with the record's verdict. The claim still says Register OPEN, Verdict none, Verified-by unchecked (claim lines 4, 6, 8). The record says "not reproduced" and that the claim is ruled out (record lines 54-56).
- (d) Suppose shift-year were added to guard the frame and the roll holds no row dated 1850. My synthetic re-run shows verify() then raises StopIteration at program line 77, so the run ends in a traceback, not a printed verdict. With one or two such rows, control_three fails instead.
- (e) The claim counts rows that "repeat another row's date and kind" (claim lines 15-16), which read literally counts both rows of a pair. The check counts only rows that match an earlier row (program line 60), which is the excess the gap needs. With no repeats found, both readings give the same verdict.
- (f) The task's limits kept me from reading claims 001 and 002, checks 001 and 002, the roll reader and the roll (source_documents/Roll1851_market_roll/Roll1851_market_roll.csv, program line 51). So the row 2 mapping and the written-procedure part are unverified. The note's figure of 48 is inferred, and I don't know whether the roll holds rows dated outside 1851.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The claim's body classifies no input as derived or imposed because its Evidence and route section is empty. The dependencies were read from the claim's statement, its Depends-on line and the check's Frame line. Refuter: stands.
2. Check 004 does not name the roll-side mutations that alter the claim's dependencies: shift-year (the frame, the count, the rows of 1851), drop-month (the count, the rows) and relabel-kind (the kind half of the repeat rule). Only duplicate-entry is named. Check 001's matrix row shows all four CAUGHT, but how check 001 relates to these dependencies was not read. drop-month and relabel-kind cannot change this failing verdict; shift-year could only if the roll held at least 51 rows dated 1850 with three repeats among them. Refuter: stands.
3. Only alter-figure alters the note's figure (row 2). Check 004 neither names it nor could catch it, since it never reads the note. Whether check 002's written collation plants and catches it is read from its Executions, which this task did not let me read. The planting place and record wording given are inferred from the Slots glosses only. Refuter: refuted.
4. No mutation in the set alters the repeat rule (date and kind both, first occurrence not counted) or the convention that the roll's count counts rows. Refuter: stands.
5. The claim's 'because' rests on an unstated convention: that the note counts each day once. The claim puts the note's counting convention out of scope, no mutation alters it, no check tests it, and the record defers it to a later plan. Refuter: stands.
6. The gap of three and the roll's 51 are literals in the check, not values read from claims 001 and 002, so no mutation of those inputs reaches them. Under the check's own duplicate-entry the count becomes 54, a gap of six, yet the check passes with three repeats. The 'could have passed' run therefore shows only that the counter finds planted repeats, not a roll in which repeats explain the gap. Refuter: narrowed.
7. The record's statement that duplicate-entry makes the main assertion pass rests on an unrecorded in-memory computation. Results gives no value or date for it, main() never applies MUTATIONS, and the probe's cell is 'not judged'. A synthetic re-run of the logic agrees, provided the 51 rows of 1851 are distinct pairs. Refuter: narrowed.
8. The claim's header has not been updated with the record's verdict. It still says Register OPEN, Verdict none, Verified-by unchecked, while the record says 'not reproduced' and that the claim is ruled out. Refuter: stands.
9. Under shift-year, the frame's mutation (not named by the check), verify() raises StopIteration if the roll holds no row dated 1850 (shown on synthetic rows). The run then ends in a traceback instead of a printed verdict; with one or two such rows, control_three fails instead. Refuter: stands.
10. The claim's wording 'repeat another row's date and kind' would count both rows of a pair. The check counts only rows matching an earlier row, which is the excess the gap needs. With no repeats found, the verdict is the same either way. Refuter: narrowed.
11. The task's limits kept me from reading claims 001 and 002, check 001, check 002, the roll reader (imported as roll) and the roll. So the note's figure of 48 is inferred from the claim's arithmetic, and whether the roll holds rows dated outside 1851 is unknown. Refuter: refuted.
```

#### The coverage audit of check 004

```
Coverage audit: check 004 (duplicates), backing claim 004

Files read, and nothing else:
- check = python_project/src/check_004_duplicates.py, with the reader it imports, python_project/src/roll.py
- record = evidence_and_reasoning/checks/004_duplicates.md
- claim = evidence_and_reasoning/claims/004_duplicates_explain_gap.md
- CSV = source_documents/Roll1851_market_roll/Roll1851_market_roll.csv

Line numbers are each file's own. "In memory" means this audit ran the check's own functions with python3 -B -I and wrote nothing. Those runs are the audit's evidence. They are not part of the check, so they close no gap.

**Run as held.** main() printed PASS for both sanity checks and both controls, and FAIL for main ("0 found"). Its RESULT line was "not reproduced; rows_1851=51; control_one=1; control_three=3; duplicates_1851=0", and it returned 1. That matches record §4 value for value and in the same order, so no row is a MISMATCH.

**Classing note.** A statement that a gate failed is classed GATED by that gate: if the statement were false, the gate would pass and the verdict line would change.

| # | Assertion | Where stated | Class | Evidence |
|---|---|---|---|---|
| 1 | The rows under test are the roll's own rows dated 1851 [Roll1851] | record §1; claim, Claim and References | ATTESTED | CSV line 1 is the header `date,kind,remark`. Lines 2–52 hold the 51 rows dated 1851, from 1851-01-07 to 1851-12-23. The first row of 1852 is line 53 (1852-01-06). The check reads this file (BASIS, check line 51). |
| 2 | The roll holds at least 51 rows of 1851 | record §3; check line 71 | GATED | Sanity report at check line 71, `value("rows_1851", n) >= 51`. PASS at 51 (record §4; in memory). |
| 3 | The roll's count for 1851 is exactly 51 ([claim 001]; rows_1851 = 51) | claim, Claim; record §1, §4 | PRINTED_ONLY | rows_1851=51 appears only on the RESULT line (check lines 71, 101). The only gate is `>= 51`, which in memory also passed at 53, 54 and 104. The CSV agrees at lines 2–52. |
| 4 | [check 001] counts 51 rows of 1851, and this check takes that count as its sanity value | record §1, §3; label at check line 71 | NOT_COMPUTED | 51 is typed as a literal at check line 71. Check 001 is neither run nor read, and no value ties the two checks. |
| 5 | Every kind in the roll is ordinary or fair | record §3; check line 72 | GATED | The gate is the reader, not the named report. roll.py lines 33–34 raise ValueError on any other kind (in memory: "line 2: unknown kind 'special'"), which stops the run before any report. So the report at check line 72 can never print FAIL through construct(); it does print FAIL when handed such a row directly. The CSV kind column, lines 2–105, holds 100 ordinary and 4 fair (lines 20, 41, 71, 94). |
| 6 | Frame: a row counts for 1851 when its date falls in calendar year 1851, as roll.in_year fixes it | check line 8; record line 8; roll.py docstring | PRINTED_ONLY | Every count applies it (`day.year == year`, roll.py line 41), but no condition pins it. In memory, with in_year shifted so that 1852 is read as 1851, the sanity check passes at 53 and both controls pass. With in_year admitting every row, the sanity check passes at 104. Only a frame that drops rows of 1851 would trip the sanity minimum. |
| 7 | Instrument: the held roll at its recorded checksum | check line 7; record line 6 | NOT_COMPUTED | Neither the check nor roll.py computes or compares a checksum. The recorded value is in no file this audit may read. The held file's sha256 today is 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3. |
| 8 | Instrument: read with the Python standard library under CPython 3.12.3 | check line 7; record line 6 | NOT_COMPUTED | The run prints no interpreter version, and `sys` is imported (check line 20) but never used. The standard-library part holds by inspection: sys, plus csv, datetime and pathlib inside roll.py. This audit's interpreter was also 3.12.3, which says nothing about the recorded run. |
| 9 | At least three of the roll's rows of 1851 repeat an earlier row's date and kind (the claim says "another row's") | claim, Claim; record §1, §2; check lines 12–13, 82 | GATED | Main report at check line 82 (`>= 3` on duplicates(rows)). It FAILs on the roll with 0 found (record §4; in memory), so the claim's assertion is refuted by its own gate. The construction in record §2 (file order, (date, kind) pairs, rows of 1851 matching an earlier pair) matches check lines 54–66. |
| 10 | Control: one row of 1851 planted twice in a copy of the distinct rows counts as one repeat (control_one = 1) | record §2, §4, §6; check line 79 | GATED | Report at check line 79 (`== 1`), PASS. The planted row is (1851-01-07, ordinary). |
| 11 | Control: three planted rows count as three (control_three = 3) | record §2, §4, §6; check line 80 | GATED | Report at check line 80 (`== 3`), PASS. The planted rows are 1851-01-07, -14 and -21, all ordinary. |
| 12 | No row of 1851 repeats an earlier row's date and kind (duplicates_1851 = 0; "the roll holds none") | record §4, §5 | PRINTED_ONLY | duplicates_1851=0 appears only on the RESULT line. The main condition fails alike at 0, 1 or 2, so no condition asserts 0. The CSV agrees: lines 2–52 carry 51 different dates. |
| 13 | "The pattern is total, not a near miss: the 51 rows are 51 distinct (date, kind) pairs" | record §5 | PRINTED_ONLY | Not computed as such. It follows from the printed 51 and 0 (51 − 0). The check's only set of distinct rows (check line 76) spans both years, 104 pairs in memory, and is never printed. No condition tells 0 from 1 or 2. |
| 14 | "No date of 1851 carries a kind twice" | check lines 88–89 (echoed in record §5) | NOT_COMPUTED | The clause is a fixed string, printed whenever the count is below 3. In memory, one planted repeat prints "...the roll holds 1: no date of 1851 carries a kind twice"; two print "holds 2" with the same clause. |
| 15 | Under the mutation duplicate-entry (three rows of 1851 repeated), the same function counts 3 and the main assertion passes, "computed by applying the mutation to the roll's rows in memory" | record §6; check line 9; record line 7 | NOT_COMPUTED | main() (check lines 92–102) never applies MUTATIONS (lines 47–49), and no report or value records a count under the mutation. Row 16 says the probe did not run it either. In memory the mutated roll gives "3 found" and line 82 passes, so the statement is true, but nothing in the check backs it. |
| 16 | The probe does not judge a program whose direct run fails; the verdict is read from this record | record §6 | NOT_COMPUTED | This describes a process outside the check. Nothing in the check or its output records a probe run. |
| 17 | The note gives a figure for 1851 ([claim 002], [Note1851]) | claim, Claim and References; record §1 | NOT_COMPUTED | BASIS (check line 51) holds only the roll. No file this audit may read gives the figure; 48 (51 − 3) is implied. |
| 18 | The roll's count exceeds the note's figure by three | claim, Claim; record §1 | NOT_COMPUTED | Nothing reads the note or takes a difference. The 3 in the main gate is typed as a literal (check lines 82, 87). |
| 19 | The repeats are why the roll exceeds the note ("because") | claim, Claim; record §1 | NOT_COMPUTED | Only the necessary condition (at least 3 repeats) is tested. Repeats are never removed and the result compared with the note. The gate is one-sided: a pass at 4 or more would not show an excess of exactly three. Not load-bearing for the refutation. |
| 20 | So the roll counts some days more than once | claim, Claim | NOT_COMPUTED | The check keys on (date, kind), so the same day entered under two kinds is never tested, and no count by date alone is made. In memory the 51 rows of 1851 carry 51 different dates (attested at CSV lines 2–52), so that reading would also give 0. |
| 21 | Not reproduced: duplicated rows do not explain the difference, [claim 004] is ruled out, and the program exited 1 | record §4, §6 | GATED | Check lines 98 and 102 derive the verdict and exit code from FAILURES; the main FAIL is the only failure (in memory: "not reproduced", returned 1). With no repeats, repeats explain no excess, whatever its size. The verdict also holds under both wrong frames, because the whole roll has 104 distinct pairs. Row 20's limit on scope applies. |

**Not tabulated.** Provenance and process lines: the Created/updated dates, "Plan: 001, task 4", Backs/Backed-by/Depends-on, By, the run date and author in record §4, and record §6's pointer to the note's counting convention. They agree across the check, the record and the claim, and no check computes them. The claim's "What is not claimed" lines are exclusions of scope, not assertions.

**List 1: negative assertions and their positive controls**

- **N1.** "The roll holds none" / duplicates_1851 = 0 (rows 9, 12).
  - Controls: control_one (one planted repeat counts 1) and control_three (three count 3). Both run through the same duplicates() as the main count, and both PASS. Present.
  - They plant into the de-duplicated, sorted copy rather than the rows in file order. The count does not depend on order, so this does not matter.
- **N2.** "Duplicated rows do not explain the difference; [claim 004] is ruled out" (row 21).
  - Controls: the two counter controls are present. The control that runs the whole procedure, the duplicate-entry mutation making line 82 pass, is stated in record §6 but not run by the check (row 15).
  - GAP.
- **N3.** "Not a near miss": the count is neither 1 nor 2 (row 13).
  - Controls: control_one shows that one repeat would read as 1, and control_three that three would read as 3. Nothing plants 2, and no condition asserts 0.
  - GAP.
- **N4.** "No date of 1851 carries a kind twice" (row 14).
  - Control: none. The clause is fixed text and prints the same at counts of 1 and 2.
  - GAP.
- **N5.** "Every kind is ordinary or fair", that is, no other kind (row 5).
  - Control: none. The named report cannot fail once the reader has run, and no control exercises the reader's refusal.
  - GAP, low stakes: the CSV attests the kinds.
- **N6.** Rows outside 1851 are not counted (row 6).
  - Control: none. Nothing shows a repeat outside 1851 left uncounted, or a repeat at the year's edge counted.
  - GAP; see boundaries (c) and (d) in list 2.
- **N7.** "The probe does not judge a program whose direct run fails" (row 16).
  - Control: none applies, since this describes a process.
  - Its consequence is that nothing ran the mutation result in row 15.

**List 2: quantities, the frames that fix them, and boundary controls**

- **Q1. rows_1851 = 51** (rows 2–4).
  - Frame: calendar year 1851 by roll.in_year, stated in both Frame lines. Fixed, though the frame itself is not gated (row 6).
  - Boundary (a), the sanity minimum `>= 51`:
    - Must pass: 51 rows of 1851.
    - Must fail: 50 rows of 1851.
    - In the check: neither is written as a control. The held roll sits at 51, so the run passes at the edge only by coincidence, and 50 is never run.
    - In memory, through the check's own sanity(): 51 gives PASS; 50 (one row of 1851 removed) gives FAIL.
    - GAP.
- **Q2. duplicates_1851 = 0** (rows 9, 12).
  - Frame: rows of calendar year 1851 by in_year, keyed by (date, kind), with "earlier" meaning earlier in the list (check lines 59–66; record §2). Fixed.
  - Boundary (b), the main minimum `>= 3`:
    - Must pass: 3 repeated rows of 1851.
    - Must fail: 2 repeated rows of 1851.
    - In the check: control_three plants 3 and checks only the count (`== 3`), never line 82's `>= 3`, so an off-by-one gate (`> 3`) would go unnoticed. The mutation that would run line 82 at 3 is not run. Nothing plants 2.
    - In memory, through the check's own verify() and line 82: 2 planted gives "2 found", FAIL; 3 planted gives "3 found", PASS; the mutated roll gives "3 found", PASS.
    - GAP: the fail side is missing and the pass side is only partly run.
  - Boundary (c), the low end of the year:
    - Must pass: a repeat dated 1851-01-01.
    - Must fail: a repeat dated 1850-12-31.
  - Boundary (d), the high end of the year:
    - Must pass: a repeat dated 1851-12-31.
    - Must fail: a repeat dated 1852-01-01.
  - For (c) and (d), in the check: no control at either end. The roll's own edges are 1851-01-07 and 1851-12-23, against 1852-01-06 (CSV lines 2, 52, 53), so the data does not test the ends either.
  - In memory, through in_year and duplicates(): 1850-12-31 not counted, 1851-01-01 counted, 1851-12-31 counted, 1852-01-01 not counted.
  - The same window also bounds Q1.
  - GAP.
- **Q3. control_one = 1 and control_three = 3** (rows 10, 11).
  - Frame: the roll's distinct pairs over both years (104), sorted, plus the planted rows of 1851, counted within 1851 (check lines 76–78; record §2, "a copy of the distinct rows"). Fixed.
  - These are equality gates with no boundary.
- **Q4. 51 distinct (date, kind) pairs among the rows of 1851** (row 13).
  - Frame: calendar year 1851, keyed by (date, kind), as the record's sentence states. Fixed.
  - The value is not computed. The check's only set of distinct rows uses a different frame (both years, 104).
- **Q5. Count under the mutation = 3** (row 15).
  - Frame: the roll's rows in file order plus its first three rows of 1851 (1851-01-07, -14 and -21, all ordinary), counted within 1851 (check lines 42–44). Fixed.
  - Not run by the check.
- **Q6. The note's figure** (row 17).
  - Frame: none. The note's counting convention is out of scope by the claim's own terms and is deferred in record §6, and the check never reads the note.
  - GAP: a quantity without a frame.
- **Q7. The difference of three** (rows 18, 19), which also supplies the main gate's literal limit 3.
  - Frame: only half fixed. The roll side is the calendar year by in_year; the note side has no frame (Q6).
  - GAP. Not load-bearing for the refutation.
- **Q8. Check 001's 51, the sanity limit** (row 4).
  - Frame: not stated here, and not shown to match in_year, since check 001 is not read.
  - GAP.

**Other observation.** The claim file still reads Register OPEN, Verdict none and Verified-by unchecked, with an empty "Evidence and route" section (claim lines 4–8, 25). The record's "ruled out" has not reached it yet.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The mutation result in the verdict is NOT_COMPUTED. Record §6 says duplicate-entry counts 3 and the main assertion passes, 'computed by applying the mutation to the roll's rows in memory', but main() never applies MUTATIONS and no report or value records the count. The record's own statement that the probe does not judge a failing program (also NOT_COMPUTED) means the probe did not run it either. So the control that runs the whole procedure for the negative verdict is stated but not run. In memory it holds: 3 found, PASS. Refuter: narrowed.
2. The main gate's boundary (>= 3) lacks written-out controls run through the gate. No control plants 2 repeats, which must fail. control_three plants 3 but checks only the count (== 3), never line 82's comparison, so an off-by-one gate (> 3) would go unnoticed. Refuter: stands.
3. The sanity minimum (>= 51) has no boundary controls: 51 rows of 1851 must pass and 50 must fail. The held roll sits at 51, so the pass side is met only by coincidence, and 50 is never run. Refuter: narrowed.
4. The year frame is not gated and neither end of the year is tested. With in_year shifted one year (1852 read as 1851), or admitting every row, every condition except main still passes (rows_1851 is 53 or 104). No control at 1851-01-01 (pass) / 1850-12-31 (fail), or at 1851-12-31 (pass) / 1852-01-01 (fail). This does not threaten this verdict, because the whole roll has 104 distinct pairs. Refuter: narrowed.
5. The roll's exact count for 1851 (51, claim 001's count) is PRINTED_ONLY. The only gate is >= 51, which in memory also passed at 53, 54 and 104. Refuter: stands.
6. The link to check 001 is NOT_COMPUTED. Its count of 51 is typed as a literal, check 001 is neither run nor read, and its frame is not shown to match in_year. Refuter: stands.
7. duplicates_1851 = 0, 'the roll holds none', 'the pattern is total, not a near miss' and '51 distinct (date, kind) pairs' are PRINTED_ONLY. No condition separates 0 from 1 or 2, and no control plants 2. The check's only set of distinct rows spans both years (104) and is never printed. Refuter: narrowed.
8. The discrepancy clause 'no date of 1851 carries a kind twice' is fixed text printed for any count below 3. At a count of 1 or 2 it contradicts the number printed beside it. It is NOT_COMPUTED, a negative with no control. Refuter: stands.
9. The instrument line 'the held roll at its recorded checksum' is NOT_COMPUTED: no checksum is computed or compared. The held file's sha256 today is 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3; the recorded value is in no file this audit may read, so they were not compared. Refuter: stands.
10. The instrument line 'CPython 3.12.3' is NOT_COMPUTED: the run prints no interpreter version, and sys is imported but never used. Refuter: stands.
11. The sanity report 'every kind is ordinary or fair' can never print FAIL through construct(), because roll.read_rows raises ValueError on any other kind first. The reader is the real gate, and no positive control exercises its refusal. Low stakes: the CSV's kind column holds only ordinary and fair. Refuter: stands.
12. The note's figure and the roll's excess of three over it are NOT_COMPUTED. The note's figure has no frame, since its counting convention is out of scope, so the main gate's limit 3 is a literal taken from a quantity that is not fully framed. Not load-bearing for the refutation. Refuter: refuted.
13. The causal 'because' is NOT_COMPUTED. The one-sided >= 3 gate can refute the claim but could never confirm an excess of exactly three: a pass at 4 or more would not show it. Not load-bearing for this refutation. Refuter: stands.
14. 'The roll counts some days more than once' is NOT_COMPUTED when read by date alone. The check keys on (date, kind), so the same day entered under two kinds is never tested, and the verdict 'duplicated rows do not explain the difference' is narrower than it reads. In memory the 51 rows of 1851 carry 51 different dates, so that reading would also give 0. Refuter: narrowed.
15. Wording drift between claim and check. The claim counts rows that repeat 'another row's' date and kind, which is all k rows of a group of k. The check counts rows that repeat 'an earlier row's', which is k-1. Both give 0 here, but two repeated pairs would meet the claim's wording (4 rows) and leave the check at 2. Refuter: narrowed.
16. The claim file does not yet carry the record's verdict. It still reads Register OPEN, Verdict none and Verified-by unchecked, with an empty 'Evidence and route' section, while the record says claim 004 is ruled out. This may be left to a later step. Refuter: narrowed.
```

#### The second pass for check 003

```
**1851 market roll: rows per month and the mean (second pass)**

The mean is **51 / 12 = 17/4 = 4.25 rows a month**, exactly. 17/4 is a terminating decimal, so nothing was rounded.

I read only source_documents/Roll1851_market_roll/Roll1851_market_roll.csv and wrote nothing. The file's sha256 is 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3. It has 2,334 bytes and 105 lines: the header `date,kind,remark` and 104 data rows. Line numbers below count the header as line 1.

**Rows dated in each month of 1851**

| Month | Rows | Days of the month |
|---|---|---|
| Jan | 4 | 7, 14, 21, 28 |
| Feb | 3 | 11, 18, 25 |
| Mar | 4 | 4, 11, 18, 25 |
| Apr | 5 | 1, 8, 15, 22, 29 |
| May | 5 | 6, 13, 15 (fair), 20, 27 |
| Jun | 4 | 3, 10, 17, 24 |
| Jul | 5 | 1, 8, 15, 22, 29 |
| Aug | 3 | 5, 19, 26 |
| Sep | 5 | 2, 9, 16, 23, 30 |
| Oct | 5 | 7, 9 (fair), 14, 21, 28 |
| Nov | 4 | 4, 11, 18, 25 |
| Dec | 4 | 2, 9, 16, 23 |
| **Total** | **51** | |

**How I computed it**
1. I parsed the CSV in memory with Python's csv module (`python3 -B -I -c '...'`). All 104 data rows have exactly 3 fields and a valid YYYY-MM-DD date. The file has no blank rows, duplicate dates, extra spaces or byte-order mark. The rows are in date order, every line ends in CRLF, and the file is all ASCII.
2. I kept the rows whose date falls in 1851: 51 of the 104. The other 53 are dated 1852. I counted the 51 by month with collections.Counter, with a month that has no rows counting as 0 (none was empty). The twelve counts add up to 51.
3. I divided by the twelve months with fractions.Fraction(51, 12), which gives 17/4 exactly, or 4.25.
4. I checked this separately with grep:
   - `grep -c "^1851-MM-"` for each month MM gave the same twelve counts.
   - `grep -c "^1851-"` gave 51 and `grep -c "^1852-"` gave 53.
   - `grep -v` showed the header is the only line that does not start with a date in 1851 or 1852.
   - sha256sum gave the hash above, and `wc -l -c` gave the line and byte counts.

**Things to know.** None of these changes 17/4, because the task says each row is a day held.
- **The file also covers 1852.** Despite its name, lines 53 to 105 are 53 rows dated 1852 (1852-01-06 to 1852-12-28). I left them out. Dividing all 104 rows by 12 would give the wrong answer.
- **Two of the counted rows are fairs, not ordinary market days.** They are 1851-05-15 ("spring fair", line 20) and 1851-10-09 ("autumn fair", line 41), both Thursdays. I counted them because the task counts rows. Counting ordinary market days only would give 49 rows and a mean of 49/12 (4.0833..., repeating).
- **Three weekly slots have no row.** All 49 ordinary rows of 1851 fall on a Tuesday, 7 days apart, except for three 14-day gaps. The missing Tuesdays are:
  - 1851-02-04, between lines 5 and 6
  - 1851-08-12, between lines 32 and 33
  - 1851-12-30, between line 52 and the next ordinary row, 1852-01-06, on line 53

  These gaps are why February and August have 3 rows and December has 4. I treated them as days the market was not held, as the task's rule says. The file gives no remark to say whether the market really was not held or the roll just leaves them out. If they were left out, the 1851 total would be 54 and the mean 54/12 = 9/2 = 4.5.
- **Commands beyond the permitted list.** The task allowed `python3 -B -c`, sha256sum and grep. I also added `-I` (isolated mode) to python3 and ran `wc -l -c` on the CSV. Both read only the named file and wrote nothing.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. The file named for 1851 also holds 53 rows dated 1852 (1852-01-06 to 1852-12-28). They were left out of the 1851 count. Dividing all 104 rows by 12 would give the wrong mean. Refuter: narrowed.
2. Two of the 51 counted 1851 rows are fairs, not ordinary market days: 1851-05-15 (spring fair) and 1851-10-09 (autumn fair), both Thursdays. They were counted because the task counts rows and a row is a day held. Counting ordinary market days only would give 49 rows and a mean of 49/12 (4.0833...). Refuter: stands.
3. Three weekly Tuesday slots of 1851 have no row: 1851-02-04, 1851-08-12 and 1851-12-30. Each is a 14-day gap in an otherwise 7-day run of ordinary rows. They were counted as days the market was not held, as the task's rule says, but the file gives no remark saying whether the market was not held or the roll left them out. If they were left out, the total would be 54 and the mean 9/2 = 4.5. These gaps are why February and August show 3 rows and December 4. Refuter: stands.
4. Process: besides the permitted python3 -B -c, sha256sum and grep, this pass added python3's -I (isolated mode) flag and ran wc -l -c on the CSV. Both read only the named file and wrote nothing. Refuter: stands.
```

#### The second pass for check 004

```
Answer: 0. None of the 51 rows dated in 1851 repeats the date and kind of an earlier row. None of them even shares a date with an earlier row.

The only file read: source_documents/Roll1851_market_roll/Roll1851_market_roll.csv (sha256 25f4a0fdf83746788452df281313dea92873ebb4635b88f1ca2f5f35e5c63fd3, 2334 bytes). It has the header date,kind,remark, then 104 data rows:
- 51 dated 1851, on file lines 2-52
- 53 dated 1852, on lines 53-105

The 1851 rows are 49 ordinary and 2 fair (1851-05-15 spring fair, 1851-10-09 autumn fair).

How I found it:
1. I checked the file's text first, so a repeat could not hide behind formatting. There is no BOM, the file is ASCII only and has no tabs. Every row has exactly 3 fields, no field has spaces at either end, and there are no blank rows. Every date parses as an ISO date, and the year from the parsed date matches the "1851-" text prefix on every row.
2. Main method (Python's csv module, in memory): go through the rows in file order and keep a set of every (date, kind) pair already seen, from any year. Count each row dated 1851 whose pair is already in the set. I ran this with three keys:
   - the exact text
   - a cleaned-up key: the parsed date plus the kind, trimmed and lower-cased
   - the date alone, a stricter test that ignores kind
   All three give 0 for 1851, and 0 for the whole file.
3. Independent cross-checks:
   - A tally of the 51 rows from 1851 finds 51 distinct (date, kind) pairs and 51 distinct dates, so 0 repeats.
   - The dates go strictly up in file order across all 104 rows, so no row can repeat an earlier date. This also means file order and date order give the same answer for "earlier".
   - grep finds 51 lines that start with "1851-" and 51 lines that contain "1851" anywhere. All 51 match ^1851-NN-NN,(ordinary|fair),.
   - Splitting the text on newlines and commas by hand, instead of using the csv module, also gives 0.

Control: I ran the same counting function on in-memory copies of the rows with a repeat planted, using the exact-text key unless noted.

Planted repeats, which it should find:
- An exact copy of 1851-05-15,fair,spring fair inserted right after the original: 1, flagged at the inserted row.
- A copy of 1851-01-07,ordinary, added after the last 1852 row: 1. A repeat far from its original is still caught, and the year comes from the row's own date, not its position.
- 1851-03-04,ordinary,second entry (same date and kind, different remark): 1. The remark is not part of the key.
- Three different 1851 rows (01-07, 06-10, 12-23), each copied once: 3. The function counts repeats rather than just noticing one.
- 1851-10-09 fair present three times: 2. Each later copy counts once, so k copies give k-1 repeats.

Negative controls, which it should not count:
- 1851-05-15,ordinary (same date, other kind): 0 with the exact and cleaned-up keys, but 1 with the date-only key. So the kind really is part of the key.
- 1851-05-16,fair (same kind, other date): 0.
- An extra copy of 1852-05-13,fair,spring fair: 0 for 1851, but 1 when counting all years. So the year filter works.

A formatting variant, " 1851-05-15 "," Fair ", gives 0 with the exact-text key and 1 with the cleaned-up key. This shows what the exact-text key alone would miss. Step 1 found no padded or differently-cased fields in the real file, so the two keys agree there. After the controls, the unchanged rows still give 0.

Note: every line of the file, header included, ends in CRLF (105 pairs, with no CR or LF on its own). A plain view does not show this, and it does not affect the count. The csv module handles it. Splitting by hand leaves the CR only on the last field (remark) of all 104 rows, never on date or kind.

How I worked: I read only that one file and wrote nothing. I used the Read tool, sha256sum, grep, and in-memory Python run as python3 -B -I -c. I added -I so Python would not import anything from the project folder, which was the shell's working directory.
```

Its gaps and concerns, each with its refuter's verdict:

```
1. Every line of the file, header included, ends in CRLF (105 pairs), which a plain view does not show. It has no effect on this count, because date and kind never carry the CR. Splitting the text on newlines by hand leaves the CR on the remark field of all 104 rows, so any later step that compares remarks must strip it. Refuter: narrowed.
2. Python was run as python3 -B -I -c, not the exact form python3 -B -c that the rules allow. The extra -I flag only isolates Python so it imports nothing from the project folder, which was the working directory. Nothing was written. Refuter: stands.
3. I took 'earlier row' to mean earlier in file order. The dates go strictly up in file order, so date order gives the same answer (0). This was a choice of reading and does not change the result. Refuter: refuted.
```

## Corrections and departures

While the readers were reading, the main thread corrected a spelling in
[check 001]'s program and record, "relabelled" to the US "relabeled",
the project's convention. A change to the tree during a fan-out breaks
the comparison the fan-out rests on; this one changed words a reader
might have read in either form and nothing a check computes, and the
comparison after it was made exact by reversing it. Otherwise none of
this round's own; the three departures entry 001 lists hold.

## Closing status

```
DONE: decisions 1 to 4 of round 007 applied; tasks 3 and 4 done: the mean 4.25 derived, duplicated rows ruled out by a check that fails by design
WAITING ON YOU: three decisions: 1 the register of claim 003, 2 the register of claim 004, 3 finding F001
```

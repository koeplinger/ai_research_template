# Review: note_v1.md, 6 September 2026

*Created 6 September 2026; updated 6 September 2026.*
Plan: 001

A referee pass by assistant (a subagent given the write-up and nothing else) of `paper/note_v1.md` at its draft of 6 September 2026, before release; blind: yes, no access to the project's claims and checks.

## Structure lens

The referee's inventory, per section, of the draft as reviewed. Five
sections, 44 lines, no displays, four claim tokens.

- **Question.** The object (two synthetic files), the yes/no question
  (does the roll support the note's count), the deliverable (a fact
  about the two files). Load-bearing: the framing and the disclaimer.
  "Market day" not defined here or later.
- **What the roll holds.** Five statements in order: 51 rows
  [claim 001]; 49 ordinary Tuesdays and 2 fairs [claim 001]; a program
  that "fails" under two perturbations; twelve monthly sums adding to 51;
  the mean 4.25 [claim 003]. Both tokens load-bearing. The mean is used
  nowhere else (decorative). Whether the sums and the total are computed
  independently is not said. Needed later and not established here:
  rows outside 1851, the weekday of the fairs, whether two rows share a
  date.
- **What the note states.** The figure forty-eight and the Tuesday
  statement [claim 002]; the collation against the first page; the
  stance (what the note says, not whether it is right). The Tuesday
  statement is testable against the roll and the draft never
  returns to it.
- **Comparison.** Three restates 51 and 48; duplicated rows ruled out
  [claim 004]; the ledger entry with the convention caution. "The
  roll's count" identifies rows with market days, the convention the
  same section declares unknown. The question is answered only
  implicitly.
- **What is not settled.** The reason undecided; two conventions; "neither
  reproduces forty-eight on its face" with a number for one only; held
  open for a later plan (decorative forward reference). "Falls short"
  presumes the roll is the standard.
- **Restatements.** 51 in three places, 49 in two, 48 in three, all
  consistent. Cross-references: the four tokens load-bearing and
  unfollowable for a blind reader; "the note's first page" load-bearing
  and unfollowable; "tension ledger" and "a later plan" procedural.

## Independently re-derived and confirmed

By the referee, from the draft alone: 49 + 2 = 51; 51 / 12 = 4.25;
51 - 48 = 3; 49 - 48 = 1; every restated figure the same figure. Not
re-derivable from the draft: the monthly sums (not given), the count
under a 25 March year (no rows outside 1851 described), the weekday of
the fairs, whether any date carries two rows, the content of any token.
The referee's own calendar computation, offered for the author to
verify and not taken from it: 1 January 1851 a Wednesday, so 1851 has
52 Tuesdays; [check 004] confirmed both.

## Findings

Ranked by severity as the referee ranked them. Each was handed to a
refuter (a subagent given the finding, the passage, and the artifacts
it cites, `governance/roles/refuter.md`); the verdict is recorded
beside it. Fixes to the draft were applied in this round, the draft
being live until its release; fixes that needed the record were brought
to the researcher and directed in prompt 006.

| # | Where | Finding | Fix proposed | Refuted? | Outcome |
|---|---|---|---|---|---|
| 1 | What is not settled, "neither reproduces forty-eight on its face" (major) | asserts a result for the 25 March year that was never computed, from a draft that describes no rows outside 1851; "on its face" hedges the gap; no reason given for the candidate | compute the window or restrict to what was done; delete "on its face"; give the reason or drop the candidate | stands: claim 005 is OPEN, "not yet checked", and the record holds no reason for the candidate | applied: restricted to what was done; the 25 March reading stated as untested; "on its face" deleted; no reason claimed |
| 2 | Comparison, duplicated rows (major) | the check excludes two rows of one date and kind, not two rows of one date with different kinds | report the number of distinct dates | narrowed: the draft glosses the check's exact predicate and claim 004 tests what it says; the fairs are Thursdays, so the 51 rows are 51 dates; what survives is that the draft leaves rows-equal-days implicit | applied: [check 004] and [claim 007] establish 51 distinct dates; the clause added at the Comparison |
| 3 | The roll holds, and Comparison: rows against market days (minor) | the draft identifies a row count with a count of market days without saying so, while calling the note's convention unknown | state the project's convention before the comparison | narrowed: the sense is recoverable from the draft, and the registry gives the roll's rows that sense, so it is not a project-only convention; what survives is the missing explicit sentence | applied: the sentence, fairs included, with the rule fixed before the count |
| 4 | The note states, the weekday statement (minor) | the weekday of the two fair rows is never stated, and the note's "no other day" is testable against the roll | state the weekday; if not Tuesday, a second divergence | stands: the fairs fall on 15 May and 9 October, both Thursdays, a divergence on the roll's face that the draft and the ledger did not record | brought and directed, prompt 006: task 5 of plan 001, [check 004], [claim 007], tension row T002; applied to the note |
| 5 | The roll holds, "fails" and "the same 51" (minor) | "fails" undefined; if the total is the sum of the twelve figures the agreement is tautological | say what the program does under each perturbation; say whether the paths are separate | narrowed: the program computes the total and the monthly sums by separate paths and asserts them equal (check 001, part 6); "fails" survives | applied: the program's behavior stated; the separate path stated |
| 6 | What is not settled, "falls short" (minor) | takes the roll as the standard, which the draft elsewhere declines | "why the two figures differ" | stands | applied, and propagated to `CURRENT_STATE.md`, the roadmap row of plan 002, and plan 002's aspect (`CHECK_METHODOLOGY.md` §7, item 1) |
| 7 | Question, and Comparison (minor) | the yes/no question is never answered; the Comparison ends procedurally | "on the count alone, the roll does not support the note's figure" | refuted: the Comparison states that the count exceeds the figure by three and enters the divergence; "does not support" would state a verdict that claims 001, 002, and 005 and row T001 withhold | none |
| 8 | The roll holds, against the note's "customary interruptions" (minor) | 49 cannot be read against the note's wording without the number of Tuesdays in 1851 | state the number and list the Tuesdays without a row | stands: the draft asserts "Tuesdays" without a check, and no artifact states 52 or the missing three | applied: [check 004] and [claim 007]; the sentence added |
| 9 | The roll holds, the mean (nitpick) | the mean is never used | delete or give it a job | stands | applied: the sentence deleted, a content cut the researcher approved in prompt 006; [claim 003] stays in the record |
| 10 | Comparison, "stands as"; What is not settled, the closing clause (nitpick) | a rhetorical verb; a repetition within the section | "is a divergence"; delete or merge the clause | narrowed: "stands" carries the sense of surviving the ruled-out explanation; the closing clause is a repetition | applied: the clause deleted; the sentence carrying the verb rewritten in the paragraph's rebuild to say that the difference survives the check |

## Deletion ledger and additions

Three sections were rebuilt rather than corrected (What the roll
holds, Comparison, What is not settled); the first version has no
changelog, so the rebuild's ledgers live here (`CHECK_METHODOLOGY.md`
§7, *what a rebuild owes*).

Deleted, classified: "The monthly mean is therefore 4.25 [claim 003]",
content, approved by the researcher, home now the record only; "and we
do not settle them in this note", restatement of "is not decided here";
"on its face", decoration; "neither reproduces forty-eight", content,
replaced by the statement that the first reading is untested. Every
other sentence of the three sections was replaced by its correction, not
appended to.

Added: the convention sentence (finding 3); the weekday and distinct
dates sentence and the Tuesdays sentence (findings 2, 4, 8); the second
divergence at the Comparison (finding 4); "since the 51 rows fall on 51
distinct dates, the excess is one of days" (finding 2). Net word delta
over the three sections: +168 (182 to 350). The whole file was read once after
the rebuild.

## What the released document rests on

After the findings were applied: [claim 001] (the count), [claim 002]
(the figure), [claim 004] (no duplicated row), and [claim 007] (the
weekdays and the distinct dates), and the arithmetic between them, which
the referee confirmed throughout. A reader should still doubt whether
the note's "market days" includes fairs, since the note's convention is
unknown and both ledger rows carry that caution; and the 25 March
reading, which the record has not tested. The document's stance, that
it records what the note says and not whether the note is right, is
kept, and the released text rests on nothing the record does not hold.

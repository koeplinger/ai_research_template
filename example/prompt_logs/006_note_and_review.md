# Prompt 006: the note, the blind referee, the refuter, and the release

*Created 6 September 2026; updated 6 September 2026.*

--- PROMPT START ---
Write the note for plan 001 as version 1 under paper/, a few short
sections. Take it through the blind referee, the note alone, and hand
every finding to a refuter. Apply what the rules let you apply; bring
me the rest with the wording, and where a fix needs a check the record
does not have, propose the task. Stop before the release; I direct it.
--- PROMPT END ---

## What was done

Wrote `paper/note_v1.md` in five sections: the question, what the
register holds, what the note states, the comparison, what is not
settled. A blind referee (a subagent given the note and nothing else,
`governance/roles/blind_referee.md`) returned the structure lens, what
it re-derived, ten findings, and what the document rests on; each
finding went to a refuter (a subagent per finding, given the finding,
the passage, and the artifacts it cites). Five stand, four are narrowed,
one is refuted; all of it is recorded in
`paper/reviews/2026-09-06_assistant_note.md`.

Brought to the researcher and directed in this round: task 5 of plan
001 (the weekdays of the 1851 rows), since the note asserted a weekday
the record had not checked; `python_project/src/check_004_weekdays.py`
with `shift-year` and `drop-month` bound, run: reproduced, the 49
ordinary rows Tuesdays, the two fairs Thursdays, 51 distinct dates, 52
Tuesdays in the year and three without a row; [claim 007], which the
researcher re-ran and assigned VERIFIED; the tension row T002 (the
note's weekday statement against the roll's two Thursday fairs,
caution live); the finding F003; and the content cut of the mean
sentence from the note. Applied to the note: the fixes the review's
Outcome column lists, three sections rebuilt with their deletion ledger
in the review. Propagated the wording of finding 6 to the current
state, the roadmap, and plan 002. Indexed check 004 and claim 007;
updated the current state and the research result.

At the researcher's word, after the findings were disposed of: the
`Released 6 September 2026` stamp written into the note, and the
release recorded in the paper index.

## Corrections and departures

Plan 001 was amended while engaged: task 5 added, with its date and
reason in the plan, the confirmation and refutation criteria unchanged.
Check 001's part 1 named the protocol note by a path relative to the
checks folder; corrected to the repository-relative path, a pointer fix
to a live artifact.

## Closing status

```
DONE: the note written, reviewed blind, every finding refuted or not, the fixes applied or directed, and released
WAITING ON YOU: closing plan 001, in the next round
```

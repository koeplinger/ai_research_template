# Prompt logs

*Created 4 September 2026; updated 6 September 2026.*

Every prompt is recorded here, numbered contiguously and zero-padded to
at least three digits, `NNN_short_description.md`, as the first act of
the round it opens (`MANIFESTO.md` §8). Entries are Markdown, so that
they carry the standard header stamp like every durable artifact. The log
is the record of what was asked and decided; the version history is the
record of what changed and when. Copy [`_template.md`](_template.md) to
start an entry.

## Immutable once committed

An entry is edited only while it is uncommitted; once committed, a
completion or a correction goes in a later entry, and the last column
below points from the earlier entry to it (`DOCUMENT_GENRES.md` §1). This
README and the template are the folder's two current-state files; every
numbered entry is immutable.

## The four parts of an entry

The prompt verbatim between the delimiters, except that material
`MANIFESTO.md` §6 keeps out of the repository (a restricted source's
text, licensed data, personal data) is replaced by a locator and a note
that it was removed before logging; what was done in response; the reason
for any correction or departure from the rules made in the round; and the
round's closing status block. These are the parts the round check looks
for, on an entry still open to editing. The closing status is the
round's final status block in the form `MANIFESTO.md` §16 fixes, inside
a fence so that its labels are not read as header fields; it carries no
`RUNNING` line, since the round has closed. The round check verifies the
form.

## Contents

| Log | Description | Completed or corrected by |
|---|---|---|
| [001](001_setup.md) | set up the project: instantiate, fill the slots, state the question and the thesis | completed by [008](008_project_review.md) |
| [002](002_sources.md) | bring in the two synthetic sources and register them | |
| [003](003_plan_001.md) | draft plan 001 and engage it | |
| [004](004_execute_tasks_1_to_3.md) | execute tasks 1 to 3 of plan 001; assign the first registers | |
| [005](005_task_4_tension_finding.md) | task 4, the tension row, the finding, and the reservation | corrected by [008](008_project_review.md) |
| [006](006_note_and_review.md) | write the note, take it through the blind referee and the refuter, release it | |
| [007](007_close_plan_001.md) | close plan 001 and the round; every gate run | corrected by [008](008_project_review.md) |
| [008](008_project_review.md) | the review of the project as a whole before its first commit; the corrections it directed | |
| [009](009_incremental_update.md) | two incremental updates the fence allows, after the template changed | |

<!-- Every entry appears here; numbering is checked contiguous and every
     entry indexed (MANIFESTO.md section 13). -->

## Not entries

| File | |
|---|---|
| [_template.md](_template.md) | the entry template; not an entry, not numbered; current state |

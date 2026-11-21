# Prompt logs

*Created 4 September 2026; updated 21 November 2026.*

Every prompt is recorded here, numbered contiguously and zero-padded to
at least three digits, `NNN_short_description.md`, as the first act of
the round it opens, setup at a prompt in the template's clone aside
(`MANIFESTO.md` §8). Entries are Markdown, so that
they carry the standard header stamp like every durable artifact; under
the stamp, a `By:` line names who did the work and, for the assistant,
the AI model, which this example withholds (`ONBOARDING.md`, *Standing
directions*). The log is the record of what was asked and decided; the
version history is the record of what changed and when. Copy
[`_template.md`](_template.md) to start an entry.

## Immutable once committed

An entry is edited only while it is uncommitted; once committed, a
completion or a correction goes in a later entry, and the last column
below points from the earlier entry to it (`DOCUMENT_GENRES.md` §1). This
README and the template are the folder's two current-state files, beside
[`attachments/README.md`](attachments/README.md), the index of what the
rounds received; every numbered entry is immutable, and so is every
attachment.

## The four parts of an entry

The prompt verbatim between the delimiters, except that material
`MANIFESTO.md` §6 keeps out of the repository (a restricted source's
text, licensed data, personal data) is replaced by a locator and a note
that it was removed before logging, and what the researcher has decided
must never reach the repository is replaced by that note alone
(`MANIFESTO.md` §8); what was done in response; the reason for any
correction or departure from the rules made in the round; and the round's
closing status block. These are the parts the round check looks for,
together with the `By:` line under the stamp, on an entry not yet
committed. The round check reads no comment in the `By:` line: a line
still holding the artifact template's placeholder, or naming the
assistant with nothing after the comma, is reported as not written. The
closing status is the round's final
status block in the form `MANIFESTO.md` §16 fixes,
or, for a round the next prompt closed, a block of that form saying why
(below). It stands inside a fence, where the round check reads it, and
outside the header block, so its labels are not header fields
(`ONTOLOGY.md` §1.1); it carries no `RUNNING` line, since the round has
closed. The round check verifies the form, and reads no comment there: a
label still carrying the artifact template's placeholder is reported as
not written. An entry whose closing status is not written is **open**,
and the round check run at a commit made before the round closes shows
it so.

A reply that hands work back while a process is still live (a long
computation, a submitted job, a run in another environment) reports it
with the `RUNNING` line §16 requires, and **does not close the round**: a
round runs to the status block that closes it (`MANIFESTO.md`, *Words
used throughout*), and that block comes when the process is done, or at
the next prompt if that comes first.

The next prompt may find the previous entry still open (`MANIFESTO.md`
§8). What follows depends on whether the researcher has committed it:

- **Uncommitted**, it is closed before that prompt is logged: what was
  done up to then, with any work drafted and not yet verified named as
  such, and a closing status saying why the round closed there. A
  process still running passes to the next round, whose entry names it
  and whose replies report it, so the closed entry's closing status
  carries no `RUNNING` line.
- **Committed**, it is never touched. The next round's entry completes
  it: under *What was done* it first names the entry it completes, then
  gives what that entry does not record of its round: what the round
  did, before the commit and after it, the reason for any correction or
  departure made in it, and its closing status. The last column of the
  Contents table below points from the one entry to the other.

So a project whose work outlasts a sitting is not obliged either to close
a round falsely or to leave one unlogged.

## Contents

| Log | Description | Completed or corrected by |
|---|---|---|
| [001](001_setup.md) | The project made from the template: the setup exchange, the run, and the work by hand after it | [004](004_sweep_rulings.md) |
| [002](002_question.md) | The question and the thesis: the research statement, the keystone, and the front page's paragraph | [021](021_last_reading.md) |
| [003](003_documentation_sweep.md) | The first documentation consistency sweep, with this project's item 10 written into its prompt | [012](012_weekdays_in_the_writeup.md), [021](021_last_reading.md) |
| [004](004_sweep_rulings.md) | The sweep's fourteen decisions, ruled and applied | [021](021_last_reading.md) |
| [005](005_sources.md) | The two sources: the roll with its program, and the note, held, registered, and indexed | [010](010_release_sweep.md) |
| [006](006_plan_001.md) | Plan 001, drafted | |
| [007](007_tasks_1_and_2.md) | Plan 001 engaged; its first two tasks, the count and the note's figure | |
| [008](008_tasks_3_and_4.md) | The registers of claims 001 and 002, two names for the mutation set, the first tension row; tasks 3 and 4 | |
| [009](009_writeup_opened.md) | The registers of claims 003 and 004, the first finding; the three waiting slots filled and the write-up drafted | [011](011_weekdays.md), [012](012_weekdays_in_the_writeup.md), [021](021_last_reading.md) |
| [010](010_release_sweep.md) | The second finding and the reading of the first voice rule; the release's first step, the documentation sweep and the recount | |
| [011](011_weekdays.md) | The eight decisions of the sweep; a task added to plan 001, the roll's weekdays | [012](012_weekdays_in_the_writeup.md) |
| [012](012_weekdays_in_the_writeup.md) | The register of claim 005, two tension rows, the third finding; the weekdays in the write-up; the consistency sweep of the record | |
| [013](013_review.md) | The seasons in the write-up, a fourth tension row; the review of the write-up | |
| [014](014_rebuild.md) | The write-up rebuilt on its review; the reading the rebuild owes; the disclosure reading | [017](017_record_sweep.md) |
| [015](015_release.md) | The write-up released; the documentation sweep and the recount that close the release | |
| [016](016_closure_checklist.md) | Five decisions of that sweep; the plan-closure checklist of plan 001, and the two coverage audits it still asked for | [021](021_last_reading.md) |
| [017](017_record_sweep.md) | Plan 001 held open for a consistency sweep of the record over what changed since round 012 | |
| [018](018_plan_closed.md) | Three decisions of that sweep; plan 001 closed, CONFIRMED; plan 002 drafted on the note's counting convention | |
| [019](019_front_page_and_sweep.md) | The front page's account of the example; the last documentation sweep | |
| [020](020_stop.md) | The glossary's entry for the counting convention; plan 002 left at DRAFT, and the project stopped | |
| [021](021_last_reading.md) | A last reading before the example goes out; five closed entries corrected forward | |
| [022](022_rulings_and_stop.md) | Two rulings on that reading; the project stopped | |
| [023](023_template_corrections.md) | The template's later corrections carried into this project's copies | |

<!-- Every entry appears here; numbering is checked contiguous and every
     entry indexed (MANIFESTO.md section 13). -->

## Not entries

| File | |
|---|---|
| [_template.md](_template.md) | the entry template; not an entry, not numbered; current state |
| [attachments/](attachments/) | what the rounds received and keep as received, each named after the entry that received it; not entries; immutable, with an index of their own |

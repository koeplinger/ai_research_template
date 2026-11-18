# Prompt logs

*Created 4 September 2026; updated 18 November 2026.*

Every prompt is recorded here, numbered contiguously and zero-padded to
at least three digits, `NNN_short_description.md`, as the first act of
the round it opens, setup at a prompt in the template's clone aside
(`MANIFESTO.md` §8). Entries are Markdown, so that
they carry the standard header stamp like every durable artifact; under
the stamp, a `By:` line names who did the work and, for the assistant,
the AI model. The log is the record of what was asked and decided; the
version history is the record of what changed and when. Copy
[`_template.md`](_template.md) to start an entry.

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
(below). It stands inside a fence so that its labels are not read as
header fields, and it carries no `RUNNING` line, since the round has
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
| <!-- [001](001_short_description.md) --> | <!-- one line --> | <!-- 014, or blank: the later entry that completes or corrects this one --> |

<!-- Every entry appears here; numbering is checked contiguous and every
     entry indexed (MANIFESTO.md section 13). -->

## Not entries

| File | |
|---|---|
| [_template.md](_template.md) | the entry template; not an entry, not numbered; current state |

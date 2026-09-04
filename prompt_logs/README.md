# Prompt logs

*Created 4 September 2026; updated 4 September 2026.*

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
for.

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

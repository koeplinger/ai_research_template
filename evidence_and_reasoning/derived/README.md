# Derived material

*Created 8 September 2026; updated 8 September 2026.*

What a plan makes from a source before anything is released: a
transcription, a collation, an extract, a processed table, a figure, an
alignment, a coded dataset. It sits between the source of record, which is
never edited (`source_documents/README.md`), and the claim that rests on
it. `DOCUMENT_GENRES.md` §2 makes it a plan's to own and freezes it when
the plan closes, and `ONTOLOGY.md` gives it the `Produced-from` predicate,
which is pre-printed on the template here.

A project whose plans derive nothing may remove this folder at the
researcher's direction, with its two `[[artifact]]` rows and its
`[[index]]` row in `tools/artifacts.toml`, and say so here.

## What belongs here, and what does not

- **Here**: material this project made from a source, which a later reader
  must be able to trace back and, where the source's conditions allow,
  re-derive. It is *evidence the project produced*, not evidence it found.
- **Not here**: the source itself, which is `source_documents/`'s and is
  never edited, renamed, or moved; a check's own record, which is
  `checks/`'s; scratch produced on the way, which is not committed; a
  rendered figure released with a write-up, which is `paper/`'s.
- **A borderline case** is decided by asking what a second reader needs:
  if a claim leans on it, it is derived material and belongs here with its
  provenance; if it only helped the work along, it is scratch.

## Two forms

- **Prose** (a transcription with an apparatus, a collation record, a
  coding scheme): Markdown, carrying the standard header stamp and the
  field lines below. Copy [`_template.md`](_template.md).
- **Non-prose** (a table, a figure, an alignment, an extract): the file
  itself, in whatever form its discipline uses, carrying no header. It is
  dated by the row that lists it below and by the check that produced it,
  as `DOCUMENT_GENRES.md`, *Non-prose files*, says. Where the form admits
  a comment or a sidecar, the provenance goes there; where it does not,
  this index carries it.

## Naming

`NNN_short_description.<ext>`, the number shared with nothing: derived
material is numbered in its own sequence, and a number is never reused. A
file that belongs to one check may take that check's number where a
project prefers it, and says so here.

## What a derived file owes

Every file here answers, in its header or in its row below:

1. **What it came from**, by source token and locus range
   (`Produced-from:`), so that a second reader reaches the same place.
2. **What made it**: the check, program, or procedure that produced it, or
   the party who made it by hand, with the date.
3. **What was imposed on it**: the conventions the derivation fixed, which
   are the `Frame:` of every claim that leans on it (a foliation scheme, a
   calendar, a normalization, a coding, an annotation release).
4. **What it is not**: where the derivation is lossy or interpretive, what
   a reader must not read off it.

The first three are the header's; the fourth is prose, and a derived file
that needs it and has no prose carries it in its row below.

## Contents

| File | Produced from | By | What it is |
|---|---|---|---|
| <!-- [NNN_name.md](NNN_name.md) --> | <!-- [ShortKey, locus range] --> | <!-- [check NNN], or a party and a date --> | <!-- one line; for a non-prose file, what a reader must not read off it --> |

<!-- Every file here appears in this table; the index is checked
     (DOCUMENT_GENRES.md, What the checker verifies, item 8). -->

## Not derived material

| File | |
|---|---|
| [_template.md](_template.md) | the template; not derived material, not indexed as such |

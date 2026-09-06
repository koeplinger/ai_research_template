# Source documents

*Created 3 September 2026; updated 6 September 2026.*

The sources of record (`PRECEDENCE.md`, tier 2): what a source *actually
says*, read against the source itself in the form the project designates.
A work belongs here once a claim is collated against it, the `ATTESTED`
register; a work merely cited lives in the registry alone. Only a source
the researcher may redistribute is held here, each with its license note;
every other source of record is consulted at its locator and indexed here
with its access conditions (`MANIFESTO.md` §6). Anything indexed here is
also registered under `evidence_and_reasoning/references/`.

Naming for held sources, fixed once here: `<key>_short_title.<ext>` for a
file, `<key>_short_title/` for a folder holding one source in several
files (a facsimile by folio, a data release with its documentation), the
key as registered.

## Index

One row per source of record. A row names **either** a held file or
folder with its license note **or** a locator with its access conditions,
never neither (`ONTOLOGY.md` §2.1, `held` and `consulted-at`).

| Key | What | File or folder, or locator | License note, or access conditions | Form consulted |
|---|---|---|---|---|
| [Roll1851] | the market roll of a fictional town, 1851 and 1852, one row per day held | `Roll1851_market_roll.csv` | synthetic, produced by `python_project/src/make_roll.py` for this example; MIT, like the code that made it | data file, as shipped |
| [Note1] | a fictional secondary note stating a count of market days for 1851 | `Note1_market_days_note.md` | synthetic, written for this example; CC BY 4.0, like the documents | the file, as shipped |

## Rules

- **A held source is never edited, renamed, or moved.** Anything derived
  from it lives outside this folder.
- **A restricted source enters the repository only in the form its terms
  allow**: cited by locus, quoted or excerpted as far as its terms permit
  and no further, in a prompt log, a note, or a check alike
  (`MANIFESTO.md` §6, §8).
- **The form consulted is part of the record.** A reading against a
  digital surrogate says so; a second reader returns to the same form
  (`CHECK_METHODOLOGY.md` §3).

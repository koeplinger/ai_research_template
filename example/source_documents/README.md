# Source documents

*Created 3 September 2026; updated 20 November 2026.*

The sources of record (`PRECEDENCE.md`, tier 2): what a source *actually
says*, read against the source itself in the form the project designates.
A work belongs here once claims are to be read against it, whatever their
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
never neither (`ONTOLOGY.md` §2.1, `held` and `consulted-at`). Where the
origin publishes a checksum for a held file, the row records that file's
SHA-256 checksum beside it; where the form consulted is a working copy
kept outside version control (*Rules*, below), the row records the
working copy's beside the locator. In this project every held source's
row records its SHA-256 checksum, whatever its origin publishes, since the
instrument of record names it (`CHECK_METHODOLOGY.md`, *Slots*). Where a held folder, or a working copy
in several files, takes checksums, they go in a checksum list,
`<key>_short_title_sha256.txt` in this folder, tracked even where the
copy is not: one line per file, its SHA-256 checksum and then its path
inside the folder or the copy. The row links the list and records the
list's own checksum. Nothing in this folder has its line endings
converted on checkout (`.gitattributes`), so every checksum recorded
here holds on every system.

| Key | What | File or folder, or locator | License note, or access conditions | Form consulted |
|---|---|---|---|---|
| [Roll1851] | the market roll of a fictional town, 1851 and 1852, with the program that writes it | [Roll1851_market_roll/](Roll1851_market_roll/), its two files' checksums in [Roll1851_market_roll_sha256.txt](Roll1851_market_roll_sha256.txt), whose own SHA-256 is bff1ff79ee8750467674f0ab84ab54deda6a86c45f274b449ebb4d683f1f47b5 | made for this project: the roll under CC BY 4.0 and the program under MIT, the project's own licenses (`LICENSE.md`) | the CSV file as held, read by program |
| [Note1851] | a fictional note stating a count of market days for 1851 | [Note1851_market_days_note.md](Note1851_market_days_note.md), SHA-256 5fb8eb5e76a7233097a77ce00ebab7b9a01e69ce51ffd791e49120309047d66b | made for this project, under CC BY 4.0 (`LICENSE.md`) | the markdown file as held, read at its page marks |

## Rules

- **A held source is never edited, renamed, or moved.** Anything derived
  from it lives outside this folder, under
  `evidence_and_reasoning/derived/`, with its `Produced-from` line naming
  the source and the locus range it came from.
- **A restricted source enters the repository only in the form its terms
  allow**: cited by locus, quoted or excerpted as far as its terms permit
  and no further, in a prompt log, a note, or a check alike
  (`MANIFESTO.md` §6, §8).
- **The form consulted is part of the record.** A reading against a
  digital surrogate says so; a second reader returns to the same form
  (`CHECK_METHODOLOGY.md` §3). Where that form is a working copy no second
  reader can obtain (the researcher's own photographs under a
  personal-use permission, an extract cut under an access agreement), the
  row names it as such and names what the second reader returns to
  instead: the original at its shelfmark, or the extract re-cut from the
  release at its identifier. The return has to be possible for somebody
  else, and saying whose copy was read is part of saying how. The working
  copy itself, which the repository may not hold, is git-ignored or kept
  outside the tree.

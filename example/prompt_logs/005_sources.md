# Prompt 005: the two sources

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
Bring in the two sources. Make the roll with the program that writes it,
and hold the two together as one source, in a folder; make the note and
hold it as a file. Register both, under the keys Roll1851 and Note1851,
and index both with their checksums.

The documentation sweep you reminded me of waits for the write-up.
--- PROMPT END ---

## What was done

The two sources, made for this project and held under
`source_documents/`, as `source_documents/README.md` names them:

- The roll, `Roll1851_market_roll/`, one source in two files. The
  program, `make_roll.py`, writes the market days of a fictional town
  for 1851 and 1852 as CSV: every Tuesday, and two fair days a year,
  less the Tuesdays the town's fictional council cancelled, one row per
  day held, with the columns date, kind and remark. Nothing in it is
  random. Its output was written to `Roll1851_market_roll.csv`, and a
  second run printed the same bytes. The CSV's line endings are the
  carriage return and line feed Python's CSV writer gives; the project's
  `.gitattributes` keeps every file under `source_documents/` byte for
  byte.
- The two files' SHA-256 checksums, in the checksum list
  `source_documents/Roll1851_market_roll_sha256.txt`, which `sha256sum
  -c` verifies from inside the folder.
- The note, `Note1851_market_days_note.md`, a fictional secondary source
  of two pages, marked in its text.

Registered, under the keys the prompt gives, in
`evidence_and_reasoning/references/sources.md`, the registry's first
file, indexed in its folder's README: [Roll1851] and [Note1851], each
with the seven required bullets. Their standing reads "not searched",
the works being made for this project. The registry's README now fixes
this project's key convention, a title word and the year the work
treats, since the works name no author.

Indexed in `source_documents/README.md`: a row for each, giving the
held folder or file, its checksum (for the roll, the checksum list and
the list's own checksum), its license note, and the form consulted. The
project glossary's *Names the sources use* gains the note's own term,
*market days* [Note1851, p. 1], set beside *market day* with no mapping
asserted.

The two statements' "holds" is now true of both files (decision 1 of the
sweep). No plan is drafted and no claim written. On the documentation
sweep the reminder of round 004 named, the researcher: "The
documentation sweep you reminded me of waits for the write-up." The
round check: no finding.

## Corrections and departures

None of this round's own; the three departures entry 001 lists hold.

## Closing status

```
DONE: the roll, with its program, and the note held, registered, and indexed with their checksums
WAITING ON YOU: the first plan, when you want it drafted
```

# Prompt 002: bring in the sources

*Created 6 September 2026; updated 6 September 2026.*

--- PROMPT START ---
Produce the two sources. The roll: a CSV with one row per market day
held, every Tuesday of 1851 and 1852 plus two fairs a year, less a few
Tuesdays the council cancelled, written by a program under
python_project/src so that anyone can regenerate it; make the 1851 count
come out at 51. The note: a two-page fictional secondary source stating
forty-eight market days for 1851 on Tuesdays only, and declining to
count 1852. Register both, index them, and say in every place that they
are synthetic.
--- PROMPT END ---

## What was done

Wrote `python_project/src/make_roll.py`, which writes
`source_documents/Roll1851_market_roll.csv`: 104 rows, 51 dated in
1851 and 53 in 1852, every row a Tuesday held or a fair; nothing in it
is random, and running it again writes the same file. Wrote
`source_documents/Note1_market_days_note.md`, two marked pages. Registered
both under `evidence_and_reasoning/references/sources.md` as [Roll1851]
and [Note1], each with the standing "synthetic, no standing to search";
indexed both in `source_documents/README.md` with their license notes;
indexed the generator in `python_project/src/README.md` as a foundation
module, with three tests under `python_project/tests/`. Added the
project's two terms to the glossary.

## Corrections and departures

None.

## Closing status

```
DONE: the roll generated and the note written, both registered and indexed
WAITING ON YOU: the first plan, in the next round
```

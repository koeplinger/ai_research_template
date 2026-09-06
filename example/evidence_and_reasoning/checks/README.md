# Checks

*Created 3 September 2026; updated 6 September 2026.*

One file per check: `NNN_short_name.md`, the number zero-padded to three
digits with an optional lower-case suffix, never reused. `[check NNN]`
resolves here (`ONTOLOGY.md` §1.3). The configured check pattern is the
numbered form; this `README.md` and [`_template.md`](_template.md) fall
outside it. A check is one self-contained investigation of one claim,
question, or construction (`CHECK_METHODOLOGY.md`); its form is
an executable program with a printed verdict, or a written collation procedure against the source of record.

## The two forms, one file each

- **A check that is a program.** The program is
  `python_project/src/check_NNN_short_name.py`, same number; the file here
  is its **record**: the header lines, what was tested, the results with
  the run's date and party, the discrepancies, the verdict, and the
  second pass, mirroring the program's `RESULT:` line
  (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item 4). One
  file, updated in place while the plan is open.
- **A check that is a written procedure.** The file here **is** the
  check: parts 1 to 3 of `CHECK_METHODOLOGY.md` §8 are the procedure,
  which any reader can follow and which freezes with the plan; parts 4 to
  6 are one dated entry per execution under `## Executions`, naming who
  followed it. That section is a progress ledger (`DOCUMENT_GENRES.md`).

Copy the template for either form and delete the parts that do not apply.
It pre-prints the mandatory fields (`ONTOLOGY.md` §8): `Plan`, `Backs`,
`Instrument`, `Mutation`, and `Frame` where the check has quantities in a
frame.

## Contents

| Check | Form | Backs | Plan | What it settles |
|---|---|---|---|---|
| [001](001_count_1851.md) | program | [claim 001] | 001 | the roll's count of market days in 1851 |
| [002](002_collate_note.md) | procedure | [claim 002] | 001 | collation of the note's stated figure |
| [003](003_duplicates.md) | program | [claim 004] | 001 | duplicated rows in the 1851 entries; fails by design, backing a claim registered RULED_OUT |
| [004](004_weekdays.md) | program | [claim 007] | 001 | the weekdays of the 1851 rows, and the Tuesdays without one |

## Not checks

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a check, not indexed as one |

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}`: an executable program with a printed verdict, or a written collation procedure against the source of record | what a check is in this project (`CHECK_METHODOLOGY.md`) | see that file's Slots table |

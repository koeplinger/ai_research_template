# Checks

*Created 3 September 2026; updated 20 November 2026.*

One file per check: `NNN_short_name.md`, the number zero-padded to three
digits with an optional lower-case suffix, never reused. `[check NNN]`
resolves here (`ONTOLOGY.md` §1.3). The configured check pattern is the
numbered form; this `README.md` and [`_template.md`](_template.md) fall
outside it. A check is one self-contained investigation of one claim,
question, or construction (`CHECK_METHODOLOGY.md`), and here takes one
of the two forms that file's Slots table fixes: a program for a count or a
calendar fact read off the roll, or a written procedure, a collation for
what the note states or a derivation for a quantity derived from a count.

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
`Instrument`, `Mutation` and `By`, which the check row of
`tools/artifacts.toml` requires, and `Frame` where the check has
quantities in a frame.

## Contents

| Check | Form | Backs | Plan | What it settles |
|---|---|---|---|---|
| [001](001_count_1851.md) | program | [claim 001] | 001 | the roll's count of market days in 1851 |
| [002](002_collate_note.md) | procedure | [claim 002] | 001 | the count of market days the note states for 1851 |
| [003](003_monthly_mean.md) | procedure | [claim 003] | 001 | the mean number of market days a month in 1851, derived |
| [004](004_duplicates.md) | program | [claim 004] | 001 | whether repeated rows explain the roll's excess over the note |
| [005](005_weekdays.md) | program | [claim 005] | 001 | the weekdays of the roll's rows of 1851, and its Tuesdays without a row |

## Not checks

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a check, not indexed as one |

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}` | what a check is in this project (`CHECK_METHODOLOGY.md`) | see that file's Slots table |

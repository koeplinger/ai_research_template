# Source index

*Created 3 September 2026; updated 6 September 2026.*

Every program in this folder, indexed; the index is checked
(`DOCUMENT_GENRES.md`, *What the checker verifies*, item 8). A check
program follows the six-part structure of `CHECK_METHODOLOGY.md` §8,
prints its own verdict, and has its record at
`evidence_and_reasoning/checks/NNN_*.md`. Copy
[`_template_check.py`](_template_check.py) to start one.

## Foundation modules

| File | Purpose |
|---|---|
| [make_roll.py](make_roll.py) | writes the synthetic market roll under `source_documents/`; its conventions are the glossary's *market day* and *roll* |

## Checks

| File | Plan, task | Backs | What it settles |
|---|---|---|---|
| [check_001_count_1851.py](check_001_count_1851.py) | 001, 1 | [claim 001] | the roll's count of market days in 1851 |
| [check_003_duplicates.py](check_003_duplicates.py) | 001, 4 | [claim 004] | duplicated rows in the 1851 entries; fails by design, backing a claim registered RULED_OUT |
| [check_004_weekdays.py](check_004_weekdays.py) | 001, 5 | [claim 007] | the weekdays of the 1851 rows, and the Tuesdays without one |

## Not checks

| File | Purpose |
|---|---|
| [_template_check.py](_template_check.py) | the check-program template; not run, not indexed as a check |

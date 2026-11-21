# Programs

*Created 3 September 2026; updated 20 November 2026.*

Every program in this folder, indexed; the index is checked
(`DOCUMENT_GENRES.md`, *What the checker verifies*, item 8). A check
program follows the six-part structure of `CHECK_METHODOLOGY.md` §8,
prints its own verdict, and has its record at
`evidence_and_reasoning/checks/NNN_*.md`. Copy
[`_template_check.py`](_template_check.py) to start one.

## Foundation modules

| File | Purpose |
|---|---|
| [roll.py](roll.py) | the roll's rows as (date, kind), and the year's boundary every count of the roll is stated in (`evidence_and_reasoning/terminology.md`, *the year's boundary*) |

## Checks

| File | Plan, task | Backs | What it settles |
|---|---|---|---|
| [check_001_count_1851.py](check_001_count_1851.py) | 001, 1 | [claim 001] | the roll's count of market days in 1851 |
| [check_004_duplicates.py](check_004_duplicates.py) | 001, 4 | [claim 004] | whether repeated rows explain the roll's excess over the note |
| [check_005_weekdays.py](check_005_weekdays.py) | 001, 6 | [claim 005] | the weekdays of the roll's rows of 1851, and its Tuesdays without a row |

## Not checks

| File | Purpose |
|---|---|
| [_template_check.py](_template_check.py) | the check-program template; not run, not indexed as a check |
| <!-- [<name>.py](<name>.py) --> | <!-- a program that backs no claim, such as one that computes the tables and figures of a write-up: the plan its Plan: line names, and what the program serves --> |

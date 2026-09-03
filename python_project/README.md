# Python project

*Created 3 September 2026; updated 3 September 2026.*

The self-contained computational suite: the check programs, any shared
foundation modules they import, and the tests of those modules. Every
program names the plan it belongs to and the claim it backs, and
[src/README.md](src/README.md) indexes it; the index is checked.

The template presumes a Python interpreter for its tools and ships this
suite in Python. A project that writes its checks in another language
keeps the same layout and the same contract (a printed verdict, a nonzero
exit on failure, a `RESULT:` summary line) and records the language in
`CHECK_METHODOLOGY.md`'s `{{CHECK_FORM}}`.

A project whose checks are all written procedures has no programs. This
folder then holds nothing but its indexes, which stay empty, and the rules
below do not apply; the project may remove the folder at the researcher's
direction, with the reason recorded (`MANIFESTO.md`, *Amending this
manifesto*). A written procedure is a check in every rule
(`CHECK_METHODOLOGY.md`), and nothing in the record requires a program.

## Structure

| Path | Purpose |
|---|---|
| [src/](src/) | all programs, flat: shared foundation modules and `check_NNN_*.py`; [src/README.md](src/README.md) indexes every one |
| [tests/](tests/) | the test suite for the foundation modules; a check program is not tested here, it is its own test |
| [conftest.py](conftest.py) | puts `src/` on the path; the whole test configuration |
| [requirements.txt](requirements.txt) | the pinned dependencies of the checks |

## Running

```bash
cd python_project
pip install -r requirements.txt
python3 -m pytest tests/ -v           # the foundation suite
python3 src/check_NNN_short_name.py   # one check
```

## Design rules

- **Runnable offline** after the dependencies are installed.
- **Deterministic**: fixed seeds wherever sampling is used.
- **The instrument of record is pinned.** Where {{VERIFICATION_TOOL}} is
  software, its exact version is in `requirements.txt`, so that a second
  reader returns to the same thing (`CHECK_METHODOLOGY.md` §3).
- **Exact arithmetic where the claim depends on it**; floating point only
  where the claim is about a floating-point quantity, and then with its
  tolerance stated and asserted.
- **A check prints its own verdict**, exits nonzero on any failure, and
  ends with one line `RESULT: <verdict>; <name>=<value>; ...` that the
  concordance check compares with the check's record
  (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item 4).
- **No assertion with a constant condition**: a reported assertion whose
  truth does not depend on the computation asserts nothing, and the
  linter reports it.
- **Every mutation is bound.** Each name in a check's `Mutation:` line is
  a member of {{MUTATION_SET}}, bound in the program so the probe can
  apply it (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item
  3).

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}` | what a check is in this project; this suite ships the program form (`CHECK_METHODOLOGY.md`) | see that file's Slots table |
| `{{VERIFICATION_TOOL}}` | the instrument of record, pinned in `requirements.txt` where it is software (`CHECK_METHODOLOGY.md` §3) | a computer-algebra library at an exact version; a statistics stack at exact versions with the data release named |
| `{{MUTATION_SET}}` | the alterations the probe applies (`CHECK_METHODOLOGY.md`) | see that file's Slots table |

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

Removing this folder is more than deleting it: the root `README.md` lists
it, `tools/artifacts.toml` carries its `[[artifact]]` and `[[index]]`
rows, and two tool docstrings name this file. Remove the rows and the
pointers in the same round, or the path check reports what is gone.

A project whose checks are all written procedures has no programs. This
folder then holds nothing but its indexes, which stay empty, and the rules
below do not apply; the project may remove the folder at the researcher's
direction, with the reason recorded (`MANIFESTO.md`, *Amending this
manifesto*). A written procedure is a check in every rule
(`CHECK_METHODOLOGY.md`), and nothing in the record requires a program.

## Structure

| Path | Purpose |
|---|---|
| [src/](src/) | the programs: shared foundation modules and `check_NNN_*.py`, flat by default; a project whose code is a package nests it under `src/` and says so here, the configuration's check-program glob following |
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
- **Seeded, and its nondeterminism stated**: fixed seeds wherever sampling
  is used, and, where seeding alone does not settle the result (threaded
  or accelerated numerics, atomic reductions, loader ordering), what
  remains nondeterministic is named and the assertion is made at a
  tolerance that covers it, or the thread count is pinned and recorded.
- **The instrument of record is pinned.** Where the instrument of record
  is software, its exact version is in `requirements.txt`, and where the
  version alone does not fix the result, the rest of the environment that
  does (the interpreter, the accelerator and its driver, the container
  digest, a frozen package manifest) is recorded with it, so that a second
  reader returns to the same thing (`CHECK_METHODOLOGY.md` §3, *the
  version and the pinned environment*).
- **Exact arithmetic where the claim depends on it**; floating point where
  the claim is about a measured, estimated, or otherwise real-valued
  quantity, and then with its tolerance stated and asserted.
- **A check prints its own verdict**, exits nonzero on any failure, and
  ends with one line `RESULT: <verdict>; <name>=<value>; ...` that the
  concordance check compares with the check's record
  (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item 4).
- **No assertion with a constant condition**: a reported assertion whose
  truth does not depend on the computation asserts nothing, and the
  linter reports it.
- **Every mutation is bound.** Each name in a check's `Mutation:` line is
  a member of {{MUTATION_SET}}, bound in the program's `MUTATIONS` to a
  function that takes what `construct()` returns and returns the altered
  object, so the probe can apply it around `construct()` and re-run
  `main()` (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item
  3; `tools/falsifiability_probe.py`). A check builds its object in
  `construct()`, called from `main()`, never at import.
- **Every data file a check reads is listed** in its `BASIS`, as paths
  relative to the repository root, so the run ledger
  (`tools/run_ledger.py`) knows when the check is stale; data read and not
  listed is outside its hash. Data the repository deliberately does not
  hold (a restricted release, a fetched benchmark, an extract too large to
  track) has no path to list: its identity is recorded on the check's
  `Instrument:` line and in the record's construction, by release,
  revision, and fingerprint, and `BASIS` names only what is in the tree,
  or is left empty. The ledger is a local cache and gates nothing, so what
  it cannot hash costs an optimization, not a claim; the record of a run
  is the check record.

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}` | what a check is in this project; this suite ships the program form (`CHECK_METHODOLOGY.md`) | see that file's Slots table |
| `{{VERIFICATION_TOOL}}` | the instrument of record, pinned in `requirements.txt` where it is software (`CHECK_METHODOLOGY.md` §3) | a computer-algebra library at an exact version; a statistics stack at exact versions with the data release named |
| `{{MUTATION_SET}}` | the alterations the probe applies (`CHECK_METHODOLOGY.md`) | see that file's Slots table |

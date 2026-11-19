# Python project

*Created 3 September 2026; updated 19 November 2026.*

The self-contained computational suite: the check programs, any shared
foundation modules they import, and the tests of those modules. Every
check program names the plan it belongs to and the claim it backs, and
[src/README.md](src/README.md) indexes it; the index is checked.

A program that backs no claim and is not a foundation module, such as
one that computes a deliverable's displays, the tables and figures of a
write-up, is indexed there too, in the *Not checks* table. Its file name
does not open with `check_` and a number: a file so named is read by the
tools as a check program and asked for the claim it backs. It names its
plan in a `Plan:` line in the header of its docstring, directly under
the stamp, and freezes with that plan, like everything a plan owns
(`DOCUMENT_GENRES.md` §2). Its row in that table gives the plan and
what the program serves.

The template presumes a Python interpreter for its tools and ships this
suite in Python. A project that writes its checks in another language
keeps the same layout and the same contract (a printed verdict, a nonzero
exit on failure, a `RESULT:` summary line) and records the language in the check form
`CHECK_METHODOLOGY.md` names in its Slots table.

Removing this folder is more than deleting it: the root `README.md` lists
it, `tools/artifacts.toml` carries its `[[artifact]]` and `[[index]]`
rows, `tools/README.md` and `GETTING_STARTED.md` §7 point here for the
pinned environment, and three tool docstrings name this file. Remove the
rows and the pointers in the same round. The path check reports a link
or a backticked path left behind, but not a row of the configuration, a
pointer in plain words, as the three docstrings write theirs, or a file
name written as a pattern; a search for this folder's name finds every
one.

A project whose checks are all written procedures, and which keeps no
other program, has no programs. This folder then holds nothing but its
indexes, which stay empty, and the rules below do not apply; the project
may remove the folder at the researcher's
direction, with the reason recorded (`MANIFESTO.md`, *Amending this
manifesto*). A written procedure is a check in every rule
(`CHECK_METHODOLOGY.md`), and nothing in the record requires a program.

## Structure

| Path | Purpose |
|---|---|
| [src/](src/) | the programs: shared foundation modules, `check_NNN_*.py`, and any other program that backs no claim, flat by default; a project whose code is a package nests it under `src/` and says so here, the configuration's check-program glob following |
| [tests/](tests/) | the test suite for the foundation modules; a check program is not tested here, it is its own test |
| [conftest.py](conftest.py) | puts `src/` on the path; the whole test configuration |
| [requirements.txt](requirements.txt) | the pinned dependencies of the checks |

## Running

A check program runs in the pinned environment, the one
`requirements.txt` fixes (`CHECK_METHODOLOGY.md` §3), never under
whichever interpreter a shell finds first. Build that environment once
per clone, at the repository root, where `.gitignore` keeps it out of
the record, and install again whenever a pin changes; where a pin is
dropped, build it anew, `--clear` added to the first line below, since
an install leaves a dropped package in place:

```bash
python3 -m venv .venv    # with the interpreter the project records in place of python3, where it records one
.venv/bin/python -m pip install -r python_project/requirements.txt
```

Only the main thread builds the environment or installs into it; a
subagent runs checks with it as it stands, since what is installed there
is what every check runs on (`MANIFESTO.md` §14).

Then name its interpreter by path in every command that runs a check or
another of this folder's programs. Each line below is given from the
repository root and is whole in itself, because an assistant's separate
shell commands need not share an activated environment or a working
directory, and a bare `python3` is then whichever interpreter the shell
finds, with whatever packages it happens to hold:

```bash
(cd python_project && ../.venv/bin/python -m pytest tests/ -v)           # the foundation suite
(cd python_project && ../.venv/bin/python src/check_NNN_short_name.py)   # one check
```

Three tools execute check programs, each with the interpreter that runs
the tool, so the command names the same interpreter (`tools/README.md`
lists the three with their options and the oldest Python they run
under):

```bash
.venv/bin/python tools/check_concordance.py      # every check program against its record
.venv/bin/python tools/falsifiability_probe.py   # every check program under each mutation it names
.venv/bin/python tools/run_ledger.py status      # which check programs are stale; run, to run them
```

No tool checks which interpreter ran a check: the run ledger hashes
`requirements.txt` and the interpreter's version, not what is installed,
so a run made outside the pinned environment can read as current.

Where the instrument of record is held in a container, the commands that
run a check are given inside it, at the digest the project records, and
name the interpreter the container holds, by its path there: an
environment built anew inside the container is not what the digest
fixes. Where the checks are written in another language, the command
that runs one check names its pinned toolchain by path in the same way;
the three tools hand every check program to the Python interpreter that
runs them, and as shipped run no such check.

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
  a member of the mutation set (`CHECK_METHODOLOGY.md`, Slots), bound in
  the program's `MUTATIONS` to a function that takes what `construct()`
  returns and returns the altered object, so the probe can apply it around
  `construct()` and re-run `main()` (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item
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

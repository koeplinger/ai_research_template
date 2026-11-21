# Tools

*Created 4 September 2026; updated 21 November 2026.*

Project scaffolding: the programs that keep the record honest. Nothing
here is part of the research. Every tool needs nothing beyond the Python
standard library (3.11 or later) and git; the hook installer is a shell
script. Each carries a `--selftest` that confirms every case it claims,
a planted defect firing or an answer coming out as stated, in a scratch
project it builds; the privacy scan's self-test builds a scratch
repository instead, and the status-block check's holds its cases in
memory. Each reports rather than blocks: a finding names the rulebook
item it implements, where there is one, and the researcher decides
(`MANIFESTO.md`, opening paragraph, and §13). The one exception is the
privacy scan the hooks install, which refuses a commit, since a leak
into the history is hard to undo; the researcher overrides it with
`--no-verify` and says why in the commit message.

The scratch project a self-test builds carries the template's
configuration as it shipped, since the files the self-test plants are
written for it, never the project's own. In the template that is
`artifacts.toml` itself. In a project, a copy of the template's,
made by the setup tool or by hand (`GETTING_STARTED.md` §1), stands
beside the project's own, unchanged, so that what the
project renames, removes, or fills in its configuration leaves the
self-tests as they are; the round check reads the project's own. A
project that takes newer tools from the template copies the newer
template's `tools/artifacts.toml` over that copy as well; one without
the copy makes it the same way, at the path the `shipped-config` row
of the newer template's configuration names, and gives it that row,
above the configuration's own row, which would
otherwise match it first, and a row in the project's tools index,
under that of the configuration.

A finding the researcher has seen and ruled to leave is entered in the
list of accepted findings in `artifacts.toml`, each entry naming the tag,
the file, the first words of the passage, and the log entry of the ruling
(`MANIFESTO.md` §16, *A ruled matter stays ruled*). The linter, the round
check, the residue check, and the session brief's findings gate leave out
every finding of that tag on the line where the passage begins, and count
it; a change to the quoted words, or a re-wrap that moves their start
off that line, brings the finding back, and an entry
that no longer matches, or cannot match, is reported. The probe's and the
concordance check's findings are not accepted through the list. A row's
`skip`, which silences a check for a whole kind of file, is the wider
tool.

| File | Purpose |
|---|---|
| [artifacts.toml](artifacts.toml) | The single source of every path pattern, artifact kind, genre default, and required field the tools read (`ONTOLOGY.md` §7), of the closed vocabularies a project may change (`GLOSSARY.md`, *Renaming a word this methodology uses*), of the publication pipeline's settings, and of the findings accepted at the researcher's ruling. A project that files its artifacts elsewhere edits this one file. |
| [lint_docs.py](lint_docs.py) | The genre and ontology linter: every statically decidable item of `DOCUMENT_GENRES.md` *What the checker verifies*, `editorial_standards.md` *What is checked mechanically*, `ONTOLOGY.md` §5, and items 1, 2, and the static half of 3 (the `Mutation:` line present, its names in the set and bound in `MUTATIONS`) of `CHECK_METHODOLOGY.md` *What is checked mechanically*, each finding tagged with its item; its docstring says what it does not decide. `--list` prints the kind, the default genre, and the derived genre of every file; `--selftest` builds a scratch project under git and plants each defect. |
| [check_round.py](check_round.py) | The round check (`MANIFESTO.md` §13): the linter, the log's numbering, the parts and the `By:` line of every entry not yet committed, and, where the publication pipeline is enabled, the build and the bibliography, in one command. `--scratch DIR` writes the clean scratch project for exercising the hooks. |
| [check_status_reply.py](check_status_reply.py) | The status-block check (`MANIFESTO.md` §16): whether a reply ends in the block's exact form. Harness-free; the wiring that runs it after each reply is the one the reply-hook slot of `MANIFESTO.md` names. |
| [new_project.py](new_project.py) | The setup tool (`GETTING_STARTED.md` §1 to §3): copies the files the template's repository tracks, leaves behind the build's own files and the pointers to them, strips the build lens, converts the shipped prose to the project's spelling variant, fills the slots it is given and the values the tools read, keeps the template's configuration as it shipped for the tools' self-tests, renames any field the project's discipline has taken, adds the project's copyright holder and citation beside the template's, installs the hooks, always writes a project front page, records in a dated working note what it did and what it left, and runs the round check in the new tree. Asks each slot's question of `GETTING_STARTED.md` §3, or reads the answers from a file kept outside both trees; `--template` writes a blank one. `--selftest` instantiates into scratch directories, with full answers and with none, and requires the round check there to be clean. |
| [privacy_scan.py](privacy_scan.py) | The privacy scan, opt-in: a stop-word list at `.privacy/stopwords.txt`, git-ignored, applied to every file, path, and commit message; run beside the round check, never inside it. |
| [query_ontology.py](query_ontology.py) | The ontology queries (`ONTOLOGY.md` §6): what a claim rests on, with weaker members flagged; what is unverified underneath it; what was deferred; the blast radius; the tension ledger as recorded; what is not finished; every site where a claim or a check record cites a claim, with both registers and the cited claim's scope fence quoted. Reports; where only reading decides, it says so. |
| [claim_sites.py](claim_sites.py) | The blast radius of one claim (`ONTOLOGY.md` §6, question 4): every token site, with the finding and tension rows by key, every dependent claim, and the Reserved cluster; beyond the question, the claim's own backing and plan; and, at the end, what a token search cannot see and what is not searched. |
| [check_concordance.py](check_concordance.py) | The concordance check (`CHECK_METHODOLOGY.md` *What is checked mechanically*, item 4): runs every check program and compares its `RESULT:` line's named values with its record's part 4, tag CHECK-4; a written procedure is listed, not compared; the verdict is printed beside the claim's, never a finding. |
| [falsifiability_probe.py](falsifiability_probe.py) | The falsifiability probe (`CHECK_METHODOLOGY.md` *What is checked mechanically*, item 3, the half that executes): every check program re-run under each mutation it or its record names, in a scratch copy of the tree, the mutation wrapped around its `construct()` as the check-program template binds it; a survival, and a program that cannot be probed, are CHECK-3 findings; the matrix is printed, the row of each program that was run ending with its runs and their seconds, and the summary line gives the seconds of the whole probe; a direct run that fails is noted, not judged; a written procedure is listed, its alteration read from its record. |
| [run_ledger.py](run_ledger.py) | The run ledger. No rulebook item: a local, git-ignored cache of check runs keyed by a hash of what each verdict rests on as the tool can see it (the program, the project modules it imports, the pinned dependencies as `requirements.txt` lists them, the interpreter's implementation and version, and the data it lists in `BASIS`; anything else is outside the hash and every status line says so), so `run` recomputes exactly what changed or did not finish; `status` says what is stale; cost is measured, never a gate. |
| [check_residue.py](check_residue.py) | The residue check: what a rebuild leaves in a live draft, listed for the reading that closes the round (`CHECK_METHODOLOGY.md` §7, which states the defect class in plain words): seams, dangling and orphaned references, phantoms, echoes, structure, and a live changelog's ledgers against the draft. The five coined names are this tool's, defined in `GLOSSARY.md`. No rulebook item; candidates for the reader, tags RESIDUE-1 to 7. Reads a typeset source when the pipeline is enabled. |
| [session_brief.py](session_brief.py) | The session brief (`MANIFESTO.md` §16; `ONBOARDING.md`): the reading order, the plans by status with the count engaged, and the standing reminders the record can compute, named in `governance/reminders.md`; printed at session start through the harness wiring and on demand. Advisory: it prints, decides nothing. |
| [install_hooks.sh](install_hooks.sh) | Installs the local git hooks, since hooks are not cloned: on pre-commit the staged privacy scan, refusing, and the round check over the working tree, reporting (refusing under `--strict`); on commit-msg the message scan. Leaves a hook it did not write alone. |

```bash
python3 tools/check_round.py            # before handing work back: every gate, one command
python3 tools/privacy_scan.py           # beside it, where a list exists; --staged, --message FILE
python3 tools/lint_docs.py              # the linter alone; --list, --selftest
python3 tools/check_status_reply.py R   # does the reply in R end in a status block?
python3 tools/query_ontology.py all     # the record's answers; rests-on NNN, unverified NNN, radius NNN, ...
python3 tools/claim_sites.py NNN        # the blast radius of one claim
python3 tools/check_residue.py          # what a rebuild left in the live drafts
python3 tools/session_brief.py          # the reading order, the plans, the reminders; --reminders
tools/install_hooks.sh                  # once per clone; --strict, --force, --uninstall
```

Three tools execute check programs, each with the interpreter that runs
the tool: the concordance check, the falsifiability probe, and the run
ledger are therefore run with the interpreter of the pinned environment,
named by its path (`python_project/README.md`, *Running*), while every
other tool runs under any Python from 3.11 on. The three need 3.11 or
later as well, so a pinned environment built on an older interpreter
cannot run them.

```bash
.venv/bin/python tools/check_concordance.py      # every check program against its record; --only NNN, --timeout S
.venv/bin/python tools/falsifiability_probe.py   # every check program under each mutation it names; --only NNN, --timeout S
.venv/bin/python tools/run_ledger.py status      # what is stale; run [--only NNN] [--force] [--timeout S], show NNN
```

Every tool answers `--selftest`.

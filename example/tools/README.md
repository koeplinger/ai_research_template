# Tools

*Created 4 September 2026; updated 6 September 2026.*

Project scaffolding: the programs that keep the record honest. Nothing
here is part of the research. Every tool needs nothing beyond the Python
standard library (3.11 or later) and git; the hook installer is a shell
script. Each carries a `--selftest` that builds a scratch project and
confirms every case it claims, a planted defect firing or an answer
coming out as stated, and reports rather than blocks: a finding names
the rulebook item it implements, and the researcher decides
(`MANIFESTO.md` §13). The one exception is the privacy scan the hooks
install, which refuses a commit, since a leak into the history is hard
to undo; the researcher overrides it with `--no-verify` and says why in
the commit message.

| File | Purpose |
|---|---|
| [artifacts.toml](artifacts.toml) | The single source of every path pattern, artifact kind, genre default, required field, and closed vocabulary the tools read (`ONTOLOGY.md` §7), and of the publication pipeline's settings. A project that files its artifacts elsewhere edits this one file. |
| [lint_docs.py](lint_docs.py) | The genre and ontology linter: every statically decidable item of `DOCUMENT_GENRES.md` *What the checker verifies*, `editorial_standards.md` *What is checked mechanically*, `ONTOLOGY.md` §5, and items 1, 2, and the static half of 3 (the `Mutation:` line present, its names in the set and bound in `MUTATIONS`) of `CHECK_METHODOLOGY.md` *What is checked mechanically*, each finding tagged with its item; its docstring says what it does not decide. `--list` prints the kind, the default genre, and the derived genre of every file; `--selftest` builds a scratch project under git and plants each defect. |
| [check_round.py](check_round.py) | The round check (`MANIFESTO.md` §13): the linter, the log's numbering and the parts of every entry still open to editing, and, where the publication pipeline is enabled, the build and the bibliography, in one command. `--scratch DIR` writes the clean scratch project for exercising the hooks. |
| [check_status_reply.py](check_status_reply.py) | The status-block check (`MANIFESTO.md` §16): whether a reply ends in the block's exact form. Harness-free; the wiring that runs it after each reply is the harness settings file `.claude/settings.json`, as `governance/harness/claude_code/README.md` describes. |
| [privacy_scan.py](privacy_scan.py) | The privacy scan, opt-in: a stop-word list at `.privacy/stopwords.txt`, git-ignored, applied to every file, path, and commit message; run beside the round check, never inside it. |
| [query_ontology.py](query_ontology.py) | The ontology queries (`ONTOLOGY.md` §6): what a claim rests on, with weaker members flagged; what is unverified underneath it; what was deferred; the blast radius; the tension ledger as recorded; what is not finished; every site where a claim or a check record cites a claim, with both registers and the cited claim's scope fence quoted. Reports; where only reading decides, it says so. |
| [claim_sites.py](claim_sites.py) | The blast radius of one claim (`ONTOLOGY.md` §6, question 4): every token site, with the finding and tension rows by key, every dependent claim, and the Reserved cluster; beyond the question, the claim's own backing and plan; and, at the end, what a token search cannot see and what is not searched. |
| [check_concordance.py](check_concordance.py) | The concordance check (`CHECK_METHODOLOGY.md` *What is checked mechanically*, item 4): runs every check program and compares its `RESULT:` line's named values with its record's part 4, tag CHECK-4; a written procedure is listed, not compared; the verdict is printed beside the claim's, never a finding. |
| [falsifiability_probe.py](falsifiability_probe.py) | The falsifiability probe (`CHECK_METHODOLOGY.md` *What is checked mechanically*, item 3, the half that executes): every check program re-run under each mutation it or its record names, in a scratch copy of the tree, the mutation wrapped around its `construct()` as the template binds it; a survival, and a program the harness cannot probe, are CHECK-3 findings; the matrix is printed; a direct run that fails is noted, not judged; a written procedure is listed, its alteration read from its record. |
| [run_ledger.py](run_ledger.py) | The run ledger. No rulebook item: a local, git-ignored cache of check runs keyed by a hash of what each verdict rests on as the tool can see it (the program, the project modules it imports, the pinned dependencies, the interpreter, and the data it lists in `BASIS`; anything else is outside the hash and every status line says so), so `run` recomputes exactly what changed or did not finish; `status` says what is stale; cost is measured, never a gate. |
| [check_residue.py](check_residue.py) | The residue check: what a rebuild leaves in a live draft, listed for the reading that closes the round (`CHECK_METHODOLOGY.md` §7): seams, dangling and orphaned references, phantoms, echoes, structure, and a live changelog's ledgers against the draft. No rulebook item; candidates for the reader, tags RESIDUE-1 to 7. Reads a typeset source when the pipeline is enabled. |
| [session_brief.py](session_brief.py) | The session brief (`MANIFESTO.md` §16; `ONBOARDING.md`): the reading order, the plans by status with the count engaged, and the standing reminders the record can compute, named in `governance/reminders.md`; printed at session start through the harness wiring and on demand. Advisory: it prints, decides nothing. |
| [install_hooks.sh](install_hooks.sh) | Installs the local git hooks, since hooks are not cloned: on pre-commit the staged privacy scan, refusing, and the round check over the working tree, reporting (refusing under `--strict`); on commit-msg the message scan. Leaves a hook it did not write alone. |

```bash
python3 tools/check_round.py            # before handing work back: every gate, one command
python3 tools/privacy_scan.py           # beside it, where a list exists; --staged, --message FILE
python3 tools/lint_docs.py              # the linter alone; --list, --selftest
python3 tools/check_status_reply.py R   # does the reply in R end in a status block?
python3 tools/query_ontology.py all     # the record's answers; rests-on NNN, unverified NNN, radius NNN, ...
python3 tools/claim_sites.py NNN        # the blast radius of one claim
python3 tools/check_concordance.py      # every check program against its record; --only NNN, --timeout S
python3 tools/falsifiability_probe.py   # every check program under each mutation it names; --only NNN, --timeout S
python3 tools/run_ledger.py status      # what is stale; run [--only NNN] [--force] [--timeout S], show NNN
python3 tools/check_residue.py          # what a rebuild left in the live drafts
python3 tools/session_brief.py          # the reading order, the plans, the reminders; --reminders
tools/install_hooks.sh                  # once per clone; --strict, --force, --uninstall
```

Every tool answers `--selftest`.

# Tools

*Created 4 September 2026; updated 5 September 2026.*

Project scaffolding: the programs that keep the record honest. Nothing
here is part of the research. Every tool needs nothing beyond the Python
standard library (3.11 or later) and git; the hook installer is a shell
script. Each carries a `--selftest` that plants each defect it looks for
and confirms it fires, and reports rather than blocks: a finding names
the rulebook item it implements, and the researcher decides
(`MANIFESTO.md` §13). The one exception is the privacy scan the hooks
install, which refuses a commit, since a leak into the history is hard
to undo; the researcher overrides it with `--no-verify` and says why in
the commit message.

| File | Purpose |
|---|---|
| [artifacts.toml](artifacts.toml) | The single source of every path pattern, artifact kind, genre default, required field, and closed vocabulary the tools read (`ONTOLOGY.md` §7), and of the publication pipeline's settings. A project that files its artifacts elsewhere edits this one file. |
| [lint_docs.py](lint_docs.py) | The genre and ontology linter: every statically decidable item of `DOCUMENT_GENRES.md` *What the checker verifies*, `editorial_standards.md` *What is checked mechanically*, `ONTOLOGY.md` §5, and items 1 to 3 of `CHECK_METHODOLOGY.md` *What is checked mechanically*, each finding tagged with its item; its docstring says what it does not decide. `--list` prints the kind, the default genre, and the derived genre of every file; `--selftest` builds a scratch project under git and plants each defect. |
| [check_round.py](check_round.py) | The round check (`MANIFESTO.md` §13): the linter, the log's numbering and the parts of every entry still open to editing, and, where the publication pipeline is enabled, the build and the bibliography, in one command. `--scratch DIR` writes the clean scratch project for exercising the hooks. |
| [check_status_reply.py](check_status_reply.py) | The status-block check (`MANIFESTO.md` §16): whether a reply ends in the block's exact form. Harness-free; the wiring that runs it after each reply is `{{REPLY_HOOK}}`. |
| [privacy_scan.py](privacy_scan.py) | The privacy scan, opt-in: a stop-word list at `.privacy/stopwords.txt`, git-ignored, applied to every file, path, and commit message; run beside the round check, never inside it. |
| [install_hooks.sh](install_hooks.sh) | Installs the local git hooks, since hooks are not cloned: on pre-commit the staged privacy scan, refusing, and the round check over the working tree, reporting (refusing under `--strict`); on commit-msg the message scan. Leaves a hook it did not write alone. |

```bash
python3 tools/check_round.py            # before handing work back: every gate, one command
python3 tools/privacy_scan.py           # beside it, where a list exists; --staged, --message FILE
python3 tools/lint_docs.py              # the linter alone; --list, --selftest
python3 tools/check_status_reply.py R   # does the reply in R end in a status block?
tools/install_hooks.sh                  # once per clone; --strict, --force, --uninstall
```

Every tool answers `--selftest`.

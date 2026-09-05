# Tools

*Created 4 September 2026; updated 4 September 2026.*

Project scaffolding: the programs that keep the record honest. Nothing
here is part of the research. Every tool needs nothing beyond the Python
standard library (3.11 or later), carries a `--selftest` that plants
each defect it looks for and confirms it fires, and reports rather than
blocks: a finding names the rulebook item it implements, and the
researcher decides (`MANIFESTO.md` §13).

| File | Purpose |
|---|---|
| [artifacts.toml](artifacts.toml) | The single source of every path pattern, artifact kind, genre default, required field, and closed vocabulary the tools read (`ONTOLOGY.md` §7). A project that files its artifacts elsewhere edits this one file. |
| [lint_docs.py](lint_docs.py) | The genre and ontology linter: every statically decidable item of `DOCUMENT_GENRES.md` *What the checker verifies*, `editorial_standards.md` *What is checked mechanically*, `ONTOLOGY.md` §5, and items 1 to 3 of `CHECK_METHODOLOGY.md` *What is checked mechanically*, each finding tagged with its item; its docstring says what it does not decide. `--list` prints the kind, the default genre, and the derived genre of every file; `--selftest` builds a scratch project under git and plants each defect. |

```bash
python3 tools/lint_docs.py             # check; exit 1 on any finding
python3 tools/lint_docs.py --list      # kind, default genre, derived genre of every file
python3 tools/lint_docs.py --selftest  # every check shown to fire
```

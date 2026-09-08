# Governance: the mechanisms, each with the rule it serves and the moment it fires

*Created 5 September 2026; updated 5 September 2026.*

`VISION.md` promises four kinds of mechanism that keep the discipline
running when attention lapses: reminders, checks, opposition, and
support. All are advisory by design, with the one exception the privacy
scan row states: they fire, they inform, and they leave the decision
with the researcher. This folder holds the ones that
are not tools (the standing reminders, the opposition roles, the harness
wirings) and this file maps every mechanism, tool or not, to the rule it
serves and the moment it fires.

| File | What it holds |
|---|---|
| [reminders.md](reminders.md) | the standing instructions, each named, with its trigger, its output, what computes it, and what it does not decide; the plan-closure checklist |
| [roles/](roles/) | the opposition roles with their standard prompts: the refuter, the blind referee, the structure census, the deletion ledger, the coverage auditor, the probe as opposition |
| [harness/](harness/) | one folder per harness with the wiring that runs the tools after each reply and at session start |

## Reminders

| Mechanism | Rule | Fires | Output | Does not decide |
|---|---|---|---|---|
| the session brief, `tools/session_brief.py` | `MANIFESTO.md` §16; `ONBOARDING.md` | at session start, through the harness wiring, and on demand | the reading order, the plans by status, the reminders the record can compute | anything: it prints |
| the documentation consistency sweep, [roles/documentation_sweep.md](roles/documentation_sweep.md) | `CHECK_METHODOLOGY.md` §7, which sweeps the record; this sweeps the documentation | after a batch of edits to the rulebooks, indexes, templates, or configuration; first of all after instantiation | the disagreements between documents, each with its two homes | which of two disagreeing statements yields: the researcher's |
| the standing reminders, [reminders.md](reminders.md) | §16, and the section each names | at the stage of work each names | one sentence in the reply, once | the action: taken only with direction |

## Checks

| Mechanism | Rule | Fires | Output | Does not decide |
|---|---|---|---|---|
| the linter, `tools/lint_docs.py` | `DOCUMENT_GENRES.md`, `editorial_standards.md`, `ONTOLOGY.md` §5, `CHECK_METHODOLOGY.md` items 1 to 3 (static) | inside the round check, and alone | findings tagged with their item | what its docstring lists as reading |
| the round check, `tools/check_round.py` | `MANIFESTO.md` §13 | before work is handed back; on pre-commit where the hooks are installed | the linter's findings and the round's own | the researcher's commit: it reports, and the hook lets the commit proceed unless installed strict |
| the concordance check, `tools/check_concordance.py` | `CHECK_METHODOLOGY.md` item 4 | when a check program has been run | every named value that disagrees with its record | the verdict word: printed beside the claim's, never a finding |
| the falsifiability probe, `tools/falsifiability_probe.py` | `CHECK_METHODOLOGY.md` item 3 (executing) and §5 | before a check is relied on; before a plan closes | the matrix, and a survival as a finding | whether the mutation set is adequate |
| the status-block check, `tools/check_status_reply.py` | `MANIFESTO.md` §16 | after each reply, through the harness wiring | the reasons a block does not conform | the truth of any line |
| the privacy scan, `tools/privacy_scan.py` | none in the donor text; `MANIFESTO.md` §6 on what must not enter; opt-in | beside the round check where a stop-word list exists, and on every commit where the hooks are installed | every place a stop word appears | what belongs on the list: the researcher's. The one mechanism that refuses (a commit, on a finding), overridden with `--no-verify` and the reason in the commit message (`MANIFESTO.md` §12) |
| the run ledger, `tools/run_ledger.py` | none; `CHECK_METHODOLOGY.md` §8 on cost | when a check *program*'s basis may have changed; a project whose checks are all written procedures never uses it | what is stale, and the cost of each run | anything: a cache |
| the residue check, `tools/check_residue.py` | none; `CHECK_METHODOLOGY.md` §7 on a rebuild | after a rebuild or a correction batch to a live draft | candidates for the reading that closes the round | any of them: candidates |
| the ontology queries, `tools/query_ontology.py`, and `tools/claim_sites.py` | `ONTOLOGY.md` §6 | when a question of §6 is asked; before a claim is revisited | the answer from the fields, flagged where §4 decides | what it says is reading |

## Opposition

| Mechanism | Rule | Fires | Output | Does not decide |
|---|---|---|---|---|
| the refuter, [roles/refuter.md](roles/refuter.md) | `MANIFESTO.md` §17; `CHECK_METHODOLOGY.md` §7 | on every sweep or review finding, before it is acted on | stands, refuted with the reason, or narrowed | the fix |
| the blind referee, [roles/blind_referee.md](roles/blind_referee.md) | `MANIFESTO.md` §17; `paper/README.md` | before a version freezes | a review record under `paper/reviews/` | the release: the researcher's |
| the structure census, [roles/structure_census.md](roles/structure_census.md) | `CHECK_METHODOLOGY.md` §7, the structure lens | at the head of every review, and before a review patches a sentence into a section it has not audited | the census table | whether to rebuild |
| the deletion ledger, [roles/deletion_ledger.md](roles/deletion_ledger.md) | `CHECK_METHODOLOGY.md` §7, what a rebuild owes | on every rebuild of a section | the ledgers in the version changelog | a content cut: the researcher's |
| the coverage auditor, [roles/coverage_auditor.md](roles/coverage_auditor.md) | `CHECK_METHODOLOGY.md` §5 and item 2 | before a check backs a claim registered `VERIFIED` or `RULED_OUT` | every atomic assertion classified, each gap refuted by a second reader | the register: the researcher's |
| the probe as opposition, [roles/falsifiability_probe.md](roles/falsifiability_probe.md) | `CHECK_METHODOLOGY.md` §5 | when a check is written, and before it is relied on | the matrix, and the check's named mutations judged against what the claim depends on | the project's mutation set: a missing mutation is proposed, and the set is amended at the researcher's direction |

## Support

| Mechanism | Rule | Fires | Output | Does not decide |
|---|---|---|---|---|
| the templates, one per artifact kind, with their guidance in comments | `ONTOLOGY.md` §8: every predicate names the template that ships its field | when an artifact is started | a form whose mandatory fields are pre-printed | the values |
| the folder indexes, every `README.md` | `DOCUMENT_GENRES.md` item 8 | when a file is added | the map of the folder, checked | what a file is for |
| the configuration, `tools/artifacts.toml` | `ONTOLOGY.md` §7 | when a project files its artifacts elsewhere | one edit that every tool follows | the filing convention |
| the hook installer, `tools/install_hooks.sh` | `MANIFESTO.md` §13 and §6 | once per clone | the git hooks | whether to install strict |
| the harness wirings, [harness/](harness/) | `MANIFESTO.md` §16, `{{REPLY_HOOK}}` | after each reply; at session start | the tools run at those moments | which harness: the researcher's |
| the guide: [GETTING_STARTED.md](../GETTING_STARTED.md), [HOW_IT_FITS_TOGETHER.md](../HOW_IT_FITS_TOGETHER.md), [FORKING.md](../FORKING.md) | `VISION.md`, *Expectation*: clear guidance on how to begin, and as the project proceeds | when a project is instantiated; at each stage, by the list of prompts the second names | the walkthrough, the system with the round as its unit of time, the prompts to make and when, and how to change a mechanism legibly | any of it: the repository is the researcher's (`FORKING.md`) |
| the worked example, [example/](../example/) | `VISION.md`, *Support*: the researcher's first model of a round | when the researcher starts, and whenever a form is in doubt | a complete small project, every gate passing, fenced as its README says | anything of the researcher's own: it is a model, never ground truth |

## Removing a mechanism

Every mechanism here can be modified, replaced, or deleted
(`VISION.md`, *The repository is the researcher's*). A removal is
deliberate and legible: the row above is struck with the reason, the
rule it served is amended or its enforcement declared by hand, and the
prompt log records the round.

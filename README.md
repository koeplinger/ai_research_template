# A research template for AI-assisted work

*Created 2 September 2026; updated 8 September 2026.*

A repository structure, a shared vocabulary, and a set of advisory checks
for research done with an AI assistant. It is a *template*: you clone it,
fill in what your field decides, and the result is your project.

The bet it makes, stated precisely: **it cannot make results correct.** It
makes provenance recoverable, claims explicit, verification status
visible, disagreement recorded, and revisions traceable. Robustness
follows from a researcher working honestly inside that structure, not from
the structure alone.

**What it cannot do.** It presumes honesty on the researcher's side: it
cannot detect self-deception or motivated reasoning, and does not try. It
is not a compliance system, not a substitute for peer review, not a
guarantee of correctness, and not a way to make an assistant trustworthy;
every mechanism informs and records, and none blocks. `VISION.md` states
the precondition and the non-goals in full, and they are worth reading
before adopting it.

It assumes no particular field. Its worked examples are drawn from
archival history, empirical economics, molecular biology, law, machine
learning, and mathematics, and where a decision belongs to a discipline it
is a **slot** you fill rather than a rule you obey.

## Start here

| If you want to | Read |
|---|---|
| get a project running | [GETTING_STARTED.md](GETTING_STARTED.md): clone to first commit, in one sitting |
| know why the parts are shaped this way | [HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md): the system, the round, and **the prompts this methodology suggests** |
| change or remove a mechanism | [FORKING.md](FORKING.md): the repository is yours, and how to change it legibly |
| see it working | [example/](example/): a small complete project, every gate passing |
| know what a word means here | [GLOSSARY.md](GLOSSARY.md): each word, and what it will be mistaken for |
| know what it is all for | [VISION.md](VISION.md): the durable statement of intent |

## What it provides

Three things meant to be one system, described in
[HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md).

- **Artifacts.** Where sources, derived material, claims, checks, plans,
  notes, the log, and the write-ups live, each with a template, an index,
  and a rule for how it may change. The organizing commitment is that the
  repository is the primary artifact and the paper is a projection of it.
- **An ontology.** The vocabulary the artifacts share, implemented rather
  than described: most predicates appear in a template as a header field,
  are checked mechanically, and can be queried across the repository, and
  the rest are carried in prose and are the sweep's business. That is what
  makes *what is this conclusion standing on* a question you answer by
  looking.
- **Governance.** Reminders, checks, opposition, and support, keeping the
  discipline running when attention lapses. All advisory: they fire, they
  inform, and they leave the decision with the researcher. The one
  exception says so.

## The files at the root

| File | What it is |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) | The walkthrough: clone, slots, first round, first plan, first check, first commit |
| [HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md) | The system as one thing, the round as the unit of time, and the prompts to make |
| [FORKING.md](FORKING.md) | How to change or remove a mechanism deliberately and legibly |
| [MANIFESTO.md](MANIFESTO.md) | The methodology: what the record is, who does what, and the round |
| [DOCUMENT_GENRES.md](DOCUMENT_GENRES.md) | The three genres of artifact and what the checker verifies |
| [CHECK_METHODOLOGY.md](CHECK_METHODOLOGY.md) | Registers, claim kinds, and the shape of a check |
| [PRECEDENCE.md](PRECEDENCE.md) | Which artifact wins when two disagree |
| [ONTOLOGY.md](ONTOLOGY.md) | The predicates the tools read and the surface syntax that carries them |
| [GLOSSARY.md](GLOSSARY.md) | The method's own words, what each will be mistaken for, and how to rename one |
| [ONBOARDING.md](ONBOARDING.md) | What every assistant session reads before it works |
| [CURRENT_STATE.md](CURRENT_STATE.md) | Where the project stands, corrected in place |
| [FINDINGS.md](FINDINGS.md) | The findings, one row each, by pointer to their claims |
| [LICENSE.md](LICENSE.md), [LICENSE-CODE](LICENSE-CODE) | The licenses, documents and code |
| [tools/](tools/), [governance/](governance/), [evidence_and_reasoning/](evidence_and_reasoning/), [paper/](paper/), [prompt_logs/](prompt_logs/), [python_project/](python_project/), [inherited/](inherited/), [source_documents/](source_documents/) | The folders, each with its own README |
| [example/](example/) | A worked example: a small project instantiated from this template, with its own README, log, and fence |

## Requirements

Git, for the version history the methodology treats as part of the record,
and Python 3.11 or later for the tools, which use the standard library
alone. Both are infrastructure rather than slots. The shipped check
programs are Python; a project whose checks are written procedures, or are
programs in another language, keeps the same contract and says so.

## Lineage

The methodology descends from the author's first attempt,
[`leech_alg`](https://github.com/koeplinger/leech_alg)
(also on [Bitbucket](https://bitbucket.org/jenskoeplinger/leech_alg)), and
was substantially reworked in a later, private project. That project is not
named here, and nothing specific to it, or to any other project of the
author's, appears in this repository.

## Licensing

Code is under the MIT License ([LICENSE-CODE](LICENSE-CODE)); all written
material is under Creative Commons Attribution 4.0 International
([LICENSE.md](LICENSE.md)). Code is permissive so it can be lifted without
friction; documents carry attribution so the methodology stays traceable to
where it came from. There is no warranty and no promise of fitness for any
purpose.

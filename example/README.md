# Market days in a synthetic market roll

*Created 2 September 2026; updated 21 November 2026.*

This project asks whether the market roll of a fictional town supports
what a fictional note states of the market days of 1851: their count, and
the days of the week they fell on. Both are synthetic files made for the
project, so nothing here is a claim about the world. A count of the
roll's rows for 1851, by a check that would fail were it otherwise, set
against the note's figure as collated against the note, answers the
first; the weekday of each row of 1851, set against what the note says of
them, answers the second. The long form is
[evidence_and_reasoning/research_statement.md](evidence_and_reasoning/research_statement.md).

## About this example

This project is a worked example of the methodology template: an
illustration to browse, not a project to run or to start from. What it
offers is its prompt log, the working files its rounds left behind, and
the write-up they led to. To start a project of your own, use the setup
tool in the `tools/` folder of the template's repository, rather than a
copy of this folder.

- **One session played both parties.** A single assistant session wrote
  every prompt in the researcher's role and carried out each round, so
  every ruling in its rounds is that session's, not a person's. The second
  passes, audits, refutations, and blind review the log records were made
  by subagents, further sessions it started.
- **It was committed once.** Its rounds ran on 20 and 21 November 2026,
  and nothing was committed until the example was complete. An entry that
  speaks of something as not yet committed was accurate when written.
- **The AI model is withheld.** Every `By:` line says so, where a project
  of your own names the model.
- **It was made from the template at commit `73ca267`.** Its rulebooks
  and tools began as copies from that commit. Setup and the rounds logged
  here changed some of them, and the template may have moved on since.
- **Its tools are not kept working here.** They ran while the project
  stood in a repository of its own, and the commands on this page may not
  run from this subfolder of the template's repository.

The first three are the departures from the rules that
`prompt_logs/001_setup.md`, *Corrections and departures*, records.

Three ways to read it:

- **As it happened.** [prompt_logs/](prompt_logs/) holds every round in
  order: what was asked, what was done, and what was left for the
  researcher to decide.
- **From a result back to its evidence.** Take a line of
  [FINDINGS.md](FINDINGS.md) to its claim, the claim to its check, and
  the check to the log entry that records it. A token such as
  `[claim 001]` or `[check 001]` names the file with that number under
  [evidence_and_reasoning/claims/](evidence_and_reasoning/claims/) or
  [evidence_and_reasoning/checks/](evidence_and_reasoning/checks/).
- **For the end product.** The write-up is
  [paper/2026-11-20_market_days_1851.md](paper/2026-11-20_market_days_1851.md),
  and its review, with what the review changed, is in
  [paper/reviews/](paper/reviews/).

## Where to start

| To see | Read |
|---|---|
| where the project stands | [CURRENT_STATE.md](CURRENT_STATE.md) |
| what the record has established | [FINDINGS.md](FINDINGS.md) |
| the question and the thesis | [evidence_and_reasoning/research_statement.md](evidence_and_reasoning/research_statement.md), [problem_statement.md](evidence_and_reasoning/problem_statement.md) |
| the project's own terms, in its glossary | [evidence_and_reasoning/terminology.md](evidence_and_reasoning/terminology.md) |
| what is open | [CURRENT_STATE.md](CURRENT_STATE.md), *What is open* |
| every plan, what it settles, and its status | [evidence_and_reasoning/research_plans/ROADMAP.md](evidence_and_reasoning/research_plans/ROADMAP.md) |
| the record itself | [evidence_and_reasoning/](evidence_and_reasoning/) |
| what was asked, and when | [prompt_logs/](prompt_logs/) |

## How this project works

It is built from a methodology template, whose rules travel with it:
[MANIFESTO.md](MANIFESTO.md) for who does what and what the record is,
[HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md) for the system as one
thing and the prompts worth making, [GLOSSARY.md](GLOSSARY.md) for the
words it uses in its own sense, [GETTING_STARTED.md](GETTING_STARTED.md)
for how this project was set up. A session reads
[ONBOARDING.md](ONBOARDING.md) before it works. This project's written
material is adapted from that template under CC BY 4.0, which
[LICENSE.md](LICENSE.md) names.

Before handing work back, and on every commit:

```bash
python3 tools/check_round.py
```

## The files at the root

| File | What it is |
|---|---|
| [CHECK_METHODOLOGY.md](CHECK_METHODOLOGY.md) | trust levels, claim kinds, and the shape of a check |
| [CURRENT_STATE.md](CURRENT_STATE.md) | where the project stands |
| [DOCUMENT_GENRES.md](DOCUMENT_GENRES.md) | the three genres of artifact and what the checker verifies |
| [FINDINGS.md](FINDINGS.md) | what the record has established |
| [FORKING.md](FORKING.md) | how to change or remove a mechanism, legibly |
| [GETTING_STARTED.md](GETTING_STARTED.md) | how this project was set up, and which rounds come first |
| [GLOSSARY.md](GLOSSARY.md) | the method's own words, and what each will be mistaken for |
| [HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md) | the system as one thing, and the prompts worth making |
| [LICENSE-CODE](LICENSE-CODE) | the license for code |
| [LICENSE.md](LICENSE.md) | the license for written material, and the citations |
| [MANIFESTO.md](MANIFESTO.md) | the operating rules: who does what, and what the record is |
| [ONBOARDING.md](ONBOARDING.md) | what every session reads before it works |
| [ONTOLOGY.md](ONTOLOGY.md) | the predicates the tools read, and their surface syntax |
| [PRECEDENCE.md](PRECEDENCE.md) | which statement governs when two disagree |
| [VISION.md](VISION.md) | the template's statement of intent, which the rulebooks cite |
| [evidence_and_reasoning/](evidence_and_reasoning/), [governance/](governance/), [inherited/](inherited/), [paper/](paper/), [prompt_logs/](prompt_logs/), [python_project/](python_project/), [source_documents/](source_documents/), [tools/](tools/) | the folders, each with its own README |

## Licensing

Written material is under Creative Commons Attribution 4.0 International
and code under the MIT License, except the held sources under
`source_documents/`, the imports under `inherited/`, the attachments under
`prompt_logs/attachments/`, and what the project quotes or derives from
them, which keep their own terms as far as those terms reach.
[LICENSE.md](LICENSE.md) and [LICENSE-CODE](LICENSE-CODE) carry both
licenses and the citation of the template this project is adapted from.

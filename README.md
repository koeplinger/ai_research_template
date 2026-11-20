# A research template for AI-assisted work

*Created 2 September 2026; updated 19 November 2026.*

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
every mechanism informs and records, and none blocks but the opt-in
privacy scan, which refuses a commit on a stop word, and every commit
while its list holds no pattern. `VISION.md` states
the precondition and the non-goals in full, and they are worth reading
before adopting it.

It assumes no particular field. Its worked examples are drawn from
archival history, empirical economics, molecular biology, law, machine
learning, and mathematics, and where a decision belongs to a discipline it
is a **slot** you fill rather than a rule you obey.

## One harness ships, and it is Anthropic's

**Today this template is armed for one AI assistant: Anthropic's Claude,
in its command-line harness.** Nothing in the methodology depends on that,
and no rule names a vendor; but the *wiring* does, and the wiring is
installed from the moment you instantiate a project, and running once the
harness trusts the project's folder.

Concretely, what ships and is armed: a settings file at the repository
root that the harness reads, a hook that checks the form of a reply
after it is written, and a command that prints the reading order at the
start of each session. `governance/harness/claude_code/` holds the
adapter; `governance/harness/README.md` holds the table of wirings and the
list of what a second one costs.

**If you work with a different assistant or harness**, everything except
that wiring still applies: the record, the checks, the registers, the
plans, the roles and the tools are all harness-free, and they run on their
own. What you do is fill the reply-hook slot with your own wiring or with
*none, with the form kept by hand*, and add or remove a folder under
`governance/harness/` by the recipe there. Be aware that the template's
setup tool records your answer to its reply-hook question but copies the
shipped wiring whatever the answer, so a project on another assistant
removes it afterwards rather than declining it up front.

**Vendor independence is intended, and is scheduled rather than promised.**
[TODO.md](TODO.md) holds that work and what each part of it touches, with
support for further assistants added one at a time, at the deliberate
pace it sets out.

## Start here

| If you want to | Read |
|---|---|
| get a project running | [GETTING_STARTED.md](GETTING_STARTED.md): clone to first commit, in one sitting; or ask the assistant, in your clone, to make the project, and it puts each setup question to you in plain words, one at a time, then runs the setup tool once |
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
  than described: most predicates are written in a form the tools read (a
  header field, a stamp, a citation token, or a file at a governed path),
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
| [GETTING_STARTED.md](GETTING_STARTED.md) | The walkthrough: clone, slots, the first rounds, first plan, first check, and the round check before each commit |
| [HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md) | The system as one thing, the round as the unit of time, and the prompts to make |
| [FORKING.md](FORKING.md) | How to change or remove a mechanism deliberately and legibly |
| [TODO.md](TODO.md) | What this template does not have yet, and what each item would touch |
| [VISION.md](VISION.md) | The durable statement of intent, which the rulebooks cite |
| [MANIFESTO.md](MANIFESTO.md) | The methodology: what the record is, who does what, and the round |
| [DOCUMENT_GENRES.md](DOCUMENT_GENRES.md) | The three genres of artifact and what the checker verifies |
| [CHECK_METHODOLOGY.md](CHECK_METHODOLOGY.md) | Registers, claim kinds, and the shape of a check |
| [PRECEDENCE.md](PRECEDENCE.md) | Which statement governs when two disagree |
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

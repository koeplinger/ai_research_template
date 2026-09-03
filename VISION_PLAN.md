# VISION_PLAN: building the template

*Created 2 September 2026; updated 2 September 2026.*

This document is **ephemeral**. It describes how this repository gets from
its present state to the state [VISION.md](VISION.md) describes, and it
records how far along that is. "Complete" means: every step below is DONE,
or DEFERRED or DROPPED with a reason recorded on the step; the close-out
sweep passes; and this file is deleted. Nothing in it is part of the
template a researcher will clone.

VISION.md is the authority. Where this plan and the vision disagree, the
vision wins and this plan is corrected.

---

## Ground rules for this build

1. **No prompt log.** The methodology this template packages requires a
   research project to keep an immutable, numbered log of every prompt. That
   rule applies to research projects built *from* the template. It does not
   apply to the construction of the template itself: **no prompts that go
   into building this repository are logged**, and nothing here is to be read
   as a research record.

2. **This repository is public, and nothing project-specific enters it.**
   The methodology is lifted from the author's own prior projects. Those
   projects, their subjects, their sources, their collaborators, and the file
   system they live on are private. Tracked files here carry none of that: no
   local file or folder names, no project names, no research topics, no names
   of third parties, no source identifiers, no logs. Every artifact is written
   generically. **The one permitted lineage reference** is the author's first
   attempt, `leech_alg`, public at
   https://github.com/koeplinger/leech_alg and
   https://bitbucket.org/jenskoeplinger/leech_alg. What is built here is a
   substantially reworked descendant of a later, private project, which is
   not named.

3. **Privacy is enforced mechanically, locally.** A git-ignored directory
   `.privacy/` holds a stop-word list and a scanner. The scanner runs over the
   whole working tree on demand, and two local git hooks (`pre-commit`,
   `commit-msg`) run it over staged contents, staged file names, and the
   commit message, refusing any commit that matches. The list and the scanner
   never enter version control; the `.gitignore` entry is the only trace of
   them here. The scanner has a self-test that proves every pattern fires and
   that ordinary words do not. **Every step below ends with a clean whole-tree
   scan.** A fresh clone has neither the list nor the hooks; they are
   reinstalled by hand before any commit from that clone.

4. **The human does every commit.** Adopted from the outset, as the manifesto
   will require of every project built from the template.

5. **Steps run top-down.** Each step has exactly one status, recorded once,
   in the tracker below. One step is normally open; two or more may be, and
   then the tracker shows it.

## Working method for a step

Draft the deliverables; review them against VISION.md section by section;
run the privacy scan; run the linter and the round gate once they exist
(step 9); hand to the researcher; mark DONE only on his word. A step's
"done when" is its closure criterion, written before the work starts.

Slots a project fills are written `{{LIKE_THIS}}` in the text and listed in
a Slots table at the end of the document, each with its meaning and examples
from at least two disciplines. The instantiation procedure of step 14
substitutes them.

Writing rule for every artifact: generic in every sentence. No proper noun
other than `leech_alg`. No domain noun from the source projects. Where an
example is needed, draw it from at least two disciplines, and prefer
disciplines other than mathematics and physics.

---

## Status vocabulary

| Status | Meaning |
|---|---|
| NOT STARTED | not begun |
| OPEN | in progress |
| READY | deliverables complete and scan clean; awaiting the researcher's acceptance |
| DONE | deliverables exist, the done-when criterion is met, whole-tree scan clean, researcher accepted |
| DEFERRED | postponed past close-out, reason recorded on the step |
| DROPPED | will not be done, reason recorded on the step |

## Tracker

The single source of status for this build. Steps are executed top-down.

| # | Step | Status | Date |
|---|---|---|---|
| 0 | Foundation of this build | DONE | 2026-09-02 |
| 1 | Licensing and repository hygiene | DONE | 2026-09-02 |
| 2 | Manifesto: operating rules for AI assistance | DONE | 2026-09-02 |
| 3 | Document genres and the state model | DONE | 2026-09-02 |
| 4 | Editorial standards | DONE | 2026-09-02 |
| 5 | Verification methodology | READY | 2026-09-03 |
| 6 | Precedence and the tension ledger | READY | 2026-09-03 |
| 7 | The Ontology | NOT STARTED | |
| 8a | Artifacts: the record core | NOT STARTED | |
| 8b | Artifacts: claims and checks | NOT STARTED | |
| 8c | Artifacts: references and sources | NOT STARTED | |
| 8d | Artifacts: plans, roadmap, notes | NOT STARTED | |
| 8e | Artifacts: prompt log and session onboarding | NOT STARTED | |
| 8f | Artifacts: publication, reviews, imports | NOT STARTED | |
| 9 | Mechanical enforcement: the tools | NOT STARTED | |
| 10 | Governance wiring: hooks, reminders, opposition, support | NOT STARTED | |
| 11 | Worked example project | NOT STARTED | |
| 12 | Breadth review beyond mathematics and physics | NOT STARTED | |
| 13 | The guide | NOT STARTED | |
| 14 | Instantiation procedure | NOT STARTED | |
| 15 | Close-out | NOT STARTED | |

## Open decisions for the researcher

Recorded here so no step silently assumes them.

- **Worked example domain (step 11).** Must be outside mathematics and
  physics, small enough to complete, and free of anything private. Candidates:
  a replication of a published descriptive statistic from an open dataset; a
  close reading of a public-domain historical document against a secondary
  claim about it; a reproduction of a small, published computational result
  from open code.
- **Harness settings tracked or not (step 10).** The source lineage keeps the
  harness settings file out of version control, which means a clone loses the
  hooks that enforce the manifesto. Proposed: track the shared settings file,
  ignore only the local one.
- **The deliverable (resolved in steps 3 and 4).** VISION's third
  discipline choice, "what a publishable deliverable is", is the slot
  `{{DELIVERABLE}}`: its form, its title convention, and what is released
  with a version of it. `paper/` stays the folder name whatever the form.
- **Harness neutrality (steps 10, 13).** The manifesto names no assistant
  vendor: §16's wiring is the slot `{{REPLY_HOOK}}`. Step 10 ships concrete
  wirings under a per-harness directory, the first for the harness the
  template is built with; a project on another harness fills the slot
  differently or keeps the form by hand. `.gitignore` currently names that
  first harness's local-settings path; step 10 revisits it.
- **Privacy scanner as a template feature (step 9).** Proposed: yes, as a
  generic opt-in tool reading a git-ignored list, with an installer for the
  hooks; many projects must keep collaborator names, embargoed topics, or
  unreleased data out of a public repository.
- **Language of check programs (steps 5, 8b, 9).** Python assumed, no
  dependencies for the tools, a small optional set for the checks. Other
  languages become a documented slot.
- **Publication pipeline (steps 8f, 9).** LaTeX assumed as the default with
  its build and residue gates; the pipeline is a slot, and a project that
  publishes otherwise disables those gates and says so.

---

## Steps

### Step 0: Foundation of this build

**Goal.** The north star, this plan, the public-facing notice that the
repository is under construction, and the privacy floor under everything
that follows.

**Deliverables.** `VISION.md`; this file; `README.md` whose first section
points at both and states that this is a template under construction, not a
research project, with no prompt log kept for the build; `.gitignore`
carrying the `.privacy/` exclusion; the local `.privacy/` scanner and
stop-word list; local `pre-commit` and `commit-msg` hooks.

**Done when.** All exist; the scanner's self-test passes; the whole-tree
scan is clean.


### Step 1: Licensing and repository hygiene

**Goal.** The legal floor, stated once, plainly.

**Deliverables.** `LICENSE.md`: Creative Commons Attribution 4.0 for all
written material (documentation, evidence, papers, figures, prompt logs),
with a recommended-citation block as a fill-in slot and a section for
inherited material. `LICENSE-CODE`: MIT for all source code. A finalized
`.gitignore`. A one-paragraph statement in `README.md` of what is licensed
how and why the split.

**Done when.** Both license files in place; README names them; scan clean.

### Step 2: Manifesto: operating rules for AI assistance

**Goal.** The binding rules for an AI assistant working inside a research
project, generic across disciplines, every discipline-specific choice a
marked slot.

**Deliverables.** `MANIFESTO.md`, seventeen sections, generalized from the
source lineage (`leech_alg` carried fourteen; the rest were added in later
projects and here). The file carries **two lenses**: the donor text, which
a project copies as its own manifesto, and marked `> **Build lens.**`
blocks stating where the rules differ while this template itself is built
(most prominently §8: a project logs every prompt; the build logs none). A
closing table summarizes the divergences; the instantiation procedure of
step 14 strips every build-lens block. The preamble states that the rules
are binding on the assistant and advisory toward the researcher, defines
the words used throughout (researcher, assistant, main thread, subagent,
harness, round, artifact, the three genres), and lists every file the
manifesto points to. The sections:

1. Role and identity: a thorough {{PERSONA}} of high integrity; a tool in
   service of the researcher, never the author, never the holder of the
   opinion; assists with reasoning, reading, computation, search,
   documentation, and argument against a position.
2. Attribution and originality: every non-trivial claim referenced or
   pointed at the check that established it; original claims marked as
   such; datasets and archival sources among the acceptable kinds; the
   researcher decides adequacy and records it.
3. Plagiarism, attribution, and standing: known disputes about a
   reference's standing searched for and recorded; finding nothing is not
   a verification.
4. Uncertainty protocol: say so and stop; never fabricate; label
   speculation.
5. Independent verification: a second pass, recorded as the assistant's
   check; the instrument or procedure of record; every claim carries a
   verification status (by the researcher, by the assistant, deferred to a
   named instrument, or unchecked); a claim is established when the
   researcher says so.
6. Privacy and sensitivity: no personal data beyond attribution; restricted
   sources enter by locator only; written as if public; imports only under
   the import policy.
7. Respectful and professional language.
8. Prompt logging: numbered, first act of the round, verbatim except for
   what §6 excludes; the reason for any correction; immutable once
   committed; the log versus the version history.
9. Terminology: glossary; and the Ontology's predicates as the vocabulary
   for recorded relations.
10. Scope discipline: nothing beyond what was asked; reads only what the
    task names and the researcher points at; no silence on an objection.
11. Editorial standards: pointer; the voice read off the researcher's own
    writing or stated by them; mechanical part checked on unfrozen
    artifacts.
12. Forward-evolving corrections: the immutable record never altered;
    frozen artifacts corrected only with authorization, in the running
    text, date-only stamp; current-state corrected in place; the reason
    for a correction recorded in the log or the commit message; the two
    authorization-gated current-state files.
13. Document genres and the round check: exactly what is checked
    mechanically per section; a failed check is reported.
14. Subagents: write no tracked file; find, do not write; a sweep reports
    before the main thread edits.
15. Git commits: the researcher performs every commit, with the rationale.
16. Status reporting and reminders: plain language; the status block,
    specified precisely enough to check; "running" checked by the
    assistant; reminders of what the stage calls for; enforcement through
    the slot `{{REPLY_HOOK}}` where the harness allows it.
17. Opposition: the assistant says when it disagrees and why; makes the
    opposite case on request; records disagreement beside the claim;
    proposes structured adversarial review when a claim is about to be
    relied on.

**Slots.** `{{PERSONA}}`; `{{VERIFICATION_TOOL}}`, the instrument or
procedure of record; `{{REPLY_HOOK}}`, the harness wiring of the reply
checker.

**Done when.** Reads as naturally for a historian or an economist as for a
physicist; every section generic or a marked slot; scan clean.

### Step 3: Document genres and the state model

**Goal.** The rule that keeps documentation from turning into a change log
of itself, and the rule that state is recorded once.

**Deliverables.** `DOCUMENT_GENRES.md`: the three genres and how each may
change; a *Words used here* section (plan status vocabulary `DRAFT`,
`ENGAGED <date>`, `CLOSED <date>, verdict <V>` with ABANDONED a verdict;
open means DRAFT or ENGAGED; the `Plan: NNN` ownership header line;
maintained; ledger versus register; the public record); the prompt log
immutable once committed, with no append exception, and the log's mutable
index pointing from a wrong entry to its correction; the frozen table
extended to derived material, imports, and written check procedures, with
the release signal (`Released <date>` line plus changelog row); a released
write-up succeeded rather than corrected; maintained artifacts under
`paper/`; an open plan's artifacts live; the standing reservation stated
generically with examples from three disciplines and its instrument
deferred to `CHECK_METHODOLOGY.md`; state recorded once, the ROADMAP an
index the checker compares with each plan; the current-state table
extended (keystone, tension ledger, research statement, references,
tools, indexes); the header rule stated precisely and non-prose files
excluded; the narrative ban renamed to the text's own past, with the
subject-matter exception; dated records and the execution-status ledger
exempt; indexes and cross-references kept on purpose; and **What the
checker verifies**, the closed, implementable list of eight checks that
step 9 implements.

**Slots.** `{{DELIVERABLE}}`, the publishable deliverable and what is
released with it.

**Done when.** Generic; the *What the checker verifies* list is closed and
implementable, and every other rule is marked as the assistant's duty; scan
clean.

### Step 4: Editorial standards

**Goal.** The prose standards for every durable artifact, and the procedure
by which a project derives the researcher's own voice.

**Deliverables.** `evidence_and_reasoning/editorial_standards.md`: scope
by pointer to the manifesto's definition of a durable artifact, with the
prompt-log carve-out; the five standards; a Conventions table holding the
project's choices as slots; the corollaries, with the "never assert what
could have been checked" rule led by its principle and illustrated from
three disciplines, and the narrative rule reduced to a pointer to the
genres file; *Writing for publication* scoped to every unfrozen `paper/`
artifact, with evidence, prose, flow, and discussion rules glossed for
non-computational disciplines and the deliverable's form a slot; *Voice*
as a slot with the four goals and a mixed mathematics-and-history example
record; **What is checked mechanically**, the closed list of editorial
checks that step 9 implements; and how to apply.

**Slots.** `{{SPELLING}}` (language and variant); `{{DASH_CONVENTION}}`;
`{{PAPER_PRONOUN}}` (the paper's agent); `{{REFERENCE_ADEQUACY}}`;
`{{DELIVERABLE}}` (shared with the genres file); `{{VOICE}}`.

**Done when.** Generic; the mechanical subset is a closed list; every
example is discipline-mixed; scan clean.

### Step 5: Verification methodology

**Goal.** The unit of work, the check, and the discipline that makes a
passing check mean something.

**Deliverables.** `CHECK_METHODOLOGY.md`: the check as the unit of
verification, owned by a plan and carrying no status of its own; a *Words
used here* section defining claim, assertion, gated (in every sense used),
verdict, check record, mutation, and docket; the **header lines** a claim
and a check carry (`Register:`, `Kind:`, `Verdict:`, `Plan:`, `Mutation:`,
and `Reserved <date>, plan NNN` with a comma so it cannot read as a change
narrative), which is what makes the mechanical checks implementable; the
**register** vocabulary (VERIFIED, DERIVED, ATTESTED, SPECULATIVE,
RULED_OUT, OPEN) with **who assigns it** stated (the assistant proposes,
the researcher assigns, because `MANIFESTO.md` §5 reserves establishment
to the researcher) and reconciled with verification status; the seven
**claim kinds** with a verdict vocabulary each, including Inferential for
an estimate under stated assumptions, and register declared independent of
kind; **the instrument or procedure of record**, which fills the
`{{VERIFICATION_TOOL}}` pointer the manifesto makes; the philosophy; **a
passing check is not a true claim** in six rules, with mutation and
robustness check explicitly distinguished so that survival is a defect in
the one case and the intended result in the other; the **standing
reservation**; the **consistency sweep** in eight items, proposed by the
assistant and run at the researcher's direction, with the structure lens
and what a rebuild owes, and with the fix-or-bring rule keyed to
maintained and authorization-gated artifacts rather than to genre alone;
the six-part shape of a check, splitting a written check procedure into
the procedure a plan freezes and one record per execution; and **What is
checked mechanically**, six items step 9 implements.


**Slots.** `{{CHECK_FORM}}`, what a check is in this project;
`{{MUTATION_SET}}`, the alterations the probe applies.


**Carried in from steps 3 and 4.** `CHECK_METHODOLOGY.md` owns the
definition of **register** (the statement's trust level) and reconciles it
with the manifesto's verification status (who checked, §5); it defines the
**standing reservation** instrument (what it says, what it licenses, how a
sweep treats a reserved claim), which the genres file now only points to;
and it treats a **written check procedure** (a collation protocol, an
estimation protocol, a reading procedure) as a first-class check beside a
check program.

**Slot.** What "computation" means in the discipline, with a table of
worked examples: a statistical re-analysis from raw data; an archival
reading against page images; a replication of an experiment; a formal
proof; a re-execution of published code; a re-coding of a survey.

**Done when.** Generic; the six-part check template of step 8b implements
it; scan clean.

### Step 6: Precedence and the tension ledger

**Goal.** What governs when sources disagree, in both directions.

**Deliverables.** `PRECEDENCE.md`: a *Words used here* section defining
divergence (a pair of statements that cannot both hold at the claim's
stated scope, so that a different sample or edition is not one), context,
the public record, and the tension ledger; the four tiers, with tier 2
covering a source consulted at its locator where access conditions keep it
out of the repository and tier 3 the references not collated; a table
mapping every register, and also the unregistered cases, onto the tier it
speaks from; the assistant's priors and the researcher's memory declared
not a tier; the trump rule with **who may apply it** (only for a register
the researcher has assigned; otherwise propose and stop); the rule in both
directions, with the routes for borrowed material split apart so that
"marked as context" can no longer read as a route to established fact;
cautions surviving; compliance, with the ledger row proposed by the
assistant and entered at the researcher's direction and a standing
reminder while it waits; **What is checked mechanically**, which claims
nothing of its own and points at the two owners; what the rulebook does
not do; and the ledger template with its four columns and its
reversed-tension marker.


**Done when.** Generic; every register and every unregistered case maps to
a tier; session onboarding (step 8e) loads it; scan clean.

### Step 7: The Ontology

**Goal.** The predicate vocabulary that makes the artifacts one system. Each
predicate is defined once, written in a fixed surface syntax inside the
artifacts, checked by a tool, and queryable across the repository. This is
the load-bearing deliverable of VISION.md and is designed here, before the
artifact templates, so the templates implement it.

**Deliverables.** `ONTOLOGY.md` with: (a) the catalogue, one entry per
predicate: name, what it relates, definition, where it is written (artifact,
field, surface syntax), how it is checked (tool, check), how it is queried;
(b) the implementation matrix, predicates against artifacts against tools;
(c) the surface-syntax conventions (reference keys, claim citations, plan
pointers, status lines, date stamps, register labels).

**Starting inventory**, generic names, extracted from the source
methodology; to be pruned and completed:

- `registered(work)`: a work consumed by project text has a registry entry.
- `cites(artifact, work)`: surface: a bracketed key; checked: no dangling keys.
- `held(source, license-note)`: a local copy exists with its redistribution
  basis recorded.
- `claims(claim, statement, register)`, register in {VERIFIED, DERIVED,
  ATTESTED, SPECULATIVE, RULED OUT, OPEN}.
- `not-claimed(claim, statement)`: the explicit scope fence.
- `gated-by(assertion, check)`: a check whose verdict would fail if the
  assertion were false; checked by the constant-condition guard, the
  coverage audit, and the falsifiability probe.
- `records(check-record, check-program)`.
- `owned-by(artifact, plan)`, from which `live(artifact)` and
  `frozen(artifact)` are derived, never stored.
- `status(plan)` in {DRAFT, ENGAGED, CLOSED, ABANDONED};
  `verdict(plan)` in {CONFIRMED, REFUTED, COMPLETE}.
- `prerequisite(plan, plan-or-claim)`; `serves(plan, hypothesis)`.
- `input-kind(input)` in {derived, imposed, conjectured}.
- `corrected(frozen-artifact, date)`: a body change under authorization,
  stamped with a date only.
- `deprecated-by(artifact, artifact)`.
- `restates(artifact, fact)`: the defect class; mitigated by
  `single-source(fact, location)` and a shadow scan.
- `in-tension(claim, public-statement, caution)`;
  `authority-tier(statement)` in {1, 2, 3, 4}.
- `reserved-by(claim, plan)`: the standing reservation.
- `logged(prompt, number)`: immutable, contiguous, indexed;
  `authorized(change, prompt)`: a human authorization recorded in the log.
- `reviewed-by(paper, review)`; `deletion-ledger(rebuild)`;
  `additions-ledger(round)`.
- `defined(term, kind)`, kind in {established, project-specific}.
- `indexed(file, index)`; `exists(path)`.
- `finding(identifier, claim)`: the gated findings file.
- `imported(artifact, origin, date)`: re-derived before built upon.
- `deferred-to(claim, tool, version, script, output)`: what the researcher
  handed to an external instrument, recorded so it is auditable.
- `status-line(reply)`: the assistant's closing status block.

**Done when.** Every predicate appears in at least one template (step 8)
and is checked or queried by at least one tool (step 9), or is marked
"declared, not yet mechanized" with a reason; every template field maps to
a predicate; scan clean.

### Step 8a: Artifacts: the record core

**Deliverables.** Templates with placeholder slots and a short worked
example each: `research_statement.md` (the question as posed; updated only
on a significant deviation); `research_result.md` (the condensed summary,
every sentence backed by a claim); `problem_statement.md` (the keystone: the
researcher's thesis as falsifiable hypotheses, SPECULATIVE register, the
ground plans are mined from); `terminology.md` (established and
project-specific terms, with an index); `FINDINGS.md` (what the record has
established, with stable identifiers and the authorization gate);
`CURRENT_STATE.md` (the top-level technical summary: established, ruled
out, open). The layout of the `evidence_and_reasoning/` directory and its
indexing README.

**Done when.** Each template's fields map to Ontology predicates; scan clean.

### Step 8b: Artifacts: claims and checks

**Deliverables.** `key_claims/` with its README (numbering, status
vocabulary, genre rule) and a claim template (header with register, date,
plan, program, record; CLAIM; WHAT IS NOT CLAIMED; REFERENCES); a
check-record template (`check_NNN_results.md`: what was tested, results,
discrepancies, verdict); a check-program template in the six-part structure
with the `report(...)` helper, the failure and findings accumulators, and
an exit status; a `python_project/` scaffold (README, requirements,
`conftest`, `src/` with its lint-enforced index, `tests/`).

**Done when.** The template check runs, passes, and is shown to fail when
its object is mutated; scan clean.

### Step 8c: Artifacts: references and sources

**Deliverables.** `references/` with its README (one file per topic; the
registry is exhaustive of works consumed by project text; self-contained;
originality verified) and the entry format (authors, title, venue, year,
URL or DOI, topics, originality note, notes). `source_documents/` with its
README (only freely redistributable documents held locally, each with a
license note; everything else by canonical identifier; naming convention;
no personal data).

**Done when.** Formats generic; scan clean.

### Step 8d: Artifacts: plans, roadmap, notes

**Deliverables.** `research_plans/` with its README (the lifecycle DRAFT,
ENGAGED, CLOSED with verdict, ABANDONED; both transitions the human's;
artifact hygiene while a plan is open; more than one plan may be engaged
and the assistant says so) and a plan template (status line; kind, whether
hypothesis or foundation; the aspect isolated; why a plan and not a
correction batch; prerequisites; tasks; sanity checks; deliverables;
confirmation and refutation criteria pre-registered; out of scope; an
execution status register that must be complete). `ROADMAP.md` template
(the ledger; the dependency graph; the ground-truth bar). `notes/` with its
README (dated; two registers, sketch and analytical note, never conflated).

**Done when.** A plan can be drafted, engaged, executed, and closed on the
templates alone; scan clean.

### Step 8e: Artifacts: prompt log and session onboarding

**Deliverables.** `prompt_logs/` with its README (numbering, immutability
once tracked, corrections in a later entry, the supplemental corrigendum
exception with its exact block form) and an entry template (date, number,
description, the prompt verbatim, what was done in response, status). A
`CLAUDE.md` template for session onboarding: the rulebooks, the precedence
rule, the keystone, the cold-start reading order, the standing constraints.

**Done when.** The round gate of step 9 can verify numbering, indexing, and
immutability on the template alone; scan clean.

### Step 8f: Artifacts: publication, reviews, imports

**Deliverables.** `paper/` with its README (one living copy of the main
write-up; versions freeze with their compiled output committed; a version
is succeeded, not corrected; title-page convention; changelogs; standalone
notes dated in the filename; build convention). `paper/reviews/` with its
README (dated, names the producing model, genre by path) and a review
template (what was independently re-derived and confirmed; corrections
applied; what remains). `inherited/` with its README (the import policy: an
import is a frozen copy at its original date with attribution, listed in an
imported table and covered in the license; anything built on is re-derived).

**Done when.** Formats generic; the pipeline slot documented; scan clean.

### Step 9: Mechanical enforcement: the tools

**Goal.** The checks that keep the record honest, none of which need an
LLM, a network, or a dependency, each with a self-test.

**Deliverables**, under `tools/`, each generic and configuration-driven:

- `lint_docs.py`: the genre linter. Configuration lists immutable
  directories, frozen globs, dated-record globs, current-state files, and
  exemptions. Checks: current-state documents carry no history narrative;
  tracked immutable files are unmodified (corrigendum appends excepted);
  frozen bodies change only with a dated stamp; every named repository path
  exists; every program appears in its index; no check assertion has a
  syntactically constant condition; the mechanical editorial rules on live
  drafts.
- The linter's specification is the union of *What the checker verifies*
  (`DOCUMENT_GENRES.md`) and *What is checked mechanically*
  (`editorial_standards.md`); nothing else is mechanical, and each check
  names the item it implements.
- `check_round.py`: every round gate in one command: the linter; log
  numbering, indexing, and immutability; index coverage; and, when the
  publication pipeline is enabled, the build (refused on a stale log or
  output) and the bibliography (every entry cited, in first-citation order).
- `check_status_reply.py`: the status-block hook.
- `claim_sites.py`: the blast radius of a claim, every artifact citing it,
  with what a citation search cannot see said in the output.
- `check_concordance.py`: load-bearing numbers and facts single-sourced,
  recomputed where computable, with a shadow scan for the wrong value in the
  right context, and a coverage report.
- `falsifiability_probe.py`: a harness that applies a project-supplied list
  of axiom-level mutations to a scratch copy of the tree, re-runs every
  check, prints the matrix, and asserts that no check survives every
  mutation. Mutations are the project's; the harness is generic.
- `run_ledger.py`: a run cache keyed by a content hash of everything a
  verdict rests on, so recomputation follows a changed basis literally.
- `check_residue.py`: refactoring residue in a live draft (seams, dangling
  and orphaned references, phantoms, echoes, structure, additions ledger);
  pipeline-specific, shipped as an optional module.
- `privacy_scan.py`: the generic form of the `.privacy/` mechanism, reading
  a git-ignored list, with a hook installer; opt-in.
- `tools/README.md` indexing all of the above.

**Done when.** Every tool passes its own self-test; the round gate passes on
the bare template; each linter check names the genre rule it enforces and
each rule names its check; scan clean.

### Step 10: Governance wiring: hooks, reminders, opposition, support

**Goal.** The mechanisms VISION.md promises, wired so they fire without
anyone remembering to fire them, and advisory by design.

**Deliverables.**

- *Hooks.* A tracked harness settings file with the stop hook for the
  status block and a session-start hook that prints the reading order and
  the count of engaged plans; a `tools/install_hooks.sh` that installs the
  pre-commit round gate (and the privacy scan where configured), since git
  hooks are not cloned.
- *Reminders.* The standing instructions, each named and placed where it
  fires: the sweep after every correction batch; the plan-closure checklist;
  the "more than one plan engaged" notice; log the prompt first; the
  findings gate.
- *Opposition*, formalized as named roles with their standard prompts under
  `governance/roles/`: the refuter (every sweep finding is handed to a reader
  instructed to refute it); the blind referee (a review with no access to
  the project's code or claims before a paper freezes); the structure census
  (before any sentence-level edit to a section); the deletion ledger (for
  every rebuild); the coverage auditor (atomic assertions classified GATED,
  PRINTED_ONLY, NOT_COMPUTED, MISMATCH, ATTESTED, each gap refuted by a
  second reader); the falsifiability probe as opposition to one's own
  checks.
- *Support.* Every template carries a worked example; `governance/README.md`
  maps each mechanism to the rule it serves and the moment it fires.

**Done when.** Each mechanism is documented with its trigger, its output,
and what it does not decide; the hooks run on a fresh clone after the
installer; scan clean.

### Step 11: Worked example project

**Goal.** Proof that the template works end to end, and the researcher's
first model of what a round looks like.

**Deliverables.** Under `example/`, a small complete project instantiated
from the template in a domain outside mathematics and physics (decision
above): a research statement; a keystone with one hypothesis; one plan
drafted, engaged, executed, and closed; two or three checks with records;
claims in each register; a reference registry; a tension-register row; a
prompt log of the example's own rounds (the example is a research project,
so its log is kept); a short paper with one review; every gate passing.

**Done when.** The round gate and the probe pass inside `example/`; a
newcomer can read it in under an hour; scan clean.

### Step 12: Breadth review beyond mathematics and physics

**Goal.** VISION.md's generalization commitment, tested adversarially.

**Deliverables.** A review of every artifact through at least four
non-physics lenses (a historian, an empirical social scientist, a
biologist, a legal scholar or a machine-learning researcher), each asked
where they are fenced out, what jargon is unexplained, and which slot they
cannot fill. Findings applied; the slot table in the guide completed with
one filled example per lens.

**Done when.** No artifact assumes a discipline outside a marked slot; scan
clean.

### Step 13: The guide

**Goal.** What VISION.md promises the researcher on day one and throughout.

**Deliverables.** `README.md` rewritten as the entry point (what the template
provides, the map of the repository, licenses, lineage);
`GETTING_STARTED.md` (clone, instantiate, fill the slots, first round, first
plan, first check, first commit); `HOW_IT_FITS_TOGETHER.md` (artifacts,
Ontology, tools, and hooks as one system, with the round as the unit of
time); `FORKING.md` (the researcher owns the clone; how to remove or change
a mechanism deliberately and legibly); a frequently-asked-questions section.

**Done when.** A reader who has never seen the lineage can start a project
from the guide alone; scan clean.

### Step 14: Instantiation procedure

**Goal.** The "set up quickly" expectation.

**Deliverables.** `tools/new_project.py` (or a documented manual procedure):
copies the template, fills the slots (project name, discipline, persona,
verification tool of record, researcher name, licenses' citation block,
start date), removes `VISION.md`, `VISION_PLAN.md` and `example/`, strips every
`> **Build lens.**` block from `MANIFESTO.md`, resets
the prompt log to entry 001, and runs the round gate.

**Done when.** A fresh instantiation passes the round gate with no edits;
scan clean.

### Reviews on record

Every step through 6 has had an independent read-only review before
acceptance. Steps 5 and 6 were reviewed by six lenses over
`CHECK_METHODOLOGY.md` and `PRECEDENCE.md`, which returned 149 findings,
42 of them major, and the majors were applied. That review also reached
four accepted files, and the amendments it forced there are recorded in
the step 2, 3, and 4 entries.


### Tracked across steps: forward references

The rulebooks name files that later steps deliver. As of step 6 the
governance documents name 22 paths that do not exist yet, among them
`ONTOLOGY.md` (step 7), the record core and the indexes (steps 8a to 8f),
and `tools/lint_docs.py`, `tools/check_round.py`, and
`tools/check_status_reply.py` (step 9). This is expected while the
template is built, and it has one consequence to keep in view: the
dangling-path check (`DOCUMENT_GENRES.md`, *What the checker verifies*,
item 7) cannot pass until step 9, and the linter is therefore not run
against a partly built template. Step 15 verifies that every named path
resolves; until then the privacy scan is the gate (`MANIFESTO.md` §13,
build lens).

### Step 15: Close-out

**Goal.** The template is complete enough to stand without this plan.

**Deliverables.** A consistency sweep over the whole repository (every
pointer resolves, including the forward references tracked above; every index complete; no duplicated state); every tool's
self-test and the round gate passing at the top level and inside
`example/`; the README's under-construction notice removed; `VISION.md`
kept as the durable statement of intent; **this file deleted**.

**Done when.** The deletion is committed by the researcher.

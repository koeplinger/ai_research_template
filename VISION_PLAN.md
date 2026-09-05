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
| 5 | Verification methodology | DONE | 2026-09-03 |
| 6 | Precedence and the tension ledger | DONE | 2026-09-03 |
| 7 | The Ontology | DONE | 2026-09-03 |
| 8a | Artifacts: the record core | DONE | 2026-09-03 |
| 8b | Artifacts: claims and checks | DONE | 2026-09-03 |
| 8c | Artifacts: references and sources | DONE | 2026-09-04 |
| 8d | Artifacts: plans, roadmap, notes | DONE | 2026-09-04 |
| 8e | Artifacts: prompt log and session onboarding | DONE | 2026-09-04 |
| 8f | Artifacts: publication, reviews, imports | DONE | 2026-09-04 |
| 9a | Tools: the configuration artifact and the linter | DONE | 2026-09-05 |
| 9b | Tools: the round check, the reply hook, the privacy scan, the hook installer | READY | 2026-09-05 |
| 9c | Tools: the ontology queries, claim sites, concordance | NOT STARTED | |
| 9d | Tools: the falsifiability probe, the run ledger, the residue check | NOT STARTED | |
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
- **The claims folder (resolved in step 7).** The Ontology hardcoded
  `evidence_and_reasoning/claims/` while `CHECK_METHODOLOGY.md`
  deliberately leaves the filing convention configurable. Resolved: no path
  is hardcoded anywhere; `tools/artifacts.toml` holds the glob, and step 8b
  ships `claims/` as the default rather than `key_claims/`, since *key
  claim* is a term of art the template need not impose.
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

**Deliverables.** `ONTOLOGY.md`: the four-things contract (what a
predicate relates, where it is written in exact surface syntax, how it is
checked, what question it answers) delivered per row, with an **Answers**
column on every catalogue table; **four surface forms** (field lines with
a colon; stamps without one, since a colon after a date opens a change
narrative; citation tokens with a grammar each, including a citation
**locus** so a folio, table column, or survey wave can be cited; and
governed files), plus an explicit list of the relations carried in prose
and parsed by nothing; a catalogue of 43 predicates in eight groups, whose
**Checked by** column points at the owning rulebook's numbered check
rather than restating or extending it; `backed-by`, the claim-to-check
link the whole system rests on, which the first draft omitted; the
relations non-computational disciplines need (`cites-at`, `produced-from`,
`witness-of`, `performed-by`, `frame`, `robustness`, `pre-registered`);
derived predicates never stored; a register ordering declared for
reporting only; the ontology's six own checks; eight queries, each saying
where it enumerates and where the deciding is reading; **§7 Where the
patterns live**, naming one configuration artifact as the single source of
every path pattern in this file and in the two rulebooks that defer to it;
and **§8 What to keep current**, ranking the fields into mandatory and
written-when-they-apply, because an unranked list of eleven obligations
per claim is a system a researcher abandons by the tenth claim.


**Done when.** Done as a specification. Two obligations it places on
later steps are carried below rather than closed here.

**Obligations this step places on step 8.** Every predicate names a
template that pre-prints its field: the mandatory fields of §8 appear in
the shipped claim, check, and check-record templates with their
vocabularies in a comment, so that filling in the form is writing the
predicate. A predicate with no template home is not shipped, and step 8
either supplies the home or deletes the row.

**Obligations this step places on step 9.** Deliver `tools/artifacts.toml`
with one row per artifact kind (glob, genre default, required fields) as
the single source of every path pattern; implement the ontology's six
checks and eight queries; and make the claim and check path patterns real,
which is what `[claim NNN]` and `[check NNN]` resolve through.


### Step 8a: Artifacts: the record core

**Deliverables.** `evidence_and_reasoning/README.md` (the index, the
reading order, the order of first use, the numbering conventions, and the
directory's Slots table); `research_statement.md` (the question as posed,
the lines of work with examples from three disciplines, scope, method;
state deferred to `CURRENT_STATE.md`); `research_result.md` (every
sentence carrying its claim token); `problem_statement.md` (the keystone:
each hypothesis with what it takes as given, classified derived, imposed,
or conjectured, and what would count against it; lines of work; what is
deliberately not pursued); `terminology.md` (established and
project-specific terms, and a *Names the sources use* table with a locus
column and a mapping column that admits *by construction, rule fixed in a
check*); `FINDINGS.md` (bare tokens, opaque keys assigned once, governance
by pointer, proposals living in the reply and the log rather than the
file); `CURRENT_STATE.md` (established, ruled out, open, engaged by
pointer to the plan index). Guidance is in HTML comments the instance
deletes; no template carries a Genre column or a second copy of state.


**Done when.** Each template's fields map to Ontology predicates; every
example is discipline-mixed or neutral; scan clean.

### Step 8b: Artifacts: claims and checks

**Deliverables.** `evidence_and_reasoning/claims/`: a README (numbered
form as the configured pattern, index with Kind and Plan as navigation and
no copy of the register, a *Not claims* row for the template) and
`_template.md` pre-printing the five mandatory fields with every
vocabulary in a comment, the seven verdict vocabularies included, and the
conditional fields listed with their syntax to add when they apply rather
than pre-printed empty. `evidence_and_reasoning/checks/`: a README (the
two forms, one file each: a program's record, or a written procedure with
one dated entry per execution under `## Executions`) and `_template.md`
pre-printing `Plan`, `Backs`, `Instrument`, `Mutation`, `Frame`, and `By`,
with the run's date and party in part 4, the second pass in part 6, and
`name = value` lines the concordance check compares. `python_project/`:
README (the contract in any language; a project with no programs told
plainly that it is missing nothing), `requirements.txt`, `conftest.py`,
`src/README.md` and `tests/README.md` as checked indexes, and
`src/_template_check.py`: six parts, `report()` with no constant
conditions, `value()` feeding the `RESULT:` line, a `MUTATIONS` binding
the probe applies, and the verdict vocabularies with three-valued kinds
set from which assertions failed.


**Done when.** The template compiles and carries no constant-condition
report; a real check built from it runs, passes, and is shown to fail
under its named mutation in step 11; scan clean.

### Step 8c: Artifacts: references and sources

**Deliverables.** `evidence_and_reasoning/references/`: a README (every
citation resolves here; organization by topic, repository, or data
source; the key grammar and locus forms with examples; entry fields as
bullets inside a `### [Key]` block with the default set, `Standing` in
both its forms, `Disputed`, and `Witness of` with the rule for a work
known only through its records) and a file template with
discipline-mixed field guidance. `source_documents/README.md`: the
source-of-record index, one row naming either a held file or folder with
its license note or a locator with its access conditions, the form
consulted, and the rule that a restricted source enters only as its terms
allow. `evidence_and_reasoning/public_record_tensions.md`: the tension
ledger in the five-column form, with unmatchable placeholders.


**Done when.** Formats generic; every row form matches the Ontology's
predicates; scan clean.

### Step 8d: Artifacts: plans, roadmap, notes

**Deliverables.** `evidence_and_reasoning/research_plans/`: a README
(the lifecycle by pointer to the genres file, which now owns it; more
than one plan engaged is said in the reply and seen in the index; an
undecided outcome closes ABANDONED unless pre-registered otherwise) and a
plan template carrying `Status`, `Serves`, and `Prerequisites` as field
lines, a prose marker for a plan with or without a hypothesis, sections
for the aspect, the hypothesis, the **design** with its assumptions
classified, tasks, sanity checks, deliverables, pre-registered
confirmation and refutation including what an undecided outcome closes
as, out of scope, an optional standing reservation and docket, and a
complete execution ledger with a fixed state vocabulary. `ROADMAP.md`:
the plan index with the one deliberate status copy the checker compares,
and a pointer to `PRECEDENCE.md` for what may be relied on in place of
any authority rule of its own. `evidence_and_reasoning/notes/`: a README
(two kinds, working and analytical, with a decision rule; what an
analytical note may and may not do; a pre-registration protocol as an
analytical note with no owning plan) and a template whose kind is a prose
marker rather than a field.


**Done when.** A plan can be drafted, engaged, executed, and closed on the
templates alone, with every rule it relies on owned by a rulebook rather
than by the README; scan clean.

### Step 8e: Artifacts: prompt log and session onboarding

**Deliverables.** `prompt_logs/`: a README (Markdown entries, numbered
and immutable once committed; the README and the template as the folder's
two current-state files; the four parts of an entry the round check looks
for; a *Completed or corrected by* column pointing from an earlier entry
to the later one) and an entry template (the prompt verbatim between
delimiters with the redaction form for restricted material; what was
done; corrections and departures, where the reason lives; the closing
status block, fenced and outside the header block). `ONBOARDING.md`, the
session-onboarding file, vendor-neutral and named in the two rulebook
tables that point at it: the first minutes as a reading order that opens
the round's log entry and reads the manifesto in full before anything
else; the precedence rule with who may apply it; the keystone; the
standing constraints a session meets in its first minutes, the manifesto
being the complete statement; a section for the researcher's standing
directions that copies no slot value; and a setup rule for a first
session, pointing at the guide step 13 ships.


**Done when.** The round check of step 9 can verify numbering, indexing,
immutability, and the four parts on the template alone; scan clean.

### Step 8f: Artifacts: publication, reviews, imports

**Deliverables.** `paper/`: a README (one living copy, succeeded by
default rather than corrected; the release as the researcher's stamp and
changelog row, the first version having no changelog; dated notes
date-first like every dated record; a blind referee before every freeze;
form, page marking, and what is released with a version all deferred to
`{{DELIVERABLE}}`; a numbered *Releasing a version* procedure) and a
changelog template with a pre-printed release row, the deletion ledger,
and the additions ledger, so that both ledgers a rebuild owes have one
home. `paper/reviews/`: a README (naming, outside readers as their
conditions allow, the structure lens and the refuter by pointer, the
fix-or-bring rule as the check methodology states it, the blind referee
as a fresh session or a subagent given the write-up alone) and a template
whose identity line stays in prose, with a `Fix proposed` column and an
optional `Plan:` line. `inherited/README.md`: the import policy and the
one ledger of imports, which `LICENSE.md` now points at; imports by
locator only where access conditions require; a candidate list at the
researcher's direction, nothing copied.


**Done when.** Formats generic; every rule the READMEs rely on is owned by
a rulebook; scan clean.

### Step 9: Mechanical enforcement: the tools

Executed as four sub-steps, each with its own review cycle, because the
tools are the largest deliverable of the build and each later tool reads
the configuration and the linter of the first: **9a** the configuration
artifact `tools/artifacts.toml` and `tools/lint_docs.py`, which implements
every item the three rulebooks and the Ontology list as checked
mechanically that a static read of the tree can decide; **9b** the round
check, the reply hook, the generic privacy scan, and the hook installer;
**9c** the ontology queries, claim sites, and concordance; **9d** the
falsifiability probe, the run ledger, and the residue check. Every tool:
no dependency beyond the Python standard library (3.11 or later, for its
TOML reader), a `--selftest` that constructs failing and passing cases so
the tool is shown to fire, and a report that names the rulebook item each
finding implements.



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

### Step 9a as built

`tools/artifacts.toml`: 45 artifact rows matched first-wins with a
slash-aware glob (the folder patterns the tools locate the log, the plan
index, and the registry by are derived from the rows, never repeated);
16 index rows, the root README among them; the field catalogue and the
derived-state names; the register, kind, verdict, plan-status, and
plan-verdict vocabularies, the inferential verdict as its two pairs; the
`{{MUTATION_SET}}` and `{{PARTIES}}` slots, empty in the template and
reported as unfilled once a check or a party exists to apply them to; the
log's five parts; the registry's required bullets; the editorial
conventions the linter reads (`us`, `no-em-dash` for the build, both
dash conventions implemented); and a `skip` escape hatch honored by every
check in one place, used once, for this plan's forward references.
`tools/lint_docs.py`: eighteen checks tagged GENRES-1 to 8, EDIT-1 and 2,
ONT-1 to 6, CHECK-1 to 3, each naming its owner's item, and a docstring
that says what it does not decide. What is read: a program's docstrings
and comments only, a configuration file's comments only, never a log
entry's verbatim region, never quoted text or block quotes for the
editorial checks, and never the italicized examples of the two files the
narrative rule names, for that check alone; every skipped span is blanked
rather than removed so line numbers stay true. The genre derivation
follows `ONTOLOGY.md` §3: a `Plan:` line overrides every default but
immutable, self, and exempt; a dated record is frozen otherwise; a
release is live until its `Released` stamp or its release row. `--list`
prints kind, default genre, and derived genre; `--selftest` builds the
scratch project under git, so the two history checks run, plants 50
defects, and confirms each check fires at the named file with the named
message while the unplanted tree is clean. `tools/README.md` indexes
both.

**Independent review**, four read-only lenses (specification, correctness,
configuration, honesty of self-test and docstring), transcripts audited
for scope: 72 findings, 26 major, every one applied. The largest: the
self-test's scratch tree was not a git repository, so the two history
checks had never been shown to fire and one was excluded from the
verdict; italics were blanked from every check, hiding real prose;
a stamp of the wrong form fell silently out of the header; the
mutation-name check did not read the template's own annotated form;
the constant-condition check trusted its own fixture.

**Run on this repository** the linter reports five findings, all true
and all owned: `tools/check_round.py` and `tools/check_status_reply.py`
are 9b's; `GETTING_STARTED.md` is step 13's; and `CLOSING_NOTE.md`, which
`DOCUMENT_GENRES.md` names as frozen on writing, has its row in the
configuration but no template, which step 13 supplies as
`_template_closing_note.md` beside the guide.

**Amendments made in 9a**, flagged at hand-over: two rulebook sentences
that stated the narrative ban by quoting the banned phrase itself (in
`DOCUMENT_GENRES.md` and `MANIFESTO.md` §12) are reworded to "its
earlier text", so the rulebooks pass their own check; one italic example
in `DOCUMENT_GENRES.md` is reflowed onto one line, the form the narrative
rule reads; the spelling examples in the `{{SPELLING}}` row of
`editorial_standards.md` are quoted rather than italicized, the form
item 1 skips; the root README gains its stamp and a table of the root's
files, which the index check reads and step 13's rewrite keeps;
`LICENSE.md`'s stamp gains the updated date the header rule requires.

### Step 9b as built

`tools/check_round.py`: every gate in one command. It runs the linter
in-process and passes its findings through under their own tags, GENRES-2
(the log's immutability) and GENRES-8 (index coverage, the log's index
included) among them, routes every finding through the linter's gate so
a row's `skip` list holds for all of them, and adds four gates of its
own. ROUND-1, the log's numbering: contiguous from 001, zero-padded, no
number twice, every name of the form `NNN_short_description.md`. ROUND-2,
the parts of an entry still open to editing, that is, uncommitted or
differing from its committed version: the parts `[log]` names, each once
and in order, searched after the verbatim region and outside fenced code,
and under the last part a fenced status block of the §16 form with no
RUNNING line; a committed entry is immutable and completed by a later
entry, so it is not re-read. ROUND-3 and ROUND-4, the publication
pipeline's gates, from a new `[publication]` table of
`tools/artifacts.toml`, disabled in the template: every output and the
build log newer than every source by modification time, which the
docstring and the table say a checkout does not preserve, the log free of
the configured error markers, the build named in the finding and never
run by the check; every bibliography entry cited, no citation the
bibliography lacks, no entry defined twice, and the entries in
first-citation order, the sources taken in configured order. Every
misconfiguration of the table is a finding, never a traceback.
`--scratch DIR` writes the linter's clean fixture with the tools into a
directory, for exercising the hooks in a throwaway repository.
`tools/check_status_reply.py`: the §16 form on a reply read from a file or
standard input, exit 0 or 1 with each reason; its two readings of the
section are stated in its docstring (a line breaks at a newline only; a
status line separated from the block by a blank line is reported); it
knows no harness, since the wiring is `{{REPLY_HOOK}}`.
`tools/privacy_scan.py`: the generic, opt-in form of the build's own
mechanism, reading a git-ignored list at `.privacy/stopwords.txt`
(whole-word patterns, with the underscore a separator in paths and a word
character in contents, and `~` substring patterns) over the working tree,
the staged content and paths, or a commit message with git's comment
lines skipped; absent the list, or where git cannot list the tree, it
gives no verdict and exits 2. It runs beside the round check, never inside
it, as `MANIFESTO.md` §13's build lens says. `tools/install_hooks.sh`:
writes `pre-commit` (the staged privacy scan, refusing; then the round
check over the working tree, reporting, or refusing under `--strict`) and
`commit-msg` (the message scan, refusing); every refusal names the
override, `--no-verify`, and asks that the commit message say why (§12);
a hook it did not write, or a hooks directory shared by `core.hooksPath`,
is left alone unless forced; `--uninstall` removes what it wrote; its
self-test exercises both hooks end to end in a throwaway repository,
including a hit that is staged only. Every tool answers `--selftest`, with
the planted stop word generated at run time so no tool's own text carries
it; the round check's self-test reuses the linter's fixture through three
helpers the linter now exposes. `tools/README.md` indexes all six files.

**Independent review**, four read-only lenses (specification, correctness,
configuration, honesty), transcripts audited for scope: 72 findings,
8 major, every one applied. The largest: the installed round gate refused
the researcher's commit, against the manifesto's opening rule and VISION's
warning that a blocking mechanism is routed around without trace, so it
now reports and the commit proceeds unless the hooks were installed
strict, while the privacy scan keeps refusing and every refusal asks for
a reason in the commit message; ROUND-2 re-read committed entries, which
§8 sanctions committing mid-round and forbids editing, so a finding could
never be cleared; the parts search read the verbatim prompt region the
configuration promises no check reads; the round check carried the
privacy scan, which no owner places there; the configuration sent a
project to a sentence of `paper/README.md` that did not exist; and the
installer's self-test could pass on the round check's scan without the
staged scan ever running.

**Run on this repository** the round check reports two findings, both
true: `GETTING_STARTED.md` and `CLOSING_NOTE.md`, which the rulebooks
name and no step so far has delivered. From this step on the end of
every step runs the round check and the privacy scan, as `MANIFESTO.md`
§13's build lens says.

**Amendments to accepted files made in 9b**, flagged at hand-over:
`paper/README.md` gains the bullet the configuration points at, that the
round check gates the build and the bibliography from `[publication]`
where the deliverable is built; `prompt_logs/README.md` gains the sentence
that owns the closing-status checks, the §16 form in a fence with no
RUNNING line, verified on an entry still open to editing;
`tools/lint_docs.py` exposes its fixture and scratch helpers, reads a
shell script's comments as prose under the `comment` header kind with the
unread spans blanked, and its fixture gains a second registry key and a
`.gitignore`; `tools/artifacts.toml` gains the `[publication]` table, a
`paper/**/*.bib` row, a `tools/*.sh` row, and the note that a typeset
source is out of the linter's reach.

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

### Amendments to accepted files made in steps 8e and 8f

Six, each forced by the templates and flagged at hand-over.
`DOCUMENT_GENRES.md` names `ONBOARDING.md` as the session-onboarding file,
exempts an imported file under `inherited/` from the header stamp since it
is a verbatim copy dated by its ledger row, and exempts `prompt_logs/
_template.md` from immutability beside the README; `MANIFESTO.md` names
`ONBOARDING.md` in its file table and gives the log entry example in
Markdown, `001_short_description.md`, so that entries carry the stamp;
`LICENSE.md` points at `inherited/README.md` as the one ledger of imports
instead of keeping a second list; `ONTOLOGY.md` §1.4 fixes the form of a
changelog's release row so the `released` predicate has a home.

Two obligations this step places on later steps: step 9's
`tools/artifacts.toml` carries the log-entry row and the four parts the
round check looks for; step 13 ships `GETTING_STARTED.md`, which
`ONBOARDING.md` already names for a first session's setup round.

### Amendments to accepted files made in steps 8c and 8d

Seven, each forced by the templates and flagged at hand-over.
`DOCUMENT_GENRES.md` now states what no rulebook had: that both plan
transitions are the researcher's, with the provenance in the log, and it
glosses the four verdicts, ABANDONED covering an outcome the
pre-registered criteria decided neither way. `ONTOLOGY.md` disambiguates
`Prerequisites` (plans by bare number, claims by token), admits the
found-form of `Standing` beside the none-found form, says that a registry
entry's fields are bullets read by entry rather than header lines, and
says that HTML comments are not read by the resolver, which is where every
template's example tokens live. `PRECEDENCE.md`'s ledger template takes
the five-column form the Ontology fixes, with the `T###` key and the
`Caution` column.

### Amendments to accepted files made in steps 8a and 8b

Five, each forced by the templates and flagged at hand-over:
`ONTOLOGY.md` admits `Verdict: none` while a claim is `OPEN` or
`SPECULATIVE`, catalogues `Backs: [claim NNN]` as the check side of
`backed-by`, and shows numbered-form globs (`[0-9]*.md`) so a folder's
`README.md` and `_template.md` fall outside the claim and check patterns;
`CHECK_METHODOLOGY.md` defines a check record as the dated entry recording
one execution, so a written procedure's executions have a home;
`DOCUMENT_GENRES.md` names a check's `## Executions` section beside a
plan's `## Execution status` in the ledger exemption and in checker 5, and
checker 1 admits the closing period and emphasis mark every accepted file
already writes after the stamp's second date.

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

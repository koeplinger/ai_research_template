# How it fits together

*Created 8 September 2026; updated 8 September 2026.*

`GETTING_STARTED.md` gets a project moving. This file says what the parts
are for, how they make one system rather than a folder of forms, and what
to do at each stage of a project. Read it once early and again when
something feels arbitrary; most of what looks arbitrary is one half of a
pair whose other half is in another file.

---

## The commitment underneath

**The repository is the primary artifact, and the paper is a projection of
it.** A reader with the repository and nothing else, no conversation
history, no memory of the sessions that produced it, should be able to
follow the work, continue it, or attack it.

Everything below follows from that. The log is immutable because a record
of what was believed at each step is worthless if it can be edited later.
Claims are files because a claim you can cite is a claim you can revisit.
Registers exist because "we checked it" and "a source says so" are
different, and a reader who cannot tell them apart is being misled by
omission. Checks carry planted faults because a check that cannot fail
tells you nothing.

---

## The three parts

### Artifacts: where things live

A project is a small number of kinds of document, each with an index, a
rule for how it may change, and, where the thing recurs, a template.

| Kind | Where | What it is |
|---|---|---|
| the question and the thesis | `evidence_and_reasoning/research_statement.md`, `problem_statement.md` | what the project is for, and the hypotheses it means to test |
| plans | `evidence_and_reasoning/research_plans/` | the unit of work: one aspect isolated, with criteria fixed before execution |
| claims | `evidence_and_reasoning/claims/` | one statement each, with its trust level, its kind, and what it does not claim |
| checks | `evidence_and_reasoning/checks/`, `python_project/src/` | one investigation each, with a verdict and a planted fault it must fail under |
| derived material | `evidence_and_reasoning/derived/` | what a plan made from a source: transcriptions, extracts, coded tables, figures |
| sources | `source_documents/`, `evidence_and_reasoning/references/` | what claims are read against, held or indexed by locator |
| notes | `evidence_and_reasoning/notes/` | dated working and analytical notes, including pre-registered protocols |
| the ledgers | `FINDINGS.md`, `evidence_and_reasoning/public_record_tensions.md` | what is established, and where this project diverges from what is published |
| the result | `evidence_and_reasoning/research_result.md` | what has been established, condensed to the altitude of the write-up |
| the project's terms | `evidence_and_reasoning/terminology.md` | the subject-matter glossary, and the names the sources use for each thing |
| imported material | `inherited/` | anything brought in from elsewhere, at its original date, with attribution, re-verified here |
| the log | `prompt_logs/` | every prompt, verbatim, in order, immutable once committed |
| the write-ups | `paper/`, `paper/reviews/` | the deliverable in its versions, and the reviews of each |

**Three genres, and that is the whole state model.** An *immutable*
artifact is never edited once committed (the log). A *frozen* artifact is
a dated record, corrected only with the researcher's authorization (a
closed plan and everything it owns). A *current-state* artifact describes
what is and is corrected in place (the rulebooks, the indexes, the status
files). `DOCUMENT_GENRES.md` says which is which and when each freezes.

### The ontology: the vocabulary they share

The artifacts are one system because they share a vocabulary, and the
vocabulary is implemented rather than described. Most predicates appear in
a template as a header field, are checked mechanically, and can be queried
across the whole repository; the rest are carried in prose and are the
sweep's business.

That is what lets you ask, by looking rather than remembering:

- *What is this conclusion standing on?* `query_ontology.py rests-on NNN`
- *Which of it is unverified?* `query_ontology.py unverified NNN`
- *If I revisit this claim, what else moves?* `claim_sites.py NNN`
- *Where might a claim be stronger than its backing?* `query_ontology.py sites`

`ONTOLOGY.md` is the catalogue: each predicate, the surface syntax that
carries it, the rulebook that owns it, the check that enforces it, and the
question it answers.

### Governance: what keeps it running when attention lapses

Four kinds of mechanism, **all advisory**. They fire, they inform, and
they leave the decision with you. One exception, marked as such: the
privacy scan refuses a commit, because a leak cannot be undone by a later
decision. It refuses only where a project has set up a stop-word list, and
a commit can still be forced with the reason recorded.

- **Reminders** say what the stage of work calls for before it is skipped.
  `governance/reminders.md` names each, what fires it, and what it does
  not decide. `tools/session_brief.py` prints the ones the record can
  compute, at the start of a session.
- **Checks** are the requirement that a class of claim be verified and the
  verification recorded rather than asserted. `tools/check_round.py` runs
  the linter and the round's own gates in one command; the concordance
  check, the falsifiability probe, the residue check and the privacy scan
  are run beside it, each at the moment `tools/README.md` names.
- **Opposition** is structured argument against your own position, played
  the same way each time by a standing role with a fixed prompt:
  `governance/roles/`. An assistant is agreeable by default, and a process
  that never contradicts you is not supporting you.
- **Support** is the templates, the indexes, and the worked example, so
  that the right thing to do is also the easy thing.

---

## The round: the unit of time

Everything is organized around one prompt and the work done in response to
it.

1. **The log entry opens the round**, before any work. The prompt goes in
   verbatim.
2. **The work happens**, through an engaged plan.
3. **The entry is completed**: what was done, by artifact; what was
   brought to you and left for your decision; the reason for any
   correction or departure.
4. **The reply closes the round** with a status block, saying in five
   seconds whether to wait, answer, or walk away. Where the harness allows
   it, a hook checks the block's form after every reply.
5. **The round check runs** before work is handed back, and again on
   commit.

A round with a process still running does not close: the reply reports it
as running, and the round closes when the process is done. A round
committed before it closed is completed by a later entry that points back.

**Nothing is edited backwards.** A mistake is corrected forward: the
current-state document is corrected in place, the frozen one is corrected
in its running text with your authorization, and the reason lives in the
round's log entry. The immutable record is where a reader goes to see what
was believed and done at each step.

---

## The prompts this methodology suggests

The mechanisms above are advisory, which means somebody has to ask. These
are the prompts worth making, when to make each, and what comes back. None
is magic wording: they are named so that the same thing is asked the same
way each time, and so that a reader of the log can see which one was made.

| Prompt | When | What comes back |
|---|---|---|
| **Make a documentation consistency sweep.** | First of all after instantiation, once the slots are filled; after a batch of edits to the rulebooks, indexes, templates, or configuration; after amending a rule or removing a mechanism; before a release and before the project closes; and whenever a pointer sent a reader to a document that did not say what it promised, which is the sign that it is overdue | Every pointer that does not resolve or misdescribes its target, every index out of step, every state recorded twice, every rule restated wrongly, every file still speaking in the template's voice, every slot value that does not read where it was substituted or was filled twice differently, and every term used in two senses or missing from the project glossary. `governance/roles/documentation_sweep.md` carries the prompt in full, with an item the project fills with its own |
| **Make a consistency sweep of the record.** | After every correction batch, at your direction | The same defect class over the claims, checks, and ledgers instead of the documentation: a fact established in one place and restated wrongly in another. `CHECK_METHODOLOGY.md` §7 |
| **Refute this finding.** | On every finding of any sweep or review, and on every gap the coverage auditor reports, before it is acted on | Stands, refuted with the reason, or narrowed to what survives. `governance/roles/refuter.md`. This is the one that keeps a review honest: in the reviews of this template's own construction, roughly half of what a first reader reported did not survive a second |
| **Referee this draft blind.** | Before a version of a write-up freezes | A structure lens, what the referee could re-derive from the page alone, findings ranked, and what the released document rests on. `governance/roles/blind_referee.md` |
| **Audit this check's coverage.** | Before a check backs an established claim | Every atomic assertion classified: gated, printed only, not computed, mismatched, attested. `governance/roles/coverage_auditor.md` |
| **Probe this check.** | When a check is written, and before it is relied on | The matrix: each named fault applied, and whether the check noticed. `governance/roles/falsifiability_probe.md`, and `tools/falsifiability_probe.py` for a program |
| **Take a structure census of this section.** | At the head of a review, and before a review patches a section | Per sentence: what it is, where its facts are established, every restatement and cross-reference. `governance/roles/structure_census.md` |
| **Check every program against its record.** | After a check program has been run, and before a plan closes on it | Every named value whose printed figure disagrees with part 4 of its record. `tools/check_concordance.py`; it prints the verdicts side by side and decides neither |
| **Read the whole file for what the rebuild left.** | On every rebuild, after the deletion ledger, before the round closes | Seams, dangling and orphaned references, phantoms, echoes, and a live changelog's ledgers against the draft, as candidates for your reading. `tools/check_residue.py`; a section-level comparison cannot see them, which is why the round ends with a reading of the whole file (`CHECK_METHODOLOGY.md` §7) |
| **Give me the deletion ledger for this rebuild.** | On every rebuild of a section, as against a correction | Every cut sentence classified, the net word delta, and every sentence added. `governance/roles/deletion_ledger.md` |
| **Make the strongest case against this conclusion.** | When you are about to rely on something and nothing has argued with it | That case, labeled as that case. `MANIFESTO.md` §17 |
| **Walk me through the plan-closure checklist.** | When an engaged plan's tasks are all done | The checklist item by item against the record, and the verdict the pre-registered criteria give. `governance/reminders.md` |
| **What does this claim rest on, and what of it is unverified?** | Before relying on a claim, and before revisiting one | The dependency tree with each member's register, weaker members flagged. `tools/query_ontology.py` |

Three rules about all of them. **Every finding goes to a refuter before it
is acted on**, including the findings of a sweep you asked for yourself.
**A sweep reports before it edits**: the findings and the files it would
touch, then your direction. And **a role is played by a reader with no
access to the first pass's reasoning**: for an assistant, a fresh session
or a subagent given the prompt and nothing else, or else a human. A role
played by the session that did the work is not opposition, and a subagent
playing one writes no tracked file: it returns its output, and the main
thread records it where the role says.

---

## What to do at each stage

**Picking the work back up**, at the start of every session. Run
`python3 tools/session_brief.py`: it prints the reading order, every plan
with its status and the count engaged, and the reminders the record can
compute. Then open the round's log entry, which is the first act of the
round. Where the harness can run a command at session start, it prints
this for you.

**Starting.** `tools/new_project.py` makes the project from the template
and asks for the sixteen slots; then the research statement and the
keystone. Then the
documentation consistency sweep, which catches what instantiation left
behind. Nothing else yet.

**Opening a line of work.** A plan, drafted and then engaged by you. Its
criteria are fixed before the evidence is seen, which is the whole point;
a plan written after the result is a summary, not a plan.

**Executing.** One task at a time, each producing a check and the claim it
backs. Propose the register with the evidence and stop; assigning it is
yours. Probe every check before you lean on it.

**When something disagrees with what is published.** A row in the tension
ledger, in the same round as the work that found it, with the caution that
survives. `PRECEDENCE.md` says what governs what.

**When the tasks are done.** The closure checklist, then the verdict
against the pre-registered criteria, then your `CLOSED` line. The plan and
everything it owns freeze.

**Opening a write-up.** One living copy of the main write-up at a time, in
the form `{{DELIVERABLE}}` names. Everything it asserts is already in the
record, with its register; the draft says what to read off the evidence
and cites the claim rather than restating its backing. The prose standards
apply to every unfrozen draft under the write-up folder, and the linter
checks the part of them it can see.

**Before a version releases.** The documentation consistency sweep, then
the blind referee, every finding refuted or not, the fixes applied where
the rules allow and brought where they do not, then your `Released` stamp
and the changelog row that goes with it. A released version freezes and is
succeeded rather than corrected: what a later reading asks for goes into
the next version, and the released one is marked superseded when that
version releases.

**After any batch of corrections.** The matching sweep: the record's, or
the documentation's, or both.

**When the project ends.** The documentation consistency sweep a last
time, then a closing note at the root, named CLOSING_NOTE.md, saying why
it closed, on the day it closed. It is the one file named in these
rulebooks that does not exist until it is written, which is why it is
named here in plain text.

---

## Where a rule lives

When you want to know why something is the way it is, this is which file
to open.

| Question | File |
|---|---|
| Who does what, and what may an assistant do on its own? | `MANIFESTO.md` |
| May I edit this file, and when does it freeze? | `DOCUMENT_GENRES.md` |
| How far may this statement be trusted, and what would back it further? | `CHECK_METHODOLOGY.md` |
| Two statements disagree; which governs? | `PRECEDENCE.md` |
| What does this header field mean, and what reads it? | `ONTOLOGY.md` |
| What does this word mean here, and may I rename it? | `GLOSSARY.md` |
| How should this sentence be written? | `evidence_and_reasoning/editorial_standards.md` |
| What fires when, and what does it not decide? | `governance/README.md` |
| What does this tool do, and what does it read? | `tools/README.md` |

---

## Frequently asked questions

**Why is the prompt log immutable?** Because its job is to show what was
believed and asked at each step. A log you can revise is a log that agrees
with the present, which is exactly the thing it exists to check.

**Why must a check be able to fail?** A check that passes whatever the
computation does is not evidence, and re-running it never reveals that.
Planting a fault and confirming the check catches it is the cheapest
available proof that the check is connected to the claim.

**Why is a register assigned by the researcher and not the assistant?**
Because declaring a claim established is the judgment the work exists to
produce. The assistant proposes one with its evidence and stops. This is
also why the four documents `MANIFESTO.md` §12 names, the findings file,
the keystone, the research statement, and the manifesto itself, need your
authorization to change substantively.

**Why is everything advisory?** A mechanism that blocked work would be
routed around within a week, and routing around it would leave no trace.
One that speaks up and records what it said keeps the record honest either
way. The single exception is the privacy scan, where a project has set one up,
because a leak is not recoverable by a later decision; even that is
overridable with the reason in the commit message.

**Why so many small files instead of one document?** Because a claim needs
to be citable, revisitable, and independently frozen, and because the
tools answer questions by reading the fields rather than parsing prose. A
claim inside a long document cannot be pointed at.

**What if a check is expensive to run?** Cost is measurement, never a
gate. Record it, use the run ledger to know when a check is stale, and run
what the claim needs. A claim you cannot afford to check is a claim with a
register lower than you wanted, which is an honest outcome.

**Can two plans be engaged at once?** Yes, and a reminder says so while it
is true, because two engaged plans touching the same material is how
scope drifts. Each plan's *Out of scope* section says which owns what.

**What happens when I am wrong about something already published?** The
same as when you are wrong about anything: correct it forward. The claim
is corrected or superseded, the finding's row says what now holds, the
reversal gets a dated note in the same round, and the key is never reused.

**Does this scale to a project with hundreds of claims?** The indexes and
the queries are what make it scale; the reading does not. Group findings
by line of inquiry once there are more than a handful, and let
`query_ontology.py` answer what you would otherwise re-read.

**What if I want to stop using part of it?** `FORKING.md`. Remove it on
purpose and legibly, rather than leaving it standing unenforced.

## Slots

None. This file describes the system, which is the same in every project;
the values a project chooses are the Slots tables of the files that own
them.

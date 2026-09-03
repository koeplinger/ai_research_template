# Document genres

*Created 2 September 2026; updated 2 September 2026.*

Every artifact in a repository built from this template belongs to exactly
one of three genres, and the genre determines how the artifact may be
changed. This is the rule that keeps documentation from becoming a change
log of itself, where it is followed. The genre checker, `tools/lint_docs.py`,
checks it mechanically and reports what it finds (`MANIFESTO.md` §13); the
section *What the checker verifies* below is the complete list of what it
checks, and everything else in this file is the assistant's duty. This
file is the canonical statement of which artifact is in which genre and
when its genre changes; `MANIFESTO.md` §12 is the canonical statement of
how a correction is made, and this file points to it.

Genre is about how an artifact may *change*. It is not about how far a
statement may be *trusted*: that is the statement's **register**, its
trust level, defined in `CHECK_METHODOLOGY.md`. A frozen artifact can carry
speculation; a current-state artifact can carry established fact.

## Words used here

Beyond the words `MANIFESTO.md` defines: a **plan** is a numbered file
under `evidence_and_reasoning/research_plans/` whose `Status:` header line
holds exactly one of `DRAFT`, `ENGAGED <date>`, or `CLOSED <date>, verdict
<VERDICT>`, the verdict one of CONFIRMED, REFUTED, COMPLETE, or ABANDONED.
A plan is **open** while its status is DRAFT or ENGAGED. An artifact
**owned** by a plan carries the header line `Plan: NNN` (optionally `,
task M`), which resolves to `evidence_and_reasoning/research_plans/NNN_*.md`.
A **maintained** artifact is current state, changed only at the
researcher's direction. A **ledger** is a file that tracks status; the word
*register* is reserved for a statement's trust level
(`CHECK_METHODOLOGY.md`). *Registry* is a different word and keeps its
ordinary sense of a catalogue, as in the reference registry. A **sweep** is a pass over many
documents at once (`MANIFESTO.md` §14). The **public record** is the
published literature, reference works, editions, and published estimates
outside the repository. A **review** is a referee pass, internal or
external, or a reader's report. Dates in headers are written `D Month
YYYY`; dates in filenames are written `YYYY-MM-DD`.

> **Build lens.** While this template is built, two genres are in
> practice: `VISION.md`, changed only at the researcher's direction, and
> everything else, current state. There is no prompt log and nothing
> frozen; `MANIFESTO.md` §12 and §13 say so. The rest of this file
> describes a project built from the template.

---

## 1. Immutable

**The prompt log. Never edited, never rewritten, never deleted.**

| Artifact | |
|---|---|
| the entries under `prompt_logs/` | every prompt, in order, with what was done in response; the folder's `README.md` is an index and is current state |

An entry is **immutable once the researcher has committed it**; its own
status line does not change this. An entry may be edited only while it is
uncommitted, in the round that wrote it. An entry committed before its
round closed is completed by a later entry that points back to it. A
statement in a committed entry that later turns out wrong is corrected in
a later entry, never in the old one, and the log's index carries a pointer
from the wrong entry's row to the entry that corrects it, so a reader who
finds the one finds the other.

---

## 2. Frozen

**A dated record of what was true, known, or decided at a point in time.**

| Artifact | Frozen when |
|---|---|
| a released version of the main write-up, together with what is released with it, {{DELIVERABLE}} | released by the researcher: a `Released <date>` header line on the version, and a row in the changelog |
| a standalone note or write-up under `paper/` not owned by an open plan | on release, the same way |
| a review under `paper/reviews/` not owned by an open plan | on writing |
| a version changelog under `paper/` | on release of the later version |
| **everything a plan owns**: the plan file, its claims, its check records, its check programs and written check procedures, its dated notes, its derived material (transcriptions, collations, extracts, tables, figures), and the write-ups and reviews it produces | **when the plan closes**, with any verdict |
| a dated note not owned by an open plan | on writing |
| a check program or written check procedure not owned by an open plan | when a claim, record, note, or paper cites its path; the checker searches for the path, and the assistant judges the rest |
| imported material under `inherited/` | on import, at its original date (`MANIFESTO.md` §6) |
| `CLOSING_NOTE.md` | on writing: it records why the project was closed, on the day it closed |

`paper/` is the template's name for the deliverable's folder whatever the
deliverable's form: an article, an edition, a working paper with its
replication package, a brief.

**A frozen artifact is corrected only with the researcher's
authorization** (`MANIFESTO.md` §12): the assistant brings the finding and
the proposed wording, and stops. Once authorized, it is corrected as §12
says: in its running text, the updated date the only change to the header,
or marked `superseded by <path>`. The version history carries the
predecessor.

**The repository is current state in every genre.** Frozen artifacts are
dated records of what is *true*, not of how the text got there: a frozen
claim, plan, check record, paper, or the prose of a check states its
content as it now stands and narrates nothing about its earlier wordings,
renamed files, or the round that corrected it. The two exceptions are the
artifacts whose subject *is* history: the prompt log (immutable), and the
dated records under `evidence_and_reasoning/notes/` and `paper/reviews/`
(frozen). Content that refers to time is not narrative and stays: that a
pre-registered prediction was contradicted by what was measured, estimated,
or read; why a deliberate alteration of a check (a mutation,
`CHECK_METHODOLOGY.md`) does or does not make it fail; what a plan measured
and what it did not.

**An addendum appended at the end is not a correction.** In a repository
of any size it is missed, by a human skimming and by an assistant reading,
while the wrong statement stays in the body, where both meet it first.

The header carries pointers and dates; the **record is the body**.
Re-pointing or re-dating a header is bookkeeping. Changing the body is a
correction, and takes the updated date.

### Versioned write-ups

The main write-up has one living copy at a time. A released version is by
default succeeded rather than corrected: a correction the researcher
authorizes goes into the next version, and the released version is marked
`superseded by <path>` when that version releases. It carries the standard
header like every artifact. Changes between versions go in a changelog,
which is a living document until its version releases.

### Maintained artifacts under `paper/`

An artifact under `paper/` that tracks something outside the plan cycle (a
reading companion to an external source, a running comparison table, a
commentary kept current against the project's claims) is listed in the
checker's current-state configuration explicitly and is not frozen at its
filename date. Its header carries the date it was last updated, and it says
what is true now. It is in scope for *Writing for publication*
(`evidence_and_reasoning/editorial_standards.md`) like a live draft.

### Artifacts of an open plan

**Nothing a plan owns freezes until the plan closes.** While a plan is
open, its plan file, claims, check records, checks, and notes are
current-state documents: edited freely in place, and **deleted when they
turn out to be obsolete**.

The reason is what the reader needs at the end. A closed plan presents a
compact, self-consistent set of artifacts from which a human or an
assistant can read the results directly. A trail of "this was found, then
corrected, then re-scoped" is not a result; it is noise that costs the
reader time and invites them to mistake a superseded statement for a live
one. So while the plan is open, **a correction is made by making the
document say the right thing**: no dated addendum, no narration of what it
used to say. The history lives in the prompt log and the version history.
On closure the frozen rules above apply in full.

### A standing reservation

Several frozen claims may depend on a question the project has deferred:
the dating of a manuscript on which three readings rest; the choice of
survey weights on which four estimates rest; the exact characterization of
a structure on which several statements' generality rests. Freezing does
not settle the question, and restricting each claim's scope one at a time
only spreads the deferral across the repository. A **standing reservation**
records the deferred question once, in the plan that will resolve it, and
each affected claim carries a `Reserved <D Month YYYY>, plan NNN` header
line: a comma after the date and never a colon, so the line is a stamp and
not a change narrative. It is bookkeeping and changes no genre; the checker
does nothing with it. What a reservation says, what it licenses, and how a sweep
treats a reserved claim are defined in `CHECK_METHODOLOGY.md`.

---

## Where state is recorded

Status is recorded **once**, in the ledger that owns it, and is never
copied into the artifacts it describes:

| What | Where it lives |
|---|---|
| what the record has **established as findings** | `FINDINGS.md`: current state; what counts as a finding is the researcher's decision |
| the state of the research as a whole | `CURRENT_STATE.md`: the top-level entry point |
| the status of every plan | the `Status:` line of the plan; `evidence_and_reasoning/research_plans/ROADMAP.md` is an index of plans, one line and a link each, whose status column the checker compares with each plan's line |
| what a plan established, and what it left open | that plan's own execution status |
| whether a given artifact is live or frozen | **derived**: live while its owning plan is open, frozen once that plan closes |
| the rules that produce all of the above | `MANIFESTO.md`, this file, `CHECK_METHODOLOGY.md`, `PRECEDENCE.md` |

An artifact **names its owning plan** in its header, `Plan: NNN`, and stops
there. That pointer is navigation. A copy of the plan's status is a second
ledger, and a second ledger drifts out of step with the first; a copy of a
repository-wide rule ("frozen on its closure") is the rulebook leaking into
a leaf, where it will be read as though this one artifact were special.
The checker reads the `Plan:` line, opens the plan file, and reads its
`Status:` line; nothing else.

The same applies to summaries: an aspect is summarized once, at the
altitude that owns it, and referred to from below by link.

---

## 3. Current state

**Describes what IS. Forward-evolving. Edited freely, in place.**

| Artifact | |
|---|---|
| `MANIFESTO.md` | the operating rules; substantive change requires the researcher's authorization |
| `DOCUMENT_GENRES.md` | this file |
| `PRECEDENCE.md` | what governs when sources disagree |
| `CHECK_METHODOLOGY.md` | how a check is written; where register is defined |
| `ONTOLOGY.md` | the predicates |
| `CURRENT_STATE.md` | the state of the research |
| `FINDINGS.md` | what the record has established; adding, removing, or substantially changing a finding requires the researcher's authorization |
| the session-onboarding file | what every assistant session must know before it works |
| every indexing `README.md` | what is in this folder, and what each file does |
| `evidence_and_reasoning/research_statement.md` | the question as posed; maintained, and changed only on a significant deviation of the question |
| `evidence_and_reasoning/problem_statement.md` | the keystone: the researcher's thesis, stated as questions or hypotheses precise enough that evidence could count against them, from which plans are drawn; maintained; in the SPECULATIVE register, it orders the reading and trumps nothing. Every plan states which of its hypotheses it serves, or why it serves none; a plan opened while no keystone is designated says so |
| `evidence_and_reasoning/public_record_tensions.md` | the tension ledger: one row per point where a result of the project diverges from the public record. The assistant brings the row in the same round as the work that creates it; the row enters at the researcher's direction (`PRECEDENCE.md`); maintained |
| `evidence_and_reasoning/research_result.md` | the condensed summary of `FINDINGS.md`, at the altitude of the write-up |
| `evidence_and_reasoning/terminology.md` | the glossary |
| `evidence_and_reasoning/editorial_standards.md` | the prose standards, including the recorded voice |
| `evidence_and_reasoning/references/**` | the reference registry |
| `evidence_and_reasoning/research_plans/ROADMAP.md` | the plan index |
| `tools/**` | the mechanical checks; their docstrings carry the standard header |
| `inherited/README.md`, `source_documents/README.md` | the import ledger; the source index |
| `LICENSE.md`, `LICENSE-CODE` | the licenses |

**Every durable artifact opens with the same header line**, `Created D
Month YYYY; updated D Month YYYY`, italicized in a document and in the
leading comment of a program, so a reader knows how current it is. The
date is the only thing a current-state artifact says about its own
history. Non-prose files (data, images, rendered output, transcription
files) carry no header; they are dated by the plan that owns them or the
index that lists them. A tracked path that matches no genre in the
checker's configuration is reported as unresolved; no default is assumed.

**The version history is the history of these files.** They carry no
history of their own.

### Narration of the text's own past

A current-state document never narrates how its own text came to be. What
must never appear:

- A dated correction notice: *"(Corrected <date>; earlier versions of this
  file said ...)"*, *"Correction of record"*.
- A settlement date: *"settled <date>"*, *"was open through version <N>"*,
  *"now proved"*, *"now confirmed"*, *"now attested"*, *"now replicated"*,
  *"SETTLED (was OPEN)"*.
- A supersession narrative: *"this supersedes the earlier statement that
  ..."*.
- A change-history footer: *"Last updated: <date> (new entries: ...;
  previous update: ...)"*. The standard header is the whole of it.
- **A sentence whose subject is a change in the text** rather than a fact,
  whether or not a date is attached: *"previously read"*, *"no longer
  holds"*, *"used to say"*, *"was found to be"* (of the text), *"before the
  correction"*, *"since corrected"*, *"an artifact of the earlier draft"*,
  *"as of <date>"* (of the text). *"Previously there were two obstacles,
  now there is one"* instead of *"there is one obstacle"*.
- **Process narrative about the document's own production**: which prompt,
  review, agent, or run produced a wording, or a header block that recounts
  successive revisions. The section states the rule; its provenance is in
  the log.
- **Rename and symbol history**: *"renamed from ..."*, *"we now use X
  instead of Y"*. Name the current symbol, path, or range and stop.
- **An end-addendum whose only content is that an edit happened.** If the
  body is right the addendum says nothing; if the body is wrong, fix the
  body.
- A status block or section restating another document's content, for
  example the state of the write-up inside a folder index.
- A section that is not about what the document is about.

**A statement about the subject of the research is content, not
narrative, whatever words it uses**: a source's revisions, a dataset's
release vintage, an institution's past, a published correction, an
instrument's artifact. So is an internal cross-reference (*"established in
the earlier sections"*), a proper noun (*"the corrected edition"*), the
dated provenance of a directive (*"recorded <date>, prompt NNN"*), and a
present-tense description of an operation a program performs.

If a current-state document said something that is now wrong, **just make
it say the right thing.** Do not announce the change in the document. The
reason goes where `MANIFESTO.md` §12 puts it, the round's log entry or the
commit message, and a reversal of a finding also gets a dated note in the
same round, so that what changed and why stays readable.

### Dated records

Two families of document exist *in order to* be historical, and the rules
above do not apply to them:

- `evidence_and_reasoning/notes/<YYYY-MM-DD>_*.md`: a dated working note;
  what a sweep, an audit, or a line of reasoning found on that day.
- `paper/reviews/<YYYY-MM-DD>_*.md`: a dated review; what a referee pass
  found, against the document as it stood. The folder's `README.md` is an
  index, and is current state like every other index.

Their subject *is* an event, and stripping the history from them would
leave nothing. They are the counterpart of the prompt log: the place a
reader goes for how a result was reached. This is what lets a
current-state document drop every trace of a correction, provided the
reason was recorded where §12 puts it.

The exemption is by path, not by plan: a dated note owned by an *open* plan
is still a dated record. The exemption covers the *events they record*,
not their own editing history: a dated note or review carries the standard
header and nothing else about itself. What the sweep, audit, or referee
pass found on its day stays; how the note's own sentences came to read as
they do is the version history's and the prompt log's.

**A plan's `## Execution status` section is a progress ledger**, and is
exempt on the same ground: it records which task was done and when, which
is exactly what lets a later reader, or a later session, resume the plan
from the repository alone. The exemption stops there. The plan's **body**,
its aspect, its directives, its task descriptions, states what is, like
any other current-state prose, and a task must not motivate itself by
narrating the incident that prompted it. The ledger carries one obligation
in return: **it must be complete.** A ledger that lists only finished
tasks, while unstarted ones live in the body, is worse than none; it tells
the reader the plan is done.

---

## Indexes and cross-references are kept on purpose

A project built from this template keeps indexes, ledgers, and
cross-references that point at information held elsewhere. That is not
redundancy to be eliminated. It serves two readers at once: a human, who
needs the material to be navigable, and an assistant, for which a good
index is the difference between reading one file and reading the whole
repository.

The line runs between **navigation** and **duplication**:

- *Navigation*: a one-line index entry with a link, a pointer to the
  owning plan, a cross-reference to the claim that settles a question.
  Keep it, and keep it current.
- *Duplication*: a second copy of a status, a rule, or another document's
  paragraph, living where it will drift. Strip it, and leave a link.

A consistency sweep therefore adds pointers and removes copies: it may
bring an index up to date; it must not add a second ledger of something
already tracked elsewhere, and it must not add content of the wrong genre.

---

## What the checker verifies

The complete list of what `tools/lint_docs.py` checks for this file, each
stated so that it can be implemented; the editorial checks are listed in
`evidence_and_reasoning/editorial_standards.md`. A finding is reported to
the researcher with its output (`MANIFESTO.md` §13).

1. **Header.** Every durable artifact, by the configured path patterns and
   excluding non-prose files, opens with a line matching `Created D Month
   YYYY; updated D Month YYYY`, and nothing follows the second date on that
   line.
2. **Immutable.** No committed file under `prompt_logs/`, other than its
   `README.md`, differs from its committed version or is deleted.
3. **Frozen.** For a frozen artifact whose body differs from its committed
   version, the updated date on the header line has changed. A change
   confined to the header (pointers, dates, `Released`, `Reserved`,
   `superseded by`) is free.
4. **Genre resolution.** Every tracked path resolves to a genre: the
   configured path patterns assign a default; a `Plan: NNN` header line
   overrides it to current state while that plan's `Status:` is DRAFT or
   ENGAGED and to frozen when it is CLOSED; a path resolving to nothing is
   reported.
5. **Narrative.** On current-state paths, outside the two dated-record
   patterns and outside any `## Execution status` section, the following
   are matched case-insensitively as whole phrases, skipping text inside
   backticks and the italicized examples in this file and the editorial
   standards: *previously* followed by *read*, *said*, *stated*,
   *reported*, or *recorded*; *used to* followed by *read*, *say*,
   *state*, or *be*; *no longer* followed by *holds*, *records*, *reads*,
   *says*, or *states*; *was found to* followed by *have* or *be*; *before
   the correction*; *since corrected*; *as of* followed by a date; *earlier
   versions of this file*; *supersedes the earlier*; *Correction of
   record*; *Last updated:* followed by an opening parenthesis; and any of
   *Corrected*, *Updated*, *Extended*, *Hardened*, *Narrowed*, *Reserved*
   followed by a date and a colon, in every genre.
6. **Ledger.** The status column of
   `evidence_and_reasoning/research_plans/ROADMAP.md` agrees with each plan's
   `Status:` line.
7. **Paths.** Every repository path named in a current-state document
   exists.
8. **Index.** Every file in a directory that has an indexing `README.md`
   appears in it.

The judgment items above (a sentence whose subject is a change; a section
off its document's subject; the reason for a correction recorded where it
belongs) are the assistant's duty.

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{DELIVERABLE}}` | The publishable deliverable: its form, and what is released with a version of it (§2) | an article: its typeset source and rendered copy; an empirical paper: the rendered copy, the estimation code, the cleaned extract or its locator, and the run logs; a critical edition: the edited text, its apparatus, and the transcription files; a brief: the filed document |

# Editorial standards

*Created 2 September 2026; updated 2 September 2026.*

The five standards, the conventions, and the corollaries below govern every
prose change to every **durable artifact** (`MANIFESTO.md`, *Words used
throughout*: every tracked document, every written check procedure, and
the docstrings and comments of every tracked program; scratch and
non-prose files out of scope). Two carve-outs: the verbatim prompt inside a
log entry is never edited; and the standards apply to the parts of a log
entry the assistant writes while the entry is uncommitted, since a
committed entry is immutable (`MANIFESTO.md` §8).

The intended reader of any of these artifacts is an expert in the field,
or a future investigator, human or assistant, who must reconstruct what
was done and why. Their time is to be respected: every sentence earns its
place, and the logic is followable on a first reading.

The examples in this file are written with *we* and in English; read them
with the project's own conventions.

> **Build lens.** The five standards, the conventions, and the corollaries
> apply to every document of the template. The build's house conventions
> are US spelling and no em-dashes (`VISION.md` keeps its own dash
> convention); no slot is filled by that. *Writing for publication* is
> shipped, not applied.

## The five standards

1. **Lead with the claim, then develop.** State the finding or claim
   first; build the apparatus that supports it afterwards. A paragraph
   announces what it is about before it elaborates.

2. **Introduce one thing at a time, each before what depends on it.**
   Never use a term before it is defined. Each sentence brings in at most
   one new object and otherwise uses only objects the reader already has.
   Do not break the thread to visit a side topic.

3. **Cut every redundancy.** Say each thing once, in its proper place. If a
   fact is stated where it belongs, do not restate it elsewhere. A pointer
   or a one-line index entry is navigation, not a restatement
   (`DOCUMENT_GENRES.md`, *Indexes and cross-references are kept on
   purpose*).

4. **One consistent vocabulary.** Fixed conventions, used the same way
   throughout. A term the glossary
   (`evidence_and_reasoning/terminology.md`) defines is used in
   exactly that sense, and two things the discipline keeps apart stay
   apart in the prose (*correlation* and *causation*; *transcription* and
   *translation*; a definition and a theorem). Spelling, punctuation, and
   naming follow the conventions below.

5. **Precision over good-sounding vagueness.** Define terms; do not
   over-claim; state plainly what is open. A sentence that sounds
   substantial but asserts nothing checkable is cut or made concrete.

## Conventions

The project's choices, recorded once and used throughout.

| Convention | This project's choice |
|---|---|
| Language and spelling | {{SPELLING}}. Quoted titles and verbatim quotations keep their source spelling. |
| Dashes | {{DASH_CONVENTION}}. |
| The paper's agent | {{PAPER_PRONOUN}}, used consistently. It performs the paper's acts (*we fix*, *this article argues*, *I measure*), not bare imperatives and not agentless passives where the paper is the agent. |
| Adequate references | {{REFERENCE_ADEQUACY}}: which kind of reference (`MANIFESTO.md` §2) is adequate for which kind of claim. |
| The deliverable | {{DELIVERABLE}}: the form of the write-up, including what its venue expects of a title, and what is released with it. |
| Names | The project's standard name for a thing, chosen once and used throughout. Where the source's own term is itself the object of study, or where its equivalence to a modern name is a claim the project has not established, the source's term is the standard name and the modern gloss is an annotation. Either way the mapping, or the fact that none is asserted, is recorded in the glossary. Frozen artifacts keep their own wording. |

## Corollaries

- Keep at most two forward references outside the introduction of any
  document.
- An introduction (where one exists) reads as a compressed version of the
  document.
- **Write in the current state.** Prose says what is true now and never
  narrates how the text got there; `DOCUMENT_GENRES.md` §3 lists what that
  excludes, what is content rather than narrative, and which artifacts are
  exempt because their subject is history. Where provenance needs a date,
  the standard header is the whole of it.
- **Body headings name subjects, not verdicts**, and carry no rhetorical
  tag line. A heading does not announce a result or pose a question the
  paragraph then answers. Where a point is substantial enough to need
  marking, start a paragraph or a subsection; where it is not, state it in
  the prose. The title of a write-up follows its venue's convention, per
  {{DELIVERABLE}}.
- **Never assert what the project could have checked and did not.**
  Phrases that assert an equivalence, an immateriality, or a consensus the
  project could have verified are cut or replaced by the verification: in
  mathematics *without loss of generality*, *clearly*, *it is easy to
  see*, *it follows immediately*; in empirical work *robust to*,
  *representative*, *typical*; in textual and historical work *as is well
  known*, *it is well established that*, *scholars agree*, *the sources
  are silent*. Where a choice of frame, sample, edition, or labeling really
  is immaterial, say which relabeling or which argument carries the one
  case to the other and cite the check that verifies it; where it has not
  been verified, say that instead.
- **Use the project's standard names**, per the Conventions.

## Writing for publication

*Scope: every artifact under `paper/` that is not frozen (`DOCUMENT_GENRES.md`
§2 says when each freezes): drafts owned by an open plan, unreleased
standalone notes and changelogs, and maintained companions. Frozen
`paper/` artifacts keep their own wording: a released version is succeeded
by the next, and any other frozen artifact is corrected only under
`MANIFESTO.md` §12. The mechanical part of this section is listed under
*What is checked mechanically* below.*

The intended reader checks the evidence (the displays, that is, the
displayed equations, tables, figures, quotations, transcriptions, or notes
that carry the result) before accepting the prose, and in many disciplines
scans it first. **A result that exists only in prose does not exist for
that reader.** The reader must be able to see it working in the evidence,
then recognize why it is relevant, and only then accept it. The standard
is *gentle in each step, comprehensive over the material*: each move small
enough to follow without effort, the sequence complete enough to leave
nothing owed. The form of the write-up (whether it has a results section,
a discussion, an appendix, or notes in their place) is {{DELIVERABLE}}.

### Evidence

- **Every load-bearing claim carries its evidence on the page or in the
  notes.** If a section says two sources disagree, both passages are
  quoted, or cited to the folio and quoted where the wording is what is at
  issue; if it says an estimate is robust, the table across specifications
  is on the page; if it says a structure is a product of two others, the
  rule that combines them is on the page.
- **Tie the general to the concrete.** A general statement may accompany a
  concrete instance; it may not replace it.
- **Show the step.** Where a consequence follows from what is displayed in
  one move, that move is written out rather than asserted.
- **Depth goes to an appendix, or to the notes, not out of the paper.** A
  thematically isolated aspect is described generally in the prose, which
  points to the appendix or note that carries its evidence.

### Prose

- **Describe, and stop.** State what a thing is; do not argue for its
  importance. A claim original to the project is marked as such with its
  bound (*to our knowledge*), per `MANIFESTO.md` §2, and no more; where the
  venue expects a contribution statement, it names what this work does and
  what the nearest prior work did, without adjectives, and does not
  adjudicate priority, which is the researcher's decision and is recorded
  in the claims.
- **No advocacy.** Not *remarkable*, not *striking*, not *beautiful*, not
  *the point at issue*. The reader decides what is remarkable.

### Flow of an argument

A paper is read in one direction, once. A section that develops a concept
along two cases carries a single relation between them, and the prose
follows that relation from beginning to end.

- **Name the relation, and keep it.** Two cases that *contrast* are held
  apart and shown side by side; two that are *two views of one thing* (two
  readings of one source; two estimators of one quantity; two descriptions
  of one structure) are shown passing from one view into the other. A
  section does not alternate between the two relations, and neither does a
  pair of neighboring sections.
- **One case, one presentation.** A case already presented in one form
  (one notation, one specification, one translation) is not presented
  again in another form later in the same argument. The second form goes
  to a note or a check record under `evidence_and_reasoning/`, not into
  the paper.
- **Define before use.** A term or a symbol arrives before the sentence
  that leans on it, so that no forward reference is load-bearing. Backward
  references to what the reader already has are free.
- **One fact, one home.** A fact is stated once, at the point where it is
  established, and referenced from anywhere else that needs it. A review
  that wants a qualification somewhere *moves* it; it does not add a
  second copy. Two consequences follow. A correction **replaces** within
  the paragraph it lands in rather than appending a clause to it, since
  appending is what compounds. And a cross-reference earns its place only
  where a reader must actually look something up: a fact established a
  paragraph earlier is not re-cited, and a reference must name something
  the target actually says.
- **The summary inherits.** A results summary repeats claims the body
  establishes. Cutting a claim from the body cuts it from the summary in
  the same round, or the summary asserts what the paper no longer shows.

### Writing a discussion

A results section does not opine. A discussion is where the author's
reading belongs, and a reading has a holder: the paper's agent, per the
Conventions.

- **The agent holds a position**: *we take*, *we look for*, *we would
  want*, *we do not settle*. Not *what motivates the search is*, and not
  *one may then ask*. An agentless motive is a motive with nobody behind
  it.
- **Say the want once, and flatly.** *We would want X* rather than *we
  hope X might one day*. A doubled hedge reads as a wish the author is
  embarrassed by.
- **Concede in the flow.** Where a point is granted before it is
  qualified, the concession sits inside the sentence after its object:
  *the date is secure, yes, but the attribution rests on the editor's
  reading*; *the estimate survives the placebo test, yes, but the
  identifying assumption is borrowed*. Not *while the date is secure, the
  attribution rests on the editor's reading*.
- **A verdict lands short.** A discussion whose sentences all run one
  length is arguing rather than concluding; each paragraph ends on a
  sentence of one clause.
- **The register** (the statement's trust level, `CHECK_METHODOLOGY.md`)
  **is declared once**, at the head of the section. Individual paragraphs
  do not re-announce that they are speculation.

### Voice

{{VOICE}}: the project's voice is read off the researcher's own prior
writing where it exists, and otherwise chosen and stated by the
researcher; it is recorded here as a list of rules a proposed sentence can
be tested against. Whatever the rules are, they serve four goals, and a
recorded voice is checked against them:

1. **The reader can redo everything the access conditions allow**
   (recompute, re-read, or re-run), and what they cannot redo is stated as
   such with its locator (`MANIFESTO.md` §6). Conventions pinned; steps
   written out; every claimed equivalence (a relabeling, a recoding, a
   collation) exhibited rather than asserted.
2. **Hypotheses, choices, and consequences stay separable.** What is
   assumed, what is a convention the author chose, and what follows are
   never in the same undifferentiated sentence.
3. **Priority is precise and never polemical.** Cite the specific content,
   name the specific limitation, endorse nothing.
4. **The evidence carries the argument**, and the prose says what to read
   off it.

An example voice record, as a model of the form; the illustrations pair a
mathematical sentence with a historical one. Replace the record with your
own:

- **Name the object in the subject position.** "Complex numbers are a
  two-dimensional algebra over the reals." "The 1832 board of health was a
  municipal body." Not "The algebra of [2] is two-dimensional." A citation
  rides inside the sentence; it never stands in for the thing being
  defined.
- **Define constructively, in the order a reader would build it.** One
  step per sentence, each with its display, its quotation, or its table
  where it has one.
- **State the positive fact first.** Not *is not decoration*, not *was not
  merely a formality*. Where a contrast is worth drawing it follows the
  fact, plainly.
- **Explain a name by its origin, once**, and say which name this document
  uses.
- **State the fence, then point past it.** "We do not develop either
  further than this subject needs; both are treated generally elsewhere."
  A scope limit belongs in the flow, without apology.
- **Attribute by name and date**, in the form the discipline's citation
  convention takes. An independent contribution is credited explicitly,
  including where the paper shows another's result to be a case of its
  own.
- **A bound is part of the claim, not an afterthought.** *To our
  knowledge*; *we found no grounds for excluding*; *the surviving registers
  do not record*.
- **Italics define; they do not insist.**
- **No commentary on the paper's rhetoric.** Not *the trade the paper
  turns on*, not *the reader is asked to keep it in view*. The paper's
  acts (*we fix*, *we do not develop*) and its one register declaration
  are not commentary.
- **Headings are short noun phrases without a leading article.**

## What is checked mechanically

The genre checker (`tools/lint_docs.py`) checks the following and reports
what it finds (`MANIFESTO.md` §13); everything else in this file is the
assistant's duty.

1. On every durable artifact: the dash convention, as the character rule
   {{DASH_CONVENTION}} names; the spelling variant, by a word list of the
   common variants for {{SPELLING}}, skipping quoted text.
2. On every unfrozen artifact under `paper/`: the phrases *without loss of
   generality*, *clearly*, *it is easy to see*, *it follows immediately*,
   *as is well known*, *it is well established that*, *scholars agree*,
   *robust to*, and the words *remarkable*, *striking*, *beautiful*, *the
   point at issue*, matched case-insensitively as whole phrases, skipping
   quoted text; and body headings that begin with an article or end in a
   question mark.
3. The current-state narrative check of `DOCUMENT_GENRES.md`, on the scope
   stated there.

## How to apply

Check every prose change against the five standards, the conventions, and
the corollaries; and every change to an unfrozen `paper/` artifact against
*Writing for publication*, including its *Voice*, as well.

A practical test for standard 2: read the paragraph as a first-time reader
and, at each sentence, ask: *do I have every term used here, and is this
sentence still on the topic the paragraph announced?* If the answer is no,
the logical order is wrong, or a side topic has intruded.

A practical test for standard 5: for each sentence, ask what would change
for the reader if it were deleted. A sentence whose deletion costs the
reader nothing checkable is vague; cut it or make it concrete.

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{SPELLING}}` | The language of project prose and its spelling variant | US English (*-ize*, *center*, *labeled*); UK English (*-ise*, *centre*, *labelled*); German, post-1996 orthography |
| `{{DASH_CONVENTION}}` | How asides and ranges are punctuated | no em-dashes, an aside moves to a comma, a colon, parentheses, or a second sentence, en-dashes for name joins and numeric ranges; spaced em-dashes for asides |
| `{{PAPER_PRONOUN}}` | The agent that performs the paper's acts | *we*, also for a single author, as in mathematics and physics; *I* for a single author, as in history and law; the document as agent (*this article argues*), with no first-person pronoun, as some humanities venues require |
| `{{REFERENCE_ADEQUACY}}` | Which kind of reference is adequate for which kind of claim (`MANIFESTO.md` §2) | a journal article or monograph for any specialist claim, an archival document by shelfmark for any claim about what a source says, a dataset by release for any figure (history of medicine); a DOI-bearing source for every empirical claim, encyclopedic sources for background only (empirical economics) |
| `{{DELIVERABLE}}` | The form of the write-up, its title convention, and what is released with it (also `DOCUMENT_GENRES.md` §2) | an article with results, discussion, and an appendix, descriptive title (mathematics); an empirical paper with a question or declarative title as the journal expects, and a replication package (economics); a monograph chapter with footnotes and no appendix (history) |
| `{{VOICE}}` | The recorded voice rules for unfrozen drafts | the example record above (mathematics and history, mixed); a record read off a dissertation chapter and a first article; a house style the researcher adopts and names |

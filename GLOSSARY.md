# Glossary: the words this methodology uses in its own sense

*Created 8 September 2026; updated 19 November 2026.*

This file defines the method's own vocabulary. It exists because a
methodology that means to serve every discipline has to name its parts,
and every name it could choose is already taken by somebody's field. The
table below says what each word means here and what it will be mistaken
for; a later section says which words a project may rename, and how.

A project's own subject-matter terms are not defined here. They go in
`evidence_and_reasoning/terminology.md`, which is the project's glossary
(`MANIFESTO.md` §9). This file is the method's, and it is the same in
every project.

Four of the rulebooks open with the words they own (`MANIFESTO.md`,
*Words used throughout*; `DOCUMENT_GENRES.md`, `CHECK_METHODOLOGY.md`,
and `PRECEDENCE.md`, *Words used here*). Those sections define the words
for the argument they are making; this file gathers them in one place,
adds the collisions, and is where a reader who meets an unfamiliar word
should look first.

## The method's words

| Word | In this methodology | Not to be confused with |
|---|---|---|
| **register** | how far a statement may be trusted: one of six levels a claim carries (`CHECK_METHODOLOGY.md` §1) | the primary source itself, in archival and administrative work (an admission register, a parish register, register data); a public record in law; a level of formality in linguistics; an entry in a catalogue |
| **registry** | the project's catalogue of references, one entry per work (`evidence_and_reasoning/references/`); a work *registered* is entered there, as the `registered` predicate records (`ONTOLOGY.md` §2.1) | a public register of companies, land, or trials; a container registry; a claim *registered* `VERIFIED`, which carries that register (`CHECK_METHODOLOGY.md` §1) |
| **claim** | one statement the project makes, filed as its own document with a register and a kind | a cause of action in law; a patent claim; an insurance claim; a claim in the everyday sense, any statement the prose makes, which carries no register (`CHECK_METHODOLOGY.md`, *Words used here*), as `MANIFESTO.md` §2 and the editorial standards' *Writing for publication* also use the word |
| **check** | one self-contained investigation of one claim, question, or construction, with a printed or written verdict (`CHECK_METHODOLOGY.md`) | a mechanical check a tool makes of the repository, such as the round check, the concordance check, or an ontology check, which reports findings and verifies no claim; a robustness check in empirical work, which is a specification and not a verification unit; a cheque |
| **gated** | of a statement: a check stands behind it that would fail if the statement were false | flow-cytometry gating; a gating network in machine learning; "blocked"; the round check's gates, the checks it runs, its gate on a build among them, each of which reports and decides nothing; the findings gate, a reminder the session brief prints (`governance/reminders.md`) |
| **verdict** | the word a check reaches, from the vocabulary its claim's kind fixes; five of those words, *reproduced*, *replicated*, *identified as stated*, *compatible*, and *inconclusive*, are fixed in senses a discipline may not expect (`CHECK_METHODOLOGY.md`, *Words used here*) | a plan's verdict, the word its `CLOSED` status line carries, from a vocabulary of its own (`DOCUMENT_GENRES.md`, *Words used here*): a plan `CONFIRMED` held its hypothesis, where a documentary check's *confirmed* found that a source says it; a refuter's verdict on a finding, *stands*, *refuted*, or *narrowed* (`governance/roles/refuter.md`); what a jury returns; a court gives judgment, not a verdict |
| **finding** | a statement the record has established, entered in `FINDINGS.md` at the researcher's decision | a finding of a tool, a sweep, or a review (*The finding tags*, below): a possible defect it reports, which establishes nothing and is never a row of the findings file; a finding of fact, as against a conclusion of law; a finding in the sense of a search result |
| **mutation** | a named alteration to something a claim depends on, planted to show that a check can fail (`CHECK_METHODOLOGY.md` §5) | a heritable change in a DNA sequence, which is a subject of study and not a method term |
| **probe** | the tool that applies each mutation and reports whether the check caught it | a labeled nucleic acid or antibody; a probing classifier |
| **construct** | in a check program, the function that builds the object under test; part 2 of a check record | an engineered DNA construct; a theoretical construct in the social sciences |
| **frame** | what fixes the quantities a claim states: the units, encoding, edition, calendar, or sample definition (`Frame:`) | a sampling frame; a reading frame; a data frame or a stack frame |
| **instrument** | the tool or procedure of record a second reader returns to (`Instrument:`) | an instrumental variable; a physical laboratory instrument, which is equipment; a legal instrument, which is a document |
| **locus** | where in a source a citation points: the page, folio, section, paragraph, table, or variable a project fixes | a position on a chromosome |
| **collation** | reading a statement against the source of record, word by word, to establish what the source says | gathering or combining; a batching function; checking a citation, which is one kind of collation |
| **reading** | of a question or a duty: one no tool can decide, left to a reader and, under the consistency sweep, the assistant's (`ONTOLOGY.md` §2) | an interpretation, the sense in which an interpretive claim states a reading (`CHECK_METHODOLOGY.md` §2); a variant reading, what one witness has at a place; a tool's reading of the fields, which is parsing |
| **attested** | the register of a claim about what a source says, making no claim that what it says is true | witnessed, as a signature on a deed |
| **witness** | one surviving record of a work, where a work survives in several | a person who gives evidence |
| **concordance** | agreement between what a check program printed and what its record states | an alphabetical index of words; a crosswalk between classification schemes; agreement between twins |
| **sweep** | a pass over many documents at once, which reports before anything is edited (`MANIFESTO.md` §14); the method names two, each a reading pass for statements that disagree: over the record (`CHECK_METHODOLOGY.md` §7) and over the documentation (`governance/roles/documentation_sweep.md`) | a hyperparameter sweep. Never write bare *the sweep* where more than one could be meant |
| **residue** | what a rebuild or a correction batch left behind in a live draft, such as a reference to something no longer there | a chemical residue; an amino-acid residue |
| **authority** | which statement of this repository governs when two disagree (`PRECEDENCE.md`) | a cited case or statute, and the hierarchy of legal sources. `PRECEDENCE.md` orders this project's own statements, and says nothing about any discipline's order of sources |
| **the public record**, also *the published literature* | what is published outside this repository: articles, editions, reference works, published estimates (`PRECEDENCE.md`, *Words used here*), at tier 4 where it is neither collated nor registered here. It names that tier, heads a column of the tension ledger, and names that ledger's file | the public record in the *legal* sense, which is the court record and the reporters; those are sources of record here, at tier 2, and a divergence from one is an ordinary tension row |
| **standing** | of a registry entry: what searching for later or contrary material found, and when; or that no search was made, and why | *locus standi*, the right to bring a claim |
| **plan** | the unit of work: an aspect isolated, with criteria fixed before execution | a project plan or a schedule |
| **round** | the unit of time: one prompt, the work it asks for, and the entry that logs it | a round of funding; a review round |
| **genre** | how an artifact may change, one of three (`DOCUMENT_GENRES.md`): *immutable*, never edited once committed; *frozen*, a dated record, corrected only with the researcher's authorization; *current-state*, a description of what is, corrected in place | a literary or musical genre; a genre of writing, such as the article or the edition, which here is the deliverable's form (`DOCUMENT_GENRES.md`, *Slots*); a statement's *register*, which is how far it may be trusted |
| **ruling** | the researcher's decision on a matter put to them, recorded in the researcher's words in the log entry of the round that gave it; a ruled matter is not raised again without evidence the ruling did not have (`MANIFESTO.md` §16) | a court's or a regulator's ruling, which binds parties; a *standing direction*, which governs later rounds |
| **standing direction** | a direction from the researcher that governs later rounds, written down in the round it is given and in the researcher's words: in the file that owns its subject where it sets a value or amends a rule, and otherwise, with the prompt that gave it, in `ONBOARDING.md`, *Standing directions* (`MANIFESTO.md`, opening, on standing directions) | a reminder, which `governance/reminders.md` calls a standing instruction and which is the method's, not the researcher's; a memory or preference held on the assistant's side, which carries at most a pointer here; a standing order in the parliamentary or the banking sense |
| **slot** | a value a project fills once, written `{{LIKE_THIS}}` and listed in a Slots table | a time slot; a slot in a schema |
| **altitude** | the level of detail a statement belongs at, so that a summary does not carry a body's precision | flight altitude; nothing else here |
| **keystone** | the project's thesis, in `evidence_and_reasoning/problem_statement.md`: what the rest is built to bear on | a keystone species |
| **harness** | the program that runs the assistant and can run a command before or after each reply | a test harness in the general sense |
| **hook** | a command the harness runs at a named moment, such as after each reply | a git hook, a script git runs at a commit, which `tools/install_hooks.sh` installs in each clone because git does not clone it; a hook in a web framework; a hook in fishing or writing |
| **main thread** | the assistant session the researcher is talking to, which carries the conversation and the researcher's standing directions, starts any subagent, and makes every edit to a document (`MANIFESTO.md` §14) | a thread of execution in a program; a discussion thread |
| **subagent** | any further session the main thread starts, given one task: it may read, search, compute, run programs, and report, and writes nothing into the working tree (`MANIFESTO.md` §14) | an agent in the economic sense; a blind reader, which a subagent is only when it is given nothing of the main thread's reasoning, as one playing an opposition role is (`governance/roles/README.md`) |
| **template** | the methodology template: the repository a project is made from, whose rulebooks, guide, tools, and artifact templates the project keeps as its own; a sentence that still describes it rather than the project speaks in *the template's voice* (`governance/roles/documentation_sweep.md`, item 5) | an *artifact template*, a file whose name begins with `_template`, copied to start one artifact of its kind and named with that kind where both could be meant (the entry template, the plan template, the check-program template); a template in the software sense; a write-up's *voice*, which is its style (`evidence_and_reasoning/editorial_standards.md`, *Voice*) |
| **build lens** | a passage of the template's documents addressed to its own construction, stripped when a project is instantiated | a lens in optics; a build in the software sense |
| **assertion** | one independently falsifiable statement inside a claim; what a check gates, one at a time | an assertion in the programming sense, which is one way to write one |
| **check record** | the dated entry recording one execution of a check: the date, who ran it, the verdict, and the second pass | the check itself, which is the investigation; a record in the archival sense |
| **second pass** | an independent route to the same result, taken by another party or another method, and recorded beside the first | a second reading; a second attempt at the same route, which is not one |
| **instrument of record** | the tool or procedure a second reader returns to in order to repeat a verification, named precisely enough that they reach the same thing | see *instrument* above |
| **docket** | a plan's list of items deferred to its closure | a court's docket; a ticket queue |
| **standing reservation** | a question the project has deliberately deferred, recorded once, with the assumption the reserved material is read under, in the plan that will resolve it; each claim whose scope depends on it carries a `Reserved` stamp naming that plan (`CHECK_METHODOLOGY.md` §6) | the *standing* of a registry entry and a *standing direction*, both above; a reservation in the booking or the legal sense |
| **structure lens** | the pass a review takes before any sentence-level finding: per section, the inventory, the order, and where each fact is established | a lens in optics; the *build lens* above, which is a different thing |
| **coverage** | of a search or a design: what it could have found, established and stated, so that finding nothing means something; of a check: which of its assertions it gates (`governance/roles/coverage_auditor.md`) | test coverage in the software sense, which is a different measure; *mutation coverage*, that every check names mutations it must fail under (`CHECK_METHODOLOGY.md`, *What is checked mechanically*, item 3) |
| **blast radius** | every place a claim is relied on, which is what moves if the claim moves | anything explosive |
| **derived**, of an input | forced by prior structure, as against *imposed* (a choice the project made) and *conjectured* (assumed and not established), the three kinds every input of a check is classified into (`CHECK_METHODOLOGY.md` §4) | the `DERIVED` register, which is a trust level and not an input kind; *derived material*, which is what a plan made from a source; a *derived* predicate or state, such as an artifact's genre, computed from other fields and never written down (`ONTOLOGY.md` §3); a derived cell line, a derived allele, a derived variable |
| **imposed** | of an input: a choice the project made, which it states as a choice rather than as a fact | imposed in the sense of forced from outside |
| **conjectured** | of an input: assumed and not established, so that what rests on it is no stronger | a conjecture in the mathematical sense, which is a claim and not an input |
| **seam** | of a rebuilt draft: a section with nothing under it before the next heading of its own level or higher, two identical adjacent paragraphs of three words or more, a paragraph that opens in the middle of a sentence, or a line that opens on a comma or a semicolon with more than a comment after it | a seam in the geological or textile sense |
| **dangling**, **orphaned** | of a cross-reference in a live draft: pointing at a label, a heading anchor, or a footnote that is not there; of a label or a footnote: pointed at by no cross-reference | dangling in the grammatical sense; a bibliography entry cited nowhere, which the round check reports (`ROUND-4`) |
| **phantom** | a bare numeric citation that resolves to nothing, or a "Section N", "Table N", "Figure N", or "Equation (N)" pointer numbered beyond what the draft has | anything in the perceptual sense |
| **echo** | a sentence with eight words or more outside its quotations, appearing twice in a draft or across the live drafts | an echo in acoustics |
| **live** | of an artifact: not yet frozen, since what freezes it (`DOCUMENT_GENRES.md` §2) has not happened; derived, never written as a field (`ONTOLOGY.md` §3). A *live draft* is a draft under the write-up folder that is not yet frozen | a caution in the tension ledger that is *live*, still standing, as against one closed on a date (`PRECEDENCE.md`); a live process, one still running (`MANIFESTO.md` §16) |
| **frozen** | of an artifact: a dated record of what was true, known, or decided at a point in time, corrected only with the researcher's authorization, in its running text, and never moved or deleted (`DOCUMENT_GENRES.md` §2, which names what freezes each kind of artifact, such as its owning plan's closing or a release; `MANIFESTO.md` §12); derived, never written as a field (`ONTOLOGY.md` §3) | an environment or a package directory frozen at its versions, which here is *pinned* (*pinned environment*, below); frozen weights or layers in machine learning; a code freeze; a frozen sample or a frozen section in the laboratory; *immutable*, the prompt log's genre, never edited once committed, with authorization or without; *released*, below |
| **released** | of a version of the write-up, or of a standalone note: carrying the researcher's `Released <date>` stamp and, for a version after the first, its release row in the changelog (`ONTOLOGY.md` §2.6). A released version of a versioned write-up is never corrected, by anyone, in any form it is released in, whether or not it has left the repository, and is succeeded instead; what is released with it is corrected as its own genre allows, unless the researcher directs for that release that it never is (`MANIFESTO.md` §12); `DOCUMENT_GENRES.md` §2 says what a release freezes | published or made public, which a release need not be, and which releases nothing; a release of a dataset or of software, which is its producer's edition (*vintage*, below); *frozen*, above: a frozen artifact is corrected with the researcher's authorization, a released version never |
| **mark**, **markup** | a mark is one annotation a reader made on a copy of a write-up: a comment, a highlight, a strike-through, a margin note; a copy's markup is all of its marks, each accounted for in a markup ledger (`paper/_template_changelog.md`) | a grade; a trademark; a label or a sign in the everyday sense, as in a version marked `superseded by <path>` or one that marks itself on the page as a draft, or a quotation mark; markup in the sense of a markup language or of text formatting, as in the status block's rule against markup around a label (`MANIFESTO.md` §16) |
| **accepted finding** | a finding of a check, or a findings-gate reminder, that the researcher has ruled to leave, entered in the `[[accepted]]` list of `tools/artifacts.toml` with the log entry of the ruling, so the tools stop raising it (`MANIFESTO.md` §16) | a finding entered in `FINDINGS.md`; a claim accepted as established |

## Words this methodology borrows from one discipline

The rulebooks draw examples from several fields, and a few borrowed terms
appear in rule text rather than in an example. They are glossed here so
that a reader outside the field they come from is not stopped by them.

| Word | What it means | Where it appears |
|---|---|---|
| **shelfmark** | the identifier under which a holding institution shelves one item, by which a second reader asks for the same thing | the source index and the registry, as the archival case of an identifier |
| **folio, recto, verso** | a leaf of a manuscript, and its front and back; a way of citing a place in one | the citation-locus examples |
| **facsimile, digital surrogate** | a reproduction of a source, photographic or digital, as against the original | the form consulted, in the source index |
| **apparatus** | an edition's record of what its witnesses read where they differ | the rule that a claim is not re-derived from a source's own summary |
| **vintage** | the release or edition of a dataset, as against its name | the discrepancy analysis of a check |
| **provenance** | where a thing came from and by what steps, recorded so a reader can follow it back | throughout |
| **pinned environment** | the software a check program runs on, held at the exact versions the project records, so that a second reader runs the check on the same thing | the instrument of record where it is software (`CHECK_METHODOLOGY.md` §3), and the running of a check program |
| **checksum** | a short string computed from a file's bytes, which changes when any byte does, so that two copies can be compared without having both at hand; SHA-256 names one standard way of computing it | the import ledger and the source index |
| **pre-registration** | fixing what will count as confirmation before the evidence is consulted | the plan's *Confirmation and refutation* section, the `Pre-registered` stamp (`ONTOLOGY.md` §2), and the protocol note `evidence_and_reasoning/notes/README.md` describes |

## The finding tags

Every finding of the linter, the round check, the concordance check, the
probe, and the residue check carries a tag naming the rule it comes from,
so that a reader can find the rule from the output. Each tool's docstring
lists the items it reports; the families are:

| Tag | The rule it enforces |
|---|---|
| `GENRES-n` | `DOCUMENT_GENRES.md`, *What the checker verifies*, item n |
| `EDIT-n` | `evidence_and_reasoning/editorial_standards.md`, *What is checked mechanically*, item n |
| `ONT-n` | `ONTOLOGY.md` §5, check n |
| `CHECK-n` | `CHECK_METHODOLOGY.md`, *What is checked mechanically*, item n |
| `ROUND-n` | the round's own items, which `tools/check_round.py` numbers: the log's, from `MANIFESTO.md` §8, and the build's and the bibliography's, from `paper/README.md`, *Conventions* |
| `RESIDUE-n` | `tools/check_residue.py`, the rebuild residue it looks for |

## Renaming a word this methodology uses

**If one of these words is a term of art in your field, rename it before
the record exists.** The cost of renaming rises with every claim, check,
and log entry written under the old name, because the log is immutable and
a frozen artifact keeps its wording; on the first day the cost is only
the edits below.

Three kinds of name, with three costs:

1. **A word in the prose.** Yours, in your copies of the rulebooks: the
   documents are the project's to change (`MANIFESTO.md`, *Amending this
   manifesto*, and `VISION.md`, *The repository is the researcher's*).
   Change the word and its *Words used* entry, and record the change in
   the round's log entry. No tool reads a word of the prose as a term,
   save the few headings, column names, and values a tool finds by name,
   such as a claim's *What is not claimed*, a plan's *Execution status*
   and its *State* column, and the states *done* and *dropped*; those keep
   their wording unless the tool that reads one is edited with it.

2. **A header field name** (`Register:`, `Mutation:`, `Instrument:`,
   `Frame:`, and the rest). Configured: `tools/artifacts.toml` carries a
   `[fields.roles]` table mapping each role to the name this project
   writes, and every tool reads the name from there. Change it there,
   change the artifact templates under `evidence_and_reasoning/`,
   `python_project/src/`, `paper/reviews/`, and `prompt_logs/` to match,
   and the checks follow. Do this before any artifact carries the field.
   The new name has the form `ONTOLOGY.md` §1.1 gives a field's name: a
   capital letter, then letters and hyphens, each from A to Z, opening
   with none of the words `Created`, `Released`, `Reserved`, and
   `Pre-registered`. It is neither a name another field carries nor
   `Genre`, `Tier`, `Live`, or `Frozen`, which name derived state
   (`ONTOLOGY.md` §5, check 6). A registry bullet, `Standing:` among
   them, is not a header field: it is renamed in `[registry] required`,
   or in the `[registry.by_kind]` table that requires it, and in the
   registry's own template. An entry's `Kind:` bullet is the exception:
   it takes the name `[fields.roles]` gives a claim's `Kind:` field, and
   is renamed with that field.

3. **A value in a closed vocabulary** (`VERIFIED`, `reproduced`, and the
   rest). A kind, a kind's verdict, and a plan's verdict are configured
   under `[vocab]` in the same file, and a project may rename one there
   or add one its discipline needs. The six registers and the plan
   statuses `DRAFT`, `ENGAGED`, and `CLOSED` are fixed, because the tools
   apply rules to each by name: renaming one means editing every tool
   that names it, and a register added to `[vocab] registers` passes the
   vocabulary check and is treated by every other rule as none of the
   six. What a value *means* is `CHECK_METHODOLOGY.md`'s, or for a plan's
   `DOCUMENT_GENRES.md`'s, and a project that changes the meaning amends
   that file and says so.

A fourth kind of name is **fixed**: the symbols the tools resolve inside a
check program, `construct`, `main`, `report`, `MUTATIONS`, `BASIS`,
`RESULT`. A project may not rename them without editing the tools that
call them, and the check-program template,
`python_project/src/_template_check.py`, names them at every use so a
reader meets the contract rather than the word. Where one collides with
the discipline (a *construct* is an engineered DNA), the check's own
docstring says in one line what the function builds, and the collision
stops there.

What a rename does not change: the rulebooks' arguments, which are about
the things and not the names. A project that renames *mutation* to
*planted fault* still owes every check a fault it would fail under.

## Slots

None. This file names the method's own vocabulary, which is the same in
every project; a project's own terms are `evidence_and_reasoning/terminology.md`'s.

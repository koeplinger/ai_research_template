# Glossary: the words this template uses in its own sense

*Created 8 September 2026; updated 8 September 2026.*

This file defines the method's own vocabulary. It exists because a
methodology that means to serve every discipline has to name its parts,
and every name it could choose is already taken by somebody's field. The
table below says what each word means here and what it will be mistaken
for; the section after it says which words a project may rename, and how.

A project's own subject-matter terms are not defined here. They go in
`evidence_and_reasoning/terminology.md`, which is the project's glossary
(`MANIFESTO.md` §9). This file is the method's, and it is the same in
every project.

The rulebooks each open with the words they own (`MANIFESTO.md`, *Words
used throughout*; `DOCUMENT_GENRES.md` and `CHECK_METHODOLOGY.md`, *Words
used here*). Those sections define the words for the argument they are
making; this file gathers them in one place, adds the collisions, and is
where a reader who meets an unfamiliar word should look first.

## The method's words

| Word | In this template | Not to be confused with |
|---|---|---|
| **register** | how far a statement may be trusted: one of six levels a claim carries (`CHECK_METHODOLOGY.md` §1) | the primary source itself, in archival and administrative work (an admission register, a parish register, register data); a public record in law; a level of formality in linguistics; an entry in a catalogue |
| **registry** | the project's catalogue of references, one entry per work (`evidence_and_reasoning/references/`) | a public register of companies, land, or trials; a container registry |
| **claim** | one statement the project makes, filed as its own document with a register and a kind | a cause of action in law; a patent claim; an insurance claim |
| **check** | one self-contained investigation of one claim, with a printed or written verdict | a robustness check in empirical work, which is a specification and not a verification unit; a cheque |
| **gated** | of a statement: a check stands behind it that would fail if the statement were false | flow-cytometry gating; a gating network in machine learning; "blocked", which is how the round check gates a build |
| **verdict** | the word a check reaches, from the vocabulary its claim's kind fixes | what a jury returns; a court gives judgment, not a verdict |
| **finding** | a statement the record has established, entered in `FINDINGS.md` at the researcher's decision | a finding of fact, as against a conclusion of law; a finding in the sense of a search result |
| **mutation** | a named alteration to something a claim depends on, planted to show that a check can fail (`CHECK_METHODOLOGY.md` §5) | a heritable change in a DNA sequence, which is a subject of study and not a method term |
| **probe** | the tool that applies each mutation and reports whether the check caught it | a labeled nucleic acid or antibody; a probing classifier |
| **construct** | in a check program, the function that builds the object under test; part 2 of a check record | an engineered DNA construct; a theoretical construct in the social sciences |
| **frame** | what fixes the quantities a claim states: the units, encoding, edition, calendar, or sample definition (`Frame:`) | a sampling frame; a reading frame; a data frame or a stack frame |
| **instrument** | the tool or procedure of record a second reader returns to (`Instrument:`) | an instrumental variable; a physical laboratory instrument, which is equipment; a legal instrument, which is a document |
| **locus** | where in a source a citation points: the page, folio, section, paragraph, table, or variable a project fixes | a position on a chromosome |
| **collation** | reading a statement against the source of record, word by word, to establish what the source says | gathering or combining; a batching function; checking a citation, which is one kind of collation |
| **attested** | the register of a claim about what a source says, making no claim that what it says is true | witnessed, as a signature on a deed |
| **witness** | one surviving record of a work, where a work survives in several | a person who gives evidence |
| **concordance** | agreement between what a check program printed and what its record states | an alphabetical index of words; a crosswalk between classification schemes; agreement between twins |
| **sweep** | a reading pass for statements that disagree: over the record (`CHECK_METHODOLOGY.md` §7) or over the documentation (`governance/roles/documentation_sweep.md`) | a hyperparameter sweep. Never write bare *the sweep* where both could be meant |
| **residue** | what a rebuild left behind in a live draft: a reference to something no longer there | a chemical residue; an amino-acid residue |
| **authority** | which statement of this repository governs when two disagree (`PRECEDENCE.md`) | a cited case or statute, and the hierarchy of legal sources. `PRECEDENCE.md` orders this project's own statements, and says nothing about any discipline's order of sources |
| **the public record**, also *the published literature* | what is published outside this repository: articles, editions, reference works, published estimates (`PRECEDENCE.md`, tier 4). It names tier 4, heads a column of the tension ledger, and names that ledger's file | the public record in the *legal* sense, which is the court record and the reporters; those are sources of record here, at tier 2, and a divergence from one is an ordinary tension row |
| **standing** | of a registry entry: what searching for later or contrary material found, and when | *locus standi*, the right to bring a claim |
| **plan** | the unit of work: an aspect isolated, with criteria fixed before execution | a project plan or a schedule |
| **round** | the unit of time: one prompt, the work it asks for, and the entry that logs it | a round of funding; a review round |
| **slot** | a value a project fills once, written `{{LIKE_THIS}}` and listed in a Slots table | a time slot; a slot in a schema |
| **altitude** | the level of detail a statement belongs at, so that a summary does not carry a body's precision | flight altitude; nothing else here |
| **keystone** | the project's thesis, in `evidence_and_reasoning/problem_statement.md`: what the rest is built to bear on | a keystone species |
| **harness** | the program that runs the assistant and can run a command before or after each reply | a test harness in the general sense |
| **hook** | a command the harness runs at a named moment, such as after each reply | a hook in a web framework; a hook in fishing or writing |
| **subagent** | a reader given one task and no access to this conversation's reasoning | an agent in the economic sense |
| **build lens** | a passage of these rulebooks addressed to the template's own construction, stripped when a project is instantiated | a lens in optics; a build in the software sense |
| **assertion** | one independently falsifiable statement inside a claim; what a check gates, one at a time | an assertion in the programming sense, which is one way to write one |
| **check record** | the dated entry recording one execution of a check: the date, who ran it, the verdict, and the second pass | the check itself, which is the investigation; a record in the archival sense |
| **second pass** | an independent route to the same result, taken by another party or another method, and recorded beside the first | a second reading; a second attempt at the same route, which is not one |
| **instrument of record** | the tool or procedure a second reader returns to in order to repeat a verification, named precisely enough that they reach the same thing | see *instrument* above |
| **docket** | a plan's list of items deferred to its closure | a court's docket; a ticket queue |
| **structure lens** | the pass a review takes before any sentence-level finding: per section, the inventory, the order, and where each fact is established | a lens in optics; the *build lens* above, which is a different thing |
| **coverage** | of a search or a design: what it could have found, established and stated, so that finding nothing means something | test coverage in the software sense, which is a different measure |
| **blast radius** | every place a claim is relied on, which is what moves if the claim moves | anything explosive |
| **derived**, of an input | forced by prior structure, as against *imposed* (a choice the project made) and *conjectured* (assumed and not established), the three kinds every input of a check is classified into (`CHECK_METHODOLOGY.md` §4) | the `DERIVED` register, which is a trust level and not an input kind; *derived material*, which is what a plan made from a source; a derived cell line, a derived allele, a derived variable |
| **imposed** | of an input: a choice the project made, which it states as a choice rather than as a fact | imposed in the sense of forced from outside |
| **conjectured** | of an input: assumed and not established, so that what rests on it is no stronger | a conjecture in the mathematical sense, which is a claim and not an input |
| **seam** | of a rebuilt draft: a section with nothing under it before the next | a seam in the geological or textile sense |
| **dangling**, **orphaned** | of a reference: pointing at what is not there, and pointed at by nothing | dangling in the grammatical sense |
| **phantom** | a bare numeric citation or a "Section N" pointer that resolves to nothing | anything in the perceptual sense |
| **echo** | a sentence of eight words or more appearing twice in a draft | an echo in acoustics |

## Words this template borrows from one discipline

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
| **pre-registration** | fixing what will count as confirmation before the evidence is consulted | `CHECK_METHODOLOGY.md` §5, and the `Pre-registered` stamp |

## The finding tags

Every mechanical finding carries a tag naming the rule it comes from, so
that a reader can find the rule from the output. The tools' own README
lists them; the families are:

| Tag | The rule it enforces |
|---|---|
| `GENRES-n` | `DOCUMENT_GENRES.md`, *What the checker verifies*, item n |
| `EDIT-n` | `evidence_and_reasoning/editorial_standards.md`, *What is checked mechanically*, item n |
| `ONT-n` | `ONTOLOGY.md` §5, check n |
| `CHECK-n` | `CHECK_METHODOLOGY.md`, *What is checked mechanically*, item n |
| `ROUND-n` | `MANIFESTO.md` §13, the round's own items |
| `RESIDUE-n` | `tools/check_residue.py`, the rebuild residue it looks for |

## Renaming a word this template uses

**If one of these words is a term of art in your field, rename it before
the record exists.** The cost of renaming rises with every claim, check,
and log entry written under the old name, because the log is immutable and
a frozen artifact keeps its wording; on the first day the cost is one
edit.

Three kinds of name, with three costs:

1. **A word in the prose.** Yours, in your copies of the rulebooks: the
   documents are the project's to change (`MANIFESTO.md`, *Amending this
   manifesto*, and `VISION.md`, *The repository is the researcher's*).
   Change the word and its *Words used* entry, and record the change in
   the round's log entry. The tools do not read prose.

2. **A header field name** (`Register:`, `Mutation:`, `Instrument:`,
   `Frame:`, and the rest). Configured: `tools/artifacts.toml` carries a
   `[fields.roles]` table mapping each role to the name this project
   writes, and every tool reads the name from there. Change it there,
   change the templates under `evidence_and_reasoning/` to match, and the
   checks follow. Do this before any artifact carries the field. A
   registry bullet, `Standing:` among them, is not a header field: it is
   renamed in `[registry] required` and in the registry's own template.

3. **A value in a closed vocabulary** (`VERIFIED`, `reproduced`, and the
   rest). Configured under `[vocab]` in the same file. A project may
   rename a value or add one its discipline needs; what a value *means*
   is `CHECK_METHODOLOGY.md`'s, and a project that changes the meaning
   amends that file and says so.

A fourth kind of name is **fixed**: the symbols the tools resolve inside a
check program, `construct`, `sanity`, `verify`, `MUTATIONS`, `BASIS`,
`RESULT`. A project may not rename them without editing the tools that
call them, and the shipped program template names them at every use so a
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

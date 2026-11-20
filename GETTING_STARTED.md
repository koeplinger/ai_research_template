# Getting started: from a clone to a first commit

*Created 8 September 2026; updated 19 November 2026.*

This is the walkthrough. It takes a clone of the template and leaves you
with a project whose first plan is engaged, whose first claim is checked,
and whose first commit is clean. It assumes nothing about your field and
no prior knowledge of where the template came from.

Two words before you start. A **round** is one prompt, the work done in
response to it, and the log entry that records it; a **slot** is a value
your project fills once, written `{{LIKE_THIS}}`, whose *owner row* is its
line in the Slots table of the file that owns it. For any other word you
meet, look first in `GLOSSARY.md`.

**Steps 1 to 3 have a tool.** `tools/new_project.py` does what can be
done mechanically: it copies the files the template's repository tracks,
removes what belongs to the template's own construction and the pointers
to it, strips the build lens, converts the shipped prose to your spelling
variant, asks you each slot's question of §3 and writes each answer where
its owner defines it, writes the values the tools read, keeps the
template's configuration as it shipped for the tools' self-tests, renames
any field your discipline has taken, adds your copyright holder and
citation beside the template's, installs the hooks, writes a front page,
records in a dated working note what it did and what it left to you,
and runs the round check in the new tree. Keep the answers file outside
both trees:

```bash
python3 tools/new_project.py --template > ../answers.toml   # then fill it in
python3 tools/new_project.py --into ../my-project --answers ../answers.toml
```

Add `--yes` to take the file as it stands; without it the tool asks about
every value, showing what the file gave, and without `--answers` it asks
about all of them.

**Setup at a prompt, as one pass.** An assistant asked to make the
project cannot answer the tool's questions for you, so it puts them to you
first and runs the tool once:

1. it puts the questions of §3 one at a time, each with the assistant's
   recommendation after the options where it has one, labeled as its own
   (`MANIFESTO.md` §16, *Putting a decision*); with them, the values the
   tools read, worked out from your answers and shown to you (§3, *The
   machine half*); and the setup decisions that are not slots, listed
   at the end of §1, the privacy list before everything else;
2. you name the new project's folder, and where the answers file goes,
   outside both trees;
3. it writes your answers there: each slot under `[slots]`, each value the
   tools read that has a key under `[machine]`, the copyright holder,
   citation and start date under `[project]`, and any rename under
   `[rename]`, leaving blank whichever of the three slots you leave to
   wait; and it runs the tool with `--answers` and `--yes`;
4. in the new project, before anything is committed, it writes your
   privacy list to `.privacy/stopwords.txt`, where there is one; the two
   standing directions under `ONBOARDING.md`, *Standing directions*; and
   the fields a kind of work needs of its own under `[registry.by_kind]` in
   `tools/artifacts.toml`, where you named any. Where you chose to drop the
   shipped Python check suite, it removes it as `python_project/README.md`
   says. It then writes entry 001, the record of the setup, as §4 says,
   recording there a privacy list of none where that was your answer,
   and marks whichever of the three slots you left to wait in its owner
   row (§3).

Read §1 to §3 anyway: they say what the tool does and why, and the
decisions are the same either way. §4 onward is yours.

Read `HOW_IT_FITS_TOGETHER.md` when you want to know *why* the parts are
shaped as they are. Read this file to get moving. The whole of it is one
sitting, and the round that states the question is the longest part.

---

## 1. Clone, and make it yours

Copy the template into a new repository of your own, then remove what
belongs to the template's own construction rather than to your project.

| Leave behind | And also |
|---|---|
| the worked example, the example folder | its rows in `README.md` and `governance/README.md`, its row in `tools/artifacts.toml`, and its mention under *Support* in `HOW_IT_FITS_TOGETHER.md` |
| the template's own work list, TODO.md | its rows in `README.md` and `tools/artifacts.toml`; your project's open work is its plans and its roadmap |
| the template's setup tool, under `tools/` | its rows in `tools/README.md` and `governance/README.md` |
| `.review/`, interim review records, if present | nothing; add it to `.gitignore` if you keep the folder for your own reviews |

Removing a folder means removing the pointers to it as well, or the path
check reports what is gone. That is the check working; §8 says what to
expect.

Every file you change takes the day of the change as its updated date, in
its header; a file you leave keeps the template's dates
(`DOCUMENT_GENRES.md` §3).

| Keep | Why |
|---|---|
| every rulebook, index, and artifact template | they are the project |
| `VISION.md` | the rulebooks cite it, and it states what the method is for |
| `tools/`, `governance/` | the checks and the standing roles |
| `LICENSE.md`, `LICENSE-CODE` | with your own copyright added, below |

**The harness.** What you have just copied includes one wiring, for
Anthropic's Claude in its command-line harness: its tracked settings file,
`.claude/settings.json`, runs the session brief as each session starts and
the status-block check after each reply, once the harness trusts this
folder. The harness asks that once for each folder, the template's and the
project's alike. Answering is a choice about what may run on your
computer, made in the harness when a session first opens in the folder;
it is not a decision of the method, and it sets no slot. The assistant
mentions it, and nothing is committed on its answer. If you decline, nothing runs, and the form of each reply's
status block is kept by hand (`governance/harness/claude_code/README.md`).
If that harness is not your assistant's, `governance/harness/README.md`,
*Adding a wiring, and removing one*, is the recipe, and `{{REPLY_HOOK}}`
in §3 is where you record what you did. Nothing else in the template is
vendor-specific, and the tools know no harness.

**The licenses.** Add your own copyright holder to `LICENSE-CODE` beside
the template's, dated by the year your project starts, and add your
project's own recommended citation to `LICENSE.md`. **Keep the template's citation** as the work yours is
adapted from: the written material is under CC BY 4.0, which requires
attribution to the original, so replacing that citation rather than adding
to it would put the project out of compliance with the license it inherits.

Then install the git hooks, which are not cloned:

```bash
bash tools/install_hooks.sh
```

That puts the round check on pre-commit, advisory: it reports and lets the
commit through. `--strict` makes it refuse instead, which you can change
at any time.

**Arm the privacy scan.** Decide, before the first commit, what must never
reach this repository, and write it to `.privacy/stopwords.txt`, one entry
per line; the folder is git-ignored, and once the list exists the hooks
scan every commit against it (`tools/privacy_scan.py` gives the form).
Typical entries: a local path prefix; the name of a private project, a
dataset the work draws on, or a collaborator who is not to be named; an
address the assistant may give an outside service. A party the record
credits by name is not an entry, since `MANIFESTO.md` §6 allows that name.
*None* is a valid answer, given by writing no list: one that exists and
holds no pattern, comments alone, refuses every commit until it holds one
or is removed. The list is not cloned, any more than the hooks are, so
every clone arms it again.

**The setup decisions that are not slots**, settled in setup (§4), each
where it is stated; the privacy list comes first, before the first
commit:

- the privacy scan's list, or none (*Arm the privacy scan*, above);
- whether the assistant may look up each work it adds to the reference
  registry outside this repository, resolving its identifier where it was
  issued and searching for later corrections or disputes, and what
  identity, if any, it and its subagents may give an outside service that
  asks for one: two standing directions, written under `ONBOARDING.md`,
  *Standing directions*; without the first, the assistant does neither
  (`MANIFESTO.md` §3 and §6);
- this project's copyright holder and citation, and the start date whose
  year dates the copyright (*The licenses*, above);
- any header field to rename because your discipline has taken its name
  (§3, *While you are in there*);
- whether the shipped Python check suite stays (§2).

---

## 2. Strip the build lens, and make the front page yours

The rulebooks, `ONBOARDING.md`, and the shipped wiring's README under
`governance/harness/` carry blocks that begin `> **Build lens.**`. They
are addressed to the construction of the template itself and say nothing
to a project. Delete every one:

```bash
grep -rn "Build lens" --include=*.md . | grep -v GETTING_STARTED
```

Delete also the two sections of `MANIFESTO.md` that describe the two
lenses: `## Two lenses`, near the top, and `## Where the two lenses
differ`, the summary table near the end. Nothing else in those files
changes.

**Rewrite the root `README.md` as your project's front page.** As shipped
it describes the template, which is not what a reader of your repository
is looking for. Keep its shape and replace its content: your project's
title, a paragraph on the question (written in the round that states it,
§4), where to start reading (`CURRENT_STATE.md`, `FINDINGS.md`, then the
record), the licenses, and a line saying the project is built from the
methodology template, with a pointer to it.

If your project will not use the shipped Python check suite, this is also
the moment to decide that; `python_project/README.md` says what removing
it touches.

---

## 3. Fill the slots

A slot is a decision the methodology cannot make for you, marked
`{{LIKE_THIS}}` in the text and listed in a Slots table at the end of the
file that owns it.

**How a slot is filled**, in two moves:

1. **Decide the value once, in the Slots table of the file that owns it.**
   Write it into the first cell, after the slot name, as a colon and the
   value:

   ```
   before   | `{{PERSONA}}` | The domain expert the assistant works as (§1) | *mathematician*; ... |
   after    | `{{PERSONA}}`: archaeologist working on ceramic typology and site chronology | The domain expert the assistant works as (§1) | *mathematician*; ... |
   ```

   Deciding it once is what *the file that owns it* protects: a slot with
   two homes is a slot with two values.

2. **Replace the token with the value everywhere else it appears**, so
   the sentence reads, except where a token is the slot's name or quotes
   it: the guide's pages (this file, `HOW_IT_FITS_TOGETHER.md`, and
   `FORKING.md`) and `GLOSSARY.md`, which are about slots rather than
   carrying them; the comments of `tools/artifacts.toml` and program
   source, which name a slot on purpose; and the log under `prompt_logs/`,
   whose committed entries keep what they recorded. Several slots
   are quoted in files that do not own them, and those are prose, not
   second definitions. A long value pasted into a sentence usually will
   not read: put a short handle in the sentence and let the Slots table
   carry the full value.

   ```bash
   grep -rno "{{[A-Z_][A-Z_]*}}" --include=*.md \
     --exclude=GETTING_STARTED.md --exclude=HOW_IT_FITS_TOGETHER.md \
     --exclude=FORKING.md --exclude=GLOSSARY.md \
     --exclude-dir=prompt_logs --exclude-dir=.venv . | sort -u
   ```

   When the slots are filled, that list holds the Slots table rows and
   nothing else, because a filled row keeps its token with the value
   after it. A token on any other line is a slot still unfilled, or one
   its owner row records as open by decision. The documentation
   consistency sweep of §4 then reads the sentences the values landed in.

**A slot that waits for its stage.** Three slots, and only these three,
depend on a write-up and may stay open, by decision, until one is opened:
`{{DELIVERABLE}}` with its machine half, `{{PAPER_PRONOUN}}`, and
`{{VOICE}}`. The decision is yours, recorded in the owner row in place of
the value, with the prompt that gave it, or *by hand* where you write it
yourself outside a round and its commit is the provenance, and the stage
that ends it:

   ```
   open     | `{{VOICE}}`: open by decision (prompt 001); filled when a write-up is opened | The recorded voice rules for unfrozen drafts | ... |
   ```

The marker is written in the owner row itself, never given to the tool
as an answer. Any other slot left blank keeps the project in setup
(`ONBOARDING.md`). Until
the stage the marker names, the slot's tokens stay in the prose, and the
grep above lists them; at that stage the slot is filled by the same two
moves.

There are sixteen; three of them may wait. Each row's question is the one
the assistant puts at setup, in plain words, adding its recommendation
after the options where it has one (`MANIFESTO.md` §16, *Putting a
decision*). An answer is a phrase that completes the sentence its token
stands in, where it stands in one, as the examples below are, with no
closing period.

| Slot | Owner | Asked in plain words |
|---|---|---|
| `{{PROJECT_TITLE}}` | `evidence_and_reasoning/README.md` | What is the project called? A short descriptive name: it opens the research statement's question and heads the front page. |
| `{{PERSONA}}` | `MANIFESTO.md` | What kind of expert should the assistant work as? A field and, where it helps, a specialty; the assistant takes that role in every session. |
| `{{VERIFICATION_TOOL}}` | `CHECK_METHODOLOGY.md` | What does a second person return to when repeating a verification? The software, data, source, or written procedure, named precisely enough (a version, a release, an archive reference, the form consulted) that they reach the same thing. |
| `{{CHECK_FORM}}` | `CHECK_METHODOLOGY.md` | A check is one self-contained investigation of one claim. Is a check here a program that prints its result, a written procedure a person follows and records, or both, chosen claim by claim? |
| `{{MUTATION_SET}}` | `CHECK_METHODOLOGY.md` | Which deliberate faults will you plant in what your claims depend on, to show that each check can fail? Give each a short name and say what it alters; a change a claim should survive belongs to a robustness check instead. |
| `{{PARTIES}}` | `ONTOLOGY.md` | Besides you and the assistant, who will the record credit by name for producing or checking a piece of work? Name each person, group, or service, or answer none; the tools report any name not on the list. |
| `{{CITATION_LOCUS}}` | `ONTOLOGY.md` | When a citation points to a place inside a work, in what units is that place given? Every unit your sources need, such as page and section, folio and line, table and column, or paragraph number. |
| `{{REFERENCE_FIELDS}}` | `ONTOLOGY.md` | Which details must every entry in the project's list of references carry, and does a kind of work need more of its own? Seven are required until you change them: authors, title, where published or held, year, identifier, keywords, and standing (what a search for later corrections or disputes found, or why none was made). |
| `{{REFERENCE_ADEQUACY}}` | `evidence_and_reasoning/editorial_standards.md` | Which kind of reference is good enough to back which kind of claim? Pairs such as a peer-reviewed article for a specialist claim, or an archival document by its reference for what that document says. |
| `{{DELIVERABLE}}` | `DOCUMENT_GENRES.md` | What will the project publish? Its form, what its venue expects of a title, how a version shows on its page which version it is and whether it is released, and what goes out with each released version besides the text, such as data, code, or transcriptions. It may wait until a write-up is opened. |
| `{{SPELLING}}` | `evidence_and_reasoning/editorial_standards.md` | In which language and spelling variant is the project's prose written: US English, UK English, or another language, for which no word list is checked? US English is checked from the start until you change it. |
| `{{DASH_CONVENTION}}` | `evidence_and_reasoning/editorial_standards.md` | How does the prose punctuate an aside inside a sentence, and a range such as 10 to 20? Asides take no em-dashes, spaced or unspaced em-dashes, or spaced en-dashes; ranges take an en-dash or the word to. The tools report every em-dash until you change the rule or turn the check off. |
| `{{PAPER_PRONOUN}}` | `evidence_and_reasoning/editorial_standards.md` | In the write-up, who performs its acts: we (even for one author), I, or the document itself (this article argues)? One choice, used throughout. It may wait until a write-up is opened. |
| `{{VOICE}}` | `evidence_and_reasoning/editorial_standards.md` | What style rules will drafts of the write-up be tested against? Rules read off your earlier writing, a house or journal style you name, or the example voice record in editorial_standards.md, kept as it stands. It may wait until a write-up is opened. |
| `{{REPLY_HOOK}}` | `MANIFESTO.md` | Every reply of the assistant ends in status lines saying whether to wait, answer, or walk away. Where and how does the program that runs the assistant check them after each reply: the wiring this repository carries, one you add, or none, with the form kept by hand? |
| `{{DISCLOSURE_RULE}}` | `MANIFESTO.md` | Do your sources' terms, an agreement, or an ethics approval limit what the project may publish or share, such as a minimum count per table cell, the scope of consent, or an embargo? State the rule, or answer none beyond the general privacy rules. |

Where more than one Slots table carries the same slot, the Owner column
above is the authority; every other table's row is a pointer to it.

### The machine half

Six slots are read by the tools as well as by people, and a value written
only in the prose is not in force:

| Slot | Where the tools read it | As shipped |
|---|---|---|
| `{{SPELLING}}` | `[editorial] spelling` | `"us"`: **enforced against your prose until you change it** |
| `{{DASH_CONVENTION}}` | `[editorial] dashes` | `"no-em-dash"`: likewise enforced |
| `{{REFERENCE_FIELDS}}` | `[registry] required`, and `[registry.by_kind]` | the seven defaults, **required of every entry** until you change them |
| `{{MUTATION_SET}}` | `[vocab] mutations` | empty: the name check is skipped, and says so |
| `{{PARTIES}}` | `[parties] names` | empty: the roster check is skipped, and says so; `["none"]` records by decision that no one beyond you and the assistant appears, and the check runs |
| `{{DELIVERABLE}}` | `[publication]` | disabled: the build and bibliography gates do not run |

The distinction matters. An empty value means the check is skipped and
reports that it was; a shipped default means the check runs, against you,
with the template's answer. All of them are in `tools/artifacts.toml`.

### While you are in there: rename what your field has taken

The methodology's own words are in `GLOSSARY.md`, each with what it will
be mistaken for. If one of them is a term of art in your field, **rename
it now**: the field names the tools read are configured in one table,
`[fields.roles]` in `tools/artifacts.toml`, and the cost of renaming rises
with every claim, check, and log entry written under the old name. On the
first day it costs only the edits `GLOSSARY.md`, *Renaming a word this
template uses*, lists.

The commonest case is *register*, which this methodology uses for a
claim's trust level and which several fields use for a primary source.

### Sixteen slots, filled five ways

Filled examples, so you can see the shape a real value takes. Each list is
a historian of medicine, an empirical microeconomist, a molecular
biologist, a scholar of contract law, and a machine-learning researcher.

**`{{PROJECT_TITLE}}`**
- Fever admissions at a London fever hospital, 1848 to 1866
- Minimum-wage spillovers in hourly wages, 2010 to 2019
- One gene's knockdown in a colorectal cell line
- Assumption of responsibility as a test of remoteness
- Sharpness-aware minimization across seeds

**`{{PERSONA}}`**
- historian of medicine working from archival institutional records
- empirical microeconomist in labor economics and applied econometrics
- molecular biologist working in sequencing and its computational analysis
- scholar of contract law, English and Commonwealth doctrine
- machine-learning researcher in empirical deep learning and evaluation

**`{{VERIFICATION_TOOL}}`**
- collation against the source in the form the source index records: the original at its shelfmark, in the holding repository's reading room
- the statistical environment at a stated version with its package directory frozen, on the named data extract
- the project's analysis container at a stated digest, holding the pinned pipeline and the reference assembly with its annotation release
- the authorized report where one exists, else the neutral-citation transcript, read at the pinpoint
- the released training and evaluation code at the named tag, in the pinned container, on one stated accelerator

**`{{CHECK_FORM}}`**
- a written collation procedure against the source in the form consulted, one dated execution per reading
- a script per check that rebuilds the analysis file from the pinned extract and asserts each figure within a tolerance
- a verifier program over a pinned pipeline's outputs for computational claims; a written protocol with named controls, one execution per replicate, at the bench
- a written procedure of three kinds: a citation check at the pinpoint, a currency check, and a reasoning check against the ratio
- a two-stage program: a produce stage that trains or loads a cached checkpoint, and a verify stage that asserts each metric within a pre-registered tolerance

**`{{MUTATION_SET}}`**
- alter one entry; drop one folio; transpose two entries; misread one numeral
- swap one treatment coding; break the merge key; shift the treatment date by a quarter; drop one stratum
- shuffle the sample-to-condition labels; drop one replicate; swap the annotation release; flip the library strandedness
- overstate the holding; plant dictum as ratio; shift the pinpoint; drop the subsequent history
- shuffle the training labels; evaluate on the training split; set the learning rate to zero; drop the seed set to one

**`{{PARTIES}}`**
- a paid transcriber; the holding repository's archivist, where a reading came by correspondence
- a coauthor; a research assistant; an independent replicator; the data provider's output-control officer
- the bench collaborator who runs replicates; the sequencing facility; the coauthor who re-analyzes from raw reads
- a named colleague who reads each authority blind at the pinpoint; the journal's cite-checker
- none

**`{{CITATION_LOCUS}}`**
- folio with recto or verso and entry number; case number and date; date and correspondents, for a letter; page, for print
- page; section; equation; table and column; figure and panel; variable and wave, for a codebook
- figure and panel; supplementary figure or table; page, for methods; sample or run identifier; accession with its version
- paragraph number, with the judge where the report has several judgments; page, for a report without paragraphs; section and subsection, for a statute
- section; table; figure; equation; appendix section; file path and commit, for code; split and version, for a dataset

**`{{REFERENCE_FIELDS}}`**
- for archival items: repository, collection, reference, description, date range, form consulted, access conditions; for print: author, title, place, publisher, year
- the seven defaults, plus producer, series and release for a dataset
- the seven defaults, plus accession and version for a database record, and supplier, catalogue and lot for a reagent
- parties, neutral citation, report citation, court, judgment date, jurisdiction, judges, currency
- the seven defaults, plus version: a preprint version, a dataset release, or a commit

**`{{REFERENCE_ADEQUACY}}`**
- an archival document by repository and shelfmark to folio and entry, for any claim about what a source says; a monograph or article to the page for any specialist claim
- a peer-reviewed article or a numbered working paper for any specialist claim; the producer's codebook by version for any statement about a variable
- a peer-reviewed primary article for any specialist claim; a database record by accession and version for any sequence claim; a reagent by identifier and lot
- a primary authority for every proposition of law, cited to its authorized report at the pinpoint; a treatise only where no authority is on the point
- a peer-reviewed paper or a preprint at a stated version for any method claim; the dataset paper and release for any claim about the data; a repository at a commit for any claim about code

**`{{DELIVERABLE}}`**
- a journal article of about nine thousand words with footnotes in the house style, drafted in markdown and rendered for submission; a title and subtitle in the journal's style; its version and date under the title, and a draft marker until the release
- a journal article in a typesetting system, an online appendix carrying the same version, and a replication package; a short descriptive title; the date of the version on its title page, and a draft marker until the release
- a research article with figures and legends, methods, supplementary tables, and a source-data file per panel; a title that states the finding; its version and date in the footer, and a draft marker until the release; released with the deposited data
- a law review article of about fifteen thousand words including footnotes, with a table of cases and a table of legislation; a title that names the doctrine; a dated draft legend on the cover page until the release
- a conference paper with an appendix of experiments in the venue's template, which sets the title block and marks the copy as under review until the release; its version number on the first page; released with the code at a tag, the configurations, and the per-seed metrics

**`{{SPELLING}}`**
- UK English, the *-ise* ending (`uk`)
- US English (`us`)
- US English (`us`)
- UK English with legal spellings kept: *judgment*; *licence* the noun, *license* the verb (`uk`)
- US English (`us`)

**`{{DASH_CONVENTION}}`**
- spaced en-dashes for asides, unspaced for ranges, no em-dashes (`en-dash-asides`)
- unspaced em-dashes for asides (`unspaced-em-dash`)
- no em-dashes; en-dashes for ranges and for fusion names (`no-em-dash`)
- spaced en-dashes for asides, unspaced for name joins (`en-dash-asides`)
- no em-dashes (`no-em-dash`)

**`{{PAPER_PRONOUN}}`**
- I, for a single-authored article
- we, also for a single author
- we
- the article itself (*this article argues*), with no first person
- we, also for a single author

**`{{VOICE}}`**
- read off two prior articles: the subject of a sentence is the institution, the clerk, or the document, never *the data*; a quotation carries its folio in the note
- state the estimand before the estimator; never a coefficient without its standard error and its clustering level; name the specification by table and column
- methods in the past tense, results in the present; one claim per paragraph anchored to its panel; every quantitative statement with its replicate count and its test
- the proposition in the text and the authority in the footnote; *held* only of the ratio, *said* of dictum
- every result is a mean and a spread over a stated number of seeds; *significantly* only with the test named

**`{{REPLY_HOOK}}`**, which four of the five fill the same way, since one wiring comes with the template; a project on another harness fills it with its own
- the wiring this repository carries, `governance/harness/claude_code/`, run from `.claude/settings.json`
- the wiring this repository carries, `governance/harness/claude_code/`, run from `.claude/settings.json`
- the wiring this repository carries, `governance/harness/claude_code/`, run from `.claude/settings.json`
- none: the work is done in a harness that cannot run a command after a reply, so the form is kept by hand
- the wiring this repository carries, `governance/harness/claude_code/`, run from `.claude/settings.json`

**`{{DISCLOSURE_RULE}}`**
- the access conditions recorded for each source; nothing quoted beyond what its terms permit
- the agency's minimum cell size and its dominance rule, with the output-control officer on the roster
- the controlled-access conditions of the deposited data, and the consent scope the approval fixed
- none beyond §6: the authorities are public
- none beyond §6: the benchmarks are open

---

## 4. The first rounds: set up, then state the question

The first rounds come in this order, and every other statement of it
points here:

1. **Setup**, wherever something is left to decide at a prompt, the two
   standing directions of §1 included: the questions of §3 and the setup
   decisions that are not slots (§1), put to you one at a time, the
   privacy list first where it is still open, so that it exists before the
   first commit. Unless you ask for them together (`MANIFESTO.md` §16),
   each answer is its own round, and in the new project each prompt opens
   its own entry, like any other. Setup at a prompt in the template's
   clone, before the project exists, is recorded instead as entry 001,
   written in the new tree after the run and before the first commit:
   every prompt of the exchange verbatim, each answer quoted as your
   ruling, and a pointer to the setup note the tool wrote, with nothing the
   privacy list holds. Under *Corrections and departures*, it says that
   the one entry records the whole exchange and follows the run it
   records, because the log, like the project, did not exist before the
   run.
2. **The question**: the round after setup's last entry, or entry 001
   where setup was not a round. It writes the two documents below, and
   the front page's paragraph on the question (§2).
3. **The documentation consistency sweep**, made with the prompt *Make a
   documentation consistency sweep*. It catches what setup left behind: a
   slot value that does not read where it was substituted, a pointer the
   tool could not reach, a file still speaking in the template's voice
   (`governance/roles/documentation_sweep.md`).

Nothing else yet. You commit at the end of each round, once you have
decided what must never reach the repository, as §8 says.

Every round begins by logging the prompt. Copy the entry template under
`prompt_logs/` to the next number, `NNN_short_description.md`, the form
the round check reads, add its row to `prompt_logs/README.md`, paste the
prompt verbatim, and only then do the work. That order is the rule, setup
at a prompt in the template's clone aside (item 1), and it is the first
thing the session brief will remind you about.

The two documents that say what the project is for:

- `evidence_and_reasoning/research_statement.md`: the question as posed,
  and what would count as answering it.
- `evidence_and_reasoning/problem_statement.md`: the keystone, your thesis
  as one or more hypotheses precise enough that evidence could count
  against them. Registered `SPECULATIVE`, because that is what a thesis is
  until something checks it.

Close the round by writing what you did into the log entry, and end with a
status block.

---

## 5. Bring in a source

A source of record is what your claims will be read against. Register it
in `evidence_and_reasoning/references/`, one entry with the fields your
`{{REFERENCE_FIELDS}}` names; if you may redistribute it, hold it under
`source_documents/` and index it there with its license note, and if you
may not, index it by locator with its access conditions. Never edit a held
source. What you make *from* it, a transcription, an extract, a coded
table, goes under `evidence_and_reasoning/derived/`.

---

## 6. The first plan

Work happens through a plan, so that what would count as success is fixed
before the evidence is seen. Copy
`evidence_and_reasoning/research_plans/_template.md` to `001_short_name.md`
and fill every section of it: the header's `Serves:` and `Prerequisites:`
lines, the aspect isolated, the hypothesis (or, where there is none, the
task and its closure criterion), the design, the tasks, the sanity checks,
the deliverables, the confirmation and refutation criteria, what is out of
scope, and the execution ledger with every task listed. Add it to
`evidence_and_reasoning/research_plans/ROADMAP.md`.

Then engage it, which is yours to do: write `Status: ENGAGED <date>`.
Nothing is executed except through an engaged plan.

---

## 7. The first check, and the first claim

A check is one self-contained investigation of one claim. Its form is
whatever you filled `{{CHECK_FORM}}` with: a program, a written procedure,
or both.

1. **Write the check** from `evidence_and_reasoning/checks/_template.md`
   (and, for a program, `python_project/src/_template_check.py`). Name in
   its header the plan it serves, the claim it backs, the instrument of
   record, the frame of any quantities it states, at least one mutation
   from your `{{MUTATION_SET}}`, and who produced it. For a program, pin
   what it runs on in `python_project/requirements.txt` and build the
   pinned environment before the first run: a check program, and each
   tool that executes one, runs with that environment's interpreter
   (`python_project/README.md`, *Running*).
2. **Show that it can fail.** Apply each mutation and confirm the check
   reaches a failing verdict. For a program, `tools/falsifiability_probe.py`
   does it; for a written procedure, plant the alteration, follow the
   procedure again, and record that it was caught. A check that survives
   its own mutations is gated on nothing.
3. **Run it, and record what it found**: the verdict, the named values,
   the discrepancies, and the second pass, which is an independent route
   to the same place.
4. **Write the claim** from `evidence_and_reasoning/claims/_template.md`:
   the statement with its scope, what is *not* claimed, the evidence and
   route, and the references. Propose a register with your evidence; the
   register is yours to assign.
5. **Index both**, in the folder READMEs.

---

## 8. Before each commit

You commit at the end of a round, the first time once you have decided
what must never reach the repository (`MANIFESTO.md` §8). Before each
commit, run the round check. It runs the linter and its own gates
together:

```bash
python3 tools/check_round.py
```

Fix what it reports, or record why you did not. Then commit. The
pre-commit hook runs the same check, so a clean run here means a clean
commit. A commit made before a round closes leaves its entry committed
open, which the round check run at that commit shows as a closing status
not written; the next round's entry completes it (`MANIFESTO.md` §8).

If you removed the worked example without removing the pointers to it, the
path check reports those pointers, naming the file and the line. That is
the check working, and §1 says what to strike.

Where §1's privacy list exists, `tools/privacy_scan.py` runs beside the
round check at every commit. It is the one mechanism that refuses by
default: the hooks call it only where the list exists, and `--no-verify`
overrides it, with the reason in the commit message. A strict install
makes the round check refuse too.

---

## 9. And then

You have a project. What to do at each stage from here is
`HOW_IT_FITS_TOGETHER.md`, which also lists **the prompts this methodology
suggests** and when to make each. The first of them, the documentation
consistency sweep, closes the first rounds (§4).

---

## Questions that come up early

**Do I have to use an AI assistant?** No. Every rule here is about the
record, and a human writing the record by hand obeys the same ones. What
assumes an assistant: the prompt log, which becomes a work log of what was
asked and done; the harness wiring, which you delete; the status block
after each reply and the check that reads it; the standing roles under
`governance/roles/`, which a colleague plays instead of a subagent; and
the reminders, which nobody prints for you. The record, the checks, the
registers and the plans are unchanged.

**Do I have to write programs?** No. `{{CHECK_FORM}}` may be a written
procedure alone, and the rulebooks treat a written procedure as a check in
every rule. If no check of yours is a program and you keep no other
program, `python_project/` can go.

**What if my field's word for something clashes?** Rename it. See
`GLOSSARY.md`, *Renaming a word this template uses*. Do it before the
record exists.

**My subject matter keeps tripping a check.** Two answers, in this order.
First, check whether the finding is right: a check that fires on ordinary
prose about your material usually means the sentence is doing two jobs.
Second, if it really is a collision, the configuration has an escape
hatch: `skip` on the artifact row in `tools/artifacts.toml`, with the
reason written beside it. An unexplained skip is worse than the finding.
For one passage you have ruled to leave, the list of accepted findings in
the same file is narrower: it names the passage and the log entry of your
ruling, and the finding returns if the passage changes (`MANIFESTO.md`
§16, *A ruled matter stays ruled*).

**What if I disagree with a rule?** Change it. The rulebooks are yours
once you clone them; `FORKING.md` says how to change one legibly, so that
a later reader can see what you did and why. A rule you route around
silently is worse than one you delete on purpose.

**How much of this do I have to do on day one?** The slots that do not
wait for a write-up (§3), and the rounds §4 lists. Everything else
arrives when the work needs it: a plan when you are ready to execute, a check when there is something
to verify, the tension ledger when something you find disagrees with what
is published.

**Where does the record end and the paper begin?** The repository is the
primary artifact and the paper is a projection of it. Anything the paper
asserts is in the record first, with its register; the paper says what to
read off the evidence.

**Nobody will read all this.** Nobody should. `ONBOARDING.md` is what a
session reads first, and it is two pages; it sends the session on to
the manifesto, read in full, and the status files. This file you read
once. The rulebooks you consult when a question comes up, and the tools
tell you which one.

## Slots

None. This file explains the slots; it fills none, and it is the same in
every project.

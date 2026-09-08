# Getting started: from a clone to a first commit

*Created 8 September 2026; updated 8 September 2026.*

This is the walkthrough. It takes a clone of the template and leaves you
with a project whose first plan is engaged, whose first claim is checked,
and whose first commit is clean. It assumes nothing about your field and
no prior knowledge of where the template came from.

**Steps 1 to 3 have a tool.** `tools/new_project.py` does them: it copies
the template, removes what belongs to the template's own construction and
the pointers to it, strips the build lens, asks you for each of the
sixteen slots, writes both halves of every value, renames any field your
discipline has taken, adds your licenses beside the template's, writes a
front page, installs the hooks, and runs the round check in the new tree.

```bash
python3 tools/new_project.py --template > answers.toml   # then fill it in
python3 tools/new_project.py --into ../my-project --answers answers.toml
```

Add `--yes` to take the file as it stands; without it the tool asks about
every value, showing what the file gave, and without `--answers` it asks
about all of them. Read steps 1 to 3 anyway: they say what it is doing and why, and you have to make the same
decisions either way. Steps 4 onward are yours.

Read `HOW_IT_FITS_TOGETHER.md` when you want to know *why* the parts are
shaped as they are. Read this file to get moving. The whole of it is one
sitting, and the first round is the longest part.

Two words before you start. A **round** is one prompt, the work done in
response to it, and the log entry that records it; a **slot** is a value
your project fills once, written `{{LIKE_THIS}}`. Everything else you
meet is in `GLOSSARY.md`.

---

## 1. Clone, and make it yours

Copy the template into a new repository of your own, then remove what
belongs to the template's own construction rather than to your project.

| Leave behind | And also |
|---|---|
| the worked example, the example folder | its rows in `README.md` and `governance/README.md`, and its row in `tools/artifacts.toml` |
| the template's own work list, TODO.md | its row in `README.md`; your project's open work is its plans and its roadmap |
| `.review/`, interim review records, if present | nothing; add it to `.gitignore` if you keep the folder for your own reviews |

Removing a folder means removing the pointers to it as well, or the path
check reports what is gone. That is the check working; §8 says what to
expect.

| Keep | Why |
|---|---|
| every rulebook, index, and template | they are the project |
| `VISION.md` | the rulebooks cite it, and it states what the method is for |
| `tools/`, `governance/` | the checks and the standing roles |
| `LICENSE.md`, `LICENSE-CODE` | with your own copyright added, below |

**The licenses.** Add your own copyright holder to `LICENSE-CODE` beside
the template's, and add your project's own recommended citation to
`LICENSE.md`. **Keep the template's citation** as the work yours is
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

---

## 2. Strip the build lens, and make the front page yours

The rulebooks and `ONBOARDING.md` carry blocks that begin
`> **Build lens.**`. They are addressed to the construction of the
template itself and say nothing to a project. Delete every one:

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
title, a paragraph on the question, where to start reading
(`CURRENT_STATE.md`, `FINDINGS.md`, then the record), the licenses, and a
line saying the project is built from this template with a pointer to it.

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
   Write it into the first cell after the slot name, as a colon and the
   value:

   ```
   before   | `{{PERSONA}}` | The domain expert the assistant works as (§1) | *mathematician*; ... |
   after    | `{{PERSONA}}`: archaeologist working on ceramic typology and site chronology | The domain expert the assistant works as (§1) | *mathematician*; ... |
   ```

   Deciding it once is what *the file that owns it* protects: a slot with
   two homes is a slot with two values.

2. **Replace the token with the value everywhere else it appears**, in
   whatever file, so the sentence reads. Several slots are quoted in
   files that do not own them, and those are prose, not second
   definitions. A long value pasted into a sentence usually will not
   read: put a short handle in the sentence and let the Slots table carry
   the full value.

   ```bash
   grep -rno "{{[A-Z_]*}}" --include=*.md . | sort -u
   ```

   When the slots are filled, that list holds the Slots table rows and
   nothing else, because a filled row keeps its token with the value
   after it. A token on any other line is a slot still unfilled. The
   documentation consistency sweep of §9 then reads the sentences the
   values landed in.

There are sixteen.

| Slot | Owner | What it decides |
|---|---|---|
| `{{PROJECT_TITLE}}` | `evidence_and_reasoning/README.md` | the project's name, as the statements use it |
| `{{PERSONA}}` | `MANIFESTO.md` | the domain expert the assistant works as |
| `{{VERIFICATION_TOOL}}` | `CHECK_METHODOLOGY.md` | the instrument or procedure of record a second reader returns to |
| `{{CHECK_FORM}}` | `CHECK_METHODOLOGY.md` | what a check is here: a program, a written procedure, or both |
| `{{MUTATION_SET}}` | `CHECK_METHODOLOGY.md` | the named faults a check must fail under |
| `{{PARTIES}}` | `ONTOLOGY.md` | who may appear on a `By:` or `Verified-by:` line |
| `{{CITATION_LOCUS}}` | `ONTOLOGY.md` | the units a citation may name a place by |
| `{{REFERENCE_FIELDS}}` | `ONTOLOGY.md` | the bullets every registry entry carries |
| `{{REFERENCE_ADEQUACY}}` | `evidence_and_reasoning/editorial_standards.md` | which kind of reference is adequate for which kind of claim |
| `{{DELIVERABLE}}` | `DOCUMENT_GENRES.md` | the publishable form, and what is released with a version |
| `{{SPELLING}}` | `evidence_and_reasoning/editorial_standards.md` | the spelling variant |
| `{{DASH_CONVENTION}}` | `evidence_and_reasoning/editorial_standards.md` | how asides and ranges are punctuated |
| `{{PAPER_PRONOUN}}` | `evidence_and_reasoning/editorial_standards.md` | the write-up's agent |
| `{{VOICE}}` | `evidence_and_reasoning/editorial_standards.md` | the recorded voice rules a proposed sentence is tested against |
| `{{REPLY_HOOK}}` | `MANIFESTO.md` | where and how the status-block check runs after each reply |
| `{{DISCLOSURE_RULE}}` | `MANIFESTO.md` | what may leave the repository, where the sources or an approval bind it |

Where two Slots tables carry the same slot, the Owner column above is the
authority; the other table's row is a pointer to it.

### The machine half

Six slots are read by the tools as well as by people, and a value written
only in the prose is not in force:

| Slot | Where the tools read it | As shipped |
|---|---|---|
| `{{SPELLING}}` | `[editorial] spelling` | `"us"`: **enforced against your prose until you change it** |
| `{{DASH_CONVENTION}}` | `[editorial] dashes` | `"no-em-dash"`: likewise enforced |
| `{{REFERENCE_FIELDS}}` | `[registry] required`, and `[registry.by_kind]` | the seven defaults, **required of every entry** until you change them |
| `{{MUTATION_SET}}` | `[vocab] mutations` | empty: the name check is skipped, and says so |
| `{{PARTIES}}` | `[parties] names` | empty: the roster check is skipped, and says so |
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
first day it is one edit.

The commonest case is *register*, which this methodology uses for a
claim's trust level and which several fields use for a primary source.

### Sixteen slots, filled five ways

Filled examples, so you can see the shape a real value takes. Each list is
a historian of medicine, an empirical microeconomist, a molecular
biologist, a scholar of contract law, and a machine-learning researcher.

**`{{PROJECT_TITLE}}`**
- Fever admissions and the house surgeon's diagnoses at a London fever hospital, 1848 to 1866
- Minimum-wage spillovers in the hourly wage distribution, 2010 to 2019
- Transcriptional consequences of one gene's knockdown in a colorectal cell line
- Assumption of responsibility as a remoteness test in the English and Commonwealth courts
- Sharpness-aware minimization against stochastic gradient descent across seeds

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
- the researcher; the assistant; a paid transcriber; the holding repository's archivist, where a reading came by correspondence
- the researcher; the assistant; a coauthor; a research assistant; an independent replicator; the data provider's output-control officer
- the researcher; the assistant; the bench collaborator who runs replicates; the sequencing facility; the coauthor who re-analyzes from raw reads
- the researcher; the assistant; a named colleague who reads each authority blind at the pinpoint; the journal's cite-checker
- the researcher; the assistant; one named coauthor who runs the baselines

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
- a journal article of about nine thousand words with footnotes in the house style, drafted in markdown and rendered for submission
- a journal article in a typesetting system, an online appendix carrying the same version, and a replication package
- a research article with figures and legends, methods, supplementary tables, and a source-data file per panel; released with the deposited data
- a law review article of about fifteen thousand words including footnotes, with a table of cases and a table of legislation
- a conference paper with an appendix of experiments, released with the code at a tag, the configurations, and the per-seed metrics

**`{{SPELLING}}`**
- UK English, the *-ise* ending; quotations keep the source's spelling (`uk`)
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
- I, with *this article* as the agent of the article's own acts
- we, also for a single author

**`{{VOICE}}`**
- read off two prior articles: the subject of a sentence is the institution, the clerk, or the document, never *the data*; a quotation carries its folio in the note
- state the estimand before the estimator; never a coefficient without its standard error and its clustering level; name the specification by table and column
- methods in the past tense, results in the present; one claim per paragraph anchored to its panel; every quantitative statement with its replicate count and its test
- the proposition in the text and the authority in the footnote; *held* only of the ratio, *said* of dictum
- every result is a mean and a spread over a stated number of seeds; *significantly* only with the test named

**`{{REPLY_HOOK}}`**
- the harness wiring the template ships, named by its folder under `governance/harness/` and by the settings file that folder's README points at. Four of the five fill it the same way, since one wiring ships; a project on another harness fills it with its own, or with *none, with the form kept by hand*
- as shipped
- as shipped
- none, where the work is done in a harness that cannot run a command after a reply, with the form kept by hand and that said here
- as shipped

**`{{DISCLOSURE_RULE}}`**
- the access conditions recorded for each source; nothing quoted beyond what its terms permit
- the agency's minimum cell size and its dominance rule, with the output-control officer on the roster
- the controlled-access conditions of the deposited data, and the consent scope the approval fixed
- none beyond §6: the authorities are public
- none beyond §6: the benchmarks are open

---

## 4. The first round: state the question

Every round begins by logging the prompt. Copy the entry
template under `prompt_logs/` to `001_short_description.md`, the form the
round check reads, paste the prompt verbatim, and only then do the work. That order is the rule, and it is the
first thing the session brief will remind you about.

The first round's work is the two documents that say what the project is
for:

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
   record, the frame its quantities are stated in, and at least one
   mutation from your `{{MUTATION_SET}}`.
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

## 8. Before the first commit

Run the round check. It runs the linter and its own gates together:

```bash
python3 tools/check_round.py
```

Fix what it reports, or record why you did not. Then commit. The
pre-commit hook runs the same check, so a clean run here means a clean
commit.

If you removed the worked example without removing the pointers to it, the
path check reports those pointers, naming the file and the line. That is
the check working, and §1 says what to strike.

If you set up a stop-word list under `.privacy/` (a git-ignored list of
words that must never reach a public repository: collaborator names, an
embargoed topic, an unreleased dataset), `tools/privacy_scan.py` runs
beside it. It is the one mechanism that refuses by default: the hooks call
it only where such a list exists, and `--no-verify` overrides it, with the
reason in the commit message. A strict install makes the round check
refuse too.

---

## 9. And then

You have a project. What to do at each stage from here is
`HOW_IT_FITS_TOGETHER.md`, which also lists **the prompts this methodology
suggests** and when to make each. The first one to make, now that the
slots are filled and every copied file still speaks in the template's
voice, is:

> Make a documentation consistency sweep.

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
every rule. If no check of yours is a program, `python_project/` can go.

**What if my field's word for something clashes?** Rename it. See
`GLOSSARY.md`, *Renaming a word this template uses*. Do it before the
record exists.

**My subject matter keeps tripping a check.** Two answers, in this order.
First, check whether the finding is right: a check that fires on ordinary
prose about your material usually means the sentence is doing two jobs.
Second, if it really is a collision, the configuration has an escape
hatch: `skip` on the artifact row in `tools/artifacts.toml`, with the
reason written beside it. An unexplained skip is worse than the finding.

**What if I disagree with a rule?** Change it. The rulebooks are yours
once you clone them; `FORKING.md` says how to change one legibly, so that
a later reader can see what you did and why. A rule you route around
silently is worse than one you delete on purpose.

**How much of this do I have to do on day one?** The slots, the research
statement, and the keystone. Everything else arrives when the work needs
it: a plan when you are ready to execute, a check when there is something
to verify, the tension ledger when something you find disagrees with what
is published.

**Where does the record end and the paper begin?** The repository is the
primary artifact and the paper is a projection of it. Anything the paper
asserts is in the record first, with its register; the paper says what to
read off the evidence.

**Nobody will read all this.** Nobody should. `ONBOARDING.md` is what a
session reads before working, and it is two pages. This file you read
once. The rulebooks you consult when a question comes up, and the tools
tell you which one.

## Slots

None. This file explains the slots; it fills none, and it is the same in
every project.

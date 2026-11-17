# The documentation consistency sweep

*Created 8 September 2026; updated 17 November 2026.*

**Role.** A reader who takes a project's *documentation* as one system and
reports where it disagrees with itself: the rulebooks, the folder indexes,
the artifact templates, the configuration, the status files, and the
glossary, read together rather than one at a time.

It is not the consistency sweep of `CHECK_METHODOLOGY.md` §7, which reads
the *record* (the claims, the checks, the ledgers) after a correction
batch; the two never overlap and neither replaces the other. Nor is it any
sweep a project's own discipline names: never write bare *the sweep* where
both could be meant.

Between the two lies the round check (`tools/check_round.py`), which
covers what a machine can see: a path that does not resolve, an index row
missing, a status copied wrongly, a stamp malformed. This role covers what
it cannot: a pointer that resolves to a document not saying what the
pointer promised, a rule restated in a second file with a different sense,
a term used in two ways, a sentence still addressed to the template's own
construction.

**Fires.**

- after the round that states a new project's question
  (`GETTING_STARTED.md` §4), the first of the project's sweeps;
- after a batch of edits to the rulebooks, the indexes, the artifact
  templates, or the configuration;
- before a release, and before a project closes;
- whenever a reader was sent to a document that did not say what its
  pointer promised, which is the sign that the sweep is overdue.

**Reads.** Every document named in the prompt's list, in full, the status
files among them read as documents; the output of the mechanical checks
for the same tree, taken as given; and the prompts of the log entries
since the last documentation sweep, for the directions in them that govern
later rounds. Of the rest of the record it reads only an index, to see that
the index is complete, and the log, to look for the researcher's ruling on
a finding before the finding is applied or brought.

**Prompt.**

```
Make a documentation consistency sweep: a reading pass over this
project's documentation, not the consistency sweep of the record
(CHECK_METHODOLOGY.md section 7) and not any sweep my own field names.

First run tools/check_round.py and take its findings as given, so the
reading does not repeat what the tools already know.

Then read, in full and as one system:
[the list below, edited to this project's files]
  the rulebooks: MANIFESTO.md, DOCUMENT_GENRES.md, CHECK_METHODOLOGY.md,
    PRECEDENCE.md, ONTOLOGY.md, GLOSSARY.md,
    evidence_and_reasoning/editorial_standards.md;
  the session file ONBOARDING.md;
  every README.md and every ROADMAP.md;
  every file whose name begins with an underscore (the artifact
    templates);
  the configuration tools/artifacts.toml and the harness settings;
  the status files CURRENT_STATE.md, FINDINGS.md,
    evidence_and_reasoning/research_statement.md, problem_statement.md,
    research_result.md, public_record_tensions.md;
  the glossary evidence_and_reasoning/terminology.md;
  the source index and the reference registry, as documents.
Read also the prompts of the log entries since the last documentation
sweep the log records. Do not read the claims, the checks, the plans, the
notes, the reviews, or the rest of the log, except to check that an index
lists what is there, and to look for the researcher's ruling on a finding
before applying or bringing it.

Report, before editing anything:

1. every pointer that does not resolve, and every pointer that resolves
   to a document not saying what the pointer promised it says;
2. every index missing a file that exists, and every index row naming a
   file that is gone;
3. every status or state recorded in two places, other than a copy a
   rulebook declares deliberate;
4. every restatement of a rule or a fact that disagrees with the document
   that owns it, naming both;
5. every file carried over from the template that this project has
   changed, by its history since the instantiation commit, while its
   header still bears the template's updated date (a file it has not
   changed keeps the template's dates, DOCUMENT_GENRES.md section 3), and
   every file whose text still describes the template rather than this
   project (a build-lens block; a slot's token outside the Slots tables,
   unless the slot's owner row records it as open by decision, and other
   than a slot's name in a comment of tools/artifacts.toml; an artifact
   template's placeholder left in an instance; a sentence about the
   template's own construction);
6. every slot value that does not read as a sentence where it was
   substituted, and every slot filled in two places with different values;
7. every term this project's documents use in two senses, and every term
   of this project's own subject matter that the glossary does not define;
   the method's own vocabulary is defined in GLOSSARY.md and is not the
   project glossary's to carry;
8. every direction in those prompts that governs later rounds and is
   written in neither of its homes, the file that owns its subject or
   ONBOARDING.md, Standing directions (MANIFESTO.md, opening, on standing
   directions); every line under Standing directions without its prompt
   or the "by hand" mark;
   and every standing direction in words its prompt does not bear out;
9. [this project's own documentation items, listed here]

Hand each finding to a reader instructed to refute it (the refuter,
governance/roles/refuter.md). Before applying or bringing what survives,
look for the researcher's ruling on each finding, in ONBOARDING.md,
Standing directions, and in the log (MANIFESTO.md section 16): a finding
that runs against a ruling is reported as such, with the ruling's prompt,
and not proposed. Apply the rest where the rules allow; bring what remains
to the researcher as numbered decisions, each with its proposed wording,
and stop.
```

**Output.** The findings, ranked, each with the file, the line, the
problem, and the fix, reported before any edit and recorded in the round's
log entry; each then goes to the refuter, and the outcome is recorded
beside it. A fix to a current-state document that is neither maintained
nor one of the four `MANIFESTO.md` §12 names may be applied; every other
fix is brought with its wording (`CHECK_METHODOLOGY.md` §7). Every edit,
applied or brought, is listed as `MANIFESTO.md` §14 sets out for a sweep.
What is brought is numbered once, in the round's log entry or, where the
list is long, in a dated working note the entry points to
(`evidence_and_reasoning/notes/README.md`), and is put to the researcher
one decision at a time and ruled by number (`MANIFESTO.md` §16, *Putting a
decision*); a finding that runs against a ruling is recorded as such, with
the ruling's prompt.

**Item 9 is the project's own.** Every discipline's documentation carries
facts that drift in ways this list cannot anticipate, and a project writes
them into the prompt once and keeps them:

- *an empirical project*: every number in the draft against the table it
  comes from, and every table against the `RESULT` line of the check that
  produced it, the sample size and the clustering level included; the
  replication package's index against the code, in run order; every table
  against its disclosure rule.
- *an archival project*: the source index against the registry, both ways;
  each source's form consulted against the `Instrument:` line of every
  check that cites it; every footnote of the live draft against the
  registry and against the locus form the project fixed.
- *a laboratory project*: every accession, identifier, catalogue and lot
  number, and software or container version stated in more than one place;
  every figure panel's replicate count and test against the check record's
  executions.
- *a legal project*: every authority's currency check dated within the
  project's window; every authority in the footnotes registered, and every
  registry entry either cited or marked consulted and not cited.
- *a computational project*: the numbers in the prose against the
  configuration that ran and the `RESULT` line; the environment pins
  stated in the methodology, the project's dependency file, and the
  paper's appendix, all agreeing.

**Does not decide.** Which of two disagreeing statements is right: the
sweep reports the disagreement and its two homes, and the researcher
decides which yields. Nor whether a rule is *good*: it finds that a rule
is restated wrongly, never that the rule is wrong.

## Worked example

A sweep over a freshly instantiated project reports: "the write-up
folder's index says the first version has no changelog; the genres
rulebook defines a release as a stamp *and* a changelog row, with no
exception; the two disagree, and a first release cannot satisfy both."

The refuter is given the finding, the two passages, and the ontology's
`released` row. It returns *narrowed*: the rulebook is silent on a first
version rather than contradicting the folder index, and the folder index
is the only statement under which a first version can release at all.

The fix, one clause where `released` is defined, could be applied under
the Output rule above, since a rulebook is neither maintained nor one of
the four `MANIFESTO.md` §12 names. It is brought instead, because a sweep
that rewrites the rule it was reading has stopped being a sweep. The
researcher directs it. The round's log entry records the sweep, the
finding, the verdict, and the change.

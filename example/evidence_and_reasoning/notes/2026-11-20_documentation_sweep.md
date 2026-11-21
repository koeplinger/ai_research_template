# The first documentation consistency sweep: 20 November 2026

*Created 20 November 2026; updated 20 November 2026.*

**Working note.** Nothing here may be cited as a result.

## What was asked

The documentation consistency sweep prompt 003 asked for, the project's
first (`governance/roles/documentation_sweep.md`), with this project's
item 10 written into its prompt first. The reading was split among four
readers by item, as the prompt allows: items 1 and 2; 3 and 4; 5, 6 and
7; 8, 9 and 10. Each reader read every document on the list in full for
its items, and each finding went to a refuter of its own
(`governance/roles/refuter.md`). The readers and refuters were subagents
that wrote nothing.

## What was found

**The round check**, taken as given: one finding, ROUND-2 on entry 003,
the entry of the round then in progress, whose closing status was not
yet written.

**Read in full.** Between them the four readers read in full every
document on the prompt's list: the seven rulebooks; `ONBOARDING.md`; the
three pages of the guide; `governance/reminders.md` and the seven role
files; every `README.md` and the plan index; every file whose name begins
with an underscore; `tools/artifacts.toml` and `.claude/settings.json`;
the docstrings of the programs under `tools/` and
`governance/harness/`, and the leading comment of `tools/install_hooks.sh`;
the six status files; `evidence_and_reasoning/terminology.md`; and the
source index and the registry, read as documents. Of the log they read
the prompts of entries 001 to 003, there being no earlier sweep. Every
file on the list was named by at least one reader, so the main thread
had none left to read.

**The findings**, 35, numbered in the order the readers returned them,
with each refuter's verdict. The refuters refuted 8, narrowed 18, and let
9 stand. Ranked by severity, those that survive:

| # | Rank | Where | Finding, as it survives its refuter | Verdict | Outcome |
|---|---|---|---|---|---|
| 17 | high | `evidence_and_reasoning/terminology.md` | the project glossary defines none of the project's own terms: *market day*, *the roll*, a *row* of it | narrowed: the terms need entries; the definitions are the researcher's | brought, decision 7 |
| 28 | high | `ONBOARDING.md`, *Standing directions* | prompt 001's direction for every round, that one session plays both parties and writes every prompt, is written in neither of its homes | narrowed: the line under *Standing directions* is a home for it | applied, A7 |
| 1, 9, 34 | medium | `evidence_and_reasoning/research_statement.md`, `problem_statement.md` | both statements say the project holds the two files, and it holds neither: the source index has no row | 1 narrowed, 9 and 34 stand | brought, decision 1 |
| 2, 31 | medium | the owner rows of the three waiting slots | the marker reads "filled when a write-up is opened"; the ruling reads "until the note is opened", and in this project *the note* also names a source | narrowed: record the researcher's meaning, in the researcher's words | brought, decision 6 |
| 7 | medium | `README.md` | entry 001 says the front page states the three departures; it states none | narrowed: insert the paragraph, or correct forward | applied, A2 |
| 8, 32 | medium | the keystone's *What it takes as given*; the research statement's second line of work | the calendar year as the year's boundary is the assistant's reading, unlabeled in the two files that hold the researcher's words | narrowed: confirm it, or label it | brought, decision 2 |
| 10 | medium | `DOCUMENT_GENRES.md` §3, the row for `FINDINGS.md` | it says only a substantial change to a finding needs the researcher; `MANIFESTO.md` §12 says every change | stands | applied, A3 |
| 18, 19 | medium, low | `terminology.md` | *the note* serves four senses and *shipped* two, with no entry choosing the project's | narrowed: entries, governing new prose | brought, decision 7 |
| 29 | medium | every log entry's `By:` line | the AI model is withheld on the assistant's own reason; no prompt gives the direction | narrowed: bring it as a decision | brought, decision 8 |
| 30 | medium | both statements' second line of work | "set aside to a plan of its own" adds a commitment prompt 002 does not make | stands | brought, decision 3 |
| 4 | low | `MANIFESTO.md`, its table of named files | `VISION.md`, named in its opening, and the settings file, named in a slot value, have no row | narrowed: both rows, reworded | brought, decision 9 |
| 3 | low | `CURRENT_STATE.md` | the file the pointers name for where the project stands holds only the template's comments | narrowed: the research goal now; the rest once the holding is settled | applied, A1 |
| 6 | low | `README.md`, *The files at the root* | `.gitignore` and `.gitattributes` are not named | narrowed: a presentation choice | brought, decision 14 |
| 12 | low | the keystone, under H-A | "Plans serving it: none yet." copies what each plan's `Serves:` line records | narrowed: a bare pointer, or the deletion | brought, decision 5 |
| 14 | low | the research statement's scope | the count for 1852, not pursued, is recorded in both statements | stands | brought, decision 4 |
| 15 | low | `governance/roles/documentation_sweep.md`, *Worked example* | it says a rulebook's fix could be applied, though `FORKING.md`, *A rule*, has an amendment made at the researcher's direction | narrowed: an ordinary fix to the role file | applied, A4 |
| 16 | low | `tools/install_hooks.sh`, the pre-commit hook | without python3 the hook refuses every commit, where no privacy list is set up and the hooks are not strict | stands | brought, decision 12 |
| 20 | low | `evidence_and_reasoning/checks/README.md` | the check-form value, pasted whole, reads heavily | narrowed: a short handle | applied, A5 |
| 21 | low | `README.md`, its header | the front page carries the setup run's Created date, where a carried-over file keeps the template's | stands | brought, decision 13 |
| 24 | low | `tools/README.md` | a clause speaks to projects made before the setup tool kept the shipped configuration; this one has it | narrowed: that clause alone | applied, A6 |
| 33 | low | `LICENSE.md`, *In a project built from the template* | it still directs adding a holder and a citation, which answer 21 ruled out | narrowed: bring the ruling's words | brought, decision 10 |
| 35 | low | `source_documents/README.md` | its rule asks a checksum only where the origin publishes one, while the instrument of record names one for every held source | narrowed: a project rule to bring | brought, decision 11 |

**Refuted, and dropped**, each with its refuter's reason:

- 5, `GETTING_STARTED.md`: the guide's account of the setup tool is the
  project's on purpose, and its head says so.
- 11, `FORKING.md`: *immutable* there names a genre, as
  `DOCUMENT_GENRES.md` uses it, not a commit.
- 13, the keystone's "no claim exists yet": the sentence speaks of
  inception, and stays true of it.
- 22, the keystone's *held*, *count*, *row*: no method word is misused;
  none of the sentences reads two ways.
- 23, two comments in `tools/artifacts.toml`: neither is false in this
  project, nor narrates its own text.
- 25, `governance/harness/README.md`: nothing in the passage is false
  here; the guide names the setup tool on purpose.
- 26, `python_project/README.md`: true of this project, which kept the
  suite.
- 27, `LICENSE.md` beside answer 21: the ruling answers what the file
  asks; finding 33 carries what survives.

**The edits applied**, each to a current-state file that is neither
maintained nor one of the four `MANIFESTO.md` §12 names, and none against
a ruling:

- A1, `CURRENT_STATE.md`, after the comment under *Research goal*: "The
  question as posed is `evidence_and_reasoning/research_statement.md`,
  and the thesis, one hypothesis (H-A), is
  `evidence_and_reasoning/problem_statement.md`."; after the comment
  under *What is open*: "H-A is untested, and no plan is drafted."
- A2, `README.md`, after the paragraph on the question, a paragraph:
  "This project is a worked example, and it departs from the rules in
  three ways for every round, as `prompt_logs/001_setup.md`,
  *Corrections and departures*, records: one assistant session plays
  both parties and writes every prompt in the researcher's role; nothing
  is committed at the end of a round, the project being committed once
  when the example is complete; and each log entry's `By:` line
  withholds the AI model."
- A3, `DOCUMENT_GENRES.md`, the row for `FINDINGS.md`: "adding, removing,
  or substantially changing a finding requires the researcher's
  authorization" becomes "every change at the researcher's direction, a
  correction of wording or a pointer included (`MANIFESTO.md` §12)".
- A4, `governance/roles/documentation_sweep.md`, *Worked example*: "could
  be applied under the Output rule above, since the rulebook is neither
  maintained nor one of the four `MANIFESTO.md` §12 names. It is brought
  instead, because" becomes "amends a rule rather than bringing a
  restatement into line with it, and an amendment is made at the
  researcher's direction (`FORKING.md`, *A rule*), so it is brought:".
- A5, `evidence_and_reasoning/checks/README.md`: "; its form is" and the
  value pasted after it become ", and here takes one of the two forms
  that file's Slots table fixes: a program for a count or a calendar fact
  read off the roll, or a written collation procedure for what the note
  states."
- A6, `tools/README.md`: the clause from "; one made before the setup tool
  kept the copy" to "under that of the configuration" is removed, the
  sentence ending at "over that copy as well."
- A7, `ONBOARDING.md`, *Standing directions*, a third line: "Who plays the
  researcher, and who writes each prompt: \"In this example one assistant
  session plays both parties, so every prompt in this log, this one
  included, is written in my role by that session, and the log says
  so.\" (prompt 001)"

## What follows

Fourteen decisions, brought for the researcher's ruling by number. Each
gives the options and their consequence; the assistant's recommendation
follows the options, labeled as its own. A ruling that changes a
document is applied in the round that records it.

1. **The two statements say the project holds the roll and the note**
   (findings 1, 9, 34). The research statement: "its results are results
   about the two files it holds"; the keystone: "It rests on two files
   the project makes and holds". Options: (a) leave both, the sources
   round making them true; (b) reword both now, to "the two files made
   for it" and "two files the project makes and will hold". The
   assistant recommends (a), with the sources brought in next.
2. **The calendar year as the year's boundary** (findings 8, 32): stated
   in both statements as "a choice of this project", which is the
   assistant's reading of prompt 002. Options: (a) confirm it, and the
   text stands with the confirming prompt as its source; (b) choose
   another boundary, and the text changes to it; (c) leave it open, and
   both passages are labeled in place as the assistant's reading. The
   assistant recommends (a) or (b), since every count is stated in this
   frame.
3. **"set aside to a plan of its own what it cannot"** (finding 30), in
   both statements' second line of work, where prompt 002 says "set
   aside what it cannot". Options: (a) confirm the words; (b) cut them
   to the prompt's. No recommendation: it is what the researcher meant.
4. **The count for 1852, not pursued, recorded twice** (finding 14).
   Options: (a) delete the research statement's bullet, the keystone's
   §3 keeping the line and its date; (b) keep both. The assistant
   recommends (a): the question already names 1851.
5. **"Plans serving it: none yet."** under H-A (finding 12). Options: (a)
   replace it with "The plans serving it are those whose `Serves:` line
   names it (`research_plans/ROADMAP.md`)."; (b) delete it; (c) keep it,
   updated at the researcher's direction as each plan opens. The
   assistant recommends (a).
6. **Which note answers 11, 14 and 15 mean** (findings 2, 31): "Leave it
   open until the note is opened." Options: (a) the project's own
   write-up, and the three markers stand, the meaning recorded in the
   researcher's words in the round that rules; (b) the source, and the
   three slots are due before the collation. The assistant recommends
   that the researcher say which, in words of their own.
7. **The project glossary** (findings 17, 18, 19). Proposed entries in
   `evidence_and_reasoning/terminology.md`, *Project-specific terms*:
   *market day*, a row of the roll, whatever its kind; *the roll*, the
   synthetic market roll of 1851 and 1852; *row*, one line of the roll's
   CSV, one day held; *the note*, the fictional source note alone, the
   project's own writing being *the write-up*; *shipped source file*, a
   source made for the project and held under `source_documents/`. The
   definitions are the researcher's: (a) take them as proposed; (b) give
   others. The assistant recommends (a), with *market day* fixed before
   any count is run.
8. **The AI model on a `By:` line** (finding 29). Options: (a) a standing
   direction to withhold it, in the researcher's words, under
   `ONBOARDING.md`, *Standing directions*; (b) no direction, and later
   entries follow `MANIFESTO.md` §8: the model as the harness reports
   it, or *not reported*. The assistant recommends (a), since the
   example ships inside a template that names no AI model.
9. **The manifesto's table of named files** (finding 4). Options: (a) two
   rows: "`VISION.md` | the template's statement of intent" and
   "`.claude/settings.json` | the harness settings the reply hook is run
   from"; (b) the first row alone; (c) neither. The assistant recommends
   (b): the settings file is named only in a slot's value, which may
   change.
10. **`LICENSE.md` and answer 21** (finding 33). Options: (a) the
    instruction to add a holder and a citation gives way to the ruling's
    words, "Keep the template's licenses and add no holder or citation:
    this example lives inside the template's repository." (prompt 001);
    (b) leave the file. The assistant recommends (a).
11. **A checksum in every held source's row** (finding 35). Options: (a)
    add to `source_documents/README.md`: "In this project every held
    source's row records its SHA-256 checksum, whatever its origin
    publishes, since the instrument of record names it
    (`CHECK_METHODOLOGY.md`, *Slots*)."; (b) leave the rule as shipped.
    The assistant recommends (a), before the sources come in.
12. **The pre-commit hook without python3** (finding 16). It refuses
    every commit, which the manifesto's opening allows only of a refusal
    to commit what would leak. Options: (a) leave the tool as the
    template ships it, noted for the template; (b) change the hook in
    this project to refuse only where a privacy list exists or the hooks
    are strict. The assistant recommends (a): the tool is the template's,
    and nothing is committed in this project before its end.
13. **The front page's Created date** (finding 21). Options: (a) the
    template's front page's Created date, 2 September 2026, as
    `DOCUMENT_GENRES.md` §3 has a carried-over file keep; (b) the day the
    setup tool wrote the page, as it stands. The assistant recommends
    (a).
14. **`.gitignore` and `.gitattributes` on the front page** (finding 6).
    Options: (a) a row naming them; (b) leave the table to its `*.md`
    scope. The assistant recommends (b).

# Market days in a synthetic market roll

*Created 6 September 2026; updated 6 September 2026.*

A worked example of the research template: a small, complete project
instantiated from the template, taken through its first plan from the
research statement to a released note, and then through a review of the
whole. Everything in it is synthetic by design: the market roll under
`source_documents/` is produced by a program shipped beside it, the
"published" note it is compared with was written for the exercise, and
nothing here is a claim about the world. What the example shows is the
process: the artifacts, the rounds, the checks, the registers (a claim's
trust level), and the mechanical checks that gate a round, all passing.

## The fence

This example is a snapshot. It was instantiated from the template at
commit `a460878` on 6 September 2026, by the steps its first log entry
records, and its rulebooks and tools are copies as of that commit.
Changes to the template's methodology after that commit do not propagate
here: the example may fall out of step with the refined rulebooks and
the guide, and where it does, it is flagged for deletion or a complete
re-do at the researcher's word, never patched into the shape of every
later rule. A small incremental update (a re-copied tool, a corrected
sentence) is allowed and is recorded in this example's own log; the whole
example is not re-run because a rule changed. Nothing in this example is
ground truth for the template: where the two disagree, the template's
rulebooks govern. Files copied from the template keep the template's
Created date; their updated date is the day the example last changed
them. The licenses are the template's own, since the example is part of
the template's repository; a project replaces them as `LICENSE.md` says.

To see what the template has changed since the snapshot, from the
template's root:

```bash
git diff a460878 HEAD --stat -- MANIFESTO.md DOCUMENT_GENRES.md CHECK_METHODOLOGY.md PRECEDENCE.md ONTOLOGY.md ONBOARDING.md tools/ governance/
```

## Two roles, who played them

The rulebooks name two parties, the researcher and the assistant. In
this example both were played by one assistant session, the one that
built the template, at the template researcher's direction to produce
the example: it wrote every prompt in the researcher's voice and
executed it. So every act the rulebooks reserve to the researcher
(engaging and closing the plan, assigning registers, directing the
release, entering the tension rows and the findings) was performed by
the assistant in the researcher's role, and the record says so where the
label carries weight: a second pass recorded as the researcher's role is
not an independent party's, and a reader should not take it as one. The
log's "I" is that role's voice.

## Reading it

A newcomer's path, about an hour. `ONBOARDING.md` is the assistant's
session file, read afterwards to see what a session sees.

1. This file (5 minutes).
2. `MANIFESTO.md`, *Words used throughout* and sections 5, 8, 12, and
   16 (15 minutes): the parties, verification, the log, corrections, the
   status block.
3. `CHECK_METHODOLOGY.md` sections 1, 2, and 8, and `DOCUMENT_GENRES.md`,
   *Words used here* (10 minutes): registers, claim kinds, the shape of
   a check, the plan lifecycle.
4. The log, the entries under [prompt_logs/](prompt_logs/) in order
   (10 minutes): what was asked and done in each round, and what the
   last entry corrected.
5. The record (15 minutes): the research statement and the keystone
   under [evidence_and_reasoning/](evidence_and_reasoning/); plan 001;
   claim 001 with check 001 and its program; claim 002 with check 002,
   the procedure form; claim 004 with check 003, a check that fails by
   design; the tension ledger; `FINDINGS.md` and `CURRENT_STATE.md`.
6. The note under [paper/](paper/) and its review (10 minutes): in the
   review's findings table, row 4 is a finding that needed a check the
   record lacked, row 7 one the refuter refuted, row 9 a content cut the
   researcher's role approved; the deletion ledger is what a rebuild
   owes.

Keys the record uses: a claim token names a file under
`evidence_and_reasoning/claims/`, a check token one under
`evidence_and_reasoning/checks/`; [Roll1851] and [Note1] are the two
sources registered in `evidence_and_reasoning/references/sources.md`; a
finding key is a row of `FINDINGS.md` and a tension key a row of the
tension ledger. The tools resolve them, so they are written bare. H-A is
the keystone's one hypothesis, that the roll and the note disagree on
1851. A slot is a project-specific value in a rulebook's Slots table. The
reminder that log entry 005 mentions is the findings-gate reminder of
`governance/reminders.md`, printed by `tools/session_brief.py` at the
start of a session.

## Running it

From this folder, each of these runs clean:

```bash
python3 tools/check_round.py            # the round check: every mechanical gate, one command
python3 tools/check_concordance.py      # each check program's RESULT line against its record
python3 tools/falsifiability_probe.py   # each program under the mutations it names
python3 tools/check_residue.py          # what a rebuild left in the live drafts
python3 tools/session_brief.py          # the reading order, the plans, the reminders
python3 tools/run_ledger.py status      # what is stale
cd python_project && python3 -m pytest -q tests && python3 src/check_001_count_1851.py
```

Check 003 fails by design: its failing verdict is the result, backing a
claim registered RULED_OUT; the probe does not judge its mutation for
that reason, and its record states what the mutation does.

## The files at the root

| File | What it is |
|---|---|
| [MANIFESTO.md](MANIFESTO.md) | the operating rules, with this project's slots filled in its Slots table |
| [DOCUMENT_GENRES.md](DOCUMENT_GENRES.md) | the three genres and what the checker verifies |
| [CHECK_METHODOLOGY.md](CHECK_METHODOLOGY.md) | registers, claim kinds, the shape of a check |
| [PRECEDENCE.md](PRECEDENCE.md) | which artifact wins when two disagree |
| [ONTOLOGY.md](ONTOLOGY.md) | the predicates and their surface syntax |
| [ONBOARDING.md](ONBOARDING.md) | the reading order for a session, and the standing directions |
| [VISION.md](VISION.md) | the template's statement of intent, carried over because the rulebooks cite it (log entry 008) |
| [CURRENT_STATE.md](CURRENT_STATE.md) | where the project stands |
| [FINDINGS.md](FINDINGS.md) | what the record has established |
| [LICENSE.md](LICENSE.md), [LICENSE-CODE](LICENSE-CODE) | the licenses, the template's own |
| [tools/](tools/), [governance/](governance/), [evidence_and_reasoning/](evidence_and_reasoning/), [paper/](paper/), [prompt_logs/](prompt_logs/), [python_project/](python_project/), [inherited/](inherited/), [source_documents/](source_documents/) | the folders, each with its own README |

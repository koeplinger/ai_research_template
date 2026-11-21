# Prompt 001: set up the project from the template

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
Make a new project from this template, for a small worked example. Its
subject: the market days of a fictional town, read from a synthetic
market roll of 1851 and 1852 and set against a fictional note that states
a count of market days for 1851. Both sources will be made for the
project and shipped with it, and nothing in it may be a claim about the
world.

In this example one assistant session plays both parties, so every
prompt in this log, this one included, is written in my role by that
session, and the log says so.

Put the setup questions to me together, numbered, with your
recommendation after the options where you have one, and I will answer
by number.

1. None: nothing here is private.
2. Market days in a synthetic market roll
3. documentary historian of administrative records
4. the shipped source file at the SHA-256 checksum its row in the source index records: the roll read with the Python standard library at a stated version, the note read at its page marks
5. a program with a printed verdict for a count or a calendar fact read off the roll; a written collation procedure, one dated execution per reading, for what the note states
6. shift-year, every date of the roll moved one year later; drop-month, one month's rows removed; duplicate-entry, rows of the roll repeated; alter-figure, a figure in a transcribed passage changed
7. none
8. row, for the roll; page, for the note; section, for either
9. the seven defaults
10. the shipped source file itself, at the checksum its row in the source index records, for any claim about what that file holds or states; nothing outside the project backs a claim here
11. Leave it open until the note is opened.
12. US English
13. no em-dashes; a range takes the word to
14. Leave it open until the note is opened.
15. Leave it open until the note is opened.
16. the wiring this repository carries, `governance/harness/claude_code/`, run from `.claude/settings.json`
17. none beyond §6: the sources are synthetic files made for this project
18. Yes, as shown.
19. No: the sources are made for this project, and nothing is to be looked up outside the repository.
20. None.
21. Keep the template's licenses and add no holder or citation: this example lives inside the template's repository. Start date 20 November 2026.
22. No rename.
23. The Python check suite stays.
24. Call the folder market-days, outside the template's clone, and keep the answers file outside both.
--- PROMPT END ---

## What was done

The exchange above is two prompts: the request, and the answers by
number to the 24 decisions the assistant then put together, as the
request asked. Each answer is the researcher's ruling on its decision, in
the researcher's words above. The decisions, in the order put, each with
the assistant's recommendation after its options where it had one,
labeled as the assistant's:

- 1, the privacy list, put first, before anything could be committed.
- 2 to 17, the sixteen slots, in the order and the plain words of
  `GETTING_STARTED.md` §3. Answers 11, 14 and 15 leave the three slots
  that may wait for a write-up open by decision.
- 18, the values the tools read, worked out from the answers and shown:
  spelling `us`, dashes `no-em-dash`, the mutation set's four short names
  (`shift-year`, `drop-month`, `duplicate-entry`, `alter-figure`), the
  roster `["none"]`, and the seven required registry bullets.
- 19 and 20, the two standing directions.
- 21, the licenses and the start date; 22, a header field to rename; 23,
  the Python check suite; 24, the new project's folder and where the
  answers file goes.

The answers file was written outside both trees: the thirteen slot
values given, the three waiting slots blank, the values of decision 18,
the start date of decision 21, and no copyright holder, citation, or
rename. The setup tool was run once from the template's clone, with that
file and `--yes`. Its printed steps:

- it copied the 81 tracked files a project keeps, leaving behind the
  template's own construction, and removed the 6 pointers to it;
- it stripped 25 build-lens blocks and lens sections; the shipped prose
  already used US spelling;
- it filled 13 of the 16 slots and wrote the values the tools read; it
  kept the template's configuration as it shipped, for the tools'
  self-tests;
- it renamed no field and left the licenses as the template's own;
- it initialized the folder as a git repository and installed the hooks;
- it wrote the front page, `README.md`, and the setup note,
  `evidence_and_reasoning/notes/2026-11-20_setup.md`, which says what the
  run did and what it left to be done;
- it stamped the 17 files it changed with 20 November 2026;
- its round check in the new tree: 0 findings over 83 files.

The tool named four sentences where a long value was substituted and may
not read: `CHECK_METHODOLOGY.md` at lines 17, 63 and 169, and
`evidence_and_reasoning/checks/README.md` at line 11. They are left to
the documentation consistency sweep, which reads them
(`GETTING_STARTED.md` §4).

By hand, in the new project, before anything was committed:

- No privacy list was written: answer 1 is none, given by writing no
  list (`GETTING_STARTED.md` §1, *Arm the privacy scan*).
- The two standing directions, under `ONBOARDING.md`, *Standing
  directions*, each in the researcher's words with this prompt.
- The open-by-decision marker in the owner row of each waiting slot:
  `DELIVERABLE` in `DOCUMENT_GENRES.md`'s Slots table, `PAPER_PRONOUN`
  and `VOICE` in `evidence_and_reasoning/editorial_standards.md`'s.
- The Python check suite was kept, and nothing was added under
  `[registry.by_kind]`.
- This entry, and its row in `prompt_logs/README.md`.

No plan is proposed at setup, and the question is the next round's.

## Corrections and departures

This one entry records the whole setup exchange and follows the run it
records, because the log, like the project, did not exist before the run
(`GETTING_STARTED.md` §4).

This example departs from the rules in three ways, for every round, and
its front page says so:

- One assistant session plays both parties, at the template researcher's
  direction. It writes every prompt in the researcher's role and carries
  it out, so the question and the thesis, every ruling, and every act
  the rulebooks reserve to the researcher (engaging and closing a plan,
  assigning a register, entering a finding or a tension row, directing a
  sweep, approving a content cut, directing the release) are that
  session's, written in the researcher's role (`MANIFESTO.md` §1, §2, §5,
  §10, §12).
- Nothing is committed at the end of a round. By the template
  researcher's choice, the project is committed once, when the example
  is complete, into the template's repository. Every log entry is
  therefore read as not yet committed, and the checks that read the
  version history are replaced by reading (`MANIFESTO.md` §8;
  `GETTING_STARTED.md` §4).
- The `By:` line withholds the AI model, which the harness reported: the
  template names no AI model in what it ships, and this example ships
  inside it (`MANIFESTO.md` §8).

## Closing status

```
DONE: the project made from the template; 13 slots filled and three left open by decision; the standing directions written
WAITING ON YOU: the research question, in the next round
```

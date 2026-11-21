# Prompt 019: the front page's account of the example; the last documentation sweep

*Created 21 November 2026; updated 21 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
Yes, make the sweep. Before it, put on the front page what a reader of
this example needs to know first: that it is an illustration to browse,
not a project to run or to start from; that one session played both
parties; that it was committed once, at the end; that it was made from
the template at commit 73ca267, on 20 and 21 November 2026; that the AI
model is withheld; that its tools are not kept working from inside the
template's example folder; and how to read it. Then the sweep, over what
has changed since the last one, and bring me what it finds.
--- PROMPT END ---

## What was done

The researcher said to make the sweep, after putting on the front page
what a reader of this example needs to know first.

**The front page.** `README.md` has a new section, *About this example*,
in place of its paragraph on the three departures: what the example is
for, the five things a reader should know before relying on it, and three
ways to read it. The departures stay recorded in
`prompt_logs/001_setup.md`.

**The documentation sweep** (`governance/roles/documentation_sweep.md`),
over the 15 documents on its list changed since round 015, what states
the same status, count, or pointer as one of them, and the prompts of
entries 016 to 019: four readers by item (1 and 2; 3 and 4; 5, 6 and 7;
8, 9 and 10), the second also reading the new section statement by
statement against the record, and a refuter for each of the 10 findings,
14 subagents in all, none of which wrote anything. The share of usage
they took is not known: the harness reports none. The tree was recorded
by the checksum of every file before they started and compared after
they returned: no file had changed. Each reader named all 15 documents
among those it read in full. The refuters narrowed 9, let 1 stand, and
refuted none.

| Findings | Rank | Where | What | Refuter | Outcome |
|---|---|---|---|---|---|
| 2, 10 | high, medium | the front page, *About this example* | "a single assistant session did the work" leaves out the subagents that made the second passes, audits, refutations, and blind review | narrowed, medium | applied |
| 7 | medium | the glossary | it has no entry for *counting convention*, the name of plan 002's question | narrowed: the proposed definition confined the term to kinds and dates | brought, decision 1 |
| 3 | medium | `prompt_logs/README.md`, `paper/reviews/README.md` | each says the AI model is named, where this example withholds it | narrowed, low | applied |
| 1, 5 | low | `CURRENT_STATE.md`, *What is open* | "is the question of plan 002" promises more than the plan, which asks only which listed convention gives forty-eight | stands; narrowed on the fix's wording | applied |
| 4 | low | the front page | "copies from that commit" leaves out what setup and the rounds changed | narrowed | applied |
| 6 | low | the glossary's opening | "it is cited", where two established terms name no work, as prompt 016, decision 4, ruled | narrowed: the exception confined to those two | applied |
| 8 | low | the glossary, `python_project/src/README.md`, `python_project/src/roll.py` | the calendar year is called the frame of every count, which stops being true at plan 002's first count on another year | narrowed: true today, and owed by that round | carried into plan 002's deliverables |
| 9 | low | `CURRENT_STATE.md`; the registry | *held* in two senses in one sentence, and in one bullet of the registry | narrowed: the registry's use misleads no one | applied to the first; the second left |

Left, with its reason: the registry's "the program held with it" keeps
the word in the sense that file uses throughout, and no reader can take
it for a program that took place.

**Brought, one decision**, with its options and the assistant's
recommendation after them:

1. **A glossary entry for *counting convention*** (finding 7). Under
   *Project-specific terms*, and in the glossary's index: "### counting
   convention (project-specific). A rule for which of the roll's rows
   count toward the note's year, such as one on a row's kind or on the
   dates the year runs between. The note's own convention is unknown
   [tension T001]; plan 002 states a list of conventions to test."
   Options: (a) add it; (b) reword it; (c) leave it out. The assistant
   recommends (a).

The round check: no finding.

## Corrections and departures

None of this round's own; the three departures entry 001 lists hold.

## Closing status

```
DONE: the front page's account of the example written; the last documentation sweep made, 10 findings, its fixes applied
WAITING ON YOU: one decision: a glossary entry for counting convention
```

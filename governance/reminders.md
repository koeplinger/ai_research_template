# Reminders: the standing instructions, each named and placed where it fires

*Created 5 September 2026; updated 8 September 2026.*

`MANIFESTO.md` §16 has the assistant say, once in its reply, what the
stage of work calls for and has not been done. This file names each
standing instruction, says what fires it, what it outputs, and what it
does not decide. The ones the record itself can compute are printed by
`tools/session_brief.py` at session start and on demand (`--reminders`),
or reported by the linter, as the *Computed by* column says; the rest are
the assistant's by reading. A reminder is
advisory: it says, it records nothing, and it acts only with direction.

| Reminder | Fires when | Output | Computed by | Does not decide |
|---|---|---|---|---|
| **log-the-prompt-first** | a round opens and no entry of it is open under the log: the latest entry is committed, or the log is empty (`MANIFESTO.md` §8) | the latest entry's name, and that this round's entry is the first act | `session_brief.py` at session start and on `--reminders`; at each later round of the same session the assistant runs `--reminders` or reads for it | what the prompt was; nor whether an open entry is this round's, since an earlier round's entry left uncommitted reads as open; a committed entry edited is not open but the linter's GENRES-2 |
| **more-than-one-plan-engaged** | more than one plan's `Status:` line reads `ENGAGED`; the index shows the same (`DOCUMENT_GENRES.md` item 6; `evidence_and_reasoning/research_plans/README.md`) | the plans, named; the reply says so while it is true | `session_brief.py` | which plan owns what: each plan's *Out of scope* does |
| **plan-closure-checklist** | an `ENGAGED` plan's execution ledger has every task done or dropped; the plan stays `ENGAGED` until the researcher closes it (`DOCUMENT_GENRES.md`, *Words used here*) | that the plan is ready to close, and the checklist below | `session_brief.py` | the verdict: the researcher's, against the pre-registered criteria |
| **sweep-after-correction** | the body of a frozen artifact differs from its committed version in the working tree, a header-only change being bookkeeping (`DOCUMENT_GENRES.md`); a correction batch to a current-state artifact, or one already committed at a round boundary, is the assistant's by reading (`CHECK_METHODOLOGY.md` §7: a sweep closes every correction batch) | the artifacts, named | `session_brief.py` for the uncommitted frozen case; reading for the rest | whether the batch is complete; the sweep's items are reading |
| **findings-gate** | a claim registered `VERIFIED` or `RULED_OUT` is cited by no row of the findings file (`MANIFESTO.md` §12); it recurs at every session start while that holds | the claims, named; the assistant brings the finding and its wording and stops, and reads past a proposal the researcher has declined, which the round's log entry records | `session_brief.py` | whether it is a finding: the researcher's |
| **verification-not-recorded** | a claim registered beyond `OPEN` or `SPECULATIVE` carries `Verified-by: unchecked` (`MANIFESTO.md` §5; `CHECK_METHODOLOGY.md` §1, *Backed by*) | the claims, named | `session_brief.py` | who should check it, or by what route |
| **reference-not-registered** | a work is leaned on and has no registry entry (`MANIFESTO.md` §2) | the linter's ONT-2 finding names the token | `lint_docs.py` for an unresolved token; a work leaned on without a token is reading | the entry's standing (§3): reading |
| **tension-row-not-entered** | a divergence was found and its row brought but not yet entered at the researcher's direction (`PRECEDENCE.md`) | the row, restated in the reply | reading | whether the row enters: the researcher's |
| **finding-proposed-not-brought** | the assistant has proposed a finding in work and not yet put it to the researcher (§12) | the proposal, in the reply | reading | what counts as a finding |
| **second-pass-not-taken** | a non-trivial conclusion is about to be presented without its independent second pass (§5) | the pass taken, or the statement that it was not | reading | the route the discipline requires: `CHECK_METHODOLOGY.md` §3 |
| **documentation-sweep-owed** | the rulebooks, the indexes, the templates, or the configuration have been edited as a batch, or the project has just been instantiated and its slots filled (`governance/roles/documentation_sweep.md`) | a proposal to make the documentation consistency sweep, with the prompt | reading | whether to make it: the researcher's |
| **adversarial-review-owed** | a claim is about to be relied on and has had no structured adversarial review (§17) | a proposal to run the refuter or the referee (`governance/roles/`) | reading | whether to run it: the researcher's |

## The plan-closure checklist

Printed by name when a plan is ready to close; the items are the
rulebooks', gathered in one place.

1. Every task in the execution ledger is done or dropped, a drop naming
   the log entry that approved it (`evidence_and_reasoning/research_plans/_template.md`).
2. The sanity checks hold: every existing check still holds, a program
   re-run and a written procedure not invalidated (the plan template's *Sanity checks*).
3. The round check is clean and the indexes are in step
   (`tools/check_round.py`).
4. The pre-registered confirmation and refutation criteria decide the
   verdict, or, where they decide neither way and the plan was executed as
   designed, it closes `INCONCLUSIVE`, unless the plan pre-registered what
   such an outcome closes as; a plan whose execution stopped closes
   `ABANDONED`, and one with no hypothesis closes `COMPLETE` on its closure
   criterion (`evidence_and_reasoning/research_plans/README.md`).
5. Every claim the plan owns carries the register the researcher assigned
   (`CHECK_METHODOLOGY.md` §1) and, where `VERIFIED` or `RULED_OUT`, names
   its backing check (`ONTOLOGY.md` §5, check 5); any finding the plan's
   claims support has been brought with its wording and entered or
   declined at the researcher's direction (`MANIFESTO.md` §12: what counts
   as a finding is the researcher's).
6. The docket is resolved in the closing round (`CHECK_METHODOLOGY.md`
   §6).
7. Everything the plan owns is in its final wording, since it freezes on
   closure (`DOCUMENT_GENRES.md`, *Artifacts of an open plan*).
8. The researcher writes the `CLOSED` line, or directs it, and the
   round's log entry is the provenance.

## How to add a reminder

Name it, say what fires it, what it outputs, and what it does not decide,
in the table above; where the record can compute the trigger, add it to
`tools/session_brief.py` with a self-test case, and say in the table that
it is computed. A reminder that fires on nothing decidable is still a
reminder: the assistant reads for it.

# Onboarding: what every session must know before it works

*Created 4 September 2026; updated 4 September 2026.*

This file is read at the start of every assistant session, before any
substantive action. Reading it, and then the manifesto in full, is the
assistant's duty (`MANIFESTO.md`, opening paragraph); where the harness
can present a file at session start, that wiring is recorded where the
harness configuration lives, and the manifesto defines no slot for it.
This file points; the rulebooks govern:
[`MANIFESTO.md`](MANIFESTO.md), [`DOCUMENT_GENRES.md`](DOCUMENT_GENRES.md),
[`CHECK_METHODOLOGY.md`](CHECK_METHODOLOGY.md),
[`PRECEDENCE.md`](PRECEDENCE.md), [`ONTOLOGY.md`](ONTOLOGY.md).

> **Build lens.** No session works on a research project here; this file
> ships as the template's onboarding and is filled by the project. The
> build's own onboarding is `MANIFESTO.md` with its build-lens blocks.

## The first minutes

    ONBOARDING.md (this file)
      -> prompt_logs/: open this round's entry from _template.md,
                       the first act of the round (MANIFESTO.md section 8)
      -> MANIFESTO.md, read in full
      -> CURRENT_STATE.md            the state of the research as a whole
      -> FINDINGS.md                 what the record has established
      -> evidence_and_reasoning/README.md, and its reading order

If the slots are still unfilled, the round is setup: follow
`GETTING_STARTED.md` and stop at every slot for the researcher's value.

## Precedence

This repository may contain claims established here that the public
record does not carry. Per `PRECEDENCE.md`: a `VERIFIED`, `RULED_OUT`, or
`DERIVED` claim of this project governs over the public record and over
the assistant's own priors, at exactly the scope the claim states; never
"correct" a passage toward what the literature says because the
literature says it. The rule runs both ways: the public record is never
promoted to established fact without a check, and a claim is never
inflated past its wording. The assistant applies the trump rule on its
own only for a claim whose register the researcher has assigned;
otherwise it states the claim with its verification status, proposes the
ledger row, and stops. Every divergence is brought as a tension-ledger
row in the same round, and the row enters at the researcher's direction.

## The keystone

The researcher's thesis, as hypotheses evidence could count against, is
[`evidence_and_reasoning/problem_statement.md`](evidence_and_reasoning/problem_statement.md):
`SPECULATIVE`, the thing being tested, trumping nothing.

## Standing constraints

The manifesto is the complete statement; these are the rules a session
meets in its first minutes.

- **Every prompt is logged** (`prompt_logs/`, immutable once committed;
  numbering contiguous).
- **Unsure means stop** (`MANIFESTO.md` §4).
- **Every non-trivial answer gets a second pass** by an independent route
  before it is presented (§5).
- **The researcher performs every commit**, engages every plan, and
  closes every plan. The assistant reports work ready and stops.
- **A register is the researcher's to assign**; the assistant proposes it
  with its evidence (`CHECK_METHODOLOGY.md` §1).
- **Four current-state files change substantively only with the
  researcher's authorization**: `FINDINGS.md`, the keystone, the research
  statement, and the manifesto (§12).
- **A frozen artifact is corrected only with authorization**: bring the
  finding and the proposed wording, and stop.
- **Read what the task names**, and outside the repository only what the
  researcher points at (§10).
- **A subagent writes no tracked file**; the main thread makes every edit
  (§14).
- **Disagreement is said where it is about to be relied on** (§17).
- **Every reply ends in a status block** (§16), and before handing work
  back the round check is run: `tools/check_round.py`.

## Standing directions

<!-- The researcher's standing directions, one line each with the prompt
     that set it, so a session knows them without re-deriving them. Do
     not copy slot values here: the instrument of record is
     CHECK_METHODOLOGY.md section 3, the mutation set and parties are
     ONTOLOGY.md's Slots, spelling and pronoun are
     editorial_standards.md's Conventions. -->

## Slots

None.

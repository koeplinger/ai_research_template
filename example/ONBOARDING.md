# Onboarding: what every session must know before it works

*Created 4 September 2026; updated 6 September 2026.*

This file is read at the start of every assistant session, before any
substantive action. Reading it, and then the manifesto in full, is the
assistant's duty (`MANIFESTO.md`, opening paragraph); where the harness
can present a file at session start, that wiring is recorded where the
harness configuration lives, and the manifesto defines no slot for it.
This file points; the rulebooks govern:
[`MANIFESTO.md`](MANIFESTO.md), [`DOCUMENT_GENRES.md`](DOCUMENT_GENRES.md),
[`CHECK_METHODOLOGY.md`](CHECK_METHODOLOGY.md),
[`PRECEDENCE.md`](PRECEDENCE.md), [`ONTOLOGY.md`](ONTOLOGY.md).

## The first minutes

    ONBOARDING.md (this file)
      -> prompt_logs/: open this round's entry from _template.md,
                       the first act of the round (MANIFESTO.md section 8)
      -> MANIFESTO.md, read in full
      -> CURRENT_STATE.md            the state of the research as a whole
      -> FINDINGS.md                 what the record has established
      -> evidence_and_reasoning/README.md, and its reading order

A reader who is not a working session skips the log entry and reads the
log itself, the entries under `prompt_logs/` in order; `README.md` gives
that reader's order.

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

- Nothing in this project is a claim about the world; both sources are
  synthetic and shipped with it (prompt 001).
- Every act the rulebooks reserve to the researcher is the researcher
  role's, and the log records it as such; in this example the role is
  played by the assistant, as `README.md` says (prompt 001).
- The two sources say in every place that they are synthetic (prompt 002).

## Slots

None; the slots of this project are filled in the rulebooks' Slots tables.

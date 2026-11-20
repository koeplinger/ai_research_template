# Onboarding: what every session must know before it works

*Created 4 September 2026; updated 19 November 2026.*

This file is read at the start of every assistant session, before any
substantive action. Reading it, and then the manifesto in full, is the
assistant's duty (`MANIFESTO.md`, opening paragraph and *Words used
throughout*); where the harness can present a file at session start,
that wiring is recorded where the harness configuration lives, and the
manifesto defines no slot for it.
This file points; the rulebooks govern:
[`MANIFESTO.md`](MANIFESTO.md), [`DOCUMENT_GENRES.md`](DOCUMENT_GENRES.md),
[`CHECK_METHODOLOGY.md`](CHECK_METHODOLOGY.md),
[`PRECEDENCE.md`](PRECEDENCE.md), [`ONTOLOGY.md`](ONTOLOGY.md),
[`GLOSSARY.md`](GLOSSARY.md),
[`evidence_and_reasoning/editorial_standards.md`](evidence_and_reasoning/editorial_standards.md).

> **Build lens.** No session works on a research project here; this file
> ships as the template's onboarding and is filled by the project. The
> build's own onboarding is `MANIFESTO.md` with its build-lens blocks. A
> prompt asking to make a project from this clone is setup at a prompt:
> its record is entry 001 of the new project (`GETTING_STARTED.md` §4),
> and nothing is logged here.

## The first minutes

    ONBOARDING.md (this file)
      -> MANIFESTO.md, read in full
      -> prompt_logs/: read the latest entry, and the paragraph below if
                       it is still open; then open this round's entry
                       from _template.md, the first act of the round
                       (MANIFESTO.md section 8)
      -> CURRENT_STATE.md            the state of the research as a whole
      -> FINDINGS.md                 what the record has established
      -> evidence_and_reasoning/README.md, and its reading order

The latest entry may be a resume point, which says where to start
(`HOW_IT_FITS_TOGETHER.md`, *Make a durable resume point*). Where it is
still open, its closing status not written, compare what it records with
the working tree and with every commit made since its round opened, and
treat what that round drafted as unverified. Then close it, with a
closing status saying why, or, if the researcher has committed it, leave
it for this round's entry to complete (`MANIFESTO.md` §8). A process of
that round still running passes to this round, whose entry names it and
whose replies report it; a verification of that round that stopped
before its end is run again in this round, before anything rests on it.

If a slot's owner row carries neither a value nor the open-by-decision
marker, or *Standing directions* below lacks the two directions settled at
setup, the round is **setup**, and `GETTING_STARTED.md` walks it through:
the questions of its §3, put to the researcher one at a time, each answer
written where the slot's owner defines it; the setup decisions that are
not slots, listed at the end of its §1; and any field name the project's
own discipline has taken, renamed in `tools/artifacts.toml` under
`[fields.roles]` before any artifact carries it (`GLOSSARY.md`, *Renaming
a word this methodology uses*). Setup proposes no plan, and of the write-up
puts only its three slots' questions, each of which may wait
(`GETTING_STARTED.md` §3), never what it will say. The rounds after
setup, and their order, are `GETTING_STARTED.md` §4.

## Precedence

This repository may contain claims established here that the public
record does not carry. Per `PRECEDENCE.md`: a `VERIFIED`, `RULED_OUT`, or
`DERIVED` claim of this project governs over the public record and over
the assistant's own priors, at exactly the scope the claim states; never
"correct" a passage toward what the literature says because the
literature says it. The rule runs both ways: the public record is never
promoted to established fact without a check, and a claim is never
inflated past its wording. The assistant applies the trump rule on its
own only for a claim whose register the researcher has assigned; for one
the assistant alone has checked, it states the claim with its
verification status, proposes the ledger row and the prose, and stops.
Every divergence is brought as a tension-ledger row in the same round,
save one found outside a fixed list being finished, which is kept and
listed when the list is handed back (`PRECEDENCE.md`, *Compliance*); the
row enters at the researcher's direction.

## The keystone

The researcher's thesis, as hypotheses evidence could count against, is
[`evidence_and_reasoning/problem_statement.md`](evidence_and_reasoning/problem_statement.md):
`SPECULATIVE`, the thing being tested, trumping nothing.

## Standing constraints

The manifesto is the complete statement; these are the rules a session
meets in its first minutes.

- **Every prompt is logged** (`prompt_logs/`, immutable once committed;
  numbering contiguous).
- **A direction that governs later rounds is written down in the round it
  is given**: in the file that owns its subject, or under *Standing
  directions* below (`MANIFESTO.md`, opening, on standing directions).
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
  finding and the proposed wording, and stop; bring the trivial
  corrections a round finds together, as one numbered list; a released
  version of a versioned write-up is never corrected (§12).
- **Read what the task names**, and outside the repository only what the
  researcher points at (§10).
- **The researcher's words are recorded as theirs, and no further**: a
  reading that goes further is labeled the assistant's, and an
  authorization is never inferred (§2, §10).
- **A subagent writes nothing into the working tree**; the main thread
  makes every edit, and checks the tree when subagents return (§14).
- **Disagreement is said where it is about to be relied on** (§17).
- **Decisions are put one at a time**, unless the researcher asks for
  several, numbered, in plain words, each with its options and their
  consequences (§16).
- **A ruled matter stays ruled**: look for the ruling before asking or
  proposing anything (§16).
- **Every reply ends in a status block** (§16), and before handing work
  back the round check is run: `tools/check_round.py`.

## Standing directions

<!-- The researcher's standing directions, one line each with the prompt
     that gave it, or "by hand" where the researcher wrote it outside a
     round and its commit is the provenance, in the researcher's words,
     quoted where they fit (MANIFESTO.md section 2), so a session knows
     them without re-deriving them. Two are settled at setup: whether the assistant may search the
     public record for the standing of a work it registers (MANIFESTO.md
     section 3), and what identity, if any, the assistant and its
     subagents may give an outside service that asks for one, recorded by
     what it is and never by the address itself (MANIFESTO.md section 6).
     Do not copy slot values here: the instrument of record and the
     mutation set are CHECK_METHODOLOGY.md's Slots, the parties and the
     citation locus are ONTOLOGY.md's, spelling and pronoun are
     editorial_standards.md's Conventions. -->

## Slots

None.

# Vision

A template for AI-assisted research.

This document states what this repository is for, who it serves, what it will
contain, and how its parts are meant to work together. It is the reference every
other artifact here answers to. It describes intent and principle; it does not
schedule work.

---

## Goal

Provide a repository that a researcher clones at the start of a project and works
inside for its duration, which helps them use AI assistance to produce
professional, publication-ready results.

The template originates in mathematics and physics, which is where its author's
practice was formed. It is not built for those fields. A historian, a biologist,
an economist, a legal scholar, or a machine-learning researcher should find the
structure natural and the vocabulary theirs. Where a discipline-specific choice is
unavoidable — which tools count as authoritative, what a verification looks like,
what a publishable deliverable is — the template provides a named slot the
researcher fills, not a default that quietly assumes a field.

---

## Context

AI assistance has changed what a single researcher can attempt. It has not changed
what makes research trustworthy. The gap between those two facts is where most
AI-assisted work goes wrong.

The failure is rarely stupidity and rarely dishonesty. It is that a capable
assistant produces fluent, plausible, well-organized output faster than a human can
scrutinize it, and the ordinary defenses of research practice were built for a
slower rate of claim production. Specific ways this shows up:

- **Fluency read as evidence.** A well-written paragraph and a verified result look
  identical on the page. Confidence in the prose gets mistaken for support.
- **Provenance lost in conversation.** The real work happens in a chat window. What
  lands in the repository is the conclusion, stripped of how it was reached, and it
  cannot be reconstructed a month later — by the researcher or by anyone else.
- **Silent revision.** A later finding contradicts an earlier one, the earlier text
  is quietly rewritten, and the fact that a position changed disappears along with
  the reason it changed.
- **Unfalsifiable claims.** Statements accumulate that no one has said how to check,
  so no one checks them.
- **Scope drift.** Each step is locally reasonable; the destination is somewhere the
  researcher never chose to go.
- **Retrofitted narrative.** The write-up presents a clean line of reasoning that
  nobody actually walked.

Researchers have asked the author for the methodology he uses to avoid this. This
repository is that methodology, made free and open so it can be used, criticized,
and forked without permission.

---

## Scope

This template is for researchers who are honest.

That is a real precondition, not a courtesy. The template makes integrity cheap and
drift visible. It cannot detect a researcher who decides to deceive themselves or
their readers, and it does not try. Every mechanism here can be satisfied
superficially by someone determined to do so. Nothing here is a control in the
audit sense.

More specifically, it assumes a researcher who:

- wants to identify original work, and has the drive to pursue it;
- is realistic about what they know and what they do not;
- can distinguish what they intend to learn during the project from what they are
  content to defer to an assistant or an external tool, and is willing to write that
  distinction down;
- accepts that a claim they have not checked is a claim they do not yet hold.

What the researcher must not delegate is judgment: what counts as an answer, what
standard of evidence applies, which questions matter, and the final opinion. An
assistant can survey, draft, compute, cross-check, argue against a position, and
maintain the record. It cannot own the conclusion. The template's job is to keep
that boundary explicit and written down rather than implicit and drifting.

The deliverable to the researcher is a working repository, plus a guide covering
what the template provides, how to get started, how the components fit together,
and what to do at each stage of a project.

---

## What the template provides

Three things that are meant to be one system.

### Artifacts

The documents and directories a project is built from: the place where sources
live, the place where derived analysis lives, the record of what has been claimed
and what has been checked, the record of how a conclusion was reached, and the
documents that become the publication.

The organizing commitment is that **the repository is the primary artifact**. The
paper is a projection of it. A reader with the repository and nothing else — no
conversation history, no memory of the sessions that produced it — should be able
to follow the work, continue it, or attack it. If the work only exists in the
researcher's head or in a chat log, it is not done.

The artifact set is shipped as templates with worked examples, so that starting a
project is filling in a structure rather than inventing one.

### Ontology

The artifacts share a vocabulary. That vocabulary is the Ontology, and it is a
first-class deliverable rather than documentation.

The Ontology defines the **predicates** research statements are expressed in — the
relations that hold between claims, sources, evidence, methods, and each other.
Illustratively, and subject to being worked out properly: what it means for one
thing to *cite* another, to *derive* from it, to *assume* it, to *verify* or
*refute* it, to *supersede* it, to *depend on* it, to be *measured against* it, or
to be *deferred to* an external tool — and what verification *status* a claim
currently carries.

The point of naming these is that a predicate is not merely defined, it is
**implemented**: it appears in the artifact templates, it can be checked, and it
can be queried across the repository. That is what makes the artifacts one system
instead of a folder of unrelated forms. It is what allows questions like *which
claims rest on something unverified*, *what changed when this result was
overturned*, or *what is this conclusion actually standing on* to be answered by
looking, rather than by remembering.

A shared vocabulary is also what makes assistance reliable. An assistant that knows
the predicates knows what kind of statement it is being asked to produce and what
would make that statement adequate.

### Governance

Mechanisms that keep the discipline running when attention lapses. They come in
four kinds:

- **Reminders** — surfacing what the stage of work calls for, before it is skipped.
- **Checks** — the requirement that specific classes of claim be verified, and that
  the verification be recorded rather than asserted.
- **Opposition** — structured argument against the researcher's own position:
  adversarial review of a claim, a deliberate case for the opposite conclusion, a
  standing role whose job is to find what is wrong. Assistants are agreeable by
  default, and a research process that never contradicts the researcher is not
  supporting them.
- **Support** — scaffolding, templates, and worked examples, so the right thing to
  do is also the easy thing to do.

These are advisory by design. They fire, they inform, and they leave the decision
with the researcher. A mechanism that blocked work would be routed around within a
week, and routing around it would leave no trace. One that speaks up and records
what it said keeps the record honest either way.

---

## Expectation

A researcher clones the repository, sets up their project quickly, receives clear
guidance on how to begin, and continues to receive it as the project proceeds.

Given honesty on the researcher's side, the mechanisms hold the work to a standard
worth publishing. That is the bet this template makes, and it should be read
precisely: the template cannot make results correct. It makes provenance
recoverable, claims explicit, verification status visible, disagreement recorded,
and revisions traceable. Robustness follows from a researcher working honestly
inside that structure — not from the structure alone.

### The repository is the researcher's

Every mechanism here can be modified, replaced, or deleted. A project will develop
needs this template did not anticipate, and a researcher who adapts the governance
to their work is using it correctly, not abandoning it.

What the template asks in return is that departures be **deliberate and legible**.
A mechanism removed on purpose, with the reason recorded, is a considered choice. A
mechanism that decayed without anyone noticing is how the failure modes in the
Context section get back in. The template's aim is to make the difference between
those two visible.

---

## Non-goals and limits

- It does not judge the quality of research questions, nor supply originality.
- It does not detect or prevent dishonesty, self-deception, or motivated reasoning.
- It is not a compliance framework, a lab notebook standard, or a regulatory
  instrument, and should not be represented as one.
- It does not replace peer review, domain expertise, or the researcher's judgment.
- It does not endorse or require any particular AI assistant, model, or vendor.
- It is not a guarantee. **There is no warranty and no promise of fitness for any
  purpose.** A researcher using this template is responsible for their results.

---

## Licensing

Free and open, in two parts:

- **Code** — MIT License.
- **Documents** — Creative Commons Attribution 4.0 International (CC BY 4.0).

Code is licensed permissively so it can be lifted into any project without
friction. Documents carry attribution because a methodology should be traceable to
where it came from, and because a researcher adapting it should be able to show
what they started from and what they changed. Both licenses permit commercial use,
modification, and redistribution.

---

## What success looks like

- A researcher clones this, and is doing real work the same day.
- A year later, someone else opens that repository and can tell what was claimed,
  what was checked, what changed, and why — without asking anyone.
- A researcher can state plainly which parts of their work they verified themselves
  and which they deferred, because the repository already records it.
- The mechanisms catch something the researcher would have missed, at least once.
- Someone forks the template, disagrees with it, and produces something better.

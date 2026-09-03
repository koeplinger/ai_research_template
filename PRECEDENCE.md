# Precedence: what governs when sources disagree

*Created 2 September 2026; updated 3 September 2026.*

A research project that verifies things independently will, sooner or
later, establish something the published record does not say, or says
otherwise. From that moment two failures are possible, and they are
opposite. A session, human or assistant, that lets the published record
silently override what this project established corrupts the work. A
session that lets enthusiasm for this project's results silently override
the published record corrupts it in the other direction. This file is the
rulebook that prevents both, and the **tension ledger** is where every
divergence stays visible.

Until a project establishes something the record does not carry, this
rulebook costs nothing: the tiers still apply, and the ledger is empty.

> **Build lens.** The template establishes nothing and cites nothing, so
> its tension ledger ships empty. The rulebook is shipped, not applied.

## Words used here

- A **divergence** is a pair of statements, one a claim of this project
  and one from the public record, that cannot both hold at the scope the
  claim states. A different result on a different sample, edition, period,
  or definition is not a divergence until the claim says it is. A
  difference of emphasis is never one.
- **Context** is prose that makes no claim of this project: borrowed
  material, carried at its tier with the hedge the writing discipline
  below requires. Context carries no register and is never cited as a
  result.
- The **public record** is what `DOCUMENT_GENRES.md` defines: the
  published literature, reference works, editions, and published estimates
  outside the repository.
- The **tension ledger** is `evidence_and_reasoning/public_record_tensions.md`.
  It is a ledger, not a register: `DOCUMENT_GENRES.md` reserves *register*
  for a statement's trust level.

---

## The order of authority

For any statement made while working in the project, authority descends in
exactly this order.

1. **This project's claims** in the registers `CHECK_METHODOLOGY.md` §1
   reaches by a gated check or an independently cross-checked argument:
   `VERIFIED`, `RULED_OUT`, and `DERIVED`, together with the checks and
   cross-checks that back them. Within this tier a claim means *exactly
   what its wording says*: the scope it states, any explicit statement of
   what it does not claim, and its register are all part of the claim.
2. **The sources of record**: what a source *actually says*, collated
   against the source itself in the form the project designates, whether
   held under `source_documents/` or, where access conditions keep it out
   of the repository, consulted at its recorded locator, shelfmark, or
   release and indexed there (`MANIFESTO.md` §6). This is authority about
   what the source **says**, never about what is **true**. A claim of this
   project resting on such a collation is `ATTESTED`.
3. **Registered references**: works cited but not collated here. Their
   canonical identity is authoritative; their content is not.
4. **The public record at large**: published literature not registered
   here, reference works, and textbook knowledge. Lowest, always.

**Which tier a statement speaks from is decided by its register**
(`CHECK_METHODOLOGY.md` §1).

| The statement | Speaks from |
|---|---|
| a claim registered `VERIFIED`, `RULED_OUT`, or `DERIVED` | tier 1 |
| a claim registered `ATTESTED` | tier 2, and only about what the source says |
| a claim registered `OPEN` or `SPECULATIVE` | no authority: an open question is not an answer, and a speculative claim is the thing being tested |
| a cited registered reference, not collated | tier 3, by its citation and not by any register |
| public-record material in prose | tier 4, carried as context with its hedge, never by a register |

**The assistant's own priors and the researcher's memory are not a tier.**
A recollection that conflicts with any tier is checked against the record
before anything is written, and a ledger row is added only when the record
itself disagrees.

## The trump rule

> **Where tier 1 and tier 4 conflict, tier 1 governs**, in every document,
> every calculation, and every judgment call made while working here. The
> divergence itself is **recorded, never suppressed**: it goes into the
> tension ledger with this project's side, the public record's side, and
> whatever caution survives.

The failure this exists to prevent is concrete: an assistant, or a
researcher working from memory, "corrects" a passage back toward what the
literature says, because the literature says it. The passage was right.

**Who may apply it.** The assistant applies the trump rule on its own only
for a claim whose register the researcher has assigned
(`CHECK_METHODOLOGY.md` §1). Where a claim the assistant alone has checked
diverges from the public record, the assistant states the claim with its
verification status (`MANIFESTO.md` §5), proposes the ledger row and the
prose, and stops.

## The rule runs in both directions

**Tier 4 is never promoted silently.** A public-record statement becomes
established fact here only by being gated by a check of this project,
which yields a claim. Otherwise it is used at its tier: collated and cited
`ATTESTED` (tier 2), cited as a registered reference (tier 3), or carried
in prose as context with its hedge (tier 4). The tell of a silent
promotion is a sentence that states a borrowed fact flatly, with no
citation and no hedge, in prose that elsewhere cites everything.

**And tier 1 does not inflate.** The trump rule covers what a claim
states, at the scope it states. It does not extend to paraphrases,
generalizations, or the `SPECULATIVE` register. A summary that drops a
claim's statement of what it does not claim has inflated the claim.

## Cautions survive the trump

Overriding the public record never deletes a caveat. Where a fact
established here stands in tension with published material, the ledger
keeps both sides visible: what this project establishes, what the public
record says, and any caution that remains live.

A result established here while the search for a prior statement of it is
still open is the pattern: the result trumps, and the possibility that it
is already known, under another name, in another literature, or in an
edition not yet consulted, remains an open caution, on the ledger, not
erased by the result.

## Compliance

- **The tension ledger** is a maintained document
  (`DOCUMENT_GENRES.md`): current state, changed at the researcher's
  direction. The assistant brings the proposed row in the same round as
  any work that creates or discovers a divergence, and whenever registered
  material conflicts with a claim of this project; the row enters at the
  researcher's direction. A divergence brought and not yet entered is a
  standing reminder (`MANIFESTO.md` §16).
- **Session onboarding** loads this rule into every assistant session at
  its start.
- **Writing discipline.** A `VERIFIED` or `RULED_OUT` claim is stated as
  what it is, with its claim citation, and is not softened merely because
  the public record has not caught up. A `DERIVED` claim is stated at its
  register, with its route. The scope, the uncertainty, and the statement
  of what is not claimed are part of the claim and are never a hedge. The
  inverse hedge is mandatory: public-record material used in prose carries
  its tier (*"the published version prints ..."*, *"the paper states
  ..."*, *"standard references give ..."*).

## What is checked mechanically

Nothing beyond what `CHECK_METHODOLOGY.md` checks for registers and what
`DOCUMENT_GENRES.md` checks for current-state documents, which together
cover this file and the ledger.

Whether a divergence has been recorded at all, whether a caution is still
live, and whether a tier 4 statement has been silently promoted are
matters of reading. They are the assistant's duty in every round that
touches a claim or a reference, and item 8 of the consistency sweep
(`CHECK_METHODOLOGY.md` §7) is where they are caught.

## What this rulebook does not do

It does not make this project infallible. A tier 1 claim is overturned by
a **better verification**: a failing check, a mutation the probe catches,
a correction the researcher authorizes. It is never overturned by an
appeal to the literature. If the public record one day supplies a
demonstration that contradicts a claim here, the route is the same as for
any suspected defect: register the source, gate the disagreement as a
check, and bring the finding under `MANIFESTO.md` §12. **Authority here
follows verification, not publication.**

Nor does it settle priority. That a result is absent from the public
record is not evidence that it is new; establishing novelty requires a
search, and the ledger's caution column is where the state of that search
is recorded.

---

## The tension ledger

One table, five columns, one row per divergence. Rows are **never
deleted** because this project's side "won": that is the point of the
ledger.

| # | What this project establishes | What the public record says | The caution that survives | Caution |
|---|---|---|---|---|
| T001 | the claim, with its citation and its register | the published statement or consensus, plainly and without polemic, with where it is said | what remains live | live, or closed D Month YYYY |

The key `T###` is assigned once and never reused; `[tension T###]`
resolves to the row (`ONTOLOGY.md` §1.3). The last column is read as
recorded; whether a caution is *still* live is reading.

### How to add a row

State this project's side with its claim citation and its register. State
the public record's side plainly, without polemic, and name where it is
said. Name the caution that survives. **A row whose caution column is
empty is suspect**: almost every divergence leaves one, and the commonest
is that no systematic search of the literature has been made, so the
absence is established for what was searched and not for the record at
large.

Where the tension is **reversed**, this project deferring to the record
rather than the other way round, say so in the row: background this
project takes from the literature and never gates is context, and the
ledger records that the trump rule does not cover it.

## Slots

None. The tiers, the trump rule, and the ledger are the same in every
discipline. What differs is what fills tier 2, which
`source_documents/README.md` records, and what counts as a check, which
`CHECK_METHODOLOGY.md` records.

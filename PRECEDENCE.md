# Precedence: what governs when sources disagree

*Created 2 September 2026; updated 2 September 2026.*

A research project that verifies things independently will, sooner or
later, establish something the published record does not say, or says
otherwise. From that moment two failures are possible, and they are
opposite. A session, human or assistant, that lets the published record
silently override what this project established corrupts the work. A
session that lets enthusiasm for this project's results silently override
the published record corrupts it in the other direction. This file is the
rulebook that prevents both, and the **tension register** is where every
divergence stays visible.

Until a project establishes something the record does not carry, this
rulebook costs nothing: every tier below still applies, and the register
is empty.

> **Build lens.** The template establishes nothing and cites nothing, so
> its tension register ships empty. The rulebook is shipped, not applied.

---

## The order of authority

For any statement made while working in the project, authority descends in
exactly this order.

1. **This project's VERIFIED and RULED OUT claims**, and the checks that
   gate them: established here, second-passed, and shown falsifiable
   (`CHECK_METHODOLOGY.md`). Within this tier a claim means *exactly what
   its wording says*: its scope lines, its *what is not claimed* section,
   and its register are part of the claim.
2. **The sources of record** held under `source_documents/`: what a
   registered document *actually says*, verified against the document
   itself rather than against a rendering, a quotation, or a summary of
   it. This is authority about what the source **says**, never about what
   is **true**.
3. **Registered references**: the canonical identity (a DOI, an archival
   shelfmark, a dataset release) of works cited but not held here and not
   independently established here.
4. **The public record at large**: published literature not registered
   here, reference works, textbook knowledge, and the assistant's own
   training priors. Lowest, always.

**Which tier a statement speaks from is decided by its register**
(`CHECK_METHODOLOGY.md`).

| Register | Speaks from |
|---|---|
| `VERIFIED`, `RULED OUT` | tier 1 |
| `DERIVED` | tier 1 once its independent cross-check is recorded; until then it carries no authority and is cited as this project's unfinished work |
| `ATTESTED` | tier 2, and only about what the source says |
| `OPEN`, `SPECULATIVE` | no authority: an open question is not an answer, and a speculative claim is the thing being tested |

A registered reference the project has neither held nor established sits
at tier 3 whatever anyone believes about it.

## The trump rule

> **Where tier 1 and tier 4 conflict, tier 1 governs**, in every document,
> every calculation, and every judgment call made while working here. The
> conflict itself is **recorded, never suppressed**: it goes into the
> tension register with this project's side, the public record's side, and
> whatever caution survives.

The failure this exists to prevent is concrete: an assistant, or a
researcher working from memory, "corrects" a passage back toward what the
literature says, because the literature says it. The passage was right.

## The rule runs in both directions

**Tier 4 is never promoted silently.** A public-record statement, however
standard, becomes usable as established fact here only by being gated (a
check, a claim of this project), or registered as a source of record and
cited as tier 2 (*"the source states"*), or explicitly marked ATTESTED or
as context. Textbook results, standard histories, and this project's own
ungated readings of registered works stay at their tier. The tell of a
silent promotion is a sentence that states a borrowed fact flatly, with no
citation and no register, in prose that elsewhere cites everything.

**And tier 1 does not inflate.** The trump rule covers what a claim
states, at the scope it states. It does not extend to paraphrases,
generalizations, or the SPECULATIVE register. A claim's *what is not
claimed* section is part of the claim, and a summary that drops it has
inflated the claim.

## Cautions survive the trump

Overriding the public record never deletes a caveat. Where a fact
established here stands in tension with published material, the register
keeps both sides visible: what this project establishes, what the public
record says, and any caution that remains live. A classification
established here while the search for a received name is still open is the
pattern: the result trumps, and the possibility that the thing already has
a name elsewhere remains an open caution, on the register, not erased by
the result.

## Compliance

- **The tension register**,
  `evidence_and_reasoning/public_record_tensions.md`, is a maintained
  document (`DOCUMENT_GENRES.md`). A row is added **in the same round** as
  any work that creates or discovers a divergence, and whenever material
  is registered whose statements conflict with a claim of this project.
- **Session onboarding** loads this rule into every assistant session at
  its start.
- **Writing discipline.** Project documents state this project's
  established facts *as* facts, with their claim citations, and never
  hedge an established claim merely because the public record has not
  caught up. The inverse hedge is mandatory: public-record material used
  in prose carries its tier (*"the published version prints ..."*, *"the
  paper states ..."*, *"standard references give ..."*).
- **This rulebook and the register are current-state documents**, checked
  for dangling paths like any other (`DOCUMENT_GENRES.md`), and the
  register is listed in the index of `evidence_and_reasoning/`.

## What is checked mechanically

Two items, both reported and neither decided (`MANIFESTO.md` §13):

1. **Every claim carries exactly one register** from the vocabulary of
   `CHECK_METHODOLOGY.md`.
2. **Paths.** This file and the tension register are current-state
   documents, so every repository path they name exists
   (`DOCUMENT_GENRES.md`).

Whether a divergence has been recorded at all, whether a caution is
complete, and whether a tier 4 statement has been silently promoted are
matters of reading. They are the assistant's duty, and the consistency
sweep is where they are caught (`CHECK_METHODOLOGY.md`).

## What this rulebook does not do

It does not make this project infallible. A tier 1 claim is overturned by
a **better verification**: a failing check, a mutation the probe catches, a
correction the researcher authorizes. It is never overturned by an appeal
to the literature. If the public record one day supplies a demonstration
that contradicts a claim here, the route is the same as for any suspected
defect: register the source, gate the disagreement as a check, and bring
the finding under `MANIFESTO.md` §12. **Authority here follows
verification, not publication.**

Nor does it settle priority. That a result is absent from the public
record is not evidence that it is new; establishing novelty requires a
search, and the register's caution column is where the state of that
search is recorded.

---

## The tension register

One table, four columns, one row per divergence. Rows are **never
deleted** because this project's side "won": that is the point of the
register.

| # | What this project establishes | What the public record says | The caution that survives |
|---|---|---|---|
| 1 | the claim, with its citation and register | the published statement, plainly and without polemic | what remains live |

### How to add a row

State this project's side with its claim citation and register. State the
public record's side plainly, without polemic, and name where it is said.
Name the caution that survives. **A row whose caution column is empty is
suspect**: almost every divergence leaves one, and the commonest is that
no systematic search of the literature has been made, so the absence is
established for what was searched and not for the record at large.

Where the tension is **reversed**, this project deferring to the record
rather than the other way round, say so in the row: background this
project takes from the literature and never gated is context, and the
register records that the trump rule does not cover it.

## Slots

None. The tiers, the trump rule, and the register are the same in every
discipline; what differs is what fills tier 2, which
`source_documents/README.md` records, and what counts as a check, which
`CHECK_METHODOLOGY.md` records.

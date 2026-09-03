# Ontology: the predicates the artifacts share

*Created 3 September 2026; updated 3 September 2026.*

The artifacts of a project built from this template are one system, not a
folder of forms, because they share a vocabulary. This file is that
vocabulary. It defines the **predicates** in which claims, sources,
evidence, plans, and provenance are related, and for each one it says the
same four things:

1. **What it relates**, and what the relation means.
2. **Where it is written**: which artifact carries it, in what exact
   surface syntax.
3. **How it is checked**: which tool reads it, or that none can and why.
4. **What it answers**: the question it lets a reader or a tool put to the
   repository.

A predicate that cannot be pointed at in a file is not in this ontology.
There is no separate database: the predicates live in the artifacts, as
header lines, stamps, citation tokens, and governed files, and the tools
read them there. That survives an inattentive researcher only if the
templates pre-print the fields, so that filling in the form *is* writing
the predicate. **Every predicate here must have a template that ships it**
(§8); one that does not is not shipped.

This file **owns the surface syntax** and **the catalogue**. It does not
restate the rules that govern each predicate: those live in the rulebook
named in the Owner column, and the Checked-by column points at that
rulebook's own numbered check rather than repeating or extending it.

> **Build lens.** The template records no research, so every predicate
> here is shipped and none is instantiated. The checks and queries below
> are specified and not yet implemented: the tools arrive with the
> template's own build, and until then the only mechanical check in this
> repository is the privacy scan (`MANIFESTO.md` §13). The build's own
> state lives in `VISION_PLAN.md`, which is not an ontology artifact.

---

## 1. Surface syntax

Four forms carry every mechanically read predicate. A fifth group of
relations is carried in prose and is read, never parsed; those are marked
*prose* in the catalogue and are listed in §2.8.

### 1.1 Field lines

A **header block** is the run of lines from the artifact's title to the
first blank line following the last header line. In a program it is the
module docstring, or the leading comment block where the language has
none; citation tokens are read from docstrings and comments only, never
from code.

A **field line** is `<Name>: <value>`, the name matched case-sensitively
from the catalogue, at most once per artifact, the value running to the
end of the line. Where a document italicizes its header, the surrounding
emphasis marks are not part of the value.

```
Register: VERIFIED
Kind: documentary
Verdict: confirmed
Plan: 003, task 2
Depends-on: 011, 014
Backed-by: [check 021]
Verified-by: assistant, collation against the source of record
Instrument: the 1543 edition, consulted as a digital surrogate
Frame: the base manuscript's foliation, fixed in [claim 002]
Mutation: variant-reading, base-witness-swap
Robustness: modernized-spelling
Prerequisites: 001, 002
Serves: H-B
```

### 1.2 Stamps

A **stamp** is a header line that takes **no colon**, because a colon
after a date opens a change narrative and the genre checker rejects it
(`DOCUMENT_GENRES.md`). There are exactly five:

```
Created 12 August 2026; updated 3 September 2026
Released 25 August 2026
Reserved 12 August 2026, plan 006a
Pre-registered 4 August 2026, evidence_and_reasoning/notes/2026-08-04_protocol.md
superseded by paper/capstone_v2.md
```

### 1.3 Citation tokens

Written inline in prose, in a table cell, or in a docstring. A bracket
immediately followed by `(` or `[` is a markdown link and is skipped.

| Token | Grammar | Resolves to |
|---|---|---|
| `[ShortKey]` | `[A-Z][A-Za-z0-9]{2,31}` | an entry in the reference registry |
| `[ShortKey, locus]` | the above, comma, a locus from {{CITATION_LOCUS}} | that work at a stated place |
| `[claim NNN]` | `NNN` is `[0-9]{3}[a-z]?` | the claim of that number, under the configured claim pattern |
| `[check NNN]` | the same | the check of that number, under the configured check pattern |
| `[finding F###]` | an opaque key, assigned once and never reused | that row of `FINDINGS.md` |
| `[tension T###]` | the same | that row of the tension ledger |
| `plan NNN` | lowercase, never inside a header line | that plan file |

**Paths are never hardcoded here.** `[claim NNN]` and `[check NNN]`
resolve through the configured patterns, because `CHECK_METHODOLOGY.md`
and `DOCUMENT_GENRES.md` deliberately leave the filing convention to the
project. §7 says where those patterns live.

### 1.4 Governed files

Some predicates are written by a file existing at a governed path: a
registry entry, a prompt-log entry, a dated review, a row in a ledger. The
pattern comes from the configuration of §7, and the predicate's row names
which.

---

## 2. The catalogue

The Owner column names the rulebook that governs the predicate. **Checked
by** points at the owner's own numbered check where one exists, names an
ontology check from §5, or says *reading* where no tool can decide it and
the duty is the assistant's under the consistency sweep
(`CHECK_METHODOLOGY.md` §7).

### 2.1 Sources and references

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `cites` | any artifact to a work | `[ShortKey]` | `MANIFESTO.md` §2 | ontology 2 | what does this rest on outside the project? |
| `cites-at` | a claim or check to the exact place in a work | `[ShortKey, locus]` | `MANIFESTO.md` §2 | ontology 2; an `ATTESTED` claim citing without a locus is reported | where exactly does the source say it? |
| `registered` | a work to its registry entry | an entry at the registry path | `MANIFESTO.md` §2 | ontology 3, against `{{REFERENCE_FIELDS}}` | is every work we lean on written down? |
| `held` | a source of record to its local copy | a row in the source index naming the file | `MANIFESTO.md` §6 | `DOCUMENT_GENRES.md` checker 7 | do we have it, or only its locator? |
| `consulted-at` | a source of record to its locator, where access conditions keep it out of the repository | the same row, giving shelfmark, release, or version, and access conditions | `MANIFESTO.md` §6 | ontology 3: the row has one of `held` or `consulted-at` | how would a second reader reach it? |
| `witness-of` | one record of a work to the work: a manuscript, edition, facsimile, release, or vintage | `Witness of: [ShortKey]` in the registry entry | `MANIFESTO.md` §2 | ontology 2 | which of these are the same work? |
| `standing-disputed` | a work to a dispute about its authorship, dating, authenticity, priority, replication, or currency | `Disputed: <what>, <source>` in the registry entry | `MANIFESTO.md` §3 | reading | is this source contested? |

### 2.2 Claims

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `asserts` | a claim to its statement | the claim's body | `CHECK_METHODOLOGY.md` §1 | reading | what is being claimed? |
| `register` | a claim to its trust level | `Register:` | `CHECK_METHODOLOGY.md` §1 | `CHECK_METHODOLOGY.md` mechanical 1 | how far may this be trusted? |
| `kind` | a claim to its claim kind | `Kind:`, lower case, spaces hyphenated (`internal-consistency`) | `CHECK_METHODOLOGY.md` §2 | `CHECK_METHODOLOGY.md` mechanical 1 | what would settle it? |
| `verdict` | a claim to the conclusion reached | `Verdict:` with a value from the declared kind's vocabulary; the Inferential vocabulary takes two, comma-separated | `CHECK_METHODOLOGY.md` §2 | `CHECK_METHODOLOGY.md` mechanical 1 | what did the work conclude? |
| `not-claimed` | a claim to what it explicitly does not assert | a `What is not claimed` section | `PRECEDENCE.md` ("tier 1 does not inflate") | reading; a claim relied on elsewhere that has none is reported by ontology 3 | where does this claim stop? |
| `original` | a claim to the fact that it has no external source | `Original: <pointer to the evidence here>` | `MANIFESTO.md` §2 | ontology 3 | is this ours, and what backs it? |
| `depends-on` | a claim to a claim it rests on | `Depends-on: NNN[, NNN]` | `CHECK_METHODOLOGY.md`, *Words used here* | ontology 4 | what falls if this falls? |
| `derives-from` | a claim to the claim, source, or construction it was obtained from | the inputs named in the claim body with their tokens | `CHECK_METHODOLOGY.md` §4 | reading | how was this reached? |
| `assumes` | a claim to an input it takes | the input named in the claim, with its `input-kind` | `CHECK_METHODOLOGY.md` §4 | reading | what is taken for granted? |
| `input-kind` | an input to *derived*, *imposed*, or *conjectured* | the word beside the input | `CHECK_METHODOLOGY.md` §4 | reading | was this forced, or chosen? |
| `measured-against` | an empirical or inferential claim to what it is compared with | the comparison named in the claim, with its range | `CHECK_METHODOLOGY.md` §2 | reading | compared to what? |
| `frame` | a claim, check, or derived artifact to the frame its quantities are expressed in: units, encoding, edition, sample definition, variable coding | `Frame: <the fixing assertion or the artifact that defines it>` | `CHECK_METHODOLOGY.md` §5 | ontology 3 on a check | in what terms is this stated? |

### 2.3 Verification

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `backed-by` | a claim to the check that establishes it, and the check to the claim it gates | `Backed-by: [check NNN]` in the claim; the claim's token in the check's header | `CHECK_METHODOLOGY.md` §1, §8; `MANIFESTO.md` §2 | ontology 5: the pair resolves in both directions, and a claim registered `VERIFIED` or `RULED_OUT` names at least one | which check backs this? |
| `gates` | a check to an assertion it would fail on | the reported assertion inside the check | `CHECK_METHODOLOGY.md` §5 | `CHECK_METHODOLOGY.md` mechanical 2, in a check program only | would this notice if the claim were false? |
| `refutes` | a check to a claim it shows not to hold | `Verdict:` with the failing word of that kind's vocabulary | `CHECK_METHODOLOGY.md` §2 | reading: a failing verdict does not entail `RULED_OUT`, and the register is the researcher's (`CHECK_METHODOLOGY.md` §1) | what did we rule out? |
| `records` | a check record to one execution of a check | a dated record naming the check and the party | `CHECK_METHODOLOGY.md` §8 | `CHECK_METHODOLOGY.md` mechanical 4 | when was this last actually run? |
| `instrument-of-record` | a check to the instrument or procedure it used | `Instrument: <name>, <version, edition, shelfmark, or release>` | `CHECK_METHODOLOGY.md` §3 | ontology 3 | what would a second reader return to? |
| `mutation` | a check to an alteration of something the claim depends on | `Mutation: <name>[, <name>]`, each a key into the project's `{{MUTATION_SET}}` | `CHECK_METHODOLOGY.md` §5 | `CHECK_METHODOLOGY.md` mechanical 3, which splits by check form | would this check notice a change? |
| `robustness` | a check to a perturbation the claim asserts independence *from* | `Robustness: <name>[, <name>]`, names disjoint from `Mutation:` | `CHECK_METHODOLOGY.md` §5 | ontology 3: the two lists are disjoint. Survival is the intended result here, and a failure is a finding | what does this not depend on? |
| `verification-status` | a claim to who checked it and how | `Verified-by: researcher \| assistant, <route> \| deferred, <instrument> \| unchecked \| <party>, <route>` | `MANIFESTO.md` §5 | ontology 3 | who actually checked this? |
| `deferred-to` | a claim to an instrument or party the researcher chose not to check behind | the `deferred` form of `Verified-by:` | `MANIFESTO.md` §5; `VISION.md` | ontology query 3 | what did we take on trust? |
| `pre-registered` | a check or claim to a protocol fixed before the evidence was consulted | `Pre-registered <D Month YYYY>, <locator>` | `CHECK_METHODOLOGY.md` §5 | ontology 3: the date precedes the earliest record's date, and the locator resolves | was this confirmatory, or exploratory? |
| `performed-by` | a check record, transcription, coding pass, or derived artifact to the party that produced it | `By: <party>` from `{{PARTIES}}` | `MANIFESTO.md` §5 | ontology 3: every name resolves to the roster | whose work is this? |

### 2.4 Derived material

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `produced-from` | a derived artifact (transcription, collation, extract, table, figure) to the source it came from and the check or program that produced it | `Produced-from: <source token>, <check or path>` | `CHECK_METHODOLOGY.md` §8 | ontology 2 | where did this material come from? |

### 2.5 Plans and state

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `owned-by` | an artifact to its plan | `Plan: NNN[, task M]` | `DOCUMENT_GENRES.md` | `DOCUMENT_GENRES.md` checker 4 | is this live or frozen? |
| `status` | a plan to its lifecycle state | `Status:` in the form `DOCUMENT_GENRES.md` fixes | `DOCUMENT_GENRES.md` | `DOCUMENT_GENRES.md` checker 6 | what is open? |
| `prerequisite` | a plan to a plan or claim it builds on | `Prerequisites: NNN[, NNN]` or `none` | this file: no rulebook fixes plan structure | ontology 3 | what must land first? |
| `serves` | a plan to a keystone hypothesis | `Serves: <hypothesis>` or `Serves: none, <reason>` | `DOCUMENT_GENRES.md` | ontology 3 | why are we doing this? |
| `reserved-by` | a claim to the plan holding a deferred question | `Reserved <date>, plan NNN` | `CHECK_METHODOLOGY.md` §6 | ontology query 4 | what is waiting on an unanswered question? |
| `finding` | a stable key to what the record has established | a row in `FINDINGS.md` carrying `[finding F###]` | `MANIFESTO.md` §12 | reading; additions are the researcher's | what has this project established? |

### 2.6 Genre and provenance

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `created`, `updated` | an artifact to its dates | the `Created` stamp | `DOCUMENT_GENRES.md` | `DOCUMENT_GENRES.md` checker 1 | how current is this? |
| `released` | a version to its release | the `Released` stamp, and a changelog row | `DOCUMENT_GENRES.md` | ontology 3: both or neither | is this out? |
| `superseded-by` | an artifact to the one that replaces it | the `superseded by` stamp on the **replaced** artifact, holding the path to its replacement | `DOCUMENT_GENRES.md` | ontology 2 | am I reading the current one? |
| `logged` | a prompt to its entry | a numbered file at the log path | `MANIFESTO.md` §8 | `DOCUMENT_GENRES.md` checker 2 | what was asked, and when? |
| `authorized` | a change to the prompt that authorized it | named in the log entry | `MANIFESTO.md` §12 | reading | who said to do this? |
| `reason-for` | a correction to why it was made | the round's log entry, or the commit message | `MANIFESTO.md` §12 | reading | why did this change? |
| `imported` | an artifact to its origin and original date | a row in the import ledger | `MANIFESTO.md` §6 | reading | where did this come from? |
| `reviewed-by` | a write-up to a review of it | a dated file at the reviews path | `DOCUMENT_GENRES.md` | `DOCUMENT_GENRES.md` checker 8 | who has read this adversarially? |

### 2.7 Precedence

| Predicate | Relates | Written as | Owner | Checked by | Answers |
|---|---|---|---|---|---|
| `tier` | a statement to its authority | **derived**, never stored as a field | `PRECEDENCE.md` | not stored, so nothing to check | what governs if these disagree? |
| `diverges` | a claim to a public-record statement it contradicts | a row in the tension ledger: claim, record, caution, and `Caution: live` or `Caution: closed <date>` | `PRECEDENCE.md` | reading, at sweep item 8; the caution field is read as recorded, not judged | where do we stand against the literature? |
| `context` | prose to borrowed material it carries | an attributing hedge naming the tier | `PRECEDENCE.md` | reading | is this ours or theirs? |

### 2.8 Carried in prose, not in syntax

These relations matter and no tool parses them. They are the sweep's
business and the reason `CHECK_METHODOLOGY.md` §7 exists: `asserts`,
`derives-from`, `assumes`, `input-kind`, `measured-against`,
`standing-disputed`, `authorized`, `reason-for`, `imported`, `context`,
`restates` (prose restating a fact established elsewhere: the defect the
sweep hunts, written nowhere by design), and `single-source` (a
load-bearing figure stated once and cited elsewhere).

---

## 3. Derived predicates are never stored

Four things follow from others and are computed. Writing one down creates
a second ledger, and a second ledger drifts (`DOCUMENT_GENRES.md`).

| Derived | From |
|---|---|
| `genre(artifact)` | the configured path patterns (§7), overridden by `owned-by` and the owning plan's `status` |
| `live` / `frozen` | `owned-by` and `status` |
| `tier(statement)` | `register` where the statement is a claim; otherwise from how it is carried, by citation for tier 3 and by hedge for tier 4 (`PRECEDENCE.md`) |
| `gated(assertion)` | the existence of a check that `gates` it |

## 4. How registers compare

Two queries below rank registers, and no rulebook orders them. For the
purpose of those queries only:

> `VERIFIED` and `DERIVED` are stronger than `ATTESTED`, which is stronger
> than `OPEN` and `SPECULATIVE`. `VERIFIED` and `DERIVED` are not ordered
> against each other. A dependency on a `RULED_OUT` claim is reported
> always, whatever the depending claim's register.

This is an ordering for reporting, not an authority ranking:
`PRECEDENCE.md` owns authority, and its tiers group `VERIFIED`, `DERIVED`,
and `RULED_OUT` together.

## 5. What the tools check

The ontology tool reads the surface syntax of §1 and reports; nothing here
blocks the researcher (`MANIFESTO.md` §13). Checks the owners already fix
are theirs, and the catalogue points at them. These are the ontology's own:

1. **Fields are known.** Every field line's name is one of the catalogue's,
   spelled as there, at most once per artifact. An unrecognized field is
   reported rather than ignored, so a typo does not silently drop a
   predicate. A stamp is matched against the five forms of §1.2, and a
   stamp written with a colon is reported.
2. **Tokens resolve.** Every citation token of §1.3 resolves to an
   existing entry, claim, check, finding, tension row, or plan.
3. **Required fields are present**, per artifact kind, from the
   configuration of §7.
4. **The dependency graph is walkable**: every `Depends-on` number
   resolves, and cycles are reported.
5. **Backing is two-way**: every `Backed-by` token resolves, the named
   check names the claim in return, and a claim registered `VERIFIED` or
   `RULED_OUT` names at least one check.
6. **Derived state is not written down.** A header field named `Genre`,
   `Tier`, `Live`, or `Frozen` is reported. Derived state stated in running
   prose is a reading matter and belongs to the sweep.

## 6. What the predicates buy

Each of these is a question the tools answer by reading the fields. Where
a query can only enumerate and not decide, it says so, and the deciding is
the assistant's under the sweep.

1. **What does this conclusion rest on?** The transitive closure of
   `depends-on` and `backed-by` from a claim, with any member weaker than
   the claim relying on it flagged, per §4.
2. **What is unverified underneath a result?** The same closure, filtered
   to `OPEN` and `SPECULATIVE`, and to `Verified-by` of unchecked or
   deferred.
3. **What did the researcher defer?** Every `Verified-by: deferred`, with
   its instrument. This is the answer to "which parts of this did you check
   yourself", and the repository produces it without anyone remembering.
4. **What is the blast radius of revisiting this claim?** Everything
   citing it by token, everything whose `Depends-on` names it, and the
   `Reserved` cluster if one holds it.
5. **Where does this project stand against the literature?** Every
   `diverges` row, with its caution as recorded. Whether a caution is
   *still* live is reading (`PRECEDENCE.md`).
6. **What is not finished?** Plans by `status`, claims by `register`,
   reservations by `Reserved`, and every `Serves: none`.
7. **Where might a claim be stronger than its backing?** Every place a
   claim cites another, listed with both registers and with the cited
   claim's *What is not claimed* quoted beside the citing sentence. The
   tool lists sites; the comparison is reading (`CHECK_METHODOLOGY.md` §5,
   rule six).
8. **What changed when a result was overturned?** Not a predicate query. A
   current-state artifact narrates none of its own past
   (`DOCUMENT_GENRES.md`); the answer is assembled from `logged` and
   `reason-for`, the round's log entry or commit message, together with
   `superseded-by` and the version history. The ontology's part is the
   pointer, not the narrative.

## 7. Where the patterns live

Every path pattern in this file, in `CHECK_METHODOLOGY.md`
("the checker's configured claim pattern"), and in `DOCUMENT_GENRES.md`
("the configured path patterns") comes from **one** configuration
artifact, `tools/artifacts.toml`. It holds one row per artifact kind:

```
[[artifact]]
kind      = "claim"
glob      = "evidence_and_reasoning/claims/*.md"
genre     = "plan-owned"
required  = ["Register", "Kind", "Verdict", "Plan", "Verified-by"]
```

It is a current-state artifact, indexed like any other, and it is the
single source of truth for filing conventions. A project that files its
claims elsewhere edits this one file, and every tool follows.

## 8. What to keep current

Eleven fields on every claim, with no ranking, is a system a researcher
fills in for three claims and abandons by the tenth. So the obligations
are ranked, and the ranking is part of the design.

**Mandatory on every claim**, and reported when missing: `Register`,
`Kind`, `Verdict`, `Plan`, `Verified-by`, and `Backed-by` once the claim
is registered `VERIFIED` or `RULED_OUT`.

**Mandatory on every check**: `Instrument`, `Mutation`, and `Frame` where
the check has quantities in a frame.

**Written when they apply**, and their absence is not a defect:
everything else. `Robustness`, `Pre-registered`, `Reserved`, `Original`,
`Serves`, `Witness of`, `Disputed`, and the prose relations of §2.8 are
written where they are true and omitted where they are not.

**Every predicate names the template that ships its field.** The artifact
templates pre-print the mandatory fields with their vocabularies in a
comment, so that a researcher who never reads this file still writes the
predicates by filling in the form. A predicate with no template home is
not shipped.

## 9. Adding a predicate

A project may add one. It earns its place only if it can say all four
things: what it relates, where it is written in exact surface syntax, how
it is checked or why it cannot be, and what question it answers. A
predicate that answers no question is a field that will go stale, and a
stale field is worse than none, because a reader trusts it.

Add the row with its Answers cell, the syntax to §1 if it is a new form,
the check to §5 or the reason it is *reading*, the field to the template,
and the required-field entry to `tools/artifacts.toml`.

The closed vocabularies (`Register`, `Kind`, and each kind's verdicts) are
`CHECK_METHODOLOGY.md`'s. A project that needs another verdict or another
kind amends that file, in place, at the researcher's direction, and this
catalogue follows.

## Slots

Three slots are this file's. `{{MUTATION_SET}}`, `{{CHECK_FORM}}`, and
`{{VERIFICATION_TOOL}}` appear above but belong to `CHECK_METHODOLOGY.md`,
and `{{DELIVERABLE}}` to `DOCUMENT_GENRES.md`; a project fills each once,
where its owner defines it.

| Slot | Meaning | Examples |
|---|---|---|
| `{{PARTIES}}` | The roster of people and agents whose work the record attributes, for `By:` and `Verified-by:` | the researcher, the assistant; a named co-author, a doctoral assistant transcribing in the archive; a research assistant coding occupations, a replication partner |
| `{{REFERENCE_FIELDS}}` | The fields a registry entry must carry, per the discipline's citation convention | author, title, venue, year, DOI; repository, collection, shelfmark, folio range, access conditions; producer, series, wave, release, documentation |
| `{{CITATION_LOCUS}}` | The units a `[ShortKey, locus]` may name | section, equation, page; folio, recto or verso, line; table, column, specification; wave, variable, value label |

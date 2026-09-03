# Check methodology

*Created 2 September 2026; updated 3 September 2026.*

This file defines the unit of verification in a repository built from this
template: the **check**. It owns four things the other rulebooks point to:
the **register** vocabulary, in which every claim's trust level is stated;
the **instrument or procedure of record**; the discipline that makes a
passing check mean something; and the **standing reservation**, the
instrument for a question the project has deliberately deferred. It also
treats a **written check procedure** as a check in every rule below.

A check is one self-contained investigation of one claim, question, or
construction. It carries no status of its own: it is live while the plan
that owns it is open, and frozen once that plan closes
(`DOCUMENT_GENRES.md`). Its form is {{CHECK_FORM}}: a program, a written
check procedure, or both. Nothing below assumes the form.

> **Build lens.** The template makes no research claims and runs no
> checks. The registers, the rules, and the sweep are shipped, not
> applied; the build's own verification is `MANIFESTO.md` §5's build lens.

## Words used here

Beyond the words `MANIFESTO.md` and `DOCUMENT_GENRES.md` define:

- A **claim** is a file under `evidence_and_reasoning/`, matching the
  checker's configured claim pattern, whose header carries a `Register:`
  line. A statement that carries no register is not a claim: it is prose,
  and `PRECEDENCE.md` says how prose carries borrowed material.
- An **assertion** is one independently falsifiable statement inside a
  claim.
- A check **gates** an assertion when it would reach a failing verdict if
  that assertion were false. An assertion so covered is **gated**, and a
  **gated check** is one whose verdict rests only on gated assertions.
- A **verdict** is a check's conclusion in the vocabulary of its claim
  kind (§2).
- A **check record** is the document recording one execution of a check:
  the date, who ran it, the verdict, and the second pass. A check may be
  executed more than once and then has more than one record.
- A **mutation** is a named alteration to something an assertion claims to
  depend on, made to confirm that the check notices.
- The **docket** of a plan is its list of items deferred to its closure.

## Header lines

A claim's header carries these lines, each once, so that the checks below
can be implemented:

```
Register: VERIFIED          one of VERIFIED, DERIVED, ATTESTED, SPECULATIVE, RULED_OUT, OPEN
Kind: documentary           one of the kinds of §2
Verdict: confirmed          a word from that kind's vocabulary
Plan: 003, task 2           the owning plan (DOCUMENT_GENRES.md)
```

A check's header adds `Mutation: <name>`, naming one or more members of
{{MUTATION_SET}}. A claim inside a standing reservation (§5) also carries
`Reserved <D Month YYYY>, plan NNN`: a comma after the date and never a
colon, so the line is a stamp and not a change narrative
(`DOCUMENT_GENRES.md`).

---

## 1. Register: how far a statement may be trusted

Every claim carries exactly one register. This is the vocabulary the whole
repository states trust in, and `PRECEDENCE.md` assigns authority by it.

| Register | Meaning | Backed by |
|---|---|---|
| `VERIFIED` | a check would fail if the statement were false | a gated check, with the independent second pass of `MANIFESTO.md` §5 recorded |
| `DERIVED` | argument establishes it, and a second route agrees | a written derivation or reading, plus an independent cross-check, both recorded |
| `ATTESTED` | a source of record says this; the register makes **no** claim that what it says is true | collation against the source of record, held or consulted at its recorded locator (`MANIFESTO.md` §6), naming the form consulted: edition, page, folio, table, or release |
| `SPECULATIVE` | hypothesis, conjecture, or reading held for testing | stated precisely enough that evidence could count against it |
| `RULED_OUT` | shown not to hold | a gated check, or a complete argument with an independent cross-check recorded |
| `OPEN` | stated precisely, not settled | nothing yet |

**Who assigns a register.** The assistant proposes a register together
with the check, the second pass, and the verification status, and stops.
The researcher assigns it, or directs that it be assigned; `VERIFIED` and
`RULED_OUT` in particular are the researcher's, because `MANIFESTO.md` §5
reserves to the researcher the declaration that a claim is established.
Until a register is assigned, the claim keeps the one it had, and a new
claim starts at `OPEN`.

**Register and verification status are different questions**, and both are
recorded. The register says **how far the statement may be trusted**; the
verification status of `MANIFESTO.md` §5 says **who checked it and by what
route**: the researcher, the assistant, deferred to a named instrument, or
unchecked. A claim carrying a researcher-assigned `VERIFIED` whose check
only the assistant has run says exactly that, and `PRECEDENCE.md` says
what may be done with it.

**Registers are never mixed inside a claim.** A sentence carrying a
`VERIFIED` clause and a `SPECULATIVE` clause is split into two.

## 2. Claim kinds, and the verdict each takes

A claim declares its kind, and its check states a verdict in that kind's
vocabulary. The kinds are not a taxonomy of disciplines; one project uses
several.

| Kind | The claim is | Verdict vocabulary |
|---|---|---|
| Formal | provable from definitions or axioms | proved / disproved |
| Computational | the output of a calculation or a pipeline | reproduced / not reproduced |
| Empirical | a statement about the world that measurement or observation can bear on | compatible / in tension / refuted |
| Inferential | a quantity estimated from data under stated assumptions | identified as stated / assumption unsupported, and replicated / not replicated |
| Documentary | what a source of record says, or whether it says it | confirmed / not confirmed |
| Interpretive | a reading a body of evidence supports | supported / underdetermined / contradicted |
| Internal consistency | two or more statements here that must agree | consistent / inconsistent |

**An empirical or inferential claim is compared to the range of
independent measurements, estimates, or readings where more than one
exists, never to a single reported figure**, and any disagreement is
recorded plainly. The verdict *in tension* is the same word
`PRECEDENCE.md` uses for a divergence from the public record, and
deliberately so. An interpretive claim states what would count against it
before the evidence is assembled.

Register and kind are independent, and a claim states both: a documentary
claim can be `VERIFIED`, a formal claim can be `OPEN`, and an interpretive
claim reaching *supported* is `DERIVED` rather than `VERIFIED` unless a
check gates it.

## 3. The instrument or procedure of record

The instrument or procedure of record for this project is
{{VERIFICATION_TOOL}}, the thing a second reader returns to in order to
repeat a verification (`MANIFESTO.md` §5). It is identified by whatever
makes that return possible: for software, the version and the pinned
environment; for a source, the edition or shelfmark and the form consulted
(original, facsimile, microfilm, digital surrogate); for a dataset, the
release or vintage. Every check names it in its header.

Other instruments may be used where they fit better. A load-bearing result
obtained elsewhere is cross-checked in the instrument of record, and the
check records both routes.

---

## 4. Philosophy

1. **Re-derive, do not transcribe.** A claim of a source counts as
   verified only when it has been established independently from the
   definitions, the data, or the document, not reproduced from the
   source's own text (`MANIFESTO.md` §5).
2. **Understand the anatomy of a mismatch.** When an independent pass
   disagrees with the source, the disagreement is diagnosed precisely,
   which definition, which step, which convention, which edition, which
   vintage, before any conclusion is drawn. A mismatch may be an error in
   the source, an error here, or a difference of conventions; the
   diagnosis says which.
3. **Keep derived and imposed apart.** Every input to a construction,
   model, or reading is classified: *derived* (forced by prior structure),
   *imposed* (a choice), or *conjectured*. A claim is never worded to
   suggest a choice was forced.
4. **A negative result is a result.** A claim may fail, or hold for
   narrower reasons than the source gives. What matters is knowing exactly
   when that conclusion is reached and why. A negative is reported with
   the same rigor as a positive.

---

## 5. A passing check is not a true claim

A check whose verdict depends on real work can still certify nothing, if
the work answers a different question. Six rules follow, each closing a
way a check can pass while testing nothing.

- **Fix the frame of reference.** A quantity is expressed in some frame:
  a basis, a coordinate system, a set of units, a text encoding, an
  edition, a sample definition, a variable coding. Used alongside objects
  in another frame, it silently tests nothing. Every such object is either
  accompanied by an assertion that fixes its frame, or obtained a second
  way and asserted to agree.
- **Give every negative a positive control.** An assertion of the form "no
  such thing exists" passes whenever the search is mis-specified, and
  re-running it never reveals that. Each negative needs a control the same
  search *must* find: a planted instance, a known positive case, a source
  known to contain what is being looked for.
- **Show every assertion falsifiable.** Alter something the assertion
  claims to *depend on*, and confirm the check reaches a failing verdict.
  An assertion that cannot fail is not an assertion. Each check names its
  mutations in its header, from {{MUTATION_SET}}; a check that survives
  the mutations it names is gated on nothing. For a check that executes,
  the alteration is applied to a scratch copy and the check re-run; for a
  written check procedure, the alteration is planted in the transcription,
  extract, or figure the procedure examines, a reader follows the
  procedure, and the record states that it was caught.
  **A perturbation the claim says it does not depend on is a robustness
  check, not a mutation.** It is recorded too, and there survival is the
  intended result. The two are never confused: a mutation that a claim
  survives is a defect, and a robustness check that a claim survives is a
  finding.
- **An empty search is not a proof of absence.** A tool that returns
  nothing returns nothing both for "there is none" and for "nothing was
  asked". A negative resting on an empty return passes exactly in the case
  it claims cannot happen. Decide absence by a construction that means one
  thing: an exhaustive enumeration over a stated domain, a bound that
  excludes the possibility, or a search whose coverage is itself
  established and stated.
- **One result may stand for many.** A solver returning one solution, a
  query returning one row, a search returning one hit, a catalogue
  returning one entry: each may stand for a family. If the claim is about
  how many there are, describe the whole set and gate two assertions: that
  everything found belongs to it, and that nothing belonging to it is
  missing.
- **Watch the citation, not just the work.** The most common defect is not
  a wrong result but an assertion that **exceeds its cited backing**:
  prose claiming more than the claim it cites establishes. It is invisible
  to every passing check and is caught only by adversarial re-reading.
  When a check record or a claim cites another claim, the citing text must
  be no stronger than the cited one.

---

## 6. A standing reservation

A body of work can be complete, every assertion gated and nothing known
wrong, while a question it rests on is **deferred**: the dating of a
manuscript on which three readings rest; the choice of weights on which
four estimates rest; an exact characterization on which several
statements' scope rests. Statements whose scope depends on the missing
answer cannot be made more than true-as-established by further work.

Without a reservation, every sweep meets the deferred question again and
narrows one sentence at a time, and no sweep is self-contained. A
**standing reservation** records the question once, declared by the plan
that will resolve it, and queues the narrowings for a single deliberate
round. It says four things:

1. the standing assumption the reserved material is read under;
2. which claims are inside it;
3. what must **not** be included in it;
4. what it does not license.

Each affected claim carries the `Reserved` header line above, removed when
that claim's reserved statements are resolved, so the absence of pointers
means the reservation holds nothing.

A reservation lowers no register and excuses no gating. A reserved claim
is still what its register says and still means what it says; what is
reserved is the **scope** of statements that depend on the deferred
question. It gives a sweep a rule instead of a judgment call:

> A sweep that finds a reserved statement wanting a further narrowing *on
> account of the deferred question* records it in that plan's docket. It
> does not edit the record.

Everything else a sweep finds is repaired as usual.

---

## 7. The consistency sweep

**A consistency sweep closes every correction batch.** The assistant
proposes it when a batch has been applied and runs it at the researcher's
direction (`MANIFESTO.md` §16).

The sweep exists because of a defect class no check can see on its own:
**prose in one document restating a fact established in another.** A
restatement is not a check, so nothing gates it; and because a fact worth
stating once is usually worth stating twice, a wrong restatement tends to
appear in *two* documents rather than one.

What a sweep covers, at minimum:

1. **Propagation.** For each newly established or corrected fact, every
   statement of it anywhere in the repository, not just the document that
   was being corrected. Assume a second copy exists until you have looked.
2. **The claims against each other**, and against the checks that back
   them: contradictions, citation drift, stale register, kind, verdict, or
   plan attribution.
3. **The top-level current-state documents** (`CURRENT_STATE.md`,
   `FINDINGS.md`, `evidence_and_reasoning/research_result.md`): every
   count they state re-counted against the record, every register checked
   against its claim, every link followed.
4. **The plans and the plan index**
   (`evidence_and_reasoning/research_plans/ROADMAP.md`), including that
   every open plan's execution ledger lists every unstarted task.
5. **The dated records** for *accuracy*, never for voice: a note that
   records a finding later contradicted, or a correction the note proposed
   that a later round adopted.
6. **The write-ups against each other**: any fact stated in two of them
   must be stated compatibly.
7. **The checks against their records and claims.**
8. **The tension ledger against the claims and the references**
   (`PRECEDENCE.md`): every divergence has a row, every row's caution is
   still live, and no public-record statement stands in prose without the
   hedge its tier requires.

**Every finding is then handed to a reader instructed to refute it**
(`MANIFESTO.md` §17). The sweep then reports its findings and the files it
would touch before editing anything (`MANIFESTO.md` §14). A fix to a
current-state artifact that is neither maintained nor one of the four
`MANIFESTO.md` §12 names may be applied; every other fix is brought with
its proposed wording, and the assistant stops.

### The structure lens, and what a rebuild owes

A sweep asks whether each sentence is *true*. That question never reaches
a sentence which is true and does not belong, or belongs somewhere else,
and a write-up can accumulate those until it has to be rebuilt. So a
review of a write-up opens with a **structure lens**, before any
sentence-level finding: per section, the inventory and the order, every
load-bearing fact, its home, every restatement site, and every
cross-reference classified load-bearing or decorative. A review may not
patch a sentence into a section whose structure it has not audited.

When a section is **rebuilt** rather than corrected, three further things
hold.

- The rebuild is delivered with a **deletion ledger**: every cut sentence
  classified *restatement*, *decoration*, or *content*, with the home of
  the surviving statement. A content cut needs the researcher's approval.
- The round reports its **net word delta** and prints every sentence it
  *added*. Corrections replace; they do not append.
- **A section-level comparison is not sufficient.** It sees only what it
  knows to count, and replacing a whole section can drop what it does not
  count: a cross-reference whose target lay inside the replaced range, a
  sentence's antecedent, a phrase that reads as a citation and resolves to
  nothing. A rebuild round therefore ends with a reading of the whole
  file.

---

## 8. The shape of a check

Every check, in whatever form, has six parts in this order:

1. **Header.** The claim or question checked, stated precisely, with its
   location in the source (section, equation, page, table, folio,
   variable). The header lines above. The references used. Pointers to
   prior checks it builds on.
2. **Construction.** The explicit definitions, data, or text the check
   rests on; every parameter named, with its domain; every convention
   fixed.
3. **Sanity checks.** Before the substantive test: reduction to known
   cases, counts and magnitudes, conventions checked against the glossary.
4. **The verification itself.**
5. **Discrepancy analysis.** If anything disagrees: how much, where, in
   what pattern.
6. **Summary.** A concise verdict in the vocabulary of the claim's kind:
   what was tested, what held, what did not, what was learned. The summary
   is actionable: it says what to check next, or why further checks along
   this line are unlikely to be needed.

A check that is a **program** prints its verdict, exits nonzero on
failure, and prints one machine-readable summary line (below). Its
execution is recorded in a check record beside it.

A **written check procedure** separates the two: parts 1 to 3 are the
procedure, which any reader can follow and which is the artifact a plan
owns and freezes; parts 4 to 6 are one check record per execution, dated
and naming who followed it.

**Cost is measurement, never a gate.** A check is judged by its verdict; a
slow or expensive check is not a failing one. Where cost is recorded, it
is recorded so the expensive checks can be examined for avoidable work,
and a check that is expensive of necessity says so in its header, so the
next reader does not go looking.

---

## What is checked mechanically

The tools check the following and report what they find (`MANIFESTO.md`
§13); everything else here is the assistant's duty.

1. **Register.** Every file matching the configured claim pattern carries
   exactly one `Register:` line, one `Kind:` line, and one `Verdict:`
   line, each holding a value from the vocabularies of §1 and §2. A file
   with none, or more than one, is reported.
2. **No unfalsifiable assertion.** In a check program, no reported
   assertion has a syntactically constant condition. Such an assertion
   passes whatever the work does.
3. **Mutation coverage.** Every check carries a `Mutation:` line naming
   members of {{MUTATION_SET}}. For a check that executes, the probe
   applies exactly the mutations that check names to a scratch copy,
   re-runs it, and reports it if it still passes. For a written check
   procedure the probe reports only an absent or unrecognized `Mutation:`
   line; whether the planted alteration was caught is read from the check
   record.
4. **Concordance.** A check program prints a summary line
   `RESULT: <verdict>; <name>=<value>; ...`; its check record states the
   same named values, and the tool reports any disagreement.
5. **Index.** Every check appears in the index that lists it.
6. **Citation sites.** Every place where a claim cites another claim is
   listed, so that rule six of §5 can be applied by reading. This is a
   report, not a verdict.

Single-sourcing a figure, and finding the wrong value stated in a passage
about the right subject, are reading duties and belong to the sweep
(§7, item 1).

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}` | What a check is in this project | an executable program with a printed verdict; a written collation protocol against the source of record; an estimation script plus a pre-registered analysis protocol; a proof written out and cross-checked by a second reader |
| `{{VERIFICATION_TOOL}}` | The instrument or procedure of record (§3), identified so a second reader can return to it | a computer-algebra system at a stated version; a statistics environment pinned to exact package versions, holding the raw data at a named release; the manuscript at its shelfmark, consulted as a digital surrogate; a printed edition, named and dated |
| `{{MUTATION_SET}}` | Named alterations to things claims *depend on*, kept where the checker can apply them. Never a perturbation a claim asserts independence from: that is a robustness check | reverse one structural convention, flip one defining sign, drop one axiom; corrupt one linked identifier, mis-key one variable's coding, drop one stratum from the frame; substitute a variant reading, swap the base manuscript, alter one date in the chronology |

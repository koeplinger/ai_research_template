# Check methodology

*Created 2 September 2026; updated 2 September 2026.*

This file defines the unit of verification in a repository built from this
template: the **check**. It owns three things the other rulebooks point to:
the **register** vocabulary, in which every claim's trust level is stated;
the discipline that makes a passing check mean something; and the
**standing reservation**, the instrument for a question the project has
deliberately deferred.

A check is one self-contained investigation of one claim, question, or
construction. It carries no status of its own: it is live while the plan
that owns it is open, and frozen once that plan closes
(`DOCUMENT_GENRES.md`). Its form is {{CHECK_FORM}}: a program, a written
check procedure, or both. Nothing below assumes the form; where a rule reads
naturally for one and not the other, both readings are given.

> **Build lens.** The template makes no research claims and runs no
> checks. The registers, the rules, and the sweep are shipped, not
> applied; the build's own verification is `MANIFESTO.md` §5's build lens.

## Words used here

Beyond the words `MANIFESTO.md` and `DOCUMENT_GENRES.md` define: an
**assertion** is one independently falsifiable statement inside a claim. An
assertion is **gated** when a check would reach a failing verdict if the
assertion were false. A **verdict** is a check's conclusion in the
vocabulary of its claim kind, below. A **mutation** is a deliberate
alteration of the object a check rests on, made to confirm that the check
notices. The **docket** of a plan is its list of items deferred to its
closure.

---

## 1. Register: how far a statement may be trusted

Every claim carries exactly one register. This is the vocabulary the whole
repository states trust in, and `PRECEDENCE.md` assigns authority by it.

| Register | Meaning | Reached by |
|---|---|---|
| `VERIFIED` | established by a check that would fail if the statement were false | a gated check, with the independent second pass of `MANIFESTO.md` §5 recorded |
| `DERIVED` | established by argument, with an independent cross-check | a written derivation or reading, plus a second route |
| `ATTESTED` | a source of record says this; the register makes **no** claim that what it says is true | collation against the source of record |
| `SPECULATIVE` | hypothesis, conjecture, or reading held for testing | stated precisely enough that evidence could count against it |
| `RULED OUT` | shown not to hold | a gated check or a complete argument |
| `OPEN` | stated precisely, not settled | nothing yet |

Register and verification status are different questions and are both
recorded. The register says **how far the statement may be trusted**; the
verification status of `MANIFESTO.md` §5 says **who checked it and by what
route**: the researcher, the assistant, deferred to a named instrument, or
unchecked. A statement can be VERIFIED by a check the assistant ran and the
researcher has not repeated, and the record says so.

**Registers are never mixed inside a statement.** A sentence that carries a
VERIFIED clause and a SPECULATIVE clause is split into two.

## 2. Claim kinds, and the verdict each takes

A check declares which kind of claim it addresses, and states its verdict
in that kind's vocabulary. The kinds are not a taxonomy of disciplines; one
project uses several.

| Kind | The claim is | Verdict vocabulary |
|---|---|---|
| Formal | provable from definitions or axioms | proved / disproved |
| Computational | the output of a calculation or a pipeline | reproduced / not reproduced |
| Empirical | a derived quantity compared to measurement or observation | compatible / in tension / refuted |
| Documentary | what a source of record says, or whether it says it | confirmed / not confirmed |
| Interpretive | a reading a body of evidence supports | supported / underdetermined / contradicted |
| Internal consistency | two or more statements in this repository that must agree | consistent / inconsistent |

**An empirical claim is compared to the spread of independent
determinations, not to a single accepted value**, and the tension is
recorded honestly. An interpretive claim states what would count against
it before the evidence is assembled.

Register and claim kind are independent, and a check states both: a
documentary claim can be VERIFIED, a formal claim can be OPEN, an
interpretive claim reaching *supported* is DERIVED and not VERIFIED unless
a check gates it.

---

## 3. Philosophy

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

## 4. A passing check is not a true claim

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
  re-running it never reveals that. Each negative needs a control object
  that the same search *must* find: a planted instance, a known positive
  case, a source known to contain what is being looked for.
- **Show every assertion falsifiable.** Alter the object the check rests
  on and confirm the check reaches a failing verdict. An assertion that
  cannot fail is not an assertion. The mutations a project uses are
  {{MUTATION_SET}}: alterations at the level of the hypotheses, not
  cosmetic ones. A check that survives every mutation is gated on nothing.
- **An empty search is not a proof of absence.** A tool that returns
  nothing returns nothing both for "there is none" and for "nothing was
  asked". A negative resting on an empty return passes exactly in the case
  it claims cannot happen. Decide absence by a construction that means one
  thing: an exhaustive enumeration over a stated domain, a bound that
  excludes the possibility, or a search whose coverage is itself
  established and stated.
- **A count of branches is not a count of things.** A solver returning one
  branch, a query returning one row, a search returning one hit: each may
  stand for a family. If the claim is about how many there are, describe
  the set and gate both inclusions.
- **Watch the citation, not just the work.** The most common defect is not
  a wrong result but an assertion that **exceeds its cited backing**:
  prose claiming more than the claim it cites establishes. It is invisible
  to every passing check and is caught only by adversarial re-reading.
  When a check record or a claim cites another claim, the citing text must
  be no stronger than the cited one.

---

## 5. A standing reservation

A body of work can be complete, every statement gated and nothing known
wrong, while a question it rests on is **deferred**: the dating of a
manuscript on which three readings rest; the choice of weights on which
four estimates rest; an exact characterization on which several
statements' generality rests. Statements whose scope depends on the
missing answer cannot be made more than true-as-established by any amount
of further work.

Left unmarked, that seam is rediscovered by every verification pass, and
each pass narrows a few more sentences without any pass being
self-contained. The instrument is a **standing reservation**, declared
once by the plan that will resolve the question. It says four things:

1. the standing assumption the reserved material is read under;
2. which claims are inside it;
3. what must **not** be included in it;
4. what it does not license.

Each affected claim carries a `Reserved <date>` header line pointing to
that plan (`DOCUMENT_GENRES.md`), removed when that claim's reserved
statements are resolved, so the absence of pointers means the reservation
holds nothing.

A reservation lowers no register and excuses no gating. A reserved claim
is still what its register says and still means what it says; what is
reserved is the **scope** of statements that depend on the deferred
question. It gives a sweep a rule instead of a judgment call:

> A sweep that finds a reserved statement wanting a further narrowing *on
> account of the deferred question* records it in that plan's docket. It
> does not edit the record.

Everything else a sweep finds is repaired as usual. A reservation converts
churn into a queue, so the eventual repair is one deliberate round instead
of a hundred small ones.

---

## 6. The consistency sweep

**Whenever a self-contained set of findings or corrections has been
applied, a documentation consistency sweep follows.** It is not optional
and not occasional; it is the closing move of any correction batch, and
`MANIFESTO.md` §16 has the assistant remind the researcher when one is
owed.

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
   them: contradictions, citation drift, stale register or plan
   attribution.
3. **The current-state core**: counts verified by counting, registers,
   links.
4. **The plans and the plan index**
   (`evidence_and_reasoning/research_plans/ROADMAP.md`), including that
   every open plan's execution ledger lists every unstarted task.
5. **The dated records** for *accuracy*, never for voice: a note that
   records a finding later contradicted, or a gated proposal since
   applied.
6. **The write-ups against each other**: any fact stated in two of them
   must be stated compatibly.
7. **The checks against their records and claims.**

**Every finding is then handed to a reader instructed to refute it**
(`MANIFESTO.md` §17), and the genre of each target decides whether the fix
may be applied or must be brought to the researcher.

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
- A per-section inventory diff is **not sufficient**. It compares the
  things it knows to count, and a whole-range replacement can drop what is
  none of those: a structural directive, a display's terminal punctuation,
  a definite article's antecedent, a phrase that reads as a citation and
  resolves to nothing. A rebuild round therefore ends with a whole-file
  pass, not with the section diff alone.

---

## 7. The shape of a check

Every check, in whatever form, has six parts in this order:

1. **Header.** The claim or question checked, stated precisely, with its
   location in the source (section, equation, page, table, folio,
   variable). The plan it belongs to (`Plan: NNN, task M`). The references
   used. Pointers to prior checks it builds on. The instrument or
   procedure of record and its version (`MANIFESTO.md` §5).
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

A check that is a program prints its own verdict and exits nonzero on
failure; its findings are recorded in a check record beside it. A check
that is a written check procedure carries the same six parts as prose, and
its record is the same document.

**Cost is measurement, never a gate.** A check is judged by its verdict; a
slow or expensive check is not a failing one. Where cost is recorded, it
is recorded so that the expensive checks can be examined for avoidable
work, and a check that is expensive of necessity says so in its header, so
the next reader does not go looking.

---

## What is checked mechanically

The tools check the following for this file and report what they find
(`MANIFESTO.md` §13); everything else here is the assistant's duty.

1. **No unfalsifiable assertion.** In a check program, no reported
   assertion has a syntactically constant condition. Such an assertion
   passes whatever the work does.
2. **Falsifiability coverage.** For checks that execute, the probe applies
   {{MUTATION_SET}} to a scratch copy of the repository, re-runs them, and
   reports any that survive every mutation. A written check procedure is
   not re-run: its header states which mutation would change its verdict,
   and the probe reports any that states none.
3. **Concordance.** Every count a check record states about its own check
   agrees with what that check reports; every load-bearing figure is
   single-sourced, and a scan reports the wrong value stated in a passage
   about a registered fact.
4. **Index.** Every check appears in the index that lists it.
5. **Citation strength.** Reported for the assistant's judgment, not
   decided: every place where a claim cites another claim, so that rule 6
   of §4 can be applied by reading.

## Slots

| Slot | Meaning | Examples |
|---|---|---|
| `{{CHECK_FORM}}` | What a check is in this project | an executable program with a printed verdict; a written collation protocol against the source of record; an estimation script plus a pre-registered analysis protocol; a proof written out and cross-checked by a second reader |
| `{{MUTATION_SET}}` | The alterations the falsifiability probe applies, at the level of the project's hypotheses | reverse one structural convention, flip one defining sign, change one axiom; perturb one coding decision, swap the weighting scheme, shift the sample window; substitute a variant reading, change the assumed edition, alter one date in the chronology |

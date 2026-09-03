# Check NNN: <!-- title: what this check settles -->

*Created D Month YYYY; updated D Month YYYY.*
Plan: NNN, task M
Backs: [claim NNN]
Instrument: <!-- name, and version | edition | shelfmark | release; for a source, the form consulted (original, facsimile, microfilm, digital surrogate) -->
Mutation: <!-- name[, name], each a member of {{MUTATION_SET}} (CHECK_METHODOLOGY.md, Slots) -->
Frame: <!-- what the quantities are stated in, and what fixes it; delete the line where there are none -->
By: <!-- who produced this record, from {{PARTIES}} (ONTOLOGY.md, Slots); for a written procedure, who wrote it, and each execution names its own party -->

<!-- HEADER FIELDS. Delete these comments in the instance.
     Backs       the claim this check backs; it names this check in its own
                 Backed-by (ONTOLOGY.md section 5, check 5).
     Instrument  the instrument or procedure of record
                 (CHECK_METHODOLOGY.md section 3).
     Mutation    an alteration of something the claim DEPENDS ON; the check
                 must fail under it. For a program the probe applies it;
                 for a procedure, state under Executions that the planted
                 alteration was caught.
     Add when they apply:
     Robustness: name[, name]    a perturbation the claim asserts independence
                                 FROM, names disjoint from Mutation. Survival
                                 is the intended result and is recorded; a
                                 failure is recorded too and is a result to
                                 report, not a defect in the check
                                 (CHECK_METHODOLOGY.md section 5).
     Pre-registered D Month YYYY, <locator>
                                 the locator a dated note under
                                 evidence_and_reasoning/notes/ holding the
                                 protocol as written before the evidence was
                                 consulted; its commit evidences the date. A
                                 program check with a protocol carries both. -->

## 1. What is checked

<!-- The claim or question, stated precisely, with its location in the
     source: [ShortKey, locus]. References used. Prior checks built on,
     by token. -->

## 2. Construction

<!-- The definitions, data, or text the check rests on; every parameter
     named with its domain; every convention fixed and, where it is a
     project convention, its glossary entry named. -->

## 3. Sanity checks

<!-- Before the substantive test: reduction to known cases, counts and
     magnitudes, conventions checked against the glossary. For a program,
     the assertions of this part are named here and reported by it. -->

<!-- FOR A PROGRAM CHECK, parts 4 to 6 record the latest run and are
     updated in place while the plan is open. FOR A WRITTEN PROCEDURE,
     delete parts 4 to 6 and record each execution under Executions. -->

## 4. Results

<!-- Run D Month YYYY, by <party>. What the verification found. Every
     named value the program prints in its RESULT line, one per line as
     `name = value`, exactly as printed; the concordance check compares
     them. -->

## 5. Discrepancies

<!-- If anything disagrees: how much, where, in what pattern, and the
     diagnosis: which definition, step, convention, edition, or vintage
     (CHECK_METHODOLOGY.md section 4, item 2). -->

## 6. Verdict

<!-- In the vocabulary of the claim's kind (the list is in the claim
     template). What was tested, what held, what did not, what was
     learned; what to check next, or why further checks along this line
     are unlikely to be needed. Then the second pass: its route, who took
     it, and whether it agreed (MANIFESTO.md section 5); the claim points
     here for it. -->

## Executions

<!-- WRITTEN PROCEDURES ONLY. One dated entry per execution, newest last;
     each states what its execution found and is corrected as its genre
     allows (DOCUMENT_GENRES.md). -->

### D Month YYYY, by <!-- party -->

<!-- Results, discrepancies, and verdict for this execution, parts 4 to 6
     of CHECK_METHODOLOGY.md section 8. Which planted alteration from
     Mutation was caught; which Robustness perturbations the claim
     survived; the second pass, its route, who took it, and whether it
     agreed. -->

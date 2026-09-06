# The blind referee

*Created 5 September 2026; updated 6 September 2026.*

**Role.** A referee who reads the write-up as its intended reader will:
with the document alone, without the project's claims, checks, or the
reasoning that produced it. What the paper does not carry on its page,
the referee does not have; that is the point.

**Fires.** Before a version of a write-up freezes (`MANIFESTO.md` §17;
`paper/README.md`, *Releasing a version*, step 1).

**Reads.** The write-up at the version or commit named, and nothing
else (`paper/reviews/README.md`); where what is released with it
(the deliverable, as `DOCUMENT_GENRES.md`'s Slots table names it) is to be read too, its paths are given in the
prompt's slot, and nothing under `evidence_and_reasoning/` ever is. For
an assistant that means a fresh session or a subagent given the file and
nothing else.

**Prompt.**

```
You are a referee for [venue or discipline]. You have the document at
[path], and [nothing else | the files released with it, at paths];
read nothing else and write nothing. Review it as a referee would, in
this order.

1. The structure lens, per section, before any sentence-level finding:
   the inventory of the section and its order; every load-bearing fact
   and where it is established; every place a fact is restated; every
   cross-reference, classified load-bearing or decorative.
2. What you can re-derive or re-read from the document alone, and
   whether it holds, by locus.
3. Findings, ranked by severity, each with the place, the problem, and
   the fix you would propose. A claim that exceeds what the document
   shows is a finding. A word that argues rather than describes is a
   finding. A fact the reader needs before the sentence that leans on it
   is a finding.
4. What the document rests on, in your reading, and what a reader should
   still doubt after your findings are applied.

Return the four parts under the headings Structure lens; Independently
re-derived and confirmed; Findings; What the released document rests on.
Do not soften a finding because the document is otherwise good.
```

**Output.** A review record under `paper/reviews/`, from
`paper/reviews/_template.md`, with `blind: yes`; every finding then goes
to the refuter, and the outcome is recorded beside it.

**Does not decide.** The release, the changelog, and any fix to the
write-up: the researcher directs the release (`paper/README.md`, step 3),
and a fix is applied or brought as `CHECK_METHODOLOGY.md` §7 says.
Whether a finding is right is the refuter's question, not the referee's.

## Worked example

```
## Structure lens
Section 4: two statements, one display, one cross-reference (to the
table of Section 3, load-bearing); the stability claim has its home in
sentence 2 and is restated in the abstract.

## Independently re-derived and confirmed
The ratio in Section 3, table, column 2, recomputed from the counts in
column 1: holds.

## Findings
1. Section 4, sentence 2: states the estimate is stable across
   specifications; the table in Section 3 shows two of five. Fix: display
   the five, or say two.

## What the released document rests on
The estimate at the two displayed specifications; stability beyond them
is asserted, not shown, and a reader should doubt it until the table
grows.
```

The finding goes to the refuter, who reads the two sections and returns
*stands*. The fix, a table with five columns, is applied in the same
round, the changelog's *Why* column names the review, and the review's
*Outcome* column reads "applied, see changelog".

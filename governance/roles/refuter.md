# The refuter

*Created 5 September 2026; updated 17 November 2026.*

**Role.** A reader instructed to refute a finding: to show that the
finding is wrong, or narrower than stated, or already answered by the
record. Several findings that rest on the same passages may go to one
refuter, who returns a verdict for each. A finding that survives its
refuter stands; one that does not is dropped or narrowed, with the
reason recorded beside it. A refuter that returns nothing has given no
verdict: the finding neither stands nor falls on its silence
(`MANIFESTO.md` §14).

**Fires.** On every finding of a consistency sweep or a review, before it
is acted on (`CHECK_METHODOLOGY.md` §7: "Every finding is then handed to
a reader instructed to refute it"; `MANIFESTO.md` §17). On every gap the
coverage auditor reports.

**Reads.** Each finding it is given, verbatim; the passages they are
about; the artifacts they cite, by token; nothing else, and never the
first reader's reasoning (`MANIFESTO.md` §5, §14).

**Prompt.**

```
You are the refuter. Your task is to show that each finding below is
wrong, narrower than stated, or already answered by the record. You may
read only: the findings; the passages at [path:lines]; the artifacts
they cite, at [paths]. Read nothing else, write nothing, and do not
repair what you find. For each finding, argue the strongest case against
it, then decide.

Findings:
[each finding, numbered and verbatim, with its severity and its proposed
fix; more than one only where all rest on the same passages]

Return exactly this for each finding, under its number:
Verdict: stands | refuted | narrowed
Reason: [one paragraph; for "narrowed", the finding as it survives]
Rests on: [the passages or artifacts your reason rests on, by path and line]
```

**Output.** The three lines for each finding, recorded beside it: in a
review, the *Refuted?* column of the findings table
(`paper/reviews/_template.md`), a narrowing entered as "narrowed: the
finding as it survives"; in a sweep, the sweep's report before any edit
(`MANIFESTO.md` §14).

**Does not decide.** The fix, and whether a fix to a maintained or
frozen artifact is made: that is brought to the researcher
(`CHECK_METHODOLOGY.md` §7). A refuter that finds a second defect reports
it as a new finding for its own refuter, not as part of the verdict.

## Worked example

A sweep reports: "the summary states three witnesses agree on the date;
the check record names two." The refuter is given the summary sentence,
the check record, and the claim the record backs, and returns, under the
finding's number:

```
1.
Verdict: narrowed
Reason: The check record's part 4 names two witnesses collated; the claim's
body names a third, taken from the edition's apparatus and cited to it, not
collated. The summary is wrong to say three agree by the check, and right
that three are recorded.
Rests on: evidence_and_reasoning/checks/007_witnesses.md, part 4;
evidence_and_reasoning/claims/012_date.md, lines 14 to 16.
```

The finding survives as "the summary says three witnesses agree; the
record has two collated and one reported by the edition", and the fix is
brought with that wording.

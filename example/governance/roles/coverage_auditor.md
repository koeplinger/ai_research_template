# The coverage auditor

*Created 5 September 2026; updated 5 September 2026.*

**Role.** A reader who classifies every atomic assertion a check makes
or its record states, so that a check certifies exactly what it gates and
nothing more (`CHECK_METHODOLOGY.md` §5: a passing check is not a true
claim). Each assertion is one of:

| Class | Meaning |
|---|---|
| `GATED` | asserted by a reported condition whose truth depends on the computation or the reading; the check would fail if it were false |
| `PRINTED_ONLY` | computed and printed, or displayed, but asserted by nothing: a reader can see it and the check cannot fail on it |
| `NOT_COMPUTED` | stated in the record or the claim and computed or read by nothing in the check |
| `MISMATCH` | stated in the record and computed by the program, and the two disagree (`tools/check_concordance.py` reports the named values; the auditor reads the rest) |
| `ATTESTED` | taken from a source of record, not computed: a reading, a published figure; it must carry its locus, and it can support no more than the register `ATTESTED` (`CHECK_METHODOLOGY.md` §1), whatever register the claim carries: a claim that leans on it while registered higher is a gap |

Every gap (any class but `GATED`, where the claim leans on the
assertion) is handed to the refuter, who tries to show the assertion is
gated after all or that the claim does not lean on it.

**Fires.** Before a check is accepted as backing a claim registered
`VERIFIED` or `RULED_OUT`; before a plan closes on its checks.

**Reads.** The check program or procedure, its record, and the claim it
backs; the source of record where an assertion is `ATTESTED`; nothing
else.

**Prompt.**

```
You are the coverage auditor for one check. Read the check at [path],
its record at [path], the claim it backs at [path], and, for an
assertion taken from a source of record, that source at [locus]; read
nothing else and write nothing. List every atomic assertion the claim
leans on and every assertion the record states, one per row:

  # | Assertion | Where stated | Class | Evidence

Class is one of: GATED (a reported condition would fail if the assertion
were false); PRINTED_ONLY (computed or displayed, asserted by nothing);
NOT_COMPUTED (stated, and computed or read by nothing in the check);
MISMATCH (stated and computed, and the two disagree); ATTESTED (taken
from a source of record, with its locus). Evidence names the reported
condition (for GATED), the print or display (PRINTED_ONLY), the
statement with nothing behind it (NOT_COMPUTED), the two values
(MISMATCH), or the locus (ATTESTED). Then list every negative assertion
and its positive control, and every quantity and the assertion that
fixes its frame; a negative without a control or a quantity without a
frame is a gap. Return the table and the two lists.
```

**Output.** The table, kept in the round's log entry and pointed at from
the check record's part 6; each gap then goes to the refuter, and the
outcome is recorded beside it.

**Does not decide.** The register: the researcher assigns it, informed by
the table (`CHECK_METHODOLOGY.md` §1). Whether a `PRINTED_ONLY` value
should be gated is the check's author's, brought with the table.

## Worked example

```
 # | Assertion                              | Where stated       | Class        | Evidence
 1 | the count is twelve                    | claim, record 4    | GATED        | report("count", value("count", n) == 12)
 2 | no duplicate among the twelve          | claim              | PRINTED_ONLY | the program prints the list; nothing asserts distinctness
 3 | the frame is the 2019 sample           | claim, Frame:      | GATED        | report("frame", sample.release == "2019")
 4 | the published count is eleven          | record 5           | ATTESTED     | [Key1, table 2]
 5 | the run took under a minute            | record 4           | NOT_COMPUTED | no timing in the program

Negatives: 2, no control. Frames: 1 fixed by 3.
```

Row 2 goes to the refuter, who returns *stands*; the author adds a
reported assertion of distinctness and its positive control, and the
record's part 4 gains the value.

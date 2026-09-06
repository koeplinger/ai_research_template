# Check 002: collation of the note's stated figure for 1851

*Created 6 September 2026; updated 6 September 2026.*
Plan: 001, task 2
Backs: [claim 002]
Instrument: the note as shipped, `source_documents/Note1_market_days_note.md`, at its committed revision
Mutation: alter-figure
By: assistant

## 1. What is checked

That the note [Note1, p. 1] states forty-eight market days for 1851,
held on Tuesdays with customary interruptions and on no other day of the
week, and that it states no count for 1852 [Note1, p. 2].

## 2. Construction

A written procedure. The reader opens the note at its committed revision,
finds the page mark `[p. 1]`, reads the first paragraph, and transcribes
the figure as written (in words) and the statement about the day of the
week; then reads `[p. 2]` and records whether a figure for 1852 is
stated. The transcription is compared word for word with the claim.

## 3. Sanity checks

The file has two page marks; the first paragraph names the year 1851;
the figure is written in words, so a digit in the transcription is a
transcription error.

## Executions

### 6 September 2026, by assistant

Results: the first paragraph under `[p. 1]` reads "records forty-eight
market days"; the day of the week is Tuesday, with interruptions "at the
turn of the year and in the depth of winter"; `[p. 2]` states no figure
for 1852. Discrepancies: none between the reading and [claim 002].
Verdict: confirmed. Mutation: in a scratch copy the figure was altered to
"forty-seven" (alter-figure) and the procedure, followed again, recorded
the altered word and flagged the disagreement with the claim; the
alteration was caught. Second pass: the assistant, in the researcher's role, re-read the
page and agreed with the transcription.

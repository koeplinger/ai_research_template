# Check 002: the note's stated figure for 1851, collated

*Created 20 November 2026; updated 21 November 2026.*
Plan: 001, task 2
Backs: [claim 002]
Instrument: the held note at its recorded checksum, the markdown file as held, read at its page marks
Mutation: alter-figure, alter-wording
By: assistant, model withheld from this shipped example

## 1. What is checked

That the note [Note1851, p. 1] states that the roll for 1851 records
forty-eight market days, held on Tuesdays throughout the year with the
customary interruptions, and on no other day of the week; and that it
states no count for 1852 [Note1851, p. 2]. This is what [claim 002]
says the note states, and nothing about whether the figure is right.

## 2. Construction

A written procedure, which any reader can follow:

1. Take the note as held, `source_documents/Note1851_market_days_note.md`,
   and confirm that its SHA-256 checksum is the one its row in the
   source index records. Control: the same computation over a scratch
   copy with one character changed must give another checksum.
2. Find the page mark of page 1, and transcribe in full the paragraph
   under it: the sentence that gives the count of market days for 1851,
   as the note writes it, in words, and the sentence on the days of the
   week the market was held.
3. Find the page mark of page 2, and record whether a count for 1852 is
   stated, by searching the page for every number, in digits or in
   words. Control: the same search over page 1 must find the count the
   note writes there in words.
4. Confirm the pinpoints: the claim cites page 1 for the count and page
   2 for its absence for 1852, and the transcription must come from
   under those page marks.
5. Compare the transcription with the statement of [claim 002], its
   citation tokens aside, in seven parts: whose roll it is; the year; the
   count, with what it counts; the day of the week; the span of the year;
   the customary interruptions, with their two times; and the statement
   that the roll shows no day held on any other day of the week. A
   difference in any of the seven is recorded; a difference in the words
   that join them is not.

The mutation set's "transcribed passage" is, for this procedure, the
claim's statement, which transcribes the note: an alteration is planted
there, in a scratch copy, since the note is a held source and is never
edited. From the fourth execution on, each records which step flagged a
planted alteration; the fourth also records it for the second and third.

## 3. Sanity checks

The file carries two page marks, in order; the paragraph under the first
names the year 1851; the count is written in words, so the count in
digits in the transcription is a transcription error.

## Executions

### 20 November 2026, by assistant, model withheld from this shipped example

Results: the checksum is the one the source index records. Page 1 reads
"The town's market roll for the year 1851 records forty-eight market
days", held on Tuesdays "with the customary interruptions at the turn
of the year and in the depth of winter", and "the roll shows no day held
on any other day of the week". Page 2 states no count for 1852: "A count
of the market days of 1852 is left to a later note."

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alteration, alter-figure: the note is a held source and is
never edited, so the alteration was planted on the project's side, in a
scratch copy of the claim's statement, the figure changed to
"forty-seven". The procedure, followed again against it, recorded
"forty-eight" from page 1 and flagged the disagreement: the alteration
was caught.

### 20 November 2026, by assistant, model withheld from this shipped example

The second execution, under the procedure as revised after its probe
reader found it untested in four places (`prompt_logs/007_tasks_1_and_2.md`).

Results: the checksum is the one the source index records, and the
control's scratch copy, with one character changed, gave another. Page
1, in full: "The town's market roll for the year 1851 records
forty-eight market days. The market was held on Tuesdays throughout the
year, with the customary interruptions at the turn of the year and in
the depth of winter, and the roll shows no day held on any other day of
the week." Page 2: "The roll for 1852 is fuller, and it is not treated
here. A count of the market days of 1852 is left to a later note." The
search for numbers on page 2 found only the year 1852, twice, and no
count; the same search on page 1, the control, found the count in
words. The count's sentence lies under the page mark of page 1, as the
claim's pinpoint says.

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alteration, alter-figure, on the project's side as before:
the figure in a scratch copy of the claim's statement changed to
"forty-seven"; the procedure, followed again, recorded "forty-eight"
and flagged the disagreement. It was caught.

Second pass: a reader without the first pass's reasoning, given the note
alone, quoted page 1's count, "forty-eight", and its sentence on the
days of the week, word for word as above, and found no count for 1852 on
page 2. It agreed.

### 20 November 2026, by assistant, model withheld from this shipped example

The third execution, after the mutation set gained alter-wording
(`prompt_logs/008_tasks_3_and_4.md`, decision 3), the procedure
unchanged.

Results: as in the second execution, word for word; the checksum, the
search for numbers on page 2 and its control, and the pinpoints all as
before.

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alteration, alter-wording, on the project's side: in a
scratch copy of the claim's statement, "held on Tuesdays" changed to
"held on Thursdays". The procedure, followed again, transcribed
"Tuesdays" from page 1 and flagged the disagreement: it was caught. The
alteration alter-figure was not planted again; the second execution
records it caught.

### 20 November 2026, by assistant, model withheld from this shipped example

The fourth execution, under the procedure as amended after the probe
reader of round 008: step 5's four parts named, and the step that
flagged each plant recorded.

Results: as in the second execution, word for word; the four parts of
step 5 each agree with [claim 002].

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alterations, on the project's side, in scratch copies of
the claim's statement: alter-wording on the interruptions, "in the depth
of winter" changed to "in the height of summer", flagged at step 5;
alter-wording on the negation, "no day held on any other day of the
week" changed to "a day held on another day of the week", flagged at
step 5; and a wrong pinpoint, the claim citing page 2 for the count,
flagged at step 4. Each was caught. The earlier plants were flagged at
step 5: alter-figure in the second execution, alter-wording on
"Tuesdays" in the third.

### 20 November 2026, by assistant, model withheld from this shipped example

The fifth execution, under the procedure as amended after the coverage
audit of round 016: step 5's parts are now seven, adding whose roll it
is, the year, what the count counts, and the span of the year.

Results: the file carries two page marks, page 1 then page 2. The note as
held gives the second execution's text word for word, and the seven parts
of step 5 each agree with [claim 002].

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alterations, on the project's side, in scratch copies:
alter-wording on whose roll it is, "the town's market roll" changed to
"the county's market roll", flagged at step 5; alter-figure on the year,
"for 1851" changed to "for 1852", flagged at step 5; alter-wording on what
is counted, "forty-eight market days" changed to "forty-eight fair days",
flagged at step 5; alter-wording on the span, "throughout the year"
changed to "for half the year", flagged at step 5; the count written in
digits in the transcription, "48 market days", flagged by the sanity
check; and a wrong pinpoint, the claim citing page 1 for the absence of a
count for 1852, flagged at step 4, since page 1 does not speak of 1852
and page 2 does. Each was caught.

### 21 November 2026, by assistant, model withheld from this shipped example

The sixth execution, after the consistency sweep of round 017: step 5's
seventh part now names the note's own clause, whose subject is the roll.

Results: as in the fifth execution; the seven parts of step 5 each agree
with [claim 002].

Discrepancies: none between the transcription and [claim 002].

Verdict: confirmed.

The planted alteration, on the project's side, in a scratch copy:
alter-wording on the clause's subject, "the roll shows no day" changed to
"the fairs show no day", flagged at step 5. It was caught.

The coverage audit of this procedure, with its gaps and their refuters'
verdicts, is kept in `prompt_logs/016_closure_checklist.md`.

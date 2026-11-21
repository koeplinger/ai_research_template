# Terminology

*Created 3 September 2026; updated 21 November 2026.*

This file defines the terminology used in the project (`MANIFESTO.md`
§9). Where established terminology exists, it is cited, save the
Gregorian calendar and the ISO form, which name no registered work, since
this project looks nothing up (prompt 016, decision 4). Where a
construction, category, variable, or notion is specific to this project,
it is marked **(project-specific)**. The threshold for inclusion is a term
a reader needs in order to follow the checks and the reasoning. The
project's standard name for each thing, and the mapping from any source's
own term to it, or the statement that no mapping is asserted, is recorded
here (`editorial_standards.md`, Conventions).

## Index

**Established terms**: Gregorian calendar ; ISO form

**Project-specific terms**: counting convention ; market day ; repeated
row ; row ; shipped source file ; the note ; the roll ; the year's
boundary

## Established terms

### Gregorian calendar

The calendar on which this project reads the roll's dates, the roll
marking no other: a choice of this project (imposed, [claim 005]). A
date's weekday is stated on it.

### ISO form

The international standard's year-month-day form, as 1851-05-15, in which
the roll writes its dates.

## Project-specific terms

### counting convention (project-specific)

A rule for which of the roll's rows count toward the note's year, such as
one on a row's kind or on the dates the year runs between. The note's own
convention is unknown [tension T001]; plan 002 states a list of
conventions to test.

### market day (project-specific)

A row of the roll, whatever its kind: an ordinary day or a fair, each a
day the market was held. The name is the question's own, in the words
the research statement uses; whether the note counts the same days under
it is part of what the project asks, so no mapping from the note's term
is asserted. It first arises in the question.

### repeated row (project-specific)

A row of the roll that repeats an earlier row's date and kind, whatever
its remark. *Duplicated row*, the word of prompt 008, names the same
thing, and stands where the plan, [claim 004], and [check 004] use it.

### row (project-specific)

One line of the roll after its head: a day held, with its date, its kind
(ordinary or fair), and, for a fair, its name in the remark column. A row
is the unit every count of the roll counts. The word also names a line of
a table, as a row of the source index or of `FINDINGS.md`, and what it is
a row of says which. Its *kind* is the value of the roll's column of that
name, not the `Kind:` field of a claim (`CHECK_METHODOLOGY.md` §2).

### shipped source file (project-specific)

A source file made for this project and held under `source_documents/`,
at the SHA-256 checksum its row in the source index records: a held
source in `ONTOLOGY.md`'s sense. The phrase is the researcher's (prompt
001, answers 4 and 10). Elsewhere in these documents *shipped* means as
the template delivered a file, as in `tools/artifacts_shipped.toml`.

### the note (project-specific)

The fictional note made for this project beside the roll, which states a
count of market days for 1851: a source of record, cited by page. This
project writes *the note* for that source alone. A dated record under
`evidence_and_reasoning/notes/` is a working note or an analytical note,
and the project's own writing under `paper/` is *the write-up*,
whatever its form (`DOCUMENT_GENRES.md` §2; prompt 004, decisions 6 and 7).

### the roll (project-specific)

The market roll of a fictional town for 1851 and 1852: a synthetic CSV
file made for this project, one row per day held, with the program that
writes it.

### the year's boundary (project-specific)

The calendar year: a row belongs to 1851 when its date falls in the
calendar year 1851. Imposed, by the researcher's choice (prompt 004,
decision 2), the roll being synthetic; every count of the roll is stated
in this frame.

## Names the sources use

| Source and locus | The source's term | This project's standard name | Mapping |
|---|---|---|---|
| [Note1851, p. 1] | market days | market day | not asserted |
| [Note1851, p. 1] | day held | market day | not asserted: whether the note counts a fair as a day held is open [tension T002] |
| [Note1851, p. 1] | the town's market roll for the year 1851; the roll | the roll | not asserted that the note's roll of one year is the whole file, or that the note read it in the state the project holds |
| [Note1851, p. 1] | customary interruptions | interruptions | the source's term is the standard name; that a Tuesday without a row is one is not asserted [claim 005] |
| [Roll1851], the kind column | ordinary; fair | ordinary; fair | the source's term is the standard name |

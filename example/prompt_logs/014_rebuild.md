# Prompt 014: the rebuild; the disclosure reading

*Created 20 November 2026; updated 20 November 2026.*
By: assistant, model withheld from this shipped example

--- PROMPT START ---
1. (a).

Then what the rebuild owes: a reading of the whole file by a fresh
reader, as its intended reader would read it. And step 5 of the release,
the disclosure reading.
--- PROMPT END ---

## What was done

The researcher ruled on the one decision of round 013, "1. (a).": the
write-up is rebuilt as proposed, its four content cuts approved. The
review's *Outcome* column and plan 001's ledger record it.

**What the rebuild owes** (`CHECK_METHODOLOGY.md` §7). Two readers, played
by subagents that wrote nothing. The share of usage they took is not
known: the harness reports none. The tree was recorded by the checksum of
every file before they started and compared after they returned: no file
had changed.

- A first-time reader, given the write-up alone, read it from start to
  finish as its intended reader would. It found the text holding on its
  own terms and raised seven points, six of which were answered in the
  text: the program's account of the days held now names the Tuesdays and
  the fairs; "checks it against" replaces "holds it to"; the ISO form, the
  date library, and the formula are said in words; the 52 Tuesdays are
  given their calendar; and the second count is named for what it was, a
  separate run of the AI assistant, which a journal's reader would
  otherwise take for a person. The seventh, the `Plan:` line, stands, by
  the rule that excepts a write-up's header lines.
- A second reader, given the write-up, the roll, its program, the note,
  and the claims, tested 63 statements and 146 figures and dates, and
  found nothing false and nothing stronger than the claim behind it. The
  one statement the wording fixes added, what the program says of the
  days held, was read against the program and the roll by the main thread.

**Step 5 of the release, the disclosure reading** (`MANIFESTO.md` §6). The
rule is the slot's: "none beyond §6: the sources are synthetic files made
for this project". Every figure, the two tables, and the quotation in the
write-up come from the two synthetic files; it names no person and draws
on no restricted source. Nothing is withheld, and no approval is required.

**Brought, one decision**, with its options and the assistant's
recommendation after them:

1. **The release** (`paper/README.md`, step 6). The version is the first,
   so there is no earlier text to show it against, and no changelog. The
   write-up to read is `paper/2026-11-20_market_days_1851.md`. Options: (a)
   release it as it stands, with a `Released 20 November 2026` stamp in its
   header; (b) hold it, naming what is to change. The assistant recommends
   (a).

The round check: no finding.

### The readers' output

#### The first-time reader, given the write-up alone

```
It holds on its own terms: recomputed from Table 1, every count, weekday and missing Tuesday is right, and each quoted phrase matches the quoted page (the roll itself was not read). Seven small text fixes remain: a leftover plan number in the header, five phrases that stop or may mislead this reader, and one figure with no stated source.

1. (unclear) line 4, header: "Plan: 001, task 5" refers to a plan the reader does not have and the note never mentions again. It is also an internal record number, the only one in a note meant to carry none. Fix: Delete the line. OLD: "Plan: 001, task 5
" NEW: ""
2. (unclear) lines 19-20, What the roll holds: This is the first mention of Tuesday, and nothing before it says the market's day was Tuesday, so the reader cannot tell why a cancelled day should be one. Fix: OLD: "none for a
Tuesday cancelled" NEW: "none for a
market Tuesday cancelled"
3. (unclear) line 47, What the roll holds: "holds it to the roll's own lines" does not tell the reader what the program does with the count. The likely meaning is that it checks the count against those lines. Fix: OLD: "holds it to the roll's own lines" NEW: "checks it against the roll's own lines"
4. (misleading) line 48, What the roll holds: A journal reader will take "a reader" to be a person who counted the rows. The note does not say who or what it was, and this file cannot settle it. If it was an AI model or a program, the sentence misleads about what kind of check this was. Fix: If it was a person, no change. If it was an AI model: OLD: "by a reader given the roll alone" NEW: "by a separate AI model given the roll alone"
5. (unclear) lines 50-51, What the roll holds: "ISO form" is a term a local-history reader may not have, and it is the note's whole reason for reading the dates as Gregorian, so the reader cannot weigh that choice. Fix: OLD: "the calendar of the ISO form
in which the roll writes its dates" NEW: "the calendar of the international standard (ISO) year-month-day form
in which the roll writes its dates"
6. (unclear) lines 52-53, What the roll holds: For this journal's readers, "date library" reads as a kind of library rather than software, and "Zeller's congruence" is named without saying what it is. Fix: OLD: "by a date library and by Zeller's
congruence, which checks" NEW: "by a software date library and by a standard weekday formula, Zeller's
congruence, which checks"
7. (unclear) line 67, What the roll holds: "the 52 Tuesdays of 1851" is the one figure with no stated place of reading, against the note's own rule. It is in neither table and comes from the calendar. The number itself is right on the Gregorian calendar. Fix: OLD: "49 of the 52 Tuesdays of 1851, and none on 4" NEW: "49 of the 52 Tuesdays that 1851 has on the Gregorian calendar, and none on 4"
```

#### The reader of its statements against the sources

```
It holds as it stands: I tested 63 statements of the sources and method and 146 figures and dates (78 table cells, 68 in the prose), recomputed from the roll in memory, with the quotation matching page 1 of the note word for word, and found nothing false or stronger than its claim. Only the six header tokens (the created and updated dates, the plan and task numbers) went untested, their sources being outside the files named.

Faults: none.
```

## Corrections and departures

None of this round's own; the three departures entry 001 lists hold.

## Closing status

```
DONE: the write-up rebuilt at the ruling; read whole by a first-time reader and against its sources, six wording fixes made; the disclosure reading made
WAITING ON YOU: one decision: the release of the write-up
```

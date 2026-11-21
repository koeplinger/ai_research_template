# Claim 005: the roll's ordinary rows of 1851 fall on Tuesdays, its fairs on Thursdays

*Created 20 November 2026; updated 20 November 2026.*
Register: VERIFIED
Kind: computational
Verdict: reproduced
Plan: 001, task 6
Verified-by: assistant, a reading of the weekdays from the held CSV by two methods of its own, by a reader without the first pass's reasoning
Backed-by: [check 005]
Depends-on: 001
Frame: the calendar year, as the roll's dates give it, fixed by the roll reader's in_year; a date's weekday, that of its ISO form on the Gregorian calendar

## Claim

Of the roll's 51 rows dated 1851 [Roll1851], the 49 ordinary rows fall on
Tuesdays and the 2 fairs, of 15 May and 9 October, on Thursdays, and no
row falls on any other weekday. Of the 52 Tuesdays of 1851, the roll
holds a row on 49; the three without one are 4 February, 12 August, and
30 December. The weekdays are derived from the roll's dates; that a date
is read on the Gregorian calendar is imposed, the roll writing its dates
in ISO form.

## What is not claimed

Nothing about why the roll holds no row on the three Tuesdays; nothing
about whether a fair is a day held in the note's sense; nothing about
what the note means by its Tuesdays or its interruptions; nothing about
1852, or about any real market.

## Evidence and route

Reached by [check 005], a program that reads the held roll at its
recorded checksum, holds the reader's rows of 1851 to the file's own
lines row for row, and takes each row's weekday from the date library,
with Zeller's congruence as a second route on every day of 1851; probed
under its four named mutations, each of which it failed under, and
audited for coverage. The second pass, a reading of the weekdays from the
held CSV by two methods of its own, by a reader without the first pass's
reasoning, is recorded in [check 005], part 6.

## References

[Roll1851].

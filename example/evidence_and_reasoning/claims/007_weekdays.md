# Claim 007: the 1851 rows fall on Tuesdays and two Thursdays, on distinct dates

*Created 6 September 2026; updated 6 September 2026.*
Register: VERIFIED
Kind: computational
Verdict: reproduced
Plan: 001, task 5
Verified-by: assistant, in the researcher's role, re-run of the program
Backed-by: [check 004]
Depends-on: 001
Frame: the calendar year and the Gregorian weekday, fixed in [check 004]

## Claim

Of the roll's 51 rows dated in 1851 [claim 001], the 49 ordinary
rows fall on Tuesdays and the 2 fairs on Thursdays, 15 May and 9 October
[Roll1851, rows 19 and 40]; the 51 rows fall on 51 distinct dates. Under
the calendar the check imposes, 1851 has 52 Tuesdays, and the roll
[Roll1851] holds no
row for three of them: 4 February, 12 August, and 30 December. The
weekday is derived from the date by the Gregorian calendar (imposed:
the standard library's arithmetic, stated in the check's frame).

## What is not claimed

Nothing about why the three Tuesdays have no row, which the roll
does not say; nothing about whether the note's author counted the fairs
as market days, which [claim 006] holds open; nothing about 1852.

## Evidence and route

The program of [check 004], which fails when every date's year is
shifted and when one month's rows are removed. The second pass is the
program's control, which counts the Tuesdays that have a row by the
calendar and reaches the same 49, and a re-run of the program by the
assistant in the researcher's role.

## References

[Roll1851].

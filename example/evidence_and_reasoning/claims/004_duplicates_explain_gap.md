# Claim 004: duplicated rows explain the roll's excess over the note's figure

*Created 20 November 2026; updated 20 November 2026.*
Register: RULED_OUT
Kind: computational
Verdict: not reproduced
Plan: 001, task 4
Verified-by: assistant, a search of the held CSV for repeated rows by a reader without the first pass's reasoning
Backed-by: [check 004]
Depends-on: 001, 002

## Claim

The roll's count for 1851 [claim 001] exceeds the note's figure
[claim 002] by three because three of the roll's rows of 1851 repeat an
earlier row's date and kind, so that without them the roll's days of
1851 number the note's forty-eight. The premise that the note's
forty-eight counts what the roll's 51 counts, each day once over the
calendar year, is imposed: the explanation is tested under it.

## What is not claimed

Nothing about what does explain the difference, if this does not;
nothing about the note's counting convention, which plan 001 leaves out
of scope, nor that the premise holds.

## Evidence and route

Ruled out by [check 004], a program that reads the held roll at its
recorded checksum, holds the reader's rows of 1851 to the file's own
lines row for row, and counts the rows of 1851 that repeat an earlier
row's date and kind: it finds none, where the claim needs three, and the
roll's 51 rows of 1851 fall on 51 distinct dates. The check could have
passed: its controls count planted repeats exactly, and a made-up roll
of 51 rows of 1851 with three repeats passes the gate that two and four
fail. It was audited twice for coverage, the second time after its
revision, and its later revisions were read against the gaps that
survived. The second pass, a search of the held CSV for repeated rows by
a reader without the first pass's reasoning, by three keys of its own,
found none; it is recorded in [check 004], part 6.

## References

[Roll1851], [Note1851].

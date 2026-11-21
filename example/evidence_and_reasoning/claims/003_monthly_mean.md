# Claim 003: the mean number of market days a month in 1851 is 4.25

*Created 20 November 2026; updated 20 November 2026.*
Register: DERIVED
Kind: formal
Verdict: proved
Plan: 001, task 3
Verified-by: assistant, a re-derivation from the held CSV by a reader without the first pass's reasoning
Backed-by: [check 003]
Depends-on: 001
Frame: the calendar year and its twelve calendar months, fixed in [check 001]

## Claim

The mean number of market days held a month in 1851 is 51 divided by
12, which is 4.25. The count, of the roll's rows [Roll1851] as
[claim 001] counts them, is derived from that claim; the divisor, twelve
calendar months, is imposed with the year's boundary.

## What is not claimed

Nothing about how the market days spread across the months, which run
from 3 to 5; nothing about 1852; nothing about the note [Note1851].

## Evidence and route

A written derivation, [check 003]: the count of [claim 001] divided by
the twelve months, read back to the count, and cross-checked by the
twelve monthly counts [check 001] gates against the held file's own
lines; audited for coverage. The second pass, a re-derivation of the mean from the held CSV by
a reader without the first pass's reasoning, gave the same 17/4; it is
recorded in [check 003], in its first execution.

## References

[Roll1851], [Note1851].

# Claim 004: duplicated rows explain the roll's excess over the note

*Created 6 September 2026; updated 6 September 2026.*
Register: RULED_OUT
Kind: computational
Verdict: not reproduced
Plan: 001, task 4
Verified-by: assistant, in the researcher's role, re-run of the program
Backed-by: [check 003]
Depends-on: 001, 002

## Claim

The roll's count for 1851 [claim 001] exceeds the note's figure
[claim 002] by three because at least three rows of 1851 duplicate
another row's date and kind. The check shows no duplicated row, so the
explanation is ruled out.

## What is not claimed

Nothing about what does explain the difference; [claim 005] and
[claim 006] hold the candidates the record has not decided.

## Evidence and route

The program of [check 003] counts rows of 1851 that repeat an earlier
row's date and kind and asserts at least three; it finds none and reaches
the failing verdict; its control shows one planted repeat counted as
one duplicate. The program was re-run as the second pass by the
assistant in the researcher's role.

## References

[Roll1851], [Note1].

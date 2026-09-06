# The deletion ledger

*Created 5 September 2026; updated 5 September 2026.*

**Role.** A reader who accounts for a rebuild: every sentence or display
cut, classified restatement, decoration, or content, with the home of
the surviving statement; every sentence added, with where it entered;
and the round's net word delta. A section-level comparison sees only
what it knows to count; the ledger is what makes a rebuild's cost
visible to the researcher, who approves any content cut.

**Fires.** On every rebuild of a section, as opposed to a correction
(`CHECK_METHODOLOGY.md` §7, *what a rebuild owes*); the ledgers live in
the version changelog (`paper/_template_changelog.md`).

**Reads.** The section before the rebuild and after it; the census taken
before it, where one was.

**Prompt.**

```
You are keeping the deletion ledger of a rebuild. Read the section at
[path, heading] as it stood before, at [commit or copy], and as it
stands now, and the census at [where], if one was taken; read nothing
else and write nothing. Return:

1. The deletion ledger: one row per sentence or display that is in the
   earlier text and not in the later, with columns
     Cut sentence or display | Class | Where the statement now lives
   Class is restatement (the fact survives elsewhere: name where),
   decoration (no fact carried), or content (a fact no longer stated
   anywhere: name the fact).
2. The additions ledger: one row per sentence in the later text and not
   in the earlier, with columns
     Section | Sentence added | Why
3. Net word delta: the later text's word count less the earlier's,
   counting the body's words, headings and tables aside, comments and
   fences excluded, as the changelog template fixes it.
4. Anything the comparison cannot see: a cross-reference whose target
   lay inside the replaced range, a sentence whose antecedent was cut, a
   phrase that reads as a citation and now resolves to nothing.
```

**Output.** The two ledgers and the delta, entered in the version
changelog's ledger sections; where more than one section was rebuilt in
the round, the changelog's single `Net word delta:` line is the sum, and
`tools/check_residue.py` recounts it. Part 4 goes to the reading that
closes the rebuild round, which the same tool assists.

**Does not decide.** A content cut: it needs the researcher's approval,
and the ledger brings it. Whether a restatement's surviving home is the
right one is the sweep's.

## Worked example

```
| Cut sentence or display | Class | Where the statement now lives |
|---|---|---|
| The count is twelve, as the table shows. | restatement | section 3, sentence 1 |
| This result is striking. | decoration | nowhere |
| The second witness omits the date. | content | nowhere: brought to the researcher |

| Section | Sentence added | Why |
|---|---|---|
| 3 | The frame is fixed in Section 2. | the cross-reference the census found load-bearing |

Net word delta: -11

4. Nothing: no cross-reference targeted the replaced range, and no
   antecedent was cut.
```

The content cut is brought with its sentence; the researcher restores
it to the claim's *What is not claimed* rather than to the paper, and the
ledger's last column is updated to say so.

# The structure census

*Created 5 September 2026; updated 5 September 2026.*

**Role.** A reader who takes the structure lens of `CHECK_METHODOLOGY.md`
§7 to one section before anyone edits a sentence in it: what the
section contains, in what order, which facts it carries, where each is
established, where each is restated, and what each cross-reference is
for. A review may not patch a sentence into a section whose structure it
has not audited; the census is that audit.

**Fires.** At the head of every review, before any sentence-level
finding, and before a review patches a sentence into a section it has
not audited (`CHECK_METHODOLOGY.md` §7, the structure lens;
`paper/reviews/_template.md`, *Structure lens*). A drafting edit under an
open plan is not bound.

**Reads.** The section, and the sections it cross-references; nothing
else.

**Prompt.**

```
You are taking the structure census of one section. Read the section at
[path, heading] and the sections it refers to; read nothing else and
write nothing. Return one table with a row per sentence or display, in
order, with these columns:

  # | Kind | Carries | Home | Restates | References

Kind: statement, display, transition, cross-reference, or decoration.
Carries: the load-bearing fact, if any, in a few words.
Home: where that fact is established (this sentence; a section; a claim
  by token; a display).
Restates: the earlier place that says the same thing, if any.
References: for a cross-reference, what the target says and whether the
  reference is load-bearing (the reader must look) or decorative.

Then, under the table: the section's inventory in one sentence (what it
contains, in order), and every fact that has more than one home.
```

**Output.** The census table, kept with the review that used it (a
review record's *Structure lens* section) or in the round's log entry
where no review was opened.

**Does not decide.** Whether to rebuild the section, which sentence to
cut, or what a restatement should become: those are the reviewer's and
the researcher's, after the census. A census that finds a fact with two
homes reports both; the sweep decides which stays (`editorial_standards.md`,
*One fact, one home*).

## Worked example

```
 # | Kind            | Carries                     | Home            | Restates | References
 1 | statement       | the count is twelve         | [claim 004]     |          |
 2 | display         | the table of twelve         | this display    |          |
 3 | statement       | the count is twelve         | [claim 004]     | 1        |
 4 | cross-reference |                             |                 |          | Section 2: fixes the frame; load-bearing
 5 | transition      |                             |                 |          |
 6 | decoration      |                             |                 |          |

Inventory: a statement, its display, a restatement, a frame reference, a
transition, a flourish. Two homes: the count, at 1 and 3.
```

The reviewer then cuts 3 as a restatement and 6 as decoration, and the
deletion ledger records both.

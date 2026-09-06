# The falsifiability probe as opposition

*Created 5 September 2026; updated 5 September 2026.*

**Role.** Opposition to one's own checks: a check is shown able to fail
before it is trusted to pass. The mechanical part is
`tools/falsifiability_probe.py`, which applies the mutations a check
names and reports a survival (`CHECK_METHODOLOGY.md`, *What is checked
mechanically*, item 3). The role is the reading around it: choosing
mutations that alter what the claim depends on, judging whether those
the check names cover every dependency, and, for a written procedure,
planting the alteration and following the procedure; whether the
project's set is adequate stays the researcher's.

**Fires.** When a check is written, before it is relied on, and before a
plan closes on it (`CHECK_METHODOLOGY.md` §5, *Show every assertion
falsifiable*).

**Reads.** The check, its record, the claim it backs, and the project's
mutation set (`{{MUTATION_SET}}`, `CHECK_METHODOLOGY.md`, *Slots*).

**Prompt.**

```
You are the probe's reader for one check. Read the check at [path], its
record, the claim it backs, and the project's mutation set at [path,
tools/artifacts.toml unless the project moved it]; read nothing else
and write nothing. For each thing the claim depends on (each input
classified derived or imposed in the claim's body, each frame, each
convention), say which mutation in the set alters it, or that none does.
Then read the probe's matrix at [output] and return:

  Dependency | Mutation that alters it | Named by the check | Matrix cell

and, under the table, every dependency no mutation alters, every named
mutation that alters nothing the claim depends on (a robustness check
misfiled), and, for a written procedure, where the alteration is to be
planted and what the record must say when it is caught.
```

**Output.** The table, kept with the check record; a missing mutation is
proposed to the mutation set (`CHECK_METHODOLOGY.md`, *Slots*) with the
dependency it alters; a misfiled one is moved to `Robustness:`.

**Does not decide.** Whether a mutation set is adequate for the project:
the set is the project's, filled at instantiation and amended at the
researcher's direction. The probe's finding, a survival, is the tool's;
the reading adds why.

## Worked example

```
Dependency                          | Mutation that alters it | Named by the check | Matrix cell
the base witness's reading of f. 3r | variant-reading         | yes                | CAUGHT
the choice of base witness          | base-witness-swap       | no                 |
the folio numbering (the frame)     | none                    |                    |

Unaltered: the frame. Misfiled: none. Proposed: a mutation "refoliate"
that shifts every folio number by one, altering the frame [claim 002]
fixes.
```

The check gains `base-witness-swap` on its `Mutation:` line and a
binding for it; the proposal for a frame mutation goes to the researcher.

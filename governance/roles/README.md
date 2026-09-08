# Opposition roles

*Created 5 September 2026; updated 5 September 2026.*

Structured argument against the researcher's own position, as
`MANIFESTO.md` §17 and `VISION.md` require: a reader instructed to find
what is wrong, given a standard prompt so that the role is played the
same way each time and its output has a fixed form. Each role is played
by a fresh session or a subagent (a reader with no access to the first
pass's reasoning, §5, §14) or by a human; the prompt is the same. A
subagent playing a role writes no tracked file: it returns its output to
the main thread, which records it where the role says (§14).

| Role | Fires | Reads | Returns |
|---|---|---|---|
| [refuter.md](refuter.md) | on every sweep or review finding | the finding, the passage, and what it cites | stands, refuted with the reason, or narrowed |
| [documentation_sweep.md](documentation_sweep.md) | after a batch of edits to the rulebooks, indexes, templates, or configuration; first of all after instantiation | the project's documentation, as one system | the disagreements, each with its two homes |
| [blind_referee.md](blind_referee.md) | before a version freezes | the write-up alone | a review record |
| [structure_census.md](structure_census.md) | at the head of a review, and before a review patches a section | the section and the sections it refers to | the census table |
| [deletion_ledger.md](deletion_ledger.md) | on every rebuild | the section before and after, and the census where one was | the two ledgers and the net word delta |
| [coverage_auditor.md](coverage_auditor.md) | before a check backs an established claim | the check, its record, the claim, and a source at a locus | every assertion classified |
| [falsifiability_probe.md](falsifiability_probe.md) | when a check is written | the check, its record, the claim, and the mutation set | the matrix, and the check's named mutations judged against what the claim depends on |

The documentation sweep is not opposition but a reading pass, and it is
kept here because it is played the same way: a standard prompt, a fixed
output, and every finding handed to the refuter.

Each file states the role, when it fires, what the reader may read
(`MANIFESTO.md` §10: what the task names and what those files point to
inside the repository; each prompt narrows that further), the prompt
verbatim, the form of the output, what the role does not decide, and a
worked example. The prompts are generic: a project fills the bracketed
slots and changes nothing else, so that a departure from the standard
prompt is visible.

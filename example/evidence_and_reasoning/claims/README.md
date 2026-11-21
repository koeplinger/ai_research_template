# Claims

*Created 3 September 2026; updated 20 November 2026.*

One file per claim: `NNN_short_name.md`, the number zero-padded to three
digits with an optional lower-case suffix, never reused. A claim is the
citable object of the record: `[claim NNN]` resolves here
(`ONTOLOGY.md` §1.3). The configured claim pattern is the numbered form;
this `README.md` and [`_template.md`](_template.md) fall outside it.

Copy the template to start one. It pre-prints the mandatory fields with
their vocabularies (`ONTOLOGY.md` §8), so that filling in the form is
writing the predicate. Genre and freezing follow the owning plan
(`DOCUMENT_GENRES.md`); who assigns a register is `CHECK_METHODOLOGY.md`
§1. A claim needs a plan before it exists: open one under
`research_plans/` first.

## Contents

| Claim | Kind | Plan | Subject |
|---|---|---|---|
| [001](001_count_1851.md) | computational | 001 | the roll's count of market days in 1851 |
| [002](002_note_states_48.md) | documentary | 001 | the count of market days the note states for 1851 |
| [003](003_monthly_mean.md) | formal | 001 | the mean number of market days a month in 1851 |
| [004](004_duplicates_explain_gap.md) | computational | 001 | repeated rows as the explanation of the difference |
| [005](005_weekdays_1851.md) | computational | 001 | the weekdays of the roll's rows of 1851, and its Tuesdays without a row |

<!-- Every claim appears here; the index is checked (DOCUMENT_GENRES.md,
     What the checker verifies, item 8). Kind and Plan are navigation;
     the register is state, lives in the claim, and is not copied here. -->

## Not claims

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a claim, not indexed as one |

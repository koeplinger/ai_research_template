# Claims

*Created 3 September 2026; updated 6 September 2026.*

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
| [001](001_count_1851.md) | computational | 001 | the roll holds 51 market days in 1851 |
| [002](002_note_states_48.md) | documentary | 001 | the note states forty-eight for 1851 |
| [003](003_monthly_mean.md) | formal | 001 | the mean monthly count for 1851 is 4.25 |
| [004](004_duplicates_explain_gap.md) | computational | 001 | duplicated rows explain the excess |
| [005](005_march_year.md) | computational | 002 | the note counted under a year beginning on 25 March |
| [006](006_ordinary_days_only.md) | interpretive | 002 | the note counted ordinary Tuesdays only |
| [007](007_weekdays.md) | computational | 001 | the 1851 rows fall on Tuesdays and two Thursdays, on distinct dates; three Tuesdays without a row |

<!-- Every claim appears here; the index is checked (DOCUMENT_GENRES.md,
     What the checker verifies, item 8). Kind and Plan are navigation;
     the register is state, lives in the claim, and is not copied here. -->

## Not claims

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a claim, not indexed as one |

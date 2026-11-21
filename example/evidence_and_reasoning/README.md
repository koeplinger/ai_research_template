# Evidence and reasoning

*Created 3 September 2026; updated 20 November 2026.*

The research record: what is claimed, why it is believed, and where every
cited work lives. Every claim made anywhere in the repository is traceable
to evidence in this folder (`MANIFESTO.md` §2, §5). The vocabulary in
which the record relates its parts is `ONTOLOGY.md`; the trust levels are
`CHECK_METHODOLOGY.md` §1; which artifact is in which genre is
`DOCUMENT_GENRES.md`'s.

## Reading order for a session arriving cold

    research_statement.md   the question as posed
    research_result.md      what has been established, condensed
    problem_statement.md    the thesis being tested, and the plans drawn from it
    research_plans/ROADMAP.md   every plan, what it settles, and its status
    claims/README.md        the claims, by number
    the claims and checks the question in hand needs

## Order of first use

A statement, then the keystone, then a plan under `research_plans/`, then
a claim and its check. A claim needs an owning plan before it exists.

## Structure

| Path | Contents |
|---|---|
| [research_statement.md](research_statement.md) | the research question as posed; maintained, changed only on a significant deviation |
| [research_result.md](research_result.md) | the condensed summary of `FINDINGS.md` at the altitude of the write-up |
| [problem_statement.md](problem_statement.md) | the keystone: the researcher's thesis as questions or hypotheses evidence could count against; maintained; SPECULATIVE |
| [terminology.md](terminology.md) | the glossary: established and project-specific terms, and the names the sources use |
| [editorial_standards.md](editorial_standards.md) | the prose standards and the recorded voice |
| [claims/](claims/) | numbered claims, one file each, with the header lines `ONTOLOGY.md` fixes |
| [checks/](checks/) | numbered checks: the record of each, and the procedure where a check is written rather than run |
| [references/](references/) | the reference registry, one file per topic, repository, or data source |
| [research_plans/](research_plans/) | numbered plans and the plan index |
| [derived/](derived/) | what a plan made from a source: transcriptions, collations, extracts, tables, figures |
| [notes/](notes/) | dated notes, of two kinds: working and analytical |
| [public_record_tensions.md](public_record_tensions.md) | the tension ledger |

## Conventions

- Claims and checks are numbered independently, `NNN` zero-padded to
  three digits with an optional lower-case suffix (`006a`), and a number
  is never reused. The configured patterns are the numbered forms; a
  folder's `README.md` and `_template.md` fall outside them.
- A check and its program share a number: `checks/NNN_*.md` records what
  `python_project/src/check_NNN_*.py` does, or is itself the written
  procedure. These are the defaults `tools/artifacts.toml` starts with.
- Every prose file here carries the standard header stamp, and every
  claim, check, plan, and prose derived file carries the field lines
  `ONTOLOGY.md` §1 fixes; a non-prose file under `derived/` carries no
  header at all (`DOCUMENT_GENRES.md` §3).

## Slots

The artifact templates in the folders below carry no slot of their own:
where one needs a slot's value, it points to the Slots table of the file
that owns the slot. This table holds the one slot this file owns.

| Slot | Meaning | Examples |
|---|---|---|
| `{{PROJECT_TITLE}}`: Market days in a synthetic market roll | the project's name, which opens the research statement's question and heads the front page | *Hospital admissions in one city, 1830 to 1850*; *Replicating the 2019 minimum-wage estimates*; *A close reading of one recent paper* |

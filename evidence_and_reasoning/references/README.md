# Reference registry

*Created 3 September 2026; updated 3 September 2026.*

Every citation anywhere in the repository resolves to an entry here
(`MANIFESTO.md` §2). A reference list carried verbatim inside material
imported under `inherited/`, or inside a review by an outside reader,
belongs to its original author and is not registered unless the project
cites the work itself. The registry is self-contained: every work relied
on is registered here in full, so that this repository is readable and
auditable on its own.

## Organization

One file per topic, or per repository or data source where the discipline
prefers (`MANIFESTO.md` §2), `snake_case_name.md`, listed below; the file
pattern is the registry row of `tools/artifacts.toml`. Copy
[`_template.md`](_template.md) to start one. Within a file, one entry per
work, headed `### [ShortKey]`.

| File | Covers |
|---|---|
| <!-- [name.md](name.md) --> | <!-- one line --> |

## The key and the locus

`[ShortKey]` is `[A-Z][A-Za-z0-9]{2,31}` (`ONTOLOGY.md` §1.3): an initial
capital, then letters and digits, no spaces or punctuation. A key names
one work and is never reused. The convention is author, year, and a short
title word run together; a project may fix another, once, here.

Cite a place in the work as `[ShortKey, locus]`, the locus in the units
the project fixes in `{{CITATION_LOCUS}}` (`ONTOLOGY.md`, Slots), for
example `[Key, p. 12]`, `[Key, section 3.2]`, `[Key, f. 12r]`, `[Key,
table 2]`, `[Key, wave 3, variable q17]`.

## Entry format

An entry's fields are bullets, `- Field: value`, inside its `### [Key]`
block; they are not header lines (`ONTOLOGY.md` §1.4). The required
fields are `{{REFERENCE_FIELDS}}`, filled once in `ONTOLOGY.md` (Slots);
the template shows the default set.

```
### [ShortKey]

- Authors:           as the work gives them; the producing body for a dataset
- Title:             as the work or its catalogue gives it
- Where:             venue, series, or repository and collection
- Year:              of the version consulted, or the range the discipline assigns
- Identifier:        DOI, shelfmark, release and version, or URL with the date retrieved
- Keywords:          for finding it across files
- Standing:          searched <where>, D Month YYYY; none found | found, see Disputed
- Disputed:          <what>, [ShortKey of the source]        (only where a dispute exists)
- Witness of:        [ShortKey]                              (only where this is one record of a work)
- Notes:
```

**Standing and Disputed.** What they record is `MANIFESTO.md` §3.

**Witness of.** A manuscript, an edition, a facsimile, a dataset release,
or a vintage that is one record of a work registered under another key
says so (`ONTOLOGY.md` §2.1). Register the work and each record of it as
separate entries, and cite the record consulted, since the locus belongs
to it. Where the work exists only through its records, its `Identifier`
reads `none; see witnesses` and its `Year` is the range the discipline
assigns; neither is reported missing. A facsimile names the manuscript it
reproduces, the manuscript names the work; the tool follows the chain.

## Not entries

| File | |
|---|---|
| [_template.md](_template.md) | the file template; carries no entries |

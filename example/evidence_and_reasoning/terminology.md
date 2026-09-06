# Terminology

*Created 3 September 2026; updated 6 September 2026.*

This file defines the terminology used in the project (`MANIFESTO.md`
§9). Where established terminology exists, it is cited. Where a
construction, category, variable, or notion is specific to this project,
it is marked **(project-specific)**. The threshold for inclusion is a term
a reader needs in order to follow the checks and the reasoning. The
project's standard name for each thing, and the mapping from any source's
own term to it, or the statement that no mapping is asserted, is recorded
here (`editorial_standards.md`, Conventions).

## Index

**Established terms**: none, since the sources are synthetic

**Project-specific terms**: market day ; roll

## Established terms

None: the sources are synthetic, and no established terminology is
leaned on.

## Project-specific terms

### market day (project-specific)

A row of the roll: a day on which the fictional town's market was
held, of kind `ordinary` (a Tuesday) or `fair`. The name is the
roll's own column heading's sense; the rule that constructs the rows
is `python_project/src/make_roll.py`, and the count of them for 1851
is fixed in [check 001].

### roll (project-specific)

The file `source_documents/Roll1851_market_roll.csv` at its committed
revision, one row per market day, the source of record for every count
in this project [Roll1851].

## Names the sources use

| Source and locus | The source's term | This project's standard name | Mapping |
|---|---|---|---|
| [Note1, p. 1] | market days | market day | by construction, rule fixed in [check 001]; whether the note's count is under the same rule is not asserted |

# Inherited material

*Created 4 September 2026; updated 20 November 2026.*

Material from another repository, a private collection, or unpublished
work enters this project only at the researcher's explicit direction and
under this policy (`MANIFESTO.md` §6): an import is a **frozen copy at its
original date, with attribution**, listed once in the ledger below,
verbatim unless its row there records a correction made at the
researcher's direction (`MANIFESTO.md` §12), and **re-verified here by
the discipline's own standard before anything builds on it**
(`MANIFESTO.md` §5). Each import keeps the terms its row here records,
and `LICENSE.md`, *Material under its own terms*, relicenses none of it.
An imported file carries no header stamp of its own: it is dated by its
row here. Where access conditions keep the material out of the
repository, it is imported by locator only (`MANIFESTO.md` §6).

Where a row records a correction, its Notes cell names what was corrected
and the prompt that directed it, in plain words such as *departs from the
origin in the heading of the third column, corrected at the researcher's
direction, prompt NNN*; where the researcher made the correction by hand,
the cell says so in place of the prompt. It is never written as
`Corrected <date>:`, a stamp word with a date and a colon, which the
linter reports in every genre, nor with a phrase such as `previously read`
or `before the correction`, which it reports in a current-state index
like this one (`DOCUMENT_GENRES.md`, *What the checker verifies*, item 5).

Where the origin publishes a checksum for the file, or the copy is kept
outside version control, git-ignored or outside the tree, the row records
the copy's SHA-256 checksum in its *Imported to* cell, after the path or
after *by locator only*. Where the copy is several files, the checksums
go in a checksum list, `<copy>_sha256.txt` in this folder, tracked even
where the copy is not: one line per file, its SHA-256 checksum and then
its path inside the copy. The row links the list and records the list's
own checksum. Nothing in this folder has its line endings converted on
checkout (`.gitattributes`), so every checksum recorded here holds on
every system.

Where the row records a checksum and the copy is corrected at the
researcher's direction, the row keeps the checksum of the copy as
imported and adds the corrected copy's after it, marked *as imported*
and *as held*. Where the checksums are in a list, the list is kept as
imported, and the corrected copy's go in a second list,
`<copy>_held_sha256.txt` in this folder, which the row links beside the
first, with its own checksum.

A **candidate list** may be kept here at the researcher's direction
(`MANIFESTO.md` §10): each item by locator and access conditions as §6
allows, with what it establishes and why it might be wanted, and nothing
copied. A candidate is context in `PRECEDENCE.md`'s sense, carried at its
tier and never cited as a result.

## Imported

| Origin | Imported to | Date at the origin | Imported on | Re-verified by | Notes |
|---|---|---|---|---|---|
| <!-- author or holder; the origin's identifier as a second reader could reach it: repository and commit, collection and shelfmark, or a release; never a local path; its license --> | <!-- [path](path) under inherited/, or: by locator only; then the copy's SHA-256 checksum, or a link to its checksum list and the list's checksum, where the policy above asks for one --> | <!-- the date the copied revision bears --> | <!-- D Month YYYY --> | <!-- [check NNN], or: not yet, nothing builds on it --> | <!-- one line; where the copy departs from the origin by a correction made at the researcher's direction: what was corrected, and the prompt, or: by the researcher's hand --> |

# Paper

*Created 4 September 2026; updated 4 September 2026.*

The write-ups: the main write-up in its versions, standalone notes, and
the reviews of both. `paper/` is the template's name for the
deliverable's folder whatever its form (`DOCUMENT_GENRES.md` §2); the
form, how a version marks itself on the page, and what is released with
it are {{DELIVERABLE}}.

## Conventions

- **One living copy of the main write-up at a time.** A released version
  freezes with what is released with it and is by default succeeded
  rather than corrected: what a later reading asks for goes into the next
  version, and the released version is marked `superseded by <path>` when
  that version releases (`DOCUMENT_GENRES.md`, *Versioned write-ups*).
- **A release is the researcher's**: a `Released D Month YYYY` stamp on
  the version, and a row in the changelog. The first version has no
  changelog; its release is its stamp and its row in the Contents table
  below.
- **Changes between versions go in a changelog**, `vN_to_vM_changelog.md`,
  which is live until vM releases and freezes then. Copy
  [`_template_changelog.md`](_template_changelog.md). The ledgers of a
  rebuild live there.
- **Standalone notes carry their date first in the filename**,
  `YYYY-MM-DD_short_topic.<ext>`, like every dated record; a note is
  released by the researcher's `Released` stamp, with no changelog, and
  freezes then.
- **Every version has a blind referee review before it freezes**
  (`MANIFESTO.md` §17), under [`reviews/`](reviews/).
- **What is released with a version** is {{DELIVERABLE}}: where the
  deliverable is built, its build output; where it is not, the file
  itself. Scratch produced on the way is not committed. The prose is
  governed by `evidence_and_reasoning/editorial_standards.md`, *Writing
  for publication*, on every unfrozen draft here.

## Releasing a version

1. A review, including a blind referee, under `reviews/`.
2. Every finding refuted or not; the fixes applied where the rules allow,
   brought to the researcher where they do not.
3. The researcher directs the release: the `Released D Month YYYY` stamp
   goes into the version's header, and the changelog's release row is
   written.
4. What {{DELIVERABLE}} releases with the version is produced and
   committed by the researcher.
5. The previous version is marked `superseded by <path>`.
6. The changelog and the review freeze with the round that closes.

## Contents

| File | What it is |
|---|---|
| <!-- [main_v1.md](main_v1.md) --> | <!-- the main write-up, version 1 --> |
| <!-- [v1_to_v2_changelog.md](v1_to_v2_changelog.md) --> | <!-- changes from v1 to v2 --> |
| [reviews/](reviews/) | the reviews, indexed in [reviews/README.md](reviews/README.md) |

## Not write-ups

| File | |
|---|---|
| [_template_changelog.md](_template_changelog.md) | the changelog template |

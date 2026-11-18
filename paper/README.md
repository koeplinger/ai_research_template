# Paper

*Created 4 September 2026; updated 18 November 2026.*

The write-ups: the main write-up in its versions, standalone notes, and
the reviews of both. `paper/` is the template's name for the
deliverable's folder whatever its form (`DOCUMENT_GENRES.md` §2); the
form, how a version marks itself on the page, and what is released with
it are the deliverable's, which `DOCUMENT_GENRES.md` fixes in its Slots
table.

## Conventions

- **One living copy of the main write-up at a time.** A released version
  freezes with what is released with it. The version, in every form it is
  released in (its source, a typeset or rendered copy, a filed document),
  is succeeded by the next, never corrected; what else is released with
  it, such as its data, code, or transcriptions, is corrected as its own
  genre allows, unless the researcher has directed for that release that
  some or all of it is never corrected either (`MANIFESTO.md` §12;
  `DOCUMENT_GENRES.md`, *Versioned write-ups*).
- **A release is the researcher's**: a `Released D Month YYYY` stamp on
  the version, and a row in the changelog. The first version has no
  changelog; its release is its stamp and its row in the Contents table
  below.
- **Changes between versions go in a changelog**, `vN_to_vM_changelog.md`,
  which is live until vM releases and freezes then. Copy
  [`_template_changelog.md`](_template_changelog.md). The ledgers of a
  rebuild live there. A version's filename ends in `_vN` before its
  extension, as in a file named main_v2.md, which is how the ledgers are
  paired with the version they describe (`tools/check_residue.py`). A
  reader's marked-up copy is accounted for in the changelog's markup
  ledger, or in a review where the version is the first
  (`reviews/README.md`).
- **Standalone notes carry their date first in the filename**,
  `YYYY-MM-DD_short_topic.<ext>`, like every dated record; a note is
  released by the researcher's `Released` stamp, with no changelog, and
  freezes then.
- **Every version has a blind referee review before it freezes**
  (`MANIFESTO.md` §17), under [`reviews/`](reviews/).
- **What is released with a version** is what the deliverable names:
  the version itself, as its build output where the deliverable is built
  and as the file itself where it is not, and what else goes out with it,
  such as data, code, or transcriptions. Scratch produced on the way is not committed. The prose is
  governed by `evidence_and_reasoning/editorial_standards.md`, *Writing
  for publication*, on every unfrozen draft here.
- **Where the deliverable is built, the round check gates the build and
  the bibliography** from the `[publication]` table of
  `tools/artifacts.toml`, which names the build command, its sources,
  outputs, and log, and the bibliography with its citation patterns; it
  starts disabled. A project that publishes otherwise leaves it disabled,
  and this bullet says so.
- **The main thread may run the build command within a round**, except to
  produce what a version is released with, and a subagent may not, since
  the build writes into the working tree (`MANIFESTO.md` §14). What the
  build writes is left uncommitted for the researcher (`MANIFESTO.md`
  §15).

## Releasing a version

1. The documentation consistency sweep
   (`governance/roles/documentation_sweep.md`), and the recount of
   `CURRENT_STATE.md`, `FINDINGS.md`, and
   `evidence_and_reasoning/research_result.md` that item 3 of the
   consistency sweep of the record makes (`CHECK_METHODOLOGY.md` §7), so
   that the version is reviewed and frozen with current counts.
2. Where the researcher directs it, the standing of each work the version
   cites is searched again as `MANIFESTO.md` §3 describes, each registry
   entry's `Standing:` bullet is brought up to date with what the search
   found, and anything that bears on the version is brought to the
   researcher.
3. A review, including a blind referee, under `reviews/`.
4. Every finding refuted or not, and every mark of each marked-up copy a
   reader returned accounted for in its markup ledger
   (`_template_changelog.md`); the fixes applied where the rules allow,
   brought to the researcher where they do not. While a direction to
   finish a list holds, a finding outside the list is left for the next
   version, except a false statement in the version, which is brought to
   the researcher once (`HOW_IT_FITS_TOGETHER.md`, *Finishing a version or
   a plan*).
5. Every figure, table, and printed value the version releases, in it or
   with it, read against the disclosure rule (`MANIFESTO.md` §6), with the
   approval that rule requires, where it requires one.
6. The researcher is shown how this version differs from the previous
   one, where there is one, in the two texts themselves and not only in
   the changelog, and directs the release: the version's page is made to
   read as the deliverable specifies for a released version, any draft
   marker removed; the `Released D Month YYYY` stamp goes into its header;
   and the changelog's release row is written.
7. What the deliverable releases with the version is produced by the
   researcher; any figure, table, or printed value in it that step 5 did
   not read, such as a value the log of a final run prints, is read
   against the disclosure rule as step 5 says; and the researcher then
   commits it, every file of it: one whose name `.gitignore` ignores, such
   as a run log ending in `.log`, is first re-included there by a line of
   its own, as the attachments are, and given a row in
   `tools/artifacts.toml` where none matches it.
8. The previous version is marked `superseded by <path>`.
9. The changelog and the review freeze with the round that closes.
10. Where the version is deposited outside the repository, the researcher
    deposits it as it was committed. The text the deposit asks for besides
    the files, such as the title, the authors, and the abstract, is copied
    from the released version, never retyped, and compared with it word
    for word before it is submitted.
11. Once it is deposited, it is read back where it was deposited, by the
    researcher or by the assistant pointed at it (`MANIFESTO.md` §10):
    its identifier resolves to it, and what the deposit shows matches the
    released version. A difference is put right at the deposit, never in
    the version. The version's row under *Contents* then records where,
    when, and under which identifier it was deposited.
12. The documentation consistency sweep again, last, over what was
    changed since the last documentation sweep
    (`governance/roles/documentation_sweep.md`, *Reads*), and the recount
    of step 1 again, of each of those three files the release wrote into.

## Contents

| File | What it is |
|---|---|
| <!-- [main_v1.md](main_v1.md) --> | <!-- the main write-up, version 1; once it is deposited, also: deposited at <where>, D Month YYYY, as <identifier> --> |
| <!-- [v1_to_v2_changelog.md](v1_to_v2_changelog.md) --> | <!-- changes from v1 to v2 --> |
| [reviews/](reviews/) | the reviews, indexed in [reviews/README.md](reviews/README.md) |

## Not write-ups

| File | |
|---|---|
| [_template_changelog.md](_template_changelog.md) | the changelog template |

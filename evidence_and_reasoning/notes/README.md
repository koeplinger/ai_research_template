# Notes

*Created 3 September 2026; updated 19 November 2026.*

Dated notes: `YYYY-MM-DD_short_name.md`. A note is a dated record
of what a sweep, an audit, a search, a reading, a day in the archive, a
cleaning or run, or a line of reasoning found on that day. A note's
subject is an event, so it is exempt from the narrative rule for what it
records, though not for how its own text came to read, and is frozen on
writing, or with the plan that owns it (`DOCUMENT_GENRES.md` §2 and *Dated
records*). Copy [`_template.md`](_template.md) to start one. The record of
a search is a *search record*, and its hits are listed as
`evidence_and_reasoning/references/README.md` says.

## Two kinds

This folder distinguishes two kinds of note, and a note says which in the
first line after its header.

- **A working note.** A sketch that speculates, or a record of the day
  without inference: a reading log, an archive day, a bench day, a
  cleaning or run log. Where the discipline keeps its day-to-day record
  outside this repository (in a laboratory notebook, a field book, an
  enclave's session log), the working note carries that record's locator
  rather than copying it; once a claim is collated against that record,
  the source index holds it as a source consulted at its locator
  (`source_documents/README.md`).
  Never cited as a result; what it records enters the record through a
  plan and its checks.
- **An analytical note.** Construction, sanity checks, and second pass
  recorded (`CHECK_METHODOLOGY.md` §8; `MANIFESTO.md` §5), serving a
  claim, a check, or a plan. It is cited by path from a claim's
  *Evidence and route* as material of the route; it backs nothing. A
  derivation or reading that *establishes* a claim is written as a check,
  not as a note.

The decision rule: analytical if a claim, check, or correction round will
cite it; otherwise a working note. A working note may later be superseded
by an analytical one; when in doubt, working.

A pre-registration protocol is an analytical note written before the
evidence is consulted, its commit evidencing the date, and named as the
locator of a check's `Pre-registered` stamp. Where the discipline lodges
its pre-registrations with a third party, that registration is the
stronger evidence of the date, and the stamp's locator is its identifier
or URL instead of, or beside, the note's path, the two comma-separated;
the note then carries the registered text verbatim so that a reader of
this repository can see what was fixed without leaving it. The checker
splits the locator at each comma followed by a space and reads a part with a slash in it, or
a dot in its last segment, as a path and resolves it, and leaves alone a
URL that opens with its scheme, such as `https://`, and any other
identifier; a DOI is therefore written as its resolver's URL. The note
carries no `Plan:` line, so it is frozen on writing; the check that names
the protocol is the plan-owned artifact.

## Contents

| File | What |
|---|---|
| <!-- [YYYY-MM-DD_short_name.md](YYYY-MM-DD_short_name.md) --> | <!-- one line, naming the kind and the plan if any --> |

## Not notes

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a note, not indexed as one |

# Research plans

*Created 3 September 2026; updated 3 September 2026.*

Numbered plan files, `NNN_short_name.md`, the number zero-padded to three
digits with an optional lower-case suffix, never reused, plus the plan
index [`ROADMAP.md`](ROADMAP.md). A plan turns a line of work into a
hypothesis with pre-registered confirmation and refutation criteria, or,
where there is no hypothesis, into a task with a pre-registered closure
criterion; execution happens only through an engaged plan, and every
artifact the work produces names the plan that owns it. Copy
[`_template.md`](_template.md) to start one.

## Lifecycle

A plan's `Status:` header line holds exactly one of `DRAFT`, `ENGAGED D
Month YYYY`, or `CLOSED D Month YYYY, verdict <V>`, the verdict one of
`CONFIRMED`, `REFUTED`, `COMPLETE`, or `ABANDONED`. What each verdict
means, and that both transitions are the researcher's, is
`DOCUMENT_GENRES.md`, *Words used here*: the researcher writes the line
or directs the assistant to write it, and the assistant never changes it
on its own initiative.

While a plan is open, everything it owns is current state
(`DOCUMENT_GENRES.md`, *Artifacts of an open plan*); on closure it
freezes, with any verdict.

## Rules

- **More than one plan may be `ENGAGED`.** The plan index shows which,
  and the assistant says so in its reply while it is true
  (`MANIFESTO.md` §16). Where two engaged plans touch the same material,
  each plan's *Out of scope* section names which plan owns what.
- A plan states its hypothesis precisely enough that evidence could count
  against it, names its prerequisites, says which keystone hypothesis it
  serves or why none, and pre-registers what counts as confirmation and
  what as refutation before execution begins. Where the pre-registered
  criteria decide neither way when the tasks are done, the plan closes
  `ABANDONED` with that outcome as its reason, unless its *Confirmation
  and refutation* section pre-registered what such an outcome closes as.
- Results live in claims and checks; sketches live in `../notes/` and
  are never cited as results.
- The index is the one place to see every plan with its status; the
  checker compares its status column with each plan's `Status:` line
  (`DOCUMENT_GENRES.md`, *What the checker verifies*, item 6).

## Not plans

| File | |
|---|---|
| [_template.md](_template.md) | the template; not a plan, not indexed as one |
| [ROADMAP.md](ROADMAP.md) | the plan index; current state |

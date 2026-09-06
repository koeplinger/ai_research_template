# Research statement

*Created 6 September 2026; updated 6 September 2026.*

## The question

Market days in a synthetic market roll asks: does the market roll of a
fictional town, as shipped under `source_documents/` at its committed
revision [Roll1851], support the count of market days for 1851 that the
secondary note shipped beside it states [Note1, p. 1]? A count read off
the roll by a gated check, compared with the note's figure collated
against the note itself, answers it; a count reported from memory, or a
figure quoted from the note without collation, does not.

## The work this project does

1. **Establish the base.** Read the roll's count for 1851 by a
   program that would fail if the count were otherwise, and collate the
   note's stated figure against the note (`MANIFESTO.md` §5).
2. **Classify the inputs.** For the count, record what is derived (the
   calendar the roll's dates follow), what is imposed (the roll is
   synthetic and its year boundary is the calendar year), and what is
   conjectured (nothing at inception) (`CHECK_METHODOLOGY.md` §4).
3. **Pursue what the base raises.** Where the two figures differ, rule out
   the explanations the record can decide, and reserve the ones it
   cannot to a plan of their own.

## Where it stands

See `CURRENT_STATE.md`.

## Scope and what is not claimed

- No new result is claimed at inception.
- Anything from outside this repository that the work builds on is
  imported and re-verified (`MANIFESTO.md` §6); nothing else is assumed.
- The sources are synthetic: the project claims nothing about any real
  town, register, or note, and its results are results about the files it
  ships.

## Method

Per `MANIFESTO.md` and `CHECK_METHODOLOGY.md`. The unit of work is the
check; a negative result is a result; no claim is worded stronger than its
evidence.

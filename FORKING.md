# Forking: the repository is yours

*Created 8 September 2026; updated 8 September 2026.*

Once you clone this template, every rule in it is yours to change. A
project will develop needs the template did not anticipate, and a
researcher who adapts the governance to their work is using it correctly,
not abandoning it (`VISION.md`, *The repository is the researcher's*).

There is one thing this file asks, and it is not that you keep anything:

> **Change it on purpose, and leave the change legible.** A rule you
> delete deliberately is fine. A rule left standing and quietly ignored is
> a lie the repository tells a later reader, and the reader it misleads
> most is you in eighteen months.

The difference between the two is about ten minutes of work, and this file
is those ten minutes.

---

## What kind of change is it?

Four kinds, in rising order of what they cost.

### 1. A value

Anything in a Slots table: the persona, the deliverable, the mutation set,
the spelling, the parties. Changing one is ordinary work. Edit it where
its owner defines it, edit the machine half in `tools/artifacts.toml`
where it has one, and record the change in the round's log entry. Nothing
else is owed.

### 2. A name

A word this methodology uses in its own sense, which your field has taken.
`GLOSSARY.md`, *Renaming a word this template uses*, is the procedure:
prose is yours to change freely; a header field name is configured in
`[fields.roles]` and every tool follows; a closed-vocabulary value is
configured under `[vocab]`. Rename **before the record exists**, because
the log is immutable and a frozen artifact keeps its wording, so the cost
rises with every round.

Renaming changes no argument. A project that renames *mutation* to
*planted fault* still owes every check a fault it would fail under.

### 3. A rule

Amending a rulebook. The rulebooks are current-state documents, corrected
in place, and `MANIFESTO.md`, *Amending this manifesto*, says how: at your
explicit direction, with the prompt or the commit as the amendment's
provenance, the updated date set, and the log entry carrying the reason.

What the amendment owes:

1. **Say what the rule was for.** Most rules here are one half of a pair.
   Before changing one, find the other half: the tool that enforces it,
   the template that pre-prints it, the index that lists it, the reminder
   that fires on it. `HOW_IT_FITS_TOGETHER.md`, *Where a rule lives*, and
   `governance/README.md` map them.
2. **Change the halves together**, in one round.
3. **Make the documentation consistency sweep afterwards**
   (`governance/roles/documentation_sweep.md`). Amending a rule in one
   file and leaving it restated in three is the exact defect that sweep
   exists to catch, and it will catch yours.

### 4. A mechanism

Removing or replacing a whole thing: a check, a role, a folder, a tool,
the harness wiring.

---

## Removing a mechanism

`governance/README.md`, *Removing a mechanism*, states the rule: a removal
is deliberate and legible. In practice, four steps.

1. **Strike the row with the reason.** Every mechanism has a row in
   `governance/README.md` or `tools/README.md` giving what it enforces,
   when it fires, and what it does not decide. Strike it there and say
   why, in one line. That row is where a later reader looks first.
2. **Amend or retire the rule it served.** A mechanism enforces a rule
   that lives in a rulebook. Either amend the rule, or keep it and say in
   the rulebook that its enforcement is now by hand. What you must not do
   is leave the rule stated and its enforcement silently gone.
3. **Remove the wiring.** A folder is not gone until its
   `[[artifact]]` and `[[index]]` rows in `tools/artifacts.toml` are gone,
   and until nothing points at it: the root `README.md`, the folder
   indexes, the tool docstrings. The path check reports what you miss,
   which is the point of it.
4. **Record it in the round's log entry**, under corrections and
   departures.

Then run the round check and the documentation sweep. If both are clean,
the removal is complete.

### What each mechanism costs to remove

| Remove | Also touches |
|---|---|
| the Python check suite | `python_project/`'s three artifact rows and three index rows in the configuration, the root README's folder row, `python_project/README.md`'s own removal note, and three tool docstrings (the concordance check, the probe, the run ledger); `{{CHECK_FORM}}` becomes a written procedure alone |
| the harness wiring | `governance/harness/`, the tracked settings file and its `harness-settings` row in the configuration, its line in `.gitignore`, and the `{{REPLY_HOOK}}` slot, which becomes *none, with the form kept by hand*. **Keep `tools/check_status_reply.py`**: the round check imports it, so ROUND-2 goes with it |
| the privacy scan | its row in the two READMEs; the staged-scan block of the pre-commit hook and the whole commit-message hook that `tools/install_hooks.sh` writes, and the installer's account of both. `MANIFESTO.md` §6 states the rule it serves in discipline-neutral terms and names no scanner, so nothing there has to change |
| the tension ledger | `PRECEDENCE.md`'s compliance section, which requires a row; amend it or the rule stands unenforced |
| the publication gate | nothing: it ships disabled, and `paper/README.md` says a project that publishes otherwise leaves it so |
| derived material | its two rows and its index row; `source_documents/README.md` names it as the destination |
| a standing role | its file, its row in `governance/roles/README.md`, and any reminder that proposes it |

---

## Replacing a mechanism

Same as removing, plus: put the replacement's row where the old one was,
so the map stays complete. A replacement that answers the same question a
different way is the healthiest kind of fork, and the row is what tells a
later reader that the question is still being answered.

If your replacement is a tool, the shipped ones have a shape worth
keeping: it reports and decides nothing; it says in its docstring what it
does not read; and it has a `--selftest` that shows every check firing and
the unplanted tree clean. That last one is why you can trust a tool you
have not read.

---

## Adding something the template does not have

Adding is cheaper than removing and owes less: a folder needs an
`[[artifact]]` row, an `[[index]]` row, a `README.md` index, and a
`_template.md` if things in it recur. A new header field needs a row in
`ONTOLOGY.md`'s catalogue naming what it relates, its surface syntax, the
rulebook that owns it, the check that enforces it, and the question it
answers; the field is then added to the template that ships it, and to
`[fields] names` and `[fields.roles]` in the configuration. `ONTOLOGY.md` §8 says a
predicate no template pre-prints is not shipped, which is a good rule to
keep: a field nobody is prompted to fill is a field nobody fills.

---

## What is worth keeping

Not a rule, an observation, and you may disagree with it.

The parts of this methodology that earn their cost are the ones that make
a later reader independent of your memory: **the immutable log**, because
it is the only record of what you believed at the time; **the register on
every claim**, because *checked* and *a source says so* are different and
prose hides the difference; **the planted fault**, because it is the
cheapest proof that a check is connected to its claim; and **the refuter**,
because a first reader's findings do not all survive a second, and acting
on all of them is worse than acting on none.

The rest is scaffolding, and scaffolding is meant to be reshaped.

## Slots

None. This file is about changing the template and is the same in every
project.

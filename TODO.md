# What this template does not have yet

*Created 8 September 2026; updated 19 November 2026.*

The template's own list of work, kept at the root while the template is
maintained. It is not a project's file: instantiation leaves it behind,
along with the worked example and the interim review records, because a
project's own open work belongs in its plans and its roadmap
(`evidence_and_reasoning/research_plans/ROADMAP.md`), not here.

Each item says what it is, why it is wanted, and what it would touch, so
that whoever picks one up knows the size of it before they start. Nothing
here is promised: the template is complete and usable as it stands, and
every item below makes it better rather than finished.

**The pace is deliberate.** The template is live and working, so the bar
for changing it is higher than it was while it was being built: each item
below arrives on its own, with its own review, rather than as part of a
push to finish. The first item is the one a reader is most likely to trip
over, because the shipped harness is armed by default.

---

## 1. More than one AI vendor

**What.** Code, configuration, and a usage path for AI assistants and
harnesses other than the one the template was built with, added one vendor
at a time.

**Why.** The methodology is about the record, not about who writes it, and
nothing in the rulebooks depends on a particular assistant. The wiring
does. Today one harness is wired and the rest of the arrangement is a
promise: `governance/harness/` holds one folder per harness,
`{{REPLY_HOOK}}` is the slot that names which, and
`governance/harness/README.md`, *Adding a wiring, and removing one*, says
what adding a wiring or removing the shipped one costs. A second wiring
turns that promise into a demonstrated fact, and until one exists the
claim that the template endorses no harness is untested.

**What it touches.** A new folder under `governance/harness/`, with its
own README and whatever the harness needs to run
`tools/check_status_reply.py` after a reply and `tools/session_brief.py`
at session start; the settings or configuration file that harness reads,
and its row in `tools/artifacts.toml`; the line in `.gitignore` that names
a per-user settings file; the `{{REPLY_HOOK}}` slot's examples; and
whatever `tools/new_project.py` must ask so that a project picks its
harness at instantiation rather than deleting one afterwards. The tools
themselves know no harness and should not have to change; if one does,
that is the finding.

**Open question.** Whether *vendor* and *harness* want separate slots. They
are separate axes: one assistant may run in several harnesses, and one
harness may run several assistants. The template currently has a slot for
the wiring and nothing for the assistant, which is right only as long as
no rule depends on which assistant it is.

---

## 2. Diagrams of the ontology

**What.** Pictures of what `ONTOLOGY.md` states in prose and tables: the
subjects, the predicates, and the objects, and how a claim, a check, a
source, a plan, and a write-up relate through them.

**Why.** The ontology is the thing that makes the artifacts one system
rather than a folder of forms, and it is the hardest part to hold in the
head from the forty-eight rows of its catalogue. A reader who can see the
graph can see at once what a claim rests on, what a check backs, and
where a predicate has no arrow into it.

**What it touches.** `ONTOLOGY.md` first, and probably
`HOW_IT_FITS_TOGETHER.md`, which explains the same thing in words for a
reader who has not opened the ontology. Whatever form the diagrams take
has to survive being read in a terminal and in a plain-text diff, has to
carry a header stamp or be listed in an index that dates it
(`DOCUMENT_GENRES.md` §3, on non-prose files), and needs a row in
`tools/artifacts.toml`. A diagram that disagrees with the table it
illustrates is the defect the documentation consistency sweep would then
have to catch, so the two want to be generated from one source or checked
against each other.

---

## 3. A guided setup, from a single first prompt

**What.** A mode in which a researcher who has cloned the template types
something like *let's start* and is walked through the decisions, one
question at a time: the expert the assistant works as, the instrument of
record, the dash convention, the rest of the sixteen slots, and finally
the research question and the first plan.

**Why.** The template asks for sixteen decisions before any work begins,
and `GETTING_STARTED.md` explains them well but assumes a reader who will
sit and read. The shortest honest path from a fork to a first round is a
conversation, and the assistant is already there. It would also make the
setup round self-documenting: the answers are the log entry.

**What it touches.** Most of it exists. `GETTING_STARTED.md` §3 puts
each slot's question in plain words, with filled examples from five
fields, and `tools/new_project.py` asks the same words in a terminal; the
three slots that wait for a write-up come last, and may stay open by
decision. An assistant asked in a clone to make a project runs setup as
one pass (`GETTING_STARTED.md`, *Setup at a prompt, as one pass*): it
puts the questions one at a time, writes the answers to a file and runs
the tool once, and records the whole exchange as the project's entry
001. What is missing is the standing prompt that starts it: its words,
and its row in `HOW_IT_FITS_TOGETHER.md`'s list of suggested prompts.
Each question stops for the researcher's answer, with the assistant's
recommendation, where it has one, after the options and labeled as its
own (`MANIFESTO.md` §16, *Putting a decision*).

---

## Slots

None. This file is the template's own work list and is left behind when a
project is made.

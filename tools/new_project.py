#!/usr/bin/env python3
"""The instantiation procedure: this template, made into a project (GETTING_STARTED.md, sections 1 to 3).

Created 8 September 2026; updated 16 November 2026.

What it does, printing each step and what it could not do:

  1. copies the files the template's git repository tracks, as they stand
     in its working tree, and nothing else, so that an answers file, a
     virtual environment, or local harness settings beside them stays
     where it is; leaves behind what belongs to the template's own
     construction (the worked example, the template's work list, and this
     program; the interim review records, the git history, and the local
     privacy list are never tracked); and makes the new tree a git
     repository.  A file not yet added to git is not copied.  A template
     folder that is not a git repository of its own, such as an unpacked
     archive, is copied whole except for what it leaves behind and the
     caches, and the run says so;
  2. removes the pointers to what it left behind, each with the comment
     block that belonged to it, so the path check has nothing to report;
  3. strips every `> **Build lens.**` blockquote, and the two sections of
     MANIFESTO.md that describe the two lenses;
  4. converts the shipped prose to the project's spelling variant, so that
     a project not writing in the template's variant does not inherit a
     failing gate; it converts only what the spelling check reads, so
     quotations, comments, and code keep their spelling, and it runs
     before the slots are filled, so no answer is rewritten;
  5. fills the slots it is given: the value into the Slots table of the
     file that owns it, and the token replaced by the value in the prose
     of every markdown file.  The guide's pages and GLOSSARY.md are left
     alone, since they are about slots rather than carrying them, and so
     are the configuration's comments and program source, which name
     slots on purpose.  A value marking a slot open by decision is
     refused: that marker is written in the slot's owner row itself, never
     given to this program (GETTING_STARTED.md section 3); a closing period
     is dropped from a value, since the sentence it lands in supplies its
     own;
  6. writes the machine halves in tools/artifacts.toml, each under the
     table it belongs to, so that a value the tools read is not left at
     the template's answer;
  7. renames any header field whose name the project's discipline has
     taken ([fields.roles]; GLOSSARY.md, "Renaming a word this template
     uses"), in the configuration, the templates, and the rulebooks;
  8. adds the project's copyright holder and citation to the licenses,
     each only where it is given, and KEEPS the template's, which CC BY
     4.0 requires of an adaptation; it names each license text it could
     not find;
  9. installs the git hooks, which are not cloned;
 10. writes a project front page over the template's README, its title
     left as {{PROJECT_TITLE}} where none is given; writes a dated working
     note under evidence_and_reasoning/notes/ recording what the run did
     and what it left to the researcher, and points to it from the head of
     GETTING_STARTED.md; and stamps every file it changed, and only those,
     with the day it runs, read from the clock: a file it did not change
     keeps the template's dates (DOCUMENT_GENRES.md section 3);
 11. runs the round check in the new tree and prints what it found.

It decides nothing about the research: every value is the researcher's,
asked for one at a time or read from an answers file.  It writes no log
entry; GETTING_STARTED.md section 4 says which entry records the setup and
what follows it.  It prints the new tree by its folder name, so that what
it prints can be recorded without a local path.  On any failure it removes
the half-made tree rather than leaving one behind.

Usage
    python3 tools/new_project.py --template > ../answers.toml
    python3 tools/new_project.py --into ../my-project --answers ../answers.toml --yes
    python3 tools/new_project.py --into ../my-project --answers ../answers.toml
    python3 tools/new_project.py --into ../my-project
    python3 tools/new_project.py --selftest

`--answers` reads the values from a file, which belongs outside both the
template and the new project; without `--yes` it asks about every value,
showing what the file gave.  Without `--answers` it asks about all of
them.  `--yes` asks nothing and uses the file as it stands.

Exit status: 0 when the new tree's round check is clean; 1 when it reports
findings (which are named, and are the researcher's to clear); 2 on a
usage error, an answers file this program cannot use, a target that exists
and is not empty, is inside the template, or contains it, or a machine
without git.
"""
from __future__ import annotations

import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- the slots

# Every slot, the file whose Slots table owns it, and the question
# GETTING_STARTED.md section 3 asks for it in plain words, word for word
# (the self-test compares the two).  The owner is where the value is
# written; each rulebook's own Slots section fixes which file that is.
SLOTS: list[tuple[str, str, str]] = [
    ("PROJECT_TITLE", "evidence_and_reasoning/README.md",
     "What is the project called? A short descriptive name: it opens the research statement's question and heads the front page."),
    ("PERSONA", "MANIFESTO.md",
     "What kind of expert should the assistant work as? A field and, where it helps, a specialty; the assistant takes that role in every session."),
    ("VERIFICATION_TOOL", "CHECK_METHODOLOGY.md",
     "What does a second person return to when repeating a verification? The software, data, source, or written procedure, named precisely enough (a version, a release, an archive reference, the form consulted) that they reach the same thing."),
    ("CHECK_FORM", "CHECK_METHODOLOGY.md",
     "A check is one self-contained investigation of one claim. Is a check here a program that prints its result, a written procedure a person follows and records, or both, chosen claim by claim?"),
    ("MUTATION_SET", "CHECK_METHODOLOGY.md",
     "Which deliberate faults will you plant in what your claims depend on, to show that each check can fail? Give each a short name and say what it alters; a change a claim should survive belongs to a robustness check instead."),
    ("PARTIES", "ONTOLOGY.md",
     "Besides you and the assistant, who will the record credit by name for producing or checking a piece of work? Name each person, group, or service, or answer none; the tools report any name not on the list."),
    ("CITATION_LOCUS", "ONTOLOGY.md",
     "When a citation points to a place inside a work, in what units is that place given? Every unit your sources need, such as page and section, folio and line, table and column, or paragraph number."),
    ("REFERENCE_FIELDS", "ONTOLOGY.md",
     "Which details must every entry in the project's list of references carry, and does a kind of work need more of its own? Seven are required until you change them: authors, title, where published or held, year, identifier, keywords, and standing (what a search for later corrections or disputes found, or why none was made)."),
    ("REFERENCE_ADEQUACY", "evidence_and_reasoning/editorial_standards.md",
     "Which kind of reference is good enough to back which kind of claim? Pairs such as a peer-reviewed article for a specialist claim, or an archival document by its reference for what that document says."),
    ("DELIVERABLE", "DOCUMENT_GENRES.md",
     "What will the project publish? Its form, what its venue expects of a title, and what goes out with each released version besides the text, such as data, code, or transcriptions. It may wait until a write-up is opened."),
    ("SPELLING", "evidence_and_reasoning/editorial_standards.md",
     "In which language and spelling variant is the project's prose written: US English, UK English, or another language, for which no word list is checked? US English is checked from the start until you change it."),
    ("DASH_CONVENTION", "evidence_and_reasoning/editorial_standards.md",
     "How does the prose punctuate an aside inside a sentence, and a range such as 10 to 20? Asides take no em-dashes, spaced or unspaced em-dashes, or spaced en-dashes; ranges take an en-dash or the word to. The tools report every em-dash until you change the rule or turn the check off."),
    ("PAPER_PRONOUN", "evidence_and_reasoning/editorial_standards.md",
     "In the write-up, who performs its acts: we (even for one author), I, or the document itself (this article argues)? One choice, used throughout. It may wait until a write-up is opened."),
    ("VOICE", "evidence_and_reasoning/editorial_standards.md",
     "What style rules will drafts of the write-up be tested against? Rules read off your earlier writing, a house or journal style you name, or the example voice record in editorial_standards.md, kept as it stands. It may wait until a write-up is opened."),
    ("REPLY_HOOK", "MANIFESTO.md",
     "Every reply of the assistant ends in status lines saying whether to wait, answer, or walk away. Where and how does the program that runs the assistant check them after each reply: the wiring this repository carries, one you add, or none, with the form kept by hand?"),
    ("DISCLOSURE_RULE", "MANIFESTO.md",
     "Do your sources' terms, an agreement, or an ethics approval limit what the project may publish or share, such as a minimum count per table cell, the scope of consent, or an embargo? State the rule, or answer none beyond the general privacy rules."),
]
# The slots whose value depends on a write-up, and which setup may leave
# open by decision until one is opened (GETTING_STARTED.md section 3).
WAITS = ("DELIVERABLE", "PAPER_PRONOUN", "VOICE")

SLOT_NAMES = [s for s, _, _ in SLOTS]
OWNER = {name: own for name, own, _ in SLOTS}

# The guide's pages and GLOSSARY.md are ABOUT slots: they name the tokens
# as examples, and a substitution there would destroy the explanation;
# GETTING_STARTED.md section 3's grep for unfilled slots excludes the same
# four files.
# Program source names them in its own diagnostics, and the configuration
# names them in its comments, for the same reason, so only markdown is
# substituted.  {{LIKE_THIS}} is the generic illustration and is never a
# slot.
ABOUT_SLOTS = {"GETTING_STARTED.md", "HOW_IT_FITS_TOGETHER.md", "FORKING.md", "GLOSSARY.md"}
SUBSTITUTE_IN = (".md",)

# The machine halves, each with the table it belongs under, so that a key
# name shared by two tables is written under the right one.
MACHINE: list[tuple[str, str, str, bool]] = [
    # (answers key, TOML table, TOML key, is a list)
    ("spelling", "editorial", "spelling", False),
    ("dashes", "editorial", "dashes", False),
    ("mutations", "vocab", "mutations", True),
    ("parties", "parties", "names", True),
    ("registry_required", "registry", "required", True),
]
# What each machine half is, as ask() puts it.
MACHINE_PROMPTS = {
    "spelling": "the spelling variant the tools check: us, uk, or none",
    "dashes": "the dash rule the tools check: no-em-dash, spaced-em-dash, unspaced-em-dash, en-dash-asides, or none",
    "mutations": "the short names a check's Mutation: line may carry, comma-separated",
    "parties": "who besides you and the assistant may appear on a By: or Verified-by: line, "
               "comma-separated, or none, which records by decision that no one does",
    "registry_required": "the bullets every reference entry must carry, comma-separated",
}

FIELD_DEFAULTS = {
    "register": "Register", "kind": "Kind", "verdict": "Verdict", "plan": "Plan",
    "depends-on": "Depends-on", "backed-by": "Backed-by", "backs": "Backs",
    "verified-by": "Verified-by", "instrument": "Instrument", "frame": "Frame",
    "mutation": "Mutation", "robustness": "Robustness", "original": "Original",
    "prerequisites": "Prerequisites", "serves": "Serves", "status": "Status",
    "by": "By", "produced-from": "Produced-from",
}

# ------------------------------------------------- what a project does not get

LEAVE_BEHIND = ["example", ".review", ".git", ".privacy", "TODO.md",
                "tools/new_project.py"]

# The pointers to what was left behind: (path, exact text, what it becomes).
# A miss is reported rather than guessed at, because a pointer that moved
# is a change this procedure has not been taught.
# The front page README.md is always written over (step 10), so its
# pointers need no entry here.
POINTERS: list[tuple[str, str, str]] = [
    ("HOW_IT_FITS_TOGETHER.md",
     "- **Support** is the artifact templates, the indexes, and the worked\n  example, so that the right thing to do is also the easy thing.",
     "- **Support** is the artifact templates and the indexes, so that the\n  right thing to do is also the easy thing."),
    ("tools/artifacts.toml",
     '''[[artifact]]
kind = "work-list"
glob = "TODO.md"
genre = "current-state"
# The template's own open work, kept while the template is maintained and
# left behind at instantiation: a project's open work is its plans and its
# roadmap.
''', ""),
    ("tools/artifacts.toml",
     '''[[artifact]]
kind = "example"
glob = "example/**"
genre = "exempt"
header = "none"
# The worked example is a project of its own, instantiated from this
# template and checked by its own copy of the tools from inside example/;
# the template's tools do not read it.

''', ""),
]
# A row of an index, matched by the path it names rather than by its wording.
POINTER_LINES = [("tools/README.md", "[new_project.py](new_project.py)"),
                 ("governance/README.md", "[example/](../example/)"),
                 ("governance/README.md", "`tools/new_project.py`")]

# GETTING_STARTED.md's account of the tool runs from the first marker
# through the second; a project gets a dateless pointer to its setup note
# in its place (step 10), so everything said there about running the tool,
# and nothing else, is template-only.
SETUP_START = "**Steps 1 to 3 have a tool.**"
SETUP_END = "§4 onward is yours."
SETUP_POINTER = """**The mechanical part of steps 1 to 3 was done for this project** by
the template's instantiation tool, which does not travel with a project.
Its working note under `evidence_and_reasoning/notes/`, dated the day of
the run, records what it did and what it left to you. Two steps of §1
belong to every clone, not once to the project: installing the hooks, and
arming the privacy scan. Sections 1 to 3 are kept below as the account of
how a project is set up, and of what to change if one of those decisions
turns out to be wrong; §4 says which rounds come first."""

# The values the tools accept for the two editorial machine halves.
SPELLINGS = ("us", "uk", "none", "")
DASHES = ("no-em-dash", "spaced-em-dash", "unspaced-em-dash", "en-dash-asides", "none", "")

BUILD_LENS = re.compile(r"^> \*\*Build lens\.\*\*.*$(?:\n^>.*$)*\n?", re.M)
LENS_SECTIONS = [("## Two lenses", "## 1. Role and identity"),
                 ("## Where the two lenses differ", "## Slots")]
SLOT_ROW = re.compile(r"^\|\s*`\{\{([A-Z_]+)\}\}`\s*\|")
STAMP = re.compile(r"^(\*Created .+?; updated )(.+?)(\.\*)$", re.M)
TOML_STAMP = re.compile(r"^(# Created .+?; updated )(.+?)(\.)$", re.M)
PY_STAMP = re.compile(r"^(Created .+?; updated )(.+?)(\.)$", re.M)
STAMPS = {".md": STAMP, ".toml": TOML_STAMP, ".py": PY_STAMP}
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]


def today_day() -> str:
    """Today, read from the clock, in the header's `D Month YYYY` form."""
    d = datetime.date.today()
    return f"{d.day} {MONTH_NAMES[d.month - 1]} {d.year}"


# ------------------------------------------------------------------ helpers


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def walk(root: Path, suffixes: tuple[str, ...] | None = None) -> list[Path]:
    return [p for p in sorted(root.rglob("*"))
            if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
            and (suffixes is None or p.suffix in suffixes)]


def toml_str(value: str) -> str:
    """A TOML basic string: the escapes the format requires, and no others."""
    out = value.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + out.replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r") + '"'


def toml_list(items: list[str]) -> str:
    return "[" + ", ".join(toml_str(i) for i in items) + "]"


class Refused(Exception):
    """The answers or the target cannot be used; nothing has been written."""


# --------------------------------------------------------- checking the answers


def slot_problem(name: str, val: object) -> str:
    """Why a slot value cannot be used, or "" where it can; ask() puts the
    question again on a problem, and check_answers refuses."""
    if not isinstance(val, str):
        return f"[slots] {name} must be a string, not {type(val).__name__}"
    if "|" in val:
        return f"[slots] {name} contains a pipe, which would break the Slots table row"
    if "\n" in val:
        return f"[slots] {name} contains a line break; a slot value is one line"
    if re.match(r"\s*open by decision", val, re.I):
        return (f"[slots] {name}: a slot left open by decision is not given a value; leave it blank, and write "
                "the marker in its owner row itself (GETTING_STARTED.md section 3)")
    return ""


def machine_value(key: str, v: object) -> tuple[object, str]:
    """A machine half normalized (case and space), and why it cannot be
    used, or "" where it can."""
    is_list = next(x[3] for x in MACHINE if x[0] == key)
    if is_list:
        if not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
            return v, f'[machine] {key} must be a list of strings, as in {key} = ["one", "two"]'
        v = [x.strip() for x in v if x.strip()]
        if key == "parties":
            v = ["none" if x.lower() == "none" else x for x in v]
            if "none" in v and len(v) > 1:
                return v, ('[machine] parties: "none" stands alone; it records by decision that no one beyond '
                           "the researcher and the assistant appears")
        return v, ""
    if not isinstance(v, str):
        return v, f"[machine] {key} must be a string"
    v = v.strip().lower()
    allowed = SPELLINGS if key == "spelling" else DASHES if key == "dashes" else None
    if allowed is not None and v not in allowed:
        return v, f"[machine] {key} must be one of: " + ", ".join(repr(a) for a in allowed)
    return v, ""


def check_answers(answers: dict) -> tuple[dict, list[str]]:
    """Everything this program will act on, checked for shape before it
    writes anything.  A value that would corrupt a markdown table or a TOML
    file, or that the tools would not read, is refused here rather than
    written and found later."""
    notes: list[str] = []
    slots = answers.get("slots") or {}
    if not isinstance(slots, dict):
        raise Refused('[slots] must be a table of NAME = "value"')
    clean: dict[str, str] = {}
    for name, val in slots.items():
        if name not in SLOT_NAMES:
            notes.append(f"[slots] {name} is not a slot of this template; ignored")
            continue
        if isinstance(val, str) and not val.strip():
            continue
        problem = slot_problem(name, val)
        if problem:
            raise Refused(problem)
        clean[name] = val.strip()
        if clean[name].endswith(".") and not clean[name].endswith(".."):
            clean[name] = clean[name][:-1].rstrip()
            notes.append(f"[slots] {name}: its closing period dropped; the sentence it lands in supplies its own")

    if not isinstance(answers.get("machine") or {}, dict):
        raise Refused("[machine] must be a table")
    machine = dict(answers.get("machine") or {})
    for key, _, _, _ in MACHINE:
        if key not in machine or machine[key] is None:
            continue
        machine[key], problem = machine_value(key, machine[key])
        if problem:
            raise Refused(problem)

    rename = answers.get("rename") or {}
    if not isinstance(rename, dict):
        raise Refused('[rename] must be a table of role = "Name"')
    for role, name in rename.items():
        if role not in FIELD_DEFAULTS:
            raise Refused(f"[rename] {role} is not a header-field role; the roles are "
                          + ", ".join(sorted(FIELD_DEFAULTS)))
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*", name or ""):
            raise Refused(f"[rename] {role} must be a field name: letters, digits and hyphens")

    proj = answers.get("project") or {}
    if not isinstance(proj, dict):
        raise Refused("[project] must be a table")
    return {"slots": clean, "machine": machine, "rename": rename, "project": proj}, notes


def target_problem(src: Path, dst: Path) -> str:
    """Why the new tree cannot be made at dst, or "" where it can; checked
    before any question is put, and again before anything is written."""
    src_r, dst_r = src.resolve(), dst.resolve()
    if src_r == dst_r or src_r in dst_r.parents or dst_r in src_r.parents:
        return (f"{dst_r.name} is inside the template, or the template is inside it; "
                "give a directory outside this tree")
    if dst.exists() and (not dst.is_dir() or any(dst.iterdir())):
        return f"{dst_r.name} exists and is not an empty directory"
    if shutil.which("git") is None:
        return "git is not installed; a project's version history is part of its record (MANIFESTO.md section 12)"
    return ""


# ------------------------------------------------------------------ the steps


def tracked(src: Path) -> list[str] | None:
    """The paths the git repository whose top is `src` tracks, or None
    where `src` is not the top of a git repository of its own (an unpacked
    archive, or a folder inside another repository)."""
    try:
        top = subprocess.run(["git", "-C", str(src), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if top.returncode != 0 or Path(top.stdout.strip()).resolve() != src.resolve():
            return None
        out = subprocess.run(["git", "-C", str(src), "ls-files", "-z"],
                             capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return [p for p in out.decode("utf-8", "surrogateescape").split("\0") if p]


def copy_tree(src: Path, dst: Path) -> tuple[str, list[str]]:
    """Step 1: the files git tracks, without the template's own
    construction.  Returns how the tree was copied, said so that it
    completes "It ...", and the tracked paths it could not copy."""
    top = {n for n in LEAVE_BEHIND if "/" not in n}
    nested = {n for n in LEAVE_BEHIND if "/" in n}
    paths = tracked(src)
    if paths is None:
        def ignore(directory: str, names: list[str]) -> set[str]:
            out = {n for n in names if n in top and Path(directory) == src}
            out |= {n for n in names if n in ("__pycache__", ".pytest_cache")}
            out |= {n for n in names if n.startswith(".run_ledger.json")}
            return out

        shutil.copytree(src, dst, ignore=ignore, symlinks=True)
        for rel in nested:
            p = dst / rel
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                shutil.rmtree(p)
        return ("copied every file in the template's folder, which is not a git repository of its own, "
                "except what it leaves behind and the caches"), []
    dst.mkdir(parents=True, exist_ok=True)
    absent, n = [], 0
    for rel in paths:
        if rel.split("/", 1)[0] in top or rel in nested:
            continue
        a, b = src / rel, dst / rel
        if a.is_symlink():
            b.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(os.readlink(a), b)
        elif a.is_file():
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(a, b)
        else:
            absent.append(rel)
            continue
        n += 1
    return f"copied the {n} tracked files a project keeps", absent


def remove_pointers(root: Path) -> list[str]:
    """Step 2: the references to what step 1 left behind."""
    missed = []
    for rel, old, new in POINTERS:
        p = root / rel
        if not p.exists():
            missed.append(f"{rel} (no such file)")
            continue
        s = read(p)
        if old not in s:
            missed.append(f"{rel}: {old.strip().splitlines()[0][:60]}")
            continue
        p.write_text(s.replace(old, new, 1), encoding="utf-8")
    for rel, needle in POINTER_LINES:
        p = root / rel
        if not p.exists():
            missed.append(f"{rel} (no such file)")
            continue
        lines = read(p).split("\n")
        keep = [ln for ln in lines if needle not in ln]
        if len(keep) == len(lines):
            missed.append(f"{rel}: a row naming {needle}")
        else:
            p.write_text("\n".join(keep), encoding="utf-8")
    return missed


def strip_build_lens(root: Path) -> int:
    """Step 3: every build-lens blockquote, and the manifesto's lens sections."""
    n = 0
    for p in walk(root, (".md",)):
        s = read(p)
        out, k = BUILD_LENS.subn("", s)
        if k:
            p.write_text(re.sub(r"\n{3,}", "\n\n", out), encoding="utf-8")
            n += k
    m = root / "MANIFESTO.md"
    s = read(m)
    for start, end in LENS_SECTIONS:
        i, j = s.find(start), s.find(end)
        if i != -1 and j > i:
            s = s[:i] + s[j:]
            n += 1
    m.write_text(re.sub(r"\n---\n\n(?=## 1\. Role)", "\n", s), encoding="utf-8")
    return n


def fill_slots(root: Path, values: dict[str, str]) -> list[tuple[str, int, str]]:
    """Step 5.  A Slots row keeps its token in every file: in the owner's the
    value is written after it, and elsewhere the row points at the owner and
    is left alone.  Markdown prose is substituted; a configuration comment
    keeps the token as the slot's name.  Returns the lines a long value may
    have broken, wherever they are."""
    long_lines: list[tuple[str, int, str]] = []
    for p in walk(root, SUBSTITUTE_IN):
        if p.name in ABOUT_SLOTS:
            continue
        s = read(p)
        if "{{" not in s:
            continue
        rel = str(p.relative_to(root))
        out, changed = [], False
        for i, line in enumerate(s.split("\n"), 1):
            row = SLOT_ROW.match(line)
            if row and row.group(1) in SLOT_NAMES:
                name = row.group(1)
                if OWNER.get(name) == rel and name in values:
                    out.append(line.replace(f"`{{{{{name}}}}}`", f"`{{{{{name}}}}}`: {values[name]}", 1))
                    changed = True
                else:
                    out.append(line)
                continue
            new, longest, own = line, 0, False
            for name, val in values.items():
                if "{{" + name + "}}" in new:
                    longest = max(longest, len(val))
                    own = own or OWNER.get(name) == rel
                    new = new.replace("{{" + name + "}}", val)
            if new != line:
                changed = True
                # A long value belongs in a Slots table cell, and in the
                # defining sentence of the file that owns the slot.
                # Substituted into a sentence anywhere else it may not read,
                # and that sentence wants a short handle instead
                # (GETTING_STARTED.md section 3).
                if longest > 60 and not line.lstrip().startswith("|"):
                    long_lines.append((rel, i, ("the value's own definition; read it once: " if own else "")
                                       + new.strip()[:100]))
            out.append(new)
        if changed:
            p.write_text("\n".join(out), encoding="utf-8")
    return long_lines


def set_key(text: str, table: str, key: str, value: str) -> tuple[str, bool]:
    """One `key = value` under one TOML table, replaced in place.  The table
    matters: `names` is a key of both [fields] and [parties]."""
    start = text.find(f"\n[{table}]\n")
    if start == -1:
        return text, False
    rest = text[start + 1:]
    m = re.search(r"^\[", rest[1:], re.M)
    end = m.start() + 1 if m else len(rest)
    body, tail = rest[:end], rest[end:]
    new_body, n = re.subn(rf"^{re.escape(key)} = (?:.|\n)*?(?=^[A-Za-z_]+ = |^#|^\[|\Z)",
                          lambda _: f"{key} = {value}\n", body, count=1, flags=re.M)
    return (text[:start + 1] + new_body + tail, True) if n else (text, False)


def write_machine_halves(root: Path, machine: dict, rename: dict) -> list[str]:
    """Steps 6 and 7, in the configuration."""
    p = root / "tools" / "artifacts.toml"
    s = read(p)
    done = []
    for key, table, tkey, is_list in MACHINE:
        if key not in machine or machine[key] is None:
            continue
        val = toml_list(machine[key]) if is_list else toml_str(machine[key])
        s, ok = set_key(s, table, tkey, val)
        what = f"{len(machine[key])} entry(s)" if is_list else repr(machine[key])
        done.append(f"[{table}] {tkey} = {what}" if ok else f"[{table}] {tkey} NOT SET, write it by hand")
    for role, name in (rename or {}).items():
        s, ok = set_key(s, "fields.roles", role, toml_str(name))
        done.append(f"{role} -> {name}" if ok else f"{role} NOT RENAMED, write it by hand")
    p.write_text(s, encoding="utf-8")
    return done


def rename_fields(root: Path, rename: dict) -> tuple[int, list[str]]:
    """Step 7, in the prose: the field at the head of a form, indented or
    not, and every mention of it as `Name:` in a rulebook or a legend."""
    pairs = [(FIELD_DEFAULTS[r], n) for r, n in (rename or {}).items() if FIELD_DEFAULTS.get(r) != n]
    if not pairs:
        return 0, []
    n_files, left = 0, []
    for p in walk(root, (".md", ".py")):
        if p.name in ABOUT_SLOTS:
            continue
        s = read(p)
        out = s
        for old, new in pairs:
            out = re.sub(rf"(?<![\w-]){re.escape(old)}:", f"{new}:", out)
        if out != s:
            p.write_text(out, encoding="utf-8")
            n_files += 1
    # Where the old word is still used without its colon, the sentence is
    # prose about the field and is the researcher's to reword.
    for old, _ in pairs:
        for p in walk(root, (".md",)):
            if p.name in ABOUT_SLOTS:
                continue
            for i, line in enumerate(read(p).split("\n"), 1):
                if re.search(rf"(?<![\w-]){re.escape(old)}(?![\w-]):?", line) and f"{old}:" not in line:
                    left.append(f"{p.relative_to(root)}:{i} still says {old!r}")
                    break
    return n_files, left


# What the spelling check does not read, and so what the conversion leaves:
# comments, fenced code, backtick spans, double-quoted text on one line,
# and block quotes (lint_docs.strip_unread and blank_quoted).
UNREAD = re.compile(r"<!--.*?-->|```.*?```|`[^`]+`|\"[^\"\n]+\"|\u201c[^\u201d\n]+\u201d|^>[^\n]*$", re.S | re.M)


def convert_spelling(root: Path, want: str, shipped: str, words: dict) -> int:
    """Step 4.  The shipped prose is written in one variant; a project that
    picks another would inherit a failing gate on prose it did not write.
    The two starter lists are parallel, so the conversion is exact for the
    words the check knows, which are the only ones it reports; what the
    check does not read keeps its spelling, so a quotation or an example
    of the other variant survives."""
    if not want or want == shipped or want not in words or shipped not in words:
        return 0
    pairs = [(a, b) for a, b in zip(words[want], words[shipped]) if a != b]

    def convert(text: str) -> str:
        for wrong, right in pairs:
            text = re.sub(rf"(?<![\w-]){re.escape(wrong)}(?![\w-])", lambda _, r=right: r, text)
            cap, cap_r = wrong[:1].upper() + wrong[1:], right[:1].upper() + right[1:]
            text = re.sub(rf"(?<![\w-]){re.escape(cap)}(?![\w-])", lambda _, r=cap_r: r, text)
        return text

    n = 0
    for p in walk(root, (".md",)):
        s = read(p)
        out, last = [], 0
        for m in UNREAD.finditer(s):
            out.append(convert(s[last:m.start()]))
            out.append(m.group(0))
            last = m.end()
        out.append(convert(s[last:]))
        new = "".join(out)
        if new != s:
            p.write_text(new, encoding="utf-8")
            n += 1
    return n


# The texts of LICENSE.md the license step edits, each matched exactly:
# (when it applies, the text, what it becomes).  A miss is reported rather
# than guessed at, as for the pointers.
LICENSE_CITED = "Recommended citation for the template:"
LICENSE_KEEP = """**Keep the template's citation**, and say that the project's material is
adapted from it. The written material is under CC BY 4.0, which requires
that credit be given to the original and that changes be indicated; a
project that replaces the citation rather than adding to it is out of
compliance with the license it inherits. One line is enough:"""
LICENSE_TODO = """## In a project built from the template

Add the project's own copyright holder to `LICENSE-CODE`, beside the
template's, and add the project's own recommended citation above.
"""
# The clause both grants of LICENSE.md carry, word for word, and the front
# page repeats (the self-test compares them).
OWN_TERMS = ("except the held sources under `source_documents/`, the imports under `inherited/`, "
             "and what the project quotes or derives from them, which keep their own terms as far "
             "as those terms reach")


def write_licenses(root: Path, holder: str, citation: str, year: str) -> tuple[list[str], list[str], bool]:
    """Step 8: the project's copyright holder and citation added, each only
    where it is given, and the template's kept.  The citation's edits of
    LICENSE.md stand or fall together: where the line introducing the
    template's citation is not found, none of them is made.  Returns what
    was done, said so that each completes "It ...", each text it could not
    find, named in words, and whether the citation was added."""
    done, missed, cited, held = [], [], False, False
    if holder:
        code = root / "LICENSE-CODE"
        if not code.exists():
            missed.append("LICENSE-CODE itself")
        else:
            c, k = re.subn(r"^(Copyright \(c\) .*)$", lambda m: m.group(1) + f"\nCopyright (c) {year} {holder}",
                           read(code), count=1, flags=re.M)
            if k:
                code.write_text(c, encoding="utf-8")
                held = True
                done.append(f"added this project's copyright holder to LICENSE-CODE, dated {year}")
            else:
                missed.append("the copyright line of LICENSE-CODE")
    lic = root / "LICENSE.md"
    if (citation or holder) and not lic.exists():
        missed.append("LICENSE.md itself")
    elif citation or holder:
        s = read(lic)
        if citation:
            if LICENSE_CITED in s:
                s = s.replace(LICENSE_CITED,
                              f"Recommended citation for this project:\n\n    {citation}\n\n"
                              f"This project's written material is adapted from the template named\n"
                              f"below, under CC BY 4.0; it has been changed for this project.\n\n"
                              f"Recommended citation for the template:", 1)
                cited = True
                # The adaptation is stated once, by the sentence just written:
                # the instruction to state it, and its sample line, give way.
                kept = re.search(re.escape(LICENSE_KEEP) + r"\n\n((?: {4}[^\n]*\n)+)", s)
                if kept:
                    s = s[:kept.start()] + ("The template's citation above is kept, as CC BY 4.0 requires, and the\n"
                                            "sentence above it indicates that the material was changed.\n") + s[kept.end():]
                else:
                    missed.append("the paragraph of LICENSE.md asking to keep the template's citation")
                done.append("added this project's citation to LICENSE.md, beside the template's")
            else:
                missed.append("the line of LICENSE.md that introduces the template's citation")
        # What is still owed, from what was done.
        owed = [x for x, still in (("Add the project's own copyright holder to `LICENSE-CODE`, beside the\ntemplate's.", not held),
                                   ("Add the project's own recommended citation above.", not cited)) if still]
        new_todo = ("## This project and the template it came from\n" if not owed
                    else "## In a project built from the template\n\n" + "\n".join(owed) + "\n")
        if LICENSE_TODO in s:
            s = s.replace(LICENSE_TODO, new_todo, 1)
        else:
            missed.append("the section of LICENSE.md saying what a project adds to the licenses")
        lic.write_text(s, encoding="utf-8")
    return done, missed, cited


PROJECT_README = """# {title}

*Created {date}; updated {date}.*

<!-- One paragraph: the question this project asks, and what would count
     as answering it. The long form is evidence_and_reasoning/research_statement.md. -->

## Where to start

| To see | Read |
|---|---|
| where the project stands | [CURRENT_STATE.md](CURRENT_STATE.md) |
| what the record has established | [FINDINGS.md](FINDINGS.md) |
| the question and the thesis | [evidence_and_reasoning/research_statement.md](evidence_and_reasoning/research_statement.md), [problem_statement.md](evidence_and_reasoning/problem_statement.md) |
| what is open, and what each plan settles | [evidence_and_reasoning/research_plans/ROADMAP.md](evidence_and_reasoning/research_plans/ROADMAP.md) |
| the record itself | [evidence_and_reasoning/](evidence_and_reasoning/) |
| what was asked, and when | [prompt_logs/](prompt_logs/) |

## How this project works

It is built from a methodology template, whose rules travel with it:
[MANIFESTO.md](MANIFESTO.md) for who does what and what the record is,
[HOW_IT_FITS_TOGETHER.md](HOW_IT_FITS_TOGETHER.md) for the system as one
thing and the prompts worth making, [GLOSSARY.md](GLOSSARY.md) for the
words it uses in its own sense, [GETTING_STARTED.md](GETTING_STARTED.md)
for how this project was set up. A session reads
[ONBOARDING.md](ONBOARDING.md) before it works. This project's written
material is adapted from that template under CC BY 4.0, which
[LICENSE.md](LICENSE.md) names.

Before handing work back, and on every commit:

```bash
python3 tools/check_round.py
```

## The files at the root

{root_files}

## Licensing

{licensing}
"""

ROOT_FILE_NOTES = {
    "MANIFESTO.md": "the operating rules: who does what, and what the record is",
    "DOCUMENT_GENRES.md": "the three genres of artifact and what the checker verifies",
    "CHECK_METHODOLOGY.md": "trust levels, claim kinds, and the shape of a check",
    "PRECEDENCE.md": "which statement governs when two disagree",
    "ONTOLOGY.md": "the predicates the tools read, and their surface syntax",
    "GLOSSARY.md": "the method's own words, and what each will be mistaken for",
    "GETTING_STARTED.md": "how this project was set up, and which rounds come first",
    "HOW_IT_FITS_TOGETHER.md": "the system as one thing, and the prompts worth making",
    "FORKING.md": "how to change or remove a mechanism, legibly",
    "ONBOARDING.md": "what every session reads before it works",
    "CURRENT_STATE.md": "where the project stands",
    "FINDINGS.md": "what the record has established",
    "VISION.md": "the statement of intent the rulebooks cite",
    "LICENSE.md": "the license for written material, and the citations",
    "LICENSE-CODE": "the license for code",
}


def write_project_readme(root: Path, title: str, date: str, cited: bool = False) -> None:
    """Step 10.  Always written, so that the template's front page, with its
    links to what was left behind, never reaches a project; the title is
    {{PROJECT_TITLE}} where none was given.  The root table is generated
    from what is there, so that it is complete for the index check
    (DOCUMENT_GENRES.md item 8)."""
    rows = ["| File | What it is |", "|---|---|"]
    for p in sorted(root.iterdir()):
        if p.name == "README.md" or p.name.startswith("."):
            continue
        if p.is_file():
            rows.append(f"| [{p.name}]({p.name}) | {ROOT_FILE_NOTES.get(p.name, 'see the file')} |")
    folders = sorted(p.name for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))
    rows.append("| " + ", ".join(f"[{d}/]({d}/)" for d in folders)
                + " | the folders, each with its own README |")
    (root / "README.md").write_text(
        PROJECT_README.format(title=title, date=date, root_files="\n".join(rows), licensing=textwrap.fill(
            "Written material is under Creative Commons Attribution 4.0 International and code under the MIT "
            f"License, {OWN_TERMS}. [LICENSE.md](LICENSE.md) and [LICENSE-CODE](LICENSE-CODE) carry both "
            "licenses and the citation of the template this project is adapted from"
            + (", with this project's beside it." if cited else "."), 74, break_on_hyphens=False)),
        encoding="utf-8")


def series(xs: list[str]) -> str:
    return xs[0] if len(xs) == 1 else "; ".join(xs[:-1]) + "; and " + xs[-1]


def paragraph(text: str) -> str:
    """A paragraph wrapped so that no line opens a markdown block."""
    lines = textwrap.fill(text, 74, break_on_hyphens=False, break_long_words=False).split("\n")
    out: list[str] = []
    for line in lines:
        if out and re.match(r"(#|>|[-*+] |\d+[.)] )", line):
            word, _, rest = line.partition(" ")
            out[-1] += " " + word
            line = rest
        if line:
            out.append(line)
    return "\n".join(out)


SETUP_NOTE = """# Setup of this project: {day}

*Created {day}; updated {day}.*

**Working note.** Nothing here may be cited as a result.

## What was asked

{asked}

## What was found

{found}

{left}

## What follows

{follows}
"""


def write_setup_note(root: Path, day: str, iso: str, did: list[str], left: list[str]) -> tuple[str, bool]:
    """Step 10: the dated working note recording what the run did and what
    it left to the researcher, a record of the day frozen on writing
    (evidence_and_reasoning/notes/README.md), indexed in its folder.
    Returns the note's path and whether its index row was written."""
    rel = f"evidence_and_reasoning/notes/{iso}_setup.md"
    (root / rel).parent.mkdir(parents=True, exist_ok=True)
    (root / rel).write_text(SETUP_NOTE.format(
        day=day,
        asked=paragraph(f"The template's instantiation tool, which does not travel with a project, made "
                        f"this project from the template on {day}, with the answers it was given."),
        found=paragraph("It " + series(did) + "."),
        left=paragraph("It left to you " + series(left) + "."),
        follows=paragraph("The rounds `GETTING_STARTED.md` §4 lists, in its order.")), encoding="utf-8")
    index = root / "evidence_and_reasoning" / "notes" / "README.md"
    row = f"| [{iso}_setup.md]({iso}_setup.md) | working note: the run that made this project from the template |"
    if not index.exists():
        return rel, False
    s = read(index)
    placeholder = re.search(r"^\| <!-- \[YYYY-MM-DD_short_name\.md\].*$", s, re.M)
    if placeholder:
        index.write_text(s[:placeholder.start()] + row + s[placeholder.end():], encoding="utf-8")
        return rel, True
    head = re.search(r"^\| File \| What \|\n\|---\|---\|\n", s, re.M)
    if head:
        index.write_text(s[:head.end()] + row + "\n" + s[head.end():], encoding="utf-8")
        return rel, True
    return rel, False


def write_setup_pointer(root: Path) -> bool:
    """Step 10: GETTING_STARTED.md's account of the tool, from SETUP_START
    through SETUP_END, gives way to SETUP_POINTER; False where either
    marker is missing."""
    p = root / "GETTING_STARTED.md"
    s = read(p) if p.exists() else ""
    i = s.find(SETUP_START)
    j = s.find(SETUP_END, i + 1) if i != -1 else -1
    if i == -1 or j == -1:
        return False
    p.write_text(s[:i] + SETUP_POINTER + s[j + len(SETUP_END):], encoding="utf-8")
    return True


def restamp(root: Path, day: str, src: Path) -> int:
    """Step 10.  A file this procedure changed is no longer the template's: its
    updated date becomes `day`, the day of the run.  A file it did not
    change, compared with the template's copy at `src`, keeps the
    template's dates (DOCUMENT_GENRES.md section 3)."""
    n = 0
    for p in walk(root, tuple(STAMPS)):
        s = read(p)
        orig = src / p.relative_to(root)
        if orig.is_file() and read(orig) == s:
            continue
        m = STAMPS[p.suffix].search(s)
        # A template's stamp is a placeholder a researcher fills when they
        # copy it; dating half of it would seed every artifact with a
        # half-filled header.
        if not m or "D Month YYYY" in m.group(0):
            continue
        out = s[:m.start(2)] + day + s[m.end(2):]
        if out != s:
            p.write_text(out, encoding="utf-8")
            n += 1
    return n


# ------------------------------------------------------------------ answers

ANSWERS_TEMPLATE = '''# Answers for tools/new_project.py.
#
# Every slot the project fills, the values the tools read, the header
# fields to rename, and the two license lines.  Keep this file outside both
# the template and the new project.  Above each slot is the question
# GETTING_STARTED.md section 3 asks in plain words, and the same section
# gives a filled example of each from five different fields.  A slot left
# blank stays unfilled.  The three that may wait for a write-up
# (DELIVERABLE, PAPER_PRONOUN, VOICE) are left blank here when they wait,
# and the marker is written in their owner rows afterwards.  An answer is a
# phrase that completes its owner's sentence, as the guide's examples are,
# with no closing period.

[project]
holder = ""          # the copyright holder for this project's code
citation = ""        # one line: author, title, year, and where it lives
date = ""            # the project's start date, "D Month YYYY": its year dates the copyright; files are stamped with the day the procedure runs

[slots]
{slots}
[machine]
# The half the tools read.  A value here is in force; the prose half alone
# is not.  spelling, dashes and registry_required ship FILLED with the
# template's answer and are enforced until changed; mutations and parties
# ship empty, and an empty one skips its check and says so.  parties =
# ["none"] records by decision that no one beyond the researcher and the
# assistant appears, and the roster check then runs.
spelling = "us"                 # "us" | "uk" | "none" | ""
dashes = "no-em-dash"           # no-em-dash | spaced-em-dash | unspaced-em-dash | en-dash-asides | none | ""
mutations = []                  # the names a Mutation: line may carry, as a header writes them
parties = []                    # the roster beyond the researcher and the assistant, or ["none"]
registry_required = ["Authors", "Title", "Where", "Year", "Identifier", "Keywords", "Standing"]
# {{{{DELIVERABLE}}}} has a machine half too, the [publication] table, which
# gates a build and a bibliography.  It ships disabled and this procedure
# leaves it so: a project that builds its deliverable fills it in by hand,
# as paper/README.md says, once it knows what the build command is.
# {{{{REFERENCE_FIELDS}}}} has a second half, [registry.by_kind], for a
# registry holding several kinds of work; it ships empty and is filled the
# same way.

[rename]
# A header field whose name this project's discipline has taken
# (GLOSSARY.md, "Renaming a word this template uses").  Cheap now, dear
# later.  Leave empty to keep the shipped names.  The roles are: register,
# kind, verdict, plan, depends-on, backed-by, backs, verified-by,
# instrument, frame, mutation, robustness, original, prerequisites,
# serves, status, by, produced-from.
# register = "Trust"
'''


def answers_template() -> str:
    """The --template output: each slot's question as comment lines above its key."""
    return ANSWERS_TEMPLATE.format(slots="".join(
        textwrap.fill(q, 72, initial_indent="# ", subsequent_indent="# ", break_on_hyphens=False)
        + f'\n{n} = ""\n\n' for n, _, q in SLOTS))


def ask(values: dict) -> dict:
    """Every value, one at a time, in the plain words of GETTING_STARTED.md
    section 3; the three slots that may wait for a write-up come last."""
    slots = dict(values.get("slots") or {})
    print("\nThe sixteen slots, one at a time. Enter blank to keep what is shown.\n")
    order = [x for x in SLOTS if x[0] not in WAITS] + [x for x in SLOTS if x[0] in WAITS]
    for k, (name, own, question) in enumerate(order):
        if k == len(SLOTS) - len(WAITS):
            print("  The last three may wait until a write-up is opened. A blank leaves the slot\n"
                  "  unfilled; the marker for a slot open by decision is written afterwards, in\n"
                  "  its owner row itself (GETTING_STARTED.md section 3).\n")
        cur = slots.get(name, "")
        print(textwrap.fill(question, 76, initial_indent="  ", subsequent_indent="  ", break_on_hyphens=False))
        print(f"    ({{{{{name}}}}}, written into {own})")
        while True:
            got = input(f"    [{cur[:50]}] > " if cur else "    > ").strip()
            problem = slot_problem(name, got) if got else ""
            if not problem:
                break
            print(f"    {problem}; again:")
        if got:
            slots[name] = got
        print()
    values["slots"] = slots

    machine = dict(values.get("machine") or {})
    print("\nThe half the tools read. A prose value alone is not in force.\n")
    for key, table, tkey, is_list in MACHINE:
        cur = machine.get(key)
        shown = ", ".join(cur) if isinstance(cur, list) else (cur or "")
        print(f"  [{table}] {tkey}: {MACHINE_PROMPTS[key]}")
        while True:
            got = input(f"    [{shown[:60]}] > ").strip()
            if not got:
                break
            value, problem = machine_value(key, [x.strip() for x in got.split(",") if x.strip()] if is_list else got)
            if not problem:
                machine[key] = value
                break
            print(f"    {problem}; again:")
    values["machine"] = machine

    rename = dict(values.get("rename") or {})
    print("\nRenaming a header field your discipline has taken (GLOSSARY.md).")
    print("  Blank keeps the shipped names; otherwise role=Name, comma-separated.")
    while True:
        got = input(f"    [{', '.join(f'{k}={v}' for k, v in rename.items())}] > ").strip()
        parts = [p for p in got.split(",") if p.strip()] if got else []
        pairs = [p.split("=", 1) for p in parts if "=" in p]
        bad = [p.strip() for p in parts if "=" not in p] + [
            r.strip() for r, n in pairs if r.strip() not in FIELD_DEFAULTS
            or not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*", n.strip())]
        if not bad:
            break
        print(f"    not a role=Name pair this program can use: {', '.join(bad)}; again:")
    for role, name in pairs:
        rename[role.strip()] = name.strip()
    values["rename"] = rename

    proj = dict(values.get("project") or {})
    print()
    for key, prompt in (("holder", "copyright holder"),
                        ("citation", "one-line citation for this project"),
                        ("date", "start date, D Month YYYY")):
        got = input(f"  {prompt} [{proj.get(key, '')}] > ").strip()
        if got:
            proj[key] = got
    values["project"] = proj
    return values


# ------------------------------------------------------------------ the run


# What to read next in the new project; a constant, so the self-test can read it.
NEXT = """
Next, in the new project:

  1. its setup note, under evidence_and_reasoning/notes/, says what this
     run did and what it left to you;
  2. GETTING_STARTED.md section 1 lists the setup decisions that are not
     slots, settled in setup; the privacy scan's list comes first, before
     the first commit;
  3. its section 4 says which rounds come first, and in what order.
"""


def instantiate(src: Path, dst: Path, answers: dict, quiet: bool = False) -> int:
    p = (lambda *a, **k: None) if quiet else print
    try:
        clean, notes = check_answers(answers)
    except Refused as e:
        print(f"new_project: {e}", file=sys.stderr)
        return 2
    slots, machine, rename, proj = clean["slots"], clean["machine"], clean["rename"], clean["project"]
    holder = str(proj.get("holder") or "").strip()
    citation = str(proj.get("citation") or "").strip()
    date = str(proj.get("date") or "").strip()
    found = re.search(r"\b(\d{4})\b", date)
    year = found.group(1) if found else str(datetime.date.today().year)
    day, iso = today_day(), datetime.date.today().isoformat()

    problem = target_problem(src, dst)
    if problem:
        print(f"new_project: {problem}", file=sys.stderr)
        return 2

    try:
        template_cfg = tomllib.loads(read(src / "tools" / "artifacts.toml"))
    except (OSError, tomllib.TOMLDecodeError) as e:
        print(f"new_project: the template's tools/artifacts.toml cannot be read: {e}", file=sys.stderr)
        return 2

    p(f"\nInstantiating {src.resolve().name} into {dst.resolve().name}\n")
    for n in notes:
        p(f"     {n}")
    if dst.exists():
        dst.rmdir()
    # What the run did and what it left, each said so that it completes
    # "It ..." and "It left to you ..." in the setup note of step 10.
    did: list[str] = []
    left: list[str] = []
    try:
        how, absent = copy_tree(src, dst)
        init = subprocess.run(["git", "init", "-q"], cwd=dst, capture_output=True, text=True)
        p(f"  1. {how}, leaving behind: " + ", ".join(LEAVE_BEHIND)
          + ("; git initialized" if init.returncode == 0 else "; git init FAILED, run it yourself"))
        for a in absent:
            p(f"     TRACKED BUT NOT IN THE WORKING TREE, not copied: {a}")
        did.append(how)
        if "not a git repository" in how:
            p("     look for anything of yours that came along: an answers file, a virtual environment,"
              " local harness settings")
            left.append("a look for anything of yours that came along with the whole folder: an answers file, "
                        "a virtual environment, local harness settings")
        if absent:
            left.append("the tracked files it could not copy, " + ", ".join(absent))
        if init.returncode != 0:
            left.append("making the new tree a git repository (git init)")

        missed = remove_pointers(dst)
        total = len(POINTERS) + len(POINTER_LINES)
        p(f"  2. removed {total - len(missed)} of {total} pointers to what was left behind")
        for m in missed:
            p(f"     NOT FOUND, remove by hand: {m}")
        did.append("left behind the template's own construction, and removed the pointers to it"
                   + (" that it found" if missed else ""))
        if missed:
            left.append("the pointers it could not find, in "
                        + ", ".join(sorted({m.split(":")[0].split(" (")[0] for m in missed})))

        p(f"  3. stripped {strip_build_lens(dst)} build-lens block(s) and lens section(s)")
        did.append("stripped the build lens")

        ed = template_cfg["editorial"]
        k = convert_spelling(dst, str(machine.get("spelling") or ""), ed.get("spelling", ""),
                             ed.get("wrong_words", {}))
        if k:
            p(f"  4. converted the shipped prose to the project's spelling in {k} file(s)")
        elif str(machine.get("spelling", "us")) in ("none", ""):
            p("  4. no word list applies to the project's prose; the shipped prose was left as it is")
        else:
            p("  4. the shipped prose already uses the project's spelling variant")
        if k:
            did.append("converted the shipped prose to the project's spelling variant")

        long_lines = fill_slots(dst, slots)
        unfilled = [name for name in SLOT_NAMES if name not in slots]
        p(f"  5. filled {len(slots)} of {len(SLOTS)} slots")
        for name in unfilled:
            p(f"     LEFT UNFILLED: {{{{{name}}}}}" + ("  (it may wait for a write-up: mark it open by decision in "
                                                     "its owner row, GETTING_STARTED.md section 3)" if name in WAITS else ""))
        for rel, i, text in long_lines:
            p(f"     may not read, look at it: {rel}:{i}  {text}...")
        landed = sorted({rel for rel, _, text in long_lines if not text.startswith("the value's own definition")})
        if len(slots) == len(SLOTS):
            did.append("filled all sixteen slots")
        elif slots:
            did.append(f"filled {len(slots)} of the 16 slots")
        if unfilled:
            left.append("the slots it was given no value for, " + ", ".join(f"`{n}`" for n in unfilled)
                        + " (`GETTING_STARTED.md` §3)")
        if landed:
            left.append("a reading of the sentences a long value was substituted into, in " + ", ".join(landed)
                        + ", which the documentation sweep makes (`GETTING_STARTED.md` §4)")
        if "VOICE" in slots:
            left.append("the example voice record in `evidence_and_reasoning/editorial_standards.md`, *Voice*, "
                        "which stays only where your voice answer keeps it")

        done = write_machine_halves(dst, machine, rename)
        p("  6. the machine halves: " + (", ".join(done) if done else "none given, the template's answers stand"))
        shipped = {"spelling": ed.get("spelling"), "dashes": ed.get("dashes"),
                   "mutations": template_cfg["vocab"].get("mutations"),
                   "parties": template_cfg.get("parties", {}).get("names"),
                   "registry_required": template_cfg["registry"].get("required")}
        failed = {d.split(" NOT ")[0] for d in done if " NOT " in d}
        written = [f"`[{t}] {tk}`" for key, t, tk, _ in MACHINE
                   if key in machine and machine[key] is not None and machine[key] != shipped.get(key)
                   and f"[{t}] {tk}" not in failed]
        did.append("wrote the values the tools read for " + ", ".join(written) if written
                   else "kept the template's answers for the values the tools read")
        unset = [d.split(" NOT ")[0] for d in done if " NOT " in d]
        if unset:
            left.append("the values it could not write, " + ", ".join(unset))
        empty = [f"[{t}] {tk}" for key, t, tk, is_list in MACHINE
                 if is_list and not (machine.get(key) if key in machine else shipped.get(key))]
        left.append("the values it never writes, `[registry.by_kind]` where a kind of work needs fields of "
                    "its own and `[publication]` where a build makes the deliverable"
                    + (", and the lists still empty, " + ", ".join(f"`{e}`" for e in empty) if empty else "")
                    + " (`GETTING_STARTED.md` §3, *The machine half*)")
        if rename:
            k, also = rename_fields(dst, rename)
            p(f"  7. renamed the field(s) in {k} file(s)")
            for line in also[:10]:
                p(f"     also names the old word in prose, look at it: {line}")
            renamed = [(r, n) for r, n in rename.items() if r not in failed]
            if renamed:
                did.append("renamed the header field(s) " + ", ".join(f"{r} to {n}" for r, n in renamed))
            if also:
                left.append("the prose still naming a renamed field, in "
                            + ", ".join(sorted({x.split(":")[0] for x in also})))
        else:
            p("  7. no field renamed")

        lic_done, lic_missed, cited = write_licenses(dst, holder, citation, year)
        given = [x for x, v in (("a citation", citation), ("a copyright holder", holder)) if v]
        p("  8. the licenses: " + ("; ".join(lic_done) if lic_done
                                  else "nothing added, " + ("no holder or citation given" if not given
                                                            else "the texts to edit were not found"))
          + "; the template's kept (CC BY 4.0)")
        for m in lic_missed:
            p(f"     NOT FOUND, edit by hand: {m}")
        did.extend(lic_done)
        owed = [x for x, v in (("citation", cited), ("copyright holder", any("LICENSE-CODE" in d for d in lic_done))) if not v]
        if owed:
            left.append("this project's " + " and ".join(owed) + " (`GETTING_STARTED.md` §1, *The licenses*)")
        if lic_missed:
            left.append("the license text it could not find, " + "; ".join(lic_missed))

        hooks = subprocess.run(["bash", str(dst / "tools" / "install_hooks.sh")],
                               cwd=dst, capture_output=True, text=True)
        p("  9. the git hooks: installed, advisory" if hooks.returncode == 0
          else "  9. the git hooks: NOT INSTALLED, run tools/install_hooks.sh yourself")
        if hooks.returncode == 0:
            did.append("installed the git hooks")
        else:
            left.append("installing the git hooks (`GETTING_STARTED.md` §1)")

        titled = "PROJECT_TITLE" in slots
        write_project_readme(dst, slots.get("PROJECT_TITLE") or "{{PROJECT_TITLE}}", day, cited)
        did.append("wrote the front page" + ("" if titled else ", its title left as the slot's token"))
        pointed = write_setup_pointer(dst)
        if not pointed:
            left.append("the passage of `GETTING_STARTED.md` on the tool, which here points to this note")
        left.append("the setup decisions it never makes: the privacy scan's list, before the first commit; the two "
                    "standing directions; and whether the shipped Python check suite stays (`GETTING_STARTED.md` §1)")
        note, indexed = write_setup_note(dst, day, iso, did, left)
        p(" 10. wrote the project's front page over the template's README"
          + ("" if titled else ", its title left as {{PROJECT_TITLE}}")
          + f", and the setup note {note}" + ("" if indexed else ", NOT INDEXED: add its row to the notes index by hand"))
        if not pointed:
            p("     NOT FOUND, rewrite by hand: GETTING_STARTED.md, the passage from " + SETUP_START
              + " to " + SETUP_END + ", which in a project points to the setup note")
        n = restamp(dst, day, src)
        p(f"     stamped the {n} file(s) it changed with {day}, the day of the run; the rest keep the template's dates")

        p(" 11. the round check, in the new tree:\n")
        r = subprocess.run([sys.executable, str(dst / "tools" / "check_round.py")],
                           cwd=dst, capture_output=True, text=True)
        p("\n".join("     " + ln for ln in (r.stdout.strip() or "(no output)").split("\n")))
        if r.stderr.strip():
            p("     the round check also wrote to standard error:")
            p("\n".join("     " + ln for ln in r.stderr.strip().split("\n")))
    except Exception as e:                                    # noqa: BLE001
        shutil.rmtree(dst, ignore_errors=True)
        print(f"new_project: {type(e).__name__}: {str(e).replace(str(dst.resolve()), dst.resolve().name)}\n"
              "new_project: nothing was left behind; the target was removed", file=sys.stderr)
        return 2

    p(NEXT)
    return r.returncode


# ----------------------------------------------------------------- self-test

SELFTEST_ANSWERS = {
    "project": {"holder": "A. Researcher", "date": "1 January 2027",
                "citation": 'A. Researcher, "A worked instantiation", 2027.'},
    "slots": {
        "PROJECT_TITLE": "A worked instantiation",
        "PERSONA": "historian of administrative records",
        "VERIFICATION_TOOL": "the source at its shelfmark, in the form the source index records",
        "CHECK_FORM": "a written collation procedure against the source of record",
        "MUTATION_SET": "alter one entry, drop one folio, transpose two entries",
        "PARTIES": "none",
        "CITATION_LOCUS": "folio and entry; page",
        "REFERENCE_FIELDS": "Authors, Title, Where, Year, Identifier, Keywords, Standing",
        "REFERENCE_ADEQUACY": "a source cited to its folio for any claim about what it says",
        "DELIVERABLE": "a note in markdown under paper/, released as the file itself",
        "SPELLING": "US English",
        "DASH_CONVENTION": "no em-dashes",
        "PAPER_PRONOUN": "we",
        "VOICE": "the subject of a sentence is the document, never the data",
        "REPLY_HOOK": "the tracked settings file of the harness this project runs in",
        "DISCLOSURE_RULE": "none beyond section 6: the sources are open",
    },
    "machine": {"spelling": "us", "dashes": "no-em-dash",
                "mutations": ["alter-one-entry", "drop-one-folio", "transpose-two-entries"],
                "parties": ["none"],
                "registry_required": ["Authors", "Title", "Where", "Year"]},
    "rename": {},
}


def selftest() -> int:
    failures = 0

    def check(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail})"))

    print("tools/new_project.py --selftest\n")

    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "project"
        rc = instantiate(ROOT, dst, SELFTEST_ANSWERS, quiet=True)
        cfg = tomllib.loads(read(dst / "tools" / "artifacts.toml"))
        unfilled = [f"{f.relative_to(dst)}:{i}" for f in walk(dst, SUBSTITUTE_IN)
                    if f.name not in ABOUT_SLOTS
                    for i, line in enumerate(read(f).split("\n"), 1)
                    for m in re.finditer(r"\{\{([A-Z_]+)\}\}", line)
                    if m.group(1) in SLOT_NAMES and OWNER.get(m.group(1)) == str(f.relative_to(dst))
                    and not line[m.end():].startswith("`: ")]
        check("a fresh instantiation passes the round check with no edits", rc == 0, f"exit {rc}")
        check("the header-field catalogue survives writing the roster, decided empty",
              len(cfg["fields"]["names"]) == 18 and cfg["parties"]["names"] == ["none"],
              f"fields={cfg['fields']['names'][:2]}, parties={cfg['parties']['names']}")
        check("each machine half lands under its own table",
              cfg["vocab"]["mutations"] == SELFTEST_ANSWERS["machine"]["mutations"]
              and cfg["registry"]["required"] == ["Authors", "Title", "Where", "Year"])
        check("every owner's Slots row carries its value", not unfilled, str(unfilled[:3]))
        check("nothing of the template's own construction is left",
              not any((dst / x).exists() for x in
                      ("example", ".review", "tools/new_project.py")))
        check("no build lens survives",
              not [str(f.relative_to(dst)) for f in walk(dst, (".md",))
                   if "Build lens" in read(f) and f.name not in ABOUT_SLOTS])
        check("the template's citation is kept beside the project's",
              "Recommended citation for the template:" in read(dst / "LICENSE.md")
              and "adapted from the template" in read(dst / "LICENSE.md"))
        check("the copyright year is the project's, not this program's",
              "Copyright (c) 2027 A. Researcher" in read(dst / "LICENSE-CODE"))
        check("a file the procedure rewrote is stamped with the day of the run, not the answers' date",
              f"; updated {today_day()}.*" in read(dst / "MANIFESTO.md"))
        cfg_stamp = TOML_STAMP.search(read(dst / "tools" / "artifacts.toml"))
        check("the configuration, rewritten with the machine halves, is stamped too",
              bool(cfg_stamp) and cfg_stamp.group(2) == today_day(), cfg_stamp.group(0) if cfg_stamp else "no stamp")
        unstamped = lambda s: PY_STAMP.sub("", TOML_STAMP.sub("", STAMP.sub("", s)))
        pairs = [(f, ROOT / f.relative_to(dst)) for f in walk(dst, tuple(STAMPS))
                 if (ROOT / f.relative_to(dst)).is_file()]
        kept = [f for f, o in pairs if read(f) == read(o)]
        moved = [str(f.relative_to(dst)) for f, o in pairs
                 if read(f) != read(o) and unstamped(read(f)) == unstamped(read(o))]
        check("a file the procedure did not change keeps the template's dates",
              bool(kept) and not moved, f"{len(kept)} kept; restamped although unchanged: {moved[:3]}")
        check("the guide's own pages still explain the slots, unsubstituted",
              "{{PERSONA}}" in read(dst / "GETTING_STARTED.md"))
        check("the front page names the template the project is adapted from",
              "adapted from that template" in read(dst / "README.md"))
        flat = lambda t: " ".join(t.split())
        check("the front page and both grants of the license carry the same clause on material under its own terms",
              OWN_TERMS in flat(read(dst / "README.md")) and flat(read(dst / "LICENSE.md")).count(OWN_TERMS) == 2)
        gs = read(dst / "GETTING_STARTED.md")
        notes_dir = dst / "evidence_and_reasoning" / "notes"
        setup_notes = sorted(notes_dir.glob("*_setup.md"))
        note = read(setup_notes[0]) if setup_notes else ""
        check("a dated setup note records what the run did, and is indexed",
              len(setup_notes) == 1 and "filled all sixteen slots" in flat(note)
              and "the setup decisions it never makes" in flat(note)
              and f"]({setup_notes[0].name})" in read(notes_dir / "README.md"), flat(note)[:300])
        check("GETTING_STARTED.md points to the note in place of the tool's account, the same in every project",
              SETUP_START not in gs and SETUP_POINTER in gs and today_day() not in gs.split("\n", 3)[3])
        check("no line of the setup note opens a markdown block inside a paragraph",
              not [ln for ln in note.split("\n")[4:] if re.match(r"(#|>|[-*+] |\d+[.)] )", ln)
                   and not ln.startswith("## ")], note[:200])
        check("the template's own examples survive the spelling of another variant only where quoted",
              '"center", "labeled"' in read(dst / "evidence_and_reasoning" / "editorial_standards.md"))
        cfgtext = read(dst / "tools" / "artifacts.toml")
        check("a configuration comment keeps the slot's token as its name",
              "# {{MUTATION_SET}}:" in cfgtext and "# {{PARTIES}}:" in cfgtext)
        def text_of(f: Path) -> str:
            try:
                return f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                return ""
        named = [str(f.relative_to(dst)) for f in walk(dst)
                 if "new_project.py" in text_of(f) or "](example/)" in text_of(f) or "](../example/)" in text_of(f)
                 or "](TODO.md)" in text_of(f)]
        check("no file of the project names this program, or links to the example or the work list", not named, str(named))
        sel = subprocess.run([sys.executable, str(dst / "tools" / "lint_docs.py"), "--selftest"],
                             cwd=dst, capture_output=True, text=True)
        check("the project's own tools can still test themselves", sel.returncode == 0,
              (sel.stdout or sel.stderr).strip().split("\n")[-1][:110])

    with tempfile.TemporaryDirectory() as d:
        uk = {**SELFTEST_ANSWERS, "machine": {**SELFTEST_ANSWERS["machine"], "spelling": "UK"},
              "slots": {**SELFTEST_ANSWERS["slots"], "SPELLING": 'UK English; never "organize"'}}
        rc = instantiate(ROOT, Path(d) / "p", uk, quiet=True)
        check("a project in the other spelling variant also passes, its machine value read whatever its case", rc == 0, f"exit {rc}")
        ed = read(Path(d) / "p" / "evidence_and_reasoning" / "editorial_standards.md")
        check("the conversion leaves quotations, the other variant's example, and the researcher's answer alone",
              '"center", "labeled"' in ed and 'never "organize"' in ed and "organization" not in ed.split("## Slots")[0])

    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "p"
        ren = {**SELFTEST_ANSWERS, "rename": {"register": "Trust", "frame": "Stated-in"}}
        rc = instantiate(ROOT, dst, ren, quiet=True)
        tpl = read(dst / "evidence_and_reasoning" / "claims" / "_template.md")
        check("with two header fields renamed, it still passes", rc == 0, f"exit {rc}")
        check("the rename reaches an indented mention in a template's legend",
              "Frame:" not in tpl and "Stated-in:" in tpl,
              str([l for l in tpl.split("\n") if "Frame" in l][:2]))

    with tempfile.TemporaryDirectory() as d:
        a, b = Path(d) / "a", Path(d) / "b"
        prog = '"""A program.\n\nCreated 1 January 2026; updated 1 January 2026.\n"""\nX = 1\n'
        tmpl = '"""A template.\n\nCreated D Month YYYY; updated D Month YYYY.\n"""\nX = 1\n'
        for root, x in ((a, "X = 1"), (b, "X = 2")):
            (root / "tools").mkdir(parents=True)
            (root / "tools" / "changed.py").write_text(prog.replace("X = 1", x))
            (root / "tools" / "same.py").write_text(prog)
            (root / "tools" / "_template.py").write_text(tmpl.replace("X = 1", x))
        restamp(b, "2 January 2030", a)
        check("a program the procedure changed takes the day; one it did not, and a template's placeholder, keep theirs",
              "updated 2 January 2030." in read(b / "tools" / "changed.py")
              and "updated 1 January 2026." in read(b / "tools" / "same.py")
              and "updated D Month YYYY." in read(b / "tools" / "_template.py"))

    with tempfile.TemporaryDirectory() as d:
        for bad, why in (({"slots": {"PERSONA": "a | b"}}, "a pipe in a slot value"),
                         ({"machine": {"mutations": "one-fault"}}, "a string where a list belongs"),
                         ({"rename": {"nosuch": "X"}}, "a role that is not a header field"),
                         ({"slots": {"PERSONA": 7}}, "a number where a string belongs"),
                         ({"slots": {"VOICE": "open by decision (prompt 001); filled when a write-up is opened"}},
                          "a slot left open by decision, given as a value"),
                         ({"machine": {"parties": ["none", "a coauthor"]}}, "none beside a party"),
                         ({"machine": {"dashes": "long dashes"}}, "a dash rule the tools do not know")):
            rc = instantiate(ROOT, Path(d) / "x", bad, quiet=True)
            check(f"refused, and nothing written: {why}", rc == 2 and not (Path(d) / "x").exists())

    for target in (ROOT, ROOT / "inside", ROOT.parent):
        rc = instantiate(ROOT, target, SELFTEST_ANSWERS, quiet=True)
        check(f"a target inside the template is refused: {target.name or target}",
              rc == 2 and (target == ROOT or not (target / "MANIFESTO.md").exists()))

    # An empty-answers run from a scratch template holding files git does not
    # track, as an assistant's run with no answers is.
    paths = tracked(ROOT)
    if paths is None:
        for name in ("an empty-answers run passes the round check", "files git does not track stay behind",
                     "the front page is written anyway, its title left as the slot, and claims no project citation",
                     "the setup note names what was left: every slot, the licenses, the decisions that are not slots",
                     "nothing is added to the license without a holder or a citation"):
            print(f"  [SKIP] {name}: this template folder is not a git repository of its own")
    with tempfile.TemporaryDirectory() as d:
        if paths is None:
            paths = []
        tpl, dst = Path(d) / "tpl", Path(d) / "p"
        tpl.mkdir()
        for rel in paths:
            if (ROOT / rel).is_file():
                (tpl / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, tpl / rel)
        for args in (["init", "-q"], ["add", "-A"]):
            subprocess.run(["git", *args], cwd=tpl, capture_output=True)
        for rel in ("answers.toml", ".venv/lib/x.py", ".claude/settings.local.json"):
            (tpl / rel).parent.mkdir(parents=True, exist_ok=True)
            (tpl / rel).write_text("untracked\n")
        rc = instantiate(tpl, dst, {}, quiet=True) if paths else -1
        if paths:
            check("an empty-answers run passes the round check", rc == 0, f"exit {rc}")
        if paths:
            check("files git does not track stay behind",
                  not any((dst / x).exists() for x in ("answers.toml", ".venv", ".claude/settings.local.json")))
            page = read(dst / "README.md")
            check("the front page is written anyway, its title left as the slot, and claims no project citation",
                  page.startswith("# {{PROJECT_TITLE}}") and "this project's beside it" not in page)
        found = sorted((dst / "evidence_and_reasoning" / "notes").glob("*_setup.md")) if paths else []
        note = " ".join(read(found[0]).split()) if found else ""
        if paths:
            check("the setup note names what was left: every slot, the licenses, the decisions that are not slots",
                  all(f"`{n}`" in note for n in SLOT_NAMES) and "this project's citation and copyright holder" in note
                  and "the setup decisions it never makes" in note and "filled 0" not in note
                  and "{{" not in note, note[:400])
            check("nothing is added to the license without a holder or a citation",
                  read(dst / "LICENSE.md") == read(tpl / "LICENSE.md"))
        shutil.rmtree(tpl / ".git")
        how, _ = copy_tree(tpl, Path(d) / "q")
        check("a template folder that is not a git repository is copied whole, and the run says so",
              "not a git repository" in how and (Path(d) / "q" / "answers.toml").exists(), how)

    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "p"
        copy_tree(ROOT, dst)
        check("on a fresh copy every pointer and every license text is found",
              remove_pointers(dst) == [] and write_licenses(dst, "H", "C", "2027")[1] == [])
        for given, still in ((("H", ""), "recommended citation"), (("", "C"), "copyright holder")):
            one = Path(d) / f"one_{bool(given[0])}"
            copy_tree(ROOT, one)
            write_licenses(one, given[0], given[1], "2027")
            lic = read(one / "LICENSE.md")
            check(f"with only one of holder and citation, the license asks only for the {still}",
                  f"own {still}" in lic and lic.count("Add the project's own") == 1, lic[-600:])
        miss = Path(d) / "miss"
        copy_tree(ROOT, miss)
        (miss / "LICENSE.md").write_text(read(miss / "LICENSE.md").replace(LICENSE_CITED, "Cite the template so:"))
        done, missed, cited = write_licenses(miss, "H", "C", "2027")
        check("a citation whose anchor is missing is not claimed, and none of its edits is made",
              not cited and missed and "The template's citation above is kept" not in read(miss / "LICENSE.md"), str(missed))

    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "p"
        copy_tree(ROOT, dst)
        long_title = "A study of " + "a very long title indeed, " * 4
        hits = fill_slots(dst, {**SELFTEST_ANSWERS["slots"], "PROJECT_TITLE": long_title})
        check("a value long enough to break a sentence is reported, in any file",
              any(r.endswith("research_statement.md") for r, _, _ in hits), str(hits[:2]))

    # The questions are GETTING_STARTED.md section 3's, word for word.
    guide = read(ROOT / "GETTING_STARTED.md")
    head = "| Slot | Owner | Asked in plain words |"
    rows = {}
    if head in guide:
        for line in guide[guide.index(head):].split("\n")[2:]:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            m = re.fullmatch(r"`\{\{([A-Z_]+)\}\}`", cells[0])
            if m and len(cells) == 3:
                rows[m.group(1)] = (cells[1].strip("`"), cells[2])
    drift = [n for n, own, q in SLOTS if rows.get(n) != (own, q)]
    check("each slot's question and owner are GETTING_STARTED.md section 3's, word for word", not drift, str(drift))
    check("the answers file prints the tokens it names", "{{DELIVERABLE}}" in answers_template()
          and "{{REFERENCE_FIELDS}}" in answers_template())
    check("the closing message points to sections 1 and 4, and names no first prompt",
          "section 4" in NEXT and "section 1" in NEXT and "first prompt" not in NEXT)

    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if argv == ["--template"]:
        print(answers_template())
        return 0
    into = answers_path = None
    yes = False
    i = 0
    while i < len(argv):
        if argv[i] == "--into" and i + 1 < len(argv):
            into = Path(argv[i + 1]).resolve(); i += 2
        elif argv[i] == "--answers" and i + 1 < len(argv):
            answers_path = Path(argv[i + 1]).resolve(); i += 2
        elif argv[i] == "--yes":
            yes = True; i += 1
        else:
            print(__doc__.split("Usage")[1], file=sys.stderr)
            return 2
    if not into:
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        answers = tomllib.loads(read(answers_path)) if answers_path else {}
    except (OSError, tomllib.TOMLDecodeError) as e:
        print(f"new_project: cannot read {answers_path}: {e}", file=sys.stderr)
        return 2
    problem = target_problem(ROOT, into)
    if problem:
        print(f"new_project: {problem}", file=sys.stderr)
        return 2
    try:
        check_answers(answers)
    except Refused as e:
        print(f"new_project: {e}", file=sys.stderr)
        return 2
    if not yes:
        answers = ask(answers)
    return instantiate(ROOT, into, answers)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

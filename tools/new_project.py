#!/usr/bin/env python3
"""The instantiation procedure: this template, made into a project (GETTING_STARTED.md, sections 1 to 3).

Created 8 September 2026; updated 8 September 2026.

What it does, printing each step and what it could not do:

  1. copies the tree, leaving behind what belongs to the template's own
     construction (the worked example, the interim review records, the git
     history, the local privacy list, and this program),
     and makes the new tree a git repository;
  2. removes the pointers to what it left behind, each with the comment
     block that belonged to it, so the path check has nothing to report;
  3. strips every `> **Build lens.**` blockquote, and the two sections of
     MANIFESTO.md that describe the two lenses;
  4. fills the sixteen slots: the value into the Slots table of the file
     that owns it, and the token replaced by the value in the prose of
     every markdown and configuration file.  The guide's own pages are
     left alone, since they are about slots rather than carrying them,
     and so is program source, whose diagnostics name slots on purpose;
  5. writes the machine halves in tools/artifacts.toml, each under the
     table it belongs to, so that a value the tools read is not left at
     the template's answer;
  6. renames any header field whose name the project's discipline has
     taken ([fields.roles]; GLOSSARY.md, "Renaming a word this template
     uses"), in the configuration, the templates, and the rulebooks;
  7. converts the shipped prose to the project's spelling variant, so
     that a project not writing in the template's variant does not
     inherit a failing gate;
  8. adds the project's copyright and citation to the licenses and KEEPS
     the template's, which CC BY 4.0 requires of an adaptation;
  9. writes a project front page over the template's README, and stamps
     every file it changed with the project's start date;
 10. installs the git hooks, which are not cloned;
 11. runs the round check in the new tree and prints what it found.

It decides nothing about the research: every value is the researcher's,
asked for one at a time or read from an answers file.  It writes no log
entry: the first round does that, and the log is the researcher's first
act in the new project.  On any failure it removes the half-made tree
rather than leaving one behind.

Usage
    python3 tools/new_project.py --template > answers.toml
    python3 tools/new_project.py --into ../my-project --answers answers.toml --yes
    python3 tools/new_project.py --into ../my-project --answers answers.toml
    python3 tools/new_project.py --into ../my-project
    python3 tools/new_project.py --selftest

`--answers` reads the values from a file; without `--yes` it asks about
every value, showing what the file gave.  Without `--answers` it asks
about all of them.  `--yes` asks nothing and uses the file as it stands.

Exit status: 0 when the new tree's round check is clean; 1 when it reports
findings (which are named, and are the researcher's to clear); 2 on a
usage error, an answers file this program cannot use, or a target that
exists and is not empty, is inside the template, or contains it.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- the slots

# Every slot, the file whose Slots table owns it, and one line on what it
# decides.  The owner is where the value is written; each rulebook's own
# Slots section fixes which file that is.
SLOTS: list[tuple[str, str, str]] = [
    ("PROJECT_TITLE", "evidence_and_reasoning/README.md", "the project's name, as the statements use it"),
    ("PERSONA", "MANIFESTO.md", "the domain expert the assistant works as"),
    ("VERIFICATION_TOOL", "CHECK_METHODOLOGY.md", "the instrument or procedure of record a second reader returns to"),
    ("CHECK_FORM", "CHECK_METHODOLOGY.md", "what a check is here: a program, a written procedure, or both"),
    ("MUTATION_SET", "CHECK_METHODOLOGY.md", "the named faults a check must fail under, as prose"),
    ("PARTIES", "ONTOLOGY.md", "who may appear on a By: or Verified-by: line, as prose"),
    ("CITATION_LOCUS", "ONTOLOGY.md", "the units a citation may name a place by"),
    ("REFERENCE_FIELDS", "ONTOLOGY.md", "the bullets every registry entry carries, as prose"),
    ("REFERENCE_ADEQUACY", "evidence_and_reasoning/editorial_standards.md", "which kind of reference is adequate for which kind of claim"),
    ("DELIVERABLE", "DOCUMENT_GENRES.md", "the publishable form, and what is released with a version"),
    ("SPELLING", "evidence_and_reasoning/editorial_standards.md", "the spelling variant, as prose"),
    ("DASH_CONVENTION", "evidence_and_reasoning/editorial_standards.md", "how asides and ranges are punctuated, as prose"),
    ("PAPER_PRONOUN", "evidence_and_reasoning/editorial_standards.md", "the write-up's agent"),
    ("VOICE", "evidence_and_reasoning/editorial_standards.md", "the recorded voice rules a proposed sentence is tested against"),
    ("REPLY_HOOK", "MANIFESTO.md", "where and how the status-block check runs after each reply"),
    ("DISCLOSURE_RULE", "MANIFESTO.md", "what may leave the repository, where the sources or an approval bind it"),
]
SLOT_NAMES = [s for s, _, _ in SLOTS]
OWNER = {name: own for name, own, _ in SLOTS}

# The guide is ABOUT slots: its pages name the tokens as examples, and a
# substitution there would destroy the explanation.  Program source names
# them in its own diagnostics, for the same reason.  {{LIKE_THIS}} is the
# generic illustration and is never a slot.
ABOUT_SLOTS = {"GETTING_STARTED.md", "HOW_IT_FITS_TOGETHER.md", "FORKING.md", "GLOSSARY.md"}
SUBSTITUTE_IN = (".md", ".toml")

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
POINTERS: list[tuple[str, str, str]] = [
    ("README.md",
     "| see it working | [example/](example/): a small complete project, every gate passing |\n", ""),
    ("README.md",
     "| [TODO.md](TODO.md) | What this template does not have yet, and what each item would touch |\n", ""),
    ("README.md",
     "| [example/](example/) | A worked example: a small project instantiated from this template, with its own README, log, and fence |\n", ""),
    ("governance/README.md",
     "| the worked example, [example/](../example/) | `VISION.md`, *Support*: the researcher's first model of a round | when the researcher starts, and whenever a form is in doubt | a complete small project, every gate passing, fenced as its README says | anything of the researcher's own: it is a model, never ground truth |\n", ""),
    ("governance/README.md",
     "| the instantiation procedure, `tools/new_project.py` | `VISION.md`, *Expectation*: the researcher sets up quickly; `GETTING_STARTED.md` §1 to §3 | once, when a project is made from the template | a project with its slots filled, the build's own files and pointers gone, the licenses and the hooks in place, and the round check run in the new tree | every value in it: each is asked for, or read from an answers file |\n", ""),
    ("HOW_IT_FITS_TOGETHER.md",
     "- **Support** is the templates, the indexes, and the worked example, so\n  that the right thing to do is also the easy thing.",
     "- **Support** is the templates and the indexes, so that the right thing\n  to do is also the easy thing."),
    ("HOW_IT_FITS_TOGETHER.md",
     "**Starting.** `tools/new_project.py` makes the project from the template\nand asks for the sixteen slots; then the research statement and the\nkeystone.",
     "**Starting.** The slots, then the research statement and the keystone."),
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
POINTERS.append(
    ("GETTING_STARTED.md",
     """**Steps 1 to 3 have a tool.** `tools/new_project.py` does them: it copies
the template, removes what belongs to the template's own construction and
the pointers to it, strips the build lens, asks you for each of the
sixteen slots, writes both halves of every value, renames any field your
discipline has taken, adds your licenses beside the template's, writes a
front page, installs the hooks, and runs the round check in the new tree.

```bash
python3 tools/new_project.py --template > answers.toml   # then fill it in
python3 tools/new_project.py --into ../my-project --answers answers.toml
```

Add `--yes` to take the file as it stands; without it the tool asks about
every value, showing what the file gave, and without `--answers` it asks
about all of them. Read steps 1 to 3 anyway: they say what it is doing and why, and you have to make the same
decisions either way. Steps 4 onward are yours.""",
     """**Steps 1 to 3 were done for this project** by the template's
instantiation procedure, which does not travel with a project: it copied
the template, removed what belonged to the template's own construction,
stripped the build lens, filled the slots, wrote the licenses and the
front page, installed the hooks, and ran the round check. They are kept
below as the record of how this project was set up, and of what to change
if one of those decisions turns out to be wrong. Steps 4 onward are the
work."""))

# A row of an index, matched by the path it names rather than by its wording.
POINTER_LINES = [("tools/README.md", "[new_project.py](new_project.py)")]

BUILD_LENS = re.compile(r"^> \*\*Build lens\.\*\*.*$(?:\n^>.*$)*\n?", re.M)
LENS_SECTIONS = [("## Two lenses", "## 1. Role and identity"),
                 ("## Where the two lenses differ", "## Slots")]
SLOT_ROW = re.compile(r"^\|\s*`\{\{([A-Z_]+)\}\}`\s*\|")
STAMP = re.compile(r"^(\*Created .+?; updated )(.+?)(\.\*)$", re.M)


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


def check_answers(answers: dict) -> tuple[dict, list[str]]:
    """Everything this program will act on, checked for shape before it
    writes anything.  A value that would corrupt a markdown table or a TOML
    file is refused here rather than written and found later."""
    notes: list[str] = []
    slots = answers.get("slots") or {}
    if not isinstance(slots, dict):
        raise Refused('[slots] must be a table of NAME = "value"')
    clean: dict[str, str] = {}
    for name, val in slots.items():
        if name not in SLOT_NAMES:
            notes.append(f"[slots] {name} is not a slot of this template; ignored")
            continue
        if not isinstance(val, str):
            raise Refused(f"[slots] {name} must be a string, not {type(val).__name__}")
        if not val.strip():
            continue
        if "|" in val:
            raise Refused(f"[slots] {name} contains a pipe, which would break the Slots table row")
        if "\n" in val:
            raise Refused(f"[slots] {name} contains a line break; a slot value is one line")
        clean[name] = val.strip()

    machine = answers.get("machine") or {}
    if not isinstance(machine, dict):
        raise Refused("[machine] must be a table")
    for key, _, _, is_list in MACHINE:
        if key not in machine or machine[key] is None:
            continue
        v = machine[key]
        if is_list and not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
            raise Refused(f'[machine] {key} must be a list of strings, as in {key} = ["one", "two"]')
        if not is_list and not isinstance(v, str):
            raise Refused(f"[machine] {key} must be a string")

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


# ------------------------------------------------------------------ the steps


def copy_tree(src: Path, dst: Path) -> None:
    """Step 1: the tree, without the template's own construction."""
    top = {n for n in LEAVE_BEHIND if "/" not in n}

    def ignore(directory: str, names: list[str]) -> set[str]:
        out = {n for n in names if n in top and Path(directory) == src}
        out |= {n for n in names if n in ("__pycache__", ".pytest_cache")}
        out |= {n for n in names if n.startswith(".run_ledger.json")}
        return out

    shutil.copytree(src, dst, ignore=ignore, symlinks=True)
    for rel in (n for n in LEAVE_BEHIND if "/" in n):
        p = dst / rel
        if p.is_file():
            p.unlink()
        elif p.is_dir():
            shutil.rmtree(p)


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
    """Step 4.  A Slots row keeps its token in every file: in the owner's the
    value is written after it, and elsewhere the row points at the owner and
    is left alone.  Prose is substituted.  Returns the lines a long value
    may have broken, wherever they are."""
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
    """Steps 5 and 6, in the configuration."""
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
    """Step 6, in the prose: the field at the head of a form, indented or
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
            else:
                continue
            break
    return n_files, left


def convert_spelling(root: Path, want: str, shipped: str, words: dict) -> int:
    """Step 7.  The shipped prose is written in one variant; a project that
    picks another would inherit a failing gate on prose it did not write.
    The two starter lists are parallel, so the conversion is exact for the
    words the check knows, which are the only ones it reports."""
    if not want or want == shipped or want not in words or shipped not in words:
        return 0
    pairs = [(a, b) for a, b in zip(words[want], words[shipped]) if a != b]
    n = 0
    for p in walk(root, (".md",)):
        s = read(p)
        out = s
        for wrong, right in pairs:
            out = re.sub(rf"(?<![\w-]){re.escape(wrong)}(?![\w-])", lambda _, r=right: r, out)
            cap, cap_r = wrong[:1].upper() + wrong[1:], right[:1].upper() + right[1:]
            out = re.sub(rf"(?<![\w-]){re.escape(cap)}(?![\w-])", lambda _, r=cap_r: r, out)
        if out != s:
            p.write_text(out, encoding="utf-8")
            n += 1
    return n


def write_licenses(root: Path, holder: str, citation: str, year: str) -> None:
    """Step 8: the project's copyright and citation added, the template's kept."""
    lic = root / "LICENSE.md"
    s = read(lic)
    s = s.replace("Recommended citation for the template:",
                  f"Recommended citation for this project:\n\n    {citation}\n\n"
                  f"This project's written material is adapted from the template named\n"
                  f"below, under CC BY 4.0; it has been changed for this project.\n\n"
                  f"Recommended citation for the template:", 1)
    s = s.replace("""## In a project built from this template

Add the project's own copyright holder to `LICENSE-CODE`, beside the
template's, and add the project's own recommended citation above.
""", """## This project and the template it came from
""", 1)
    s = s.replace("""**Keep the template's citation**, and say that the project's material is
adapted from it. The written material is under CC BY 4.0, which requires
that credit be given to the original and that changes be indicated; a
project that replaces the citation rather than adding to it is out of
compliance with the license it inherits. One line is enough:""",
                  """The template's citation above is kept, as CC BY 4.0 requires: credit to
the original, and an indication that changes were made. The form is:""", 1)
    lic.write_text(s, encoding="utf-8")
    code = root / "LICENSE-CODE"
    if code.exists() and holder:
        c = re.sub(r"^(Copyright \(c\) .*)$",
                   lambda m: m.group(1) + f"\nCopyright (c) {year} {holder}",
                   read(code), count=1, flags=re.M)
        code.write_text(c, encoding="utf-8")


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

Written material is under Creative Commons Attribution 4.0 International
and code under the MIT License; [LICENSE.md](LICENSE.md) and
[LICENSE-CODE](LICENSE-CODE) carry both, and the citations of this project
and of the template it is adapted from.
"""

ROOT_FILE_NOTES = {
    "MANIFESTO.md": "the operating rules: who does what, and what the record is",
    "DOCUMENT_GENRES.md": "the three genres of artifact and what the checker verifies",
    "CHECK_METHODOLOGY.md": "trust levels, claim kinds, and the shape of a check",
    "PRECEDENCE.md": "which statement governs when two disagree",
    "ONTOLOGY.md": "the predicates the tools read, and their surface syntax",
    "GLOSSARY.md": "the method's own words, and what each will be mistaken for",
    "GETTING_STARTED.md": "how this project was set up, and how a first round goes",
    "HOW_IT_FITS_TOGETHER.md": "the system as one thing, and the prompts worth making",
    "FORKING.md": "how to change or remove a mechanism, legibly",
    "ONBOARDING.md": "what every session reads before it works",
    "CURRENT_STATE.md": "where the project stands",
    "FINDINGS.md": "what the record has established",
    "VISION.md": "the statement of intent the rulebooks cite",
    "LICENSE.md": "the license for written material, and the citations",
    "LICENSE-CODE": "the license for code",
}


def write_project_readme(root: Path, title: str, date: str) -> None:
    """Step 9.  The root table is generated from what is there, so that it is
    complete for the index check (DOCUMENT_GENRES.md item 8)."""
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
        PROJECT_README.format(title=title, date=date, root_files="\n".join(rows)), encoding="utf-8")


def restamp(root: Path, date: str) -> int:
    """Step 9.  A file this procedure rewrote is no longer the template's as of
    the template's date: its updated date is the day the project was made."""
    if not date:
        return 0
    n = 0
    for p in walk(root, (".md",)):
        s = read(p)
        # A template's stamp is a placeholder a researcher fills when they
        # copy it; dating half of it would seed every artifact with a
        # half-filled header.
        if "Created D Month YYYY" in s:
            continue
        out = STAMP.sub(lambda m: m.group(1) + date + m.group(3), s, count=1)
        if out != s:
            p.write_text(out, encoding="utf-8")
            n += 1
    return n


# ------------------------------------------------------------------ answers

ANSWERS_TEMPLATE = '''# Answers for tools/new_project.py.
#
# Every slot the project fills, the values the tools read, the header
# fields to rename, and the two license lines.  GETTING_STARTED.md section
# 3 says what each decides, and gives one filled example per slot from five
# different fields.

[project]
holder = ""          # the copyright holder for this project's code
citation = ""        # one line: author, title, year, and where it lives
date = ""            # the project's start date, "D Month YYYY"

[slots]
{slots}
[machine]
# The half the tools read.  A value here is in force; the prose half alone
# is not.  spelling, dashes and registry_required ship FILLED with the
# template's answer and are enforced until changed; mutations and parties
# ship empty, and an empty one skips its check and says so.
spelling = "us"                 # "us" | "uk" | "none" | ""
dashes = "no-em-dash"           # no-em-dash | spaced-em-dash | unspaced-em-dash | en-dash-asides | none | ""
mutations = []                  # the names a Mutation: line may carry, as a header writes them
parties = []                    # the roster beyond the researcher and the assistant
registry_required = ["Authors", "Title", "Where", "Year", "Identifier", "Keywords", "Standing"]
# {{DELIVERABLE}} has a machine half too, the [publication] table, which
# gates a build and a bibliography.  It ships disabled and this procedure
# leaves it so: a project that builds its deliverable fills it in by hand,
# as paper/README.md says, once it knows what the build command is.
# {{REFERENCE_FIELDS}} has a second half, [registry.by_kind], for a
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
    return ANSWERS_TEMPLATE.format(slots="".join(f'{n} = ""    # {what}\n' for n, _, what in SLOTS))


def ask(values: dict) -> dict:
    """Every value, one at a time, as GETTING_STARTED.md section 3 says to."""
    slots = dict(values.get("slots") or {})
    print("\nThe sixteen slots. Enter blank to keep what is shown.\n")
    for name, own, what in SLOTS:
        cur = slots.get(name, "")
        print(f"  {name}  ({what}; owned by {own})")
        got = input(f"    [{cur[:50]}] > " if cur else "    > ").strip()
        if got:
            slots[name] = got
    values["slots"] = slots

    machine = dict(values.get("machine") or {})
    print("\nThe half the tools read. A prose value alone is not in force.\n")
    for key, table, tkey, is_list in MACHINE:
        cur = machine.get(key)
        shown = ", ".join(cur) if isinstance(cur, list) else (cur or "")
        print(f"  [{table}] {tkey}" + ("   (comma-separated)" if is_list else ""))
        got = input(f"    [{shown[:60]}] > ").strip()
        if got:
            machine[key] = [x.strip() for x in got.split(",") if x.strip()] if is_list else got
    values["machine"] = machine

    rename = dict(values.get("rename") or {})
    print("\nRenaming a header field your discipline has taken (GLOSSARY.md).")
    print("  Blank keeps the shipped names; otherwise role=Name, comma-separated.")
    got = input(f"    [{', '.join(f'{k}={v}' for k, v in rename.items())}] > ").strip()
    if got:
        for pair in got.split(","):
            if "=" in pair:
                role, name = pair.split("=", 1)
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


def instantiate(src: Path, dst: Path, answers: dict, quiet: bool = False) -> int:
    p = (lambda *a, **k: None) if quiet else print
    try:
        clean, notes = check_answers(answers)
    except Refused as e:
        print(f"new_project: {e}", file=sys.stderr)
        return 2
    slots, machine, rename, proj = clean["slots"], clean["machine"], clean["rename"], clean["project"]
    date = str(proj.get("date") or "").strip()
    found = re.search(r"\b(\d{4})\b", date)
    year = found.group(1) if found else "2026"

    src_r, dst_r = src.resolve(), dst.resolve()
    if src_r == dst_r or src_r in dst_r.parents or dst_r in src_r.parents:
        print(f"new_project: {dst} is inside the template, or the template is inside it; "
              "give a directory outside this tree", file=sys.stderr)
        return 2
    if dst.exists() and any(dst.iterdir()):
        print(f"new_project: {dst} exists and is not empty", file=sys.stderr)
        return 2

    p(f"\nInstantiating {src_r.name} into {dst}\n")
    for n in notes:
        p(f"     {n}")
    if dst.exists():
        dst.rmdir()
    try:
        copy_tree(src, dst)
        init = subprocess.run(["git", "init", "-q"], cwd=dst, capture_output=True, text=True)
        p("  1. copied the tree, leaving behind: " + ", ".join(LEAVE_BEHIND)
          + ("; git initialized" if init.returncode == 0 else "; git init FAILED, run it yourself"))

        missed = remove_pointers(dst)
        total = len(POINTERS) + len(POINTER_LINES)
        p(f"  2. removed {total - len(missed)} of {total} pointers to what was left behind")
        for m in missed:
            p(f"     NOT FOUND, remove by hand: {m}")

        p(f"  3. stripped {strip_build_lens(dst)} build-lens block(s) and lens section(s)")

        long_lines = fill_slots(dst, slots)
        p(f"  4. filled {len(slots)} of {len(SLOTS)} slots")
        for name in SLOT_NAMES:
            if name not in slots:
                p(f"     LEFT UNFILLED: {{{{{name}}}}}")
        for rel, i, text in long_lines:
            p(f"     may not read, look at it: {rel}:{i}  {text}...")

        done = write_machine_halves(dst, machine, rename)
        p("  5. the machine halves: " + (", ".join(done) if done else "none given, the template's answers stand"))
        if rename:
            k, left = rename_fields(dst, rename)
            p(f"  6. renamed the field(s) in {k} file(s)")
            for line in left[:10]:
                p(f"     also names the old word in prose, look at it: {line}")
        else:
            p("  6. no field renamed")

        ed = tomllib.loads(read(src / "tools" / "artifacts.toml"))["editorial"]
        k = convert_spelling(dst, str(machine.get("spelling") or ""), ed.get("spelling", ""),
                             ed.get("wrong_words", {}))
        p(f"  7. converted the shipped prose to the project's spelling in {k} file(s)" if k
          else "  7. the shipped prose already uses the project's spelling variant")

        if proj.get("holder") or proj.get("citation"):
            write_licenses(dst, str(proj.get("holder", "")), str(proj.get("citation", "")), year)
            p(f"  8. the licenses: this project's citation added and its copyright dated {year}, "
              "the template's kept (CC BY 4.0)")
        else:
            p("  8. the licenses: NOT TOUCHED, no holder or citation given")

        if slots.get("PROJECT_TITLE"):
            write_project_readme(dst, slots["PROJECT_TITLE"], date or "D Month YYYY")
            p("  9. wrote the project's front page over the template's README")
        else:
            p("  9. the README: NOT REWRITTEN, no project title given")
        n = restamp(dst, date)
        p(f"     stamped {n} file(s) with {date}" if n else "     no file re-stamped, no start date given")

        hooks = subprocess.run(["bash", str(dst / "tools" / "install_hooks.sh")],
                               cwd=dst, capture_output=True, text=True)
        p(" 10. the git hooks: installed, advisory" if hooks.returncode == 0
          else " 10. the git hooks: NOT INSTALLED, run tools/install_hooks.sh yourself")

        p(" 11. the round check, in the new tree:\n")
        r = subprocess.run([sys.executable, str(dst / "tools" / "check_round.py")],
                           cwd=dst, capture_output=True, text=True)
        p("\n".join("     " + ln for ln in (r.stdout.strip() or "(no output)").split("\n")))
        if r.stderr.strip():
            p("     the round check also wrote to standard error:")
            p("\n".join("     " + ln for ln in r.stderr.strip().split("\n")))
    except Exception as e:                                    # noqa: BLE001
        shutil.rmtree(dst, ignore_errors=True)
        print(f"new_project: {type(e).__name__}: {e}\n"
              "new_project: nothing was left behind; the target was removed", file=sys.stderr)
        return 2

    p("""
Next, in the new project:

  1. read GETTING_STARTED.md from section 4: the first round opens with
     its log entry, and the entry is written before the work;
  2. make the first prompt of the project, which is:

         Make a documentation consistency sweep.

     It is what catches a slot value that does not read where it was
     substituted, a pointer this procedure could not reach, and a file
     still speaking in the template's voice
     (governance/roles/documentation_sweep.md).
""")
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
        "PARTIES": "the researcher and the assistant; no other party",
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
                "parties": ["a paid transcriber"],
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
        check("the header-field catalogue survives writing the roster",
              len(cfg["fields"]["names"]) == 18 and cfg["parties"]["names"] == ["a paid transcriber"],
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
        check("a file the procedure rewrote is stamped with the project's date",
              "; updated 1 January 2027.*" in read(dst / "MANIFESTO.md"))
        check("the guide's own pages still explain the slots, unsubstituted",
              "{{PERSONA}}" in read(dst / "GETTING_STARTED.md"))
        check("the front page names the template the project is adapted from",
              "adapted from that template" in read(dst / "README.md"))
        sel = subprocess.run([sys.executable, str(dst / "tools" / "lint_docs.py"), "--selftest"],
                             cwd=dst, capture_output=True, text=True)
        check("the project's own tools can still test themselves", sel.returncode == 0,
              (sel.stdout or sel.stderr).strip().split("\n")[-1][:110])

    with tempfile.TemporaryDirectory() as d:
        uk = {**SELFTEST_ANSWERS, "machine": {**SELFTEST_ANSWERS["machine"], "spelling": "uk"}}
        rc = instantiate(ROOT, Path(d) / "p", uk, quiet=True)
        check("a project in the other spelling variant also passes", rc == 0, f"exit {rc}")

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
        for bad, why in (({"slots": {"PERSONA": "a | b"}}, "a pipe in a slot value"),
                         ({"machine": {"mutations": "one-fault"}}, "a string where a list belongs"),
                         ({"rename": {"nosuch": "X"}}, "a role that is not a header field"),
                         ({"slots": {"PERSONA": 7}}, "a number where a string belongs")):
            rc = instantiate(ROOT, Path(d) / "x", bad, quiet=True)
            check(f"refused, and nothing written: {why}", rc == 2 and not (Path(d) / "x").exists())

    for target in (ROOT, ROOT / "inside", ROOT.parent):
        rc = instantiate(ROOT, target, SELFTEST_ANSWERS, quiet=True)
        check(f"a target inside the template is refused: {target.name or target}",
              rc == 2 and (target == ROOT or not (target / "MANIFESTO.md").exists()))

    with tempfile.TemporaryDirectory() as d:
        dst = Path(d) / "p"
        copy_tree(ROOT, dst)
        long_title = "A study of " + "a very long title indeed, " * 4
        hits = fill_slots(dst, {**SELFTEST_ANSWERS["slots"], "PROJECT_TITLE": long_title})
        check("a value long enough to break a sentence is reported, in any file",
              any(r.endswith("research_statement.md") for r, _, _ in hits), str(hits[:2]))

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
    if not yes:
        answers = ask(answers)
    return instantiate(ROOT, into, answers)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

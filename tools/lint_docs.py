#!/usr/bin/env python3
"""The genre and ontology linter: every statically decidable check, in one program.

Created 4 September 2026; updated 5 September 2026.

Reads tools/artifacts.toml, the single source of every path pattern and
vocabulary (ONTOLOGY.md section 7), walks every tracked or untracked-but-
not-ignored file, and reports.  Nothing here blocks the researcher: a
finding names the rulebook item it implements, and the researcher decides
(MANIFESTO.md section 13).  No dependency beyond the standard library;
Python 3.11 or later for its TOML reader; git for the two history checks.

WHAT EACH TAG IMPLEMENTS
  GENRES-1..8   DOCUMENT_GENRES.md, What the checker verifies, items 1 to 8
  EDIT-1..2     editorial_standards.md, What is checked mechanically, 1 and 2
  ONT-1..6      ONTOLOGY.md, section 5, checks 1 to 6
  CHECK-1..3    CHECK_METHODOLOGY.md, What is checked mechanically, 1 to 3
                (item 5 is GENRES-8; item 6, the citation sites, is the
                listing tool that ships beside this one)

WHAT IS NEVER READ: HTML comments, fenced code, and backtick spans, in every
file; a program's code, so that only its docstrings and comments are prose;
a configuration file's values, so that only its comments are prose; the
verbatim region of a log entry; markdown link targets, for tokens; quoted
text and block quotes, for the editorial checks; and the italicized examples
of the two files the narrative rule names, for the narrative check.  Every
skipped span is blanked, not removed, so line numbers stay true.  A
template's placeholders (NNN, D Month YYYY, <...>) are admitted where the
artifact kind is "template".

WHAT IT DOES NOT DECIDE: whether a mutation actually breaks a check (the
probe, CHECK_METHODOLOGY.md item 3, dynamic half); whether a check record's
values agree with its program's RESULT line (the concordance tool, item 4);
which version a changelog's release row belongs to (read, not checked);
everything the rulebooks assign to reading.

Usage
    python3 tools/lint_docs.py              check; exit 1 on any finding (--quiet: the summary line only when there is a finding)
    python3 tools/lint_docs.py --list       kind, default genre, and derived genre of every file
    python3 tools/lint_docs.py --selftest   build a scratch project under git, plant each
                                            defect, confirm the named check fires at the
                                            named file; exit 1 if any check stays silent or
                                            has no case
"""
from __future__ import annotations

import ast
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MONTHS = ("January|February|March|April|May|June|July|August|September|"
          "October|November|December")
DATE = rf"\d{{1,2}} (?:{MONTHS}) \d{{4}}"
PDATE = r"D Month YYYY"
ANYDATE = rf"(?:{DATE}|{PDATE})"

STAMP_RE = re.compile(rf"^\*?Created ({ANYDATE}); updated ({ANYDATE})\.?\*?\s*$")
STAMP_OPENER_RE = re.compile(r"^\*?(Created|Released|Reserved|Pre-registered|superseded by)\b", re.I)
STAMP_FORMS = [
    re.compile(rf"^Released {ANYDATE}$"),
    re.compile(rf"^Reserved {ANYDATE}, plan (?:[0-9]{{3}}[a-z]?|NNN)$"),
    re.compile(rf"^Pre-registered {ANYDATE}, \S.*$"),
    re.compile(r"^superseded by \S.*$"),
]
COLON_STAMP_RE = re.compile(r"^(Created|Released|Reserved|Pre-registered|superseded by)\s*:", re.I)
STAMP_NARRATIVE_RE = re.compile(
    rf"\b(?:Corrected|Updated|Extended|Hardened|Narrowed|Reserved)\s+{DATE}\s*:", re.I)
FIELD_RE = re.compile(r"^([A-Z][A-Za-z-]*): ?(.*)$")


def status_re(cfg: dict) -> re.Pattern:
    """The three forms a plan's Status: line may take, the verdict names
    from the configuration."""
    v = "|".join(map(re.escape, cfg["vocab"].get("plan_verdicts", ["CONFIRMED", "REFUTED", "COMPLETE", "ABANDONED"])))
    return re.compile(rf"^(?:DRAFT|ENGAGED {DATE}|CLOSED {DATE}, verdict (?:{v}))$")


NARRATIVE = [
    (re.compile(r"\bpreviously\s+(?:read|said|stated|reported|recorded)\b", re.I), "previously <verb>"),
    (re.compile(r"\bused\s+to\s+(?:read|say|state|be)\b", re.I), "used to <verb>"),
    (re.compile(r"\bno\s+longer\s+(?:holds|records|reads|says|states)\b", re.I), "no longer <verb>"),
    (re.compile(r"\bwas\s+found\s+to\s+(?:have|be)\b", re.I), "was found to"),
    (re.compile(r"\bbefore\s+the\s+correction\b", re.I), "before the correction"),
    (re.compile(r"\bsince\s+corrected\b", re.I), "since corrected"),
    (re.compile(rf"\bas\s+of\s+{DATE}", re.I), "as of <date>"),
    (re.compile(r"\bearlier\s+versions?\s+of\s+this\s+file\b", re.I), "earlier versions of this file"),
    (re.compile(r"\bsupersedes\s+the\s+earlier\b", re.I), "supersedes the earlier"),
    (re.compile(r"\bCorrection\s+of\s+record\b", re.I), "Correction of record"),
    (re.compile(r"^Last updated:.*\(", re.I), "Last updated: (...)"),
]
PAPER_PHRASES = ["without loss of generality", "clearly", "it is easy to see",
                 "it follows immediately", "as is well known", "it is well established that",
                 "scholars agree", "robust to", "remarkable", "striking", "beautiful",
                 "the point at issue"]

NUM = r"[0-9]{3}[a-z]?"
TOKEN_CLAIM = re.compile(rf"\[claim ({NUM})\]")
TOKEN_CHECK = re.compile(rf"\[check ({NUM})\]")
TOKEN_FINDING = re.compile(r"\[finding (F[0-9]{3,})\]")
TOKEN_TENSION = re.compile(r"\[tension (T[0-9]{3,})\]")
TOKEN_PLAN = re.compile(rf"(?<![\w/])plan ({NUM})(?![\w-])")
TOKEN_KEY = re.compile(r"\[([A-Z][A-Za-z0-9]{2,31})(?:,\s*[^\]]+)?\](?![\(\[])")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./-]*(?:/|\.(?:md|py|toml|txt|sh|json|tex|pdf)))`")
PLACEHOLDER = re.compile(r"NNN|YYYY|<|>|\{\{|_short_|\*|\[0-9\]|name\.md|topic\.md|D Month|\bv[NM](?=[_.])|_v[NM]\b")

FINDINGS: list[tuple[str, str, int, str]] = []
_TREE: "Tree | None" = None


def report(item: str, path: str, line: int, msg: str) -> None:
    """Every finding passes here, so `skip` in the row for `path` is honored
    by every check in one place."""
    if _TREE is not None:
        row = _TREE.rows.get(path)
        if row and item in row.get("skip", []):
            return
    FINDINGS.append((item, path, line, msg))


# ------------------------------------------------------------------ config

def load_config(root: Path) -> dict:
    with open(root / "tools" / "artifacts.toml", "rb") as fh:
        return tomllib.load(fh)


def git(root: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=root, capture_output=True,
                              text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def all_files(root: Path) -> list[str]:
    out = git(root, "ls-files", "-co", "--exclude-standard", "-z")
    if not out:
        return sorted(str(p.relative_to(root)) for p in root.rglob("*")
                      if p.is_file() and ".git" not in p.parts)
    return sorted(f for f in out.split("\0") if f and (root / f).is_file())


_GLOB_CACHE: dict[str, re.Pattern] = {}


def glob_to_re(glob: str) -> re.Pattern:
    """A shell glob as a regex in which `*` and `?` never cross a slash and
    `**` matches any depth."""
    if glob in _GLOB_CACHE:
        return _GLOB_CACHE[glob]
    out, i = [], 0
    while i < len(glob):
        c = glob[i]
        if glob.startswith("**/", i):
            out.append("(?:.*/)?"); i += 3
        elif glob.startswith("**", i):
            out.append(".*"); i += 2
        elif c == "*":
            out.append("[^/]*"); i += 1
        elif c == "?":
            out.append("[^/]"); i += 1
        elif c == "[":
            j = glob.find("]", i)
            out.append(glob[i:j + 1] if j > 0 else re.escape(c)); i = (j + 1) if j > 0 else i + 1
        else:
            out.append(re.escape(c)); i += 1
    rx = re.compile("^" + "".join(out) + "$")
    _GLOB_CACHE[glob] = rx
    return rx


def match(glob: str, rel: str) -> bool:
    return bool(glob_to_re(glob).match(rel))


def classify(cfg: dict, rel: str) -> dict | None:
    for row in cfg["artifact"]:
        if match(row["glob"], rel):
            return row
    return None


def glob_dir(glob: str) -> str:
    """The fixed directory prefix of a glob: everything before its first
    wildcard, up to the last slash."""
    cut = min([i for i in (glob.find("*"), glob.find("?"), glob.find("[")) if i >= 0] or [len(glob)])
    return glob[:cut].rsplit("/", 1)[0] if "/" in glob[:cut] else ""


# ------------------------------------------------------------------ reading

def _blank(m: re.Match) -> str:
    """The match with every character but a newline turned into a space, so
    that what is skipped keeps every line number true."""
    return re.sub(r"[^\n]", " ", m.group(0))


def strip_unread(text: str, keep_backticks: bool = False) -> str:
    """Blank what no tool reads: HTML comments, fenced code, and backtick
    spans, any of which may cross a line.  Bold keeps its content; italics
    are read, except where the narrative check says otherwise."""
    text = re.sub(r"<!--.*?-->", _blank, text, flags=re.S)
    text = re.sub(r"```.*?```", _blank, text, flags=re.S)
    if not keep_backticks:
        text = re.sub(r"`[^`]+`", _blank, text, flags=re.S)
    text = re.sub(r"\*\*([^*]+?)\*\*", r"\1", text, flags=re.S)
    return text


def blank_italics(text: str) -> str:
    """Single-line italic spans with flanking content, after list markers
    at line start are set aside so `* item` never opens a span."""
    text = re.sub(r"^(\s*)\*(?=\s)", r"\1 ", text, flags=re.M)
    return re.sub(r"(?<![\w*\\])\*(?=\S)[^*\n]+?(?<=\S)\*(?![\w*])", _blank, text)


def blank_quoted(text: str) -> str:
    """Quoted text and block quotes, which the editorial checks skip."""
    text = re.sub(r'"[^"\n]+"', _blank, text)
    text = re.sub(r"“[^”\n]+”", _blank, text)
    return "\n".join(re.sub(r"[^\n]", " ", l) if l.startswith(">") else l for l in text.splitlines())


def prose_of(text: str, row: dict, cfg: dict, keep_backticks: bool = False) -> str:
    """What the tools read as prose for this artifact.  A markdown artifact:
    everything but the unread spans.  A program: its docstrings and `#`
    comments only, never code (ONTOLOGY.md section 1.1).  A configuration
    file: its comments only.  A log entry: never its verbatim region."""
    hk = row.get("header", "stamp")
    if hk == "docstring":
        lines = text.splitlines()
        keep = [""] * len(lines)
        try:
            tree = ast.parse(text)
        except SyntaxError:
            return ""
        for node in ast.walk(tree):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                for ln in range(node.lineno, (node.end_lineno or node.lineno) + 1):
                    keep[ln - 1] = lines[ln - 1]
        for i, line in enumerate(lines):
            if line.lstrip().startswith("#"):
                keep[i] = line
        return strip_unread("\n".join(keep), keep_backticks)
    if hk == "comment":
        return strip_unread("\n".join(l if l.lstrip().startswith("#") else "" for l in text.splitlines()), keep_backticks)
    if row.get("kind") == "log-entry":
        p0, p1 = cfg["log"]["parts"][0], cfg["log"]["parts"][1]
        text = re.sub(re.escape(p0) + r".*?" + re.escape(p1), _blank, text, flags=re.S)
    return strip_unread(text, keep_backticks)


def _is_headerish(s: str) -> bool:
    return bool(STAMP_RE.match(s) or FIELD_RE.match(s) or STAMP_OPENER_RE.match(s))


def header_block(text: str, header_kind: str) -> tuple[list[tuple[int, str]], int]:
    """The header lines with their true 1-based line numbers, and the line
    the body starts at.  Markdown: after the title, the run of header-
    shaped lines up to the first blank line.  Docstring: the module
    docstring's leading run, its first line skipped unless it is a stamp."""
    lines = text.splitlines()
    out: list[tuple[int, str]] = []
    if header_kind == "docstring":
        try:
            mod = ast.parse(text)
        except SyntaxError:
            return [], 1
        if not (mod.body and isinstance(mod.body[0], ast.Expr) and isinstance(mod.body[0].value, ast.Constant)
                and isinstance(mod.body[0].value.value, str)):
            return [], 1
        start = mod.body[0].lineno
        for k, raw in enumerate(mod.body[0].value.value.splitlines()):
            s = raw.strip()
            if k == 0 and not STAMP_RE.match(s):
                continue
            if not s:
                if out:
                    break
                continue
            if _is_headerish(s):
                out.append((start + k, s))
            elif out:
                break
        return out, (out[-1][0] + 1 if out else 1)
    if header_kind == "comment":
        for i, raw in enumerate(lines, 1):
            s = raw.lstrip("# ").strip()
            if STAMP_RE.match(s):
                out.append((i, s))
                break
        return out, 1
    started = False
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if i == 1 and s.startswith("#"):
            continue
        if not s:
            if started:
                break
            continue
        if _is_headerish(s):
            out.append((i, s))
            started = True
        else:
            break
    return out, (out[-1][0] + 1 if out else 1)


def fields_of(header: list[tuple[int, str]]) -> dict[str, tuple[int, str]]:
    out: dict[str, tuple[int, str]] = {}
    for ln, s in header:
        if STAMP_RE.match(s) or STAMP_OPENER_RE.match(s) and not COLON_STAMP_RE.match(s):
            continue
        m = FIELD_RE.match(s)
        if m:
            out.setdefault(m.group(1), (ln, m.group(2).strip()))
    return out


def stamp_of(header: list[tuple[int, str]]) -> tuple[int, str, str] | None:
    for ln, s in header:
        m = STAMP_RE.match(s)
        if m:
            return ln, m.group(1), m.group(2)
    return None


# ------------------------------------------------------------------ the tree

class Tree:
    def __init__(self, root: Path, cfg: dict):
        self.root, self.cfg = root, cfg
        self.files = all_files(root)
        self.rows = {f: classify(cfg, f) for f in self.files}
        self.text: dict[str, str] = {}
        for f in self.files:
            try:
                self.text[f] = (root / f).read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                self.text[f] = ""
        self.headers = {f: header_block(self.text[f], (self.rows[f] or {}).get("header", "stamp"))
                        for f in self.files if self.rows[f]}
        self.plans = {self.num(f): f for f in self.files if self.kind(f) == "plan"}
        self.plan_status = {f: fields_of(self.headers[f][0]).get("Status", (0, ""))[1] for f in self.plans.values()}
        self.claims = {self.num(f): f for f in self.files if self.kind(f) == "claim"}
        self.checks = {self.num(f): f for f in self.files if self.kind(f) == "check"}
        self.programs = {self.num(f): f for f in self.files if self.kind(f) == "check-program"}
        self.keys = set()
        for f in self.files:
            if self.kind(f) == "registry":
                self.keys |= set(re.findall(r"^### \[([A-Z][A-Za-z0-9]{2,31})\]", self.text[f], re.M))
        self.basenames = {Path(f).name for f in self.files} | {p for f in self.files for p in Path(f).parts[:-1]}

    def kind(self, f: str) -> str:
        return (self.rows[f] or {}).get("kind", "")

    @staticmethod
    def num(f: str) -> str:
        m = re.match(rf"(?:check_)?({NUM})_", Path(f).name)
        return m.group(1) if m else Path(f).name

    def first_of_kind(self, kind: str) -> str | None:
        return next((f for f in self.files if self.kind(f) == kind), None)

    def dir_of_kind(self, kind: str) -> str:
        row = next((r for r in self.cfg["artifact"] if r["kind"] == kind), None)
        return glob_dir(row["glob"]) if row else ""

    def is_template(self, f: str) -> bool:
        return self.kind(f) == "template"

    def plan_of(self, f: str) -> tuple[str | None, str]:
        """(plan file, status) named by this artifact's Plan: line, if any."""
        pl = fields_of(self.headers[f][0]).get("Plan") if f in self.headers else None
        if not pl or not pl[1]:
            return None, ""
        num = pl[1].split(",")[0].strip()
        pf = self.plans.get(num)
        return pf, (self.plan_status.get(pf, "") if pf else "")

    def genre(self, f: str) -> str:
        """The derived genre (ONTOLOGY.md section 3), never stored: one of
        current-state, frozen, immutable, exempt, or unresolved."""
        row = self.rows[f]
        if not row:
            return "unresolved"
        g = row["genre"]
        if g in ("exempt", "immutable", "frozen"):
            return g
        if g == "self":
            return "frozen" if self.plan_status.get(f, "").startswith("CLOSED") else "current-state"
        pf, st = self.plan_of(f)
        if pf:
            return "frozen" if st.startswith("CLOSED") else "current-state"
        if g == "dated-record":
            return "frozen"
        if g == "release":
            if any(s.startswith("Released ") for _, s in self.headers[f][0]):
                return "frozen"
            if row["kind"] == "changelog" and re.search(r"^\| \(release\) \|", self.text[f], re.M):
                return "frozen"
            return "current-state"
        return "current-state"

    def prose(self, f: str, keep_backticks: bool = False) -> str:
        return prose_of(self.text[f], self.rows[f] or {}, self.cfg, keep_backticks)


# ------------------------------------------------------------------ checks

def check_genres_1_header(t: Tree) -> None:
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none":
            continue
        st = stamp_of(t.headers[f][0])
        if not st:
            hit = next(((i, l) for i, l in enumerate(t.text[f].splitlines(), 1)
                        if re.match(r"^\s*(#\s*)?\*?Created\b", l)), None)
            if hit:
                report("GENRES-1", f, hit[0], f"stamp line does not match the exact form: {hit[1].strip()[:60]!r}")
            else:
                report("GENRES-1", f, 1, "no header stamp `Created D Month YYYY; updated D Month YYYY`")
            continue
        if PDATE in (st[1], st[2]) and not t.is_template(f):
            report("GENRES-1", f, st[0], "placeholder date in a non-template artifact")


def check_genres_2_immutable(t: Tree) -> None:
    logdir = t.dir_of_kind("log-entry")
    if not logdir:
        return
    changed = git(t.root, "diff", "--name-only", "-z", "HEAD", "--", logdir + "/")
    for f in changed.split("\0"):
        if f and Path(f).name not in ("README.md",) and not Path(f).name.startswith("_template"):
            report("GENRES-2", f, 1, "committed prompt-log entry modified or deleted")


def check_genres_3_frozen(t: Tree) -> None:
    for f in t.files:
        if t.genre(f) != "frozen" or (t.rows[f] or {}).get("header", "stamp") == "none":
            continue
        old = git(t.root, "show", f"HEAD:{f}")
        if not old or old == t.text[f]:
            continue
        hk = t.rows[f].get("header", "stamp")
        oh, ob = header_block(old, hk)
        nh, nb = t.headers[f]
        if "\n".join(old.splitlines()[ob - 1:]) != "\n".join(t.text[f].splitlines()[nb - 1:]):
            so, sn = stamp_of(oh), stamp_of(nh)
            if so and sn and so[2] == sn[2]:
                report("GENRES-3", f, sn[0], "frozen body changed but the updated date did not")


def check_genres_4_resolution(t: Tree) -> None:
    for f, row in t.rows.items():
        if not row:
            report("GENRES-4", f, 1, "path matches no row of tools/artifacts.toml")
            continue
        if t.is_template(f) or row.get("header", "stamp") == "none":
            continue
        fl = fields_of(t.headers[f][0])
        if row["kind"] == "plan":
            st = fl.get("Status")
            if not st or not st[1]:
                report("GENRES-4", f, 1, "plan carries no Status: line")
            elif not status_re(t.cfg).match(st[1]):
                report("GENRES-4", f, st[0], f"Status: not one of the three forms: {st[1]!r}")
            continue
        pl = fl.get("Plan")
        if pl and pl[1]:
            pf, st = t.plan_of(f)
            if not pf:
                report("GENRES-4", f, pl[0], f"Plan: {pl[1].split(',')[0].strip()} names no plan file")
            elif not st:
                report("GENRES-4", f, pl[0], "the owning plan carries no Status: line")


def check_genres_5_narrative(t: Tree) -> None:
    italic_files = set(t.cfg.get("narrative", {}).get("italic_examples_in", []))
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none" or not t.text[f]:
            continue
        clean = t.prose(f)
        for i, line in enumerate(clean.splitlines(), 1):
            if STAMP_NARRATIVE_RE.search(line):
                report("GENRES-5", f, i, "a stamp followed by a colon opens a change narrative")
        if t.genre(f) != "current-state" or row["genre"] == "dated-record":
            continue
        if f in italic_files:
            clean = blank_italics(clean)
        skip = False
        for i, line in enumerate(clean.splitlines(), 1):
            if re.match(r"^## ", line):
                skip = bool(re.match(r"^## (Execution status|Executions)\b", line))
            if skip:
                continue
            for rx, name in NARRATIVE:
                if rx.search(line):
                    report("GENRES-5", f, i, f"narration of the text's own past: {name}")


def check_genres_6_ledger(t: Tree) -> None:
    idx = t.first_of_kind("plan-index")
    if not idx:
        return
    lines = t.prose(idx).splitlines()
    status_col, seen = None, set()
    for i, line in enumerate(lines, 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if status_col is None:
            if "Status" in cells:
                status_col = cells.index("Status")
            continue
        m = re.search(rf"\[[^\]]*\]\(({NUM})_[^)]*\)|(?<!\S)({NUM})(?!\S)", line)
        if not m or set(line) <= set("|- "):
            continue
        num = m.group(1) or m.group(2)
        pf = t.plans.get(num)
        if not pf:
            report("GENRES-6", idx, i, f"index row for plan {num}, which has no file")
            continue
        seen.add(num)
        cell = cells[status_col] if status_col is not None and status_col < len(cells) else ""
        st = t.plan_status.get(pf, "")
        if cell.split()[:1] != st.split()[:1]:
            report("GENRES-6", idx, i, f"status column says {cell!r}, plan says {st!r}")
    for num, pf in t.plans.items():
        if num not in seen:
            report("GENRES-6", idx, 1, f"index has no row for plan {num}")


def check_genres_7_paths(t: Tree) -> None:
    for f in t.files:
        if t.genre(f) != "current-state" or t.is_template(f):
            continue
        clean = t.prose(f, keep_backticks=True)
        base = (t.root / f).parent
        seen: set[str] = set()
        for i, line in enumerate(clean.splitlines(), 1):
            cands = [m.group(2) for m in LINK_RE.finditer(line)] + BACKTICK_PATH_RE.findall(line)
            for c in cands:
                c = c.split("#")[0].strip()
                if not c or c in seen or PLACEHOLDER.search(c) or "://" in c or c.startswith("mailto:"):
                    continue
                seen.add(c)
                if (base / c).exists() or (t.root / c).exists():
                    continue
                bare = c.rstrip("/")
                if "/" not in bare and bare in t.basenames:
                    continue
                report("GENRES-7", f, i, f"named path does not exist: {c}")


def check_genres_8_index(t: Tree) -> None:
    for row in t.cfg.get("index", []):
        readme = row["readme"]
        if readme not in t.text:
            continue
        listing = t.text[readme]
        for f in t.files:
            if f == readme or not match(row["lists"], f):
                continue
            if Path(f).name not in listing:
                report("GENRES-8", readme, 1, f"file not listed in this index: {f}")


def check_edit_1(t: Tree) -> None:
    ed = t.cfg.get("editorial", {})
    dashes, spelling = ed.get("dashes", ""), ed.get("spelling", "")
    if not dashes:
        report("EDIT-1", "tools/artifacts.toml", 1, "dash convention unfilled; check skipped")
    if not spelling:
        report("EDIT-1", "tools/artifacts.toml", 1, "spelling convention unfilled; check skipped")
    wrong = ed.get("wrong_words", {}).get(spelling, []) if spelling not in ("", "none") else []
    wrx = re.compile(r"\b(" + "|".join(map(re.escape, wrong)) + r")\b", re.I) if wrong else None
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none":
            continue
        clean = blank_quoted(t.prose(f))
        for i, line in enumerate(clean.splitlines(), 1):
            if dashes == "no-em-dash" and "—" in line:
                report("EDIT-1", f, i, "em-dash where the convention is none")
            elif dashes == "spaced-em-dash" and re.search(r"\S—|—\S", line):
                report("EDIT-1", f, i, "em-dash touching a character where the convention is spaced")
            if wrx:
                m = wrx.search(line)
                if m:
                    report("EDIT-1", f, i, f"spelling variant {m.group(1)!r} against the {spelling} convention")


def check_edit_2(t: Tree) -> None:
    rx = re.compile(r"\b(" + "|".join(re.escape(p) for p in PAPER_PHRASES) + r")\b", re.I)
    paper = t.dir_of_kind("version")
    for f, row in t.rows.items():
        if not row or not paper or not f.startswith(paper + "/"):
            continue
        if t.genre(f) != "current-state" or t.is_template(f) or row["genre"] == "dated-record" or row["kind"] == "index":
            continue
        clean = blank_quoted(t.prose(f))
        for i, line in enumerate(clean.splitlines(), 1):
            m = rx.search(line)
            if m:
                report("EDIT-2", f, i, f"phrase the standards ban in a live draft: {m.group(1)!r}")
            h = re.match(r"^#{2,}\s+(.*)$", line)
            if h and (re.match(r"^(A|An|The)\s", h.group(1)) or h.group(1).rstrip().endswith("?")):
                report("EDIT-2", f, i, "heading begins with an article or ends in a question mark")


def check_ont_1_fields(t: Tree) -> None:
    names = set(t.cfg["fields"]["names"])
    derived = set(t.cfg["fields"]["derived"])
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none":
            continue
        seen: set[str] = set()
        for ln, s in t.headers[f][0]:
            if STAMP_RE.match(s):
                continue
            if COLON_STAMP_RE.match(s):
                report("ONT-1", f, ln, f"a stamp written with a colon: {s[:40]!r}")
                continue
            if STAMP_OPENER_RE.match(s):
                if not any(r.match(s) for r in STAMP_FORMS):
                    report("ONT-1", f, ln, f"stamp matches none of the five forms: {s[:40]!r}")
                continue
            m = FIELD_RE.match(s)
            if not m:
                continue
            name = m.group(1)
            if name in derived:
                report("ONT-6", f, ln, f"derived state written as a field: {name}")
            elif name not in names:
                report("ONT-1", f, ln, f"unrecognized header field: {name}")
            elif name in seen:
                report("ONT-1", f, ln, f"field repeated: {name}")
            seen.add(name)


def check_ont_2_tokens(t: Tree) -> None:
    fnd = t.first_of_kind("findings")
    findings_keys = set(re.findall(r"^\|\s*(F[0-9]{3,})\s*\|", t.text.get(fnd, "") if fnd else "", re.M))
    led = t.first_of_kind("ledger")
    tension_keys = set(re.findall(r"^\|\s*(T[0-9]{3,})\s*\|", t.text.get(led, "") if led else "", re.M))
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none" or t.is_template(f):
            continue
        clean = t.prose(f)
        for i, line in enumerate(clean.splitlines(), 1):
            l = LINK_RE.sub(" ", line)
            for n in TOKEN_CLAIM.findall(l):
                if n not in t.claims:
                    report("ONT-2", f, i, f"[claim {n}] resolves to no claim")
            for n in TOKEN_CHECK.findall(l):
                if n not in t.checks:
                    report("ONT-2", f, i, f"[check {n}] resolves to no check")
            for k in TOKEN_FINDING.findall(l):
                if k not in findings_keys:
                    report("ONT-2", f, i, f"[finding {k}] resolves to no row of the findings file")
            for k in TOKEN_TENSION.findall(l):
                if k not in tension_keys:
                    report("ONT-2", f, i, f"[tension {k}] resolves to no row of the tension ledger")
            for n in TOKEN_PLAN.findall(l):
                if n not in t.plans:
                    report("ONT-2", f, i, f"plan {n} resolves to no plan file")
            rest = TOKEN_TENSION.sub(" ", TOKEN_FINDING.sub(" ", TOKEN_CHECK.sub(" ", TOKEN_CLAIM.sub(" ", l))))
            for k in TOKEN_KEY.findall(rest):
                if k not in t.keys:
                    report("ONT-2", f, i, f"[{k}] resolves to no registry entry")
        # stamps that name a path, and a plan's prerequisites
        base = (t.root / f).parent
        for ln, s in t.headers[f][0]:
            m = re.match(rf"^superseded by (\S.*)$|^Pre-registered {ANYDATE}, (\S.*)$", s)
            if m:
                p = (m.group(1) or m.group(2)).strip()
                if not ((base / p).exists() or (t.root / p).exists()):
                    report("ONT-2", f, ln, f"stamp names a path that does not exist: {p}")
        if row["kind"] == "plan":
            pre = fields_of(t.headers[f][0]).get("Prerequisites")
            if pre and pre[1] and pre[1].strip() != "none":
                bare = re.sub(r"\[claim [^\]]+\]", " ", pre[1])
                for n in re.findall(rf"\b({NUM})\b", bare):
                    if n not in t.plans:
                        report("ONT-2", f, pre[0], f"Prerequisites names no plan: {n}")


def check_ont_3_required(t: Tree) -> None:
    parties = set(t.cfg.get("parties", {}).get("names", []))
    saw_party, warned_party = False, False
    for f, row in t.rows.items():
        if not row or t.is_template(f):
            continue
        fl = fields_of(t.headers[f][0]) if f in t.headers else {}
        for name in row.get("required", []):
            if name not in fl:
                report("ONT-3", f, 1, f"required field missing: {name}")
        for name in sorted(set(row.get("required", [])) | {"Register", "Kind", "Verdict", "Status", "Serves", "Prerequisites", "Backs", "Mutation"}):
            if name in fl and not fl[name][1]:
                report("ONT-3", f, fl[name][0], f"field present but empty: {name}")
        if row["kind"] in ("check", "check-program"):
            mut = {x.strip() for x in fl.get("Mutation", (0, ""))[1].split(",") if x.strip()}
            rob = {x.strip() for x in fl.get("Robustness", (0, ""))[1].split(",") if x.strip()}
            if mut & rob:
                report("ONT-3", f, fl["Mutation"][0], f"Mutation and Robustness share names: {sorted(mut & rob)}")
        for name in ("By", "Verified-by"):
            if name in fl and fl[name][1]:
                v = fl[name][1].split(",")[0].strip()
                if v in ("researcher", "assistant", "deferred", "unchecked"):
                    continue
                saw_party = True
                if parties and v not in parties:
                    report("ONT-3", f, fl[name][0], f"{name} names a party not on the roster: {v!r}")
        if row["kind"] == "registry":
            for m in re.finditer(r"^### \[([A-Z][A-Za-z0-9]{2,31})\]\n(.*?)(?=^### |\Z)", t.text[f], re.M | re.S):
                key, body = m.group(1), m.group(2)
                for name in t.cfg["registry"]["required"]:
                    if not re.search(rf"^- {re.escape(name)}:", body, re.M):
                        report("ONT-3", f, t.text[f][:m.start()].count("\n") + 1, f"entry [{key}] lacks the bullet {name}")
    if saw_party and not parties and not warned_party:
        report("ONT-3", "tools/artifacts.toml", 1, "roster unfilled ({{PARTIES}}); party check skipped")


def check_ont_4_depends(t: Tree) -> None:
    graph: dict[str, list[str]] = {}
    for num, f in t.claims.items():
        dep = fields_of(t.headers[f][0]).get("Depends-on")
        graph[num] = []
        if dep and dep[1]:
            for d in [x.strip() for x in dep[1].split(",") if x.strip()]:
                if d not in t.claims:
                    report("ONT-4", f, dep[0], f"Depends-on names no claim: {d}")
                else:
                    graph[num].append(d)
    state: dict[str, int] = {}

    def visit(n: str, stack: list[str]) -> None:
        state[n] = 1
        for d in graph.get(n, []):
            if state.get(d) == 1:
                report("ONT-4", t.claims[n], 1, f"dependency cycle: {' -> '.join(stack + [n, d])}")
            elif state.get(d, 0) == 0:
                visit(d, stack + [n])
        state[n] = 2
    for n in graph:
        if state.get(n, 0) == 0:
            visit(n, [])


def check_ont_5_backing(t: Tree) -> None:
    for num, f in t.claims.items():
        fl = fields_of(t.headers[f][0])
        bb = fl.get("Backed-by")
        if fl.get("Register", (0, ""))[1] in ("VERIFIED", "RULED_OUT") and not (bb and TOKEN_CHECK.findall(bb[1])):
            report("ONT-5", f, 1, "a claim registered VERIFIED or RULED_OUT names no check in Backed-by")
        if not bb:
            continue
        for cn in TOKEN_CHECK.findall(bb[1]):
            cf = t.checks.get(cn)
            if not cf:
                report("ONT-5", f, bb[0], f"Backed-by [check {cn}] resolves to no check")
            elif num not in TOKEN_CLAIM.findall(fields_of(t.headers[cf][0]).get("Backs", (0, ""))[1]):
                report("ONT-5", f, bb[0], f"[check {cn}] does not name [claim {num}] in its Backs")
    for cn, cf in list(t.checks.items()) + list(t.programs.items()):
        backs = fields_of(t.headers[cf][0]).get("Backs")
        if not backs:
            continue
        for num in TOKEN_CLAIM.findall(backs[1]):
            cl = t.claims.get(num)
            if not cl:
                report("ONT-5", cf, backs[0], f"Backs [claim {num}] resolves to no claim")
            elif cn not in TOKEN_CHECK.findall(fields_of(t.headers[cl][0]).get("Backed-by", (0, ""))[1]):
                report("ONT-5", cf, backs[0], f"[claim {num}] does not name [check {cn}] in its Backed-by")


def check_check_1_register(t: Tree) -> None:
    v = t.cfg["vocab"]
    for num, f in t.claims.items():
        hdr = t.headers[f][0]
        for name in ("Register", "Kind", "Verdict"):
            n = sum(1 for _, s in hdr if s.startswith(name + ":"))
            if n > 1:
                report("CHECK-1", f, 1, f"{name} present {n} times, not once")
        fl = fields_of(hdr)
        reg, kind, ver = fl.get("Register", (1, "")), fl.get("Kind", (1, "")), fl.get("Verdict", (1, ""))
        if reg[1] and reg[1] not in v["registers"]:
            report("CHECK-1", f, reg[0], f"Register not in the vocabulary: {reg[1]!r}")
        if kind[1] and kind[1] not in v["kinds"]:
            report("CHECK-1", f, kind[0], f"Kind not in the vocabulary: {kind[1]!r}")
        if not ver[1]:
            continue
        if ver[1] == "none":
            if reg[1] not in ("OPEN", "SPECULATIVE", ""):
                report("CHECK-1", f, ver[0], f"Verdict none on a claim registered {reg[1]}")
            continue
        if reg[1] in ("OPEN", "SPECULATIVE"):
            report("CHECK-1", f, ver[0], f"Verdict {ver[1]!r} on a claim registered {reg[1]}")
        allowed = v["verdicts"].get(kind[1])
        if allowed is None:
            continue
        parts = [p.strip() for p in ver[1].split(",")]
        if allowed and isinstance(allowed[0], list):
            ok = len(parts) == len(allowed) and all(p in grp for p, grp in zip(parts, allowed))
        else:
            ok = len(parts) == 1 and parts[0] in allowed
        if not ok:
            report("CHECK-1", f, ver[0], f"Verdict {ver[1]!r} not in the {kind[1]} vocabulary")


def _is_constant(node: ast.AST) -> bool:
    """Syntactically constant: nothing in the subtree can vary with the
    computation."""
    for n in ast.walk(node):
        if isinstance(n, (ast.Name, ast.Call, ast.Attribute, ast.Subscript, ast.Starred, ast.Lambda)):
            return False
    return True


def check_check_2_constant(t: Tree) -> None:
    for f in t.files:
        if t.kind(f) != "check-program":
            continue
        try:
            tree = ast.parse(t.text[f])
        except SyntaxError as e:
            report("CHECK-2", f, e.lineno or 1, f"does not parse: {e.msg}")
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "report":
                cond = node.args[1] if len(node.args) >= 2 else next((k.value for k in node.keywords if k.arg == "ok"), None)
                if cond is not None and _is_constant(cond):
                    report("CHECK-2", f, node.lineno, "report() with a constant condition asserts nothing")


def check_check_3_mutation(t: Tree) -> None:
    known = set(t.cfg["vocab"].get("mutations", []))
    saw = False
    for f in t.files:
        kind = t.kind(f)
        if kind not in ("check", "check-program") or t.is_template(f):
            continue
        fl = fields_of(t.headers[f][0])
        mut = fl.get("Mutation")
        if not mut or not mut[1]:
            report("CHECK-3", f, 1, "no Mutation: line")
            continue
        saw = True
        names = [x.strip() for x in mut[1].split(",") if x.strip()]
        if known:
            for n in names:
                if n not in known:
                    report("CHECK-3", f, mut[0], f"mutation not in the project's set: {n!r}")
        if kind == "check-program":
            try:
                tree = ast.parse(t.text[f])
            except SyntaxError:
                continue
            bound: set[str] = set()
            for node in ast.walk(tree):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else []
                if any(getattr(tg, "id", "") == "MUTATIONS" for tg in targets):
                    val = node.value
                    if isinstance(val, ast.Dict):
                        bound |= {k.value for k in val.keys if isinstance(k, ast.Constant)}
                    elif isinstance(val, ast.Call) and getattr(val.func, "id", "") == "dict":
                        bound |= {k.arg for k in val.keywords if k.arg}
                if isinstance(node, ast.Assign) and any(isinstance(tg, ast.Subscript) and getattr(tg.value, "id", "") == "MUTATIONS"
                                                        and isinstance(tg.slice, ast.Constant) for tg in node.targets):
                    bound |= {tg.slice.value for tg in node.targets if isinstance(tg, ast.Subscript)}
            for n in names:
                if n not in bound:
                    report("CHECK-3", f, mut[0], f"mutation {n!r} not bound in MUTATIONS")
    if saw and not known:
        report("CHECK-3", "tools/artifacts.toml", 1, "mutation set unfilled ({{MUTATION_SET}}); name check skipped")


CHECKS = [check_genres_1_header, check_genres_2_immutable, check_genres_3_frozen,
          check_genres_4_resolution, check_genres_5_narrative, check_genres_6_ledger,
          check_genres_7_paths, check_genres_8_index, check_edit_1, check_edit_2,
          check_ont_1_fields, check_ont_2_tokens, check_ont_3_required, check_ont_4_depends,
          check_ont_5_backing, check_check_1_register, check_check_2_constant, check_check_3_mutation]
ITEMS = ["GENRES-1", "GENRES-2", "GENRES-3", "GENRES-4", "GENRES-5", "GENRES-6", "GENRES-7", "GENRES-8",
         "EDIT-1", "EDIT-2", "ONT-1", "ONT-2", "ONT-3", "ONT-4", "ONT-5", "ONT-6", "CHECK-1", "CHECK-2", "CHECK-3"]


def run_checks(root: Path) -> Tree:
    global _TREE
    FINDINGS.clear()
    t = Tree(root, load_config(root))
    _TREE = t
    for c in CHECKS:
        c(t)
    return t


def run(root: Path, quiet: bool = False) -> int:
    t = run_checks(root)
    for item, path, line, msg in sorted(FINDINGS):
        print(f"{item:9s} {path}:{line}: {msg}")
    n = len(FINDINGS)
    if not quiet or n:
        print(f"\n{len(t.files)} files, {n} finding(s)")
    return 1 if n else 0


def list_tree(root: Path) -> int:
    t = Tree(root, load_config(root))
    print(f"{'kind':14s} {'default':14s} {'derived':14s} path")
    for f in t.files:
        row = t.rows[f] or {}
        print(f"{row.get('kind', '?'):14s} {row.get('genre', '?'):14s} {t.genre(f):14s} {f}")
    return 0


# ------------------------------------------------------------------ selftest

STAMP = "*Created 1 January 2026; updated 1 January 2026.*"


def fixture() -> dict[str, str]:
    """A small but realistic project: an open plan and a closed one, claims
    and checks under each, a note, a review, a log entry, a released version
    with its changelog, every index.  Clean under every check; the log
    entry's verbatim region carries an em-dash and a spelling variant on
    purpose, since no check may read it."""
    S = STAMP
    return {
        "README.md": f"# Index\n\n{S}\n\n| File | |\n|---|---|\n| [MANIFESTO.md](MANIFESTO.md) | |\n| [DOCUMENT_GENRES.md](DOCUMENT_GENRES.md) | |\n| [CHECK_METHODOLOGY.md](CHECK_METHODOLOGY.md) | |\n| [PRECEDENCE.md](PRECEDENCE.md) | |\n| [ONTOLOGY.md](ONTOLOGY.md) | |\n| [ONBOARDING.md](ONBOARDING.md) | |\n| [CURRENT_STATE.md](CURRENT_STATE.md) | |\n| [FINDINGS.md](FINDINGS.md) | |\n| [LICENSE.md](LICENSE.md) | |\n",
        "MANIFESTO.md": f"# M\n\n{S}\n\nRules.\n",
        "DOCUMENT_GENRES.md": f"# G\n\n{S}\n\nGenres.\n",
        "CHECK_METHODOLOGY.md": f"# C\n\n{S}\n\nChecks.\n",
        "PRECEDENCE.md": f"# P\n\n{S}\n\nTiers.\n",
        "ONTOLOGY.md": f"# O\n\n{S}\n\nPredicates.\n",
        "ONBOARDING.md": f"# On\n\n{S}\n\nRead.\n",
        "CURRENT_STATE.md": f"# S\n\n{S}\n\nState.\n",
        "FINDINGS.md": f"# F\n\n{S}\n\n| Key | Finding |\n|---|---|\n| F001 | x [claim 002] |\n",
        "LICENSE.md": f"# L\n\n{S}\n\nMIT.\n",
        "evidence_and_reasoning/README.md": f"# E\n\n{S}\n\n| File |\n|---|\n| [research_statement.md](research_statement.md) |\n| [editorial_standards.md](editorial_standards.md) |\n| [public_record_tensions.md](public_record_tensions.md) |\n| [claims/](claims/) |\n| [checks/](checks/) |\n| [research_plans/](research_plans/) |\n| [notes/](notes/) |\n| [references/](references/) |\n",
        "evidence_and_reasoning/research_statement.md": f"# RS\n\n{S}\n\nThe question.\n",
        "evidence_and_reasoning/editorial_standards.md": f"# Ed\n\n{S}\n\n",
        "evidence_and_reasoning/public_record_tensions.md": f"# T\n\n{S}\n\n| # | a | b | c | Caution |\n|---|---|---|---|---|\n| T001 | [claim 002] | [Key1] | x | live |\n",
        "evidence_and_reasoning/claims/README.md": f"# Claims\n\n{S}\n\n| Claim |\n|---|\n| [001](001_a.md) |\n| [002](002_b.md) |\n",
        "evidence_and_reasoning/claims/001_a.md": f"# Claim 001: a\n\n{S}\nRegister: OPEN\nKind: documentary\nVerdict: none\nPlan: 001, task 1\nVerified-by: unchecked\nBacked-by: [check 001]\n\n## Claim\n\nSays so [Key1, p. 2].\n",
        "evidence_and_reasoning/claims/002_b.md": f"# Claim 002: b\n\n{S}\nRegister: VERIFIED\nKind: documentary\nVerdict: confirmed\nPlan: 002, task 1\nVerified-by: researcher\nBacked-by: [check 002]\n\n## Claim\n\nHolds [Key1, f. 3r].\n",
        "evidence_and_reasoning/checks/README.md": f"# Checks\n\n{S}\n\n| Check |\n|---|\n| [001](001_a.md) |\n| [002](002_b.md) |\n",
        "evidence_and_reasoning/checks/001_a.md": f"# Check 001: a\n\n{S}\nPlan: 001, task 1\nBacks: [claim 001]\nInstrument: the edition\nMutation: variant-reading\n\n## 1\n\nx\n",
        "evidence_and_reasoning/checks/002_b.md": f"# Check 002: b\n\n{S}\nPlan: 002, task 1\nBacks: [claim 002]\nInstrument: the edition\nMutation: variant-reading\n\n## 1\n\ny\n",
        "evidence_and_reasoning/research_plans/README.md": f"# Plans\n\n{S}\n\n| Plan |\n|---|\n| [001](001_a.md) |\n| [002](002_b.md) |\n| [ROADMAP.md](ROADMAP.md) |\n",
        "evidence_and_reasoning/research_plans/001_a.md": f"# Plan 001: a\n\n{S}\nStatus: ENGAGED 1 January 2026\nServes: none, setup\nPrerequisites: none\n\n## Execution status\n\n| Task | State |\n|---|---|\n| 1 | done |\n",
        "evidence_and_reasoning/research_plans/002_b.md": f"# Plan 002: b\n\n{S}\nStatus: CLOSED 2 January 2026, verdict COMPLETE\nServes: none, setup\nPrerequisites: 001\n\n## Execution status\n\n| Task | State |\n|---|---|\n| 1 | done |\n",
        "evidence_and_reasoning/research_plans/ROADMAP.md": f"# Roadmap\n\n{S}\n\n| Plan | Q | Status |\n|---|---|---|\n| [001](001_a.md) | a | ENGAGED |\n| [002](002_b.md) | b | CLOSED |\n",
        "evidence_and_reasoning/notes/README.md": f"# N\n\n{S}\n\n| File |\n|---|\n| [2026-01-02_x.md](2026-01-02_x.md) |\n",
        "evidence_and_reasoning/notes/2026-01-02_x.md": f"# x: 2 January 2026\n\n{S}\n\n**Working note.** Found y.\n",
        "evidence_and_reasoning/references/README.md": f"# R\n\n{S}\n\n| File |\n|---|\n| [topic.md](topic.md) |\n",
        "evidence_and_reasoning/references/topic.md": f"# References: topic\n\n{S}\n\n### [Key1]\n\n- Authors: A\n- Title: T\n- Where: W\n- Year: 2020\n- Identifier: doi\n- Keywords: k\n- Standing: searched x, 1 January 2026; none found\n\n### [Key2]\n\n- Authors: B\n- Title: U\n- Where: W\n- Year: 2021\n- Identifier: doi\n- Keywords: k\n- Standing: searched x, 1 January 2026; none found\n",
        "paper/README.md": f"# Paper\n\n{S}\n\n| File |\n|---|\n| [main_v1.md](main_v1.md) |\n| [v1_to_v2_changelog.md](v1_to_v2_changelog.md) |\n| [reviews/](reviews/) |\n",
        "paper/main_v1.md": f"# Main\n\n{S}\nReleased 3 January 2026\n\nThe write-up [claim 002].\n",
        "paper/v1_to_v2_changelog.md": f"# Changelog: v1 to v2\n\n{S}\n\n| Where | What | Why | Backed by |\n|---|---|---|---|\n| s1 | x | review | [claim 002] |\n",
        "paper/reviews/README.md": f"# Rv\n\n{S}\n\n| File |\n|---|\n| [2026-01-03_r_main.md](2026-01-03_r_main.md) |\n",
        "paper/reviews/2026-01-03_r_main.md": f"# Review: main, 3 January 2026\n\n{S}\n\nA referee pass by r of `main_v1.md` at v1; blind: yes.\n",
        "prompt_logs/README.md": f"# Logs\n\n{S}\n\n| Log |\n|---|\n| [001](001_setup.md) |\n",
        "prompt_logs/001_setup.md": f"# Prompt 001: setup\n\n{S}\n\n--- PROMPT START ---\nset it up — colour it\n--- PROMPT END ---\n\n## What was done\n\nSetup.\n\n## Corrections and departures\n\nnone\n\n## Closing status\n\n```\nDONE: setup\n```\n",
        "python_project/README.md": f"# Py\n\n{S}\n\n| File |\n|---|\n| [src/](src/) |\n| [conftest.py](conftest.py) |\n",
        "python_project/conftest.py": '"""Puts src on the path.\n\nCreated 1 January 2026; updated 1 January 2026.\n"""\nimport sys\n',
        "python_project/src/README.md": f"# Src\n\n{S}\n\n| File |\n|---|\n| [check_002_b.py](check_002_b.py) |\n",
        "python_project/src/check_002_b.py": '"""Check 002: b.\n\nCreated 1 January 2026; updated 1 January 2026.\nPlan: 002, task 1\nBacks: [claim 002]\nInstrument: x\nMutation: variant-reading\n"""\nimport sys\nMUTATIONS: dict[str, "callable"] = {"variant-reading": lambda o: o}\nFAILURES = []\ndef report(n, ok, d=""):\n    if not ok:\n        FAILURES.append(n)\nreport("x", len(sys.argv) >= 1)\n',
        "tools/README.md": f"# Tools\n\n{S}\n\n| File |\n|---|\n| [artifacts.toml](artifacts.toml) |\n",
        ".gitignore": "*.log\n.privacy/\n__pycache__/\n*.py[cod]\n",
    }


def scratch_config() -> str:
    """The shipped configuration, its one unfilled slot filled so that the
    scratch project is a project and not a template."""
    cfg_text = (ROOT / "tools" / "artifacts.toml").read_text()
    assert "\nmutations = []\n" in cfg_text
    return cfg_text.replace("\nmutations = []\n", '\nmutations = ["variant-reading"]\n')


def scratch_project(tmp: Path, files: dict[str, str], cfg_text: str) -> None:
    """Write the fixture and the configuration under `tmp`."""
    (tmp / "tools").mkdir(parents=True, exist_ok=True)
    (tmp / "tools" / "artifacts.toml").write_text(cfg_text)
    for rel, body in files.items():
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text(body)


def scratch_commit(tmp: Path) -> None:
    """Make `tmp` a repository with everything committed, so the history
    checks have a HEAD to read."""
    for args in (["init", "-q"], ["add", "-A"], ["-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "fixture"]):
        subprocess.run(["git", *args], cwd=tmp, capture_output=True)


def selftest() -> int:
    cfg_text = scratch_config()
    failures, covered = 0, set()
    write_all = lambda tmp, files: scratch_project(tmp, files, cfg_text)
    commit = scratch_commit

    def run_case(name: str, item: str, path: str, needle: str, mutate) -> None:
        nonlocal failures
        covered.add(item)
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            files = fixture()
            write_all(tmp, files)
            commit(tmp)
            mutate(tmp, files)
            run_checks(tmp)
            found = list(FINDINGS)
            hit = any(x[0] == item and x[1] == path and needle in x[3] for x in found)
            others = sorted({x[0] for x in found if x[0] != item})
            failures += 0 if hit else 1
            print(f"  [{'PASS' if hit else 'FAIL'}] {item:9s} {name}"
                  + (f"   (also: {others})" if others and hit else "")
                  + ("" if hit else f"   (got: {[(x[0], x[1], x[3][:40]) for x in found]})"))

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        write_all(tmp, fixture())
        commit(tmp)
        run_checks(tmp)
        ok = not FINDINGS
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] the unplanted tree is clean under every check"
              + ("" if ok else f": {[(x[0], x[1], x[3][:50]) for x in FINDINGS]}"))

    def w(tmp, rel, body):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text(body)

    def sub(rel, a, b):
        return lambda t, f: w(t, rel, f[rel].replace(a, b))

    def add(rel, extra):
        return lambda t, f: w(t, rel, f[rel] + extra)

    C1, C2, K2, P2 = "evidence_and_reasoning/claims/001_a.md", "evidence_and_reasoning/claims/002_b.md", "evidence_and_reasoning/checks/002_b.md", "python_project/src/check_002_b.py"
    run_case("a rulebook with no stamp", "GENRES-1", "MANIFESTO.md", "no header stamp", lambda t, f: w(t, "MANIFESTO.md", "# M\n\nRules.\n"))
    run_case("a stamp with trailing text", "GENRES-1", "MANIFESTO.md", "exact form", sub("MANIFESTO.md", STAMP, "*Created 1 January 2026; updated 1 January 2026 (typo).*"))
    run_case("a committed log entry edited", "GENRES-2", "prompt_logs/001_setup.md", "modified", add("prompt_logs/001_setup.md", "\nafterthought\n"))
    run_case("a frozen claim's body edited, date unmoved", "GENRES-3", C2, "updated date did not", add(C2, "\nMore.\n"))
    run_case("a frozen review edited, date unmoved", "GENRES-3", "paper/reviews/2026-01-03_r_main.md", "updated date did not", add("paper/reviews/2026-01-03_r_main.md", "\nMore.\n"))
    run_case("an unmatched path", "GENRES-4", "stray.md", "no row", lambda t, f: w(t, "stray.md", "# s\n"))
    run_case("a Plan: naming no plan", "GENRES-4", C1, "names no plan", sub(C1, "Plan: 001", "Plan: 009"))
    run_case("a plan whose Status: is malformed", "GENRES-4", "evidence_and_reasoning/research_plans/001_a.md", "three forms", sub("evidence_and_reasoning/research_plans/001_a.md", "Status: ENGAGED 1 January 2026", "Status: Engaged"))
    run_case("historical voice in a rulebook", "GENRES-5", "MANIFESTO.md", "previously", add("MANIFESTO.md", "\nThis section previously read otherwise.\n"))
    run_case("a stamp with a colon narrative", "GENRES-5", "MANIFESTO.md", "change narrative", add("MANIFESTO.md", "\nUpdated 2 January 2026: clause tightened.\n"))
    run_case("index status disagreeing with the plan", "GENRES-6", "evidence_and_reasoning/research_plans/ROADMAP.md", "status column", sub("evidence_and_reasoning/research_plans/ROADMAP.md", "| ENGAGED |", "| DRAFT |"))
    run_case("a plan with no index row", "GENRES-6", "evidence_and_reasoning/research_plans/ROADMAP.md", "no row for plan", sub("evidence_and_reasoning/research_plans/ROADMAP.md", "| [002](002_b.md) | b | CLOSED |\n", ""))
    run_case("a named path that does not exist", "GENRES-7", "MANIFESTO.md", "does not exist", add("MANIFESTO.md", "\nSee `tools/nothing.py`.\n"))
    run_case("a path named in a docstring", "GENRES-7", "python_project/conftest.py", "does not exist", sub("python_project/conftest.py", "Puts src on the path.", "Puts `src/gone.py` on the path."))
    run_case("a claim missing from its index", "GENRES-8", "evidence_and_reasoning/claims/README.md", "not listed", sub("evidence_and_reasoning/claims/README.md", "| [002](002_b.md) |\n", ""))
    run_case("an em-dash", "EDIT-1", "MANIFESTO.md", "em-dash", add("MANIFESTO.md", "\nOne — two.\n"))
    run_case("a UK spelling", "EDIT-1", "MANIFESTO.md", "spelling variant", add("MANIFESTO.md", "\nIt is labelled.\n"))
    run_case("an advocacy word in a live draft", "EDIT-2", "paper/main_v2.md", "ban in a live draft", lambda t, f: (w(t, "paper/main_v2.md", f"# P2\n\n{STAMP}\n\nA remarkable result.\n"), w(t, "paper/README.md", f["paper/README.md"] + "| [main_v2.md](main_v2.md) |\n")))
    run_case("a heading ending in a question mark", "EDIT-2", "paper/main_v2.md", "question mark", lambda t, f: (w(t, "paper/main_v2.md", f"# P2\n\n{STAMP}\n\n## Does it hold?\n\nYes.\n"), w(t, "paper/README.md", f["paper/README.md"] + "| [main_v2.md](main_v2.md) |\n")))
    run_case("an unknown header field", "ONT-1", C1, "unrecognized", sub(C1, "Kind: documentary", "Kind: documentary\nProgram: x"))
    run_case("a repeated field", "ONT-1", C1, "repeated", sub(C1, "Kind: documentary", "Kind: documentary\nKind: formal"))
    run_case("a stamp with a colon", "ONT-1", C1, "with a colon", sub(C1, "Verified-by: unchecked", "Verified-by: unchecked\nReserved: 1 January 2026, plan 001"))
    run_case("a stamp matching no form", "ONT-1", C1, "none of the five", sub(C1, "Verified-by: unchecked", "Verified-by: unchecked\nReserved 1 January 2026 plan 001"))
    run_case("a claim token resolving to nothing", "ONT-2", "CURRENT_STATE.md", "[claim 042]", add("CURRENT_STATE.md", "\nSee [claim 042].\n"))
    run_case("a registry key resolving to nothing", "ONT-2", "CURRENT_STATE.md", "[Nope99]", add("CURRENT_STATE.md", "\nSee [Nope99].\n"))
    run_case("a plan token resolving to nothing", "ONT-2", "CURRENT_STATE.md", "plan 042", add("CURRENT_STATE.md", "\nSee plan 042.\n"))
    run_case("a superseded-by path that does not exist", "ONT-2", "paper/main_v1.md", "stamp names a path", sub("paper/main_v1.md", "Released 3 January 2026", "Released 3 January 2026\nsuperseded by paper/gone.md"))
    run_case("a prerequisite naming no plan", "ONT-2", "evidence_and_reasoning/research_plans/002_b.md", "Prerequisites names no plan", sub("evidence_and_reasoning/research_plans/002_b.md", "Prerequisites: 001", "Prerequisites: 009"))
    run_case("a missing required field", "ONT-3", C1, "required field missing", sub(C1, "Verified-by: unchecked\n", ""))
    run_case("an empty field", "ONT-3", C1, "present but empty", sub(C1, "Verified-by: unchecked", "Verified-by:"))
    run_case("a registry entry lacking a bullet", "ONT-3", "evidence_and_reasoning/references/topic.md", "lacks the bullet", sub("evidence_and_reasoning/references/topic.md", "- Standing: searched x, 1 January 2026; none found\n", ""))
    run_case("Mutation and Robustness sharing a name", "ONT-3", K2, "share names", sub(K2, "Mutation: variant-reading", "Mutation: variant-reading\nRobustness: variant-reading"))
    run_case("a dependency naming no claim", "ONT-4", C1, "names no claim", sub(C1, "Verified-by: unchecked", "Verified-by: unchecked\nDepends-on: 042"))
    run_case("a dependency cycle", "ONT-4", C1, "cycle", sub(C1, "Verified-by: unchecked", "Verified-by: unchecked\nDepends-on: 001"))
    run_case("one-way backing, from the claim side", "ONT-5", C2, "does not name", sub(K2, "Backs: [claim 002]", "Backs: [claim 001]"))
    run_case("one-way backing, from the check side", "ONT-5", K2, "does not name", sub(C2, "Backed-by: [check 002]\n", ""))
    run_case("a VERIFIED claim naming no check", "ONT-5", C2, "names no check", sub(C2, "Backed-by: [check 002]\n", ""))
    run_case("derived state as a field", "ONT-6", C1, "derived state", sub(C1, "Kind: documentary", "Kind: documentary\nGenre: frozen"))
    run_case("a register outside the vocabulary", "CHECK-1", C1, "Register not", sub(C1, "Register: OPEN", "Register: PROVEN"))
    run_case("a kind outside the vocabulary", "CHECK-1", C1, "Kind not", sub(C1, "Kind: documentary", "Kind: textual"))
    run_case("a verdict outside its kind", "CHECK-1", C2, "not in the documentary", sub(C2, "Verdict: confirmed", "Verdict: proved"))
    run_case("a verdict on an OPEN claim", "CHECK-1", C1, "on a claim registered OPEN", sub(C1, "Verdict: none", "Verdict: confirmed"))
    run_case("a constant-condition report", "CHECK-2", P2, "constant condition", sub(P2, "report(\"x\", len(sys.argv) >= 1)", "report(\"x\", 1 == 1)"))
    run_case("a constant keyword condition", "CHECK-2", P2, "constant condition", sub(P2, "report(\"x\", len(sys.argv) >= 1)", "report(\"x\", ok=True)"))
    run_case("an unbound mutation name", "CHECK-3", P2, "not bound", sub(P2, '"variant-reading": lambda o: o', ''))
    run_case("a check with no Mutation: line", "CHECK-3", K2, "no Mutation", sub(K2, "Mutation: variant-reading\n", ""))
    run_case("a mutation outside the project's set", "CHECK-3", K2, "not in the project's set", sub(K2, "Mutation: variant-reading", "Mutation: bogus"))
    run_case("the mutation set left unfilled", "CHECK-3", "tools/artifacts.toml", "unfilled", lambda t, f: w(t, "tools/artifacts.toml", cfg_text.replace('mutations = ["variant-reading"]', "mutations = []")))
    run_case("the dash convention left unfilled", "EDIT-1", "tools/artifacts.toml", "unfilled", lambda t, f: w(t, "tools/artifacts.toml", cfg_text.replace('dashes = "no-em-dash"', 'dashes = ""')))
    run_case("a party off the roster, roster unfilled", "ONT-3", "tools/artifacts.toml", "roster unfilled", sub(C2, "Verified-by: researcher", "Verified-by: an outsider"))

    missing = [i for i in ITEMS if i not in covered]
    for i in missing:
        failures += 1
        print(f"  [FAIL] {i:9s} exercised by no case")
    print(f"\n  VERDICT: {'every check shown to fire, and the unplanted tree clean' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if "--list" in argv:
        return list_tree(ROOT)
    return run(ROOT, quiet="--quiet" in argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

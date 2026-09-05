#!/usr/bin/env python3
"""The round check: every gate a round must pass, in one command.

Created 5 September 2026; updated 5 September 2026.

Run before work is handed back and before changes are reported ready to
commit (MANIFESTO.md section 13).  Nothing here blocks the researcher: a
finding names the item it implements, and the researcher decides.  It
reads tools/artifacts.toml for every path, pattern, and setting, and it
honors a row's `skip` list like the linter does.  The privacy scan is a
separate command, tools/privacy_scan.py, run beside this one.

WHAT IT RUNS
  the linter, tools/lint_docs.py, whose findings pass through under their
      own tags; among them GENRES-2, the log's immutability, and GENRES-8,
      the index coverage of every folder, the log's index included
  ROUND-1  the log's numbering: contiguous from 001, zero-padded to at
           least three digits, no number twice, every name of the form
           NNN_short_description.md (MANIFESTO.md section 8)
  ROUND-2  the parts of an entry the researcher may still edit, that is,
           one not yet committed or differing from its committed version:
           the parts [log] names, each once and in order, searched after
           the verbatim region, which ends at the first closing delimiter,
           and outside fenced code; and, under the
           last part, a fenced status block of the section-16 form with no
           RUNNING line (prompt_logs/README.md, "The four parts of an
           entry").  A committed entry is immutable and is completed by a
           later entry, so it is not re-read here.
  ROUND-3  the build, where [publication] is enabled: every output and the
           build log newer than every source, and the log matching no
           error marker.  "Newer" is by modification time, which a
           checkout does not preserve: the gate is meaningful on a tree
           where the build has run since the sources last changed, and a
           git-ignored log is absent on a fresh clone until then.  The
           build is the researcher's to run; the finding names the
           command.
  ROUND-4  the bibliography, where [publication] names one: every entry
           cited, no citation of an entry the bibliography lacks, no entry
           defined twice, and the entries in the order of their first
           citation, taking the sources in the configured order and
           alphabetically within a glob, comments included, keys compared
           as written.

Usage
    python3 tools/check_round.py               exit 1 on any finding, 2 if misconfigured
    python3 tools/check_round.py --selftest    plant each defect in a scratch project
    python3 tools/check_round.py --scratch DIR write the clean scratch project, these
                                               tools included, into DIR (absent or empty),
                                               for exercising the hooks in a throwaway
                                               repository
"""
from __future__ import annotations

import os
import re
import secrets
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_status_reply  # noqa: E402
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
report = lint_docs.report  # one gate for every finding, so `skip` is honored in one place

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[^\n]*\n(.*?)^ {0,3}\1[^\n]*$", re.S | re.M)
OPEN_FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})", re.M)


# ------------------------------------------------------------------ the log

def log_entries(t: lint_docs.Tree) -> list[str]:
    return [f for f in t.files if t.kind(f) == "log-entry"]


def log_index(t: lint_docs.Tree) -> str:
    d = t.dir_of_kind("log-entry")
    return f"{d}/README.md" if d and f"{d}/README.md" in t.text else (d or "prompt_logs")


def check_round_1_numbering(t: lint_docs.Tree) -> None:
    seen: dict[int, str] = {}
    for f in log_entries(t):
        m = re.match(r"(\d+)_\S", Path(f).name)
        if not m:
            report("ROUND-1", f, 1, "entry name is not of the form NNN_short_description.md")
            continue
        if len(m.group(1)) < 3:
            report("ROUND-1", f, 1, "entry number not zero-padded to three digits")
        n = int(m.group(1))
        if n == 0:
            report("ROUND-1", f, 1, "entry numbered 000; numbering starts at 001")
        if n in seen:
            report("ROUND-1", f, 1, f"entry number {n:03d} used twice: also {seen[n]}")
        seen.setdefault(n, f)
    if seen:
        for n in sorted(set(range(1, max(seen) + 1)) - set(seen)):
            report("ROUND-1", log_index(t), 1, f"entry {n:03d} missing: numbering is not contiguous")


def editable_entries(t: lint_docs.Tree) -> set[str]:
    """Entries the researcher may still edit: untracked, or differing from HEAD."""
    d = t.dir_of_kind("log-entry")
    if not d:
        return set()
    if not lint_docs.git(t.root, "rev-parse", "--verify", "HEAD"):
        return set(log_entries(t))
    changed = lint_docs.git(t.root, "diff", "--name-only", "-z", "HEAD", "--", d + "/")
    new = lint_docs.git(t.root, "ls-files", "--others", "--exclude-standard", "-z", "--", d + "/")
    return {f for f in (changed + new).split("\0") if f}


def check_round_2_parts(t: lint_docs.Tree) -> None:
    parts = t.cfg.get("log", {}).get("parts", [])
    if len(parts) < 3:
        report("ROUND-2", "tools/artifacts.toml", 1, "[log] parts needs the two delimiters and at least one further part")
        return
    editable = editable_entries(t)
    for f in log_entries(t):
        if f not in editable:
            continue
        lines = t.text[f].splitlines()
        pos: list[int] = []
        # the two delimiters, anywhere; the verbatim region between them is read by no check
        for p in parts[:2]:
            hits = [i for i, l in enumerate(lines, 1) if l.strip() == p]
            if not hits:
                report("ROUND-2", f, 1, f"part missing: {p!r}")
            pos.append(hits[0] if hits else 0)
        if pos[0] and pos[1] and pos[1] < pos[0]:
            report("ROUND-2", f, pos[1], f"{parts[1]!r} stands before {parts[0]!r}")
        start = pos[1] if all(pos) else 0
        # the remaining parts, after the verbatim region and outside fenced code
        after = "\n".join(lines[start:])
        blanked = re.sub(FENCE_RE, lint_docs._blank, after).splitlines()
        for p in parts[2:]:
            hits = [start + i for i, l in enumerate(blanked, 1) if l.strip() == p]
            if not hits:
                report("ROUND-2", f, 1, f"part missing: {p!r}")
            elif len(hits) > 1:
                report("ROUND-2", f, hits[1], f"part repeated: {p!r}")
            pos.append(hits[0] if hits else 0)
        if all(pos) and pos != sorted(pos):
            report("ROUND-2", f, pos[0], "parts out of order: " + ", ".join(p for _, p in sorted(zip(pos, parts))))
        if not pos[-1]:
            continue
        tail = "\n".join(lines[pos[-1]:])
        m = FENCE_RE.search(tail)
        if not m:
            o = OPEN_FENCE_RE.search(tail)
            if o:
                report("ROUND-2", f, pos[-1] + tail[:o.start()].count("\n") + 1, "closing status: fence not closed")
            else:
                report("ROUND-2", f, pos[-1], "closing status carries no fenced status block")
            continue
        fence_line = pos[-1] + tail[:m.start()].count("\n") + 1
        for p in check_status_reply.check(m.group(2)):
            report("ROUND-2", f, fence_line, f"closing status block: {p}")
        if re.search(r"^RUNNING: ", m.group(2), re.M):
            report("ROUND-2", f, fence_line, "closing status names RUNNING; a round that has closed runs nothing")


# ------------------------------------------------------------------ the build

def _expand(root: Path, globs: list[str]) -> list[Path]:
    out: list[Path] = []
    for g in globs:
        out += sorted(p for p in root.glob(g) if p.is_file())
    return out


def check_round_3_build(t: lint_docs.Tree) -> None:
    pub = t.cfg.get("publication", {})
    if not pub.get("enabled"):
        return
    root = t.root
    build = pub.get("build") or "the build"
    sources = _expand(root, pub.get("sources", []))
    if not sources:
        report("ROUND-3", "tools/artifacts.toml", 1, "[publication] enabled but its sources match no file")
        return
    newest_src = max(p.stat().st_mtime for p in sources)
    newest_name = max(sources, key=lambda p: p.stat().st_mtime).relative_to(root)
    for g in pub.get("outputs", []):
        outs = _expand(root, [g])
        if not outs:
            report("ROUND-3", "tools/artifacts.toml", 1, f"no file matches the output {g!r}; run {build}")
        for p in outs:
            if p.stat().st_mtime < newest_src:
                report("ROUND-3", str(p.relative_to(root)), 1, f"output older than {newest_name}; run {build}")
    log = pub.get("log")
    if not log:
        return
    lp = root / log
    if not lp.is_file():
        report("ROUND-3", log, 1, f"build log missing; run {build}")
        return
    if lp.stat().st_mtime < newest_src:
        report("ROUND-3", log, 1, f"build log older than {newest_name}; run {build}")
    try:
        markers = [re.compile(x) for x in pub.get("log_errors", [])]
    except re.error as e:
        report("ROUND-3", "tools/artifacts.toml", 1, f"[publication] log_errors pattern unusable: {e}")
        return
    for i, line in enumerate(lp.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if any(m.search(line) for m in markers):
            report("ROUND-3", log, i, f"build log carries an error marker: {line.strip()[:80]}")
            break


def check_round_4_bibliography(t: lint_docs.Tree) -> None:
    pub = t.cfg.get("publication", {})
    bib = pub.get("bibliography")
    if not pub.get("enabled") or not bib:
        return
    root = t.root
    bp = root / bib
    if not bp.is_file():
        report("ROUND-4", bib, 1, "bibliography named in [publication] does not exist")
        return
    try:
        entry_re, cite_re = re.compile(pub.get("entry", "")), re.compile(pub.get("cite", ""))
    except re.error as e:
        report("ROUND-4", "tools/artifacts.toml", 1, f"[publication] entry or cite pattern unusable: {e}")
        return
    if entry_re.groups < 1 or cite_re.groups < 1:
        report("ROUND-4", "tools/artifacts.toml", 1, "[publication] entry and cite patterns each need a capturing group for the key")
        return
    entries: list[tuple[str, int]] = []
    for i, line in enumerate(bp.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        m = entry_re.search(line)
        if m and m.group(1):
            entries.append((m.group(1), i))
    keys = [k for k, _ in entries]
    seen: set[str] = set()
    for key, i in entries:
        if key in seen:
            report("ROUND-4", bib, i, f"entry {key!r} defined twice")
        seen.add(key)
    # (source, line, column, rank of the source in the configured order) of each key's first citation
    first: dict[str, tuple[str, int, int, int]] = {}
    for rank, p in enumerate(_expand(root, pub.get("sources", []))):
        if p == bp:
            continue
        rel = str(p.relative_to(root))
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for m in cite_re.finditer(line):
                for k, key in enumerate(k.strip() for k in (m.group(1) or "").split(",") if k.strip()):
                    first.setdefault(key, (rel, i, m.start() + k, rank))
    for key, (rel, i, _, _) in first.items():
        if key not in keys:
            report("ROUND-4", rel, i, f"citation of {key!r}, which the bibliography does not carry")
    for key, i in entries:
        if key not in first:
            report("ROUND-4", bib, i, f"entry {key!r} is cited nowhere")
    cited = [k for k in dict.fromkeys(keys) if k in first]
    by_first = sorted(cited, key=lambda k: (first[k][3], first[k][1], first[k][2]))
    for pos, (a, b) in enumerate(zip(cited, by_first), 1):
        if a != b:
            report("ROUND-4", bib, dict(entries)[a], f"entry {a!r} stands at position {pos} but {b!r} is cited first there; the order is first-citation order")
            break


# ------------------------------------------------------------------ running

CHECKS = [check_round_1_numbering, check_round_2_parts, check_round_3_build, check_round_4_bibliography]
ITEMS = ["ROUND-1", "ROUND-2", "ROUND-3", "ROUND-4"]


def run_round(root: Path) -> tuple[lint_docs.Tree, list[tuple[str, str, int, str]]]:
    t = lint_docs.run_checks(root)
    for c in CHECKS:
        c(t)
    return t, list(lint_docs.FINDINGS)


def run(root: Path) -> int:
    try:
        t, found = run_round(root)
    except (OSError, KeyError, ValueError, TypeError, re.error, IndexError) as e:
        print(f"round check: misconfigured: {e}")
        return 2
    for item, path, line, msg in sorted(found):
        print(f"{item:9s} {path}:{line}: {msg}")
    n = len(found)
    pub = "enabled" if t.cfg.get("publication", {}).get("enabled") else "disabled"
    print(f"\nround check: {n} finding(s) over {len(t.files)} files; publication gates {pub}")
    return 1 if n else 0


# ------------------------------------------------------------------ scratch

def write_scratch(target: Path) -> None:
    """The linter's clean fixture plus these tools, in `target`."""
    if target.exists() and any(target.iterdir()):
        raise SystemExit(f"--scratch: {target} exists and is not empty")
    files = lint_docs.fixture()
    tools = sorted(p for p in (ROOT / "tools").iterdir() if p.suffix in (".py", ".sh"))
    rows = "\n".join(f"| [{p.name}]({p.name}) |" for p in [ROOT / "tools" / "artifacts.toml", *tools])
    files["tools/README.md"] = f"# Tools\n\n{lint_docs.STAMP}\n\n| File |\n|---|\n{rows}\n"
    lint_docs.scratch_project(target, files, lint_docs.scratch_config())
    for p in tools:
        shutil.copy2(p, target / "tools" / p.name)


# ------------------------------------------------------------------ selftest

def selftest() -> int:
    cfg_text = lint_docs.scratch_config()
    failures, covered = 0, set()
    S = lint_docs.STAMP
    LOG2 = "prompt_logs/002_next.md"

    def w(tmp: Path, rel: str, body: str) -> None:
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text(body)

    def entry(n: int, name: str, closing: str = "DONE: setup", prompt: str = "x") -> str:
        return (f"# Prompt {n:03d}: {name}\n\n{S}\n\n--- PROMPT START ---\n{prompt}\n--- PROMPT END ---\n\n"
                f"## What was done\n\nSetup.\n\n## Corrections and departures\n\nnone\n\n## Closing status\n\n```\n{closing}\n```\n")

    def index_logs(tmp: Path, files: dict, *names: str) -> None:
        w(tmp, "prompt_logs/README.md", files["prompt_logs/README.md"] + "".join(f"| [{n[:3]}]({n}) |\n" for n in names))

    def second(tmp: Path, files: dict, body: str | None = None, name: str = LOG2) -> None:
        """A fresh, uncommitted, indexed entry: the one ROUND-2 reads."""
        w(tmp, name, body if body is not None else entry(2, "next"))
        index_logs(tmp, files, Path(name).name)

    def enable_publication(tmp: Path, files: dict, stale_output: bool = False, stale_log: bool = False, log_error: bool = False,
                           drop_log: bool = False, bib: str = "@misc{Key1,\n@misc{Key2,\n", cite_text: str = "See [Key1] and [Key2].",
                           extra: tuple[tuple[str, str], ...] = ()) -> None:
        cfg = cfg_text
        for a, b in (("enabled = false", "enabled = true"), ('build = ""', 'build = "make paper"'),
                     ("sources = []", 'sources = ["paper/*.md", "paper/*.bib"]'),
                     ("outputs = []", 'outputs = ["paper/out/main.pdf"]'),
                     ('log = ""', 'log = "paper/out/main.log"'),
                     ("log_errors = []", "log_errors = ['^! ']"),
                     ('bibliography = ""', 'bibliography = "paper/refs.bib"'),
                     ('entry = ""', "entry = '^@\\w+\\{([^,\\s]+),'"),
                     ('cite = ""', "cite = '\\[([A-Z][A-Za-z0-9]{2,31})(?:, [^\\]]*)?\\]'")) + extra:
            # `extra` names the text as rewritten by the pairs above, anchored
            # past the configuration's commented example where the two coincide
            assert cfg.count(a) == 1, a
            cfg = cfg.replace(a, b)
        w(tmp, "tools/artifacts.toml", cfg)
        w(tmp, "paper/refs.bib", bib)
        w(tmp, "paper/README.md", files["paper/README.md"] + "| [refs.bib](refs.bib) |\n| [main_v2.md](main_v2.md) |\n")
        w(tmp, "paper/main_v2.md", f"# Main, second version\n\n{S}\n\nThe write-up [claim 002]. {cite_text}\n")
        w(tmp, "paper/out/main.log", "! Undefined control sequence.\n" if log_error else "Output written on main.pdf.\n")
        (tmp / "paper" / "out" / "main.pdf").write_bytes(b"%PDF-1.4\n")
        newest = max(p.stat().st_mtime for p in [tmp / "paper" / "main_v2.md", tmp / "paper" / "refs.bib"])
        when = newest - 100 if stale_output else newest + 100
        os.utime(tmp / "paper" / "out" / "main.pdf", (when, when))
        when = newest - 100 if stale_log else newest + 100
        os.utime(tmp / "paper" / "out" / "main.log", (when, when))
        if drop_log:
            (tmp / "paper" / "out" / "main.log").unlink()

    def run_case(name: str, item: str, path: str, needle: str, mutate) -> None:
        nonlocal failures
        covered.add(item)
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            files = lint_docs.fixture()
            lint_docs.scratch_project(tmp, files, cfg_text)
            lint_docs.scratch_commit(tmp)
            mutate(tmp, files)
            _, found = run_round(tmp)
            hit = any(x[0] == item and x[1] == path and needle in x[3] for x in found)
            others = sorted({x[0] for x in found if x[0] != item})
            failures += 0 if hit else 1
            print(f"  [{'PASS' if hit else 'FAIL'}] {item:9s} {name}"
                  + (f"   (also: {others})" if others and hit else "")
                  + ("" if hit else f"   (got: {[(x[0], x[1], x[3][:50]) for x in found]})"))

    def clean_case(name: str, mutate, before_commit=None) -> None:
        nonlocal failures
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            files = lint_docs.fixture()
            if before_commit:
                before_commit(files)
            lint_docs.scratch_project(tmp, files, cfg_text)
            lint_docs.scratch_commit(tmp)
            mutate(tmp, files)
            _, found = run_round(tmp)
            failures += 0 if not found else 1
            print(f"  [{'PASS' if not found else 'FAIL'}] {name}"
                  + ("" if not found else f": {[(x[0], x[1], x[3][:50]) for x in found]}"))

    clean_case("the unplanted tree is clean under every enabled gate", lambda t, f: None)
    clean_case("a second, uncommitted, indexed entry keeps the tree clean", lambda t, f: second(t, f))
    clean_case("a prompt that quotes a part heading is not read",
               lambda t, f: second(t, f, entry(2, "next", prompt="pasted:\n## What was done\n## Closing status\n```\nDONE: quoted\n```")))
    clean_case("a fenced example inside a part is not read",
               lambda t, f: second(t, f, entry(2, "next").replace("Setup.", "Setup.\n\n```\n## Corrections and departures\n```")))
    clean_case("a committed entry with a malformed closing status is not re-read", lambda t, f: None,
               before_commit=lambda f: f.__setitem__("prompt_logs/001_setup.md", entry(1, "setup", closing="Done: committed as is")))
    clean_case("a skip list on the entry row is honored",
               lambda t, f: (second(t, f, entry(2, "next", closing="Done: x")),
                             w(t, "tools/artifacts.toml", cfg_text.replace('glob = "prompt_logs/[0-9]*.md"\ngenre = "immutable"',
                                                                            'glob = "prompt_logs/[0-9]*.md"\ngenre = "immutable"\nskip = ["ROUND-2"]'))))
    clean_case("an enabled pipeline with fresh output and a cited, ordered bibliography is clean",
               lambda t, f: enable_publication(t, f))
    run_case("a linter finding passes through under its own tag", "GENRES-1", "MANIFESTO.md", "no header stamp",
             lambda t, f: w(t, "MANIFESTO.md", "# M\n\nRules.\n"))
    run_case("a committed entry edited is the linter's finding", "GENRES-2", "prompt_logs/001_setup.md", "modified",
             lambda t, f: w(t, "prompt_logs/001_setup.md", f["prompt_logs/001_setup.md"] + "\nafterthought\n"))
    run_case("a gap in the numbering", "ROUND-1", "prompt_logs/README.md", "not contiguous",
             lambda t, f: second(t, f, entry(3, "later"), "prompt_logs/003_later.md"))
    run_case("a number used twice", "ROUND-1", "prompt_logs/001_zz_other.md", "used twice",
             lambda t, f: second(t, f, entry(1, "other"), "prompt_logs/001_zz_other.md"))
    run_case("a number not zero-padded", "ROUND-1", "prompt_logs/02_short.md", "zero-padded",
             lambda t, f: second(t, f, entry(2, "short"), "prompt_logs/02_short.md"))
    run_case("an entry numbered 000", "ROUND-1", "prompt_logs/000_zero.md", "starts at 001",
             lambda t, f: second(t, f, entry(0, "zero"), "prompt_logs/000_zero.md"))
    run_case("an entry named by number alone", "ROUND-1", "prompt_logs/002.md", "not of the form",
             lambda t, f: second(t, f, entry(2, "bare"), "prompt_logs/002.md"))
    run_case("a part missing", "ROUND-2", LOG2, "part missing",
             lambda t, f: second(t, f, entry(2, "next").replace("## Corrections and departures\n\nnone\n\n", "")))
    run_case("a delimiter missing", "ROUND-2", LOG2, "part missing: '--- PROMPT END ---'",
             lambda t, f: second(t, f, entry(2, "next").replace("--- PROMPT END ---\n", "")))
    run_case("a part repeated", "ROUND-2", LOG2, "part repeated",
             lambda t, f: second(t, f, entry(2, "next").replace("## What was done\n", "## What was done\n\nx\n\n## What was done\n")))
    run_case("parts out of order", "ROUND-2", LOG2, "out of order",
             lambda t, f: second(t, f, entry(2, "next").replace("## What was done\n\nSetup.\n\n## Corrections and departures\n\nnone\n",
                                                                "## Corrections and departures\n\nnone\n\n## What was done\n\nSetup.\n")))
    run_case("a closing status with no fenced block", "ROUND-2", LOG2, "no fenced",
             lambda t, f: second(t, f, entry(2, "next").replace("```\nDONE: setup\n```\n", "DONE: setup\n")))
    run_case("a closing status whose fence is not closed", "ROUND-2", LOG2, "not closed",
             lambda t, f: second(t, f, entry(2, "next").replace("```\nDONE: setup\n```\n", "```\nDONE: setup\n")))
    run_case("a closing status of the wrong form", "ROUND-2", LOG2, "not a status line",
             lambda t, f: second(t, f, entry(2, "next", closing="Done: setup")))
    run_case("a closing status with IDLE beside DONE", "ROUND-2", LOG2, "IDLE",
             lambda t, f: second(t, f, entry(2, "next", closing="DONE: setup\nIDLE: waiting")))
    run_case("a closing status naming RUNNING", "ROUND-2", LOG2, "RUNNING",
             lambda t, f: second(t, f, entry(2, "next", closing="RUNNING: the build")))
    run_case("a closing status in a tilde fence is read", "ROUND-2", LOG2, "not a status line",
             lambda t, f: second(t, f, entry(2, "next", closing="Done: x").replace("```", "~~~")))
    run_case("an output older than a source", "ROUND-3", "paper/out/main.pdf", "older than",
             lambda t, f: enable_publication(t, f, stale_output=True))
    run_case("a build log older than a source", "ROUND-3", "paper/out/main.log", "older than",
             lambda t, f: enable_publication(t, f, stale_log=True))
    run_case("a build log missing", "ROUND-3", "paper/out/main.log", "build log missing",
             lambda t, f: enable_publication(t, f, drop_log=True))
    run_case("a build log with an error marker", "ROUND-3", "paper/out/main.log", "error marker",
             lambda t, f: enable_publication(t, f, log_error=True))
    run_case("an output missing", "ROUND-3", "tools/artifacts.toml", "no file matches the output",
             lambda t, f: (enable_publication(t, f), (t / "paper" / "out" / "main.pdf").unlink()))
    run_case("sources matching no file", "ROUND-3", "tools/artifacts.toml", "match no file",
             lambda t, f: enable_publication(t, f, extra=(('sources = ["paper/*.md", "paper/*.bib"]', 'sources = ["paper/none/*.md"]'),)))
    run_case("an unusable error-marker pattern", "ROUND-3", "tools/artifacts.toml", "log_errors pattern unusable",
             lambda t, f: enable_publication(t, f, extra=(("log_errors = ['^! ']", "log_errors = ['[']"),)))
    run_case("an entry cited nowhere", "ROUND-4", "paper/refs.bib", "cited nowhere",
             lambda t, f: enable_publication(t, f, bib="@misc{Key1,\n@misc{Key2,\n@misc{Key3,\n"))
    run_case("a citation the bibliography lacks", "ROUND-4", "paper/main_v2.md", "does not carry",
             lambda t, f: enable_publication(t, f, cite_text="See [Key1], [Key2], and [Key9]."))
    run_case("entries out of first-citation order", "ROUND-4", "paper/refs.bib", "first-citation order",
             lambda t, f: enable_publication(t, f, bib="@misc{Key2,\n@misc{Key1,\n"))
    run_case("an entry defined twice", "ROUND-4", "paper/refs.bib", "defined twice",
             lambda t, f: enable_publication(t, f, bib="@misc{Key1,\n@misc{Key2,\n@misc{Key1,\n"))
    run_case("a bibliography that does not exist", "ROUND-4", "paper/none.bib", "does not exist",
             lambda t, f: enable_publication(t, f, extra=(('bibliography = "paper/refs.bib"', 'bibliography = "paper/none.bib"'),)))
    run_case("a cite pattern without a capturing group", "ROUND-4", "tools/artifacts.toml", "capturing group",
             lambda t, f: enable_publication(t, f, extra=(("cite = '\\[([A-Z][A-Za-z0-9]{2,31})(?:, [^\\]]*)?\\]'", "cite = '\\[[A-Z][A-Za-z0-9]{2,31}\\]'"),)))
    run_case("an unusable entry pattern", "ROUND-4", "tools/artifacts.toml", "unusable",
             lambda t, f: enable_publication(t, f, extra=(("\nentry = '^@\\w+\\{([^,\\s]+),'", "\nentry = '('"),)))

    for i in [i for i in ITEMS if i not in covered]:
        failures += 1
        print(f"  [FAIL] {i:9s} exercised by no case")
    print(f"\n  VERDICT: {'every gate shown to fire, and the unplanted tree clean' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if len(argv) == 2 and argv[0] == "--scratch":
        write_scratch(Path(argv[1]).resolve())
        print(f"scratch project written to {argv[1]}")
        return 0
    if argv:
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    return run(ROOT)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

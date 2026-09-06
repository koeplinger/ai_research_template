#!/usr/bin/env python3
"""The privacy scan: a stop-word list that never enters version control, applied to every file, path, and commit message.

Created 5 September 2026; updated 5 September 2026.

Opt-in.  Many projects must keep something out of a public repository
that no rulebook can name in advance: a collaborator, an embargoed topic,
an unreleased dataset, a local path.  The researcher lists those as
patterns in .privacy/stopwords.txt, which .gitignore keeps out of version
control, and this program reports every place a pattern appears: in the
contents of a file, in a file's path, or in a commit message.  Where the
list is absent the scan says so and exits 2; the hooks tools/install_hooks.sh
installs call it only where the list exists.

The list: one pattern per line.  Blank lines and lines beginning with #
are ignored.  A plain line matches as a whole word or phrase, without
regard to case: in contents, letters, digits, and the underscore are the
word characters, so foo_bar is one token; in a path, the underscore, the
hyphen, the dot, and the slash separate words, since file names join words
that way.  A line beginning with ~ matches as a substring anywhere, inside
a longer token included.  A bare ~ or an empty pattern is reported and
ignored.  A file whose first bytes contain a NUL is taken as binary and
its contents are not read; its path still is.  In a commit message, the
lines git strips (those beginning with #) are not read.

Usage
    python3 tools/privacy_scan.py                 the working tree: every tracked or
                                                  untracked-but-not-ignored file
    python3 tools/privacy_scan.py --staged        what is about to be committed: staged
                                                  contents and paths
    python3 tools/privacy_scan.py --message FILE  a commit message
    python3 tools/privacy_scan.py --selftest      a scratch list in a scratch repository,
                                                  every mode exercised; then the project's
                                                  own list, where present, pattern by pattern,
                                                  without printing any of it

Exit status: 0 clean; 1 findings, or a failed self-test; 2 no list, no
repository to list, or a usage error.  A verdict is never given over an
empty listing: where git cannot list the tree, nothing is scanned and the
exit status says so.
"""
from __future__ import annotations

import os
import re
import secrets
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIST = Path(".privacy") / "stopwords.txt"
WORD = r"A-Za-z0-9_"
PATHWORD = r"A-Za-z0-9"


class Patterns:
    """The compiled list: one regex per pattern for contents, one for paths."""

    def __init__(self, path: Path):
        self.content: list[re.Pattern] = []
        self.path: list[re.Pattern] = []
        self.ignored: list[int] = []
        for n, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("~"):
                body = line[1:].strip()
                if not body:
                    self.ignored.append(n)
                    continue
                rx = re.compile(re.escape(body), re.I)
                self.content.append(rx)
                self.path.append(rx)
            else:
                self.content.append(re.compile(rf"(?<![{WORD}])" + re.escape(line) + rf"(?![{WORD}])", re.I))
                self.path.append(re.compile(rf"(?<![{PATHWORD}])" + re.escape(line) + rf"(?![{PATHWORD}])", re.I))

    def __len__(self) -> int:
        return len(self.content)


def git(root: Path, *args: str) -> bytes | None:
    """The command's output, or None where git failed or is absent."""
    try:
        return subprocess.run(["git", *args], cwd=root, capture_output=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def scan_text(label: str, data: bytes, pats: Patterns, skip_comments: bool = False) -> list[tuple[str, str, int, str]]:
    """One tuple per hit: ("CONTENT", label, line, text)."""
    if b"\0" in data[:8192]:
        return []
    out = []
    for i, line in enumerate(data.decode("utf-8", errors="replace").splitlines(), 1):
        if skip_comments and line.startswith("#"):
            continue
        if any(p.search(line) for p in pats.content):
            out.append(("CONTENT", label, i, line.strip()[:120]))
    return out


def scan_name(rel: str, pats: Patterns) -> list[tuple[str, str, int, str]]:
    return [("PATH", rel, 0, "")] if any(p.search(rel) for p in pats.path) else []


def _names(out: bytes) -> list[str]:
    return [os.fsdecode(b) for b in out.split(b"\0") if b]


def scan_tree(root: Path, pats: Patterns) -> tuple[list[tuple[str, str, int, str]] | None, int]:
    out = git(root, "ls-files", "-co", "--exclude-standard", "-z")
    if out is None:
        return None, 0
    findings: list[tuple[str, str, int, str]] = []
    n = 0
    for rel in _names(out):
        findings += scan_name(rel, pats)
        p = root / rel
        if p.is_file():
            n += 1
            findings += scan_text(rel, p.read_bytes(), pats)
    return findings, n


def scan_staged(root: Path, pats: Patterns) -> tuple[list[tuple[str, str, int, str]] | None, int]:
    out = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    if out is None:
        return None, 0
    findings: list[tuple[str, str, int, str]] = []
    names = _names(out)
    for rel in names:
        findings += scan_name(rel, pats)
        blob = git(root, "show", f":{rel}")
        if blob is None:
            findings.append(("UNREAD", rel, 0, "staged content could not be read"))
        else:
            findings += scan_text(rel, blob, pats)
    return findings, len(names)


def format_finding(f: tuple[str, str, int, str]) -> str:
    kind, label, line, text = f
    if kind == "PATH":
        return f"PATH    {label}"
    if kind == "UNREAD":
        return f"UNREAD  {label}: {text}"
    return f"CONTENT {label}:{line}: {text}"


def report(findings: list[tuple[str, str, int, str]], what: str) -> int:
    if findings:
        print(f"privacy scan: FINDINGS ({len(findings)}) in {what}")
        for f in findings:
            print(f"  {format_finding(f)}")
        return 1
    print(f"privacy scan: clean ({what})")
    return 0


def selftest() -> int:
    failures = 0
    # Tokens no shipped text carries, so a project's list is never tripped by
    # the tools themselves; the substring token begins with a letter the
    # others cannot contain.
    word, a, b = ("w" + secrets.token_hex(3) for _ in range(3))
    phrase, sub = f"{a} {b}", "q" + secrets.token_hex(2)

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail})"))

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / ".privacy").mkdir()
        (tmp / ".privacy" / "stopwords.txt").write_text(f"# a scratch list\n\n{word}\n{phrase.upper()}\n~{sub}\n~\n\n")
        (tmp / ".gitignore").write_text(".privacy/\n")
        (tmp / "notes").mkdir()
        (tmp / "notes" / "clean.md").write_text(f"{word}s and {word}_x; nothing else.\n")
        (tmp / "notes" / "word.md").write_text(f"The {word}, once.\n")
        (tmp / "notes" / "phrase.md").write_text(f"Met {phrase} in town.\n")
        (tmp / "notes" / "sub.md").write_text(f"A token like Ab{sub.upper()}cd trips the substring rule.\n")
        (tmp / "notes" / "binary.bin").write_bytes(b"\0\0" + word.encode() + b"\0")
        (tmp / "notes" / f"003_{word}_note.md").write_text("Nothing inside.\n")
        (tmp / "notes" / f"{word}s.md").write_text("Nothing inside either.\n")
        for args in (["init", "-q"], ["add", "-A"]):
            subprocess.run(["git", *args], cwd=tmp, capture_output=True)
        pats = Patterns(tmp / ".privacy" / "stopwords.txt")
        case("three patterns loaded and the bare ~ set aside", len(pats) == 3 and pats.ignored == [6], f"{len(pats)} {pats.ignored}")
        f, n = scan_tree(tmp, pats)
        hits = {x[1] for x in f}
        case("a whole word is caught", "notes/word.md" in hits, str(f))
        case("a phrase is caught without regard to case", "notes/phrase.md" in hits, str(f))
        case("a substring is caught inside a token", "notes/sub.md" in hits, str(f))
        case("a word joined by underscores in a path is caught", f"notes/003_{word}_note.md" in hits, str(f))
        case("a longer word in a path is not the word", f"notes/{word}s.md" not in hits, str(f))
        case("a longer word, or one joined by an underscore, is not the word in contents", "notes/clean.md" not in hits, str(f))
        case("a binary file's contents are not read", not any(x[0] == "CONTENT" and x[1] == "notes/binary.bin" for x in f), str(f))
        case("the tree scan counts its files", n == 8, str(n))
        f2, _ = scan_staged(tmp, pats)
        case("the staged scan sees the same hits", {x[1] for x in f2} == hits, str(f2))
        msg = tmp / "msg"
        msg.write_text(f"add the {word} note\n")
        case("a commit message is caught", bool(scan_text("commit message", msg.read_bytes(), pats, skip_comments=True)))
        msg.write_text(f"add the note\n# Changes to be committed:\n#\tnew file: {word}.md\n")
        case("git's comment lines in a message are not read", not scan_text("commit message", msg.read_bytes(), pats, skip_comments=True))
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / "x.md").write_text(word)
        f, n = scan_tree(tmp, pats)
        case("a directory git cannot list gives no verdict", f is None and n == 0, str((f, n)))

    own = ROOT / LIST
    if own.exists():
        pats = Patterns(own)
        raw = [l.strip() for l in own.read_text(encoding="utf-8", errors="replace").splitlines()
               if l.strip() and not l.strip().startswith("#") and l.strip() != "~"]
        silent, broad = 0, 0
        for line, pat in zip(raw, pats.content):
            if line.startswith("~"):
                if not pat.search(f"lorem Xx{line[1:].strip()}Yy ipsum"):
                    silent += 1
            else:
                if not pat.search(f"lorem {line} ipsum"):
                    silent += 1
                if pat.search(f"lorem X{line}Y ipsum"):
                    broad += 1
        case("the project's own list: each pattern shown to fire", silent == 0, f"{silent} silent")
        case("the project's own list: no whole-word pattern matches inside a longer token", broad == 0, f"{broad} broad")
    else:
        print(f"  [SKIP] no project list at {LIST}; the scratch list stood in")
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if argv and not (argv == ["--staged"] or (len(argv) == 2 and argv[0] == "--message")):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    path = ROOT / LIST
    if not path.exists():
        print(f"privacy scan: no stop-word list at {LIST}; create it to opt in (it is git-ignored)")
        return 2
    pats = Patterns(path)
    for n in pats.ignored:
        print(f"privacy scan: line {n} of {LIST} is a bare ~; ignored", file=sys.stderr)
    if not len(pats):
        print(f"privacy scan: the list at {LIST} holds no pattern")
        return 2
    if not argv:
        findings, n = scan_tree(ROOT, pats)
        what = f"working tree, {n} files"
    elif argv[0] == "--staged":
        findings, n = scan_staged(ROOT, pats)
        what = f"staged content and paths, {n} files"
    else:
        if not Path(argv[1]).is_file():
            print("privacy scan: --message needs a readable file", file=sys.stderr)
            return 2
        return report(scan_text("commit message", Path(argv[1]).read_bytes(), pats, skip_comments=True), "commit message")
    if findings is None:
        print("privacy scan: git could not list the tree (not a repository, or git absent); nothing scanned")
        return 2
    return report(findings, what)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

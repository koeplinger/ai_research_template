#!/usr/bin/env python3
"""The residue check: what a rebuild or a correction batch leaves behind in a live draft, listed for the reading that closes the round.

Created 5 September 2026; updated 5 September 2026.

No rulebook lists these as checked mechanically.  CHECK_METHODOLOGY.md
section 7 makes a rebuild's duties reading ("a rebuild round therefore
ends with a reading of the whole file") and names what a section-level
comparison drops: a cross-reference whose target lay inside the replaced
range, a sentence's antecedent, a phrase that reads as a citation and
resolves to nothing.  This program lists, on every live draft under the
write-up folder and, where [publication] is enabled, on its LaTeX
sources, what such a reading should not miss; a line here is a candidate
for the reader, never a verdict.  Optional: a project that keeps no live
draft in these forms has nothing for it to read.  It honors a row's
`skip` list, like the linter.

  RESIDUE-1  seams: a section with nothing under it before the next
             heading of its own level or higher, two identical adjacent
             paragraphs, a paragraph that opens in the middle of a sentence
  RESIDUE-2  dangling references: a reference to a label, heading anchor,
             or footnote that no longer exists; labels are pooled across
             every LaTeX source
  RESIDUE-3  orphaned references: a label or footnote nothing refers to
  RESIDUE-4  phantoms: a bare numeric citation, or a "Section N", "Table
             N", "Figure N", or "Equation (N)" beyond what the draft has,
             read outside citation tokens, links, and quotations
  RESIDUE-5  echoes: a sentence of eight words or more that appears twice,
             in one paragraph, one draft, or across the live drafts
  RESIDUE-6  structure: a heading level that skips, a heading title that
             repeats (reported at the repeat), an explicit heading number
             out of sequence
  RESIDUE-7  the ledgers of a live changelog against the draft it
             describes (paper/_template_changelog.md): a cut sentence
             classed decoration or content still in the draft, a cut
             restatement not fewer than before, an added sentence not in
             the draft, a stated net word delta that does not match the
             body words of the two versions; the versions are found by
             `_vN` before the extension, as paper/README.md fixes

A markdown draft is read through the linter's prose view (comments,
fences, and backtick spans blank); a LaTeX source (.tex) named by the
[publication] sources is read from the linter's file walk with its %
comments blank, every source the globs match, since a typeset file
carries no header from which live or frozen could be derived.  The
Ontology's citation tokens are the linter's and are not read here.

Usage
    python3 tools/check_residue.py             every live draft
    python3 tools/check_residue.py --selftest

Exit status: 0 nothing listed; 1 something listed; 2 tools/artifacts.toml
unreadable, or a usage error.
"""
from __future__ import annotations

import re
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MIN_WORDS = 8
ABBREV = re.compile(r"\b(et al|Fig|Figs|Eq|Eqs|cf|e\.g|i\.e|vs|No|Nos|pp?|Vol|ch|Dr|Mr|Mrs|Ms|Prof|St)\.", re.I)
TEX_HEAD = re.compile(r"\\(part|chapter|section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?\{([^}]*)\}")
TEX_REF = re.compile(r"\\(?:eq|page|auto|c|C|v|name)?ref\*?\{([^}]*)\}|\\hyperref\[([^\]]*)\]")
TEX_LABEL = re.compile(r"\\label\{([^}]*)\}")


class Draft:
    def __init__(self, t: lint_docs.Tree, path: str, kind: str):
        self.path, self.kind = path, kind
        if kind == "md":
            self.text = t.prose(path)
            self.raw = t.text[path]
            self.titles = t.prose(path, keep_backticks=True)
            self.body_start = t.headers[path][1]
        else:
            raw = t.text[path]
            self.text = re.sub(r"(?<!\\)%[^\n]*", lambda m: " " * len(m.group(0)), raw)
            self.raw, self.titles, self.body_start = raw, self.text, 1
        self.lines = self.text.splitlines()


def drafts_of(t: lint_docs.Tree) -> list[Draft]:
    out = []
    paper = t.dir_of_kind("version")
    for f, row in t.rows.items():
        if row and paper and f.startswith(paper + "/") and row["kind"] in ("version", "companion") \
                and t.genre(f) == "current-state" and not t.is_template(f):
            out.append(Draft(t, f, "md"))
    pub = t.cfg.get("publication", {})
    if pub.get("enabled"):
        for g in pub.get("sources", []):
            for f in t.files:
                if lint_docs.match(g, f) and f.endswith(".tex"):
                    out.append(Draft(t, f, "tex"))
    return out


def paragraphs(d: Draft) -> list[tuple[int, list[str]]]:
    """(first line, the lines) of each non-empty paragraph."""
    out, start, buf = [], None, []
    for i, line in enumerate(d.lines + [""], 1):
        if line.strip():
            if start is None:
                start = i
            buf.append(line)
        elif buf:
            out.append((start, buf))
            start, buf = None, []
    return out


def headings(d: Draft) -> list[tuple[int, int, str]]:
    """(line, level, title), the title with backticks kept for anchoring."""
    out = []
    for i, line in enumerate(d.titles.splitlines(), 1):
        if d.kind == "md":
            m = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
            if m:
                out.append((i, len(m.group(1)), m.group(2)))
        else:
            m = TEX_HEAD.search(line)
            if m:
                out.append((i, ("part", "chapter", "section", "subsection", "subsubsection", "paragraph").index(m.group(1)), m.group(2)))
    return out


def anchor(title: str) -> str:
    return re.sub(r"[^\w -]", "", title.replace("`", "").lower()).strip().replace(" ", "-")


def check_seams(d: Draft) -> None:
    hs = headings(d)
    for k, (ln, lvl, title) in enumerate(hs):
        nxt = next((h[0] for h in hs[k + 1:] if h[1] <= lvl), len(d.lines) + 1)
        if not any(l.strip() for l in d.lines[ln:nxt - 1]):
            lint_docs.report("RESIDUE-1", d.path, ln, f"empty section: {title!r}")
    paras = [(ln, " ".join(l.strip() for l in ls)) for ln, ls in paragraphs(d)]
    for (a_ln, a), (b_ln, b) in zip(paras, paras[1:]):
        if a == b and len(a.split()) >= 3:
            lint_docs.report("RESIDUE-1", d.path, b_ln, "paragraph repeats the one before it")
    raw_lines = d.raw.splitlines()
    for ln, p in paras:
        first_raw = raw_lines[ln - 1].lstrip() if ln - 1 < len(raw_lines) else ""
        if re.match(r"^[a-z]", p) and not first_raw.startswith("`"):
            lint_docs.report("RESIDUE-1", d.path, ln, f"paragraph opens in the middle of a sentence: {p[:60]!r}")


def tex_labels(d: Draft) -> tuple[dict[str, int], dict[str, int]]:
    labels = {m.group(1): i for i, l in enumerate(d.lines, 1) for m in TEX_LABEL.finditer(l)}
    refs: dict[str, int] = {}
    for i, l in enumerate(d.lines, 1):
        for m in TEX_REF.finditer(l):
            for key in (m.group(1) or m.group(2) or "").split(","):
                refs.setdefault(key.strip(), i)
    return labels, refs


def check_references(drafts: list[Draft]) -> None:
    tex = [d for d in drafts if d.kind == "tex"]
    if tex:
        pooled = {k for d in tex for k in tex_labels(d)[0]}
        referenced = {k for d in tex for k in tex_labels(d)[1]}
        for d in tex:
            labels, refs = tex_labels(d)
            for key, i in refs.items():
                if key not in pooled:
                    lint_docs.report("RESIDUE-2", d.path, i, f"reference to a label that does not exist in any source: {key!r}")
            for key, i in labels.items():
                if key not in referenced:
                    lint_docs.report("RESIDUE-3", d.path, i, f"label nothing refers to: {key!r}")
    for d in drafts:
        if d.kind != "md":
            continue
        anchors = {anchor(title) for _, _, title in headings(d)}
        for i, l in enumerate(d.lines, 1):
            for m in re.finditer(r"\]\(#([^)]+)\)", l):
                if m.group(1) not in anchors:
                    lint_docs.report("RESIDUE-2", d.path, i, f"link to a heading that does not exist: #{m.group(1)}")
        defined = {m.group(1): i for i, l in enumerate(d.lines, 1) for m in [re.match(r"^\[\^([^\]]+)\]:", l)] if m}
        used: dict[str, int] = {}
        for i, l in enumerate(d.lines, 1):
            for m in re.finditer(r"\[\^([^\]]+)\](?!:)", l):
                used.setdefault(m.group(1), i)
                if m.group(1) not in defined:
                    lint_docs.report("RESIDUE-2", d.path, i, f"footnote used and not defined: [^{m.group(1)}]")
        for key, i in defined.items():
            if key not in used:
                lint_docs.report("RESIDUE-3", d.path, i, f"footnote defined and never used: [^{key}]")


def check_phantoms(d: Draft) -> None:
    if d.kind == "md":
        sections = sum(1 for _, lvl, _ in headings(d) if lvl == 2)
        tables = len(re.findall(r"(?im)^\s*(?:\*{1,2}|_{1,2})?Table \d+", d.text))
        figures = len(re.findall(r"(?im)^\s*(?:\*{1,2}|_{1,2}|!\[)?Figure \d+", d.text))
        equations = len(re.findall(r"\(\d+\)\s*$", d.text, re.M))
        text = lint_docs.blank_quoted(d.text)
    else:
        sections = len(re.findall(r"\\section\*?(?:\[[^\]]*\])?\{", d.text))
        tables = len(re.findall(r"\\begin\{table", d.text))
        figures = len(re.findall(r"\\begin\{figure", d.text))
        equations = len(re.findall(r"\\begin\{(?:equation|align|gather)", d.text))
        text = d.text
    have = {"Section": sections, "Table": tables, "Figure": figures, "Equation": equations}
    for i, l in enumerate(text.splitlines(), 1):
        l2 = lint_docs.TOKEN_KEY.sub(" ", lint_docs.LINK_RE.sub(" ", l))
        if d.kind == "md":
            for m in re.finditer(r"(?<![\w\[\]])\[(\d{1,3})\](?![\(\[\w:])", l2):
                lint_docs.report("RESIDUE-4", d.path, i, f"bare numeric citation [{m.group(1)}] resolves to nothing the record reads")
        for m in re.finditer(r"\b(Section|Table|Figure|Equation)s?\s+\(?(\d+)(?:\.\d+)*\)?", l2):
            n = int(m.group(2))
            if n > have[m.group(1)]:
                lint_docs.report("RESIDUE-4", d.path, i, f"{m.group(0).strip()!r} names more than the draft has ({have[m.group(1)]} {m.group(1).lower()}(s) counted); a candidate for reading")


def sentences(d: Draft) -> list[tuple[int, str]]:
    """(line, sentence) for every sentence of eight words or more, the
    line the one holding the sentence's first word."""
    out = []
    for start, ls in paragraphs(d):
        if re.match(r"^\s*(#|\||\\|\[\^)", ls[0]):
            continue
        offsets, pos = [], 0
        for k, l in enumerate(ls):
            offsets.append((pos, start + k))
            pos += len(l) + 1
        joined = ABBREV.sub(lambda m: m.group(0).replace(".", "\0"), "\n".join(ls))
        joined = re.sub(r"(\d)\.(\d)", "\\1\0\\2", joined)
        for m in re.finditer(r"[^.!?]*[.!?]", joined):
            s = " ".join(m.group(0).replace("\0", ".").split())
            if len(s.split()) >= MIN_WORDS:
                first = m.start() + len(m.group(0)) - len(m.group(0).lstrip())
                line = max(ln for off, ln in offsets if off <= first)
                out.append((line, s))
    return out


def check_echoes(drafts: list[Draft]) -> None:
    seen: dict[str, tuple[str, int]] = {}
    for d in drafts:
        for ln, s in sentences(d):
            key = s.lower()
            if key in seen:
                g, gl = seen[key]
                lint_docs.report("RESIDUE-5", d.path, ln, f"sentence also at {g}:{gl}: {s[:80]!r}")
            else:
                seen[key] = (d.path, ln)


def check_structure(d: Draft) -> None:
    hs = headings(d)
    seen: set[str] = set()
    last_level, last_num = None, None
    for ln, lvl, title in hs:
        if last_level is not None and lvl > last_level + 1:
            lint_docs.report("RESIDUE-6", d.path, ln, f"heading level skips from {last_level} to {lvl}: {title!r}")
        last_level = lvl
        a = anchor(title)
        if a in seen:
            lint_docs.report("RESIDUE-6", d.path, ln, f"heading title repeats: {title!r}")
        seen.add(a)
        m = re.match(r"^(\d+)\.?\s", title)
        if m and lvl == 2:
            n = int(m.group(1))
            if last_num is not None and n != last_num + 1:
                lint_docs.report("RESIDUE-6", d.path, ln, f"heading number {n} follows {last_num}")
            last_num = n


def normalize(s: str) -> str:
    s = re.sub(r"[*_`]", "", s)
    s = s.strip().strip("\"'“”‘’").strip()
    return " ".join(s.split()).lower().rstrip(".!?")


def body_words(t: lint_docs.Tree, f: str) -> int:
    lines = t.prose(f).splitlines()[t.headers[f][1] - 1:]
    return sum(len(re.findall(r"\w+", l)) for l in lines if not re.match(r"^\s*(#|\|)", l))


def check_ledgers(t: lint_docs.Tree) -> None:
    paper = t.dir_of_kind("changelog")
    for f, row in t.rows.items():
        if not row or row["kind"] != "changelog" or t.genre(f) != "current-state" or t.is_template(f):
            continue
        m = re.search(r"v(\d+)_to_v(\d+)", Path(f).name)
        if not m:
            continue

        def version(n: str) -> str | None:
            return next((g for g in t.files if g.startswith(paper + "/") and re.search(rf"_v{n}\.[^.]+$", Path(g).name) and t.kind(g) == "version"), None)

        old, new = version(m.group(1)), version(m.group(2))
        if not new:
            lint_docs.report("RESIDUE-7", f, 1, f"no version named *_v{m.group(2)}.<ext> under {paper}/ to read the ledgers against")
            continue
        draft = normalize(t.prose(new))
        old_text = normalize(t.prose(old)) if old else ""
        text = t.prose(f)
        section = None
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("## "):
                section = line.lower()
                continue
            if not line.startswith("|") or set(line) <= set("|- "):
                continue
            cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
            if not cells or not cells[0]:
                continue
            if section and "deletion" in section and normalize(cells[0]) != normalize("Cut sentence or display"):
                cut, cls = normalize(cells[0]), (cells[1].lower() if len(cells) > 1 else "")
                if not cut:
                    continue
                if cls.startswith("restatement"):
                    if draft.count(cut) >= old_text.count(cut) and draft.count(cut):
                        lint_docs.report("RESIDUE-7", f, i, f"cut restatement is not fewer in {new} than in {old or 'the previous version'}: {cells[0][:60]!r}")
                elif cut in draft:
                    lint_docs.report("RESIDUE-7", f, i, f"cut sentence ({cls or 'unclassed'}) still in {new}: {cells[0][:60]!r}")
            elif section and "additions" in section and len(cells) > 1 and normalize(cells[0]) != "section":
                added = normalize(cells[1])
                if added and added not in draft:
                    lint_docs.report("RESIDUE-7", f, i, f"added sentence not in {new}: {cells[1][:60]!r}")
        d = re.search(r"^Net word delta:\s*([+-]?\d+)\s*$", text, re.M)
        if d and old:
            actual = body_words(t, new) - body_words(t, old)
            if int(d.group(1)) != actual:
                lint_docs.report("RESIDUE-7", f, text[:d.start()].count("\n") + 1, f"stated net word delta {d.group(1)}; counting body words of the prose view, headings and tables aside, {new} has {actual:+d} against {old}")


def residue(t: lint_docs.Tree) -> int:
    drafts = drafts_of(t)
    for d in drafts:
        check_seams(d)
        check_phantoms(d)
        check_structure(d)
    check_references(drafts)
    check_echoes(drafts)
    check_ledgers(t)
    return len(drafts)


def run(root: Path) -> int:
    try:
        t = lint_docs.use(lint_docs.Tree(root, lint_docs.load_config(root)))
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"check_residue: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    n = residue(t)
    for item, path, line, msg in sorted(lint_docs.FINDINGS):
        print(f"{item:9s} {path}:{line}: {msg}")
    k = len(lint_docs.FINDINGS)
    print(f"\nresidue: {n} live draft(s) read, {k} candidate(s) for the reader")
    return 1 if k else 0


def selftest() -> int:
    failures = 0
    S = lint_docs.STAMP
    V2, CL = "paper/main_v2.md", "paper/v1_to_v2_changelog.md"
    ITEMS = [f"RESIDUE-{i}" for i in range(1, 8)]
    covered: set[str] = set()
    LONG = "The write-up [claim 002], with a sentence long enough to count as one of eight words."

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:500]})"))

    def run_on(mutate, lint: bool = False, cfg: str | None = None):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            files = lint_docs.fixture()
            files[V2] = f"# Main, second version\n\n{S}\n\n## Question\n\n{LONG}\n\n### Detail\n\nOf it.\n\n## Answer\n\nIt holds. It holds.\n"
            files["paper/README.md"] += "| [main_v2.md](main_v2.md) |\n"
            mutate(files)
            lint_docs.scratch_project(tmp, files, cfg or lint_docs.scratch_config())
            lint_docs.scratch_commit(tmp)
            if lint:
                lint_docs.run_checks(tmp)
                case("the scratch tree with a live draft is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:3]))
            t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
            residue(t)
            return list(lint_docs.FINDINGS)

    def planted(name: str, item: str, path: str, needle: str, mutate, line: int | None = None) -> None:
        covered.add(item)
        f = run_on(mutate)
        case(name, any(x[0] == item and x[1] == path and needle in x[3] and (line is None or x[2] == line) for x in f), str(f))

    def add(rel: str, extra: str):
        return lambda files: files.__setitem__(rel, files[rel] + extra)

    f = run_on(lambda files: None, lint=True)
    case("a clean live draft with a subsection lists nothing", not f, str(f))
    case("a frozen version is not read", not any(x[1] == "paper/main_v1.md" for x in run_on(add("paper/main_v1.md", "\n## Empty\n"))))
    planted("an empty section", "RESIDUE-1", V2, "empty section: 'Nothing here'", add(V2, "\n## Nothing here\n\n## After\n\nText.\n"))
    planted("a paragraph repeating the one before", "RESIDUE-1", V2, "repeats the one before", add(V2, "\nOne two three.\n\nOne two three.\n"))
    planted("a paragraph opening mid-sentence", "RESIDUE-1", V2, "middle of a sentence", add(V2, "\nwhich was left behind by the cut.\n"))
    case("a paragraph opening with a code span is not a seam", not any(x[0] == "RESIDUE-1" for x in run_on(add(V2, "\n`base` is the module.\n"))))
    planted("a link to a heading that does not exist", "RESIDUE-2", V2, "does not exist: #gone", add(V2, "\nSee [above](#gone).\n"))
    case("a link to a heading with a code span or an underscore resolves", not any(x[0] == "RESIDUE-2" for x in run_on(add(V2, "\n## The `foo()` function\n\nA.\n\n## the_variable\n\nB. See [it](#the-foo-function) and [that](#the_variable).\n"))))
    planted("a footnote used and not defined", "RESIDUE-2", V2, "used and not defined", add(V2, "\nA point.[^9]\n"))
    planted("a footnote defined and never used", "RESIDUE-3", V2, "never used", add(V2, "\n[^7]: A note.\n"))
    planted("a bare numeric citation", "RESIDUE-4", V2, "bare numeric citation [12]", add(V2, "\nAs shown in [12].\n"))
    case("a reference-style link is not a bare citation", not any(x[0] == "RESIDUE-4" for x in run_on(add(V2, "\nAs shown in [text][12].\n\n[12]: https://example.org/\n"))))
    planted("a section number beyond the draft's", "RESIDUE-4", V2, "'Section 7' names more", add(V2, "\nSee Section 7.\n"))
    planted("a table number beyond the draft's", "RESIDUE-4", V2, "'Table 2' names more", add(V2, "\n*Table 1.* Counts.\n\nSee Table 2.\n"))
    planted("a figure number beyond the draft's", "RESIDUE-4", V2, "'Figure 3' names more", add(V2, "\nSee Figure 3.\n"))
    planted("an equation number beyond the draft's", "RESIDUE-4", V2, "'Equation (4)' names more", add(V2, "\nBy Equation (4).\n"))
    case("a section named in a citation locus or a quotation is not a phantom", not any(x[0] == "RESIDUE-4" for x in run_on(add(V2, "\nSee [Key1, Section 12] and \"Section 9 is unclear\".\n"))))
    planted("a sentence appearing twice in one draft", "RESIDUE-5", V2, "sentence also at", add(V2, f"\n{LONG}\n"))
    planted("a sentence appearing twice in one paragraph", "RESIDUE-5", V2, "sentence also at", add(V2, "\nThis sentence has enough words to be counted here. This sentence has enough words to be counted here.\n"))
    f = run_on(lambda files: (files.__setitem__("paper/note_v1.md", f"# Note\n\n{S}\n\n{LONG}\n"), files.__setitem__("paper/README.md", files["paper/README.md"] + "| [note_v1.md](note_v1.md) |\n")))
    case("an echo across two live drafts is listed with the twin's line", any(x[0] == "RESIDUE-5" and "main_v2.md:7" in x[3] for x in f), str(f))
    case("two sentences sharing a tail after an abbreviation are not echoes", not any(x[0] == "RESIDUE-5" for x in run_on(add(V2, "\nSmith et al. show that the count is one for every cohort studied. Jones et al. show that the count is one for every cohort studied here.\n"))))
    planted("a heading level that skips", "RESIDUE-6", V2, "level skips", add(V2, "\n##### Deep\n\nText.\n"))
    planted("a heading title that repeats, at the repeat", "RESIDUE-6", V2, "title repeats", add(V2, "\n## Answer\n\nAgain.\n"), line=17)
    planted("a heading number out of sequence", "RESIDUE-6", V2, "number 3 follows 1", add(V2, "\n## 1. First\n\nA.\n\n## 3. Third\n\nB.\n"))
    ledger = "\n## The deletion ledger\n\n| Cut sentence or display | Class | Where the statement now lives |\n|---|---|---|\n| *It holds.* | decoration | nowhere |\n| It holds | restatement | section 2 |\n\n## The additions ledger\n\nNet word delta: +99\n\n| Section | Sentence added | Why |\n|---|---|---|\n| 2 | A sentence that was never added. | review |\n"
    planted("a cut decoration still in the draft, emphasis and period aside", "RESIDUE-7", CL, "cut sentence (decoration) still in", add(CL, ledger))
    planted("a cut restatement not fewer than before", "RESIDUE-7", CL, "cut restatement is not fewer", add(CL, ledger))
    planted("an added sentence not in the draft", "RESIDUE-7", CL, "added sentence not in", add(CL, ledger))
    planted("a stated net word delta that does not match", "RESIDUE-7", CL, "stated net word delta +99", add(CL, ledger))

    def ok_ledger(files):
        def words(text):
            body = lint_docs.strip_unread(text).splitlines()[lint_docs.header_block(text, "stamp")[1] - 1:]
            return sum(len(re.findall(r"\w+", l)) for l in body if not re.match(r"^\s*(#|\|)", l))
        files[V2] = files[V2].replace("It holds. It holds.", "It holds.")
        files["paper/main_v1.md"] = files["paper/main_v1.md"].replace("The write-up [claim 002].", "The write-up [claim 002]. The write-up [claim 002].")
        delta = words(files[V2]) - words(files["paper/main_v1.md"])
        files[CL] += f"\n## The deletion ledger\n\n| Cut sentence or display | Class | Where the statement now lives |\n|---|---|---|\n| Gone for good. | decoration | nowhere |\n| The write-up | restatement | section 1 |\n\n## The additions ledger\n\nNet word delta: {delta:+d}\n\n| Section | Sentence added | Why |\n|---|---|---|\n| 2 | It holds. | review |\n"
    f = run_on(ok_ledger)
    case("ledgers that agree with the draft list nothing (a restatement fewer than before)", not any(x[0] == "RESIDUE-7" for x in f), str(f))
    planted("a changelog with no version to read against", "RESIDUE-7", "paper/v2_to_v3_changelog.md", "no version named *_v3",
            lambda files: (files.__setitem__("paper/v2_to_v3_changelog.md", f"# Changelog: v2 to v3\n\n{S}\n\n| Where in vN | What changed in vM | Why | Backed by |\n|---|---|---|---|\n"),
                           files.__setitem__("paper/README.md", files["paper/README.md"] + "| [v2_to_v3_changelog.md](v2_to_v3_changelog.md) |\n")))
    companion_cfg = lint_docs.scratch_config().replace('# [[artifact]]\n# kind = "companion"\n# glob = "paper/reading_companion.md"\n# genre = "current-state"',
                                                        '[[artifact]]\nkind = "companion"\nglob = "paper/reading_companion.md"\ngenre = "current-state"')
    assert companion_cfg != lint_docs.scratch_config()
    f = run_on(lambda files: (files.__setitem__("paper/reading_companion.md", f"# Companion\n\n{S}\n\n{LONG}\n"), files.__setitem__("paper/README.md", files["paper/README.md"] + "| [reading_companion.md](reading_companion.md) |\n")), cfg=companion_cfg)
    case("a maintained companion under the write-up folder is read", any(x[0] == "RESIDUE-5" and x[1] == "paper/reading_companion.md" for x in f), str(f))
    tex_cfg = lint_docs.scratch_config().replace("enabled = false", "enabled = true").replace("sources = []", 'sources = ["paper/*.tex"]')

    def tex(files):
        files["paper/main.tex"] = "\\section[One]{One}\\label{sec:one}\nSee \\ref{sec:gone}, \\ref{sec:intro}, and Section 4. % \\ref{sec:comment}\n% \\ref{sec:comment2}\n\\section{Two}\\label{sec:two}\nText.\n\nleft behind.\n"
        files["paper/intro.tex"] = "\\section{Intro}\\label{sec:intro}\nSee \\ref{sec:one}.\n"
        files["paper/README.md"] += "| [main.tex](main.tex) |\n| [intro.tex](intro.tex) |\n"
    f = run_on(tex, lint=True, cfg=tex_cfg)
    case("a LaTeX source with the pipeline enabled: a reference to no label in any source", any(x[0] == "RESIDUE-2" and x[1] == "paper/main.tex" and "sec:gone" in x[3] for x in f), str(f))
    case("a LaTeX source: a label referenced from another source is not orphaned, one nothing refers to is", any(x[0] == "RESIDUE-3" and "sec:two" in x[3] for x in f) and not any("sec:intro" in x[3] or "sec:one" in x[3] for x in f), str(f))
    case("a LaTeX source: a section number beyond the count", any(x[0] == "RESIDUE-4" and "'Section 4' names more" in x[3] for x in f), str(f))
    case("a LaTeX source: a comment, trailing or whole-line, is not read", not any("sec:comment" in x[3] for x in f), str(f))
    case("a LaTeX source: a seam", any(x[0] == "RESIDUE-1" and x[1] == "paper/main.tex" and "middle of a sentence" in x[3] for x in f), str(f))
    for i in [i for i in ITEMS if i not in covered]:
        failures += 1
        print(f"  [FAIL] {i:9s} exercised by no case")
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if argv:
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    return run(ROOT)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""The concordance check: a check program's RESULT line against its record (CHECK_METHODOLOGY.md, What is checked mechanically, item 4).

Created 5 September 2026; updated 5 September 2026.

A check program ends with one line on standard output,
RESULT: <verdict>; <name>=<value>; ..., and its check record states the
same named values under its part 4, one per line as name = value, exactly
as printed.  This program runs every check program (or the one named),
takes the last RESULT line on its standard output, and reports under
CHECK-4 every disagreement: a value that differs, a name printed and not
stated, a name stated and not printed, a program that prints no RESULT
line, and a program with no record.  It honors a row's `skip` list, every
artifact the row matches, like the linter.  Each program runs with the
interpreter running this tool, from the parent of the configured
check-program directory, which is how python_project/README.md, Running,
says a check is run.  Comments, fenced code, and backtick spans under
part 4 are not read.

WHAT IT DOES NOT DECIDE.  A written check procedure has no program and
nothing to run: it is listed as such and not compared.  The verdict word
is printed beside the backed claim's Verdict, marked where the words
differ, never a finding: who assigns the register and its verdict is
CHECK_METHODOLOGY.md section 1's.  Single-sourcing a figure across
documents, and the wrong value stated in a passage about the right
subject, are reading duties of the sweep (CHECK_METHODOLOGY.md section
7, item 1).  A program that exits nonzero, prints more than one RESULT
line, or prints a RESULT part without "=" is noted and still compared.

Usage
    python3 tools/check_concordance.py                run every check program, compare
    python3 tools/check_concordance.py --only NNN     one check
    python3 tools/check_concordance.py --timeout S    seconds per program (default 600)
    python3 tools/check_concordance.py --selftest

Exit status: 0 no disagreement; 1 a disagreement; 2 an unknown check
number, a usage error, or tools/artifacts.toml unreadable.
"""
from __future__ import annotations

import contextlib
import io
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RESULT_RE = re.compile(r"^RESULT:\s*(.*?)\s*$", re.M)
VALUE_LINE = re.compile(r"^\s*-?\s*([A-Za-z_][\w.\-]*)\s*=\s*(.+?)\s*$")


def parse_result(line: str) -> tuple[str, dict[str, str], list[str]]:
    """(verdict, {name: value}, parts carrying no '=')."""
    parts = [p.strip() for p in line.split(";")]
    verdict, values, dropped = parts[0], {}, []
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            values[k.strip()] = v.strip()
        elif p:
            dropped.append(p)
    return verdict, values, dropped


def record_values(prose: str) -> tuple[int, dict[str, tuple[int, str]]] | None:
    """(line of the part-4 heading, {name: (line, value)}); None where the
    record has no part 4.  Read from the prose view, so comments, fences,
    and backtick spans are blank."""
    lines = prose.splitlines()
    start = next((i for i, l in enumerate(lines, 1) if re.match(r"^## 4\.", l)), None)
    if start is None:
        return None
    out: dict[str, tuple[int, str]] = {}
    for j in range(start, len(lines)):
        if re.match(r"^## ", lines[j]):
            break
        v = VALUE_LINE.match(lines[j])
        if v:
            out[v.group(1)] = (j + 1, v.group(2))
    return start, out


def run_program(root: Path, prog: str, cwd: Path, timeout: float) -> tuple[list[str], str]:
    """(every RESULT line on standard output, how the run ended).  The
    program runs unbuffered, so what it printed before a timeout is kept."""
    try:
        p = subprocess.run([sys.executable, "-u", str(root / prog)], cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode("utf-8", errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return RESULT_RE.findall(out), f"did not finish (timed out after {timeout:g} s)"
    return RESULT_RE.findall(p.stdout), ("" if p.returncode == 0 else f"exited {p.returncode}")


def concordance(t: lint_docs.Tree, timeout: float, only: str | None = None) -> tuple[list[str], int, int]:
    """Findings go through lint_docs.report; returns (notes, programs run, written procedures)."""
    notes, ran, written = [], 0, 0
    cwd = t.root / Path(t.dir_of_kind("check-program")).parent if t.programs else t.root
    for num, prog in sorted(t.programs.items()):
        if only and num != only:
            continue
        ran += 1
        rec = t.checks.get(num)
        results, ended = run_program(t.root, prog, cwd, timeout)
        if ended:
            notes.append(f"NOTE      {prog}: {ended}")
        if len(results) > 1:
            notes.append(f"NOTE      {prog}: prints {len(results)} RESULT lines; the last is compared")
        if not results:
            lint_docs.report("CHECK-4", prog, 1, "prints no RESULT line on standard output" + (f" ({ended})" if ended else ""))
            continue
        verdict, printed, dropped = parse_result(results[-1])
        for p in dropped:
            notes.append(f"NOTE      {prog}: RESULT part {p!r} carries no '=' and is not compared")
        if not rec:
            lint_docs.report("CHECK-4", prog, 1, f"no check record numbered {num} to compare with")
            continue
        parsed = record_values(t.prose(rec))
        if parsed is None:
            if printed:
                lint_docs.report("CHECK-4", rec, 1, f"record has no part 4 to state {', '.join(printed)}")
            else:
                notes.append(f"NOTE      {rec}: no part 4, and the program prints no named value; nothing to compare")
            continue
        heading, stated = parsed
        for k, v in printed.items():
            if k not in stated:
                lint_docs.report("CHECK-4", rec, heading, f"{k}: program prints {v!r}, record states nothing")
            elif stated[k][1] != v:
                lint_docs.report("CHECK-4", rec, stated[k][0], f"{k}: program prints {v!r}, record states {stated[k][1]!r}")
        for k, (ln, v) in stated.items():
            if k not in printed:
                lint_docs.report("CHECK-4", rec, ln, f"{k}: record states {v!r}, program prints nothing")
        for cn in lint_docs.TOKEN_CLAIM.findall(lint_docs.fields_of(t.headers[prog][0]).get("Backs", (0, ""))[1]):
            cf = t.claims.get(cn)
            cv = lint_docs.fields_of(t.headers[cf][0]).get("Verdict", (0, "?"))[1] if cf else "(no such claim)"
            notes.append(f"NOTE      {prog}: verdict printed {verdict!r}; [claim {cn}] Verdict: {cv}" + ("" if cv == verdict else "   (the words differ; never a finding)"))
    for num, rec in sorted(t.checks.items()):
        if num not in t.programs and (not only or num == only):
            written += 1
            notes.append(f"NOTE      {rec}: no program; a written procedure, not compared")
    return notes, ran, written


def run(root: Path, timeout: float, only: str | None) -> int:
    try:
        t = lint_docs.use(lint_docs.Tree(root, lint_docs.load_config(root)))
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"check_concordance: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    if only and only not in t.programs and only not in t.checks:
        print(f"check_concordance: no check numbered {only} under the configured patterns", file=sys.stderr)
        return 2
    notes, ran, written = concordance(t, timeout, only)
    for item, path, line, msg in sorted(lint_docs.FINDINGS):
        print(f"{item:9s} {path}:{line}: {msg}")
    for n in notes:
        print(n)
    k = len(lint_docs.FINDINGS)
    print(f"\nconcordance: {ran} program(s) run, {k} disagreement(s); {written} written procedure(s) not compared")
    return 1 if k else 0


def selftest() -> int:
    failures = 0
    P2, K2 = "python_project/src/check_002_b.py", "evidence_and_reasoning/checks/002_b.md"
    PRINT = 'print("RESULT: confirmed; count=" + str(len(sys.argv)))'

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:500]})"))

    def run_on(mutate, timeout: float = 30, only: str | None = None, cfg: str | None = None, lint: bool = False):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            files = lint_docs.fixture()
            mutate(files)
            lint_docs.scratch_project(tmp, files, cfg or lint_docs.scratch_config())
            lint_docs.scratch_commit(tmp)
            if lint:
                lint_docs.run_checks(tmp)
                case("the scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:3]))
            t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
            notes, ran, written = concordance(t, timeout, only)
            return list(lint_docs.FINDINGS), notes, ran, written

    def sub(rel: str, a: str, b: str):
        def m(files):
            assert files[rel].count(a) == 1, (rel, a)
            files[rel] = files[rel].replace(a, b)
        return m

    f, n, ran, written = run_on(lambda files: None, lint=True)
    case("the unplanted tree agrees", not f, str(f))
    case("the verdict is printed beside the claim's for reading", any("verdict printed 'confirmed'; [claim 002] Verdict: confirmed" in x for x in n), str(n))
    case("a written procedure is noted, not compared", any("001_a.md: no program; a written procedure" in x for x in n) and ran == 1 and written == 1, str(n))
    f, _, _, _ = run_on(sub(K2, "count = 1", "count = 2"))
    case("a value that differs is reported at the value's line", any(x[0] == "CHECK-4" and x[1] == K2 and x[2] == 15 and "prints '1', record states '2'" in x[3] for x in f), str(f))
    f, _, _, _ = run_on(sub(K2, "count = 1", "count = 1\nextra = 3"))
    case("a name stated and not printed is reported at its line", any(x[2] == 16 and "extra: record states '3', program prints nothing" in x[3] for x in f), str(f))
    f, _, _, _ = run_on(sub(P2, PRINT, PRINT[:-1] + ' + "; n=5")'))
    case("a name printed and not stated is reported at the part-4 heading", any(x[2] == 13 and "n: program prints '5', record states nothing" in x[3] for x in f), str(f))
    f, _, _, _ = run_on(sub(K2, "count = 1\n", "count = 1\n\n```\ncount = 9\n```\n\n<!--\ncount = 8\n-->\n"))
    case("a value inside a fence or a comment under part 4 is not read", not f, str(f))
    f, _, _, _ = run_on(sub(P2, PRINT, 'pass'))
    case("a program printing no RESULT line is reported", any(x[1] == P2 and "prints no RESULT line on standard output" in x[3] for x in f), str(f))
    f, _, _, _ = run_on(sub(P2, PRINT, PRINT.replace('print(', 'print(file=sys.stderr, *[')[:-1] + '])'))
    case("a RESULT line on standard error is not a RESULT line", any("prints no RESULT line on standard output" in x[3] for x in f), str(f))
    f, _, _, _ = run_on(sub(K2, "## 4. Results\n\ncount = 1\n", ""))
    case("a record with no part 4 is reported when values are printed", any("no part 4 to state count" in x[3] for x in f), str(f))
    f, n, _, _ = run_on(lambda files: (sub(K2, "## 4. Results\n\ncount = 1\n", "")(files), sub(P2, PRINT, 'print("RESULT: confirmed")')(files)))
    case("a record with no part 4 and a program printing no value is noted, not reported", not f and any("nothing to compare" in x for x in n), str((f, n)))
    f, _, _, _ = run_on(sub(P2, "import sys\n", "import sys\nraise SystemExit(3)\n"))
    case("a program that stops before its RESULT line is reported with its exit status", any("prints no RESULT line on standard output (exited 3)" in x[3] for x in f), str(f))
    f, n, _, _ = run_on(sub(P2, PRINT, 'print("RESULT: confirmed; count=2")\nraise SystemExit(1)'))
    case("a program that exits nonzero after its RESULT line is noted and still compared", any("exited 1" in x for x in n) and any("count: program prints '2', record states '1'" in x[3] for x in f), str((f, n)))
    f, n, _, _ = run_on(sub(P2, PRINT, 'print("RESULT: confirmed; count=7")\n' + PRINT))
    case("two RESULT lines are noted and the last compared", not f and any("prints 2 RESULT lines" in x for x in n), str((f, n)))
    f, n, _, _ = run_on(sub(P2, PRINT, 'print("RESULT: confirmed; count=" + str(len(sys.argv)) + "; range=1;2")'))
    case("a RESULT part without '=' is noted", any("carries no '='" in x for x in n), str((f, n)))
    f, _, _, _ = run_on(sub(P2, "import sys\n", "import sys, time\ntime.sleep(5)\n"), timeout=1)
    case("a program that exceeds the timeout is reported as unfinished", any("did not finish (timed out" in x[3] for x in f), str(f))
    f, n, _, _ = run_on(sub(P2, PRINT, PRINT + "\nimport time\ntime.sleep(5)\n"), timeout=1)
    case("a RESULT line printed before a timeout is still compared", not f and any("did not finish" in x for x in n), str((f, n)))

    def drop_record(files):
        del files[K2]
        files["evidence_and_reasoning/checks/README.md"] = files["evidence_and_reasoning/checks/README.md"].replace("| [002](002_b.md) |\n", "")
    f, _, _, _ = run_on(drop_record)
    case("a program with no record is reported", any("no check record numbered 002" in x[3] for x in f), str(f))
    f, n, _, _ = run_on(sub(P2, PRINT, 'print("RESULT: not confirmed; count=" + str(len(sys.argv)))'))
    case("a verdict differing from the claim's is marked, never a finding", not f and any("(the words differ; never a finding)" in x for x in n), str((f, n)))
    _, _, ran, written = run_on(lambda files: None, only="002")
    case("--only runs the named program alone", ran == 1 and written == 0, str((ran, written)))
    _, _, ran, written = run_on(lambda files: None, only="001")
    case("--only on a written procedure runs nothing and lists it", ran == 0 and written == 1, str((ran, written)))
    skipping = lint_docs.scratch_config().replace('glob = "evidence_and_reasoning/checks/[0-9]*.md"\ngenre = "plan-owned"',
                                                  'glob = "evidence_and_reasoning/checks/[0-9]*.md"\ngenre = "plan-owned"\nskip = ["CHECK-4"]')
    assert skipping != lint_docs.scratch_config()
    f, _, _, _ = run_on(sub(K2, "count = 1", "count = 2"), cfg=skipping)
    case("a skip list on the record's row is honored", not f, str(f))
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        lint_docs.scratch_project(tmp, lint_docs.fixture(), lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = run(tmp, 30, "042")
        case("an unknown --only number exits 2", code == 2, str(code))
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    timeout, only = 600.0, None
    it = iter(argv)
    for a in it:
        if a == "--timeout":
            try:
                timeout = float(next(it))
            except (StopIteration, ValueError):
                print(__doc__.split("Usage")[1], file=sys.stderr)
                return 2
        elif a == "--only":
            only = next(it, "")
            if not re.fullmatch(lint_docs.NUM, only):
                print(__doc__.split("Usage")[1], file=sys.stderr)
                return 2
        else:
            print(__doc__.split("Usage")[1], file=sys.stderr)
            return 2
    return run(ROOT, timeout, only)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

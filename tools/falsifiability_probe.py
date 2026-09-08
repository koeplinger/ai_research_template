#!/usr/bin/env python3
"""The falsifiability probe: every check program re-run under each mutation it names, in a scratch copy of the tree (CHECK_METHODOLOGY.md, What is checked mechanically, item 3, the half that executes).

Created 5 September 2026; updated 5 September 2026.

For a check that executes, the probe applies exactly the mutations the
check names to a scratch copy and re-runs it, reporting it under CHECK-3
if it still passes (item 3; section 5: "a mutation that a claim survives
is a defect").  The names applied are the program's Mutation: line and
its record's, the program's first; a name only the record carries comes
out UNBOUND.  A mutation is applied the way python_project/src/_template_check.py
binds it: the program's MUTATIONS maps each name to a function that takes
what construct() returns and returns the altered object, and the probe
runs the program with that function wrapped around construct(), so main()
sanity checks and verifies the altered object.  The program runs
unbuffered, with the interpreter running this tool, from a copy of the
whole tree (.git and the usual caches excepted; a large tree costs the
copy), from the parent of the configured program directory, as
python_project/README.md, Running, says a check is run; nothing it writes
lands in the tree.

The matrix prints one row per program and one cell per mutation named:
CAUGHT where the mutated run reaches a failing verdict; SURVIVES where it
passes, a finding at the Mutation: line; UNBOUND where the name has no
callable entry in MUTATIONS, which the linter's CHECK-3 reports; ERROR
where the run ended in an exception, a signal, or a timeout, said as
such, since none is a verdict.  Before any mutation is judged, two runs
must pass: the program run directly, and the program run through the
probe's own harness with no mutation.  A program whose direct run fails or
does not finish is noted and not judged, since a failing verdict may be
the check's own result (a claim RULED_OUT is backed by one), and nothing
is learned from re-running it; a program that passes directly but not
through the harness, or that has no construct() and main() to wrap, is
reported as one the probe cannot probe.  A construct() called at import
time, rather than from main(), is outside the probe's reach.  The probe
reserves the exit statuses 97, 98, and 99 for its own harness and reads
them only beside its own PROBE: line, so a program's own exit status is
never mistaken for the harness's.  It honors a row's `skip` list, like
the linter.

WHAT IT DOES NOT DECIDE.  A written check procedure has nothing to run:
whether the planted alteration was caught is read from its record's
Executions, and the probe lists the procedure and says so; an absent or
unrecognized Mutation: line on either form is the linter's CHECK-3.  A
Robustness perturbation is not applied: there survival is the intended
result and is recorded in the check record (section 5).  Whether a
mutation set is adequate, and whether a mutation alters what the claim
depends on, is reading.

Usage
    python3 tools/falsifiability_probe.py              every check program
    python3 tools/falsifiability_probe.py --only NNN
    python3 tools/falsifiability_probe.py --timeout S  seconds per run (default 600)
    python3 tools/falsifiability_probe.py --selftest

Exit status: 0 no finding; 1 a survival, or a program that cannot be
probed; 2 an unknown check, a usage error, or tools/artifacts.toml
unreadable.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
UNBOUND, NO_HOOK, NO_VERDICT = 97, 98, 99
IGNORED = (".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".run_ledger.json*")
RUNNER = r'''
import importlib.util, os, sys, traceback
path, name = sys.argv[1], sys.argv[2]
sys.argv = [path]  # the program sees the argv of a direct run
sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
PROBE = [None]
def leave(msg, code):
    print("PROBE: " + msg); PROBE[0] = code; sys.exit(code)
try:
    spec = importlib.util.spec_from_file_location("check_under_probe", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_under_probe"] = mod
    spec.loader.exec_module(mod)
except SystemExit:
    if PROBE[0] is None: leave("the program exited while being imported; not a verdict", 99)
    raise
except BaseException as e:
    traceback.print_exc(); leave("the import ended in an exception: %s: %s" % (type(e).__name__, e), 99)
missing = [n for n in ("construct", "main") if not callable(getattr(mod, n, None))]
if missing:
    leave("no " + " and ".join(n + "()" for n in missing) + " to wrap", 98)
if name:
    muts = getattr(mod, "MUTATIONS", None)
    if not isinstance(muts, dict) or name not in muts:
        leave("mutation not bound in MUTATIONS: " + name, 97)
    if not callable(muts[name]):
        leave("MUTATIONS[%r] is bound to a value that is not callable" % name, 97)
    orig = mod.construct
    def wrapped(*a, **k):
        obj = orig(*a, **k)
        try:
            return muts[name](obj)
        except SystemExit:
            leave("the mutation itself exited; not a verdict", 99)
    mod.construct = wrapped
try:
    code = mod.main()
except SystemExit as e:
    if PROBE[0] is not None: sys.exit(PROBE[0])
    code = e.code
except BaseException as e:
    traceback.print_exc(); leave("the run ended in an exception: %s: %s" % (type(e).__name__, e), 99)
if code is None or not isinstance(code, int):
    leave("main() returned no exit status; not a verdict", 99)
sys.exit(0 if code == 0 else 1)
'''


def fields(t: lint_docs.Tree, f: str) -> dict[str, tuple[int, str]]:
    return lint_docs.fields_of(t.headers[f][0]) if f in t.headers else {}


def names_of(t: lint_docs.Tree, f: str) -> list[str]:
    return [x.strip() for x in fields(t, f).get(lint_docs.F("mutation"), (0, ""))[1].split(",") if x.strip()]


def scratch_copy(root: Path, tmp: Path) -> Path:
    """The whole tree, .git and the caches excepted, under tmp/tree."""
    dest = tmp / "tree"
    shutil.copytree(root, dest, symlinks=True, ignore=shutil.ignore_patterns(*IGNORED))
    return dest


def run_one(argv: list[str], cwd: Path, timeout: float) -> tuple[int | None, str]:
    """(exit status, or None on timeout; the last PROBE: line, else the last line of stderr)."""
    try:
        p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, f"timed out after {timeout:g} s"
    probe = [l for l in (p.stdout + "\n" + p.stderr).splitlines() if l.startswith("PROBE:")]
    return p.returncode, (probe[-1] if probe else (p.stderr.strip().splitlines() or [""])[-1][:120])


def classify(code: int | None, msg: str) -> tuple[str, str]:
    """(cell word, detail) for a mutated run."""
    if code is None:
        return "ERROR", msg
    if code < 0:
        return "ERROR", f"killed by signal {-code}, not a verdict"
    if code == 0:
        return "SURVIVES", ""
    if code == UNBOUND and msg.startswith("PROBE: ") and ("not bound" in msg or "not callable" in msg):
        return "UNBOUND", msg[7:]
    if code == NO_HOOK and msg.startswith("PROBE: no "):
        return "NOT PROBED", msg[7:]
    if code == NO_VERDICT and msg.startswith("PROBE: "):
        return "ERROR", msg[7:]
    return "CAUGHT", ""


def probe(t: lint_docs.Tree, timeout: float, only: str | None = None) -> tuple[list[str], list[str], int]:
    """Findings go through lint_docs.report; returns (matrix lines, notes, programs probed)."""
    matrix, notes, ran = [], [], 0
    todo = [(n, p) for n, p in sorted(t.programs.items()) if not only or n == only]
    if todo:
        prog_dir = Path(t.dir_of_kind("check-program"))
        with tempfile.TemporaryDirectory() as d:
            scratch = scratch_copy(t.root, Path(d))
            cwd = scratch / prog_dir.parent
            for num, prog in todo:
                ran += 1
                rec = t.checks.get(num)
                mline = fields(t, prog).get(lint_docs.F("mutation"), (1, ""))[0]
                names = list(dict.fromkeys(names_of(t, prog) + (names_of(t, rec) if rec else [])))
                if rec and names_of(t, rec) != names_of(t, prog):
                    notes.append(f"NOTE      {rec}: its Mutation line ({', '.join(names_of(t, rec)) or 'none'}) differs from the program's ({', '.join(names_of(t, prog)) or 'none'}); both are applied")
                if not names:
                    matrix.append(f"  [check {num}]  (no Mutation line: the linter's CHECK-3 reports it; nothing to apply)")
                    continue
                code, msg = run_one([sys.executable, "-u", str(scratch / prog)], cwd, timeout)
                if code != 0:
                    what = msg if code is None else f"exited {code}"
                    word = "ERROR" if code is None else "FAILS"
                    notes.append(f"NOTE      {prog}: the direct run {'did not finish (' + msg + ')' if code is None else 'reaches a failing verdict (exited ' + str(code) + ')'}; its mutations are not judged, and the verdict is read from its record")
                    matrix.append(f"  [check {num}]  direct: {word} ({what})  " + "  ".join(f"{n}: not judged" for n in names))
                    continue
                code, msg = run_one([sys.executable, "-u", "-c", RUNNER, str(scratch / prog), ""], cwd, timeout)
                if code != 0:
                    detail = msg[7:] if msg.startswith("PROBE: ") else (msg if code is None else f"exited {code}")
                    if code == NO_HOOK and msg.startswith("PROBE: no "):
                        lint_docs.report("CHECK-3", prog, 1, f"cannot be probed: {detail} (the template's form)")
                    else:
                        lint_docs.report("CHECK-3", prog, 1, f"cannot be probed: its verdict is not reached by calling main() as the template's form does ({detail})")
                    matrix.append(f"  [check {num}]  direct: passes  harness: FAILS ({detail})  " + "  ".join(f"{n}: not probed" for n in names))
                    continue
                cells = []
                for k, n in enumerate(names):
                    code, msg = run_one([sys.executable, "-u", "-c", RUNNER, str(scratch / prog), n], cwd, timeout)
                    word, detail = classify(code, msg)
                    cells.append(f"{n}: {word}" + (f" ({detail})" if detail and word != "SURVIVES" else ""))
                    if word == "SURVIVES":
                        lint_docs.report("CHECK-3", prog, mline, f"survives the mutation {n!r} it names: a mutation a check survives is a defect (section 5)")
                    elif word == "NOT PROBED":
                        lint_docs.report("CHECK-3", prog, 1, f"cannot be probed: {detail} (the template's form)")
                        cells += [f"{m}: not probed" for m in names[k + 1:]]
                        break
                matrix.append(f"  [check {num}]  direct: passes  harness: passes  " + "  ".join(cells))
    for num, rec in sorted(t.checks.items()):
        if num not in t.programs and (not only or num == only):
            if names_of(t, rec):
                notes.append(f"NOTE      {rec}: a written procedure; whether the planted alteration was caught is read from its Executions")
            else:
                notes.append(f"NOTE      {rec}: a written procedure with no Mutation line: the linter's CHECK-3 reports it")
    return matrix, notes, ran


def run(root: Path, timeout: float, only: str | None) -> int:
    try:
        t = lint_docs.use(lint_docs.Tree(root, lint_docs.load_config(root)))
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"falsifiability_probe: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    if only and only not in t.programs and only not in t.checks:
        print(f"falsifiability_probe: no check numbered {only} under the configured patterns", file=sys.stderr)
        return 2
    if t.programs and not t.dir_of_kind("check-program"):
        print("falsifiability_probe: the check-program row's glob names no directory", file=sys.stderr)
        return 2
    matrix, notes, ran = probe(t, timeout, only)
    print("The matrix:" if matrix else "The matrix: (no check program)")
    for m in matrix:
        print(m)
    for item, path, line, msg in sorted(lint_docs.FINDINGS):
        print(f"{item:9s} {path}:{line}: {msg}")
    for n in notes:
        print(n)
    k = len(lint_docs.FINDINGS)
    print(f"\nprobe: {ran} program(s) probed, {k} finding(s)")
    return 1 if k else 0


def selftest() -> int:
    failures = 0
    P2, K2 = "python_project/src/check_002_b.py", "evidence_and_reasoning/checks/002_b.md"
    GOOD = '"variant-reading": lambda o: o + 1'
    CHECK = 'report("x", value("count", obj) == 1)'

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:500]})"))

    def digest(tmp: Path) -> dict[str, str]:
        return {str(p.relative_to(tmp)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in tmp.rglob("*") if p.is_file() and ".git" not in p.parts}

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
            before = digest(tmp)
            matrix, notes, ran = probe(t, timeout, only)
            return list(lint_docs.FINDINGS), matrix, notes, ran, before == digest(tmp)

    def sub(rel: str, a: str, b: str):
        def m(files):
            assert files[rel].count(a) == 1, (rel, a)
            files[rel] = files[rel].replace(a, b)
        return m

    f, m, n, ran, same = run_on(lambda files: None, lint=True)
    case("a mutation the check catches is CAUGHT, and no finding", not f and any("variant-reading: CAUGHT" in x for x in m), str((f, m)))
    case("a written procedure is listed, its alteration read from its Executions", any("001_a.md: a written procedure;" in x for x in n), str(n))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"variant-reading": lambda o: o'))
    case("a mutation the check survives is reported at the Mutation line", any(x[0] == "CHECK-3" and x[1] == P2 and x[2] == 7 and "survives the mutation 'variant-reading'" in x[3] for x in f) and any("SURVIVES" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"other": lambda o: o'))
    case("a name not bound in MUTATIONS is UNBOUND, the linter's finding, not the probe's", not f and any("variant-reading: UNBOUND" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"variant-reading": "not a function"'))
    case("a name bound to something not callable is UNBOUND, said so", not f and any("UNBOUND (MUTATIONS['variant-reading'] is bound to a value that is not callable)" in x for x in m), str((f, m)))
    f, m, n, _, _ = run_on(sub(P2, CHECK, 'report("x", value("count", obj) == 2)'))
    case("a program whose direct run fails is noted, not reported, and not judged", not f and any("reaches a failing verdict (exited 1)" in x for x in n) and any("direct: FAILS (exited 1)  variant-reading: not judged" in x for x in m), str((f, m, n)))
    f, m, n, _, _ = run_on(sub(P2, "def construct():\n", "import time\ntime.sleep(5)\ndef construct():\n"), timeout=1)
    case("a program whose direct run does not finish is noted as ERROR, not judged", not f and any("direct: ERROR (timed out" in x for x in m) and any("did not finish" in x for x in n), str((f, m, n)))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"variant-reading": lambda o: 1 / 0'))
    case("a mutated run that ends in an exception is ERROR with the exception named", not f and any("ERROR (the run ended in an exception: ZeroDivisionError" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"variant-reading": lambda o: sys.exit(1)'))
    case("a mutation that itself exits is ERROR, not CAUGHT", not f and any("ERROR (the mutation itself exited" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, GOOD, '"variant-reading": lambda o: __import__("time").sleep(5) or o'), timeout=1)
    case("a mutated run that exceeds the timeout is ERROR", not f and any("ERROR (timed out" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, "def construct():\n    return len(sys.argv)\ndef main():\n    obj = construct()\n", "def main():\n    obj = len(sys.argv)\n"))
    case("a program without construct() cannot be probed and is reported", any("cannot be probed: no construct() to wrap" in x[3] for x in f) and any("harness: FAILS (no construct() to wrap)" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, 'if __name__ == "__main__":\n    raise SystemExit(main())', 'if __name__ == "__main__":\n    SEED = 1\n    raise SystemExit(main())').__call__ and (lambda files: (sub(P2, "def main():\n    obj = construct()\n", "def main():\n    obj = construct() + SEED - 1\n")(files), sub(P2, 'if __name__ == "__main__":\n    raise SystemExit(main())', 'if __name__ == "__main__":\n    SEED = 1\n    raise SystemExit(main())')(files))))
    case("a program that passes directly but not through the harness is reported, not judged", any("its verdict is not reached by calling main()" in x[3] for x in f) and any("harness: FAILS" in x and "not probed" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, "    return 1 if FAILURES else 0\n", "    return None\n"))
    case("a main() that returns no exit status is not a verdict: not probed", any("main() returned no exit status" in x[3] for x in f), str((f, m)))
    f, m, _, _, _ = run_on(sub(P2, "    return 1 if FAILURES else 0\n", "    return 99 if FAILURES else 0\n"))
    case("a program's own exit status 99 under a mutation is CAUGHT, not the harness's code", not f and any("variant-reading: CAUGHT" in x for x in m), str((f, m)))
    two_cfg = lint_docs.scratch_config().replace('mutations = ["variant-reading"]', 'mutations = ["variant-reading", "other"]')
    two = lambda files: (sub(P2, "Mutation: variant-reading", "Mutation: variant-reading, other")(files),
                         sub(P2, GOOD, GOOD + ', "other": lambda o: o')(files),
                         sub(K2, "Mutation: variant-reading", "Mutation: variant-reading, other")(files))
    f, m, _, _, _ = run_on(two, cfg=two_cfg)
    case("two mutations named: one caught, one surviving, one finding", len(f) == 1 and any("variant-reading: CAUGHT  other: SURVIVES" in x for x in m), str((f, m)))
    f, m, n, _, _ = run_on(sub(K2, "Mutation: variant-reading", "Mutation: variant-reading, base-witness-swap"), cfg=two_cfg.replace('"other"', '"base-witness-swap"'))
    case("a name only the record carries is applied and comes out UNBOUND, with a note", not f and any("base-witness-swap: UNBOUND" in x for x in m) and any("differs from the program's" in x for x in n), str((f, m, n)))
    f, m, _, _, _ = run_on(lambda files: (sub(P2, "Mutation: variant-reading\n", "Mutation: variant-reading\nRobustness: other\n")(files), sub(P2, GOOD, GOOD + ', "other": lambda o: o')(files)), cfg=two_cfg)
    case("a Robustness perturbation is not applied", not f and not any("other:" in x for x in m), str((f, m)))
    f, m, _, _, _ = run_on(lambda files: (sub(P2, "Mutation: variant-reading\n", "")(files), sub(K2, "Mutation: variant-reading\n", "")(files)))
    case("a check with no Mutation line on either form has nothing to apply, the linter's finding", not f and any("no Mutation line" in x for x in m), str((f, m)))
    _, _, _, _, same = run_on(sub(P2, "def construct():\n", "open('../README.md', 'a').write('x')\nopen('src/left_behind.txt', 'w').write('x')\ndef construct():\n"))
    case("a program that writes beside and above its folder writes into the scratch copy, not the tree", same)
    _, m, _, ran, _ = run_on(lambda files: None, only="002")
    case("--only probes the named program alone", ran == 1 and len(m) == 1, str((ran, m)))
    _, m, n, ran, _ = run_on(lambda files: None, only="001")
    case("--only on a written procedure probes nothing and lists it", ran == 0 and not m and any("001_a.md" in x for x in n), str((ran, m, n)))

    def no_program(files):
        del files[P2]
        files["python_project/src/README.md"] = files["python_project/src/README.md"].replace("| [check_002_b.py](check_002_b.py) |\n", "")
    _, m, n, ran, _ = run_on(no_program)
    case("a project of written procedures alone still has them listed", ran == 0 and not m and any("001_a.md" in x for x in n) and any("002_b.md" in x for x in n), str((ran, m, n)))
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

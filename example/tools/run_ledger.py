#!/usr/bin/env python3
"""The run ledger: a local cache of check runs, keyed by a hash of what each verdict rests on, so that recomputation follows a changed basis.

Created 5 September 2026; updated 5 September 2026.

No rulebook item owns this tool, and it decides nothing.  The record of
a run is the check record (CHECK_METHODOLOGY.md section 8), which the
concordance check compares with the program's RESULT line; this ledger is
read by nothing else.  It is a cache beside the program directory,
.run_ledger.json, git-ignored, and it answers one question: which checks
must be run again because something their verdict rests on has changed.

A check program's BASIS, as this tool can see it: the program's own
text; every module or package under the configured program directory it
imports, transitively, relative imports included; the pinned
dependencies, requirements.txt beside that directory; the interpreter's
implementation and version; and every path the program lists in a
module-level BASIS = ["..."], relative to the repository root, a
directory standing for every file under it, which is how a program says
which data it reads (python_project/src/_template_check.py pre-prints the
list).  Anything else a program reads is outside the hash, and every
status line says so.  `run` recomputes exactly the checks whose hash
changed or whose last run did not finish; a check whose basis is
unchanged is not run again unless forced.  Each run's seconds are kept,
since cost is measured and never a gate (section 8): the expensive
checks can be examined for avoidable work.  The cached runs are kept as a
local convenience; the record of a run stays the check record.

Usage
    python3 tools/run_ledger.py status                 each program: current, stale, or never run
    python3 tools/run_ledger.py run [--only NNN] [--force] [--timeout S]
                                                       run and record what is stale (everything, with --force)
    python3 tools/run_ledger.py show NNN               the cached runs of one check
    python3 tools/run_ledger.py --selftest

Exit status: status, 0 when every program is current, 1 otherwise; run,
0 when every run recorded reached a passing verdict, 1 when one failed
(a run that did not finish is counted apart, and is not a failure); 2
an unknown check, a usage error, or tools/artifacts.toml unreadable.
"""
from __future__ import annotations

import ast
import datetime
import hashlib
import json
import platform
import re
import subprocess
import sys
import tempfile
import time
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ".run_ledger.json"
RESULT_RE = re.compile(r"^RESULT:.*$", re.M)


def project_of(t: lint_docs.Tree) -> Path:
    return t.root / Path(t.dir_of_kind("check-program")).parent


def declared_basis(text: str) -> list[str]:
    """The paths a program lists in BASIS = [...]; empty where it lists none."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    for node in tree.body:
        targets = node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else []
        if any(getattr(x, "id", "") == "BASIS" for x in targets) and isinstance(node.value, (ast.List, ast.Tuple)):
            return [e.value for e in node.value.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
    return []


def imports_of(text: str) -> list[tuple[int, str | None, list[str]]]:
    """(level, module, names) for every import statement; [] where the text does not parse."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out.append((0, None, [a.name for a in node.names]))
        elif isinstance(node, ast.ImportFrom):
            out.append((node.level, node.module, [a.name for a in node.names]))
    return out


def resolve(src: Path, importer: Path, level: int, module: str | None, names: list[str]) -> list[Path]:
    """The project files an import statement names: a module file, or every
    file of a package; nothing where the import is not the project's."""
    base = importer.parent
    for _ in range(max(level - 1, 0)):
        base = base.parent
    if level == 0:
        base = src

    def find(dotted: str) -> list[Path]:
        parts = dotted.split(".")
        for n in range(len(parts), 0, -1):
            p = base.joinpath(*parts[:n])
            if p.with_suffix(".py").is_file():
                return [p.with_suffix(".py")]
            if (p / "__init__.py").is_file():
                return sorted(q for q in p.rglob("*.py"))
        return []

    if module:
        return find(module)
    if level > 0:
        return [q for n in names for q in find(n)]
    return [q for n in names for q in find(n)]


def basis_files(t: lint_docs.Tree, prog: str) -> dict:
    """What is hashed, and what was looked for and not found."""
    src = t.root / t.dir_of_kind("check-program")
    root = t.root.resolve()
    start = t.root / prog
    files, seen, todo, modules = [start], {start}, [start], []
    while todo:
        p = todo.pop()
        for level, module, names in imports_of(p.read_text(encoding="utf-8", errors="replace")):
            for q in resolve(src, p, level, module, names):
                if q not in seen:
                    seen.add(q)
                    files.append(q)
                    modules.append(str(q.relative_to(t.root)))
                    todo.append(q)
    req = project_of(t) / "requirements.txt"
    declared, data, missing = declared_basis(start.read_text(encoding="utf-8", errors="replace")), [], []
    for rel in declared:
        q = (t.root / rel)
        try:
            inside = q.resolve().is_relative_to(root)
        except OSError:
            inside = False
        if Path(rel).is_absolute() or not inside:
            missing.append(f"{rel} (outside the repository)")
        elif q.is_dir():
            data += sorted(x for x in q.rglob("*") if x.is_file())
        elif q.is_file():
            data.append(q)
        else:
            missing.append(rel)
    return {"program": start, "modules": files[1:], "module_names": modules, "requirements": req if req.is_file() else None,
            "declared": declared, "data": data, "missing": missing}


def basis_hash(t: lint_docs.Tree, prog: str) -> tuple[str, dict, list[str]]:
    """(hash, what was hashed, files that could not be read)."""
    b = basis_files(t, prog)
    h = hashlib.sha256(f"{sys.implementation.name} {platform.python_version()}".encode())
    unreadable = []
    for p in sorted(set([b["program"]] + b["modules"] + ([b["requirements"]] if b["requirements"] else []) + b["data"])):
        rel = str(p.relative_to(t.root))
        try:
            h.update(rel.encode() + b"\0" + p.read_bytes() + b"\0")
        except OSError as e:
            unreadable.append(rel)
            h.update(b"unreadable " + rel.encode() + str(e).encode() + b"\0")
    for rel in b["missing"]:
        h.update(b"missing " + rel.encode() + b"\0")
    return h.hexdigest(), b, unreadable


def load_ledger(t: lint_docs.Tree) -> tuple[dict, bool]:
    """(the ledger, whether the file was unreadable and is being replaced)."""
    p = project_of(t) / LEDGER
    if not p.is_file():
        return {}, False
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        data = None
    ok = isinstance(data, dict) and all(isinstance(v, list) and all(isinstance(r, dict) and "basis" in r for r in v) for v in data.values())
    if not ok:
        print(f"run_ledger: {p.relative_to(t.root)} unreadable or not a ledger; starting a new one (the old file is kept as {LEDGER}.corrupt)", file=sys.stderr)
        return {}, True
    return data, False


def save_ledger(t: lint_docs.Tree, ledger: dict, corrupt: bool) -> None:
    p = project_of(t) / LEDGER
    if corrupt and p.exists():
        p.replace(p.with_suffix(".json.corrupt"))
    p.write_text(json.dumps(ledger, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def describe(b: dict, unreadable: list[str]) -> str:
    parts = ["program"]
    parts.append(f"{len(b['module_names'])} imported project file(s)" + (f" ({', '.join(b['module_names'])})" if b["module_names"] else ""))
    parts.append("requirements.txt" if b["requirements"] else "requirements.txt (absent)")
    parts.append("interpreter")
    if b["declared"]:
        parts.append("BASIS: " + ", ".join(b["declared"]) + f" ({len(b['data'])} file(s))")
    else:
        parts.append("no BASIS list")
    line = "; ".join(parts) + "; anything else it reads is outside the hash"
    if b["missing"]:
        line += f"\n      declared but missing: {', '.join(b['missing'])}"
    if unreadable:
        line += f"\n      could not be read: {', '.join(unreadable)}"
    return line


def status(t: lint_docs.Tree) -> tuple[list[str], int]:
    ledger, _ = load_ledger(t)
    out, stale = [], 0
    for num, prog in sorted(t.programs.items()):
        h, b, unreadable = basis_hash(t, prog)
        runs = ledger.get(num, [])
        last = runs[-1] if runs else None
        if not last:
            state, stale = "never run", stale + 1
        elif last["exit"] is None:
            state, stale = f"stale (the last run, {last['when']}, did not finish)", stale + 1
        elif last["basis"] != h:
            state, stale = f"stale (basis changed since {last['when']})", stale + 1
        else:
            state = f"current (run {last['when']}, {last['seconds']:.1f} s, exit {last['exit']})"
        out.append(f"  [check {num}]  {state}\n      basis: {describe(b, unreadable)}")
    if not t.programs:
        out.append("  (no check program)")
    return out, stale


def run_checks(t: lint_docs.Tree, only: str | None, force: bool, timeout: float) -> tuple[list[str], int, int]:
    """(lines, runs that failed, runs that did not finish)."""
    ledger, corrupt = load_ledger(t)
    out, failed, unfinished, ran = [], 0, 0, 0
    cwd = project_of(t)
    for num, prog in sorted(t.programs.items()):
        if only and num != only:
            continue
        h, _, _ = basis_hash(t, prog)
        runs = ledger.setdefault(num, [])
        if runs and runs[-1]["basis"] == h and runs[-1]["exit"] is not None and not force:
            out.append(f"  [check {num}]  current; not run (use --force)")
            continue
        ran += 1
        t0 = time.monotonic()
        try:
            p = subprocess.run([sys.executable, "-u", str(t.root / prog)], cwd=cwd, capture_output=True, text=True, timeout=timeout)
            code, result = p.returncode, (RESULT_RE.findall(p.stdout) or [""])[-1]
        except subprocess.TimeoutExpired as e:
            got = e.stdout.decode("utf-8", errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
            code, result = None, (RESULT_RE.findall(got) or [""])[-1]
        seconds = time.monotonic() - t0
        when = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
        runs.append({"basis": h, "when": when, "seconds": round(seconds, 3), "exit": code, "result": result})
        if code is None:
            unfinished += 1
        elif code != 0:
            failed += 1
        out.append(f"  [check {num}]  ran {seconds:.1f} s, " + ("did not finish (timed out)" if code is None else f"exit {code}") + (f", {result}" if result else ", no RESULT line"))
    save_ledger(t, ledger, corrupt)
    if not ran:
        out.append("  (nothing to run: every basis is current)" if t.programs else "  (no check program)")
    return out, failed, unfinished


def show(t: lint_docs.Tree, num: str) -> list[str]:
    runs, _ = load_ledger(t)
    runs = runs.get(num, [])
    if not runs:
        return [f"  [check {num}]  no cached run (the record of a run is the check record)"]
    return [f"  [check {num}]  {r['when']}  {r['seconds']:.1f} s  " + ("did not finish" if r["exit"] is None else f"exit {r['exit']}") + f"  {r['result'] or '(no RESULT line)'}  basis {r['basis'][:12]}" for r in runs]


def selftest() -> int:
    failures = 0
    P2 = "python_project/src/check_002_b.py"

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:400]})"))

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        files = lint_docs.fixture()
        S = lint_docs.STAMP
        files["python_project/src/base.py"] = f'"""A foundation module.\n\n{S.strip("*")}\n"""\nimport deep\nfrom pkg import part\nK = deep.D + part.P\n'
        files["python_project/src/deep.py"] = f'"""A deeper module.\n\n{S.strip("*")}\n"""\nimport base\nD = 1\n'
        files["python_project/src/pkg/__init__.py"] = f'"""A package.\n\n{S.strip("*")}\n"""\nfrom . import part\n'
        files["python_project/src/pkg/part.py"] = f'"""A package member.\n\n{S.strip("*")}\n"""\nP = 0\n'
        files["python_project/src/README.md"] += "| [base.py](base.py) |\n| [deep.py](deep.py) |\n| [pkg/](pkg/) |\n"
        files["python_project/requirements.txt"] = "pytest==8.3.3\n"
        files["python_project/README.md"] += "| [requirements.txt](requirements.txt) |\n"
        files[P2] = files[P2].replace("import sys\n", "import sys\nimport base\nBASIS = [\"source_documents/data.txt\", \"source_documents/extract\"]\n")
        files["source_documents/data.txt"] = "1\n"
        files["source_documents/extract/a.txt"] = "a\n"
        files["source_documents/README.md"] = f"# Sources\n\n{S}\n\n| File |\n|---|\n| [data.txt](data.txt) |\n| [extract/](extract/) |\n"
        lint_docs.scratch_project(tmp, files, lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        lint_docs.run_checks(tmp)
        case("the extended scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:4]))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        out, stale = status(t)
        case("a program never run is stale", stale == 1 and "never run" in out[0], str(out))
        case("the basis names the transitive imports once each, the package included", "4 imported project file(s)" in out[0] and "pkg/part.py" in out[0] and "deep.py" in out[0], str(out))
        case("the basis names the declared data, a directory standing for its files, and what is outside", "BASIS: source_documents/data.txt, source_documents/extract (2 file(s))" in out[0] and "anything else it reads is outside the hash" in out[0], str(out))
        out, failed, unfinished = run_checks(t, None, False, 30)
        case("run records a passing run with its RESULT line", failed == 0 and unfinished == 0 and "exit 0, RESULT: confirmed; count=1" in out[0], str(out))
        case("the ledger is written beside the program directory", (tmp / "python_project" / LEDGER).is_file())
        out, stale = status(t)
        case("after a run the program is current", stale == 0 and "current (run" in out[0], str(out))
        out, _, _ = run_checks(t, None, False, 30)
        case("a current program is not run again", "not run (use --force)" in out[0], str(out))
        out, _, _ = run_checks(t, None, True, 30)
        case("--force runs it anyway", "ran " in out[0], str(out))
        case("show lists every cached run", len(show(t, "002")) == 2, str(show(t, "002")))
        h0, _, _ = basis_hash(t, P2)
        (tmp / "python_project" / "src" / "pkg" / "part.py").write_text(files["python_project/src/pkg/part.py"].replace("P = 0", "P = 2"))
        h1, _, _ = basis_hash(t, P2)
        case("a change to a package member reached through a relative import changes the basis", h0 != h1)
        (tmp / "source_documents" / "extract" / "a.txt").write_text("b\n")
        h2, _, _ = basis_hash(t, P2)
        case("a change under a declared directory changes the basis", h1 != h2)
        (tmp / "python_project" / "requirements.txt").write_text("pytest==8.3.4\n")
        h3, _, _ = basis_hash(t, P2)
        case("a change to a pin changes the basis", h2 != h3)
        out, stale = status(t)
        case("a changed basis is stale", stale == 1 and "stale (basis changed since" in out[0], str(out))
        (tmp / P2).write_text((tmp / P2).read_text().replace('"source_documents/extract"', '"source_documents/gone.txt", "/etc/hosts", "../outside"'))
        out, _ = status(t)
        case("a declared path that is missing or outside the repository is said so", "declared but missing: source_documents/gone.txt, /etc/hosts (outside the repository), ../outside (outside the repository)" in out[0], str(out))
        (tmp / P2).write_text((tmp / P2).read_text().replace('report("x", value("count", obj) == 1)', 'report("x", value("count", obj) == 2)'))
        out, failed, unfinished = run_checks(t, None, False, 30)
        case("a failing run is recorded with its exit status and counted as failed", failed == 1 and unfinished == 0 and "exit 1" in out[0], str(out))
        (tmp / P2).write_text((tmp / P2).read_text().replace("import base\n", "import base, time\ntime.sleep(5)\n"))
        out, failed, unfinished = run_checks(t, None, False, 1)
        case("a run that does not finish is recorded as such and not counted as failed", failed == 0 and unfinished == 1 and "did not finish" in out[0], str(out))
        out, stale = status(t)
        case("a program whose last run did not finish is stale", stale == 1 and "did not finish" in out[0], str(out))
        out, _, _ = run_checks(t, None, False, 1)
        case("and is run again without --force", "ran " in out[0], str(out))
        (tmp / P2).write_text("def broken(:\n")
        out, _ = status(t)
        case("a program that does not parse still has a basis, its imports unread", "0 imported project file(s)" in out[0], str(out))
        (tmp / "python_project" / LEDGER).write_text("[1, 2]")
        with_err = io.StringIO()
        with contextlib.redirect_stderr(with_err):
            ledger, corrupt = load_ledger(t)
        case("a corrupt ledger is said so and replaced, the old file kept", ledger == {} and corrupt and "unreadable or not a ledger" in with_err.getvalue())
        save_ledger(t, {}, corrupt)
        case("the corrupt file is kept beside the new one", (tmp / "python_project" / (LEDGER + ".corrupt")).is_file())
        (tmp / P2).write_text(files[P2])
        (tmp / "python_project" / "src" / "check_003_c.py").write_text(files[P2].replace("Check 002: b", "Check 003: c").replace("[claim 002]", "[claim 002]"))
        out, _, _ = run_checks(t, "002", False, 30)
        case("--only runs the named program and leaves the other untouched", any("[check 002]  ran" in x for x in out) and not any("[check 003]  ran" in x for x in out), str(out))
        case("a check with no cached run says so", "no cached run" in show(t, "042")[0])
        (tmp / "python_project" / "src" / "check_003_c.py").unlink()
        lint_docs.run_checks(tmp)
        stray = [x for x in lint_docs.FINDINGS if ".run_ledger" in x[1] or "requirements" in x[3]]
        case("the ledger file and the kept corrupt copy leave the scratch tree clean under the linter", not stray, str(stray))
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        lint_docs.scratch_project(tmp, lint_docs.fixture(), lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = main_on(tmp, ["show", "042"])
        case("show on an unknown check exits 2", code == 2, str(code))
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main_on(root: Path, argv: list[str]) -> int:
    if not argv or argv[0] not in ("status", "run", "show"):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    cmd, rest = argv[0], argv[1:]
    only, force, timeout = None, False, 600.0
    it = iter(rest)
    for a in it:
        if a == "--only" and cmd == "run":
            only = next(it, "")
        elif a == "--force" and cmd == "run":
            force = True
        elif a == "--timeout" and cmd == "run":
            try:
                timeout = float(next(it))
            except (StopIteration, ValueError):
                print(__doc__.split("Usage")[1], file=sys.stderr)
                return 2
        elif cmd == "show" and only is None:
            only = a
        else:
            print(__doc__.split("Usage")[1], file=sys.stderr)
            return 2
    if (cmd == "show" and only is None) or (only is not None and not re.fullmatch(lint_docs.NUM, only)):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        t = lint_docs.use(lint_docs.Tree(root, lint_docs.load_config(root)))
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"run_ledger: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    if only and only not in t.programs:
        print(f"run_ledger: no check program numbered {only} under the configured pattern", file=sys.stderr)
        return 2
    if cmd == "status":
        out, stale = status(t)
        print("\n".join(out))
        print(f"\nrun ledger: {len(t.programs)} program(s), {stale} stale or never run")
        return 1 if stale else 0
    if cmd == "run":
        out, failed, unfinished = run_checks(t, only, force, timeout)
        print("\n".join(out))
        print(f"\nrun ledger: {failed} recorded run(s) failed, {unfinished} did not finish")
        return 1 if failed else 0
    print("\n".join(show(t, only)))
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    return main_on(ROOT, argv)


import contextlib  # noqa: E402
import io  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

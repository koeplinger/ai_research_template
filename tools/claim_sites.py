#!/usr/bin/env python3
"""The blast radius of a claim (ONTOLOGY.md section 6, question 4): everything citing it by token, everything whose Depends-on names it, and the Reserved cluster if one holds it.

Created 5 September 2026; updated 5 September 2026.

For [claim NNN] the report lists, by reading fields and tokens only, the
three things the question names: every artifact whose prose carries the
token, with the line, the findings and tension rows among them by key;
every claim whose Depends-on names it, with its register; and the
Reserved cluster, every claim reserved under the same plan, where a
Reserved stamp holds it.  Beyond the question, for the reader, it adds
the checks the claim's own Backed-by names and the plan that owns it,
under a heading that says so.

What a token search cannot see is said at the end of every report: a
restatement in prose without the token (the `restates` relation of
ONTOLOGY.md section 2.8, written nowhere by design), a derived table or
figure that used the claim without naming it, a write-up's paraphrase;
a token inside backticks, a fenced block, an HTML comment, or a markdown
link, which no tool reads (ONTOLOGY.md section 1.3); a file whose
configured row carries header = none, which no tool reads; and a claim
that depends on this one only through another claim's Depends-on, which
the rests-on query shows.  A report, not a gate.

Usage
    python3 tools/claim_sites.py NNN        the report for [claim NNN]
    python3 tools/claim_sites.py --selftest

Exit status: 0 with the report; 2 when the claim does not exist, on a
usage error, or when tools/artifacts.toml cannot be read.
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
NOT_SEEN = ("Not seen here: a restatement in prose without the token, a derived table or figure that used "
            "the claim without naming it, a write-up's paraphrase (the sweep's, CHECK_METHODOLOGY.md section 7, "
            "item 1); a token inside backticks, a fenced block, an HTML comment, or a markdown link, which no tool "
            "reads (ONTOLOGY.md section 1.3); and a claim depending on this one through another claim's "
            "Depends-on, which `query_ontology.py rests-on` on that claim shows.")


def load(root: Path) -> lint_docs.Tree:
    """The tree, installed as the linter's current tree so report() honors skip lists."""
    return lint_docs.use(lint_docs.Tree(root, lint_docs.load_config(root)))


def fields(t: lint_docs.Tree, f: str) -> dict[str, tuple[int, str]]:
    return lint_docs.fields_of(t.headers[f][0]) if f in t.headers else {}


def register(t: lint_docs.Tree, num: str) -> str:
    f = t.claims.get(num)
    return fields(t, f).get("Register", (0, "?"))[1] if f else "?"


def unread_kinds(t: lint_docs.Tree) -> list[str]:
    return sorted({r["kind"] for r in t.cfg["artifact"] if r.get("header") == "none"})


def token_sites(t: lint_docs.Tree, token: str, exclude: str = "") -> list[tuple[str, int, str]]:
    """(file, line, text) of every prose line carrying `token`, links skipped."""
    out = []
    for f, row in t.rows.items():
        if not row or row.get("header", "stamp") == "none" or t.is_template(f) or f == exclude:
            continue
        for i, line in enumerate(t.prose(f).splitlines(), 1):
            if token in lint_docs.LINK_RE.sub(" ", line):
                out.append((f, i, line.strip()))
    return out


def reserved_plan(t: lint_docs.Tree, f: str) -> str | None:
    for _, s in t.headers[f][0]:
        m = re.match(rf"^Reserved {lint_docs.ANYDATE}, plan ({lint_docs.NUM})$", s)
        if m:
            return m.group(1)
    return None


def sites(t: lint_docs.Tree, num: str) -> list[str]:
    f = t.claims.get(num)
    if not f:
        raise KeyError(num)
    token = f"[claim {num}]"
    fl = fields(t, f)
    out = [f"{token}  {fl.get('Register', (0, '?'))[1]}  {f}", ""]
    out.append("Cited by token:")
    hits = token_sites(t, token, exclude=f)
    for g, i, text in hits:
        out.append(f"  {g}:{i}: {text}")
    if not hits:
        out.append("  (nowhere)")
    keyed = []
    for kind, rx in (("findings", r"^\|\s*(F[0-9]{3,})\s*\|"), ("ledger", r"^\|\s*(T[0-9]{3,})\s*\|")):
        g = t.first_of_kind(kind)
        if g:
            for line in t.prose(g).splitlines():
                m = re.match(rx, line)
                if m and token in lint_docs.LINK_RE.sub(" ", line):
                    keyed.append(f"  [{'finding' if kind == 'findings' else 'tension'} {m.group(1)}]  {g}")
    out.append("  among them, by key:" if keyed else "  (no finding or tension row)")
    out += keyed
    out.append("")
    out.append("Depended on by:")
    deps = [(n, g) for n, g in sorted(t.claims.items())
            if num in [x.strip() for x in fields(t, g).get("Depends-on", (0, ""))[1].split(",")]]
    for n, g in deps:
        out.append(f"  [claim {n}]  {register(t, n)}  {g}")
    if not deps:
        out.append("  (no claim)")
    out.append("")
    rp = reserved_plan(t, f)
    if rp:
        cluster = [n for n, g in sorted(t.claims.items()) if reserved_plan(t, g) == rp]
        out.append(f"Reserved cluster, plan {rp}: " + ", ".join(f"[claim {n}]" for n in cluster))
    else:
        out.append("Reserved cluster: none (no Reserved stamp)")
    out.append("")
    out.append("Beyond question 4, for the reader:")
    backed = lint_docs.TOKEN_CHECK.findall(fl.get("Backed-by", (0, ""))[1])
    for n in backed:
        out.append(f"  Backed-by names [check {n}]" + ("" if n in t.checks else "  (resolves to no check)"))
    if not backed:
        out.append("  Backed-by names no check")
    pf, st = t.plan_of(f)
    out.append(f"  owned by plan {t.num(pf)}, Status: {st or '(none)'}" if pf else "  owned by no plan (no Plan: line, or it resolves to no plan file)")
    out.append("")
    out.append(NOT_SEEN)
    out.append("Not searched: files whose configured row carries header = none (" + ", ".join(unread_kinds(t)) + ").")
    return out


def selftest() -> int:
    failures = 0
    S = lint_docs.STAMP

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:600]})"))

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        files = lint_docs.fixture()
        files["evidence_and_reasoning/claims/003_c.md"] = (
            f"# Claim 003: c\n\n{S}\nRegister: VERIFIED\nKind: documentary\nVerdict: confirmed\nPlan: 001, task 1\n"
            f"Verified-by: researcher\nBacked-by: [check 003]\nDepends-on: 001, 002\nReserved 2 January 2026, plan 001\n\n"
            f"## Claim\n\nThis claim, [claim 003], rests on [claim 001] and [claim 002].\n\n## What is not claimed\n\nNothing about d.\n")
        files["evidence_and_reasoning/claims/004_d.md"] = (
            f"# Claim 004: d\n\n{S}\nRegister: ATTESTED\nKind: documentary\nVerdict: confirmed\nPlan: 001, task 1\n"
            f"Verified-by: deferred, the edition\nReserved 2 January 2026, plan 001\n\n## Claim\n\nSays d [Key1, p. 4].\n")
        files["evidence_and_reasoning/checks/003_c.md"] = (
            f"# Check 003: c\n\n{S}\nPlan: 001, task 1\nBacks: [claim 003]\nInstrument: the edition\nMutation: variant-reading\n\n## 1\n\nz\n")
        files["evidence_and_reasoning/claims/README.md"] += "| [003](003_c.md) |\n| [004](004_d.md) |\n"
        files["evidence_and_reasoning/checks/README.md"] += "| [003](003_c.md) |\n"
        files["FINDINGS.md"] += "| F002 | y [claim 001](evidence_and_reasoning/claims/001_a.md) |\n"
        lint_docs.scratch_project(tmp, files, lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        lint_docs.run_checks(tmp)
        case("the extended scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:3]))
        t = load(tmp)
        r = "\n".join(sites(t, "002"))
        case("a token site in the findings file is listed, and by key", "FINDINGS.md:" in r and "[finding F001]" in r, r)
        case("a token site in the tension ledger is listed by key", "[tension T001]" in r, r)
        case("a token site in a write-up is listed", "paper/main_v1.md:" in r, r)
        case("a claim whose Depends-on names it is listed with its register", "[claim 003]  VERIFIED" in r, r)
        case("a check that backs the claim is a token site, through its Backs line", "checks/002_b.md:" in r, r)
        case("the claim's own Backed-by and plan are listed beyond the question", "Beyond question 4" in r and "Backed-by names [check 002]" in r and "owned by plan 002, Status: CLOSED" in r, r)
        case("a claim with no Reserved stamp reports no cluster", "Reserved cluster: none" in r, r)
        case("what a token search cannot see is said, and what is not searched", "Not seen here" in r and "Not searched: files whose configured row carries header = none (" in r and "imported" in r, r)
        r = "\n".join(sites(t, "003"))
        case("the Reserved cluster lists every claim reserved under the plan", "Reserved cluster, plan 001: [claim 003], [claim 004]" in r, r)
        case("the claim's own file, which carries its token, is not a site of itself", "claims/003_c.md:" not in r, r)
        r = "\n".join(sites(t, "001"))
        case("the same file is a site of the claim it cites", "claims/003_c.md:" in r, r)
        case("a token inside a markdown link is not a site, in a keyed row either", "[finding F002]" not in r and "FINDINGS.md:" not in r, r)
        r = "\n".join(sites(t, "004"))
        case("a claim nobody cites says so in every section",
             "Cited by token:\n  (nowhere)" in r and "(no finding or tension row)" in r and "Depended on by:\n  (no claim)" in r and "Backed-by names no check" in r, r)
        try:
            sites(t, "042")
            case("an unknown claim is refused", False)
        except KeyError:
            case("an unknown claim is refused", True)
    with tempfile.TemporaryDirectory() as d:
        try:
            load(Path(d))
            case("a tree without a configuration is refused", False)
        except (OSError, tomllib.TOMLDecodeError):
            case("a tree without a configuration is refused", True)
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if len(argv) != 1 or not re.fullmatch(lint_docs.NUM, argv[0]):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        t = load(ROOT)
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"claim_sites: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    try:
        print("\n".join(sites(t, argv[0])))
    except KeyError:
        print(f"claim_sites: no claim numbered {argv[0]} under the configured claim pattern", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

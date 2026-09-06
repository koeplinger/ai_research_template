#!/usr/bin/env python3
"""The ontology queries: the questions ONTOLOGY.md section 6 says the record answers from its fields.

Created 5 September 2026; updated 5 September 2026.

Each query enumerates by reading fields and tokens.  Where a rulebook
decides, the line is marked FLAG; where only reading can decide, the
output says so (ONTOLOGY.md section 6: "Where a query can only enumerate
and not decide, it says so").  A report, not a gate: exit 0 with the
answer, 2 on a usage error, an unknown claim, or when tools/artifacts.toml
cannot be read.

  rests-on NNN    question 1: the closure of Depends-on and Backed-by from
                  the claim, each member with its register; a member weaker
                  than the claim relying on it is flagged by the ordering
                  of section 4, and a RULED_OUT member always; a register
                  section 4 does not order is said to be unordered.  A
                  check is a leaf of the walk: what it backs besides this
                  claim is not what the claim rests on.
  unverified NNN  question 2: the same closure, kept to OPEN, SPECULATIVE,
                  and RULED_OUT members and to Verified-by unchecked or
                  deferred, a dependency resolving to no claim included
  deferred        question 3: every Verified-by: deferred, with its
                  instrument
  radius NNN      question 4: the blast radius, by tools/claim_sites.py
  literature      question 5: every row of the tension ledger, its columns
                  and its caution as recorded; whether a caution is still
                  live is reading
  unfinished      question 6: plans by Status, claims by register,
                  reservations by Reserved, every Serves: none
  sites           question 7: every place a claim or a check record cites
                  a claim, in its header or its body, with both registers
                  and the cited claim's "What is not claimed" quoted in
                  full beside the citing line; the comparison is reading
                  (CHECK_METHODOLOGY.md, What is checked mechanically,
                  item 6)
  all             every question that takes no claim number
Question 8 is not a predicate query and has no command (section 6).

Usage
    python3 tools/query_ontology.py <question>       a question that takes no claim
    python3 tools/query_ontology.py <question> NNN   one that takes a claim number
    python3 tools/query_ontology.py --selftest
"""
from __future__ import annotations

import re
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import claim_sites  # noqa: E402
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STRENGTH = {"VERIFIED": 3, "DERIVED": 3, "ATTESTED": 2, "OPEN": 1, "SPECULATIVE": 1}
ORDERED = ("OPEN", "SPECULATIVE", "ATTESTED", "DERIVED", "VERIFIED", "RULED_OUT")
fields, register, load = claim_sites.fields, claim_sites.register, claim_sites.load


def _flag(dep_reg: str, on_reg: str) -> str:
    if dep_reg == "RULED_OUT":
        return "   FLAG: RULED_OUT, reported always (ONTOLOGY.md section 4)"
    if dep_reg not in STRENGTH:
        return f"   (Register {dep_reg!r} is not one section 4 orders)"
    if on_reg not in STRENGTH:
        return ""
    if STRENGTH[dep_reg] < STRENGTH[on_reg]:
        return f"   FLAG: weaker than the {on_reg} claim relying on it (ONTOLOGY.md section 4)"
    return ""


def closure(t: lint_docs.Tree, num: str) -> list[tuple[int, str, str, str]]:
    """(depth, kind, number, note) in depth-first order, each member's
    subtree following it, over Depends-on and Backed-by; a member seen
    twice is listed again with "(listed above)" and not walked again."""
    if num not in t.claims:
        raise KeyError(num)
    out: list[tuple[int, str, str, str]] = []
    seen = {("claim", num)}

    def walk(n: str, depth: int) -> None:
        fl = fields(t, t.claims[n])
        for c in lint_docs.TOKEN_CHECK.findall(fl.get("Backed-by", (0, ""))[1]):
            note = "" if c in t.checks else "   (resolves to no check)"
            if ("check", c) in seen:
                note += "   (listed above)"
            seen.add(("check", c))
            out.append((depth + 1, "check", c, note))
        for d in [x.strip() for x in fl.get("Depends-on", (0, ""))[1].split(",") if x.strip()]:
            if d not in t.claims:
                out.append((depth + 1, "claim", d, "   (resolves to no claim)"))
                continue
            flag = _flag(register(t, d), register(t, n))
            if d == num:
                out.append((depth + 1, "claim", d, flag + "   (the claim itself: a cycle)"))
                continue
            if ("claim", d) in seen:
                out.append((depth + 1, "claim", d, flag + "   (listed above)"))
                continue
            seen.add(("claim", d))
            out.append((depth + 1, "claim", d, flag))
            walk(d, depth + 1)

    walk(num, 0)
    return out


def rests_on(t: lint_docs.Tree, num: str) -> list[str]:
    out = [f"[claim {num}]  {register(t, num)}  rests on:"]
    members = closure(t, num)
    for depth, kind, n, note in members:
        reg = f"  {register(t, n)}" if kind == "claim" and n in t.claims else ""
        out.append("  " * depth + f"[{kind} {n}]{reg}{note}")
    if not members:
        out.append("  (nothing: no Depends-on, no Backed-by)")
    return out


def unverified(t: lint_docs.Tree, num: str) -> list[str]:
    out = [f"[claim {num}]  {register(t, num)}  unverified underneath:"]
    listed: set[str] = set()
    for _, kind, n, _ in closure(t, num):
        if kind != "claim" or n in listed:
            continue
        listed.add(n)
        if n not in t.claims:
            out.append(f"  [claim {n}]  (resolves to no claim)")
            continue
        reg = register(t, n)
        vb = fields(t, t.claims[n]).get("Verified-by", (0, ""))[1]
        why = []
        if reg in ("OPEN", "SPECULATIVE"):
            why.append(reg)
        if reg == "RULED_OUT":
            why.append("RULED_OUT, reported always (ONTOLOGY.md section 4)")
        if vb.split(",")[0].strip() in ("unchecked", "deferred"):
            why.append(f"Verified-by: {vb}")
        if why:
            out.append(f"  [claim {n}]  " + "; ".join(why))
        else:
            listed.discard(n)
    if len(out) == 1:
        out.append("  (none: no member is OPEN, SPECULATIVE, or RULED_OUT, none is unchecked or deferred, and every one resolves)")
    return out


def deferred(t: lint_docs.Tree) -> list[str]:
    out = ["Deferred to an instrument or party (Verified-by: deferred):"]
    for n, f in sorted(t.claims.items()):
        vb = fields(t, f).get("Verified-by", (0, ""))[1]
        if vb.split(",")[0].strip() == "deferred":
            out.append(f"  [claim {n}]  {register(t, n)}  {vb}")
    if len(out) == 1:
        out.append("  (none)")
    return out


def _cells(line: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def literature(t: lint_docs.Tree) -> list[str]:
    out = ["Against the public record (the tension ledger, caution as recorded):"]
    g = t.first_of_kind("ledger")
    if not g:
        out.append("  (no file matches the configured ledger row)")
        return out
    labels, rows = None, 0
    for line in t.prose(g).splitlines():
        if not line.startswith("|"):
            continue
        cells = _cells(line)
        if labels is None:
            if any("Caution" in c for c in cells):
                labels = cells
            continue
        m = re.match(r"^(T[0-9]{3,})$", cells[0])
        if not m:
            continue
        rows += 1
        claims = ", ".join(f"[claim {c}]" for c in lint_docs.TOKEN_CLAIM.findall(lint_docs.LINK_RE.sub(" ", line)))
        out.append(f"  [tension {m.group(1)}]  {claims or '(no claim token)'}")
        for label, cell in zip(labels[1:], cells[1:]):
            out.append(f"      {label}: {cell or '(empty)'}")
        if len(cells) < len(labels):
            out.append(f"      (the row has {len(cells)} cells; the header has {len(labels)})")
    out.append("  (no row: the ledger is empty)" if not rows else "  Whether a caution is still live is reading (PRECEDENCE.md; sweep item 8).")
    return out


def unfinished(t: lint_docs.Tree) -> list[str]:
    out = ["Plans by Status:"]
    for n, f in sorted(t.plans.items()):
        out.append(f"  plan {n}  {t.plan_status.get(f) or '(no Status)'}")
    if not t.plans:
        out.append("  (no plan)")
    out.append("Claims by register:")
    configured = list(t.cfg.get("vocab", {}).get("registers", []))
    by_reg: dict[str, list[str]] = {}
    for n, f in sorted(t.claims.items()):
        by_reg.setdefault(register(t, n), []).append(n)
    for reg in ORDERED:
        if reg in by_reg:
            out.append(f"  {reg}: " + ", ".join(f"[claim {n}]" for n in by_reg[reg]))
    for reg, ns in by_reg.items():
        if reg in ORDERED:
            continue
        why = "(configured, but not one ONTOLOGY.md section 4 orders)" if reg in configured else "(not in the configured vocabulary)"
        out.append(f"  {reg}: " + ", ".join(f"[claim {n}]" for n in ns) + f"   {why}")
    if not t.claims:
        out.append("  (no claim)")
    out.append("Reservations (Reserved stamps, by plan):")
    clusters: dict[str, list[str]] = {}
    for n, f in sorted(t.claims.items()):
        rp = claim_sites.reserved_plan(t, f)
        if rp:
            clusters.setdefault(rp, []).append(n)
    for rp, ns in sorted(clusters.items()):
        out.append(f"  plan {rp}: " + ", ".join(f"[claim {n}]" for n in ns))
    if not clusters:
        out.append("  (none)")
    out.append("Plans serving no hypothesis (Serves: none):")
    n_found = 0
    for n, f in sorted(t.plans.items()):
        sv = fields(t, f).get("Serves", (0, ""))[1]
        if sv.split(",")[0].strip() == "none":
            n_found += 1
            out.append(f"  plan {n}  Serves: {sv}")
    if not n_found:
        out.append("  (none)")
    return out


def not_claimed(t: lint_docs.Tree, f: str) -> str | None:
    """The section's text, whitespace collapsed; "" where the section is
    present and empty; None where the heading is absent."""
    m = re.search(r"^## What is not claimed[^\n]*\n(.*?)(?=^## |\Z)", t.prose(f), re.S | re.M)
    return " ".join(m.group(1).split()) if m else None


def sites(t: lint_docs.Tree) -> list[str]:
    out = ["Every place a claim or a check record cites a claim, in its header or its body (the comparison of rule six is reading):"]
    n_found = 0
    for f in sorted(t.files):
        kind = t.kind(f)
        if kind not in ("claim", "check") or t.is_template(f):
            continue
        own = t.num(f)
        own_reg = register(t, own) if kind == "claim" else "check"
        backs = lint_docs.TOKEN_CLAIM.findall(fields(t, f).get("Backs", (0, ""))[1]) if kind == "check" else []
        for i, line in enumerate(t.prose(f).splitlines(), 1):
            for n in lint_docs.TOKEN_CLAIM.findall(lint_docs.LINK_RE.sub(" ", line)):
                if kind == "claim" and n == own:
                    continue
                n_found += 1
                cited_reg = register(t, n) if n in t.claims else "(no such claim)"
                tag = "  (the claim it backs)" if n in backs else ""
                out.append(f"  {f}:{i}  [{own_reg}] cites [claim {n}] [{cited_reg}]{tag}")
                out.append(f"      citing: {line.strip()}")
                if n in t.claims:
                    nc = not_claimed(t, t.claims[n])
                    if nc is None:
                        out.append("      not claimed: (the cited claim has no What is not claimed section)")
                    else:
                        out.append(f"      not claimed: {nc or '(the section is present and empty)'}")
    if not n_found:
        out.append("  (no site)")
    return out


QUESTIONS = {"rests-on": (rests_on, True), "unverified": (unverified, True), "deferred": (deferred, False),
             "radius": (claim_sites.sites, True), "literature": (literature, False),
             "unfinished": (unfinished, False), "sites": (sites, False)}


def answer(t: lint_docs.Tree, q: str, num: str | None) -> list[str]:
    if q == "all":
        out = []
        for name, (fn, needs) in QUESTIONS.items():
            if not needs:
                out += fn(t) + [""]
        return out
    fn, needs = QUESTIONS[q]
    return fn(t, num) if needs else fn(t)


def selftest() -> int:
    failures = 0
    S = lint_docs.STAMP

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:700]})"))

    def claim(n, title, reg, verdict, plan, vb, extra="", body="x.", fence="\n\n## What is not claimed\n\nNothing more.\n"):
        return (f"# Claim {n}: {title}\n\n{S}\nRegister: {reg}\nKind: documentary\nVerdict: {verdict}\nPlan: {plan}, task 1\n"
                f"Verified-by: {vb}\n{extra}\n## Claim\n\n{body}{fence}")

    def check(n, title, plan):
        return f"# Check {n}: {title}\n\n{S}\nPlan: {plan}, task 1\nBacks: [claim {n}]\nInstrument: the edition\nMutation: variant-reading\n\n## 1\n\nThe claim [claim {n}] against [claim 002].\n"

    base = lint_docs.fixture()
    base["evidence_and_reasoning/claims/003_c.md"] = claim("003", "c", "VERIFIED", "confirmed", "001", "researcher",
        "Backed-by: [check 003]\nDepends-on: 001, 002, 005, 006, 007\nReserved 2 January 2026, plan 001\n",
        "This claim, [claim 003], rests on [claim 001], [claim 002], [claim 005], [claim 006], and [claim 007].",
        "\n\n## What is not claimed\n\nNothing about d.\n")
    base["evidence_and_reasoning/claims/004_d.md"] = claim("004", "d", "ATTESTED", "confirmed", "001", "deferred, the edition",
        "Reserved 2 January 2026, plan 001\nDepends-on: 003\n", "Says d [Key1, p. 4].", "\n\n## What is not claimed\n\n<!-- only the template's comment -->\n")
    base["evidence_and_reasoning/claims/005_e.md"] = claim("005", "e", "RULED_OUT", "not confirmed", "002", "researcher",
        "Backed-by: [check 005]\n", "Not e.", "\n\n## What is not claimed\n\nThat e never held.\n")
    base["evidence_and_reasoning/claims/006_f.md"] = claim("006", "f", "DERIVED", "confirmed", "002", "researcher",
        "Depends-on: 002\n", "Follows from [claim 002].", "")
    base["evidence_and_reasoning/claims/007_g.md"] = claim("007", "g", "SPECULATIVE", "none", "001", "deferred, the edition", "", "Perhaps g.", "")
    base["evidence_and_reasoning/checks/003_c.md"] = check("003", "c", "001")
    base["evidence_and_reasoning/checks/005_e.md"] = check("005", "e", "002")
    base["evidence_and_reasoning/claims/README.md"] += "".join(f"| [{n}]({n}_{s}.md) |\n" for n, s in (("003", "c"), ("004", "d"), ("005", "e"), ("006", "f"), ("007", "g")))
    base["evidence_and_reasoning/checks/README.md"] += "| [003](003_c.md) |\n| [005](005_e.md) |\n"

    def scratch(files, lint: bool):
        tmp = Path(tempfile.mkdtemp())
        lint_docs.scratch_project(tmp, files, lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        if lint:
            lint_docs.run_checks(tmp)
            case("the extended scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:4]))
        return load(tmp)

    t = scratch(base, lint=True)
    r = "\n".join(answer(t, "rests-on", "003"))
    case("rests-on walks Depends-on and Backed-by", "  [check 003]" in r and "  [claim 001]  OPEN" in r and "  [claim 002]  VERIFIED" in r, r)
    case("rests-on flags a weaker member", "[claim 001]  OPEN   FLAG: weaker" in r and "[claim 007]  SPECULATIVE   FLAG: weaker" in r, r)
    case("rests-on flags a RULED_OUT member always", "[claim 005]  RULED_OUT   FLAG: RULED_OUT" in r, r)
    case("rests-on does not order DERIVED against VERIFIED", "[claim 006]  DERIVED\n" in r + "\n", r)
    case("rests-on nests each member's subtree under it", "  [claim 001]  OPEN   FLAG: weaker than the VERIFIED claim relying on it (ONTOLOGY.md section 4)\n    [check 001]\n  [claim 002]" in r, r)
    case("rests-on marks a member reached twice", "    [claim 002]  VERIFIED   (listed above)" in r, r)
    r = "\n".join(answer(t, "rests-on", "004"))
    case("rests-on walks transitively", "  [claim 003]  VERIFIED" in r and "      [check 001]" in r, r)
    case("a stronger member under a weaker claim is not flagged", "[claim 003]  VERIFIED   FLAG" not in r, r)
    r = "\n".join(answer(t, "unverified", "004"))
    case("unverified keeps OPEN and SPECULATIVE members and drops the rest", "[claim 001]  OPEN; Verified-by: unchecked" in r and "[claim 007]  SPECULATIVE; Verified-by: deferred, the edition" in r and "[claim 002]" not in r and "[claim 006]" not in r, r)
    case("unverified reports a RULED_OUT member always", "[claim 005]  RULED_OUT, reported always" in r, r)
    r = "\n".join(answer(t, "unverified", "006"))
    case("unverified says when there is nothing", "(none: no member is OPEN" in r, r)
    r = "\n".join(answer(t, "deferred", None))
    case("deferred lists each deferral with its instrument", "[claim 004]  ATTESTED  deferred, the edition" in r and "[claim 007]  SPECULATIVE  deferred, the edition" in r, r)
    r = "\n".join(answer(t, "radius", "002"))
    case("radius is the blast radius of claim_sites", "Not seen here" in r and "[claim 003]  VERIFIED" in r, r)
    r = "\n".join(answer(t, "literature", None))
    case("literature lists a row with its claim token and every column", "[tension T001]  [claim 002]" in r and "What this project establishes: [claim 002]" in r and "Caution (live, or closed D Month YYYY): live" in r, r)
    r = "\n".join(answer(t, "unfinished", None))
    case("unfinished lists plans by status", "plan 001  ENGAGED 1 January 2026" in r and "plan 002  CLOSED" in r, r)
    case("unfinished lists claims by register", "OPEN: [claim 001]" in r and "RULED_OUT: [claim 005]" in r and "DERIVED: [claim 006]" in r, r)
    case("unfinished lists reservations by plan", "plan 001: [claim 003], [claim 004]" in r, r)
    case("unfinished lists Serves: none with the reason", "plan 001  Serves: none, setup" in r, r)
    r = "\n".join(answer(t, "sites", None))
    case("sites lists a claim citing a claim with both registers", "claims/003_c.md:" in r and "[VERIFIED] cites [claim 001] [OPEN]" in r, r)
    case("sites quotes the cited claim's What is not claimed in full", "not claimed: That e never held." in r, r)
    case("sites says when the cited claim has no such section", "cites [claim 001] [OPEN]\n      citing: This claim" in r and "has no What is not claimed section" in r, r)
    case("sites says when the section is present and empty", "cites [claim 004] [ATTESTED]" not in r or "(the section is present and empty)" in r, r)
    case("sites lists a check record's header and body citations and marks the claim it backs",
         "checks/003_c.md:5  [check] cites [claim 003] [VERIFIED]  (the claim it backs)" in r and "checks/003_c.md:11  [check] cites [claim 003]" in r, r)
    case("sites does not list a claim's own token", "[VERIFIED] cites [claim 003]" not in r and "[check] cites [claim 003] [VERIFIED]  (the claim it backs)" in r, r)
    r = "\n".join(answer(t, "all", None))
    case("all answers every question that takes no claim", all(k in r for k in ("Deferred", "Against the public record", "Plans by Status", "Every place")), r)
    try:
        answer(t, "rests-on", "042")
        case("an unknown claim is refused", False)
    except KeyError:
        case("an unknown claim is refused", True)
    try:
        answer(t, "bogus", None)
        case("an unknown question is refused", False)
    except KeyError:
        case("an unknown question is refused", True)

    # a second tree the linter rejects, for the branches a clean tree cannot reach
    rejected = lint_docs.fixture()
    rejected["evidence_and_reasoning/claims/003_c.md"] = claim("003", "c", "PROVEN", "confirmed", "001", "researcher",
        "Backed-by: [check 042]\nDepends-on: 001, 003, 042\n", "x.", "")
    rejected["evidence_and_reasoning/claims/004_d.md"] = claim("004", "d", "VERIFIED", "confirmed", "001", "researcher",
        "Backed-by: [check 002]\nDepends-on: 003\n", "Cites [claim 004] itself.", "\n\n## What is not claimed\n\nSection kept.\n")
    rejected["evidence_and_reasoning/claims/README.md"] += "| [003](003_c.md) |\n| [004](004_d.md) |\n"
    rejected["evidence_and_reasoning/public_record_tensions.md"] = base["evidence_and_reasoning/public_record_tensions.md"].replace(
        "| T001 | [claim 002] | [Key1] | x | live |", "| T001 | [claim 002](../claims/002_b.md) | [Key1] | x | |")
    t = scratch(rejected, lint=False)
    r = "\n".join(answer(t, "rests-on", "004"))
    case("on a tree the linter rejects: a register outside the vocabulary is said to be unordered", "[claim 003]  PROVEN   (Register 'PROVEN' is not one section 4 orders)" in r, r)
    case("on a tree the linter rejects: a Depends-on naming no claim is said so", "[claim 042]   (resolves to no claim)" in r, r)
    case("on a tree the linter rejects: a Backed-by naming no check is said so", "[check 042]   (resolves to no check)" in r, r)
    case("on a tree the linter rejects: a cycle names itself", "[claim 003]" in r and "(listed above)" in r, r)
    r = "\n".join(answer(t, "rests-on", "003"))
    case("on a tree the linter rejects: a self-dependency is a cycle", "(the claim itself: a cycle)" in r, r)
    r = "\n".join(answer(t, "unverified", "004"))
    case("on a tree the linter rejects: unverified lists the unresolved dependency", "[claim 042]  (resolves to no claim)" in r, r)
    r = "\n".join(answer(t, "literature", None))
    case("a linked token in a ledger row is not read, and an empty caution is said", "(no claim token)" in r and "): (empty)" in r, r)
    r = "\n".join(answer(t, "unfinished", None))
    case("a register outside the configured vocabulary is said so", "PROVEN: [claim 003]   (not in the configured vocabulary)" in r, r)
    empty = lint_docs.fixture()
    empty["evidence_and_reasoning/public_record_tensions.md"] = "\n".join(l for l in empty["evidence_and_reasoning/public_record_tensions.md"].splitlines() if not l.startswith("| T001")) + "\n"
    t = scratch(empty, lint=False)
    r = "\n".join(answer(t, "literature", None))
    case("an empty ledger says so", "(no row: the ledger is empty)" in r, r)
    r = "\n".join(answer(t, "rests-on", "001"))
    case("a claim with nothing under it says so", "(nothing: no Depends-on, no Backed-by)" in r or "[check 001]" in r, r)
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if not argv or (argv[0] not in QUESTIONS and argv[0] != "all"):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    q = argv[0]
    needs = q != "all" and QUESTIONS[q][1]
    if needs and (len(argv) != 2 or not re.fullmatch(lint_docs.NUM, argv[1])) or (not needs and len(argv) != 1):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        t = load(ROOT)
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"query_ontology: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    try:
        print("\n".join(answer(t, q, argv[1] if needs else None)))
    except KeyError as e:
        print(f"query_ontology: no claim numbered {e.args[0]} under the configured claim pattern", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

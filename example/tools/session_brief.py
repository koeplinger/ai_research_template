#!/usr/bin/env python3
"""The session brief: the reading order, the plans by status, and the reminders the record can compute, printed at the start of a session and on demand.

Created 5 September 2026; updated 5 September 2026.

What every session reads first is ONBOARDING.md; this program prints its
reading order verbatim, then every plan with its Status: line and the
count of those ENGAGED, then the standing reminders of MANIFESTO.md
section 16 that the record itself can compute (governance/reminders.md
names them and says what each does not decide):

  log-the-prompt-first      no entry of this round is open under the log
                            (section 8): the latest entry is committed
  more-than-one-plan-engaged  the plan index shows more than one ENGAGED
                            plan (research_plans/README.md)
  plan-closure-checklist    an ENGAGED plan whose execution ledger has
                            every task done or dropped: it stays ENGAGED
                            until the researcher closes it
  sweep-after-correction    a frozen artifact differs from its committed
                            version: a consistency sweep closes the batch
                            (CHECK_METHODOLOGY.md section 7)
  findings-gate             a claim registered VERIFIED or RULED_OUT that
                            no row of the findings file cites: bring the
                            finding and its wording (section 12)
  verification-not-recorded  a claim registered beyond OPEN or SPECULATIVE
                            whose Verified-by is unchecked

Advisory: it prints, and decides nothing.  A harness that can run a
command at session start runs this one; the wiring is recorded under
governance/harness/.  The execution ledger is read as the plan template
lays it out: a table whose header names a State column.  A frozen
artifact counts as corrected when its body differs from its committed
version; a header-only change is bookkeeping (DOCUMENT_GENRES.md).

Usage
    python3 tools/session_brief.py               the brief
    python3 tools/session_brief.py --reminders   the reminders alone
    python3 tools/session_brief.py --selftest

Exit status: 0 the brief printed; 2 a usage error, or tools/artifacts.toml
unreadable.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def reading_order(t: lint_docs.Tree) -> list[str]:
    """The indented block under "The first minutes" of the onboarding file."""
    f = t.first_of_kind("onboarding")
    if not f:
        return ["  (no onboarding file under the configured row)"]
    lines, inside, out = t.text[f].splitlines(), False, []
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = "first minutes" in line.lower()
            continue
        if not inside:
            continue
        if line.startswith(("    ", "\t")):
            out.append(line.replace("\t", "    ", 1))
        elif out and not line.strip():
            out.append("")
        elif out:
            break
    while out and not out[-1]:
        out.pop()
    return out or [f"  (no indented reading order under a 'first minutes' heading of {f})"]


def plans(t: lint_docs.Tree) -> tuple[list[str], int]:
    out, engaged = [], 0
    for n, f in sorted(t.plans.items()):
        st = t.plan_status.get(f) or "(no Status)"
        engaged += st.startswith("ENGAGED")
        out.append(f"  plan {n}  {st}")
    return out or ["  (no plan)"], engaged


def fields(t: lint_docs.Tree, f: str) -> dict[str, tuple[int, str]]:
    return lint_docs.fields_of(t.headers[f][0]) if f in t.headers else {}


def ledger_states(t: lint_docs.Tree, f: str) -> list[str]:
    """The State column of a plan's execution ledger, located by the
    table's header; empty where the plan has no ledger or no State column."""
    text = t.prose(f)
    m = re.search(r"^## Execution status[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return []
    states, col = [], None
    for line in m.group(1).splitlines():
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            col = next((i for i, c in enumerate(cells) if c.strip("*_ ").lower() == "state"), None)
            if col is None:
                return []
            continue
        if len(cells) > col:
            states.append(cells[col].lower())
    return states


def gone_frozen(t: lint_docs.Tree, f: str, row: dict) -> bool:
    """Whether a file gone from the tree was frozen, read from its committed
    header the way the linter derives a genre (ONTOLOGY.md section 3)."""
    if row["genre"] in ("frozen", "dated-record", "immutable"):
        return True
    old = lint_docs.git(t.root, "show", f"HEAD:{f}")
    if not old:
        return False
    hdr, _ = lint_docs.header_block(old, row.get("header", "stamp"))
    pl = lint_docs.fields_of(hdr).get("Plan")
    if pl and pl[1]:
        pf = t.plans.get(pl[1].split(",")[0].strip())
        return bool(pf) and t.plan_status.get(pf, "").startswith("CLOSED")
    return row["genre"] == "release" and any(s.startswith("Released ") for _, s in hdr)


def body_changed(t: lint_docs.Tree, f: str) -> bool:
    """Whether a tracked artifact's body differs from its committed version;
    a file gone from the tree (deleted, or renamed, which reads as a
    deletion beside an untracked file) counts as changed."""
    old = lint_docs.git(t.root, "show", f"HEAD:{f}")
    if f not in t.text:
        return bool(old)
    if not old or old == t.text[f]:
        return False
    hk = (t.rows[f] or {}).get("header", "stamp")
    _, ob = lint_docs.header_block(old, hk)
    _, nb = lint_docs.header_block(t.text[f], hk)
    return "\n".join(old.splitlines()[ob - 1:]) != "\n".join(t.text[f].splitlines()[nb - 1:])


def reminders(t: lint_docs.Tree) -> list[str]:
    out = []
    logdir = t.dir_of_kind("log-entry")
    entries = sorted(f for f in t.files if t.kind(f) == "log-entry")
    if logdir:
        if lint_docs.git(t.root, "rev-parse", "--verify", "HEAD"):
            # an entry is open while untracked or staged new; a committed entry edited is the linter's GENRES-2
            staged = lint_docs.git(t.root, "diff", "--name-only", "-z", "--diff-filter=A", "HEAD", "--", logdir + "/")
            new = lint_docs.git(t.root, "ls-files", "--others", "--exclude-standard", "-z", "--", logdir + "/")
            open_entries = [f for f in (staged + new).split("\0") if f and t.kind(f) == "log-entry"]
        else:
            open_entries = entries
        if not open_entries:
            latest = Path(entries[-1]).name if entries else None
            out.append("REMINDER  log-the-prompt-first: no entry of this round is open under " + logdir + "/"
                       + (f"; the latest, {latest}, is committed" if latest else "; the log is empty, so this round's entry is 001")
                       + " (MANIFESTO.md section 8: the entry is the first act of the round)")
    engaged = [n for n, f in sorted(t.plans.items()) if (t.plan_status.get(f) or "").startswith("ENGAGED")]
    if len(engaged) > 1:
        out.append("REMINDER  more-than-one-plan-engaged: " + ", ".join(f"plan {n}" for n in engaged)
                   + " (research_plans/README.md: say so in the reply while it is true)")
    for n in engaged:
        states = ledger_states(t, t.plans[n])
        if states and all(re.fullmatch(r"(done|dropped)(,.*)?", s) for s in states):
            out.append(f"REMINDER  plan-closure-checklist: plan {n} has every task done or dropped; it stays ENGAGED until the researcher closes it, and the checklist is governance/reminders.md")
    frozen_changed = []
    if lint_docs.git(t.root, "rev-parse", "--verify", "HEAD"):
        for f in [x for x in lint_docs.git(t.root, "diff", "--name-only", "-z", "HEAD").split("\0") if x]:
            row = t.rows.get(f) if f in t.rows else lint_docs.classify(t.cfg, f)
            if not row or row.get("header", "stamp") == "none":
                continue
            if f not in t.text:
                if gone_frozen(t, f, row) and body_changed(t, f):
                    frozen_changed.append(f + " (gone from the tree)")
            elif t.genre(f) == "frozen" and body_changed(t, f):
                frozen_changed.append(f)
    if frozen_changed:
        out.append("REMINDER  sweep-after-correction: the body of a frozen artifact differs from its committed version: " + ", ".join(frozen_changed)
                   + " (CHECK_METHODOLOGY.md section 7: a consistency sweep closes every correction batch)")
    fnd = t.first_of_kind("findings")
    cited = set(lint_docs.TOKEN_CLAIM.findall(lint_docs.LINK_RE.sub(" ", t.prose(fnd)))) if fnd else set()
    established = [n for n, f in sorted(t.claims.items()) if fields(t, f).get("Register", (0, ""))[1] in ("VERIFIED", "RULED_OUT") and n not in cited]
    if established:
        out.append("REMINDER  findings-gate: established and cited by no findings row: " + ", ".join(f"[claim {n}]" for n in established)
                   + " (MANIFESTO.md section 12: bring the finding and its wording, and stop)")
    unchecked = [n for n, f in sorted(t.claims.items())
                 if fields(t, f).get("Register", (0, ""))[1] not in ("OPEN", "SPECULATIVE", "")
                 and fields(t, f).get("Verified-by", (0, ""))[1].split(",")[0].strip() == "unchecked"]
    if unchecked:
        out.append("REMINDER  verification-not-recorded: registered beyond OPEN yet Verified-by unchecked: " + ", ".join(f"[claim {n}]" for n in unchecked)
                   + " (MANIFESTO.md section 5)")
    return out or ["  (no reminder the record can compute; the rest are the assistant's by reading)"]


def brief(t: lint_docs.Tree) -> list[str]:
    out = ["Reading order (ONBOARDING.md):"] + reading_order(t) + [""]
    lines, engaged = plans(t)
    out += [f"Plans ({engaged} engaged):"] + lines + ["", "Reminders (MANIFESTO.md section 16):"] + reminders(t)
    return out


def selftest() -> int:
    failures = 0
    S = lint_docs.STAMP

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:500]})"))

    def w(tmp: Path, rel: str, body: str) -> None:
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text(body)

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        files = lint_docs.fixture()
        files["ONBOARDING.md"] = f"# On\n\n{S}\n\n## The first minutes\n\n    ONBOARDING.md\n      -> MANIFESTO.md\n\nText.\n\n## Next\n\n    not this\n"
        p1 = "evidence_and_reasoning/research_plans/001_a.md"
        files[p1] = files[p1].replace("| 1 | done |", "| 1 | done |\n| 2 | not started |")
        lint_docs.scratch_project(tmp, files, lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        lint_docs.run_checks(tmp)
        case("the scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:3]))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(brief(t))
        case("the reading order is the onboarding file's indented block, and nothing after it", "    ONBOARDING.md\n      -> MANIFESTO.md" in r and "not this" not in r, r)
        case("plans are listed by status with the count engaged", "Plans (1 engaged):" in r and "plan 001  ENGAGED 1 January 2026" in r and "plan 002  CLOSED" in r, r)
        case("with the log committed, the round's entry is not yet open", "log-the-prompt-first" in r and "001_setup.md, is committed" in r, r)
        case("one engaged plan raises no multiple-engagement reminder", "more-than-one-plan-engaged" not in r, r)
        case("a plan with an unstarted task is not ready to close", "plan-closure-checklist" not in r, r)
        w(tmp, "prompt_logs/002_next.md", f"# Prompt 002: next\n\n{S}\n\n--- PROMPT START ---\nx\n--- PROMPT END ---\n\n## What was done\n\n## Corrections and departures\n\n## Closing status\n\n```\nDONE: x\n```\n")
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("an untracked entry silences the log reminder", "log-the-prompt-first" not in "\n".join(reminders(t)))
        subprocess.run(["git", "add", "prompt_logs/002_next.md"], cwd=tmp, capture_output=True)
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a staged new entry silences it too", "log-the-prompt-first" not in "\n".join(reminders(t)))
        subprocess.run(["git", "rm", "-q", "--cached", "prompt_logs/002_next.md"], cwd=tmp, capture_output=True)
        (tmp / "prompt_logs" / "002_next.md").unlink()
        w(tmp, "prompt_logs/001_setup.md", files["prompt_logs/001_setup.md"] + "\nedited after commit\n")
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a committed entry edited is the linter's, not an open entry", "log-the-prompt-first" in "\n".join(reminders(t)))
        w(tmp, "prompt_logs/001_setup.md", files["prompt_logs/001_setup.md"])
        w(tmp, "ONBOARDING.md", f"# On\n\n{S}\n\n## The First Minutes, in short\n\n\tONBOARDING.md\n\n\t  -> MANIFESTO.md\nprose after\n\n    not this either\n")
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(brief(t))
        case("the reading order accepts a tab, keeps a blank line inside the block, and ends at the first prose line", "    ONBOARDING.md\n\n      -> MANIFESTO.md\n\nPlans" in r and "not this either" not in r, r)
        w(tmp, "ONBOARDING.md", files["ONBOARDING.md"])
        w(tmp, "evidence_and_reasoning/research_plans/003_c.md", files[p1].replace("Plan 001: a", "Plan 003: c"))
        w(tmp, p1, files[p1].replace("| 2 | not started |", "| 2 | dropped |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("two engaged plans are named", "more-than-one-plan-engaged: plan 001, plan 003" in r, r)
        case("an engaged plan with every task done or dropped is reported ready to close", "plan-closure-checklist: plan 001" in r, r)
        p3 = "evidence_and_reasoning/research_plans/003_c.md"
        w(tmp, p3, files[p1].replace("Plan 001: a", "Plan 003: c").replace("| Task | State |\n|---|---|\n| 1 | done |\n| 2 | not started |", "| Task | Date | State |\n|---|---|---|\n| 1 | | done |\n| 2 | | dropped |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("the State column is found by the ledger's header, wherever it stands", "plan-closure-checklist: plan 003" in r, r)
        w(tmp, p3, files[p1].replace("Plan 001: a", "Plan 003: c").replace("| Task | State |\n|---|---|\n| 1 | done |\n| 2 | not started |", "| Task | **State** |\n|:---|:---:|\n| 1 | done |\n| 2 | dropped, entry 004 |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("an aligned separator, an emphasized header, and a drop naming its entry are read", "plan-closure-checklist: plan 003" in "\n".join(reminders(t)))
        w(tmp, p3, files[p1].replace("Plan 001: a", "Plan 003: c").replace("| 2 | not started |", "| 2 | done (partly) |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a state outside the vocabulary is not done", "plan-closure-checklist: plan 003" not in "\n".join(reminders(t)))
        w(tmp, p3, files[p1].replace("Plan 001: a", "Plan 003: c").replace("| Task | State |", "| Task | Progress |").replace("| 2 | not started |", "| 2 | dropped |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a ledger without a State column raises no closure reminder", "plan-closure-checklist: plan 003" not in "\n".join(reminders(t)))
        w(tmp, p3, files[p1].replace("Plan 001: a", "Plan 003: c").split("## Execution status")[0])
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a plan without an execution ledger raises no closure reminder", "plan-closure-checklist: plan 003" not in "\n".join(reminders(t)))
        c2 = "evidence_and_reasoning/claims/002_b.md"
        w(tmp, c2, files[c2].replace("updated 1 January 2026", "updated 3 January 2026"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        case("a header-only change to a frozen artifact is bookkeeping, not a correction", "sweep-after-correction" not in "\n".join(reminders(t)))
        w(tmp, c2, files[c2] + "\nA correction.\n")
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("a changed frozen body calls for the sweep", "sweep-after-correction: the body of a frozen artifact differs from its committed version: " + c2 in r, r)
        (tmp / c2).unlink()
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("a frozen artifact gone from the tree calls for the sweep", c2 + " (gone from the tree)" in r, r)
        w(tmp, c2, files[c2])
        w(tmp, "FINDINGS.md", files["FINDINGS.md"].replace("| F001 | x [claim 002] |", "| F001 | x [claim 001] |"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("an established claim no findings row cites is the findings gate", "findings-gate: established and cited by no findings row: [claim 002]" in r, r)
        w(tmp, c2, files[c2].replace("Verified-by: researcher", "Verified-by: unchecked"))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("a claim registered beyond OPEN and unchecked is reported", "verification-not-recorded: registered beyond OPEN yet Verified-by unchecked: [claim 002]" in r, r)
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        files = lint_docs.fixture()
        del files["prompt_logs/001_setup.md"]
        files["prompt_logs/README.md"] = files["prompt_logs/README.md"].replace("| [001](001_setup.md) |\n", "")
        lint_docs.scratch_project(tmp, files, lint_docs.scratch_config())
        lint_docs.scratch_commit(tmp)
        lint_docs.run_checks(tmp)
        case("the empty-log scratch tree is clean under the linter", not lint_docs.FINDINGS, str(lint_docs.FINDINGS[:3]))
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("an empty log says this round's entry is 001", "the log is empty, so this round's entry is 001" in r, r)
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        lint_docs.scratch_project(tmp, lint_docs.fixture(), lint_docs.scratch_config())
        subprocess.run(["git", "init", "-q"], cwd=tmp, capture_output=True)
        t = lint_docs.use(lint_docs.Tree(tmp, lint_docs.load_config(tmp)))
        r = "\n".join(reminders(t))
        case("a repository with no commit yet treats every entry as open and raises no log reminder", "log-the-prompt-first" not in r and "sweep-after-correction" not in r, r)
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    if argv and argv != ["--reminders"]:
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        t = lint_docs.use(lint_docs.Tree(ROOT, lint_docs.load_config(ROOT)))
    except (OSError, tomllib.TOMLDecodeError, KeyError) as e:
        print(f"session_brief: tools/artifacts.toml: {e}", file=sys.stderr)
        return 2
    print("\n".join(reminders(t) if argv else brief(t)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

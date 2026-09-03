#!/usr/bin/env python3
"""Check NNN: <title: what this check settles>.

Created D Month YYYY; updated D Month YYYY.
Plan: NNN, task M
Backs: [claim NNN]
Instrument: <name, and version | edition | release>
Frame: <what the quantities are stated in, and what fixes it; delete where there are none>
Mutation: <name[, name], each a member of the project's mutation set, bound in MUTATIONS below>
Robustness: <name[, name], disjoint from Mutation, or delete the line>
By: <party from the roster>

WHAT IS CHECKED: <one sentence>.  The full part 1, the construction, and
the results are in the record, evidence_and_reasoning/checks/NNN_short_name.md;
this docstring does not repeat them.

The header lines above are read by the tools (ONTOLOGY.md section 1.1):
one per line, name, colon, value, nothing after the value.  Delete the
angle-bracket placeholders in the instance.
"""
from __future__ import annotations

import sys

# ---------------------------------------------------------------------------
# Reporting.  Every substantive assertion goes through report(); the linter
# rejects a report whose condition is syntactically constant, because such
# a report passes whatever the computation does (CHECK_METHODOLOGY.md,
# section 5, "Show every assertion falsifiable").
# ---------------------------------------------------------------------------

FAILURES: list[str] = []
VALUES: dict[str, object] = {}


def report(name: str, ok: bool, detail: str = "") -> None:
    """Print one PASS/FAIL line and remember failures for the exit code."""
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def value(name: str, v: object) -> object:
    """Record a named value for the RESULT line; the record states the same."""
    VALUES[name] = v
    return v


# One entry per name on the Mutation line: a function the probe applies to
# the object under test in a scratch copy, so the check can be shown to fail
# under it (CHECK_METHODOLOGY.md, section 5).  A name with no entry here is
# reported as unbound.
MUTATIONS: dict[str, "callable"] = {
    # "variant-reading": lambda obj: obj.with_reading("B"),
}


# ---------------------------------------------------------------------------
# Part 2: construction.  The explicit definitions, data, or text the check
# rests on; every parameter named with its domain; every convention fixed.
# Import a foundation module here rather than restating it.
# ---------------------------------------------------------------------------


def construct():
    """Build the object under test and return it."""
    raise NotImplementedError("part 2: construction")


# ---------------------------------------------------------------------------
# Part 3: sanity checks.  Before the substantive test: reduction to known
# cases, counts and magnitudes, conventions against the glossary.
# ---------------------------------------------------------------------------


def sanity(obj) -> None:
    # Example of a real assertion: the boolean depends on the computation.
    #   report("sanity: reduces to the known case", obj.reduce() == KNOWN)
    raise NotImplementedError("part 3: sanity checks")


# ---------------------------------------------------------------------------
# Part 4: the verification itself.  Each assertion is a report() whose
# boolean depends on the computation.  Every negative has a positive
# control the same search must find.  Every frame is fixed or agreed by a
# second route (CHECK_METHODOLOGY.md, section 5).
# ---------------------------------------------------------------------------


def verify(obj) -> None:
    # Example of a real assertion, with its value recorded for the RESULT
    # line so the record can state the same:
    #   report("main: the count is as claimed", value("count", obj.count()) == 12)
    # And a negative with its positive control (CHECK_METHODOLOGY.md, section 5):
    #   report("control: the search finds the planted instance", found(planted))
    #   report("negative: the search finds nothing else", not found(other))
    raise NotImplementedError("part 4: verification")


# ---------------------------------------------------------------------------
# Part 5: discrepancy analysis.  If anything disagrees: how much, where, in
# what pattern.  Printed, and reported where the pattern itself is a claim.
# ---------------------------------------------------------------------------


def discrepancies(obj) -> None:
    pass


# ---------------------------------------------------------------------------
# Part 6: summary and the RESULT line.  The verdict is in the vocabulary of
# the claim's kind (CHECK_METHODOLOGY.md, section 2):
#   formal: proved | disproved            computational: reproduced | not reproduced
#   empirical: compatible | in tension | refuted
#   inferential: identified as stated | assumption unsupported, and
#                replicated | not replicated  (two values, comma-separated)
#   documentary: confirmed | not confirmed
#   interpretive: supported | underdetermined | contradicted
#   internal-consistency: consistent | inconsistent
# For a two-valued kind the default below suffices.  For a three-valued kind
# set the verdict from WHICH assertions failed, not from how many.  The RESULT
# line is the machine-readable summary the concordance check compares with
# the record: RESULT: <verdict>; <name>=<value>; ...
# ---------------------------------------------------------------------------


def main() -> int:
    print(__doc__.splitlines()[0])
    obj = construct()
    sanity(obj)
    verify(obj)
    discrepancies(obj)
    verdict = "<verdict word>" if not FAILURES else "<failing verdict word>"
    print()
    print(f"  {len(FAILURES)} failure(s)" if FAILURES else "  all assertions passed")
    print("RESULT: " + verdict + "".join(f"; {k}={v}" for k, v in VALUES.items()))
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())

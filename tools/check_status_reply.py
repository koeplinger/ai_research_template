#!/usr/bin/env python3
"""The status-block check: does a reply end in the form MANIFESTO.md section 16 fixes?

Created 5 September 2026; updated 5 September 2026.

The form is the section's: the block is the run of status lines at the
end of the reply, trailing whitespace ignored; a status line is one of
the four labels, a colon, a space, and at least one further character,
with no markup around the label; IDLE stands alone.  Two readings this
program makes are its own and are stated here: a line is a line at a
newline only, whatever the harness shows; and a status line that stands
above the block, separated from it by blank lines, is reported, since the
section admits no blank line inside the block and a line so placed is
read as prose by anyone who reads only the end.  The program checks the
form and nothing else; that every line is true is the assistant's duty.

It knows no harness.  The wiring that runs it after each reply is
{{REPLY_HOOK}}, recorded where the harness configuration lives; that
wiring hands the reply text to this program and maps its exit status to
whatever the harness does with a bounced reply.

Usage
    python3 tools/check_status_reply.py REPLY.txt    the reply in a file
    ... | python3 tools/check_status_reply.py        the reply on standard input
    python3 tools/check_status_reply.py --selftest   accepting and rejecting cases

Exit status: 0 the block conforms; 1 it does not, each reason on standard
output; 2 a usage error.
"""
from __future__ import annotations

import re
import sys

LABELS = ("DONE", "RUNNING", "WAITING ON YOU", "IDLE")
STATUS_LINE = re.compile(r"^(DONE|RUNNING|WAITING ON YOU|IDLE): .+$")
NEAR_LABEL = re.compile(r"(\*\*|`|_|#+\s*)?(DONE|RUNNING|WAITING ON YOU|IDLE)(\*\*|`|_)?\s*:", re.I)


def lines_of(text: str) -> list[str]:
    """The reply's lines, broken at newlines only, trailing whitespace and
    trailing blank lines dropped."""
    text = text.replace("\r\n", "\n").replace("\r", "\n").rstrip()
    return [l.rstrip() for l in text.split("\n")] if text else []


def block_of(text: str) -> list[str]:
    """The run of status lines at the end of the reply; empty when the last
    line is not a status line."""
    block: list[str] = []
    for line in reversed(lines_of(text)):
        if STATUS_LINE.match(line):
            block.insert(0, line)
        else:
            break
    return block


def check(text: str) -> list[str]:
    """Every way the reply fails the form; empty when it conforms."""
    lines = lines_of(text)
    if not lines:
        return ["the reply is empty"]
    block = block_of(text)
    if not block:
        last = lines[-1]
        hint = " (a label in the wrong case, with markup around it, or without the colon, the space, and text after them)" if NEAR_LABEL.search(last) else ""
        return [f"the last line is not a status line{hint}: {last[:80]!r}"]
    problems = []
    labels = [STATUS_LINE.match(l).group(1) for l in block]
    if "IDLE" in labels and len(block) > 1:
        problems.append("IDLE stands in a block of more than one line; IDLE appears only alone")
    above = lines[:len(lines) - len(block)]
    while above and not above[-1]:
        above.pop()
    if len(above) < len(lines) - len(block) and above and STATUS_LINE.match(above[-1]):
        problems.append(f"a status line stands above a blank line, outside the block; the block admits no blank line inside it: {above[-1][:60]!r}")
    return problems


def selftest() -> int:
    cases = [
        ("one DONE line", "Did the thing.\n\nDONE: the thing\n", True),
        ("DONE and WAITING ON YOU", "Text.\n\nDONE: a\nWAITING ON YOU: b\n", True),
        ("RUNNING beside DONE", "DONE: a\nRUNNING: the probe, five minutes\n", True),
        ("IDLE alone", "All quiet.\n\nIDLE: nothing running; waiting for the next prompt\n", True),
        ("trailing whitespace and blank lines", "DONE: a   \n\n\n   \n", True),
        ("two DONE lines", "DONE: a\nDONE: b\n", True),
        ("prose, a blank line, then the block", "Some prose.\n\nDONE: now\n", True),
        ("a label with two spaces after the colon", "DONE:  a\n", True),
        ("text after the label that contains a colon", "DONE: x: y\n", True),
        ("Windows line endings", "Text.\r\n\r\nDONE: a\r\n", True),
        ("a reply that is only a status block", "DONE: a\n", True),
        ("a paragraph separator inside the last line is not a line break", "DONE: amore\n", True),
        ("no block at all", "Did the thing and that is all.\n", False),
        ("prose ending in a label word", "It is done.\n", False),
        ("prose after the block", "DONE: a\n\nLet me know.\n", False),
        ("a lower-case label", "Done: a\n", False),
        ("a bold label", "**DONE:** a\n", False),
        ("a backticked label", "`DONE`: a\n", False),
        ("no space after the colon", "DONE:a\n", False),
        ("nothing after the label", "DONE: \n", False),
        ("IDLE beside DONE", "DONE: a\nIDLE: b\n", False),
        ("IDLE beside RUNNING", "IDLE: a\nRUNNING: b\n", False),
        ("IDLE beside WAITING ON YOU", "WAITING ON YOU: a\nIDLE: b\n", False),
        ("two IDLE lines", "IDLE: a\nIDLE: b\n", False),
        ("a status line above a blank line, then the block", "WAITING ON YOU: earlier\n\nDONE: now\n", False),
        ("a fence closing the reply", "```\nDONE: a\n```\n", False),
        ("an indented label", "  DONE: a\n", False),
        ("an unknown label", "FINISHED: a\n", False),
        ("an empty reply", "\n\n", False),
    ]
    failures = 0
    for name, text, expect_ok in cases:
        problems = check(text)
        ok = (not problems) == expect_ok
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {'accepts' if expect_ok else 'rejects'} {name}"
              + ("" if ok else f"   (got: {problems})"))
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if len(argv) > 1 or (argv and argv[0].startswith("--")):
        print(__doc__.split("Usage")[1], file=sys.stderr)
        return 2
    try:
        raw = open(argv[0], "rb").read() if argv else sys.stdin.buffer.read()
    except OSError as e:
        print(f"check_status_reply: {e}", file=sys.stderr)
        return 2
    problems = check(raw.decode("utf-8", errors="replace"))
    for p in problems:
        print(f"status block: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

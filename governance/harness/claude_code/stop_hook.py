#!/usr/bin/env python3
"""The stop hook for one harness: the reply's final text handed to tools/check_status_reply.py, and a non-conforming reply bounced.

Created 5 September 2026; updated 5 September 2026.

This is the wiring MANIFESTO.md section 16 calls {{REPLY_HOOK}}, for a
command-line harness that runs a command when the assistant stops and
hands it, on standard input, a JSON object naming the session's
transcript.  The hook reads the transcript, takes the assistant's text
after the last user prompt or tool result, which is where the block must
stand, and hands it to tools/check_status_reply.py; where the block does
not conform it prints the reasons on standard error and exits 2, which
this harness treats as "do not stop: read the reasons and reply again".
When the object says the hook is already active for this stop (the reply
being judged was itself produced after a bounce), it exits 0, so no
reply is bounced twice.  A transcript it cannot read, a hook object it
cannot parse, or a checker it cannot import is not a reason to bounce: it
exits 0 and says why on standard error.  A stop with no text after the
last prompt or tool result is let through too, and said so: the harness
may fire the hook before the final text is in the transcript, and a
bounce of a conforming reply would cost the researcher a repeated reply;
the form is then the assistant's duty (section 16).

The transcript is one JSON record per line, the lines broken at newlines
only, since a record's text may carry other line separators; a record of
type "assistant" carries a message whose content is a list of blocks,
one of which may be text; a record marked as a sidechain belongs to a
subagent and is not the reply.  The harness's settings file, .claude/settings.json at the
repository root, names this hook; governance/harness/claude_code/README.md
says how it is installed and removed.

Usage
    python3 governance/harness/claude_code/stop_hook.py            reads the hook object on standard input
    python3 governance/harness/claude_code/stop_hook.py --selftest
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
try:
    import check_status_reply  # noqa: E402
except ImportError:
    check_status_reply = None


def final_reply(transcript: Path) -> str:
    """The assistant's text since the last user record, main thread only."""
    texts: list[str] = []
    for line in reversed(transcript.read_text(encoding="utf-8-sig", errors="replace").split("\n")):
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(rec, dict) or rec.get("isSidechain"):
            continue
        kind = rec.get("type")
        if kind == "user":
            break
        if kind != "assistant":
            continue
        msg = rec.get("message")
        content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(content, str):
            texts.append(content)
        elif isinstance(content, list):
            for block in reversed(content):
                if isinstance(block, dict) and block.get("type") == "text" and block.get("text"):
                    texts.append(block["text"])
    return "\n".join(reversed(texts))


def decide_raw(raw: str) -> tuple[int, str]:
    """The hook object as read from standard input, decided."""
    try:
        hook = json.loads(raw or "{}")
    except json.JSONDecodeError as e:
        return 0, f"stop hook: the hook object is not JSON ({e}); nothing checked"
    if not isinstance(hook, dict):
        return 0, "stop hook: the hook object is not an object; nothing checked"
    return decide(hook)


def decide(hook: dict) -> tuple[int, str]:
    """(exit status, what to say on standard error)."""
    if hook.get("stop_hook_active") is True:
        return 0, ""
    if check_status_reply is None:
        return 0, "stop hook: tools/check_status_reply.py is not importable; nothing checked"
    path = hook.get("transcript_path")
    if not isinstance(path, str) or not path or not Path(path).is_file():
        return 0, "stop hook: no readable transcript in the hook object; nothing checked"
    try:
        text = final_reply(Path(path))
    except OSError as e:
        return 0, f"stop hook: transcript unreadable ({e}); nothing checked"
    if not text.strip():
        return 0, "stop hook: no text after the last prompt or tool result; nothing checked, and the form is the assistant's duty"
    problems = check_status_reply.check(text)
    if not problems:
        return 0, ""
    return 2, ("The reply's status block does not conform (MANIFESTO.md section 16): "
               + "; ".join(problems)
               + ". End the reply with one or more consecutive lines of the form DONE: ..., RUNNING: ..., WAITING ON YOU: ..., or IDLE: ..., IDLE only alone, nothing after them.")


def selftest() -> int:
    failures = 0

    def case(name: str, ok: bool, detail: str = "") -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"   ({detail[:400]})"))

    def rec(kind: str, blocks, side: bool = False) -> str:
        return json.dumps({"type": kind, "isSidechain": side, "message": {"role": kind, "content": blocks}})

    def transcript(tmp: Path, lines: list[str]) -> str:
        p = tmp / "t.jsonl"
        p.write_text("\n".join(lines) + "\n")
        return str(p)

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        good = [rec("user", [{"type": "text", "text": "do it"}]),
                rec("assistant", [{"type": "text", "text": "Starting."}]),
                rec("assistant", [{"type": "tool_use", "id": "1", "name": "Bash", "input": {}}]),
                rec("user", [{"type": "tool_result", "tool_use_id": "1", "content": "ok"}]),
                json.dumps({"type": "attachment"}),
                rec("assistant", [{"type": "thinking", "thinking": "..."}]),
                rec("assistant", [{"type": "text", "text": "Done with it.\n\nDONE: the thing"}]),
                rec("assistant", [{"type": "text", "text": "DONE: subagent chatter"}], side=True)]
        code, msg = decide({"transcript_path": transcript(tmp, good), "stop_hook_active": False})
        case("a conforming final reply passes", code == 0 and not msg, str((code, msg)))
        bad = good[:-2] + [rec("assistant", [{"type": "text", "text": "Done with it, let me know."}])]
        code, msg = decide({"transcript_path": transcript(tmp, bad), "stop_hook_active": False})
        case("a reply without a status block is bounced with the reasons", code == 2 and "not a status line" in msg and "section 16" in msg, str((code, msg)))
        case("text before the last tool result is not the reply", "Starting" not in final_reply(Path(transcript(tmp, bad))))
        split = good[:-2] + [rec("assistant", [{"type": "text", "text": "First part."}]), rec("assistant", [{"type": "text", "text": "DONE: second part"}])]
        case("a reply split over two records is joined in order", final_reply(Path(transcript(tmp, split))) == "First part.\nDONE: second part", final_reply(Path(transcript(tmp, split))))
        odd = good[:-2] + ["[1, 2]", json.dumps({"type": "assistant", "message": "a string, not an object"}),
                           json.dumps({"type": "assistant", "message": {"content": "DONE: as a plain string"}})]
        case("a non-object line, a string message, and a string content are read or skipped, never a crash",
             final_reply(Path(transcript(tmp, odd))) == "DONE: as a plain string", final_reply(Path(transcript(tmp, odd))))
        side = good[:-2] + [rec("assistant", [{"type": "text", "text": "DONE: x"}]), rec("assistant", [{"type": "text", "text": "no block here"}], side=True)]
        code, _ = decide({"transcript_path": transcript(tmp, side), "stop_hook_active": False})
        case("a subagent's record is not the reply", code == 0)
        code, msg = decide({"transcript_path": transcript(tmp, bad), "stop_hook_active": True})
        case("an active hook bounces nothing twice", code == 0 and not msg)
        code, msg = decide({"transcript_path": str(tmp / "missing.jsonl"), "stop_hook_active": False})
        case("a missing transcript is not a reason to bounce", code == 0 and "nothing checked" in msg, str((code, msg)))
        code, msg = decide({})
        case("an empty hook object is not a reason to bounce", code == 0)
        only_tools = good[:4]
        code, msg = decide({"transcript_path": transcript(tmp, only_tools), "stop_hook_active": False})
        case("a stop straight after a tool result is let through and said so", code == 0 and "no text" in msg, str((code, msg)))
        thinking = good[:4] + [rec("assistant", [{"type": "thinking", "thinking": "..."}])]
        code, msg = decide({"transcript_path": transcript(tmp, thinking), "stop_hook_active": False})
        case("a thinking-only tail is let through and said so", code == 0 and "no text" in msg, str((code, msg)))
        sep = good[:-2] + [rec("assistant", [{"type": "text", "text": "Done.\u2028\n\nDONE: x"}])]
        case("a line separator inside a record's text does not tear the record", final_reply(Path(transcript(tmp, sep))).endswith("DONE: x"), final_reply(Path(transcript(tmp, sep))))
        torn = good[:-1] + ['{"type": "assistant", "message": {"content": [{"type": "text", "te']
        code, _ = decide({"transcript_path": transcript(tmp, torn), "stop_hook_active": False})
        case("a last line torn mid-write is skipped, and the reply before it judged", code == 0)
        p = tmp / "crlf.jsonl"
        p.write_bytes(b"\xef\xbb\xbf" + "\r\n".join(good[:-1]).encode() + b"\r\n")
        code, msg = decide({"transcript_path": str(p), "stop_hook_active": False})
        case("a transcript with a byte-order mark and Windows line endings is read", code == 0 and not msg, str((code, msg)))
        two = good[:-2] + [rec("assistant", [{"type": "text", "text": "WAITING ON YOU: a\n\nDONE: b\nIDLE: c"}])]
        code, msg = decide({"transcript_path": transcript(tmp, two), "stop_hook_active": False})
        case("two reasons are joined legibly", code == 2 and "; a status line stands above" in msg and "IDLE stands in a block" in msg, msg)
        code, msg = decide({"transcript_path": transcript(tmp, bad), "stop_hook_active": "false"})
        case("only a true stop_hook_active flag counts as active", code == 2, str((code, msg)))
        code, msg = decide({"transcript_path": 123, "stop_hook_active": False})
        case("a transcript path that is not a string is not a reason to bounce", code == 0 and "no readable transcript" in msg, str((code, msg)))
        for raw, needle in (("[1, 2]", "not an object"), ("not json", "not JSON"), ("", "no readable transcript")):
            code, msg = decide_raw(raw)
            case(f"standard input {raw!r} is not a reason to bounce", code == 0 and needle in msg, str((code, msg)))
    print(f"\n  VERDICT: {'every case decided as expected' if not failures else f'{failures} failure(s)'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if argv == ["--selftest"]:
        return selftest()
    code, msg = decide_raw(sys.stdin.read())
    if msg:
        print(msg, file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

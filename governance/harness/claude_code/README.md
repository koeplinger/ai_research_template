# Harness wiring: Claude Code

*Created 5 September 2026; updated 8 September 2026.*

The wiring for one command-line harness, the one this template was built
with. It is the wiring a project records in the reply-hook slot
(`MANIFESTO.md` §16), and the session-start presentation of the reading
order, for which `ONBOARDING.md` defines no slot; nothing else. The rules
the hooks serve live in the rulebooks; this folder only says how this
harness runs the tools.

| File | What it does |
|---|---|
| [stop_hook.py](stop_hook.py) | When the assistant stops, reads the reply's final text from the session transcript and hands it to `tools/check_status_reply.py`; a non-conforming status block is bounced back to the assistant with the reasons (exit 2), a conforming one passes. It bounces nothing twice; a transcript it cannot read, and a stop with no text after the last prompt or tool result (the harness may fire the hook before the final text is written), are not reasons to bounce, and it says so. `--selftest` runs it on synthetic transcripts. |

The settings file the harness reads is [`.claude/settings.json`](../../../.claude/settings.json)
at the repository root, tracked so that a clone has the hooks without a
step. It names two hooks:

- **SessionStart** runs `tools/session_brief.py`, whose output the
  harness adds to the session's context: the reading order, the plans by
  status with the count engaged, and the reminders the record can
  compute.
- **Stop** runs `stop_hook.py`.

Both commands resolve the repository through the variable the harness
sets for its hooks, `CLAUDE_PROJECT_DIR`, and fall back to the working
directory; where neither holds the script, the command exits 0 and runs
nothing, so a missing script is never a bounce. The harness decides when a project's hooks may run (it asks
whether to trust the folder); that decision is the researcher's, and
where the hooks do not run, the form of §16 is the assistant's duty by
hand. The harness's per-user settings file, `.claude/settings.local.json`,
is git-ignored.

## What the hooks do not decide

The stop hook checks the form of the status block and nothing else: that
`RUNNING` names a live process and `DONE` something finished is the
assistant's duty (§16). The researcher sees the reply that was bounced as
well as the one that replaces it: the bounce produces the conforming
follow-up, it does not withhold the first. The session-start brief
prints; the reminders it cannot compute (a tension row brought and not
yet entered, a finding proposed and not yet brought) remain the
assistant's by reading, as `governance/reminders.md` says.

> **Build lens.** The log reminder is read under the build lens of
> `MANIFESTO.md` §8 and not acted on, since the build keeps no prompt log.

## Another harness

`../README.md`, *Adding a wiring, and removing one*, says what it costs.
That list lives one level up on purpose: a recipe for leaving this harness
should not be inside the folder it tells you to delete.

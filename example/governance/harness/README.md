# Harness wirings

*Created 5 September 2026; updated 6 September 2026.*

One folder per harness, each holding the commands that make that
harness run the template's tools at the moments the manifesto names:
after each reply (the reply hook of `MANIFESTO.md` §16) and at session
start (`ONBOARDING.md`). The tools themselves know no harness; a wiring
is a thin adapter from what the harness provides (a transcript, a hook
object, an environment variable) to what a tool reads (a reply on
standard input, a repository root).

| Folder | Harness |
|---|---|
| [claude_code/](claude_code/) | the command-line harness this template was built with; its settings file is `.claude/settings.json` at the repository root |

The template endorses no harness (`VISION.md`, *Non-goals and limits*).
A project adds a folder for its own, or keeps the form of §16 by hand and
records that in the slot.

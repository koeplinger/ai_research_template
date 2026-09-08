# Harness wirings

*Created 5 September 2026; updated 8 September 2026.*

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
One wiring ships because one had to; the rest of this file is what a
second costs.

## Adding a wiring, and removing one

A wiring does two things, and nothing in the tools has to change for it:
after each reply, hand the reply's text to `tools/check_status_reply.py`
and treat exit 1 as a non-conforming block; at session start, print
`tools/session_brief.py`. How the harness provides the reply, and what it
does with the verdict, is the adapter's business.

**To add one**, in the order the checks will notice:

1. a folder beside the others, named for the harness, holding its adapter
   and a `README.md` saying what the harness gives the adapter and what
   the adapter does not decide;
2. the harness's own settings or configuration file, wherever it reads it;
3. in `tools/artifacts.toml`: an `[[artifact]]` row for that settings path
   (the `harness-settings` row is the model), an `[[artifact]]` row for the
   adapter if it is not Python, and an `[[index]]` pair naming the new
   folder's README and what it lists;
4. in `.gitignore`: the harness's per-user settings file, if it has one,
   beside the line that names the shipped harness's;
5. a row in the table above;
6. the `{{REPLY_HOOK}}` slot, which is what a project answers to say which
   wiring it uses.

**To remove one**, the same list in reverse, and then delete the folder
and its settings file. **Do not delete `tools/check_status_reply.py`**:
the round check imports it, so ROUND-2 goes with it. A project whose
harness can run neither command keeps the form of `MANIFESTO.md` §16 by
hand and says so in the reply-hook slot; the checker still runs inside the
round check.

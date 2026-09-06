#!/usr/bin/env bash
# tools/install_hooks.sh: installs the local git hooks, since hooks are not
# cloned.  pre-commit runs, where a stop-word list exists at
# .privacy/stopwords.txt, the privacy scan over what is staged, and then the
# round check, tools/check_round.py, over the whole working tree, staged or
# not.  commit-msg runs the privacy scan over the message.  The privacy scan
# refuses the commit on a finding, since a leak into the history is hard to
# undo; the round check reports its findings and lets the commit proceed,
# as MANIFESTO.md section 13 has every check inform and the researcher
# decide, unless the hooks were installed with --strict.  A refusal names
# the override, git commit --no-verify, and asks that the commit message
# say why (MANIFESTO.md section 12).  A hook this script did not write is
# left alone unless --force is given; a hooks directory shared beyond this
# repository (core.hooksPath) is never written without --force.
#
# Created 5 September 2026; updated 5 September 2026.
#
# Usage
#   tools/install_hooks.sh              install pre-commit and commit-msg
#   tools/install_hooks.sh --strict     the round check refuses the commit too
#   tools/install_hooks.sh --force      replace hooks written by hand, or write
#                                       into a shared hooks directory
#   tools/install_hooks.sh --uninstall  remove the hooks this script wrote
#   tools/install_hooks.sh --selftest   in a throwaway repository: a clean
#                                       commit passes; a staged stop word and
#                                       one in the message are refused; a
#                                       linter finding is reported and the
#                                       commit proceeds, or is refused under
#                                       --strict; a foreign hook is left alone
#
# Exit status: 0 done; 1 refused, or a failed self-test; 2 not a repository,
# or python3 not found.
set -u

MARK="# installed by tools/install_hooks.sh"

hook_dir() {
  local root="$1" d
  d="$(git -C "$root" rev-parse --git-path hooks 2>/dev/null)" || return 1
  case "$d" in /*) printf '%s\n' "$d" ;; *) printf '%s/%s\n' "$root" "$d" ;; esac
}

shared_hook_dir() {
  # true when the hooks directory is set by core.hooksPath rather than the repository's own
  local root="$1"
  [ -n "$(git -C "$root" config --get core.hooksPath 2>/dev/null)" ]
}

write_pre_commit() {
  local strict="$1"
  cat <<EOF
#!/usr/bin/env bash
$MARK
# The privacy scan over what is staged, where a stop-word list exists; then
# the round check over the whole working tree, staged or not.
ROOT="\$(git rev-parse --show-toplevel)" || exit 2
cd "\$ROOT" || exit 2
command -v python3 >/dev/null || { echo "pre-commit: python3 not on PATH; no gate ran" >&2; exit 2; }
status=0
if [ -r .privacy/stopwords.txt ]; then
  python3 tools/privacy_scan.py --staged || status=1
fi
if ! python3 tools/check_round.py; then
  if [ "$strict" = "yes" ]; then
    status=1
  else
    echo "pre-commit: the round check reports the findings above over the working tree; the commit proceeds, and the decision is the researcher's (MANIFESTO.md section 13)" >&2
  fi
fi
if [ "\$status" -ne 0 ]; then
  echo "pre-commit: refused on the findings above; fix and retry, or commit with --no-verify and say why in the commit message (MANIFESTO.md sections 12 and 13)" >&2
fi
exit "\$status"
EOF
}

write_commit_msg() {
  cat <<EOF
#!/usr/bin/env bash
$MARK
# The privacy scan over the commit message, where a stop-word list exists.
ROOT="\$(git rev-parse --show-toplevel)" || exit 2
cd "\$ROOT" || exit 2
[ -r .privacy/stopwords.txt ] || exit 0
command -v python3 >/dev/null || { echo "commit-msg: python3 not on PATH; the scan did not run" >&2; exit 2; }
if ! python3 tools/privacy_scan.py --message "\$1"; then
  echo "commit-msg: refused on the findings above; reword, or commit with --no-verify and say why in the commit message (MANIFESTO.md sections 12 and 13)" >&2
  exit 1
fi
EOF
}

ours() { [ -f "$1" ] && grep -q -F "$MARK" "$1"; }

install() {
  local root="$1" force="$2" strict="$3" dir name target
  dir="$(hook_dir "$root")" || { echo "install_hooks: $root is not a git repository" >&2; return 2; }
  if shared_hook_dir "$root" && [ "$force" != "yes" ]; then
    echo "install_hooks: hooks for this repository live at $dir (core.hooksPath), shared beyond it; not written (use --force to write there anyway)"
    return 1
  fi
  command -v python3 >/dev/null || echo "install_hooks: python3 is not on PATH; the hooks will not run until it is" >&2
  mkdir -p "$dir"
  for name in pre-commit commit-msg; do
    target="$dir/$name"
    if [ -f "$target" ] && ! ours "$target" && [ "$force" != "yes" ]; then
      echo "install_hooks: $target exists and was not written by this script; left alone (use --force to replace it)"
      return 1
    fi
    case "$name" in pre-commit) write_pre_commit "$strict" > "$target" ;; commit-msg) write_commit_msg > "$target" ;; esac
    chmod +x "$target"
    echo "install_hooks: wrote $target"
  done
}

uninstall() {
  local root="$1" dir name target
  dir="$(hook_dir "$root")" || { echo "install_hooks: $root is not a git repository" >&2; return 2; }
  for name in pre-commit commit-msg; do
    target="$dir/$name"
    if ours "$target"; then rm -f "$target"; echo "install_hooks: removed $target"
    elif [ -f "$target" ]; then echo "install_hooks: $target was not written by this script; left alone"
    fi
  done
}

selftest() {
  local here tmp fails=0
  here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' RETURN
  local repo="$tmp/repo"
  python3 "$here/check_round.py" --scratch "$repo" > /dev/null || { echo "  [FAIL] could not write the scratch project"; return 1; }
  git -C "$repo" init -q
  git -C "$repo" -c user.name=t -c user.email=t@t add -A
  git -C "$repo" -c user.name=t -c user.email=t@t commit -q -m "scratch" || { echo "  [FAIL] scratch commit"; return 1; }
  install "$repo" no no > /dev/null || { echo "  [FAIL] install"; return 1; }
  local d; d="$(hook_dir "$repo")"
  [ -x "$d/pre-commit" ] && [ -x "$d/commit-msg" ] && echo "  [PASS] both hooks installed and executable" \
    || { echo "  [FAIL] hooks not installed"; fails=$((fails+1)); }

  commit_in() { git -C "$repo" -c user.name=t -c user.email=t@t commit -q -m "$1" >"$tmp/out" 2>&1; }
  add_all() { git -C "$repo" add -A; }
  reset_in() { git -C "$repo" reset -q --hard HEAD; git -C "$repo" clean -q -fdx -e .privacy; }
  # A token no shipped text carries, so a project's list is never tripped by the tools themselves.
  local word="w$(od -An -N4 -tx1 /dev/urandom | tr -d ' \n')"

  printf '\nA line.\n' >> "$repo/CURRENT_STATE.md"; add_all
  if commit_in "a clean change"; then echo "  [PASS] a clean commit passes"
  else echo "  [FAIL] a clean commit was refused:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1)); fi

  mkdir -p "$repo/.privacy"; printf '%s\n' "$word" > "$repo/.privacy/stopwords.txt"
  printf '\nAn %s.\n' "$word" >> "$repo/CURRENT_STATE.md"; add_all
  git -C "$repo" restore --worktree CURRENT_STATE.md   # the hit is staged only: the working tree is clean
  if commit_in "a change"; then echo "  [FAIL] a staged stop word was committed"; fails=$((fails+1))
  elif grep -q "privacy scan: FINDINGS ([0-9]*) in staged content" "$tmp/out"; then echo "  [PASS] a stop word staged, and only staged, is refused by the staged scan"
  else echo "  [FAIL] refused, but not by the staged scan:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1)); fi
  reset_in

  printf '\nAnother line.\n' >> "$repo/CURRENT_STATE.md"; add_all
  if commit_in "mention the $word"; then echo "  [FAIL] a stop word in the message was committed"; fails=$((fails+1))
  elif grep -q "in commit message" "$tmp/out"; then echo "  [PASS] a stop word in the commit message is refused"
  else echo "  [FAIL] refused, but not by the message scan:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1)); fi
  reset_in
  rm -rf "$repo/.privacy"

  printf '# M\n\nRules.\n' > "$repo/MANIFESTO.md"; add_all
  if ! commit_in "drop a stamp"; then echo "  [FAIL] a linter finding refused the commit under the default hook:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1))
  elif grep -q "GENRES-1" "$tmp/out" && grep -q "the commit proceeds" "$tmp/out"; then echo "  [PASS] a linter finding is reported and the commit proceeds"
  else echo "  [FAIL] committed, but the finding was not reported:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1)); fi
  git -C "$repo" reset -q --hard HEAD~1

  install "$repo" yes yes > /dev/null
  printf '# M\n\nRules.\n' > "$repo/MANIFESTO.md"; add_all
  if commit_in "drop a stamp"; then echo "  [FAIL] a linter finding was committed under --strict"; fails=$((fails+1))
  elif grep -q "GENRES-1" "$tmp/out"; then echo "  [PASS] under --strict a linter finding is refused"
  else echo "  [FAIL] refused, but not by the linter:"; sed 's/^/         /' "$tmp/out"; fails=$((fails+1)); fi
  reset_in

  printf '#!/bin/sh\nexit 0\n' > "$d/pre-commit"
  if install "$repo" no no > /dev/null; then echo "  [FAIL] a foreign hook was replaced without --force"; fails=$((fails+1))
  else echo "  [PASS] a foreign hook is left alone without --force"; fi
  install "$repo" yes no > /dev/null && ours "$d/pre-commit" && echo "  [PASS] --force replaces it" \
    || { echo "  [FAIL] --force did not replace it"; fails=$((fails+1)); }
  git -C "$repo" config core.hooksPath "$tmp/shared"
  if install "$repo" no no > /dev/null; then echo "  [FAIL] a shared hooks directory was written without --force"; fails=$((fails+1))
  else echo "  [PASS] a shared hooks directory (core.hooksPath) is left alone without --force"; fi
  git -C "$repo" config --unset core.hooksPath
  uninstall "$repo" > /dev/null
  [ ! -f "$d/pre-commit" ] && [ ! -f "$d/commit-msg" ] && echo "  [PASS] --uninstall removes what it wrote" \
    || { echo "  [FAIL] --uninstall left a hook"; fails=$((fails+1)); }

  if [ "$fails" -eq 0 ]; then echo; echo "  VERDICT: every case decided as expected"; else echo; echo "  VERDICT: $fails failure(s)"; fi
  [ "$fails" -eq 0 ]
}

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
force=no; strict=no; mode=install
for arg in "$@"; do
  case "$arg" in
    --selftest) mode=selftest ;;
    --uninstall) mode=uninstall ;;
    --force) force=yes ;;
    --strict) strict=yes ;;
    *) echo "install_hooks: unknown argument: $arg" >&2; exit 2 ;;
  esac
done
case "$mode" in
  selftest) selftest; exit $? ;;
  uninstall) [ -n "$ROOT" ] || { echo "install_hooks: not inside a git repository" >&2; exit 2; }; uninstall "$ROOT"; exit $? ;;
  install) [ -n "$ROOT" ] || { echo "install_hooks: not inside a git repository" >&2; exit 2; }; install "$ROOT" "$force" "$strict"; exit $? ;;
esac

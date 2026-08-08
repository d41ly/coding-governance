#!/usr/bin/env bash
# check-wiring.sh — detect coding-governance tools installed-but-unwired in THIS repo, and
# (with --fix/--session) wire the zero-risk ones. Spec: memory/tooling/builds/2026-07-15-TOOL-aWireWarden/.
#
#   check-wiring.sh            # --check (default): report; exit 1 if any installed tool is unwired
#   check-wiring.sh --fix      # wire the safe cases (core.hooksPath when unset); exit reflects remainder
#   check-wiring.sh --session  # like --fix but ALWAYS exit 0 — the SessionStart hook mode
#
# Wiring the git hooks opts into running this repo's committed hooks (a git trust boundary). Auto-fix
# sets core.hooksPath ONLY when unset and NEVER overwrites an already-set value (e.g. a deliberate
# out-of-tree copy per WIRE-INTO-PROJECT.md §5). Agent-cap wiring is never auto-applied — it would mean
# rewriting settings.json, the file the SessionStart hook lives in.
KIT_CHECK_WIRING_VERSION=1.0
set -u

MODE=check
case "${1:-}" in
  ""|--check) MODE=check ;;
  --fix)      MODE=fix ;;
  --session)  MODE=session ;;
  *) echo "usage: $(basename "$0") [--check|--fix|--session]" >&2; exit 2 ;;
esac

# Not a git repo → nothing to wire; never an error (and never break session start).
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "skip     — not a git repo"; exit 0; }
cd "$ROOT" || { [ "$MODE" = session ] && exit 0; exit 0; }

DO_FIX=0; case "$MODE" in fix|session) DO_FIX=1 ;; esac
unwired=0

# Absolute path of an existing directory ("" if it does not resolve).
abspath() { ( cd "$1" 2>/dev/null && pwd ); }

# First of the candidates that is a file ("" if none).
first_of() { for c in "$@"; do [ -f "$c" ] && { echo "$c"; return; }; done; }

# THE wired signal, for every arm: the hook's marker substring present in .claude/settings.json.
# settings-merge.py documents that same substring as the deployer's is-it-wired test (its module
# docstring), so this is the one predicate stated once — not a second spelling of it. Grepping it
# directly also removes the "settings-merge.py absent, cannot verify" skip, which was a false
# all-clear in every adopter (the tool is copied in per WIRE §3c step 4 / §5, so an arm that
# REQUIRED it to answer reported `skip … exit 0` on the state the runbook calls the one bad state).
wired() { [ -f .claude/settings.json ] && grep -qF "$1" .claude/settings.json; }

# The launcher named in a remedy string. It is PRINTED rather than run, which is exactly why it
# must be resolved by running: a remedy line naming a launcher that cannot execute is a wrong
# answer that looks like a right one. A host with no usable python still gets a remedy — the
# fallback name is honest about being a guess.
. "$ROOT/tools/lib/resolve-python.sh"
PY=$(resolve_python) || PY=python3

# --- Check H: git hooks (core.hooksPath) ---------------------------------------------------------
check_hooks() {
  if ! { [ -f .githooks/pre-commit ] && git ls-files --error-unmatch .githooks/pre-commit >/dev/null 2>&1; }; then
    echo "skip     hooks     — no tracked .githooks/pre-commit"
    return
  fi
  local cur curdir
  cur=$(git config core.hooksPath 2>/dev/null || true)
  if [ -n "$cur" ]; then
    curdir=$(abspath "$cur")
    if [ -n "$curdir" ] && [ -f "$curdir/pre-commit" ]; then
      echo "ok       hooks     — core.hooksPath -> $cur"
    else
      echo "UNWIRED  hooks     — core.hooksPath='$cur' resolves to no pre-commit; NOT overwriting (deliberate?). Fix: git config core.hooksPath .githooks"
      unwired=$((unwired+1))
    fi
    return
  fi
  # unset — the fresh-clone case
  if [ "$DO_FIX" = 1 ]; then
    git config core.hooksPath .githooks && echo "FIXED    hooks     — set core.hooksPath -> .githooks"
  else
    echo "UNWIRED  hooks     — core.hooksPath unset; .githooks gates (incl. branch guard) dormant. Fix: git config core.hooksPath .githooks"
    unwired=$((unwired+1))
  fi
}

# --- Check A: agent-cap PreToolUse hook in .claude/settings.json ----------------------------------
# Advisory: no mode mutates settings.json (the SessionStart hook must not rewrite its own file).
check_agentcap() {
  local smerge; smerge=$(first_of tools/settings-merge.py settings-merge.py)
  # Left as a plain skip on purpose: agent-cap's hook path is not declared anywhere this script can
  # read (settings-merge.py hardcodes it), so "settings wired, script missing" cannot be told from a
  # deliberate out-of-tree copy. The recall arm below CAN — its fragment declares `hook_path`.
  if [ ! -f .claude/hooks/agent-cap.js ]; then
    echo "skip     agent-cap — not adopted (.claude/hooks/agent-cap.js absent)"
    return
  fi
  if wired "agent-cap.js"; then
    echo "ok       agent-cap — PreToolUse hook wired in .claude/settings.json"
  else
    echo "UNWIRED  agent-cap — agent-cap.js present but hook not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py}"
    unwired=$((unwired+1))
  fi
}

# --- Check R: recall-opened PostToolUse hook (memory-recall kit — an OPT-IN) ----------------------
# FIVE states, not two. `adopt-memory-recall.sh` copies the hook only under `--with-hook`, so an
# absent hook file with nothing in settings.json is a TRUE signal ("opt-in not taken"), never
# UNWIRED. Mirroring the agent-cap arm literally would print a permanent false alarm in the repo
# that runs THIS script as its own SessionStart hook, which is the fastest way to train every node
# to ignore the wiring verifier. Both halves — the marker and the script path — are read from the
# fragment, so this arm asserts nothing the shipped kit does not itself declare.
# Advisory like every other arm: no mode rewrites settings.json.
json_str() {  # value of a top-level "key": "..." in a small flat JSON file
  sed -n 's|.*"'"$2"'"[[:space:]]*:[[:space:]]*"\([^"]*\)".*|\1|p' "$1" | head -1
}
check_recall_opened() {
  local frag smerge marker hookjs
  # Resolved by path because the kit is COPIED: <root>/memory-recall/ in an adopter,
  # <root>/tools/memory-recall/ in this repo.
  frag=$(first_of memory-recall/recall-opened.fragment.json tools/memory-recall/recall-opened.fragment.json)
  if [ -z "$frag" ]; then
    echo "skip     recall    — memory-recall kit not adopted (no recall-opened.fragment.json)"
    return
  fi
  smerge=$(first_of tools/settings-merge.py settings-merge.py)
  marker=$(json_str "$frag" marker)
  hookjs=$(json_str "$frag" hook_path)
  if [ -z "$marker" ] || [ -z "$hookjs" ]; then
    echo "UNWIRED  recall    — $frag declares no marker/hook_path; settings-merge.py refuses it too. Fix: restore the shipped fragment"
    unwired=$((unwired+1))
    return
  fi
  if [ ! -f "$hookjs" ]; then
    if wired "$marker"; then
      echo "UNWIRED  recall    — settings.json dispatches the hook but $hookjs is missing; every Read runs node against nothing. Fix: bash $(dirname "$frag")/adopt-memory-recall.sh --scaffold --with-hook"
      unwired=$((unwired+1))
    else
      echo "skip     recall    — recall-opened hook opt-in not taken (adopt-memory-recall.sh --with-hook)"
    fi
    return
  fi
  if wired "$marker"; then
    echo "ok       recall    — recall-opened PostToolUse hook wired in .claude/settings.json"
  else
    echo "UNWIRED  recall    — $hookjs present but hook not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py} --fragment $frag"
    unwired=$((unwired+1))
  fi
}


# --- Check E: line endings on the RENDERED wiring files -------------------------------------------
# A `git worktree` checkout can land CRLF on a path .gitattributes pins `eol=lf`, and `git status`
# stays CLEAN because the index normalises on commit. The symptom is a gate that diffs a rendered
# file against a fresh render and reports EVERY line as drift on a file the session never touched.
#
# THE BOUND IS DERIVED, and it is deliberately not "every eol=lf path": that attribute covers 46
# files here, which is far wider than anything this arm should rewrite. The population is the tracked
# files under .claude/ that carry the pin — check-wiring.sh's OWN domain, intersected with the pin,
# both read from the tree rather than listed here. Measured: exactly the two rendered Skills, which
# are also exactly the files an adopt script byte-compares.
#
# The repair REWRITES THE BYTES, because a `git checkout --` remedy is state-dependent and this is
# not. Measured: `git diff` reports NO content change on such a file (the clean filter normalises)
# while `git status --porcelain` DOES list it — the two disagree, so a checkout-based repair restores
# the file or silently no-ops depending on which one git consults. A previous build hit the no-op and
# needed `rm` first. Rewriting the bytes is correct in both states.
check_eol() {
  local pop f bad=""
  pop=$(git ls-files .claude/ 2>/dev/null | xargs -r git check-attr eol -- 2>/dev/null \
        | sed -n 's/^\(.*\): eol: lf$/\1/p')
  if [ -z "$pop" ]; then
    echo "skip     eol       — no tracked .claude/ path carries an eol=lf pin"
    return
  fi
  for f in $pop; do
    [ -f "$f" ] || continue
    if LC_ALL=C grep -qU $'\r' "$f" 2>/dev/null; then bad="$bad $f"; fi
  done
  if [ -z "$bad" ]; then
    echo "ok       eol       — every eol=lf-pinned .claude/ file is LF in the worktree"
    return
  fi
  if [ "$DO_FIX" = 1 ]; then
    for f in $bad; do
      # Rewrite in place, then verify: a repair that reports success without checking is the class of
      # bug this whole arm exists to catch one level up.
      LC_ALL=C tr -d '\r' < "$f" > "$f.eoltmp" && mv -f "$f.eoltmp" "$f"
      if LC_ALL=C grep -qU $'\r' "$f" 2>/dev/null; then
        echo "UNWIRED  eol       — $f still holds CRLF after the repair. Fix by hand: tr -d '\\r'"
        unwired=$((unwired+1))
      else
        echo "fixed    eol       — $f rewritten to LF (the index already normalised, so git status was clean)"
      fi
    done
    return
  fi
  for f in $bad; do
    echo "UNWIRED  eol       — $f holds CRLF despite its eol=lf pin; a byte-comparing gate will report every line as drift. Fix: bash tools/check-wiring.sh --fix"
    unwired=$((unwired+1))
  done
}

check_hooks
check_agentcap
check_recall_opened
check_eol

[ "$MODE" = session ] && exit 0
[ "$unwired" = 0 ] && exit 0 || exit 1

#!/usr/bin/env bash
# policy-shim.sh — the shell half of the policy mirror's helper, policy-mirror.js (TOOL-dGroundRules-5).
#
#   bash <this kit>/policy-shim.sh landed      # the landed revision's full sha
#   bash <this kit>/policy-shim.sh get <key>   # policy.py get <key> --json, passed through
#
# Run in the repository to read. JavaScript resolves neither the remote ladder nor a python launcher,
# so the helper asks this file, which carries both canonical blocks inline, byte-identical, graded by
# the resolver self-test's parity rows like every other copy.
#
# `landed` is the reader's `derive_landed_revision`: the remote the ladder names and its branch, else
# `main`, at refs/remotes/<remote>/<branch>, or refs/heads/<branch> where the ladder names no remote.
# A ladder refusal, or a ref that names no commit, exits 2 printing the reader's refusal line.
# Where the ladder named no branch and the `main` fallback names no commit, that line names the
# fallback and how to name the default branch, byte for byte the reader's (TOOL-dGroundRules-73).
# `get` runs `policy.py get <key> --json` under the resolved launcher, its stdout, stderr and exit
# passed through; no launcher exits 2 printing the resolver's own lines.
#
#   Exit 0 answered · 2 refused, no launcher, or wrong invocation.
set -u
# Git's location variables, dropped as the reader drops them: a hook exports them, and this reads
# the repository it runs in.
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX
case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac
USAGE="usage: bash <this kit>/policy-shim.sh landed | get <key>"

# >>> remote_ladder_sh -- canonical copy: resolve-remote.sh in the gov lib dir (byte-identical; gated)
# resolve_remote_sh -> RR_REMOTE RR_BRANCH RR_OBSERVED RR_WHY, rc 0; rc 1 with RR_WHY on a refusal.
# The ladder, row for row, is resolve_remote.py in the gov lib dir: GOV_REMOTE, else the current
# branch remote unless it is ".", else the ONLY remote; several and none chosen, or a name that is
# no remote here, refuses naming GOV_REMOTE; no remote at all is RR_REMOTE="" and rc 0. RR_OBSERVED
# is what <remote>/HEAD names; RR_BRANCH is GOV_DEFAULT_BRANCH, else RR_OBSERVED. Fetches nothing.
# RR_GIT names the git command, so a caller holding a pinned wrapper function passes it.
resolve_remote_sh() {
  local _rr_git=${RR_GIT:-git} _rr_names _rr_n _rr_list _rr_cur _rr_where _rr_how=GOV_REMOTE _rr_head _rr_bad
  RR_REMOTE=${GOV_REMOTE:-}; RR_BRANCH=""; RR_OBSERVED=""; RR_WHY=""
  _rr_names=$("$_rr_git" remote 2>/dev/null) || _rr_names=""
  _rr_n=$(printf "%s" "$_rr_names" | grep -c . || true)
  _rr_list=$(printf "%s" "$_rr_names" | tr "\n" " ")
  [ -n "$_rr_list" ] || _rr_list=none
  # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous.
  _rr_cur=$("$_rr_git" symbolic-ref --quiet HEAD 2>/dev/null) || _rr_cur=""
  case "$_rr_cur" in refs/heads/?*) _rr_cur=${_rr_cur#refs/heads/} ;; *) _rr_cur="" ;; esac
  if [ -z "$RR_REMOTE" ] && [ -n "$_rr_cur" ]; then
    RR_REMOTE=$("$_rr_git" config "branch.$_rr_cur.remote" 2>/dev/null) || RR_REMOTE=""
    _rr_how="branch.$_rr_cur.remote"
    [ "$RR_REMOTE" != . ] || RR_REMOTE=""
  fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -eq 1 ]; then RR_REMOTE=$_rr_names; fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -gt 1 ]; then
    _rr_where="a detached HEAD"; [ -z "$_rr_cur" ] || _rr_where="branch $_rr_cur"
    RR_WHY="cannot choose a remote: GOV_REMOTE is unset, $_rr_where has no configured remote, and this repository has $_rr_n remotes ($_rr_list). Name it: export GOV_REMOTE=<remote>."
    return 1
  fi
  # A name holding whitespace is no remote: `grep -F` would split it into several patterns.
  case "$RR_REMOTE" in *[[:space:]]*) _rr_bad=1 ;; *) _rr_bad=0 ;; esac
  if [ -n "$RR_REMOTE" ] && { [ "$_rr_bad" = 1 ] || ! printf "%s\n" "$_rr_names" | grep -qxF -- "$RR_REMOTE"; }; then
    RR_WHY="$_rr_how names $RR_REMOTE, which is no remote of this repository ($_rr_list). Name one that is: export GOV_REMOTE=<remote>."
    RR_REMOTE=""
    return 1
  fi
  if [ -n "$RR_REMOTE" ]; then
    _rr_head=$("$_rr_git" symbolic-ref --quiet "refs/remotes/$RR_REMOTE/HEAD" 2>/dev/null) || _rr_head=""
    case "$_rr_head" in "refs/remotes/$RR_REMOTE"/?*) RR_OBSERVED=${_rr_head#"refs/remotes/$RR_REMOTE"/} ;; esac
  fi
  RR_BRANCH=${GOV_DEFAULT_BRANCH:-$RR_OBSERVED}
  return 0
}
# <<< remote_ladder_sh

# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python

case "${1:-}:$#" in
  landed:1)
    resolve_remote_sh || { printf 'policy: refused · .governance/policy.toml:0 · %s\n' "$RR_WHY" >&2; exit 2; }
    if [ -n "$RR_REMOTE" ]; then REF="refs/remotes/$RR_REMOTE/${RR_BRANCH:-main}"; else REF="refs/heads/${RR_BRANCH:-main}"; fi
    WHY=""
    if [ -z "$RR_BRANCH" ] && [ -n "$RR_REMOTE" ]; then
      WHY=", and main is only the fallback: refs/remotes/$RR_REMOTE/HEAD names no branch and GOV_DEFAULT_BRANCH is unset. Name the default branch: git remote set-head $RR_REMOTE -a, or export GOV_DEFAULT_BRANCH=<branch>."
    elif [ -z "$RR_BRANCH" ]; then
      WHY=", and main is only the fallback: this clone has no remote and GOV_DEFAULT_BRANCH is unset. Name the local default branch: export GOV_DEFAULT_BRANCH=<branch>."
    fi
    git rev-parse --verify -q "$REF^{commit}" \
      || { printf 'policy: refused · .governance/policy.toml:0 · %s names no commit in this repository%s\n' "$REF" "$WHY" >&2; exit 2; }
    ;;
  get:2)
    PY=$(resolve_python) || exit 2
    exec "$PY" -B "$HERE/policy.py" get "$2" --json
    ;;
  *) echo "$USAGE" >&2; exit 2 ;;
esac

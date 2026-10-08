# resolve-remote.sh — which remote "landed" is measured on, and its default branch (TOOL-dLadderedRemote-1).
#
# The canonical shell copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer
# carries the block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity
# table reds a copy that drifts. Its Python twin, with the same ladder and the same refusal text, is
# `resolve_remote.py` beside this file, and the same test's behaviour arm runs both over one truth
# table. Sourced by that test and by nothing else; every consumer carries the block instead.
#
# The block carries no single quote, so a caller may embed it inside a single-quoted program.

# >>> remote_ladder_sh -- canonical copy: resolve-remote.sh in the gov lib dir (byte-identical; gated)
# resolve_remote_sh -> RR_REMOTE RR_BRANCH RR_OBSERVED RR_WHY, rc 0; rc 1 with RR_WHY on a refusal.
# The ladder, row for row, is resolve_remote.py in the gov lib dir: GOV_REMOTE, else the current
# branch remote unless it is ".", else the ONLY remote; several and none chosen, or a name that is
# no remote here, refuses naming GOV_REMOTE; no remote at all is RR_REMOTE="" and rc 0. RR_OBSERVED
# is what <remote>/HEAD names; RR_BRANCH is GOV_DEFAULT_BRANCH, else RR_OBSERVED. Fetches nothing.
# RR_GIT names the git command, so a caller holding a pinned wrapper function passes it.
resolve_remote_sh() {
  local _rr_git=${RR_GIT:-git} _rr_names _rr_n _rr_list _rr_cur _rr_where _rr_how=GOV_REMOTE _rr_head
  RR_REMOTE=${GOV_REMOTE:-}; RR_BRANCH=""; RR_OBSERVED=""; RR_WHY=""
  _rr_names=$("$_rr_git" remote 2>/dev/null) || _rr_names=""
  _rr_n=$(printf "%s" "$_rr_names" | grep -c . || true)
  _rr_list=$(printf "%s" "$_rr_names" | tr "\n" " ")
  [ -n "$_rr_list" ] || _rr_list=none
  _rr_cur=$("$_rr_git" symbolic-ref --quiet --short HEAD 2>/dev/null) || _rr_cur=""
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
  if [ -n "$RR_REMOTE" ] && ! printf "%s\n" "$_rr_names" | grep -qxF -- "$RR_REMOTE"; then
    RR_WHY="$_rr_how names $RR_REMOTE, which is no remote of this repository ($_rr_list). Name one that is: export GOV_REMOTE=<remote>."
    RR_REMOTE=""
    return 1
  fi
  if [ -n "$RR_REMOTE" ]; then
    _rr_head=$("$_rr_git" symbolic-ref --quiet --short "refs/remotes/$RR_REMOTE/HEAD" 2>/dev/null) || _rr_head=""
    case "$_rr_head" in "$RR_REMOTE"/?*) RR_OBSERVED=${_rr_head#"$RR_REMOTE"/} ;; esac
  fi
  RR_BRANCH=${GOV_DEFAULT_BRANCH:-$RR_OBSERVED}
  return 0
}
# <<< remote_ladder_sh

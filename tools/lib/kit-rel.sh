#!/usr/bin/env bash
# The one "where does this file sit in its repository" walk, for a file that SHIPS.
#
# TOOL-aRepatriatedFork-18 S2. A shipped suite used to spell its own kit directory as a default,
# `KIT_REL="${KIT_REL:-tools/<kit>}"` or `${KIT_REL:-tools}`, and nothing ever set the variable: at
# any prefix but gov's the default named a directory that is not there, and the two spellings meant
# two different things (TOOL-dRetiredFork-39). The walk below is the one `<prefix>/check-wiring.sh` and
# the unattended adopter already carry, printing the file's OWN directory relative to the repo root.
#
# THE WALK IS LOGICAL, NOT PHYSICAL, which is the junction contract those two record: `pwd` without
# `-P` keeps the path the caller traversed, so a kit dir that is a junction anchors to the ADOPTING
# repo. Asking git answers with the junction's TARGET, and was measured to.
#
# USAGE — a shipped suite cannot source this file (`<prefix>/lib/` travels to nobody), so each one
# carries the block between the markers below INLINE, byte-identical, and
# `resolve-python.test.sh` gates every copy against this one:
#
#   HERE="$(cd "$(dirname "$0")" && pwd)"
#   KIT_REL=$(derive_self_rel "$HERE") || { echo "not inside a git repository"; exit 2; }
#
# It prints the directory and returns 0, EMPTY for a file at the repository root, which is a legal
# install; it returns 1 when the walk reaches the filesystem root with no `.git` on the way.

# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel

# TOOL-aRepatriatedFork-47 S2 — the `{prefix}` token resolved against a tool root, the shell twin of
# the `resolve_prefix_token` block in `resolve_prefix_token.py` beside this file. Same contract, and
# `resolve-python.test.sh` runs both over one truth table: an empty or `.` root drops the token with
# its slash and a bare token becomes `.`; any other root replaces the token. Carried INLINE by every
# shell reader of the token, byte-identical, gated like the block above.
#
#   resolve_prefix_sh '{prefix}/a/b' "$TROOT"    # prints the resolved path
#
# >>> resolve_prefix_sh -- canonical copy: kit-rel.sh in the gov lib dir (byte-identical; gated)
resolve_prefix_sh() {
  local _rps_s="$1"
  case "${2:-}" in
    ""|.) _rps_s=${_rps_s//"{prefix}/"/}; _rps_s=${_rps_s//"{prefix}"/.} ;;
    *) _rps_s=${_rps_s//"{prefix}"/"$2"} ;;
  esac
  printf '%s\n' "$_rps_s"
}
# <<< resolve_prefix_sh

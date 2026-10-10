#!/usr/bin/env bash
# post-merge.sh — the full bar on a LANDED sha, and its verdict published as a remote ref
# (TOOL-aFrugalTurnstile-6, design D7).
#
#   bash <this kit>/post-merge.sh <sha> [--remote <name>]
#
# Exit 0 is a green whose publication completed, 1 is a red or any verdict whose publication failed,
# and 2 is a refusal before any bar ran, or a bar whose scratch worktree's HEAD moved under it.
#
# WHAT IT DOES. It makes a detached scratch worktree of <sha> at `<common-dir>/gate-pm.<pid>`, runs
# the bar that <sha> declares (`GOV_GATE_CMD` in `.githooks/gate-env.sh` as committed there, else
# this kit's runner) with `GATE_FULL=1` through this kit's own `run-gates.sh --hold`, so it queues on
# the host turnstile like any bar, and publishes: a RED pushes `<sha>:refs/gov/bar-red` when that ref
# is absent or an ancestor of <sha>; a GREEN deletes the ref when it names <sha> or an ancestor of it.
# Every push is leased on the sha it observed, so a ref that moved in between is a lost race, never
# an overwrite. It keeps the last verdict in `<common-dir>/gate-post-merge`, writes a GREEN's record
# to `<common-dir>/gate-bar-green.shared` (design D3, `by post-merge`), and copies the bar's run
# record to `<common-dir>/gate-run/<run id>/` before the worktree goes.
#
# WHAT THIS DOES NOT CHECK: it grades the tree at `<sha>` alone, never the push that landed it; it
# trusts this clone's remote-tracking ref for "landed"; it applies three keys of the gate-env file
# and no other assignment in it; it retries nothing; and two runs racing on the ref are serialised by
# the lease, never ordered by when their shas landed, so a red that finishes after a descendant's
# green is still published and binds until the next green that descends from it.
set -u

# ---- the scrub (spec §4 "The scrub"), before any git call reads the environment -------------------
# `GIT_DIR` and its family first: under a hook they point git at the caller's repository. The bar's
# interpreter and its command come from the tree at <sha>, never from here; the arm seams and the
# reuse mode would let the caller choose a verdict; an inherited holder nonce would skip the queue.
# `GATE_SELFTESTS` and `GATE_TURNSTILE_DIR` stay honoured: the first is the owner's switch, the
# second moves the queue and never a verdict.
PM_SCRUB="GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES
  GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX GOV_GATE_CMD GOV_GATE_CMD_TEST GOV_PYTHON GATE_LEGS GATE_REUSE
  GATE_BASE GATE_DOCS_BASE GATE_PUSH_BASE GATE_ATTRIBUTE GATE_SPAWN_CMD GATE_SPAWN_FLOOR
  GATE_VERDICT_FAULT GATE_RUN_ID GATE_TURNSTILE_HOLDER"
PM_DROPPED=""
for _k in $PM_SCRUB $(compgen -e); do
  case "$_k" in
    *_PY|GATE_INHERITED_RED*) ;;
    *) case " ${PM_SCRUB//$'\n'/ } " in *" $_k "*) ;; *) continue ;; esac ;;
  esac
  if [ -n "${!_k+x}" ]; then
    case " $PM_DROPPED " in *" $_k "*) ;; *) PM_DROPPED="$PM_DROPPED $_k" ;; esac
  fi
  unset "$_k"
done
[ -z "$PM_DROPPED" ] || echo "post-merge: not honoured from the environment:$PM_DROPPED"

PM_USAGE="post-merge: usage: post-merge.sh <sha> [--remote <name>]"
CDIR=""; SHA=""; RUN_ID=""; REMOTE=""; WT=""

write_post_merge_record() { # verdict · published · why -> <common-dir>/gate-post-merge, tmp then rename
  [ -n "$CDIR" ] || return 0
  local why=${3//[$'\t\n\r']/ }
  { printf 'sha\t%s\nverdict\t%s\nrun_id\t%s\npublished\t%s\nwhy\t%s\nremote\t%s\nstamped\t%s\n' \
      "$SHA" "$1" "$RUN_ID" "$2" "$why" "$REMOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$CDIR/gate-post-merge.tmp" && mv -f "$CDIR/gate-post-merge.tmp" "$CDIR/gate-post-merge"; } 2>/dev/null \
    || echo "post-merge: $CDIR/gate-post-merge could not be written"
}

write_refusal() { # why · [usage] -> the REFUSING line, the REFUSED record, exit 2
  echo "post-merge: REFUSING — $1"
  [ -z "${2:-}" ] || echo "$PM_USAGE"
  write_post_merge_record REFUSED none "$1"
  exit 2
}

# ---- 1. the arguments, the work tree, the common dir and this kit's own directory -----------------
PM_ARG=""; PM_REMOTE_SET=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --remote)
      [ "$#" -ge 2 ] && [ -n "$2" ] || { PM_BAD="--remote needs a name"; break; }
      GOV_REMOTE=$2; PM_REMOTE_SET=1; shift 2 ;;
    -*) PM_BAD="unknown option $1"; break ;;
    *) if [ -n "$PM_ARG" ]; then PM_BAD="one <sha> only, and $1 is a second"; break; fi
       PM_ARG=$1; shift ;;
  esac
done
[ -n "$PM_REMOTE_SET" ] && export GOV_REMOTE
TOP=$(git rev-parse --show-toplevel 2>/dev/null) || TOP=""
[ -n "$TOP" ] && CDIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || CDIR=""
[ -z "${PM_BAD:-}" ] || write_refusal "$PM_BAD" usage
[ -n "$PM_ARG" ] || write_refusal "no <sha> was named" usage
[ -n "$TOP" ] || write_refusal "not inside a git work tree"
[ -n "$CDIR" ] || write_refusal "the git common dir of $TOP does not resolve"
cd "$TOP" || write_refusal "cannot enter $TOP"
SHA=$(git rev-parse -q --verify "$PM_ARG^{commit}" 2>/dev/null) || SHA=""
[ -n "$SHA" ] || write_refusal "$PM_ARG names no commit in this repository" usage
KITDIR=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || KITDIR=""
[ -n "$KITDIR" ] && [ -f "$KITDIR/run-gates.sh" ] || write_refusal "this kit's runner is not beside $0"

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
KIT_REL=$(derive_self_rel "$KITDIR") || write_refusal "$KITDIR is not inside a git repository"

# ---- 2. the remote, by the lander's ladder, and "landed" ------------------------------------------
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
resolve_remote_sh || write_refusal "$RR_WHY"
[ -n "$RR_REMOTE" ] || write_refusal "this repository has no remote, so nothing names where a verdict is published"
REMOTE=$RR_REMOTE
[ -n "$RR_BRANCH" ] || write_refusal "$REMOTE names no default branch here; fix once: git remote set-head $REMOTE -a"
PM_LANDED="refs/remotes/$REMOTE/$RR_BRANCH"
git rev-parse -q --verify "$PM_LANDED^{commit}" >/dev/null 2>&1 \
  || write_refusal "$PM_LANDED does not resolve in this clone; fetch $REMOTE first"
# THE SAFETY HALF (S1): a green on an unlanded sha descending from a red would clear the red before
# the fix reached the default branch.
git merge-base --is-ancestor "$SHA" "$PM_LANDED" 2>/dev/null \
  || write_refusal "${SHA:0:8} is not on $REMOTE/$RR_BRANCH as this clone last fetched it, so it has not landed"

# ---- 3. the bar, read at <sha> and never sourced ---------------------------------------------------
# read_policy_key is the hook's, byte for byte: the hook ships verbatim and sources no kit.
read_policy_key() { # file text · key -> the LAST `<key>=` line's value, cleaned; nothing when none assigns it
  local line v="" hit=""
  while IFS= read -r line || [ -n "$line" ]; do
    line=${line%$'\r'}
    case "$line" in "$2="*) v=${line#"$2="}; hit=1 ;; esac
  done <<< "$1"
  [ -n "$hit" ] || return 0
  v=${v%%[[:space:]]#*}
  while [ "${v% }" != "$v" ] || [ "${v%$'\t'}" != "$v" ]; do v=${v%?}; done
  while [ "${v# }" != "$v" ]; do v=${v# }; done
  case "$v" in
    \"*\") v=${v#\"}; v=${v%\"} ;;
    \'*\') v=${v#\'}; v=${v%\'} ;;
  esac
  printf '%s' "$v"
}

check_bar_value() { # bar command · sha -> rc 0, or rc 1 with PM_WHY; the executing word is the hook's: word 1, or word 2 after bash or sh
  local -a w=()
  local prog
  PM_WHY=""
  read -ra w <<<"$1"
  prog=${w[0]-}
  case "$prog" in
    bash|sh)
      prog=${w[1]-}
      case "$prog" in -*|'') PM_WHY="the declared bar '$1' puts ${prog:-nothing} where its script must be"; return 1 ;; esac ;;
  esac
  if [ "$(git cat-file -t "$2:$prog" 2>/dev/null)" != blob ]; then
    PM_WHY="the declared bar '$1' executes $prog, which is not a path tracked at ${2:0:8}"; return 1
  fi
  return 0
}

# The blob goes to a FILE and the shape loop reads the file: a loop fed by a command substitution can
# block forever under MSYS (the shell-hygiene leg's class).
PM_ENV_FILE=$(mktemp) || write_refusal "cannot create a scratch file for the gate-env read"
git show "$SHA:.githooks/gate-env.sh" >"$PM_ENV_FILE" 2>/dev/null || : >"$PM_ENV_FILE"
PM_ENV=$(<"$PM_ENV_FILE")
# A line naming the key in any other shape is one the hook would SOURCE and this reader would miss.
while IFS= read -r _l || [ -n "$_l" ]; do
  _l=${_l%$'\r'}
  case "$_l" in ''|'#'*|GOV_GATE_CMD=*) continue ;; esac
  [[ "$_l" =~ ^[[:space:]]*# ]] && continue
  if [[ "$_l" =~ (^|[^A-Za-z0-9_])GOV_GATE_CMD([^A-Za-z0-9_]|$) ]]; then
    rm -f "$PM_ENV_FILE"
    write_refusal "a line of .githooks/gate-env.sh at ${SHA:0:8} names GOV_GATE_CMD in a shape this reader does not apply: $_l"
  fi
done <"$PM_ENV_FILE"
rm -f "$PM_ENV_FILE"
PM_DEFAULT_BAR="bash ${KIT_REL:+$KIT_REL/}run-gates.sh"
BAR=$(read_policy_key "$PM_ENV" GOV_GATE_CMD)
if [ -n "$BAR" ]; then
  check_bar_value "$BAR" "$SHA" || write_refusal "$PM_WHY"
else
  BAR=$PM_DEFAULT_BAR
  git cat-file -e "$SHA:${KIT_REL:+$KIT_REL/}run-gates.sh" 2>/dev/null \
    || write_refusal "no bar is declared and the runner ${KIT_REL:+$KIT_REL/}run-gates.sh is absent at ${SHA:0:8}"
fi
case "$BAR" in *$'\t'*|*$'\n'*) write_refusal "the bar's command holds a tab or a newline" ;; esac
_v=$(read_policy_key "$PM_ENV" GOV_PYTHON); [ -z "$_v" ] || export GOV_PYTHON="$_v"
_v=$(read_policy_key "$PM_ENV" GATE_SELFTESTS); [ -z "$_v" ] || export GATE_SELFTESTS="$_v"

# ---- the bounded network call (observe_remote's shape and constants, from the unattended driver) --
PM_BOUND=60; PM_CONNECT_BOUND=20; PM_LOWSPEED_BYTES=1000
PM_BOUND_LIVE=1
timeout -k 1s 10 true >/dev/null 2>&1 || {
  PM_BOUND_LIVE=0
  echo "post-merge: NOTE — no working \`timeout -k\` on this host, so the ${PM_BOUND}s wall clock on each network call is inert"
}
run_remote() { # <outfile> · <git args…> -> rc (124 = the wall fired); output to a FILE, never a pipe
  local out=$1; shift
  local -a pre=()
  [ "$PM_BOUND_LIVE" = 1 ] && pre=(timeout -k 5s "$PM_BOUND")
  "${pre[@]}" env GIT_TERMINAL_PROMPT=0 \
      "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$PM_CONNECT_BOUND -o BatchMode=yes" \
    git -c credential.interactive=never \
        -c "http.lowSpeedLimit=$PM_LOWSPEED_BYTES" -c "http.lowSpeedTime=$PM_BOUND" \
        "$@" >"$out" 2>/dev/null
}

PM_RED_REF=refs/gov/bar-red
read_remote_red() { # -> rc 0 with PM_RED_STATE present|absent and PM_RED_SHA; rc 1 with PM_WHY
  local f rc
  PM_RED_STATE=""; PM_RED_SHA=""; PM_WHY=""
  f=$(mktemp) || { PM_WHY="cannot create a scratch file to bound the read"; return 1; }
  run_remote "$f" ls-remote --exit-code "$REMOTE" "$PM_RED_REF"; rc=$?
  case "$rc" in
    0) PM_RED_STATE=present; read -r PM_RED_SHA _ <"$f" ;;
    2) PM_RED_STATE=absent ;;
    124) PM_WHY="the read of $PM_RED_REF was killed by this script's own ${PM_BOUND}s bound" ;;
    *) PM_WHY="git ls-remote $REMOTE $PM_RED_REF exited $rc" ;;
  esac
  rm -f "$f"
  [ "$PM_RED_STATE" = absent ] && return 0
  [ "$PM_RED_STATE" = present ] && [ -n "$PM_RED_SHA" ] && return 0
  [ -n "$PM_WHY" ] || PM_WHY="git ls-remote printed no sha for $PM_RED_REF"
  PM_RED_STATE=""
  return 1
}

# The leased push, from the scratch worktree, by remote NAME; the porcelain line decides, as
# write_claim reads it. <src> is a sha to create or advance the ref, or empty to delete it.
PM_PUSH_SRC=""
write_red_ref() { # lease (observed sha, empty when absent) -> rc 0, or rc 1 with PM_WHY
  local lease=$1 f rc l line rf tok=""
  PM_WHY=""
  rf="$PM_WT_GD/pre-push-refusal"; rm -f "$rf" 2>/dev/null
  f=$(mktemp) || { PM_WHY="cannot create a scratch file to bound the push"; return 1; }
  run_remote "$f" -C "$WT" push --porcelain "--force-with-lease=$PM_RED_REF:$lease" "$REMOTE" "$PM_PUSH_SRC:$PM_RED_REF"; rc=$?
  line=""
  while IFS= read -r l; do
    case "$l" in ?$'\t'*":$PM_RED_REF"$'\t'*) line=${l%$'\r'} ;; esac
  done <"$f"
  rm -f "$f"
  if [ "$rc" = 124 ]; then PM_WHY="the push was killed by this script's own ${PM_BOUND}s bound"
  elif [ -z "$line" ]; then PM_WHY="git push exited $rc and printed no status line for $PM_RED_REF"
  elif [ "${line:0:1}" != '!' ]; then return 0
  else
    case "$line" in
      *"(stale info)"*|*"(fetch first)"*) PM_WHY="lost the race on the lease: ${line##*$'\t'}" ;;
      *) PM_WHY="the push was rejected: ${line##*$'\t'}" ;;
    esac
  fi
  if [ -f "$rf" ]; then
    IFS=$'\t' read -r tok _ <"$rf" || :
    PM_WHY="$PM_WHY · the scratch worktree's pre-push hook refused it: ${tok:-an empty refusal file}"
  fi
  return 1
}
remove_red_ref() { # lease (the observed sha) -> as write_red_ref, deleting the ref
  PM_PUSH_SRC=""; write_red_ref "$1"
}

run_bar() { # -> PM_VERDICT GREEN|RED|REFUSED, with PM_WHY on REFUSED
  local -a words=()
  local rc v head
  PM_VERDICT=""; PM_WHY=""
  read -ra words <<<"$BAR"
  ( cd "$WT" && GATE_FULL=1 GATE_RUN_ID="$RUN_ID" bash "$KITDIR/run-gates.sh" --hold -- "${words[@]}" </dev/null ); rc=$?
  head=$(git -C "$WT" rev-parse -q --verify HEAD 2>/dev/null) || head=""
  if [ "$head" != "$SHA" ]; then
    PM_VERDICT=REFUSED; PM_WHY="the scratch worktree's HEAD reads ${head:-nothing} after the bar, not ${SHA:0:8}, so no verdict describes the sha"; return 0
  fi
  if [ "$rc" != 0 ]; then PM_VERDICT=RED; return 0; fi
  PM_VERDICT=GREEN
  if [ "$BAR" = "$PM_DEFAULT_BAR" ]; then
    v=$(awk -F'\t' '$1=="verdict"{print $2; exit}' "$PM_WT_GD/gate-run/$RUN_ID/verdict" 2>/dev/null)
    if [ "$v" != GREEN ]; then
      echo "post-merge: the runner exited 0 and its run record does not read verdict GREEN — treating it as RED"
      PM_VERDICT=RED
    fi
  fi
}

write_run_record() { # -> PM_RUN_COPY, the copy of the bar's run record under the common dir, or empty
  PM_RUN_COPY=""
  [ -d "$PM_WT_GD/gate-run/$RUN_ID" ] || return 0
  mkdir -p "$CDIR/gate-run" 2>/dev/null && rm -rf "$CDIR/gate-run/$RUN_ID" 2>/dev/null
  if cp -R "$PM_WT_GD/gate-run/$RUN_ID" "$CDIR/gate-run/$RUN_ID" 2>/dev/null; then
    PM_RUN_COPY="$CDIR/gate-run/$RUN_ID"
  else
    echo "post-merge: the run record at $PM_WT_GD/gate-run/$RUN_ID could not be copied to $CDIR/gate-run/"
  fi
}

write_bar_green() { # -> <common-dir>/gate-bar-green.shared in design D3's grammar, by post-merge
  local tree w paths=""
  local -a words=()
  tree=$(git rev-parse -q --verify "$SHA^{tree}" 2>/dev/null) || tree=""
  read -ra words <<<"$BAR"
  for w in "${words[@]}"; do case "$w" in */*|*.sh) paths="$paths${paths:+ }$w" ;; esac; done
  { printf 'sha\t%s\ntree\t%s\nbar\t%s\nbar_paths\t%s\nkind\tfull\nbase\t\nselftests\t%s\nrun_id\t%s\nby\tpost-merge\nstamped\t%s\n' \
      "$SHA" "$tree" "$BAR" "$paths" "${GATE_SELFTESTS:+1}" "$RUN_ID" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$CDIR/gate-bar-green.shared.tmp" && mv -f "$CDIR/gate-bar-green.shared.tmp" "$CDIR/gate-bar-green.shared"; } 2>/dev/null \
    || echo "post-merge: $CDIR/gate-bar-green.shared could not be written"
}

# ---- 4. the scratch worktree, and its cleanup ------------------------------------------------------
if [ -n "${EPOCHREALTIME:-}" ]; then RUN_ID="post-merge-${EPOCHREALTIME//[!0-9]/}${RANDOM}-$$"
else printf -v RUN_ID 'post-merge-%(%s)T%s-%s' -1 "$RANDOM" "$$"; fi
. "$KITDIR/lib-attribute.sh" 2>/dev/null && declare -F add_scratch_worktree >/dev/null \
  || write_refusal "lib-attribute.sh beside this script did not load"
WT="$CDIR/gate-pm.$$"
add_scratch_worktree "$WT" "$SHA" || write_refusal "a detached worktree of ${SHA:0:8} could not be made at $WT"
trap 'remove_scratch_worktree "$WT" || echo "post-merge: the scratch worktree at $WT could not be removed — remove it by hand"' EXIT
PM_WT_GD=$(git -C "$WT" rev-parse --path-format=absolute --git-dir 2>/dev/null) || PM_WT_GD=""
[ -n "$PM_WT_GD" ] || write_refusal "the git dir of the scratch worktree at $WT does not resolve"

# ---- 5. the bar ------------------------------------------------------------------------------------
echo "post-merge: ${SHA:0:8} on $REMOTE/$RR_BRANCH — bar: $BAR — through the host turnstile, GATE_FULL=1"
run_bar
[ "$PM_VERDICT" != REFUSED ] || write_refusal "$PM_WHY"
write_run_record

# ---- 6. the publication ----------------------------------------------------------------------------
PM_PUB=""; PM_PUB_WHY=""; PM_SAY=""
if ! read_remote_red; then
  PM_PUB=failed; PM_PUB_WHY=$PM_WHY
else
  PM_ANC=""
  # A ref object missing locally is not an ancestor, so it is kept: the safe direction.
  [ "$PM_RED_STATE" = present ] && git merge-base --is-ancestor "$PM_RED_SHA" "$SHA" 2>/dev/null && PM_ANC=1
  if [ "$PM_VERDICT" = RED ]; then
    if [ "$PM_RED_STATE" = absent ]; then
      PM_PUSH_SRC=$SHA; if write_red_ref ""; then PM_PUB=pushed; PM_SAY=pushed; fi
    elif [ "$PM_RED_SHA" = "$SHA" ]; then PM_PUB=none; PM_SAY="already names it"
    elif [ -n "$PM_ANC" ]; then
      PM_PUSH_SRC=$SHA; if write_red_ref "$PM_RED_SHA"; then PM_PUB=pushed; PM_SAY="advanced from ${PM_RED_SHA:0:8}"; fi
    else PM_PUB=kept; PM_SAY="kept at ${PM_RED_SHA:0:8}, which is not an ancestor"
    fi
  else
    if [ "$PM_RED_STATE" = absent ]; then PM_PUB=none; PM_SAY="absent, nothing to do"
    elif [ "$PM_RED_SHA" = "$SHA" ] || [ -n "$PM_ANC" ]; then
      if remove_red_ref "$PM_RED_SHA"; then PM_PUB=cleared; PM_SAY=cleared; fi
    else PM_PUB=kept; PM_SAY="kept at ${PM_RED_SHA:0:8}, which is not an ancestor"
    fi
  fi
  [ -n "$PM_PUB" ] || { PM_PUB=failed; PM_PUB_WHY=$PM_WHY; }
fi

# ---- 7. the records, and the exit ------------------------------------------------------------------
[ "$PM_VERDICT" = GREEN ] && write_bar_green
if [ "$PM_PUB" = failed ]; then
  echo "post-merge: publish FAILED — $PM_PUB_WHY"
elif [ "$PM_VERDICT" = GREEN ]; then
  echo "post-merge: GREEN at ${SHA:0:8} — $PM_RED_REF $PM_SAY"
else
  echo "post-merge: RED at ${SHA:0:8} — $PM_RED_REF $PM_SAY — run record ${PM_RUN_COPY:-none}"
fi
write_post_merge_record "$PM_VERDICT" "$PM_PUB" "$PM_PUB_WHY"
[ "$PM_VERDICT" = GREEN ] && [ "$PM_PUB" != failed ] && exit 0
exit 1

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
# to `<common-dir>/gate-bar-green.shared` (design D3, `by post-merge`) only when the scratch worktree is
# still clean after the bar (TOOL-aFrugalTurnstile-17), and copies the bar's run
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
# `GATE_REUSE_LINEAGE` is a reuse mode too, and the one this bar's `GATE_FULL` would switch on
# (TOOL-aSparedSpawn-33 S7). `GATE_SELFTESTS` and `GATE_TURNSTILE_DIR` stay honoured: the first is the
# owner's switch, the second moves the queue and never a verdict.
PM_SCRUB="GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES
  GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX GOV_GATE_CMD GOV_GATE_CMD_TEST GOV_PYTHON GATE_LEGS GATE_REUSE
  GATE_REUSE_LINEAGE GATE_BASE GATE_DOCS_BASE GATE_PUSH_BASE GATE_ATTRIBUTE GATE_SPAWN_CMD GATE_SPAWN_FLOOR
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
  local why=${3//[$'\t\n\r']/ } t
  # The temp's name is unknown until the write creates it (TOOL-dRedressedBar-24): `mktemp -u` names
  # it and creates nothing, so the `>` below is the open that makes it. One fork, once per bar.
  t=$(mktemp -u "$CDIR/gate-post-merge.XXXXXXXX" 2>/dev/null)
  { printf 'sha\t%s\nverdict\t%s\nrun_id\t%s\npublished\t%s\nwhy\t%s\nremote\t%s\nstamped\t%s\n' \
      "$SHA" "$1" "$RUN_ID" "$2" "$why" "$REMOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$t" && mv -f "$t" "$CDIR/gate-post-merge"; } 2>/dev/null \
    || { [ -z "$t" ] || rm -f "$t" 2>/dev/null; echo "post-merge: $CDIR/gate-post-merge could not be written"; }
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

# >>> gov_ref_sh — canonical copy: gov-ref.sh in gov's lib dir (byte-identical; gated)
# I1 AND I2, ONE WRITER FOR EVERY GOVERNANCE REF (TOOL-dPlacedRequest-11): a run claim, the bar-red
# ref and every later register, request and card ref are written here, never by a hand copy.
# `build_gov_commit` builds the commit over the empty tree under the fixed `gov-claim` identity,
# parented on the tip its caller read, so `git log <ref>` on the remote lists every write in order; a
# create, whose tip read is empty, is the one parentless commit. It prints nothing and returns 1 when
# git cannot build it. `write_gov_ref` pushes `--porcelain --force-with-lease=<ref>:<expected>`, the
# expected sha EMPTY for a create, and the porcelain line whose second field ends in `:<ref>` decides,
# never the exit alone: `!` with `(stale info)` or `(fetch first)` is 1, LOST; any other `!`, no status
# line, or the bound firing (124) is 2, NOT COMPLETED; any other flag is 0. The cause is in
# GOVREF_WHY. An EMPTY source returns 2 `no source` and pushes nothing, so a failed build captured as
# `c=$(build_gov_commit …)` is never a deletion; `remove_gov_ref` is the one deletion form, its
# expected sha non-empty, and it reaches the same push and porcelain read through `write_gov_ref`,
# which admits an empty source only when `remove_gov_ref` is its caller.
# THE CALLER SETS THREE NAMES: GOVREF_RUNNER, a function taking `<outfile> <git args…>` that runs git
# bounded and writes its stdout to the file; GOVREF_REMOTE, the remote NAME the push names, so the
# pre-push hook observes `<name>/HEAD`; GOVREF_GITDIR, the git dir whose `pre-push-refusal` a hook
# writes, empty to read no token.
# NO REFUSAL TOKEN IS THIS PUSH'S CAUSE. The refusal file is one per git dir and nothing here removes
# it, so another push from the same git dir can write it while this call runs: a token newer than the
# stamp this call created just before its push is appended on rc 2 as an ADVISORY only. The
# `default-branch` hint comes from this call's own read: rc 2 and no `refs/remotes/<name>/HEAD`.
# The stamp is a scratch file of its own, never the push's output file, which git writes after the
# hook ran and so would read every token as stale.
# THE ONE SUCCESS EXIT JOINS THE FEED (TOOL-dPlacedRequest-13 S3): it calls `write_feed_success` from
# the `gov_feed_sh` block every carrier of this one carries beside it (TOOL-dPlacedRequest-34 S5), which
# sets this node's cache ref `refs/gov/remote/<tail>` to what it wrote, or clears it on a deletion, and
# appends the event. A lost or uncompleted write appends nothing.
# WHAT THIS DOES NOT CHECK: a token written in the stamp's own filesystem tick reads as stale and is
# omitted; a token another push wrote during this call reads as fresh and is printed beside this
# push's own cause, never as it.
build_gov_commit() { # tip read or empty · message -> prints the commit; rc 1 when git cannot build it
  local t c
  local -a p=()
  [ -z "$1" ] || p=(-p "$1")
  t=$(git mktree </dev/null 2>/dev/null) && [ -n "$t" ] || return 1
  c=$(GIT_AUTHOR_NAME=gov-claim GIT_AUTHOR_EMAIL=gov-claim@invalid GIT_COMMITTER_NAME=gov-claim GIT_COMMITTER_EMAIL=gov-claim@invalid \
    git commit-tree "$t" "${p[@]}" -m "$2" 2>/dev/null) && [ -n "$c" ] || return 1
  printf '%s\n' "$c"
}
write_gov_ref() {    # ref · expected sha or empty · src -> 0 written, 1 lost, 2 not completed; GOVREF_WHY
  local ref="$1" exp="$2" src="$3" s f rc l line rf="" tok="" hd=""
  GOVREF_WHY=""
  if [ -z "$src" ] && [ "${FUNCNAME[1]:-}" != remove_gov_ref ]; then GOVREF_WHY="no source"; return 2; fi
  s=$(mktemp) || { GOVREF_WHY="cannot create a scratch file to bound the push"; return 2; }
  f=$(mktemp) || { rm -f "$s"; GOVREF_WHY="cannot create a scratch file to bound the push"; return 2; }
  "$GOVREF_RUNNER" "$f" push --porcelain "--force-with-lease=$ref:$exp" "$GOVREF_REMOTE" "$src:$ref" && rc=0 || rc=$?
  line=""
  while IFS= read -r l; do
    case "$l" in ?$'\t'*":$ref"$'\t'*) line=${l%$'\r'} ;; esac
  done <"$f"
  if [ "$rc" = 124 ]; then GOVREF_WHY="the push was killed by this kit's own bound"; rc=2
  elif [ -z "$line" ]; then GOVREF_WHY="git push exited $rc and printed no status line for $ref"; rc=2
  elif [ "${line:0:1}" != '!' ]; then rc=0
  else
    case "$line" in
      *"(stale info)"*|*"(fetch first)"*) GOVREF_WHY="lost the race on the lease: ${line##*$'\t'}"; rc=1 ;;
      *) GOVREF_WHY="the push was refused: ${line##*$'\t'}"; rc=2 ;;
    esac
  fi
  if [ "$rc" = 2 ]; then
    [ -z "${GOVREF_GITDIR:-}" ] || rf="$GOVREF_GITDIR/pre-push-refusal"
    if [ -n "$rf" ] && [ "$rf" -nt "$s" ]; then
      { IFS=$'\t' read -r tok _ <"$rf"; } 2>/dev/null || :
      GOVREF_WHY="$GOVREF_WHY · a pre-push refusal was recorded during this push: ${tok:-an empty refusal file}"
    fi
    hd=$(git symbolic-ref -q "refs/remotes/$GOVREF_REMOTE/HEAD" 2>/dev/null) || hd=""
    [ -n "$hd" ] || GOVREF_WHY="$GOVREF_WHY · default-branch · fix once: git remote set-head $GOVREF_REMOTE -a"
  fi
  rm -f "$s" "$f"
  [ "$rc" = 0 ] || return "$rc"
  write_feed_success "$ref" "$src"
  return 0
}
remove_gov_ref() {   # ref · expected sha -> as write_gov_ref, pushing the ref's deletion
  GOVREF_WHY=""
  [ -n "$2" ] || { GOVREF_WHY="no expected sha"; return 2; }
  write_gov_ref "$1" "$2" ""
}
# <<< gov_ref_sh
# >>> gov_feed_sh — canonical copy: gov-feed.sh in gov's lib dir (byte-identical; gated)
# THE NODE LOCKS (TOOL-dPlacedRequest-24): a node-local file two sessions of this node write, the
# feed's log and the offline queue's, is read and written only under a lock directory beside it in
# the common dir, taken through `write_dir_lock_wait` with the stem `node`, so a stale break appends
# `node-lock-broken` or `node-guard-cleared`. NODE_LOCK_BOUND is the seconds a node lock may hold:
# a pinned literal, because a holder does local file work alone and never pushes while it holds.
NODE_LOCK_BOUND=10
# THE DIRECTORY LOCK (TOOL-aGraftedHelix-37), a factory (TOOL-aPiecewiseGrade-6), moved into this
# block (TOOL-dPlacedRequest-24) so every carrier holds the one definition. `write_dir_lock` takes the
# lock with `mkdir` and writes its deadline into `until` and the caller's token into `owner`. A lock it cannot
# make is broken only when `check_dir_lock_stale` reads it stale - a deadline already passed,
# or none and a directory older than two minutes - and only by the writer that takes the guard
# `<lock>.break` with `mkdir`. Holding the guard it re-reads the rule, breaks a lock still stale,
# makes it again and writes both files before it releases the guard; a re-read finding the lock live,
# or a re-make losing to a plain `mkdir`, releases the guard and reports busy. So no breaker removes
# a lock another breaker made. A guard older than one minute was left by a crash: the writer finding
# it removes it and reports busy, never taking it in the same call, and the next call breaks the
# lock. Each self-heal appends a health event, named from the caller's stem, once the guard is
# released. `write_dir_lock_wait` is the one retrying take: it calls `write_dir_lock` every 50 ms
# until it takes or its ceiling in seconds passes, read on the whole-second clock. `remove_dir_lock`
# clears the lock only while its `owner` reads the caller's token, the turnstile's nonce pattern, so
# a release never removes the fresh lock of a writer that broke it. `until` stays a bare epoch.
# WHAT THIS DOES NOT CHECK: removing an abandoned guard is itself unguarded, so two writers removing
# one at once while a third takes a fresh guard between them can admit two breakers; that needs a
# writer to die or stall for a minute inside the break, then four writers in one git dir in one
# window. An owner that outlives its recorded deadline (no runnable `timeout -k`) is breakable while
# it pushes, and its own release can land between a breaker's re-read and its removal. Both the
# deadline and the age are wall-clock reads, so a clock stepped forward breaks a live lock.
# A writer in another git dir takes another lock. Each event goes through the `health_log_sh` block
# every carrier holds beside this one (TOOL-dPlacedRequest-36), to `resolve_health_log` of `ROOT`
# where the driver sets it, so its spec-tokens lock in the sidecar dir logs to the repository's log,
# else of the lock's parent, which for a node lock is the common dir: no unset name under `set -u`.
# THE OWNER'S PROCESSES, read as data in the lock (TOOL-aPiecewiseGrade-6 S9). A holder may write one
# `pid.<role>` file per process with `write_dir_lock_pid`: the pid, its procfs start token or `-`, the
# writer's runtime as `$HOSTNAME:$OSTYPE`, and an optional end file, last because a path may carry a
# space. `check_dir_lock_stale` also reads a lock stale when it holds at least one such file and every
# one names a process gone: a digit pid, this runtime, `check_proc_gone` answering gone, and an end
# file that exists or whose directory is gone, or none recorded. An empty file, the pending `-`, a
# foreign runtime or a missing stamp reads live. A lock with no pid file keeps the deadline and age
# rule alone. The procfs read is `${PROCFS_ROOT:-/proc}`: the driver sets PROCFS_ROOT from its fixture
# seam, and a carrier with no driver reads `/proc`.
# WHAT THIS DOES NOT CHECK: two process tables printing one `$HOSTNAME:$OSTYPE`, such as two MSYS
# installs on one host, read each other's pids gone and can break a live lock; and a reused pid with
# no token reads live, so its lock waits for the deadline.
PT_TOKEN=""
read_proc_token() { # pid -> sets PT_TOKEN to its procfs start token, or `-` when procfs cannot say
  local _l="" _r
  local -a _f
  PT_TOKEN=-
  case "${1:-}" in ""|*[!0-9]*) return 0 ;; esac
  { IFS= read -r _l < "${PROCFS_ROOT:-/proc}/$1/stat" || [ -n "$_l" ]; } 2>/dev/null || return 0
  # EVERY FIELD AFTER THE LAST `)` IS NUMERIC OR ONE LETTER. The command name inside the parentheses
  # may carry spaces and parentheses of its own, so the split starts after it: field 3 is `_f[0]`.
  _r=${_l##*) }
  read -r -a _f <<<"$_r"
  [ "${#_f[@]}" -ge 20 ] || return 0
  case "${_f[19]}" in ""|*[!0-9]*) return 0 ;; esac
  PT_TOKEN=${_f[19]}
  return 0
}
# Is the RECORDED process still there? Dead, or its pid now carrying another start token, is gone.
check_proc_gone() { # pid · recorded token -> 0 when that process no longer exists
  kill -0 "$1" 2>/dev/null || return 0
  [ "${2:--}" != - ] || return 1
  read_proc_token "$1"
  [ "$PT_TOKEN" != - ] && [ "$PT_TOKEN" != "$2" ] && return 0
  return 1
}
check_dir_lock_stale() { # lock dir -> 0 when its deadline passed, or it has none and is older than two minutes, or every process it records is gone
  local lu="" f p t w e n=0; { read -r lu <"$1/until"; } 2>/dev/null || :
  case "$lu" in *[!0-9]*) lu="" ;; esac
  for f in "$1"/pid.*; do
    [ -f "$f" ] || continue
    p=""; t=""; w=""; e=""; { read -r p t w e <"$f"; } 2>/dev/null || :
    case "$p" in ""|*[!0-9]*) n=-1; break ;; esac
    [ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && check_proc_gone "$p" "$t" \
      && { [ -z "$e" ] || [ -e "$e" ] || [ ! -d "${e%/*}" ]; } || { n=-1; break; }
    n=$((n + 1))
  done
  [ "$n" -le 0 ] || return 0
  if [ -n "$lu" ]; then [ "$lu" -lt "$EPOCHSECONDS" ]; return; fi
  [ -n "$(find "$1" -maxdepth 0 -mmin +2 2>/dev/null)" ]
}
write_dir_lock_pid() { # lock dir · role · pid, or - for pending · end file, optional -> <lock>/pid.<role> written; always 0
  read_proc_token "$3"
  printf '%s %s %s %s\n' "$3" "$PT_TOKEN" "${HOSTNAME:-}:${OSTYPE:-}" "${4:-}" >"$1/pid.$2" 2>/dev/null || :
  return 0
}
write_dir_lock() { # lock dir · owner token · seconds it may hold · health-event stem -> 0 taken, 1 busy
  local lk="$1" g="$1.break" broke=""
  if ! mkdir "$lk" 2>/dev/null; then
    check_dir_lock_stale "$lk" || return 1
    if ! mkdir "$g" 2>/dev/null; then
      if [ -n "$(find "$g" -maxdepth 0 -mmin +1 2>/dev/null)" ]; then
        rm -rf "$g"
        add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-guard-cleared" "$g"
      fi
      return 1
    fi
    if ! check_dir_lock_stale "$lk"; then rmdir "$g" 2>/dev/null; return 1; fi
    rm -rf "$lk"
    mkdir "$lk" 2>/dev/null || { rmdir "$g" 2>/dev/null; return 1; }
    broke=1
  fi
  printf '%s\n' "$(( $EPOCHSECONDS + $3 ))" >"$lk/until" 2>/dev/null || :
  printf '%s\n' "$2" >"$lk/owner" 2>/dev/null || :
  if [ -n "$broke" ]; then
    rmdir "$g" 2>/dev/null
    add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended "$4-lock-broken" "$lk"
  fi
  return 0
}
write_dir_lock_wait() { # lock dir · owner token · seconds it may hold · health-event stem · seconds to wait -> 0 taken, 1 busy
  local end=$(( EPOCHSECONDS + ${5:-0} ))
  until write_dir_lock "$1" "$2" "$3" "$4"; do
    [ "$EPOCHSECONDS" -lt "$end" ] || return 1
    sleep 0.05
  done
  return 0
}
remove_dir_lock() { # lock dir · owner token -> removes it only while its owner file reads that token
  local o=""; { read -r o <"$1/owner"; } 2>/dev/null || :
  [ -n "$2" ] && [ "$o" = "$2" ] && rm -rf "$1"
  return 0
}
# I4, THE CHANGE FEED (TOOL-dPlacedRequest-13): `<git-common-dir>/gov-feed.log`, node-local and never
# pushed, one LF-terminated line per governance ref write this node made or saw, six TAB fields:
# seq (a positive integer rising across refs), ref (the remote ref name), kind (the segment after
# `refs/gov/`), blob (the commit's tree, `-` on a deletion), commit (40 hex, 40 zeros on a deletion)
# and seen-utc (`2026-10-25T14:03:07Z`, this node's clock at the append). The key is ref, blob and
# commit. `write_gov_ref`'s success exit calls `write_feed_success`, which calls `add_feed_event`, so every
# writer joins by construction.
# APPENDING ONCE: under the feed's node lock (above, a 5 s wait) an event whose blob and commit
# equal the newest line of its ref appends nothing (TOOL-dPlacedRequest-27), so a retry appends nothing and a repeat with another
# event of the ref between, a second clear of `bar-red` say, appends again; `seq` is one more
# than the larger of the counter `gov-feed.seq` and the last all-digit first field of the log, so a
# lagging counter never repeats a `seq`; a last byte that is not LF is closed with one first, so a
# torn line stays for `check_feed` to name. A failure prints ONE `feed: NOTE -` line on stderr and
# returns 0, as the health log's appender does: the governance write already landed.
# THE CONTAINED APPEND (TOOL-dPlacedRequest-39): the clock test, the common dir and the git reads run
# in the caller's shell; the lock, the key check, the counter and the append run in a subshell whose
# `EXIT` trap, armed once the lock is taken, calls `remove_dir_lock` with this call's token. So an
# abort inside it, an unbound name under a carrier's `set -u`, a function no carrier defines or a
# failed write, ends the subshell alone: the append prints `feed: NOTE - <ref>: the append exited
# <rc>` and returns 0, and no lock is left for the next writer to wait out. The subshell sets no
# global a caller reads. WHAT THIS DOES NOT CHECK: an abort between the take and the trap's arming
# leaves the lock to its deadline; an abort after the line is written reads as a NOTE all the same.
# THE BASH FLOOR (TOOL-dPlacedRequest-37): a node lock's deadline reads `EPOCHSECONDS`, bash 5's,
# and this is the one take a carrier with no driver reaches, so where it is unset the append prints
# one `feed: NOTE -` line naming it and returns 0, before it touches the lock, the log or git.
# THE CACHE `refs/gov/remote/<tail>` mirrors `refs/gov/<tail>` on the remote: what this node fetched
# and, through `write_gov_ref`, what it wrote. `add_feed_sightings` appends, oldest first, the unseen
# first-parent chain of every cached ref whose tip is not the commit of the feed's newest line for
# that ref, stopping at that commit or at the first commit not authored `gov-claim`, appended as a
# lone event, so a ref another node set back to a commit an older line holds is sighted again.
# `derive_feed_events` is the same walk with no feed to stop at; `check_feed` holds a feed to it per
# ref git still holds (`missing`, `duplicate` for two consecutive events of one ref with one blob and
# commit, `extra` on a ref whose tip is a `gov-claim` commit, `order`, `torn`), and `write_feed`
# writes it as a fresh feed where none is present.
# GOVFEED_DIR names the common dir; unset, the first call resolves it once for the process.
# WHAT THIS DOES NOT CHECK: two breakers the guard's own blind spots (above) admit can both append, which
# gives two events one `seq` and loses none; `seq` and `seen-utc` are node-local and never compared; a
# ref's events from before a deletion of it are outside every chain git holds and are not compared;
# a retry made after another event of its ref landed appends again, an event that did happen.
add_feed_event() {   # ref · commit, or empty for a deletion -> 0 always, the event appended once
  local ref="$1" c="${2:-}" d k t=- r s=0 l n now tok rc=0
  [ -n "${EPOCHSECONDS:-}" ] || { printf 'feed: NOTE - no EPOCHSECONDS, bash 5 or later is required\n' >&2; return 0; }
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: NOTE - no git common dir resolves here, so this write of %s is not in the feed\n' "$ref" >&2; return 0; }
  k=${ref#refs/gov/}; k=${k%%/*}
  if [ -z "$c" ]; then
    c=0000000000000000000000000000000000000000
  else
    r=$(git rev-parse "$c^{commit}" "$c^{tree}" 2>/dev/null) || r=""
    r=${r//$'\r'/}; c=${r%%$'\n'*}; t=${r#*$'\n'}
    [ "${#c}:${#t}" = 40:40 ] || c=""
    case "$c$t" in *[!0-9a-f]*|"") printf 'feed: NOTE - %s names no commit this clone holds, so the write is not in the feed\n' "$ref" >&2; return 0 ;; esac
  fi
  tok="$BASHPID.$RANDOM"
  ( write_dir_lock_wait "$d/gov-feed.lock" "$tok" "$NODE_LOCK_BOUND" node 5 || exit 3
    trap 'remove_dir_lock "$d/gov-feed.lock" "$tok"' EXIT
    if [ -f "$d/gov-feed.log" ] && FEED_EV="$ref"$'\t'"$t"$'\t'"$c" awk -F'\t' '
        BEGIN { split(ENVIRON["FEED_EV"], ev, "\t") }
        $2 == ev[1] { p = $4 "\t" $5 }
        END { exit !(p == ev[2] "\t" ev[3]) }' "$d/gov-feed.log" 2>/dev/null; then
      exit 0
    fi
    if [ -f "$d/gov-feed.seq" ]; then { read -r s <"$d/gov-feed.seq"; } 2>/dev/null || :; fi
    s=${s%$'\r'}
    case "$s" in ""|*[!0-9]*) s=0 ;; esac
    l=0
    if [ -s "$d/gov-feed.log" ]; then
      l=$(awk -F'\t' '$1 ~ /^[0-9]+$/ { s = $1 } END { print s + 0 }' "$d/gov-feed.log" 2>/dev/null) || l=0
      case "$l" in ""|*[!0-9]*) l=0 ;; esac
      [ -z "$(tail -c1 "$d/gov-feed.log" 2>/dev/null)" ] || printf '\n' >>"$d/gov-feed.log"
    fi
    n=$(( (10#$s > 10#$l ? 10#$s : 10#$l) + 1 ))
    TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
    if ! printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$n" "$ref" "$k" "$t" "$c" "$now" >>"$d/gov-feed.log" 2>/dev/null; then
      printf 'feed: NOTE - %s/gov-feed.log could not be written, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2
    elif ! { printf '%s\n' "$n" >"$d/gov-feed.seq.$$" && mv -f "$d/gov-feed.seq.$$" "$d/gov-feed.seq"; } 2>/dev/null; then
      rm -f "$d/gov-feed.seq.$$" 2>/dev/null
      printf 'feed: NOTE - %s/gov-feed.seq could not be written; the next append reads the log past it\n' "$d" >&2
    fi
    exit 0 ) || rc=$?
  case "$rc" in
    0) ;;
    3) printf 'feed: NOTE - the feed lock in %s was held for 5s, so this write of %s at %s is not in the feed\n' "$d" "$ref" "$c" >&2 ;;
    *) printf 'feed: NOTE - %s: the append exited %s\n' "$ref" "$rc" >&2 ;;
  esac
  return 0
}
# THE ONE SUCCESS EXIT (TOOL-dPlacedRequest-34 S5): a governance write that landed sets this node's cache
# ref `refs/gov/remote/<tail>` to the commit it wrote, or clears it on a deletion, then appends the event,
# so the cache always names what this node last wrote or fetched. `write_gov_ref` calls it, and so does a
# carrier whose push is no `write_gov_ref` call, the lander's fenced beat (S6). A cache ref git cannot
# move prints ONE `feed: NOTE -` line and the event is appended all the same: the write already landed.
write_feed_success() { # ref · commit, or empty for a deletion -> 0 always; the cache ref set or cleared, the event appended
  if [ -n "${2:-}" ]; then git update-ref "refs/gov/remote/${1#refs/gov/}" "$2" 2>/dev/null
  else git update-ref -d "refs/gov/remote/${1#refs/gov/}" 2>/dev/null; fi \
    || printf 'feed: NOTE - the cache ref refs/gov/remote/%s was not set to this write\n' "${1#refs/gov/}" >&2
  add_feed_event "$1" "${2:-}"
  return 0
}
derive_feed_events() { # cache prefix · [feed file] -> `ref TAB kind TAB blob TAB commit` per event, per ref oldest first
  local pre="${1%/}/" feed="${2:-}" rows r t g s
  rows=$(git for-each-ref --format='%(refname) %(objectname)' "$pre" 2>/dev/null | FEED_FILE="$feed" FEED_PRE="$pre" awk '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") < 5) continue
              newest[x[2]] = x[5] } }
    { sub(/\r$/, ""); g = "refs/gov/" substr($1, length(ENVIRON["FEED_PRE"]) + 1)
      if ((g in newest) && newest[g] == $2) next
      print $2, g, (g in newest ? newest[g] : "-") }')
  [ -n "$rows" ] || return 0
  printf '%s\n' "$rows" | while read -r t g s; do
    git log --first-parent --format='%H %T %an' "$t" 2>/dev/null | awk -v ref="$g" -v stop="$s" '
      { sub(/\r$/, "") }
      $1 == stop { exit }
      { a = $0; sub(/^[^ ]+ [^ ]+ /, "", a); n++; h[n] = $1; tr[n] = $2; if (a != "gov-claim") exit }
      END { k = ref; sub(/^refs\/gov\//, "", k); sub(/\/.*$/, "", k)
            for (i = n; i >= 1; i--) printf "%s\t%s\t%s\t%s\n", ref, k, tr[i], h[i] }'
  done
  return 0
}
add_feed_sightings() { # cache prefix -> 0 always; every unseen commit of a cached ref appended oldest first
  local pre="${1:-refs/gov/remote/}" r k t c
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -n "${GOVFEED_DIR%$'\r'}" ] || return 0
  while IFS=$'\t' read -r r k t c; do
    [ -z "$c" ] || add_feed_event "$r" "$c"
  done < <(derive_feed_events "$pre" "${GOVFEED_DIR%$'\r'}/gov-feed.log")
  return 0
}
check_feed() {       # cache prefix · [feed file, the node's by default] -> one line per finding and rc 1, or rc 0
  local pre="${1%/}/" f="${2:-}" dv au
  if [ -z "$f" ]; then
    [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
    f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  fi
  dv=$(derive_feed_events "$pre")
  au=$(git for-each-ref --format='%(refname) %(authorname)' "$pre" 2>/dev/null)
  FEED_FILE="$f" FEED_PRE="$pre" FEED_DV="$dv" FEED_AU="$au" awk '
    BEGIN {
      np = length(ENVIRON["FEED_PRE"])
      m = split(ENVIRON["FEED_AU"], a, "\n")
      for (i = 1; i <= m; i++) { ln = a[i]; sub(/\r$/, "", ln); if (ln == "") continue
        r = ln; sub(/ .*$/, "", r); au = ln; sub(/^[^ ]* /, "", au)
        g = "refs/gov/" substr(r, np + 1); held[g] = 1; if (au == "gov-claim") chain[g] = 1 }
      m = split(ENVIRON["FEED_DV"], a, "\n")
      for (i = 1; i <= m; i++) { if (split(a[i], x, "\t") != 4) continue
        dn[x[1]]++; ds[x[1], dn[x[1]]] = x[4]; inch[x[1] SUBSEP x[4]] = 1 }
      f = ENVIRON["FEED_FILE"]; bad = 0
      while ((getline ln < f) > 0) {
        sub(/\r$/, "", ln)
        if (split(ln, x, "\t") != 6) { print "torn " ln; bad = 1; continue }
        k = x[4] SUBSEP x[5]
        if ((x[2] in last) && last[x[2]] == k) { print "duplicate " x[2] " " x[5]; bad = 1; continue }
        last[x[2]] = k
        if (!(x[2] in held)) continue
        if ((x[2] SUBSEP x[5]) in inch) { fn[x[2]]++; fs[x[2], fn[x[2]]] = x[5]; got[x[2] SUBSEP x[5]] = 1 }
        else if (x[2] in chain) { print "extra " x[2] " " x[5]; bad = 1 }
      }
      for (g in dn) {
        j = 0; off = ""
        for (i = 1; i <= dn[g]; i++) {
          c = ds[g, i]
          if (!((g SUBSEP c) in got)) { print "missing " g " " c; bad = 1; continue }
          j++; if (off == "" && fs[g, j] != c) off = fs[g, j]
        }
        if (off != "") { print "order " g " " off; bad = 1 }
      }
      exit bad }'
}
write_feed() {       # cache prefix -> rc 0 the derived feed written, rc 2 naming a feed already present
  local pre="${1%/}/" d now n=0 l
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: no git common dir resolves here, so no feed was rebuilt\n'; return 2; }
  if [ -e "$d/gov-feed.log" ]; then printf 'feed: a feed is present, so nothing was rebuilt over it: %s\n' "$d/gov-feed.log"; return 2; fi
  TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
  { while IFS= read -r l; do n=$((n + 1)); printf '%s\t%s\t%s\n' "$n" "$l" "$now"; done < <(derive_feed_events "$pre"); } >"$d/gov-feed.log.$$" \
    && printf '%s\n' "$n" >"$d/gov-feed.seq.$$" && mv -f "$d/gov-feed.seq.$$" "$d/gov-feed.seq" && mv -f "$d/gov-feed.log.$$" "$d/gov-feed.log" \
    || { rm -f "$d/gov-feed.log.$$" "$d/gov-feed.seq.$$"; printf 'feed: %s could not be written, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
  printf 'feed: rebuilt %s event(s) from %s into %s\n' "$n" "$pre" "$d/gov-feed.log"
  return 0
}
print_feed() {       # [seq] -> every event whose seq is at or after it, in file order
  local from="${1:-0}" d
  case "$from" in ""|*[!0-9]*) printf 'feed: a replay starts at a sequence number, not %s\n' "$from"; return 2 ;; esac
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -f "$d/gov-feed.log" ] || return 0
  awk -F'\t' -v from="$from" 'NF == 6 && $1 ~ /^[0-9]+$/ && $1 + 0 >= from + 0' "$d/gov-feed.log"
}
# THE OBSERVER CLOCK, I8 (TOOL-dPlacedRequest-17): the one reader of a first sighting. Per
# `ref TAB commit` pair on stdin, in order, the `seen-utc` of the oldest feed line of that ref and
# commit, or `-` where the feed holds none, has none of that shape, or cannot be read. Every lease
# deadline is now minus that stamp, both read on this node's clock, never the holder's `beat-utc`.
read_first_seen() {  # `ref TAB commit` pairs on stdin -> one `seen-utc` or `-` per pair
  local f=""
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  [ -z "${GOVFEED_DIR%$'\r'}" ] || f="${GOVFEED_DIR%$'\r'}/gov-feed.log"
  FEED_FILE="$f" awk -F'\t' '
    BEGIN { f = ENVIRON["FEED_FILE"]
            if (f != "") while ((getline ln < f) > 0) {
              sub(/\r$/, "", ln)
              if (split(ln, x, "\t") != 6 || x[6] !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]Z$/) continue
              if (!((x[2] SUBSEP x[5]) in seen)) seen[x[2], x[5]] = x[6] } }
    { sub(/\r$/, ""); print (($1 SUBSEP $2) in seen ? seen[$1, $2] : "-") }'
}
# <<< gov_feed_sh
# >>> health_log_sh — canonical copy: health-log.sh in gov's lib dir (byte-identical; gated)
# I3, THE HEALTH LOG (TOOL-aGraftedHelix-8): `<git-common-dir>/health.log`, one LF-terminated UTF-8
# line per automatic self-heal, four TAB-separated fields: utc (`YYYY-MM-DDTHH:MM:SS+00:00`), source
# and event (each `^[a-z][a-z0-9-]*$`), and a detail whose TAB, CR and LF are each folded to one space
# and which is cut to 240 characters. At HEALTH_LOG_CAP_LINES lines the appender first keeps the
# newest half, through a temp file and a rename, then appends. `derive_health_log <common-dir>` prints
# the path and spawns nothing; `resolve_health_log <repo-dir>` asks git once and prints it, or fails
# printing nothing; `add_health_event <log> <source> <event> <detail>` is the only writer. A refused
# token, an empty path or a failed write prints ONE `health: NOTE -` line on stderr and returns 0: it
# never fails its caller. WHAT IT DOES NOT DO: serialize concurrent writers (a trim racing an append
# can lose that line; ponytail: one rename, a lock file if a lost line is ever observed); validate
# what a detail means; or tell a repository with no writer installed from one where nothing healed.
HEALTH_LOG_CAP_LINES=500
derive_health_log() { printf '%s/health.log\n' "$1"; }
resolve_health_log() {
  local _hl_c
  _hl_c=$(git -C "$1" rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || return 1
  _hl_c=${_hl_c%$'\r'}
  [ -n "$_hl_c" ] || return 1
  derive_health_log "$_hl_c"
}
add_health_event() {
  local _hl_log=${1:-} _hl_src=${2:-} _hl_ev=${3:-} _hl_d=${4:-} _hl_why="" _hl_n=0 _hl_t
  local _hl_a=abcdefghijklmnopqrstuvwxyz
  case "$_hl_src" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="source '$_hl_src' is not a lowercase token" ;; esac
  case "$_hl_ev" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="event '$_hl_ev' is not a lowercase token" ;; esac
  [ -n "$_hl_log" ] || _hl_why="no log path resolved"
  if [ -z "$_hl_why" ]; then
    _hl_d=${_hl_d//$'\t'/ }; _hl_d=${_hl_d//$'\r'/ }; _hl_d=${_hl_d//$'\n'/ }; _hl_d=${_hl_d:0:240}
    _hl_t=$(date -u +%Y-%m-%dT%H:%M:%S+00:00 2>/dev/null) || _hl_t=""
    [ -n "$_hl_t" ] || _hl_why="date printed no UTC stamp"
  fi
  if [ -z "$_hl_why" ] && [ -f "$_hl_log" ]; then
    _hl_n=$(wc -l < "$_hl_log" 2>/dev/null) || _hl_n=0
    _hl_n=${_hl_n//[!0-9]/}
    if [ "${_hl_n:-0}" -ge "$HEALTH_LOG_CAP_LINES" ]; then
      { tail -n $((HEALTH_LOG_CAP_LINES / 2)) "$_hl_log" > "$_hl_log.trim.$$" && mv -f "$_hl_log.trim.$$" "$_hl_log"; } 2>/dev/null \
        || { rm -f "$_hl_log.trim.$$" 2>/dev/null; _hl_why="the trim to the newest $((HEALTH_LOG_CAP_LINES / 2)) lines failed"; }
    fi
  fi
  if [ -z "$_hl_why" ]; then
    { printf '%s\t%s\t%s\t%s\n' "$_hl_t" "$_hl_src" "$_hl_ev" "$_hl_d" >> "$_hl_log"; } 2>/dev/null && return 0
    _hl_why="the append failed"
  fi
  printf 'health: NOTE - %s: %s; nothing written\n' "${_hl_log:-(no path)}" "$_hl_why" >&2
  return 0
}
# <<< health_log_sh

run_worktree_remote() { # <outfile> · <git args…> -> as run_remote, from the scratch worktree
  local out=$1; shift
  run_remote "$out" -C "$WT" "$@"
}

# The leased push, from the scratch worktree, by remote NAME, through the one writer above
# (TOOL-dPlacedRequest-11). <src> is a sha to create or advance the ref; `remove_red_ref` deletes it.
# GOVREF_RUNNER, GOVREF_REMOTE and GOVREF_GITDIR are set once the scratch worktree exists.
PM_PUSH_SRC=""
write_red_ref() { # lease (observed sha, empty when absent) -> rc 0, or rc 1 with PM_WHY
  PM_WHY=""
  write_gov_ref "$PM_RED_REF" "$1" "$PM_PUSH_SRC" && return 0
  PM_WHY=$GOVREF_WHY; return 1
}
remove_red_ref() { # lease (the observed sha) -> as write_red_ref, deleting the ref
  PM_WHY=""
  remove_gov_ref "$PM_RED_REF" "$1" && return 0
  PM_WHY=$GOVREF_WHY; return 1
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
  local tree w paths="" dirty t
  local -a words=()
  # The hook's and the driver's writers refuse a dirty tree, and so does this one: a bar judged on rc
  # and HEAD alone may have rewritten tracked files, and the record would certify the pristine tree.
  if ! dirty=$(git -C "$WT" status --porcelain --ignore-submodules=untracked 2>/dev/null) || [ -n "$dirty" ]; then
    echo "post-merge: no gate-bar-green.shared written — the scratch worktree is not clean after the bar"
    return 0
  fi
  tree=$(git rev-parse -q --verify "$SHA^{tree}" 2>/dev/null) || tree=""
  read -ra words <<<"$BAR"
  for w in "${words[@]}"; do case "$w" in */*|*.sh) paths="$paths${paths:+ }$w" ;; esac; done
  t=$(mktemp -u "$CDIR/gate-bar-green.shared.XXXXXXXX" 2>/dev/null)
  { printf 'sha\t%s\ntree\t%s\nbar\t%s\nbar_paths\t%s\nkind\tfull\nbase\t\nselftests\t%s\nrun_id\t%s\nby\tpost-merge\nstamped\t%s\n' \
      "$SHA" "$tree" "$BAR" "$paths" "${GATE_SELFTESTS:+1}" "$RUN_ID" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      > "$t" && mv -f "$t" "$CDIR/gate-bar-green.shared"; } 2>/dev/null \
    || { [ -z "$t" ] || rm -f "$t" 2>/dev/null; echo "post-merge: $CDIR/gate-bar-green.shared could not be written"; }
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
GOVREF_RUNNER=run_worktree_remote; GOVREF_REMOTE=$REMOTE; GOVREF_GITDIR=$PM_WT_GD

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

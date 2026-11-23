#!/usr/bin/env bash
# The governance ref's one compare-and-swap writer, canonical copy (TOOL-dPlacedRequest-11, I1, I2).
#
# USAGE: `<prefix>/lib/` ships nothing, so a writer cannot source this file. Each one carries the
# block between the markers below INLINE, byte-identical, and the parity table in
# `resolve-python.test.sh` beside this file reds a copy that drifts. A probe sources this file whole,
# with gov-feed.sh beside it, whose `add_feed_event` the writer's success exit calls.

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
# appends the event. A lost or uncompleted write appends nothing. A CHAIN'S LOWER COMMITS
# (KICK-dKeptSession-63 S16): a caller that built several commits and lands them in this one write
# names those below the source as trailing arguments, oldest first, and on rc 0 each is appended with
# `add_feed_event` in the order given before the source's own event, so this node's feed holds a first
# sighting of every commit the write landed. Nothing is walked: a caller naming none appends the one
# event, whatever history lies under its source.
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
write_gov_ref() {    # ref · expected sha or empty · src · [lower commit ...] -> 0 written, 1 lost, 2 not completed; GOVREF_WHY
  local ref="$1" exp="$2" src="$3" s f rc l line rf="" tok="" hd="" lc
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
  for lc in "${@:4}"; do add_feed_event "$ref" "$lc"; done
  write_feed_success "$ref" "$src"
  return 0
}
remove_gov_ref() {   # ref · expected sha -> as write_gov_ref, pushing the ref's deletion
  GOVREF_WHY=""
  [ -n "$2" ] || { GOVREF_WHY="no expected sha"; return 2; }
  write_gov_ref "$1" "$2" ""
}
# <<< gov_ref_sh

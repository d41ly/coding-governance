#!/usr/bin/env bash
# push-main.sh — the sanctioned lander for a push to the default branch (TOOL-aLeasedGauntlet-1,
# ports inCMS ARCH-aLeasedGauntlet-1).
#
# Reconciles the default branch BEFORE the pre-push full gate runs, so the gate never runs on an
# already-stale tree; if origin advances DURING the gate the push is rejected and this re-reconciles
# + re-gates, bounded by GOV_PUSH_MAIN_MAX_RETRIES (default 3). It sets a marker the pre-push hook
# requires, so a raw `git push` to the default branch is refused and steered here. Bypass:
# git push --no-verify.
#
# First push to a BRAND-NEW remote (no default-branch ref yet): seed it once with `git push
# --no-verify origin <branch>` — push-main reconciles an EXISTING branch and can't bootstrap one.
#
# USAGE
#   push-main.sh                             the attended landing: from the primary tree, with the
#                                            default branch checked out, pushing that branch.
#   push-main.sh --prepare  --slug <slug>    merge THIS branch onto the tip the remote advertises,
#                                            in place, and move the branch to that merge.
#   push-main.sh --land     --slug <slug>    push that prepared merge, and nothing else, as the
#                                            default branch.
#   push-main.sh --carry    --slug <slug>    print what such a push would publish that rode in
#                                            through the LOCAL default branch; exit 1 on a commit
#                                            belonging to another build.
#   push-main.sh --prepared --slug <slug>    exit 0 when HEAD carries a prepared merge; read-only.
#
# WHY THE FLAGS EXIST — TOOL-dDerivedDocket-2. The attended path lands only from the primary tree
# with the default branch checked out, and it pushes that branch, which every build on the node
# shares. A run that is never on it therefore had to leave its own tree to land, and its landing
# could publish another build's unpushed commits. The flags land IN PLACE: the merge is made in the
# run's own worktree ONTO the advertised tip, exactly that merge is pushed as the default branch,
# and a commit that rode in through the local one and belongs to another build refuses the landing.
#
# EXIT CODES UNDER A FLAG. 0 done · 1 the landing was refused or failed · 2 an ARGUMENT refusal ·
# 3 an OBSERVATION failure: not a repository, an undeterminable default branch, an `ls-remote` or a
# fetch that did not answer. Two codes and not one, because a driver reads them differently: a 2
# says its own invocation is wrong and no retry will help, a 3 says the clone or the network is.
# The no-argument invocation keeps BASE's codes, its own exit 2 included.
set -u

# ---- ARGUMENTS, parsed before the first git call ------------------------------------------------
# BASE accepted no arguments and IGNORED any it was given, so a mistyped `--land` ran the attended
# path and pushed the local default branch — the exact hazard these flags exist to remove. Anything
# that is not one of the four flags or its `--slug` is therefore refused, and that refusal is the
# one observable change to the no-flag contract. It reaches only an invocation that passed something.
MODE=""
SLUG=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --prepare|--land|--carry|--prepared)
      if [ -n "$MODE" ]; then
        echo "push-main: '$1' and '--$MODE' are two different acts — run one flag per invocation." >&2
        exit 2
      fi
      MODE=${1#--}; shift ;;
    --slug)
      if [ "$#" -lt 2 ]; then
        echo "push-main: --slug needs the build slug as its value." >&2
        exit 2
      fi
      SLUG=$2; shift 2 ;;
    --slug=*)
      echo "push-main: spell the slug as two words, '--slug <slug>': $1" >&2
      exit 2 ;;
    *)
      echo "push-main: unrecognised argument '$1' — the flags are --prepare, --land, --carry and --prepared, each with --slug <slug>; no argument at all is the attended landing." >&2
      exit 2 ;;
  esac
done
if [ -z "$MODE" ] && [ -n "$SLUG" ]; then
  echo "push-main: --slug names a build but no flag says what to do with it — add --prepare, --land, --carry or --prepared." >&2
  exit 2
fi
if [ -n "$MODE" ]; then
  # The SAME grammar the memory tree enforces on a build-folder name, because that is what a slug
  # is; it reaches a commit message, so it is validated before it gets there.
  case "$SLUG" in
    *[!A-Za-z0-9-]* | "" | [!A-Za-z]*)
      echo "push-main: --$MODE needs --slug <slug>, a build-folder name: a letter, then letters, digits or dashes: '$SLUG'" >&2
      exit 2 ;;
  esac
fi
# What an OBSERVATION failure exits with. BASE spells 2 for every one of them and that spelling is
# kept for the no-flag path; under a flag they are 3, so a driver can tell "your invocation is
# wrong" from "the remote did not answer" (S7).
obs=2
[ -n "$MODE" ] && obs=3

top=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "push-main: not a git repo" >&2; exit "$obs"; }
cd "$top" || exit "$obs"

# Resolve the default branch, GOV_DEFAULT_BRANCH first then origin/HEAD. Fail CLOSED if neither is
# set — silently assuming 'main' would let a push to a real 'develop'/'master' default run un-gated.
def=${GOV_DEFAULT_BRANCH:-$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null)}
def=${def#origin/}
if [ -z "$def" ]; then
  echo "push-main: can't determine the default branch (origin/HEAD unset, GOV_DEFAULT_BRANCH unset) —" >&2
  echo "  set it with 'git remote set-head origin -a', or export GOV_DEFAULT_BRANCH=<branch>." >&2
  exit "$obs"
fi
remote=${GOV_REMOTE:-$(git config "branch.$def.remote" 2>/dev/null || echo origin)}
max=${GOV_PUSH_MAIN_MAX_RETRIES:-3}
marker="$(git rev-parse --git-dir)/push-main-active"

# The marker is a SOFT advisory guard: a SIGKILL/OOM/power-loss during the gate can leak it (this
# trap can't catch those). Worst case a later raw push skips reconcile-before-gate and wastes ONE
# gate run; nothing red reaches origin, and the next push-main run's EXIT trap clears a stale marker.
#
# NOT INSTALLED FOR THE TWO READ-ONLY FLAGS. `--carry` and `--prepared` answer a question and write
# nothing, and a trap that removes a file is a write — one a concurrent `--land` in this same
# worktree would feel. Their claim to write nothing is kept true here rather than asserted.
case "$MODE" in
  carry|prepared) ;;
  *) trap 'rm -f "$marker"' EXIT INT TERM ;;
esac

# KEEP THE CONNECTION ALIVE ACROSS THE GATE. The gate runs INSIDE the push: git connects and
# negotiates refs BEFORE `pre-push` fires - that is how the hook receives remote_sha on stdin - and
# the socket then idles for the entire bar. A server closes an idle SSH session, so the push dies at
# the very end, AFTER a green gate, with "Connection closed by remote host" and "unable to write
# flush packet: Broken pipe". The refusal this script prints for that case names auth, permissions
# and protocol, which is why it reads as anything except a timeout.
#
# It is not intermittent. It is a deadline race that a slow bar loses every time, so the longer the
# adopter's bar, the more certain the failure - and the failure lands on the attempt that did
# everything right.
#
# Measured on an adopter (inCMS, node `a`, 2026-08-27), same objects and same auth throughout: a push
# to a scratch ref, whose hook ran only a ~4-minute subset, SUCCEEDED; four pushes to main, whose hook
# ran the 16-to-65-minute full bar, all died this way, two of them after the gate printed PASSED.
# Setting these three options and changing nothing else landed it first try. That repo's charter had
# recorded the same failure a fortnight earlier as "unrelated to code".
#
# THIS REPO PUSHES OVER HTTPS and so cannot exercise it, which is exactly why it went unnoticed here:
# the exposure belongs to every adopter that installs this lander and pushes over SSH.
#
# `:=` so a caller who has their own GIT_SSH_COMMAND keeps it - theirs may carry an identity or a
# proxy this must not drop. ServerAliveCountMax is deliberately large: the product with the interval
# is the tolerated silence, and it has to outlast the SLOWEST bar an adopter can produce, not the
# fastest. Costs one 32-byte keepalive every 30 s on an otherwise idle socket.
: "${GIT_SSH_COMMAND:=ssh -o ServerAliveInterval=30 -o ServerAliveCountMax=120 -o TCPKeepAlive=yes}"
export GIT_SSH_COMMAND

# ---- SHARED BY BOTH PATHS -----------------------------------------------------------------------
# Lifted out of the attended path by TOOL-dDerivedDocket-2 so the in-place landing writes the same
# record and classifies a failure by the same reading. Two spellings of either would be two answers
# to one question, and the copy is always the one that drifts.

# Classify a push failure on what git SAID (streamed live via tee, also captured), not on whether
# origin moved (a guard on the wrong signal calls a gate-passed-but-network-failed push "RED", and
# loops a still-RED commit as a race when a peer advanced origin during the gate).
parse_push_class() {  # captured-output-file -> race | unreachable | red
  if grep -qiE 'rejected|fetch first|non-fast-forward|stale info' "$1"; then echo race; return 0; fi
  if grep -qiE 'unable to access|could not resolve host|could not read from remote|connection|timed out' "$1"; then
    echo unreachable; return 0
  fi
  git fetch "$remote" "$def" 2>/dev/null || true
  if git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then echo red; else echo race; fi
}

# THE LANDER MARKER, when the project declares one. It carries the pushed COMMIT, not just its own
# existence: a bare touched file is satisfied by any previous landing, which is the
# pass-by-finding-anything shape the unattended kit's own Definition of Done was stuck in before
# this. The unattended verb compares the sha, so evidence of an earlier landing cannot stand in
# for this one. Written only on the branch where the push actually succeeded, which is the whole
# point of it being evidence.
#
# SOURCED, not sed-parsed. The driver SOURCES this conf, so parsing it here with a pattern that
# only matches a double-quoted value read a DIFFERENT value than the reader did for any unquoted
# or single-quoted declaration - one half honouring a key the other could not see. A subshell
# source is the driver's exact semantics without polluting this script's namespace.
write_lander_marker() {  # -> 1 when the push landed but the record could not be written
  local lm _gcd
  [ -f .unattended.conf ] || return 0
  lm=$(. ./.unattended.conf 2>/dev/null; printf '%s' "${LANDER_MARKER:-}")
  [ -n "$lm" ] || return 0
  # RESOLVED AGAINST THE GIT COMMON DIR, which is the only directory both halves agree on. It
  # was tree-relative and wrong twice: each half resolved it against its own cwd, and in a
  # LINKED WORKTREE `.git` is a FILE, so `.git/unattended-landed` fails with `Not a directory`
  # and no unattended run could ever land from one.
  #
  # AND THE FAILURE IS REPORTED. `2>/dev/null || true` meant a lander that pushed but could
  # not record it still printed `landed`, and `--landed` then refused blaming the lander for
  # writing nothing - the one diagnosis guaranteed to send the reader at the wrong half.
  _gcd=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd) || _gcd=""
  if [ -z "$_gcd" ]; then
    echo "push-main: pushed $def, but could not resolve the git common dir to write the lander marker ($lm). The push SUCCEEDED and is not recorded." >&2
    return 1
  fi
  if ! printf 'landed %s at %s by push-main\n' "$def" "$(git rev-parse HEAD)" > "$_gcd/$lm"; then
    echo "push-main: pushed $def, but could not write the lander marker at $_gcd/$lm. The push SUCCEEDED and is not recorded." >&2
    return 1
  fi
  return 0
}

# ---- THE IN-PLACE LANDING (TOOL-dDerivedDocket-2) -----------------------------------------------
# Nothing below reads or writes the LOCAL default branch, with one exception that is the point of
# the carry set: `--land` READS it, to refuse publishing what rode in through it.

# R, the tip the remote ADVERTISES. Advertised and not fetched, because the fetched ref is a local
# copy of an earlier answer and this landing has to sit on what the remote holds now.
resolve_tip() {  # -> R on stdout
  local out rc
  out=$(git ls-remote "$remote" "refs/heads/$def" 2>/dev/null); rc=$?
  out=$(printf '%s\n' "$out" | awk 'NR==1{print $1}')
  if [ "$rc" -ne 0 ] || [ -z "$out" ]; then
    echo "push-main: could not observe $remote/$def — 'git ls-remote $remote refs/heads/$def' answered nothing, so the tip this landing must sit on is unknown." >&2
    return 1
  fi
  printf '%s\n' "$out"
}

# R's OBJECT, which a merge onto it and a walk that excludes it both need present. The fetched ref
# is cross-checked against the advertisement: a disagreement is a race between two reads of one
# remote, and acting on either answer would be acting on a tip that is no longer there.
read_tip_object() {  # R
  local f
  if ! git fetch "$remote" "$def" 2>/dev/null; then
    echo "push-main: 'git fetch $remote $def' failed, so the advertised tip ${1:0:8} is not here to land onto." >&2
    return 1
  fi
  f=$(git rev-parse --verify --quiet "refs/remotes/$remote/$def" 2>/dev/null || true)
  if [ -n "$f" ] && [ "$f" != "$1" ]; then
    echo "push-main: $remote/$def moved between two reads — advertised ${1:0:8}, fetched ${f:0:8}. Nothing was changed; re-run." >&2
    return 1
  fi
  if ! git cat-file -e "$1^{commit}" 2>/dev/null; then
    echo "push-main: $remote advertises ${1:0:8} for $def but fetching $def did not bring that commit here." >&2
    return 1
  fi
  return 0
}

# THE PREPARED MERGE, re-derived from the graph and never read from a file. Three facts, and the
# refusal names the one that failed:
#   1. a merge T sits on HEAD's first-parent line, every commit before it carrying one parent;
#   2. T's FIRST parent is the tip the remote advertises NOW;
#   3. T has a second parent and HEAD contains T.
# `rev-list --first-parent --min-parents=2 --max-count=1` is fact 1 whole: it walks the first-parent
# line and yields the NEAREST merge, so a second merge stacked on T is what comes back and fails
# fact 2 — which is the refusal AC10 asks for. A plain `git merge <remote>/<def>` on the branch
# produces a merge whose first parent is the old branch tip, and fails fact 2 the same way.
check_prepared_merge() {  # R -> T on stdout
  local t p1 p2
  t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD 2>/dev/null || true)
  if [ -z "$t" ]; then
    echo "push-main: HEAD carries no prepared merge — no merge commit sits on its first-parent line. Run 'push-main.sh --prepare --slug $SLUG' first." >&2
    return 1
  fi
  p1=$(git rev-parse --verify --quiet "$t^1" 2>/dev/null || true)
  p2=$(git rev-parse --verify --quiet "$t^2" 2>/dev/null || true)
  if [ "$p1" != "$1" ]; then
    echo "push-main: the merge ${t:0:8} on HEAD's first-parent line has ${p1:0:8} as its first parent, not the advertised tip ${1:0:8}." >&2
    echo "  A plain 'git merge $remote/$def', a second merge stacked on the prepared one, or a tip that moved since it was prepared all read this way." >&2
    echo "  Run 'push-main.sh --prepare --slug $SLUG', which merges this branch ONTO the advertised tip." >&2
    return 1
  fi
  if [ -z "$p2" ]; then
    echo "push-main: ${t:0:8} has no second parent, so it carries no branch to land." >&2
    return 1
  fi
  if ! git merge-base --is-ancestor "$t" HEAD 2>/dev/null; then
    echo "push-main: ${t:0:8} is not contained in HEAD, so the prepared merge is not what this push would publish." >&2
    return 1
  fi
  printf '%s\n' "$t"
}

# THE CARRY SET: the commits this push would publish that rode in through the LOCAL default branch.
#
#   C = rev-list HEAD --not R   ∩   rev-list refs/heads/<def> --not R
#
# The intersection is what makes it the right set. `T minus local <def>` EXCLUDES exactly the
# commits that came in through a merge of the local default branch, so it can never name one — and
# naming one is the whole job. A clone with no local default branch carries nothing in through it,
# so the set is empty rather than unknown.
derive_carry_set() {  # R · output-file
  local a b
  a=$(mktemp) || return 1
  b=$(mktemp) || return 1
  git rev-list HEAD --not "$1" 2>/dev/null | sort > "$a"
  if git rev-parse --verify --quiet "refs/heads/$def" >/dev/null 2>&1; then
    git rev-list "refs/heads/$def" --not "$1" 2>/dev/null | sort > "$b"
  else
    : > "$b"
  fi
  comm -12 "$a" "$b" > "$2"
  rm -f "$a" "$b"
  return 0
}

# WHICH BUILD A COMMIT BELONGS TO: the first unit id in its subject, else the build folders it
# touches, else `unknown`. An `unknown` counts as FOREIGN — a landing may publish what it can
# account for, and failing open here would give back the hazard this refusal exists to close.
resolve_commit_build() {  # sha · memory-root -> a build slug, or `unknown`
  local subj id rest folders one
  subj=$(git log -1 --format=%s "$1" 2>/dev/null || true)
  id=$(printf '%s' "$subj" | grep -oE '[A-Z][A-Z]+-[A-Za-z]+-[0-9]+' | head -1)
  if [ -n "$id" ]; then
    rest=${id#*-}
    printf '%s\n' "${rest%-*}"
    return 0
  fi
  folders=$(git show --pretty=format: --name-only "$1" 2>/dev/null \
    | awk -v p="$2/builds/" 'index($0,p)==1 { r=substr($0,length(p)+1); i=index(r,"/"); if (i>1) print substr(r,1,i-1) }' \
    | sort -u)
  if [ -n "$folders" ]; then
    # This build's own folder is not foreign, so a set that is entirely this build's reads as this
    # build's; anything else is named by the first member that is not.
    for one in $folders; do
      [ "$one" = "$SLUG" ] || { printf '%s\n' "$one"; return 0; }
    done
    printf '%s\n' "$SLUG"
    return 0
  fi
  printf 'unknown\n'
}

# The carry set, graded. ONE spelling, which both `--carry` and `--land` call: two derivations of
# one predicate can disagree about one landing, and the disagreement would surface at the push.
check_carry_set() {  # R -> 1 when a member belongs to another build
  local f mroot sha bld subj foreign
  mroot=$(. ./.unattended.conf 2>/dev/null; printf '%s' "${MEMORY_ROOT:-}")
  [ -n "$mroot" ] || mroot=memory
  f=$(mktemp) || return 1
  derive_carry_set "$1" "$f" || { rm -f "$f"; return 1; }
  foreign=0
  while read -r sha; do
    [ -n "$sha" ] || continue
    bld=$(resolve_commit_build "$sha" "$mroot")
    subj=$(git log -1 --format=%s "$sha" 2>/dev/null || true)
    if [ "$bld" = "$SLUG" ]; then
      printf 'carry %s · %s · %s\n' "${sha:0:8}" "$bld" "$subj"
    else
      printf 'carry %s · %s · %s  FOREIGN\n' "${sha:0:8}" "$bld" "$subj"
      echo "push-main: this push would publish ${sha:0:8}, which belongs to build '$bld' and not to '$SLUG': $subj" >&2
      foreign=1
    fi
  done < "$f"
  rm -f "$f"
  if [ "$foreign" = 1 ]; then
    echo "push-main: REFUSING — the landing would publish a commit of another build that rode in through the local $def. Land that build's work from its own run, or drop the merge that brought it in." >&2
    return 1
  fi
  return 0
}

# `--prepare`: merge THIS branch onto the advertised tip, in place, and move the branch to it.
#
# THE SUBJECT NAMES THE SLUG AND NO UNIT ID. `build_commit` in the unattended kit joins a commit to
# a unit by the unit id as a whole token in its subject, so a unit id here would make the landing
# merge that unit's build commit and move every verdict derived from it.
cmd_prepare() {  # -> 0 prepared (or already was) · 1 refused · 3 nothing could be observed
  local branch oldb R t
  branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
  if [ -z "$branch" ]; then
    echo "push-main: HEAD is detached, and preparing a landing moves the branch it is made on — check the run's branch out first." >&2
    return 1
  fi
  if [ "$branch" = "$def" ]; then
    echo "push-main: on '$branch', which IS '$def' — --prepare merges a run's own branch onto the advertised tip, and there is no run branch here. The attended landing is push-main.sh with no argument." >&2
    return 1
  fi
  # A dirty tree makes the merge refuse to START — NOT a merge conflict; catch it here with the real
  # remedy instead of the misleading "CONFLICT" the merge-failure path would print.
  if [ -n "$(git status --porcelain -uno 2>/dev/null)" ]; then
    echo "push-main: the working tree has uncommitted changes — commit or stash before landing $def." >&2
    return 1
  fi
  R=$(resolve_tip) || return 3
  read_tip_object "$R" || return 3
  oldb=$(git rev-parse --verify HEAD)
  # IDEMPOTENT. A branch whose tip is already a merge onto this very tip is already prepared, and
  # preparing it again would stack a second merge that `--land` then refuses.
  if [ -n "$(git rev-parse --verify --quiet HEAD^2 2>/dev/null || true)" ] && [ "$(git rev-parse HEAD^1)" = "$R" ]; then
    t=$(git rev-parse HEAD^2)
    echo "push-main: prepared ${oldb:0:8} — first parent ${R:0:8} (the advertised tip) · second parent ${t:0:8}"
    return 0
  fi
  if ! git checkout --detach "$R" >/dev/null 2>&1; then
    echo "push-main: could not check out the advertised tip ${R:0:8} to merge onto; nothing was changed." >&2
    return 1
  fi
  if ! git merge --no-ff "$oldb" -m "merge: $SLUG — land onto $remote/$def at ${R:0:8}" >/dev/null 2>&1; then
    git merge --abort >/dev/null 2>&1 || true
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: merging '$branch' onto $remote/$def at ${R:0:8} CONFLICTS. Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    echo "  Reconcile on the branch first — 'git merge $remote/$def' on '$branch', resolve, commit — then run --prepare again." >&2
    return 1
  fi
  t=$(git rev-parse --verify HEAD)
  if [ "$t" = "$R" ]; then
    # `git merge` says "Already up to date" and creates nothing when the branch is contained in the
    # tip. There is then no landing to prepare, and HEAD must not be left detached at the tip.
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: '$branch' is already contained in $remote/$def at ${R:0:8} — there is nothing to land." >&2
    return 1
  fi
  # COMPARE-AND-SWAP. `git branch -f` would not notice a sibling session moving the branch under
  # this merge; passing the old value refuses instead of silently discarding whatever arrived.
  if ! git update-ref "refs/heads/$branch" "$t" "$oldb" 2>/dev/null; then
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: '$branch' moved while this merge was being made, so the merge was NOT kept. Re-run --prepare." >&2
    return 1
  fi
  if ! git checkout "$branch" >/dev/null 2>&1; then
    echo "push-main: prepared ${t:0:8} and moved '$branch' to it, but could not check '$branch' back out — HEAD is detached at the merge." >&2
    return 1
  fi
  echo "push-main: prepared ${t:0:8} — first parent ${R:0:8} (the advertised tip) · second parent ${oldb:0:8}"
  return 0
}

# `--land`: push the prepared merge, and only it, as the default branch.
cmd_land() {
  local attempt R t pout rc cls
  attempt=1
  while [ "$attempt" -le "$max" ]; do
    R=$(resolve_tip) || exit 3
    read_tip_object "$R" || exit 3
    if ! t=$(check_prepared_merge "$R"); then
      [ "$attempt" -gt 1 ] && echo "push-main: $remote/$def moved again between the re-prepare and this attempt." >&2
      exit 1
    fi
    check_carry_set "$R" || exit 1
    # IN THIS WORKTREE'S OWN GIT DIR, which is the one the pre-push hook reads when the push is
    # issued from here. The lander marker below is the one resolved against the COMMON dir; the two
    # files answer different questions and live in different places on purpose.
    touch "$marker"
    echo "push-main: gating + pushing ${t:0:8} to $def (attempt $attempt/$max)..." >&2
    pout=$(mktemp)
    # HEAD, never refs/heads/<def>: the local default branch is shared by every build on this node,
    # and publishing it is the defect these flags close.
    git push "$remote" "HEAD:refs/heads/$def" 2>&1 | tee "$pout" >&2
    rc=${PIPESTATUS[0]}
    rm -f "$marker"
    if [ "$rc" -eq 0 ]; then
      rm -f "$pout"
      write_lander_marker || exit 1
      echo "push-main: landed $def on $remote." >&2
      exit 0
    fi
    cls=$(parse_push_class "$pout")
    rm -f "$pout"
    case "$cls" in
      race)
        # RE-PREPARE, rather than merging the new tip INTO the branch. That reconcile makes a merge
        # whose first parent is the old branch tip, which this run own precondition then refuses,
        # and it demotes the commits the remote gained onto a second parent of the default branch
        # first-parent line. Re-preparing keeps the invariant on every attempt, and the merge that
        # was already graded stays an ancestor of what is finally pushed.
        echo "push-main: push rejected — $remote/$def advanced during the gate; re-preparing onto the new tip and re-gating..." >&2
        cmd_prepare || exit $?
        attempt=$((attempt + 1)) ;;
      unreachable)
        echo "push-main: could not reach $remote — the gate ran but nothing was pushed; retry when the remote is reachable." >&2
        exit 1 ;;
      red)
        echo "push-main: push failed and $remote/$def is unchanged — the gate is RED (output above). Fix it and re-run." >&2
        exit 1 ;;
    esac
  done
  echo "push-main: $remote/$def is moving faster than the gate ($max attempts exhausted) — land when the fleet is quieter, or coordinate." >&2
  exit 1
}

# `--carry`: the same set `--land` grades, printed and nothing else.
cmd_carry() {
  local R
  R=$(resolve_tip) || exit 3
  # The object is needed to exclude it from the walk. It is USUALLY already here — it is the
  # prepared merge first parent — so this fetches only when it is not, which keeps the one
  # observation this read-only verb is allowed.
  if ! git cat-file -e "$R^{commit}" 2>/dev/null; then
    read_tip_object "$R" || exit 3
  fi
  check_carry_set "$R" || exit 1
  exit 0
}

# `--prepared`: the precondition `--land` applies, asked as a question. One spelling, so the driver
# that gates on it and the lander that enforces it cannot disagree about one landing.
cmd_prepared() {
  local R t
  R=$(resolve_tip) || exit 3
  t=$(check_prepared_merge "$R") || exit 1
  echo "push-main: prepared ${t:0:8} — first parent ${R:0:8} (the advertised tip) · second parent $(git rev-parse "$t^2" | cut -c1-8)"
  exit 0
}

case "$MODE" in
  prepare)  cmd_prepare; exit $? ;;
  land)     cmd_land ;;
  carry)    cmd_carry ;;
  prepared) cmd_prepared ;;
esac

# ---- THE ATTENDED LANDING, from the primary tree with the default branch checked out -------------
branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
if [ "$branch" != "$def" ]; then
  echo "push-main: on '$branch', not '$def' — land $def from the primary tree on $def." >&2
  exit 2
fi

# A dirty tree makes the reconcile merge refuse to START — NOT a merge conflict; catch it here with
# the real remedy instead of the misleading "reconcile CONFLICT" the merge-failure path would print.
if [ -n "$(git status --porcelain -uno 2>/dev/null)" ]; then
  echo "push-main: the working tree has uncommitted changes — commit or stash before landing $def." >&2
  exit 2
fi

attempt=1
while [ "$attempt" -le "$max" ]; do
  git fetch "$remote" "$def" 2>/dev/null || { echo "push-main: 'git fetch $remote $def' failed." >&2; exit 2; }

  if ! git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then
    echo "push-main: $remote/$def advanced — reconciling before the gate (attempt $attempt/$max)..." >&2
    if ! git merge --no-ff "$remote/$def" -m "Merge $remote/$def into $def (push-main reconcile)"; then
      git merge --abort
      echo "push-main: reconcile CONFLICT — resolve manually, commit, then re-run push-main. Aborted (no push)." >&2
      exit 1
    fi
  fi

  touch "$marker"
  echo "push-main: gating + pushing $def (attempt $attempt/$max)..." >&2
  pout=$(mktemp)
  git push "$remote" "$def" 2>&1 | tee "$pout" >&2
  rc=${PIPESTATUS[0]}
  rm -f "$marker"
  if [ "$rc" -eq 0 ]; then
    rm -f "$pout"
    write_lander_marker || exit 1
    echo "push-main: landed $def on $remote." >&2
    exit 0
  fi

  cls=$(parse_push_class "$pout")
  rm -f "$pout"

  case "$cls" in
    race)
      echo "push-main: push rejected — $remote/$def advanced during the gate; re-reconciling and re-gating..." >&2
      attempt=$((attempt + 1)) ;;
    unreachable)
      echo "push-main: could not reach $remote — the gate ran but nothing was pushed; retry when the remote is reachable." >&2
      exit 1 ;;
    red)
      echo "push-main: push failed and $remote/$def is unchanged — the gate is RED (output above). Fix it and re-run push-main." >&2
      exit 1 ;;
  esac
done

echo "push-main: $remote/$def is moving faster than the gate ($max attempts exhausted) — land when the fleet is quieter, or coordinate." >&2
exit 1

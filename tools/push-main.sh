#!/usr/bin/env bash
# push-main.sh — the sanctioned lander for a push to the default branch (TOOL-aLeasedGauntlet-1,
# ports adopter ic ARCH-aLeasedGauntlet-1).
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
#   push-main.sh            --slug <slug>    the attended landing, fenced on that build's lease.
#   push-main.sh --prepare  --slug <slug>   merge THIS branch onto the tip the remote advertises,
#                                            in place, and move the branch to that merge.
#   push-main.sh --land     --slug <slug>    push that prepared merge, and nothing else, as the
#                                            default branch.
#   push-main.sh --carry    --slug <slug>    print what such a push would publish that rode in
#                                            through the LOCAL default branch; exit 1 on a commit
#                                            belonging to another build.
#   push-main.sh --prepared --slug <slug>    exit 0 when HEAD carries a prepared merge; read-only.
#
# KIT VERSIONS ARE MINTED HERE, NOT ON A BRANCH (TOOL-aMendedFleet-65). The minting `--prepare` runs
# the deployer's `govkit.py mint` over the advertised tip..the branch tip and writes each kit version
# the landing owes INTO the prepared merge; the attended landing mints over the fetched tip and
# commits the result as `mint: kit versions onto <remote>/<branch> at <sha8> for <unit>`, the
# newest unit the pushed range names, with a `Pass: none` trailer (TOOL-aRoutedQuill-3). A branch therefore
# owes no bump: the epoch legs grade one only at the push boundary. Where no deployer resolves beside
# this lander, which is every adopter, both paths say so in one line and land as before. What a mint
# does NOT do: re-stamp the kickoff manifest, so a minted carrier on its watch line still reds C5.
#
# GENERATED OUTPUTS ARE REGENERATED HERE TOO (TOOL-aPrimedIndex-4). After the mint, both paths run
# the run-gates kit's `regen.py --write` over the tree about to be pushed: a reconcile merge leaves
# the `merge=ours` indexes stale, and the push bar refuses a stale declared output before its first
# leg. `--prepare` folds what it moved into the prepared merge beside the mint; the attended landing
# commits it as `regen: generated outputs onto <remote>/<branch> at <sha8> for <unit>`, `Pass: none`.
# In `--prepare`, gov first's walk is folded before the regeneration, so a generator reading HEAD sees
# it committed (PLAY-dOrderedCharter-85), the order the attended landing's own commits keep.
# Each lander commit, and each fold, is made only when the stage holds a diff (`write_staged_change`,
# TOOL-dSettledStage-1): a regeneration staging no change makes no commit, and the landing goes on to
# the bar. A stage which fails refuses the landing with no push, and refuses the fold, rather than
# reading as nothing staged (TOOL-dSettledStage-3). A failed write refuses the landing as a refused
# mint does. No regen.py beside this lander
# says so in one line and lands as before. What it does NOT do: prove the result fresh -- the push bar's
# preflight is that check, and a regeneration cannot fix a check red for another reason.
# AFTER A LANDING (TOOL-aFrugalTurnstile-8). Both landing paths read `GATE_POST_MERGE` from the
# gate-env file committed at the landed tip; `local` starts the run-gates kit's post-merge bar on that
# tip, detached, and returns at once, logging to `<common-dir>/gate-post-merge-<sha8>.log` and
# recording the start in `<common-dir>/gate-post-merge.start`; `ci` says remote CI owns it. What
# this does NOT check: whether that bar ever finished, or what it published.
#
# THE FENCED PUSH (TOOL-dPlacedRequest-15). Given `--slug`, under `--land` or the attended landing,
# each attempt first asks the unattended driver beside this lander for the fence, `--lease fence
# build <slug>`, once and before it clears the hook's verdict files. A fence line names the lease
# ref, the tip the driver read and a beat parented on it; the push then carries the branch and the
# beat in ONE `git push --atomic` under `--force-with-lease=<lease ref>:<tip>`, so a holder replaced
# between that read and the push lands nothing, and the landed beat joins this node's change feed.
# `fence — none` (leases off, no lease on the remote) and no driver beside this lander push as before;
# a `lease refused` line, a beat that is the tip or not parented on it, and any read that is no
# well-formed line refuse, exit 1, nothing pushed. A fenced push that fails with the default branch
# unchanged reads the lease once: moved is `fenced`, the lease lost; unmoved is `unfenced`, the remote
# refused the atomic push, which never falls back to an unfenced one. What this does NOT check: the
# remote's support for `--atomic` before the bar runs, so such a remote spends a bar to say `unfenced`.
# A MOVE BY THIS HOLDER'S OWN WRITE IS `refenced` (TOOL-dPlacedRequest-29): a lease that moved is first
# re-read with `--lease fence build <slug> --after <the tip read>`, and a fence line there, this
# session's lease at the same epoch on a tip descending from the one read, retries the push within
# the same attempt bound and without re-preparing, the next attempt's fence read fencing on the new
# tip; only a refusal, a later epoch or another holder, is `fenced`. A re-fence read that does not
# answer, `lease refused — offline`, is `unreachable`, exit 1 with no abort remedy (TOOL-dPlacedRequest-43).
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
# 4 the push LANDED UNGATED: git reported success and the hook left no allow record for the pushed
# commit, so no bar certified what is now on the remote (TOOL-aSignalledHook-1). Retrying cannot
# help, because the push already happened; the landing needs a bar and a decision.
# The no-argument invocation keeps BASE's codes, its own exit 2 included.
set -u

# ---- ARGUMENTS, parsed before the first git call ------------------------------------------------
# BASE accepted no arguments and IGNORED any it was given, so a mistyped `--land` ran the attended
# path and pushed the local default branch — the exact hazard these flags exist to remove. Anything
# that is not one of the four flags or its `--slug` is therefore refused, and that refusal is the
# one observable change to the no-flag contract. It reaches only an invocation that passed something.
MODE=""
SLUG=""
SLUG_SET=""
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
      SLUG=$2; SLUG_SET=1; shift 2 ;;
    --slug=*)
      echo "push-main: spell the slug as two words, '--slug <slug>': $1" >&2
      exit 2 ;;
    *)
      echo "push-main: unrecognised argument '$1' — the flags are --prepare, --land, --carry and --prepared, each with --slug <slug>; no argument at all is the attended landing, and '--slug <slug>' alone is the attended landing fenced on that build's lease." >&2
      exit 2 ;;
  esac
done
# THE ATTENDED LANDING TAKES `--slug` TOO (TOOL-dPlacedRequest-15 S6): with it the landing fences on
# that build's lease, and without it the landing names no build and covers no lease.
if [ -n "$MODE" ] || [ -n "$SLUG_SET" ]; then
  # The SAME grammar the memory tree enforces on a build-folder name, because that is what a slug
  # is; it reaches a commit message and a lease ref, so it is validated before it gets there.
  case "$SLUG" in
    *[!A-Za-z0-9-]* | "" | [!A-Za-z]*)
      echo "push-main: ${MODE:+--$MODE needs }--slug <slug>, a build-folder name: a letter, then letters, digits or dashes: '$SLUG'" >&2
      exit 2 ;;
  esac
fi
# What an OBSERVATION failure exits with. BASE spells 2 for every one of them and that spelling is
# kept for the no-flag path; under a flag they are 3, so a driver can tell "your invocation is
# wrong" from "the remote did not answer" (S7).
obs=2
[ -n "$MODE" ] && obs=3

# This script's own directory, read BEFORE the cd below: a relative $0 resolves from the caller's
# directory and nowhere else. It is the tool root the lexicon kit is looked for in (TOOL-aMendedFleet-3).
self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || self_dir=""
top=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "push-main: not a git repo" >&2; exit "$obs"; }
cd "$top" || exit "$obs"

# THE REMOTE FIRST, then ITS default branch (TOOL-aRepatriatedFork-8 S1). This read `origin/HEAD`
# before it knew which remote it would push to, so on a node whose remote is named anything else
# (adopter ic's node `d` names it after the project) it exited 2 before its first fetch. The ladder
# is the lib dir's canonical since TOOL-dLadderedRemote-1, inlined below and gated byte-identical, so
# every probe that asks which ref "landed" means now answers as this lander does. Several remotes and
# none configured is a refusal: guessing picks a remote nobody chose.
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
branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
if ! resolve_remote_sh; then
  echo "push-main: can't determine which remote to land on — $RR_WHY" >&2
  exit "$obs"
fi
remote=$RR_REMOTE
if [ -z "$remote" ]; then
  echo "push-main: this repository has no remote to land on. Add one: git remote add <name> <url>." >&2
  exit "$obs"
fi

# Resolve the default branch, GOV_DEFAULT_BRANCH first then that remote's HEAD. Fail CLOSED if neither
# is set — silently assuming 'main' would let a push to a real 'develop'/'master' default run un-gated.
def=$RR_BRANCH
if [ -z "$def" ]; then
  echo "push-main: can't determine the default branch ($remote/HEAD unset, GOV_DEFAULT_BRANCH unset) —" >&2
  echo "  set it with 'git remote set-head $remote -a', or export GOV_DEFAULT_BRANCH=<branch>." >&2
  exit "$obs"
fi
max=${GOV_PUSH_MAIN_MAX_RETRIES:-3}
gd=$(git rev-parse --git-dir)
marker="$gd/push-main-active"
# THE HOOK'S VERDICT (S2): `<token><TAB><message>`, written by .githooks/pre-push on every refusal and
# on a red bar, cleared by it on every run and by this script before every push.
refusal="$gd/pre-push-refusal"
# THE BAR THE HOOK VETTED (closing review round 1 H1): `<class><TAB><path><TAB><blob>`, written by the
# hook once it has vetted the bar and before it runs it, cleared by it on every run and by this script
# before every push. The lander marker is written only when it reads `default` or `tracked`.
barfile="$gd/pre-push-bar"
# THE HOOK'S ALLOW RECORD (TOOL-aSignalledHook-1): `<pushed sha><TAB><gate run id>`, written by the
# hook only at its one success exit on a default-branch push, cleared by it on every run and by this
# script before every push. git's exit 0 is not a verdict: on Git for Windows a hook that dies by a
# signal, KILL included, is read as success, and the push lands with no bar. Read by check_push_allow.
allowfile="$gd/pre-push-allow"

# The marker is a SOFT advisory guard: a SIGKILL/OOM/power-loss during the gate can leak it (this
# trap can't catch those). Worst case a later raw push skips reconcile-before-gate and wastes ONE
# gate run; nothing red reaches origin, and the next push-main run's EXIT trap clears a stale marker.
#
# NOT INSTALLED FOR THE TWO READ-ONLY FLAGS. `--carry` and `--prepared` answer a question and write
# nothing, and a trap that removes a file is a write — one a concurrent `--land` in this same
# worktree would feel. Their claim to write nothing is kept true here rather than asserted.
case "$MODE" in
  carry|prepared) ;;
  # A signal RESUMES here, deliberately, unlike the F5 fix in run-selftests. bash defers a trap until
  # the foreground `git push` returns, so an exiting handler would publish the push and then exit
  # before write_lander_marker: a landed push with no marker, which `--landed` refuses. Resuming lets
  # the push and its record finish together (closing review round 2, F1).
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
# Measured on adopter ic (node `a`, 2026-08-27), same objects and same auth throughout: a push
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
# The wiring checker derives `core.sshCommand` from the definition line below by reading this file,
# never sourcing it, so its shape is a contract: ONE line, `GOV_SSH_KEEPALIVE='...'`, single-quoted.
GOV_SSH_KEEPALIVE='ssh -o ServerAliveInterval=30 -o ServerAliveCountMax=120 -o TCPKeepAlive=yes'
: "${GIT_SSH_COMMAND:=$GOV_SSH_KEEPALIVE}"
export GIT_SSH_COMMAND

# ---- SHARED BY BOTH PATHS -----------------------------------------------------------------------
# Lifted out of the attended path by TOOL-dDerivedDocket-2 so the in-place landing writes the same
# record and classifies a failure by the same reading. Two spellings of either would be two answers
# to one question, and the copy is always the one that drifts. What each one READS is
# TOOL-aRepatriatedFork-5 and -8's: the hook's own verdict and the bar it vetted, never the push's words.

# THE ORDER OF EVIDENCE is adopter ic's: the hook's own verdict; else a probe of the push URL, so that
# unreachability is OBSERVED rather than inferred; else fetch and ancestry, a race or a failure the
# hook did not claim. An absent verdict is the cue to probe, never a pass: a hook that predates the
# channel, or a push that died before the hook ran, writes none. The push's own output is never an
# input here (the attended push says why, S2). Every class but `race` has already said why on
# stderr; a caller retries on `race` and `refenced` and exits 1 otherwise.
derive_push_failure() {  # -> refused | unreachable | unchanged | refenced | fenced | unfenced | race on stdout
  local tok msg lt fr ft rc
  tok=""; msg=""
  [ -f "$refusal" ] && IFS=$'\t' read -r tok msg < "$refusal"
  case "$tok" in
    gate-red)
      echo "push-main: the bar RAN and is RED, so nothing was pushed — read $gd/gate-last-summary.txt, fix it, and re-run push-main." >&2
      echo refused; return 0 ;;
    head-moved)
      echo "push-main: the bar ran GREEN but HEAD moved while it ran, so the green does not describe the pushed tree — re-run push-main. ($msg)" >&2
      echo refused; return 0 ;;
    signalled)
      # TOOL-aSignalledHook-1: the hook was sent a signal, so a bar may have run and been stopped
      # part-way. Nothing was pushed; whatever sent the signal decides whether to try again.
      echo "push-main: the pre-push hook was sent a signal and refused, stopping any bar it had started, so nothing was pushed — re-run push-main when whatever stopped it is done. ($msg)" >&2
      echo refused; return 0 ;;
    ?*)
      echo "push-main: pre-push refused the push ($tok) — a precondition; no leg ran: $msg" >&2
      echo refused; return 0 ;;
  esac
  if ! git ls-remote "$(git remote get-url --push "$remote" 2>/dev/null || printf '%s' "$remote")" "refs/heads/$def" >/dev/null 2>&1; then
    echo "push-main: could not reach $remote — a probe of its push URL failed after the push did, and the hook left no verdict; retry when the remote is reachable." >&2
    echo unreachable; return 0
  fi
  git fetch "$remote" "$def" 2>/dev/null || true
  if git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then
    echo "push-main: the push failed, $remote/$def is unchanged and reachable, and the hook left no verdict — the remote refused it or the hook predates its refusal channel; read the push output above." >&2
    # A FENCED PUSH READS ITS LEASE ONCE, here and only here (TOOL-dPlacedRequest-15 S4): moved from
    # the tip the fence read is `refenced` where the driver re-fences on it and `fenced` otherwise
    # (TOOL-dPlacedRequest-29 S2), unmoved is `unfenced`; a read that fails stays `unchanged`.
    [ -n "$FENCE_REF" ] || { echo unchanged; return 0; }
    if ! lt=$(git ls-remote "$remote" "$FENCE_REF" 2>/dev/null); then
      echo "push-main: the lease $FENCE_REF could not be read after the fenced push failed, so whether it was taken is unknown; nothing landed." >&2
      echo unchanged; return 0
    fi
    lt=${lt%%[[:space:]]*}
    if [ "$lt" != "$FENCE_TIP" ]; then
      # The re-fence runs in this function's own subshell, so the FENCE_ names it sets die with it;
      # the next attempt's fence read is the one its push carries (S3).
      fr=$FENCE_REF; ft=$FENCE_TIP
      read_fence_line "$ft" && rc=0 || rc=$?
      if [ "$rc" = 0 ] && [ -n "$FENCE_REF" ]; then
        echo "push-main: the lease moved under this holder's own write; re-fencing on ${FENCE_TIP:0:8} (attempt $((attempt + 1))/$max)" >&2
        echo refenced; return 0
      fi
      # THE RE-FENCE READ DID NOT ANSWER (TOOL-dPlacedRequest-43 S28): whether the lease was taken is
      # unknown, so the holder is told to retry, never to abort. ONLY AN EXPLICIT REFUSAL BY THE LEASE
      # IS `fenced` (TOOL-dPlacedRequest-99 S3): `read_fence_line`'s 1. Its 3 offline, its 4 for every
      # read it could not use, a `lease not written` line and a bad beat among them, and a `none`
      # answer are `unreachable`, a retry with no abort remedy.
      if [ "$rc" != 1 ]; then
        echo "push-main: unreachable — the lease $fr moved from ${ft:0:8} and the re-fence read gave no answer this lander can use (return $rc), so whether it was taken is unknown; nothing landed, retry when the remote answers." >&2
        echo unreachable; return 0
      fi
      echo "push-main: fenced — the lease $fr was taken after the fence read it at ${ft:0:8} and is now ${lt:-deleted}, so the atomic push landed nothing; end the run with --abort $SLUG --code claim-lost." >&2
      echo fenced; return 0
    fi
    echo "push-main: unfenced — the remote refused the atomic push while the lease $FENCE_REF still reads ${FENCE_TIP:0:8}, so nothing landed; a remote without atomic pushes cannot fence a landing, and leases stay off there: RUN_CLAIMS=\"off\" in .unattended.conf lands unfenced again." >&2
    echo unfenced; return 0
  fi
  echo race
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
# check_push_allow — after git reports a push successful, require the hook's allow record to name
# the pushed commit (TOOL-aSignalledHook-1). Without it the push is on the remote and no bar
# certified it: the hook was killed, and on Git for Windows a hook that dies by a signal reads as
# success. The trap in the hook turns every catchable signal into a refusal, so what reaches this
# line is a KILL or a TerminateProcess. It cannot be undone here, only refused the name `landed`:
# no lander marker, a line saying what happened, and exit 4 from the caller. The lander's own EXIT
# trap still clears its marker file.
# THE PUSHED SHA AND THE REMOTE'S TIP ARE CAPTURED BEFORE THE PUSH and passed in, never re-read after
# it: a commit landing in this tree during the upload would otherwise read as a push no hook allowed.
# NOTHING PUSHED IS NOT UNGATED. When the remote already held the commit, git runs the hook with no ref
# lines, the hook exits as `skip-nondefault` and writes no record, and git still exits 0; that
# re-run of a landing that already happened is reported as such (closing review round 1).
check_push_allow() {  # pushed sha · the remote's tip before the push -> 0 when the hook allowed it; else the UNGATED report and 1
  local pushed=$1 was=$2 sha="" run=""
  if [ "$pushed" = "$was" ]; then
    echo "push-main: $remote/$def already held ${pushed:0:8} before this push, so nothing was pushed and no hook verdict is owed." >&2
    return 0
  fi
  [ -f "$allowfile" ] && IFS=$'\t' read -r sha run < "$allowfile"
  [ -n "$sha" ] && [ "$sha" = "$pushed" ] && return 0
  echo "push-main: landed UNGATED — git reports ${pushed:0:8} pushed to $remote/$def, but the pre-push hook left no allow record for it${sha:+ (its record names ${sha:0:8})} in $allowfile. The hook was killed before it decided: on Git for Windows a hook that dies by a signal reads as success. The commit is on $remote and NO bar certified it; NOT writing the lander marker. Run the bar on $remote/$def and decide whether to keep it." >&2
  return 1
}

write_lander_marker() {  # -> 1 when the push landed but the record could not be written
  local lm _gcd bar barpath barblob
  [ -f .unattended.conf ] || return 0
  lm=$(. ./.unattended.conf 2>/dev/null; printf '%s' "${LANDER_MARKER:-}")
  # A STUB-GATED PUSH IS NOT A LANDING (TOOL-aRepatriatedFork-5). GOV_GATE_CMD_TEST is the hook's
  # one declared escape: it lets an untracked stub stand in for the bar so the hook can be tested
  # at all. The marker is what `unattended.sh --landed` accepts as a landing through this lander,
  # so writing it here would let a push nobody's bar gated read as a gated landing.
  #
  # READ FROM THE HOOK'S VERDICT, NEVER FROM THIS ENVIRONMENT (closing review round 1 H1). This
  # tested GOV_GATE_CMD_TEST in its own environment, and the hook also takes it from the
  # gate-env.sh it sources, so a stub-gated push got the marker. No verdict at all, from a hook
  # that predates the file or never reached the bar, is not a gated landing either.
  bar=""; barpath=""; barblob=""
  [ -f "$barfile" ] && IFS=$'\t' read -r bar barpath barblob < "$barfile"
  case "$bar" in
    default|tracked) ;;
    stub) [ -n "$lm" ] && echo "push-main: pushed $def, and the hook vetted the bar as a declared STUB (GOV_GATE_CMD_TEST); NOT writing the lander marker ($lm), because a stub-gated push is not a landing." >&2
          lm="" ;;
    *)    [ -n "$lm" ] && echo "push-main: pushed $def, but the hook recorded no vetted bar in $barfile, so nothing says a bar gated this push; NOT writing the lander marker ($lm)." >&2
          lm="" ;;
  esac
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
  # The pushed commit FIRST, since `--landed` reads the line's first sha; then the bar the hook
  # vetted, by class, path and blob (M1), so a reader can tell the whole bar from a cheap one.
  if ! printf 'landed %s at %s by push-main bar %s %s %s\n' "$def" "$(git rev-parse HEAD)" "$bar" "$barpath" "$barblob" > "$_gcd/$lm"; then
    echo "push-main: pushed $def, but could not write the lander marker at $_gcd/$lm. The push SUCCEEDED and is not recorded." >&2
    return 1
  fi
  return 0
}

# THE POST-MERGE BAR, where the landed tip declares one (TOOL-aFrugalTurnstile-8, design D10). The
# declaration is `GATE_POST_MERGE` in the gate-env file AS COMMITTED AT THE LANDED TIP, read by
# `git show` and parsed by `read_policy_key`, a byte-identical copy of the pre-push hook's (the hook
# ships verbatim and sources no kit; push-main.test.sh holds the pair). Never the working tree, never
# R, never this environment: the bar that runs is the one the landed commit asks for.
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
# `local` starts the run-gates kit's post-merge script on the landed tip, DETACHED: all three streams
# redirected and under nohup, because a background job that keeps the lander's stdout makes every
# `$(...)` capture of push-main wait for the whole bar. The start goes to stderr and to a key-per-line
# record, `<common-dir>/gate-post-merge.start`; the log is per sha so a second landing cannot truncate
# a bar still writing. `ci` and a value outside the set print one line and start nothing; undeclared
# prints nothing. Always 0: the landing already happened, so a failure to start is a line, not a code.
# WHAT THIS DOES NOT CHECK: whether the bar it started ever finished or published a verdict.
run_post_merge() {  # -> 0 always; one stderr line whenever the landed tip declares anything
  local tip blob pm py dir gcd log pid winpid got rc
  tip=$(git rev-parse HEAD 2>/dev/null) || return 0
  blob=$(git show "$tip:.githooks/gate-env.sh" 2>/dev/null) || return 0
  pm=$(read_policy_key "$blob" GATE_POST_MERGE)
  case "$pm" in
    '')    return 0 ;;
    ci)    echo "push-main: post-merge bar — GATE_POST_MERGE=ci at ${tip:0:8}, so remote CI runs it; nothing started here." >&2
           return 0 ;;
    local) ;;
    *)     echo "push-main: post-merge bar NOT started — GATE_POST_MERGE at ${tip:0:8} is '$pm', outside 'local ci'." >&2
           return 0 ;;
  esac
  got=$(resolve_lander_kit run-gates post-merge.sh); rc=$?
  if [ "$rc" = 1 ]; then
    echo "push-main: post-merge bar NOT started — no usable python launcher, so the run-gates kit could not be located. The landing stands." >&2
    return 0
  fi
  if [ "$rc" != 0 ]; then
    echo "push-main: post-merge bar NOT started — no run-gates kit holding post-merge.sh beside this lander. The landing stands." >&2
    return 0
  fi
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  gcd=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd) || gcd=""
  if [ -z "$gcd" ]; then
    echo "push-main: post-merge bar NOT started — the git common dir could not be resolved. The landing stands." >&2
    return 0
  fi
  log="$gcd/gate-post-merge-${tip:0:8}.log"
  nohup "${BASH:-bash}" "$top/$dir/post-merge.sh" "$tip" --remote "$remote" </dev/null >"$log" 2>&1 &
  pid=$!
  winpid=$(cat "/proc/$pid/winpid" 2>/dev/null || true)
  if printf 'sha\t%s\npid\t%s\nwinpid\t%s\nlog\t%s\nstarted\t%s\nby\tpush-main\n' \
      "$tip" "$pid" "$winpid" "$log" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$gcd/gate-post-merge.start" 2>/dev/null; then
    echo "push-main: post-merge bar started on ${tip:0:8} — pid $pid, log $log" >&2
  else
    echo "push-main: post-merge bar started on ${tip:0:8} — pid $pid, log $log; the start record could not be written." >&2
  fi
  return 0
}

# ---- THE FENCE, read once per attempt and pushed atomically — TOOL-dPlacedRequest-15 -------------
# The fence read's result: the lease ref, the tip the driver read and the beat on it, or all three
# empty for no fence. Set by `read_fence_line` and read by the push and by `derive_push_failure`.
FENCE_REF=""; FENCE_TIP=""; FENCE_BEAT=""

# `check_fence_beat <tip> <beat>` holds the beat to the one shape the remote checks: a commit other
# than the tip whose first parent is the tip. A beat equal to the tip re-pushes an unchanged lease
# ref, for which git sends no command, so nothing would compare it; it is refused before any push.
check_fence_beat() {  # tip · beat -> 0 when the beat is parented on the tip and is not it; else its line and 1
  local p
  if [ "$1" = "$2" ]; then
    echo "push-main: the fence beat ${2:0:8} IS the lease tip, an unchanged lease ref the remote never checks, so the landing would carry no fence; nothing was pushed." >&2
    return 1
  fi
  p=$(git rev-parse --verify --quiet "$2^" 2>/dev/null) || p=""
  [ "$p" = "$1" ] && return 0
  echo "push-main: the fence beat ${2:0:8} has ${p:-no parent here} as its first parent, not the lease tip ${1:0:8}, so it does not stand on the tip the fence read; nothing was pushed." >&2
  return 1
}

# `read_fence_line` asks the unattended driver beside this lander, `--lease fence build <slug>`, and
# parses its result in ONE place, failing closed. No `--slug`, or no driver beside this lander, is no
# fence, and so is exit 0 with one `fence — none · …` line. Exit 0 with one `fence — <lease ref> <tip>
# <beat>` line is a fence, each field checked and the beat held by `check_fence_beat`. Exit 1 with
# one `lease refused — …` line refuses. Anything else, an empty, multi-line or odd-exit read included,
# refuses as unparsed: only a missing driver means no fence. A driver beside this lander that no
# python finds refuses too, as `run_gov_first` does. Handed the tip a failed push fenced on, it asks
# `--after <tip>`, the re-fence `derive_push_failure` reads (TOOL-dPlacedRequest-29 S2).
# ITS FOUR RETURNS (TOOL-dPlacedRequest-99 S3), so a reader can tell a lease that refused from a read
# that never answered: 0 a fence, or none; 1 an explicit `lease refused — <cause>` line other than
# `offline`, the one answer that says the lease is another's; 3 `lease refused — offline`; 4 every
# non-answer, an unparsed, multi-line or empty read, an exit-2 `lease not written — …` line, the
# no-python branch and a `check_fence_beat` failure on a fence line the driver did answer. Both
# first-fence callers test `if ! read_fence_line`, so 3 and 4 refuse the landing there as 1 does.
read_fence_line() {  # [tip a failed push fenced on] -> 0 with FENCE_REF, FENCE_TIP and FENCE_BEAT set, or all empty for none; 1 refused by the lease, 3 the read did not answer (`lease refused — offline`), 4 no answer it can use; its line printed
  local got rc dir out rest fr ft fb kit=unattended anchor=unattended.sh
  FENCE_REF=""; FENCE_TIP=""; FENCE_BEAT=""
  [ -n "$SLUG" ] || return 0
  got=$(resolve_lander_kit "$kit" "$anchor"); rc=$?
  if [ "$rc" = 1 ]; then
    if [ -f "$self_dir/$kit/$anchor" ] || [ -f "$self_dir/../$kit/$anchor" ]; then
      echo "push-main: the fence read did not run — an unattended driver is beside this lander and no usable python launcher finds it, so the landing of '$SLUG' cannot be fenced; nothing was pushed." >&2
      return 4
    fi
    rc=2
  fi
  if [ "$rc" != 0 ]; then
    echo "push-main: fence — none · no unattended driver beside this lander, so no lease is fenced" >&2
    return 0
  fi
  dir=${got#*$'\t'}
  out=$("${BASH:-bash}" "$top/$dir/$anchor" --lease fence build "$SLUG" ${1:+--after "$1"}); rc=$?
  out=${out//$'\r'/}
  case "$rc:$out" in
    *$'\n'*) ;;
    "0:fence — none · "?*)
      echo "push-main: $out" >&2
      return 0 ;;
    "0:fence — "*)
      rest=${out#"fence — "}; fr=${rest%% *}; rest=${rest#* }; ft=${rest%% *}; fb=${rest#* }
      if [ "$fr" = "refs/gov/leases/$SLUG/build" ] && [[ $ft =~ ^[0-9a-f]{40}([0-9a-f]{24})?$ ]] && [[ $fb =~ ^[0-9a-f]{40}([0-9a-f]{24})?$ ]]; then
        echo "push-main: $out" >&2
        check_fence_beat "$ft" "$fb" || return 4
        FENCE_REF=$fr; FENCE_TIP=$ft; FENCE_BEAT=$fb
        return 0
      fi ;;
    "1:lease refused — offline · "*)
      # AN UNANSWERED READ IS NO REFUSAL BY THE LEASE (TOOL-dPlacedRequest-43 S28): returned apart, 3,
      # so the re-fence reads it `unreachable` and never tells a holder to abort.
      echo "push-main: the fence read of '$SLUG' did not answer, so nothing was pushed — $out" >&2
      return 3 ;;
    "1:lease refused — "?*)
      echo "push-main: the fence refused the landing of '$SLUG', so nothing was pushed — $out" >&2
      return 1 ;;
    "2:lease not written — "?*)
      echo "push-main: the fence read of '$SLUG' wrote no answer, so nothing was pushed — $out" >&2
      return 4 ;;
  esac
  rest=${out%%$'\n'*}
  echo "push-main: fence read unparsed — exit $rc · ${rest:-(empty)}" >&2
  return 4
}

# `write_effect_push <refspec>` is the landing's one push. With no fence it is the single-ref push
# both paths always made; with one, the refspec and the beat go in ONE `--atomic` push whose lease is
# the fence's tip, and once it lands the beat joins this node's change feed (TOOL-dPlacedRequest-13).
# Its output is SHOWN and never read (S2); a failure is classified by `derive_push_failure`.
write_effect_push() {  # refspec -> git's exit
  local rc
  if [ -z "$FENCE_REF" ]; then
    git push "$remote" "$1" >&2
    return
  fi
  git push --atomic "--force-with-lease=$FENCE_REF:$FENCE_TIP" "$remote" "$1" "$FENCE_BEAT:$FENCE_REF" >&2 && rc=0 || rc=$?
  [ "$rc" != 0 ] || write_feed_success "$FENCE_REF" "$FENCE_BEAT"   # the cache names the landed beat (TOOL-dPlacedRequest-34 S6)
  return "$rc"
}

# The change feed's appender and the health log's, inlined byte-identical from the lib dir's
# canonical copies (TOOL-dPlacedRequest-13, -36), as every writer of a governance ref carries them.
# >>> gov_feed_sh — canonical copy: gov-feed.sh in gov's lib dir (byte-identical; gated)
# THE NODE LOCKS (TOOL-dPlacedRequest-24): a node-local file two sessions of this node write, the
# feed's log and the offline queue's, is read and written only under a lock directory beside it in
# the common dir, taken through `write_dir_lock_wait` with the stem `node`, so a stale break appends
# `node-lock-broken` or `node-guard-cleared`. NODE_LOCK_BOUND is the seconds a node lock may hold,
# a pinned literal over every section it covers (TOOL-dPlacedRequest-49 S33): the feed append,
# `add_feed_event`; the queue's append, `add_gov_queue`, and its flush's two file passes,
# `write_gov_queue`, which pushes with no lock held; the offline write's hold through
# `write_gov_queue_hold`, from its read of the queue through its append, which builds the commit but
# never pushes; and `write_request_record`'s compare, copy and `.typed` append. The longest is the
# offline write's hold, measured once on node d on 2026-11-20 over the lease fixture:
# 1.412 s, PINNED, under this bound.
NODE_LOCK_BOUND=10
# THE DIRECTORY LOCK (TOOL-aGraftedHelix-37), a factory (TOOL-aPiecewiseGrade-6), moved into this
# block (TOOL-dPlacedRequest-24) so every carrier holds the one definition. `write_dir_lock` takes the
# lock with `mkdir`, sets `_fl_mine=1` in the caller's shell, then writes the caller's token into
# `owner` and only then its deadline into `until` (TOOL-dPlacedRequest-49 S5), so a taken lock always
# carries the token `remove_dir_lock` matches, even where an abort stops the take. A lock it cannot
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
  _fl_mine=1
  printf '%s\n' "$2" >"$lk/owner" 2>/dev/null || :
  printf '%s\n' "$(( $EPOCHSECONDS + $3 ))" >"$lk/until" 2>/dev/null || :
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
# `EXIT` trap is armed BEFORE the take (TOOL-dPlacedRequest-49 S6) and acts only once `write_dir_lock`
# has set `_fl_mine`, which the subshell empties first: it then releases the lock directory where its
# `owner` reads this call's token, and clears one with no `owner` only while no `gov-feed.lock.break`
# guard exists (TOOL-dPlacedRequest-52 S20); every other lock it leaves. A breaker in `write_dir_lock`
# holds that guard from before its `rm -rf` until after it writes `owner`, so a breaker's window is
# never cleared. So an abort anywhere after the `mkdir`, an unbound
# name under a carrier's `set -u`, a function no carrier defines or a failed write, ends the subshell
# alone: the append prints `feed: NOTE - <ref>: the append exited <rc>` and returns 0, and no lock is
# left for the next writer to wait out; a busy take, exit 3, finds the flag empty and leaves the
# holder's lock. The subshell sets no global a caller reads. WHAT THIS DOES NOT CHECK: the one window
# left is a third writer's own `mkdir`-to-`owner` window, after a peer broke this writer's lock and
# released it, which a holder that outlives NODE_LOCK_BOUND and a full peer cycle can find at its exit
# and clear; an abort after the line is written reads as a NOTE all the same.
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
# A staging name beside <dest> that nobody can know before it is written: <dest>.<SRANDOM twice>.tmp, or
# mktemp -u's where bash has no SRANDOM; 1 when neither names one. The run-gates runner carries the same line.
derive_temp_path() { if [ -n "${SRANDOM:-}" ]; then printf -v "$1" '%s.%s%s.tmp' "$2" "$SRANDOM" "$SRANDOM"; else printf -v "$1" '%s' "$(mktemp -u "$2.XXXXXXXX" 2>/dev/null)"; [ -n "${!1}" ]; fi; }
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
  ( _fl_mine=
    trap '[ -z "$_fl_mine" ] || { [ -s "$d/gov-feed.lock/owner" ] || [ -e "$d/gov-feed.lock.break" ] || rm -rf "$d/gov-feed.lock"; remove_dir_lock "$d/gov-feed.lock" "$tok"; }' EXIT
    write_dir_lock_wait "$d/gov-feed.lock" "$tok" "$NODE_LOCK_BOUND" node 5 || exit 3
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
    elif st=""; ! { derive_temp_path st "$d/gov-feed.seq" && printf '%s\n' "$n" >"$st" && mv -f "$st" "$d/gov-feed.seq"; } 2>/dev/null; then
      [ -z "$st" ] || rm -f "$st" 2>/dev/null
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
  local pre="${1%/}/" d now n=0 l lt="" st=""
  [ -n "${GOVFEED_DIR:-}" ] || GOVFEED_DIR=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || GOVFEED_DIR=""
  d=${GOVFEED_DIR%$'\r'}
  [ -n "$d" ] || { printf 'feed: no git common dir resolves here, so no feed was rebuilt\n'; return 2; }
  if [ -e "$d/gov-feed.log" ]; then printf 'feed: a feed is present, so nothing was rebuilt over it: %s\n' "$d/gov-feed.log"; return 2; fi
  TZ=UTC printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1
  derive_temp_path lt "$d/gov-feed.log" && derive_temp_path st "$d/gov-feed.seq" \
    || { printf 'feed: no staging name resolves beside %s, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
  { while IFS= read -r l; do n=$((n + 1)); printf '%s\t%s\t%s\n' "$n" "$l" "$now"; done < <(derive_feed_events "$pre"); } >"$lt" \
    && printf '%s\n' "$n" >"$st" && mv -f "$st" "$d/gov-feed.seq" && mv -f "$lt" "$d/gov-feed.log" \
    || { rm -f "$lt" "$st"; printf 'feed: %s could not be written, so no feed was rebuilt\n' "$d/gov-feed.log"; return 2; }
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

# WHICH BUILD A COMMIT BELONGS TO. A commit is this build's only when every signal it carries says
# so; `unknown` counts as FOREIGN, because a landing may publish what it can account for and failing
# open here would give back the hazard this refusal exists to close.
#
# THE BUILD FOLDERS IT TOUCHES DECIDE FIRST. Any `<memory-root>/builds/<slug>/` other than this
# build's makes it that build's.
#
# A SUBJECT CLAIMS OWNERSHIP ONLY AT ITS HEAD: a `<verb>(<slug>):` prefix, a unit id followed by a
# colon, or `merge: <unit id>`. An id anywhere else is a CITATION and never ownership. This used to
# take the first id ANYWHERE in the subject, before the folders, so another build's records commit
# leading with this build's id — `records(<other>): <this build's id> closes …`, an ordinary shape
# once one build disposes another's ask — read as this build's and was published unflagged (closing
# diff review round 1, F7). A claim naming another build is FOREIGN even when every folder it
# touches is this build's; a claim naming no build (`fix(unattended):`) is FOREIGN by the same
# comparison.
resolve_commit_build() {  # sha · memory-root -> a build slug, or `unknown`
  local subj claim folders one
  subj=$(git log -1 --format=%s "$1" 2>/dev/null || true)
  claim=$(printf '%s\n' "$subj" | sed -nE \
    -e 's/^[a-z][a-z-]*\(([A-Za-z0-9_.-]+)\):.*/\1/p' -e 't' \
    -e 's/^[A-Z][A-Z]+-([A-Za-z]+)-[0-9]+:.*/\1/p' -e 't' \
    -e 's/^merge: [A-Z][A-Z]+-([A-Za-z]+)-[0-9]+( .*)?$/\1/p' | head -n 1)
  folders=$(git show --pretty=format: --name-only "$1" 2>/dev/null \
    | awk -v p="$2/builds/" 'index($0,p)==1 { r=substr($0,length(p)+1); i=index(r,"/"); if (i>1) print substr(r,1,i-1) }' \
    | sort -u)
  if [ -n "$folders" ]; then
    for one in $folders; do
      [ "$one" = "$SLUG" ] || { printf '%s\n' "$one"; return 0; }
    done
    # Every folder is this build's, and a head claim naming another build still contradicts them.
    if [ -n "$claim" ] && [ "$claim" != "$SLUG" ]; then printf '%s\n' "$claim"; return 0; fi
    printf '%s\n' "$SLUG"
    return 0
  fi
  if [ -n "$claim" ]; then printf '%s\n' "$claim"; return 0; fi
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

# ---- MERGE LOSS, before --prepare moves the branch — TOOL-aMendedFleet-3 ------------------------
# The two resolvers below are the pre-push hook's, inlined byte-identically from the canonical copies
# their marker lines name and gated by the resolve-python self-test's parity table. TOOL-aMendedFleet-65
# reuses them for its version minter rather than adding a second resolver to this script.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  # THE BAR'S OWN RESOLUTION, taken with no spawn (TOOL-aMeasuredDrag-11). The run-gates runner
  # exports GATE_RESOLVED_PY as four lines: the version, the launcher it resolved, and GOV_PYTHON and
  # PATH as it saw them. With no caller override the loop below is decided by GOV_PYTHON, PATH and the
  # floor, so a memo matching both byte for byte, at or above THIS floor, is what the loop would print.
  # Anything else, malformed or partial included, is ignored and the loop runs. Only an absolute
  # launcher is admitted (TOOL-aMeasuredDrag-12): a relative one names another file once a leg
  # changes directory, and a bare name does too under a PATH holding `.`.
  _rp_re=$'^([0-9]+)\\.([0-9]+)\n(/[^\n]*|[A-Za-z]:/[^\n]*|[A-Za-z]:\\\\[^\n]*)\n([^\n]*)\n(.*)$'
  if [ -z "${1:-}" ] && [[ ${GATE_RESOLVED_PY:-} =~ $_rp_re ]] \
    && [ "${BASH_REMATCH[4]}" = "${GOV_PYTHON:-}" ] && [ "${BASH_REMATCH[5]}" = "$PATH" ] \
    && [ $(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} )) -ge "$_rp_fv" ]; then
    printf '%s\n' "${BASH_REMATCH[3]}"
    return 0
  fi
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
# `resolve_lander_kit <kit home> <file>` is every lander stage's ONE kit resolution
# (TOOL-dSafePassage-26 S52): the python the resolver runs, then the kit directory `resolve_kit_dir`
# finds from THIS script's own directory, and the FILE test under the toplevel (TOOL-aMendedFleet-111
# S2: the resolver answers relative to this script's tree, and `$top` is the cwd's, so a tree without
# the kit made python exit 2 and read as a DEAD PROBE). It echoes `<python><TAB><kit dir>` and
# returns 0; else it echoes the skip reason and returns 1 for no python, 2 for no kit. Each stage
# prints its own line from that code, and `run_gov_first` turns a missing python into a refusal.
resolve_lander_kit() {  # kit home · file -> "<python>\t<kit dir>" · 0; else the reason · 1 no python, 2 no kit
  local py dir
  if ! py=$(resolve_python 2>/dev/null); then
    echo "no usable python launcher"
    return 1
  fi
  if ! dir=$(resolve_kit_dir "$py" "$1" "$2" "$self_dir" 2>/dev/null) || [ ! -f "$top/$dir/$2" ]; then
    echo "no $1 kit holding $2 beside this lander"
    return 2
  fi
  printf '%s\t%s\n' "$py" "$dir"
}
# `check_merge_losses R T` runs the lexicon kit's `--merge-losses` over `R..T`, the merges a prepared
# landing would publish, so a merge that LOST a definition a parent carried is refused here, before
# the branch moves, rather than after the bar at the push. Exit 1 of the mode returns 1 with its
# lines; a DEAD PROBE, no python and no kit each print one line and return 0, because the pre-push
# hook grades the same range again at the push and binds there. The kit is found from THIS script's
# own directory, the tool root it was installed into, never from a typed prefix. The kit is a declared
# slot (PLAY-dOrderedCharter-17): no kit prints `slot point.flow.leg-pack · not-installed: <fallback>`,
# and a run prints `searched-empty` (no loss) or `filled` (a loss) on stderr. `run_minter` and
# `run_gov_first` print the same grammar at `point.flow.version`.
check_merge_losses() {  # R · T -> 1 when a merge in R..T loses a definition; 0 otherwise, any skip printed
  local py dir out rc got
  got=$(resolve_lander_kit lexicon lexicon.py); rc=$?
  if [ "$rc" = 1 ]; then
    echo "push-main: the merge-loss check did NOT run — no usable python launcher; the pre-push hook grades the landing again." >&2
    return 0
  fi
  if [ "$rc" != 0 ]; then
    echo "push-main: slot point.flow.leg-pack · not-installed: the pre-push hook grades the landing again — no lexicon kit beside this lander." >&2
    return 0
  fi
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  out=$("$py" "$top/$dir/lexicon.py" --merge-losses "$1..$2" 2>&1); rc=$?
  case "$rc" in
    0) echo "push-main: slot point.flow.leg-pack · searched-empty" >&2; return 0 ;;
    1) echo "push-main: slot point.flow.leg-pack · filled" >&2; printf '%s\n' "$out" | sed 's/^/  /' >&2; return 1 ;;
  esac
  echo "push-main: DEAD PROBE — the merge-loss check could not answer, so this prepare continues; the pre-push hook binds the landing:" >&2
  printf '%s\n' "$out" | sed 's/^/  /' >&2
  return 0
}

# ---- GENERATED OUTPUTS, regenerated at the landing — TOOL-aPrimedIndex-4 -------------------------
# `run_regen` runs the run-gates kit's `regen.py --write` over the WORKING TREE; the caller commits
# what it wrote. Found the way the minter finds the deployer, from this script's own directory, and
# the file test under the toplevel for the merge-loss check's reason: the kit can resolve beside
# this lander while the tree being landed lacks the file. No python or no regen.py prints one line
# and returns 0, and the push bar's preflight then grades the outputs. A stage that moved nothing is
# not echoed. On a failed write or a refused declaration the verb's output goes to stderr and this
# returns 1.
run_regen() {  # -> 0 regenerated or announced-skipped · 1 a write failed or the declaration was refused
  local py dir out rc got
  got=$(resolve_lander_kit run-gates regen.py); rc=$?
  if [ "$rc" = 1 ]; then
    echo "push-main: generated outputs were NOT regenerated — no usable python launcher; the push bar's preflight grades them."
    return 0
  fi
  if [ "$rc" != 0 ]; then
    echo "push-main: generated outputs were NOT regenerated — no regen.py beside this lander; the push bar's preflight grades them."
    return 0
  fi
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  out=$("$py" "$top/$dir/regen.py" --write 2>&1); rc=$?
  if [ "$rc" -eq 0 ]; then
    printf '%s\n' "$out" | grep -v -e ' · moved: none$' || true
    return 0
  fi
  echo "push-main: the generated outputs could NOT be regenerated (regen.py exit $rc):" >&2
  printf '%s\n' "$out" | sed 's/^/  /' >&2
  return 1
}

# `remove_new_untracked <snapshot>` cleans every untracked file the snapshot does not hold, the snapshot
# being what the snapshot writer below wrote before the stage. The reset after a failed stage
# restores tracked files only, and a stage also CREATES files (a new ledger shard, a render's
# temporary, gov first's receipt, before-images and orders), which then dirtied the tree the next
# landing requires clean (TOOL-aPrimedIndex-8). NUL-safe end to end; an unreadable state cleans nothing.
#
# The snapshot writer, given <file>, writes into it the sorted NUL-separated list of untracked,
# not-ignored paths `git ls-files` prints, <file> being the caller's `mktemp`. It returns
# non-zero when <file> is empty (the `mktemp` failed), or `git ls-files` or the sort fails, read
# through PIPESTATUS, and each caller refuses on that before its stage runs, so a snapshot that
# cannot be written never falls through to a walk or a regeneration (TOOL-dSafePassage-35 S10, S11).
# `remove_new_untracked` writes its current set with it too. Its three stage callers, each on a tree
# it required clean, so every path cleaned is one the stage made:
# `cmd_prepare`'s one snapshot, before gov first and kept through the regeneration, its tree the
# minted merge (TOOL-dSafePassage-27); the attended path's gov-first snapshot, its tree the mint
# commit (TOOL-dSafePassage-25 S2); and the attended regeneration's, its tree gov first's commit.
write_untracked_snapshot() {  # snapshot file -> nothing on stdout
  local st
  [ -n "${1:-}" ] && [ -f "$1" ] || return 1
  git ls-files --others --exclude-standard -z 2>/dev/null | LC_ALL=C sort -z > "$1"
  st="${PIPESTATUS[0]}${PIPESTATUS[1]}"
  [ "$st" = "00" ]
}

remove_new_untracked() {  # snapshot file -> nothing on stdout
  local now
  [ -f "${1:-}" ] || return 0
  now=$(mktemp) || return 0
  # the current set from the snapshot's own writer, so the two sets `comm` compares are one shape
  # (TOOL-dSafePassage-42 S18)
  if write_untracked_snapshot "$now"; then
    LC_ALL=C comm -z -13 "$1" "$now" | xargs -0 -r git clean -f -q -- >/dev/null 2>&1 || true
  fi
  rm -f "$now"
}

# `write_staged_change` stages the working tree and answers whether the stage now differs from HEAD,
# the one place the lander stages before its four commits: the mint, gov first and regeneration
# commits of the attended landing, and `write_merge_fold` (TOOL-dSettledStage-1). A dirty status does
# not imply a staged diff. Landing 12764ec21 aborted before its bar because the regeneration rewrote
# a tracked file checked out with CRLF bytes with its committed LF bytes under `core.autocrlf=true`:
# status reported it modified on its cached size alone, staging normalized it back to the committed
# blob, nothing was staged, and the commit failed. A stage equal to HEAD answers 1, as a clean tree
# does, and its caller commits nothing, silently. An error from `git diff` answers 0, so the caller's
# commit runs and refuses with its own line rather than landing a tree the lander never committed.
# A failed status or stage answers 2, and every caller refuses on it rather than reading it as
# nothing staged (the closing review's item 1, TOOL-dSettledStage-3).
write_staged_change() {  # -> 0 the index differs from HEAD · 1 the tree was clean, or staging left nothing · 2 staging failed
  local dirt
  dirt=$(git status --porcelain --ignore-submodules=untracked 2>/dev/null) || return 2
  [ -n "$dirt" ] || return 1
  git add -A || return 2
  git diff --cached --quiet && return 1
  return 0
}

# ---- KIT VERSIONS, minted at the landing — TOOL-aMendedFleet-65 ----------------------------------
# `run_minter <base> [<head>]` runs the deployer's `mint` verb, which writes the next version of every
# kit whose shipped bytes moved in <base>..<head> with no bump dating the move, into the WORKING TREE;
# the caller commits what it wrote. Found the way the merge-loss check finds its kit, from this
# script's own directory. No python or no deployer, which is every adopter because govkit stays in
# gov, prints one line and returns 0: the landing proceeds exactly as it did before this existed.
# The minter's lines go to stdout on success; on a refusal to stderr, and this returns 1.
run_minter() {  # base · [head] -> 0 minted, clean or announced-skipped · 1 the minter refused
  local py dir out rc got
  got=$(resolve_lander_kit govkit govkit.py); rc=$?
  if [ "$rc" = 1 ]; then
    echo "push-main: kit versions were NOT minted — no usable python launcher; the push bar's epoch legs grade the landing."
    return 0
  fi
  # A missing deployer is a skip, never a refusal.
  if [ "$rc" != 0 ]; then
    echo "push-main: slot point.flow.version · not-installed: the push bar's epoch legs grade the landing — no govkit deployer beside this lander, so kit versions were NOT minted."
    return 0
  fi
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  out=$("$py" "$top/$dir/govkit.py" mint --base "$1" ${2:+--head "$2"} 2>&1); rc=$?
  if [ "$rc" -eq 0 ]; then
    printf '%s\n' "$out" | grep -v -e ' · clean$' -e ' · skip · ' || true
    echo "push-main: slot point.flow.version · filled" >&2
    return 0
  fi
  echo "push-main: the version minter REFUSED (exit $rc):" >&2
  printf '%s\n' "$out" | sed 's/^/  /' >&2
  return 1
}

# ---- GOV FIRST, at the landing — TOOL-dSafePassage-8 --------------------------------------------
# `run_gov_first` runs the deployer's `update --target <this tree> --write` in its SOURCE mode: every
# upgrade step this landing declares walks on gov's own tree before any adopter meets it, recorded in
# gov's source-mode receipt in the WORKING TREE, and the deployer's landing check re-runs each applied
# step's witness; the caller commits the receipt. Found the way the minter finds the deployer. No
# deployer beside the lander, which is every adopter, prints one line and returns 0. A deployer with
# no python REFUSES: no later gate runs a step on gov, so a skip would land a step gov never ran. The
# walk's lines go to stdout on success; on a refusal to stderr, and this returns 1.
run_gov_first() {  # -> 0 walked or announced-skipped · 1 a step, the landing check or the resolver refused
  local py dir out rc got kit=govkit anchor=govkit.py
  got=$(resolve_lander_kit "$kit" "$anchor"); rc=$?
  if [ "$rc" = 1 ]; then
    if [ -f "$self_dir/$kit/$anchor" ] || [ -f "$self_dir/../$kit/$anchor" ]; then
      echo "push-main: the upgrade steps could NOT be run on gov first — a govkit deployer is beside this lander and no usable python launcher runs it, and no later gate runs a step on gov." >&2
      return 1
    fi
    echo "push-main: slot point.flow.version · not-installed: the gov-first walk is skipped as not gov's tree — no govkit deployer beside this lander."
    return 0
  fi
  if [ "$rc" != 0 ]; then
    echo "push-main: slot point.flow.version · not-installed: the gov-first walk is skipped as not gov's tree — no govkit deployer beside this lander."
    return 0
  fi
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  out=$("$py" "$top/$dir/govkit.py" update --target "$top" --write 2>&1); rc=$?
  if [ "$rc" -eq 0 ]; then
    printf '%s\n' "$out"
    echo "push-main: slot point.flow.version · filled" >&2
    return 0
  fi
  echo "push-main: the upgrade steps REFUSED on gov first (exit $rc):" >&2
  # The indent with no fork; a CR before a line end drops, as Git for Windows' `sed` drops it.
  out=${out//$'\r\n'/$'\n'}; out=${out%$'\r'}
  printf '  %s\n' "${out//$'\n'/$'\n  '}" >&2
  return 1
}

# `read_mint_unit <range>` prints the unit id the attended mint commit names (TOOL-aRoutedQuill-3
# S11): the newest one <range>'s own commits attribute, by the memory-tree kit's routed-commits
# reading, so the commit its pre-push leg grades names a unit like every other routed commit. Found
# the way the deployer is found. No python, no kit or no attributed commit prints nothing, and the
# mint then names no unit, which that leg reds exactly as it reds the range that owed the mint.
read_mint_unit() {  # range -> the unit id on stdout, or nothing
  local py dir out got
  got=$(resolve_lander_kit memory-tree routed_commits.py) || return 0
  py=${got%%$'\t'*} dir=${got#*$'\t'}
  # Output and status apart (TOOL-aRoutedQuill-12 S11): a refusal prints on stdout and exits 2, and
  # piped straight into `head` its first line became the unit id.
  out=$("$py" "$top/$dir/routed_commits.py" --newest-unit "$1" 2>/dev/null) || return 0
  printf '%s\n' "$out" | head -n 1
}

# `write_merge_fold <first> <second> <message>` rewrites the detached prepared merge over the working
# tree, same parents and message, when the tree differs from HEAD, and leaves the new merge in the
# caller's `t`. `commit-tree`, so no pre-commit hook fires (the MINT note in `cmd_prepare`). Its two
# callers: after gov first's walk, so the regeneration meets the walk committed at HEAD, and after the
# regeneration (PLAY-dOrderedCharter-85). Each caller refuses on its own 1 with its own stage's text.
write_merge_fold() {  # first parent · second parent · message -> 0 HEAD is the merge over the tree, or the tree was HEAD's · 1 the stage, the commit or the ref move failed
  write_staged_change
  case $? in 1) return 0 ;; 2) return 1 ;; esac
  t=$(git commit-tree "$(git write-tree)" -p "$1" -p "$2" -m "$3") && git update-ref --no-deref HEAD "$t" || return 1
}

# `--prepare`: merge THIS branch onto the advertised tip, in place, and move the branch to it.
#
# THE SUBJECT NAMES THE SLUG AND NO UNIT ID. `build_commit` in the unattended kit joins a commit to
# a unit by the unit id as a whole token in its subject, so a unit id here would make the landing
# merge that unit's build commit and move every verdict derived from it.
cmd_prepare() {  # -> 0 prepared (or already was) · 1 refused · 3 nothing could be observed
  local branch oldb R t dirt msg
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
  # remedy instead of the misleading "CONFLICT" the merge-failure path would print. The ONE definition
  # of dirty the attended path and .githooks/pre-push spell (TOOL-aRepatriatedFork-8 S3): the hook
  # refuses an untracked file at `--land` anyway, so the retired `-uno` here only moved that refusal
  # past a merge it had already made.
  dirt=$(git status --porcelain --ignore-submodules=untracked 2>/dev/null) || dirt="(git status failed)"
  if [ -n "$dirt" ]; then
    echo "push-main: the working tree has uncommitted changes or untracked files — commit, stash or remove them before landing $def:" >&2
    printf '%s\n' "$dirt" | sed 's/^/    /' >&2
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
  msg="merge: $SLUG — land onto $remote/$def at ${R:0:8}"
  if ! git merge --no-ff "$oldb" -m "$msg" >/dev/null 2>&1; then
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
  # MINT INTO THE MERGE (TOOL-aMendedFleet-65 S3): the versions this landing owes are written over
  # the merged tree and the merge is REWRITTEN with them, same parents and subject, so the value
  # enters through the prepared merge itself and the idempotency check above still sees one merge
  # on the tip. `commit-tree`, not `--no-commit` and `git commit`: concluding a merge with
  # `git commit` fires the pre-commit staged legs over the whole landing diff, which `git merge`
  # never fires. A refusal takes the CONFLICT path's exit shape: the branch is left unmoved.
  if ! run_minter "$R" "$oldb"; then
    git reset -q --hard "$t" >/dev/null 2>&1 || true
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: the kit versions this landing owes could not be minted (named above). Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  # GOV FIRST INTO THE MERGE (TOOL-dSafePassage-8 S4): after the mint and before the regeneration,
  # so gov's receipt joins the one rewritten merge. ONE snapshot, taken before it and kept until the
  # regeneration passes (TOOL-dSafePassage-27), so a refused walk (TOOL-dSafePassage-25) and a
  # refused regeneration below both clean the receipt, the before-images and the orders the walk
  # created, which the reset leaves untracked. A snapshot taken after the walk would hold them.
  gfsnap=$(mktemp)
  if ! write_untracked_snapshot "$gfsnap"; then
    rm -f "$gfsnap"
    git reset -q --hard "$t" >/dev/null 2>&1 || true
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: gov first could not snapshot the untracked files before its walk, so the walk did not run. Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  if ! run_gov_first; then
    git reset -q --hard "$t" >/dev/null 2>&1 || true
    remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: the upgrade steps this landing declares did not hold on gov first (named above). Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  # FOLD THE WALK BEFORE THE REGENERATION (PLAY-dOrderedCharter-85): the policy mirror renders only a
  # committed input, so the mint's and the walk's output enter the merge first. The refusals below
  # then reset to this folded `t`, and the checkout of the branch takes away what the walk created.
  if ! write_merge_fold "$R" "$oldb" "$msg"; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: could not fold the upgrade steps' output into the merge before the regeneration. Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  # REGENERATE INTO THE MERGE (TOOL-aPrimedIndex-4): after the mint, because a minted version can
  # itself stale an output that stamps it; folded by the same rewrite, same parents and subject.
  if ! run_regen; then
    git reset -q --hard "$t" >/dev/null 2>&1 || true
    remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: the generated outputs this landing owes could not be regenerated (named above). Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  rm -f "$gfsnap"
  if ! write_merge_fold "$R" "$oldb" "$msg"; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: could not commit the minted versions into the merge. Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
  # MERGE LOSS (TOOL-aMendedFleet-3): the CONFLICT path's exit shape, so a refused landing leaves the
  # branch exactly where it was. `R..t` holds this merge and every merge the branch carries past R.
  if ! check_merge_losses "$R" "$t"; then
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: landing '$branch' onto $remote/$def at ${R:0:8} would publish a merge that loses a definition one of its parents carried (named above). Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    echo "  Restore it in a new commit on '$branch', or add 'superseded: <name> -> <successor>' to that merge's message, then run --prepare again." >&2
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
  local attempt R t rc cls pushed
  attempt=1
  while [ "$attempt" -le "$max" ]; do
    R=$(resolve_tip) || exit 3
    read_tip_object "$R" || exit 3
    if ! t=$(check_prepared_merge "$R"); then
      [ "$attempt" -gt 1 ] && echo "push-main: $remote/$def moved again between the re-prepare and this attempt." >&2
      exit 1
    fi
    check_carry_set "$R" || exit 1
    # THE FENCE READ, once per attempt and before the verdict files are cleared (TOOL-dPlacedRequest-15
    # S3): a refusal has printed its line and pushes nothing, and the case below exits 1 on it.
    if ! read_fence_line; then
      cls=refused
    else
      # IN THIS WORKTREE'S OWN GIT DIR, which is the one the pre-push hook reads when the push is
      # issued from here. The lander marker below is the one resolved against the COMMON dir; the two
      # files answer different questions and live in different places on purpose. Touched BEFORE the
      # clear and held until the verdict files are read. A claim push from this git dir is not waited
      # on: the hook clears the verdict files only on a default-branch push (TOOL-dPlacedRequest-11).
      touch "$marker"
      # The hook's verdict and the bar it vetted are cleared before every push, as the attended path
      # clears them, so a file an earlier push's hook wrote cannot be read as this one's answer.
      rm -f "$refusal" "$barfile" "$allowfile"
      echo "push-main: gating + pushing ${t:0:8} to $def (attempt $attempt/$max)..." >&2
      # HEAD, never refs/heads/<def>: the local default branch is shared by every build on this node,
      # and publishing it is the defect these flags close. Its output is SHOWN and never read (S2).
      # THE SHA PUSHED, NOT THE PREPARED ONE (TOOL-aPrimedIndex-10): under in-place the close commits its
      # records on the prepared merge, so HEAD is what the hook vets and names in its allow record.
      pushed=$(git rev-parse --verify HEAD)
      write_effect_push "HEAD:refs/heads/$def"
      rc=$?
      if [ "$rc" -eq 0 ]; then
        check_push_allow "$pushed" "$R" || exit 4
        write_lander_marker || exit 1
        run_post_merge
        cls=landed
      else
        cls=$(derive_push_failure)
      fi
    fi
    rm -f "$marker"
    if [ "$cls" = landed ]; then
      echo "push-main: landed $def on $remote." >&2
      exit 0
    fi
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
      refenced)
        # THIS HOLDER'S OWN WRITE MOVED THE LEASE (TOOL-dPlacedRequest-29 S3): the default branch did
        # not move, so the prepared merge stands; the next attempt's fence read fences on the new tip.
        attempt=$((attempt + 1)) ;;
      *)
        # refused, unreachable, unchanged, fenced or unfenced: derive_push_failure has said which,
        # and why; or a fence read refused, which read_fence_line has said.
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
# `branch` was read at the top, where the remote is resolved from it (TOOL-aRepatriatedFork-8 S1).
if [ "$branch" != "$def" ]; then
  echo "push-main: on '$branch', not '$def' — land $def from the primary tree on $def." >&2
  exit 2
fi

# A dirty tree makes the reconcile merge refuse to START — NOT a merge conflict; catch it here with
# the real remedy instead of the misleading "reconcile CONFLICT" the merge-failure path would print.
# ONE definition of dirty, spelled identically in .githooks/pre-push, which refuses the same tree
# (TOOL-aRepatriatedFork-8 S3, from adopter ic's ARCH-dWaryGatepost-1). `-uno`, the spelling this used,
# passed a brand-new untracked source file that the bar then certified and the push did not carry.
# `--ignore-submodules=untracked` also refuses a moved submodule pointer and a tracked edit inside a
# submodule, and ignores a submodule's own untracked files, which no commit here can carry.
dirt=$(git status --porcelain --ignore-submodules=untracked 2>/dev/null) || dirt="(git status failed)"
if [ -n "$dirt" ]; then
  echo "push-main: the working tree has uncommitted changes or untracked files — commit, stash or remove them before landing $def:" >&2
  printf '%s\n' "$dirt" | sed 's/^/    /' >&2
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

  # MINT, on every attempt (TOOL-aMendedFleet-65 S4): this path has no prepared merge, so the versions
  # this landing owes over the fetched tip are their own commit. `--no-verify` for the reason
  # --prepare uses `commit-tree`; the pre-push bar below grades the commit like every other one it
  # pushes. It touches version carriers, which are product paths, so its SUBJECT names the newest
  # unit the pushed range attributes (TOOL-aRoutedQuill-3 S11) and its `Pass: none` trailer keeps
  # the unattended kit's pass reader from taking the mint for that unit's pass.
  mt=$(git rev-parse --verify "refs/remotes/$remote/$def")
  if ! run_minter "$mt"; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    echo "push-main: the kit versions this landing owes could not be minted (named above). Aborted (no push)." >&2
    exit 1
  fi
  write_staged_change; staged=$?
  if [ "$staged" = 2 ]; then
    echo "push-main: could not stage the minted versions. Aborted (no push)." >&2
    exit 1
  fi
  if [ "$staged" = 0 ]; then
    mint_unit=$(read_mint_unit "$mt..HEAD")
    if ! git commit -q --no-verify -m "mint: kit versions onto $remote/$def at ${mt:0:8}${mint_unit:+ for $mint_unit}" -m "Pass: none"; then
      echo "push-main: could not commit the minted versions. Aborted (no push)." >&2
      exit 1
    fi
  fi

  # GOV FIRST, on every attempt, after the mint (TOOL-dSafePassage-8 S4): its own commit, named and
  # trailered as the mint commit is, so the routed-commits leg and the pass reader read it alike. A
  # refusal cleans what the walk created against a snapshot taken before it (TOOL-dSafePassage-25).
  gfsnap=$(mktemp)
  if ! write_untracked_snapshot "$gfsnap"; then
    rm -f "$gfsnap"
    echo "push-main: gov first could not snapshot the untracked files before its walk, so the walk did not run. Aborted (no push)." >&2
    exit 1
  fi
  if ! run_gov_first; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
    echo "push-main: the upgrade steps this landing declares did not hold on gov first (named above). Aborted (no push)." >&2
    exit 1
  fi
  rm -f "$gfsnap"
  write_staged_change; staged=$?
  if [ "$staged" = 2 ]; then
    echo "push-main: could not stage gov's receipt of the upgrade steps. Aborted (no push)." >&2
    exit 1
  fi
  if [ "$staged" = 0 ]; then
    gf_unit=$(read_mint_unit "$mt..HEAD")
    if ! git commit -q --no-verify -m "steps: gov first onto $remote/$def at ${mt:0:8}${gf_unit:+ for $gf_unit}" -m "Pass: none"; then
      echo "push-main: could not commit gov's receipt of the upgrade steps. Aborted (no push)." >&2
      exit 1
    fi
  fi

  # REGENERATE, on every attempt, after the mint (TOOL-aPrimedIndex-4): its own commit, named and
  # trailered as the mint commit is, so the routed-commits leg and the pass reader read it alike.
  rgsnap=$(mktemp)
  if ! write_untracked_snapshot "$rgsnap"; then
    rm -f "$rgsnap"
    echo "push-main: the regeneration could not snapshot the untracked files before it ran, so it did not run. Aborted (no push)." >&2
    exit 1
  fi
  if ! run_regen; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    remove_new_untracked "$rgsnap"; rm -f "$rgsnap"
    echo "push-main: the generated outputs this landing owes could not be regenerated (named above). Aborted (no push)." >&2
    exit 1
  fi
  rm -f "$rgsnap"
  write_staged_change; staged=$?
  if [ "$staged" = 2 ]; then
    echo "push-main: could not stage the regenerated outputs. Aborted (no push)." >&2
    exit 1
  fi
  if [ "$staged" = 0 ]; then
    regen_unit=$(read_mint_unit "$mt..HEAD")
    if ! git commit -q --no-verify -m "regen: generated outputs onto $remote/$def at ${mt:0:8}${regen_unit:+ for $regen_unit}" -m "Pass: none"; then
      echo "push-main: could not commit the regenerated outputs. Aborted (no push)." >&2
      exit 1
    fi
  fi

  # THE FENCE READ under `--slug`, once per attempt and before the clear (TOOL-dPlacedRequest-15 S3,
  # S6); with no slug it reads nothing and the push below is today's. A refusal pushes nothing.
  if ! read_fence_line; then
    cls=refused
  else
    # The marker first, then the clear; the marker stays until the verdict files have been read. No
    # claim push is waited on (TOOL-dPlacedRequest-11).
    touch "$marker"
    rm -f "$refusal" "$barfile" "$allowfile"
    echo "push-main: gating + pushing $def (attempt $attempt/$max)..." >&2
    # THE PUSH'S OUTPUT IS SHOWN, NEVER READ (S2). It carries the bar's own output, so classifying on
    # its words let any leg that printed `connection` report a red bar as an unreachable remote
    # (TOOL-aHonedRuleset-10), and any leg that printed `rejected` fake a race and re-run the bar.
    # A fenced push names the branch in full, since a second refspec rides beside it.
    pushed=$(git rev-parse --verify "refs/heads/$def")
    was=$(git rev-parse -q --verify "refs/remotes/$remote/$def") || was=""
    if [ -n "$FENCE_REF" ]; then write_effect_push "refs/heads/$def:refs/heads/$def"; else write_effect_push "$def"; fi
    rc=$?
    if [ "$rc" -eq 0 ]; then
      check_push_allow "$pushed" "$was" || exit 4
      write_lander_marker || exit 1
      run_post_merge
      cls=landed
    else
      # The hook's verdict first, then a probe, then ancestry: derive_push_failure, shared with --land.
      cls=$(derive_push_failure)
    fi
  fi
  rm -f "$marker"
  if [ "$cls" = landed ]; then
    echo "push-main: landed $def on $remote." >&2
    exit 0
  fi
  case "$cls" in
    race)
      echo "push-main: push rejected — $remote/$def advanced during the gate; re-reconciling and re-gating..." >&2
      attempt=$((attempt + 1)) ;;
    refenced)
      # TOOL-dPlacedRequest-29 S3: the lease moved under this holder's own write; nothing to reconcile.
      attempt=$((attempt + 1)) ;;
    *)
      exit 1 ;;
  esac
done

echo "push-main: $remote/$def is moving faster than the gate ($max attempts exhausted) — land when the fleet is quieter, or coordinate." >&2
exit 1

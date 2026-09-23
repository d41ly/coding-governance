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
set -u

top=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "push-main: not a git repo" >&2; exit 2; }
cd "$top" || exit 2

# THE REMOTE FIRST, then ITS default branch (TOOL-aRepatriatedFork-8 S1). This read `origin/HEAD`
# before it knew which remote it would push to, so on a node whose remote is named anything else
# (inCMS's node `d` names it `incms`) it exited 2 before its first fetch. The remote is GOV_REMOTE,
# else the current branch's configured remote, else the repository's ONLY remote. Several remotes
# and none configured is a refusal: guessing picks a remote nobody chose.
branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
remote=${GOV_REMOTE:-}
[ -n "$remote" ] || remote=$(git config "branch.$branch.remote" 2>/dev/null || true)
if [ -z "$remote" ]; then
  remotes=$(git remote 2>/dev/null)
  case "$remotes" in *$'\n'*|"") ;; *) remote=$remotes ;; esac
  if [ -z "$remote" ]; then
    echo "push-main: can't determine which remote to land on — GOV_REMOTE is unset, '$branch' has no configured remote, and this repository has $(printf '%s' "$remotes" | grep -c .) remotes." >&2
    echo "  Name it: export GOV_REMOTE=<remote>." >&2
    exit 2
  fi
fi

# Resolve the default branch, GOV_DEFAULT_BRANCH first then that remote's HEAD. Fail CLOSED if neither
# is set — silently assuming 'main' would let a push to a real 'develop'/'master' default run un-gated.
def=${GOV_DEFAULT_BRANCH:-$(git symbolic-ref --short "refs/remotes/$remote/HEAD" 2>/dev/null)}
def=${def#"$remote"/}
if [ -z "$def" ]; then
  echo "push-main: can't determine the default branch ($remote/HEAD unset, GOV_DEFAULT_BRANCH unset) —" >&2
  echo "  set it with 'git remote set-head $remote -a', or export GOV_DEFAULT_BRANCH=<branch>." >&2
  exit 2
fi
max=${GOV_PUSH_MAIN_MAX_RETRIES:-3}
gd=$(git rev-parse --git-dir)
marker="$gd/push-main-active"
# THE HOOK'S VERDICT (S2): `<token><TAB><message>`, written by .githooks/pre-push on every refusal and
# on a red bar, cleared by it on every run and by this script before every push.
refusal="$gd/pre-push-refusal"

# The marker is a SOFT advisory guard: a SIGKILL/OOM/power-loss during the gate can leak it (this
# trap can't catch those). Worst case a later raw push skips reconcile-before-gate and wastes ONE
# gate run; nothing red reaches origin, and the next push-main run's EXIT trap clears a stale marker.
trap 'rm -f "$marker"' EXIT INT TERM

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

if [ "$branch" != "$def" ]; then
  echo "push-main: on '$branch', not '$def' — land $def from the primary tree on $def." >&2
  exit 2
fi

# A dirty tree makes the reconcile merge refuse to START — NOT a merge conflict; catch it here with
# the real remedy instead of the misleading "reconcile CONFLICT" the merge-failure path would print.
# ONE definition of dirty, spelled identically in .githooks/pre-push, which refuses the same tree
# (TOOL-aRepatriatedFork-8 S3, from inCMS's ARCH-dWaryGatepost-1). `-uno`, the spelling this used,
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

  rm -f "$refusal"
  touch "$marker"
  echo "push-main: gating + pushing $def (attempt $attempt/$max)..." >&2
  # THE PUSH'S OUTPUT IS SHOWN, NEVER READ (S2). It carries the bar's own output, so classifying on
  # its words let any leg that printed `connection` report a red bar as an unreachable remote
  # (TOOL-aHonedRuleset-10), and any leg that printed `rejected` fake a race and re-run the bar.
  git push "$remote" "$def" >&2
  rc=$?
  rm -f "$marker"
  if [ "$rc" -eq 0 ]; then
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
    if [ -f .unattended.conf ]; then
      lm=$(. ./.unattended.conf 2>/dev/null; printf '%s' "${LANDER_MARKER:-}")
      # A STUB-GATED PUSH IS NOT A LANDING (TOOL-aRepatriatedFork-5). GOV_GATE_CMD_TEST is the hook's
      # one declared escape: it lets an untracked stub stand in for the bar so the hook can be tested
      # at all. The marker is what `unattended.sh --landed` accepts as a landing through this lander,
      # so writing it here would let a push nobody's bar gated read as a gated landing.
      if [ -n "$lm" ] && [ -n "${GOV_GATE_CMD_TEST:-}" ]; then
        echo "push-main: pushed $def under GOV_GATE_CMD_TEST, so the bar was a declared STUB; NOT writing the lander marker ($lm), because a stub-gated push is not a landing." >&2
        lm=""
      fi
      if [ -n "$lm" ]; then
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
          exit 1
        fi
        if ! printf 'landed %s at %s by push-main\n' "$def" "$(git rev-parse HEAD)" > "$_gcd/$lm"; then
          echo "push-main: pushed $def, but could not write the lander marker at $_gcd/$lm. The push SUCCEEDED and is not recorded." >&2
          exit 1
        fi
      fi
    fi
    echo "push-main: landed $def on $remote." >&2
    exit 0
  fi

  # THE ORDER OF EVIDENCE is inCMS's: the hook's own verdict; else a probe of the push URL, so that
  # unreachability is OBSERVED rather than inferred; else fetch and ancestry, a race or a failure the
  # hook did not claim. An absent verdict is the cue to probe, never a pass: a hook that predates the
  # channel, or a push that died before the hook ran, writes none.
  tok=""; msg=""
  [ -f "$refusal" ] && IFS=$'\t' read -r tok msg < "$refusal"
  case "$tok" in
    gate-red)
      echo "push-main: the bar RAN and is RED, so nothing was pushed — read $gd/gate-last-summary.txt, fix it, and re-run push-main." >&2
      exit 1 ;;
    head-moved)
      echo "push-main: the bar ran GREEN but HEAD moved while it ran, so the green does not describe the pushed tree — re-run push-main. ($msg)" >&2
      exit 1 ;;
    ?*)
      echo "push-main: pre-push refused the push ($tok) — a precondition; no leg ran: $msg" >&2
      exit 1 ;;
  esac
  if ! git ls-remote "$(git remote get-url --push "$remote" 2>/dev/null || printf '%s' "$remote")" "refs/heads/$def" >/dev/null 2>&1; then
    echo "push-main: could not reach $remote — a probe of its push URL failed after the push did, and the hook left no verdict; retry when the remote is reachable." >&2
    exit 1
  fi
  git fetch "$remote" "$def" 2>/dev/null || true
  if git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then
    echo "push-main: the push failed, $remote/$def is unchanged and reachable, and the hook left no verdict — the remote refused it or the hook predates its refusal channel; read the push output above." >&2
    exit 1
  fi
  echo "push-main: push rejected — $remote/$def advanced during the gate; re-reconciling and re-gating..." >&2
  attempt=$((attempt + 1))
done

echo "push-main: $remote/$def is moving faster than the gate ($max attempts exhausted) — land when the fleet is quieter, or coordinate." >&2
exit 1

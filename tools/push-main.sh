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

# Resolve the default branch, GOV_DEFAULT_BRANCH first then origin/HEAD. Fail CLOSED if neither is
# set — silently assuming 'main' would let a push to a real 'develop'/'master' default run un-gated.
def=${GOV_DEFAULT_BRANCH:-$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null)}
def=${def#origin/}
if [ -z "$def" ]; then
  echo "push-main: can't determine the default branch (origin/HEAD unset, GOV_DEFAULT_BRANCH unset) —" >&2
  echo "  set it with 'git remote set-head origin -a', or export GOV_DEFAULT_BRANCH=<branch>." >&2
  exit 2
fi
remote=${GOV_REMOTE:-$(git config "branch.$def.remote" 2>/dev/null || echo origin)}
max=${GOV_PUSH_MAIN_MAX_RETRIES:-3}
marker="$(git rev-parse --git-dir)/push-main-active"

# The marker is a SOFT advisory guard: a SIGKILL/OOM/power-loss during the gate can leak it (this
# trap can't catch those). Worst case a later raw push skips reconcile-before-gate and wastes ONE
# gate run; nothing red reaches origin, and the next push-main run's EXIT trap clears a stale marker.
trap 'rm -f "$marker"' EXIT INT TERM

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
  # Classify a push failure on what git SAID (streamed live via tee, also captured), not on whether
  # origin moved (a guard on the wrong signal calls a gate-passed-but-network-failed push "RED", and
  # loops a still-RED commit as a race when a peer advanced origin during the gate).
  pout=$(mktemp)
  git push "$remote" "$def" 2>&1 | tee "$pout" >&2
  rc=${PIPESTATUS[0]}
  rm -f "$marker"
  if [ "$rc" -eq 0 ]; then
    rm -f "$pout"
    echo "push-main: landed $def on $remote." >&2
    exit 0
  fi

  if grep -qiE 'rejected|fetch first|non-fast-forward|stale info' "$pout"; then
    cls=race
  elif grep -qiE 'unable to access|could not resolve host|could not read from remote|connection|timed out' "$pout"; then
    cls=unreachable
  else
    git fetch "$remote" "$def" 2>/dev/null || true
    if git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then cls=red; else cls=race; fi
  fi
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

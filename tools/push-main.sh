#!/usr/bin/env bash
# push-main.sh — the sanctioned lander for a push to the default branch (TOOL-aLeasedGauntlet-1,
# ports inCMS ARCH-aLeasedGauntlet-1).
#
# Reconciles the default branch BEFORE the pre-push full gate runs, so the gate never runs on an
# already-stale tree; if origin advances DURING the gate the push is rejected and this re-reconciles
# + re-gates, bounded by GOV_PUSH_MAIN_MAX_RETRIES (default 3). It sets a marker the pre-push hook
# requires, so a raw `git push` to the default branch is refused and steered here. Bypass:
# git push --no-verify.
set -u

top=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "push-main: not a git repo" >&2; exit 2; }
cd "$top" || exit 2

def=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null); def=${def#origin/}
def=${GOV_DEFAULT_BRANCH:-${def:-main}}
remote=${GOV_REMOTE:-$(git config "branch.$def.remote" 2>/dev/null || echo origin)}
max=${GOV_PUSH_MAIN_MAX_RETRIES:-3}
marker="$(git rev-parse --git-dir)/push-main-active"

trap 'rm -f "$marker"' EXIT INT TERM

branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
if [ "$branch" != "$def" ]; then
  echo "push-main: on '$branch', not '$def' — land $def from the primary tree on $def." >&2
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
  if git push "$remote" "$def"; then
    rm -f "$marker"
    echo "push-main: landed $def on $remote." >&2
    exit 0
  fi
  rm -f "$marker"

  git fetch "$remote" "$def" 2>/dev/null || true
  if git merge-base --is-ancestor "$remote/$def" HEAD 2>/dev/null; then
    echo "push-main: push failed but $remote/$def is unchanged — the gate is RED (see above), not a remote race. Fix it and re-run push-main." >&2
    exit 1
  fi
  echo "push-main: push rejected — $remote/$def advanced during the gate; re-reconciling and re-gating..." >&2
  attempt=$((attempt + 1))
done

echo "push-main: $remote/$def is moving faster than the gate ($max attempts exhausted) — land when the fleet is quieter, or coordinate." >&2
exit 1

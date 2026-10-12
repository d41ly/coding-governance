#!/usr/bin/env bash
# **Serves:** research TOOL-aBriskPreflight-6
# TOOL-aBriskPreflight-6's instrument: the pre-push hook on a claim-shaped push, one hook at a time.
#
#   bash <this> --setup <clone> <source-repo> <rev>
#   bash <this> --run <clone> <hook-dir> <label> <outdir> [--untraced]
#
# --setup clones <source-repo> into <clone>, which must not exist, checks out <rev>, records
# origin/HEAD as origin/main, points core.hooksPath at the clone's own `.githooks`, and builds a claim
# commit the way `write_claim` does: `git mktree` over empty input, then `git commit-tree`. Its sha is
# written to <clone>/.git/claim-sha. A throwaway clone, because the hook writes the push journal of
# the git dir it runs in.
# --run copies <hook-dir>'s pre-push and straggler-guard.sh over the clone's own `.githooks`, appends
# a host-state line to <outdir>/runs.log, then feeds `.githooks/pre-push origin <url>` one line,
# `refs/gov/runs/x <claim> refs/gov/runs/x <zeros>`, from the clone's root. It is traced under the
# baseline's run-traced.sh, which writes <outdir>/<label>.trace, .out and a runs.log row; with
# --untraced it is timed bare and the same row is written. It then prints that row and the last line
# of the clone's push journal. GOV_DEFAULT_BRANCH, GOV_RUNLOG and GOV_BRANCH_GATE_CMD are unset, as
# the unattended suite's hooked claim block unsets them.
#
# WHAT IT DOES NOT CHECK: a real `git push`, so git's own cost around the hook is not in the figure;
# and a hook copied in differs from the clone's HEAD, which nothing on this push path reads, since the
# dirty-tree check sits below the `skip-nondefault` exit.
set -u
here=$(cd "$(dirname "$0")" && pwd) || exit 2
case "${1:-}" in
  --setup)
    clone=${2:-}; src=${3:-}; rev=${4:-}
    [ -n "$clone" ] && [ -n "$src" ] && [ -n "$rev" ] || { echo "usage: $0 --setup <clone> <source-repo> <rev>"; exit 2; }
    [ ! -e "$clone" ] || { echo "claim-push: $clone exists; a setup never reuses a tree"; exit 2; }
    git clone -q --local --no-checkout "$src" "$clone" || exit 2
    git -C "$clone" checkout -q -b bp6 "$rev" || exit 2
    git -C "$clone" remote set-head origin main || exit 2
    git -C "$clone" config core.hooksPath .githooks
    t=$(git -C "$clone" mktree </dev/null) || exit 2
    c=$(git -C "$clone" -c user.name=claim -c user.email=claim@example.invalid commit-tree -m "claim x" "$t") || exit 2
    printf '%s\n' "$c" > "$clone/.git/claim-sha"
    echo "claim-push: clone $clone at $(git -C "$clone" rev-parse --short HEAD) · origin/HEAD $(git -C "$clone" symbolic-ref --short refs/remotes/origin/HEAD) · claim $c"
    ;;
  --run)
    clone=${2:-}; hooks=${3:-}; label=${4:-}; out=${5:-}; mode=${6:-traced}
    [ -f "$clone/.git/claim-sha" ] && [ -f "$hooks/pre-push" ] && [ -f "$hooks/straggler-guard.sh" ] && [ -n "$label" ] && [ -n "$out" ] \
      || { echo "usage: $0 --run <clone> <hook-dir> <label> <outdir> [--untraced]"; exit 2; }
    mkdir -p "$out" && out=$(cd "$out" && pwd) || exit 2
    cp "$hooks/pre-push" "$hooks/straggler-guard.sh" "$clone/.githooks/" || exit 2
    c=$(cat "$clone/.git/claim-sha")
    line="refs/gov/runs/x $c refs/gov/runs/x 0000000000000000000000000000000000000000"
    url=$(git -C "$clone" remote get-url origin)
    journal="$(cd "$clone" && cd "$(git rev-parse --git-common-dir)" && pwd)/runlog/pushes.log"
    bash "$here/2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh" "$label" "$out"
    if [ "$mode" = --untraced ]; then
      s=$EPOCHREALTIME
      ( cd "$clone" && env -u GOV_DEFAULT_BRANCH -u GOV_RUNLOG -u GOV_BRANCH_GATE_CMD \
          bash .githooks/pre-push origin "$url" <<< "$line" >"$out/$label.out" 2>&1 )
      rc=$?; e=$EPOCHREALTIME
      printf 'label=%s rc=%s start=%s end=%s wall=%s\n' "$label" "$rc" "$s" "$e" "$(awk -v a="$s" -v b="$e" 'BEGIN{printf "%.1f", b-a}')" >> "$out/runs.log"
    else
      env -u GOV_DEFAULT_BRANCH -u GOV_RUNLOG -u GOV_BRANCH_GATE_CMD \
        bash "$here/2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh" "$clone" "$label" "$out" \
        .githooks/pre-push origin "$url" <<< "$line"
    fi
    tail -n 2 "$out/runs.log"
    echo "journal: $(tail -n 1 "$journal" 2>/dev/null)"
    ;;
  *) echo "usage: $0 --setup <clone> <source-repo> <rev> | --run <clone> <hook-dir> <label> <outdir> [--untraced]"; exit 2 ;;
esac

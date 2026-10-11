#!/usr/bin/env bash
# probes-ab.sh <A|B> <outdir> <driver> — TOOL-aBriskPreflight-4 AC10, one arm of the A/B.
#
# Runs THIS worktree's four declared preflight probes, read from `.unattended.conf`, through the
# bounded runner's two halves sliced out of <driver>, and appends one `arm` row to <outdir>/runs.log.
#   A — the four through `run_bounded`, one after another, in the block's read order: wiring,
#       --carry, --prepared, profile. Today's preflight.
#   B — the four started through `init_bounded` in `init_preflight_probes`'s order, then read
#       through `read_bounded` in the block's read order. The built preflight.
# Each arm PROVES IT RAN, or its row says `ran=no` and it exits 1: the wiring check's status is 0,
# the lander's two statuses are 0 or 1, and the profile's stdout carries a `wall` row.
# What it does NOT do: run a verb, write the process ledger (the recorder is a no-op here), or run
# any bar or suite. The lander runs only its two read-only flags, under the declared GATE_BOUND.
# Run `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh <label> <outdir>` before each arm.
arm=$1; out=$2; drv=$3
case "$arm" in A|B) ;; *) echo "probes-ab: the arm is A or B, got '$arm'"; exit 2 ;; esac
[ -d "$out" ] && [ -f "$drv" ] || { echo "probes-ab: usage: probes-ab.sh <A|B> <outdir> <driver>"; exit 2; }
cd "$(git rev-parse --show-toplevel)" || exit 2
ROOT=$(pwd)
# shellcheck disable=SC1091
. ./.unattended.conf
GATE_BOUND_LIVE=0; timeout -k 1s 10 true >/dev/null 2>&1 && GATE_BOUND_LIVE=1
RB_BOUND=""; RB_HANDLE=""; RB_OUT=""; RB_STDOUT=""; RB_ERR=""; RB_TOOK=0
slug=aBriskPreflight
halves="$out/halves.$$.sh"; : > "$halves"
for fn in run_bounded init_bounded read_bounded; do sed -n "/^$fn() {/,/^}\$/p" "$drv" >> "$halves"; done
[ "$(grep -c '^}$' "$halves")" = 3 ] || { echo "probes-ab: could not slice the runner and its two halves out of $drv"; rm -f "$halves"; exit 2; }
# shellcheck disable=SC1090
. "$halves"; rm -f "$halves"
write_proc_record() { :; }
t0=$EPOCHREALTIME
if [ "$arm" = A ]; then
  # shellcheck disable=SC2086
  run_bounded $WIRING_CHECK; w=$?; tw=$RB_TOOK
  # shellcheck disable=SC2086
  run_bounded $LANDER --carry --slug "$slug"; c=$?
  # shellcheck disable=SC2086
  run_bounded $LANDER --prepared --slug "$slug"; p=$?
  # shellcheck disable=SC2086
  run_bounded $GATE_PROFILE_CMD; g=$?; prof=$RB_STDOUT
else
  hw=""; hc=""; hp=""; hg=""
  # shellcheck disable=SC2086
  init_bounded $WIRING_CHECK && hw=$RB_HANDLE
  # shellcheck disable=SC2086
  init_bounded $LANDER --carry --slug "$slug" && hc=$RB_HANDLE
  # shellcheck disable=SC2086
  init_bounded $LANDER --prepared --slug "$slug" && hp=$RB_HANDLE
  # shellcheck disable=SC2086
  init_bounded $GATE_PROFILE_CMD && hg=$RB_HANDLE
  [ -n "$hw" ] && [ -n "$hc" ] && [ -n "$hp" ] && [ -n "$hg" ] || { echo "probes-ab: a start could not make its capture"; exit 1; }
  read_bounded "$hw"; w=$?; tw=$RB_TOOK
  read_bounded "$hc"; c=$?
  read_bounded "$hp"; p=$?
  read_bounded "$hg"; g=$?; prof=$RB_STDOUT
fi
t1=$EPOCHREALTIME
ran=yes
[ "$w" = 0 ] || ran=no
case "$c$p" in [01][01]) ;; *) ran=no ;; esac
printf '%s\n' "$prof" | grep -q "^wall	" || ran=no
printf 'arm %s wall=%s wiring=%s(%ss) carry=%s prepared=%s profile=%s ran=%s at=%s\n' "$arm" \
  "$(awk -v a="$t0" -v b="$t1" 'BEGIN{printf "%.1f", b-a}')" "$w" "$tw" "$c" "$p" "$g" "$ran" "$(date -u +%H:%M:%SZ)" >> "$out/runs.log"
[ "$ran" = yes ]

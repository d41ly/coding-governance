#!/usr/bin/env bash
# run-traced.sh <tree> <label> <outdir> <script> [args...]
# Runs <script> from <tree> under the spawn-counting trace, recording the trace, stdout+stderr, rc and wall.
tree=$1; label=$2; out=$3; shift 3
mkdir -p "$out"
cd "$tree" || exit 2
s=$EPOCHREALTIME
env SHELLOPTS=xtrace BASH_XTRACEFD=9 PS4='+${EPOCHREALTIME} ${BASHPID} ${BASH_SOURCE##*/}:${LINENO} ' \
  bash "$@" 9>>"$out/$label.trace" >"$out/$label.out" 2>&1
rc=$?
e=$EPOCHREALTIME
printf 'label=%s rc=%s start=%s end=%s wall=%s\n' "$label" "$rc" "$s" "$e" "$(awk -v a="$s" -v b="$e" 'BEGIN{printf "%.1f", b-a}')" >> "$out/runs.log"

#!/usr/bin/env bash
# run-timed.sh <tree> <label> <outdir> <script> [args...]
# Runs <script> from <tree> untraced, recording stdout+stderr, rc and wall, and the host's spawn cost
# measured just before (five /usr/bin/true) so a reading carries the load it was taken under.
tree=$1; label=$2; out=$3; shift 3
mkdir -p "$out"
cd "$tree" || exit 2
p=$EPOCHREALTIME; for _i in 1 2 3 4 5; do /usr/bin/true; done; q=$EPOCHREALTIME
s=$EPOCHREALTIME
bash "$@" >"$out/$label.out" 2>&1
rc=$?
e=$EPOCHREALTIME
printf 'label=%s rc=%s start=%s wall=%s spawn5=%s\n' "$label" "$rc" "$s" \
  "$(awk -v a="$s" -v b="$e" 'BEGIN{printf "%.1f", b-a}')" "$(awk -v a="$p" -v b="$q" 'BEGIN{printf "%.2f", b-a}')" >> "$out/runs.log"

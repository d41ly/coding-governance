#!/usr/bin/env bash
# stall.sh <s> — a measure-legs fixture leg that HANGS and still spawns. TOOL-dRedressedBar-18, AC6.
#
# The shape of this build's hung canary: blocked reading a FIFO while a loop beside it keeps spawning
# `sleep`, so process churn alone would call it alive. It prints nothing while blocked, its tree's
# CPU stays near zero, and a delayed writer frees the FIFO after <s> seconds, so it ends by itself.
set -u
s=${1:-20}
d=$(mktemp -d "${TMPDIR:-/tmp}/stall.XXXXXXXX") || exit 1
mkfifo "$d/fifo" || exit 1
( while :; do sleep 1; done ) &
spinner=$!
( sleep "$s"; printf 'go\n' > "$d/fifo" ) &
IFS= read -r _line < "$d/fifo"
kill "$spinner" 2>/dev/null
wait "$spinner" 2>/dev/null
rm -rf "$d"
exit 0

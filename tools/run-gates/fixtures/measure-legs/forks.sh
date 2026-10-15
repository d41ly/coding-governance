#!/usr/bin/env bash
# forks.sh <n> — a measure-legs fixture leg that FORKS. TOOL-dRedressedBar-19, AC32.
#
# n `( /usr/bin/true )` subshells and n `$(true)` substitutions: every one is a fork of this shell,
# the path a bar's bash legs spend most of their processes on, where spawn.py's children are native
# spawns. With n = 0 it is the zero-count twin, so the two job totals differ by at least 2n.
set -u
n=${1:-0}
i=0
while [ "$i" -lt "$n" ]; do
  ( /usr/bin/true )
  got=$(true)
  i=$((i + 1))
done
exit 0

#!/usr/bin/env bash
# orphan.sh <hold_s> [<mark>] — a measure-legs fixture leg whose root ends while a process it started
# still holds the capture. TOOL-dRedressedBar-22, S2 and S9; the mark is TOOL-dRedressedBar-25 S18.
#
# It prints `early`, starts a background subshell that sleeps <hold_s> and then prints `late`, and
# exits 0 at once. The subshell inherits the leg's stdout, so at the root's exit the raw capture is
# still held, the leg's job still has processes, and the profiler keeps the capture pending. The
# two lines are 6 and 5 bytes, so the capture reads 6 at the root's exit and 11 once `late` lands.
#
# With <mark>, the subshell closes its stdout and stderr after `late` and only then creates <mark>,
# so once the mark exists `late` is in the capture and no process of the leg holds it: a leg that
# waits on the mark places the run end after both, where a fixed sleep only hoped to.
set -u
s=${1:-6}; m=${2:-}
printf 'early\n'
if [ -n "$m" ]; then ( sleep "$s"; printf 'late\n'; exec 1>&- 2>&-; : > "$m" ) &
else ( sleep "$s"; printf 'late\n' ) &
fi
exit 0

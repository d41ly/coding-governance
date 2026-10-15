#!/usr/bin/env bash
# orphan.sh <hold_s> — a measure-legs fixture leg whose root ends while a process it started still
# holds the capture. TOOL-dRedressedBar-22, S2 and S9.
#
# It prints `early`, starts a background subshell that sleeps <hold_s> and then prints `late`, and
# exits 0 at once. The subshell inherits the leg's stdout, so at the root's exit the raw capture is
# still held, the leg's job still has processes, and the profiler keeps the capture pending. The
# two lines are 6 and 5 bytes, so the capture reads 6 at the root's exit and 11 once `late` lands.
set -u
s=${1:-6}
printf 'early\n'
( sleep "$s"; printf 'late\n' ) &
exit 0

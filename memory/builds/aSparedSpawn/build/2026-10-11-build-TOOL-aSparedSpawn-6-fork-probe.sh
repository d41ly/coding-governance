#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-6
# TOOL-aSparedSpawn-6 unit 0 (S1, AC1) - the price of one `( : )` fork in a shell that holds the
# unattended driver's definitions, against the same fork in a bare shell, quiet and under load.
#
#   bash <this file> <path to unattended.sh> [forks, default 20] [loaders, default 8]
#
# THE SOURCED SHELL is built from the driver's own bytes: every function definition is lifted out
# with the same column-0 span rule the suite's slice_fn uses and sourced, so the shell's heap holds
# what a shell that sourced the refactored driver holds. The driver itself is not sourced, because
# at the sha this instrument first ran it executed its verb dispatch at top level and could not be.
#
# THE LOAD is N background loops of `( : )` forks, each in its own bash, standing in for the eight
# concurrent shards the research measured under: a build pass may run no suite. The instrument starts
# them, records their pids, and kills exactly those pids before it prints the loaded verdict.
#
# Output: one line per (shell, load) cell, `<cell> forks <n> total_ms <t> per_fork_ms <p>`, and a
# final `verdict` line comparing the loaded sourced fork against the 3000 ms stop price.
set -u
DRV=${1:?usage: fork-probe.sh <path to unattended.sh> [forks] [loaders]}
N=${2:-20}
W=${3:-8}
[ -r "$DRV" ] || { echo "fork-probe: cannot read the driver at $DRV"; exit 2; }
WORK=$(mktemp -d) || exit 2
trap 'rm -rf "$WORK"' EXIT
awk '/^[A-Za-z_][A-Za-z0-9_]*\(\) *\{.*\} *(#.*)?$/ && !f { print; next }
     /^[A-Za-z_][A-Za-z0-9_]*\(\) *\{/ && !f { f = 1 }
     f { print }
     f && /^\}[[:space:]]*(#.*)?$/ { f = 0 }' "$DRV" > "$WORK/fns.sh"
FNS=$(grep -c '^[A-Za-z_][A-Za-z0-9_]*() *{' "$WORK/fns.sh")
[ "$FNS" -gt 100 ] || { echo "fork-probe: lifted only $FNS function(s) out of $DRV, so the sourced shell would not hold the driver"; exit 2; }
# The timed body. EPOCHREALTIME is bash's own clock, so the measurement spawns nothing but the forks.
cat > "$WORK/time.sh" <<'TIME'
t0=${EPOCHREALTIME/,/.}; i=0
while [ "$i" -lt "$N" ]; do ( : ); i=$((i + 1)); done
t1=${EPOCHREALTIME/,/.}
awk -v a="$t0" -v b="$t1" -v n="$N" -v c="$CELL" 'BEGIN { t = (b - a) * 1000; printf "%s forks %d total_ms %.1f per_fork_ms %.2f\n", c, n, t, t / n }'
TIME
measure() { # cell · sourced(0|1)
  if [ "$2" = 1 ]; then
    CELL=$1 N=$N bash -c '. "$1" || exit 2; [ "$(declare -F | wc -l)" -gt 100 ] || { echo "the sourced shell holds no driver functions"; exit 2; }; . "$2"' _ "$WORK/fns.sh" "$WORK/time.sh"
  else
    CELL=$1 N=$N bash -c '. "$1"' _ "$WORK/time.sh"
  fi
}
echo "fork-probe: $FNS driver functions lifted from $DRV · $N forks per cell · $W loaders"
measure bare-quiet 0
measure sourced-quiet 1
pids=""
i=0
while [ "$i" -lt "$W" ]; do bash -c 'while :; do ( : ); done' </dev/null >/dev/null 2>&1 & pids="$pids $!"; i=$((i + 1)); done
sleep 2
loaded=$( { measure bare-loaded 0; measure sourced-loaded 1; } )
for p in $pids; do kill "$p" 2>/dev/null; done
for p in $pids; do wait "$p" 2>/dev/null; done
left=0; for p in $pids; do kill -0 "$p" 2>/dev/null && left=$((left + 1)); done
printf '%s\n' "$loaded"
echo "fork-probe: $W loaders reaped, $left still alive"
per=$(printf '%s\n' "$loaded" | awk '$1 == "sourced-loaded" { print $NF }')
awk -v p="${per:-x}" 'BEGIN { if (p == "x") { print "verdict UNREAD - the loaded sourced cell printed no figure"; exit 1 }
  if (p + 0 > 3000) { print "verdict STOP - a loaded sourced fork costs " p " ms, above the 3000 ms price"; exit 1 }
  print "verdict GO - a loaded sourced fork costs " p " ms, under the 3000 ms price" }'

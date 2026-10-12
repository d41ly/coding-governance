#!/usr/bin/env bash
# TOOL-aSparedSpawn-7 S1 / AC1 - the traced census of check-unattended.sh, and the AC2 / AC5 readings
# on the same conforming tree.
#
#   bash <this> <conforming-tree> <out-dir>
#
# <conforming-tree> is a clone of this repository at the commit under test, which the merge bar holds
# green: `git clone --local` into a SHORT root under TEMP (a deep scratchpad root hits MAX_PATH). It is
# never this worktree - a whole-leg run inside a pass is barred, and the clone is what makes the run
# reproducible. <out-dir> receives the raw trace, the region map and the table.
#
# WHAT IT MEASURES. One unscoped run under `bash -x` with PS4 carrying $EPOCHREALTIME, $LINENO and the
# call stack's line numbers, so every traced command is attributed to the line of the LEG's own source
# it was reached from (a library function's command to the leg line that called it). Regions: the
# prologue, `core`, the 28 region, and each post-28 check block, read off the leg's own guard lines.
# Per region: traced seconds (each line charged until the next one starts) and EXTERNAL commands (a
# traced command word that is no builtin, keyword or function of the leg or its library).
#
# WHAT IT DOES NOT MEASURE. Forks of `$(...)` and pipelines without an external command are not
# counted as spawns, and xtrace's own write cost is charged to the line after each trace line, so the
# seconds rank by line count as much as by work (the trace-profile-measures-itself gotcha): rank by
# the spawn column, and read `f` from both columns. A child script's own commands are invisible to
# `bash -x` (bash-x-does-not-follow-children); they show as the one external command that ran them.
#
# THEN, on the same tree: `--only core` (AC2: exit 0, one liveness line naming every post-28 check as
# skipped) and the unscoped run untraced (AC5: exit 0, no output). Each reading is printed with its rc.
set -u
TREE=${1:?usage: census.sh <conforming-tree> <out-dir>}; OUT=${2:?usage: census.sh <conforming-tree> <out-dir>}
mkdir -p "$OUT" || exit 2
OUT=$(cd "$OUT" && pwd)
cd "$TREE" || exit 2
LEG=tools/unattended/check-unattended.sh
LIB=tools/unattended/lib-unattended.sh
[ -f "$LEG" ] && [ -f "$LIB" ] || { echo "census: $TREE carries no unattended kit at tools/unattended"; exit 2; }
echo "census: tree $(git rev-parse HEAD) · node $(hostname) · $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# the region map, from the leg's own guard lines: <first line> <region>
awk '
  { ln = $0; sub(/\r$/, "", ln) }
  ln == "if check_selected core; then" { print NR, "core" }
  ln ~ /^if \[ "\$SCOPE" != skip28 \] && check_selected 28; then$/ { print NR, "r28" }
  ln == "if [ \"$SCOPE\" = only28 ] || [ \"$SCOPE\" = core ]; then" { print NR, "post-anchor" }
  ln ~ /^if check_selected [0-9]+; then$/ { n = ln; sub(/^if check_selected /, "", n); sub(/;.*/, "", n); print NR, "c" n }
  ln == "fi   # ---- end of the checks `--only 28` skips" { print NR, "tail" }
' "$LEG" > "$OUT/regions.txt"
[ "$(grep -c . "$OUT/regions.txt")" -ge 4 ] || { echo "census: the leg's guard lines were not found, so no region can be attributed: $OUT/regions.txt"; exit 2; }
{ compgen -b; compgen -k; grep -hoE '^[[:space:]]*[A-Za-z_][A-Za-z0-9_]*\(\)' "$LEG" "$LIB" | tr -d ' \t()'; } | sort -u > "$OUT/internal.txt"

t0=$EPOCHREALTIME
PS4='+|$EPOCHREALTIME|$LINENO|${BASH_LINENO[*]}| ' bash -x "$LEG" > "$OUT/traced.out" 2> "$OUT/trace.txt"
rc=$?
echo "census: traced unscoped run rc=$rc wall $(awk -v a="$t0" -v b="$EPOCHREALTIME" 'BEGIN { printf "%.1f", b - a }')s; stdout $(grep -c . "$OUT/traced.out") line(s)"

awk -v RF="$OUT/regions.txt" -v IF="$OUT/internal.txt" '
  BEGIN {
    while ((getline l < RF) > 0) { split(l, a, " "); nr++; rs[nr] = a[1]; rn[nr] = a[2] }
    while ((getline l < IF) > 0) internal[l] = 1
    FS = "|"
  }
  function region(line,   i, r) { r = "prologue"; for (i = 1; i <= nr; i++) if (line >= rs[i]) r = rn[i]; return r }
  /^\++\|[0-9.]+\|[0-9]+\|/ {
    ts = $2 + 0; ln = $3 + 0; n = split($4, st, " ")
    if (n >= 2) ln = st[n - 1] + 0          # the outermost frame: the leg line that reached this command
    cmd = $0; sub(/^\++\|[^|]*\|[^|]*\|[^|]*\| /, "", cmd)
    if (prev != "") { sec[prev] += ts - pts }
    r = region(ln); prev = r; pts = ts; lines[r]++
    w = cmd; sub(/^[A-Za-z_][A-Za-z0-9_]*(\[[^]]*\])?\+?=[^ ]*( |$)/, "", w)   # a leading assignment
    split(w, ww, " "); c = ww[1]; gsub(/\047/, "", c); sub(/^.*\//, "", c)   # xtrace prints the test bracket quoted
    if (c != "" && c !~ /=/ && !(c in internal) && !(ww[1] in internal)) ext[r]++
    seen[r] = 1
  }
  END {
    for (r in seen) { T += sec[r]; E += ext[r] }
    printf "%-12s %10s %8s %8s\n", "region", "seconds", "spawns", "lines"
    for (r in seen) printf "%-12s %10.2f %8d %8d\n", r, sec[r], ext[r], lines[r] | "sort -k3,3nr"
    close("sort -k3,3nr")
    for (r in seen) if (r == "r28" || r ~ /^c[0-9]+$/ || r == "post-anchor") { ts2 += sec[r]; es2 += ext[r] }
    printf "TOTAL        %10.2f %8d\n", T, E
    printf "f (28 region + post-28 checks): seconds %.3f · spawns %.3f\n", (T ? ts2 / T : 0), (E ? es2 / E : 0)
  }' "$OUT/trace.txt" | tee "$OUT/census.txt"

out=$(bash "$LEG" --only core 2>&1); rc=$?
echo "AC2: --only core rc=$rc"; printf '%s\n' "$out" | sed 's/^/  /'
out=$(bash "$LEG" 2>&1); rc=$?
echo "AC5: unscoped rc=$rc, $(printf '%s' "$out" | grep -c .) line(s) of output"; printf '%s\n' "$out" | sed 's/^/  /' | head -20

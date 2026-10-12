#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-18
# The direct check TOOL-aSparedSpawn-18's pass ran. Usage: bash <this> <frozen-clone> <instrument> <scratch-dir> ok|red|held
#
# Runs the width A/B instrument (`2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh`, or a copy of it at
# another revision) with AB_LOAD=0 over a two-leg GATE_LEGS manifest of `bash -c` legs, so each of its
# six bars costs seconds. `ok`: a repo leg and a kit-subject selftests leg, both exit 0. `red`: the kit
# leg exits 1. `held`: both legs are self-tests, so a bar without GATE_SELFTESTS=1 holds every leg and
# refuses having executed nothing. Prints the rows' load, width, gate_lines, legs, rc (when the
# instrument writes one) and artifact columns, then the quiet width-4 arm's `GATE` lines. Run once over
# the changed instrument and once over the base's, and once over a copy with GATE_SELFTESTS=1 removed
# (the staged break that isolates the count from the knob). No step runs a suite or the tree's bar.
set -u
C=${1:?frozen clone}; AB=${2:?instrument}; S=${3:?scratch dir}; CASE=${4:?case}
mkdir -p "$S" || exit 2
T=$(mktemp -d -p "$S") || exit 2
kit_rc=0; first='"chunk": "records", "subject": "repo"'
case "$CASE" in
  ok) ;;
  red) kit_rc=1 ;;
  held) first='"chunk": "selftests", "subject": "repo"' ;;
  *) echo "direct-checks: case is ok, red or held" >&2; exit 2 ;;
esac
printf '[\n {"name": "fx first", "argv": ["bash", "-c", "echo fx-first-ran"], %s, "ceiling": 60},\n {"name": "fx kit", "argv": ["bash", "-c", "echo fx-kit-ran; exit %s"], "chunk": "selftests", "subject": "kit", "ceiling": 60}\n]\n' \
  "$first" "$kit_rc" > "$T/legs.json"
AB_LOAD=0 bash "$AB" "$C" "$T/legs.json" "$T/rows.tsv" > "$T/ab.log" 2>&1 || { echo "direct-checks: the instrument exited $?" >&2; cat "$T/ab.log" >&2; exit 1; }
awk -F'\t' 'NR == 1 { for (i = 1; i <= NF; i++) col[$i] = i }
  /^#/ { print; next }
  { printf "%s\t%s\t%s\t%s\t%s\t%s\n", $col["load"], $col["width"], $col["gate_lines"], $col["legs"],
      (("rc" in col) ? $col["rc"] : "-"), $col["artifact"] }' "$T/rows.tsv"
grep -h '^GATE\|executed NOTHING' "$T"/rows.tsv.ab-quiet-4-*.out

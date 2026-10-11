#!/usr/bin/env bash
# ab-run.sh <rounds> — interleaved whole-preflight A/B: old arm %TEMP%/bp/AO, new arm %TEMP%/bp/AN.
# Each arm is reset to its fixture commit and its claim deleted from the mirror before it runs, and
# a run counts only when its output carries `preflight OK` (an A/B arm must prove it ran).
set -u
SP="C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-sleepy-kapitsa-1f69c8/653ff713-97af-487f-8f4e-2f4c9c73a605/scratchpad"
OUT="$SP/meas/ab"; mkdir -p "$OUT"
R="$TEMP/bp/R.git"
for i in $(seq 1 "$1"); do
  for arm in AO AN; do
    d="$TEMP/bp/$arm"
    git -C "$d" reset -q --hard fixture && git -C "$d" clean -fdq
    git -C "$R" update-ref -d refs/gov/runs/aTimedFixture 2>/dev/null
    git -C "$d" update-ref -d refs/gov/remote/runs/aTimedFixture 2>/dev/null
    bash "$SP/host-state.sh" "ab-$arm-$i" "$OUT"
    bash "$SP/run-timed.sh" "$d" "ab-$arm-$i" "$OUT" tools/unattended/unattended.sh --preflight aTimedFixture --keepalive-id abtest
    ok=$(grep -c 'preflight OK' "$OUT/ab-$arm-$i.out")
    echo "proof label=ab-$arm-$i preflight-ok=$ok last=$(tail -1 "$OUT/ab-$arm-$i.out" | cut -c1-120)" >> "$OUT/runs.log"
  done
done
echo done >> "$OUT/runs.log"

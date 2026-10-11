#!/usr/bin/env bash
# host-state.sh <label> <outdir> — one line of host state beside a timing: spawn cost of five
# /usr/bin/true, a bare $(...) fork, and the kernel pool counters (a leak there inflates every spawn).
label=$1; out=$2
p=$EPOCHREALTIME; for _i in 1 2 3 4 5; do /usr/bin/true; done; q=$EPOCHREALTIME
_x=$(:); r=$EPOCHREALTIME
pool=$(powershell.exe -NoProfile -Command "\$c=Get-Counter '\Memory\Pool Paged Bytes','\Memory\Pool Nonpaged Bytes','\Memory\Committed Bytes','\Processor(_Total)\% Processor Time' -ErrorAction SilentlyContinue; (\$c.CounterSamples | ForEach-Object { [math]::Round(\$_.CookedValue/1, 0) }) -join ' '" 2>/dev/null | tr -d '\r')
set -- $pool
printf 'host label=%s at=%s spawn5=%s fork=%s paged=%sMB nonpaged=%sMB committed=%sMB cpu=%s%%\n' "$label" "$(date -u +%H:%M:%SZ)" \
  "$(awk -v a="$p" -v b="$q" 'BEGIN{printf "%.2f", b-a}')" "$(awk -v a="$q" -v b="$r" 'BEGIN{printf "%.2f", b-a}')" \
  "$(( ${1:-0} / 1048576 ))" "$(( ${2:-0} / 1048576 ))" "$(( ${3:-0} / 1048576 ))" "${4:-?}" >> "$out/runs.log"

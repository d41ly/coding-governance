#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-15
# The direct checks TOOL-aSparedSpawn-15's pass ran, one step per criterion it could observe without
# a suite. Usage: bash <this> <repo-root> <scratch-dir> ac1|ac3|ac5|ac6|ac8
#
# Each step drives the CHANGED construct over a hand-built fixture, and where a criterion names a
# staged break it builds that break in a scratch copy and never in the tree. No step runs a suite,
# a slice of one, or a bar. What none of them observes is written in the acceptance ledger.
#   ac1  the agent-cap ratio arm's instrument over the shipped hook and a copy whose identifier
#        walk copies the line prefix per quote again, quiet and under twelve fork loops
#   ac3  the R6 arm's tick measurement (its sleep a stub on PATH) over the shipped `ts_tick_start` and a copy with `cat` and
#        `date` put back, quiet and under twelve fork loops, then over a file with no ticker
#   ac5  the run_bounded marker arms over the shipped run_bounded and a bound that captures through
#        a command substitution, plus the control
#   ac6  resume-tick's read_task_gone on a killed and an unkilled sleep (the second waits 120 s)
#   ac8  the kickoff S4 command over the shipped checker and a copy whose read_session_id reads
#        stdin although --session answered (the second waits 120 s)
set -u
# The launcher, resolved before any cd from the repository this record sits in, four levels up.
. "${BASH_SOURCE[0]%/*}/../../../../tools/lib/resolve-python.sh" || exit 2
PY=$(resolve_python) || exit 2
R=${1:?repo root}; S=${2:?scratch dir}; step=${3:?step}
mkdir -p "$S" || exit 2
# The shell's own spelling of the scratch dir: ac3 puts a directory under it on PATH, and a `C:/`
# spelling splits there at the drive colon, so the stub is never found and the ticker never ends.
S=$(cd "$S" && pwd) || exit 2
arm_fork_load() { LOADP=(); local k; for k in 1 2 3 4 5 6 7 8 9 10 11 12; do ( while :; do /usr/bin/true; done ) & LOADP+=($!); done; }
remove_fork_load() { kill "${LOADP[@]}" 2>/dev/null; wait "${LOADP[@]}" 2>/dev/null; }

case "$step" in
ac1)
  # The break: one line ahead of the walk that slices the whole prefix and scans it per quote,
  # which is the shape the walk replaced.
  B='  if (!/([A-Za-z_$][\w$]*)$/.test(line.slice(0, p + 1))) return false' \
    awk '/^  let s = p\r?$/ { print ENVIRON["B"] } { print }' "$R/tools/hooks/agent-cap.js" > "$S/broken-cap.js"
  cmp -s "$S/broken-cap.js" "$R/tools/hooks/agent-cap.js" && { echo "the staged break matched nothing"; exit 2; }
  build_payload() { "$PY" -c "
import json, sys
n = 8000; j = (',' + chr(10)) if sys.argv[1] == 'nl' else ','
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': 'const x = [' + j.join(\"f(a%d, void 'lit%d')\" % (i, i) for i in range(n)) + ']'}}))
" "$1"; }
  one=$(build_payload one); ctl=$(build_payload nl)
  measure_hook() { # label hook
    local c0 c1 c2 crc orc cms oms lim v
    c0=${EPOCHREALTIME//[.,]/}
    printf '%s' "$ctl" | node "$2" >/dev/null 2>&1; crc=$?
    c1=${EPOCHREALTIME//[.,]/}
    printf '%s' "$one" | node "$2" >/dev/null 2>&1; orc=$?
    c2=${EPOCHREALTIME//[.,]/}
    cms=$(( (10#$c1 - 10#$c0) / 1000 )); oms=$(( (10#$c2 - 10#$c1) / 1000 )); lim=$(( 4 * cms + 2000 ))
    if [ "$crc" != 0 ] || [ "$orc" != 0 ]; then v="FAIL (exit)"; elif [ "$oms" -le "$lim" ]; then v=ok; else v="FAIL (ratio)"; fi
    echo "ac1 $1: $v · one line ${oms} ms · one per line ${cms} ms · limit ${lim} ms · exits $orc/$crc"
  }
  measure_hook "shipped, quiet" "$R/tools/hooks/agent-cap.js"
  measure_hook "restored copy, quiet" "$S/broken-cap.js"
  arm_fork_load
  measure_hook "shipped, 12 fork loops" "$R/tools/hooks/agent-cap.js"
  measure_hook "restored copy, 12 fork loops" "$S/broken-cap.js"
  remove_fork_load; rm -f "$S/broken-cap.js" ;;
ac3)
  # The break: the nonce read through `cat` and the time through `ts_now`, as before the unit.
  awk '/^      _cur=""; \{ IFS= read -r _cur < "\$_d\/nonce"; \} 2>\/dev\/null\r?$/ {
         print "      [ \"$(cat \"$_d/nonce\" 2>/dev/null)\" = \"$_n\" ] || exit 0"; getline; next }
       { i = index($0, "${EPOCHSECONDS:-$(ts_now)}"); if (i) $0 = substr($0, 1, i - 1) "$(ts_now)" substr($0, i + 26) }
       { print }' "$R/tools/run-gates/run-gates.sh" > "$S/broken-rg.sh"
  [ "$(grep -c 'cat "$_d/nonce"\|"$(ts_now)" > "$_d/heartbeat.tmp"' "$S/broken-rg.sh")" = 2 ] || { echo "the staged break matched nothing"; exit 2; }
  measure_tick() { # label run-gates.sh — the arm's own block, with its scratch moved under $S
    local tk6=$S/tick6 t6s t6e body6 period6 ttl6 long6
    rm -rf "$tk6"; mkdir -p "$tk6/b" "$tk6/bin"; printf '%s' tick > "$tk6/b/nonce"
    sed -n '/^ts_now()/p;/^ts_alive()/p;/^ts_tick_start() {/,/^}$/p' "$2" > "$tk6/fn.sh"
    printf '%s\n' '#!/bin/bash' \
      'd=${0%/bin/sleep}; k=0; { read -r k < "$d/count"; } 2>/dev/null; k=$((k + 1)); printf "%s\n" "$k" > "$d/count"' \
      '[ "$k" -le 10 ] || { printf "%s\n" "${EPOCHREALTIME//[.,]/}" > "$d/end"; printf x > "$d/b/nonce"; }' > "$tk6/bin/sleep"
    chmod +x "$tk6/bin/sleep"
    grep -q '^ts_tick_start() {' "$tk6/fn.sh" && (
      . "$tk6/fn.sh" || exit 1
      TS_DIR=$tk6/b; TS_NONCE=tick; TS_TICK_EVERY=1; TS_TTL=6
      printf '%s\n' "${EPOCHREALTIME//[.,]/}" > "$tk6/start"
      PATH="$tk6/bin:$PATH" ts_tick_start || exit 1
      _w6=0; while [ ! -s "$tk6/end" ] && [ "$_w6" -lt 600 ] && kill -0 "${TS_TICK_PID:-none}" 2>/dev/null; do sleep 0.1; _w6=$((_w6 + 1)); done
    ) >/dev/null 2>&1
    t6s=""; t6e=""
    { read -r t6s < "$tk6/start"; read -r t6e < "$tk6/end"; } 2>/dev/null
    if grep -q '^ts_tick_start() {' "$tk6/fn.sh" && [ -n "$t6s" ] && [ -n "$t6e" ]; then
      body6=$(( (10#$t6e - 10#$t6s) / 10000 )); period6=$(( 1000 + body6 ))
      ttl6=$(( (3 * period6 + 999) / 1000 )); [ "$ttl6" -ge 6 ] || ttl6=6; long6=$(( ttl6 + 8 ))
      echo "ac3 $1: one tick ${period6} ms (${body6} ms of it the body) · TTL ${ttl6} s · leg ${long6} s"
    else
      echo "ac3 $1: no measured period"
    fi
    rm -rf "$tk6"
  }
  measure_tick "shipped, quiet" "$R/tools/run-gates/run-gates.sh"
  measure_tick "cat and date put back, quiet" "$S/broken-rg.sh"
  arm_fork_load
  measure_tick "shipped, 12 fork loops" "$R/tools/run-gates/run-gates.sh"
  measure_tick "cat and date put back, 12 fork loops" "$S/broken-rg.sh"
  remove_fork_load
  measure_tick "a file with no ticker" "$R/tools/run-gates/README.md"
  rm -f "$S/broken-rg.sh" ;;
ac5)
  sed -n '/^run_bounded() {/,/^}$/p' "$R/tools/unattended/unattended.sh" > "$S/rb_fn.sh"
  GATE_BOUND_LIVE=1; GATE_BOUND=2; ROOT=$S
  write_proc_record() { :; }
  . "$S/rb_fn.sh"
  run_marker_arms() { # label — the suite's two subject arms, markers under $S
    local m=$S/rb-marks p rc
    rm -rf "$m"; mkdir -p "$m"
    run_bounded bash -c 'sleep 60 & echo $! > "$1"; wait $! && : > "$2"' _ "$m/child.pid" "$m/child.done" >/dev/null 2>&1; rc=$?
    echo "ac5 $1 child: rc $rc · marker $([ -e "$m/child.done" ] && echo PRESENT || echo absent) at the return"
    p=""; { read -r p < "$m/child.pid"; } 2>/dev/null; [ -z "$p" ] || kill "$p" 2>/dev/null
    run_bounded bash -c '( sleep 60 & echo $! > "$1"; wait $! && : > "$2" ) & exit 0' _ "$m/grand.pid" "$m/grand.done" >/dev/null 2>&1
    echo "ac5 $1 grandchild: marker $([ -e "$m/grand.done" ] && echo PRESENT || echo absent) at the return"
    p=""; { read -r p < "$m/grand.pid"; } 2>/dev/null; [ -z "$p" ] || kill "$p" 2>/dev/null
    command sleep 1; echo "ac5 $1 after the kills: child marker $([ -e "$m/child.done" ] && echo PRESENT || echo absent)"
  }
  t0=$EPOCHSECONDS; run_marker_arms shipped; echo "ac5 shipped arms took $((EPOCHSECONDS - t0)) s"
  m=$S/rb-marks
  _ctl=$(timeout -k 5s 2 bash -c '( sleep 30 & wait $! && : > "$1" ) & exit 0' _ "$m/ctl.done" 2>&1)
  echo "ac5 control: marker $([ -e "$m/ctl.done" ] && echo PRESENT || echo absent) at the return"
  run_bounded() { RB_OUT=$(timeout -k 5s "$GATE_BOUND" "$@" 2>&1); }
  t0=$EPOCHSECONDS; run_marker_arms "pipe-captured bound"; echo "ac5 pipe-captured arms took $((EPOCHSECONDS - t0)) s"
  rm -rf "$m" "$S/rb_fn.sh" ;;
ac6)
  RT_HANG=120
  eval "$(sed -n '/^derive_winpid() {/,/^}$/p;/^read_task_gone() {/,/^}$/p' "$R/tools/unattended/resume-tick.test.sh")"
  type read_task_gone >/dev/null 2>&1 && type derive_winpid >/dev/null 2>&1 || { echo "the extraction found no function"; exit 2; }
  sleep 300 & a=$!; sleep 300 & b=$!
  wa=$(derive_winpid "$a"); wb=$(derive_winpid "$b")
  taskkill //F //PID "$wa" >/dev/null 2>&1
  t0=$EPOCHSECONDS; ra=$(read_task_gone "$wa"); echo "ac6 killed: read $ra after $((EPOCHSECONDS - t0)) s"
  t0=$EPOCHSECONDS; rb=$(read_task_gone "$wb"); echo "ac6 never killed: read $rb after $((EPOCHSECONDS - t0)) s"
  taskkill //F //PID "$wb" >/dev/null 2>&1; kill "$a" "$b" 2>/dev/null; wait 2>/dev/null ;;
ac8)
  d=$S/ac8; rm -rf "$d"; mkdir -p "$d/repo"; git -C "$d/repo" init -q
  sed 's/\[ "\$CARD_VERB" = append \] || \[ -n "\$CARD_SID" \] || \[ -t 0 \] || sid=/[ "$CARD_VERB" = append ] || [ -t 0 ] || sid=/' \
    "$R/skills/session-kickoff/manifest-check.sh" > "$d/broken.sh"
  cmp -s "$d/broken.sh" "$R/skills/session-kickoff/manifest-check.sh" && { echo "the staged break matched nothing"; exit 2; }
  mkfifo "$d/openstdin"; exec 9<>"$d/openstdin"
  for c in "$R/skills/session-kickoff/manifest-check.sh" "$d/broken.sh"; do
    t0=$EPOCHSECONDS
    (cd "$d/repo" && timeout 120 bash "$c" --card --path --session "ac8-t9s" <&9 > "$d/out" 2>&1); got=$?
    echo "ac8 ${c##*/}: exit $got after $((EPOCHSECONDS - t0)) s · $(grep -c 'orientation/ac8-t9s.md' "$d/out") path line(s)"
  done
  exec 9>&-; rm -rf "$d" ;;
*) echo "unknown step: $step"; exit 2 ;;
esac

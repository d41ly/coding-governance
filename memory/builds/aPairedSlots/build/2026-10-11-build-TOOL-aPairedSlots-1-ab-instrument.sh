#!/usr/bin/env bash
# **Serves:** journal TOOL-aPairedSlots-1
# The two-bar A/B behind node a's `slots` value. Three arms, each a pair of FULL bars
# (`GATE_FULL=1`, self-tests held as the default bar holds them) over two frozen clones of one base:
#
#   A  serial      bar 1 then bar 2, each at the profile's own width
#   B  concurrent  both at once, each at half the profile's width (`GATE_JOBS`)
#   C  concurrent  both at once, each at the profile's own width
#
# The metric is the owner's: MAKESPAN, the seconds from the first bar's start until both have
# finished, plus each bar's own wall. A bar's finish is its exit, green or red; the verdicts are
# recorded beside the times so a red arm is never read as a fast one.
#
# EVERY BAR PROVES IT RAN ITS LEGS. A bar's `GATE ok` plus `GATE FAIL` lines must equal the legs its
# clone's manifest does not hold (the runner's own held predicate: subject `kit` or chunk
# `selftests`), and its run record must carry a verdict file. A bar that fails either is marked
# `proof=NO` and its arm-run is void, whatever its exit code says.
#
# THE TWO CLONES ARE SEPARATE REPOSITORIES, deliberately: this measures what the legs cost when two
# bars share the host, not what two bars do to one common dir's shared files. The second question is
# TOOL-aPairedSlots-5's, and its own check runs two worktrees of ONE repository.
#
# A QUIET HOST AND A HELD TURNSTILE. Before each arm-run the plan waits until no bar outside this
# instrument's own tree is running, bounded by QUIET_MAX seconds, and then runs the arm under the
# clone runner's `--hold`, so a bar from a runner that knows the host turnstile queues instead of
# joining (owner, 2026-10-11: hold per arm-run). A sampler writes the host's load every SAMPLE_EVERY
# seconds for the whole arm-run: foreign bars, all bash processes, `/proc/loadavg` and the CPU
# reading `typeperf` gives. Contamination is RECORDED, never silently excluded.
#
# Usage, all paths forward-slashed:
#   ab-instrument.sh init <root> <source-repo> <base-sha>  two frozen clones and a frozen bare remote
#   ab-instrument.sh plan <root> <order>                    e.g. "A1 B1 C1 C2 B2 A2", each quiet+held
#   ab-instrument.sh arm  <root> <arm> <rep>                one arm-run, normally under --hold
# Results land in <root>/results.tsv (one row per bar, then one per arm-run) and <root>/samples.tsv.
set -u

QUIET_MAX=${QUIET_MAX:-7200}
SAMPLE_EVERY=${SAMPLE_EVERY:-60}
SELF=$(cd "$(dirname "$0")" && pwd)/$(basename "$0")

print_err() { printf 'ab: %s\n' "$*" >&2; }

# The legs a full bar runs: every manifest row the runner does not hold. The runner's predicate is
# `subjects[i] = kit || chunks[i] = selftests` with GATE_SELFTESTS unset, read from the CLONE's own
# manifest so a manifest that moved between bases cannot be graded against another's count.
measure_expected_legs() { # clone -> stdout: the count
  python -c '
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
print(sum(1 for l in d if not (l.get("subject") == "kit" or l.get("chunk") == "selftests")))
' "$1/tools/gate-legs.json"
}

cmd_init() { # root source base
  local root=$1 src=$2 base=$3 c
  mkdir -p "$root" || return 1
  [ -e "$root/remote.git" ] && { print_err "init: $root/remote.git exists; pick a fresh root"; return 1; }
  # FROZEN BY PINNING, NOT BY DELETING: a bare remote advertising exactly `main` at the base, so a
  # leg that reads the default branch reads a value, not an absence. No hook runs on a fetch.
  git init -q --bare "$root/remote.git" || return 1
  git -C "$root/remote.git" fetch -q --no-tags "$src" "$base:refs/heads/main" || return 1
  git -C "$root/remote.git" symbolic-ref HEAD refs/heads/main
  for c in c1 c2; do
    git clone -q --no-hardlinks "$root/remote.git" "$root/$c" || return 1
    # The local config the gov tree's own checks read; copied, never invented.
    git -C "$src" config --local --get-regexp '^(merge\.|core\.hookspath)' 2>/dev/null \
      | while read -r k v; do git -C "$root/$c" config "$k" "$v"; done
  done
  printf 'base\t%s\nsource\t%s\nexpected_legs\t%s\n' "$(git -C "$root/c1" rev-parse HEAD)" "$src" \
    "$(measure_expected_legs "$root/c1")" > "$root/init.tsv"
  printf 'arm\trep\tbar\twidth\tstart\tend\twall\trc\tverdict\tok\tfail\texpected\tproof\tqueued_from\tpauses\tlast\n' > "$root/results.tsv"
  printf 'epoch\tarm\trep\tforeign_bars\tbash_procs\tloadavg\tcpu_pct\tmem_free_kb\n' > "$root/samples.tsv"
  cat "$root/init.tsv"
}

# Bars this instrument did not start: every run-gates.sh process whose ppid chain does not reach
# the arm-run's own pid, and which is not one of that pid's ANCESTORS — the `--hold` runner the arm
# runs under is a run-gates.sh process and the arm's parent, not a foreign bar. A pid table that
# errs can only over-count, which only marks contamination.
scan_foreign_bars() { # own-pid -> stdout: the count
  local own=$1 n=0 p q depth anc=" "
  q=$own; depth=0
  while [ -n "$q" ] && [ "$q" != 1 ] && [ "$depth" -lt 40 ]; do
    anc="$anc$q "; q=$(cat "/proc/$q/ppid" 2>/dev/null) || q=""; depth=$((depth+1))
  done
  for p in $(ps -ef 2>/dev/null | awk '/run-gates\.sh/ && !/awk/ {print $2}'); do
    case "$anc" in *" $p "*) continue ;; esac
    q=$p; depth=0
    while [ -n "$q" ] && [ "$q" != 1 ] && [ "$depth" -lt 40 ]; do
      [ "$q" = "$own" ] && break
      q=$(cat "/proc/$q/ppid" 2>/dev/null) || q=""
      depth=$((depth+1))
    done
    [ "$q" = "$own" ] || n=$((n+1))
  done
  printf '%s\n' "$n"
}

run_sampler() { # root arm rep own-pid -> appends rows every SAMPLE_EVERY seconds until own-pid exits
  local root=$1 arm=$2 rep=$3 own=$4 cpu la mf bp fb
  while kill -0 "$own" 2>/dev/null; do
    fb=$(scan_foreign_bars "$own")
    bp=$(ps -W 2>/dev/null | grep -c '/usr/bin/bash')
    la=$(cut -d' ' -f1 /proc/loadavg 2>/dev/null)
    mf=$(awk '/^MemFree:/ {print $2}' /proc/meminfo 2>/dev/null)
    cpu=$(typeperf '\Processor(_Total)\% Processor Time' -sc 1 2>/dev/null | sed -n 3p | cut -d, -f2 | tr -d '"\r')
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$(date +%s)" "$arm" "$rep" "$fb" "$bp" "${la:--}" "${cpu:--}" "${mf:--}" >> "$root/samples.tsv"
    sleep "$SAMPLE_EVERY"
  done
}

# One bar, foreground. Writes <root>/out/<arm><rep>-<bar>.{log,start,end,rc}.
run_bar() { # root arm rep bar width-or-empty
  local root=$1 arm=$2 rep=$3 bar=$4 w=$5 o
  o="$root/out/$arm$rep-$bar"
  date +%s > "$o.start"
  if [ -n "$w" ]; then
    (cd "$root/$bar" && GATE_FULL=1 GATE_JOBS=$w bash tools/run-gates/run-gates.sh) > "$o.log" 2>&1
  else
    (cd "$root/$bar" && GATE_FULL=1 bash tools/run-gates/run-gates.sh) > "$o.log" 2>&1
  fi
  echo $? > "$o.rc"
  date +%s > "$o.end"
}

# The row for one finished bar, with its proof. The run record is the newest under the clone's git
# dir: one bar runs per clone per arm-run, so the newest is this one.
measure_bar() { # root arm rep bar -> appends a results row, stdout: the wall
  local root=$1 arm=$2 rep=$3 bar=$4 o s e rc ok fail exp proof rec w qf pz last verdict
  o="$root/out/$arm$rep-$bar"
  s=$(cat "$o.start"); e=$(cat "$o.end"); rc=$(cat "$o.rc")
  ok=$(grep -c '^GATE ok ' "$o.log"); fail=$(grep -c '^GATE FAIL ' "$o.log")
  exp=$(awk -F'\t' '$1=="expected_legs" {print $2}' "$root/init.tsv")
  rec=$(ls -td "$root/$bar/.git/gate-run"/*/ 2>/dev/null | head -1)
  verdict=$(cat "${rec}verdict" 2>/dev/null | head -1); verdict=${verdict:--}
  w=$(awk -F'\t' '$1=="width" {print $2}' "${rec}header" 2>/dev/null)
  qf=$(awk -F'\t' '$1=="queued_from" {print $2}' "${rec}header" 2>/dev/null)
  pz=$(grep -c . "${rec}pauses" 2>/dev/null); pz=${pz:-0}
  last=$(grep '^gates ' "$o.log" | tail -1 | tr '\t' ' ' | cut -c1-120)
  proof=NO
  [ "$((ok + fail))" = "$exp" ] && [ "$verdict" != - ] && proof=yes
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$arm" "$rep" "$bar" "${w:--}" "$s" "$e" \
    "$((e - s))" "$rc" "$verdict" "$ok" "$fail" "$exp" "$proof" "${qf:--}" "$pz" "${last:--}" >> "$root/results.tsv"
}

cmd_arm() { # root arm rep
  local root=$1 arm=$2 rep=$3 full half p1 p2 sp s0 e1 e2 mk proofs
  mkdir -p "$root/out"
  full=$(cd "$root/c1" && bash tools/run-gates/run-gates.sh --print-profile 2>/dev/null | awk -F'\t' '$1=="width" {print $2}')
  case "$full" in ''|*[!0-9]*) print_err "arm: the profile printed no width"; return 1 ;; esac
  half=$(( full / 2 )); [ "$half" -ge 1 ] || half=1
  run_sampler "$root" "$arm" "$rep" "$$" & sp=$!
  s0=$(date +%s)
  case "$arm" in
    A) run_bar "$root" A "$rep" c1 ""; run_bar "$root" A "$rep" c2 "" ;;
    B) run_bar "$root" B "$rep" c1 "$half" & p1=$!; run_bar "$root" B "$rep" c2 "$half" & p2=$!; wait "$p1" "$p2" ;;
    C) run_bar "$root" C "$rep" c1 "" & p1=$!; run_bar "$root" C "$rep" c2 "" & p2=$!; wait "$p1" "$p2" ;;
    *) print_err "arm: no arm '$arm'"; kill "$sp" 2>/dev/null; return 1 ;;
  esac
  kill "$sp" 2>/dev/null
  measure_bar "$root" "$arm" "$rep" c1; measure_bar "$root" "$arm" "$rep" c2
  e1=$(cat "$root/out/$arm$rep-c1.end"); e2=$(cat "$root/out/$arm$rep-c2.end")
  mk=$(( (e1 > e2 ? e1 : e2) - s0 ))
  proofs=$(awk -F'\t' -v a="$arm" -v r="$rep" '$1==a && $2==r && $3 ~ /^c[12]$/ {print $13}' "$root/results.tsv" | sort -u | tr '\n' ' ')
  printf '%s\t%s\tMAKESPAN\t%s\t%s\t%s\t%s\t-\t-\t-\t-\t-\t%s\t-\t-\t-\n' "$arm" "$rep" "$full/$half" "$s0" \
    "$(( e1 > e2 ? e1 : e2 ))" "$mk" "${proofs% }" >> "$root/results.tsv"
  printf 'arm %s rep %s makespan %ss proof %s\n' "$arm" "$rep" "$mk" "${proofs% }"
}

check_quiet() { # root -> rc 0 once no foreign bar runs, 1 after QUIET_MAX seconds
  local root=$1 t0 n
  t0=$(date +%s)
  while :; do
    n=$(scan_foreign_bars "$$")
    [ "$n" = 0 ] && return 0
    [ $(( $(date +%s) - t0 )) -ge "$QUIET_MAX" ] && { print_err "quiet: $n foreign bar(s) still running after ${QUIET_MAX}s; running anyway, recorded"; return 1; }
    sleep 60
  done
}

cmd_plan() { # root order
  local root=$1 order=$2 step arm rep q v
  # No bar knob of the calling shell reaches an arm: each arm sets the two it means, and the hold
  # exports the holder nonce itself.
  for v in $(compgen -v GATE_); do unset "$v"; done
  for step in $order; do
    arm=${step%?}; rep=${step#?}
    q=quiet; check_quiet "$root" || q=noisy
    printf '%s\t%s\t%s\tQUIET\t%s\n' "$(date +%s)" "$arm" "$rep" "$q" >> "$root/plan.log"
    # The hold is the clone runner's: it takes the host turnstile like a bar and runs this arm with
    # GATE_TURNSTILE_HOLDER exported, so both of the arm's bars NEST rather than queue behind it.
    (cd "$root/c1" && bash tools/run-gates/run-gates.sh --hold -- bash "$SELF" arm "$root" "$arm" "$rep") >> "$root/plan.log" 2>&1
    printf '%s\t%s\t%s\tDONE\trc %s\n' "$(date +%s)" "$arm" "$rep" "$?" >> "$root/plan.log"
  done
  printf '%s\tPLAN\tDONE\n' "$(date +%s)" >> "$root/plan.log"
}

main() {
  local verb=${1:-}; shift || true
  case "$verb" in
    init) cmd_init "$@" ;;
    plan) cmd_plan "$@" ;;
    arm)  cmd_arm "$@" ;;
    *) print_err "usage: init <root> <source-repo> <base> | plan <root> <order> | arm <root> <arm> <rep>"; return 2 ;;
  esac
}
main "$@"

#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# The full bar green at the push boundary; earlier runs scoped. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo.
#   bash tools/run-gates.sh                # legs run CONCURRENTLY, width min(8, nproc)
#   GATE_JOBS=1 bash tools/run-gates.sh    # one worker — the serial bar, through this same pool
# Legs live in tools/gate-legs.json (single source); this runner is a thin iterator over it.
#
# Legs run through a bounded worker pool. They are safe to run together
# because each heavy leg is already hermetic — it builds its own `mktemp -d` scratch repo, sets git
# config only inside it, and never writes into the real tree. Execution order is a scheduling detail;
# REPORTING is always manifest order, so the output is byte-stable whatever the width.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/tools/lib/resolve-python.sh"
PYBIN=$(resolve_python) || { echo "run-gates: no usable python — required to parse tools/gate-legs.json"; exit 2; }
fails=0; n=0; skips=0

# Baseline for conditional legs: the mainline tip we gate against. Override with GATE_BASE.
# Unresolvable (no remote / shallow / detached) → empty, and changed() fails safe to "run".
DEFBR=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null); DEFBR=${DEFBR#origin/}
BASE=$(git rev-parse --verify -q "${GATE_BASE:-origin/${DEFBR:-main}}" 2>/dev/null) || BASE=
changed() { [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

gd="$(git rev-parse --git-dir 2>/dev/null)"; sfile=""; TIMINGS=""
[ -n "$gd" ] && { sfile="$gd/gate-last-summary.txt"; TIMINGS="$gd/gate-timings.tsv"; }

# Pool width. 8 is MEASURED, not guessed: at width 16 each leg dilates under load faster than the
# extra worker repays, so wall clock is the longest leg either way. A non-numeric or <1 value is
# clamped to 1 rather than refused — this knob only schedules work, it can never skip a leg.
cores=$(nproc 2>/dev/null) || cores=${NUMBER_OF_PROCESSORS:-4}
case "$cores" in ''|*[!0-9]*) cores=4 ;; esac
JOBS=${GATE_JOBS:-$(( cores < 8 ? cores : 8 ))}
# Bound by LENGTH before any numeric test touches the value. Both `[ "$JOBS" -lt 1 ]` and `$(( JOBS < 1 ))`
# ERROR on an int64 overflow instead of comparing, so a 20-digit value used to sail past the clamp into a
# dispatch loop whose own `[ "$(live)" -lt "$JOBS" ]` errored identically: the runner spun forever having
# executed ZERO legs and printed no verdict, which on the push boundary is a hang rather than a red.
# `:-` substitutes the default for null as well as unset, so JOBS is never empty and an '' alternative here
# would be dead — the arm that "covered" it was measuring the default width, not the clamp.
case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac
[ "$JOBS" -lt 1 ] && JOBS=1

WORK=$(mktemp -d) || { echo "run-gates: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$WORK"' EXIT

# Read the leg manifest as name<RS>guard(comma-joined)<RS>argv(joined by <US>) per line, where
# RS=\x1e and US=\x1f (non-whitespace, so an empty guard field survives `read`; a tab would collapse).
# Line 1 is the advisory DISPATCH ORDER: leg indices longest-first from the timing cache the previous
# run wrote. A leg the cache does not know scores 0 and sorts last; an absent or unreadable cache
# yields manifest order. It is a scheduling hint only — it can never change a verdict.
# Command-substitution surfaces a parse failure (a `< <()` process-sub would swallow it).
legs=$("$PYBIN" -c '
import json, os, sys
try:
    data = json.load(open("tools/gate-legs.json"))
except Exception as e:
    sys.stderr.write("parse error: %s\n" % e); sys.exit(3)
if not isinstance(data, list) or not data:
    sys.stderr.write("gate-legs.json empty or not a list\n"); sys.exit(3)
durs = {}
cache = sys.argv[1] if len(sys.argv) > 1 else ""
if cache and os.path.exists(cache):
    try:
        for line in open(cache, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 2: durs[p[0]] = float(p[1])
    except Exception:
        durs = {}          # a corrupt cache is a missing cache, never a failed run
order = sorted(range(len(data)), key=lambda i: -durs.get(data[i]["name"], 0.0))
rows = [" ".join(str(i) for i in order)]
rows += [l["name"] + "\x1e" + ",".join(l.get("guard", [])) + "\x1e" + "\x1f".join(l["argv"]) for l in data]
sys.stdout.buffer.write(("\n".join(rows) + "\n").encode())   # LF bytes (Windows text stdout is CRLF); \x1e field sep is non-whitespace so an empty guard field is preserved (a tab would collapse)
' "$TIMINGS") || { echo "run-gates: cannot parse tools/gate-legs.json"; exit 2; }

# Rows stay 1:1 with the manifest so the dispatch indices address the same legs the reader reports.
# An empty name is the drop-sentinel: kept in the arrays to hold the index, never run and never counted.
names=(); guards=(); argvs=(); ORDER=""; first=1
while IFS= read -r line; do
  if [ "$first" = 1 ]; then ORDER=$line; first=0; continue; fi
  IFS=$'\x1e' read -r nm gd_ av <<<"$line"
  names+=("$nm"); guards+=("$gd_"); argvs+=("$av")
done <<<"$legs"
total=${#names[@]}

# Guard evaluation runs SERIALLY and up front: it is a read-only `git diff` per guarded leg, and
# deciding before dispatch keeps the skip verdict independent of scheduling.
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  [ -z "${guards[$i]}" ] && continue
  IFS=, read -ra gp <<<"${guards[$i]}"
  changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"
done

runleg() { # leg index — writes .out, then .sec, then ATOMICALLY .rc (the completion signal)
  local i=$1 s e out rc
  local argv; IFS=$'\x1f' read -ra argv <<<"${argvs[$i]}"
  case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac   # the manifest stores the canonical python3; run under the resolved PYBIN
  s=$(date +%s%N)
  out=$("${argv[@]}" </dev/null 2>&1); rc=$?   # legs never read stdin — deny it so a stray reader can't hang the bar
  e=$(date +%s%N)
  printf '%s\n' "$out" > "$WORK/$i.out"
  printf '%s.%03d\n' "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))" > "$WORK/$i.sec"
  printf '%s' "$rc" > "$WORK/$i.rc.tmp" && mv -f "$WORK/$i.rc.tmp" "$WORK/$i.rc"
}

report_one() { # leg index — emits exactly the line the serial bar has always emitted
  local i=$1 rc
  n=$((n+1))
  if [ ! -f "$WORK/$i.rc" ]; then
    fails=$((fails+1)); printf 'GATE FAIL  %s (no result)\n' "${names[$i]}"
    FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]} (no result)"$'\n'; return
  fi
  rc=$(cat "$WORK/$i.rc")
  if [ "$rc" = skip ]; then
    skips=$((skips+1)); printf 'GATE skip  %s (unchanged vs %s)\n' "${names[$i]}" "${DEFBR:-baseline}"
  elif [ "$rc" = 0 ]; then printf 'GATE ok    %s\n' "${names[$i]}"
  else fails=$((fails+1)); printf 'GATE FAIL  %s (exit %d)\n' "${names[$i]}" "$rc"; sed 's/^/    /' "$WORK/$i.out"
       FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  ${names[$i]} (exit $rc)"$'\n'; fi   # TOOL-aLeasedGauntlet-1 S3: keep for the durable summary
}

# Dispatch and report from ONE shell, so this shell owns every worker and can BLOCK on `wait -n`
# rather than poll for results. That is not a style preference: a poll tick costs a `sleep` PROCESS,
# measured at ~75ms for a 50ms sleep on this platform, and an earlier revision that polled every 50ms
# spent ~317s of a 617s serial run doing nothing but spawning them.
# Dispatch order is the advisory longest-first hint; REPORTING walks the manifest, so a leg prints
# only once every leg before it has printed.
disp=($ORDER); ndisp=${#disp[@]}; di=0; next=0
live() { jobs -rp | wc -l; }
while [ "$next" -lt "$total" ]; do
  if [ -z "${names[$next]}" ]; then next=$((next+1)); continue; fi   # drop-sentinel: holds an index, never runs
  di_before=$di
  while [ "$di" -lt "$ndisp" ] && [ "$(live)" -lt "$JOBS" ]; do
    k=${disp[$di]}; di=$((di+1))
    { [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue   # sentinel, or already decided by the guard pass
    runleg "$k" &
  done
  if [ -f "$WORK/$next.rc" ]; then report_one "$next"; next=$((next+1)); continue; fi
  if [ "$(live)" -gt 0 ]; then wait -n 2>/dev/null || true; continue; fi
  # Nothing running. That is NOT yet evidence this leg has no result: `jobs -rp` counts only RUNNING
  # jobs, so a worker that finished between the file check and the count is invisible, and with
  # instant legs the pool can drain faster than the reader walks. Exhaust dispatch, reap everything,
  # and re-check before declaring a leg dead — an earlier revision skipped this and reported a
  # perfectly healthy leg as "(no result)" roughly one run in three.
  if [ "$di" -lt "$ndisp" ]; then
    # Nothing is running and legs remain. Normally the pass above dispatched one; if it dispatched
    # NOTHING, force one here so every iteration makes progress and the loop can never spin.
    # Falling through to the report instead would declare an UNDISPATCHED leg dead, and that is not
    # hypothetical: guarding on "did this pass advance?" did exactly that. The window is a worker
    # that is live when the dispatch pass looks (so nothing dispatches) and finished by the liveness
    # check (so nothing is waited on), and the timing cache makes it common by decoupling dispatch
    # order from manifest order — measured at 6 of 30 legs falsely reported, on the second run only,
    # because the first run is the one with no cache.
    if [ "$di" -eq "$di_before" ]; then
      k=${disp[$di]}; di=$((di+1))
      if [ -n "${names[$k]}" ] && [ ! -f "$WORK/$k.rc" ]; then runleg "$k" & fi
    fi
    continue
  fi
  wait                                     # everything dispatched and nothing running: reap, look once more
  [ -f "$WORK/$next.rc" ] && continue
  report_one "$next"; next=$((next+1))     # genuinely no result: report it, never hang
done
wait

# Feed the next run's dispatch order. Advisory: a failed write costs wall clock, never a verdict.
if [ -n "$TIMINGS" ]; then
  new="$WORK/timings.new"; merged="$WORK/timings.merged"; : > "$new"
  for ((i=0; i<total; i++)); do
    [ -z "${names[$i]}" ] && continue
    [ -f "$WORK/$i.sec" ] && printf '%s\t%s\n' "${names[$i]}" "$(cat "$WORK/$i.sec")" >> "$new"
  done
  # A guard-SKIPPED leg never enters runleg(), so it produces no .sec. Rewriting the file from this
  # run's rows alone therefore DELETED the cached duration of every skipped leg — and the runs where
  # guards fire are exactly the diff-scoped ones, so a scoped run blanked the dispatch hint the next
  # full run depends on. Carry forward any cached row this run did not measure. A leg dropped from the
  # manifest falls out on its own, because the python side keys the hint on the manifest's names.
  cp "$new" "$merged" 2>/dev/null || true
  [ -s "$TIMINGS" ] && awk -F'\t' 'NR==FNR{seen[$1]=1;next} !($1 in seen)' "$new" "$TIMINGS" >> "$merged" 2>/dev/null
  cp "$merged" "$TIMINGS" 2>/dev/null || true
fi

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
# TOOL-aLeasedGauntlet-1 S3: write the verdict + failing-leg rows to a durable file (worktree-safe
# gitdir) so a `| tail`/`Select-Object -Last N` can't discard which leg failed.
if [ "$fails" = 0 ]; then
  [ -n "$sfile" ] && printf 'gates GREEN — %s/%s legs passed%s\n' "$((n-skips))" "$((n-skips))" "$skipnote" >"$sfile" 2>/dev/null || true
  echo "gates GREEN — $((n-skips))/$((n-skips)) legs passed$skipnote"; exit 0
else
  [ -n "$sfile" ] && { printf '%s' "${FAILED_LEGS:-}" >"$sfile"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote" >>"$sfile"; } 2>/dev/null || true
  echo "gates RED — $fails/$n legs failed$skipnote"
  [ -n "$sfile" ] && echo "gate summary saved to $sfile"
  exit 1
fi

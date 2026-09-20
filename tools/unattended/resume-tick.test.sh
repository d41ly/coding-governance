#!/usr/bin/env bash
# Runnable check for resume-tick.sh — the OS-scheduled out-of-process resumer: one arm per decision
# of its table, every one over a scratch git repo with a STUB `claude` first on PATH.
# Run: bash tools/unattended/resume-tick.test.sh   (exit 0 = all pass)
#
# WITHHELD FROM THE BAR AND FROM ADOPTERS, like every suite in this kit (kit.toml `project-owned`):
# its subject is the tick's decision table, which moves only when this file's sibling moves.
# `run-unattended-gates.sh` enumerates it through its budget row; the main loop runs it at
# VERIFYING. A build pass never runs it whole — the pass observes each arm by running the tick over
# the arm's fixture directly from this file's sourced prologue (spec TOOL-aWokenSentinel-5 §6).
#
# WHAT THIS FILE DOES NOT CHECK, stated up front because a structural check reads as a semantic one
# to everybody who did not write it: it never runs the real `claude` — the stub answers `auth status`
# from STUB_LOGGED_IN and sleeps on `-p` — so whether the CLI accepts `--max-turns`, resumes the
# session, or honours the CONTINUE payload is measured nowhere here (spec §4 records the CLI
# measurement). It does not prove the tick is REGISTERED on any node (the adopter's --check INFO
# line reports that), and the POSIX arms of the kill and the detach are UNVERIFIED: no registered
# node is POSIX, and this suite runs where it runs.
#
# EVERY ARM DRIVES ITS OWN TREE. The tick keys on a worktree list, a conf, a run-state record and
# the tree's clocks, so every fixture is a scratch `git init` under a SHORT path — the scratchpad's
# is long enough to break a clone on Windows — carrying exactly those and never the real tree. The
# tick, the library and the driver are COPIED to a scratch kit dir, so the dead-probe arm can shadow
# the driver beside the tick without touching the kit under test.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# RESUME_TICK_TEST_TMP is the pass's seam: a unit pass runs one arm at a time from a sourced copy of
# this prologue and must put its scratch under the session scratchpad, not /tmp.
# RESUME_TICK_TEST_GITTMP is every fixture's: a `git init` wants a SHORT path on Windows.
TMP="${RESUME_TICK_TEST_TMP:-$(mktemp -d)}"
# POSIX-SPELLED, whatever the caller passed: the stub dir goes on PATH, and a `C:/…` element there
# splits at the drive colon into two directories that exist nowhere, so the REAL `claude` wins —
# measured on node `a` the first time this suite ran, on a scratchpad spelled by its drive letter.
TMP=$(cd "$TMP" && pwd)
GITTMP="${RESUME_TICK_TEST_GITTMP:-$TMP}"
pass=0; fail=0
print_ok()   { echo "ok   $1"; pass=$((pass+1)); }
print_bad()  { echo "FAIL $1"; fail=$((fail+1)); }
check_same() { if [ "$2" = "$3" ]; then print_ok "$1"; else print_bad "$1: expected [$3], got [$2]"; fi; }
check_hit()  { if grep -qF -- "$2" <<<"$1"; then print_ok "$3"; else print_bad "$3: missing [$2] in [$(printf '%s' "$1" | head -c 300)]"; fi; }
check_miss() { if grep -qF -- "$2" <<<"$1"; then print_bad "$3: unexpected [$2]"; else print_ok "$3"; fi; }

# THE KIT COPY: the tick, the library it sources and the driver it calls, nothing else.
KIT="$TMP/kit"; mkdir -p "$KIT"
cp "$HERE/resume-tick.sh" "$HERE/lib-unattended.sh" "$HERE/unattended.sh" "$KIT/"
TICK="$KIT/resume-tick.sh"
SID="11111111-2222-3333-4444-555555555555"
# THE TRANSCRIPT ROOT is pointed at an empty scratch directory for the whole suite, so the box's
# real transcripts are never one of `--liveness`'s four signals and `HOME` is untouched.
mkdir -p "$TMP/cfg-empty"; export CLAUDE_CONFIG_DIR="$TMP/cfg-empty"

# THE STUB `claude`, first on PATH: writes its argv and its own pid to STUB_LOG, answers
# `auth status` with `{"loggedIn": true}` or `false` from STUB_LOGGED_IN, and on `-p` sleeps 15 s
# then writes `done`. The log path is BAKED into the stub, because the launcher carries PATH and
# nothing else the arm exported. `(( $$ ))` is the stub's own pid: the arms that must wait for a
# launched stub to end kill it by that, so a green run leaves no sleeper behind.
STUB_LOG="$TMP/stub.log"
build_stub() {
  mkdir -p "$TMP/stub"
  {
    printf '#!/bin/sh\n'
    printf 'printf "pid %%s argv %%s\\n" "$$" "$*" >> %q\n' "$STUB_LOG"
    printf 'case "$1" in\n'
    printf '  auth) if [ "${STUB_LOGGED_IN:-true}" = false ]; then printf "{\\n  \\"loggedIn\\": false\\n}\\n"; else printf "{\\n  \\"loggedIn\\": true\\n}\\n"; fi ;;\n'
    printf '  -p) sleep 15; printf "done\\n" >> %q ;;\n' "$STUB_LOG"
    printf 'esac\nexit 0\n'
  } > "$TMP/stub/claude"
  chmod +x "$TMP/stub/claude"
}
build_stub
export PATH="$TMP/stub:$PATH"
# THE STUB MUST WIN BEFORE ANY ARM RUNS: a suite whose `claude` resolves to the real CLI would
# resume a real session from a fixture record, so this is a refusal and not an assertion.
case "$(command -v claude)" in
  "$TMP/stub/claude") ;;
  *) echo "resume-tick.test: REFUSED — claude resolves to $(command -v claude), not the stub under $TMP/stub, so an arm could reach the real CLI"; exit 2 ;;
esac

# remove_stubs — every stub `-p` still sleeping, by the pid it logged, then the log. Called by every
# fixture build, not only at exit: a stub launched by one arm writes `done` fifteen seconds later,
# into the log a later arm is asserting empty.
remove_stubs() {
  local p
  [ -f "$STUB_LOG" ] && for p in $(sed -n 's/^pid \([0-9]*\) argv -p .*/\1/p' "$STUB_LOG"); do kill "$p" 2>/dev/null; done
  rm -f "$STUB_LOG"
  return 0
}
# remove_leftovers — the stubs, the arm's own sleeper, then the scratch.
remove_leftovers() {
  remove_stubs
  [ -n "${SLEEP_PID:-}" ] && kill "$SLEEP_PID" 2>/dev/null
  rm -rf "$TMP"
  [ "$GITTMP" = "$TMP" ] || rm -rf "$GITTMP/rt-fx"
  return 0
}
trap remove_leftovers EXIT

# build_fixture <pid-fact> [session-fact] -> FX, a scratch repo: the driver suite's mkconf shape
# plus RESUME_STALE_BOUND="1" and NEITHER resume knob (the NOTE arm wants the default announced),
# a tRun build README, a RUN.md at BUILDING carrying the session and the pid, ONE commit dated an
# hour ago so a clean tree reads STALE against the one-second bound and a "line newer than the
# last move" is any line dated now. Null global and system git config, the kit's seed idiom.
build_fixture() {
  FX="$GITTMP/rt-fx"; rm -rf "$FX"; mkdir -p "$FX/memory/builds/tRun"
  ( cd "$FX" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false ) || { echo "FAIL fixture: git init failed under $FX"; exit 2; }
  # RE-SPELLED BY GIT: the tick prints worktree paths as `git worktree list` spells them, and on
  # Windows that is the long name of a directory this file may have reached by its 8.3 short one.
  FX=$( cd "$FX" && git rev-parse --show-toplevel )
  cat > "$FX/.unattended.conf" <<'EOF'
MEMORY_ROOT=memory
UNITS_REGION_CUTOFF="2026-08-19"
LANDER="echo land"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
GATE_BOUND="3600"
UNIT_STALL_BOUND="1800"
REVIEW_ROUNDS="7"
RESUME_STALE_BOUND="1"
WIRING_CHECK="true"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA=""
DOD_EXTRA=""
EOF
  printf -- '---\nslug: tRun\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-tRun-1\n---\n\n# tRun\n' > "$FX/memory/builds/tRun/README.md"
  printf '# tRun — run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n## Run facts\nwitness: abc\nphase: BUILDING\nsession: %s\npid: %s\n\n## Parked\n' "${2:-$SID}" "$1" > "$FX/memory/builds/tRun/RUN.md"
  ( cd "$FX" && GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null git add -A \
      && GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_COMMITTER_DATE="$(( $(date -u +%s) - 3600 )) +0000" \
         git commit -q -m fixture ) || { echo "FAIL fixture: the commit did not land in $FX"; exit 2; }
  remove_stubs
  FX_GITDIR=$( cd "$FX" && git rev-parse --absolute-git-dir )
  SIDECAR="$FX_GITDIR/unattended"
}
# run_tick_over <tick> [args] — OUT, ERR, RC and SECS are what the tick did; SECS is the wall it took.
run_tick_over() {
  local t="$1" t0; shift; t0=$(date +%s)
  OUT=$(bash "$t" --repo "$FX" "$@" 2>"$TMP/err"); RC=$?; ERR=$(cat "$TMP/err"); SECS=$(( $(date +%s) - t0 ))
}
# read_stub_log — the log once the launched stub has started, polled up to ten seconds because
# the launch is detached and the child starts after the tick returned; empty when it never came.
read_stub_log() {
  local i; for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
    [ -s "$STUB_LOG" ] && grep -q 'argv -p' "$STUB_LOG" && break; sleep 0.5
  done
  cat "$STUB_LOG" 2>/dev/null || true
}
# seed_log <n> <utc> — n attempt lines in the sidecar, all stamped <utc>.
seed_log() {
  local i; mkdir -p "$SIDECAR"
  for i in $(seq 1 "$1"); do printf '%s attempt %s session %s pid 999999999 pid-alive no out %s/resume.tRun.%s.out\n' "$2" "$i" "$SID" "$SIDECAR" "$i"; done >> "$SIDECAR/resume.tRun.log"
}
NOW_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
OLD_UTC=$(date -u -d "@$(( $(date -u +%s) - 7200 ))" +%Y-%m-%dT%H:%M:%SZ)
UTC_RE='^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z '

# ---- AC8: a root that is not a git repository is REFUSED naming the dir, exit 2; the kit dir is
# ---- derived from $0 and the tick spells no path outside its own directory.
mkdir -p "$TMP/notrepo"
OUT=$(bash "$TICK" --repo "$TMP/notrepo" 2>&1); RC=$?
check_same "AC8 a non-repo root exits 2" "$RC" "2"
check_hit "$OUT" "REFUSED — $TMP/notrepo is not a git repository, so there is no worktree list to walk" "AC8 the refusal names the dir"
check_same "AC8 the kit dir is derived from \$0" "$(grep -c 'dirname "$0"' "$HERE/resume-tick.sh")" "1"
check_same "AC8 the tick spells no kit path by literal" "$(grep -cE 'tools/(unattended|lib|memory-tree|run-gates)' "$HERE/resume-tick.sh")" "0"
# ...and a root with no conf is refused too, before any walk.
build_fixture 999999999; rm -f "$FX/.unattended.conf"
OUT=$(bash "$TICK" --repo "$FX" 2>&1); RC=$?
check_same "AC8 a root with no conf exits 2" "$RC" "2"
check_hit "$OUT" "carries no .unattended.conf, so the tick has no bounds to read" "AC8 the no-conf refusal"

# ---- AC7: --dry-run prints the decision it WOULD act on with ` (dry-run)` appended and does
# ---- nothing — no launch, no kill, no sidecar line, no launcher, no login probe; an empty walk is
# ---- an announced nothing at exit 0.
build_fixture 999999999
run_tick_over "$TICK" --dry-run
check_same "AC7 dry-run exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: tRun · $FX · resumed · attempt 1 · out $SIDECAR/resume.tRun." "AC7 dry-run prints the resumed decision"
check_same "AC7 the decision line ends (dry-run)" "$(printf '%s\n' "$OUT" | grep -c ' (dry-run)$')" "1"
check_same "AC7 dry-run invokes nothing" "$([ -f "$STUB_LOG" ] && echo invoked || echo nothing)" "nothing"
check_same "AC7 dry-run writes no sidecar line" "$([ -s "$SIDECAR/resume.tRun.log" ] && echo written || echo none)" "none"
check_same "AC7 dry-run writes no launcher" "$(ls "$SIDECAR"/resume.tRun.*.sh 2>/dev/null | grep -c '')" "0"
build_fixture 999999999 absent
run_tick_over "$TICK"
check_same "AC7 an empty walk exits 0" "$RC" "0"
check_same "AC7 an empty walk is announced" "$OUT" "resume-tick: no bound run in 1 worktree(s)"
# ...AC5's pass half: the two NOTEs name the root conf's path, a file that exists, once each.
check_same "AC5 the NOTE for RESUME_ATTEMPTS prints once" "$(printf '%s\n' "$ERR" | grep -c 'declares no RESUME_ATTEMPTS')" "1"
check_same "AC5 the NOTE for RESUME_TURNS prints once" "$(printf '%s\n' "$ERR" | grep -c 'declares no RESUME_TURNS')" "1"
NOTE_PATH=$(printf '%s\n' "$ERR" | sed -n 's/.*Declare one in \(.*\) to change it.*/\1/p' | head -n 1)
check_same "AC5 the NOTE names a file that exists" "$([ -n "$NOTE_PATH" ] && [ -f "$NOTE_PATH" ] && echo yes || echo no)" "yes"

# ---- AC2: a logged-out CLI is an ANNOUNCED skip at exit 0 — the stub saw `auth status` and no
# ---- `-p`, and no sidecar line was written; a LIVE record probes neither login nor the stub.
build_fixture 999999999
STUB_LOGGED_IN=false run_tick_over "$TICK"
check_same "AC2 logged-out exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: tRun · $FX · SKIP — the CLI is not logged in on this node; nothing can resume tRun" "AC2 the logged-out skip is announced"
check_same "AC2 the stub saw auth status" "$(grep -c 'argv auth status' "$STUB_LOG")" "1"
check_same "AC2 the stub saw no -p" "$(grep -c 'argv -p' "$STUB_LOG")" "0"
check_same "AC2 no sidecar line" "$([ -s "$SIDECAR/resume.tRun.log" ] && echo written || echo none)" "none"
mkdir -p "$FX_GITDIR/gate-logs" && touch "$FX_GITDIR/gate-logs/leg.log"; rm -f "$STUB_LOG"
run_tick_over "$TICK"
check_same "AC2 a LIVE record exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: tRun · $FX · skip · verdict LIVE" "AC2 a LIVE record is skipped by verdict"
check_same "AC2 a LIVE record consults neither login nor the stub" "$([ -f "$STUB_LOG" ] && echo invoked || echo nothing)" "nothing"

# ---- AC1: the STALE fixture with a dead recorded pid is RESUMED: one line ending in the .out path,
# ---- the tick back within 5 s while the stub still sleeps (the launch is DETACHED), the argv
# ---- carrying the session, the flag, the turns and the payload's first instruction, the sidecar
# ---- line stamped and counted, the launcher beside it.
build_fixture 999999999
run_tick_over "$TICK"
check_same "AC1 exits 0" "$RC" "0"
check_same "AC1 one decision line" "$(printf '%s\n' "$OUT" | grep -c '')" "1"
check_hit "$OUT" "resume-tick: tRun · $FX · resumed · attempt 1 · out $SIDECAR/resume.tRun." "AC1 the resumed decision line"
check_same "AC1 the tick returned within 5 s, so the launch is detached" "$([ "$SECS" -le 5 ] && echo yes || echo "no: ${SECS}s")" "yes"
LOG=$(read_stub_log)
check_hit "$LOG" "argv -p --resume $SID --dangerously-skip-permissions --max-turns 40 " "AC1 the stub was launched with the session, the flag and the turns"
check_miss "$LOG" "done" "AC1 the stub is still running when the tick has returned"
check_hit "$LOG" "--keepalive-id" "AC1 the payload carries its first instruction"
check_hit "$LOG" "/unattended.sh --resume tRun --keepalive-id" "AC1 the payload names the driver beside the tick — absolute here, because the scratch kit is outside the fixture root"
check_same "AC1 the stub saw auth status first" "$(head -n 1 "$STUB_LOG" | grep -c 'argv auth status')" "1"
check_same "AC1 one sidecar line" "$(grep -c '' "$SIDECAR/resume.tRun.log")" "1"
check_same "AC1 the sidecar line starts with a UTC stamp" "$(grep -cE "$UTC_RE" "$SIDECAR/resume.tRun.log")" "1"
check_hit "$(cat "$SIDECAR/resume.tRun.log")" " attempt 1 session $SID pid 999999999 pid-alive no out $SIDECAR/resume.tRun." "AC1 the sidecar line's fields"
check_same "AC1 the launcher exists beside the log" "$(ls "$SIDECAR"/resume.tRun.*.sh 2>/dev/null | grep -c '')" "1"
check_same "AC1 the launcher records the argv" "$(grep -c -- '--dangerously-skip-permissions --max-turns 40' "$SIDECAR"/resume.tRun.*.sh)" "1"
OUT_PATH=$(sed -n 's/.* out //p' "$SIDECAR/resume.tRun.log" | head -n 1)
check_same "AC1 the .out the line names is the one the launcher writes" "$(grep -c -- ">$OUT_PATH" "$SIDECAR"/resume.tRun.*.sh)" "1"

# ---- AC3: the cap is CONSECUTIVE, not lifetime. Six lines newer than the last move (the hour-old
# ---- commit) exhaust it and invoke nothing; six lines OLDER than it launch attempt 7, because a
# ---- move resets the count; five newer lines launch attempt 6.
build_fixture 999999999; seed_log 6 "$NOW_UTC"
run_tick_over "$TICK"
check_same "AC3 exhausted exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: tRun · $FX · skip · ATTEMPTS EXHAUSTED · last $NOW_UTC · out $SIDECAR/resume.tRun.6.out" "AC3 six newer lines exhaust the cap naming the last"
check_same "AC3 exhausted invokes nothing" "$([ -f "$STUB_LOG" ] && echo invoked || echo nothing)" "nothing"
check_same "AC3 exhausted writes no line" "$(grep -c '' "$SIDECAR/resume.tRun.log")" "6"
build_fixture 999999999; seed_log 6 "$OLD_UTC"
run_tick_over "$TICK"
check_hit "$OUT" "· resumed · attempt 7 · out " "AC3 six lines older than the last move launch attempt 7"
check_same "AC3 the seventh line landed" "$(grep -c ' attempt 7 ' "$SIDECAR/resume.tRun.log")" "1"
build_fixture 999999999; seed_log 5 "$NOW_UTC"
run_tick_over "$TICK"
check_hit "$OUT" "· resumed · attempt 6 · out " "AC3 five newer lines launch attempt 6"

# ---- AC4: a LIVE recorded pid is killed with its tree before the launch. The arm's own background
# ---- sleep, recorded by its WINDOWS pid under MSYS (ps's WINPID column, once the forked child has
# ---- exec'd into `sleep`) and by $! elsewhere; gone from tasklist / kill -0 afterwards.
sleep 300 & SLEEP_PID=$!
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*)
    WPID=""; for i in 1 2 3 4 5 6 7 8 9 10; do
      WPID=$(ps -p "$SLEEP_PID" | awk -v p="$SLEEP_PID" 'NR>1 && $1==p && $NF ~ /sleep/ {print $4}'); [ -n "$WPID" ] && break; sleep 0.5
    done ;;
  *) WPID=$SLEEP_PID ;;
esac
if [ -n "$WPID" ]; then
  build_fixture "$WPID"
  run_tick_over "$TICK"
  check_hit "$OUT" "· resumed · attempt 1 · out " "AC4 a live pid is still resumed"
  check_same "AC4 the stub was invoked" "$(read_stub_log | grep -c 'argv -p')" "1"
  check_hit "$(cat "$SIDECAR/resume.tRun.log")" " pid $WPID pid-alive yes out " "AC4 the sidecar line records pid-alive yes"
  case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) check_same "AC4 the sleep is gone from tasklist" "$(tasklist //FI "PID eq $WPID" 2>/dev/null | grep -c 'No tasks are running')" "1" ;;
    *) check_same "AC4 the sleep is gone" "$(kill -0 "$SLEEP_PID" 2>/dev/null && echo alive || echo gone)" "gone" ;;
  esac
else
  print_bad "AC4 fixture: no pid for the background sleep, so the kill arm would probe an empty value and prove nothing"
fi
kill "$SLEEP_PID" 2>/dev/null; wait "$SLEEP_PID" 2>/dev/null; SLEEP_PID=""

# ---- AC12: the two announced skips of the walk. A driver whose --liveness exits non-zero is a dead
# ---- probe: the run is skipped naming its first line, nothing launches, no line is written. A
# ---- second worktree with no conf is skipped by name while the first tree's run still gets its
# ---- decision line.
KIT2="$TMP/kit2"; mkdir -p "$KIT2"; cp "$TICK" "$KIT/lib-unattended.sh" "$KIT2/"
printf '#!/bin/sh\necho "UNATTENDED check 52 FAILED — the liveness cannot be measured on this node (stubbed)"\nexit 1\n' > "$KIT2/unattended.sh"
build_fixture 999999999
run_tick_over "$KIT2/resume-tick.sh"
check_same "AC12 a dead probe exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: tRun · $FX · liveness probe failed: UNATTENDED check 52 FAILED — the liveness cannot be measured on this node (stubbed)" "AC12 the dead probe is announced with its first line"
check_same "AC12 a dead probe launches nothing" "$([ -f "$STUB_LOG" ] && echo invoked || echo nothing)" "nothing"
check_same "AC12 a dead probe writes no line" "$([ -s "$SIDECAR/resume.tRun.log" ] && echo written || echo none)" "none"
build_fixture 999999999
WT2="$GITTMP/rt-wt2"; rm -rf "$WT2"
( cd "$FX" && git worktree add -q "$WT2" -b wt2 ) || print_bad "AC12 fixture: git worktree add failed"
WT2=$( cd "$FX" && git worktree list --porcelain | sed -n 's/^worktree //p' | sed -n 2p )
rm -f "$WT2/.unattended.conf"
run_tick_over "$TICK" --dry-run
check_same "AC12 a conf-less tree exits 0" "$RC" "0"
check_hit "$OUT" "resume-tick: $WT2 · skipped: no .unattended.conf in this worktree" "AC12 the conf-less tree is skipped by name"
check_hit "$OUT" "resume-tick: tRun · $FX · resumed · attempt 1" "AC12 the first tree's run still gets its decision line"
check_same "AC12 two lines, one per tree" "$(printf '%s\n' "$OUT" | grep -c '')" "2"
( cd "$FX" && git worktree remove --force "$WT2" ) >/dev/null 2>&1; rm -rf "$WT2"

n=$((pass+fail))
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Derived from
# the seven arm blocks each run ALONE from the sourced prologue on node a, 2026-09-20 (the pass that
# wrote this file may not run the suite): AC8 6, AC7 11, AC2 8, AC1 15, AC3 7, AC4 4, AC12 8 — 59
# executed, pinned at ~10% headroom. The main loop's first green at VERIFYING confirms the executed
# count against this floor. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=53
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; fail=$((fail+1)); }
echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ]

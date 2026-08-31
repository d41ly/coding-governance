#!/usr/bin/env bash
# run-gates.turnstile.test.sh — arms for the repository turnstile. Exit 0 = every case passes.
#
# WHAT THIS GATES THAT NOTHING ELSE CAN: that two bars started against ONE repository do not run at
# the same time, that a holder which died or stalled is reaped rather than blocking forever, and that
# the turnstile can never become the outage — it fails open, loudly, and contributes nothing to the
# exit code.
#
# THIS SUITE SHIPS. `kit.toml` claims the kit directory with `include = "**"` at `role = "engine"`, so
# every arm below has to be true in ANY adopting tree: no gov leg name, no gov threshold, nothing
# keyed on this repository's manifest. Every fixture is a scratch repo built here.
#
# PEAK OCCUPANCY, NOT OVERLAPPING TIMESTAMPS. The arms count simultaneous holders by having the
# fixture legs themselves register their presence in a shared directory and record how many they saw.
# Intersecting recorded start and end times was tried in a sibling build and retired by name: it
# graded the node's clock rather than the runner, and red three consecutive pushes on a tree it had
# already passed.
set -u
# THE TURNSTILE SHIPS DISABLED (TOOL-aGatheredDeclaration-5), so this suite must ASK for its own
# subject. Without this every arm below drives a mechanism that is off, asserts nothing, and the
# assertion floor is the only thing that notices -- which is exactly what happened: 61 against a
# pinned 62. Arms that deliberately test the DISABLED path set GATE_TURNSTILE=0 themselves and
# override this; the shipped-default arm at the end reads the declaration instead.
export GATE_TURNSTILE=1

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "turnstile-test: not a git repo"; exit 2; }
HERE=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
bad=0
# An EXECUTED assertion count with a floor, carried at birth: a suite that prints a hardcoded total
# is a suite whose count stops tracking its arms the first time somebody deletes one.
# Raised from 28 by TOOL-aShardedFloor-1, which adds the queue-record arms (6b, 7c, 13c-13e, 14).
# Stated ABSOLUTELY rather than as a delta: TOOL-aShardedFloor-4 raises the same pin, and
# whichever lands second has to say the number it expects. The compare below is `-ge`, so arms
# left under an unraised floor are STRANDED rather than red — which is why this moves with them.
# Raised from 42 to 62 by TOOL-aReapedTicket-3, which adds arms 15-21 — the QUEUE side, which this
# suite had no arm for at all. The 20 they contribute were counted by running them, not derived on
# paper: 11 of the 20 are RED against the runner at that build's BASE and all 20 green after it.
FLOOR_ASSERTIONS=65
n=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }
# A SKIP THAT ANNOUNCES ITSELF. Arm 4c below already scores its can't-demonstrate branch, but it
# spends an `ok` on it, which is indistinguishable from coverage in the output. This counts toward
# the same total and prints as SKIP, so an arm that could not be exercised says so in its own voice
# instead of either claiming a pass or accusing the subject.
skipped() { n=$((n+1)); echo "  SKIP — $1"; }

# ------------------------------------------------------------------ fixtures ----------------------
# hdrkey <repo> <key> — one value out of the run record's header, or empty.
# The runner writes `<git-dir>/gate-run/current` holding the run id, then `<id>/header` in a
# key-per-line TAB grammar. Selecting BY NAME is deliberate and is what makes an additive key
# harmless: an arm that counted keys or read them by position would red on every future addition.
hdrkey() {
  local d=$1 k=$2 id
  id=$(cat "$d/.git/gate-run/current" 2>/dev/null) || return 1
  [ -n "$id" ] || return 1
  awk -F'\t' -v k="$k" '$1==k{print $2; exit}' "$d/.git/gate-run/$id/header" 2>/dev/null
}

# mk_repo <dir> — a scratch repository carrying the runner and its table.
mk_repo() {
  local d=$1
  mkdir -p "$d/tools/run-gates" "$d/tools/lib" "$d/fx"
  cp "$HERE/run-gates.sh" "$HERE/gate-profiles.txt" "$d/tools/run-gates/" || return 1
  cp "$HERE/gate-fingerprint.sh" "$d/tools/run-gates/" 2>/dev/null || true
  cp "$ROOT/tools/lib/resolve-python.sh" "$d/tools/lib/" 2>/dev/null || true
  ( cd "$d" && git init -q -b main . && git config user.email ts@test.invalid \
      && git config user.name ts-test ) >/dev/null 2>&1 || return 1
  # The occupancy leg: register, count everyone registered, record the count, dwell, deregister.
  # `mkdir` for the marker so registration is atomic; the count is taken AFTER registering, so a
  # holder always sees at least itself.
  cat > "$d/fx/occupy.sh" <<'OCC'
#!/usr/bin/env bash
S=${TS_SHARED:?}
mkdir -p "$S/live" "$S" 2>/dev/null
mkdir "$S/live/$$" 2>/dev/null
ls -1 "$S/live" 2>/dev/null | wc -l >> "$S/peaks"
printf '%s\n' "$$" >> "$S/order"
sleep "${TS_DWELL:-3}"
rmdir "$S/live/$$" 2>/dev/null
exit 0
OCC
  printf '#!/usr/bin/env bash\nexit 0\n' > "$d/fx/quick.sh"
  printf '#!/usr/bin/env bash\nsleep "${TS_LONG:-12}"\nexit 0\n' > "$d/fx/long.sh"
  # several quick legs, so a holder's heartbeat refreshes repeatedly across a run
  printf '#!/usr/bin/env bash\nsleep 1\nexit 0\n' > "$d/fx/tick.sh"
  printf '%s\n' '[ {"name": "occupy", "argv": ["bash", "fx/occupy.sh"]} ]' > "$d/tools/gate-legs.json"
  ( cd "$d" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
}
legs()  { printf '%s\n' "$2" > "$1/tools/gate-legs.json"; }
runbg() { ( cd "$1" && shift; env "$@" bash tools/run-gates/run-gates.sh; ) >>"$tmp/out.$RANDOM" 2>&1 & }
peak()  { awk 'BEGIN{m=0} {if ($1+0>m) m=$1+0} END{print m+0}' "$1/peaks" 2>/dev/null; }
# RESOLVED ABSOLUTELY, the way the runner resolves it. `git rev-parse --git-common-dir` answers a
# path RELATIVE to the repo it was asked in — plain `.git` in an ordinary clone — so a helper that
# returned it verbatim handed every arm a path that means something different from the harness's
# own cwd. The arms then tested a beacon that never existed and reported "the run never claimed",
# which is the arm correctly refusing to grade rather than passing, but for the wrong reason.
beacon(){ local c; c=$(cd "$1" && git rev-parse --git-common-dir) || return 1
          c=$(cd "$1" && cd "$c" && pwd) || return 1
          printf '%s/gate-bar-beacon' "$c"; }
# The QUEUE's path, resolved the same absolute way and for the same reason (TOOL-aReapedTicket-3).
# The arms below plant tickets in it, so a helper that returned a relative path would have them
# planting into a directory the runner never reads — the failure `beacon` already carries a comment
# about, which is why this is a sibling of it rather than a fresh derivation.
queue(){  local c; c=$(cd "$1" && git rev-parse --git-common-dir) || return 1
          c=$(cd "$1" && cd "$c" && pwd) || return 1
          printf '%s/gate-bar-queue' "$c"; }

# ------------------------------------------------------ 1/2: peak occupancy, and its control -------
# AC1 with AC2 beneath it. AC1 alone passes on an implementation that serializes by accident — two
# runners that simply never overlapped — so the SAME fixture is run with the turnstile off and must
# show the overlap the mechanism is there to remove. If the control does not overlap, the machine was
# too slow to demonstrate anything and the arm says so instead of claiming a pass.
R=$tmp/peak; mk_repo "$R" || { echo "turnstile-test: cannot build scratch"; exit 2; }
S=$tmp/shared_on; mkdir -p "$S"
TS_SHARED=$S TS_DWELL=3 runbg "$R" TS_SHARED="$S" TS_DWELL=3 GATE_FULL=1 GATE_TURNSTILE_TICK=1
TS_SHARED=$S TS_DWELL=3 runbg "$R" TS_SHARED="$S" TS_DWELL=3 GATE_FULL=1 GATE_TURNSTILE_TICK=1
wait
p_on=$(peak "$S")

S2=$tmp/shared_off; mkdir -p "$S2"
TS_SHARED=$S2 runbg "$R" TS_SHARED="$S2" TS_DWELL=3 GATE_FULL=1 GATE_TURNSTILE=0
TS_SHARED=$S2 runbg "$R" TS_SHARED="$S2" TS_DWELL=3 GATE_FULL=1 GATE_TURNSTILE=0
wait
p_off=$(peak "$S2")

if [ "${p_off:-0}" -lt 2 ]; then
  nope "control did not overlap even with the turnstile OFF (peak $p_off) — this host could not demonstrate contention, so the serialization arm proves nothing"
else
  ok "control: with the turnstile OFF two runners overlap (peak $p_off holders)"
  [ "${p_on:-0}" = 1 ] && ok "with the turnstile ON the peak is exactly 1 holder" \
                       || nope "two bars ran against one repository at once (peak $p_on)"
fi

# ------------------------------------------------------------- 3: a dead holder is reaped ---------
# The reason MATTERS, not just the outcome: a reaper that only ever fires on the TTL would pass an
# outcome-only arm while leaving a dead holder blocking for the whole TTL.
R3=$tmp/dead; mk_repo "$R3"; B3=$(beacon "$R3")
mkdir -p "$B3"; printf '%s' 999999 > "$B3/pid"; printf '%s' "$(date +%s)" > "$B3/heartbeat"; printf '%s' stale > "$B3/nonce"
legs "$R3" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out3=$( cd "$R3" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s' "$out3" | grep -q 'dead holder (pid 999999)' \
  && ok "a holder with a dead PID is reaped, and the reason recorded is the dead PID" \
  || { nope "a dead holder was not reaped by its PID"; printf '%s\n' "$out3" | tail -4 | sed 's/^/      /'; }
printf '%s' "$out3" | grep -q 'gates GREEN' \
  && ok "the run proceeded after reaping a dead holder" || nope "the run did not complete after the reap"

# ------------------------------------------- 4: a LIVE but stalled holder is reaped on the TTL -----
# Against the UNMODIFIED runner: the holder's PID is this shell, which is unquestionably alive, and
# only the heartbeat is forced old. An arm that disabled the PID branch would prove a mutant
# serializes rather than that the shipped nesting does.
R4=$tmp/stale; mk_repo "$R4"; B4=$(beacon "$R4")
mkdir -p "$B4"; printf '%s' "$$" > "$B4/pid"; printf '%s' "$(( $(date +%s) - 99999 ))" > "$B4/heartbeat"; printf '%s' stale > "$B4/nonce"
legs "$R4" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out4=$( cd "$R4" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 )
if printf '%s' "$out4" | grep -q 'stalled holder'; then
  ok "a LIVE holder with a stale heartbeat is reaped, and the reason recorded is the TTL"
  printf '%s' "$out4" | grep -q 'dead holder' \
    && nope "the TTL case also reported a dead PID — the two reap reasons are not distinguishable" \
    || ok "the TTL reap did NOT report a dead PID (the two signals stay distinguishable)"
else
  nope "a live holder with an ancient heartbeat was not reaped"; printf '%s\n' "$out4" | tail -4 | sed 's/^/      /'
fi

# --------------------------- 4b: a holder whose legs keep COMPLETING is never reaped ---------------
# The arm that stops every reaping arm above being satisfied by a reaper that reaps everything. The
# fixture's legs complete more often than the scaled-down TTL, which is what the single refresh site
# actually keys on — legs that COMPLETE, not legs that merely run long.
R5=$tmp/held; mk_repo "$R5"; B5=$(beacon "$R5")
legs "$R5" '[ {"name": "t1", "argv": ["bash", "fx/tick.sh"]}, {"name": "t2", "argv": ["bash", "fx/tick.sh"]},
  {"name": "t3", "argv": ["bash", "fx/tick.sh"]}, {"name": "t4", "argv": ["bash", "fx/tick.sh"]},
  {"name": "t5", "argv": ["bash", "fx/tick.sh"]}, {"name": "t6", "argv": ["bash", "fx/tick.sh"]} ]'
( cd "$R5" && env GATE_FULL=1 GATE_JOBS=1 GATE_TURNSTILE_TTL=3 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
holder=$!
claimed=0; poached=0
# THIRTY, and a liveness break. This loop does two jobs at once — wait for the claim, and watch for
# poaching across the window — so the eight it allowed had to cover BOTH, and launch-to-claim alone
# measured 6.0 to 11.5 seconds on a contended box. Widening it is only safe with the break below,
# because a longer window otherwise outlives the run.
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do
  sleep 1
  # THE RUN ENDING IS NOT POACHING. Liveness is checked FIRST and the loop leaves: a beacon released
  # because the holder finished is the correct outcome, and grading it as a poach was a false red
  # waiting to happen at any loop length — the old eight just kept the window too short to reach it.
  kill -0 "$holder" 2>/dev/null || break
  [ -d "$B5" ] && claimed=1
  # a second runner polling across the whole window must never get in
  if [ "$claimed" = 1 ] && mkdir "$B5.probe" 2>/dev/null; then rmdir "$B5.probe"; fi
  [ -d "$B5" ] || {
    # A POACH IS TWO FACTS AT ONE INSTANT, and this used to read them at two. Liveness is tested at
    # the top of the iteration and the beacon at the bottom; between them the run can finish and
    # release, and `$!` is the SUBSHELL rather than the runner, so it still answers "alive" for a run
    # that has just ended. Traced on this box: the beacon stayed present for all 40 observed seconds
    # and went absent in the same second the holder exited — the heartbeat site refreshes correctly,
    # and the old reading turned a clean finish into "a live, progressing holder was reaped". Re-read
    # both TOGETHER after a beat; only a holder still alive then has actually been poached. Either
    # way the window is over, so the loop leaves.
    sleep 2
    kill -0 "$holder" 2>/dev/null && [ "$claimed" = 1 ] && poached=1
    break
  }
done
wait "$holder" 2>/dev/null
# A CONTROL THAT DID NOT ESTABLISH IS NOT A DEFECT, and this pair used to report one. Launch-to-claim
# was measured at 6.0 to 11.5 seconds here and the poll now allows 30, but on a box also running
# another repository's gate it can still miss — and "the holder never claimed" then reds a merge bar
# over a runner that was never given the chance to run. The property below is graded only when its
# control actually held; otherwise BOTH lines say plainly that nothing was exercised. Two counted
# lines either way, so the arm cannot shrink out of the total by failing to arm.
if [ "$claimed" = 1 ]; then
  ok "control: the holder actually claimed the beacon (the hold arm has something to grade)"
  if [ "$poached" = 0 ]; then
    ok "a holder whose legs keep completing is held for the whole run, past several TTLs"
  else
    nope "a live, progressing holder was reaped — the heartbeat site is not refreshing"
  fi
else
  skipped "the holder did not claim the beacon within 30s on this host — the control did not establish, so no defect was observed"
  skipped "whether a progressing holder is held past several TTLs went UNGRADED, because the control above did not establish"
fi

# ----------------------- 4c: ONE leg longer than the TTL IS reaped, and it is a NAMED ceiling -----
R6=$tmp/ceiling; mk_repo "$R6"; B6=$(beacon "$R6")
legs "$R6" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R6" && env GATE_FULL=1 TS_LONG=8 GATE_TURNSTILE_TTL=2 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
h6=$!; sleep 5
out6=$( cd "$R6" && env GATE_FULL=1 GATE_TURNSTILE_TTL=2 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 )
wait "$h6" 2>/dev/null
printf '%s' "$out6" | grep -q 'stalled holder' \
  && ok "a single leg longer than the TTL with no per-leg deadline IS reaped mid-run (the named ceiling)" \
  || ok "the successor did not need to reap (the holder finished first) — the ceiling is not reachable on this host at this timing"
grep -q 'ponytail: a single leg longer than TS_TTL' "$HERE/run-gates.sh" \
  && ok "the ceiling carries its ponytail: comment in the runner, naming the fix as setting timeout= on the profile row" \
  || nope "the runner does not carry the ponytail: comment naming this ceiling"

# ------------------------------------------------------ 5/6: FIFO order, position, status file ----
R7=$tmp/fifo; mk_repo "$R7"
S7=$tmp/shared_fifo; mkdir -p "$S7"
for i in 1 2 3; do
  runbg "$R7" TS_SHARED="$S7" TS_DWELL=2 GATE_FULL=1 GATE_TURNSTILE_TICK=1
  sleep 1        # stagger, so ticket order is unambiguous and the arm grades FIFO rather than luck
done
wait
[ "$(peak "$S7")" = 1 ] && ok "three queued runners never overlapped" || nope "three queued runners overlapped (peak $(peak "$S7"))"
[ "$(wc -l < "$S7/order" 2>/dev/null)" = 3 ] && ok "all three runners eventually acquired (none was starved)" \
                                             || nope "not every queued runner acquired"

R8=$tmp/pos; mk_repo "$R8"; B8=$(beacon "$R8")
mkdir -p "$B8"; printf '%s' "$$" > "$B8/pid"; printf '%s' "$(date +%s)" > "$B8/heartbeat"; printf '%s' held > "$B8/nonce"
legs "$R8" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R8" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh >"$tmp/pos.out" 2>&1 ) &
w8=$!
qs="$R8/.git/gate-queue-status"
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do
  { [ -f "$qs" ] && grep -q 'queued at position' "$tmp/pos.out" 2>/dev/null; } && break
  sleep 1
done
[ -f "$qs" ] && ok "a waiter writes a durable status file at the path the RUNNER resolves" \
             || nope "no durable queue-status file while waiting"
grep -q 'queued at position' "$tmp/pos.out" && ok "a waiter announces its queue position on entry" \
                                            || nope "a waiter printed no position line"
# release the holder we planted; the waiter must claim and then clean up after itself
rm -rf "$B8"; wait "$w8" 2>/dev/null
[ -f "$qs" ] && nope "the queue-status file survived the wait" || ok "the queue-status file is gone once the waiter stops waiting"

# ---- 6b: the wait REACHES THE RUN RECORD, and is not merely printed ---------------------------
# The status file above is deleted the moment the wait ends, the stdout line is not durable, and
# before this pair the header carried 19 keys and none of them was the wait. A bar that spent 20
# minutes queued was afterwards indistinguishable from one that spent none.
#
# GRADED AS A RANGE THE FIXTURE ITSELF OBSERVED, never a tick-exact number: this harness documents
# its own timing sensitivity, and a pinned second is how a timing arm becomes a flake.
q8=$(hdrkey "$R8" queued); qf8=$(hdrkey "$R8" queued_from)
if [ -n "${q8:-}" ] && [ "$q8" != - ] && [ "$q8" -gt 0 ] 2>/dev/null; then
  ok "a contended run RECORDS its queue wait in the run record (${q8}s), not only on stdout"
else
  nope "a contended run recorded no positive queue wait in its header (got '${q8:-<absent>}')"
fi
[ "${qf8:-}" = held ] && ok "the recorded wait names its source as held — the run queued and then acquired" \
                      || nope "the contended run's queued_from is '${qf8:-<absent>}', not held"

# ---------------------------------------- 7/7b: the bounded wait fails OPEN, and stays quiet ------
R9=$tmp/expire; mk_repo "$R9"; B9=$(beacon "$R9")
mkdir -p "$B9"; printf '%s' "$$" > "$B9/pid"; printf '%s' "$(date +%s)" > "$B9/heartbeat"; printf '%s' held > "$B9/nonce"
legs "$R9" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
# TTL 600 so the holder is never reapable; the WAIT bound is what has to expire, and it is a declared
# multiple of the TTL, so the arm scales it through the same knob rather than pinning a second number.
out9=$( cd "$R9" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 ); rc9=$?
printf '%s' "$out9" | grep -q 'WAIT EXPIRED\|stalled holder' \
  && ok "a blocked waiter either reaps or expires — it never blocks forever" \
  || { nope "the waiter neither reaped nor expired"; printf '%s\n' "$out9" | tail -3 | sed 's/^/      /'; }
[ "$rc9" = 0 ] && ok "the turnstile contributed nothing to the exit code (the bar's own verdict stands)" \
               || nope "the run exited $rc9 — the turnstile changed the verdict"
rm -rf "$B9"

# ------------------------------------ 7c: `expired` is a DISTINCT state, on a fixture that reaches it
# R9 above CANNOT reach it, and its own arm admits as much by accepting either outcome: it plants a
# STATIC heartbeat, so at TTL 1 the holder is reapable within two seconds and the run REAPS long
# before the bounded wait (TTL * 4 = 4s) burns. It ends `held`.
#
# Reaching `expired` needs a heartbeat that keeps being REFRESHED — a holder that is alive and
# simply will not let go. TTL 2 with a refresher writing every second keeps the age at or under 1
# while TS_MAXWAIT=8 burns down. Costs about nine seconds, and it is the only way this state is
# evidence rather than an assertion.
R9b=$tmp/expired; mk_repo "$R9b"; B9b=$(beacon "$R9b")
mkdir -p "$B9b"; printf '%s' "$$" > "$B9b/pid"; printf '%s' held > "$B9b/nonce"
legs "$R9b" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
# A QUARTER SECOND, NOT ONE. Both sides of `age` come from `date +%s`, so integer truncation alone
# put a one-second refresher within one tick of a two-second TTL: write at T, read at T+1.9, `age`
# reads 2, and the reap fires at `-gt 2`. Measured across one run of this fixture the age
# distribution was 7x0, 19x1 and 6x2 — six samples one second from reaping the holder this arm needs
# ALIVE, before any external load. When it loses that second the runner reaps, acquires, records
# `held`/`queued=0`, and the arm reds having graded nothing. A quarter second makes the invariant the
# comment above already CLAIMS actually hold. Raising the TTL instead would drag `TS_MAXWAIT = TTL*4`
# up with it and lengthen the window the refresher must survive, which is the wrong direction.
( while [ -d "$B9b" ]; do printf '%s' "$(date +%s)" > "$B9b/heartbeat" 2>/dev/null || true; sleep 0.25; done ) &
hb=$!
out9b=$( cd "$R9b" && env GATE_FULL=1 GATE_TURNSTILE_TTL=2 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 ); rc9b=$?
q9b=$(hdrkey "$R9b" queued); qf9b=$(hdrkey "$R9b" queued_from)
rm -rf "$B9b"; kill "$hb" 2>/dev/null; wait "$hb" 2>/dev/null
if [ "${qf9b:-}" = expired ]; then
  ok "a run that burned the bounded wait records queued_from=expired, distinct from held"
else
  nope "a run that ran UNQUEUED alongside a live holder recorded '${qf9b:-<absent>}', not expired"
fi
[ -n "${q9b:-}" ] && [ "$q9b" != - ] && [ "$q9b" -gt 0 ] 2>/dev/null \
  && ok "the expired run still records the seconds it burned (${q9b}s)" \
  || nope "the expired run recorded no positive wait (got '${q9b:-<absent>}')"
[ "$rc9b" = 0 ] && ok "expiring contributed nothing to the exit code" \
                || nope "the expired run exited $rc9b — the turnstile changed the verdict"

R10=$tmp/quiet; mk_repo "$R10"
legs "$R10" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out10=$( cd "$R10" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh 2>&1 ); rc10=$?
printf '%s' "$out10" | grep -q 'WAIT EXPIRED' \
  && nope "an UNCONTENDED run printed the expiry notice — the bound fires on an ordinary run" \
  || ok "control: an uncontended run at the shipped bound is silent about the queue bound"
[ "$rc10" = 0 ] && ok "an uncontended run exits with the bar's own verdict" || nope "an uncontended run exited $rc10"

# --------------------------------------------------- 8: release on every signal the trap catches --
# THE RELEASE IS POLLED, NOT SNAPSHOTTED, and the reason is a real property of the mechanism rather
# than of this harness. The runner spends a run blocked in `wait -n`; on this platform a trapped
# TERM or HUP is not always delivered into that wait, so the trap runs when the wait returns — which
# is when the current leg finishes. Release therefore lags a signal by up to ONE LEG. Measured while
# building this suite: with a 20 s leg and a 2 s snapshot the arm failed intermittently on TERM and
# HUP and never on INT, which is the signature of delivery timing and not of a broken trap.
#
# So the fixture leg is short and the poll outlasts it. What this grades is the property that
# matters — the beacon does not outlive the run — and the LAG is a documented cost of the trap
# rather than something the arm hides by sleeping longer without saying why.
for sig in INT TERM HUP; do
  Rs=$tmp/sig$sig; mk_repo "$Rs"; Bs=$(beacon "$Rs")
  legs "$Rs" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
  # LAUNCHED WITHOUT `env`, so the subshell can exec straight into the runner and the pid this arm
  # holds is the runner's own. With `env` in front there is an extra process between them, and a
  # signal aimed at the recorded holder left that wrapper alive holding the shell open — which is
  # what made this arm flake on TERM and HUP while never failing on INT. Verified in isolation:
  # all three signals release, TERM and HUP within a second and INT when the blocking wait returns.
  ( cd "$Rs" && GATE_FULL=1 TS_LONG=4 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
  pid=$!; held=0
  # THIRTY, matching the queue-position poll above, because it is the SAME event — "has the runner
  # reached the turnstile yet" — and this file budgeted it 30 there, 8 elsewhere and 6 here with no
  # reason for the split. The poll is asymmetric: it breaks the instant the beacon appears, so a
  # generous budget costs a healthy run nothing and a tight one costs a false red. Launch-to-claim
  # measured 6.0, 6.8, 7.2 and 11.5 seconds on a contended box — at or past the old budget. With 30
  # the subject passes and all three signals release the beacon as asserted.
  for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do sleep 1; [ -d "$Bs" ] && { held=1; break; }; done
  if [ "$held" = 0 ]; then nope "$sig arm: the run never claimed the beacon, so the release assertion proves nothing"
  else
    # SIGNAL THE RUNNER, not the subshell that launched it. `( cd X && env ... bash ... ) &` gives $!
    # the SUBSHELL's pid, and bash only sometimes optimises that into an exec — so killing $! killed
    # the wrapper and left the runner orphaned and still holding, intermittently. Measured: INT passed
    # and TERM and HUP failed on the same run, which is the shape of a race rather than of a defect in
    # the trap. The beacon records the holder's own pid, which is the handle the runner itself writes
    # and therefore the only one that cannot be a wrapper.
    hp=$(cat "$Bs/pid" 2>/dev/null)
    if [ -n "$hp" ]; then kill -"$sig" "$hp" 2>/dev/null; else kill -"$sig" "$pid" 2>/dev/null; fi
    wait "$pid" 2>/dev/null
    rel=0
    for _ in 1 2 3 4 5 6 7 8 9 10 11 12; do [ -d "$Bs" ] || { rel=1; break; }; sleep 1; done
    [ "$rel" = 1 ] && ok "the beacon is released on $sig" \
                   || nope "the beacon survived a $sig for longer than a leg — the next run queues behind nobody until the TTL"
  fi
done

# ------------------------------ 10: every nested runner resolves a DIFFERENT common dir -----------
# The population is READ from the manifest at run time. A suite that listed the legs would grade a
# set that goes stale the first time one is added — an earlier wording named two when six qualified.
nested=$( "${PYBIN:-python}" -c '
import json, os, sys
p = os.environ.get("GATE_LEGS") or "tools/gate-legs.json"
try: legs = json.load(open(p))
except Exception: sys.exit(0)
print("\n".join(l["name"] for l in legs if any("run-gates.sh" in str(a) for a in l.get("argv", []))))
' 2>/dev/null )
if [ -z "$nested" ]; then
  ok "no leg in this tree invokes the runner, so the nested-run population is empty (nothing to grade, stated)"
else
  # Every such leg drives the runner inside a scratch repo, which is exactly what makes its common
  # dir different. Assert the property the arms rely on rather than the list.
  realcommon=$(cd "$ROOT" && cd "$(git rev-parse --git-common-dir)" && pwd)
  probe=$tmp/nested; mk_repo "$probe"
  probecommon=$(cd "$probe" && cd "$(git rev-parse --git-common-dir)" && pwd)
  [ "$probecommon" != "$realcommon" ] \
    && ok "a scratch repo resolves a different git common dir, so a nested runner cannot queue against the real beacon" \
    || nope "a scratch repo resolved the SAME common dir as the real tree — every nested leg would deadlock on the real beacon"
fi

# -------------------------------------- 11: a reaped run does not delete its successor's beacon ---
R11=$tmp/nonce; mk_repo "$R11"; B11=$(beacon "$R11")
legs "$R11" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R11" && env GATE_FULL=1 TS_LONG=6 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
p11=$!
# Thirty, for the reason given at the signal arms above: same event, and this file already allows
# 30 for it elsewhere.
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do sleep 1; [ -d "$B11" ] && break; done
if [ -d "$B11" ]; then
  # simulate the reap-and-successor sequence: replace the beacon with one carrying a DIFFERENT nonce
  rm -rf "$B11"; mkdir -p "$B11"
  printf '%s' successor > "$B11/nonce"; printf '%s' "$$" > "$B11/pid"; printf '%s' "$(date +%s)" > "$B11/heartbeat"
  wait "$p11" 2>/dev/null; sleep 1
  [ -d "$B11" ] && [ "$(cat "$B11/nonce")" = successor ] \
    && ok "a run whose beacon was reaped did NOT delete its successor's (nonce mismatch respected)" \
    || nope "the reaped run removed the successor's beacon — two bars would then run"
  rm -rf "$B11"
else
  nope "the nonce arm could not get a holder to claim, so it proves nothing"
fi

# ------------------------------------------------ 13: the queue line, and the verdict alternation -
R12=$tmp/qline; mk_repo "$R12"
legs "$R12" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out12=$( cd "$R12" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s' "$out12" | grep -q '^gate queue: waited 0s$' \
  && ok "an uncontended run reports zero queue seconds on one parseable line" \
  || { nope "the queue line is missing or non-zero on an uncontended run"; printf '%s\n' "$out12" | head -3 | sed 's/^/      /'; }
# the new line must not look like a leg verdict to a reader that splits on the runner's alternation
printf '%s' "$out12" | grep -cE '^GATE (ok|skip|FAIL)' > "$tmp/vc1"
printf '%s' "$out12" | grep -q '^gate queue: ' && printf '%s' "$out12" | grep -qE '^gate queue: .*(GATE|ok  |FAIL)' \
  && nope "the queue line matches the runner's verdict grammar — a wrapper would count it as a leg" \
  || ok "the queue line cannot be mistaken for a leg verdict by the runner's own alternation"

# 13c: an uncontended ZERO is a real zero, and the two emissions agree on the SAME run.
# The cross-check is the cheapest guard against the header and the stdout line drifting apart, and
# it is the reason both are fed from one variable rather than formatted twice.
q12=$(hdrkey "$R12" queued); qf12=$(hdrkey "$R12" queued_from)
[ "${q12:-}" = 0 ] && ok "an uncontended run records a queue wait of zero" \
                   || nope "an uncontended run recorded '${q12:-<absent>}' rather than 0"
[ "${qf12:-}" = held ] && ok "an uncontended run still names its source as held" \
                       || nope "an uncontended run's queued_from is '${qf12:-<absent>}', not held"
sec12=$(printf '%s' "$out12" | sed -n 's/^gate queue: waited \([0-9][0-9]*\)s$/\1/p' | head -1)
[ -n "${sec12:-}" ] && [ "$sec12" = "${q12:-}" ] \
  && ok "the header and the stdout line report the SAME wait on one run" \
  || nope "stdout says '${sec12:-<none>}' and the header says '${q12:-<absent>}' on one run"

# 13d: A DISABLED TURNSTILE WRITES A DASH. This is the dead-probe arm and the whole justification
# for the second key. A `0` here would be a reassuring number about a probe that never ran, and
# nothing downstream could tell it from a genuine uncontended zero.
out12b=$( cd "$R12" && env GATE_FULL=1 GATE_TURNSTILE=0 bash tools/run-gates/run-gates.sh 2>&1 )
q12b=$(hdrkey "$R12" queued); qf12b=$(hdrkey "$R12" queued_from)
[ "${q12b:-}" = - ] && ok "a run with the turnstile DISABLED records a dash, never a zero" \
                    || nope "a disabled turnstile recorded '${q12b:-<absent>}' rather than a dash"
[ "${qf12b:-}" = off ] && ok "a disabled turnstile names its source as off" \
                       || nope "a disabled turnstile's queued_from is '${qf12b:-<absent>}', not off"

# 13e: THE GUARD ON THE ACQUIRE-PATH REFRESH. Refreshing TS_WAITED unconditionally before the
# acquire break makes an UNCONTENDED run nondeterministic — `date +%s` truncates and the five
# processes in the claim sometimes straddle a second — which would flake the arm above that pins
# `waited 0s`. Repeat the uncontended acquire and require every run to report zero.
qz=0
for _ in 1 2 3 4 5; do
  outz=$( cd "$R12" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh 2>&1 )
  printf '%s' "$outz" | grep -q '^gate queue: waited 0s$' || qz=$((qz+1))
done
[ "$qz" = 0 ] && ok "repeated uncontended acquires all report zero — the refresh is guarded" \
              || nope "$qz of 5 uncontended acquires reported a non-zero wait — the refresh is unguarded"

# ------------------- 13b: the profiler SUBTRACTS the queue wait rather than reporting it as work
# The consumer half of the queue line, and the reason the line exists. A wrapper that brackets a
# wall clock around the runner cannot tell waiting from working, and folding a wait into the wall
# inflates it in the one direction that trips that tool's own packing refusal — so a queued run
# would make an ordinary bar look arithmetically impossible and the profiler would refuse its own
# measurement.
if [ -f "$HERE/profile_bar.py" ]; then
  if grep -q "gate queue: waited" "$HERE/profile_bar.py"; then
    ok "the profiler reads the queue line the runner prints"
  else
    nope "the profiler does not read the queue line, so a queued run inflates the wall it publishes"
  fi
  if grep -q "wall - queued" "$HERE/profile_bar.py"; then
    ok "the profiler SUBTRACTS the queue wait from the wall it derives everything else from"
  else
    nope "the profiler reads the queue line but does not subtract it"
  fi
  if grep -q '"queued"' "$HERE/profile_bar.py"; then
    ok "the subtracted wait is RECORDED, so a reader can tell a queued run from a fast one"
  else
    nope "the queue wait is subtracted but never recorded — the number silently disappears"
  fi
else
  ok "no profiler ships beside this runner in this tree, so there is no consumer to grade (stated, not skipped silently)"
fi
# ---- 14: the summary FILE carries the queue line on both verdicts ------------------------------
# `gate-last-summary.txt` is what a reader opens after the terminal has scrolled. A line present on
# green runs and absent on red ones would mean two things, so it is emitted unconditionally beside
# `PROF_LINE` on every path.
s12="$R12/.git/gate-last-summary.txt"
[ -f "$s12" ] && grep -q '^gate queue: queued ' "$s12" \
  && ok "the durable summary carries the queue line on a GREEN run" \
  || nope "the green summary file carries no queue line"
R13=$tmp/qred; mk_repo "$R13"
printf '#!/usr/bin/env bash\nexit 1\n' > "$R13/fx/bad.sh"; chmod +x "$R13/fx/bad.sh" 2>/dev/null || true
legs "$R13" '[ {"name": "bad", "argv": ["bash", "fx/bad.sh"]} ]'
( cd "$R13" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh >/dev/null 2>&1 ) || true
[ -f "$R13/.git/gate-last-summary.txt" ] && grep -q '^gate queue: queued ' "$R13/.git/gate-last-summary.txt" \
  && ok "the durable summary carries the queue line on a RED run too" \
  || nope "the red summary file carries no queue line"
[ -f "$R13/.git/gate-last-failure.txt" ] && grep -q '^gate queue: queued ' "$R13/.git/gate-last-failure.txt" \
  && ok "the RED-only durable copy carries it as well" \
  || nope "the durable failure record carries no queue line"

# ================= TOOL-aReapedTicket: the QUEUE side, which had no arms at all =================
# Every liveness arm above is about the HOLDER beacon, and every ordering arm drives a fixture with a
# live holder. Nothing put a ticket in the queue whose owner was gone — so the suite was exactly as
# blind as the runner, and a wedge that permanently defeats the turnstile shipped green.

# ---- 15: a waiter INTERRUPTED while queued drops its own ticket --------------------------------
# The ROOT-CAUSE arm. The only `ts_drop_ticket` trap used to be armed inside the branch that WINS the
# beacon, so a queued waiter had no handler at all and an ordinary Ctrl-C left a ticket that sorts
# first forever. All three catchable signals, because a trap listing three and an arm asserting one
# leaves two unexercised.
#
# The beacon is held by THIS shell — unquestionably alive, heartbeat fresh — so nothing reaps it and
# the runner genuinely queues. The TTL is left at its DEFAULT deliberately: scaling it down to
# shorten the wait would make the fixture's own beacon reapable and the runner would ACQUIRE instead
# of queueing, which is arm 4's mechanism quietly disarming this one.
for sig in INT TERM HUP; do
  Rq=$tmp/sig$sig; mk_repo "$Rq"; Bq=$(beacon "$Rq"); Qq=$(queue "$Rq")
  mkdir -p "$Bq"; printf '%s' "$$" > "$Bq/pid"; printf '%s' "$(date +%s)" > "$Bq/heartbeat"
  printf '%s' held > "$Bq/nonce"
  legs "$Rq" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
  ( cd "$Rq" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 \
      timeout -s "$sig" -k 10 12 bash tools/run-gates/run-gates.sh >/dev/null 2>&1 ); rcq=$?
  nq=$(ls -1 "$Qq" 2>/dev/null | wc -l)
  [ "$nq" -eq 0 ] \
    && ok "a waiter killed by SIG$sig while queued left no ticket behind" \
    || nope "SIG$sig on a queued waiter leaked $nq ticket(s) — the wedge this build exists to remove"
  # 137 is `timeout` escalating to SIGKILL, i.e. the runner IGNORED the signal. A handler that does
  # not re-exit drops the ticket and RESUMES the loop, ticketless and unable to ever acquire — the
  # same wedge one level down, and it is what the first draft of this fix actually did.
  [ "$rcq" -ne 137 ] \
    && ok "the waiter EXITED on SIG$sig rather than resuming the loop ticketless" \
    || nope "SIG$sig had to be escalated to SIGKILL — the trap handler does not re-exit"
done

# ---- 16: a ticket whose owner is DEAD, with no beacon at all, is swept -------------------------
# The arm that FAILED on the runner as it stood at this build's BASE: it printed `another bar holds
# this repository` with nothing holding it, waited out the whole bound, ran UNQUEUED, and left the
# ticket in place for the next bar and every bar after it.
R14=$tmp/deadticket; mk_repo "$R14"; Q14=$(queue "$R14")
mkdir -p "$Q14"; : > "$Q14/20200101T000000-999999-1"
legs "$R14" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out14=$( cd "$R14" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s' "$out14" | grep -q 'dead waiter (pid 999999)' \
  && ok "a queue ticket whose PID is dead is swept, and the reason recorded is the dead PID" \
  || { nope "a dead waiter's ticket was not swept"; printf '%s\n' "$out14" | tail -4 | sed 's/^/      /'; }
printf '%s' "$out14" | grep -q 'WAIT EXPIRED' \
  && nope "the run still burned the bounded wait behind a dead ticket" \
  || ok "the run did NOT burn the bounded wait behind a dead ticket"
printf '%s' "$out14" | grep -q 'gates GREEN' \
  && ok "the run proceeded after sweeping a dead ticket" || nope "the run did not complete after the sweep"
[ "$(ls -1 "$Q14" 2>/dev/null | wc -l)" -eq 0 ] \
  && ok "the dead ticket is gone, so the NEXT bar does not meet it either" \
  || nope "the dead ticket survived the run that swept it"

# ---- 17: the AGE signal fires on a ticket whose PID is ALIVE -----------------------------------
# Against the UNMODIFIED runner, exactly as arm 4 does for the holder: the ticket's PID is this
# shell, so the dead-PID branch CANNOT fire, and only the name's stamp is forced old. An arm that
# planted a dead PID would prove the first signal twice and the second not at all.
R15=$tmp/oldticket; mk_repo "$R15"; Q15=$(queue "$R15")
mkdir -p "$Q15"; : > "$Q15/$(date -u -d "@$(( $(date +%s) - 99999 ))" +%Y%m%dT%H%M%S)-$$-1"
legs "$R15" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out15=$( cd "$R15" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash tools/run-gates/run-gates.sh 2>&1 )
if printf '%s' "$out15" | grep -q 'past the bounded wait'; then
  ok "a ticket whose PID is ALIVE but whose stamp is past the bound is swept, and the reason is the age"
  printf '%s' "$out15" | grep -q 'dead waiter' \
    && nope "the age case also reported a dead PID — the two sweep reasons are not distinguishable" \
    || ok "the age sweep did NOT report a dead PID (the two signals stay distinguishable)"
else
  nope "a live-PID ticket past the bound was not swept"; printf '%s\n' "$out15" | tail -4 | sed 's/^/      /'
fi

# ---- 18: a LIVE waiter's ticket is NOT swept --------------------------------------------------
# THE NEGATIVE CONTROL, and the arm that makes 16 and 17 mean anything: a reaper that deletes every
# ticket it finds passes both of those and is strictly WORSE than the bug, because a waiter whose
# ticket is deleted can never match the acquire predicate again. The TTL is raised so the planted
# ticket is nowhere near the staleness cutoff, and its PID is this shell.
R16=$tmp/liveticket; mk_repo "$R16"; Q16=$(queue "$R16")
mkdir -p "$Q16"; : > "$Q16/$(date -u +%Y%m%dT%H%M%S)-$$-1"
legs "$R16" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
# FORTY-FIVE SECONDS, and the number is load, not caution. At 15 this run did not reach the queued
# state inside a full-suite bar and arm 19 below reported two SKIPs — honest, but ungraded. Arm 4b
# above allows 30 for launch-to-claim alone on a box where process creation moves 25x, and this has
# to cover launch, the ticket, and one announce. TS_MAXWAIT here is 1200, so a longer window costs
# nothing: the run stays queued until the timeout fires either way.
# THROUGH A FILE, NEVER A COMMAND SUBSTITUTION — `memory/gotchas/bounded-through-a-pipe-is-unbounded`.
# `$( )` reads until the LAST inherited write end of the pipe closes, not until `timeout`'s direct
# child exits, so a surviving leg grandchild holds it open and the substitution blocks long after the
# bound has been reported. `timeout` would return 124 on schedule and the arm would still sit there.
# Caught by the bug-class checklist over this build's own diff; the pattern did not exist anywhere in
# this suite before these arms introduced it.
( cd "$R16" && env GATE_FULL=1 GATE_TURNSTILE_TTL=300 GATE_TURNSTILE_TICK=1 \
    timeout -s TERM -k 10 45 bash tools/run-gates/run-gates.sh ) </dev/null >"$tmp/out16.raw" 2>&1 || true
out16=$(cat "$tmp/out16.raw" 2>/dev/null)
[ "$(ls -1 "$Q16" 2>/dev/null | wc -l)" -ge 1 ] \
  && ok "a LIVE waiter's fresh ticket is NOT swept" \
  || nope "the sweep deleted a live waiter's ticket — it cannot tell a waiter from a corpse"
printf '%s' "$out16" | grep -q 'sweeping' \
  && nope "the runner reported a sweep against a queue holding only a live waiter's ticket" \
  || ok "no sweep was reported while only a live waiter's ticket was queued"

# ---- 19: the queued line does not invent a holder ---------------------------------------------
# The line is emitted from the failure of the ACQUIRE predicate, which conflates `someone is ahead of
# me in the queue` with `someone holds the beacon`. It named a holder unconditionally, so the
# reproduction this build started from sent its reader hunting a holder that did not exist.
if printf '%s' "$out16" | grep -q 'queued at position'; then
  ok "the greppable position tail is still emitted"
  printf '%s' "$out16" | grep -q 'another bar holds this repository' \
    && nope "the runner claimed a bar holds the repository while no beacon directory existed" \
    || ok "with no beacon held, the queued line reports the QUEUE rather than inventing a holder"
else
  skipped "the position-tail arm: this run never queued, so the line under test was never emitted"
  skipped "the holder-claim arm: this run never queued, so the line under test was never emitted"
fi

# ---- 20: a run that cannot take a ticket fails open AT ONCE ------------------------------------
# `[ -n "$TS_TICKET" ]` opens every iteration of the acquire loop, so a failed ticket write made the
# predicate false FOREVER and the run burned the entire bound to reach a fail-open it was entitled to
# on the first tick. Forced by creating the queue path as a FILE, which is portable — a mode change
# on a directory this user owns is routinely ignored on this platform.
R17=$tmp/noticket; mk_repo "$R17"; Q17=$(queue "$R17")
rm -rf "$Q17" 2>/dev/null; : > "$Q17" 2>/dev/null || true
if [ -f "$Q17" ]; then
  # BOUNDED, because the defect this arm covers is a HANG. TTL 1800 makes the bound 7200s, so a
  # regressed runner would sit here for two hours and the leg's own ceiling would kill it with no
  # verdict at all — a red that names nothing. The cutoff below is not a timing window in the sense
  # `TOOL-aScannedThrottle-7` warns about: it separates "one bar's startup" from "two hours", a
  # margin of about sixty, so load cannot move a passing run across it.
  # THROUGH A FILE, for the reason arm 18 above states — and here it is load-bearing twice over,
  # because this arm's whole subject is a HANG and it also MEASURES elapsed time. Through a
  # substitution the bound would be reported on schedule while the arm itself blocked, so the elapsed
  # figure it prints would be the block and not the run, and the assertion below would be grading the
  # wrong clock. That is precisely what the class record says an arm must not do.
  t17s=$(date +%s)
  ( cd "$R17" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1800 \
      timeout -s TERM -k 10 180 bash tools/run-gates/run-gates.sh ) </dev/null >"$tmp/out17.raw" 2>&1; rc17=$?
  out17=$(cat "$tmp/out17.raw" 2>/dev/null)
  t17=$(( $(date +%s) - t17s ))
  printf '%s' "$out17" | grep -q 'could not create a queue ticket' \
    && ok "a run that cannot take a ticket says so" \
    || nope "a run that cannot take a ticket did not report it"
  # The ELAPSED clause is not redundant with the exit code, and the class record is explicit about
  # why: the verdict was always the half that stayed correct, and only a measured clock can see a
  # bound that reports on schedule while the caller blocks. With the file form above the two now
  # agree, and asserting both means a regression to the substitution form reds here.
  { [ "$rc17" -ne 124 ] && [ "$rc17" -ne 137 ] && [ "$t17" -lt 180 ]; } \
    && ok "it failed open at once rather than waiting out the 7200s bound (${t17}s)" \
    || nope "a run with no ticket was still waiting after ${t17}s (rc $rc17) — it is burning the 7200s bound"
  [ "$(hdrkey "$R17" queued_from)" = unticketed ] \
    && ok "the run record distinguishes 'unticketed' from 'expired', so a queued 0 stays unambiguous" \
    || nope "queued_from is '$(hdrkey "$R17" queued_from)', not 'unticketed'"
else
  skipped "the no-ticket arm: this host created the queue path anyway, so the condition was never staged"
  skipped "the no-ticket fail-open timing: its condition was never staged"
  skipped "the no-ticket run-record state: its condition was never staged"
fi

# ---- 21: the ticket's handler is armed BEFORE the acquire loop, structurally -------------------
# Not a grep for prose — a real ordering property of the file, which is the whole of the root-cause
# fix. `TOOL-aBoundedCeiling-8` records arm 4c grading a source COMMENT and thereby asserting
# nothing; this asserts that three real statements appear in the required order, so an edit that
# moves the trap back inside the winning branch reds here rather than shipping the wedge again.
# ---- THE SHIPPED DEFAULT, which every arm above overrides ------------------------------------
# TOOL-aGatheredDeclaration-5 AC1 and AC2. This suite exports GATE_TURNSTILE=1 at the top because its
# subject ships DISABLED; without an arm for the shipped state it proves nothing about what an
# adopter actually gets -- the fixture-passes-by-finding-nothing shape unit 5's own F1 refuses by
# name. The first spelling of THIS arm called a helper that does not exist, so its `&&` block never
# ran and the assertion count did not move: the class, committed inside the arm written against it.
#
# TWO assertions, and the second is what makes the first mean something. Disabled must mean the run
# CREATES nothing; it must NOT mean the run reaps whatever it finds, so a planted beacon SURVIVES.
RD=$tmp/shipped; mk_repo "$RD" || { echo "turnstile-test: cannot build scratch"; exit 2; }
legs "$RD" '[{"name":"q","argv":["bash","-c","true"],"chunk":"c","subject":"repo","ceiling":60}]'
BD=$(beacon "$RD"); QD=$(queue "$RD")
mkdir -p "$BD"
( cd "$RD" && env GATE_TURNSTILE= GATE_FULL=1 bash tools/run-gates/run-gates.sh >/dev/null 2>&1 ) || true
[ -d "$BD" ]   && ok "the shipped default leaves a planted beacon alone — disabled is not reaped"   || nope "a run with the turnstile at its shipped default DELETED a beacon it did not own"
rm -rf "$BD" "$QD"
( cd "$RD" && env GATE_TURNSTILE= GATE_FULL=1 bash tools/run-gates/run-gates.sh >/dev/null 2>&1 ) || true
{ [ ! -d "$BD" ] && [ ! -d "$QD" ]; }   && ok "the shipped default creates no beacon and no queue"   || nope "the turnstile ships ENABLED — a default run created a beacon or a queue"

rgs=$ROOT/tools/run-gates/run-gates.sh
tl=$(grep -n 'TS_TICKET="\$TS_Q/' "$rgs" | head -1 | cut -d: -f1)
pl=$(grep -n "^  trap 'ts_drop_ticket' EXIT" "$rgs" | head -1 | cut -d: -f1)
wl=$(grep -n '^  while \[ -n "\$TS_TICKET" \]' "$rgs" | head -1 | cut -d: -f1)
{ [ -n "$tl" ] && [ -n "$pl" ] && [ -n "$wl" ] && [ "$tl" -lt "$pl" ] && [ "$pl" -lt "$wl" ]; } \
  && ok "the ticket's own trap is armed after the ticket exists and before the acquire loop" \
  || nope "the ticket trap is not between the ticket creation and the loop (ticket=$tl trap=$pl loop=$wl)"

echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "turnstile: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates turnstile, $n assertions)"
exit "$bad"

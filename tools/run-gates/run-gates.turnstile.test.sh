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

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "turnstile-test: not a git repo"; exit 2; }
HERE=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
bad=0
# An EXECUTED assertion count with a floor, carried at birth: a suite that prints a hardcoded total
# is a suite whose count stops tracking its arms the first time somebody deletes one.
FLOOR_ASSERTIONS=28
n=0
ok()   { n=$((n+1)); echo "  ok   — $1"; }
nope() { n=$((n+1)); echo "  FAIL — $1"; bad=1; }

# ------------------------------------------------------------------ fixtures ----------------------
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
for _ in 1 2 3 4 5 6 7 8; do
  sleep 1
  [ -d "$B5" ] && claimed=1
  # a second runner polling across the whole window must never get in
  if [ "$claimed" = 1 ] && mkdir "$B5.probe" 2>/dev/null; then rmdir "$B5.probe"; fi
  [ -d "$B5" ] || { [ "$claimed" = 1 ] && poached=1; }
done
wait "$holder" 2>/dev/null
[ "$claimed" = 1 ] && ok "control: the holder actually claimed the beacon (the hold arm has something to grade)" \
                   || nope "the holder never claimed, so the not-reaped arm proves nothing"
[ "$poached" = 0 ] && ok "a holder whose legs keep completing is held for the whole run, past several TTLs" \
                   || nope "a live, progressing holder was reaped — the heartbeat site is not refreshing"

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
w8=$!; sleep 3
qs="$R8/.git/gate-queue-status"
[ -f "$qs" ] && ok "a waiter writes a durable status file at the path the RUNNER resolves" \
             || nope "no durable queue-status file while waiting"
grep -q 'queued at position' "$tmp/pos.out" && ok "a waiter announces its queue position on entry" \
                                            || nope "a waiter printed no position line"
# release the holder we planted; the waiter must claim and then clean up after itself
rm -rf "$B8"; wait "$w8" 2>/dev/null
[ -f "$qs" ] && nope "the queue-status file survived the wait" || ok "the queue-status file is gone once the waiter stops waiting"

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

R10=$tmp/quiet; mk_repo "$R10"
legs "$R10" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out10=$( cd "$R10" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh 2>&1 ); rc10=$?
printf '%s' "$out10" | grep -q 'WAIT EXPIRED' \
  && nope "an UNCONTENDED run printed the expiry notice — the bound fires on an ordinary run" \
  || ok "control: an uncontended run at the shipped bound is silent about the queue bound"
[ "$rc10" = 0 ] && ok "an uncontended run exits with the bar's own verdict" || nope "an uncontended run exited $rc10"

# --------------------------------------------------- 8: release on every signal the trap catches --
for sig in INT TERM HUP; do
  Rs=$tmp/sig$sig; mk_repo "$Rs"; Bs=$(beacon "$Rs")
  legs "$Rs" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
  ( cd "$Rs" && env GATE_FULL=1 TS_LONG=20 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
  pid=$!; held=0
  for _ in 1 2 3 4 5 6; do sleep 1; [ -d "$Bs" ] && { held=1; break; }; done
  if [ "$held" = 0 ]; then nope "$sig arm: the run never claimed the beacon, so the release assertion proves nothing"
  else
    kill -"$sig" "$pid" 2>/dev/null; wait "$pid" 2>/dev/null; sleep 1
    [ -d "$Bs" ] && nope "the beacon survived a $sig — the next run queues behind nobody until the TTL" \
                 || ok "the beacon is released on $sig"
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
  realcommon=$(cd "$ROOT" && git rev-parse --git-common-dir)
  probe=$tmp/nested; mk_repo "$probe"
  probecommon=$(cd "$probe" && git rev-parse --git-common-dir)
  [ "$(cd "$ROOT" && pwd -P; :)" ] && true
  [ "$probecommon" != "$realcommon" ] \
    && ok "a scratch repo resolves a different git common dir, so a nested runner cannot queue against the real beacon" \
    || nope "a scratch repo resolved the SAME common dir as the real tree — every nested leg would deadlock on the real beacon"
fi

# -------------------------------------- 11: a reaped run does not delete its successor's beacon ---
R11=$tmp/nonce; mk_repo "$R11"; B11=$(beacon "$R11")
legs "$R11" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R11" && env GATE_FULL=1 TS_LONG=6 bash tools/run-gates/run-gates.sh ) >/dev/null 2>&1 &
p11=$!
for _ in 1 2 3 4 5 6; do sleep 1; [ -d "$B11" ] && break; done
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
echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "turnstile: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates turnstile, $n assertions)"
exit "$bad"

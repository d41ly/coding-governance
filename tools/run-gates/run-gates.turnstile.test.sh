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
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "turnstile-test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
KIT="${KIT_REL##*/}"
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
_rkd_py=$(resolve_python) || { echo "turnstile-test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
LIB_DIR=$(resolve_kit_dir "$_rkd_py" lib resolve-python.sh "$HERE") || exit 2
LIB="${LIB_DIR##*/}"

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "turnstile-test: not a git repo"; exit 2; }
HERE=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
# Fixture identity and line endings for every git below, through the environment and not per repo
# (TOOL-aSparedSpawn-9 S1): no spawn, and command scope outranks a node's global autocrlf=true.
export GIT_AUTHOR_NAME=ts-test GIT_AUTHOR_EMAIL=ts@test.invalid GIT_COMMITTER_NAME=ts-test GIT_COMMITTER_EMAIL=ts@test.invalid
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
# THE HOST TURNSTILE IS THIS SUITE'S OWN (TOOL-aFrugalTurnstile-5 S7). The runner's beacon and queue
# live in a host-wide directory, so a fixture bar left on the default would queue behind every real
# bar on the machine, and one inside a real bar's leg would NEST and never claim at all. `mk_repo`
# clears it, so every arm starts on an empty turnstile exactly as a fresh common dir gave it before.
export GATE_TURNSTILE_DIR="$tmp/gate-turnstile"
# THE SLOT COUNT IS THIS SUITE'S OWN TOO (TOOL-aPairedSlots-15): one, whatever the caller exported, so
# an arm that names no count runs at the kit default and an operator's two-slot shell reds nothing.
export GATE_TURNSTILE_SLOTS=1
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
# Raised from 66 to 71 by TOOL-dDerivedDocket-25, which adds arm 22: five assertions, the same five
# counted on the branch where the first bar never establishes (one FAIL and four SKIPs).
# Raised from 71 to 74 by TOOL-dDerivedDocket-64, which adds arm 6c inside the position fixture:
# three assertions, every one unconditional, counted off the block rather than read off a run.
# Raised from 74 to 78 by TOOL-aGraftedHelix-8: one health-log line each in arms 3, 7c, 16 and 22,
# arm 22's counted on its never-established branch too, as a SKIP.
# Raised from 78 to 101 by TOOL-aFrugalTurnstile-5, which adds arms 23-28: 5, 4, 4, 6, 2 and 2
# assertions, every one unconditional or counted on both branches, counted off the blocks.
# Raised from 101 to 144 by TOOL-aPairedSlots-15: the 33 of arms 29-43 (TOOL-aPairedSlots-2 to -5),
# which left this floor where it was, and the 10 of arms 44-48, counted off the blocks.
FLOOR_ASSERTIONS=144
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
  rm -rf "$GATE_TURNSTILE_DIR"/gate-bar-beacon "$GATE_TURNSTILE_DIR"/gate-bar-beacon.* "$GATE_TURNSTILE_DIR/gate-bar-queue" 2>/dev/null
  mkdir -p "$d/${PFX}${KIT}" "$d/${PFX}${LIB}" "$d/fx"
  cp "$HERE/run-gates.sh" "$HERE/gate-profiles.txt" "$d/${PFX}${KIT}/" || return 1
  cp "$HERE/gate-fingerprint.sh" "$d/${PFX}${KIT}/" 2>/dev/null || true
  cp "$ROOT/${LIB_DIR}/resolve-python.sh" "$d/${PFX}${LIB}/" 2>/dev/null || true
  ( cd "$d" && git init -q --template= -b main . ) >/dev/null 2>&1 || return 1
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
  printf '%s\n' '[ {"name": "occupy", "argv": ["bash", "fx/occupy.sh"]} ]' > "$d/${PFX}gate-legs.json"
  ( cd "$d" && git add -A && git commit -qm seed ) >/dev/null 2>&1 || return 1
}
legs()  { printf '%s\n' "$2" > "$1/${PFX}gate-legs.json"; }
runbg() { ( cd "$1" && shift; env "$@" bash $KIT_REL/run-gates.sh; ) >>"$tmp/out.$RANDOM" 2>&1 & }
peak()  { awk 'BEGIN{m=0} {if ($1+0>m) m=$1+0} END{print m+0}' "$1/peaks" 2>/dev/null; }
# The beacon and the queue of the HOST turnstile every fixture repo shares (TOOL-aFrugalTurnstile-5),
# under the suite's own `GATE_TURNSTILE_DIR`. The repo argument is kept so each arm still names the
# repository it is about; the path no longer depends on it. They were the git common dir's, resolved
# absolutely, and the arms planting there were what that resolution existed for. `queue` also leaves
# its path in `_queue`, which its callers read instead of forking a substitution (TOOL-aSweptBar-5).
beacon(){ printf '%s/gate-bar-beacon' "$GATE_TURNSTILE_DIR"; }
queue(){  printf -v _queue '%s/gate-bar-queue' "$GATE_TURNSTILE_DIR"; printf '%s' "$_queue"; }

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
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${bad:-0}" = 0 ] && echo "PASS ($n assertions)" || echo "FAIL ($n assertions)"; [ "${bad:-0}" = 0 ] && exit 0; exit 1; fi

# ------------------------------------------------------------- 3: a dead holder is reaped ---------
# The reason MATTERS, not just the outcome: a reaper that only ever fires on the TTL would pass an
# outcome-only arm while leaving a dead holder blocking for the whole TTL.
R3=$tmp/dead; mk_repo "$R3"; B3=$(beacon "$R3")
mkdir -p "$B3"; printf '%s' 999999 > "$B3/pid"; printf '%s' "$(date +%s)" > "$B3/heartbeat"; printf '%s' stale > "$B3/nonce"
legs "$R3" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out3=$( cd "$R3" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
printf '%s' "$out3" | grep -q 'dead holder (pid 999999)' \
  && ok "a holder with a dead PID is reaped, and the reason recorded is the dead PID" \
  || { nope "a dead holder was not reaped by its PID"; printf '%s\n' "$out3" | tail -4 | sed 's/^/      /'; }
[[ $out3 == *'gates GREEN'* ]] \
  && ok "the run proceeded after reaping a dead holder" || nope "the run did not complete after the reap"
# TOOL-aGraftedHelix-8: the reap is a self-heal, so it leaves ONE I3 line in the repository's health
# log, naming the dead pid. The log is read by its fields; its stamp and fold are the resolver suite's.
hl3=$(awk -F'\t' '$2 == "run-gates" && $3 == "beacon-reaped"' "$R3/.git/health.log" 2>/dev/null)
[ "$(printf '%s' "$hl3" | grep -c .)" = 1 ] && [ "$(printf '%s' "$hl3" | cut -f4)" = "dead holder pid 999999" ] \
  && ok "the dead holder's reap appended one beacon-reaped line naming its pid" \
  || nope "the dead holder's reap left '$(printf '%s' "$hl3" | tr '\t\n' ' ;')' in the health log, not one beacon-reaped line"

# ------------------------------------------- 4: a LIVE but stalled holder is reaped on the TTL -----
# Against the UNMODIFIED runner: the holder's PID is this shell, which is unquestionably alive, and
# only the heartbeat is forced old. An arm that disabled the PID branch would prove a mutant
# serializes rather than that the shipped nesting does.
R4=$tmp/stale; mk_repo "$R4"; B4=$(beacon "$R4")
mkdir -p "$B4"; printf '%s' "$$" > "$B4/pid"; printf '%s' "$(( $(date +%s) - 99999 ))" > "$B4/heartbeat"; printf '%s' stale > "$B4/nonce"
legs "$R4" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out4=$( cd "$R4" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
if [[ $out4 == *'stalled holder'* ]]; then
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
( cd "$R5" && env GATE_FULL=1 GATE_JOBS=1 GATE_TURNSTILE_TTL=3 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1 &
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

# ------------- 4c: a LIVE holder inside a long leg is NOT reaped (TOOL-aQuenchedHarness-8) --------
# THIS ARM IS INVERTED FROM WHAT IT USED TO BE, and the inversion is the unit. It previously asserted
# that a leg longer than the TTL IS reaped mid-run, and scored BOTH outcomes `ok` — which
# `TOOL-aBoundedCeiling-8` records as an arm that cannot fail. Its only `nope` graded a source
# COMMENT, which that row also names, and the comment was deleted with the cliff it described.
#
# What the runner does now: `ts_tick_start` refreshes the beacon on a TIMER at `TS_TTL / 6`, so a
# holder inside a leg of any length stays live and the successor QUEUES. The old behaviour was
# reproduced before the fix — a successor printed `reaping the beacon of a stalled holder
# (heartbeat 13s old, ttl 6s)` against a holder that was alive and working, and both bars ran.
# THE NUMBERS ARE SIZED FOR A CONTENDED HOST, and the control is graded before the property. A TTL
# of 2 s with a 1 s tick redded twice on this box while another repository's gate ran beside it:
# one late tick — a `date` and an `mv` through MSYS cost 0.3 to 0.75 s each here — and the
# heartbeat read older than the TTL, so a LIVE holder was reaped and the arm named a ticker
# defect that was not there (TOOL-aGradedDialect-13). A TTL of 6 keeps the same property — the leg
# is still several TTLs long, and a ticker that does NOT refresh leaves a 14 s-old heartbeat that
# the successor reaps exactly as before — while a tick a few hundred milliseconds late changes
# nothing. And the successor used to launch after a flat 5 s whether or not the holder had
# claimed; launch-to-claim measured 6 to 11.5 s under load, and an unclaimed beacon makes the
# property pass VACUOUSLY. The claim is now the control, polled the way 4b polls it.
#
# THE TTL IS MEASURED, NOT TYPED (TOOL-aSparedSpawn-15 S3). A TTL is a time by definition, so this is
# the one arm where a clock stays; what it stops being is a guess. Before the runs, the SHIPPED
# `ts_tick_start`, with the one helper it calls, is sourced from the runner and run for ten ticks
# against a scratch beacon, with a `sleep` stub first on its PATH: one spawn in place of the real
# sleep's one, returning at once, so the ten bodies cost the spawns a real tick pays and nothing
# waits a second. The stub counts its calls in a file and, on the eleventh, stamps the end and
# replaces the nonce, which ends the ticker by its own guard. A stub on PATH and not a function, as
# TOOL-aSparedSpawn-11 found, because a definition here is a name the naming leg grades. One tick's
# period is the tick plus the mean body; the TTL is three periods and never under 6 s, and the leg
# is the TTL plus 8 s, so a ticker that does NOT refresh still leaves a heartbeat the successor
# reaps. A tick body that grows a spawn (a `cat` or a `date` put back) raises the printed period,
# and a period that cannot be read is a FAIL, never a typed fallback.
tk6=$tmp/tick6; mkdir -p "$tk6/b" "$tk6/bin"; printf '%s' tick > "$tk6/b/nonce"
sed -n '/^ts_alive()/p;/^ts_tick_start() {/,/^}$/p' "$HERE/run-gates.sh" > "$tk6/fn.sh"
printf '%s\n' '#!/bin/bash' \
  'd=${0%/bin/sleep}; k=0; { read -r k < "$d/count"; } 2>/dev/null; k=$((k + 1)); printf "%s\n" "$k" > "$d/count"' \
  '[ "$k" -le 10 ] || { printf "%s\n" "${EPOCHREALTIME//[.,]/}" > "$d/end"; printf x > "$d/b/nonce"; }' > "$tk6/bin/sleep"
chmod +x "$tk6/bin/sleep"
# The shell's own spelling of the stub's directory: a TMPDIR spelled `C:/...` would split the PATH
# entry at the drive colon, and the ticker would run the real `sleep` and never end.
tk6bin=$(cd "$tk6/bin" && pwd)
grep -q '^ts_tick_start() {' "$tk6/fn.sh" && [ -n "$tk6bin" ] && (
  # shellcheck disable=SC1090
  . "$tk6/fn.sh" || exit 1
  TS_DIR=$tk6/b; TS_NONCE=tick; TS_TICK_EVERY=1; TS_TTL=6
  printf '%s\n' "${EPOCHREALTIME//[.,]/}" > "$tk6/start"
  PATH="$tk6bin:$PATH" ts_tick_start || exit 1
  # A HANG BOUND the pass path never reaches: the poll ends on the stamp, or on the ticker's exit.
  _w6=0; while [ ! -s "$tk6/end" ] && [ "$_w6" -lt 600 ] && kill -0 "${TS_TICK_PID:-none}" 2>/dev/null; do sleep 0.1; _w6=$((_w6 + 1)); done
) >/dev/null 2>&1
t6s=""; t6e=""
{ read -r t6s < "$tk6/start"; read -r t6e < "$tk6/end"; } 2>/dev/null
if grep -q '^ts_tick_start() {' "$tk6/fn.sh" && [ -n "$t6s" ] && [ -n "$t6e" ]; then
  body6=$(( (10#$t6e - 10#$t6s) / 10000 )); period6=$(( 1000 + body6 ))
  ttl6=$(( (3 * period6 + 999) / 1000 )); [ "$ttl6" -ge 6 ] || ttl6=6; long6=$(( ttl6 + 8 ))
  ok "R6 measured: one tick is ${period6} ms (${body6} ms of it the body), so the TTL is ${ttl6} s and the leg ${long6} s"
else
  ttl6=6; long6=14
  nope "R6 printed no measured period: the shipped ts_tick_start did not extract or did not tick ten times, so the TTL below is a typed guess"
fi
rm -rf "$tk6"
R6=$tmp/ceiling; mk_repo "$R6"; B6=$(beacon "$R6")
legs "$R6" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R6" && env GATE_FULL=1 TS_LONG=$long6 GATE_TURNSTILE_TTL=$ttl6 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1 &
h6=$!; claimed6=0
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do
  sleep 1; kill -0 "$h6" 2>/dev/null || break; [ -d "$B6" ] && { claimed6=1; break; }
done
if [ "$claimed6" = 1 ]; then
  ok "control: the long-leg holder claimed the beacon (the ceiling arm has something to grade)"
  out6=$( cd "$R6" && env GATE_FULL=1 GATE_TURNSTILE_TTL=$ttl6 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
  wait "$h6" 2>/dev/null
  printf '%s' "$out6" | grep -q 'stalled holder' \
    && nope "a LIVE holder inside a leg longer than the TTL was reaped — the ticker is not refreshing the beacon" \
    || ok "a live holder inside a leg longer than the TTL is NOT reaped; the successor queues instead"
else
  wait "$h6" 2>/dev/null
  skipped "the long-leg holder did not claim the beacon within 30s on this host — the control did not establish, so no defect was observed"
  skipped "whether a live holder inside a long leg is reaped went UNGRADED, because the control above did not establish"
fi

# ---- 4d: the ticker is DETACHED, so GATE_JOBS=1 still dispatches -------------------------------
# The turnstile block and the dispatch pool are one shell. An undetached ticker is a live job
# forever: `live()` counts it, `[ "$(live)" -lt "$JOBS" ]` is false at width 1 forever, and the
# terminal `wait` never returns. GRADED ON ELAPSED TIME under a hard outer bound, not on a message —
# a hung bar prints nothing to grep for, which is the whole point.
R6b=$tmp/serial; mk_repo "$R6b"
legs "$R6b" '[ {"name": "q1", "argv": ["bash", "fx/quick.sh"]}, {"name": "q2", "argv": ["bash", "fx/quick.sh"]} ]'
# 180 s, not 60: the bound exists to catch a bar that never returns, and a HUNG bar hits 180 exactly
# as it hit 60. A two-leg serial bar merely SLOW on a contended host — the profile probe, the
# manifest parse and two legs, each a handful of MSYS spawns — crossed 60 twice on this box with
# another repository's gate beside it and was named a dispatch defect (TOOL-aGradedDialect-13).
( cd "$R6b" && env GATE_FULL=1 GATE_JOBS=1 GATE_TURNSTILE_TTL=12 GATE_TURNSTILE_TICK=1 timeout 180 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
rc6b=$?
[ "$rc6b" != 124 ] && ok "a two-leg bar at GATE_JOBS=1 dispatches and completes with the ticker running (rc $rc6b)" \
                   || nope "GATE_JOBS=1 hit the 180s outer bound — the ticker is counted as a live job and the pool never dispatches"

# ---- 4e: a SIGKILLed holder's ticker stops, so nothing refreshes a beacon its owner has left ----
# No trap runs on SIGKILL. The ticker's own nonce and pid guards are the mitigation, and this is the
# arm that observes them: after the holder is killed outright, its beacon must go STALE. If the
# orphan kept ticking it would refresh whatever later bar recreates that constant path, disabling
# the stale-holder signal repo-wide — a permanent wedge arriving through the fix.
R6c=$tmp/orphan; mk_repo "$R6c"; B6c=$(beacon "$R6c")
legs "$R6c" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R6c" && env GATE_FULL=1 TS_LONG=25 GATE_TURNSTILE_TTL=6 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1 &
h6c=$!
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do [ -f "$B6c/heartbeat" ] && break; sleep 1; done
if [ -f "$B6c/pid" ]; then
  { hp6c=$(<"$B6c/pid"); } 2>/dev/null
  sleep 2
  kill -9 "$hp6c" 2>/dev/null || true
  sleep 1; { hb_at_kill=$(<"$B6c/heartbeat"); } 2>/dev/null
  sleep 4
  { hb_after=$(<"$B6c/heartbeat"); } 2>/dev/null
  [ "$hb_at_kill" = "$hb_after" ] \
    && ok "a SIGKILLed holder's ticker stops writing, so its beacon goes stale and stays reapable" \
    || nope "the beacon kept advancing after its holder was SIGKILLed ($hb_at_kill -> $hb_after) — an orphan ticker is still writing"
else
  nope "the holder never wrote a beacon pid, so the orphan-ticker arm graded nothing"
fi
{ kill -9 "$h6c"; wait "$h6c"; } 2>/dev/null || true

# ---- 4f: no ticker survives a NORMAL run -------------------------------------------------------
# The tidy path, asserted separately from 4e's violent one. `ts_tick_stop` runs first in every
# handler; this checks it actually reaped rather than merely being written down.
R6d=$tmp/tickerdead; mk_repo "$R6d"; B6d=$(beacon "$R6d")
legs "$R6d" '[ {"name": "q", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R6d" && env GATE_FULL=1 GATE_TURNSTILE_TTL=6 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
[ -d "$B6d" ] && nope "the beacon directory survived a normal run" \
              || ok "a normal run releases its beacon, and with it the ticker that refreshed it"

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
( cd "$R8" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh >"$tmp/pos.out" 2>&1 ) &
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
# ---- 6c (TOOL-dDerivedDocket-64): the waiter BEATS. `gate-queue-heartbeat` sits under the git dir the
# ---- runner resolves while the waiter waits, and its mtime ADVANCES at one unchanged position — the
# ---- silence a status file rewritten only on a position change would leave an out-of-process
# ---- liveness reader. Polled, never slept a fixed time: under a loaded bar one loop iteration can
# ---- outlast a fixed sleep. RED against a runner copy with the write line deleted (no file), and one
# ---- writing it only when the position changes (no advance).
qh="$R8/.git/gate-queue-heartbeat"
qh1=$(stat -c %Y "$qh" 2>/dev/null) || qh1=""
qh2=$qh1
for _ in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30; do
  [ -n "$qh1" ] || break
  sleep 1
  qh2=$(stat -c %Y "$qh" 2>/dev/null) || qh2=""
  { [ -n "$qh2" ] && [ "$qh2" -gt "$qh1" ]; } && break
done
[ -n "$qh1" ] && ok "a waiter writes gate-queue-heartbeat under its own git dir" \
              || nope "no gate-queue-heartbeat under the git dir while waiting"
{ [ -n "$qh1" ] && [ -n "$qh2" ] && [ "$qh2" -gt "$qh1" ]; } \
  && ok "the heartbeat's mtime advances while the waiter waits at one position ($qh1 -> $qh2)" \
  || nope "the heartbeat did not advance while the waiter waited (${qh1:-absent} -> ${qh2:-absent})"
# release the holder we planted; the waiter must claim and then clean up after itself
rm -rf "$B8"; wait "$w8" 2>/dev/null
[ -f "$qs" ] && nope "the queue-status file survived the wait" || ok "the queue-status file is gone once the waiter stops waiting"
# ...and the heartbeat is NOT cleaned up with it: a reader goes by its mtime, so a leftover ages out,
# while a removal at the acquire would drop the newest move before the first leg lands. RED against a
# runner copy removing it beside `gate-queue-status`.
[ -f "$qh" ] && ok "the heartbeat outlives the wait, so the move nearest the first leg is kept" \
             || nope "the runner removed gate-queue-heartbeat when the wait ended"

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
out9=$( cd "$R9" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 ); rc9=$?
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
# AND NO FORK IN THE WRITE (TOOL-aSparedSpawn-15 S2). It wrote `$(date +%s)`, one spawn a tick, and
# a spawn on a loaded node `a` costs 632 to 818 ms, so a quarter-second refresher became a
# one-second one and the runner reaped the holder this arm needs alive. `$EPOCHSECONDS` is the same
# integer from a builtin; the `sleep` is the one spawn left in the loop.
( while [ -d "$B9b" ]; do printf '%s' "$EPOCHSECONDS" > "$B9b/heartbeat" 2>/dev/null || true; sleep 0.25; done ) &
hb=$!
out9b=$( cd "$R9b" && env GATE_FULL=1 GATE_TURNSTILE_TTL=2 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 ); rc9b=$?
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
# TOOL-aGraftedHelix-8: failing open is the turnstile healing a wedge, so it is ONE turnstile-expired line.
hl9b=$(awk -F'\t' '$2 == "run-gates" && $3 == "turnstile-expired"' "$R9b/.git/health.log" 2>/dev/null)
[ "$(printf '%s' "$hl9b" | grep -c .)" = 1 ] && printf '%s' "$hl9b" | cut -f4 | grep -qE '^waited [0-9]+s bound [0-9]+s$' \
  && ok "the expired wait appended one turnstile-expired line with its waited and bound seconds" \
  || nope "the expired wait left '$(printf '%s' "$hl9b" | tr '\t\n' ' ;')' in the health log, not one turnstile-expired line"

R10=$tmp/quiet; mk_repo "$R10"
legs "$R10" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out10=$( cd "$R10" && env GATE_FULL=1 bash $KIT_REL/run-gates.sh 2>&1 ); rc10=$?
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
  ( cd "$Rs" && GATE_FULL=1 TS_LONG=4 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1 &
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
    { hp=$(<"$Bs/pid"); } 2>/dev/null
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
# The launcher, RESOLVED by running it where the shared resolver is present; this suite SHIPS, so
# the fallback is the bare name, marked as the guess it is. `PYBIN=` overrides.
TS_PY="${PYBIN:-}"
[ -n "$TS_PY" ] || TS_PY=$(resolve_python 2>/dev/null)
[ -n "$TS_PY" ] || TS_PY=python   # gov:literal-python — last-resort fallback when the inline resolver found no launcher that runs
nested=$( "$TS_PY" -c '
import json, os, sys
p = os.environ.get("GATE_LEGS") or "'"${PFX}gate-legs.json"'"
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
  # Since TOOL-aFrugalTurnstile-5 the BEACON is host-wide and a different common dir no longer keeps a
  # nested runner off it: nesting does (arm 24). What a separate common dir still keeps apart is the
  # health log and the scratch owner record, which stay per repository.
  [ "$probecommon" != "$realcommon" ] \
    && ok "a scratch repo resolves a different git common dir, so a nested runner's health log and scratch owner stay its own" \
    || nope "a scratch repo resolved the SAME common dir as the real tree — a nested leg would write the real tree's health log and scratch owner"
fi

# -------------------------------------- 11: a reaped run does not delete its successor's beacon ---
R11=$tmp/nonce; mk_repo "$R11"; B11=$(beacon "$R11")
legs "$R11" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R11" && env GATE_FULL=1 TS_LONG=6 bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1 &
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
out12=$( cd "$R12" && env GATE_FULL=1 bash $KIT_REL/run-gates.sh 2>&1 )
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
out12b=$( cd "$R12" && env GATE_FULL=1 GATE_TURNSTILE=0 bash $KIT_REL/run-gates.sh 2>&1 )
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
  outz=$( cd "$R12" && env GATE_FULL=1 bash $KIT_REL/run-gates.sh 2>&1 )
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
( cd "$R13" && env GATE_FULL=1 bash $KIT_REL/run-gates.sh >/dev/null 2>&1 ) || true
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
  Rq=$tmp/sig$sig; mk_repo "$Rq"; Bq=$(beacon "$Rq"); queue "$Rq" >/dev/null; Qq=$_queue
  mkdir -p "$Bq"; printf '%s' "$$" > "$Bq/pid"; printf '%s' "$(date +%s)" > "$Bq/heartbeat"
  printf '%s' held > "$Bq/nonce"
  legs "$Rq" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
  ( cd "$Rq" && env GATE_FULL=1 GATE_TURNSTILE_TICK=1 \
      timeout -s "$sig" -k 10 12 bash $KIT_REL/run-gates.sh >/dev/null 2>&1 ); rcq=$?
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
R14=$tmp/deadticket; mk_repo "$R14"; queue "$R14" >/dev/null; Q14=$_queue
mkdir -p "$Q14"; : > "$Q14/20200101T000000-999999-1"
legs "$R14" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out14=$( cd "$R14" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
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
# TOOL-aGraftedHelix-8: the sweep is a self-heal, so it is ONE ticket-swept line naming the dead pid.
hl14=$(awk -F'\t' '$2 == "run-gates" && $3 == "ticket-swept"' "$R14/.git/health.log" 2>/dev/null)
[ "$(printf '%s' "$hl14" | grep -c .)" = 1 ] && [ "$(printf '%s' "$hl14" | cut -f4)" = "dead waiter pid 999999" ] \
  && ok "the dead waiter's sweep appended one ticket-swept line naming its pid" \
  || nope "the dead waiter's sweep left '$(printf '%s' "$hl14" | tr '\t\n' ' ;')' in the health log, not one ticket-swept line"

# ---- 17: the AGE signal fires on a ticket whose PID is ALIVE -----------------------------------
# Against the UNMODIFIED runner, exactly as arm 4 does for the holder: the ticket's PID is this
# shell, so the dead-PID branch CANNOT fire, and only the name's stamp is forced old. An arm that
# planted a dead PID would prove the first signal twice and the second not at all.
R15=$tmp/oldticket; mk_repo "$R15"; queue "$R15" >/dev/null; Q15=$_queue
mkdir -p "$Q15"; : > "$Q15/$(date -u -d "@$(( $(date +%s) - 99999 ))" +%Y%m%dT%H%M%S)-$$-1"
legs "$R15" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
out15=$( cd "$R15" && env GATE_FULL=1 GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
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
R16=$tmp/liveticket; mk_repo "$R16"; queue "$R16" >/dev/null; Q16=$_queue
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
    timeout -s TERM -k 10 45 bash $KIT_REL/run-gates.sh ) </dev/null >"$tmp/out16.raw" 2>&1 || true
{ out16=$(<"$tmp/out16.raw"); } 2>/dev/null
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
  printf '%s' "$out16" | grep -q 'another bar holds this host' \
    && nope "the runner claimed a bar holds the host while no beacon directory existed" \
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
R17=$tmp/noticket; mk_repo "$R17"; queue "$R17" >/dev/null; Q17=$_queue
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
      timeout -s TERM -k 10 180 bash $KIT_REL/run-gates.sh ) </dev/null >"$tmp/out17.raw" 2>&1; rc17=$?
  { out17=$(<"$tmp/out17.raw"); } 2>/dev/null
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
rgs=$ROOT/${PFX}${KIT}/run-gates.sh
tl=$(grep -n 'TS_TICKET="\$TS_Q/' "$rgs" | head -1 | cut -d: -f1)
pl=$(grep -n "^  trap 'ts_drop_ticket' EXIT" "$rgs" | head -1 | cut -d: -f1)
wl=$(grep -n '^  while \[ -n "\$TS_TICKET" \]' "$rgs" | head -1 | cut -d: -f1)
{ [ -n "$tl" ] && [ -n "$pl" ] && [ -n "$wl" ] && [ "$tl" -lt "$pl" ] && [ "$pl" -lt "$wl" ]; } \
  && ok "the ticket's own trap is armed after the ticket exists and before the acquire loop" \
  || nope "the ticket trap is not between the ticket creation and the loop (ticket=$tl trap=$pl loop=$wl)"

# ---- 22: the scratch sweep spares a LIVE bar and a FOREIGN repository (TOOL-dDerivedDocket-25) -----
# The sweep deletes directories, so what it must NOT delete is the whole of its safety. Two bars
# against one repository with the turnstile OFF, so the second starts while the first still runs:
# the first bar's owned scratch must survive the second and its verdict must be unchanged, and a
# scratch dir whose owner names ANOTHER common dir, with a dead pid, must survive too. THE CONTROL is
# a dir THIS repository's dead bar owns, planted only after the first bar has swept, which the second
# bar MUST remove: without it both survivals pass on a runner that never sweeps anything. The ambient
# `TMPDIR` is private to the arm, and the first bar holds on a go-file rather than a clock, so a slow
# second bar cannot outlive it and read as a sweep.
R22=$tmp/sweep; mk_repo "$R22"
printf '#!/usr/bin/env bash\ni=0; while [ ! -e "${TS_GO:?}" ] && [ "$i" -lt 1800 ]; do sleep 0.1; i=$((i + 1)); done\nexit 0\n' > "$R22/fx/wait.sh"
( cd "$R22" && git add -A && git commit -qm wait ) >/dev/null 2>&1
A22=$tmp/ambient22; mkdir -p "$A22"
mkdir -p "$A22/gate-work.foreign"
printf '999999\t%s\t0\n' "/nowhere/else/.git" > "$A22/gate-work.foreign/owner"
printf '%s\n' '[ {"name": "waiter", "argv": ["bash", "fx/wait.sh"]} ]' > "$tmp/wait22.json"
printf '%s\n' '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]' > "$tmp/quick22.json"
( cd "$R22" && env TMPDIR="$A22" TS_GO="$tmp/go22" GATE_FULL=1 GATE_TURNSTILE=0 GATE_WALL=0 \
    GATE_LEGS="$tmp/wait22.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out22a" 2>&1 &
h22=$!
# The first bar has SWEPT once its header carries the ambient count: the sweep runs before the count
# and the header is written after both. Its own dir is the one with an owner that is not planted here.
w22=""; i22=0
while [ "$i22" -lt 240 ]; do
  if [ -n "$(hdrkey "$R22" tmpdir_entries)" ]; then
    for d22 in "$A22"/gate-work.*; do
      [ "${d22##*/}" = gate-work.foreign ] && continue
      [ -f "$d22/owner" ] && w22=$d22
    done
  fi
  [ -n "$w22" ] && break
  kill -0 "$h22" 2>/dev/null || break
  sleep 0.5; i22=$((i22 + 1))
done
if [ -n "$w22" ]; then
  # THIS repository's common dir IN THE RUNNER'S OWN SPELLING, read from the live owner record. Under
  # MSYS one directory has two spellings (`/tmp/...` and `/c/Users/.../Temp/...`), so a spelling this
  # arm derived itself could differ from the runner's and red the control for a reason that is not
  # the sweep's. What keeps that read from being the subject grading itself is an IDENTITY check on
  # the directory, not on its spelling: the recorded dir must hold this repository's own
  # `gate-run/current`, read through both paths. The foreign arm below grades the comparison itself.
  c22=$(cut -f2 "$w22/owner" 2>/dev/null)
  { [ -n "$c22" ] && [ -n "$(cat "$R22/.git/gate-run/current" 2>/dev/null)" ] \
      && [ "$(cat "$c22/gate-run/current" 2>/dev/null)" = "$(cat "$R22/.git/gate-run/current" 2>/dev/null)" ]; } \
    && ok "control: the first bar owns a gate-work dir, has swept, and its owner names this repository's git dir" \
    || nope "the first bar's owner record names '$c22', which is not this repository's git dir"
  mkdir -p "$A22/gate-work.deadmine"
  printf '999999\t%s\t0\n' "$c22" > "$A22/gate-work.deadmine/owner"
  ( cd "$R22" && env TMPDIR="$A22" GATE_FULL=1 GATE_TURNSTILE=0 GATE_WALL=0 GATE_LEGS="$tmp/quick22.json" \
      bash $KIT_REL/run-gates.sh ) >"$tmp/out22b" 2>&1
  { [ ! -e "$A22/gate-work.deadmine" ] && grep -q 'sweeping the scratch of a dead bar (pid 999999)' "$tmp/out22b"; } \
    && ok "control: the second bar swept, and announced, a dead bar of THIS repository's scratch" \
    || { nope "the second bar did not sweep a dead bar's scratch, so the two survivals below prove nothing"; tail -4 "$tmp/out22b" | sed 's/^/      /'; }
  # TOOL-aGraftedHelix-8: ONE scratch-swept line for the one dead bar of this repository, and none
  # for the foreign owner the sweep spared.
  hl22=$(awk -F'\t' '$2 == "run-gates" && $3 == "scratch-swept"' "$R22/.git/health.log" 2>/dev/null)
  [ "$(printf '%s' "$hl22" | grep -c .)" = 1 ] && [ "$(printf '%s' "$hl22" | cut -f4)" = "dead bar pid 999999" ] \
    && ok "the dead bar's scratch sweep appended one scratch-swept line naming its pid" \
    || nope "the dead bar's scratch sweep left '$(printf '%s' "$hl22" | tr '\t\n' ' ;')' in the health log, not one scratch-swept line"
  [ -d "$w22" ] && [ -f "$w22/owner" ] \
    && ok "a LIVE bar's scratch survived a second bar's sweep" \
    || nope "a second bar removed the scratch of a bar that was still running"
  [ -f "$A22/gate-work.foreign/owner" ] \
    && ok "a dead bar's scratch whose owner names ANOTHER repository survived" \
    || nope "the sweep removed scratch owned by another repository"
  : > "$tmp/go22"; wait "$h22"; rc22=$?
  { [ "$rc22" = 0 ] && grep -q '^gates GREEN — ' "$tmp/out22a"; } \
    && ok "the first bar's verdict is unchanged by the second bar's sweep (rc 0, GREEN)" \
    || { nope "the first bar's verdict changed after a second bar ran beside it (rc $rc22)"; tail -4 "$tmp/out22a" | sed 's/^/      /'; }
else
  : > "$tmp/go22"; wait "$h22" 2>/dev/null
  nope "the first bar never showed an owned, swept gate-work dir under its ambient TMPDIR, so the live-bar arm has no subject"
  skipped "the dead-owner control: the first bar never established"
  skipped "the live bar's survival: the first bar never established"
  skipped "the foreign owner's survival: the first bar never established"
  skipped "the first bar's verdict: the first bar never established"
  skipped "the scratch-swept health line: the first bar never established"
fi

# ---- 23: ONE BAR PER HOST, and the beacon names its holder (TOOL-aFrugalTurnstile-5 AC1, AC2) -----
# Two REPOSITORIES under one host dir, which the common-dir key let run at once. The holder's leg
# waits on a go-file, released only once the second bar has queued or has registered beside it, so
# neither verdict below rests on a clock. The beacon's fields are read while it is held.
R23a=$tmp/hostA; R23b=$tmp/hostB; mk_repo "$R23a"; mk_repo "$R23b"; B23=$(beacon "$R23a"); S23=$tmp/shared23
mkdir -p "$S23"
printf '#!/usr/bin/env bash\nS=${TS_SHARED:?}\nmkdir -p "$S/live"; mkdir "$S/live/$$"\nls -1 "$S/live" | wc -l >> "$S/peaks"\ni=0; while [ ! -e "$S/go" ] && [ "$i" -lt 1500 ]; do sleep 0.2; i=$((i + 1)); done\nrmdir "$S/live/$$"\nexit 0\n' > "$tmp/hold23.sh"
printf '[ {"name": "hold", "argv": ["bash", "%s"]} ]\n' "$tmp/hold23.sh" > "$tmp/hold23.json"
( cd "$R23a" && env TS_SHARED="$S23" GATE_FULL=1 GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 GATE_LEGS="$tmp/hold23.json" \
    bash $KIT_REL/run-gates.sh ) >"$tmp/out23a" 2>&1 &
h23=$!
i23=0; while [ ! -s "$S23/peaks" ] && kill -0 "$h23" 2>/dev/null && [ "$i23" -lt 2400 ]; do sleep 0.1; i23=$((i23 + 1)); done
{ f23_repo=$(<"$B23/repo"); } 2>/dev/null; { f23_run=$(<"$B23/run"); } 2>/dev/null
{ f23_ttl=$(<"$B23/ttl"); } 2>/dev/null; { f23_pid=$(<"$B23/pid"); } 2>/dev/null
( cd "$R23b" && env TS_SHARED="$S23" GATE_FULL=1 GATE_TURNSTILE_TICK=1 GATE_LEGS="$tmp/hold23.json" \
    bash $KIT_REL/run-gates.sh ) >"$tmp/out23b" 2>&1 &
w23=$!
i23=0
while ! grep -q 'queued at position' "$tmp/out23b" 2>/dev/null && ! grep -q '^ *2' "$S23/peaks" 2>/dev/null \
      && kill -0 "$w23" 2>/dev/null && [ "$i23" -lt 2400 ]; do sleep 0.1; i23=$((i23 + 1)); done
: > "$S23/go"; wait "$w23" 2>/dev/null; wait "$h23" 2>/dev/null
top23=$(unset GIT_DIR GIT_WORK_TREE; cd "$R23a" && git rev-parse --show-toplevel); run23=$(hdrkey "$R23a" run_id)
[ -n "$f23_repo" ] && [ "$f23_repo" = "$top23" ] && ok "the host beacon's repo names the holder's top level" \
  || nope "the host beacon's repo read '$f23_repo', not the holder's top level '$top23'"
[ -n "$f23_run" ] && [ "$f23_run" = "$run23" ] && ok "the host beacon's run is the holder's run id" \
  || nope "the host beacon's run read '$f23_run', not the holder's run id '$run23'"
[ "$f23_ttl" = 600 ] && ok "the host beacon's ttl is the holder's TTL" \
  || nope "the host beacon's ttl read '$f23_ttl', not the holder's 600"
[ "$(peak "$S23")" = 1 ] && ok "two repositories under one host dir never held at once (peak 1)" \
  || nope "two repositories under one host dir ran at once (peak $(peak "$S23"))"
grep -qF "another bar holds this host — $top23 run $run23 pid $f23_pid — queued at position" "$tmp/out23b" \
  && ok "the second repository's queue line names the holder's top level, run id and pid" \
  || { nope "the second repository's bar did not name its holder"; grep -E 'holds|queued' "$tmp/out23b" | sed 's/^/      /'; }

# ---- 24: a runner inside the holder's own leg NESTS rather than queueing (AC3) --------------------
# The deadlock the host key would otherwise create: a suite's scratch-repo bar queued behind the
# very bar whose leg started it. THE CONTROL unsets the inherited nonce in the same leg, and the
# inner bar must then queue; without it, a runner that never queues at all passes the first half.
# The control's inner TTL of 5 bounds its wait at the 20 s fail-open.
R24o=$tmp/nestout; R24i=$tmp/nestin; mk_repo "$R24o"; mk_repo "$R24i"
legs "$R24i" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
# `-u GATE_LEGS` IS LOAD-BEARING: the outer bar's manifest is passed through it, and an inner runner
# that inherited it would run this same leg again, nesting without end.
printf '#!/usr/bin/env bash\ncd "%s" && env -u GATE_LEGS bash %s/run-gates.sh > "%s" 2>&1\nexit 0\n' "$R24i" "$KIT_REL" "$tmp/out24in" > "$tmp/nest24.sh"
printf '#!/usr/bin/env bash\ncd "%s" && env -u GATE_LEGS -u GATE_TURNSTILE_HOLDER GATE_TURNSTILE_TTL=5 bash %s/run-gates.sh > "%s" 2>&1\nexit 0\n' "$R24i" "$KIT_REL" "$tmp/out24un" > "$tmp/unnest24.sh"
printf '[ {"name": "nest", "argv": ["bash", "%s"]} ]\n' "$tmp/nest24.sh" > "$tmp/nest24.json"
printf '[ {"name": "unnest", "argv": ["bash", "%s"]} ]\n' "$tmp/unnest24.sh" > "$tmp/unnest24.json"
( cd "$R24o" && env GATE_FULL=1 GATE_TURNSTILE_TTL=5 GATE_TURNSTILE_TICK=1 GATE_LEGS="$tmp/nest24.json" bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
grep -q '^gate queue: nested under ' "$tmp/out24in" 2>/dev/null && ok "a runner started by the holder's leg prints that it is nested" \
  || { nope "a runner started by the holder's leg did not nest"; tail -4 "$tmp/out24in" 2>/dev/null | sed 's/^/      /'; }
[ "$(hdrkey "$R24i" queued_from)" = nested ] && ok "the nested run's header reads queued_from nested" \
  || nope "the nested run's header reads queued_from '$(hdrkey "$R24i" queued_from)', not nested"
grep -q 'queued at position' "$tmp/out24in" 2>/dev/null && nope "the nested runner queued behind its own parent" \
  || ok "the nested runner took no place in the queue"
# The control's OUTER bar runs a TTL of 30 and its inner one 5: the inner waits out 20 s at most,
# and judges the holder by the holder's 30, so a heartbeat a loaded host delays past 5 s is no reap.
( cd "$R24o" && env GATE_FULL=1 GATE_TURNSTILE_TTL=30 GATE_TURNSTILE_TICK=1 GATE_LEGS="$tmp/unnest24.json" bash $KIT_REL/run-gates.sh ) >/dev/null 2>&1
grep -q 'queued at position' "$tmp/out24un" 2>/dev/null && ok "control: with the nonce unset in the same leg, the inner runner queues" \
  || { nope "control: with the nonce unset the inner runner did not queue, so the nesting half proves nothing"; grep -E 'gate queue|reaping|holds|EXPIRED' "$tmp/out24un" 2>/dev/null | sed 's/^/      /'; }

# ---- 25: staleness is judged by the HOLDER's ttl (AC5) --------------------------------------------
# A live holder whose heartbeat is 400 s old is fresh under its own ttl of 600 and stale under the
# waiter's 60. The waiter must queue, not reap, and the beacon must outlive the killed waiter; with
# the beacon's ttl removed, as an older runner writes it, the waiter's own 60 s applies and it reaps.
R25=$tmp/hostttl; mk_repo "$R25"; B25=$(beacon "$R25")
legs "$R25" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
sleep 300 & hp25=$!
mkdir -p "$B25"; printf '%s' "$hp25" > "$B25/pid"; printf '%s' $(( $(date +%s) - 400 )) > "$B25/heartbeat"
printf 'planted' > "$B25/nonce"; printf '600' > "$B25/ttl"
( cd "$R25" && exec env GATE_FULL=1 GATE_TURNSTILE_TTL=60 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >"$tmp/out25a" 2>&1 &
w25=$!
i25=0; while ! grep -q 'queued at position\|reaping' "$tmp/out25a" 2>/dev/null && kill -0 "$w25" 2>/dev/null && [ "$i25" -lt 1200 ]; do sleep 0.1; i25=$((i25 + 1)); done
kill "$w25" 2>/dev/null; wait "$w25" 2>/dev/null
grep -q 'another bar holds this host' "$tmp/out25a" && ok "a holder fresh under its own ttl is queued behind" \
  || nope "a holder fresh under its own ttl of 600 was not queued behind"
grep -q 'reaping' "$tmp/out25a" && nope "the waiter reaped a holder by its OWN ttl of 60 rather than the holder's 600" \
  || ok "no reaping line for a holder fresh under its own ttl"
[ -d "$B25" ] && ok "the holder's beacon survived the waiter" || nope "the holder's beacon was removed while it was fresh under its own ttl"
rm -f "$B25/ttl"
out25b=$( cd "$R25" && env GATE_FULL=1 GATE_TURNSTILE_TTL=60 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 )
printf '%s' "$out25b" | grep -q 'reaping the beacon of a stalled holder (heartbeat [0-9]*s old, ttl 60s)' \
  && ok "a beacon with no ttl is judged by the waiter's own (stalled, ttl 60s)" \
  || nope "a beacon with no ttl was not reaped as stalled under the waiter's ttl 60s"
kill "$hp25" 2>/dev/null; wait "$hp25" 2>/dev/null; rm -rf "$B25"

# ---- 26: `--hold -- <command…>` admits a bar that is not the runner (AC6, AC7) ---------------------
# The command's status is the run's, the beacon is gone afterwards, the command sees the holder's
# nonce, and no run record is written. The probe is a file so no quoting crosses the runner.
R26=$tmp/holdverb; mk_repo "$R26"; B26=$(beacon "$R26")
legs "$R26" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
cat > "$tmp/probe26.sh" <<'P26'
echo "holder=${GATE_TURNSTILE_HOLDER:-}"
echo "nonce=$(cat "$GATE_TURNSTILE_DIR/gate-bar-beacon/nonce" 2>/dev/null)"
P26
out26=$( cd "$R26" && bash $KIT_REL/run-gates.sh --hold -- false 2>&1 ); rc26=$?
{ [ "$rc26" = 1 ] && ! printf '%s' "$out26" | grep -q 'gates GREEN'; } && ok "--hold -- false exits 1 and runs no leg" \
  || nope "--hold -- false exited $rc26 (or ran the legs)"
[ -d "$B26" ] && nope "--hold left its beacon behind" || ok "--hold released its beacon"
out26=$( cd "$R26" && bash $KIT_REL/run-gates.sh --hold -- bash "$tmp/probe26.sh" 2>&1 )
h26=$(printf '%s\n' "$out26" | sed -n 's/^holder=//p'); n26=$(printf '%s\n' "$out26" | sed -n 's/^nonce=//p')
[ -n "$h26" ] && [ "$h26" = "$n26" ] && ok "the held command sees GATE_TURNSTILE_HOLDER equal to the beacon's nonce" \
  || nope "the held command saw holder '$h26' against the beacon's nonce '$n26'"
( cd "$R26" && bash $KIT_REL/run-gates.sh --hold -- true ) >/dev/null 2>&1 && ok "--hold -- true exits 0" || nope "--hold -- true did not exit 0"
[ -e "$R26/.git/gate-run" ] && nope "--hold wrote a run record" || ok "--hold wrote no run record"
out26=$( cd "$R26" && bash $KIT_REL/run-gates.sh --hold 2>&1 ); rc26=$?
{ [ "$rc26" = 2 ] && printf '%s' "$out26" | grep -q -- '--hold needs a command'; } && ok "--hold with no command exits 2 with its usage line" \
  || nope "--hold with no command exited $rc26: $(printf '%s' "$out26" | tail -1)"

# ---- 27: an unusable host dir falls back to the common dir, announced (AC12) ----------------------
R27=$tmp/hostfile; mk_repo "$R27"; : > "$tmp/hostfile27"
legs "$R27" '[ {"name": "long", "argv": ["bash", "fx/long.sh"]} ]'
( cd "$R27" && env GATE_TURNSTILE_DIR="$tmp/hostfile27" GATE_FULL=1 TS_LONG=6 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >"$tmp/out27" 2>&1 &
h27=$!; seen27=0
i27=0; while kill -0 "$h27" 2>/dev/null && [ "$i27" -lt 2400 ]; do [ -d "$R27/.git/gate-bar-beacon" ] && { seen27=1; break; }; sleep 0.1; i27=$((i27 + 1)); done
wait "$h27" 2>/dev/null
grep -q 'could not be created, so this bar queues per repository' "$tmp/out27" && ok "an unusable host dir is announced" \
  || nope "an unusable host dir fell back silently, or not at all"
[ "$seen27" = 1 ] && ok "the fallback beacon was claimed under the repository's common dir" \
  || nope "no beacon appeared under the repository's common dir when the host dir was unusable"

# ---- 28: the default host dir is spelled identically by every reader (AC10) ------------------------
# A reader of another spelling probes a queue no bar writes and reports "no interrupted act" over it.
spell28='GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile'
[ "$(grep -cF "$spell28" "$HERE/run-gates.sh")" -ge 1 ] && ok "the runner spells the default host dir" \
  || nope "the runner does not spell the default host dir as '$spell28'"
if ua28=$(resolve_kit_dir "$_rkd_py" unattended unattended.sh "$HERE" 2>/dev/null) && [ -f "$ROOT/$ua28/unattended.sh" ]; then
  [ "$(grep -cF "$spell28" "$ROOT/$ua28/unattended.sh")" -ge 1 ] && ok "the unattended driver spells it identically" \
    || nope "the unattended driver reads the turnstile queue under another spelling"
else
  skipped "the unattended driver's spelling: that kit is not installed in this tree"
fi

# ================= TOOL-aPairedSlots-2: the turnstile as a COUNTING SEMAPHORE ===================
# Every arm below runs its bars at GATE_TURNSTILE_SLOTS=2 under the suite's own host dir, each bar in
# a repository of its own, so the arms stay true once a worktree may hold only one slot
# (TOOL-aPairedSlots-5). A hold leg registers, then waits on its own go-file, so no verdict rests on
# a clock: an arm releases its holders only after it has read what it asserts.
printf '#!/usr/bin/env bash\nS=${TS_SHARED:?}\nmkdir -p "$S/live"; mkdir "$S/live/$$"\nls -1 "$S/live" | wc -l >> "$S/peaks"\ni=0; while [ ! -e "$S/go" ] && [ "$i" -lt 1500 ]; do sleep 0.2; i=$((i + 1)); done\nrmdir "$S/live/$$"\nexit 0\n' > "$tmp/holdS.sh"
printf '[ {"name": "hold", "argv": ["bash", "%s"]} ]\n' "$tmp/holdS.sh" > "$tmp/holdS.json"
# run_slot_bar <repo> <shared dir> <out file> [VAR=value…] — a backgrounded two-slot bar running the hold leg; its pid in SLOT_PID
run_slot_bar() {
  local r=$1 s=$2 o=$3; shift 3
  ( cd "$r" && env TS_SHARED="$s" GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 \
      GATE_LEGS="$tmp/holdS.json" "$@" bash $KIT_REL/run-gates.sh ) >"$o" 2>&1 &
  SLOT_PID=$!
}
# check_registered <shared dir> <count> <pid> — until <count> holders have registered there, or <pid> exits
check_registered() {
  # THE COUNT DEFAULTS TO 0. `grep -c` over a file not yet written prints nothing, and an empty
  # operand makes the comparison an error, which ended this loop at once and let an arm read the
  # beacons before any holder had registered: observed on the first slice of these arms.
  local i=0 c
  while :; do
    c=$(grep -c . "$1/peaks" 2>/dev/null); c=${c:-0}
    [ "$c" -lt "$2" ] && kill -0 "$3" 2>/dev/null && [ "$i" -lt 2400 ] || break
    sleep 0.1; i=$((i + 1))
  done
}
BS=$(beacon x)

# ---- 29: with slots=2 two bars hold at once and a third queues (AC1); its line names both (AC2) -------
R29a=$tmp/slotA; R29b=$tmp/slotB; R29c=$tmp/slotC; mk_repo "$R29a"; mk_repo "$R29b"; mk_repo "$R29c"
S29=$tmp/shared29; mkdir -p "$S29"
run_slot_bar "$R29a" "$S29" "$tmp/out29a"; p29a=$SLOT_PID; check_registered "$S29" 1 "$p29a"
run_slot_bar "$R29b" "$S29" "$tmp/out29b"; p29b=$SLOT_PID; check_registered "$S29" 2 "$p29b"
{ h29a=$(<"$BS/pid"); } 2>/dev/null; { h29b=$(<"$BS.2/pid"); } 2>/dev/null
run_slot_bar "$R29c" "$tmp/shared29c" "$tmp/out29c"; p29c=$SLOT_PID; mkdir -p "$tmp/shared29c"; : > "$tmp/shared29c/go"
i29=0; while ! grep -q 'queued at position' "$tmp/out29c" 2>/dev/null && kill -0 "$p29c" 2>/dev/null && [ "$i29" -lt 2400 ]; do sleep 0.1; i29=$((i29 + 1)); done
peak29=$(peak "$S29")
: > "$S29/go"; wait "$p29a" "$p29b" "$p29c" 2>/dev/null
[ "$peak29" = 2 ] && ok "slots=2: two bars held at once (peak 2)" || nope "slots=2: the occupancy peak was $peak29, not 2"
grep -q 'queued at position' "$tmp/out29c" && ok "slots=2: the third bar queued" \
  || { nope "slots=2: the third bar did not queue behind two holders"; tail -4 "$tmp/out29c" | sed 's/^/      /'; }
grep -q "2 of 2 bar slots on this host are held — .*pid $h29a.*pid $h29b\|2 of 2 bar slots on this host are held — .*pid $h29b.*pid $h29a" "$tmp/out29c" \
  && ok "the third bar's queue line counts two of two slots held and names both holders' pids" \
  || { nope "the third bar's queue line did not name both holders ($h29a, $h29b)"; grep -E 'held|queued' "$tmp/out29c" | sed 's/^/      /'; }
[ "$(hdrkey "$R29c" slots)" = 2 ] && ok "the third bar's header records slots 2" || nope "the third bar's header records slots '$(hdrkey "$R29c" slots)'"
s29a=$(hdrkey "$R29a" slot); s29b=$(hdrkey "$R29b" slot)
{ [ "$s29a" = 1 ] && [ "$s29b" = 2 ]; } || { [ "$s29a" = 2 ] && [ "$s29b" = 1 ]; } \
  && ok "the two holders' headers record slots 1 and 2" || nope "the two holders' headers record slot '$s29a' and '$s29b'"

# ---- 30: a dead slot is reaped while the other holder keeps running (AC3) ---------------------------
R30a=$tmp/reapA; R30b=$tmp/reapB; mk_repo "$R30a"; mk_repo "$R30b"; S30=$tmp/shared30; mkdir -p "$S30"
legs "$R30b" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
run_slot_bar "$R30a" "$S30" "$tmp/out30a"; p30a=$SLOT_PID; check_registered "$S30" 1 "$p30a"
{ n30a=$(<"$BS/nonce"); } 2>/dev/null
sh -c 'exit 0' & dead30=$!; wait "$dead30" 2>/dev/null
mkdir -p "$BS.2"; printf '%s' "$dead30" > "$BS.2/pid"; printf '%s' "$(date +%s)" > "$BS.2/heartbeat"; printf 'planted30' > "$BS.2/nonce"
out30=$( cd "$R30b" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh 2>&1 ); rc30=$?
alive30=0; kill -0 "$p30a" 2>/dev/null && alive30=1
{ n30after=$(<"$BS/nonce"); } 2>/dev/null
: > "$S30/go"; wait "$p30a" 2>/dev/null
[ "$(printf '%s\n' "$out30" | grep -c 'reaping the beacon of a dead holder')" = 1 ] && ok "the dead slot was reaped once" \
  || nope "the dead slot was not reaped exactly once"
[ "$rc30" = 0 ] && printf '%s\n' "$out30" | grep -q '^gate queue: acquired' && ok "the bar behind it claimed and ran" \
  || nope "the bar behind the dead slot did not claim and run (rc $rc30)"
[ "$alive30" = 1 ] && [ -n "$n30a" ] && [ "$n30after" = "$n30a" ] && ok "the live holder of slot 1 ran on, its nonce untouched" \
  || nope "the live holder of slot 1 was disturbed (alive $alive30, nonce '$n30a' then '$n30after')"

# ---- 31: a release frees only its own slot, never a sibling's or a successor's (AC4) ------------------
R31w=$tmp/relW; R31x=$tmp/relX; mk_repo "$R31w"; mk_repo "$R31x"; S31w=$tmp/shared31w; S31x=$tmp/shared31x; mkdir -p "$S31w" "$S31x"
run_slot_bar "$R31w" "$S31w" "$tmp/out31w"; p31w=$SLOT_PID; check_registered "$S31w" 1 "$p31w"
run_slot_bar "$R31x" "$S31x" "$tmp/out31x"; p31x=$SLOT_PID; check_registered "$S31x" 1 "$p31x"
n31w=$(cat "$BS/nonce" 2>/dev/null)
# X holds slot 2. Its nonce is replaced, as a successor's claim after a reap would replace it.
printf 'successor31' > "$BS.2/nonce"
: > "$S31x/go"; wait "$p31x" 2>/dev/null
[ -d "$BS.2" ] && [ "$(cat "$BS.2/nonce" 2>/dev/null)" = successor31 ] && ok "a run whose slot was re-claimed left the successor's beacon" \
  || nope "a run whose slot was re-claimed removed the successor's beacon"
[ -d "$BS" ] && [ "$(cat "$BS/nonce" 2>/dev/null)" = "$n31w" ] && ok "a release left the other slot's holder in place" \
  || nope "a release freed another slot's beacon"
rm -rf "$BS.2"; : > "$S31w/go"; wait "$p31w" 2>/dev/null

# ---- 32: a runner started by the slot-2 holder's leg NESTS (AC5) -------------------------------------
R32w=$tmp/nestW; R32o=$tmp/nestO; R32i=$tmp/nestI; mk_repo "$R32w"; mk_repo "$R32o"; mk_repo "$R32i"; S32=$tmp/shared32; mkdir -p "$S32"
legs "$R32i" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
# The inner runner's TTL of 5 bounds a run that FAILS to nest at a 20 s fail-open, as arm 24's control
# is bounded; a nested run never waits, so the bound costs a passing run nothing.
# AT ONE SLOT (TOOL-aPairedSlots-15): the inner runner's own count holds no slot 2, so only a nesting
# test that reads every beacon present finds its parent, which is the case the glob exists for.
printf '#!/usr/bin/env bash\ncd "%s" && env -u GATE_LEGS GATE_TURNSTILE_SLOTS=1 GATE_TURNSTILE_TTL=5 bash %s/run-gates.sh > "%s" 2>&1\nexit 0\n' "$R32i" "$KIT_REL" "$tmp/out32in" > "$tmp/nest32.sh"
printf '[ {"name": "nest", "argv": ["bash", "%s"]} ]\n' "$tmp/nest32.sh" > "$tmp/nest32.json"
run_slot_bar "$R32w" "$S32" "$tmp/out32w"; p32w=$SLOT_PID; check_registered "$S32" 1 "$p32w"
( cd "$R32o" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 GATE_LEGS="$tmp/nest32.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out32o" 2>&1
s32o=$(hdrkey "$R32o" slot)
: > "$S32/go"; wait "$p32w" 2>/dev/null
[ "$s32o" = 2 ] && ok "the outer bar held slot 2 beside slot 1's holder" || nope "the outer bar held slot '$s32o', not 2"
grep -q '^gate queue: nested under ' "$tmp/out32in" 2>/dev/null && ok "a runner started by the slot-2 holder's leg nests" \
  || { nope "a runner started by the slot-2 holder's leg did not nest"; tail -4 "$tmp/out32in" 2>/dev/null | sed 's/^/      /'; }

# ---- 33: at the default count a bar writes no slot key (AC6) --------------------------------------
# A FIXTURE TABLE WITH NO `slots` KEY (TOOL-aPairedSlots-15): the copied real table is tuned data, and
# the day it gains a key this arm would stop testing the default.
printf 't\t0\t0\twidth=2,timeout=0,wall=0,mempause=0\n' > "$tmp/noslots.txt"
R33=$tmp/slots1; mk_repo "$R33"; legs "$R33" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R33" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS= GATE_PROFILES="$tmp/noslots.txt" GATE_PROFILE= bash $KIT_REL/run-gates.sh ) >"$tmp/out33" 2>&1
[ -z "$(hdrkey "$R33" slots)" ] && [ -z "$(hdrkey "$R33" slot)" ] && ok "a bar at the default count writes neither slots nor slot" \
  || nope "a bar at the default count wrote a slot key"
grep -q 'bar slots' "$tmp/out33" && nope "a bar at the default count printed a slots clause" || ok "a bar at the default count printed no slots clause"


# ================= TOOL-aPairedSlots-3: the shared dispatch width =================================
# A bar that acquires slot 2 while slot 1 is held reads the held count once and takes the width its
# rule names. The rule is a constant in the runner, `TS_SHARE_RULE`, so each arm sets it in the
# fixture repository's own runner copy; the profile is a fixture row of width 4.
printf 't\t0\t0\twidth=4,timeout=0,wall=0,mempause=0\n' > "$tmp/w4.txt"
# set_share_rule <repo> <rule> — the fixture runner's TS_SHARE_RULE, asserted to have moved
set_share_rule() {
  sed -i "s/^TS_SHARE_RULE=.*/TS_SHARE_RULE=$2/" "$1/$KIT_REL/run-gates.sh"
  grep -q "^TS_SHARE_RULE=$2\$" "$1/$KIT_REL/run-gates.sh"
}
# run_beside_holder <repo> <out> [VAR=value…] — a quick-leg bar run while a slot-1 holder waits
run_beside_holder() {
  local r=$1 o=$2 s; shift 2
  s=$tmp/sharedW.$RANDOM; mkdir -p "$s"
  run_slot_bar "$WIDTH_W" "$s" "$o.w"; local pw=$SLOT_PID; check_registered "$s" 1 "$pw"
  ( cd "$r" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_PROFILES="$tmp/w4.txt" GATE_PROFILE= GATE_JOBS= "$@" \
      bash $KIT_REL/run-gates.sh ) >"$o" 2>&1
  : > "$s/go"; wait "$pw" 2>/dev/null
}
WIDTH_W=$tmp/widthW; mk_repo "$WIDTH_W"

# ---- 34: under `half` the bar beside a holder dispatches at half width; under `full` at full (AC1) ---
R34h=$tmp/widthHalf; R34f=$tmp/widthFull; mk_repo "$R34h"; mk_repo "$R34f"
legs "$R34h" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'; legs "$R34f" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
if set_share_rule "$R34h" half && set_share_rule "$R34f" full; then
  run_beside_holder "$R34h" "$tmp/out34h"; run_beside_holder "$R34f" "$tmp/out34f"
  grep -q '^gate profile: width 2 at dispatch — 2 of 2 bar slots held (half)$' "$tmp/out34h" && [ "$(hdrkey "$R34h" width)" = 2 ] \
    && ok "half: the bar beside a holder dispatched at width 2 and its header records 2" \
    || { nope "half: no width-2 dispatch line, or the header width reads '$(hdrkey "$R34h" width)'"; grep 'gate profile' "$tmp/out34h" | sed 's/^/      /'; }
  grep -q '^gate profile: width 4 at dispatch — 2 of 2 bar slots held (full)$' "$tmp/out34f" && [ "$(hdrkey "$R34f" width)" = 4 ] \
    && ok "full: the bar beside a holder dispatched at width 4 and its header records 4" \
    || { nope "full: no width-4 dispatch line, or the header width reads '$(hdrkey "$R34f" width)'"; grep 'gate profile' "$tmp/out34f" | sed 's/^/      /'; }
else
  nope "the fixture runner carries no TS_SHARE_RULE line to set, so the width arms grade nothing"
fi

# ---- 35: the operator's GATE_JOBS is never divided (AC2) -----------------------------------------
R35=$tmp/widthJobs; mk_repo "$R35"; legs "$R35" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
if set_share_rule "$R35" half; then
  run_beside_holder "$R35" "$tmp/out35" GATE_JOBS=3
  [ "$(hdrkey "$R35" width)" = 3 ] && ok "half beside a holder: GATE_JOBS=3 dispatched at 3" \
    || nope "half beside a holder: GATE_JOBS=3 dispatched at '$(hdrkey "$R35" width)'"
else
  nope "the fixture runner carries no TS_SHARE_RULE line to set"
fi

# ---- 36: a bar alone prints no dispatch line and keeps the profile's width (AC3) -----------------
R36=$tmp/widthAlone; mk_repo "$R36"; legs "$R36" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
if set_share_rule "$R36" half; then
  ( cd "$R36" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_PROFILES="$tmp/w4.txt" GATE_PROFILE= GATE_JOBS= bash $KIT_REL/run-gates.sh ) >"$tmp/out36" 2>&1
  grep -q 'at dispatch' "$tmp/out36" && nope "a bar holding the only held slot printed a dispatch line" \
    || ok "a bar holding the only held slot printed no dispatch line"
  [ "$(hdrkey "$R36" width)" = 4 ] && ok "and its header records the profile's width 4" || nope "and its header records width '$(hdrkey "$R36" width)'"
else
  nope "the fixture runner carries no TS_SHARE_RULE line to set"
fi

# ---- 37: two concurrent bars pause on ONE host reading (AC4) -------------------------------------
# The memory pause reads a host-wide source, so two bars share it with no second mechanism. One
# GATE_MEMINFO file at 95 % used under a 90 % threshold, two bars of two legs each: the second leg's
# dispatch waits while the first runs, in BOTH bars.
printf 'MemTotal: 1000 kB\nMemAvailable: 50 kB\n' > "$tmp/mem95"
printf '#!/usr/bin/env bash\nsleep 2\nexit 0\n' > "$tmp/slow37.sh"
printf '[ {"name": "slow", "argv": ["bash", "%s"]}, {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]\n' "$tmp/slow37.sh" > "$tmp/legs37.json"
R37a=$tmp/memA; R37b=$tmp/memB; mk_repo "$R37a"; mk_repo "$R37b"
for r37 in "$R37a" "$R37b"; do
  ( cd "$r37" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 GATE_JOBS=2 GATE_MEMPAUSE=90 GATE_MEMINFO="$tmp/mem95" GATE_LEGS="$tmp/legs37.json" \
      bash $KIT_REL/run-gates.sh ) >"$tmp/out37.${r37##*/}" 2>&1 &
done
wait
for r37 in "$R37a" "$R37b"; do
  id37=$(cat "$r37/.git/gate-run/current" 2>/dev/null)
  [ -s "$r37/.git/gate-run/$id37/pauses" ] && ok "bar ${r37##*/} paused on the shared host reading" \
    || nope "bar ${r37##*/} did not pause on the shared host reading"
done

# ================= TOOL-aPairedSlots-4: the docs key ===============================================
# A doc-only bar is one whose GATE_DOCS_BASE resolves, with GATE_FULL unset. Each fixture repository
# gets a second commit touching a doc path, so `GATE_DOCS_BASE=HEAD~1` names a real base. The non-doc
# holder below runs at the kit default of one slot, so a doc-only bar that queued would wait behind it.
build_docs_repo() { # <dir> — mk_repo plus a second commit, so HEAD~1 resolves
  mk_repo "$1" || return 1
  printf 'doc\n' > "$1/NOTES.md"; ( cd "$1" && git add -A && git commit -qm doc ) >/dev/null 2>&1
}
# run_docs_bar <repo> <out> [VAR=value…] — a doc-only bar in the foreground
run_docs_bar() {
  local r=$1 o=$2; shift 2
  ( cd "$r" && env GATE_FULL= GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_TICK=1 "$@" bash $KIT_REL/run-gates.sh ) >"$o" 2>&1
}
DK=$GATE_TURNSTILE_DIR/gate-docs-beacon

# ---- 38: a doc-only bar is admitted at once while a non-doc bar holds the only slot (AC1) ----------
R38w=$tmp/docsW; R38d=$tmp/docsD; mk_repo "$R38w"; build_docs_repo "$R38d"; S38=$tmp/shared38; mkdir -p "$S38"
legs "$R38d" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R38w" && env TS_SHARED="$S38" GATE_FULL=1 GATE_TURNSTILE_SLOTS= GATE_PROFILES="$tmp/noslots.txt" GATE_PROFILE= GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 \
    GATE_LEGS="$tmp/holdS.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out38w" 2>&1 &
p38w=$!; check_registered "$S38" 1 "$p38w"
run_docs_bar "$R38d" "$tmp/out38d"
held38=0; kill -0 "$p38w" 2>/dev/null && held38=1
: > "$S38/go"; wait "$p38w" 2>/dev/null
grep -q '^gate queue: docs-only — admitted on the docs key, not queued$' "$tmp/out38d" && [ "$held38" = 1 ] \
  && ok "a doc-only bar was admitted on the docs key and finished while the non-doc holder still ran" \
  || { nope "a doc-only bar was not admitted at once beside the non-doc holder (holder alive: $held38)"; grep -E 'gate queue|queued' "$tmp/out38d" | sed 's/^/      /'; }
grep -q 'queued at position' "$tmp/out38d" && nope "the doc-only bar took a ticket and queued" || ok "the doc-only bar took no place in the queue"
[ "$(hdrkey "$R38d" queued_from)" = docs ] && ok "its header records queued_from docs" \
  || nope "its header records queued_from '$(hdrkey "$R38d" queued_from)'"

# ---- 39: a doc-only bar's release frees its own run id and no other (AC2) --------------------------
R39a=$tmp/docsA; R39b=$tmp/docsB; build_docs_repo "$R39a"; build_docs_repo "$R39b"; S39=$tmp/shared39; mkdir -p "$S39"
legs "$R39b" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R39a" && env TS_SHARED="$S39" GATE_FULL= GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_TICK=1 \
    GATE_LEGS="$tmp/holdS.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out39a" 2>&1 &
p39a=$!; check_registered "$S39" 1 "$p39a"
run_docs_bar "$R39b" "$tmp/out39b"
run39a=$(hdrkey "$R39a" run_id); run39b=$(hdrkey "$R39b" run_id)
[ -n "$run39a" ] && [ -d "$DK/$run39a" ] && ok "the live doc-only bar's beacon stood while its neighbour released" \
  || nope "the live doc-only bar's beacon was gone after its neighbour released"
[ -n "$run39b" ] && [ ! -e "$DK/$run39b" ] && ok "the finished doc-only bar's own beacon is gone" \
  || nope "the finished doc-only bar left its beacon behind"
: > "$S39/go"; wait "$p39a" 2>/dev/null

# ---- 40: a runner started by a doc-only bar's leg nests (AC3) --------------------------------------
R40o=$tmp/docsO; R40i=$tmp/docsI; build_docs_repo "$R40o"; mk_repo "$R40i"
legs "$R40i" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
printf '#!/usr/bin/env bash\ncd "%s" && env -u GATE_LEGS GATE_TURNSTILE_TTL=5 bash %s/run-gates.sh > "%s" 2>&1\nexit 0\n' "$R40i" "$KIT_REL" "$tmp/out40in" > "$tmp/nest40.sh"
printf '[ {"name": "nest", "argv": ["bash", "%s"]} ]\n' "$tmp/nest40.sh" > "$tmp/nest40.json"
run_docs_bar "$R40o" "$tmp/out40o" GATE_LEGS="$tmp/nest40.json"
grep -q '^gate queue: nested under ' "$tmp/out40in" 2>/dev/null && ok "a runner started by a doc-only bar's leg nests" \
  || { nope "a runner started by a doc-only bar's leg did not nest"; tail -3 "$tmp/out40in" 2>/dev/null | sed 's/^/      /'; }

# ---- 41: the docs key is not a slot, and a full bar is never doc-only (AC4) ------------------------
R41d=$tmp/docsHold; R41n=$tmp/docsNon; R41f=$tmp/docsFull; build_docs_repo "$R41d"; mk_repo "$R41n"; build_docs_repo "$R41f"
S41=$tmp/shared41; mkdir -p "$S41"
legs "$R41n" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'; legs "$R41f" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
( cd "$R41d" && env TS_SHARED="$S41" GATE_FULL= GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_TICK=1 \
    GATE_LEGS="$tmp/holdS.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out41d" 2>&1 &
p41d=$!; check_registered "$S41" 1 "$p41d"
( cd "$R41n" && env GATE_FULL=1 GATE_TURNSTILE_SLOTS=2 bash $KIT_REL/run-gates.sh ) >"$tmp/out41n" 2>&1
( cd "$R41f" && env GATE_FULL=1 GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_SLOTS= GATE_PROFILES="$tmp/noslots.txt" GATE_PROFILE= bash $KIT_REL/run-gates.sh ) >"$tmp/out41f" 2>&1
: > "$S41/go"; wait "$p41d" 2>/dev/null
grep -q '^gate queue: waited 0s$' "$tmp/out41n" && ! grep -q 'at dispatch' "$tmp/out41n" \
  && ok "a non-doc bar beside a doc-only holder waited 0s and took no shared width" \
  || nope "a non-doc bar beside a doc-only holder waited or was narrowed"
[ "$(hdrkey "$R41f" queued_from)" = held ] && ! grep -q 'docs-only' "$tmp/out41f" \
  && ok "a full bar with GATE_DOCS_BASE set took a slot as a non-doc bar" \
  || nope "a full bar with GATE_DOCS_BASE set took the docs key (queued_from '$(hdrkey "$R41f" queued_from)')"

# ---- 42: a dead docs beacon is swept by the next doc-only bar (AC5) --------------------------------
R42=$tmp/docsSweep; build_docs_repo "$R42"; legs "$R42" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
sh -c 'exit 0' & dead42=$!; wait "$dead42" 2>/dev/null
mkdir -p "$DK/planted42"; printf '%s' "$dead42" > "$DK/planted42/pid"; printf '%s' "$(date +%s)" > "$DK/planted42/heartbeat"; printf 'p42' > "$DK/planted42/nonce"
run_docs_bar "$R42" "$tmp/out42"
grep -q 'sweeping the docs beacon of a dead holder' "$tmp/out42" && [ ! -e "$DK/planted42" ] \
  && ok "a dead docs beacon was swept by the next doc-only bar" || nope "a dead docs beacon was left standing"

# ================= TOOL-aPairedSlots-5: one slot per worktree =====================================
# Two bars in ONE worktree would share every file under its git dir, so the claim refuses a second
# slot to a worktree that holds one; two worktrees of one repository are two git dirs and run at once.

# ---- 43: one worktree holds one slot, two worktrees of one repository hold two (AC1) ---------------
R43=$tmp/wtOne; mk_repo "$R43"; S43=$tmp/shared43; mkdir -p "$S43"
# AUTOCRLF OFF BEFORE THE CHECKOUT: a host whose global config converts line endings checks the
# second worktree out with CRLF, and its runner then refuses the table on a carriage return after its 90 (observed on node a).
( cd "$R43" && git config core.autocrlf false && git worktree add -q -b w2 "$tmp/wtTwo" ) >/dev/null 2>&1
run_slot_bar "$R43" "$S43" "$tmp/out43a"; p43a=$SLOT_PID; check_registered "$S43" 1 "$p43a"
h43a=$(cat "$BS/pid" 2>/dev/null)
run_slot_bar "$R43" "$S43" "$tmp/out43b"; p43b=$SLOT_PID
i43=0; while ! grep -q 'queued at position' "$tmp/out43b" 2>/dev/null && kill -0 "$p43b" 2>/dev/null && [ "$i43" -lt 2400 ]; do sleep 0.1; i43=$((i43 + 1)); done
peak43=$(peak "$S43")
: > "$S43/go"; wait "$p43a" "$p43b" 2>/dev/null
[ "$peak43" = 1 ] && ok "two bars in one worktree never held at once (peak 1)" || nope "two bars in one worktree held at once (peak $peak43)"
grep -q "held, and this worktree's bar holds slot 1 — .*pid $h43a" "$tmp/out43b" && ok "the second bar's queue line names this worktree's holder" \
  || { nope "the second bar's queue line did not name this worktree's holder"; grep -E 'held|queued' "$tmp/out43b" | sed 's/^/      /'; }
S43w=$tmp/shared43w; mkdir -p "$S43w"
if [ -d "$tmp/wtTwo/$KIT_REL" ]; then
  run_slot_bar "$R43" "$S43w" "$tmp/out43c"; p43c=$SLOT_PID; check_registered "$S43w" 1 "$p43c"
  run_slot_bar "$tmp/wtTwo" "$S43w" "$tmp/out43d"; p43d=$SLOT_PID; check_registered "$S43w" 2 "$p43d"
  peak43w=$(peak "$S43w")
  : > "$S43w/go"; wait "$p43c" "$p43d" 2>/dev/null
  [ "$peak43w" = 2 ] && ok "two worktrees of one repository held at once (peak 2)" || nope "two worktrees of one repository did not hold at once (peak $peak43w)"
else
  nope "the second worktree was not created, so the two-worktree half grades nothing"
fi

# ================= TOOL-aPairedSlots-15: the closing review's mediums and lows ======================

# ---- 44: a reap judges the holder whose nonce guards the removal (AC1) -------------------------------
# Sourced, not run: the runner's `ts_try_reap` and `scan_dead_docs_beacons`, each pid read routed
# through a reader that swaps the beacon's nonce as it reads, as a successor claiming the slot between
# the judgement and the removal would. Pid 999999 is dead to the runner's own `ts_alive`. A reap that
# read the nonce first spares the successor; one that read it after the pid, or that does not re-read
# it, deletes it. The routed count is asserted, so a runner whose pid read changed spelling reds here.
F44=$tmp/reap44; mkdir -p "$F44/slot" "$F44/docs/b"
for d44 in "$F44/slot" "$F44/docs/b"; do
  printf '999999' > "$d44/pid"; printf '%s' "$(date +%s)" > "$d44/heartbeat"; printf 'judged' > "$d44/nonce"
done
(
  eval "$(sed -n '/^num_ok() {/p;/^ts_now()/p;/^ts_alive()/p;/^ts_try_reap() {/,/^}/p;/^scan_dead_docs_beacons() {/,/^}/p' \
    "$HERE/run-gates.sh" | sed 's|cat "\$d/pid"|read_pid_and_swap "$d"|')"
  read_pid_and_swap() { cat "$1/pid"; printf 'successor' > "$1/nonce"; }
  add_health_event() { :; }
  TS_TTL=600; TS_SLOT_DIRS=("$F44/slot"); TS_DOCS_ROOT="$F44/docs"; RG_HEALTH_LOG=/dev/null
  declare -f ts_try_reap scan_dead_docs_beacons | grep -c read_pid_and_swap > "$F44/routed"
  ts_try_reap 2>/dev/null; scan_dead_docs_beacons 2>/dev/null
  exit 0
)
[ "$(cat "$F44/routed" 2>/dev/null)" = 2 ] && [ -d "$F44/slot" ] && [ "$(cat "$F44/slot/nonce" 2>/dev/null)" = successor ] \
  && ok "a slot whose nonce changed after its pid was read survived the reap" \
  || nope "a slot whose nonce changed after its pid was read was reaped"
[ -d "$F44/docs/b" ] && [ "$(cat "$F44/docs/b/nonce" 2>/dev/null)" = successor ] \
  && ok "a docs beacon whose nonce changed after its pid was read survived the sweep" \
  || nope "a docs beacon whose nonce changed after its pid was read was swept"

# ---- 45: a bar at one slot does not claim beside its worktree's slot-2 holder (AC2) ------------------
# A two-slot bar elsewhere holds slot 1 and a two-slot bar in this worktree holds slot 2; slot 1 frees,
# and a one-slot bar from this worktree reaches the head. It must wait for its own worktree's holder.
R45=$tmp/lowW; R45o=$tmp/lowO; mk_repo "$R45"; mk_repo "$R45o"; S45=$tmp/shared45; S45o=$tmp/shared45o; mkdir -p "$S45" "$S45o"
run_slot_bar "$R45o" "$S45o" "$tmp/out45o"; p45o=$SLOT_PID; check_registered "$S45o" 1 "$p45o"
run_slot_bar "$R45" "$S45" "$tmp/out45b"; p45b=$SLOT_PID; check_registered "$S45" 1 "$p45b"
h45b=$(cat "$BS.2/pid" 2>/dev/null)
: > "$S45o/go"; wait "$p45o" 2>/dev/null
( cd "$R45" && env TS_SHARED="$S45" TS_DWELL=1 GATE_FULL=1 GATE_TURNSTILE_SLOTS=1 GATE_TURNSTILE_TTL=600 \
    GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >"$tmp/out45c" 2>&1 &
p45c=$!
i45=0; while ! grep -q 'queued at position' "$tmp/out45c" 2>/dev/null && kill -0 "$p45c" 2>/dev/null && [ "$i45" -lt 2400 ]; do sleep 0.1; i45=$((i45 + 1)); done
: > "$S45/go"; wait "$p45b" "$p45c" 2>/dev/null
peak45=$(peak "$S45")
[ "$peak45" = 1 ] && [ "$(grep -c . "$S45/peaks")" = 2 ] && ok "a one-slot bar never ran beside its worktree's slot-2 holder (peak 1)" \
  || nope "a one-slot bar ran beside its worktree's slot-2 holder (peak $peak45, $(grep -c . "$S45/peaks") registrations)"
grep -q "no bar holds this host's first slot, but this worktree's bar holds slot 2 — .*pid $h45b" "$tmp/out45c" \
  && ok "its queue line names the slot-2 holder in its own worktree" \
  || { nope "its queue line did not name the slot-2 holder ($h45b)"; grep -E 'held|queued' "$tmp/out45c" | sed 's/^/      /'; }

# ---- 46: a doc-only bar waits for its own worktree's holder, and a bar waits for its docs beacon (AC3)
R46=$tmp/docsSame; build_docs_repo "$R46"; S46=$tmp/shared46; mkdir -p "$S46"
( cd "$R46" && env TS_SHARED="$S46" GATE_FULL=1 GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 \
    GATE_LEGS="$tmp/holdS.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out46h" 2>&1 &
p46h=$!; check_registered "$S46" 1 "$p46h"
h46=$(cat "$BS/pid" 2>/dev/null)
( cd "$R46" && env TS_SHARED="$S46" TS_DWELL=1 GATE_FULL= GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >"$tmp/out46d" 2>&1 &
p46d=$!
i46=0; while ! grep -q "this worktree's bar holds" "$tmp/out46d" 2>/dev/null && kill -0 "$p46d" 2>/dev/null && [ "$i46" -lt 2400 ]; do sleep 0.1; i46=$((i46 + 1)); done
: > "$S46/go"; wait "$p46h" "$p46d" 2>/dev/null
peak46=$(peak "$S46")
[ "$peak46" = 1 ] && [ "$(grep -c . "$S46/peaks")" = 2 ] && ok "a doc-only bar never ran beside its worktree's holder (peak 1)" \
  || nope "a doc-only bar ran beside its worktree's holder (peak $peak46, $(grep -c . "$S46/peaks") registrations)"
grep -q "^gate queue: docs-only — this worktree's bar holds slot 1 — .*pid $h46 — waiting for it$" "$tmp/out46d" \
  && ok "the doc-only bar said it waits for its worktree's holder, naming it" \
  || { nope "the doc-only bar did not name its worktree's holder ($h46)"; grep -E 'gate queue' "$tmp/out46d" | sed 's/^/      /'; }
R46b=$tmp/docsSameB; build_docs_repo "$R46b"; S46b=$tmp/shared46b; mkdir -p "$S46b"
( cd "$R46b" && env TS_SHARED="$S46b" GATE_FULL= GATE_DOCS_BASE=HEAD~1 GATE_TURNSTILE_TICK=1 \
    GATE_LEGS="$tmp/holdS.json" bash $KIT_REL/run-gates.sh ) >"$tmp/out46e" 2>&1 &
p46e=$!; check_registered "$S46b" 1 "$p46e"
( cd "$R46b" && env TS_SHARED="$S46b" TS_DWELL=1 GATE_FULL=1 GATE_TURNSTILE_TTL=600 GATE_TURNSTILE_TICK=1 bash $KIT_REL/run-gates.sh ) >"$tmp/out46f" 2>&1 &
p46f=$!
i46=0; while ! grep -q 'queued at position' "$tmp/out46f" 2>/dev/null && kill -0 "$p46f" 2>/dev/null && [ "$i46" -lt 2400 ]; do sleep 0.1; i46=$((i46 + 1)); done
: > "$S46b/go"; wait "$p46e" "$p46f" 2>/dev/null
peak46b=$(peak "$S46b")
[ "$peak46b" = 1 ] && [ "$(grep -c . "$S46b/peaks")" = 2 ] && ok "a non-doc bar never ran beside its worktree's doc-only bar (peak 1)" \
  || nope "a non-doc bar ran beside its worktree's doc-only bar (peak $peak46b, $(grep -c . "$S46b/peaks") registrations)"
grep -q "this worktree's bar holds the docs key — " "$tmp/out46f" && ok "its queue line names the docs key its worktree holds" \
  || { nope "its queue line did not name the docs key"; grep -E 'held|queued' "$tmp/out46f" | sed 's/^/      /'; }

# ---- 47: a docs beacon left unfinished is swept by its age (AC5) -------------------------------------
R47=$tmp/docsUnfinished; build_docs_repo "$R47"; legs "$R47" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
mkdir -p "$DK/planted47"; printf 'p47' > "$DK/planted47/nonce"; touch -d "@$(( $(date +%s) - 100 ))" "$DK/planted47"
run_docs_bar "$R47" "$tmp/out47" GATE_TURNSTILE_TTL=5
grep -q 'sweeping the docs beacon of an unfinished holder' "$tmp/out47" && [ ! -e "$DK/planted47" ] \
  && ok "a docs beacon with no pid and no heartbeat, older than the ttl, was swept" || nope "an unfinished docs beacon was left standing"

# ---- 48: a stalled docs holder is swept by its heartbeat (AC6) ---------------------------------------
R48=$tmp/docsStalled; build_docs_repo "$R48"; legs "$R48" '[ {"name": "quick", "argv": ["bash", "fx/quick.sh"]} ]'
sleep 300 & live48=$!
mkdir -p "$DK/planted48"; printf '%s' "$live48" > "$DK/planted48/pid"; printf '%s' "$(( $(date +%s) - 100 ))" > "$DK/planted48/heartbeat"
printf '5' > "$DK/planted48/ttl"; printf 'p48' > "$DK/planted48/nonce"
run_docs_bar "$R48" "$tmp/out48"
kill "$live48" 2>/dev/null; wait "$live48" 2>/dev/null
grep -q 'sweeping the docs beacon of a stalled holder' "$tmp/out48" && [ ! -e "$DK/planted48" ] \
  && ok "a docs beacon whose live holder's heartbeat outlived its ttl was swept" || nope "a stalled docs beacon was left standing"
echo
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "turnstile: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; bad=1; }
[ "$bad" = 0 ] && echo "PASS ($n assertions)"
[ "$bad" = 0 ] || echo "FAIL (run-gates turnstile, $n assertions)"
exit "$bad"

#!/usr/bin/env bash
# run-gates.test.sh — canary: gate-legs.json is well-formed AND run-gates.sh sources every leg from it
# (no inlined leg command). Exit 0 = clean. Runs as a leg of run-gates.sh itself.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "canary: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
# The resolver, INLINED byte-identically from tools/lib/resolve-python.sh -- this harness SHIPS
# with the kit and tools/lib/ never travels. Enrols itself in the parity population, which is
# grep-derived from the marker below (the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` S2).
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
PYBIN=$(resolve_python) || { echo "canary: no usable python"; exit 2; }
fail=0
# the run-gates promotion spec's S11: an EXECUTED assertion count, incremented at each assertion rather
# than written as a literal. A hardcoded count is the recorded failure this leg exists for.
FLOOR_ASSERTIONS=65
n=0
# The manifest, derived exactly as run-gates.sh derives it: this kit's dir SIBLING. Hardcoding
# `tools/gate-legs.json` here would be a gov spelling in a harness that now ships (S1/S3).
# Normalised through the SAME `cd ... && pwd` chain on both sides: under MSYS `git rev-parse
# --show-toplevel` answers `C:/...` and `pwd` answers `/c/...`, and a strip across the two
# flavours leaves an ABSOLUTE path that resolves to nothing.
KITDIR=$(cd "$(dirname "$0")" && pwd)
ROOTN=$(cd "$ROOT" && pwd)
KITREL=${KITDIR#"$ROOTN"/}
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"

# 1. manifest well-formed: non-empty list; every leg has a non-empty name, an argv with a launcher
#    AND a script (len >= 2), and argv[0] in the allowed set. An empty name is the runner's
#    drop-sentinel (run-gates.sh skips it), and a launcher-only argv runs `bash </dev/null` = a silent
#    no-op GATE ok — both are green-by-absence shapes this canary exists to forbid.
n=$((n+1))
"$PYBIN" -c '
import json, sys
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)
if not isinstance(legs, list) or not legs:
    print("canary: %s is empty or not a list" % sys.argv[1]); sys.exit(1)
ok = {"bash", "python", "python3", "node"}   # node joined with the workflow-script gates (U6)
bad = [l.get("name", "?") for l in legs
       if not str(l.get("name", "")).strip() or not l.get("argv") or len(l["argv"]) < 2 or l["argv"][0] not in ok]
if bad:
    print("canary: malformed leg(s) (empty name, argv len < 2, or argv[0] not in {bash,python,python3,node}): " + ", ".join(bad)); sys.exit(1)
' "$LEGS_FILE" || fail=1

# 1b. every `guard` pathspec matches at least one TRACKED path. This is the quietest hole a guard can
#     open: `git diff --quiet BASE -- does/not/exist` reports NO difference, so a leg guarded on a
#     typo, a renamed kit or a deleted file skips on EVERY scoped run, forever, printing a reassuring
#     `GATE skip`. Checked against `git ls-files` rather than the filesystem, because the guard is a
#     pathspec git resolves, and an untracked file is invisible to it.
n=$((n+1))
"$PYBIN" -c '
import json, subprocess, sys
tracked = subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split()
bad = []
for l in json.load(open(sys.argv[1])):
    for g in l.get("guard", []):
        if not any(t == g or t.startswith(g) for t in tracked):
            bad.append("%s -> %s" % (l["name"], g))
if bad:
    print("canary: guard pathspec matches no tracked path (the leg would skip forever): " + "; ".join(bad))
    sys.exit(1)
' "$LEGS_FILE" || fail=1

# 2. no leg SCRIPT-PATH arg (argv[1..] that looks like a path) is hardcoded in run-gates.sh —
#    launcher tokens (bash/python/python3) and flags are excluded; the parse path is the manifest
#    filename, not a leg path, so it never matches.
paths=$("$PYBIN" -c '
import json, sys
rows = [a for l in json.load(open(sys.argv[1])) for a in l["argv"][1:] if "/" in a or a.endswith(".sh") or a.endswith(".py")]
sys.stdout.buffer.write(("\n".join(rows) + ("\n" if rows else "")).encode())   # LF bytes (Windows text stdout is CRLF)
' "$LEGS_FILE")
# ONE assertion over a population, counted once. Incrementing per iteration made the reported count
# track the MANIFEST SIZE rather than the assertion set, so the floor would red the day a leg was
# removed — a count that moves for reasons unrelated to the arms is not a count of the arms.
n=$((n+1))
while IFS= read -r p; do
  [ -z "$p" ] && continue
  if grep -qF -- "$p" "$KITREL/run-gates.sh"; then
    echo "canary: leg script path '$p' is hardcoded in $KITREL/run-gates.sh — source it from $LEGS_FILE"; fail=1
  fi
done <<<"$paths"

# 3. the bounded pool: concurrency must not change WHAT the bar reports, only how fast. Every arm
#    below runs against a SCRATCH repo carrying its own four-leg manifest — never the real 47-leg
#    bar, which would cost minutes and couple this canary to every other kit's health.
SCRATCH=$(mktemp -d) || { echo "canary: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$SCRATCH"' EXIT
mkdir -p "$SCRATCH/tools/run-gates" "$SCRATCH/fx"
# The runner is copied from THIS harness's own kit dir, not from gov's prefix. This file
# SHIPS, and a hardcoded `tools/run-gates/` here made it red on arrival at any other prefix.
cp "$KITDIR/run-gates.sh" "$SCRATCH/tools/run-gates/run-gates.sh"
# EVERY leg sleeps, and that is load-bearing. With only one slow leg a serial run and a concurrent
# run both cost about that leg, so arm 3c could not tell them apart — measured: forcing width 1 left
# the canary green. Four sleeping legs make serial (6.5s) and concurrent (2s) genuinely diverge.
# Leg 1 sleeps LONGEST so it finishes last, which is what gives arm 3b something to catch.
# THE RENDEZVOUS PREAMBLE, shared by both timed fixtures. A fixture ANNOUNCES itself and then WAITS
# for peers, recording the PEAK number it ever saw announced at once. That is what makes this arm
# measure the RUNNER: dispatch skew is absorbed by the wait instead of deciding the verdict. The
# retired form timed two runs and compared elapsed time, which is a fact about the NODE -- it red
# three consecutive pushes on a machine running a second bar, over a tree it had already passed.
#
# IDENTITY ARRIVES AS ARGV. Three of the four legs run this same `mid.sh`, and run-gates.sh execs a
# leg's argv verbatim with no per-leg variable, so a fixture cannot key on its own script name: all
# three would write one path and the survivor would be the LAST leg to start, which HIDES a real
# overlap rather than faking one. `mid.sh` stays ONE file because arm 3d copies bad.sh over it.
#
# The peak is written BEFORE the sleep and before any exit, so a fixture that exits non-zero still
# leaves its record -- an end-of-fixture write would never run for one that exits 3.
RVWAIT_TICKS=30        # 30 x 100ms = 3s. The one bound left: the batch must dispatch inside it.
                       # Lengthening it costs only the width-1 run, where every leg waits it out.
rendezvous='leg="${1:-$(basename "$0" .sh)}"
d="$(dirname "$0")/ts"; mkdir -p "$d"; : > "$d/$leg.up"
trap "rm -f \"$d\"/\"$leg\".up" EXIT
peak=0
for _ in $(seq 1 RVTICKS); do
  n=$(ls "$d"/*.up 2>/dev/null | grep -c .)
  [ "$n" -gt "$peak" ] && peak=$n
  [ "$peak" -ge 4 ] && break
  sleep 0.1
done
printf "%s\\n" "$peak" > "$d/$leg.peak"'
rendezvous=${rendezvous//RVTICKS/$RVWAIT_TICKS}
printf '#!/usr/bin/env bash\n%s\nsleep 2\nexit 0\n'   "$rendezvous" > "$SCRATCH/fx/slow.sh"
printf '#!/usr/bin/env bash\n%s\nsleep 1.5\nexit 0\n' "$rendezvous" > "$SCRATCH/fx/mid.sh"
printf '#!/usr/bin/env bash\necho "boom detail"\nexit 3\n' > "$SCRATCH/fx/bad.sh"
printf '#!/usr/bin/env bash\nexit 0\n'                     > "$SCRATCH/fx/instant.sh"
cat > "$SCRATCH/tools/gate-legs.json" <<'JSON'
[
  {"name": "alpha slow", "argv": ["bash", "fx/slow.sh", "alpha"]},
  {"name": "beta fast",  "argv": ["bash", "fx/mid.sh", "beta"]},
  {"name": "gamma fast", "argv": ["bash", "fx/mid.sh", "gamma"]},
  {"name": "delta fast", "argv": ["bash", "fx/mid.sh", "delta"]}
]
JSON
( cd "$SCRATCH" && git init -q . && git config user.email t@e && git config user.name t ) >/dev/null 2>&1

# CLEARS fx/ts FIRST. Without it the width-1 run reads the width-4 run's records and the negative
# control passes on stale evidence -- this repo's fixture-passes-by-finding-nothing class exactly.
run_scratch() { rm -rf "$SCRATCH/fx/ts"; ( cd "$SCRATCH" && GATE_FULL= GATE_BASE= GATE_JOBS=$1 bash tools/run-gates/run-gates.sh 2>&1 ); }
# Read IMMEDIATELY after a run: the next run_scratch deletes these.
peaks_now()  { cat "$SCRATCH/fx/ts"/*.peak 2>/dev/null | sort -rn | tr "\n" " "; }
npeaks_now() { ls "$SCRATCH/fx/ts"/*.peak 2>/dev/null | grep -c . || true; }

# 3a. width 1 and width 4 agree line for line. This is the equivalence the pool rests on: one code
#     path, so the serial reading is not a second implementation that can drift.
s1=$(run_scratch 1); peaks1=$(peaks_now); n1=$(npeaks_now)
s4=$(run_scratch 4); peaks4=$(peaks_now); n4=$(npeaks_now)
# THE PROFILE LINE IS FILTERED BY NAME, because it legitimately differs between the two runs: it
# reports the EFFECTIVE width, which is the one thing these runs are supposed to disagree about. The
# companion arms below are what stop that filter from hiding the line's disappearance — a filter with
# no presence check is a way to make any regression in the filtered line invisible.
f1=$(printf '%s\n' "$s1" | grep -v '^gate profile: ')
f4=$(printf '%s\n' "$s4" | grep -v '^gate profile: ')
n=$((n+1))
if [ "$f1" != "$f4" ]; then
  echo "canary: GATE_JOBS=1 and GATE_JOBS=4 disagree — concurrency changed the report"
  diff <(printf '%s\n' "$f1") <(printf '%s\n' "$f4") | sed 's/^/    /'; fail=1
fi
# The profile line exists AND precedes the first leg verdict — an operator who cannot see the knobs
# before the run starts cannot tell a thrashing box from a slow one.
first_marker() { printf '%s\n' "$1" | grep -E '^(gate profile: |GATE )' | head -1; }
for _w in 1 4; do
n=$((n+1))
  eval "_s=\$s$_w"
  case "$(first_marker "$_s")" in
    'gate profile: '*) ;;
    '') echo "canary: the width-$_w run printed no 'gate profile: ' line, so arm 3a's filter is hiding its absence rather than its width"; fail=1 ;;
    *)  echo "canary: the width-$_w run printed a leg verdict BEFORE its 'gate profile: ' line: $(first_marker "$_s")"; fail=1 ;;
  esac
done

# 3b. reporting is in MANIFEST order even though leg 1 finishes last.
got=$(printf '%s\n' "$s4" | grep -c '^GATE ')
ordered=$(printf '%s\n' "$s4" | grep '^GATE ' | sed 's/^GATE [a-z]*  *//')
want=$'alpha slow\nbeta fast\ngamma fast\ndelta fast'
n=$((n+1))
if [ "$ordered" != "$want" ]; then
  echo "canary: legs did not report in manifest order under concurrency; got:"
  printf '%s\n' "$ordered" | sed 's/^/    /'; fail=1
fi
n=$((n+1))
[ "$got" = 4 ] || { echo "canary: expected 4 GATE lines from the scratch bar, got $got"; fail=1; }

# 3c. concurrency actually OVERLAPS, asserted as a RENDEZVOUS rather than as elapsed time.
#     WHAT THIS CLAIMS: run-gates.sh DISPATCHED four legs at once. What it deliberately does NOT
#     claim: anything about how fast the node ran them. That distinction is the whole fix. Both
#     retired forms graded this leg against load it does not control -- first an absolute
#     five-second deadline, then twice-the-concurrent-under-the-serial, whose stated premise was that
#     uniform load
#     cancels in a ratio. It does not: the serial run has no overlap to lose, so contention costs it
#     only slowdown, while the concurrent run's entire advantage IS overlap. Measured nine times on
#     node c -- red under contention, green when quiet, red-then-GREEN on a byte-identical tree --
#     and it blocked three consecutive pushes of a records-only commit. The build that replaced it
#     is recorded in the memory tree; its id is deliberately NOT cited here, because the drift signal
#     for non-terminal specs cited by product source sits at its pin and naming one reds the bar.
#
#     Each fixture announces itself and WAITS for peers, recording the peak it saw. Dispatch skew is
#     absorbed by that wait instead of deciding the verdict, so the only bound left is that the batch
#     dispatches within RVWAIT_TICKS -- and lengthening that costs only the width-1 run.
#
#     EQUALITY, not "at least one pair overlapped": a pool clamped to width 2 satisfies any
#     at-least-one form while being exactly the regression this arm exists to catch.
n=$((n+1))
[ "$n4" = 4 ] || { echo "canary: width-4 produced $n4 rendezvous record(s), not 4 - the arm would compare a smaller set than it claims"; fail=1; }
n=$((n+1))
[ "$n1" = 4 ] || { echo "canary: width-1 produced $n1 rendezvous record(s), not 4 - the arm would compare a smaller set than it claims"; fail=1; }
# The peak is the FIRST field of the reverse-sorted list: the most legs any one leg ever saw at once.
peak4=${peaks4%% *}; peak1=${peaks1%% *}
n=$((n+1))
[ "$peak4" = 4 ] || { echo "canary: width-4 peaked at $peak4 legs in flight, not 4 - the pool did not dispatch the batch together (peaks: $peaks4, wait ${RVWAIT_TICKS}x100ms)"; fail=1; }
# THE NEGATIVE CONTROL, and it is what gives the line above its meaning: the same fixtures at width 1
# must NEVER see a peer. Without it the arm passes on any implementation that writes a 4.
n=$((n+1))
[ "$peak1" = 1 ] || { echo "canary: width-1 peaked at $peak1 legs in flight, not 1 - the serial path overlapped, so the width-4 reading proves nothing (peaks: $peaks1)"; fail=1; }

# 3d. a failing leg keeps its exit code, its indented output, and its row in the durable summary.
cp "$SCRATCH/fx/bad.sh" "$SCRATCH/fx/mid.sh"
red=$(run_scratch 4)
n=$((n+1))
printf '%s\n' "$red" | grep -q '^GATE FAIL  beta fast  (exit 3)$' \
  || { echo "canary: a failing leg lost its GATE FAIL line or exit code"; fail=1; }
n=$((n+1))
printf '%s\n' "$red" | grep -q '^    boom detail$' \
  || { echo "canary: a failing leg's output was not indented under its GATE FAIL line"; fail=1; }
n=$((n+1))
printf '%s\n' "$red" | grep -q '^gates RED — 3/4 legs failed$' \
  || { echo "canary: the RED verdict line did not tally the failing legs"; fail=1; }
n=$((n+1))
grep -q 'beta fast' "$SCRATCH/.git/gate-last-summary.txt" 2>/dev/null \
  || { echo "canary: the failing leg never reached gate-last-summary.txt"; fail=1; }
printf '#!/usr/bin/env bash\n%s\nsleep 1.5\nexit 0\n' "$rendezvous" > "$SCRATCH/fx/mid.sh"   # restored WITH the rendezvous, or 3d leaves a fixture the later arms cannot use

# 3e. the timing cache is ADVISORY. A corrupt one must cost wall clock and nothing else, because it
#     is written by every run and a half-written file after a kill is the expected state, not a bug.
printf 'not\ta\tnumber\n\x00garbage\n' > "$SCRATCH/.git/gate-timings.tsv"
corrupt=$(run_scratch 4)
n=$((n+1))
printf '%s\n' "$corrupt" | grep -q '^gates GREEN — 4/4 legs passed$' \
  || { echo "canary: a corrupt gate-timings.tsv changed the verdict"; printf '%s\n' "$corrupt" | sed 's/^/    /'; fail=1; }

# 3f. GATE_JOBS only schedules. A garbage, zero, negative or absurd width still reports EVERY leg —
#     this knob must never be a way to make the bar check less than it checks. The sleeps are dropped
#     first: these runs are serial by construction and paying 6.5s each proves nothing extra.
#     Every value here REACHES the clamp. An empty string does not and was removed: `${GATE_JOBS:-…}`
#     substitutes the default for null as well as unset, so `GATE_JOBS=""` measured width 8 while its
#     comment claimed it proved clamping — which is how the overflow below shipped.
#     The `timeout` is the point, not defensive noise: before the length bound, the 20-digit value
#     made the runner spin forever having executed ZERO legs, so without a timeout this arm would
#     HANG the bar rather than red it — converting a production hang into a hang on the gate.
# TOOL-aPromptedMandate-13 - the budget is a VARIABLE so the two branches below are reachable by the
# harness. Both fire only when `timeout` expires, and on a healthy host it never does, so with a
# hardcoded 60 the outcomes this arm distinguishes could not be exercised at all - a deliverable
# whose own acceptance is unobservable, which is the unfailable-check class one level up.
CLAMP_BUDGET=${CLAMP_BUDGET:-60}
# The width the clamp is SUPPOSED to yield, mirroring run-gates.sh:81-82 INCLUDING ITS CASE ORDER:
# `*[!0-9]*` is tested FIRST there, so `nonsense` (8 chars) clamps to 1 and not to 64 despite also
# matching `?????*`. Getting that order wrong would send the control to the wrong width and quietly
# restore the very mis-inference this unit removes.
clamp_target() {
  case "$1" in
    *[!0-9]*) echo 1 ;;
    ?????*)   echo 64 ;;
    *)        [ "$1" -lt 1 ] 2>/dev/null && echo 1 || echo "$1" ;;
  esac
}
# ...and it is a COPY of run-gates' clamp, so it is JOINED to the source rather than trusted. Two
# copies of one computation agree until they do not, and nothing here could observe a divergence:
# the arms below read the source's own case arms and assert this function reproduces them, so a
# clamp edit that this copy does not follow reds instead of silently sending the control to the
# wrong width. The ORDER matters as much as the mapping - `nonsense` matches `?????*` too, and only
# run-gates testing `*[!0-9]*` first makes it 1.
_ct_src=$(sed -n 's/.*case "\$JOBS" in \(.*\) esac.*/\1/p' "$ROOT/tools/run-gates/run-gates.sh" | head -1)
case "$_ct_src" in
  *'*[!0-9]*) JOBS=1'*'?????*) JOBS=64'*) ;;
  *) echo "canary: run-gates' clamp no longer reads as the two ordered arms clamp_target mirrors, so the control width this suite computes is no longer joined to the source it copies: $_ct_src"; fail=1 ;;
esac
# THE LIVE CONTROL, as a function so the suite can drive BOTH its outcomes rather than wait for an
# unlucky host. Exit 124 says the budget expired and NOTHING about why; the message this replaces
# asserted a spinning clamp from it. The control runs the SAME fixture at the width the clamp should
# have produced, so the clamp path is the only difference between subject and control.
#
# MEASURED 2026-08-18: under four concurrent full bars this arm accused the clamp for 0, -3 and
# nonsense, and the same canary exits 0 in isolation. Three malformed widths do not all start
# spinning and then all stop.
#
# It PRINTS the verdict and returns non-zero for either outcome - undecidable FAILS too, because an
# arm that could not look has not looked, and scoring that green is fixture-passes-by-finding-nothing
# with the machine blamed for the fixture. The caller owns `fail`, so the self-test below can call
# this in a subshell and read the message without reddening the suite.
clamp_expired_verdict() { # width-input -> prints the verdict, always returns 1
  local w="$1" ctw ctl crc
  ctw=$(clamp_target "$w")
  ctl=$(GATE_FULL= GATE_BASE= GATE_JOBS="$ctw" timeout "$CLAMP_BUDGET" bash -c "cd '$SCRATCH' && bash tools/run-gates/run-gates.sh" 2>&1); crc=$?
  if [ "$crc" = 124 ]; then
    echo "canary: GATE_JOBS='$w' and its width-$ctw control BOTH expired - this host could not finish the fixture at any width, so the clamp is unproven either way"
  else
    echo "canary: GATE_JOBS='$w' never terminated while its width-$ctw control finished - the clamp let it spin"
  fi
  return 1
}
cp "$SCRATCH/fx/instant.sh" "$SCRATCH/fx/slow.sh"; cp "$SCRATCH/fx/instant.sh" "$SCRATCH/fx/mid.sh"
for w in 0 -3 nonsense 99999999999999999999 999999999999999999999999999999; do
n=$((n+1))
n=$((n+1))
  out=$(GATE_FULL= GATE_BASE= GATE_JOBS="$w" timeout "$CLAMP_BUDGET" bash -c "cd '$SCRATCH' && bash tools/run-gates/run-gates.sh" 2>&1); trc=$?
  if [ "$trc" = 124 ]; then
    clamp_expired_verdict "$w"
    fail=1; continue
  fi
  printf '%s\n' "$out" | grep -q '^gates GREEN — 4/4 legs passed$' \
    || { echo "canary: GATE_JOBS='$w' did not clamp to a working width"; printf '%s\n' "$out" | tail -3 | sed 's/^/    /'; fail=1; }
done

# 3f-bis. TOOL-aPromptedMandate-13: BOTH outcomes of the expiry verdict, driven by the budget knob
#        rather than by an unlucky host. Without this the two branches ship unreachable, which is the
#        unfailable-check class the unit exists to remove, one level up. Each runs in a SUBSHELL so
#        the `return 1` it is supposed to emit is OBSERVED here instead of reddening this suite.
#
#        UNDECIDABLE: a budget nothing can finish inside makes the control expire too, and the
#        verdict must decline to blame the clamp.
#
#        `0.05`, NOT `0`. MEASURED on this node: `timeout 0 sleep 2` exits 0 - a zero duration means
#        NO LIMIT in coreutils, not an instant one. Written as 0 this arm ran the control with the
#        timeout disabled, the control finished, the spun branch fired, and the arm reported the
#        defect it was written to catch. It caught it in MY code, which is the arm working.
v=$( CLAMP_BUDGET=0.05 clamp_expired_verdict 0 2>&1 )
case "$v" in
  *"BOTH expired"*|*"unproven either way"*) ;;
  *) echo "canary: the expiry verdict did not report an undecidable host when its own control expired: $v"; fail=1 ;;
esac
#        SPUN: a budget the control comfortably finishes inside leaves the clamp as the difference.
#        It asserts the message ONLY when the control actually finished - on a loaded host it may
#        not, and an arm that reds there would be naming a cause it never checked, which is the
#        defect this whole unit removes. Reported as a loud skip instead of a silent pass.
v=$( CLAMP_BUDGET=60 clamp_expired_verdict 0 2>&1 )
case "$v" in
  *"the clamp let it spin"*)  ;;
  *"BOTH expired"*) echo "canary: SKIP the spun-outcome arm - this host could not finish the control inside 60s, so the outcome it asserts was not produced" ;;
  *) echo "canary: the expiry verdict emitted neither outcome when its control was run: $v"; fail=1 ;;
esac
#        ...and the two outcomes are DISTINGUISHABLE, which is the whole point of the unit.
[ "$( CLAMP_BUDGET=0.05 clamp_expired_verdict 0 2>&1 )" != "$( CLAMP_BUDGET=60 clamp_expired_verdict 0 2>&1 )" ] \
  || { echo "canary: the two expiry outcomes emit the same message, so the verdict cannot be read"; fail=1; }

# 3g. a healthy leg is NEVER reported "(no result)" — the reader must not conclude a still-pending
#     leg is dead just because no job is RUNNING at the instant it looks.
#     This is a RACE, and the fixture is tuned to the condition that actually reproduces it rather
#     than to a plausible-looking one. MEASURED against the pre-fix reader: 30 instant legs at
#     WIDTH 1 fires 6 runs in 8, while widths 2, 4 and 8 fire 0 in 8 — at width 1 the reader
#     dispatches a worker and looks for its result immediately, which is the whole window. An earlier
#     version of this arm used the 4-leg manifest at mixed widths, reproduced at 1-in-40, and let the
#     pre-fix reader pass. Do not "simplify" this back to the shared fixture.
mkdir -p "$SCRATCH/many/tools/run-gates" "$SCRATCH/many/fx"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$SCRATCH/many/tools/run-gates/run-gates.sh"
cp "$SCRATCH/fx/instant.sh" "$SCRATCH/many/fx/a.sh"
"$PYBIN" -c '
import json, sys
json.dump([{"name": "l%02d" % i, "argv": ["bash", "fx/a.sh"]} for i in range(30)],
          open(sys.argv[1], "w", newline="\n"), indent=1)
' "$SCRATCH/many/tools/gate-legs.json"
( cd "$SCRATCH/many" && git init -q . && git config user.email t@e && git config user.name t ) >/dev/null 2>&1
#     The ABSENCE of "(no result)" is not on its own an assertion: a fixture that never ran has none
#     either. Two breakages were reproduced passing this arm silently — a missing manifest, and an
#     omitted `git init`, which is worse, because `git rev-parse --show-toplevel` then walks UP to the
#     parent scratch repo and the arm runs the 4-leg manifest at width 1: exactly the configuration
#     the comment above forbids, reported green. So assert the run HAPPENED first.
for rep in 1 2 3 4; do
  o=$( cd "$SCRATCH/many" && GATE_FULL= GATE_BASE= GATE_JOBS=1 bash tools/run-gates/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^gates GREEN — 30/30 legs passed$' \
    || { echo "canary: the 30-leg width-1 fixture did not run — arm 3g proves nothing"
    n=$((n+1))
         printf '%s\n' "$o" | tail -3 | sed 's/^/    /'; fail=1; break; }
  case "$o" in
    *"(no result)"*) echo "canary: a healthy leg was reported (no result) — the reader gave up before its worker landed"
    n=$((n+1))
                     printf '%s\n' "$o" | grep -E "no result|RED" | sed 's/^/    /'; fail=1; break ;;
  esac
done

# 3h. the GUARD / SKIP path, and the advisory cache's survival across a scoped run.
#     This diff moved the run-or-skip decision into a serial pre-pass that materialises the literal
#     string `skip` into <i>.rc. That one file has THREE consumers: dispatch suppression, the
#     `GATE skip` branch, and the skips tally. Until this arm existed NO fixture declared a `guard`,
#     so none of the three ever executed and an unconditional-skip regression — every guarded leg
#     skipped regardless of the diff, the canonical green-while-checking-less shape this file exists
#     to forbid — kept the whole suite green BY CONSTRUCTION rather than by luck.
G="$SCRATCH/guarded"
mkdir -p "$G/tools/run-gates" "$G/fx"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$G/tools/run-gates/run-gates.sh"
cp "$SCRATCH/fx/instant.sh" "$G/fx/a.sh"
cat > "$G/tools/gate-legs.json" <<'JSON'
[
  {"name": "plain one", "argv": ["bash", "fx/a.sh"]},
  {"name": "guarded",   "argv": ["bash", "fx/a.sh"], "guard": ["never/touched.txt"]},
  {"name": "plain two", "argv": ["bash", "fx/a.sh"]}
]
JSON
( cd "$G" && git init -q -b main . && git config user.email t@e && git config user.name t \
  && git add -A && git commit -qm fx ) >/dev/null 2>&1
# Pass 1 with no origin ref: BASE is unresolvable, changed() fails SAFE to "run", so all three legs
# execute and all three land a timing row. This is also the arm for that fail-safe.
o=$( cd "$G" && GATE_FULL= GATE_BASE= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$' \
  || { echo "canary: with no resolvable BASE a guarded leg did not fail safe to RUN"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
# Pass 2 with origin/HEAD pinned: the guard path resolves and the unchanged leg must SKIP.
( cd "$G" && git update-ref refs/remotes/origin/main HEAD \
  && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
for w in 1 4; do
n=$((n+1))
n=$((n+1))
n=$((n+1))
  o=$( cd "$G" && GATE_FULL= GATE_BASE= GATE_JOBS=$w bash tools/run-gates/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^GATE skip  guarded  (unchanged vs main)$' \
    || { echo "canary: width $w printed no GATE skip line for a guarded, unchanged leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed (1 skipped)$' \
    || { echo "canary: width $w did not tally the skip (expected 2/2 passed, 1 skipped)"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  [ "$(printf '%s\n' "$o" | grep '^GATE ' | sed -n 2p)" = "GATE skip  guarded  (unchanged vs main)" ] \
    || { echo "canary: width $w reported the skipped leg away from its manifest position"; fail=1; }
done
# C1: the skipped leg produced no timing this run. Its CACHED row from pass 1 must survive, or every
# diff-scoped run blanks the dispatch hint the next full run needs.
n=$((n+1))
grep -q '^guarded	' "$G/.git/gate-timings.tsv" 2>/dev/null \
  || { echo "canary: the skipped leg's cached timing row was dropped by the cache rewrite"; fail=1; }

# 3i. GATE_FULL bypasses every guard. This is the invariant the whole diff-scoping scheme rests on:
#     `.githooks/pre-push` sets it, so a guard can only ever scope a NON-authoritative run and a
#     too-narrow guard costs an early signal rather than a wrong merge verdict. Asserted against the
#     SAME fixture that skips without it, so the two readings differ only by the variable.
for w in 1 4; do
n=$((n+1))
n=$((n+1))
  o=$( cd "$G" && GATE_FULL=1 GATE_BASE= GATE_JOBS=$w bash tools/run-gates/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$' \
    || { echo "canary: GATE_FULL=1 at width $w did not run every leg past its guard"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^GATE skip' \
    && { echo "canary: GATE_FULL=1 at width $w still skipped a guarded leg"; fail=1; }
done

# 3j MOVED to run-gates.gov.test.sh (G3). It asserted that GOV's `.githooks/pre-push` forces the
#    full bar — a fact about gov's tree, sitting in the half whose whole contract is that every
#    assertion holds in ANY tree. An adopter has no such hook unless they also took push-main, which
#    is not in the default selection, so this arm was red on arrival in every default install.

# 4. THE HARDWARE PROFILE TABLE. The runner's knobs are DECLARED rather than computed from core
#    count alone, and the governing invariant is that no knob may ever turn a leg into a PASS or a
#    SKIP. Every arm below runs against a SCRATCH repo, never the real bar.
#
#    THE SELECTION ARMS DRIVE A FIXTURE TABLE, NOT THE SHIPPED ONE, and that is the whole design of
#    this section. The shipped table is DATA an adopter is expected to tune, so an arm keyed on its
#    figures is memory/gotchas/pin-copied-from-another-corpus.md — it would red on their tree while
#    saying nothing about it. A fixture whose thresholds this file writes is true everywhere, needs
#    no skip when the shipped table is edited or removed, and lets the arms name exact readings.
#    Exactly ONE arm reads the shipped table (4e), because its subject IS that file's own content.
P="$SCRATCH/prof"
mkdir -p "$P/tools/run-gates" "$P/fx" "$P/shim"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$P/tools/run-gates/run-gates.sh"
printf '#!/usr/bin/env bash\nexit 0\n'          > "$P/fx/a.sh"
printf '#!/usr/bin/env bash\nsleep 4\nexit 0\n' > "$P/fx/sleeper.sh"
cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "two", "argv": ["bash", "fx/a.sh"]}
]
JSON
( cd "$P" && git init -q . && git config user.email t@e && git config user.name t ) >/dev/null 2>&1
runp() { ( cd "$P" && env GATE_FULL= GATE_BASE= "$@" bash tools/run-gates/run-gates.sh 2>&1 ); }
profline() { printf '%s\n' "$1" | grep '^gate profile: ' | head -1; }
profname() { profline "$1" | sed 's/^gate profile: //; s/  (.*//'; }

# THE FIXTURE TABLE the selection arms drive. Three rows, most-capable-first, zero-threshold
# catch-all last — the shape the grammar declares — with thresholds this file chose so the arms can
# name exact readings. It is INSTALLED as the scratch runner's own table, so no seam points at it and
# the ordinary derivation is what finds it: an arm driving GATE_PROFILES would be grading the seam
# rather than the path every real run takes.
printf 'big\t16\t24000\twidth=8,timeout=0\nsmall\t4\t0\twidth=4,timeout=0\nany\t0\t0\twidth=2,timeout=0\n' \
  > "$P/tools/run-gates/gate-profiles.txt"

# 4a. the most-capable row is selected when BOTH its thresholds are met. Seams, not real hardware:
#     the node running this suite is whatever it is, and an arm that depends on that grades the box.
n=$((n+1))
got=$(profname "$(runp GATE_CORES=16 GATE_RAM_MB=32000)")
[ "$got" = big ] || { echo "canary: 16 cores and 32000 MB selected '$got', not the fixture's most-capable row 'big'"; fail=1; }

# 4b. THE RAM GUARD, which is the whole reason this table exists: cores alone are the wrong question
#     and the built-in formula cannot express this at all. SAME core count, a RAM reading below the
#     top row's threshold, and the selection must land on the middle row instead.
n=$((n+1))
got=$(profname "$(runp GATE_CORES=16 GATE_RAM_MB=8000)")
[ "$got" = small ] || { echo "canary: 16 cores and 8000 MB selected '$got', not the middle row 'small' — the RAM guard is not armed, and a high-core low-RAM box would take the widest profile"; fail=1; }

# 4c. unknown hardware lands on the LAST row by ordinary threshold matching, and says so. A detection
#     failure must cost SPEED, never COVERAGE, and the tag is how an operator tells the two apart
#     afterwards.
n=$((n+1))
n=$((n+1))
o=$(runp GATE_CORES=0 GATE_RAM_MB=0)
got=$(profname "$o")
[ "$got" = any ] || { echo "canary: unknown hardware selected '$got', not the table's last (catch-all) row 'any'"; fail=1; }
case "$(profline "$o")" in *'detection failed'*) ;; *) echo "canary: an unresolvable hardware reading was not tagged as a detection failure: $(profline "$o")"; fail=1 ;; esac
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
  || { echo "canary: a detection failure changed the VERDICT — a knob must only ever cost speed"; fail=1; }

# 4d. a profile name that resolves to nothing REFUSES, and lists the names that do exist. An
#     operator who mistyped a row name gets the roster, not a silent fall-through to some other row.
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILE=no-such-row-4f2a); rc=$?
[ "$rc" = 2 ] || { echo "canary: an unknown GATE_PROFILE exited $rc, not 2"; fail=1; }
printf '%s\n' "$o" | grep -q 'big' \
  || { echo "canary: the unknown-GATE_PROFILE refusal did not list the row names that do exist"; fail=1; }

# 4e. THE PINNED KNOB SET, and the ONE arm whose subject is the SHIPPED table rather than a fixture:
#     what it grades is that file's own content. It is the left-shift of the governing invariant. The
#     runner declares what it IMPLEMENTS; this pin declares what has been REVIEWED, and they are
#     deliberately two separate statements — a knob added to the table reds here until an author
#     edits this line, which is the moment they read the invariant. Collapsing the two would remove
#     the only forcing function a coverage knob would ever meet.
PINNED_KNOBS="timeout width"
PTBL="$KITREL/gate-profiles.txt"
n=$((n+1))
if [ ! -f "$PTBL" ]; then
  # ANNOUNCED, and counted, so the executed total does not move with the table's presence. A skip
  # that silently shrinks the count reds the floor with a message about arithmetic instead of a
  # message about what went ungraded.
  echo "canary: SKIP the pinned-knob arm — $PTBL is absent, so this tree declares no knobs to grade (the runner falls back to its built-in formula, which arm 4f drives on purpose)"
else
  tblknobs=$(grep -vE '^[[:space:]]*(#|$)' "$PTBL" | cut -f4 | tr ',' '\n' | sed 's/=.*//' | sort -u | tr '\n' ' ')
  # An EMPTY read makes the loop below unreachable, and an unreachable loop certifies the pin by
  # never comparing it — a table whose rows carry no fourth field reads empty here and would pass.
  [ -n "${tblknobs// /}" ] \
    || { echo "canary: $PTBL yielded NO knob keys, so the pinned-set comparison below would pass by finding nothing"; fail=1; }
  for k in $tblknobs; do
    case " $PINNED_KNOBS " in *" $k "*) ;; *) echo "canary: $PTBL declares knob key '$k', which is not in this suite's pinned set ($PINNED_KNOBS). Read the governing invariant in the table's header before adding it: no knob may ever turn a leg into a PASS or a SKIP."; fail=1 ;; esac
  done
fi

# 4f. THE ROLLBACK. An ABSENT table is a fallback, never a refusal: this kit deploys, and an adopter
#     may take it without the table. Deleting it restores the built-in formula, and this arm is what
#     proves that rather than hoping for it.
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILES=definitely/absent/gate-profiles.txt)
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
  || { echo "canary: with no profile table the runner did not fall back and run every leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
case "$(profline "$o")" in *'built-in default'*) ;; *) echo "canary: the no-table run was not tagged as the built-in default: $(profline "$o")"; fail=1 ;; esac

# 4g. GATE_JOBS overrides the WIDTH ONLY. The row is still selected and still supplies every other
#     knob — an override that silently disabled the rest of the profile would make the table a lie
#     the moment anyone set a width.
printf 'solo\t0\t0\twidth=8,timeout=9\n' > "$P/fx/tbl-timeout.txt"
n=$((n+1))
n=$((n+1))
pl=$(profline "$(runp GATE_PROFILES=fx/tbl-timeout.txt GATE_JOBS=3)")
case "$pl" in *'width 3,'*) ;; *) echo "canary: GATE_JOBS=3 did not reach the reported width: $pl"; fail=1 ;; esac
case "$pl" in *'timeout 9s'*) ;; *) echo "canary: GATE_JOBS suppressed the row's OTHER knob — the override is not width-only: $pl"; fail=1 ;; esac

# 4h. A LEG THAT OUTLIVES THE TIMEOUT IS RED, NAMED, AND THE RUN IS RED. Never a skip and never a
#     green: this knob converts an unbounded hang into a verdict, which is the one way a knob may
#     change coverage at all — upward. Recorded motivating failure: a leg that hung with zero output
#     and wedged a whole bar at 46 of 65.
printf 'tight\t0\t0\twidth=2,timeout=1\n' > "$P/fx/tbl-tight.txt"
cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "sleeper", "argv": ["bash", "fx/sleeper.sh"]}
]
JSON
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILES=fx/tbl-tight.txt)
printf '%s\n' "$o" | grep -q '^GATE FAIL  sleeper  (timed out after 1s)$' \
  || { echo "canary: a leg that outlived the per-leg timeout was not reported FAILED with a timeout tail"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
printf '%s\n' "$o" | grep -q '^gates RED — 1/2 legs failed$' \
  || { echo "canary: a timed-out leg did not make the run RED — a timeout must never read as a skip or a pass"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "two", "argv": ["bash", "fx/a.sh"]}
]
JSON

# 4i. THE REFUSALS. A silently ignored knob is a knob the operator believes they set, so a table the
#     runner cannot honour REFUSES rather than guessing. Each fixture below is load-bearing: against
#     the shipped table every one of these is unreachable, so an arm driving the real file would pass
#     by finding nothing — memory/gotchas/fixture-passes-by-finding-nothing.md.
printf '# c\ngood\t0\t0\twidth=2,timeout=0\nthis row has no tabs at all\n' > "$P/fx/tbl-malformed.txt"
printf 'good\t8\t0\twidth=8,turbo=1\nfallback\t0\t0\twidth=2,timeout=0\n'  > "$P/fx/tbl-badknob.txt"
printf 'toobig\t99\t0\twidth=8,timeout=0\n'                                > "$P/fx/tbl-nocatchall.txt"
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILES=fx/tbl-malformed.txt); rc=$?
[ "$rc" = 2 ] || { echo "canary: a malformed profile row exited $rc, not 2"; fail=1; }
printf '%s\n' "$o" | grep -q 'fx/tbl-malformed.txt:3:' \
  || { echo "canary: the malformed-row refusal did not name the file AND the line number: $o"; fail=1; }
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILES=fx/tbl-badknob.txt); rc=$?
[ "$rc" = 2 ] || { echo "canary: an unknown knob key exited $rc, not 2 — a knob the runner ignores is a knob the operator believes they set"; fail=1; }
printf '%s\n' "$o" | grep -q "turbo" \
  || { echo "canary: the unknown-knob refusal did not name the offending key: $o"; fail=1; }
n=$((n+1))
n=$((n+1))
o=$(runp GATE_CORES=1 GATE_RAM_MB=1 GATE_PROFILES=fx/tbl-nocatchall.txt); rc=$?
[ "$rc" = 2 ] || { echo "canary: a table matching NOTHING exited $rc, not 2 — unmatchable and absent are different states and only one is an operator error"; fail=1; }
printf '%s\n' "$o" | grep -q 'fx/tbl-nocatchall.txt' \
  || { echo "canary: the no-matching-row refusal did not name the table: $o"; fail=1; }

# 4j. THE LENGTH BOUND on every hardware reading, and nothing else observes it. Both `[ "$v" -gt 0 ]`
#     and `$(( ))` ERROR on an int64 overflow instead of comparing, which is how a 20-digit width
#     value once span the dispatch loop forever having executed ZERO legs. A rejected reading is
#     UNKNOWN, so the run still completes and every leg still runs.
for bad in 99999999999999999999 not-a-number; do
n=$((n+1))
n=$((n+1))
  o=$(runp GATE_CORES="$bad" GATE_RAM_MB="$bad")
  printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
    || { echo "canary: hardware seam '$bad' did not complete with every leg run"; printf '%s\n' "$o" | tail -3 | sed 's/^/    /'; fail=1; }
  case "$(profline "$o")" in *'detection failed'*) ;; *) echo "canary: hardware seam '$bad' was not rejected by the length bound: $(profline "$o")"; fail=1 ;; esac
done

# 4k. THE DETECTION CHAIN ITSELF. The GATE_CORES/GATE_RAM_MB seams BYPASS detection, so no arm above
#     this one exercises a single real source. A PATH shim fails the first core source and the first
#     RAM source; the runner must still resolve a profile, and its line must name the chain it walked
#     rather than reading like a first-source hit.
printf '#!/usr/bin/env bash\nexit 7\n' > "$P/shim/nproc"
printf '#!/usr/bin/env bash\nexit 7\n' > "$P/shim/getconf"
chmod +x "$P/shim/nproc" "$P/shim/getconf"
n=$((n+1))
n=$((n+1))
o=$( cd "$P" && env GATE_FULL= GATE_BASE= PATH="$P/shim:$PATH" bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
  || { echo "canary: with its first core and RAM sources failing, the runner did not complete"; printf '%s\n' "$o" | tail -3 | sed 's/^/    /'; fail=1; }
case "$(profline "$o")" in
  *'via nproc,getconf'*) ;;
  *) echo "canary: the detection chain fell through but the line does not name the sources it tried: $(profline "$o")"; fail=1 ;;
esac
rm -f "$P/shim/nproc" "$P/shim/getconf"

[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "canary: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; fail=1; }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] && exit 0 || exit 1

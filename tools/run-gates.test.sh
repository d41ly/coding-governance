#!/usr/bin/env bash
# run-gates.test.sh — canary: gate-legs.json is well-formed AND run-gates.sh sources every leg from it
# (no inlined leg command). Exit 0 = clean. Runs as a leg of run-gates.sh itself.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "canary: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/tools/lib/resolve-python.sh"
PYBIN=$(resolve_python) || { echo "canary: no usable python"; exit 2; }
fail=0

# 1. manifest well-formed: non-empty list; every leg has a non-empty name, an argv with a launcher
#    AND a script (len >= 2), and argv[0] in the allowed set. An empty name is the runner's
#    drop-sentinel (run-gates.sh skips it), and a launcher-only argv runs `bash </dev/null` = a silent
#    no-op GATE ok — both are green-by-absence shapes this canary exists to forbid.
"$PYBIN" -c '
import json, sys
try:
    legs = json.load(open("tools/gate-legs.json"))
except Exception as e:
    print("canary: gate-legs.json does not parse: %s" % e); sys.exit(1)
if not isinstance(legs, list) or not legs:
    print("canary: gate-legs.json is empty or not a list"); sys.exit(1)
ok = {"bash", "python", "python3", "node"}   # node joined with the workflow-script gates (U6)
bad = [l.get("name", "?") for l in legs
       if not str(l.get("name", "")).strip() or not l.get("argv") or len(l["argv"]) < 2 or l["argv"][0] not in ok]
if bad:
    print("canary: malformed leg(s) (empty name, argv len < 2, or argv[0] not in {bash,python,python3,node}): " + ", ".join(bad)); sys.exit(1)
' || fail=1

# 1b. every `guard` pathspec matches at least one TRACKED path. This is the quietest hole a guard can
#     open: `git diff --quiet BASE -- does/not/exist` reports NO difference, so a leg guarded on a
#     typo, a renamed kit or a deleted file skips on EVERY scoped run, forever, printing a reassuring
#     `GATE skip`. Checked against `git ls-files` rather than the filesystem, because the guard is a
#     pathspec git resolves, and an untracked file is invisible to it.
"$PYBIN" -c '
import json, subprocess, sys
tracked = subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split()
bad = []
for l in json.load(open("tools/gate-legs.json")):
    for g in l.get("guard", []):
        if not any(t == g or t.startswith(g) for t in tracked):
            bad.append("%s -> %s" % (l["name"], g))
if bad:
    print("canary: guard pathspec matches no tracked path (the leg would skip forever): " + "; ".join(bad))
    sys.exit(1)
' || fail=1

# 2. no leg SCRIPT-PATH arg (argv[1..] that looks like a path) is hardcoded in run-gates.sh —
#    launcher tokens (bash/python/python3) and flags are excluded; the parse path is the manifest
#    filename, not a leg path, so it never matches.
paths=$("$PYBIN" -c '
import json, sys
rows = [a for l in json.load(open("tools/gate-legs.json")) for a in l["argv"][1:] if "/" in a or a.endswith(".sh") or a.endswith(".py")]
sys.stdout.buffer.write(("\n".join(rows) + ("\n" if rows else "")).encode())   # LF bytes (Windows text stdout is CRLF)
')
while IFS= read -r p; do
  [ -z "$p" ] && continue
  if grep -qF -- "$p" tools/run-gates.sh; then
    echo "canary: leg script path '$p' is hardcoded in run-gates.sh — source it from gate-legs.json"; fail=1
  fi
done <<<"$paths"

# 3. the bounded pool: concurrency must not change WHAT the bar reports, only how fast. Every arm
#    below runs against a SCRATCH repo carrying its own four-leg manifest — never the real 47-leg
#    bar, which would cost minutes and couple this canary to every other kit's health.
SCRATCH=$(mktemp -d) || { echo "canary: cannot create a scratch dir"; exit 2; }
trap 'rm -rf "$SCRATCH"' EXIT
mkdir -p "$SCRATCH/tools/lib" "$SCRATCH/fx"
cp "$ROOT/tools/run-gates.sh" "$SCRATCH/tools/run-gates.sh"
cp "$ROOT/tools/lib/resolve-python.sh" "$SCRATCH/tools/lib/resolve-python.sh"
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
run_scratch() { rm -rf "$SCRATCH/fx/ts"; ( cd "$SCRATCH" && GATE_FULL= GATE_BASE= GATE_JOBS=$1 bash tools/run-gates.sh 2>&1 ); }
# Read IMMEDIATELY after a run: the next run_scratch deletes these.
peaks_now()  { cat "$SCRATCH/fx/ts"/*.peak 2>/dev/null | sort -rn | tr "\n" " "; }
npeaks_now() { ls "$SCRATCH/fx/ts"/*.peak 2>/dev/null | grep -c . || true; }

# 3a. width 1 and width 4 agree line for line. This is the equivalence the pool rests on: one code
#     path, so the serial reading is not a second implementation that can drift.
s1=$(run_scratch 1); peaks1=$(peaks_now); n1=$(npeaks_now)
s4=$(run_scratch 4); peaks4=$(peaks_now); n4=$(npeaks_now)
if [ "$s1" != "$s4" ]; then
  echo "canary: GATE_JOBS=1 and GATE_JOBS=4 disagree — concurrency changed the report"
  diff <(printf '%s\n' "$s1") <(printf '%s\n' "$s4") | sed 's/^/    /'; fail=1
fi

# 3b. reporting is in MANIFEST order even though leg 1 finishes last.
got=$(printf '%s\n' "$s4" | grep -c '^GATE ')
ordered=$(printf '%s\n' "$s4" | grep '^GATE ' | sed 's/^GATE [a-z]*  *//')
want=$'alpha slow\nbeta fast\ngamma fast\ndelta fast'
if [ "$ordered" != "$want" ]; then
  echo "canary: legs did not report in manifest order under concurrency; got:"
  printf '%s\n' "$ordered" | sed 's/^/    /'; fail=1
fi
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
[ "$n4" = 4 ] || { echo "canary: width-4 produced $n4 rendezvous record(s), not 4 - the arm would compare a smaller set than it claims"; fail=1; }
[ "$n1" = 4 ] || { echo "canary: width-1 produced $n1 rendezvous record(s), not 4 - the arm would compare a smaller set than it claims"; fail=1; }
# The peak is the FIRST field of the reverse-sorted list: the most legs any one leg ever saw at once.
peak4=${peaks4%% *}; peak1=${peaks1%% *}
[ "$peak4" = 4 ] || { echo "canary: width-4 peaked at $peak4 legs in flight, not 4 - the pool did not dispatch the batch together (peaks: $peaks4, wait ${RVWAIT_TICKS}x100ms)"; fail=1; }
# THE NEGATIVE CONTROL, and it is what gives the line above its meaning: the same fixtures at width 1
# must NEVER see a peer. Without it the arm passes on any implementation that writes a 4.
[ "$peak1" = 1 ] || { echo "canary: width-1 peaked at $peak1 legs in flight, not 1 - the serial path overlapped, so the width-4 reading proves nothing (peaks: $peaks1)"; fail=1; }

# 3d. a failing leg keeps its exit code, its indented output, and its row in the durable summary.
cp "$SCRATCH/fx/bad.sh" "$SCRATCH/fx/mid.sh"
red=$(run_scratch 4)
printf '%s\n' "$red" | grep -q '^GATE FAIL  beta fast (exit 3)$' \
  || { echo "canary: a failing leg lost its GATE FAIL line or exit code"; fail=1; }
printf '%s\n' "$red" | grep -q '^    boom detail$' \
  || { echo "canary: a failing leg's output was not indented under its GATE FAIL line"; fail=1; }
printf '%s\n' "$red" | grep -q '^gates RED — 3/4 legs failed$' \
  || { echo "canary: the RED verdict line did not tally the failing legs"; fail=1; }
grep -q 'beta fast' "$SCRATCH/.git/gate-last-summary.txt" 2>/dev/null \
  || { echo "canary: the failing leg never reached gate-last-summary.txt"; fail=1; }
printf '#!/usr/bin/env bash\n%s\nsleep 1.5\nexit 0\n' "$rendezvous" > "$SCRATCH/fx/mid.sh"   # restored WITH the rendezvous, or 3d leaves a fixture the later arms cannot use

# 3e. the timing cache is ADVISORY. A corrupt one must cost wall clock and nothing else, because it
#     is written by every run and a half-written file after a kill is the expected state, not a bug.
printf 'not\ta\tnumber\n\x00garbage\n' > "$SCRATCH/.git/gate-timings.tsv"
corrupt=$(run_scratch 4)
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
cp "$SCRATCH/fx/instant.sh" "$SCRATCH/fx/slow.sh"; cp "$SCRATCH/fx/instant.sh" "$SCRATCH/fx/mid.sh"
for w in 0 -3 nonsense 99999999999999999999 999999999999999999999999999999; do
  out=$(GATE_FULL= GATE_BASE= GATE_JOBS="$w" timeout 60 bash -c "cd '$SCRATCH' && bash tools/run-gates.sh" 2>&1); trc=$?
  [ "$trc" = 124 ] && { echo "canary: GATE_JOBS='$w' never terminated — the clamp let it spin"; fail=1; continue; }
  printf '%s\n' "$out" | grep -q '^gates GREEN — 4/4 legs passed$' \
    || { echo "canary: GATE_JOBS='$w' did not clamp to a working width"; printf '%s\n' "$out" | tail -3 | sed 's/^/    /'; fail=1; }
done

# 3g. a healthy leg is NEVER reported "(no result)" — the reader must not conclude a still-pending
#     leg is dead just because no job is RUNNING at the instant it looks.
#     This is a RACE, and the fixture is tuned to the condition that actually reproduces it rather
#     than to a plausible-looking one. MEASURED against the pre-fix reader: 30 instant legs at
#     WIDTH 1 fires 6 runs in 8, while widths 2, 4 and 8 fire 0 in 8 — at width 1 the reader
#     dispatches a worker and looks for its result immediately, which is the whole window. An earlier
#     version of this arm used the 4-leg manifest at mixed widths, reproduced at 1-in-40, and let the
#     pre-fix reader pass. Do not "simplify" this back to the shared fixture.
mkdir -p "$SCRATCH/many/tools/lib" "$SCRATCH/many/fx"
cp "$SCRATCH/tools/run-gates.sh" "$SCRATCH/many/tools/run-gates.sh"
cp "$ROOT/tools/lib/resolve-python.sh" "$SCRATCH/many/tools/lib/resolve-python.sh"
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
  o=$( cd "$SCRATCH/many" && GATE_FULL= GATE_BASE= GATE_JOBS=1 bash tools/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^gates GREEN — 30/30 legs passed$' \
    || { echo "canary: the 30-leg width-1 fixture did not run — arm 3g proves nothing"
         printf '%s\n' "$o" | tail -3 | sed 's/^/    /'; fail=1; break; }
  case "$o" in
    *"(no result)"*) echo "canary: a healthy leg was reported (no result) — the reader gave up before its worker landed"
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
mkdir -p "$G/tools/lib" "$G/fx"
cp "$SCRATCH/tools/run-gates.sh" "$G/tools/run-gates.sh"
cp "$ROOT/tools/lib/resolve-python.sh" "$G/tools/lib/resolve-python.sh"
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
o=$( cd "$G" && GATE_FULL= GATE_BASE= GATE_JOBS=4 bash tools/run-gates.sh 2>&1 )
printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$' \
  || { echo "canary: with no resolvable BASE a guarded leg did not fail safe to RUN"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
# Pass 2 with origin/HEAD pinned: the guard path resolves and the unchanged leg must SKIP.
( cd "$G" && git update-ref refs/remotes/origin/main HEAD \
  && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
for w in 1 4; do
  o=$( cd "$G" && GATE_FULL= GATE_BASE= GATE_JOBS=$w bash tools/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^GATE skip  guarded (unchanged vs main)$' \
    || { echo "canary: width $w printed no GATE skip line for a guarded, unchanged leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed (1 skipped)$' \
    || { echo "canary: width $w did not tally the skip (expected 2/2 passed, 1 skipped)"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  [ "$(printf '%s\n' "$o" | grep '^GATE ' | sed -n 2p)" = "GATE skip  guarded (unchanged vs main)" ] \
    || { echo "canary: width $w reported the skipped leg away from its manifest position"; fail=1; }
done
# C1: the skipped leg produced no timing this run. Its CACHED row from pass 1 must survive, or every
# diff-scoped run blanks the dispatch hint the next full run needs.
grep -q '^guarded	' "$G/.git/gate-timings.tsv" 2>/dev/null \
  || { echo "canary: the skipped leg's cached timing row was dropped by the cache rewrite"; fail=1; }

# 3i. GATE_FULL bypasses every guard. This is the invariant the whole diff-scoping scheme rests on:
#     `.githooks/pre-push` sets it, so a guard can only ever scope a NON-authoritative run and a
#     too-narrow guard costs an early signal rather than a wrong merge verdict. Asserted against the
#     SAME fixture that skips without it, so the two readings differ only by the variable.
for w in 1 4; do
  o=$( cd "$G" && GATE_FULL=1 GATE_BASE= GATE_JOBS=$w bash tools/run-gates.sh 2>&1 )
  printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$' \
    || { echo "canary: GATE_FULL=1 at width $w did not run every leg past its guard"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^GATE skip' \
    && { echo "canary: GATE_FULL=1 at width $w still skipped a guarded leg"; fail=1; }
done

# 3j. the push boundary FORCES the full bar. The hook is the only place this is guaranteed, and a
#     scoped authoritative run would mean no run ever executes every leg against the tree that lands.
grep -q '^export GATE_FULL=1$' "$ROOT/.githooks/pre-push" \
  || { echo "canary: .githooks/pre-push does not force GATE_FULL — the authoritative run would be diff-scoped"; fail=1; }

[ "$fail" = 0 ] && exit 0 || exit 1

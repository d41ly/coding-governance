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
printf '#!/usr/bin/env bash\nsleep 2\nexit 0\n'            > "$SCRATCH/fx/slow.sh"
printf '#!/usr/bin/env bash\nsleep 1.5\nexit 0\n'          > "$SCRATCH/fx/mid.sh"
printf '#!/usr/bin/env bash\necho "boom detail"\nexit 3\n' > "$SCRATCH/fx/bad.sh"
printf '#!/usr/bin/env bash\nexit 0\n'                     > "$SCRATCH/fx/instant.sh"
cat > "$SCRATCH/tools/gate-legs.json" <<'JSON'
[
  {"name": "alpha slow", "argv": ["bash", "fx/slow.sh"]},
  {"name": "beta fast",  "argv": ["bash", "fx/mid.sh"]},
  {"name": "gamma fast", "argv": ["bash", "fx/mid.sh"]},
  {"name": "delta fast", "argv": ["bash", "fx/mid.sh"]}
]
JSON
( cd "$SCRATCH" && git init -q . && git config user.email t@e && git config user.name t ) >/dev/null 2>&1

run_scratch() { ( cd "$SCRATCH" && GATE_JOBS=$1 bash tools/run-gates.sh 2>&1 ); }

# 3a. width 1 and width 4 agree line for line. This is the equivalence the pool rests on: one code
#     path, so the serial reading is not a second implementation that can drift.
t0=$(date +%s%N); s1=$(run_scratch 1); t1=$(date +%s%N); ser_ms=$(( (t1-t0)/1000000 ))
t0=$(date +%s%N); s4=$(run_scratch 4); t1=$(date +%s%N); par_ms=$(( (t1-t0)/1000000 ))
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

# 3c. concurrency actually OVERLAPS. Asserted as a RATIO between the two runs arm 3a already made on
#     this machine at this moment, never as an absolute deadline. An earlier version pinned
#     `par_ms < 5000`, which graded this leg against load it does not control: it is leg 47 of 47 and
#     the bar now dispatches at width 8, so it times itself while competing with seven siblings.
#     Measured idle at 2.7-3.6s but 4.1-9.8s under contention, and the bar's own cache records this
#     whole leg at 65s against a ~16.5s sleep floor. A trip would red the bar for a reason unrelated
#     to any leg's assertion and point the operator straight at --no-verify. Uniform load and cold
#     start cancel in a ratio; a pool degraded to serial still fails it, because then par ~= ser.
[ $((par_ms*2)) -lt "$ser_ms" ] \
  || { echo "canary: width-4 (${par_ms}ms) did not beat half of width-1 (${ser_ms}ms) — the pool is not overlapping"; fail=1; }

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
printf '#!/usr/bin/env bash\nsleep 1.5\nexit 0\n' > "$SCRATCH/fx/mid.sh"

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
  out=$(GATE_JOBS="$w" timeout 60 bash -c "cd '$SCRATCH' && bash tools/run-gates.sh" 2>&1); trc=$?
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
  o=$( cd "$SCRATCH/many" && GATE_JOBS=1 bash tools/run-gates.sh 2>&1 )
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
o=$( cd "$G" && GATE_JOBS=4 bash tools/run-gates.sh 2>&1 )
printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$' \
  || { echo "canary: with no resolvable BASE a guarded leg did not fail safe to RUN"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
# Pass 2 with origin/HEAD pinned: the guard path resolves and the unchanged leg must SKIP.
( cd "$G" && git update-ref refs/remotes/origin/main HEAD \
  && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
for w in 1 4; do
  o=$( cd "$G" && GATE_JOBS=$w bash tools/run-gates.sh 2>&1 )
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

[ "$fail" = 0 ] && exit 0 || exit 1

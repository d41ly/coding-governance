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
FLOOR_ASSERTIONS=129
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

# 1a. THE MANIFEST KEY SET. Every row carries `name` and `argv`, may carry `guard` and `impure`,
#     and carries nothing else. A mistyped `impure` — `impur`, `Impure`, `inpure` — is otherwise
#     silent: the reuse path reads the key it knows, finds nothing, and treats a leg whose verdict
#     depends on a remote as reusable on a byte-identical tree. The typo is the whole failure
#     mode, so the pin is on the SET rather than on any one key.
#
#     A SCHEMA ARM, which is why it ships. It asserts a shape true of any manifest in any tree and
#     names no leg of this repo's corpus; the gov-only harness next door holds the arms that do.
#     It reads LEGS_FILE — the derived path — so it grades whatever manifest the tree it runs in
#     actually has, and hardcoding `tools/gate-legs.json` in a harness that ships is the
#     pin-copied-from-another-corpus class this kit refuses by name.
#
#     ITS CONTROL IS A MANIFEST WITH NO `impure` ANYWHERE, WHICH MUST PASS. The key is optional
#     and, until a deployer unit teaches govkit to carry it, gov-only: an adopting tree's emitted
#     manifest cannot contain one. An arm that reds on its ABSENCE is an arm that reds in every
#     adopting tree on arrival, which is the same defect one level up from the one it guards.
n=$((n+1))
"$PYBIN" -c '
import json, sys
KNOWN = {"name", "argv", "guard", "impure", "chunk", "subject", "ceiling"}
try:
    legs = json.load(open(sys.argv[1]))
except Exception as e:
    print("canary: %s does not parse: %s" % (sys.argv[1], e)); sys.exit(1)
stray = []
for l in legs:
    if not isinstance(l, dict):
        print("canary: a leg row is not an object"); sys.exit(1)
    for k in l:
        if k not in KNOWN:
            stray.append("%s -> %s" % (l.get("name", "?"), k))
if stray:
    print("canary: leg row(s) carry a key outside the pinned set %s: %s"
          % (sorted(KNOWN), ", ".join(stray)))
    print("canary: a near-miss spelling of `impure` is exactly what this pin exists to catch —")
    print("canary: the reuse path would find no declaration and reuse a leg that reads a remote.")
    sys.exit(1)
' "$LEGS_FILE" || fail=1

# ---- 1c. THE PER-LEG CEILING'S BOUND IS A CLOCK, NOT A MESSAGE. TOOL-aBoundedCeiling-1 AC1/AC2.
#     The message was always the correct half of memory/gotchas/bounded-through-a-pipe-is-unbounded.md,
#     so an arm asserting "timed out after Ns" is satisfied by the broken code. This one measures
#     ELAPSED TIME against a control, which is the only instrument that can see the defect.
#
#     IT GRADES THE CONSTRUCT, NOT THE BAR. A whole-bar timing assertion is a fact about the node:
#     measured on node `a` while writing this, a bar carrying ONE trivial leg exceeded 120 s under
#     ambient load, which would make any absolute bar-level bound flaky in exactly the way that
#     drives people to delete arms. The construct below is compared against a 60 s sleeper, a 30x
#     margin, so it survives a slow box and still fails a wrong construct.
#
#     WHAT IT DOES NOT CHECK: that run-gates.sh USES this construct. Arm 1d does that, by source.
n=$((n+1))
_cw=$(mktemp -d)
_t0=$(date +%s)
timeout -k 5s 2 bash -c 'sleep 60 & exit 0' </dev/null >"$_cw/grandchild.raw" 2>&1
_t1=$(date +%s)
_took=$(( _t1 - _t0 ))
# The control: the SAME command through a command substitution, which is the form that does not
# bound the clock. Without it a green here could mean "this box is fast", not "the form is right".
_t2=$(date +%s)
_ctl=$(timeout -k 5s 2 bash -c 'sleep 60 & exit 0' 2>&1)
_t3=$(date +%s)
_ctltook=$(( _t3 - _t2 ))
if [ "$_took" -gt 20 ]; then
  echo "canary: a file-captured 2s timeout over a backgrounded grandchild took ${_took}s — the bound"
  echo "canary: is on the verdict and not on the clock, which is bounded-through-a-pipe-is-unbounded."
  fail=1
elif [ "$_ctltook" -le 20 ]; then
  echo "canary: the CONTROL returned in ${_ctltook}s, so this host does not reproduce the pipe defect"
  echo "canary: and the arm above proved nothing. Not a pass: a control that cannot fail is the"
  echo "canary: vacuous-selector class, and this arm is reported UNPROVEN rather than green."
  fail=1
fi
rm -rf "$_cw"

# ---- 1d. THE RUNNER USES THAT CONSTRUCT. Scoped to CODE LINES: a whole-file grep reds on the
#     comments documenting the fix, which is absence-assertion-over-whole-file-text happening inside
#     the guard. TOOL-aBoundedCeiling-1.
n=$((n+1))
if grep -nE '^[[:space:]]*[^#]*=\$\(timeout ' "$KITDIR/run-gates.sh" >/dev/null 2>&1; then
  echo "canary: run-gates.sh captures a timeout through a command substitution on a code line —"
  echo "canary: that bounds the verdict and not the clock. Redirect to a file and read the file."
  grep -nE '^[[:space:]]*[^#]*=\$\(timeout ' "$KITDIR/run-gates.sh" | sed 's/^/    /'
  fail=1
fi

# 1a-control: the same predicate over a manifest with NO `impure` key must PASS, and over one with
#     a near-miss spelling must FAIL. Both halves, because the arm above is a negative search and a
#     negative search passes just as happily over a population it never selected.
n=$((n+1))
ctl=$(mktemp -d)
printf '%s' '[{"name":"a","argv":["bash","x.sh"]},{"name":"b","argv":["bash","y.sh"],"guard":["z/"]}]' > "$ctl/clean.json"
printf '%s' '[{"name":"a","argv":["bash","x.sh"],"impur":"typo"}]' > "$ctl/typo.json"
keyset_probe() { "$PYBIN" -c '
import json, sys
KNOWN = {"name", "argv", "guard", "impure", "chunk", "subject", "ceiling"}
legs = json.load(open(sys.argv[1]))
sys.exit(1 if any(k not in KNOWN for l in legs for k in l) else 0)
' "$1"; }
if keyset_probe "$ctl/clean.json" && ! keyset_probe "$ctl/typo.json"; then :
else
  echo "canary: the manifest key-set predicate is unarmed — it must PASS a manifest with no impure key and FAIL a near-miss spelling; one of the two did not hold"
  fail=1
fi
rm -rf "$ctl"
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
printf 'not\ta\tnumber\n\x00garbage\n' > "$SCRATCH/.git/gate-ledger.tsv"
corrupt=$(run_scratch 4)
n=$((n+1))
printf '%s\n' "$corrupt" | grep -q '^gates GREEN — 4/4 legs passed$' \
  || { echo "canary: a corrupt gate-ledger.tsv changed the verdict"; printf '%s\n' "$corrupt" | sed 's/^/    /'; fail=1; }

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
grep -q '^guarded	' "$G/.git/gate-ledger.tsv" 2>/dev/null \
  || { echo "canary: the skipped leg's cached row was dropped by the ledger rewrite"; fail=1; }

# 3h2. SUBJECT: a kit-subject leg is HELD unless asked, and GATE_FULL does not ask.
#     TOOL-dUnstalledConvoy-26. A kit self-test stages a break into a copy of a checker and asserts
#     the checker still catches it — a job that exists when the kit's source changes and not at all
#     in a repo that copy-installs the kit and never edits it. The `guard = ["{kit}/"]` those legs
#     used to lean on does NOT do that job: `changed()` returns 0 the instant GATE_FULL is set, and
#     .githooks/pre-push sets it whenever it decides a full run is owed, which is the one boundary an
#     adopter actually feels. So the decision is a declared subject, not a guard.
S="$SCRATCH/subject"
mkdir -p "$S/tools/run-gates" "$S/fx"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$S/tools/run-gates/run-gates.sh"
# The FINGERPRINT script too: `gate-full-green` is written only when FPRINT_START is non-empty, and
# without this file the fingerprint is the empty string, so the stamp arm below would assert against
# a stamp no fixture can produce — passing for the wrong reason or failing for one.
cp "$KITDIR/gate-fingerprint.sh" "$S/tools/run-gates/" 2>/dev/null || true
cp "$SCRATCH/fx/instant.sh" "$S/fx/a.sh"
cat > "$S/tools/gate-legs.json" <<'JSON'
[
  {"name": "a repo leg",        "argv": ["bash", "fx/a.sh"], "subject": "repo"},
  {"name": "a kit self-test",   "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "an undeclared leg", "argv": ["bash", "fx/a.sh"]}
]
JSON
( cd "$S" && git init -q -b main . && git config user.email t@e && git config user.name t \
  && git add -A && git commit -qm fx ) >/dev/null 2>&1

# OFF: the kit leg is held, and it is held with its OWN verb. Not `skip`, whose tail says
# `unchanged vs <branch>` — false here, since the leg is not unchanged, it is out of subject.
o=$( cd "$S" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE held  a kit self-test  ' \
  || { echo "canary: a kit-subject leg was not HELD with the switch off"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE held  a kit self-test  (unchanged vs' \
  && { echo "canary: the held leg reused the guard verb's tail, which claims it was unchanged"; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE ok    a repo leg$' \
  || { echo "canary: a repo-subject leg did not run with the switch off"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
# An UNDECLARED leg defaults to `repo` and RUNS. The other default would silently remove from every
# bar a leg whose descriptor never spoke about subjects at all.
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE ok    an undeclared leg$' \
  || { echo "canary: an undeclared leg did not default to repo and run"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }

# GATE_FULL DOES NOT ASK. This is the arm the whole unit rests on: GATE_FULL means "ignore every
# guard", and a kit's own self-tests are not a guard. If this ever passes, every adopter is back to
# running them at the push boundary.
o=$( cd "$S" && GATE_FULL=1 GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE held  a kit self-test  ' \
  || { echo "canary: GATE_FULL unlocked the kit-subject legs, which is the bypass this replaced"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }

# ON: the switch is the only thing that asks, and it asks for all of them.
o=$( cd "$S" && GATE_FULL= GATE_SELFTESTS=1 GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE ok    a kit self-test$' \
  || { echo "canary: GATE_SELFTESTS=1 did not run the kit-subject leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q '^GATE held' \
  && { echo "canary: something was still held with the switch on"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
# ...and the switch state reaches the stamp, or a green cannot say what it covered and the push
# boundary has nothing to read. TOOL-dUnstalledConvoy-27 is the reader.
n=$((n+1))
grep -q '^selftests	1$' "$S/.git/gate-full-green" 2>/dev/null \
  || { echo "canary: a switch-ON green did not record the switch in its stamp"; fail=1; }
# ITS NEGATIVE CONTROL, and without it the field is unfalsifiable: an implementation that wrote an
# unconditional `1` passes every other arm in this file, and the push boundary's coverage predicate
# then reads every partial bar as a complete one. The row must be present and EMPTY, never absent —
# absent and empty read the same to a grep, and TOOL-dUnstalledConvoy-27 defaults a missing key to
# HELD, so the two agree; what must not happen is a `1`.
o=$( cd "$S" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
grep -q '^selftests	1$' "$S/.git/gate-full-green" 2>/dev/null \
  && { echo "canary: a switch-OFF green recorded selftests=1 — the stamp claims a coverage the run did not have"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }

# 3h3. THE HELD LEGS REACH THE ARITHMETIC: the run total, the recorded figure, and the chunk close.
#     TOOL-dUnstalledConvoy-31 and -32. Its parent gave the on-demand hold its own counter so it
#     would stay out of `skips`, which the full-green stamp conjoins. Kept out of `skips`, it was
#     also kept out of every figure `skips` feeds — so a bar that ran 43 of 85 legs printed
#     `85/85 legs passed`, and the chunk holding nothing but kit self-tests closed GREEN. Both
#     numbers are what a reader quotes, which is what makes this arithmetic worth an arm.
S2="$SCRATCH/heldmath"
mkdir -p "$S2/tools/run-gates" "$S2/fx"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$S2/tools/run-gates/run-gates.sh"
cp "$KITDIR/gate-fingerprint.sh" "$S2/tools/run-gates/" 2>/dev/null || true
cp "$SCRATCH/fx/instant.sh" "$S2/fx/a.sh"
# TWO CHUNKS, ONE OF EACH SHAPE. `mixed` proves the tally is per-chunk and does not swallow the
# chunk it appears in; `held` proves the all-held chunk changes verdict. A fixture with only the
# second would pass on a runner that called every chunk skipped.
cat > "$S2/tools/gate-legs.json" <<'JSON'
[
  {"name": "m repo one", "argv": ["bash", "fx/a.sh"], "subject": "repo", "chunk": "mixed"},
  {"name": "m repo two", "argv": ["bash", "fx/a.sh"], "subject": "repo", "chunk": "mixed"},
  {"name": "m kit one",  "argv": ["bash", "fx/a.sh"], "subject": "kit",  "chunk": "mixed"},
  {"name": "h kit one",  "argv": ["bash", "fx/a.sh"], "subject": "kit",  "chunk": "held"},
  {"name": "h kit two",  "argv": ["bash", "fx/a.sh"], "subject": "kit",  "chunk": "held"}
]
JSON
( cd "$S2" && git init -q -b main . && git config user.email t@e && git config user.name t \
  && git add -A && git commit -qm fx ) >/dev/null 2>&1

o=$( cd "$S2" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
# -31 AC1: the total is the count that RAN. Two repo legs ran, so the total is 2 and not 5.
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed' \
  || { echo "canary: the run total counted legs that were held rather than run"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }
# -31 AC2: and it NAMES the held population, or the smaller number is a smaller lie — a bar that
# shrank with no explanation reads as a bar that shrank for reasons nobody recorded.
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed (3 held: kit self-tests, GATE_SELFTESTS=1 runs them)$' \
  || { echo "canary: the summary did not name the held population beside the reduced total"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }
# -31 AC3: the RECORDED figure is the printed one. Two call sites computing one number is how they
# come to disagree, and the record is what a later run and the push boundary read instead of stdout.
n=$((n+1))
vf="$S2/.git/gate-run/$(cat "$S2/.git/gate-run/current" 2>/dev/null)/verdict"
if [ -f "$vf" ]; then
  awk -F'\t' '$1=="ran" && $2==2 {ok=1} END{exit !ok}' "$vf" \
    || { echo "canary: the recorded run figure disagrees with the printed total"; awk -F'\t' '$1=="ran"||$1=="held"||$1=="skipped"' "$vf" | sed 's/^/    /'; fail=1; }
  n=$((n+1))
  awk -F'\t' '$1=="held" && $2==3 {ok=1} END{exit !ok}' "$vf" \
    || { echo "canary: the held count is not on the run record at all"; fail=1; }
else
  echo "canary: no verdict record was written, so the recorded-figure arms prove nothing"; fail=1
fi
# -32 AC1: an all-held chunk closes SKIPPED. The runner already had this rule for guard-skips and
# already asserted it in a comment; what it lacked was reachability from the newer skip kind.
n=$((n+1))
printf '%s\n' "$o" | grep -qE '^---- chunk held: skipped  \(0 ran, 0 failed, 0 skipped, 0 reused, 2 held\)$' \
  || { echo "canary: a chunk whose every leg was held closed green-by-absence"; printf '%s\n' "$o" | grep -- '---- chunk' | sed 's/^/    /'; fail=1; }
# -32 AC2: its control — a chunk that DID run stays green, and carries its own held tally. Without
# this a runner that called every chunk skipped would pass the arm above.
n=$((n+1))
printf '%s\n' "$o" | grep -qE '^---- chunk mixed: green  \(2 ran, 0 failed, 0 skipped, 0 reused, 1 held\)$' \
  || { echo "canary: a mixed chunk lost its held tally or changed verdict"; printf '%s\n' "$o" | grep -- '---- chunk' | sed 's/^/    /'; fail=1; }

# -31 AC4: with the switch ON nothing is held, so the total is the whole manifest and the note is
# gone. A note that survives a run with nothing to report is the same defect pointing the other way.
o=$( cd "$S2" && GATE_FULL= GATE_SELFTESTS=1 GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN — 5/5 legs passed$' \
  || { echo "canary: with the switch on the total was not the whole manifest, or a stale held note survived"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }

# 3h4. AN ALL-HELD RUN REFUSES. TOOL-dUnstalledConvoy-26 AC10. A repository whose whole manifest is
#      kit-subject would otherwise print `gates GREEN — 0/0 legs passed` on every run forever while
#      executing not one leg, and stamp a record saying so. Measured before the fix: exit 0 and
#      exactly that line.
S3="$SCRATCH/allheld"
mkdir -p "$S3/tools/run-gates" "$S3/fx"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$S3/tools/run-gates/run-gates.sh"
cp "$KITDIR/gate-fingerprint.sh" "$S3/tools/run-gates/" 2>/dev/null || true
cp "$SCRATCH/fx/instant.sh" "$S3/fx/a.sh"
cat > "$S3/tools/gate-legs.json" <<'JSON'
[
  {"name": "k one", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "k two", "argv": ["bash", "fx/a.sh"], "subject": "kit"}
]
JSON
( cd "$S3" && git init -q -b main . && git config user.email t@e && git config user.name t \
  && git add -A && git commit -qm fx ) >/dev/null 2>&1

o=$( cd "$S3" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 ); rc=$?
n=$((n+1))
[ "$rc" = 2 ] \
  || { echo "canary: an all-held run exited $rc, not the configuration-refusal code 2"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q 'executed NOTHING' \
  || { echo "canary: an all-held run did not say it executed nothing"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q 'GATE_SELFTESTS=1' \
  || { echo "canary: the refusal did not name the switch that would fix it"; fail=1; }
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates GREEN' \
  && { echo "canary: an all-held run reported a GREEN over an empty population"; fail=1; }

# ITS CONTROL, and it is what keeps the refusal narrow. The SAME manifest with one repo-subject leg
# added is an ordinary partial bar and must stay green — a refusal that fired here would red every
# adopter whose kits are all held, which is every adopter.
cat > "$S3/tools/gate-legs.json" <<'JSON'
[
  {"name": "k one", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "k two", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "r one", "argv": ["bash", "fx/a.sh"], "subject": "repo"}
]
JSON
( cd "$S3" && git add -A && git commit -qm two ) >/dev/null 2>&1
o=$( cd "$S3" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 ); rc=$?
n=$((n+1))
{ [ "$rc" = 0 ] && printf '%s\n' "$o" | grep -q '^gates GREEN — 1/1 legs passed'; } \
  || { echo "canary: CONTROL — one repo-subject leg beside two held ones must still be a green partial bar, got rc=$rc"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }
# ...and with the switch ON the all-held manifest is an ordinary full bar, not a refusal. The
# refusal is about a run that executed nothing, never about the subject values themselves.
o=$( cd "$S3" && GATE_FULL= GATE_SELFTESTS=1 GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 ); rc=$?
n=$((n+1))
{ [ "$rc" = 0 ] && printf '%s\n' "$o" | grep -q '^gates GREEN — 3/3 legs passed$'; } \
  || { echo "canary: CONTROL — with the switch on, the same manifest must run every leg, got rc=$rc"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }

# M4 — THE REFUSAL LEAVES A RECORD. This runner's crash signal is a run directory with a header and
# NO verdict, so exiting between the two manufactures that signature for a deliberate refusal; and
# the durable summary would otherwise still carry the PREVIOUS run's `gates GREEN` for anyone who
# reads the file instead of the terminal.
cat > "$S3/tools/gate-legs.json" <<'JSON'
[
  {"name": "k one", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "k two", "argv": ["bash", "fx/a.sh"], "subject": "kit"}
]
JSON
( cd "$S3" && git add -A && git commit -qm allheld ) >/dev/null 2>&1
( cd "$S3" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh >/dev/null 2>&1 )
n=$((n+1))
vf3="$S3/.git/gate-run/$(cat "$S3/.git/gate-run/current" 2>/dev/null)/verdict"
awk -F'\t' '$1=="verdict" && $2=="REFUSED"{ok=1} END{exit !ok}' "$vf3" 2>/dev/null \
  || { echo "canary: the all-held refusal left NO verdict record, which is this runner's crash signature"; fail=1; }
n=$((n+1))
grep -q 'gates REFUSED' "$S3/.git/gate-last-summary.txt" 2>/dev/null \
  || { echo "canary: the durable summary does not say the run was refused"; sed -n '$p' "$S3/.git/gate-last-summary.txt" 2>/dev/null | sed 's/^/    /'; fail=1; }
n=$((n+1))
grep -q 'gates GREEN' "$S3/.git/gate-last-summary.txt" 2>/dev/null \
  && { echo "canary: a refused run left a GREEN standing in the durable summary"; fail=1; }

# H5 — THE RED LINE'S DENOMINATOR IS WHAT RAN, the same figure the green line uses. `$n` is the whole
# manifest, so a red bar that held 42 legs reported `1/85 legs failed` — a ratio against a
# population it never ran, in the one line a reader looks at when something is broken.
mkdir -p "$S3/fx"
printf '#!/usr/bin/env bash\nexit 1\n' > "$S3/fx/red.sh"
cat > "$S3/tools/gate-legs.json" <<'JSON'
[
  {"name": "k one", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "k two", "argv": ["bash", "fx/a.sh"], "subject": "kit"},
  {"name": "r ok",  "argv": ["bash", "fx/a.sh"], "subject": "repo"},
  {"name": "r bad", "argv": ["bash", "fx/red.sh"], "subject": "repo"}
]
JSON
( cd "$S3" && git add -A && git commit -qm redbar ) >/dev/null 2>&1
o=$( cd "$S3" && GATE_FULL= GATE_SELFTESTS= GATE_JOBS=4 bash tools/run-gates/run-gates.sh 2>&1 )
n=$((n+1))
printf '%s\n' "$o" | grep -q '^gates RED — 1/2 legs failed' \
  || { echo "canary: the RED line's denominator is not the count that ran"; printf '%s\n' "$o" | grep '^gates' | sed 's/^/    /'; fail=1; }
n=$((n+1))
grep -q 'gates RED — 1/2 legs failed' "$S3/.git/gate-last-summary.txt" 2>/dev/null \
  || { echo "canary: the durable RED summary disagrees with stdout about the denominator"; fail=1; }

# 3i. GATE_FULL bypasses every guard. This is the invariant the whole diff-scoping scheme rests on:
#     `.githooks/pre-push` no longer sets it unconditionally: it DECIDES, and forces a total run
#     when no recorded full green covers the pushed tip. So a guard can now scope the
#     authoritative run too, and what bounds the damage is that obligation rather than a
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
# EVERY WRITE BELOW LANDS IN $P, INCLUDING A `tools/gate-legs.json` and a `git config user.email`.
# Assert first that $P is not inside the repo under test — by GIT IDENTITY, never by comparing path
# strings, because under MSYS one directory has two spellings and mount points are not symlinks. A
# scratch resolving into the real tree would overwrite the bar's own leg manifest with a two-leg
# fixture and rewrite this repo's commit identity.
#
# IT EXITS, and it runs BEFORE the mkdir. The first spelling printed REFUSING, set `fail=1`, and then
# performed every write it had just refused — there is no `set -e` here, so a message is not a stop.
# A guard that detects the corruption and then commits it is worse than none, because it also files a
# report saying it held.
if [ "$( cd "$P" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null )" = "$( cd "$ROOT" && git rev-parse --show-toplevel 2>/dev/null )" ]; then
  echo "canary: REFUSING — the section-4 scratch $P resolves to the repo under test, so its fixture writes would clobber the real gate-legs.json and rewrite this repo's commit identity. Nothing was written."
  exit 2
fi
n=$((n+1))
mkdir -p "$P/tools/run-gates" "$P/fx" "$P/shim"
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$P/tools/run-gates/run-gates.sh"
printf '#!/usr/bin/env bash\nexit 0\n'          > "$P/fx/a.sh"
# An ORPHAN plus a foreground sleep, because that pair is what the blocker was made of: the
# grandchild holds the leg's inherited write end open, and a pipe-captured leg then blocks for the
# whole hang no matter what `timeout` reports.
printf '#!/usr/bin/env bash\nbash -c "sleep 20" &\nsleep 20\nexit 0\n' > "$P/fx/sleeper.sh"
# A leg that IGNORES SIGTERM is the only thing that exercises the kill-after at all: `timeout` sends
# TERM at the bound and escalates to KILL only after `-k`, and that path exits 137 rather than 124.
# The first spelling mapped 124 alone, so the very case `-k` exists for reported as a bare exit code
# that reads like an OOM.
printf '#!/usr/bin/env bash\ntrap "" TERM\nsleep 25\nexit 0\n' > "$P/fx/stubborn.sh"
cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "two", "argv": ["bash", "fx/a.sh"]}
]
JSON
( cd "$P" && git init -q . && git config user.email t@e && git config user.name t ) >/dev/null 2>&1
runp() { ( cd "$P" && env GATE_FULL= GATE_BASE= "$@" bash tools/run-gates/run-gates.sh 2>&1 ); }
profline() { printf '%s\n' "$1" | grep '^gate profile: ' | head -1; }
# A LEG's own measured seconds, from the timing cache the runner writes for the next run's dispatch
# hint. Truncated to an integer: the arm compares magnitudes and `[` cannot read a decimal.
leg_secs() { awk -F'\t' -v n="$1" '$1==n { printf "%d", $2 + 0 }' "$P/.git/gate-ledger.tsv" 2>/dev/null; }
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

# THE HOST PROBE that gates 4g and 4h. The runner DELIBERATELY degrades where `timeout` does not run,
# announcing the knob INERT and taking the width alone — a supported state, on a BSD base install or a
# minimal image. Asserting a timeout there reds an adopter's bar and blames the runner's override
# logic for a missing binary. `timeout` is RUN, never probed for on PATH, which is this tree's rule.
HAVE_TIMEOUT=0; timeout 1 true >/dev/null 2>&1 && HAVE_TIMEOUT=1

# 4g. GATE_JOBS overrides the WIDTH ONLY. The row is still selected and still supplies every other
#     knob — an override that silently disabled the rest of the profile would make the table a lie
#     the moment anyone set a width.
printf 'solo\t0\t0\twidth=8,timeout=9\n' > "$P/fx/tbl-timeout.txt"
n=$((n+1))
n=$((n+1))
if [ "$HAVE_TIMEOUT" = 1 ]; then
  pl=$(profline "$(runp GATE_PROFILES=fx/tbl-timeout.txt GATE_JOBS=3)")
  case "$pl" in *'width 3,'*) ;; *) echo "canary: GATE_JOBS=3 did not reach the reported width: $pl"; fail=1 ;; esac
  case "$pl" in *'timeout 9s'*) ;; *) echo "canary: GATE_JOBS suppressed the row's OTHER knob — the override is not width-only: $pl"; fail=1 ;; esac
else
  echo "canary: SKIP arm 4g's timeout half — no working \`timeout\` on this host, so the runner's INERT branch is what runs (arm 4m grades that branch instead)"
  pl=$(profline "$(runp GATE_PROFILES=fx/tbl-timeout.txt GATE_JOBS=3)")
  case "$pl" in *'width 3,'*) ;; *) echo "canary: GATE_JOBS=3 did not reach the reported width: $pl"; fail=1 ;; esac
fi

# 4h. A LEG THAT OUTLIVES THE TIMEOUT IS RED, NAMED, AND THE RUN IS RED. Never a skip and never a
#     green: this knob converts an unbounded hang into a verdict, which is the one way a knob may
#     change coverage at all — upward. Recorded motivating failure: a leg that hung with zero output
#     and wedged a whole bar at 46 of 65.
#
#     WHAT THIS ARM MUST NOT ASSERT IS A COUNT. It first shipped pinning `1/2 legs failed`, and the
#     full bar duly red it: under an 8-wide bar the INSTANT fixture leg also outlived a one-second
#     budget, because spawning bash on a saturated box can take longer than that. The runner was
#     correct and the arm was grading the NODE — the same defect this file's arm 3c retired twice, one
#     level up. So the budget is generous enough that only the sleeper can plausibly exceed it, and
#     what is asserted is the SLEEPER's own row plus a RED verdict, whatever else the machine did.
printf 'tight\t0\t0\twidth=2,timeout=3\n' > "$P/fx/tbl-tight.txt"
cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "sleeper", "argv": ["bash", "fx/sleeper.sh"]}
]
JSON
#
#     AND IT GRADES THE CLOCK, NOT ONLY THE MESSAGE. The first landing of this knob captured the timed
#     leg through a command substitution: `$( )` reads until EOF and EOF waits on the last inherited
#     write end, so an orphaned grandchild held the pipe and the worker blocked for the entire hang
#     while `timeout` reported 124. Measured 51.4 s against a 1 s bound — the verdict bounded, the
#     clock untouched, which is the one property the knob exists for. THIS ARM ASSERTED THE MESSAGE
#     AND PASSED, the fixture-passes-by-finding-nothing class this build names.
#
#     Graded against a CONTROL rather than a deadline: the same fixture, same runner, timeout OFF. An
#     absolute wall-clock budget would grade the NODE — the defect arm 3c retired twice and the defect
#     that red this very arm on the full bar. Load inflates both runs, so the DIFFERENCE survives it.
n=$((n+1))
n=$((n+1))
n=$((n+1))
n=$((n+1))
if [ "$HAVE_TIMEOUT" = 1 ]; then
  o=$(runp GATE_PROFILES=fx/tbl-tight.txt)
  # THE LEG'S CLOCK, NOT THE PROCESS TREE'S. The first spelling subtracted two WHOLE-RUN wall clocks,
  # so the runner's fixed startup — measured at 19 s on node `a`, against a 17 s signal — sat inside
  # both terms along with its jitter. Three sequential pairs of this very fixture gave differences of
  # 12, 11 and 20 s against a threshold of 10, and under bar-shaped load the same arm measured 6, 8
  # and -3: actual REDs, accusing the runner of the blocker this commit fixed. Only the overhead MEAN
  # cancels between two runs; its jitter never does.
  #
  # The runner already writes each leg's own duration to the timing cache, so read THAT, between the
  # two runs — the control overwrites the row. Signal against measured constant is now ~20 s to ~0 s
  # rather than 17 s to 19 s; that ratio is the number to re-check before shortening the fixture.
  t_timed=$(leg_secs sleeper)
  printf '%s\n' "$o" | grep -q '^GATE FAIL  sleeper  (timed out after 3s)$' \
    || { echo "canary: a leg that outlived the per-leg timeout was not reported FAILED with a timeout tail"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^gates RED' \
    || { echo "canary: a timed-out leg did not make the run RED — a timeout must never read as a skip or a pass"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q '^GATE skip' \
    && { echo "canary: a timed-out leg was reported as a SKIP — the one thing a knob may never turn a leg into"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf 'loose\t0\t0\twidth=2,timeout=0\n' > "$P/fx/tbl-loose.txt"
  runp GATE_PROFILES=fx/tbl-loose.txt >/dev/null 2>&1
  t_ctl=$(leg_secs sleeper)
  { [ -n "$t_timed" ] && [ -n "$t_ctl" ]; } \
    || { echo "canary: the ledger carried no 'sleeper' row for one of the two runs, so the elapsed assertion could not look — an arm that could not measure has not measured (timed '${t_timed}', control '${t_ctl}')"; fail=1; }
  { [ -n "$t_timed" ] && [ -n "$t_ctl" ] && [ "$(( t_ctl - t_timed ))" -ge 10 ]; } \
    || { echo "canary: the per-leg timeout bounded the VERDICT and not the CLOCK — the sleeper leg itself took ${t_timed}s under a 3s bound against ${t_ctl}s untimed over the same 20s fixture. A knob that reports 124 while the worker blocks for the whole hang leaves the bar wedged exactly as it was before the knob existed."; fail=1; }
  # THE KILL-AFTER, driven by a leg that ignores TERM. Nothing else reaches it, and the tail is
  # accepted either way: which signal wins is the host's business, that the leg is NAMED is ours.
  cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "stubborn", "argv": ["bash", "fx/stubborn.sh"]}
]
JSON
n=$((n+1))
  o=$(runp GATE_PROFILES=fx/tbl-tight.txt)
  printf '%s\n' "$o" | grep -qE '^GATE FAIL  stubborn  [(]timed out after 3s(, killed)?[)]$' \
    || { echo "canary: a leg that IGNORES SIGTERM was not reported with a timeout tail — the kill-after escalates to SIGKILL and that path exits 137, not 124, so it is the one case -k exists for"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  cat > "$P/tools/gate-legs.json" <<'JSON'
[
  {"name": "one", "argv": ["bash", "fx/a.sh"]},
  {"name": "sleeper", "argv": ["bash", "fx/sleeper.sh"]}
]
JSON
else
  echo "canary: SKIP arm 4h — no working \`timeout\` on this host, so no leg can be bounded and the runner takes its INERT branch instead; arm 4m grades that branch. The assertions are counted either way, so the executed total does not move with host capability."
fi
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

# 4l. THE DECLARED SOURCE OF THE WIDTH IS NAMED WHERE A READER LOOKS. The unit repaired the charter's
#     stale `min(8, nproc)` and armed it there — and left the same formula in the two files closest to
#     the change, both of which SHIP. That is the two-answers-to-one-question class relocated rather
#     than removed, so the arm is here, in the half that travels, and grades the CLASS: both halves,
#     so a DELETED sentence cannot satisfy the negative alone.
for f in "$KITREL/run-gates.sh" "$KITREL/README.md"; do
n=$((n+1))
n=$((n+1))
  [ -f "$f" ] || { echo "canary: $f is absent, so the width-source arm would pass by finding nothing"; fail=1; continue; }
  grep -qF 'min(8, nproc)' "$f" \
    && { echo "canary: $f still states the built-in width formula, which describes only the absent-table fallback now — the width is declared in gate-profiles.txt and read from there"; fail=1; }
  grep -qF 'gate-profiles.txt' "$f" \
    || { echo "canary: $f never names gate-profiles.txt, so a reader of the kit is told where the width comes from by a file that no longer decides it"; fail=1; }
done

# 4m. THE INERT BRANCH. The runner supports a host with no working `timeout` by announcing the knob
#     dead and taking the width alone. Nothing drove that branch, so the announcement could have been
#     wrong or absent and every arm would still be green — and arms 4g/4h would have blamed the
#     runner's own logic for the missing binary. Driven with the PATH shim arm 4k already uses.
printf '#!/usr/bin/env bash\nexit 127\n' > "$P/shim/timeout"
chmod +x "$P/shim/timeout"
n=$((n+1))
n=$((n+1))
n=$((n+1))
o=$( cd "$P" && env GATE_FULL= GATE_BASE= PATH="$P/shim:$PATH" GATE_PROFILES=fx/tbl-timeout.txt bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s\n' "$o" | grep -q 'INERT' \
  || { echo "canary: with no working timeout the runner did not announce the knob INERT — a knob the operator set and the host cannot honour is worse than no knob"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
case "$(profline "$o")" in *'timeout off'*) ;; *) echo "canary: the INERT run still reported a live timeout on its visibility line: $(profline "$o")"; fail=1 ;; esac
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
  || { echo "canary: an unusable timeout changed the VERDICT — a missing host binary must cost the knob, never a leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
rm -f "$P/shim/timeout"

# 4n. A DROPPED GATE_PROFILE ANNOUNCES ITSELF. The fallback branch cannot honour a row name, and used
#     to drop it in silence — while the SAME typo against a present table exits 2 listing the rows
#     that exist. One state fatal, the other invisible, for one operator error. Warned rather than
#     refused, because refusing would block the documented table-deletion rollback for anyone carrying
#     GATE_PROFILE in their environment.
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILE=whatever GATE_PROFILES=definitely/absent/gate-profiles.txt)
printf '%s\n' "$o" | grep -q '^gates GREEN — 2/2 legs passed$' \
  || { echo "canary: a dropped GATE_PROFILE stopped the fallback from running every leg"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
case "$(profline "$o")" in
  *'GATE_PROFILE ignored'*) ;;
  *) echo "canary: GATE_PROFILE was dropped without saying so on the durable visibility line: $(profline "$o")"; fail=1 ;;
esac

# 4o. THE DECLARED HALF OF EVERY COMPARISON IS LENGTH-BOUNDED TOO. `num_ok` bounds the DETECTED
#     readings and AC12 arms that; the row validator was digits-only, so a twenty-digit threshold
#     ERRORED instead of comparing and dropped the run to the catch-all with no refusal, and a
#     twenty-digit `timeout=` silently became `off` while disabling the very warning that would have
#     said so. Both fixtures are load-bearing: against the shipped table neither case is reachable.
printf 'huge\t99999999999999999999\t0\twidth=2,timeout=0\n' > "$P/fx/tbl-longthr.txt"
printf 'huge\t0\t0\twidth=2,timeout=99999999999999999999\n'  > "$P/fx/tbl-longknob.txt"
for f in tbl-longthr tbl-longknob; do
n=$((n+1))
n=$((n+1))
  o=$(runp GATE_PROFILES=fx/$f.txt); rc=$?
  [ "$rc" = 2 ] || { echo "canary: an over-long declared value in fx/$f.txt exited $rc, not 2 — a value the runner cannot compare must refuse, not be silently dropped"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
  printf '%s\n' "$o" | grep -q "fx/$f.txt:1:" \
    || { echo "canary: the over-long-value refusal for fx/$f.txt did not name the file AND the line: $o"; fail=1; }
done

# 4p. AN INDENTED COMMENT IS A COMMENT. The runner skipped `#` at column 0 only, while this file's own
#     comment filter strips leading blanks — so the two readers of one file disagreed about which
#     lines are even rows, and an indented note (which the shipped table's header explicitly invites)
#     killed the whole bar with a message about field counts.
printf '  # an indented note\n   \nfine\t0\t0\twidth=2,timeout=0\n' > "$P/fx/tbl-indent.txt"
n=$((n+1))
n=$((n+1))
o=$(runp GATE_PROFILES=fx/tbl-indent.txt); rc=$?
[ "$rc" = 0 ] || { echo "canary: an indented comment or a whitespace-only line was refused as a malformed row (exit $rc)"; printf '%s\n' "$o" | sed 's/^/    /'; fail=1; }
[ "$(profname "$o")" = fine ] \
  || { echo "canary: the row after an indented comment was not selected; got '$(profname "$o")'"; fail=1; }

# 4q. THE RAM GUARD SEES THE LIMIT THAT IS ENFORCED, not the host's. Every detection source reports
#     HOST physical memory, which inside a memory-capped container is not the number deciding whether
#     eight scratch repos fit — a 4 GB runner on a 512 GB host read 512 GB and selected the widest
#     row, the exact thrash this table exists to stop, in the environment the bar is scheduled to move
#     to. MIN rather than replace, so a bogus limit can only make the bar slower.
mkdir -p "$P/cg"
n=$((n+1))
n=$((n+1))
n=$((n+1))
printf '2147483648\n' > "$P/cg/memory.max"        # 2 GB, well under any real host reading
o=$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" bash tools/run-gates/run-gates.sh 2>&1 )
case "$(profline "$o")" in
  *'via '*'cgroup'*) ;;
  *) echo "canary: an enforced cgroup memory limit was not read, so the RAM guard cannot fire in a container: $(profline "$o")"; fail=1 ;;
esac
[ "$(profname "$o")" != "$(profname "$(runp)")" ] || echo "canary: SKIP the cgroup-selection half — this host already selects the same row at 2 GB, so the fixture cannot show the limit changing the choice"
printf 'max\n' > "$P/cg/memory.max"               # v2's no-limit spelling is UNKNOWN, never a reading
o=$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" bash tools/run-gates/run-gates.sh 2>&1 )
case "$(profline "$o")" in
  *cgroup*) echo "canary: the literal 'max' was taken as a memory READING rather than as no limit: $(profline "$o")"; fail=1 ;;
esac
#     BOTH SOURCES, in the loop shape the function walks. Every fixture first wrote only the v2
#     filename — including the one labelled "v1's sentinel" — so the v1 element was reached solely by
#     its readability guard failing, and a typo in that path would have been invisible. That is
#     fixture-passes-by-finding-nothing one arm over from where this fold closed it, and v1 is the
#     branch that matters on the older images this source was added for.
rm -f "$P/cg/memory.max"; mkdir -p "$P/cg/memory"
printf '2147483648\n' > "$P/cg/memory/memory.limit_in_bytes"     # v1, and the ONLY source present
n=$((n+1))
o=$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" bash tools/run-gates/run-gates.sh 2>&1 )
case "$(profline "$o")" in
  *'via '*'cgroup'*) ;;
  *) echo "canary: the cgroup v1 limit file was never opened, so the older images this source exists for are ungraded: $(profline "$o")"; fail=1 ;;
esac
n=$((n+1))
printf '9223372036854771712\n' > "$P/cg/memory/memory.limit_in_bytes"   # v1's sentinel, in v1's file
o=$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" bash tools/run-gates/run-gates.sh 2>&1 )
case "$(profline "$o")" in
  *cgroup*) echo "canary: the cgroup v1 no-limit sentinel was taken as a memory reading: $(profline "$o")"; fail=1 ;;
esac

#     AND THE SEAM OUTRANKS THE CAP. An operator who sets GATE_RAM_MB has bypassed detection by
#     definition, so capping it with ambient container state hands the box back the deciding vote in
#     the very arms written so the box could not decide — and disables the only escape hatch when the
#     cgroup reading is wrong. Measured: the threshold arms above are byte-for-byte an invocation that
#     selected a different row once a 2 GB limit existed, so the SHIPPED canary red inside any
#     memory-capped container. The deliberate UNKNOWN of GATE_RAM_MB=0 must survive it too.
rm -rf "$P/cg"; mkdir -p "$P/cg"
printf '2147483648\n' > "$P/cg/memory.max"
n=$((n+1))
n=$((n+1))
pl=$(profline "$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" GATE_CORES=16 GATE_RAM_MB=32000 bash tools/run-gates/run-gates.sh 2>&1 )")
case "$pl" in
  *cgroup*) echo "canary: an explicit GATE_RAM_MB was capped by the cgroup source — the seam bypasses detection by definition, and the shipped threshold arms would red inside any memory-capped container: $pl"; fail=1 ;;
esac
pl=$(profline "$( cd "$P" && env GATE_FULL= GATE_BASE= GATE_CGROUP_ROOT="$P/cg" GATE_CORES=0 GATE_RAM_MB=0 bash tools/run-gates/run-gates.sh 2>&1 )")
case "$pl" in
  *'detection failed'*) ;;
  *) echo "canary: GATE_RAM_MB=0 is a deliberate UNKNOWN and the cgroup source replaced it with a reading: $pl"; fail=1 ;;
esac
rm -rf "$P/cg"

# 5. THE BASE IS THE BRANCH POINT. A branch is graded on what IT changed, not on everything that
#    landed while it was open, so the baseline is the merge-base with the default branch — used
#    ONLY where it is a proper ancestor of HEAD, with the origin tip standing otherwise.
#
#    THE DIVERGED CASE IS THE ONLY ONE THAT SEPARATES THE TWO SEMANTICS, which is why it is built
#    here rather than asserted against the fixture above: that one points its remote ref at HEAD,
#    so merge-base == HEAD and both rules give the same answer. An arm that only used it would
#    grade a distinction it cannot see.
n=$((n+1))
BB=$(mktemp -d)
mkdir -p "$BB/tools/run-gates" "$BB/tools/lib" "$BB/fx" "$BB/ga" "$BB/gb"
cp "$KITDIR/run-gates.sh" "$KITDIR/gate-profiles.txt" "$BB/tools/run-gates/" 2>/dev/null
cp "$KITDIR/gate-fingerprint.sh" "$BB/tools/run-gates/" 2>/dev/null || true
cp "$ROOT/tools/lib/resolve-python.sh" "$BB/tools/lib/" 2>/dev/null || true
printf '#!/usr/bin/env bash\nexit 0\n' > "$BB/fx/a.sh"
echo x > "$BB/ga/f"; echo y > "$BB/gb/f"
printf '%s\n' '[' \
  '  {"name": "ga leg", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "gb leg", "argv": ["bash", "fx/a.sh"], "guard": ["gb/"]}' \
  ']' > "$BB/tools/gate-legs.json"
( cd "$BB" && git init -q -b main . && git config user.email c@t && git config user.name c \
   && git add -A && git commit -qm seed \
   && git update-ref refs/remotes/origin/main HEAD \
   && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
# diverge: the branch touches ga/, then the default branch advances on gb/ only
( cd "$BB" && git checkout -q -b feature && echo edited > ga/f && git add -A && git commit -qm branch \
   && git checkout -q main && echo advanced > gb/f && git add -A && git commit -qm advance \
   && git update-ref refs/remotes/origin/main HEAD && git checkout -q feature ) >/dev/null 2>&1
bout=$( cd "$BB" && env GATE_FULL= GATE_BASE= bash tools/run-gates/run-gates.sh 2>&1 )
if printf '%s' "$bout" | grep -q '^GATE skip  gb leg'; then
  : # the branch never touched gb/, and against the BRANCH POINT it is unchanged
else
  echo "canary: on a diverged branch, a leg whose guard the BRANCH did not touch did not skip — the baseline is still the remote TIP, so every branch is graded on other people's commits"
  printf '%s\n' "$bout" | grep '^GATE ' | sed 's/^/    /'; fail=1
fi
n=$((n+1))
# THE CONTROL, and without it the arm above passes on a runner that skips everything: the leg the
# branch DID touch must still run.
printf '%s' "$bout" | grep -q '^GATE ok    ga leg' \
  || { echo "canary: the leg whose guard the branch DID touch was skipped too — the baseline is scoping away real changes"; fail=1; }
n=$((n+1))
# An unresolvable baseline runs EVERYTHING. Fail-safe, and it is the property that makes every
# scoping rule above safe to get wrong.
( cd "$BB" && git update-ref -d refs/remotes/origin/main; git symbolic-ref -d refs/remotes/origin/HEAD ) >/dev/null 2>&1
bout2=$( cd "$BB" && env GATE_FULL= GATE_BASE= bash tools/run-gates/run-gates.sh 2>&1 )
printf '%s' "$bout2" | grep -q '^GATE skip' \
  && { echo "canary: a leg skipped with NO resolvable baseline — the scoping rule does not fail safe"; fail=1; } || :
rm -rf "$BB"
# 6. CHUNKED REPORTING. Fixture-driven and true in any tree, so it ships; the assertion about
#    which chunk names THIS repo declares is the gov harness's, next door.
n=$((n+1))
CK=$(mktemp -d)
mkdir -p "$CK/tools/run-gates" "$CK/tools/lib" "$CK/fx" "$CK/g"
cp "$KITDIR/run-gates.sh" "$KITDIR/gate-profiles.txt" "$CK/tools/run-gates/" 2>/dev/null
cp "$KITDIR/gate-fingerprint.sh" "$CK/tools/run-gates/" 2>/dev/null || true
cp "$ROOT/tools/lib/resolve-python.sh" "$CK/tools/lib/" 2>/dev/null || true
printf '#!/usr/bin/env bash\nexit 0\n' > "$CK/fx/a.sh"
echo g > "$CK/g/f"
# INTERLEAVED ON PURPOSE. The manifest is not grouped, so the reader's walk is a real permutation
# rather than an identity — an arm over an already-grouped fixture would pass on a runner that
# never grouped anything.
printf '%s\n' '[' \
  '  {"name": "alpha", "argv": ["bash", "fx/a.sh"], "chunk": "one"},' \
  '  {"name": "beta",  "argv": ["bash", "fx/a.sh"], "chunk": "two"},' \
  '  {"name": "gamma", "argv": ["bash", "fx/a.sh"], "chunk": "one"},' \
  '  {"name": "delta", "argv": ["bash", "fx/a.sh"]}' \
  ']' > "$CK/tools/gate-legs.json"
( cd "$CK" && git init -q -b main . && git config user.email c@t && git config user.name c \
   && git add -A && git commit -qm seed ) >/dev/null 2>&1
cout=$( cd "$CK" && env GATE_FULL=1 bash tools/run-gates/run-gates.sh 2>&1 )
# SNAPSHOT THE SUMMARY NOW. Every run overwrites it, and the all-skipped fixture below runs a
# DIFFERENT manifest with different chunk names — so an assertion deferred to the end looks for
# this run's chunks in that run's file and reports a missing roll-up that is really a missing run.
csum=$(cat "$CK/.git/gate-last-summary.txt" 2>/dev/null)
order=$(printf '%s' "$cout" | grep -E '^GATE ok    ' | sed 's/^GATE ok    //' | tr '\n' ' ')
case "$order" in
  "alpha gamma beta delta "*) ;;
  *) echo "canary: chunked reporting did not group an interleaved manifest — legs reported as: $order"; fail=1 ;;
esac
n=$((n+1))
printf '%s' "$cout" | grep -qE '^---- chunk one: green  \(2 ran, 0 failed, 0 skipped, 0 reused, 0 held\)$' \
  || { echo "canary: the per-chunk verdict line is missing or off-grammar"; printf '%s\n' "$cout" | grep 'chunk' | sed 's/^/    /'; fail=1; }
n=$((n+1))
# A LEG WITH NO KEY falls into `default` rather than being dropped — a leg that vanishes from the
# report because nobody classified it is the quietest possible green-by-absence.
printf '%s' "$cout" | grep -q '^---- chunk default: green' \
  || { echo "canary: a leg carrying no chunk key did not report under a default chunk"; fail=1; }
n=$((n+1))
# AN ALL-SKIPPED CHUNK REPORTS AS SKIPPED, NEVER GREEN. One altitude above the same rule for a
# single leg, and the louder of the two: a green chunk line is what a reader scans for.
printf '%s\n' '[' \
  '  {"name": "guarded", "argv": ["bash", "fx/a.sh"], "guard": ["g/"], "chunk": "gone"},' \
  '  {"name": "free", "argv": ["bash", "fx/a.sh"], "chunk": "here"}' \
  ']' > "$CK/tools/gate-legs.json"
( cd "$CK" && git add -A && git commit -qm two \
   && git update-ref refs/remotes/origin/main HEAD \
   && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
sout=$( cd "$CK" && env GATE_FULL= GATE_BASE= bash tools/run-gates/run-gates.sh 2>&1 )
if printf '%s' "$sout" | grep -q '^GATE skip  guarded'; then
  printf '%s' "$sout" | grep -qE '^---- chunk gone: skipped' \
    || { echo "canary: a chunk whose every leg was skipped did not report as skipped"; printf '%s\n' "$sout" | grep 'chunk' | sed 's/^/    /'; fail=1; }
else
  echo "canary: the all-skipped chunk fixture did not skip anything, so that arm proves nothing"; fail=1
fi
n=$((n+1))
# ITS CONTROL: the chunk that did run must still be green, or a runner that called every chunk
# skipped would pass the arm above.
printf '%s' "$sout" | grep -qE '^---- chunk here: green' \
  || { echo "canary: the chunk that DID run was not reported green — the skipped verdict above is not discriminating"; fail=1; }
n=$((n+1))
# THE ROLL-UP IS DURABLE AND NOT ON STDOUT: per-chunk wall time belongs in a file, because a
# duration on a terminal line invites comparison between runs that are not comparable.
printf '%s' "$cout" | awk -F'\t' '$1=="chunk"{found=1} END{exit !found}' \
  && { echo "canary: the chunk roll-up leaked onto stdout"; fail=1; } || :
printf '%s\n' "$csum" | awk -F'\t' '$1=="chunk" && $2=="one"{found=1} END{exit !found}' \
  || { echo "canary: the durable summary carries no chunk roll-up row"; fail=1; }
rm -rf "$CK"
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "canary: executed $n assertions, below the pinned floor $FLOOR_ASSERTIONS"; fail=1; }
[ "$fail" = 0 ] && echo "PASS ($n assertions)"
[ "$fail" = 0 ] && exit 0 || exit 1

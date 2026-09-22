#!/usr/bin/env bash
# Self-test for check-verifier-fanout.sh. The PREDICATE's own arms live in tools/hooks/agent-cap.test.sh
# — this file tests the things the gate adds on top of it: the population, the self-exclusion, the
# empty-population failure, and that the delegation actually reaches the hook rather than reporting
# clean because nothing ran.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
GATE="$HERE/check-verifier-fanout.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
fails=0
arm() { # label · expected-substring · command…
  local label=$1 want=$2; shift 2
  local out; out=$("$@" 2>&1)
  case "$out" in
    *"$want"*) printf 'arm ok    %s\n' "$label" ;;
    *) fails=$((fails+1)); printf 'arm FAIL  %s — expected to see: %s\n' "$label" "$want"
       printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# The RED fixture is not synthetic. It is the verify stage of the bespoke closing-review workflow
# written in this repo on 2026-08-09 — reconstructed from the session transcript, because the script
# was an inline `script` string on a Workflow tool call and was never a file. That is also the point
# of the finding that moved this rule into the hook: a gate over repo files could not have seen it.
cat >"$TMP/the-incident.js" <<'EOF'
export const meta = { name: 'closing-review', description: 'the shape that motivated the rule' }
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(`Adversarially verify: ${f.title}`, { label: `verify:${f.id}` })
    .then((v) => ({ ...f, verdict: v }))))
EOF
cat >"$TMP/bounded.js" <<'EOF'
export const meta = { name: 'ok-harness', description: 'the bounded shape' }
const MAX_VERIFIERS = 5
const batches = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(batches.map((g) => () => agent(g)), 5)
EOF
# Not a workflow: no `export const meta`. It carries the banned shape, so if the marker filter is
# dropped this file starts redding the bar and the arm below says so.
cat >"$TMP/not-a-workflow.js" <<'EOF'
const helper = all.map((f) => () => agent(f.claim))
EOF

arm 'the incident script is caught' 'verifier-fanout: FAILED' bash "$GATE" "$TMP/the-incident.js"
arm '...and the report names the rule' 'verify-stage agents at 5 TOTAL' bash "$GATE" "$TMP/the-incident.js"
arm 'a bounded harness is clean' 'obey the ≤5-verifier rule' bash "$GATE" "$TMP/bounded.js"
# Both states over the SAME two files: a gate that only ever reds is not discriminating, it is broken.
arm 'a mixed set reports only the offender' 'the-incident.js' bash "$GATE" "$TMP/bounded.js" "$TMP/the-incident.js"

# The DISCOVERY path — the shipped tree. Every arm above hands the gate explicit files, and the
# explicit path never touches git, so none of them exercises the population.
arm 'the shipped tree is clean' 'verifier-fanout: clean' bash "$GATE"
# ...and it judged more than zero of them. "clean over an empty set" and "clean" print differently,
# but only because something asserts the count.
out=$(bash "$GATE" 2>&1)
n=$(printf '%s' "$out" | sed -n 's/.*clean — \([0-9]*\) workflow script.*/\1/p')
if [ -n "$n" ] && [ "$n" -ge 3 ]; then printf 'arm ok    the population is the real harness set (%s scripts)\n' "$n"
else fails=$((fails+1)); printf 'arm FAIL  the population collapsed (got %s scripts)\n' "${n:-none}"; fi

# An empty population is a FAILURE, not a pass — the class this repo keeps a catalogue record about.
E="$TMP/empty"; mkdir -p "$E"
( cd "$E" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'x\n' > README.md && git add -A && git commit -qm empty --no-verify ) >/dev/null 2>&1
mkdir -p "$E/tools/hooks" && cp "$(cd "$HERE/../hooks" && pwd)/agent-cap.js" "$E/tools/hooks/agent-cap.js"
# TOOL-dRetiredFork-10: the gate now resolves its predicate RELATIVE TO ITSELF, so the fixture
# has to put it where an install actually puts it. It previously sat at the bare repository
# root and worked only because the gate hard-coded `$ROOT/tools/hooks/` -- the literal this
# unit removes. No kit installs a workflow gate at a repo root, so the old fixture described a
# layout that never existed, and it would have kept passing while real adopters stayed broken.
mkdir -p "$E/tools/workflows" && cp "$GATE" "$E/tools/workflows/gate.sh"
arm 'an empty population is not a pass' 'the population is empty, which is not a pass' \
  bash -c 'cd "$1" && bash ./tools/workflows/gate.sh' _ "$E"

# The marker filter: a `.js` that is not a workflow is not judged, even carrying the banned shape.
arm 'a non-workflow .js is not judged by the discovery path' 'verifier-fanout: clean' \
  bash -c 'cp "$2" "$1/tools/x-helper.js" && cp "$3" "$1/tools/wf.js" && cd "$1" && bash ./tools/workflows/gate.sh' \
  _ "$E" "$TMP/not-a-workflow.js" "$TMP/bounded.js"

# The gate has no predicate of its own: break the delegation and it must FAIL, not pass quietly.
D="$TMP/nohook"; mkdir -p "$D"
( cd "$D" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'x\n' > README.md && git add -A && git commit -qm base --no-verify ) >/dev/null 2>&1
mkdir -p "$D/tools/workflows" && cp "$GATE" "$D/tools/workflows/gate.sh"
arm 'a missing predicate is a named failure' 'has no predicate to delegate to' \
  bash -c 'cd "$1" && bash ./tools/workflows/gate.sh' _ "$D"


# ---- TOOL-dRetiredFork-10: the gate resolves at a FOREIGN install prefix -------------------------
# These three arms are the reason the unit exists. Before it, the population filter and the hook
# path both spelled `tools/`, so an adopter who installs at `scripts/` got an EMPTY population and
# a missing predicate — and every one of them carried a hand-maintained carve-out to fix it.
#
# The fixtures are built here rather than borrowed, because the two real adopters are foreign trees
# this suite must not depend on: a fixture keyed to inCMS's current bytes grades a moving target.
mkfix() { # $1 = fixture root · $2 = where the hook goes, relative to the root ("" = no hook at all)
  local fix=$1 hookrel=$2
  mkdir -p "$fix/scripts/workflows"
  cp "$HERE/check-verifier-fanout.sh" "$fix/scripts/workflows/"
  # a bounded harness, so the population is non-empty and the verdict is legitimately clean
  cat >"$fix/scripts/workflows/harness.js" <<'JS'
export const meta = { name: 'fixture', description: 'a bounded harness', phases: [] }
const LENSES = ['security', 'correctness', 'integration']
const out = await boundedParallel(LENSES.map((l) => () => agent(`check ${l}`)), 5)
JS
  if [ -n "$hookrel" ]; then
    mkdir -p "$fix/$(dirname "$hookrel")"
    cp "$HERE/../hooks/agent-cap.js" "$fix/$hookrel"
  fi
  ( cd "$fix" && git init -q . && git config user.email t@t && git config user.name t \
      && git add -A && git commit -q -m fixture --no-verify ) >/dev/null 2>&1
}

# AC2 — the NicoCares shape: kit at `scripts/`, hook a directory up from the harnesses. Rung 2.
FIX_A=$(mktemp -d); mkfix "$FIX_A" "scripts/hooks/agent-cap.js"
out=$(cd "$FIX_A" && bash scripts/workflows/check-verifier-fanout.sh 2>&1); rc=$?
if [ "$rc" = 0 ]; then printf 'arm ok    AC2: resolves at a scripts/ install and exits 0\n'
else fails=$((fails+1)); printf 'arm FAIL  AC2: a scripts/ install did not pass (rc=%s)\n%s\n' "$rc" "$out"; fi
case "$out" in *"1 workflow script"*) printf 'arm ok    AC2: and the population is non-empty there\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC2: population wrong at a foreign prefix: %s\n' "$out" ;; esac

# AC3 — the inCMS shape: NO scripts/hooks/ at all, the only copy at .claude/hooks/. Rung 3, which a
# two-rung chain strands. This arm is the one that would have caught that.
FIX_B=$(mktemp -d); mkfix "$FIX_B" ".claude/hooks/agent-cap.js"
out=$(cd "$FIX_B" && bash scripts/workflows/check-verifier-fanout.sh 2>&1); rc=$?
if [ "$rc" = 0 ]; then printf 'arm ok    AC3: resolves the .claude/hooks/ copy when no sibling exists\n'
else fails=$((fails+1)); printf 'arm FAIL  AC3: the third rung did not resolve (rc=%s)\n%s\n' "$rc" "$out"; fi

# AC4 — no hook anywhere. The gate must REFUSE and NAME what it probed. A gate that cannot find its
# predicate and prints a clean line is the failure this whole build keeps finding.
FIX_C=$(mktemp -d); mkfix "$FIX_C" ""
out=$(cd "$FIX_C" && bash scripts/workflows/check-verifier-fanout.sh 2>&1); rc=$?
if [ "$rc" != 0 ]; then printf 'arm ok    AC4: an unresolvable predicate REFUSES (rc=%s)\n' "$rc"
else fails=$((fails+1)); printf 'arm FAIL  AC4: no hook anywhere and the gate still passed\n%s\n' "$out"; fi
case "$out" in *"hooks/"*".claude/hooks/"*) printf 'arm ok    AC4: and the refusal names the probes it tried\n' ;;
  *) fails=$((fails+1)); printf 'arm FAIL  AC4: the refusal does not name its probes: %s\n' "$out" ;; esac

# ANTI-VACUITY. Every arm above would also pass if the fixtures were empty and the gate refused for
# an unrelated reason, so pin the thing that actually distinguishes them: fixture A and fixture C
# differ ONLY by the presence of the hook, and their verdicts must differ.
outA=$(cd "$FIX_A" && bash scripts/workflows/check-verifier-fanout.sh 2>&1)
outC=$(cd "$FIX_C" && bash scripts/workflows/check-verifier-fanout.sh 2>&1)
if [ "$outA" != "$outC" ]; then printf 'arm ok    the hook is what the fixtures are testing, not the tree shape\n'
else fails=$((fails+1)); printf 'arm FAIL  identical verdicts with and without the predicate\n'; fi

rm -rf "$FIX_A" "$FIX_B" "$FIX_C"

if [ "$fails" = 0 ]; then echo "PASS — check-verifier-fanout: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1

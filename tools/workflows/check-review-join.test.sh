#!/usr/bin/env bash
# check-review-join.test.sh — self-test for BOTH U6 gates: the ref-keyed-join ban and the workflow
# syntax parser. Exit 0 = every arm held · 1 = an arm failed.
#
#   bash tools/workflows/check-review-join.test.sh
#
# DISCIPLINES THIS FILE OBEYS (ported with the build, TOOL-aFoldedQuarry-7):
#  * Every arm asserts the SPECIFIC MESSAGE the branch emits, never the process exit code alone. A
#    probe that only reads `$?` reports success while exercising nothing — six of them did upstream.
#  * Fixtures are BATCHED into one scratch directory and one invocation per arm, not a fresh scratch
#    repo per assertion.
#  * `PASS` prints after the LAST arm. Upstream printed it ~150 lines early and landed a red bar
#    because the head of the output said success.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE="tools/workflows/check-review-join.sh"
SYNTAX="tools/workflows/check-workflow-syntax.js"
fails=0
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

arm() { # label · expected-substring · command…
  local label=$1 want=$2; shift 2
  local out; out=$("$@" 2>&1)
  case "$out" in
    *"$want"*) printf 'arm ok    %s\n' "$label" ;;
    *) fails=$((fails+1)); printf 'arm FAIL  %s — expected to see: %s\n' "$label" "$want"
       printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# ---- fixtures (batched: written once, each arm points at the one it needs) ----------------------
cat >"$TMP/bracket.js" <<'EOF'
const verdicts = {}
for (const v of all) verdicts[v.ref] = v
EOF
cat >"$TMP/mapset.js" <<'EOF'
const u = "https://example.com/a//b"
const m = new Map()
m.set(f.ref, v)
EOF
cat >"$TMP/identifier.js" <<'EOF'
const verdictByRef = Object.create(null)
EOF
# The GREEN comment fixture is the whole point of stripping comments: tier2-review.js itself
# DOCUMENTS the retired join, and a whole-file-text absence assertion would red on that prose.
cat >"$TMP/comment-only.js" <<'EOF'
// The retired join was `verdicts[v.ref] = v`, which collided on a shared file:line.
/* verdictByRef was the identifier; m.set(f.ref, v) was the Map spelling of the same defect. */
const verdictById = new Map()
verdictById.set(f.id, v)
EOF
# A `//` inside a STRING must not end the code line — otherwise the ban after it goes unseen.
cat >"$TMP/url-then-ban.js" <<'EOF'
const doc = "see https://example.com/x"; const m = {}; m[f.ref] = v
EOF
cat >"$TMP/broken-syntax.js" <<'EOF'
export const meta = { name: 'broken' }
const x = (1 + 2
EOF
# The runtime dialect: module export + top-level await + top-level return, all three at once.
cat >"$TMP/dialect-ok.js" <<'EOF'
export const meta = { name: 'ok', description: 'd', phases: [] }
const r = await agent('x', { schema: {} })
if (!r) return { note: 'dead' }
log('fine')
return { ok: true }
EOF

# ---- RED arms: each ban fires with its OWN message ----------------------------------------------
arm 'ban: object literal keyed by .ref' 'object/Map literal keyed by a .ref string' \
  bash "$GATE" "$TMP/bracket.js"
arm 'ban: Map keyed by .ref'            'Map keyed by a .ref string' \
  bash "$GATE" "$TMP/mapset.js"
arm 'ban: retired identifier'           'the retired verdictByRef identifier' \
  bash "$GATE" "$TMP/identifier.js"
arm 'ban: url in a string does not hide a later ban' 'object/Map literal keyed by a .ref string' \
  bash "$GATE" "$TMP/url-then-ban.js"
arm 'ban: the failure names the remedy' 'Key the join on the integer id' \
  bash "$GATE" "$TMP/bracket.js"

# ---- GREEN arms ---------------------------------------------------------------------------------
arm 'comments describing the retired join are prose, not code' 'clean — no ref-keyed verdict join' \
  bash "$GATE" "$TMP/comment-only.js"
arm 'the shipped tree is clean' 'clean — no ref-keyed verdict join' \
  bash "$GATE"

# ---- the gate cannot pass by looking at nothing --------------------------------------------------
arm 'an empty scan is not a pass' 'nothing was scanned, which is not a pass' \
  bash "$GATE" "$TMP/does-not-exist.js"

# ---- syntax gate --------------------------------------------------------------------------------
arm 'syntax: a real parse failure is reported' 'SyntaxError' \
  node "$SYNTAX" "$TMP/broken-syntax.js"
arm 'syntax: export + top-level await + top-level return all parse' 'parsed clean' \
  node "$SYNTAX" "$TMP/dialect-ok.js"
arm 'syntax: the shipped harness parses' 'workflow script(s) parsed clean' \
  node "$SYNTAX"

# ---- the harness itself carries the indexed join --------------------------------------------------
# Positive assertions on the SHIPPED file: a source-level absence ban proves the old join is gone,
# and these prove the new one is present. Only both together mean "index-keyed".
H='tools/workflows/tier2-review.js'
arm 'harness: orchestrator assigns the id' 'id: i + 1' grep -F 'id: i + 1' "$H"
arm 'harness: the verdict map is keyed on the integer' 'verdictById = new Map()' grep -F 'verdictById = new Map()' "$H"
arm 'harness: the schema demands an integer id' "id: { type: 'integer' }" grep -F "id: { type: 'integer' }" "$H"
arm 'harness: a conflicting repeat demotes to unverified' 'conflicts.add(v.id)' grep -F 'conflicts.add(v.id)' "$H"
# The pin is on the marker's SHAPE, not its value: a literal pin reds on every version bump, which
# makes the bump edit a test that is not about versions. The value lives in the file itself.
arm 'harness: the version marker is well-formed' "version: '" grep -E "version: '[0-9]+\.[0-9]+'" "$H"
# The bounded verifier count, asserted POSITIVELY. The absence ban proves the linear form is gone;
# only this proves the bounded one is present. Both, or "clean" means "empty".
arm 'harness: the verifier count is bounded' 'MAX_VERIFIERS' grep -F 'Math.ceil(allFindings.length / MAX_VERIFIERS)' "$H"
arm 'harness: the bounded split carries the marker' 'gov:fixed-verifiers' grep -F 'gov:fixed-verifiers' "$H"

# ---- THE DISCOVERY PATH ---------------------------------------------------------------------------
# Both gates take explicit paths and never touch git on that path, so every arm above exercises the
# scanner and none of them exercises the POPULATION. These four run each gate with NO arguments in a
# throwaway repo where the offending file is UNTRACKED — which is exactly the state the widening is
# about, and the state both gates were blind to.
D="$TMP/discover"
mkdir -p "$D/tools/workflows"
( cd "$D" && git init -q . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false && git config commit.gpgsign false
  # Two seeds, because the two gates have DIFFERENT populations: review-join scans every .js under
  # tools/, while the syntax gate scans only files carrying the `export const meta` marker. With one
  # plain seed the ignored-file arm below would empty the syntax gate's population and red for the
  # opposite reason to the one it is testing — measured, not guessed.
  printf 'const x = 1\n' > tools/workflows/seed.js
  printf "export const meta = { name: 'seed', description: 'a tracked workflow' }\nawait log('hi')\n" \
    > tools/workflows/seed-workflow.js
  git add -A && git commit -qm seed --no-verify )
cp "$GATE" "$D/gate.sh"; cp "$SYNTAX" "$D/syntax.js"

# never staged, never committed — visible to `git ls-files --others`, invisible to `git ls-files`
cat >"$D/tools/workflows/scratch-join.js" <<'EOF'
const verdicts = {}
for (const v of all) verdicts[v.ref] = v
EOF
arm 'discovery: an UNTRACKED banned join is caught' 'scratch-join.js' \
  bash -c 'cd "$1" && bash ./gate.sh' _ "$D"
cat >"$D/tools/workflows/scratch-workflow.js" <<'EOF'
export const meta = { name: 'x', description: 'y' }
const a = (
EOF
arm 'discovery: an UNTRACKED workflow script is parsed' 'SyntaxError' \
  bash -c 'cd "$1" && node ./syntax.js' _ "$D"

# ...and IGNORED stays ignored, which is the escape hatch the widening leans on. Same two files, one
# .gitignore line: both gates must go quiet, or "untracked" would mean "unignorable".
printf 'tools/workflows/scratch-*.js\n' > "$D/.gitignore"
arm 'discovery: a git-ignored file is not judged (review-join)' 'clean — no ref-keyed verdict join' \
  bash -c 'cd "$1" && bash ./gate.sh' _ "$D"
arm 'discovery: a git-ignored file is not judged (syntax)' 'parsed clean' \
  bash -c 'cd "$1" && node ./syntax.js' _ "$D"

# ...and the widened population still FAILS on an empty selection. A gate that greens over nothing is
# the class this repo keeps a catalogue record about, and widening a selector is exactly when that
# protection is easiest to drop.
E="$TMP/emptyrepo"; mkdir -p "$E"
( cd "$E" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'x\n' > README.md && git add -A && git commit -qm empty --no-verify )
cp "$GATE" "$E/gate.sh"
arm 'discovery: an empty population is still not a pass' 'the population is empty, which is not a pass' \
  bash -c 'cd "$1" && bash ./gate.sh' _ "$E"

# ---- verdict, LAST -------------------------------------------------------------------------------
if [ "$fails" = 0 ]; then echo "PASS — review-join + workflow-syntax gates: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1

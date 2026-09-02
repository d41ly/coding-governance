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

# ---- D7: a status this gate cannot interpret is a REFUSAL, never a verdict -----------------------
# Both halves of one root: the loop read "the pipeline exited non-zero" as "rule 5 fired".
# The false RED. agent-cap exits 2 on its own environment refusal BEFORE any rule runs, and that
# message has no line starting with two spaces and L, so the sed emptied it and the gate reported a
# ref-keyed verdict join with a blank body - sending an operator off to rewrite a join that is not
# there. Reproduced exactly this way against the shipped tree.
arm 'a predicate refusing its ENVIRONMENT is not a join report' 'is its own refusal and not a join'   env AGENT_CAP=7 bash "$GATE"

# The false GREEN, and the reason `set -o pipefail` is now set beside `set -u`: only the hook's
# status was read, so a builder that threw fed empty stdin to a JSON.parse whose catch exits 0 and
# the file was recorded clean. A stub predicate returning an unclassifiable status stands in for
# every such shape. The gate's own header preaches that a probe which cannot move must say so.
BS="$TMP/badstatus"; mkdir -p "$BS/tools/workflows" "$BS/tools/hooks"
( cd "$BS" && git init -q . && git config user.email t@t.test && git config user.name t
  printf "export const meta = { name: 'x' }
await log('hi')
" > tools/workflows/w.js
  printf 'process.exit(3)
' > tools/hooks/agent-cap.js
  git add -A && git commit -qm badstatus --no-verify )
cp "$GATE" "$BS/gate.sh"
arm 'a status the gate cannot classify is a refusal, not a pass' 'neither clean nor a rule hit'   bash -c 'cd "$1" && bash ./gate.sh' _ "$BS"

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
# TOOL-dTieredTribunal-14 S8 - the gate DELEGATES its predicate to the hook now, so a scratch repo
# without one meets the missing-predicate refusal instead of the verdict this arm asserts.
mkdir -p "$D/tools/hooks" && cp "$ROOT/tools/hooks/agent-cap.js" "$D/tools/hooks/agent-cap.js"

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
# S8 - same reason as the $D site. `$E` and not `$D`: the scratch variable is per SITE, and `E` is
# not bound until this block, so a `$D` spelling here would judge the wrong repo.
mkdir -p "$E/tools/hooks" && cp "$ROOT/tools/hooks/agent-cap.js" "$E/tools/hooks/agent-cap.js"
arm 'discovery: an empty population is still not a pass' 'the population is empty, which is not a pass' \
  bash -c 'cd "$1" && bash ./gate.sh' _ "$E"

# TOOL-dTieredTribunal-14 S8 - the missing-predicate refusal's own failing case, OBSERVED. A gate whose
# predicate is absent must SAY SO rather than pass, and a refusal nobody has watched fire is an
# assertion about nothing. Named `N` and not `D`, which is already bound to the discovery repo.
N="$TMP/nohook"; mkdir -p "$N/tools/workflows"
( cd "$N" && git init -q . && git config user.email t@t.test && git config user.name t
  printf "export const meta = { name: 'x' }\nawait log('hi')\n" > tools/workflows/w.js
  git add -A && git commit -qm nohook --no-verify )
cp "$GATE" "$N/gate.sh"
arm 'the predicate being absent is a refusal, not a pass' 'a gate whose predicate is absent must say so' \
  bash -c 'cd "$1" && bash ./gate.sh' _ "$N"

# ---- ARM 2: the agent wave that silently drops itself (TOOL-dRetiredFork-7) ----------------------
# Absorbed from inCMS, REDUCED: its arms keyed on that repo's own record ids are left behind, because
# an arm keyed on a foreign corpus reds on absence rather than on behaviour.
#
# Each fixture is a whole scratch TREE, not a lone file, because arm 2's population and its liveness
# refusal are both properties of the scan, and an explicit file list bypasses the refusal by design.
a2tree() {  # $1 = dir · $2 = harness body
  mkdir -p "$1/tools/workflows" "$1/tools/hooks"
  cp "$ROOT/tools/hooks/agent-cap.js" "$1/tools/hooks/agent-cap.js"
  printf '%s\n' "$2" > "$1/tools/workflows/h.js"
  ( cd "$1" && git init -q . && git config user.email t@t.test && git config user.name t \
    && git add -A && git commit -q -m f --no-verify ) >/dev/null 2>&1
}

A2=$(mktemp -d)
a2tree "$A2/nocount" 'const LENSES = ["a","b","c"]
const raw = await Promise.all(LENSES.map((l) => agent(l)))
const live = raw.filter(Boolean)
return { note: "clean: 0 findings", findings: live }'
arm 'arm 2: a falsy-dropped wave with NO arity counter is caught' 'never counts them' \
  bash -c 'cd "$1" && bash "$2"' _ "$A2/nocount" "$ROOT/$GATE"

# THE FALSY DROP IS A FAMILY, not a spelling. `.filter((r) => r)` walked past the first version of
# this arm upstream, so it is fixtured here rather than trusted.
a2tree "$A2/arrow" 'const LENSES = ["a","b","c"]
const raw = await Promise.all(LENSES.map((l) => agent(l)))
const live = raw.filter((r) => r)
return { note: "clean", findings: live }'
arm 'arm 2: the arrow spelling of the falsy drop is judged too' 'never counts them' \
  bash -c 'cd "$1" && bash "$2"' _ "$A2/arrow" "$ROOT/$GATE"

# THE COUNTER NAME IS CAPTURED, NEVER MATCHED. A correct harness whose counter is spelled
# `deadLenses` rather than `lensesDead` went RED upstream; that regression is fixtured.
a2tree "$A2/named" 'const LENSES = ["a","b","c"]
const raw = await Promise.all(LENSES.map((l) => agent(l)))
const live = raw.filter(Boolean)
const deadLenses = LENSES.length - live.length
if (deadLenses) log("dead " + deadLenses)
return { note: deadLenses ? "PARTIAL" : "clean", dead: deadLenses }'
arm 'arm 2: an oddly-named counter that IS read passes' 'clean — no ref-keyed' \
  bash -c 'cd "$1" && bash "$2"' _ "$A2/named" "$ROOT/$GATE"

# A COUNT COMPUTED AND NEVER CONSULTED is the same silent pass wearing a number.
a2tree "$A2/unread" 'const LENSES = ["a","b","c"]
const raw = await Promise.all(LENSES.map((l) => agent(l)))
const live = raw.filter(Boolean)
const lensesDead = LENSES.length - live.length
return { note: "clean: 0 findings", findings: live }'
arm 'arm 2: a counter computed and never read is caught' 'never reads the count' \
  bash -c 'cd "$1" && bash "$2"' _ "$A2/unread" "$ROOT/$GATE"

# S3's LIVENESS REFUSAL: a scanned population that judges NOTHING is not a pass.
a2tree "$A2/vacuous" 'const LENSES = ["a","b","c"]
const raw = await Promise.all(LENSES.map((l) => agent(l)))
log(raw.length)'
arm 'arm 2: agents dispatched but nothing judged REFUSES' 'judged NONE of them' \
  bash -c 'cd "$1" && bash "$2"' _ "$A2/vacuous" "$ROOT/$GATE"

rm -rf "$A2"

# ---- verdict, LAST -------------------------------------------------------------------------------
if [ "$fails" = 0 ]; then echo "PASS — review-join + workflow-syntax gates: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1

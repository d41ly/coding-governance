#!/usr/bin/env bash
# Runnable check for the portable agent-cap.js Workflow fan-out guard — BOTH rules:
#   rule 1  raw parallel()/pipeline() outside a `gov:bounded-fanout` line   (concurrency)
#   rule 2  a verify stage that spawns one agent per item                    (verifier arity)
# Run: bash hooks/agent-cap.test.sh   (exit 0 = all pass)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
HOOK="$HERE/agent-cap.js"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
# The one resolver, not the retired `command -v python3 || python` idiom this repo banned — which the
# ban could not see here, because it matches only `command -v`.
if [ -f "$HERE/../lib/resolve-python.sh" ]; then
  . "$HERE/../lib/resolve-python.sh"
  TESTPY=$(resolve_python) || { echo "agent-cap.test: no usable python"; exit 2; }
else
  TESTPY=python3   # gov:literal-python — last-resort fallback when ../lib/ is absent (adopter layout)
fi
check() { # name expected_exit json
  printf '%s' "$3" | node "$HOOK" >/dev/null 2>"$TMP/err"; local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
# js <name> <expected_exit> — the script body arrives on stdin, so a fixture can be written as real
# multi-line JavaScript instead of a \n-spliced one-liner. Every rule-2 fixture below is a SHAPE, and
# a shape squeezed onto one line stops being the shape that was written last time.
js() { # name expected_exit  (script on stdin)
  local name=$1 want=$2
  local payload
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  # An EMPTY payload makes every ALLOW arm pass for the wrong reason — the hook exits 0 on
  # unparseable input by design. A fixture that produced nothing is a failure, not a silent green.
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  check "$name" "$want" "$payload"
}

# ---- rule 1: concurrency ------------------------------------------------------------------------
check "raw parallel(items.map) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const r = await parallel(D.map(d => () => agent(d.p)))"}}'
check "raw pipeline(items,...) → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const r = await pipeline(files, s1, s2)"}}'
check "non-Workflow tool → allow" 0 '{"tool_name":"Bash","tool_input":{"command":"parallel(x.map(y))"}}'
check "member .parallel( → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"queue.parallel(2); log(1)"}}'
check "comment mentioning parallel() → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"// use boundedParallel(), never raw parallel()\nconst r = await boundedParallel(t,5)"}}'
check "parallel() only inside a string → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"const meta = { description: \"finders run, never raw parallel()\" }\nconst r = await boundedParallel(t, 5)"}}'
check "string mentions parallel() + a real raw parallel( → deny" 2 '{"tool_name":"Workflow","tool_input":{"script":"const note = \"we avoid parallel() normally\"\nconst r = await parallel(items.map(f))"}}'
# The helper line itself is sanctioned, and its fan-out receiver is now BOUNDED — the old fixture
# fanned `D.map(d=>()=>agent(d.p))`, which rule 2 correctly denies. A fixture that the gate must
# reject cannot double as the fixture proving it accepts.
check "boundedParallel + marker → allow" 0 '{"tool_name":"Workflow","tool_input":{"script":"async function boundedParallel(t,cap=5){const o=[];for(let i=0;i<t.length;i+=cap)o.push(...await parallel(t.slice(i,i+cap))); // gov:bounded-fanout\nreturn o}\nconst LENSES = [1,2,3]\nconst r = await boundedParallel(LENSES.map(d=>()=>agent(d)),5)"}}'

# ---- rule 2: verifier arity ---------------------------------------------------------------------
# THE PROVENANCE OF THESE FIXTURES: the first is the verify stage of the bespoke closing-review
# workflow written in this repo's own session on 2026-08-09, reconstructed from the transcript. It is
# not a synthetic approximation of the mistake; it is the mistake. The nine after it are the evasions
# a reviewer proposed when asked to defeat the rule — each was ALLOWED by an earlier cut of this hook
# and each is here because it was, not because it was imagined.
js "rule2: one agent per finding → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(`Adversarially verify: ${f.title}`, { label: `verify:${f.id}` })))
EOF
js "rule2: fan-out wrapped over many lines → deny" 2 <<'EOF'
const verdicts = await boundedParallel(all.map((f) => () =>
  agent(
    `line one
line two
line three
line four
line five
line six`,
    { label: `verify:${f.id}` })), 5)
EOF
js "rule2: flatMap → deny" 2 <<'EOF'
const r = await boundedParallel(all.flatMap((f) => [() => agent(f.claim)]), 5)
EOF
js "rule2: Array.from → deny" 2 <<'EOF'
const r = await boundedParallel(Array.from(all, (f) => () => agent(f.claim)), 5)
EOF
js "rule2: loop-built thunks → deny" 2 <<'EOF'
const th = []
for (const f of all) {
  th.push(() => agent(f.claim))
}
const r = await boundedParallel(th, 5)
EOF
js "rule2: forEach-built thunks → deny" 2 <<'EOF'
const th = []
all.forEach((f) => th.push(() => agent(f.claim)))
const r = await boundedParallel(th, 5)
EOF
js "rule2: renamed receiver → deny" 2 <<'EOF'
const groups = all
const r = await boundedParallel(groups.map((f) => () => agent(f.claim)), 5)
EOF
# The marker is a CLAIM; these three make it falsely and must still red, or the whitelist degenerates
# into "write the magic comment".
js "rule2: marker over chunk(all,1) → deny" 2 <<'EOF'
const b = chunk(all, 1) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker over splitInto(all, all.length) → deny" 2 <<'EOF'
const b = splitInto(all, all.length) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marker with a literal above the cap → deny" 2 <<'EOF'
const b = splitInto(all, 9) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# THE BYPASSES. Every one of these was ALLOWED by the first cut of rule 2 and reported "clean" by the
# merge-bar leg that delegates to it — found by an adversarial review of the commit that introduced
# the rule, each reproduced against this tree before it was fixed. They are here because a whitelist
# is only as good as the spellings it refuses, and the ones it has never seen are the ones that get
# written. The root cause was a single line: an unrecognised receiver fell through to ALLOW.
js "bypass: the marker on the agent() line itself → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.map((f) => () => agent(f.claim)), 5) // gov:fixed-verifiers
EOF
js "bypass: a .filter().map() chain → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.filter(Boolean).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a call-result receiver → deny" 2 <<'EOF'
const r = await boundedParallel(Object.values(byId).map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a spread literal → deny" 2 <<'EOF'
const items = [...allFindings]
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: [].concat(x) → deny" 2 <<'EOF'
const items = [].concat(allFindings)
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a reassigned receiver → deny" 2 <<'EOF'
let items = [1, 2]
items = allFindings
const r = await boundedParallel(items.map((f) => () => agent(f.claim)), 5)
EOF
js "bypass: a braceless for-of body → deny" 2 <<'EOF'
const out = []
for (const f of allFindings) out.push(await agent(f.claim))
EOF
js "bypass: a braceless while body → deny" 2 <<'EOF'
let i = 0
while (i < all.length) out.push(await agent(all[i++].claim))
EOF
js "bypass: a marked .concat() derivation → deny" 2 <<'EOF'
const LENSES = [{ k: 1 }, { k: 2 }]
const more = LENSES.concat(allFindings) // gov:fixed-verifiers
const r = await boundedParallel(more.map((f) => () => agent(f.k)), 5)
EOF
js "bypass: .reduce() instead of .map() → deny" 2 <<'EOF'
const r = await boundedParallel(allFindings.reduce((a, f) => a.concat([() => agent(f.claim)]), []), 5)
EOF

# ---- rule 2: the shapes that MUST pass ----------------------------------------------------------
# Without these the rule could be satisfied by denying everything, which is a gate that stops work
# rather than stopping a defect.
js "rule2: bounded group count + marker → allow" 0 <<'EOF'
const MAX_VERIFIERS = 5
const batches = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(batches.map((g) => () => agent(g)), 5)
EOF
js "rule2: a fixed lens literal → allow" 0 <<'EOF'
const LENSES = [{ k: 'security' }, { k: 'correctness' }, { k: 'seams' }, { k: 'dead-code' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked derivation from a bounded literal → allow" 0 <<'EOF'
const ALL_LENSES = [{ s: 'a' }, { s: 'b' }, { s: 'c' }]
const LENSES = a.lenses ? ALL_LENSES.filter((L) => a.lenses.includes(L.s)) : ALL_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.s)), 5)
EOF
js "rule2: a single synthesis agent → allow" 0 <<'EOF'
const synth = await agent('synthesize the confirmed findings', { label: 'synth' })
EOF
# The synthesis stage builds its PROMPT with a .map over every finding. A proximity-based scan read
# that as a fan-out and denied a one-agent call — measured on tools/workflows/tier2-review.js:290.
js "rule2: a synth prompt that quotes a .map → allow" 0 <<'EOF'
const synth = await agent(
  'findings:\n' + allFindings.map((f) => f.claim).join('\n'),
  { label: 'synth' })
EOF

# ---- scriptPath: a saved script is a FILE, and a node hook has fs -------------------------------
# Exiting 0 here made both rules unenforceable the moment anyone wrote the offending script to disk.
# NODE'S VIEW OF THE PATH, not the shell's. Under MSYS/git-bash one directory has two spellings and
# `mktemp -d` hands back the POSIX one (`/tmp/tmp.X`), which node cannot open. The first cut of these
# three arms passed for the wrong reason: the "offending file denied" arm was green because the read
# FAILED, not because the rule fired — a fixture that proves nothing while looking like proof.
NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP")
GOOD="$TMP/good.js"; printf 'const s = await agent("one")\n' > "$GOOD"
BAD="$TMP/bad.js";   printf 'const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)\n' > "$BAD"
GOOD="$NODEDIR/good.js"; BAD="$NODEDIR/bad.js"
check "scriptPath → clean file allowed" 0 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\"}}"
check "scriptPath → offending file denied" 2 "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$BAD\"}}"
check "scriptPath → unreadable path refused, not waved through" 2 '{"tool_name":"Workflow","tool_input":{"scriptPath":"/no/such/workflow.js"}}'
# A `name:` run supplies no source at all. It is ALLOWED here and covered by the merge-bar leg over
# tools/workflows/ instead — declared, not papered over.
check "name-only run → allow (no source reaches the hook)" 0 '{"tool_name":"Workflow","tool_input":{"name":"tier2-review"}}'

# ---- rule 3: the hook READS THE BOUND ------------------------------------------------------------
# EVERY ARM HERE ASSERTS ITS OWN MESSAGE, never the exit code. All three rules exit 2, so an arm
# keyed on 2 passes when a completely different branch fires — which is how the retired `cap-5` arm
# worked: it asserted that the REMEDIATION TEXT mentioned the number, on a fixture that tripped rule
# 1, and read as proof the cap was enforced while `CAP` decided nothing at all.
msg() { # name expected_exit needle   (script on stdin)
  local name=$1 want=$2 needle=$3 payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | node "$HOOK" >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); return
  fi
  if grep -qF "$needle" "$TMP/err"; then echo "ok   $name"; pass=$((pass+1))
  else echo "FAIL $name (exit $got as wanted, but no branch named: $needle)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

# S1 — the CALL SITE argument.
msg "rule3: call site cap 99 → deny naming the call site + 99" 2 \
  'the cap argument at the boundedParallel() CALL SITE is 99' <<'EOF'
const r = await boundedParallel(thunks, 99)
EOF
js "rule3: call site cap 5 → allow" 0 <<'EOF'
const r = await boundedParallel(thunks, 5)
EOF
# The forward paren join, which is the whole mechanism: every shipped call site spans lines, so a
# per-line read of argument 2 sees nothing at all.
msg "rule3: cap 500 written across lines → deny naming 500" 2 \
  'the cap argument at the boundedParallel() CALL SITE is 500' <<'EOF'
const r = await boundedParallel(
  thunks,
  500
)
EOF
# A TRAILING COMMA is not an argument. Measured: the prettier-formatted shape both shipped harnesses
# use split into two, and the phantom second one read as a cap of nothing — the predicate denied this
# repo's own review harness on its formatting.
js "rule3: one argument + a trailing comma → allow (not a phantom cap)" 0 <<'EOF'
async function boundedParallel(thunks, cap = 5) { return thunks }
const r = await boundedParallel(
  LENSES.map((L) => () => L),
)
EOF

# S2 — the DEFAULT PARAMETER, which governs a call that passes no cap.
js "rule3: no cap argument against a bounded default → allow" 0 <<'EOF'
async function boundedParallel(thunks, cap = 5) { return thunks }
const r = await boundedParallel(thunks)
EOF
msg "rule3: a wide default parameter → deny naming the DEFAULT PARAMETER + 99" 2 \
  'the DEFAULT PARAMETER of boundedParallel() is 99' <<'EOF'
async function boundedParallel(t, cap = 99) { return t }
EOF
msg "rule3: no cap argument and no helper defined → deny" 2 \
  'there is no DEFAULT PARAMETER to resolve the bound from' <<'EOF'
const r = await boundedParallel(thunks)
EOF

# S3 — the `||` fallback no longer binds, for ANY consumer. This is the defect that let two shipped
# harnesses raise their own agent count from the caller while the guard read the literal.
msg "rule3: cap bound by an || fallback → deny naming the fallback form" 2 \
  'bound by an `<expr> || 5` FALLBACK form' <<'EOF'
const CAP = (args && args.cap) || 5
const r = await boundedParallel(thunks, CAP)
EOF
# ...and the same binder, refused for the MARKER's K — one narrowing, every consumer.
msg "rule3: a marked K bound by an || fallback → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
const MAX_VERIFIERS = (args && args.maxVerifiers) || 5
const b = chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
# A BARE REASSIGNMENT invalidates the NUMBER, not just the receiver. The sweep existed for the
# whitelist and was never mirrored onto the consts map, so `let K = 5; K = 500` published a 5.
msg "rule3: a reassigned K → deny" 2 \
  'which this file does not show to be bounded' <<'EOF'
let K = 5
K = 500
const b = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF

# S4 — `gov:bounded-fanout` is a CLAIM about a width, checked like its sibling. It used to exempt its
# line outright, so a line slicing fifty wide returned before any shape check.
msg "rule3: marked line slicing 50 wide → deny naming the width" 2 \
  'the gov:bounded-fanout MARKED LINE slice width is 50' <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += 50)
    out.push(...(await parallel(thunks.slice(i, i + 50)))) // gov:bounded-fanout
  return out
}
EOF
msg "rule3: a marker on a line with no slice at all → deny" 2 \
  'does not slice a bare identifier by a visible width' <<'EOF'
const r = await parallel(everything) // gov:bounded-fanout
EOF
# The canonical shipped helper body must stay green: its width token is the helper's own `cap`
# PARAMETER, which S1 and S2 have already bounded. Without this case S4 denies all three harnesses.
js "rule3: the canonical helper body → allow" 0 <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const r = await boundedParallel(thunks, 5)
EOF

# ---- the cap is a FILE CONSTANT: AGENT_CAP is refused, not ignored -------------------------------
# The header advertised this override for two releases after it stopped deciding anything. A
# silently-ignored knob that appears to work is how that survived, so it denies and says why.
AGENT_CAP=50 printf '%s' '{"tool_name":"Workflow","tool_input":{"script":"const r = await agent(1)"}}' \
  > "$TMP/envpayload"
AGENT_CAP=50 node "$HOOK" < "$TMP/envpayload" >/dev/null 2>"$TMP/env.err"; envrc=$?
if [ "$envrc" = 2 ] && grep -qF 'AGENT_CAP is set (50) and this guard NO LONGER reads it' "$TMP/env.err"; then
  echo "ok   a set AGENT_CAP is refused with a message"; pass=$((pass+1))
else
  echo "FAIL a set AGENT_CAP was not refused (exit $envrc)"; sed 's/^/     /' "$TMP/env.err"; fail=$((fail+1))
fi
node "$HOOK" < "$TMP/envpayload" >/dev/null 2>&1
if [ "$?" = 0 ]; then echo "ok   ...and an UNSET AGENT_CAP changes nothing"; pass=$((pass+1))
else echo "FAIL an unset AGENT_CAP denied a clean script"; fail=$((fail+1)); fi

# The rule-2 remediation text still names the number it enforces.
if grep -qF 'verify-stage agents at 5 TOTAL' <(printf '%s' '{"tool_name":"Workflow","tool_input":{"script":"const r = await boundedParallel(all.map((f) => () => agent(f.c)), 5)"}}' | node "$HOOK" 2>&1); then
  echo "ok   rule-2 deny text names the 5-verifier cap"; pass=$((pass+1))
else echo "FAIL rule-2 deny text does not name the cap"; fail=$((fail+1)); fi

# ---- the two copies ------------------------------------------------------------------------------
# `.claude/hooks/agent-cap.js` is the WIRED copy and `tools/hooks/agent-cap.js` is the kit's. Nothing
# gated them: check-wiring.sh asserts the hook is wired, never that the wired one is this one. A
# stale wired copy enforces yesterday's rules while the kit documents today's.
# The arm used to sit inside `if BOTH files exist`, so a DELETED wired copy satisfied it by absence —
# the parity assertion's own failure mode. Inside the governance repo the pair is REQUIRED; in an
# adopting tree with no tools/hooks/ the arm skips loudly instead of vanishing.
ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [ -n "$ROOT" ] && [ -f "$ROOT/tools/hooks/agent-cap.js" ]; then
  if [ ! -f "$ROOT/.claude/hooks/agent-cap.js" ]; then
    echo "FAIL the wired copy .claude/hooks/agent-cap.js is MISSING (parity must not be satisfiable by absence)"
    fail=$((fail+1))
  elif diff -q <(sed 's/\r$//' "$ROOT/.claude/hooks/agent-cap.js") <(sed 's/\r$//' "$ROOT/tools/hooks/agent-cap.js") >/dev/null; then
    echo "ok   the wired copy matches the kit copy"; pass=$((pass+1))
  else
    echo "FAIL .claude/hooks/agent-cap.js has drifted from tools/hooks/agent-cap.js"
    echo "     fix: cp tools/hooks/agent-cap.js .claude/hooks/agent-cap.js"
    fail=$((fail+1))
  fi
else
  echo "skip the two-copy parity arm — no tools/hooks/agent-cap.js in this tree"
fi

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]

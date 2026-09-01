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

# ---- rule 5: the ref-keyed verdict join -----------------------------------------------------------
# TOOL-dTieredTribunal-14's section 4 declared these ten arms as what "the failing case has been
# observed" means for that unit, and the unit landed WITHOUT them: `git show --stat fb2d692e` never
# touched this file, and no arm here named `join`, `.ref` or `--only`. Rule 5 was covered only
# INDIRECTLY, through check-review-join.sh delegating to this hook — so the hook's own suite could
# not tell whether its own rule worked. Written now, from that table, against the shipped rule.
#
# jso <name> <expected_exit> <flag> — like `js`, but passes a selector flag, which the three
# selector arms need and which `check`/`js` cannot express.
jso() { # name expected_exit flag  (script on stdin)
  local name=$1 want=$2 flag=$3 payload got
  payload=$("$TESTPY" -c 'import json,sys; print(json.dumps({"tool_name":"Workflow","tool_input":{"script":sys.stdin.read()}}))')
  case "$payload" in *'"script"'*) ;; *) echo "FAIL $name (the payload builder produced nothing)"; fail=$((fail+1)); return;; esac
  printf '%s' "$payload" | node "$HOOK" "$flag" >/dev/null 2>"$TMP/err"; got=$?
  if [ "$got" = "$want" ]; then echo "ok   $name (exit $got)"; pass=$((pass+1))
  else echo "FAIL $name (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}

# The three bans. Each fires with NO raw primitive anywhere in the fixture, which is the whole point
# of the port: the file gate could only ever see files, and the modality where this defect actually
# happens is an inline `script` string on a Workflow call.
js "rule5: the bracket ban fires with no raw primitive present" 2 <<'EOF'
const verdicts = {}
verdicts[v.ref] = v
EOF
js "rule5: the Map ban fires" 2 <<'EOF'
const m = new Map()
m.set(f.ref, v)
EOF
js "rule5: the retired identifier fires" 2 <<'EOF'
const verdictByRef = new Map()
EOF

# Prose is NOT code. This is the narrowing the port deliberately took over the awk it replaced, and
# it is load-bearing: `tools/workflows/tier2-review.js` carries a comment that necessarily spells the
# banned expression while documenting the retired join, and a whole-file-text ban reds on it.
js "rule5: a comment documenting the join is prose" 0 <<'EOF'
// never key the join on m[f.ref] = v again; use the integer id
const r = 1
EOF
js "rule5: a string mentioning the join is prose" 0 <<'EOF'
const s = "do not write m[f.ref] = v"
EOF
js "rule5: a template mentioning the join is prose" 0 <<'EOF'
const prompt = `Never key a verdict join on verdictByRef; use the integer id.`
EOF

# The integer-keyed join is the SANCTIONED shape, and an arm that only proves denial is satisfied by
# a rule that denies everything.
js "rule5: the integer-keyed join is untouched" 0 <<'EOF'
const verdictById = new Map()
verdictById.set(f.id, v)
EOF

# The selector, as ONE arm set of three. The eighth alone proves only that the fixture is harmless;
# the ninth is what shows the flag actually narrowed something; the tenth is what stops the flag
# being a silent switch that disables the cap whenever it is misspelled.
jso "rule5: --only=join passes a rule-2 breach that carries no join" 0 --only=join <<'EOF'
const r = await parallel(D.map((d) => () => agent(d.p)))
EOF
js "rule5: the same script unfiltered still denies" 2 <<'EOF'
const r = await parallel(D.map((d) => () => agent(d.p)))
EOF
jso "rule5: an unrecognised selector refuses" 2 --only=bogus <<'EOF'
const r = 1
EOF

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

# ---- gov:sequential-agents (TOOL-dFoldedVerdict-4) ----------------------------------------------
# THE ONE LOOP SHAPE THE HOOK ADMITS. Owner-ratified spelling, 2026-09-01. It exists because a
# ratified `parallelism route: none` verdict forbids the bounded PARALLEL fan this hook permits while
# this hook forbade the strictly sequential dispatch that verdict requires — a harness iterating a
# build's units sat in the gap and could not be written at all.
#
# The ADMIT arm first, then one arm per clause. Each refusal names the FIRST clause that failed, so
# a fixture breaking two clauses proves only the earlier one — which is why C8's fixture keeps its
# `await` and breaks the function boundary instead.
js "seq: marked, bounded receiver, awaited, one call → ALLOW" 0 <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: an array LITERAL receiver is bounded too → ALLOW" 0 <<'EOF'
const units = ['a', 'b', 'c']
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C3 — a bare marker claims concurrency one and says nothing about the TOTAL, which is the half the
# owner ruling insists on. Two rules, not one.
js "seq: a bare marker with no bound → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C4 — the number is CHECKED, through the same resolver every other consumer uses.
js "seq: a bound above the cap → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(9)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# AC6 — a bound the file cannot RESOLVE, in the two shapes that look resolved and are not. An
# `<expr> || <int>` right-hand side is a caller-settable knob wearing a constant's clothes, which is
# how two shipped harnesses raised their own verifier count past the cap while every gate stayed
# green; a `.length` is a number nobody wrote down.
js "seq: an or-bound K → deny" 2 <<'EOF'
const K = (args && args.cap) || 5
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(K)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
js "seq: a .length K → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(units.length)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C6 — THE CLAUSE THAT CARRIES THE WEIGHT. Without it the marker's number is an author's assertion
# over an array of any size, which is the shape the owner ruling names as the thing to refuse.
js "seq: marked, but the receiver is not proven bounded → deny" 2 <<'EOF'
const units = findings.map((f) => f.id)
const out = []
for (const u of units) { // gov:sequential-agents(5)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
# C7 — AWAIT-ADJACENCY on THIS occurrence. A loop that collects unawaited calls is building a thunk
# array with extra steps.
js "seq: marked and bounded but the call is not awaited → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(agent('do ' + u, { label: 'u' }))
}
EOF
# C8 — awaited, but through a function boundary, which is the evasion the ban exists for. This
# fixture keeps the `await` deliberately: break C7 as well and the refusal names C7 and proves
# nothing about C8.
js "seq: awaited THROUGH a function boundary → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  const run = async () => out.push(await agent('do ' + u, { label: 'u' }))
  await run()
}
EOF
# THE NINTH CONDITION, judged after the scan. Two awaited calls in one marked body spend twice the
# bound, so the marker would name a number the loop does not obey.
js "seq: TWO awaited calls in one marked body → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  out.push(await agent('a ' + u, { label: 'u' }))
  out.push(await agent('b ' + u, { label: 'u' }))
}
EOF
# NESTED LOOPS FAIL CLOSED with no extra clause: the walk stops at the first enclosing loop, so an
# unmarked inner loop inside a marked outer one is refused at the inner header.
js "seq: an unmarked inner loop inside a marked outer one → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) { // gov:sequential-agents(3)
  for (const p of u.parts) {
    out.push(await agent('do ' + p, { label: 'p' }))
  }
}
EOF
# AND THE UNMARKED LOOP STILL DENIES WITH ITS ORIGINAL SENTENCE. This is the arm that proves the
# marker is an affordance and not a weakening: no claim, no change.
js "seq: an unmarked loop is denied exactly as before → deny" 2 <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) {
  out.push(await agent('do ' + u, { label: 'u' }))
}
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
# THE LENS ALLOWANCE IS THE SAME 5 AS EVERYTHING ELSE, and these three arms are why it can be. It
# read as 6 for one release and that was never a decision: the counter scored `1 + every top-level
# comma`, so a prettier-formatted 5-element array measured 6 and the constant had been raised to fit
# the error. Both drift-audit waves ship exactly this shape, so without the trailing-comma arm below
# lowering the number would deny two shipped harnesses — and the arm that proves the count is fixed
# has to be the multi-line, trailing-comma form, because the single-line one never mis-measured.
js "rule2: five lenses, prettier-formatted with a trailing comma → allow" 0 <<'EOF'
const LENSES = [
  { k: 'dead-code' },
  { k: 'unwired' },
  { k: 'duplication' },
  { k: 'inefficient' },
  { k: 'instruments' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses → deny (the allowance is 5)" 2 <<'EOF'
const LENSES = [{ k: 'a' }, { k: 'b' }, { k: 'c' }, { k: 'd' }, { k: 'e' }, { k: 'f' }]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: six lenses with a trailing comma → deny (the comma is not a sixth escape)" 2 <<'EOF'
const LENSES = [
  { k: 'a' },
  { k: 'b' },
  { k: 'c' },
  { k: 'd' },
  { k: 'e' },
  { k: 'f' },
]
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked derivation from a bounded literal → allow" 0 <<'EOF'
const ALL_LENSES = [{ s: 'a' }, { s: 'b' }, { s: 'c' }]
const LENSES = a.lenses ? ALL_LENSES.filter((L) => a.lenses.includes(L.s)) : ALL_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.s)), 5)
EOF
# TOOL-dTieredTribunal-13 S5 — the marked branch now judges EVERY top-level value branch. THREE of
# these five DENY arms are the reproduced holes: before this unit each PASSED, because either accept
# could return on a single arm while the other stayed caller-supplied. The other two are the guards
# inside the new predicate, which had no arm at all — and a guard nobody has watched fail is an
# assertion about nothing. Every one was run against the shipped file and its verdict recorded.
js "rule2: marked ternary whose OTHER arm is caller-supplied → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC : args.customLenses // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: marked .filter ROOTED on a caller value → deny" 2 <<'EOF'
const ALL = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.lenses.filter((L) => ALL.includes(L)) // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: bounded split in one arm, caller value in the other → deny" 2 <<'EOF'
const MAX_VERIFIERS = 5
const items = [1, 2, 3]
const b = cond ? chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) : args.custom // gov:fixed-verifiers
const r = await boundedParallel(b.map((g) => () => agent(g)), 5)
EOF
js "rule2: marked line whose right-hand side yields NO branch → deny" 2 <<'EOF'
const LENSES = // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
EOF
js "rule2: marked ternary whose : is not on the line → deny" 2 <<'EOF'
const SPEC = [{ k: 'a' }, { k: 'b' }]
const LENSES = args.kind === 'spec' ? SPEC // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
EOF
js "rule2: a marked ternary between two sibling literals → allow" 0 <<'EOF'
const SPEC_LENSES = [{ k: 'a' }, { k: 'b' }]
const DIFF_LENSES = [{ k: 'c' }, { k: 'd' }]
const LENSES = kind === 'spec-audit' ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers
const r = await boundedParallel(LENSES.map((L) => () => agent(L.k)), 5)
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

# D10 - a REASSIGNED receiver must SAY so. The reason map is written by both scan passes and was
# never cleared on accept, so a name refused on pass 1 for declaration order and then accepted on
# pass 2 kept the pass-1 text; the sweep below took the name back and the refusal printed an
# explanation of a branch pass 2 had just blessed. The verdict was right and the reason was wrong,
# which is precisely the "operator fixes it by guessing" failure the map was added to remove. This
# arm asserts the TEXT, because an exit-code arm cannot tell a right reason from a wrong one.
msg "rule2: a reassigned marked receiver -> deny NAMING the reassignment" 2   'was REASSIGNED after its bounded assignment' <<'EOF'
let LENSES = ALL.filter((L) => L.on) // gov:fixed-verifiers
const ALL = [1, 2, 3]
LENSES = args.custom
const r = await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
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

# ---- rule 4: a direct `Agent` spawn is COUNTED ---------------------------------------------------
# THE SEAM WAS MEASURED BEFORE ANY OF THIS WAS WRITTEN, per the spec's own F4: a throwaway PreToolUse
# hook on the `Agent` matcher captured a real spawn's payload on node a. `tool_name` arrives as
# exactly `Agent`, and `session_id`, `prompt_id` and `tool_use_id` are all present. The fixtures below
# are that payload shape, not a guess at it.
#
# THE TOKEN DIRECTORY IS ISOLATED WITHOUT A KNOB: the hook resolves it from the payload's own `cwd`,
# so a scratch tree with a `.git` directory in it is all the isolation this needs. A test-only env
# override would be one more caller-settable knob in the unit that exists to remove them.
mkdir -p "$TMP/agentrepo/.git"
AGJ="$NODEDIR/agentrepo"                       # node's spelling of the path, as the scriptPath arms use
AGROOT="$TMP/agentrepo/.git/agent-cap"
apay() { # session · prompt · tool_use_id
  printf '{"tool_name":"Agent","cwd":"%s","session_id":"%s","prompt_id":"%s","tool_use_id":"%s"}' \
    "$AGJ" "$1" "$2" "$3"
}

# AC23 — six SEQUENTIAL spawns in one turn: five allowed, the sixth denied. Asserted on a string
# unique to this branch and never on the exit code, which all four rules in this file share.
ok5=1
for i in 1 2 3 4 5; do
  printf '%s' "$(apay S1 P1 "u$i")" | node "$HOOK" >/dev/null 2>"$TMP/ag.err" || ok5=0
done
printf '%s' "$(apay S1 P1 u6)" | node "$HOOK" >/dev/null 2>"$TMP/ag6.err"; rc6=$?
if [ "$ok5" = 1 ] && [ "$rc6" = 2 ] \
   && grep -qF 'direct-Agent spawn budget for this prompt is exhausted' "$TMP/ag6.err"; then
  echo "ok   rule4: six sequential spawns — five allowed, the sixth denied by name"; pass=$((pass+1))
else
  echo "FAIL rule4: sequential budget (first five ok=$ok5, sixth exit $rc6)"; sed 's/^/     /' "$TMP/ag6.err"; fail=$((fail+1))
fi

# ...and the SAME tool_use_id re-fed does not spend a second slot. A hook re-invoked for one call
# would otherwise burn the turn's budget on a single spawn.
printf '%s' "$(apay S1 P1 u3)" | node "$HOOK" >/dev/null 2>&1; rcdup=$?
[ "$rcdup" = 0 ] && { echo "ok   rule4: a repeated tool_use_id is idempotent"; pass=$((pass+1)); } \
                 || { echo "FAIL rule4: a repeated tool_use_id was charged again (exit $rcdup)"; fail=$((fail+1)); }

# AC24 — THE ARM THE READ-THEN-DECIDE DESIGN FAILS. Six CONCURRENT payloads: exactly five slots
# exist afterwards and exactly ONE deny is emitted. Run repeatedly, not once, because the miscount it
# guards against is nondeterministic — measured on node a, a four-call burst overlapped its hook
# processes and two of four read the same count. Create-a-token-THEN-count does not fix that either:
# each of six processes sees between its own ordinal and six, so several deny. Only the atomic claim
# of a NUMBERED slot decides it in the create, which is why the slots are numbered.
conc=1; why=""
for round in 1 2 3 4 5 6 7 8; do
  P="Pc$round"
  rm -f "$TMP"/ag.rc.*
  for i in 1 2 3 4 5 6; do
    ( printf '%s' "$(apay S1 "$P" "c$round-$i")" | node "$HOOK" >/dev/null 2>&1; echo $? > "$TMP/ag.rc.$i" ) &
  done
  wait
  denies=$(cat "$TMP"/ag.rc.* 2>/dev/null | grep -c '^2$')
  slots=$(ls "$AGROOT/S1__$P" 2>/dev/null | grep -c .)
  if [ "$denies" != 1 ] || [ "$slots" != 5 ]; then conc=0; why="round $round: $denies deny(s), $slots slot(s)"; break; fi
done
[ "$conc" = 1 ] && { echo "ok   rule4: 8 concurrent bursts of six — exactly 5 slots, exactly 1 deny, every time"; pass=$((pass+1)); } \
                || { echo "FAIL rule4: concurrent burst miscounted ($why)"; fail=$((fail+1)); }

# AC25 — a FRESH prompt resets the budget, with no cleanup step run in between. The budget is keyed
# per prompt precisely so nothing has to remember to clear it.
printf '%s' "$(apay S1 Pfresh n1)" | node "$HOOK" >/dev/null 2>&1; rcf=$?
[ "$rcf" = 0 ] && { echo "ok   rule4: a new prompt resets the budget with no cleanup"; pass=$((pass+1)); } \
               || { echo "FAIL rule4: a new prompt did not reset the budget (exit $rcf)"; fail=$((fail+1)); }

# AC26 — a slot IDLE past SLOT_TTL_MS is reclaimed, and one still inside it is NOT. Both directions,
# because an expiry that always fires is a cap that does not exist, and one that never fires is the
# permanent budget this arm was added to end. The clock is moved with `touch -d`, never by sleeping:
# the constant is 45 minutes and a test that waits for it is a test nobody runs.
#
# THE STALE CASE IS THE REGRESSION ARM. Before the expiry landed, five sequential spawns exhausted a
# turn's budget forever — measured, six sequential spawns with distinct tool_use_ids and the sixth
# denied against five long-idle slots. Revert SLOT_TTL_MS to Infinity and this arm goes red.
for i in 1 2 3 4 5; do
  printf '%s' "$(apay Sttl Pttl "t$i")" | node "$HOOK" >/dev/null 2>&1
done
TURNTTL="$AGROOT/Sttl__Pttl"
if [ ! -d "$TURNTTL" ]; then
  echo "FAIL rule4: the TTL fixture claimed no slots — $TURNTTL absent"; fail=$((fail+1))
else
  # Age slot-1 only. The remaining four stay fresh, which is what makes the second half a control
  # rather than a restatement of the first.
  touch -d '46 minutes ago' "$TURNTTL/slot-1" 2>/dev/null || touch -A -004600 "$TURNTTL/slot-1" 2>/dev/null
  printf '%s' "$(apay Sttl Pttl t6)" | node "$HOOK" >/dev/null 2>&1; rcstale=$?
  printf '%s' "$(apay Sttl Pttl t7)" | node "$HOOK" >/dev/null 2>"$TMP/ttl.err"; rcfresh=$?
  if [ "$rcstale" = 0 ] && [ "$rcfresh" = 2 ] \
     && grep -qF 'within the last' "$TMP/ttl.err"; then
    echo "ok   rule4: an idle slot past the TTL is reclaimed; four fresh ones are not"; pass=$((pass+1))
  else
    echo "FAIL rule4: slot TTL (stale-reclaim exit $rcstale want 0, fresh-deny exit $rcfresh want 2)"
    sed 's/^/     /' "$TMP/ttl.err"; fail=$((fail+1))
  fi
fi

# ...and the DENY MESSAGE says which rule it is enforcing. It used to read "already spawned in this
# turn", which described a permanent budget and named the concurrency rule in the same breath. A
# message that misstates the rule sends the reader to consolidate work that did not need it.
printf '%s' "$(apay Smsg Pmsg m1)" | node "$HOOK" >/dev/null 2>&1
for i in 2 3 4 5 6; do
  printf '%s' "$(apay Smsg Pmsg "m$i")" | node "$HOOK" >/dev/null 2>"$TMP/msg.err"
done
grep -qF 'claimed in this turn within the last' "$TMP/msg.err" \
  && grep -qF 'is reclaimed on the next spawn' "$TMP/msg.err" \
  && { echo "ok   rule4: the deny message states the window, not a permanent budget"; pass=$((pass+1)); } \
  || { echo "FAIL rule4: deny message does not state the reclaim window"; sed 's/^/     /' "$TMP/msg.err"; fail=$((fail+1)); }

# FAIL OPEN when the budget cannot be KEYED — and prove it by the ABSENCE of a token, not by the exit
# code alone, which a hook that allowed everything would also produce. A hook that denies every spawn
# because a payload field is missing is worse than the burst it prevents; a token it could not
# CREATE is a different fact and denies (the branch above it).
before=$(ls "$AGROOT" 2>/dev/null | grep -c .)
printf '{"tool_name":"Agent","cwd":"%s","session_id":"S9","tool_use_id":"x"}' "$AGJ" \
  | node "$HOOK" >/dev/null 2>&1; rcn=$?
after=$(ls "$AGROOT" 2>/dev/null | grep -c .)
{ [ "$rcn" = 0 ] && [ "$before" = "$after" ]; } \
  && { echo "ok   rule4: an unkeyable payload fails OPEN and writes no token"; pass=$((pass+1)); } \
  || { echo "FAIL rule4: unkeyable payload (exit $rcn, dirs $before -> $after)"; fail=$((fail+1)); }

# ---- the two copies ------------------------------------------------------------------------------
# `.claude/hooks/agent-cap.js` is the WIRED copy and `tools/hooks/agent-cap.js` is the kit's. Nothing
# gated them: check-wiring.sh asserts the hook is wired, never that the wired one is this one. A
# stale wired copy enforces yesterday's rules while the kit documents today's.
# The arm used to sit inside `if BOTH files exist`, so a DELETED wired copy satisfied it by absence —
# the parity assertion's own failure mode. Inside the governance repo the pair is REQUIRED; in an
# adopting tree with no tools/hooks/ the arm skips loudly instead of vanishing.
# The kit copy is LOCATED, never assumed at one prefix. Gating on the literal `tools/hooks/` made
# this arm disarm itself in every tree that installs the kit anywhere else: measured in a scratch
# repo with the kit at `<root>/hooks/` and NO wired copy at all, this file reported "39 passed, 0
# failed", exit 0. A stale wired hook enforcing yesterday's fan-out rules was undetectable there.
# Finding nothing is still a legitimate skip — an adopting tree need not carry the kit — but finding
# the kit and then not checking it is not.
ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
KITJS=""
if [ -n "$ROOT" ]; then
  for c in "$ROOT/tools/hooks/agent-cap.js" "$ROOT/hooks/agent-cap.js"; do
    [ -f "$c" ] && { KITJS="$c"; break; }
  done
  # Last resort: ask git where it is, so a prefix nobody listed still arms the arm.
  if [ -z "$KITJS" ]; then
    rel=$(git -C "$ROOT" ls-files -- '*/hooks/agent-cap.js' 'hooks/agent-cap.js' 2>/dev/null \
          | grep -v '^\.claude/' | head -1)
    [ -n "$rel" ] && KITJS="$ROOT/$rel"
  fi
fi
if [ -n "$KITJS" ]; then
  if [ ! -f "$ROOT/.claude/hooks/agent-cap.js" ]; then
    echo "FAIL the wired copy .claude/hooks/agent-cap.js is MISSING (parity must not be satisfiable by absence)"
    fail=$((fail+1))
  elif diff -q <(sed 's/\r$//' "$ROOT/.claude/hooks/agent-cap.js") <(sed 's/\r$//' "$KITJS") >/dev/null; then
    echo "ok   the wired copy matches the kit copy"; pass=$((pass+1))
  else
    echo "FAIL .claude/hooks/agent-cap.js has drifted from ${KITJS#"$ROOT/"}"
    echo "     fix: cp ${KITJS#"$ROOT/"} .claude/hooks/agent-cap.js"
    fail=$((fail+1))
  fi
else
  echo "skip the two-copy parity arm — no kit copy of agent-cap.js is tracked in this tree (looked for tools/hooks/, hooks/, then any */hooks/ outside .claude/)"
fi


# ---- rule 2: LENS PROSE IS NOT CODE (TOOL-aLexedStripper-2) --------------------------------------
# Every arm below is the SAME correct five-element lens array, fanned through the sanctioned helper.
# Only the English inside one prompt differs, and every one of them must ADMIT.
#
# THE PROVENANCE: five of these spellings DENIED against `agent-cap` 1.8, measured across both array
# shapes before the fix was wired — a literal `...` read as a spread by the array-literal guard, and
# an unmatched `[`, `]`, `)` or `}` read as bracket structure by the join-forward walk or by
# `topLevelArgs`. An adopter hit this and filed it as a gov ask; their diagnosis blamed apostrophes
# and prescribed U+2019, and both of those admit at 1.8 — which is why the apostrophe and U+2019 rows
# are here too, as the negative result.
#
# The ADMIT direction is the whole point of this group. A fixture set that only ever asserts denials
# cannot catch a guard that has become a blanket.

js "rule2 prose: a literal ... in a prompt is not a spread" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows ... then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched [ in a prompt is not an array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows [see the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ] in a prompt does not close the array" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows], then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched ) in a prompt does not shift the depth" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows), then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: an unmatched } in a prompt does not close the element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `list the rows}, then the table` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: apostrophes and an em dash, the adopter's stale diagnosis" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `check S2's rows and the table's keys — then stop` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 prose: SIX lenses still deny, whatever the prose" 2 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `list the rows ... then the table` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
  { key: "f", prompt: `six` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# ---- rule 2: an interpolation holds CODE, and both directions are checked ------------------------
# `blankLiterals` blanks `${…}` bodies. Rule 2 may not, or an `agent(` written inside one becomes
# invisible to the only rule that bounds it. The multi-line shape is the one a per-line span view
# cannot reach: its `}` is not on its opening line.

js "rule2 interp: an unbounded fan inside a single-line interpolation denies" 2 <<'EOF'
const all = args.everything
const r = `x: ${await Promise.all(all.map((f) => agent(f.p)))}`
return r
EOF

js "rule2 interp: an unbounded fan inside a MULTI-line interpolation denies" 2 <<'EOF'
const all = args.everything
const report = `results: ${await Promise.all(
  all.map((f) => agent(f.prompt))
)}`
return report
EOF

js "rule2 interp: a BOUNDED fan inside an interpolation still admits" 0 <<'EOF'
const L = [{a:1},{a:2},{a:3},{a:4},{a:5}]
const r = `res: ${await boundedParallel(L.map((x) => () => agent(x)), 5)}`
return r
EOF

# ---- rule 2: template-literal edges (TOOL-aLexedStripper-2 S2, TOOL-aLexedStripper-5) ------------
# A nested template must BALANCE, or the fallback path fires on a legal script. A backtick that this
# file cannot model — inside a regex literal, a string, or a comment — must not change a verdict:
# the fallback returns the pre-change view, so these are the shipped hook's own answers.

js "rule2 edges: a nested template balances and admits" 0 <<'EOF'
const n = `a${`b`}c`
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a regex literal admits a legal harness" 0 <<'EOF'
const re = /`/
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick in a regex character class admits" 0 <<'EOF'
const re = /[`~]/g
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a quoted string admits" 0 <<'EOF'
const s = "a ` b"
const t = 'c ` d'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

js "rule2 edges: a backtick inside a comment admits" 0 <<'EOF'
// a stray ` in a line comment
/* and one ` in a block comment */
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `one` },
  { key: "b", prompt: `two` },
  { key: "c", prompt: `three` },
  { key: "d", prompt: `four` },
  { key: "e", prompt: `five` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# THE FAIL-OPEN THIS GROUP EXISTS FOR. An unterminated template literal blanks everything below it
# under a naive template-aware view, hiding the fan entirely. The fallback denies it because the
# shipped hook denies it — which is the property, not a coincidence.
js "rule2 edges: an unbounded fan below an unterminated backtick still denies" 2 <<'EOF'
const stray = `an unterminated template literal
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF


# The same class in the OTHER field-count regime. A stray `)` drives topLevelArgs' depth negative and
# every comma AFTER it then counts at top level, so denial depends on how many commas follow -- i.e.
# on how many fields each element has. A one-field array is denied only when the prose sits in the
# LAST element; a two-field one is denied wherever it sits. Both regimes are here because a fixture
# in one of them measures the other wrongly, which is how two independent grids disagreed on `)`.
js "rule2 prose: one-field element, stray ) in the LAST element" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { prompt: `one` },
  { prompt: `two` },
  { prompt: `three` },
  { prompt: `four` },
  { prompt: `list the rows), then the table` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF

# The other end of the same rule: a `)` with no comma after it inside its element was ALWAYS harmless,
# so this arm admits at BASE too. It is here to pin the boundary, not the fix -- without it the group
# only ever asserts the denying side and cannot notice the guard becoming a blanket.
js "rule2 prose: a stray ) at the very end of the prose was never a denial" 0 <<'EOF'
const MAX_VERIFIERS = 5
const LENSES = [
  { key: "a", prompt: `hunt auth holes` },
  { key: "b", prompt: `hunt logic bugs` },
  { key: "c", prompt: `the rows, then the table)` },
  { key: "d", prompt: `hunt dead code` },
  { key: "e", prompt: `hunt seams` },
]
await boundedParallel(LENSES.map((l) => () => agent(l.prompt)), MAX_VERIFIERS)
EOF


# ---- renderCodeView: the FAIL-OPEN arms (TOOL-aLexedStripper-5) ----------------------------------
# Every arm here is a script the SHIPPED hook denies, and each one was ADMITTED by some revision of
# renderCodeView before it reached this file. They exist because two closing-review rounds found a
# fail-open in this view and the first repair was measured insufficient for the second shape. A view
# that blanks anything can hide a fan-out; these are the shapes that proved it.

js "renderCodeView: an unbounded fan below an unterminated block-comment opener denies" 2 <<'EOF'
const x = 1 /* never closed
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

js "renderCodeView: a regex-borne /* closed by a later ordinary */ denies" 2 <<'EOF'
const re = /\/*/
const all = args.everything
await boundedParallel(all.map((x) => () => agent(x)), 5)
const d = a */ b
EOF

# The apostrophe inside a regex literal. The view used to run to end of line and synthesize a closer
# the source never had, taking the fan on that line with it.
js "renderCodeView: an apostrophe in a regex does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (/won't/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: the same line without the apostrophe denies too (control)" 2 <<'EOF'
const all = args.everything
if (/wont/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
EOF

js "renderCodeView: an unpaired double quote does not swallow the fan on its line" 2 <<'EOF'
const all = args.everything
if (x === 5") await Promise.all(all.map((f) => agent(f.prompt)))
EOF

# A block comment is NOT blanked by this view, deliberately, so a primitive named inside one still
# trips rule 1 exactly as the dossier says it does. This arm pins that posture rather than the bug.
js "renderCodeView: a raw primitive inside a block comment still denies (fail-closed posture)" 2 <<'EOF'
/* the shape this bans is parallel(items.map(...)) */
const r = await parallel(D.map((d) => () => agent(d.p)))
EOF


# ---- TOOL-dMispairedQuote-1: a quote pairs with the WRONG partner ---------------------------------
# Every arm below was staged RED against the tip before it landed. The defect: each of this file's
# string views pairs a quote with the next quote of the same kind on the line, so an apostrophe in
# prose earlier on that line pairs with the quote opening `agent('a'` and the span blanked between
# them carries the fan-out. `addc6169` already demanded a matching PAIR; a pair exists, and it is the
# wrong one. The construct holding the apostrophe is not the mechanism -- these arms carry a regex, a
# double-quoted string, a block comment and a template literal, and the shipped hook admitted all
# four. The CONTROL beside each is the same line with the apostrophe removed.

js "mispaired quote: regex literal shares the fan-out line -> deny" 2 <<'EOF'
const re = /won't/
const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: SAME LINE is the load-bearing part -> deny" 2 <<'EOF'
const re = /won't/; const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: control, same line without the apostrophe -> deny" 2 <<'EOF'
const re = /wont/; const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: apostrophe in a DOUBLE-quoted string -> deny" 2 <<'EOF'
const s = "don't"; const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: apostrophe in a BLOCK COMMENT -> deny" 2 <<'EOF'
/* don't */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: apostrophe in a TEMPLATE literal -> deny" 2 <<'EOF'
const s = `don't`; const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: LOOSE apostrophe opening a word -> deny" 2 <<'EOF'
/* run 'em */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "mispaired quote: rule 2 counter loses the agent( -> deny" 2 <<'EOF'
const re = /won't/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

js "mispaired quote: rule 2 control, no apostrophe -> deny" 2 <<'EOF'
const re = /wont/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)
EOF

js "mispaired quote: rule 3 loses a declared cap of 50 -> deny" 2 <<'EOF'
const B = ['a','b']
const re = /won't/; const r = await boundedParallel(B.map((x) => () => agent('x')), 50)
EOF

js "mispaired quote: rule 3, an unpaired double quote swallows the bound -> deny" 2 <<'EOF'
const B = ['a','b']
const c = x === 5"; const r = await boundedParallel(B.map((x) => () => agent(x)), 50)
EOF

# Rule 5, the ref-keyed-join ban, is defeated by the same apostrophe and nobody had named it. Both
# of these ADMIT at the tip and deny after.
js "mispaired quote: rule 5 join hidden by an apostrophe -> deny" 2 <<'EOF'
const re = /won't/; m.get(f.ref); const s = 'x'
EOF

js "mispaired quote: rule 5 verdictByRef hidden by an apostrophe -> deny" 2 <<'EOF'
const re = /won't/; const verdictByRef = {}; const s = 'x'
EOF

js "mispaired quote: rule 5 control, no apostrophe -> deny" 2 <<'EOF'
const re = /wont/; m.get(f.ref); const s = 'x'
EOF

# ---- and the ADMIT direction, which is half the class -------------------------------------------
# A fixture group that only ever asserts denials cannot catch a fail-closed that has become a
# fail-open. Each of these passes at the tip and must keep passing.

js "mispaired quote: a legal log() with a contraction in its trailing comment -> allow" 0 <<'EOF'
log('parallel(') // we don't allow it
EOF

js "mispaired quote: return + a string naming a primitive -> allow" 0 <<'EOF'
function f() { return 'parallel (nope)' }
await boundedParallel([() => agent(1)], 5)
EOF

js "mispaired quote: case + a string naming a primitive -> allow" 0 <<'EOF'
switch (x) { case 'parallel (nope)': break }
await boundedParallel([() => agent(1)], 5)
EOF

js "mispaired quote: throw + a string naming a primitive -> allow" 0 <<'EOF'
if (x) throw 'pipeline (nope)'
await boundedParallel([() => agent(1)], 5)
EOF

js "mispaired quote: aLexedStripper-5's own fixture stays legal -> allow" 0 <<'EOF'
const SEP = /[`]/
const all = ['a','b']
await boundedParallel(all.map((x) => () => agent(x)), 5)
EOF

# ---- the keyword clause, fixtured over its DECLARED SET rather than sampled ----------------------
# `checkLiteralOpen` admits a quote as an opener after a JS keyword, because `return 'x'` is ordinary
# code. Eleven keywords are declared and each is also an English word, so `/* <keyword> 'em */`
# mispairs for every member: a STATED residual, one arm per member so the leak is recorded rather
# than assumed away, and none of them a regression -- all eleven ADMIT at the tip too. The three
# connectives dropped from the set are the CONTROL: they deny.
for kw in return case throw typeof instanceof new delete void yield await else; do
  js "keyword residual: /* $kw 'em */ above a raw parallel( -> allow (stated residual)" 0 <<EOF
/* $kw 'em */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF
done

for kw in in of do run one; do
  js "keyword control: /* $kw 'em */ is not a declared opener -> deny" 2 <<EOF
/* $kw 'em */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF
done


# ---- TOOL-dMispairedQuote-3: no denial may be LOST ------------------------------------------------
# Correcting what counts as a string literal does not only un-hide fan-outs; it un-hides every other
# character the old mispairing was blanking, and rules 2, 3 and 5 walk brackets and balance parens
# ACROSS lines. Three DENY-to-ADMIT moves were reproduced against unit 1 alone. Each has a fixture
# here, and each was ALSO closed by the property arm below -- which is what makes the property worth
# its bytes: the next repair to these views inherits it without knowing these three shapes.

js "no-regress: a backtick inside a regex, above a multi-line cap-50 call -> deny" 2 <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /it's`don't/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF

js "no-regress: an exposed backtick leaks the template mode -> deny" 2 <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /a'b`c/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF

js "no-regress: a quoted URL inside a same-line template -> deny" 2 <<'EOF'
const p = `see 'http://x' now`; await parallel(all.map(f))
EOF

js "no-regress: a DOUBLE-quoted URL in a template does it without an apostrophe -> deny" 2 <<'EOF'
const p = `see "http://x" now`; await parallel(all.map(f))
EOF

# ---- S10: `verbatim` is CHECKED, not asserted ----------------------------------------------------
# The three renderShipped* bodies must equal their counterparts in the BASE blob. Only the name line
# differs. A tree where that blob does not resolve -- every adopter -- gets an announced SKIP.
GOV_BASE_SHA=${GOV_BASE_SHA:-d65da7ab}
# DERIVED, never spelled: a `tools/hooks/` literal is gov's own install prefix and resolves to
# nothing in a target that installed this kit elsewhere, which is what the shipped-surface ratchet
# refuses. `git ls-files --full-name` answers where THIS hook actually lives in THIS tree.
HOOKREL=$(git -C "$HERE" ls-files --full-name -- "$HOOK" 2>/dev/null | head -1)
if [ -n "$HOOKREL" ] && git -C "$HERE" show "$GOV_BASE_SHA:$HOOKREL" > "$TMP/base-hook.js" 2>/dev/null; then
  cat > "$TMP/byte.py" <<'PYEOF'
import sys, pathlib
base = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n")
cur = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").replace("\r\n", "\n")
PAIRS = [("function stripStrings(line) {", "function renderShippedLine(line) {"),
         ("function renderCodeView(script) {", "function renderShippedView(script) {"),
         ("function blankLiterals(script) {", "function renderShippedBlanks(script) {")]
def block(text, header):
    ls = text.split("\n")
    s = ls.index(header)
    e = s
    while ls[e] != "}":
        e += 1
    return "\n".join(ls[s + 1:e + 1])
bad = 0
for b, c in PAIRS:
    try:
        if block(base, b) != block(cur, c):
            print("DRIFT %s is not the BASE bytes of %s" % (c, b)); bad += 1
    except ValueError as e:
        print("MISSING %s or %s (%s)" % (b, c, e)); bad += 1
print("bodies-compared 3 drifted %d" % bad)
sys.exit(1 if bad else 0)
PYEOF
  "$TESTPY" "$TMP/byte.py" "$TMP/base-hook.js" "$HOOK" > "$TMP/byte.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress: the three renderShipped* bodies are the BASE bytes"; pass=$((pass+1))
  else
    echo "FAIL no-regress: a renderShipped* body has drifted from BASE"; sed 's/^/     /' "$TMP/byte.out"; fail=$((fail+1))
  fi
else
  echo "skip no-regress byte arm — $GOV_BASE_SHA:${HOOKREL:-<this hook is not tracked here>} does not resolve in this tree, so there is nothing to compare the frozen bodies against"
fi

# ---- S9: THE PROPERTY. No script this hook denied at BASE may be admitted now. --------------------
# The population is every tracked file PLUS the fixtures below. The second half is not padding:
# unit 1 alone flips ZERO tracked files, because every reproduced shape is synthetic. A property arm
# whose population holds no instance of the class it guards can only ever pass.
if [ -s "$TMP/base-hook.js" ]; then
  mkdir -p "$TMP/nrfix"
  # TOOL-dFoldedVerdict-4 S7. The FIRST is the ratified path: BASE denies it, this hook admits it, and
  # deleting the marker restores the denial — which is what makes the loss marker-attributed rather
  # than merely tolerated. The SECOND is the control: an unmarked braceless loop that BOTH hooks deny,
  # so the affordance is proven scoped to the marker and not to loops in general.
  cat > "$TMP/nrfix/seq-marked-bounded.js" <<'EOF'
const MAX = 5
const units = [1, 2, 3, 4, 5]
const out = []
for (const u of units) { // gov:sequential-agents(MAX)
  out.push(await agent('do ' + u, { label: 'u' }))
}
EOF
  cat > "$TMP/nrfix/seq-unmarked-braceless.js" <<'EOF'
const units = [1, 2, 3]
const out = []
for (const u of units) out.push(await agent('do ' + u, { label: 'u' }))
EOF
  cat > "$TMP/nrfix/backtick-in-regex.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /it's`don't/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/exposed-backtick.js" <<'EOF'
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
const L = ['a','b']
const re = /a'b`c/
await boundedParallel(
  L.map((s) => () => agent(s)),
  50,
)
EOF
  cat > "$TMP/nrfix/template-borne-comment.js" <<'EOF'
const p = `see 'http://x' now`; await parallel(all.map(f))
EOF
  cat > "$TMP/nr.py" <<'PYEOF'
import json, subprocess, sys, pathlib
base_hook, cur_hook, root, fixdir = sys.argv[1:5]
root = pathlib.Path(root).resolve()
files = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True).stdout.split()
pop = [root / f for f in files] + sorted(pathlib.Path(fixdir).glob("*.js"))
lost, ratified, denied, n = [], [], 0, 0
for p in pop:
    try:
        body = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    payload = json.dumps({"tool_name": "Workflow", "tool_input": {"script": body}})
    a = subprocess.run(["node", base_hook], input=payload, capture_output=True, text=True, timeout=120).returncode
    n += 1
    if a != 2:
        continue
    denied += 1
    b = subprocess.run(["node", cur_hook], input=payload, capture_output=True, text=True, timeout=120).returncode
    # ADMISSION IS `exit != 2`, not `exit == 0`. The hook BLOCKS only on 2, so a crash (1) or a
    # timeout is an admission too — and scoring it as 0 made this arm blind to exactly the two
    # defects the closing review found in the code it guards.
    if b != 2:
        # CLASS-SCOPED RATIFICATION (TOOL-dFoldedVerdict-4). A denial this hook no longer makes is
        # ratified ONLY when the marker is what bought it: strip every `gov:sequential-agents` token
        # from the bytes and re-run. Denial restored means the marker did it, and the loss is this
        # unit's declared affordance. Denial NOT restored means something else changed, and that is a
        # regression whatever it looks like. No path list and no BASE-sha bump: the ratification is
        # keyed on the CLASS, so a file nobody thought to enumerate is graded the same way.
        stripped = body.replace("gov:sequential-agents", "")
        rp = json.dumps({"tool_name": "Workflow", "tool_input": {"script": stripped}})
        r = subprocess.run(["node", cur_hook], input=rp, capture_output=True, text=True, timeout=120).returncode
        if r == 2:
            ratified.append("%s (exit %d, denial restored by removing the marker)" % (p, b))
        else:
            lost.append("%s (exit %d)" % (p, b))
for f in lost:
    print("LOST a denial: %s" % f)
for f in ratified:
    print("RATIFIED a marker-attributed loss: %s" % f)
# REDS ON ZERO RATIFICATIONS, so the ratification branch cannot go unexercised and pass by never
# running — which is the same could-not-fail shape as the empty-population guard beside it.
print("population %d scanned, %d denied at BASE, %d denial(s) lost, %d ratified" % (n, denied, len(lost), len(ratified)))
sys.exit(1 if lost or denied == 0 or not ratified else 0)
PYEOF
  "$TESTPY" "$TMP/nr.py" "$TMP/base-hook.js" "$HOOK" "$HERE/../.." "$TMP/nrfix" > "$TMP/nr.out" 2>&1
  if [ $? = 0 ]; then
    echo "ok   no-regress: no denial lost against BASE ($(tail -1 "$TMP/nr.out"))"; pass=$((pass+1))
  else
    echo "FAIL no-regress: a denial the BASE hook made is gone"; sed 's/^/     /' "$TMP/nr.out"; fail=$((fail+1))
  fi
else
  echo "skip no-regress property arm — the BASE blob does not resolve in this tree, so there is no shipped hook to compare verdicts against"
fi


# ---- closing-review folds: a guard that times out, or crashes, does not guard --------------------
# A PreToolUse hook is NON-BLOCKING when it times out AND when it exits 1. Both were reachable.

# F1. `checkLiteralOpen` copied the whole line prefix per quote, so cost was quadratic in LINE
# length and every ordinary `return 'x'` paid it. Measured before the fix: 253 KB on one line took
# 33.8 s against 62 ms at BASE. This arm is a BUDGET, not a verdict: it fails if the hook takes
# longer on one long line than a generous multiple of the same script split across lines.
long_one=$("$TESTPY" -c "
import json
n = 8000
line = 'const x = [' + ','.join(\"f(a%d, 'lit%d')\" % (i, i) for i in range(n)) + ']'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': line}}))
")
t0=$(date +%s)
printf '%s' "$long_one" | node "$HOOK" >/dev/null 2>&1
t1=$(date +%s)
if [ $((t1 - t0)) -le 10 ]; then
  echo "ok   quadratic budget: 8000 literals on ONE line in $((t1 - t0))s (<= 10s)"; pass=$((pass+1))
else
  echo "FAIL quadratic budget: 8000 literals on ONE line took $((t1 - t0))s — a hook that times out is NON-BLOCKING"; fail=$((fail+1))
fi

# F2. A throw in the corrected views must not become an admission. This script drives
# `parseBranches` past its recursion limit, which is PRE-EXISTING: the BASE hook exits 1 on it and
# therefore does not block. Denying is stricter than BASE and is this file's stated posture.
deep=$("$TESTPY" -c "
import json
k = ' ? args.big : '.join('c%d' % i for i in range(9000))
sc = 'const K = ' + k + ' : args.big // gov:fixed-verifiers\nawait boundedParallel(K.map((g) => () => agent(g)), 5)'
print(json.dumps({'tool_name':'Workflow','tool_input':{'script': sc}}))
")
printf '%s' "$deep" | node "$HOOK" >/dev/null 2>&1; deeprc=$?
if [ "$deeprc" = 2 ]; then
  echo "ok   crash posture: a script neither view can scan is DENIED, not admitted at exit 1"; pass=$((pass+1))
else
  echo "FAIL crash posture: a script neither view can scan exited $deeprc — only 2 blocks"; fail=$((fail+1))
fi


# Residual (c), from the closing review: an apostrophe after an OPERATOR is in a legal opener
# position, so prose that writes one still mispairs. Not a regression — it admits at BASE too — and
# it is fixtured here so the leak is recorded rather than assumed away, with its control beside it.
js "opener residual: an apostrophe after an operator still mispairs -> allow (stated residual)" 0 <<'EOF'
/* rock - 'n roll */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF

js "opener residual: control, the same line without the apostrophe -> deny" 2 <<'EOF'
/* rock - n roll */ const r = await parallel([() => agent('a'), () => agent('b')])
EOF

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]

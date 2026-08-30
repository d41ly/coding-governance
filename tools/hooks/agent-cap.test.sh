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

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]

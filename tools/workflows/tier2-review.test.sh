#!/usr/bin/env bash
# tier2-review self-test — the ARGUMENT CONTRACT only.
#
# TOOL-dTieredTribunal-11's closing review found two defects in this file's input validation and
# neither could have been caught, because the harness had no test at all. This suite covers the
# refusals that run BEFORE any agent is spawned: the spec-audit subject validator, the base-shape
# ladder, and whether the `args` header documents the fields the file actually reads.
#
# WHAT THIS DOES NOT CHECK, stated here because a structural check reads as a semantic one to
# everybody who did not write it. Nothing downstream of the refusals is exercised: no lens prompt,
# no schema, no batching, no synthesis, no report. Those need an orchestrator and live agents, and
# this suite deliberately holds none. A green run here means the harness refuses what it says it
# refuses; it says nothing about the review it produces once it accepts.
#
# HOW it reaches the code: the prelude is EXTRACTED and evaluated. A workflow script cannot be
# imported — it declares top-level `const`s against runtime globals and has no export — so the arms
# slice from the end of `meta` to the first line the validators have all run before, and evaluate
# that with stubs. The extraction is asserted live below: an extraction that silently yields nothing
# would make every arm pass by finding nothing, which is the failure class this build catalogued.

set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "tier2-review-test: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

FILE="tools/workflows/tier2-review.js"
[ -f "$FILE" ] || { echo "tier2-review-test: the subject $FILE is absent — a suite whose subject is missing must say so, not pass"; exit 2; }
command -v node >/dev/null 2>&1 || { echo "tier2-review-test: node is not on PATH, so nothing can be evaluated — refusing rather than passing"; exit 2; }

TMP="$(mktemp -d)" || exit 2
trap 'rm -rf "$TMP"' EXIT

cat > "$TMP/run.js" <<'JSEOF'
const fs = require('fs')
const FILE = process.argv[2]
const src = fs.readFileSync(FILE, 'utf8')
const lines = src.split('\n')

let pass = 0
let fail = 0
const ck = (ok, name) => { if (ok) { pass++; console.log('ok   ' + name) } else { fail++; console.log('FAIL ' + name) } }
const die = (why) => { console.log('tier2-review-test: ' + why); process.exit(2) }

// ---- extract the prelude, and PROVE the extraction moved -------------------------------------
const metaEnd = lines.findIndex((l) => l === '}')
const stop = lines.findIndex((l) => l.startsWith('const baseLooksPinned'))
if (metaEnd === -1) die('could not find the end of the `meta` block — the extraction anchor moved, and an empty body would pass every arm below')
if (stop === -1) die('could not find `const baseLooksPinned` — the extraction anchor moved, and an empty body would pass every arm below')
if (stop <= metaEnd) die('the extraction anchors are out of order (' + metaEnd + ' then ' + stop + ')')
const body = lines.slice(metaEnd + 1, stop).join('\n')
if (!/badSubject/.test(body) || !/const a = cfg/.test(body)) {
  die('the extracted prelude does not contain the validators under test — the arms would pass by finding nothing')
}
ck(true, 'the prelude extraction is live (' + (stop - metaEnd - 1) + ' lines, both validators present)')

// ---- one arm ----------------------------------------------------------------------------------
const BLOB = 'abc1234'
const base = { repo: '/tmp/r', reviewDir: 'memory/reviews', unitIds: ['TOOL-x-1'], base: 'a'.repeat(40), head: 'a'.repeat(40) }
function arm(name, extra, want) {
  let threw = null
  try {
    new Function('args', 'log', 'parallel', 'agent', 'phase', body)(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  // A harness fault is NOT a pass. Every arm below expects a refusal, and an arm that "passes"
  // because the evaluation itself blew up is the fixture that finds nothing.
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === null ? !threw : !!threw && threw.indexOf(want) !== -1, name)
}

const NOTHING = 'reviews nothing'
const SHAPE = 'needs `subjects`'

// B2 — a spec audit that resolved no subject reviews nothing and may not report a clean bill.
arm('zero subjects, round 1 -> refused', { kind: 'spec-audit', round: 1, subjects: [] }, NOTHING)
arm('zero subjects, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [] }, NOTHING)

// D6 — a FALSY offender. `find(pred) || null` used to collapse each of these onto the pass
// sentinel, so the `!x` arm of the validator could never fire. Every existing fixture supplied a
// truthy bad subject, which is why nothing caught it: the general rule is that a validator whose
// predicate has a `!x` arm needs one fixture whose offender is falsy.
for (const [label, v] of [['null', null], ['undefined', undefined], ['0', 0], ['empty string', ''], ['false', false]]) {
  arm('falsy subject [' + label + '], round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [v] }, SHAPE)
}
// ...and a real offender sitting BEHIND a falsy one was masked with them, because find returns first.
arm('falsy then genuinely bad, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [null, { path: 'a.md', blob: 'zzz' }] }, SHAPE)
arm('a non-object subject, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: ['a.md'] }, SHAPE)

// The malformed-blob ladder is UNCHANGED: warn at round 1, refuse above it. Both halves, because
// an arm asserting only the refusal is satisfied by a checker that refuses everything.
arm('malformed blob, round 1 -> warns and proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'a.md', blob: 'zzz' }] }, null)
arm('malformed blob, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [{ path: 'a.md', blob: 'zzz' }] }, SHAPE)
arm('a good subject, round 1 -> proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'a.md', blob: BLOB }] }, null)
arm('a good subject, round 2 -> proceeds', { kind: 'spec-audit', round: 2, subjects: [{ path: 'a.md', blob: BLOB }] }, null)

// The kind is a CLOSED set, and the diff-review default owes none of the above.
arm('diff-review with no subjects -> untouched', { round: 1 }, null)
arm('an unknown kind -> refused', { kind: 'code-review', round: 1 }, 'kind')

// ---- D9 — the `args` header must carry every field the file reads --------------------------------
// BUILD-METHOD M4 sends a reader to that block for the spec-audit spelling, and it named neither
// `kind` nor `subjects` when the rule was written to point at it. An omitted `kind` DEFAULTS rather
// than refusing, so a header missing the field buys the exact failure M4 exists to prevent. Scoped
// past the `const a = cfg` alias: a `chunk(a, n)` helper above it reads `a.length` off a local.
const alias = src.indexOf('\nconst a = cfg')
const hStart = src.indexOf('// --- inputs (via Workflow')
const hEnd = src.indexOf('// S5 (TOOL-aGuardedTally-1)')
if (alias === -1 || hStart === -1 || hEnd === -1 || hEnd <= hStart) {
  die('could not locate the args alias or the args header block — this arm would pass by finding nothing')
}
const hdr = src.slice(hStart, hEnd)
const fields = [...new Set([...src.slice(alias).matchAll(/\ba\.([A-Za-z_$][\w$]*)/g)].map((m) => m[1]))].sort()
if (!fields.length) die('found no fields read off the args alias — this arm would pass by finding nothing')
const missing = fields.filter((f) => !hdr.includes(f))
ck(missing.length === 0, 'the args header documents all ' + fields.length + ' fields read off `a`' + (missing.length ? ' — missing: ' + missing.join(' ') : ''))

console.log('---- ' + pass + ' passed, ' + fail + ' failed ----')
process.exit(fail ? 1 : 0)
JSEOF

node "$TMP/run.js" "$ROOT/$FILE"

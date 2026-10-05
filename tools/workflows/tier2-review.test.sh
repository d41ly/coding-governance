#!/usr/bin/env bash
# tier2-review self-test — the ARGUMENT CONTRACT, and the durability contract over stub agents.
#
# TOOL-dTieredTribunal-11's closing review found two defects in this file's input validation and
# neither could have been caught, because the harness had no test at all. This suite covers the
# refusals that run BEFORE any agent is spawned: the spec-audit subject validator, the base-shape
# ladder, the kind enum, and whether the `args` header documents the fields the file actually reads.
#
# TOOL-dDerivedDocket-29 added a SECOND half: the whole script evaluated the way its runtime does,
# the AsyncFunction shape `unattended-build.test.sh` already uses, with stub agents that RECORD each
# label, prompt and schema and return a canned value or null. It grades the resume probe, the review
# key, lens and skeptic-batch reuse, the write-before-return instruction and `path` on all three
# agent schemas, and the `exit`/`pending` contract on every death path.
#
# WHAT THIS DOES NOT CHECK, stated here because a structural check reads as a semantic one to
# everybody who did not write it. No agent is real: nothing here proves a live agent WRITES the file
# its prompt names, or that the platform validates a schema the way the stub pretends to, and the
# probe's reading of a directory is a canned return. Those are observed only by a real review, the
# build's closing review. A green run here says the script does what it says with the returns it is
# handed; it says nothing about what live agents hand it.
# Round 2 note: the first cut of this header claimed the base-shape ladder and did not reach it —
# the extraction stopped one line short. The stop anchor moved rather than the claim.
#
# HOW it reaches the code: the prelude is EXTRACTED and evaluated. A workflow script cannot be
# imported — it declares top-level `const`s against runtime globals and has no export — so the arms
# slice from the end of `meta` to the first line every validator has already run before, and
# evaluate that with stubs. The extraction is asserted live below, and the assertion count is held
# against a FLOOR: both exist because an arm block stranded past an early exit would otherwise
# shrink this suite silently, which is the one failure a self-test cannot report about itself.

set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "tier2-review-test: not inside a git repository"; exit 2; }
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "tier2-review-test: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

FILE="$KIT_REL/tier2-review.js"
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
const die = (why) => { console.log('tier2-review-test: ' + why); console.log('---- ' + pass + ' passed, ' + (fail + 1) + ' failed ----'); process.exit(2) }

// ---- extract the prelude, and PROVE the extraction moved -------------------------------------
// The stop anchor is the line after the base-shape ladder, NOT the ladder's own first line: at
// `const baseLooksPinned` the ladder is excluded and the two arms below would grade nothing.
const metaEnd = lines.findIndex((l) => l === '}')
const stop = lines.findIndex((l) => l.startsWith('const reviewDir = a.reviewDir'))
if (metaEnd === -1) die('could not find the end of the `meta` block — the extraction anchor moved, and an empty body would pass every arm below')
if (stop === -1) die('could not find `const reviewDir = a.reviewDir` — the extraction anchor moved, and an empty body would pass every arm below')
if (stop <= metaEnd) die('the extraction anchors are out of order (' + metaEnd + ' then ' + stop + ')')
const body = lines.slice(metaEnd + 1, stop).join('\n')
for (const needed of ['badSubject', 'const a = cfg', 'baseLooksPinned']) {
  if (!body.includes(needed)) die('the extracted prelude is missing `' + needed + '` — the arms would pass by finding nothing')
}
ck(true, 'the prelude extraction is live (' + (stop - metaEnd - 1) + ' lines, all three validators present)')

// ---- one arm ----------------------------------------------------------------------------------
const BLOB = 'abc1234'
const SHA = 'a'.repeat(40)
const base = { repo: '/tmp/r', reviewDir: 'memory/reviews', unitIds: ['TOOL-x-1'], base: SHA, head: SHA }
function arm(name, extra, want) {
  let threw = null
  try {
    new Function('args', 'log', 'parallel', 'agent', 'phase', body)(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  // A harness fault is NOT a pass. Most arms below expect a refusal, and an arm that "passes"
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
const MOVING = 'must be an immutable sha'

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

// The base-shape LADDER, which this suite claimed before it reached it. Same shape as the subject
// ladder: warn at round 1, refuse above it — and a spec audit short-circuits it entirely, because
// a spec has no commit range and its anchor is the per-subject blob instead.
arm('a moving ref as base, round 1 -> warns and proceeds', { round: 1, base: 'origin/main' }, null)
arm('a moving ref as base, round 2 -> refused', { round: 2, base: 'origin/main' }, MOVING)
arm('a spec audit ignores base entirely', { kind: 'spec-audit', round: 2, base: 'origin/main', subjects: [{ path: 'a.md', blob: BLOB }] }, null)

// ---- TOOL-aSightedSkeptic-7 AC1 — `intensity`, a closed set read in the prelude ----------------------
// The proceeding arms also read the RESOLVED value back, so they cannot pass over a prelude that never
// reads `intensity`: on the parent the read throws `intensity is not defined`, a harness fault.
function armIntensity(name, extra, want) {
  let got = null
  let threw = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn intensity')(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === 'refused' ? !!threw && threw.indexOf('intensity') !== -1 : !threw && got === want, name + (threw ? ' (threw: ' + threw + ')' : ' (resolved ' + JSON.stringify(got) + ')'))
}
const GOOD_SPEC = { kind: 'spec-audit', round: 1, subjects: [{ path: 'a.md', blob: BLOB }] }
armIntensity('intensity: an unknown value is refused', { intensity: 'medium' }, 'refused')
armIntensity('intensity: a non-string is refused', { intensity: 7 }, 'refused')
armIntensity('intensity: light on a diff review proceeds', { intensity: 'light' }, 'light')
armIntensity('intensity: absent proceeds', {}, 'full')
armIntensity('intensity: light on a spec audit is refused', Object.assign({ intensity: 'light' }, GOOD_SPEC), 'refused')
armIntensity('intensity: full on a spec audit proceeds', Object.assign({ intensity: 'full' }, GOOD_SPEC), 'full')

// ---- D9 — the `args` header must carry every field the file reads --------------------------------
// BUILD-METHOD M4 sends a reader to that block for the spec-audit spelling, and it named neither
// `kind` nor `subjects` when the rule was written to point at it. An omitted `kind` DEFAULTS rather
// than refusing, so a header missing the field buys the exact failure M4 exists to prevent. Scoped
// past the `const a = cfg` alias: a `chunk(a, n)` helper above it reads `a.length` off a local.
//
// ROUND 2: this arm first tested `hdr.includes(f)`, which the D9 PROSE in the same window satisfied
// — deleting the two documentation lines left it green. A field is DOCUMENTED only where it is
// written as a `name:` key, which is the shape the block actually uses and prose does not.
const alias = src.indexOf('\nconst a = cfg')
const hStart = src.indexOf('// --- inputs (via Workflow')
const hEnd = src.indexOf('// S5 (TOOL-aGuardedTally-1)')
if (alias === -1 || hStart === -1 || hEnd === -1 || hEnd <= hStart) {
  die('could not locate the args alias or the args header block — this arm would pass by finding nothing')
}
const hdr = src.slice(hStart, hEnd)
const fields = [...new Set([...src.slice(alias).matchAll(/\ba\.([A-Za-z_$][\w$]*)/g)].map((m) => m[1]))].sort()
if (!fields.length) die('found no fields read off the args alias — this arm would pass by finding nothing')
const missing = fields.filter((f) => !new RegExp('(^|[^\\w$])' + f + '\\s*:').test(hdr))
ck(missing.length === 0, 'the args header documents all ' + fields.length + ' fields read off `a` as `name:` keys' + (missing.length ? ' — missing: ' + missing.join(' ') : ''))

// ==== TOOL-dDerivedDocket-29 — THE WHOLE SCRIPT, over stub agents ==================================
// The runner evaluates the file as the Workflow runtime does. Each stub is looked up by exact label
// first and then by the longest label prefix; a function stub is called with (label, prompt), and an
// absent or null one returns null, which is how a dead agent reaches a script. Every return is a
// deep copy, so no arm can mutate another's fixture through the harness.
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
const whole = src.replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =')
function resolveStub(stubs, label) {
  if (Object.prototype.hasOwnProperty.call(stubs, label)) return stubs[label]
  let best = null
  for (const k of Object.keys(stubs)) if (label.indexOf(k) === 0 && (best === null || k.length > best.length)) best = k
  return best === null ? undefined : stubs[best]
}
// `source` evaluates a REWRITTEN script instead of the file; only the review-shape arm passes one.
async function runReview(args, stubs, source) {
  const trace = []
  const logs = []
  const agent = async (prompt, opts) => {
    const label = (opts && opts.label) || '(unlabelled)'
    trace.push({ label: label, prompt: String(prompt), schema: opts && opts.schema })
    let v = resolveStub(stubs, label)
    if (typeof v === 'function') v = v(label, String(prompt))
    return v === undefined || v === null ? null : JSON.parse(JSON.stringify(v))
  }
  const parallel = async (thunks) => Promise.all(thunks.map((t) => t()))
  let result = null
  let threw = null
  try {
    result = await new AsyncFunction('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'workflow', source || whole)(
      args, agent, parallel, async () => [], () => {}, (m) => logs.push(String(m)), {}, async () => ({}))
  } catch (e) { threw = e.message }
  const scanSpawned = (p) => trace.filter((t) => t.label.indexOf(p) === 0).map((t) => t.label)
  return { trace: trace, logs: logs, result: result, threw: threw, scanSpawned: scanSpawned }
}

const B = 'b'.repeat(40)
const H = 'c'.repeat(40)
const DIFF = { repo: '/tmp/r', base: B, head: H, round: 1, context: 'ctx', reviewDir: 'memory/reviews' }
const SPEC = { repo: '/tmp/r', kind: 'spec-audit', round: 1, context: 'ctx', subjects: [{ path: 's.md', blob: 'abc1234' }] }
const buildProbe = (finds, verifies, base, head) => ({ commonDir: '/cd', base: base || B, head: head || H, finds: finds || [], verifies: verifies || [] })
// One finding per lens, so five lenses make five ids and five batches of one: verify:ids-1-1 .. 5-5.
const buildLensReturn = (label) => {
  const lens = label.slice('find:'.length)
  return { lens: lens, path: '/cd/review-lenses/k/find-' + lens + '.json', findings: [{ file: lens + '.js', line: 1, where: 'section 1', severity: 'high', claim: lens + ' claim', impact: 'i', fix: 'f' }] }
}
const buildEmptyLens = (label) => ({ lens: label.slice('find:'.length), path: '/p', findings: [] })
const buildVerdicts = (verdict) => (label, prompt) => {
  const m = /ids ([0-9, ]+)\)/.exec(prompt)
  const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
  return { path: '/cd/v.json', verdicts: ids.map((id) => ({ id: id, verdict: verdict, reason: 'r' })) }
}
// The synthesis places every CONFIRMED id in one item unless told to drop one.
const buildSynth = (drop) => (label, prompt) => {
  const head = prompt.split('UNVERIFIED findings')[0]
  const ids = [...head.matchAll(/id=(\d+) \[/g)].map((x) => parseInt(x[1], 10)).filter((id) => id !== drop)
  return { path: 'memory/reviews/r.md', summary: 's', items: [{ severity: 'HIGH', ids: ids }] }
}
const ALL_OK = { 'resume:probe': buildProbe(), 'find:': buildLensReturn, 'verify:': buildVerdicts('confirmed'), synth: buildSynth(null) }
const buildStubs = (over) => Object.assign({}, ALL_OK, over)
const checkNoThrow = (r, name) => { if (r.threw) { console.log('HARNESS-BROKEN ' + name + ' -> ' + r.threw); fail++; return false } return true }
// A lens FILE as the probe would re-emit it, under a given key.
const buildLensFile = (lens, key) => Object.assign({ name: 'find-' + lens + '.json', key: key }, buildLensReturn('find:' + lens))

async function runWholeScriptArms() {
  // ---- the passing case first: every agent returns, the exit is complete and pending is empty.
  let r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'complete run')) {
    ck(r.result.exit === 'complete' && Array.isArray(r.result.pending) && r.result.pending.length === 0 && Number.isInteger(r.result.blockers),
      'a run where every agent returned exits complete, with no pending label and an integer blocker count')
    ck(typeof r.result.key === 'string' && r.result.key.indexOf('diff-review-r1-' + B.slice(0, 12) + '-' + H.slice(0, 12) + '-') === 0,
      'the diff-review key is kind, round and the RESOLVED base and head, then the input print: ' + r.result.key)
    ck(r.trace[0] && r.trace[0].label === 'resume:probe', 'the resume probe is the first agent, before any lens')
  }
  const K = r.result ? r.result.key : ''

  // ---- AC1: every find: prompt and every verify: prompt NAMES its file under review-lenses/, and
  // ---- all three agent schemas REQUIRE path. The skeptic half is read too, which is the half a
  // ---- lens-only check would leave ungraded.
  const finds = r.trace.filter((t) => t.label.indexOf('find:') === 0)
  const verifies = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
  ck(finds.length === 5 && finds.every((t) => t.prompt.indexOf('/review-lenses/' + K + '/find-' + t.label.slice(5) + '.json') !== -1),
    'AC1 every find: prompt names review-lenses/<key>/find-<lens>.json')
  ck(verifies.length === 5 && verifies.every((t) => {
    const m = /^verify:ids-(\d+)-(\d+)$/.exec(t.label)
    return m && t.prompt.indexOf('/review-lenses/' + K + '/verify-' + m[1] + '-' + m[2] + '.json') !== -1
  }), 'AC1 every verify: prompt names review-lenses/<key>/verify-<first id>-<last id>.json')
  ck(finds.every((t) => t.prompt.indexOf('BEFORE you return') !== -1) && verifies.every((t) => t.prompt.indexOf('BEFORE you return') !== -1),
    'AC1 both prompt kinds order the write BEFORE the return')
  ck(finds.every((t) => t.schema && t.schema.required.indexOf('path') !== -1), 'AC1 the diff finding schema lists path in required')
  ck(verifies.every((t) => t.schema && t.schema.required.indexOf('path') !== -1), 'AC1 the verdict schema lists path in required')
  const rs = await runReview(SPEC, ALL_OK)
  if (checkNoThrow(rs, 'spec-audit complete run')) {
    const sf = rs.trace.filter((t) => t.label.indexOf('find:') === 0)
    // `where` is read off the ITEM schema, which is where the spec kind requires it (TOOL-dTieredTribunal-11
    // S3); it is what tells this schema from the diff one. The first cut read it off the top-level
    // `required`, which holds lens, path and findings on both kinds, so this arm could never pass.
    const extractItemRequired = (t) => {
      const items = t.schema && t.schema.properties && t.schema.properties.findings && t.schema.properties.findings.items
      return (items && items.required) || []
    }
    ck(sf.length === 4 && sf.every((t) => t.schema && t.schema.required.indexOf('path') !== -1 && extractItemRequired(t).indexOf('where') !== -1 &&
      t.prompt.indexOf('/review-lenses/' + rs.result.key + '/find-' + t.label.slice(5) + '.json') !== -1),
      'AC1 the spec finding schema lists path in required, and every spec lens prompt names its file')
  }

  // ---- AC4: a DEAD probe reuses nothing, dispatches every lens and says so.
  r = await runReview(DIFF, buildStubs({ 'resume:probe': null }))
  if (checkNoThrow(r, 'dead probe')) {
    ck(r.scanSpawned('find:').length === 5, 'AC4 a dead probe dispatches all five lenses')
    ck(r.logs.some((l) => l.indexOf('nothing could be reused') !== -1), 'AC4 ...and the log says nothing could be reused')
  }

  // ---- AC2: two lenses die; the re-run is fed the three survivors' files and dispatches exactly two.
  r = await runReview(DIFF, buildStubs({ 'find:seams': null, 'find:intent': null }))
  let k2 = ''
  if (checkNoThrow(r, 'two dead lenses')) {
    k2 = r.result.key
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:seams find:intent',
      'AC2 the first run defers, pending the two dead lenses')
  }
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe([buildLensFile('security', k2), buildLensFile('correctness', k2), buildLensFile('verification', k2)]) }))
  if (checkNoThrow(r, 'two-survivor re-run')) {
    ck(r.scanSpawned('find:').join(' ') === 'find:seams find:intent', 'AC2 the re-run with identical args spawns exactly the two missing lenses: ' + r.scanSpawned('find:').join(' '))
    ck(r.result.exit === 'complete' && r.result.lensesReused === 3, 'AC2 ...and completes, reporting three lenses reused')
  }

  // ---- AC3: a file whose key differs in ONE component is dispatched; the variant's own key is
  // ---- reused. Both halves per component: a stale-key arm alone passes over a harness that
  // ---- reuses nothing at all.
  const variants = [
    ['another round', Object.assign({}, DIFF, { round: 2 }), null],
    ['another head sha', DIFF, buildProbe([], [], B, 'd'.repeat(40))],
    ['another resolved base sha', DIFF, buildProbe([], [], 'e'.repeat(40), H)],
    ['another context', Object.assign({}, DIFF, { context: 'ctx2' }), null],
    ['another byDesign', Object.assign({}, DIFF, { byDesign: 'bd2' }), null],
    ['another priorFindings', Object.assign({}, DIFF, { priorFindings: [{ ref: 'a:1', claim: 'c' }] }), null],
    ['another lensNotes', Object.assign({}, DIFF, { lensNotes: { security: 'n2' } }), null],
    ['another specs', Object.assign({}, DIFF, { specs: ['x.md'] }), null],
    ['another checklist', Object.assign({}, DIFF, { checklist: ['a class'] }), null],
  ]
  for (const [what, args, probe] of variants) {
    const own = await runReview(args, buildStubs(probe ? { 'resume:probe': probe } : {}))
    if (!checkNoThrow(own, 'AC3 ' + what)) continue
    const stale = await runReview(args, buildStubs({ 'resume:probe': Object.assign({}, probe || buildProbe(), { finds: [buildLensFile('security', K)] }) }))
    const fresh = await runReview(args, buildStubs({ 'resume:probe': Object.assign({}, probe || buildProbe(), { finds: [buildLensFile('security', own.result.key)] }) }))
    if (!checkNoThrow(stale, 'AC3 stale ' + what) || !checkNoThrow(fresh, 'AC3 fresh ' + what)) continue
    ck(own.result.key !== K && stale.scanSpawned('find:security').length === 1,
      'AC3 ' + what + ': a lens file under the old key is dispatched')
    ck(fresh.scanSpawned('find:security').length === 0, 'AC3 ' + what + ': ...and one under its own key is reused')
  }
  const s1 = await runReview(SPEC, ALL_OK)
  const specMoved = Object.assign({}, SPEC, { subjects: [{ path: 's.md', blob: 'abc1235' }] })
  const s2 = await runReview(specMoved, buildStubs({ 'resume:probe': buildProbe([buildLensFile('prior-art', s1.result ? s1.result.key : '')]) }))
  if (checkNoThrow(s1, 'AC3 spec base') && checkNoThrow(s2, 'AC3 spec moved')) {
    ck(s2.result.key !== s1.result.key && s2.scanSpawned('find:prior-art').length === 1,
      'AC3 one spec-audit subject blob moved: the lens file under the old key is dispatched')
  }
  // The key is compared to the FILE's own key field, never to the name alone.
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe([Object.assign(buildLensFile('security', K), { key: K + 'x' })]) }))
  if (checkNoThrow(r, 'AC3 name matches, key does not')) ck(r.scanSpawned('find:security').length === 1, 'AC3 a file with the right name and a different key field is dispatched')

  // ---- AC5: a verify file is reused ONLY with the right key AND the right claim print.
  const allLensFiles = ['security', 'correctness', 'seams', 'verification', 'intent'].map((l) => buildLensFile(l, K))
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(allLensFiles) }))
  let print = ''
  if (checkNoThrow(r, 'AC5 print capture')) {
    ck(r.scanSpawned('find:').length === 0, 'AC5 with every lens file present no lens is dispatched')
    const v1 = r.trace.find((t) => t.label === 'verify:ids-1-1')
    const m = v1 ? /"batch":"([0-9a-f]{8})"/.exec(v1.prompt) : null
    print = m ? m[1] : ''
    ck(print.length === 8, 'AC5 the verify prompt names the batch print the file must carry')
  }
  const vfile = (batch) => ({ name: 'verify-1-1.json', key: K, batch: batch, path: '/cd/v.json', verdicts: [{ id: 1, verdict: 'confirmed', reason: 'r' }] })
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(allLensFiles, [vfile(print)]) }))
  if (checkNoThrow(r, 'AC5 matching print')) ck(r.scanSpawned('verify:ids-1-1').length === 0 && r.result.batchesReused === 1, 'AC5 a verify file with the key and the matching print is reused')
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(allLensFiles, [vfile('0badf00d')]) }))
  if (checkNoThrow(r, 'AC5 other print')) ck(r.scanSpawned('verify:ids-1-1').length === 1, 'AC5 the right ids over a print of other claims is dispatched')

  // ---- AC6: the three lens-stage death paths all defer and none reads clean or partial.
  r = await runReview(DIFF, buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'AC6 all lenses dead')) {
    ck(r.result.exit === 'deferred-platform' && r.result.blockers === null && r.result.pending.length === 5 &&
      r.result.pending.every((p) => p.indexOf('find:') === 0), 'AC6 every lens dead: deferred-platform, blockers null, five find: labels pending')
  }
  r = await runReview(DIFF, buildStubs({ 'find:': buildEmptyLens, 'find:security': null, 'find:seams': null }))
  if (checkNoThrow(r, 'AC6 two dead, survivors empty')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:security find:seams' && !/^(clean|partial)/.test(r.result.note),
      'AC6 two lenses dead and the survivors found nothing: deferred, those two pending, a note that is neither clean nor partial')
  }
  r = await runReview(DIFF, buildStubs({ 'find:intent': null, 'verify:': buildVerdicts('refuted') }))
  if (checkNoThrow(r, 'AC6 one dead, all refuted')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:intent' && !/^(clean|partial)/.test(r.result.note),
      'AC6 one lens dead and every finding refuted: deferred')
  }
  r = await runReview(DIFF, buildStubs({ 'find:': buildEmptyLens }))
  if (checkNoThrow(r, 'AC6 control')) ck(r.result.exit === 'complete' && r.result.note === 'clean: 0 findings', 'AC6 control: no death and nothing found is complete and clean')

  // ---- AC7: a dead skeptic batch defers WITHOUT a synthesis; a dead synthesis defers; the tally
  // ---- fault stays complete beside a null count.
  r = await runReview(DIFF, buildStubs({ 'verify:ids-2-2': null }))
  if (checkNoThrow(r, 'AC7 dead batch')) {
    ck(r.result.exit === 'deferred-platform' && r.result.blockers === null && r.result.pending.join(' ') === 'verify:ids-2-2',
      'AC7 one skeptic batch dead: deferred, blockers null, that batch pending')
    ck(r.scanSpawned('synth').length === 0, 'AC7 ...and no synthesis runs over the half-judged set')
  }
  r = await runReview(DIFF, buildStubs({ synth: null }))
  if (checkNoThrow(r, 'AC7 dead synthesis')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'synth', 'AC7 a dead synthesis: deferred, synth pending')
  }
  r = await runReview(DIFF, buildStubs({ synth: buildSynth(3) }))
  if (checkNoThrow(r, 'AC7 tally fault')) {
    ck(r.result.exit === 'complete' && r.result.blockers === null, 'AC7 a synthesis leaving one confirmed id out: complete beside blockers null')
  }

  // ==== TOOL-aSightedSkeptic-5 — five diff lenses, `lensNotes`, and the review-shape bump ===========
  // ---- AC1: the lens set and its ORDER, read off what a complete run actually spawns.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'five-lens run')) {
    ck(r.scanSpawned('find:').join(' ') === 'find:security find:correctness find:seams find:verification find:intent',
      'the diff lens set is security correctness seams verification intent: ' + r.scanSpawned('find:').join(' '))
  }

  // ---- AC3: a note reaches its OWN lens and no other prompt. The count of five is asserted beside
  // ---- the absence, so "no other prompt carries it" cannot pass over a run that spawned fewer lenses.
  r = await runReview(Object.assign({}, DIFF, { lensNotes: { verification: 'NOTE-MARK' } }), ALL_OK)
  if (checkNoThrow(r, 'lensNotes placement')) {
    const nf = r.trace.filter((t) => t.label.indexOf('find:') === 0)
    const nv = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
    ck(nf.some((t) => t.label === 'find:verification' && t.prompt.indexOf('NOTE-MARK') !== -1),
      'a lensNotes entry reaches its own lens prompt and no other: find:verification carries the note')
    ck(nf.length === 5 && nv.length > 0 && nf.concat(nv).every((t) => t.label === 'find:verification' || t.prompt.indexOf('NOTE-MARK') === -1),
      'a lensNotes entry reaches its own lens prompt and no other: the other four find: and every verify: prompt do not')
  }

  // ---- AC4: six malformed values refuse BEFORE any agent spawns, naming the field and the legal
  // ---- keys of the run's own kind; the control is a legal spec-kind key, which proceeds.
  const DIFF_KEYS = 'security | correctness | seams | verification | intent'
  const SPEC_KEYS = 'underspecification | contradiction | unstated-assumption | prior-art'
  const malformed = [
    ['a string', DIFF, 'note', DIFF_KEYS],
    ['an array', DIFF, ['security'], DIFF_KEYS],
    ['null', DIFF, null, DIFF_KEYS],
    // The retired key is spelled by concatenation, so this file keeps no literal of it (spec AC7).
    ['the retired key on a diff review', DIFF, { ['regress' + 'ions']: 'n' }, DIFF_KEYS],
    ['a diff key on a spec audit', SPEC, { verification: 'n' }, SPEC_KEYS],
    ['an empty note', DIFF, { security: '' }, DIFF_KEYS],
  ]
  for (const [what, args, notes, keys] of malformed) {
    r = await runReview(Object.assign({}, args, { lensNotes: notes }), ALL_OK)
    ck(typeof r.threw === 'string' && r.threw.indexOf('lensNotes') !== -1 && r.threw.indexOf(keys) !== -1 && r.trace.length === 0,
      'a malformed lensNotes refuses before any agent spawns: ' + what + (r.threw ? '' : ' (accepted)'))
  }
  r = await runReview(Object.assign({}, SPEC, { lensNotes: { 'prior-art': 'n' } }), ALL_OK)
  ck(!r.threw && r.result && r.result.exit === 'complete' && r.scanSpawned('find:').length === 4,
    'a malformed lensNotes refuses before any agent spawns: control, a spec-kind key on a spec audit, proceeds')

  // ---- AC5: the absence is ANNOUNCED in the log and in RUN INTEGRITY; a supplied note silences the
  // ---- warning and is named instead.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'absent lensNotes')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('lensNotes') !== -1) && !!sp && sp.prompt.indexOf('lens notes: none supplied') !== -1,
      'absent lensNotes is announced in the log and in RUN INTEGRITY')
  }
  r = await runReview(Object.assign({}, DIFF, { lensNotes: { security: 'n' } }), ALL_OK)
  if (checkNoThrow(r, 'supplied lensNotes')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(!r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('lensNotes') !== -1) && !!sp && sp.prompt.indexOf('lens notes supplied for: security') !== -1,
      'absent lensNotes is announced in the log and in RUN INTEGRITY: a supplied note logs no warning and is named there')
  }

  // ---- AC6: a lens file written under ANOTHER review shape is dispatched. The literal is rewritten
  // ---- in a copy of the script, and the rewrite is asserted to have TAKEN before its key is used:
  // ---- a replace that matched nothing would evaluate the same script and prove nothing.
  const shapeRe = /const REVIEW_SHAPE = '([^']*)'/
  const shifted = whole.replace(shapeRe, (m, v) => "const REVIEW_SHAPE = '" + v + "-older'")
  r = await runReview(DIFF, ALL_OK, shifted)
  const KS = r.result ? r.result.key : ''
  ck(shapeRe.test(whole) && shifted !== whole && !r.threw && KS !== '' && KS !== K,
    'a lens file written under another review shape is dispatched: the rewrite took and the keys differ')
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe([buildLensFile('security', KS)]) }))
  if (checkNoThrow(r, 'review shape stale')) ck(KS !== K && r.scanSpawned('find:security').length === 1,
    'a lens file written under another review shape is dispatched: find:security under the older shape is dispatched')
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe([buildLensFile('security', K)]) }))
  if (checkNoThrow(r, 'review shape fresh')) ck(r.scanSpawned('find:security').length === 0,
    'a lens file written under another review shape is dispatched: ...and one under the real key is reused')

  // ==== TOOL-aSightedSkeptic-1 — renderBrief(role) opens every finder AND every skeptic prompt =======
  // Every arm asserts a non-zero prompt count beside its every(), so none passes over a run that
  // spawned nothing. Each is RED against the parent render, whose skeptic prompt carries no brief.
  const scanPrompts = (run, prefix) => run.trace.filter((t) => t.label.indexOf(prefix) === 0)
  r = await runReview(Object.assign({}, DIFF, { context: 'CTX-MARK', byDesign: 'BD-MARK' }), ALL_OK)
  if (checkNoThrow(r, 'briefed skeptic')) {
    const bv = scanPrompts(r, 'verify:')
    ck(bv.length === 5 && bv.every((t) => t.prompt.indexOf('REPO: /tmp/r') !== -1 && t.prompt.indexOf('git -C /tmp/r diff ' + B + '...' + H) !== -1 &&
      t.prompt.indexOf('CTX-MARK') !== -1 && t.prompt.indexOf('BD-MARK') !== -1),
      'a skeptic prompt carries the repo, the range, the context and the by-design list')
  }
  for (const [what, args] of [['diff', DIFF], ['spec', SPEC]]) {
    r = await runReview(args, ALL_OK)
    if (!checkNoThrow(r, 'shared brief ' + what)) continue
    const bf = scanPrompts(r, 'find:')
    const bp = bf.concat(scanPrompts(r, 'verify:'))
    const ctxLines = new Set(bp.map((t) => t.prompt.split('\n').find((l) => l.indexOf('CONTEXT: ') === 0) || '(no CONTEXT line)'))
    ck(bf.length > 0 && bp.length > bf.length && bp.every((t) => t.prompt.indexOf('REPO: /tmp/r') === 0) && ctxLines.size === 1 && !ctxLines.has('(no CONTEXT line)'),
      'every finder and skeptic prompt opens with the shared brief: ' + what + ' run, ' + bp.length + ' prompts, ' + ctxLines.size + ' distinct CONTEXT line(s)')
  }
  r = await runReview(DIFF, ALL_OK)
  const rsp = await runReview(SPEC, ALL_OK)
  if (checkNoThrow(r, 'pre-existing diff') && checkNoThrow(rsp, 'pre-existing spec')) {
    const dv = scanPrompts(r, 'verify:')
    const sv = scanPrompts(rsp, 'verify:')
    ck(dv.length === 5 && dv.every((t) => t.prompt.indexOf('PRE-EXISTING') !== -1 && t.prompt.indexOf('refute any finding one of these covers') !== -1) &&
      scanPrompts(r, 'find:').length === 5 && scanPrompts(r, 'find:').every((t) => t.prompt.indexOf('PRE-EXISTING') === -1) &&
      sv.length === 4 && sv.every((t) => t.prompt.indexOf('PRE-EXISTING') === -1),
      'a diff skeptic is told to refute a pre-existing defect and a by-design one')
    ck(sv.every((t) => t.prompt.indexOf('/tmp/r') !== -1 && t.prompt.indexOf('s.md') !== -1 && t.prompt.indexOf('abc1234') !== -1) && sv.length === 4,
      'a spec-audit skeptic prompt names the repo and every subject at its blob')
  }
  r = await runReview(Object.assign({}, DIFF, { round: 2, priorFindings: [{ ref: 'p.js:9', claim: 'PRIOR-MARK' }] }), ALL_OK)
  if (checkNoThrow(r, 'fold-round brief')) {
    const fv = scanPrompts(r, 'verify:')
    const ff = scanPrompts(r, 'find:')
    ck(fv.length === 5 && fv.every((t) => t.prompt.indexOf('PRIOR-MARK') !== -1 && t.prompt.indexOf('refuted as a duplicate') !== -1),
      'a fold-round skeptic is shown the prior round\'s findings: every verify: prompt carries PRIOR-MARK and the duplicate rule')
    ck(ff.length === 5 && ff.every((t) => t.prompt.indexOf('PRIOR-MARK') !== -1 && t.prompt.indexOf('Judge the FIX') !== -1),
      'a fold-round skeptic is shown the prior round\'s findings: ...and every find: prompt still carries PRIOR-MARK and Judge the FIX')
  }

  // ==== TOOL-aSightedSkeptic-3 — `specs`, and the range's commit messages, reach every reader ========
  // Every arm is RED against the parent render, which reads no `specs` and names no commit log.
  // ---- AC1: both paths and the INTENT block in every finder AND skeptic prompt.
  r = await runReview(Object.assign({}, DIFF, { specs: ['a.md', 'b.md'] }), ALL_OK)
  if (checkNoThrow(r, 'specs reach every prompt')) {
    const ip = scanPrompts(r, 'find:').concat(scanPrompts(r, 'verify:'))
    ck(ip.length === 10 && ip.every((t) => t.prompt.indexOf('INTENT') !== -1 && t.prompt.indexOf('  - a.md') !== -1 && t.prompt.indexOf('  - b.md') !== -1),
      'specs reach every finder and skeptic prompt: ' + ip.length + ' prompts')
  }
  // ---- AC2: no specs - the commit log over the RESOLVED shas. The base is handed as an abbreviation
  // ---- and the head as a ref, so a command built from the refs as given cannot match.
  r = await runReview(Object.assign({}, DIFF, { base: 'bbbbbbb', head: 'HEAD' }), ALL_OK)
  if (checkNoThrow(r, 'commit log default')) {
    const lf = scanPrompts(r, 'find:')
    ck(lf.length === 5 && lf.every((t) => t.prompt.indexOf('log --format=%B ' + B + '..' + H) !== -1 && t.prompt.indexOf('these are the statement of intent') !== -1),
      'no specs: every diff finder is handed the commit log over the resolved shas')
  }
  // ---- AC3: neither context nor specs is announced twice; the control supplies specs.
  const NOCTX = Object.assign({}, DIFF)
  delete NOCTX.context
  r = await runReview(NOCTX, ALL_OK)
  if (checkNoThrow(r, 'no intent')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('`specs`') !== -1 && l.indexOf('`context`') !== -1) && /Intent: NEITHER/.test(ri),
      'no specs and no context: announced in the log and RUN INTEGRITY')
  }
  r = await runReview(Object.assign({}, NOCTX, { specs: ['a.md', 'b.md'] }), ALL_OK)
  if (checkNoThrow(r, 'intent supplied')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(!r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('`specs`') !== -1) && !!sp && sp.prompt.indexOf('Intent: 2 spec document(s)') !== -1,
      'specs supplied: no intent warning, and RUN INTEGRITY counts the two documents')
  }
  // ---- AC4: each malformed value refuses before any agent, naming the field.
  const refusedSpecs = [['not an array', 'a.md'], ['a non-string member', [7]], ['an empty member', ['']], ['a leading slash', ['/abs.md']],
    ['a drive letter', ['C:/x.md']], ['a .. segment', ['a/../b.md']], ['a backslash', ['a\\b.md']], ['null', null],
    // Closing review round 1, L1: a home-relative path, and a newline that would forge a brief line.
    ['a leading tilde', ['~/x.md']], ['a control character', ['a\nb.md']]]
  for (const [what, v] of refusedSpecs) {
    r = await runReview(Object.assign({}, DIFF, { specs: v }), ALL_OK)
    ck(typeof r.threw === 'string' && r.threw.indexOf('`specs`') !== -1 && r.trace.length === 0,
      'specs refused before any agent: ' + what + (r.threw ? '' : ' (accepted)'))
  }
  // ---- AC5: on a spec audit, `specs` is sibling context and may not name a subject.
  r = await runReview(Object.assign({}, SPEC, { specs: ['s.md'] }), ALL_OK)
  ck(typeof r.threw === 'string' && r.threw.indexOf('`specs`') !== -1 && r.trace.length === 0,
    'spec-audit: a spec that is also a subject is refused')
  r = await runReview(Object.assign({}, SPEC, { specs: ['overview.md'] }), ALL_OK)
  if (checkNoThrow(r, 'spec sibling context')) {
    const sf = scanPrompts(r, 'find:')
    ck(sf.length === 4 && sf.every((t) => t.prompt.indexOf('SIBLING CONTEXT') !== -1 && t.prompt.indexOf('  - overview.md') !== -1 && t.prompt.indexOf('log --format=%B') === -1),
      'spec-audit: specs render as sibling context')
  }

  // ==== TOOL-aSightedSkeptic-4 — `checklist`, split round-robin over the lenses of the run's kind =====
  // Every arm is RED against the parent render, which reads no `checklist`: no prompt carries an item,
  // no line is logged, nothing refuses. Item names and descriptions are unique tokens, so "occurs
  // exactly once" counts the item and never a neighbour that contains it.
  const CL_N = 7
  const clName = (n) => 'CLA' + n + 'X'
  const clDesc = (n) => 'DSC' + n + 'X'
  const countIn = (s, needle) => s.split(needle).length - 1
  const CL_LINES = []
  for (let n = 1; n <= CL_N; n++) CL_LINES.push('- [ ] ' + clName(n) + '\n    ' + clDesc(n) + '\n    memory/gotchas/c' + n + '.md')
  const CL_STR = '# PRE-ONE header\n# PRE-TWO header\n\n' + CL_LINES.join('\n\n') + '\n'
  const CL_ARR = []
  for (let n = 1; n <= CL_N; n++) CL_ARR.push(clName(n) + ': ' + clDesc(n))
  // Item n is in exactly ONE find: prompt, once, labelled C<n>, with its description beside it, and
  // that prompt is the lens at (n - 1) % K in lens order.
  const scanSplit = (run, keys) => {
    const fp = scanPrompts(run, 'find:')
    if (fp.length !== keys.length) return false
    for (let n = 1; n <= CL_N; n++) {
      const holders = fp.filter((t) => t.prompt.indexOf(clName(n)) !== -1)
      if (holders.length !== 1 || countIn(holders[0].prompt, clName(n)) !== 1) return false
      if (holders[0].label !== 'find:' + keys[(n - 1) % keys.length]) return false
      if (!new RegExp('(^|\\n)C' + n + ' (\\[ \\] )?' + clName(n)).test(holders[0].prompt)) return false
      if (holders[0].prompt.indexOf(clDesc(n)) === -1) return false
    }
    return true
  }
  const DIFF_ORDER = ['security', 'correctness', 'seams', 'verification', 'intent']
  const SPEC_ORDER = ['underspecification', 'contradiction', 'unstated-assumption', 'prior-art']
  // ---- AC1: a string checklist, preamble and seven items.
  const rcl = await runReview(Object.assign({}, DIFF, { checklist: CL_STR }), ALL_OK)
  if (checkNoThrow(rcl, 'checklist string')) {
    const fp = scanPrompts(rcl, 'find:')
    const vp = scanPrompts(rcl, 'verify:')
    ck(scanSplit(rcl, DIFF_ORDER) && fp.every((t) => t.prompt.indexOf('PRE-ONE') !== -1 && t.prompt.indexOf('PRE-TWO') !== -1 &&
      t.prompt.indexOf('Begin such a finding\'s claim with its C<n> label') !== -1) &&
      vp.length === 5 && vp.every((t) => t.prompt.indexOf('CLA') === -1 && t.prompt.indexOf('DSC') === -1 && t.prompt.indexOf('CHECKLIST') === -1),
      'checklist string: every item in exactly one finder prompt')
  }
  // ---- AC2: a CRLF twin splits identically and keys identically; an array is one item per element.
  const rcr = await runReview(Object.assign({}, DIFF, { checklist: CL_STR.replace(/\n/g, '\r\n') }), ALL_OK)
  if (checkNoThrow(rcr, 'checklist CRLF') && rcl.result) {
    ck(scanSplit(rcr, DIFF_ORDER) && rcr.result.key === rcl.result.key,
      'checklist string: continuation lines stay with their item')
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: CL_ARR }), ALL_OK)
  if (checkNoThrow(r, 'checklist array')) {
    const fp = scanPrompts(r, 'find:')
    ck(scanSplit(r, DIFF_ORDER) && fp.every((t) => t.prompt.indexOf('CHECKLIST') !== -1 && t.prompt.indexOf('PRE-ONE') === -1),
      'checklist array: each element is one item')
  }
  // ---- Closing review round 1, L5: a line NOT indented still continues the item above it, and the
  // ---- refusal's rule text says so. Item 1 is the security lens's share.
  r = await runReview(Object.assign({}, DIFF, { checklist: '- CLAQ1X\nTRAILQX\n- CLAQ2X' }), ALL_OK)
  const rrule = await runReview(Object.assign({}, DIFF, { checklist: 'no item line here' }), ALL_OK)
  if (checkNoThrow(r, 'checklist unindented continuation')) {
    const fp = scanPrompts(r, 'find:')
    ck(fp.length === 5 && fp.filter((t) => t.prompt.indexOf('TRAILQX') !== -1).map((t) => t.label).join(' ') === 'find:security' &&
      /(^|\n)C1 CLAQ1X\nTRAILQX/.test(fp[0].prompt) && typeof rrule.threw === 'string' &&
      rrule.threw.indexOf('every later line not starting "- " continues the item above it, indented or not') !== -1,
      'checklist string: a line not starting "- " continues its item, indented or not')
  }
  // ---- AC3: the assignment is recoverable from the log and RUN INTEGRITY; an empty share is said.
  if (rcl.result) {
    const cl = rcl.logs.filter((l) => l.indexOf('checklist:') === 0)
    const sp = rcl.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(cl.length === 1 && / — security C1 C6; correctness C2 C7; seams C3; verification C4; intent C5$/.test(cl[0]) &&
      ri.indexOf('Checklist: 7 item(s)') !== -1,
      'checklist: the log names every lens\'s share')
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: ['one', 'two', 'three'] }), ALL_OK)
  if (checkNoThrow(r, 'checklist three items')) {
    const none = scanPrompts(r, 'find:').filter((t) => t.prompt.indexOf('holds none') !== -1).map((t) => t.label)
    ck(none.join(' ') === 'find:verification find:intent',
      'checklist: fewer items than lenses leaves an explicit empty share: ' + none.join(' '))
  }
  // ---- AC4: absent and empty are each announced in their own words; a real checklist warns nothing.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'checklist absent')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const fp = scanPrompts(r, 'find:')
    ck(r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('no `checklist` was supplied') !== -1) && !!sp &&
      sp.prompt.indexOf('Checklist: NONE swept — absent') !== -1 && fp.length === 5 && fp.every((t) => t.prompt.indexOf('CHECKLIST') === -1),
      'checklist absent: announced in the log and RUN INTEGRITY')
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: '   ' }), ALL_OK)
  if (checkNoThrow(r, 'checklist empty')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('`checklist` was supplied with no item') !== -1) && !!sp &&
      sp.prompt.indexOf('Checklist: NONE swept — supplied with no item') !== -1,
      'checklist empty: announced as supplied with no item')
  }
  if (rcl.result) {
    ck(!rcl.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('`checklist`') !== -1) && rcl.logs.some((l) => l.indexOf('checklist:') === 0),
      'checklist supplied: no checklist warning')
  }
  // ---- AC5: six malformed values refuse before any agent spawns.
  const refusedChecklists = [['7', 7], ['{}', {}], ['null', null], ['[1]', [1]], ["['  ']", ['  ']], ['a string with no item line', 'no item line here']]
  for (const [what, v] of refusedChecklists) {
    r = await runReview(Object.assign({}, DIFF, { checklist: v }), ALL_OK)
    ck(typeof r.threw === 'string' && r.threw.indexOf('checklist') !== -1 && r.trace.length === 0,
      'checklist refused before any agent: ' + what + (r.threw ? '' : ' (accepted)'))
  }
  // ---- AC6: a spec audit splits over its own four lenses and sweeps the spec set.
  r = await runReview(Object.assign({}, SPEC, { checklist: CL_STR }), ALL_OK)
  if (checkNoThrow(r, 'spec-audit checklist')) {
    const fp = scanPrompts(r, 'find:')
    ck(scanSplit(r, SPEC_ORDER) && fp.every((t) => t.prompt.indexOf('against the spec set') !== -1),
      'spec-audit: the checklist splits over the spec lenses')
  }

  // ==== TOOL-aSightedSkeptic-2 — the skeptic judges each finding's proposed fix as well as its claim ====
  // Every arm is RED against the parent render: its verify prompt shows no fix, its schema has no
  // fixVerdict, its synthesis prints the finder's fix unmarked, and its batch print ignores the fix.
  const buildFixLens = (label) => {
    const lr = buildLensReturn(label)
    lr.findings[0].fix = 'FIXMARK-' + lr.lens
    return lr
  }
  const buildFixVerdicts = (fixVerdict, fixNote) => (label, prompt) => {
    const vr = buildVerdicts('confirmed')(label, prompt)
    for (const v of vr.verdicts) { v.fixVerdict = fixVerdict; v.fixNote = fixNote }
    return vr
  }
  // The CONFIRMED section of the synthesis prompt, one entry per finding.
  const scanConfirmedEntries = (run) => {
    const sp = run.trace.find((t) => t.label === 'synth')
    if (!sp) return []
    const sec = sp.prompt.split('UNVERIFIED findings')[0]
    return sec.slice(sec.indexOf('CONFIRMED findings')).split('\n- id=').slice(1)
  }
  // ---- AC1: one diff-kind and one spec-kind run; every verify prompt carries each finding's fix.
  const rfd = await runReview(DIFF, buildStubs({ 'find:': buildFixLens }))
  const rfs = await runReview(SPEC, buildStubs({ 'find:': buildFixLens }))
  if (checkNoThrow(rfd, 'fix verdict diff') && checkNoThrow(rfs, 'fix verdict spec')) {
    const vp = scanPrompts(rfd, 'verify:').concat(scanPrompts(rfs, 'verify:'))
    ck(vp.length === 9 && vp.every((t) => /FIXMARK-[a-z-]+/.test(t.prompt) && t.prompt.indexOf('"sound"') !== -1 &&
      t.prompt.indexOf('"unsound"') !== -1 && t.prompt.indexOf('fixVerdict') !== -1),
      'fix verdict: every verify prompt shows each finding\'s fix and asks for fixVerdict')
  }
  // ---- AC2: the item schema, read off what the skeptic was actually handed.
  const vs = rfd.trace.find((t) => t.label.indexOf('verify:') === 0)
  const vItem = vs && vs.schema && vs.schema.properties && vs.schema.properties.verdicts && vs.schema.properties.verdicts.items
  const vProps = (vItem && vItem.properties) || {}
  ck(!!vProps.fixVerdict && JSON.stringify(vProps.fixVerdict.enum) === '["sound","unsound","none"]' &&
    !!vProps.fixNote && vProps.fixNote.type === 'string' &&
    Array.isArray(vItem.required) && vItem.required.indexOf('fixVerdict') === -1 && vItem.required.indexOf('fixNote') === -1,
    'fix verdict: the verdict schema carries fixVerdict and fixNote, neither required')
  // ---- AC3: confirmed + unsound with a note — the note and REJECTED on every CONFIRMED entry, and
  // ---- the confirmed count unchanged against the plain run.
  const rbase = await runReview(DIFF, ALL_OK)
  r = await runReview(DIFF, buildStubs({ 'verify:': buildFixVerdicts('unsound', 'NOTEMARK use the other guard') }))
  if (checkNoThrow(rbase, 'fix verdict base') && checkNoThrow(r, 'fix verdict unsound')) {
    const ce = scanConfirmedEntries(r)
    ck(ce.length === 5 && ce.every((e) => e.indexOf('REJECTED') !== -1 && e.indexOf('NOTEMARK use the other guard') !== -1) &&
      r.result.confirmed === rbase.result.confirmed && r.result.confirmed === 5,
      'fix verdict: an unsound fix reaches the synthesis as the correction, the finding still confirmed')
  }
  // ---- AC4: an unsound fix with an EMPTY note is still to be designed, never the finder's fix.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildFixVerdicts('unsound', '') }))
  if (checkNoThrow(r, 'fix verdict unsound no note')) {
    const ce = scanConfirmedEntries(r)
    ck(ce.length === 5 && ce.every((e) => e.indexOf('REJECTED') !== -1 && e.indexOf('STILL TO BE DESIGNED') !== -1),
      'fix verdict: an unsound fix with no correction is still to be designed')
  }
  // ---- Closing review round 1, M3: the INSTRUCTED shape of "unsound, no correction" is an empty note
  // ---- with the why in `reason`; the verify prompt says so, and that shape renders STILL TO BE
  // ---- DESIGNED with the why on the why-real line and the finder's fix, marked unsound, handed on.
  r = await runReview(DIFF, buildStubs({ 'verify:': (label, prompt) => {
    const vr = buildFixVerdicts('unsound', '')(label, prompt)
    for (const v of vr.verdicts) v.reason = 'WHYMARK-' + v.id
    return vr
  } }))
  if (checkNoThrow(r, 'fix verdict reason only')) {
    const ce = scanConfirmedEntries(r)
    const vp = scanPrompts(r, 'verify:')
    const cf3 = Array.isArray(r.result.confirmedFindings) ? r.result.confirmedFindings : []
    ck(vp.length === 5 && vp.every((t) => t.prompt.indexOf('`fixNote` holds ONLY the corrected fix, and is empty when you have none') !== -1 &&
      t.prompt.indexOf('say why the fix is unsound in `reason`') !== -1) &&
      ce.length === 5 && ce.every((e, i) => e.indexOf('STILL TO BE DESIGNED') !== -1 && e.indexOf('why-real: WHYMARK-' + (i + 1)) !== -1) &&
      cf3.length === 5 && cf3.every((e) => e.fix === 'f' && e.fixVerdict === 'unsound'),
      'fix verdict: a reason-only unsound verdict is still to be designed, its why in reason')
  }
  // ---- Closing review round 1, M5: sound, none and unsound in one run, each rendered on its own
  // ---- CONFIRMED entry and each counted in RUN INTEGRITY.
  r = await runReview(DIFF, buildStubs({ 'find:': buildFixLens, 'verify:': (label, prompt) => {
    const vr = buildVerdicts('confirmed')(label, prompt)
    for (const v of vr.verdicts) {
      v.fixVerdict = v.id <= 2 ? 'sound' : v.id === 3 ? 'none' : 'unsound'
      if (v.id > 3) v.fixNote = 'CORR-' + v.id
    }
    return vr
  } }))
  if (checkNoThrow(r, 'fix verdict three values')) {
    const ce = scanConfirmedEntries(r)
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(ce.length === 5 && ce.slice(0, 2).every((e) => e.indexOf('fix (judged SOUND by the skeptic): FIXMARK-') !== -1) &&
      ce[2].indexOf('fix: none proposed') !== -1 &&
      ce.slice(3).every((e, i) => e.indexOf('REJECTED') !== -1 && e.indexOf('CORR-' + (i + 4)) !== -1) &&
      ri.indexOf('2 judged sound, 2 judged UNSOUND, 1 none proposed, 0 NOT JUDGED') !== -1,
      'fix verdict: sound, none and unsound are each rendered and counted in RUN INTEGRITY')
  }
  // ---- AC5: the existing stub verdicts carry no fixVerdict, so all five confirmed fixes are unjudged.
  if (checkNoThrow(rbase, 'fix verdict unjudged')) {
    const sp = rbase.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(rbase.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('no skeptic judged') !== -1 && /ids 1, 2, 3, 4, 5$/.test(l)) &&
      ri.indexOf('5 NOT JUDGED') !== -1,
      'fix verdict: an unjudged fix is counted, logged and named in RUN INTEGRITY')
  }
  // ---- AC6: the AC5 print was taken over fix 'f'; the same ids and claims under another fix dispatch.
  const otherFixFiles = allLensFiles.map((lf) => {
    const c = JSON.parse(JSON.stringify(lf))
    c.findings[0].fix = 'another fix'
    return c
  })
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(otherFixFiles, [vfile(print)]) }))
  if (checkNoThrow(r, 'fix verdict other fix')) {
    ck(print.length === 8 && r.scanSpawned('find:').length === 0 && r.scanSpawned('verify:ids-1-1').length === 1,
      'fix verdict: a verify file judged over another fix is dispatched')
  }

  // ==== TOOL-aSightedSkeptic-6 — one severity rubric, a skeptic's binding grade, an uncertain verdict ==
  // Every arm is RED against the parent render: no prompt carries a rubric, the verdict schema closes
  // at confirmed and refuted, the synthesis bracket is the finder's grade, no ungraded count exists, an
  // uncertain verdict is held as neither confirmed, refuted nor unverified, and no `regraded` returns.
  const RUBRIC_END = 'how alarming the defect looks.'
  const scanRubric = (p) => {
    const i = p.indexOf('SEVERITY RUBRIC')
    const j = i === -1 ? -1 : p.indexOf(RUBRIC_END, i)
    return j === -1 ? null : p.slice(i, j + RUBRIC_END.length)
  }
  // A skeptic stub answering `verdict` for every id, with `grade(id)` as the skeptic's severity.
  const buildGradedVerdicts = (verdict, grade) => (label, prompt) => {
    const vr = buildVerdicts(verdict)(label, prompt)
    for (const v of vr.verdicts) {
      v.reason = 'RSN-' + v.id
      const g = grade ? grade(v.id) : undefined
      if (g) v.severity = g
    }
    return vr
  }
  // ---- AC1: the same rubric bytes in every find:, verify: and synth prompt, on both kinds.
  const rrd = await runReview(DIFF, ALL_OK)
  const rrs = await runReview(SPEC, ALL_OK)
  if (checkNoThrow(rrd, 'rubric diff') && checkNoThrow(rrs, 'rubric spec')) {
    const scanRubricOk = (run, n) => {
      const rp = scanPrompts(run, 'find:').concat(scanPrompts(run, 'verify:'), scanPrompts(run, 'synth'))
      const texts = [...new Set(rp.map((t) => scanRubric(t.prompt)))]
      return rp.length === n && texts.length === 1 && !!texts[0] && ['blocker:', 'high:', 'medium:', 'low:'].every((g) => texts[0].indexOf(g) !== -1)
    }
    ck(scanRubricOk(rrd, 11) && scanRubricOk(rrs, 9), 'severity: one rubric reaches every finder, skeptic and synthesis prompt')
  }
  // ---- AC2: the item schema the skeptic was handed.
  const vs6 = scanPrompts(rrd, 'verify:')[0]
  const vi6 = vs6 && vs6.schema && vs6.schema.properties && vs6.schema.properties.verdicts && vs6.schema.properties.verdicts.items
  const vp6 = (vi6 && vi6.properties) || {}
  ck(!!vp6.verdict && Array.isArray(vp6.verdict.enum) && vp6.verdict.enum.indexOf('uncertain') !== -1 &&
    !!vp6.severity && JSON.stringify(vp6.severity.enum) === '["blocker","high","medium","low"]' &&
    Array.isArray(vi6.required) && vi6.required.indexOf('severity') === -1,
    'severity: the verdict schema carries uncertain and an optional severity')
  // ---- AC3: the finder grades every finding high; the skeptic confirms id 1 at blocker, the rest at high.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildGradedVerdicts('confirmed', (id) => (id === 1 ? 'blocker' : 'high')) }))
  if (checkNoThrow(r, 'binding grade')) {
    const ce = scanConfirmedEntries(r)
    ck(ce.length === 5 && /^1 \[blocker\] \(finder graded high, skeptic graded blocker\)/.test(ce[0]) &&
      ce.slice(1).every((e) => /^\d+ \[high\] /.test(e) && e.indexOf('finder graded') === -1) &&
      r.logs.some((l) => /^note: 1 confirmed finding\(s\) RE-GRADED/.test(l) && /ids 1$/.test(l)),
      'severity: the skeptic\'s grade binds the synthesis line')
  }
  // ---- AC4: the existing stub verdicts carry no grade, so every finding falls back to the finder's.
  if (checkNoThrow(rrd, 'ungraded')) {
    const ce = scanConfirmedEntries(rrd)
    const sp = rrd.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(ce.length === 5 && ce.every((e) => /^\d+ \[high\] /.test(e)) &&
      rrd.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('UNGRADED') !== -1 && /ids 1, 2, 3, 4, 5$/.test(l)) &&
      ri.indexOf('5 UNGRADED') !== -1,
      'severity: a confirmed verdict with no grade falls back to the finder\'s, counted and announced')
  }
  // ---- AC5: one batch answers uncertain; it is unverified, outside precision, and listed with its reason.
  r = await runReview(DIFF, buildStubs({ 'verify:ids-3-3': buildGradedVerdicts('uncertain') }))
  if (checkNoThrow(r, 'uncertain verdict')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const uv = sp ? sp.prompt.slice(sp.prompt.indexOf('UNVERIFIED findings')) : ''
    const head = sp ? sp.prompt.split('UNVERIFIED findings')[0] : ''
    ck(r.result.uncertain === 1 && r.result.unverified === 1 && r.result.confirmed === 4 && r.result.refuted === 0 &&
      r.result.precision === 1 && /id=3 \[high\][^\n]*\n[\s\S]*status: UNCERTAIN[^\n]*RSN-3/.test(uv) && head.indexOf('id=3 [') === -1,
      'severity: an uncertain verdict is counted unverified, never refuted or confirmed')
  }
  // ---- AC6: skeptics confirm at blocker; the stub synthesis places every id in one HIGH item.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildGradedVerdicts('confirmed', () => 'blocker') }))
  if (checkNoThrow(r, 'regraded')) {
    ck(Array.isArray(r.result.regraded) && r.result.regraded.join(' ') === '1 2 3 4 5' && r.result.highs === 5 && r.result.blockers === 0,
      'severity: a synthesis placing an id off its binding grade is returned in regraded')
  }
  // ---- AC7: every verify prompt, both kinds, answers uncertain only for a blocker or high finding.
  const uvp = scanPrompts(rrd, 'verify:').concat(scanPrompts(rrs, 'verify:'))
  ck(uvp.length === 9 && uvp.every((t) => t.prompt.indexOf('graded blocker or high is answered "uncertain"') !== -1 &&
    t.prompt.indexOf('graded medium or low (the bracketed grade) is "refuted"') !== -1 && t.prompt.indexOf('Default to refuted when uncertain') === -1),
    'severity: the uncertain rule follows the finder\'s grade')

  // ==== TOOL-aSightedSkeptic-7 — `intensity`, and a light run that announces the lenses it skips ======
  // Every arm is RED against the parent render: it reads no `intensity`, so a light run dispatches all
  // five lenses, returns neither field, logs no skip, keys identically to a full run and carries no
  // LIGHT_LENSES literal for the rewrite to take.
  const LIGHT = Object.assign({}, DIFF, { intensity: 'light' })
  const rl = await runReview(LIGHT, ALL_OK)
  const rf = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(rl, 'light run') && checkNoThrow(rf, 'full run')) {
    // ---- AC2: the light lenses alone are dispatched; an absent value dispatches all five.
    ck(rl.scanSpawned('find:').join(' ') === 'find:correctness find:seams find:verification' && rf.scanSpawned('find:').length === 5,
      'intensity: light dispatches only the light lenses: ' + rl.scanSpawned('find:').join(' '))
    // ---- AC3: a skip is neither live nor dead, and every count runs over the three that ran.
    ck(rl.result.exit === 'complete' && rl.result.lensesDead === 0 && rl.result.lensesRun === 3 && rl.result.intensity === 'light' &&
      Array.isArray(rl.result.skippedLenses) && rl.result.skippedLenses.join(' ') === 'security intent' && rl.result.agents === 3 + 3 + 1 &&
      rf.result.intensity === 'full' && Array.isArray(rf.result.skippedLenses) && rf.result.skippedLenses.length === 0,
      'intensity: a skipped lens is neither live nor dead: a light run completes, three lenses in its agent count')
    // ---- AC4: the light run's log and RUN INTEGRITY name both skipped lenses; the full run names
    // ---- its intensity and carries no skipped-lens clause.
    const lsp = rl.trace.find((t) => t.label === 'synth')
    const fsp = rf.trace.find((t) => t.label === 'synth')
    const lri = lsp ? lsp.prompt.slice(lsp.prompt.indexOf('RUN INTEGRITY')) : ''
    const fri = fsp ? fsp.prompt.slice(fsp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(rl.logs.some((l) => l.indexOf('WARNING: intensity light') === 0 && l.indexOf('security') !== -1 && l.indexOf('intent') !== -1 && l.indexOf('NOT run') !== -1) &&
      /Intensity: light[^\n]*security[^\n]*intent[^\n]*NOT run/.test(lri) && lsp.prompt.indexOf('intensity light, raw') !== -1,
      'intensity: a light run announces its skipped lenses in the log and RUN INTEGRITY')
    ck(!!fsp && fsp.prompt.indexOf('intensity full, raw') !== -1 && fri.indexOf('NOT run') === -1 && fri.indexOf('Intensity:') === -1 &&
      !rf.logs.some((l) => l.indexOf('intensity light') !== -1),
      'intensity: a light run announces its skipped lenses: a full run names intensity full and no skipped lens')
    // ---- AC7: the key differs by intensity; a full-key correctness file is dispatched in a light run,
    // ---- a light-key one is reused, and a skipped lens's file is never reused or named as reused.
    const KL = rl.result.key
    const KF = rf.result.key
    const rk1 = await runReview(LIGHT, buildStubs({ 'resume:probe': buildProbe([buildLensFile('correctness', KF)]) }))
    const rk2 = await runReview(LIGHT, buildStubs({ 'resume:probe': buildProbe([buildLensFile('correctness', KL), buildLensFile('security', KL)]) }))
    if (checkNoThrow(rk1, 'intensity key full file') && checkNoThrow(rk2, 'intensity key light file')) {
      ck(KL !== KF && rk1.scanSpawned('find:correctness').length === 1 && rk2.scanSpawned('find:correctness').length === 0 &&
        rk2.result.lensesReused === 1 && rk2.scanSpawned('find:security').length === 0 && !rk2.logs.some((l) => l.indexOf('reused find:security') !== -1),
        'intensity: the key differs by intensity')
    }
  }
  // ---- AC3 second half: the three running lenses all die; pending names exactly those three.
  r = await runReview(LIGHT, buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'light run all dead')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:correctness find:seams find:verification' &&
      r.result.lensesDead === 3 && r.result.intensity === 'light' && r.result.skippedLenses.join(' ') === 'security intent',
      'intensity: a skipped lens is neither live nor dead: three running lenses dead defer, pending only those three')
  }
  // ---- AC5: a copy whose LIGHT_LENSES names a dead key, or none, refuses before any agent, on either
  // ---- kind and at full intensity. The rewrite is asserted to have TAKEN before the throw is graded.
  const lightRe = /const LIGHT_LENSES = \[[^\]]*\]/
  for (const [what, lit, args] of [['a renamed key, diff review', "['correctness', 'seams', 'verificaton']", DIFF], ['an empty literal, spec audit', '[]', SPEC]]) {
    const src2 = whole.replace(lightRe, 'const LIGHT_LENSES = ' + lit)
    r = await runReview(args, ALL_OK, src2)
    ck(lightRe.test(whole) && src2 !== whole && typeof r.threw === 'string' && r.threw.indexOf('LIGHT_LENSES') !== -1 && r.trace.length === 0,
      'intensity: LIGHT_LENSES must name live lenses: ' + what + (r.threw ? '' : ' (accepted)'))
  }
  // ---- AC6: a six-item checklist reaches a RUNNING lens, each item in exactly one find: prompt, on a
  // ---- light run over three lenses and on a full run over five.
  const SIX = [1, 2, 3, 4, 5, 6].map((n) => 'SIXA' + n + 'Z')
  const scanSix = (run, n) => {
    const fp = scanPrompts(run, 'find:')
    return fp.length === n && SIX.every((s) => fp.filter((t) => t.prompt.indexOf(s) !== -1).length === 1 && fp.some((t) => countIn(t.prompt, s) === 1))
  }
  const rl6 = await runReview(Object.assign({}, LIGHT, { checklist: SIX }), ALL_OK)
  const rf6 = await runReview(Object.assign({}, DIFF, { checklist: SIX }), ALL_OK)
  if (checkNoThrow(rl6, 'light checklist') && checkNoThrow(rf6, 'full checklist')) {
    ck(scanSix(rl6, 3) && scanSix(rf6, 5), 'intensity: every checklist item reaches a running lens')
  }
  // ---- Closing review round 1, L6: a note for a lens the light run skipped is reported UNREAD, in the
  // ---- log and RUN INTEGRITY, and is never listed as supplied for a lens that ran.
  r = await runReview(Object.assign({}, LIGHT, { lensNotes: { security: 'n' } }), ALL_OK)
  if (checkNoThrow(r, 'light run skipped-lens note')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(ri.indexOf('lens notes supplied for: no lens that ran; lens notes for skipped lenses, unread: security.') !== -1 &&
      ri.indexOf('lens notes supplied for: security') === -1 &&
      r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('unread: security') !== -1),
      'intensity: a lens note for a skipped lens is reported unread')
  }

  // ==== TOOL-aSightedSkeptic-10 — the surfaces two "Observed by" claims named and no arm read ==========
  // Closing review round 1, H1 and H2. Each arm reads the surface its scope item renders on, counts what
  // it reads before grading it, and was observed RED against the staged break its spec's §4 table names.
  const OBS_NOTE = 'OBSNOTE-10 guard the other branch'
  // A skeptic confirming every id at blocker, rejecting the finder's fix with a corrected one.
  const buildRejectedVerdicts = (label, prompt) => {
    const vr = buildFixVerdicts('unsound', OBS_NOTE)(label, prompt)
    for (const v of vr.verdicts) v.severity = 'blocker'
    return vr
  }
  const scanConfirmedLogs = (run) => run.logs.filter((l) => l.indexOf('  CONFIRMED [') === 0)
  // ---- S1: a dead synthesis logs every confirmed finding at its binding grade, its fix through renderFixLine.
  r = await runReview(DIFF, buildStubs({ synth: null, 'find:': buildFixLens, 'verify:': buildRejectedVerdicts }))
  if (checkNoThrow(r, 'observed-by dead synthesis')) {
    const cl = scanConfirmedLogs(r)
    ck(cl.length === 5 && cl.every((l) => l.indexOf('  CONFIRMED [blocker] ') === 0),
      'observed-by: a dead synthesis logs every CONFIRMED finding at its binding grade')
    ck(cl.length === 5 && cl.every((l) => l.indexOf('REJECTED') !== -1 && l.indexOf(OBS_NOTE) !== -1 && l.indexOf('NOT JUDGED') === -1),
      'observed-by: a dead synthesis logs every CONFIRMED finding\'s fix through renderFixLine')
  }
  // ---- S2: a dead skeptic batch logs the four confirmed findings at their binding grade.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildGradedVerdicts('confirmed', () => 'blocker'), 'verify:ids-2-2': null }))
  if (checkNoThrow(r, 'observed-by dead batch')) {
    const cl = scanConfirmedLogs(r)
    ck(cl.length === 4 && cl.every((l) => l.indexOf('  CONFIRMED [blocker] ') === 0),
      'observed-by: a dead skeptic batch logs every CONFIRMED finding at its binding grade')
  }
  // ---- S3: one uncertain answer, counted apart from no verdict in the note, RUN INTEGRITY and the log.
  r = await runReview(DIFF, buildStubs({ 'verify:ids-3-3': buildGradedVerdicts('uncertain') }))
  if (checkNoThrow(r, 'observed-by one uncertain')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    const uw = r.logs.filter((l) => l.indexOf('WARNING: 1 finding(s) answered UNCERTAIN') === 0)
    ck(r.result.uncertain === 1 && uw.length === 1 &&
      String(r.result.note).indexOf('PARTIAL: 1 finding(s) are unverified — 1 answered uncertain by a skeptic, 0 with no usable verdict') === 0 &&
      ri.indexOf('1 answered UNCERTAIN by a skeptic, 0 with NO usable verdict') !== -1 &&
      !r.logs.some((l) => l.indexOf('with NO usable verdict') !== -1),
      'observed-by: one uncertain answer is counted apart from no verdict in the note, RUN INTEGRITY and the log')
  }
  // ---- S4: every batch uncertain; the note never reads as none judged.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildGradedVerdicts('uncertain') }))
  if (checkNoThrow(r, 'observed-by all uncertain')) {
    const note = String(r.result.note)
    ck(r.result.uncertain === 5 && r.result.unverified === 5 && note.indexOf('none confirmed or refuted') !== -1 &&
      note.indexOf('5 answered uncertain by a skeptic, 0 with no usable verdict') !== -1 && note.indexOf('none judged') === -1,
      'observed-by: an all-uncertain round never reads as none judged')
  }
  await runLedgerArms()
}

// ==== TOOL-aSightedSkeptic-8 — every finding keeps its lens; ledger, confirmedFindings and appendix ====
// Every arm is RED against the parent render: its findings carry no `lens`, no prompt line names one,
// and no return carries `ledger`, `confirmedFindings` or `appendix`. Self-contained, so the block runs
// the same wherever it is called from. The stub lens `<key>` writes its one finding at `<key>.js:1`,
// which is how each arm tells which lens raised a finding without asking the harness.
async function runLedgerArms() {
  const LORDER = ['security', 'correctness', 'seams', 'verification', 'intent']
  const lensOfRef = (ref) => String(ref).split('.js:')[0]
  const scanLedger = (run, n) => !!run.result && Array.isArray(run.result.ledger) && run.result.ledger.length === n
  const scanPrompts = (run, prefix) => run.trace.filter((t) => t.label.indexOf(prefix) === 0)
  let r = null
  // ---- AC1: the lens is the DISPATCH key — on a complete run, against an echo of 'bogus', and over
  // ---- lens files reused from the probe.
  const lc = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(lc, 'ledger complete run')) {
    ck(scanLedger(lc, 5) && lc.result.ledger.every((e, i) => e.id === i + 1 && e.lens === LORDER[i] && lensOfRef(e.ref) === e.lens),
      'ledger: every finding carries its dispatching lens: a complete run, five entries in id order')
  }
  const buildBogusLens = (label) => {
    const lr = buildLensReturn(label)
    lr.lens = 'bogus'
    lr.findings[0].lens = 'bogus'
    return lr
  }
  r = await runReview(DIFF, buildStubs({ 'find:seams': buildBogusLens }))
  if (checkNoThrow(r, 'ledger bogus echo')) {
    ck(scanLedger(r, 5) && r.result.ledger[2].lens === 'seams' && r.result.ledger.every((e) => e.lens !== 'bogus' && lensOfRef(e.ref) === e.lens),
      'ledger: every finding carries its dispatching lens: an echo of bogus still yields seams')
  }
  const LK = lc.result ? lc.result.key : ''
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(LORDER.map((l) => buildLensFile(l, LK))) }))
  if (checkNoThrow(r, 'ledger reused lenses')) {
    ck(r.scanSpawned('find:').length === 0 && r.result.lensesReused === 5 && scanLedger(r, 5) &&
      r.result.ledger.every((e, i) => e.lens === LORDER[i] && lensOfRef(e.ref) === e.lens),
      'ledger: every finding carries its dispatching lens: every lens file reused yields the same lenses')
  }

  // ---- AC2: `lens=<key>` follows the grade on every verify line and every CONFIRMED synthesis line,
  // ---- and the stubs' own id patterns still match (the run completing with five confirmed says so).
  // The synthesis line may carry TOOL-aSightedSkeptic-6's grade parenthetical between the bracket and the lens.
  const LINE_RE = /^id=(\d+) \[high\](?: \([^)]*\))? lens=([a-z-]+) ([a-z-]+)\.js:1 — /
  const vl = scanPrompts(lc, 'verify:')
  ck(vl.length === 5 && vl.every((t) => {
    const lines = t.prompt.split('\n').filter((l) => l.indexOf('id=') === 0)
    return lines.length === 1 && lines.every((l) => { const m = LINE_RE.exec(l); return !!m && m[2] === m[3] && m[2] === LORDER[+m[1] - 1] })
  }), 'ledger: the skeptic and synthesis lines name the lens: every verify: finding line')
  const lsp = lc.trace.find((t) => t.label === 'synth')
  const lhead = lsp ? lsp.prompt.split('UNVERIFIED findings')[0] : ''
  const lcl = lhead.split('\n').filter((l) => l.indexOf('- id=') === 0).map((l) => l.slice(2))
  ck(!!lc.result && lc.result.confirmed === 5 && [...lhead.matchAll(/id=(\d+) \[/g)].length === 5 && lcl.length === 5 &&
    lcl.every((l) => { const m = LINE_RE.exec(l); return !!m && m[2] === m[3] }),
    'ledger: the skeptic and synthesis lines name the lens: every CONFIRMED synth line, id pattern intact')
  r = await runReview(DIFF, buildStubs({ 'verify:ids-2-2': null }))
  if (checkNoThrow(r, 'ledger deferred log')) {
    const dl = r.logs.filter((l) => /^ {2}(CONFIRMED|UNVERIFIED) \[/.test(l))
    ck(dl.length === 5 && dl.every((l) => { const m = / lens=([a-z-]+) ([a-z-]+)\.js:1 - /.exec(l); return !!m && m[1] === m[2] }),
      'ledger: the skeptic and synthesis lines name the lens: the deferred path\'s log lines')
  }

  // ---- AC3: one batch per state. id 1 refuted, 2 uncertain, 3 no verdict, 4 contradicted, 5 confirmed
  // ---- at low with an unsound fix.
  const VS = {
    'verify:ids-1-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'r1' }] },
    'verify:ids-2-2': { path: '/v', verdicts: [{ id: 2, verdict: 'uncertain', reason: 'r2' }] },
    'verify:ids-3-3': { path: '/v', verdicts: [] },
    'verify:ids-4-4': { path: '/v', verdicts: [{ id: 4, verdict: 'confirmed', reason: 'a' }, { id: 4, verdict: 'refuted', reason: 'b' }] },
    'verify:ids-5-5': { path: '/v', verdicts: [{ id: 5, verdict: 'confirmed', reason: 'r5', severity: 'low', fixVerdict: 'unsound', fixNote: 'n5' }] },
  }
  r = await runReview(DIFF, buildStubs(VS))
  if (checkNoThrow(r, 'ledger verdict states')) {
    const L = scanLedger(r, 5) ? r.result.ledger : []
    ck(L.map((e) => e.verdict).join(' ') === 'refuted uncertain unverified unverified confirmed' &&
      L[0].reason === 'r1' && L[3].reason === 'contradictory verdicts' && L[4].skepticSeverity === 'low' && L[4].fixVerdict === 'unsound' &&
      L.every((e, i) => e.lens === LORDER[i] && e.severity === 'high' && e.claim === LORDER[i] + ' claim'),
      'ledger: every verdict state reaches the ledger: ' + L.map((e) => e.verdict).join(' '))
    ck(L.length === 5 && L[0].skepticSeverity === null && L[0].fixVerdict === null && L[2].skepticSeverity === null &&
      L[2].fixVerdict === null && L[2].reason === '' && L[3].skepticSeverity === null,
      'ledger: every verdict state reaches the ledger: the absent fields read null, a missing reason reads empty')
  }

  // ---- AC4: confirmedFindings is round N+1's priorFindings, with a rejected fix replaced.
  const cf = lc.result && Array.isArray(lc.result.confirmedFindings) ? lc.result.confirmedFindings : null
  ck(!!cf && cf.length === lc.result.confirmed && cf.length === 5 &&
    cf.every((e, i) => e.id === i + 1 && e.lens === LORDER[i] && e.ref === LORDER[i] + '.js:1' && e.claim === LORDER[i] + ' claim' &&
      e.severity === 'high' && e.fix === 'f' && e.fixVerdict === null),
    'ledger: confirmedFindings feeds the next round: one entry per confirmed finding')
  const unsound2 = (label, prompt) => {
    const vr = buildVerdicts('confirmed')(label, prompt)
    for (const v of vr.verdicts) Object.assign(v, { severity: 'blocker', fixVerdict: 'unsound', fixNote: 'better fix' })
    return vr
  }
  r = await runReview(DIFF, buildStubs({ 'verify:ids-2-2': unsound2 }))
  if (checkNoThrow(r, 'ledger rejected fix')) {
    const c2 = Array.isArray(r.result.confirmedFindings) ? r.result.confirmedFindings : []
    ck(c2.length === 5 && c2[1].fix === 'better fix' && c2[1].fixVerdict === 'unsound' && c2[1].severity === 'blocker' &&
      c2.filter((e, i) => i !== 1).every((e) => e.fix === 'f' && e.severity === 'high'),
      'ledger: confirmedFindings feeds the next round: a rejected fix is replaced by the skeptic\'s note, at the binding grade')
  }
  // ---- Closing review round 1, L3 (finding 16): an EMPTY or blank note is no correction, so the
  // ---- finder's fix stays, marked by fixVerdict unsound; dropping the `&& note` guard hands on ''.
  for (const [what, note] of [['an empty note', ''], ['a blank note', '   ']]) {
    r = await runReview(DIFF, buildStubs({ 'verify:ids-2-2': { path: '/v', verdicts: [{ id: 2, verdict: 'confirmed', reason: 'r', fixVerdict: 'unsound', fixNote: note }] } }))
    if (!checkNoThrow(r, 'ledger unsound ' + what)) continue
    const c3 = Array.isArray(r.result.confirmedFindings) ? r.result.confirmedFindings : []
    ck(c3.length === 5 && c3[1].fix === 'f' && c3[1].fixVerdict === 'unsound',
      'ledger: confirmedFindings feeds the next round: an unsound fix with ' + what + ' keeps the finder\'s fix, marked unsound')
  }
  r = await runReview(Object.assign({}, DIFF, { round: 2, priorFindings: cf }), ALL_OK)
  if (checkNoThrow(r, 'ledger round two')) {
    const f2 = scanPrompts(r, 'find:')
    ck(!!cf && f2.length === 5 && f2.every((t) => cf.every((e) => t.prompt.indexOf('  - ' + e.ref + ' - ' + e.claim) !== -1)),
      'ledger: confirmedFindings feeds the next round: a round-2 run given it carries every ref and claim in every find: prompt')
  }

  // ---- AC5: the harness renders the table, refuted rows included, and hands it to the synthesis
  // ---- verbatim. id 1's claim and reason carry a pipe and a line break; the row count does not move.
  const buildPipeLens = (label) => {
    const lr = buildLensReturn(label)
    if (lr.lens === 'security') lr.findings[0].claim = 'a | b\nc'
    return lr
  }
  r = await runReview(DIFF, buildStubs({ 'find:': buildPipeLens, 'verify:ids-1-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'x | y\r\nz' }] } }))
  if (checkNoThrow(r, 'ledger appendix')) {
    const ap = typeof r.result.appendix === 'string' ? r.result.appendix : ''
    const al = ap.split('\n')
    const rows = al.slice(4)
    const unescaped = (row) => row.split('').filter((ch, i) => ch === '|' && row[i - 1] !== '\\').length
    ck(al[0] === '## Appendix — every finding' && al[1] === '' &&
      al[2] === '| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |' && al[3] === '|---|---|---|---|---|---|---|---|---|' &&
      rows.length === 5 && rows.length === r.result.ledger.length && rows[0].indexOf('| 1 | security | security.js:1 | high | - | refuted |') === 0,
      'ledger: the appendix is rendered by the harness: heading, nine columns, one row per finding, the refuted one included')
    ck(rows.length === 5 && rows.every((row) => unescaped(row) === 10) && rows[0].indexOf('x \\| y z') !== -1 && ap.indexOf('\r') === -1,
      'ledger: the appendix is rendered by the harness: a pipe and a line break in a cell leave the row count unchanged')
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(ap.length > 0 && !!sp && sp.prompt.indexOf(ap) !== -1 && sp.prompt.indexOf('VERBATIM') !== -1,
      'ledger: the appendix is handed to the synthesis verbatim')
  }
  // ---- Closing review round 1, L2: a reason carrying every other boundary Python's str.splitlines
  // ---- breaks on. The appendix must split into the same lines under that rule as under `\n`.
  r = await runReview(DIFF, buildStubs({ 'verify:ids-1-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'p\u2028q\u2029r\x85s\x0bt\x0cu\x1cv\x1ew' }] } }))
  if (checkNoThrow(r, 'ledger appendix splitlines')) {
    const ap = typeof r.result.appendix === 'string' ? r.result.appendix : ''
    const al = ap.split('\n')
    ck(al.length === 9 && ap.split(/\r\n|[\n\r\x0b\x0c\x1c-\x1e\x85\u2028\u2029]/).length === al.length && al[4].indexOf('| p q r s t u v w |') !== -1,
      'ledger: the appendix is rendered by the harness: a U+2028 in a reason cell leaves the row count unchanged')
  }
  // ---- TOOL-aMendedFleet-17 AC2: a claim's head labels resolve to the run's item slugs in `classes`,
  // ---- an out-of-range label stays `C<n>`, and an unlabelled claim renders `-` in the ninth column.
  const buildLabelLens = (label) => {
    const lr = buildLensReturn(label)
    if (lr.lens === 'security') lr.findings[0].claim = 'C2 — x'
    if (lr.lens === 'correctness') lr.findings[0].claim = '[C1] C9: y'
    return lr
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: ['[ ] alpha-one (universal)', '[ ] beta-two'] }), buildStubs({ 'find:': buildLabelLens }))
  if (checkNoThrow(r, 'ledger classes')) {
    const lg = Array.isArray(r.result.ledger) ? r.result.ledger : []
    const al = (typeof r.result.appendix === 'string' ? r.result.appendix : '').split('\n')
    ck(lg.length === 5 && JSON.stringify(lg.map((e) => e.classes)) === JSON.stringify([['beta-two'], ['alpha-one', 'C9'], [], [], []]) &&
      al[2].endsWith(' | fixVerdict | classes |') && al[4].endsWith(' | beta-two |') && al[5].endsWith(' | alpha-one C9 |') &&
      al.slice(6).every((row) => row.endsWith(' | - |')),
      'ledger: classes resolves each head label to its item slug, keeps C<n> out of range, and renders - when unlabelled')
  }

  // ---- AC6: six exit paths. `confirmed` keeps its per-path type, which unattended-build.js reads.
  const fieldsOk = (run) => !!run.result && Array.isArray(run.result.ledger) && Array.isArray(run.result.confirmedFindings) && typeof run.result.appendix === 'string'
  const paths = [
    ['every lens dead', buildStubs({ 'find:': null }), 'array', (x) => x.ledger.length === 0 && x.appendix === ''],
    ['no finding raised', buildStubs({ 'find:': buildEmptyLens }), 'array', (x) => x.ledger.length === 0 && x.appendix === ''],
    ['every finding refuted', buildStubs({ 'verify:': buildVerdicts('refuted') }), 'array',
      (x) => x.ledger.length === 5 && x.ledger.every((e) => e.verdict === 'refuted') && x.confirmedFindings.length === 0 && x.appendix.split('\n').length === 9],
    ['one skeptic batch dead', buildStubs({ 'verify:ids-2-2': null }), 'integer',
      (x) => x.exit === 'deferred-platform' && x.ledger.length === 5 && x.ledger[1].verdict === 'unverified' && x.confirmedFindings.length === 4],
    ['the synthesis dead', buildStubs({ synth: null }), 'integer', (x) => x.exit === 'deferred-platform' && x.ledger.length === 5 && x.confirmedFindings.length === 5],
    ['complete', ALL_OK, 'integer', (x) => x.exit === 'complete' && x.ledger.length === 5 && x.confirmedFindings.length === 5 && x.appendix.length > 0],
  ]
  // Closing review round 1, L3 (finding 19): `regraded` is an array where a synthesis ran, which is the
  // complete path alone, and ABSENT on the other five, since no adjudicated count exists there.
  let regradedSeen = 0
  const regradedWrong = []
  for (const [what, stubs, ctype, extra] of paths) {
    r = await runReview(DIFF, stubs)
    if (!checkNoThrow(r, 'ledger exit ' + what)) continue
    const typed = ctype === 'array' ? Array.isArray(r.result.confirmed) : Number.isInteger(r.result.confirmed)
    ck(fieldsOk(r) && typed && extra(r.result), 'ledger: every exit path carries the ledger: ' + what)
    regradedSeen++
    if (what === 'complete' ? !Array.isArray(r.result.regraded) : 'regraded' in r.result) regradedWrong.push(what)
  }
  ck(regradedSeen === 6 && regradedWrong.length === 0,
    'severity: regraded is returned only where a synthesis ran, over the six exit paths' + (regradedWrong.length ? ' — wrong on: ' + regradedWrong.join(', ') : ''))
}

runWholeScriptArms().then(() => {
  console.log('---- ' + pass + ' passed, ' + fail + ' failed ----')
  process.exit(fail ? 1 : 0)
}, (e) => {
  console.log('HARNESS-BROKEN the whole-script arms threw: ' + e.message)
  console.log('---- ' + pass + ' passed, ' + (fail + 1) + ' failed ----')
  process.exit(2)
})
JSEOF

out=$(node "$TMP/run.js" "$ROOT/$FILE"); rc=$?
printf '%s\n' "$out"

# The arms run inside a node process, so the count crosses a process boundary and this shell cannot
# see an arm that never ran. A `die()` above exits early by design; a block stranded past one would
# shrink the total in silence. The FLOOR is what notices — raise it whenever arms are added.
# RAISED 20 -> 60 by TOOL-dDerivedDocket-29: the whole-script arms execute 40 assertions, 30 call sites
# with the AC3 pair run once per each of six key components. COUNTED off the block, not off a suite
# run: the pass that wrote them runs no suite.
# RAISED 60 -> 77 by TOOL-aSightedSkeptic-5: 17 assertions, counted off the block the same way — the
# lensNotes key component's AC3 pair (2), the lens set (1), note placement (2), six malformed values
# and their control (7), the announced absence (2) and the review-shape rewrite (3).
# RAISED 77 -> 84 by TOOL-aSightedSkeptic-1: 7 assertions, counted off the block — the briefed skeptic
# (1), the shared brief on a diff and a spec run (2), the pre-existing rule (1), the spec skeptic's
# subjects (1) and the fold round, skeptic and finder halves (2).
# RAISED 84 -> 100 by TOOL-aSightedSkeptic-3: 16 assertions, counted off the block — the specs key
# component's AC3 pair (2), specs in every prompt (1), the commit-log default (1), the announced
# absence and its control (2), eight refused values (8) and the spec-audit overlap and sibling arms (2).
# RAISED 100 -> 117 by TOOL-aSightedSkeptic-4: 17 assertions, counted off the block — the checklist
# key component's AC3 pair (2), the string split (1), the CRLF twin and the array (2), the log line and
# the empty share (2), absent, empty and the control (3), six refused values (6) and the spec audit (1).
# RAISED 117 -> 123 by TOOL-aSightedSkeptic-2: 6 assertions, counted off the block — the fix in every
# verify prompt (1), the schema (1), unsound with and without a note (2), the unjudged count (1) and
# the batch print over the fix (1).
# RAISED 123 -> 130 by TOOL-aSightedSkeptic-6: 7 assertions, counted off the block — the rubric in every
# prompt (1), the schema (1), the binding grade (1), the ungraded fallback (1), the uncertain verdict
# (1), the regraded return (1) and the uncertain rule in every verify prompt (1).
# RAISED 130 -> 145 by TOOL-aSightedSkeptic-7: 15 assertions, counted off the block — six prelude
# intensity arms (6), the light lens set (1), a skip neither live nor dead, complete and all-dead (2),
# the light and full announcements (2), the key by intensity (1), two LIGHT_LENSES rewrites (2) and the
# checklist over the running lenses (1).
# RAISED 145 -> 165 by TOOL-aSightedSkeptic-8: 20 assertions, counted off the block — the dispatching
# lens on a complete, an echoing and a reused run (3), the lens on the verify, synthesis and deferred-log
# lines (3), the verdict states and their null fields (2), confirmedFindings, the rejected fix and the
# round-2 hand-off (3), the appendix table, its escaping and the synthesis hand-off (3) and six exit paths (6).
# RAISED 165 -> 175 by the closing review's round-1 fold of the harness-side mediums and lows: 10
# assertions, counted off the block — two refused specs values (2), the unindented continuation (1), the
# reason-only unsound verdict (1), the three fix verdicts together (1), the unread skipped-lens note (1),
# the empty and blank unsound notes (2), the splitlines boundaries in a cell (1) and regraded per exit path (1).
# RAISED 175 -> 180 by TOOL-aSightedSkeptic-10: 5 assertions, counted off the block — the synthesis-death
# log's binding grade and rendered fix (2), the deferred log's binding grade (1), one uncertain answer
# apart from no verdict (1) and an all-uncertain note (1).
# RAISED 180 -> 181 by TOOL-aMendedFleet-17: 1 assertion, the ledger's `classes` and the appendix's
# ninth column over labelled, out-of-range and unlabelled claims (1).
FLOOR_ASSERTIONS=181
executed=$(printf '%s\n' "$out" | sed -n 's/^---- \([0-9][0-9]*\) passed.*/\1/p' | tail -1)
if [ -z "$executed" ]; then
  echo "FAIL the runner printed no assertion count at all — it died before its summary line"
  exit 1
fi
if [ "$executed" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL executed $executed assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an early exit or a die()"
  exit 1
fi
n=$executed
[ "$rc" = 0 ] && echo "PASS ($n assertions)"
exit $rc

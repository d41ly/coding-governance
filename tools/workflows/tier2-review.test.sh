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

KIT_REL="${KIT_REL:-tools/workflows}"
set -u
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
async function runReview(args, stubs) {
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
    result = await new AsyncFunction('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'workflow', whole)(
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
// One finding per lens, so four lenses make four ids and four batches of one: verify:ids-1-1 .. 4-4.
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
  ck(finds.length === 4 && finds.every((t) => t.prompt.indexOf('/review-lenses/' + K + '/find-' + t.label.slice(5) + '.json') !== -1),
    'AC1 every find: prompt names review-lenses/<key>/find-<lens>.json')
  ck(verifies.length === 4 && verifies.every((t) => {
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
    ck(sf.length === 4 && sf.every((t) => t.schema && t.schema.required.indexOf('path') !== -1 && t.schema.required.indexOf('where') !== -1 &&
      t.prompt.indexOf('/review-lenses/' + rs.result.key + '/find-') !== -1),
      'AC1 the spec finding schema lists path in required, and every spec lens prompt names its file')
  }

  // ---- AC4: a DEAD probe reuses nothing, dispatches every lens and says so.
  r = await runReview(DIFF, buildStubs({ 'resume:probe': null }))
  if (checkNoThrow(r, 'dead probe')) {
    ck(r.scanSpawned('find:').length === 4, 'AC4 a dead probe dispatches all four lenses')
    ck(r.logs.some((l) => l.indexOf('nothing could be reused') !== -1), 'AC4 ...and the log says nothing could be reused')
  }

  // ---- AC2: two lenses die; the re-run is fed the two survivors' files and dispatches exactly two.
  r = await runReview(DIFF, buildStubs({ 'find:seams': null, 'find:regressions': null }))
  let k2 = ''
  if (checkNoThrow(r, 'two dead lenses')) {
    k2 = r.result.key
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:seams find:regressions',
      'AC2 the first run defers, pending the two dead lenses')
  }
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe([buildLensFile('security', k2), buildLensFile('correctness', k2)]) }))
  if (checkNoThrow(r, 'two-survivor re-run')) {
    ck(r.scanSpawned('find:').join(' ') === 'find:seams find:regressions', 'AC2 the re-run with identical args spawns exactly the two missing lenses: ' + r.scanSpawned('find:').join(' '))
    ck(r.result.exit === 'complete' && r.result.lensesReused === 2, 'AC2 ...and completes, reporting two lenses reused')
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
  const allLensFiles = ['security', 'correctness', 'seams', 'regressions'].map((l) => buildLensFile(l, K))
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
    ck(r.result.exit === 'deferred-platform' && r.result.blockers === null && r.result.pending.length === 4 &&
      r.result.pending.every((p) => p.indexOf('find:') === 0), 'AC6 every lens dead: deferred-platform, blockers null, four find: labels pending')
  }
  r = await runReview(DIFF, buildStubs({ 'find:': buildEmptyLens, 'find:security': null, 'find:seams': null }))
  if (checkNoThrow(r, 'AC6 two dead, survivors empty')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:security find:seams' && !/^(clean|partial)/.test(r.result.note),
      'AC6 two lenses dead and the survivors found nothing: deferred, those two pending, a note that is neither clean nor partial')
  }
  r = await runReview(DIFF, buildStubs({ 'find:regressions': null, 'verify:': buildVerdicts('refuted') }))
  if (checkNoThrow(r, 'AC6 one dead, all refuted')) {
    ck(r.result.exit === 'deferred-platform' && r.result.pending.join(' ') === 'find:regressions' && !/^(clean|partial)/.test(r.result.note),
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
FLOOR_ASSERTIONS=60
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

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
// The stop is the line after the `}` closing the base-shape ladder, found from `const baseLooksPinned`:
// AT that line the ladder is excluded, and a stop on a line above it strands what moves below it.
const metaEnd = lines.findIndex((l) => l === '}')
const ladder = lines.findIndex((l) => l.startsWith('const baseLooksPinned'))
if (metaEnd === -1) die('could not find the end of the `meta` block — the extraction anchor moved, and an empty body would pass every arm below')
if (ladder === -1) die('could not find `const baseLooksPinned`, the line the stop after the `if (!baseLooksPinned)` ladder is found from — the extraction anchor moved, and an empty body would pass every arm below')
const stop = lines.findIndex((l, i) => i > ladder && l === '}') + 1
if (stop === 0) die('could not find the `}` closing the `if (!baseLooksPinned)` ladder below `const baseLooksPinned` — the extraction anchor moved, and an empty body would pass every arm below')
if (stop <= metaEnd) die('the extraction anchors are out of order (' + metaEnd + ' then ' + stop + ')')
const body = lines.slice(metaEnd + 1, stop).join('\n')
for (const needed of ['badSubject', 'const a = cfg', 'baseLooksPinned']) {
  if (!body.includes(needed)) die('the extracted prelude is missing `' + needed + '` — the arms would pass by finding nothing')
}
ck(true, 'the prelude extraction is live (' + (stop - metaEnd - 1) + ' lines, all three validators present)')

// ---- one arm ----------------------------------------------------------------------------------
const BLOB = 'abc1234'
const SHA = 'a'.repeat(40)
// `scratch` rides every arm (TOOL-aEvidencedLens-2 S7): a spec audit refuses without it, and a diff
// review never reads it, so carrying it here reds no arm and leaves every proceeding spec arm proceeding.
const base = { repo: '/tmp/r', reviewDir: 'memory/reviews', unitIds: ['TOOL-x-1'], base: SHA, head: SHA, scratch: '/tmp/s' }
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
arm('falsy then genuinely bad, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [null, { path: 'memory/builds/dX/spec/a.md', blob: 'zzz' }] }, SHAPE)
arm('a non-object subject, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: ['a.md'] }, SHAPE)

// The malformed-blob ladder is UNCHANGED: warn at round 1, refuse above it. Both halves, because
// an arm asserting only the refusal is satisfied by a checker that refuses everything.
arm('malformed blob, round 1 -> warns and proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: 'zzz', id: 'TOOL-x-1', rev: 1 }] }, null)
arm('malformed blob, round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: 'zzz' }] }, SHAPE)
arm('a good subject, round 1 -> proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1 }] }, null)
arm('a good subject, round 2 -> proceeds', { kind: 'spec-audit', round: 2, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1 }] }, null)

// The kind is a CLOSED set, and the diff-review default owes none of the above.
arm('diff-review with no subjects -> untouched', { round: 1 }, null)
arm('an unknown kind -> refused', { kind: 'code-review', round: 1 }, 'kind')

// The base-shape LADDER, which this suite claimed before it reached it. Same shape as the subject
// ladder: warn at round 1, refuse above it — and a spec audit short-circuits it entirely, because
// a spec has no commit range and its anchor is the per-subject blob instead.
arm('a moving ref as base, round 1 -> warns and proceeds', { round: 1, base: 'origin/main' }, null)
arm('a moving ref as base, round 2 -> refused', { round: 2, base: 'origin/main' }, MOVING)
arm('a spec audit ignores base entirely', { kind: 'spec-audit', round: 2, base: 'origin/main', subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1 }] }, null)
// TOOL-dLadderedRemote-4 — a diff review's base is REQUIRED: it used to default to a literal remote
// ref, which names nothing on a node whose remote is called something else. Absent and blank are both
// refused before any agent; a spec audit has no range and still owes none.
const NO_BASE = 'a diff review needs `base`'
arm('a diff review with no base -> refused', { round: 1, base: undefined }, NO_BASE)
arm('a diff review with a blank base -> refused', { round: 1, base: '  ' }, NO_BASE)
arm('a spec audit with no base -> proceeds', { kind: 'spec-audit', round: 1, base: undefined, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1 }] }, null)

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
const GOOD_SPEC = { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1 }] }
armIntensity('intensity: an unknown value is refused', { intensity: 'medium' }, 'refused')
armIntensity('intensity: a non-string is refused', { intensity: 7 }, 'refused')
armIntensity('intensity: light on a diff review proceeds', { intensity: 'light' }, 'light')
armIntensity('intensity: absent proceeds', {}, 'full')
armIntensity('intensity: light on a spec audit is refused', Object.assign({ intensity: 'light' }, GOOD_SPEC), 'refused')
armIntensity('intensity: full on a spec audit proceeds', Object.assign({ intensity: 'full' }, GOOD_SPEC), 'full')

// ---- TOOL-dFairHearing-2 AC1 — `preset`, a closed set read in the prelude, refused beside the diff kind ----
// The proceeding arms read the RESOLVED value back, so none passes over a prelude that never reads
// `preset`: on the base render the read throws `preset is not defined`, a harness fault. A refusal must
// START `tier2-review: \`preset\`` and carry its word, so an unrelated throw cannot satisfy one.
const DESIGN_SPEC = { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/build/a.md', blob: BLOB, id: 'PLAY-dX-1' }] }
function armPreset(name, extra, want, word) {
  let got = null
  let threw = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn preset')(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === 'refused' ? !!threw && threw.indexOf('tier2-review: `preset`') === 0 && threw.indexOf(word) !== -1 : !threw && got === want,
    name + (threw ? ' (threw: ' + threw + ')' : ' (resolved ' + JSON.stringify(got) + ')'))
}
armPreset('preset: design-audit over a design subject proceeds', Object.assign({ preset: 'design-audit' }, DESIGN_SPEC), 'design-audit')
armPreset('preset: absent on a spec audit is unit-spec', DESIGN_SPEC, 'unit-spec')
armPreset('preset: absent on a diff review is unit-spec', {}, 'unit-spec')
armPreset('preset: an unknown preset is refused naming the set', Object.assign({ preset: 'no-such-preset' }, DESIGN_SPEC), 'refused', 'unit-spec | design-audit')
armPreset('preset: a non-string is refused', Object.assign({ preset: 7 }, DESIGN_SPEC), 'refused', 'unit-spec | design-audit')
armPreset('preset: an empty string is refused', Object.assign({ preset: '' }, DESIGN_SPEC), 'refused', 'unit-spec | design-audit')
armPreset('preset: unit-spec beside the diff kind is refused naming it', { kind: 'diff-review', preset: 'unit-spec' }, 'refused', 'diff-review')

// ---- TOOL-dFairHearing-3 AC1 — `optIn`'s SHAPE, refused in the prelude before the literals read it ----
// The proceeding arm reads the RESOLVED value back, so it cannot pass over a prelude that never reads
// `optIn`: on the base render the read throws `optIn is not defined`, a harness fault. A refusal must
// START `tier2-review: \`optIn\``, so an unrelated throw cannot satisfy one.
function armOptIn(name, value, want) {
  let got = null
  let threw = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn optIn')(Object.assign({}, base, GOOD_SPEC, { optIn: value }), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === 'refused' ? !!threw && threw.indexOf('tier2-review: `optIn`') === 0 : !threw && JSON.stringify(got) === want,
    name + (threw ? ' (threw: ' + threw + ')' : ' (resolved ' + JSON.stringify(got) + ')'))
}
armOptIn('optIn: {} proceeds', {}, '{}')
armOptIn('optIn: absent proceeds as {}', undefined, '{}')
armOptIn('optIn: an array is refused', [], 'refused')
armOptIn('optIn: a non-string value is refused', { topology: 7 }, 'refused')
armOptIn('optIn: a key outside the lens-key grammar is refused', { 'Topology!': 'reuse' }, 'refused')
armOptIn('optIn: null is refused', null, 'refused')

// ---- TOOL-dFairHearing-4 AC1-AC4 — the address key, its equality and order, and `batchBy` ----------
// Each arm reads a name the base harness does not define, so on the base it throws `... is not defined`,
// a harness fault counted as a failure. The proceeding `batchBy` arms read the RESOLVED value back.
function evalAddress(extra, ret) {
  try {
    return new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn ' + ret)(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { console.log('HARNESS-BROKEN address: ' + ret + ' -> ' + e.message); return null }
}
{
  const dfn = evalAddress({}, '[deriveAddressKey, checkSameAddress, deriveAddressOrder]')
  const sfn = evalAddress(GOOD_SPEC, '[deriveAddressKey, checkSameAddress, deriveAddressOrder]')
  if (!dfn || !sfn) fail++
  else {
    const dk = (file, line) => dfn[0]({ file: file, line: line, lens: 'l', id: 1 })
    const sk = (where) => sfn[0]({ file: 'x.md', where: where, lens: 'l', id: 1 })
    ck(JSON.stringify(dfn[0]({ file: '.\\src\\a.js', line: 12, lens: 'security', id: 3 })) === JSON.stringify({ file: 'src/a.js', at: 12, lens: 'security', id: 3 }),
      'address: a diff finding keys to its slash-folded file, its line, its lens and its id')
    const wants = [['section 4 [walk-table] Design', '[walk-table]'], ['section 2 S5', '§2'], ['AC3 against section 6', 'AC3'], ['§ 7', '§7'], ['status header', null]]
    const gots = wants.map((w) => sk(w[0]).at)
    ck(gots.every((g, i) => g === wants[i][1]), 'address: a spec finding keys its first [tag], else its leftmost section token, else null: ' + JSON.stringify(gots))
    ck(dfn[1](dk('a.js', 10), dk('a.js', 13)) && !dfn[1](dk('a.js', 10), dk('a.js', 14)) && !dfn[1](dk('a.js', 10), dk('b.js', 10)),
      'address: diff lines within 3 on one file are one address, 4 apart or on two files are not')
    const nk = dk('a.js', undefined)
    ck(nk.at === null && !dfn[1](nk, nk) && !dfn[1](nk, dk('a.js', 10)), 'address: a key with no address matches nothing, itself included')
    ck(sfn[1](sk('section 2'), sk('§2')) && !sfn[1](sk('§2'), sk('§3')), 'address: spec keys at one token are one address, at two are not')
    const six = [{ id: 1, file: 'a.js', line: 100, lens: 'security' }, { id: 2, file: 'c.js', line: 5, lens: 'security' }, { id: 3, file: 'b.js', line: 7, lens: 'correctness' },
      { id: 4, file: 'a.js', line: 42, lens: 'correctness' }, { id: 5, file: 'b.js', line: 7, lens: 'seams' }, { id: 6, file: 'a.js', line: 42, lens: 'intent' }]
    const ord = dfn[2](six)
    ck(ord !== six && ord.map((f) => f.id).join(',') === '4,6,1,3,5,2' && six.map((f) => f.id).join(',') === '1,2,3,4,5,6',
      'address: the order is file, line by value, lens and id, in a new array, the argument left in id order: ' + ord.map((f) => f.id).join(','))
    const sord = sfn[2]([{ id: 1, file: 'x.md', where: 'status header', lens: 'a' }, { id: 2, file: 'x.md', where: '§9', lens: 'b' }, { id: 3, file: 'w.md', where: '', lens: 'c' }])
    ck(sord.map((f) => f.id).join(',') === '3,2,1', 'address: a spec finding with no address sorts after every addressed finding of its file: ' + sord.map((f) => f.id).join(','))
    // TOOL-dFairHearing-32 AC2 - the section class is `section ?<n>` or `§ ?<n>`, any case, each as `§<n>`.
    // RED against a class that requires the space, which keys `§4` and `section4` to null.
    const secs = ['§4', 'Section 3 Design', 'section4', '§ 4', 'SECTION 12'].map((w) => sk(w).at)
    ck(secs.join(' ') === '§4 §3 §4 §4 §12', 'address: FH32 AC2 the section forms key as §4 §3 §4 §4 §12: ' + JSON.stringify(secs))
  }
}
// ---- TOOL-dFairHearing-23 AC39 — a repo-absolute path, its repo-relative spelling and a lower-case drive key as one file.
// RED against the parent, whose key keeps the repo prefix, so the three keys differ.
{
  const rfn = evalAddress({ repo: 'C:/R' }, '[deriveAddressKey]')
  const files = rfn ? ['C:/R/src/a.js', 'src/a.js', 'c:/R/src/a.js'].map((file) => rfn[0]({ file: file, line: 1, lens: 'l', id: 1 }).file) : []
  ck(files.length === 3 && files.every((x) => x === 'src/a.js'), 'FH23 AC39 address: under repo C:/R the three spellings key as src/a.js: ' + JSON.stringify(files))
}
// A closed-set argument `field`: a proceeding arm reads the RESOLVED value back, a refusal must name `field`.
function armClosedSet(field, name, extra, want) {
  let got = null
  let threw = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn ' + field)(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === 'refused' ? !!threw && threw.indexOf('tier2-review: `' + field + '`') === 0 : !threw && got === want, name + (threw ? ' (threw: ' + threw + ')' : ' (resolved ' + JSON.stringify(got) + ')'))
}
armClosedSet('batchBy', 'batchBy: absent resolves to id', {}, 'id')
armClosedSet('batchBy', 'batchBy: id proceeds', { batchBy: 'id' }, 'id')
armClosedSet('batchBy', 'batchBy: address proceeds', { batchBy: 'address' }, 'address')
armClosedSet('batchBy', 'batchBy: section is refused', { batchBy: 'section' }, 'refused')
armClosedSet('batchBy', 'batchBy: a number is refused', { batchBy: 1 }, 'refused')
armClosedSet('batchBy', 'batchBy: null is refused', { batchBy: null }, 'refused')

// ---- TOOL-dFairHearing-7 AC1/AC2 — deriveTwinPairs over the address key, and `addressTwins` ----------
// On the base harness neither name is defined, a harness fault counted as a failure, and `'on'` proceeds.
{
  const dtp = evalAddress({}, 'deriveTwinPairs')
  const stp = evalAddress(GOOD_SPEC, 'deriveTwinPairs')
  if (!dtp || !stp) fail++
  else {
    const df = (id, file, line) => ({ id: id, file: file, line: line, lens: 'l' })
    const dgot = dtp([df(1, 'a.js', 10)], [df(2, 'a.js', 12), df(3, 'a.js', 14), df(4, 'b.js', 10)])
    ck(JSON.stringify(dgot) === JSON.stringify([{ confirmed: 1, refuted: 2 }]),
      'twins: a confirmed a.js:10 pairs with a refuted a.js:12 alone, not a.js:14 nor b.js:10: ' + JSON.stringify(dgot))
    const sf = (id, where) => ({ id: id, file: 'x.md', where: where, lens: 'l' })
    const sgot = stp([sf(1, 'section 2 S5'), sf(3, 'status header')], [sf(2, '§2'), sf(4, 'status header')])
    ck(JSON.stringify(sgot) === JSON.stringify([{ confirmed: 1, refuted: 2 }]),
      'twins: a spec finding at `section 2 S5` pairs with one at `§2`, and `status header` pairs with nothing: ' + JSON.stringify(sgot))
  }
}
armClosedSet('addressTwins', 'addressTwins: absent resolves to shown', {}, 'shown')
armClosedSet('addressTwins', 'addressTwins: hidden proceeds', { addressTwins: 'hidden' }, 'hidden')
armClosedSet('addressTwins', 'addressTwins: shown proceeds', { addressTwins: 'shown' }, 'shown')
armClosedSet('addressTwins', "addressTwins: 'on' is refused", { addressTwins: 'on' }, 'refused')
armClosedSet('addressTwins', 'addressTwins: true is refused', { addressTwins: true }, 'refused')

// ---- TOOL-aEvidencedLens-2 AC3 — `scratch`, required on a spec audit and refused by shape ---------
// The proceeding arms read the RESOLVED value back, so none passes over a prelude that never reads
// `scratch`: on the base render the read throws `scratch is not defined`, a harness fault. A refusal
// must START `tier2-review:` and name `scratch`, so an unrelated throw cannot satisfy one.
function armScratch(name, extra, want) {
  let got = null
  let threw = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn scratch')(Object.assign({}, base, extra), () => {}, null, null, null)
  } catch (e) { threw = e.message }
  if (threw && /has already been declared|is not defined|Unexpected|Invalid or unexpected/.test(threw)) {
    console.log('HARNESS-BROKEN ' + name + ' -> ' + threw)
    fail++
    return
  }
  ck(want === 'refused' ? !!threw && threw.indexOf('tier2-review:') === 0 && threw.indexOf('`scratch`') !== -1 : !threw && got === want,
    name + (threw ? ' (threw: ' + threw + ')' : ' (resolved ' + JSON.stringify(got) + ')'))
}
armScratch('spec scratch: absent is refused', Object.assign({ scratch: undefined }, GOOD_SPEC), 'refused')
armScratch('spec scratch: a relative path is refused', Object.assign({ scratch: 'tmp/s' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: a multi-line value is refused', Object.assign({ scratch: '/tmp/s\nX' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: equal to repo is refused', Object.assign({ scratch: '/tmp/r' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: repo with a trailing slash is refused', Object.assign({ scratch: '/tmp/r/' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: under repo is refused', Object.assign({ scratch: '/tmp/r/sub' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: under repo by case and backslash is refused', Object.assign({ repo: 'c:/r', scratch: 'C:\\R\\x' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: an absolute path outside repo proceeds', GOOD_SPEC, '/tmp/s')
armScratch('spec scratch: a sibling sharing the repo prefix proceeds', Object.assign({ scratch: '/tmp/rs' }, GOOD_SPEC), '/tmp/rs')
armScratch('spec scratch: a Windows path proceeds, folded to forward slashes', Object.assign({ scratch: 'C:\\t\\s' }, GOOD_SPEC), 'C:/t/s')
armScratch('spec scratch: a diff review never reads it', { scratch: 7 }, '')
// TOOL-aEvidencedLens-21 AC1 (closing review M1, replay id 38) - the under-`repo` test is textual, so a
// relative `repo`, either MSYS spelling and a `..` segment are refused by name. Each of the four proceeded
// on the base render; the two controls and the diff kind's relative `repo` still proceed.
armScratch('spec scratch: a relative repo is refused', Object.assign({ repo: '.', scratch: 'C:/projects/x/tmp' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: under a drive repo by its MSYS spelling is refused', Object.assign({ repo: 'C:/p/x', scratch: '/c/p/x/t' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: under an MSYS repo by its drive spelling is refused', Object.assign({ repo: '/c/p/x', scratch: 'C:/p/x/t' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: a .. segment is refused', Object.assign({ repo: '/tmp/r', scratch: '/tmp/q/../r/x' }, GOOD_SPEC), 'refused')
armScratch('spec scratch: a drive path outside a drive repo proceeds', Object.assign({ repo: 'C:/p/x', scratch: 'C:/t/s' }, GOOD_SPEC), 'C:/t/s')
armScratch('spec scratch: a diff review keeps a relative repo', { repo: '.', scratch: 7 }, '')

// ---- TOOL-aEvidencedLens-4 AC1 — `prevBlob`, refused malformed and refused at round 1 (spec F1) ----
// A refusal names `prevBlob`, so the subject ladder's own `needs \`subjects\`` throw cannot satisfy one.
const PREV = '`prevBlob`'
arm('fold: a malformed prevBlob at round 2 -> refused', { kind: 'spec-audit', round: 2, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1, prevBlob: 'zz' }] }, PREV)
arm('fold: a well-formed prevBlob at round 1 -> refused', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1, prevBlob: 'abc1235' }] }, PREV)
arm('fold: a well-formed prevBlob at round 2 -> proceeds', { kind: 'spec-audit', round: 2, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 1, prevBlob: 'abc1235' }] }, null)
arm('fold: a diff review ignores a bad prevBlob', { round: 1, subjects: [{ path: 'a.md', blob: BLOB, prevBlob: 'zz' }] }, null)

// ---- TOOL-dTrueNorth-5 AC1 — the PIN. A spec-audit subject carries `id` and `rev`, and a subject
// missing or malforming either is refused at EVERY round, round 1 included, naming the field: the
// record pins `<id>@rev-<rev>`, so an unpinned subject would write the record this refusal stops.
// Against the base harness each refusal below proceeds instead.
const PIN_REV = '`rev`'
const PIN_ID = '`id`'
arm('pin: a subject with no rev, round 1 -> refused naming rev', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1' }] }, PIN_REV)
arm('pin: a subject with no rev, round 2 -> refused naming rev', { kind: 'spec-audit', round: 2, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1' }] }, PIN_REV)
arm('pin: rev 0 -> refused naming rev', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 0 }] }, PIN_REV)
arm("pin: rev '2', a string -> refused naming rev", { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: '2' }] }, PIN_REV)
arm("pin: id 'x-1', outside the id grammar -> refused naming id", { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'x-1', rev: 2 }] }, PIN_ID)
arm('pin: a subject with no id -> refused naming id', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, rev: 2 }] }, PIN_ID)
arm('pin: two subjects sharing an id -> refused naming the repeat', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 2 }, { path: 'memory/builds/dX/spec/b.md', blob: 'abc1235', id: 'TOOL-x-1', rev: 1 }] }, 'repeats subject 0')
arm('pin: a pinned subject proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 2 }] }, null)
// ---- TOOL-dTrueNorth-5 AC2 — the binding line is the harness's render, pure, inside this prelude.
{
  let rendered = null
  try {
    const rab = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn renderAuditBinding')(
      Object.assign({}, base, { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 2 }] }), () => {}, null, null, null)
    rendered = rab([{ path: 'memory/builds/dX/spec/a.md', id: 'TOOL-x-1', rev: 3 }, { path: 'memory/builds/dX/spec/b.md', id: 'TOOL-x-2', rev: 1 }])
  } catch (e) { rendered = 'threw: ' + e.message }
  ck(rendered === '**Serves:** spec-audit TOOL-x-1@rev-3 TOOL-x-2@rev-1',
    'pin: renderAuditBinding pins each subject in subject order: ' + JSON.stringify(rendered))
}
// ---- TOOL-dTrueNorth-20 AC13 (S14) — THE PRODUCER PINS THE READER'S LITERAL. The memory-tree kit's
// gen_build_index.py exempts a spec-audit record whose harness, at its adding commit, defines no function
// named by its AUDIT_WRITER_MARK constant, its one spelling of it. This arm reads that constant out of the
// file and asserts this harness defines the function, so renaming it reds THIS suite, before the reader
// is stranded and every unpinned record reads as an older harness's. The kit is the one the gotchas arms
// resolve, passed as the third argument; a kit that is not there fails the arm naming why.
{
  const mtd = process.argv[4] || ''
  let mark = null
  let why = ''
  try {
    const m = /^AUDIT_WRITER_MARK = "([A-Za-z_$][\w$]*)"\s*$/m.exec(fs.readFileSync(require('path').join(mtd, 'gen_build_index.py'), 'utf8'))
    if (m) mark = m[1]
    else why = 'gen_build_index.py spells no AUDIT_WRITER_MARK = "<name>" line'
  } catch (e) { why = "the memory-tree kit's gen_build_index.py could not be read: " + e.message }
  const defined = mark !== null && new RegExp('^(?:export\\s+)?(?:async\\s+)?function\\s+' + mark.replace(/\$/g, '\\$') + '\\s*\\(', 'm').test(src)
  ck(defined, 'mark: the harness defines the function AUDIT_WRITER_MARK names in gen_build_index.py (' + (mark || why) +
    '), so a rename reds here before it strands that reader')
}
// ---- TOOL-dTrueNorth-13 AC1 — TWO subject classes, told apart by path. A subject whose path holds no
// builds/<slug>/spec/ segment is a DESIGN subject: its id is required in the same grammar, a `rev` on it
// is refused naming the field, and it is exempt from the repeat refusal, which runs over spec subjects
// only. Against the harness TOOL-dTrueNorth-5 left, both proceeding arms below are refused for a rev.
const DESIGN_A = { path: 'memory/builds/dX/build/a.md', blob: 'abc1234', id: 'PLAY-dX-1' }
const DESIGN_B = { path: 'memory/builds/dX/build/b.md', blob: 'def5678', id: 'PLAY-dX-1' }
arm('design: two design subjects sharing an id, no rev, round 1 -> proceeds', { kind: 'spec-audit', round: 1, subjects: [DESIGN_A, DESIGN_B] }, null)
arm('design: a rev on a design subject -> refused naming rev', { kind: 'spec-audit', round: 1, subjects: [Object.assign({ rev: 2 }, DESIGN_A), DESIGN_B] }, PIN_REV)
arm('design: a design subject with no id -> refused naming id', { kind: 'spec-audit', round: 1, subjects: [{ path: DESIGN_A.path, blob: BLOB }] }, PIN_ID)
arm('design: a design subject beside the spec of its own id -> proceeds', { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/p.md', blob: BLOB, id: 'PLAY-dX-1', rev: 2 }, DESIGN_A] }, null)
// ---- TOOL-dTrueNorth-13 AC2 — the mixed binding and the subjects line, both the harness's pure renders.
{
  let rendered = null
  let reviewed = null
  let firstBare = null
  try {
    const fns = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn [renderAuditBinding, renderReviewedLine]')(
      Object.assign({}, base, { kind: 'spec-audit', round: 1, subjects: [DESIGN_A] }), () => {}, null, null, null)
    const MIXED = [{ path: 'memory/builds/dX/spec/x.md', blob: 'aaa1111', id: 'TOOL-x-1', rev: 3 }, DESIGN_A, DESIGN_B]
    rendered = fns[0](MIXED)
    reviewed = fns[1](MIXED)
    firstBare = fns[0]([DESIGN_A, { path: 'memory/builds/dX/spec/p.md', blob: BLOB, id: 'PLAY-dX-1', rev: 2 }])
  } catch (e) { rendered = 'threw: ' + e.message }
  ck(rendered === '**Serves:** spec-audit TOOL-x-1@rev-3 PLAY-dX-1',
    'design: renderAuditBinding pins the spec subject and serves the shared design id once, bare: ' + JSON.stringify(rendered))
  ck(reviewed === 'Reviewed: memory/builds/dX/spec/x.md@aaa1111, memory/builds/dX/build/a.md@abc1234, memory/builds/dX/build/b.md@def5678',
    'design: renderReviewedLine names every subject as path@blob in subject order: ' + JSON.stringify(reviewed))
  ck(firstBare === '**Serves:** spec-audit PLAY-dX-1@rev-2',
    'design: an id a spec subject pins is never repeated bare, even where a design subject names it first: ' + JSON.stringify(firstBare))
}

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
// TOOL-dTrueNorth-5 AC1 — `id` and `rev` are fields of a SUBJECT, not of `a`, so the arm above cannot see
// them; the header's `subjects:` key line names both, as the refusal reads them.
const subjectsKey = (hdr.match(/^\/\/\s+subjects:.*$/m) || [''])[0]
ck(/\bid\b/.test(subjectsKey) && /\brev\b/.test(subjectsKey), 'pin: the args header documents a spec-audit subject\'s id and rev: ' + subjectsKey)

// ---- TOOL-dFairHearing-17 AC1-AC4 — the round state's pure rule, its record line, and its two arguments.
// The rule and the renderer are prelude functions, reached through the extracted body. Against the base
// harness, which defines no deriveRoundState and reads neither argument, every arm below reds.
const RS_SPEC = { kind: 'spec-audit', subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: BLOB, id: 'TOOL-x-1', rev: 2 }] }
let roundFns = null
try {
  roundFns = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn [deriveRoundState, renderRoundLine]')(
    Object.assign({}, base, RS_SPEC, { round: 1 }), () => {}, null, null, null)
} catch (e) { console.log('HARNESS-BROKEN round state: the prelude did not yield deriveRoundState -> ' + e.message) }
const ROUND_ROWS = [
  // AC1 - the planted flat and oscillating sequences stop; their strictly falling twins do not.
  ['flat', [3], 3, 5, 'NON-CONVERGENT'], ['oscillating', [2, 1], 2, 5, 'NON-CONVERGENT'],
  ['falling twin of flat', [3], 2, 5, 'CONVERGING'], ['falling twin of oscillating', [3, 2], 1, 5, 'CONVERGING'],
  // AC2 - the bound at the caller's limit, the ceiling one run past it, and no limit reaching neither.
  ['at the limit', [3, 2], 1, 3, 'BOUNDED'], ['one run past the limit', [4, 3, 2], 1, 3, 'CEILING'],
  ['under the limit', [3], 2, 3, 'CONVERGING'], ['no limit', [3, 2], 1, null, 'CONVERGING'],
  // AC3 - zero first, past the limit too; round 1's bound and its non-terminal twin.
  ['clean round 1', [], 0, 3, 'CONVERGED'], ['clean after a fall', [2, 1], 0, 3, 'CONVERGED'], ['clean past the limit', [4, 3, 2], 0, 3, 'CONVERGED'],
  ['round 1 at a limit of 1', [], 2, 1, 'BOUNDED'], ['round 1 under a limit of 3', [], 2, 3, 'CONVERGING'],
]
for (const [what, prior, count, limit, want] of ROUND_ROWS) {
  const got = roundFns ? roundFns[0](prior, count, limit) : 'no function'
  ck(got === want, 'round state: ' + what + ' deriveRoundState(' + JSON.stringify(prior) + ', ' + count + ', ' + limit + ') is ' + want + ': ' + got)
}
{
  const line = roundFns ? roundFns[1]({ round: 1, roundLimit: null, priorCounts: [], roundCount: null, roundState: null }) : 'no function'
  ck(line === 'review-round round=1 limit=- prior=- count=- state=-', 'round state: renderRoundLine writes every absent value as -, never 0: ' + line)
}
// AC4 - both arguments refused by name, before any agent; a round that disagrees with its prior sequence is refused naming both.
for (const v of [0, 2.5, '3']) arm('round state: roundLimit ' + JSON.stringify(v) + ' -> refused naming roundLimit', Object.assign({}, RS_SPEC, { round: 1, roundLimit: v }), '`roundLimit`')
for (const v of ['x', [1, -1], [1.5]]) arm('round state: priorCounts ' + JSON.stringify(v) + ' -> refused naming priorCounts', Object.assign({}, RS_SPEC, { priorCounts: v }), '`priorCounts`')
arm('round state: round 3 with priorCounts [2] -> refused naming both', Object.assign({}, RS_SPEC, { round: 3, priorCounts: [2] }), '`round` 3 disagrees with `priorCounts`')
arm('round state: round 3 with priorCounts [4, 2] and roundLimit 3 -> proceeds', Object.assign({}, RS_SPEC, { round: 3, priorCounts: [4, 2], roundLimit: 3 }), null)
{
  let inferred = null
  try {
    inferred = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn round')(
      Object.assign({}, base, RS_SPEC, { priorCounts: [4, 2] }), () => {}, null, null, null)
  } catch (e) { inferred = 'threw: ' + e.message }
  ck(inferred === 3, 'round state: with no round, priorCounts [4, 2] makes the evaluated round 3: ' + inferred)
}

// ---- TOOL-dFairHearing-17 AC6 — THE PARITY ARM: deriveRoundState against the driver's review_state.
// The shell block before this runner sliced `review_state()` and the `RUNAWAY_CEILING=` line out of the
// unattended kit's driver and ran them over every row of the domain both can see: 0 to 3 prior counts,
// each 0 to 3, a count of 0 to 3 and a limit of 1 to 4 with the round at or below it. Highs are 0 there,
// so the driver's blocker count and the harness's count are one number. The domain stops at the limit on
// purpose: past it the driver refuses the round outright where the harness reports CEILING, so the two
// answer different questions there, and CEILING lies outside the domain on both sides. The arm asserts
// the four tokens reachable inside it, and AC2's direct case above holds CEILING. A driver that could not
// be read or sliced fails the arm by name; it never skips.
{
  let text = ''
  try { text = fs.readFileSync(process.argv[6] || '', 'utf8') } catch (e) { text = 'PRODUCER-FAILED the driver rows could not be read: ' + e.message }
  const failed = text.indexOf('PRODUCER-FAILED') === 0
  const rows = failed ? [] : text.split('\n').filter((l) => l.trim() !== '').map((l) => l.replace(/\r$/, '').split('|'))
  // The domain, enumerated here independently, so a producer that emitted fewer rows cannot pass.
  let want = 0
  for (let len = 0; len <= 3; len++) want += Math.pow(4, len) * 4 * (4 - len)
  const bad = rows.filter((r) => {
    const prior = r[0] === '' ? [] : r[0].split(' ').map(Number)
    return !roundFns || r.length !== 4 || roundFns[0](prior, Number(r[1]), Number(r[2])) !== r[3]
  })
  ck(!failed && rows.length === want && bad.length === 0,
    'round state: deriveRoundState equals the driver\'s review_state on every one of ' + want + ' rows (' +
      (failed ? text.trim() : rows.length + ' read, ' + bad.length + ' disagree' + (bad.length ? ', first ' + bad[0].join('|') : '')) + ')')
  const seen = new Set(rows.map((r) => r[3]))
  const inDomain = ['CONVERGED', 'NON-CONVERGENT', 'BOUNDED', 'CONVERGING']
  ck(!failed && inDomain.every((t) => seen.has(t)) && !seen.has('CEILING'),
    'round state: the parity rows hold each of the four in-domain tokens and no CEILING: ' + [...seen].sort().join(' '))
}

// ---- TOOL-dFairHearing-18 AC1-AC3 — the `walk` argument, the slicer and the gap check, over the prelude ----
// Against the base harness, which has no whole-design preset and defines neither function, every arm reds:
// the preset itself is refused, so no refusal names `walk`, and reading either function is a harness fault.
const WALK_KEY = 'f'.repeat(64)
const WALK_OK = { items: [{ tag: 'plan.input', step: 's1' }], scenarios: [{ id: 'S1', name: 'the first', walks: 'one path' }], run: 1, keySha: WALK_KEY }
const WALK_SPEC = Object.assign({}, DESIGN_SPEC, { preset: 'whole-design' })
const buildWalk = (over) => Object.assign({}, WALK_SPEC, { walk: Object.assign({}, WALK_OK, over) })
const WALK_NO = 'tier2-review: `walk'
arm('walk: whole-design with no walk -> refused naming walk', WALK_SPEC, 'tier2-review: `walk`')
arm('walk: a walk under preset unit-spec -> refused naming walk', Object.assign({}, DESIGN_SPEC, { preset: 'unit-spec', walk: WALK_OK }), 'tier2-review: `walk`')
arm('walk: runs 0 -> refused naming walk.runs', buildWalk({ runs: 0 }), WALK_NO + '.runs`')
arm('walk: runs 4 -> refused naming walk.runs', buildWalk({ runs: 4 }), WALK_NO + '.runs`')
arm('walk: run 3 past runs 2 -> refused naming walk.run', buildWalk({ runs: 2, run: 3 }), WALK_NO + '.run`')
arm('walk: seed x -> refused naming walk.seed', buildWalk({ seed: 'x' }), WALK_NO + '.seed`')
arm('walk: a seeded walk with no keySha -> refused naming walk.keySha', buildWalk({ keySha: undefined }), WALK_NO + '.keySha`')
arm('walk: a 63-hex keySha -> refused naming walk.keySha', buildWalk({ keySha: 'f'.repeat(63) }), WALK_NO + '.keySha`')
arm('walk: an item tag carrying a newline -> refused naming walk.items', buildWalk({ items: [{ tag: 'plan\ninput', step: 's1' }] }), WALK_NO + '.items`')
arm('walk: two scenarios sharing an id -> refused naming walk.scenarios',
  buildWalk({ scenarios: [{ id: 'S1', name: 'a', walks: 'b' }, { id: 'S1', name: 'c', walks: 'd' }] }), WALK_NO + '.scenarios`')
arm('walk: an empty items -> refused naming walk.items', buildWalk({ items: [] }), WALK_NO + '.items`')
// TOOL-dFairHearing-23 AC40 - the grid's ceilings, each refused naming its field and its ceiling, each limit itself proceeding.
// RED against the parent, which refuses none: every refusing arm proceeds there.
{
  const items = (n) => Array.from({ length: n }, (_, i) => ({ tag: 'i' + i, step: 's1' }))
  const scenario = (over) => [Object.assign({ id: 'S1', name: 'n', walks: 'w' }, over)]
  arm('FH23 AC40 walk: a run-1 walker slice of 201 cells -> refused naming walk and its 200-cell ceiling', buildWalk({ items: items(201) }),
    WALK_NO + '` deals walker slot 1 of run 1 201 cells, above the 200-cell ceiling')
  arm('FH23 AC40 walk: a walker slice of 200 cells -> proceeds', buildWalk({ items: items(200) }), null)
  // TOOL-dFairHearing-27 AC19 - the cap is read on the slices `deriveWalkSlices` deals for the call's own `run`: 30 items
  // of one step under 7 scenarios deal run 2's step slot 210 cells, refused before the first agent, where run 1's
  // scenario deal stays under the ceiling. RED against a cap read on the run-1 deal alone, which admits both.
  const SC7W = Array.from({ length: 7 }, (_, j) => ({ id: 'S' + (j + 1), name: 'n', walks: 'w' }))
  arm('FH27 AC19 walk: a run-2 band of 210 cells -> refused naming the slice', buildWalk({ items: items(30), scenarios: SC7W, run: 2 }),
    WALK_NO + '` deals walker slot 3 of run 2 210 cells, above the 200-cell ceiling')
  arm('FH27 AC19 walk: the same grid under run 1 -> proceeds', buildWalk({ items: items(30), scenarios: SC7W, run: 1 }), null)
  arm('FH23 AC40 walk: a scenario name of 121 characters -> refused naming walk.scenarios and its 120-character ceiling',
    buildWalk({ scenarios: scenario({ name: 'n'.repeat(121) }) }), WALK_NO + '.scenarios` member 0 carries a name of 121 characters, above the 120-character ceiling')
  arm('FH23 AC40 walk: a scenario name of 120 characters -> proceeds', buildWalk({ scenarios: scenario({ name: 'n'.repeat(120) }) }), null)
  arm('FH23 AC40 walk: a walks of 601 characters -> refused naming walk.scenarios and its 600-character ceiling',
    buildWalk({ scenarios: scenario({ walks: 'w'.repeat(601) }) }), WALK_NO + '.scenarios` member 0 carries a walks of 601 characters, above the 600-character ceiling')
  arm('FH23 AC40 walk: a walks of 600 characters -> proceeds', buildWalk({ scenarios: scenario({ walks: 'w'.repeat(600) }) }), null)
}
let walkFns = null
{
  let got = null
  try {
    got = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn [walk, deriveWalkSlices, deriveWalkGaps]')(
      Object.assign({}, base, WALK_SPEC, { walk: { items: WALK_OK.items, scenarios: WALK_OK.scenarios, run: 1, keySha: WALK_KEY } }), () => {}, null, null, null)
  } catch (e) { console.log('HARNESS-BROKEN walk: the prelude did not yield walk and its two functions -> ' + e.message) }
  ck(!!got && got[0].runs === 2 && got[0].seed === 'reverted-escapes' && got[0].run === 1,
    'walk: a valid walk proceeds, reading runs 2 and seed reverted-escapes when both are absent: ' + JSON.stringify(got && got[0]))
  walkFns = got ? got.slice(1) : null
}
// AC2 - ten items in five steps of two through seven scenarios, every run dealing each of the 70 cells exactly once.
{
  const items = Array.from({ length: 10 }, (_, i) => ({ tag: 'i' + i, step: 'p' + Math.floor(i / 2) }))
  const scenarios = Array.from({ length: 7 }, (_, j) => ({ id: 'S' + (j + 1), name: 'n', walks: 'w' }))
  const slices = (run, sc) => (walkFns ? walkFns[0](items, sc || scenarios, run) : [[], [], [], [], []])
  const dealtOnce = (sl) => { const all = sl.flat().map((c) => c.join('|')); return all.length === 70 && new Set(all).size === 70 }
  const scenariosOf = (s) => s.map((c) => c[1]).filter((x, i, all) => all.indexOf(x) === i).join(' ')
  const itemsOf = (s) => s.map((c) => c[0]).filter((x, i, all) => all.indexOf(x) === i).join(' ')
  const r1 = slices(1)
  ck(scenariosOf(r1[0]) === 'S1 S6' && scenariosOf(r1[1]) === 'S2 S7' && [2, 3, 4].every((w) => r1[w].length === 10) &&
    r1.every((s) => s.length && itemsOf(s) === 'i0 i1 i2 i3 i4 i5 i6 i7 i8 i9') && dealtOnce(r1),
    'walk: run 1 deals S1 S6 and S2 S7 to slots 1 and 2, one scenario to each other, every slice holding all ten items, each cell once: ' + r1.map(scenariosOf).join(' / '))
  const r2 = slices(2)
  ck(r2.every((s, w) => s.length === 14 && itemsOf(s) === 'i' + 2 * w + ' i' + (2 * w + 1)) && dealtOnce(r2),
    'walk: run 2 gives each slot one step\'s two items through all seven scenarios, each cell once: ' + r2.map(itemsOf).join(' / '))
  const r3 = slices(3)
  ck(r3.every((s, w) => s.every((c) => (Number(c[0].slice(1)) + Number(c[1].slice(1)) - 1) % 5 === w)) && dealtOnce(r3),
    'walk: run 3 gives cell (i, j) to slot (i + j) mod 5 + 1, each cell once')
  const r13 = slices(1, scenarios.slice(0, 3))
  ck(r13[3].length === 0 && r13[4].length === 0 && r13[0].length === 10, 'walk: over three scenarios run 1 leaves slots 4 and 5 empty')
}
// AC3 - one walker's table against its two-cell slice: complete, the planted whitespace witness, and six planted defects.
{
  const slices = [[['a', 'S1'], ['b', 'S1']], [], [], [], []]
  const row = (item, over) => Object.assign({ item: item, scenario: 'S1', actor: '=', needs: '=', witness: '=', route: '=', verdict: 'holds', findings: [] }, over)
  const gapsOf = (rows, n) => (walkFns ? walkFns[1](slices, [{ findings: Array.from({ length: n || 0 }, () => ({})), walk: rows }, null, null, null, null]) : null)
  const whole = gapsOf([row('a'), row('b')])
  ck(!!whole && whole.length === 0, 'walk: a complete table returns no gap: ' + JSON.stringify(whole))
  const planted = gapsOf([row('a', { witness: '  ' }), row('b')])
  ck(!!planted && planted.length === 1 && planted[0].indexOf('a · S1') === 0 && planted[0].indexOf('witness') !== -1,
    'walk: the planted whitespace witness returns one gap naming the item, the scenario and witness: ' + JSON.stringify(planted))
  for (const [what, rows, n] of [['a missing row', [row('a')]], ['two rows for one cell', [row('a'), row('a'), row('b')]],
    ['a row outside the slice', [row('a'), row('b'), row('c')]], ['the verdict maybe', [row('a', { verdict: 'maybe' }), row('b')]],
    ['a finding index past the findings', [row('a', { verdict: 'finding', findings: [1] }), row('b')], 1],
    ['not-on-path with an empty reason', [row('a', { verdict: 'not-on-path', reason: '' }), row('b')]]]) {
    const g = gapsOf(rows, n)
    ck(!!g && g.length === 1, 'walk: ' + what + ' returns one gap: ' + JSON.stringify(g))
  }
}

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
    // TOOL-aOrientedCast-27 - a label is `<slug> · <scope> · <stage>`: the whole one is kept as `full`,
    // and `label` is the stage after its last ` · `, which every stub and stage read keys on as before.
    const full = (opts && opts.label) || '(unlabelled)'
    const label = full.split(' · ').pop()
    // TOOL-aOrientedCast-10 - the effort each spawn asked for, and whether its options carry the key at all.
    trace.push({ label: label, full: full, prompt: String(prompt), schema: opts && opts.schema, agentType: opts && opts.agentType,
      effort: opts && opts.effort, hasEffort: !!opts && Object.prototype.hasOwnProperty.call(opts, 'effort') })
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
// TOOL-aMendedFleet-93 S4 - absent `workerType` reads as Plan, so the durable-spawn arms below pin `none`,
// which spawns exactly as an absent value did before the default.
// TOOL-dFairHearing-1 S9 - absent `addressTwins` reads as shown and absent `fixJudge` as class, so every arm
// below pins `hidden` and `instance`, which run exactly as an absent value did before the two flips; the
// arms that read the defaults themselves delete the pins.
const DIFF = { repo: '/tmp/r', base: B, head: H, round: 1, context: 'ctx', reviewDir: 'memory/reviews', workerType: 'none', addressTwins: 'hidden', fixJudge: 'instance' }
const SPEC = { repo: '/tmp/r', kind: 'spec-audit', round: 1, context: 'ctx', subjects: [{ path: 'memory/builds/dX/spec/s.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1 }], scratch: '/tmp/s', workerType: 'none', addressTwins: 'hidden', fixJudge: 'instance' }
const DESIGN = Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/build/a.md', blob: 'abc1234', id: 'PLAY-dX-1' }] })
const buildProbe = (finds, verifies, base, head) => ({ commonDir: '/cd', base: base || B, head: head || H, finds: finds || [], verifies: verifies || [] })
// One finding per lens, so five lenses make five ids and five batches of one: verify:batch-1 .. verify:batch-5.
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
// TOOL-dFairHearing-6 - an item's `grades`, every id it holds at one grade: the stubs below place each id
// at the item's severity, the count the tally read before per-id grades.
const buildGrades = (ids, sev) => Object.fromEntries(ids.map((id) => [String(id), sev]))
// The synthesis places every CONFIRMED id in one item unless told to drop one.
const buildSynth = (drop) => (label, prompt) => {
  const head = prompt.split('UNVERIFIED findings')[0]
  const ids = [...head.matchAll(/id=(\d+) \[/g)].map((x) => parseInt(x[1], 10)).filter((id) => id !== drop)
  return { path: 'memory/reviews/r.md', summary: 's', items: [{ severity: 'HIGH', ids: ids, grades: buildGrades(ids, 'HIGH'), specs: ['TOOL-x-1'] }] }
}
const ALL_OK ={ 'resume:probe': buildProbe(), 'find:': buildLensReturn, 'verify:': buildVerdicts('confirmed'), synth: buildSynth(null) }
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
    // TOOL-dFairHearing-15 - DIFF passes no `checklist`, so the checklist agent spawns first and the probe second.
    ck(r.trace[0] && r.trace[0].label === 'resume:checklist' && r.trace[1] && r.trace[1].label === 'resume:probe',
      'the checklist agent, then the resume probe, are the first two agents, before any lens')
    // TOOL-dFairHearing-32 AC1 - the resume probe's instruction names the skeptic file by the name the
    // batches write. The retired id-range spelling is AC1's tree-wide grep, so this file never spells it.
    const probeAsk = (r.trace.find((t) => t.label === 'resume:probe') || { prompt: '' }).prompt
    ck(probeAsk.indexOf('verify-batch-<n>.json') !== -1, 'FH32 AC1 the resume:probe prompt names verify-batch-<n>.json')
  }
  const K = r.result ? r.result.key : ''

  // ---- TOOL-dFairHearing-37 AC6: a `repo` of `C:\x\y` reaches every prompt's `git -C` as `C:/x/y`, the
  // fold at the harness's one `repo` read. RED against that read taking `a.repo` raw, as at unit 32's commit.
  {
    const rw = await runReview(Object.assign({}, DIFF, { repo: 'C:\\x\\y' }), ALL_OK)
    const ps = rw.trace.map((t) => t.prompt)
    const named = ps.join('\n').match(/git -C [^\s`]+/g) || []
    ck(!rw.threw && named.length > 0 && named.every((g) => g === 'git -C "C:/x/y"') && ps.every((p) => p.indexOf('C:\\x') === -1),
      'FH37 AC6 a repo of C:\\x\\y reaches every prompt as git -C "C:/x/y": ' + named.length + ' git -C command(s), ' +
      JSON.stringify(named.filter((g) => g !== 'git -C "C:/x/y"').slice(0, 3)))
  }

  // ---- TOOL-dFairHearing-40 AC19: every `git -C` quotes `repo`, so a `repo` of `C:/x y/z` reaches each
  // prompt as one argument, and a `repo` holding `$`, `"` or a backtick is refused naming it before any
  // agent spawns. RED against the harness at unit 37's commit `6d768c563`, where all 13 interpolations
  // are bare and no character of `repo` is refused. This run is the diff kind; the spec presets are the
  // `FH43 AC7` arm in runWalkArms.
  {
    const rs = await runReview(Object.assign({}, DIFF, { repo: 'C:/x y/z' }), ALL_OK)
    const named = rs.trace.map((t) => t.prompt).join('\n').match(/git -C (?:"[^"]*"|[^\s`]+)/g) || []
    ck(!rs.threw && named.length > 0 && named.every((g) => g === 'git -C "C:/x y/z"'),
      'FH40 AC19 a repo of C:/x y/z reaches every prompt of a diff review as git -C "C:/x y/z": ' + named.length + ' git -C command(s), ' +
      JSON.stringify(named.filter((g) => g !== 'git -C "C:/x y/z"').slice(0, 3)))
    const unrefused = []
    for (const c of ['$', '"', '`']) {
      const rr = await runReview(Object.assign({}, DIFF, { repo: '/tmp/a' + c + 'b' }), ALL_OK)
      if (!rr.threw || rr.threw.indexOf(JSON.stringify(c)) === -1 || rr.trace.length !== 0) unrefused.push(c + ' ' + (rr.threw || 'did not throw'))
    }
    ck(unrefused.length === 0, 'FH40 AC19 a repo holding $, " or a backtick is refused naming it before any agent spawns: ' + JSON.stringify(unrefused))
  }

  // ---- TOOL-dFairHearing-43 AC1: `base` and `head` reach the checklist agent's and the probe's shell lines, so a
  // value outside the ref shape is refused naming its field before any agent; a moving ref and a parent suffix
  // complete, the checklist agent first. RED against the harness at unit 40, where the `head` run spawns that agent
  // with the value in its command.
  {
    const unrefused = []
    for (const [field, v] of [['head', 'HEAD;echo PWNED'], ['base', 'abc $(echo PWNED)'], ['base', 'ab`c'], ['base', '-x']]) {
      const rr = await runReview(Object.assign({}, DIFF, { [field]: v }), ALL_OK)
      if (!rr.threw || rr.threw.indexOf('tier2-review:') !== 0 || rr.threw.indexOf('`' + field + '`') === -1 || rr.trace.length !== 0) unrefused.push(field + ' ' + v + ' ' + (rr.threw || 'did not throw'))
    }
    ck(unrefused.length === 0, 'FH43 AC1 a base or head outside the ref shape is refused naming its field before any agent spawns: ' + JSON.stringify(unrefused))
    const stopped = []
    for (const over of [{ base: 'origin/main' }, { head: 'HEAD~1' }]) {
      const rr = await runReview(Object.assign({}, DIFF, over), ALL_OK)
      if (rr.threw || !rr.trace[0] || rr.trace[0].label !== 'resume:checklist') stopped.push(JSON.stringify(over) + ' ' + rr.threw)
    }
    ck(stopped.length === 0, 'FH43 AC1 a base of origin/main and a head of HEAD~1 each complete, the checklist agent first: ' + JSON.stringify(stopped))
  }

  // ---- TOOL-aOrientedCast-27 AC8: every whole label is `<slug> · <kind> round <n> · <stage>`, the slug
  // read from a `builds/<slug>/` reviewDir and absent outside one; every check carries its count, so an
  // empty trace cannot pass. Against renderAgentLabel staged to return the stage alone, each reds.
  {
    const rb = await runReview(Object.assign({}, DIFF, { reviewDir: 'memory/builds/tB/reviews' }), ALL_OK)
    const fb = rb.trace.map((t) => t.full)
    ck(!rb.threw && fb.length > 0 && fb.every((f) => f.indexOf('tB · diff-review round 1 · ') === 0),
      'OC27 AC8 in a build folder every label opens "tB · diff-review round 1 · ": ' + fb.length + ' label(s)')
    const ends = [/ · resume:probe$/, / · find:[a-z-]+$/, / · verify:batch-\d+$/, / · synth$/].map((re) => fb.filter((f) => re.test(f)).length)
    ck(ends.every((c) => c > 0), 'OC27 AC8 ...and the probe, a finder, a skeptic batch and the synthesis each carry one: ' + ends.join(' '))
    const fr = r.trace.map((t) => t.full)
    ck(fr.length > 0 && fr.every((f) => f.indexOf('diff-review round 1 · ') === 0),
      'OC27 AC8 outside a build folder every label opens "diff-review round 1 · ", with no slug part: ' + fr.length + ' label(s)')
    const rs = await runReview(SPEC, ALL_OK)
    const fsa = rs.trace.map((t) => t.full)
    ck(!rs.threw && fsa.length > 0 && fsa.every((f) => f.indexOf('spec-audit round 1 · ') === 0),
      'OC27 AC8 a spec audit labels every agent "spec-audit round 1 · ": ' + fsa.length + ' label(s)')
    const rd = await runReview(Object.assign({}, DIFF, { reviewDir: 'memory/builds/tB/reviews' }), buildStubs({ 'find:seams': null }))
    ck(!rd.threw && rd.result && JSON.stringify(rd.result.pending) === '["find:seams"]',
      'OC27 AC8 a dead find:seams leaves pending holding its stage key, never a whole label: ' + JSON.stringify(rd.result && rd.result.pending))
    // ---- AC16: the run's identity is its first log line and the first key of every return.
    ck(rb.logs[0] === 'tB · diff-review round 1 · review' && rb.result && Object.keys(rb.result)[0] === 'identity' &&
      rb.result.identity === rb.logs[0], 'OC27 AC16 the first log line is the identity, and the complete return leads with it: ' + JSON.stringify(rb.logs[0]))
    ck(rs.logs[0] === 'spec-audit round 1 · review' && rs.result && Object.keys(rs.result)[0] === 'identity',
      'OC27 AC16 a spec audit outside a build folder logs "spec-audit round 1 · review" first: ' + JSON.stringify(rs.logs[0]))
    ck(rd.result && Object.keys(rd.result)[0] === 'identity' && rd.result.identity === 'tB · diff-review round 1 · review',
      'OC27 AC16 the deferred return leads with the identity too: ' + (rd.result ? Object.keys(rd.result)[0] : 'no result'))
  }

  // ---- AC1: every find: prompt and every verify: prompt NAMES its file under review-lenses/, and
  // ---- all three agent schemas REQUIRE path. The skeptic half is read too, which is the half a
  // ---- lens-only check would leave ungraded.
  const finds = r.trace.filter((t) => t.label.indexOf('find:') === 0)
  const verifies = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
  ck(finds.length === 5 && finds.every((t) => t.prompt.indexOf('/review-lenses/' + K + '/find-' + t.label.slice(5) + '.json') !== -1),
    'AC1 every find: prompt names review-lenses/<key>/find-<lens>.json')
  ck(verifies.length === 5 && verifies.every((t) => {
    const m = /^verify:batch-(\d+)$/.exec(t.label)
    return m && t.prompt.indexOf('/review-lenses/' + K + '/verify-batch-' + m[1] + '.json') !== -1
  }), 'AC1 every verify: prompt names review-lenses/<key>/verify-batch-<n>.json')
  ck(finds.every((t) => t.prompt.indexOf('BEFORE you return') !== -1) && verifies.every((t) => t.prompt.indexOf('BEFORE you return') !== -1),
    'AC1 both prompt kinds order the write BEFORE the return')
  ck(finds.every((t) => t.schema && t.schema.required.indexOf('path') !== -1), 'AC1 the diff finding schema lists path in required')
  ck(verifies.every((t) => t.schema && t.schema.required.indexOf('path') !== -1), 'AC1 the verdict schema lists path in required')
  // TOOL-dTrueNorth-5 AC2 — the spec kind's synthesis prompt carries the binding line the harness
  // rendered from the subjects' pins, between its markers, and no longer asks the agent to compose the
  // id list. Against the base harness the marker block is absent and the composing sentence is there.
  const pinRun = await runReview(Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/spec/m.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 3 }, { path: 'memory/builds/dX/spec/u.md', blob: 'abc9999', id: 'TOOL-x-2', rev: 1 }] }), ALL_OK)
  if (checkNoThrow(pinRun, 'pin: spec-audit synthesis')) {
    const pinSynth = pinRun.trace.filter((t) => t.label === 'synth').map((t) => t.prompt)
    ck(pinSynth.length === 1 && pinSynth[0].indexOf('<<<SERVES\n**Serves:** spec-audit TOOL-x-1@rev-3 TOOL-x-2@rev-1\nSERVES>>>') !== -1 &&
      pinSynth[0].indexOf('the reviewed spec set defines') === -1,
      'pin: the spec-audit synthesis prompt carries the rendered, pinned binding line and no composing sentence: ' + pinSynth.length + ' synthesis prompt(s)')
    // TOOL-dTrueNorth-13 AC2 — the subjects line is rendered too, between its own markers, and the
    // sentence asking the agent to compose one is gone. Against the harness TOOL-dTrueNorth-5 left, both red.
    ck(pinSynth.length === 1 &&
      pinSynth[0].indexOf('<<<REVIEWED\nReviewed: memory/builds/dX/spec/m.md@abc1234, memory/builds/dX/spec/u.md@abc9999\nREVIEWED>>>') !== -1 &&
      pinSynth[0].indexOf('naming each reviewed subject') === -1,
      'design: the spec-audit synthesis prompt carries the rendered Reviewed: line and no composing sentence: ' + pinSynth.length + ' synthesis prompt(s)')
  }
  const designRun = await runReview(Object.assign({}, SPEC, { subjects: [DESIGN_A, DESIGN_B] }), ALL_OK)
  if (checkNoThrow(designRun, 'design: spec-audit synthesis')) {
    const ds = designRun.trace.filter((t) => t.label === 'synth').map((t) => t.prompt)
    ck(ds.length === 1 && ds[0].indexOf('<<<SERVES\n**Serves:** spec-audit PLAY-dX-1\nSERVES>>>') !== -1 &&
      ds[0].indexOf('<<<REVIEWED\nReviewed: memory/builds/dX/build/a.md@abc1234, memory/builds/dX/build/b.md@def5678\nREVIEWED>>>') !== -1,
      'design: a design audit runs whole, its synthesis copying the bare id and both design subjects: ' + ds.length + ' synthesis prompt(s)')
  }
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
    ck(sf.length === 5 && sf.every((t) => t.schema && t.schema.required.indexOf('path') !== -1 && extractItemRequired(t).indexOf('where') !== -1 &&
      t.prompt.indexOf('/review-lenses/' + rs.result.key + '/find-' + t.label.slice(5) + '.json') !== -1),
      'AC1 the spec finding schema lists path in required, and every spec lens prompt names its file')
    // ---- TOOL-aEvidencedLens-2 AC1/AC4 — the probe policy and the evidence field, spec kind only.
    ck(sf.length === 5 && sf.every((t) => {
      const at = t.prompt.indexOf('PROBE POLICY')
      return at !== -1 && t.prompt.indexOf('PROBE POLICY', at + 1) === -1 && at > t.prompt.indexOf('LENS: ') && t.prompt.indexOf('LENS: ') !== -1 &&
        ['scratch directory /tmp/s.', '120 seconds', 'DURABILITY', '--selftest'].every((w) => t.prompt.indexOf(w, at) !== -1)
    }) && rs.trace.filter((t) => t.label === 'synth').length === 1 && rs.trace.filter((t) => t.label === 'synth').every((t) => t.prompt.indexOf('PROBE POLICY') === -1),
      'the probe policy sits once under LENS: in every spec find: prompt, naming the scratch, the bound, the DURABILITY exception and --selftest, and not in synth')
    const df = r.trace.filter((t) => t.label.indexOf('find:') === 0)
    ck(sf.length === 5 && sf.every((t) => extractItemRequired(t).indexOf('evidence') !== -1 && t.prompt.indexOf('impact,fix,evidence}]') !== -1) &&
      df.length === 5 && df.every((t) => extractItemRequired(t).indexOf('evidence') === -1 && t.prompt.indexOf('PROBE POLICY') === -1),
      'the spec finding schema requires evidence and its return line names it; the diff schema and prompts carry neither')
    // AC6 - the rules are in the print and `scratch` is not.
    const rs2 = await runReview(Object.assign({}, SPEC, { scratch: '/tmp/s2' }), ALL_OK)
    const ruleRe = /'Time a stated wall-clock goal once, when one run of it is bounded\.'/
    const ruled = whole.replace(ruleRe, "'Time a stated wall-clock goal twice.'")
    const rs3 = await runReview(SPEC, ALL_OK, ruled)
    ck(!rs2.threw && rs2.result.key === rs.result.key && ruleRe.test(whole) && ruled !== whole && !rs3.threw && rs3.result.key !== rs.result.key,
      'the review key moves with a PROBE_RULES edit and not with scratch')
    const rw = await runReview(Object.assign({}, SPEC, { scratch: 'C:\\t\\s' }), ALL_OK)
    ck(!rw.threw && rw.trace.filter((t) => t.label.indexOf('find:') === 0).every((t) => t.prompt.indexOf('PROBE POLICY — repository /tmp/r, scratch directory C:/t/s.') !== -1) &&
      rw.trace.some((t) => t.label.indexOf('find:') === 0), 'a Windows scratch reaches the PROBE POLICY line folded to C:/t/s')
    // TOOL-aEvidencedLens-21 AC6 (replay id 37) - the per-role scratch rule is constant text, so it rides
    // every probing prompt, both PROBE POLICY slices stay byte-identical, and no diff prompt carries it.
    const ROLE_RULE = 'named for your own role, <lens key> for a finder or verify-<batch> for a skeptic'
    const sv6 = rs.trace.filter((t) => t.label.indexOf('verify:') === 0)
    const extractPolicySlice = (p) => { const at = p.indexOf('PROBE POLICY'); return at === -1 ? null : p.slice(at, p.indexOf('\n\n', at)) }
    ck(sf.length === 5 && sv6.length > 0 && sf.concat(sv6).every((t) => t.prompt.indexOf(ROLE_RULE) !== -1 && extractPolicySlice(t.prompt) === extractPolicySlice(sf[0].prompt)) &&
      r.trace.length > 0 && r.trace.every((t) => t.prompt.indexOf(ROLE_RULE) === -1),
      'the per-role scratch rule is in every spec find: and verify: prompt, the two PROBE POLICY slices identical, and in no diff prompt')
  }

  // ---- AC4: a DEAD probe reuses nothing, dispatches every lens and says so.
  r = await runReview(DIFF, buildStubs({ 'resume:probe': null }))
  if (checkNoThrow(r, 'dead probe')) {
    ck(r.scanSpawned('find:').length === 5, 'AC4 a dead probe dispatches all five lenses')
    ck(r.logs.some((l) => l.indexOf('nothing could be reused') !== -1), 'AC4 ...and the log says nothing could be reused')
  }

  // ---- TOOL-aMendedFleet-67 S5 - `workerType` routes the JUDGES and only them, and they write nothing.
  // ---- The default half reads the first run's judges, so an arm that always sets the option reds here.
  // TOOL-dFairHearing-11 S2 - `none` types every judge as PLATFORM_TYPE, so no judge spawns untyped.
  ck(finds.concat(verifies).every((t) => t.agentType === 'general-purpose'), 'workerType: none, every judge spawn carries agentType general-purpose')
  const ABSENT = Object.assign({}, DIFF)
  delete ABSENT.workerType
  const rd = await runReview(ABSENT, ALL_OK)
  let KP = ''
  if (checkNoThrow(rd, 'workerType absent run')) {
    KP = rd.result.key
    ck(rd.trace.filter((t) => /^(find|verify):/.test(t.label)).length === 10 &&
      rd.trace.filter((t) => /^(find|verify):/.test(t.label)).every((t) => t.agentType === 'Plan'),
      'workerType: absent, every finder and skeptic batch spawns as Plan (TOOL-aMendedFleet-93 S4)')
  }
  r = await runReview(Object.assign({}, DIFF, { workerType: 'Plan' }), ALL_OK)
  if (checkNoThrow(r, 'workerType run')) {
    ck(r.result.key === KP, 'workerType: an explicit Plan run keys as an absent one')
    const judges = r.trace.filter((t) => /^(find|verify):/.test(t.label))
    const orch = r.trace.filter((t) => !/^(find|verify):/.test(t.label))
    ck(judges.length === 10 && judges.every((t) => t.agentType === 'Plan'), 'workerType: all five finders and five skeptic batches spawn as Plan')
    ck(orch.length === 3 && orch[0].label === 'resume:checklist' && orch[0].agentType === 'Plan' && orch[1].label === 'resume:probe' &&
      orch[1].agentType === 'Plan' && orch[2].agentType === 'general-purpose',
      'workerType: the probe takes Plan and the synthesis general-purpose, never the worker type: ' + orch.map((t) => t.label + '=' + t.agentType).join(' '))
    ck(judges.every((t) => t.prompt.indexOf('DURABILITY') === -1), 'workerType: no judge is told to write a lens or verify file')
    ck(judges.every((t) => t.prompt.indexOf('Set path to an empty string') !== -1), 'workerType: every judge is told to return path empty')
    ck(r.logs.some((l) => l.indexOf('worker type Plan') === 0 && l.indexOf('NOT durable') !== -1), 'workerType: the log says the results are not durable')
    ck(r.result.key !== K, 'workerType: the key differs from the default run\'s, so no default lens file answers it')
  }
  for (const [lbl, v] of [['two words', 'two words'], ['a number', 7], ['65 characters', 'A'.repeat(65)]]) {
    r = await runReview(Object.assign({}, DIFF, { workerType: v }), ALL_OK)
    ck(!!r.threw && r.threw.indexOf('workerType') !== -1 && r.trace.length === 0, 'workerType: ' + lbl + ' is refused before any spawn')
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
  const specMoved = Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/spec/s.md', blob: 'abc1235', id: 'TOOL-x-1', rev: 1 }] })
  const s2 = await runReview(specMoved, buildStubs({ 'resume:probe': buildProbe([buildLensFile('reuse', s1.result ? s1.result.key : '')]) }))
  if (checkNoThrow(s1, 'AC3 spec base') && checkNoThrow(s2, 'AC3 spec moved')) {
    ck(s2.result.key !== s1.result.key && s2.scanSpawned('find:reuse').length === 1,
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
    const v1 = r.trace.find((t) => t.label === 'verify:batch-1')
    const m = v1 ? /"batch":"([0-9a-f]{8})"/.exec(v1.prompt) : null
    print = m ? m[1] : ''
    ck(print.length === 8, 'AC5 the verify prompt names the batch print the file must carry')
  }
  const vfile = (batch) => ({ name: 'verify-batch-1.json', key: K, batch: batch, ids: [1], path: '/cd/v.json', verdicts: [{ id: 1, verdict: 'confirmed', reason: 'r' }] })
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(allLensFiles, [vfile(print)]) }))
  if (checkNoThrow(r, 'AC5 matching print')) ck(r.scanSpawned('verify:batch-1').length === 0 && r.result.batchesReused === 1, 'AC5 a verify file with the key and the matching print is reused')
  r = await runReview(DIFF, buildStubs({ 'resume:probe': buildProbe(allLensFiles, [vfile('0badf00d')]) }))
  if (checkNoThrow(r, 'AC5 other print')) ck(r.scanSpawned('verify:batch-1').length === 1, 'AC5 the right ids over a print of other claims is dispatched')

  // ---- TOOL-dFairHearing-4 AC5/AC6 — address-ordered batches, numbered labels and files, `ids` carried.
  // Five lenses of two findings each, every lens's first citing a.js line 10 and its second its own file.
  {
    const buildAddressLens = (label) => {
      const lens = label.slice('find:'.length)
      const mk = (file, claim) => ({ file: file, line: file === 'a.js' ? 10 : 1, severity: 'high', claim: lens + ' ' + claim, impact: 'i', fix: 'f' })
      return { lens: lens, path: '/p', findings: [mk('a.js', 'shared'), mk(lens + '.js', 'own')] }
    }
    const A_IDS = [1, 3, 5, 7, 9]
    const readBatches = (rr) => rr.trace.filter((t) => t.label.indexOf('verify:') === 0)
      .map((t) => ({ label: t.label, prompt: t.prompt, ids: [...t.prompt.matchAll(/^id=(\d+) \[/gm)].map((x) => parseInt(x[1], 10)) }))
    const ra = await runReview(Object.assign({}, DIFF, { batchBy: 'address' }), buildStubs({ 'find:': buildAddressLens }))
    const rd = await runReview(DIFF, buildStubs({ 'find:': buildAddressLens }))
    if (checkNoThrow(ra, 'batch: address run') && checkNoThrow(rd, 'batch: id run')) {
      const ga = readBatches(ra)
      const gd = readBatches(rd)
      const shared = (g) => g.map((x) => x.ids.filter((id) => A_IDS.indexOf(id) !== -1).length).join(',')
      ck(shared(ga) === '2,2,1,0,0', 'batch: by address the five a.js findings fill three consecutive batches: ' + shared(ga))
      ck(gd.length === 5 && gd.every((x) => x.ids.filter((id) => A_IDS.indexOf(id) !== -1).length <= 1), 'batch: by id no two a.js findings share a batch: ' + shared(gd))
      const NUMBERED = 'verify:batch-1 verify:batch-2 verify:batch-3 verify:batch-4 verify:batch-5'
      ck(ga.map((x) => x.label).join(' ') === NUMBERED && gd.map((x) => x.label).join(' ') === NUMBERED,
        'batch: both orders spawn exactly five skeptics, verify:batch-1 to verify:batch-5')
      ck([ga, gd].every((g) => g.every((x, i) => x.ids.length === 2 && x.prompt.indexOf('/verify-batch-' + (i + 1) + '.json') !== -1 &&
        x.prompt.indexOf('"ids":[' + x.ids.join(',') + ']') !== -1)), 'batch: each verify prompt names verify-batch-<n>.json and an "ids" list equal to its own findings')
      ck(ra.logs.some((l) => / verifier\(s\) \(cap \d+\) by address$/.test(l)) && rd.logs.some((l) => / verifier\(s\) \(cap \d+\) by id$/.test(l)),
        'batch: the verifier log line names the order it sliced by')
    }
    const lensFiles = ['security', 'correctness', 'seams', 'verification', 'intent'].map((l) => Object.assign({ name: 'find-' + l + '.json', key: K }, buildAddressLens('find:' + l)))
    const r0 = await runReview(DIFF, buildStubs({ 'find:': buildAddressLens, 'resume:probe': buildProbe(lensFiles) }))
    const v1 = r0.trace.find((t) => t.label === 'verify:batch-1')
    const bp = v1 ? (/"batch":"([0-9a-f]{8})"/.exec(v1.prompt) || [])[1] || '' : ''
    const bids = v1 ? [...v1.prompt.matchAll(/^id=(\d+) \[/gm)].map((x) => parseInt(x[1], 10)) : []
    const vf = (name, ids) => Object.assign({ name: name, key: K, batch: bp, path: '/cd/v.json', verdicts: bids.map((id) => ({ id: id, verdict: 'confirmed', reason: 'r' })) }, ids ? { ids: ids } : {})
    const reuseArm = async (file, reused, name) => {
      const rr = await runReview(DIFF, buildStubs({ 'find:': buildAddressLens, 'resume:probe': buildProbe(lensFiles, [file]) }))
      if (checkNoThrow(rr, name)) ck(bp.length === 8 && rr.scanSpawned('verify:batch-1').length === (reused ? 0 : 1) && rr.result.batchesReused === (reused ? 1 : 0), name)
    }
    await reuseArm(vf('verify-batch-1.json', bids), true, 'batch: verify-batch-1.json with the key, the batch print and ids is reused, batchesReused 1')
    await reuseArm(vf('verify-1-2.json', bids), false, 'batch: the same file named verify-1-2.json is dispatched')
    await reuseArm(vf('verify-batch-1.json', null), false, 'batch: the same file lacking ids is dispatched')
  }

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
  r = await runReview(DIFF, buildStubs({ 'verify:batch-2': null }))
  if (checkNoThrow(r, 'AC7 dead batch')) {
    ck(r.result.exit === 'deferred-platform' && r.result.blockers === null && r.result.pending.join(' ') === 'verify:batch-2',
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

  // ---- TOOL-aMendedFleet-111 AC7: every deferred note and `durable` follow `workerType`. Under the
  // ---- absent default, Plan, no judge wrote a file, so the note says a re-run dispatches every judge
  // ---- again and `durable` is false; under `none` the note keeps "dispatch only" and `durable` is
  // ---- true. Staged red by restoring the unconditional "dispatch only" wording.
  const ABS111 = Object.assign({}, DIFF); delete ABS111.workerType
  r = await runReview(ABS111, buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'aMF-111 AC7 absent, lenses dead'))
    ck(r.result.durable === false && r.result.note.indexOf('dispatches every finder and skeptic again') !== -1 && r.result.note.indexOf('dispatch only') === -1,
      'aMF-111 AC7 workerType absent, every lens dead: durable false, the note re-dispatches every judge')
  r = await runReview(DIFF, buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'aMF-111 AC7 none, lenses dead'))
    ck(r.result.durable === true && r.result.note.indexOf('dispatch only find:') !== -1,
      'aMF-111 AC7 workerType none, every lens dead: durable true, the note dispatches only the dead')
  r = await runReview(ABS111, buildStubs({ synth: null }))
  if (checkNoThrow(r, 'aMF-111 AC7 absent, synthesis dead')) {
    ck(r.result.durable === false && r.result.note.indexOf('every finder and skeptic again, plus the synthesis') !== -1,
      'aMF-111 AC7 workerType absent, the synthesis dead: durable false, the note re-dispatches every judge and the synthesis')
    ck(r.logs.some((l) => l.indexOf('the synthesis agent DIED') !== -1 && l.indexOf('plus the synthesis') !== -1 && l.indexOf('dispatches only the synthesis') === -1),
      'aMF-111 AC7 ...and the synthesis-died log says the same')
  }
  r = await runReview(DIFF, buildStubs({ synth: null }))
  if (checkNoThrow(r, 'aMF-111 AC7 none, synthesis dead'))
    ck(r.result.durable === true && r.result.note.indexOf('dispatch only the synthesis') !== -1,
      'aMF-111 AC7 workerType none, the synthesis dead: durable true, the note dispatches only the synthesis')

  // ==== TOOL-aSightedSkeptic-5 — five diff lenses, `lensNotes`, and the review-shape bump ===========
  // ---- AC1: the lens set and its ORDER, read off what a complete run actually spawns.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'five-lens run')) {
    ck(r.scanSpawned('find:').join(' ') === 'find:security find:correctness find:seams find:verification find:intent',
      'the diff lens set is security correctness seams verification intent: ' + r.scanSpawned('find:').join(' '))
  }
  // ---- TOOL-aEvidencedLens-1 AC1: the spec catalogue and its ORDER, off what a spec audit spawns. RED
  // ---- against the base render, which spawns the four retired lenses.
  r = await runReview(SPEC, ALL_OK)
  if (checkNoThrow(r, 'five spec lenses')) {
    ck(r.scanSpawned('find:').join(' ') === 'find:coherence find:grounding find:reuse find:blast-radius find:failure-envelope',
      'spec catalogue: the spec lens set is coherence grounding reuse blast-radius failure-envelope: ' + r.scanSpawned('find:').join(' '))
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
  const SPEC_KEYS = 'coherence | grounding | reuse | blast-radius | failure-envelope'
  const malformed = [
    ['a string', DIFF, 'note', DIFF_KEYS],
    ['an array', DIFF, ['security'], DIFF_KEYS],
    ['null', DIFF, null, DIFF_KEYS],
    // The retired key is spelled by concatenation, so this file keeps no literal of it (spec AC7).
    ['the retired key on a diff review', DIFF, { ['regress' + 'ions']: 'n' }, DIFF_KEYS],
    ['a diff key on a spec audit', SPEC, { verification: 'n' }, SPEC_KEYS],
    // TOOL-aEvidencedLens-1 - the retired spec key, spelled by concatenation for the same reason.
    // RED against the base render, whose catalogue still carries it and accepts the note.
    ['spec catalogue: the retired spec key on a spec audit', SPEC, { ['prior-' + 'art']: 'n' }, SPEC_KEYS],
    ['an empty note', DIFF, { security: '' }, DIFF_KEYS],
  ]
  for (const [what, args, notes, keys] of malformed) {
    r = await runReview(Object.assign({}, args, { lensNotes: notes }), ALL_OK)
    ck(typeof r.threw === 'string' && r.threw.indexOf('lensNotes') !== -1 && r.threw.indexOf(keys) !== -1 && r.trace.length === 0,
      'a malformed lensNotes refuses before any agent spawns: ' + what + (r.threw ? '' : ' (accepted)'))
  }
  r = await runReview(Object.assign({}, SPEC, { lensNotes: { reuse: 'n' } }), ALL_OK)
  ck(!r.threw && r.result && r.result.exit === 'complete' && r.scanSpawned('find:').length === 5,
    'a malformed lensNotes refuses before any agent spawns: control, a spec-kind key on a spec audit, proceeds')
  // ---- TOOL-dFairHearing-9 AC4: a per-preset map, each run reading its own literal's entry and no other.
  // ---- Five finders are asserted beside each absence, so it cannot pass over a run that spawned none.
  // ---- RED against the base harness, which refuses `unit-spec` as a lens key.
  const PER_PRESET = { 'unit-spec': { reuse: 'FH9-N1' }, 'design-audit': { 'alternatives-and-cost': 'FH9-N2' } }
  const noteCarriers = (run, mark) => run.trace.filter((t) => t.prompt.indexOf(mark) !== -1).map((t) => t.label).join(' ')
  for (const [preset, own, other, lens] of [['unit-spec', 'FH9-N1', 'FH9-N2', 'reuse'], ['design-audit', 'FH9-N2', 'FH9-N1', 'alternatives-and-cost']]) {
    r = await runReview(Object.assign({}, SPEC, preset === 'unit-spec' ? {} : { preset: preset }, { lensNotes: PER_PRESET }), ALL_OK)
    ck(!r.threw && r.scanSpawned('find:').length === 5 && noteCarriers(r, own) === 'find:' + lens && noteCarriers(r, other) === '',
      'lens notes: AC4 a ' + preset + ' run reads its own per-preset entry, in find:' + lens + ' alone, and never another preset\'s: ' + (r.threw || noteCarriers(r, own)))
  }
  // ---- TOOL-dFairHearing-9 AC6: a typo'd key, flat or in the run's entry, names the legal keys; an object
  // ---- mixing literal names with lens keys names both forms. Each before the first agent.
  for (const [what, notes, word] of [['a typo\'d flat key', { nope: 'x' }, 'legal keys: ' + SPEC_KEYS],
    ['a typo\'d key in the run\'s entry', { 'unit-spec': { nope: 'x' } }, 'legal keys: ' + SPEC_KEYS],
    ['a mixed object', { 'unit-spec': { reuse: 'x' }, reuse: 'y' }, 'per-preset form']]) {
    r = await runReview(Object.assign({}, SPEC, { lensNotes: notes }), ALL_OK)
    ck(typeof r.threw === 'string' && r.threw.indexOf('tier2-review: `lensNotes`') === 0 && r.threw.indexOf(word) !== -1 && r.trace.length === 0,
      'lens notes: AC6 ' + what + ' refuses before any agent, naming "' + word + '": ' + r.threw)
  }
  // ---- TOOL-dFairHearing-9 AC7: the flat and the per-preset form of one note derive one review key.
  const kFlat = await runReview(Object.assign({}, SPEC, { lensNotes: { reuse: 'N' } }), ALL_OK)
  const kPer = await runReview(Object.assign({}, SPEC, { lensNotes: { 'unit-spec': { reuse: 'N' } } }), ALL_OK)
  ck(!!kFlat.result && !!kPer.result && !!kFlat.result.key && kFlat.result.key === kPer.result.key,
    'lens notes: AC7 the flat and the per-preset form of one note derive one review key: ' + (kFlat.threw || kFlat.result.key) + ' / ' + (kPer.threw || (kPer.result && kPer.result.key)))

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
    ck(bv.length === 5 && bv.every((t) => t.prompt.indexOf('REPO: /tmp/r') !== -1 && t.prompt.indexOf('git -C "/tmp/r" diff ' + B + '...' + H) !== -1 &&
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
      sv.length === 5 && sv.every((t) => t.prompt.indexOf('PRE-EXISTING') === -1),
      'a diff skeptic is told to refute a pre-existing defect and a by-design one')
    ck(sv.every((t) => t.prompt.indexOf('/tmp/r') !== -1 && t.prompt.indexOf('s.md') !== -1 && t.prompt.indexOf('abc1234') !== -1) && sv.length === 5,
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
  r = await runReview(Object.assign({}, SPEC, { specs: [SPEC.subjects[0].path] }), ALL_OK)
  ck(typeof r.threw === 'string' && r.threw.indexOf('`specs`') !== -1 && r.trace.length === 0,
    'spec-audit: a spec that is also a subject is refused')
  r = await runReview(Object.assign({}, SPEC, { specs: ['overview.md'] }), ALL_OK)
  if (checkNoThrow(r, 'spec sibling context')) {
    const sf = scanPrompts(r, 'find:')
    ck(sf.length === 5 && sf.every((t) => t.prompt.indexOf('SIBLING CONTEXT') !== -1 && t.prompt.indexOf('  - overview.md') !== -1 && t.prompt.indexOf('log --format=%B') === -1),
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
  const SPEC_ORDER = ['coherence', 'grounding', 'reuse', 'blast-radius', 'failure-envelope']
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
  // On the SPEC kind since TOOL-dFairHearing-15: a diff review with none acquires one, armed below.
  r = await runReview(SPEC, ALL_OK)
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
  // ---- AC6: a spec audit splits over its own five lenses and sweeps the spec set.
  r = await runReview(Object.assign({}, SPEC, { checklist: CL_STR }), ALL_OK)
  if (checkNoThrow(r, 'spec-audit checklist')) {
    const fp = scanPrompts(r, 'find:')
    ck(scanSplit(r, SPEC_ORDER) && fp.every((t) => t.prompt.indexOf('against the spec set') !== -1),
      'spec-audit: the checklist splits over the spec lenses')
  }

  // ==== TOOL-dFairHearing-15 — a diff review given no `checklist` ACQUIRES one (AC1-AC4) ===============
  // Every arm is RED against the parent render, which spawns no `resume:checklist` agent: AC1's items reach
  // no prompt, and every no-checklist run logs the absent WARNING and states `absent` in RUN INTEGRITY.
  // TOOL-dFairHearing-23 S36 - the stub ends in the checker's `# by design —` head, as every whole stdout does.
  const ACQ = '# recurring-bug-class checklist for b..c (1 file(s))\n# 3 class(es) selected by an anchor + 0 universal\n\n' +
    '- [ ] ACQONEX\n- [ ] ACQTWOX\n- [ ] ACQTHREEX\n\n# by design — 0 invariant(s) this selection touches\n'
  const extractChecklistLine = (run) => {
    const sp = run.trace.find((t) => t.label === 'synth')
    return (/(^|\n)(Checklist: [^\n]*)/.exec(sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : '') || ['', '', ''])[2]
  }
  // TOOL-dFairHearing-48 S6 - a prefix of any depth: one spelling ending the memory-tree kit's directory, one not.
  const CHECKER_SPELLED = /ls-files --error-unmatch (\S*\/)?gotchas\.py/g
  r = await runReview(DIFF, buildStubs({ 'resume:checklist': { checklist: ACQ } }))
  if (checkNoThrow(r, 'FH15 checklist acquired')) {
    const cp = r.trace[0] || { label: '', prompt: '' }
    const inKit = [...cp.prompt.matchAll(CHECKER_SPELLED)].map((x) => /(^|\/)memory-tree\/$/.test(x[1] || ''))
    ck(cp.label === 'resume:checklist' && cp.prompt.indexOf('--for-diff ' + B + '..' + H) !== -1 &&
      inKit.includes(true) && inKit.includes(false),
      'FH48 AC6 FH15 AC1 the first agent is resume:checklist, naming --for-diff <base>..<head> and both checker spellings: ' + cp.label)
    ck(['ACQONEX', 'ACQTWOX', 'ACQTHREEX'].every((x, i) => scanPrompts(r, 'find:').some((t) => new RegExp('(^|\\n)C' + (i + 1) + ' \\[ \\] ' + x).test(t.prompt))),
      'FH15 AC1 the three acquired items reach the finder prompts as C1, C2 and C3')
    ck(r.logs.indexOf('checklist from --for-diff ' + B + '..' + H) !== -1 &&
      extractChecklistLine(r).indexOf('acquired by the harness from --for-diff ' + B + '..' + H) !== -1,
      'FH15 S3 an acquired checklist is logged and stated in RUN INTEGRITY: ' + extractChecklistLine(r))
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: ['CALLERONEX'] }), buildStubs({ 'resume:checklist': { checklist: ACQ } }))
  ck(!r.threw && r.scanSpawned('resume:checklist').length === 0 && scanPrompts(r, 'find:').some((t) => t.prompt.indexOf('CALLERONEX') !== -1) &&
    r.trace.length > 0 && r.trace.every((t) => t.prompt.indexOf('ACQONEX') === -1), 'FH15 AC2 a caller\'s checklist wins, and no checklist agent spawns')
  for (const [what, ret, why] of [['a checklistError', { checklistError: 'no checker tracked' }, 'no checker tracked'],
    ['stdout with no item line', { checklist: '# recurring-bug-class checklist for b..c (0 file(s))\n' }, 'no bug class selected'],
    ['a dead agent', null, 'the checklist agent died']]) {
    r = await runReview(DIFF, buildStubs({ 'resume:checklist': ret }))
    const line = extractChecklistLine(r)
    ck(!r.threw && r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf(why) !== -1) && line.indexOf(why) !== -1 &&
      line.indexOf('supplied with no item') === -1 && line.indexOf('— absent') === -1,
      'FH15 AC3 ' + what + ' is warned and named in RUN INTEGRITY, never as absent or supplied: ' + (r.threw || line))
  }
  r = await runReview(SPEC, buildStubs({ 'resume:checklist': { checklist: ACQ } }))
  ck(!r.threw && r.trace.length > 0 && r.scanSpawned('resume:checklist').length === 0 && r.trace.every((t) => t.prompt.indexOf('ACQONEX') === -1),
    'FH15 AC4 a spec audit with no checklist spawns no checklist agent')

  // ==== TOOL-aGraftedHelix-3 — the checker's by-design block becomes `byDesign`, never an item =========
  // Every arm is RED against the parent render, which reads no block: the entry is swept as item C2,
  // nothing is logged, RUN INTEGRITY carries no `By design:` clause, and nothing refuses a bad count.
  const BD_ENTRY = 'inv-one — It looks wrong. → It is the ruling. (TOOL-x-1)'
  const BD_CL = '# recurring-bug-class checklist for a (1 file(s))\n# 1 class(es) selected by an anchor + 0 universal\n\n' +
    '- [ ] BDCLASSX\n      d\n      memory/gotchas/c.md\n\n# by design — 1 invariant(s) this selection touches\n- ' + BD_ENTRY + '\n'
  const BD_LABEL = 'Intended behaviour — invariants this change touches:\n' + BD_ENTRY
  const sweptAsItem = (fp) => fp.some((t) => /(^|\n)C\d+ inv-one/.test(t.prompt))
  r = await runReview(Object.assign({}, DIFF, { checklist: BD_CL }), ALL_OK)
  if (checkNoThrow(r, 'by-design block')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    const fp = scanPrompts(r, 'find:')
    ck(r.logs.indexOf('by-design: 1 invariant(s) from the checklist\'s by-design block') !== -1 &&
      ri.indexOf('By design: 1 invariant(s) from the checklist\'s by-design block.') !== -1,
      'by-design: the block is logged and stated in RUN INTEGRITY')
    ck(fp.length === 5 && fp.every((t) => t.prompt.indexOf(BD_LABEL) !== -1) &&
      fp.filter((t) => t.prompt.indexOf('BDCLASSX') !== -1).length === 1 && !sweptAsItem(fp),
      'by-design: every lens reads the entry as intended behaviour, and no lens sweeps it as a class')
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: BD_CL, byDesign: 'BDCALLERX' }), ALL_OK)
  if (checkNoThrow(r, 'by-design block beside a caller byDesign')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    const fp = scanPrompts(r, 'find:')
    ck(r.logs.indexOf('by-design: the caller\'s byDesign') !== -1 &&
      r.logs.indexOf('by-design: 1 invariant(s) from the checklist\'s by-design block') !== -1 &&
      ri.indexOf('By design: the caller\'s byDesign; 1 invariant(s) from the checklist\'s by-design block.') !== -1,
      'by-design: a caller byDesign beside a block logs both sources, and RUN INTEGRITY names both')
    ck(fp.length === 5 && fp.every((t) => t.prompt.indexOf('Known and tracked — do not re-report:\nBDCALLERX\n' + BD_LABEL) !== -1) &&
      !sweptAsItem(fp),
      'by-design: the caller\'s value and the entry each sit under their own label, and the items still exclude the block')
  }
  r = await runReview(Object.assign({}, DIFF, { checklist: BD_CL.replace('by design — 1 invariant', 'by design — 2 invariant') }), ALL_OK)
  ck(typeof r.threw === 'string' && r.threw.indexOf('claims 2 invariant(s) and carries 1 entry line(s)') !== -1 && r.trace.length === 0,
    'by-design: a head claiming 2 over one entry refuses before any agent, naming both numbers')
  r = await runReview(Object.assign({}, DIFF, { checklist: '# recurring-bug-class checklist for a (1 file(s))\n' +
    '# 0 class(es) selected by an anchor + 0 universal\n\n# by design — 0 invariant(s) this selection touches\n' }), ALL_OK)
  if (checkNoThrow(r, 'by-design header-only remainder')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(r.logs.some((l) => l.indexOf('`checklist` was supplied with no item') !== -1) &&
      r.logs.indexOf('by-design: none supplied — no caller byDesign and a block of 0') !== -1 &&
      ri.indexOf('By design: none supplied — no caller byDesign and a block of 0.') !== -1,
      'by-design: a remainder of header lines alone is zero items, and a block of 0 is said')
  }

  // ==== TOOL-aGraftedHelix-29 — the REAL checker's --for-diff over a range that ADDS an invariant =======
  // The shell block before this runner ran the memory-tree kit's gotchas.py over a two-commit fixture:
  // `bd-base` at the base, `bd-new` added by the range, both anchored on the script it edits. Every arm
  // is RED against the parent checker, which read the block from the working tree and listed both.
  const BD_RANGE = process.argv[3] ? fs.readFileSync(process.argv[3], 'utf8') : 'PRODUCER-FAILED no output file was passed'
  const bdRan = BD_RANGE.indexOf('PRODUCER-FAILED') !== 0
  ck(bdRan, 'by-design range: the real checker ran over the fixture range' + (bdRan ? '' : ' - ' + BD_RANGE.trim()))
  r = await runReview(Object.assign({}, DIFF, { checklist: BD_RANGE }), ALL_OK)
  if (checkNoThrow(r, 'by-design range')) {
    const fp = scanPrompts(r, 'find:')
    ck(r.logs.indexOf('by-design: 1 invariant(s) from the checklist\'s by-design block') !== -1,
      'by-design range: the harness logs one invariant, the base\'s, from the real checker\'s block')
    ck(fp.length === 5 &&
      fp.every((t) => t.prompt.indexOf('Intended behaviour — invariants this change touches:\nbd-base — ') !== -1) &&
      r.trace.every((t) => t.prompt.indexOf('BDNEWLOOKS') === -1),
      'by-design range: every lens reads bd-base as intended behaviour, and no prompt carries bd-new\'s ruling')
    ck(fp.filter((t) => t.prompt.indexOf('NEW/CHANGED invariant bd-new') !== -1).length === 1,
      'by-design range: exactly one lens sweeps the added invariant as a NEW/CHANGED item')
  }
  // ---- TOOL-dFairHearing-15 AC5: the same real stdout ACQUIRED by the checklist agent keeps the checker's
  // item order as the C<n> labels and its by-design block reaches `byDesign`. RED against the parent render,
  // which spawns no checklist agent, so no item reaches a prompt and no invariant is logged.
  r = await runReview(DIFF, buildStubs({ 'resume:checklist': { checklist: BD_RANGE } }))
  if (bdRan && checkNoThrow(r, 'FH15 acquired by-design range')) {
    const fp = scanPrompts(r, 'find:')
    const acqItems = BD_RANGE.split('\n# by design')[0].replace(/\r/g, '').split('\n').filter((l) => l.indexOf('- ') === 0).map((l) => l.slice(2).replace(/\s+$/, ''))
    ck(acqItems.length > 0 && acqItems.every((x, i) => fp.filter((t) => t.prompt.indexOf('C' + (i + 1) + ' ' + x) !== -1).length === 1),
      'FH15 AC5 the acquired items reach the finders as C<n> in the checker\'s order: ' + acqItems.length + ' item(s)')
    ck(r.logs.indexOf('by-design: 1 invariant(s) from the checklist\'s by-design block') !== -1 && !fp.some((t) => /(^|\n)C\d+ bd-base/.test(t.prompt)),
      'FH15 AC5 the acquired by-design block reaches byDesign, and no lens sweeps it as a class')
  }
  // ---- TOOL-dFairHearing-23 AC27: the same real stdout cut inside its item list, or before its by-design head, is a
  // checklistError and passes no checklist. RED against the parent render, which admits any return holding one `- ` line.
  if (bdRan) {
    const bdHead = BD_RANGE.indexOf('\n# by design')
    const bdLast = BD_RANGE.lastIndexOf('\n- ', bdHead)
    for (const [what, ret] of [['cut inside its item list', BD_RANGE.slice(0, bdLast + 1)], ['cut before its by-design head', BD_RANGE.slice(0, bdHead + 1)],
      ['missing one item above its head', BD_RANGE.slice(0, bdLast + 1) + BD_RANGE.slice(bdHead + 1)]]) {
      r = await runReview(DIFF, buildStubs({ 'resume:checklist': { checklist: ret } }))
      ck(!r.threw && r.logs.some((l) => l.indexOf('WARNING: no checklist was acquired — checklistError') === 0) && r.logs.indexOf('checklist from --for-diff ' + B + '..' + H) === -1,
        'FH23 AC27 the real stdout ' + what + ' is a checklistError WARNING and passes no checklist: ' + (r.threw || r.logs.filter((l) => l.indexOf('checklist') !== -1).join(' / ')))
    }
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
    ck(vp.length === 10 && vp.every((t) => /FIXMARK-[a-z-]+/.test(t.prompt) && t.prompt.indexOf('"sound"') !== -1 &&
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
    ck(print.length === 8 && r.scanSpawned('find:').length === 0 && r.scanSpawned('verify:batch-1').length === 1,
      'fix verdict: a verify file judged over another fix is dispatched')
  }

  // ==== TOOL-aSightedSkeptic-6 — one severity rubric, a skeptic's binding grade, an uncertain verdict ==
  // Every arm is RED against the parent render: no prompt carries a rubric, the verdict schema closes
  // at confirmed and refuted, the synthesis bracket is the finder's grade, no ungraded count exists, an
  // uncertain verdict is held as neither confirmed, refuted nor unverified, and no `regraded` returns.
  const RUBRIC_END = 'how alarming the defect looks.'
  const scanRubric = (p) => {
    // Anchored on the rubric's own opening: TOOL-aEvidencedLens-4's spec acquire sentence names the
    // rubric ("graded by the SEVERITY RUBRIC below"), and a bare-name search took that line instead.
    const i = p.indexOf('SEVERITY RUBRIC - grade')
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
    ck(scanRubricOk(rrd, 11) && scanRubricOk(rrs, 11), 'severity: one rubric reaches every finder, skeptic and synthesis prompt')
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
  r = await runReview(DIFF, buildStubs({ 'verify:batch-3': buildGradedVerdicts('uncertain') }))
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
  ck(uvp.length === 10 && uvp.every((t) => t.prompt.indexOf('graded blocker or high is answered "uncertain"') !== -1 &&
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
  r = await runReview(DIFF, buildStubs({ 'verify:': buildGradedVerdicts('confirmed', () => 'blocker'), 'verify:batch-2': null }))
  if (checkNoThrow(r, 'observed-by dead batch')) {
    const cl = scanConfirmedLogs(r)
    ck(cl.length === 4 && cl.every((l) => l.indexOf('  CONFIRMED [blocker] ') === 0),
      'observed-by: a dead skeptic batch logs every CONFIRMED finding at its binding grade')
  }
  // ---- S3: one uncertain answer, counted apart from no verdict in the note, RUN INTEGRITY and the log.
  r = await runReview(DIFF, buildStubs({ 'verify:batch-3': buildGradedVerdicts('uncertain') }))
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
  r = await runReview(DIFF, buildStubs({ 'verify:batch-2': null }))
  if (checkNoThrow(r, 'ledger deferred log')) {
    const dl = r.logs.filter((l) => /^ {2}(CONFIRMED|UNVERIFIED) \[/.test(l))
    ck(dl.length === 5 && dl.every((l) => { const m = / lens=([a-z-]+) ([a-z-]+)\.js:1 - /.exec(l); return !!m && m[1] === m[2] }),
      'ledger: the skeptic and synthesis lines name the lens: the deferred path\'s log lines')
  }

  // ---- AC3: one batch per state. id 1 refuted, 2 uncertain, 3 no verdict, 4 contradicted, 5 confirmed
  // ---- at low with an unsound fix.
  const VS = {
    'verify:batch-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'r1' }] },
    'verify:batch-2': { path: '/v', verdicts: [{ id: 2, verdict: 'uncertain', reason: 'r2' }] },
    'verify:batch-3': { path: '/v', verdicts: [] },
    'verify:batch-4': { path: '/v', verdicts: [{ id: 4, verdict: 'confirmed', reason: 'a' }, { id: 4, verdict: 'refuted', reason: 'b' }] },
    'verify:batch-5': { path: '/v', verdicts: [{ id: 5, verdict: 'confirmed', reason: 'r5', severity: 'low', fixVerdict: 'unsound', fixNote: 'n5' }] },
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
  r = await runReview(DIFF, buildStubs({ 'verify:batch-2': unsound2 }))
  if (checkNoThrow(r, 'ledger rejected fix')) {
    const c2 = Array.isArray(r.result.confirmedFindings) ? r.result.confirmedFindings : []
    ck(c2.length === 5 && c2[1].fix === 'better fix' && c2[1].fixVerdict === 'unsound' && c2[1].severity === 'blocker' &&
      c2.filter((e, i) => i !== 1).every((e) => e.fix === 'f' && e.severity === 'high'),
      'ledger: confirmedFindings feeds the next round: a rejected fix is replaced by the skeptic\'s note, at the binding grade')
  }
  // ---- Closing review round 1, L3 (finding 16): an EMPTY or blank note is no correction, so the
  // ---- finder's fix stays, marked by fixVerdict unsound; dropping the `&& note` guard hands on ''.
  for (const [what, note] of [['an empty note', ''], ['a blank note', '   ']]) {
    r = await runReview(DIFF, buildStubs({ 'verify:batch-2': { path: '/v', verdicts: [{ id: 2, verdict: 'confirmed', reason: 'r', fixVerdict: 'unsound', fixNote: note }] } }))
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
  r = await runReview(DIFF, buildStubs({ 'find:': buildPipeLens, 'verify:batch-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'x | y\r\nz' }] } }))
  if (checkNoThrow(r, 'ledger appendix')) {
    const ap = typeof r.result.appendix === 'string' ? r.result.appendix : ''
    const al = ap.split('\n')
    const rows = al.slice(4)
    const unescaped = (row) => row.split('').filter((ch, i) => ch === '|' && row[i - 1] !== '\\').length
    ck(al[0] === '## Appendix — every finding' && al[1] === '' &&
      al[2] === '| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |' && al[3] === '|---|---|---|---|---|---|---|---|---|---|' &&
      rows.length === 5 && rows.length === r.result.ledger.length && rows[0].indexOf('| 1 | security | security.js:1 | high | - | refuted |') === 0,
      'ledger: the appendix is rendered by the harness: heading, ten columns, one row per finding, the refuted one included')
    ck(rows.length === 5 && rows.every((row) => unescaped(row) === 11) && rows[0].indexOf('x \\| y z') !== -1 && ap.indexOf('\r') === -1,
      'ledger: the appendix is rendered by the harness: a pipe and a line break in a cell leave the row count unchanged')
    // TOOL-dFairHearing-8 S8 - the synthesis's copy differs from the returned one in each confirmed row's
    // disposition cell alone: `(synthesis)` there, `-` in the return, since this stub returns no dispositions.
    const sp = r.trace.find((t) => t.label === 'synth')
    const handed = al.map((l) => (l.indexOf(' | confirmed | ') !== -1 ? l.replace(/ - \|$/, ' (synthesis) |') : l)).join('\n')
    ck(ap.length > 0 && !!sp && handed !== ap && sp.prompt.indexOf(handed) !== -1 && sp.prompt.indexOf('VERBATIM') !== -1,
      'ledger: the appendix is handed to the synthesis verbatim but for the confirmed rows\' (synthesis) cells')
  }
  // ---- Closing review round 1, L2: a reason carrying every other boundary Python's str.splitlines
  // ---- breaks on. The appendix must split into the same lines under that rule as under `\n`.
  r = await runReview(DIFF, buildStubs({ 'verify:batch-1': { path: '/v', verdicts: [{ id: 1, verdict: 'refuted', reason: 'p\u2028q\u2029r\x85s\x0bt\x0cu\x1cv\x1ew' }] } }))
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
      al[2].endsWith(' | fixVerdict | classes | disposition |') && al[4].endsWith(' | beta-two | - |') && al[5].endsWith(' | alpha-one C9 | - |') &&
      al.slice(6).every((row) => row.endsWith(' | - | - |')),
      'ledger: classes resolves each head label to its item slug, keeps C<n> out of range, and renders - when unlabelled')
  }

  // ---- AC6: six exit paths. `confirmed` keeps its per-path type, which unattended-build.js reads.
  const fieldsOk = (run) => !!run.result && Array.isArray(run.result.ledger) && Array.isArray(run.result.confirmedFindings) && typeof run.result.appendix === 'string'
  const paths = [
    ['every lens dead', buildStubs({ 'find:': null }), 'array', (x) => x.ledger.length === 0 && x.appendix === ''],
    ['no finding raised', buildStubs({ 'find:': buildEmptyLens }), 'array', (x) => x.ledger.length === 0 && x.appendix === ''],
    ['every finding refuted', buildStubs({ 'verify:': buildVerdicts('refuted') }), 'array',
      (x) => x.ledger.length === 5 && x.ledger.every((e) => e.verdict === 'refuted') && x.confirmedFindings.length === 0 && x.appendix.split('\n').length === 9],
    ['one skeptic batch dead', buildStubs({ 'verify:batch-2': null }), 'integer',
      (x) => x.exit === 'deferred-platform' && x.ledger.length === 5 && x.ledger[1].verdict === 'unverified' && x.confirmedFindings.length === 4],
    ['the synthesis dead', buildStubs({ synth: null }), 'integer', (x) => x.exit === 'deferred-platform' && x.ledger.length === 5 && x.confirmedFindings.length === 5],
    ['complete', ALL_OK, 'integer', (x) => x.exit === 'complete' && x.ledger.length === 5 && x.confirmedFindings.length === 5 && x.appendix.length > 0],
  ]
  // Closing review round 1, L3 (finding 19): `regraded` is an array where a synthesis ran, which is the
  // complete path alone, and ABSENT on the other five, since no adjudicated count exists there.
  let regradedSeen = 0
  const regradedWrong = []
  // TOOL-aMendedFleet-18 - each exit's `shape` matches the S1 grammar at the stage its path reaches,
  // is logged, and reads `out-tokens=unknown` because the stub runtime's `budget` has no `spent`.
  const SHAPE_RE = /^review-shape kind=(diff-review|spec-audit) round=\d+ intensity=(full|light) at=(find|verify|synth) raw=(\d+|-) confirmed=(\d+|-) refuted=(\d+|-) merged=(\d+|-) unverified=(\d+|-) blocker=(\d+|-) high=(\d+|-) medium=(\d+|-) low=(\d+|-) agents=\d+ out-tokens=unknown$/
  const shapeStage = { 'every lens dead': 'find', 'no finding raised': 'find', 'every finding refuted': 'verify',
    'one skeptic batch dead': 'verify', 'the synthesis dead': 'synth', complete: 'synth' }
  let shapeSeen = 0
  const shapeWrong = []
  let synthPromptShape = false
  for (const [what, stubs, ctype, extra] of paths) {
    r = await runReview(DIFF, stubs)
    if (!checkNoThrow(r, 'ledger exit ' + what)) continue
    const typed = ctype === 'array' ? Array.isArray(r.result.confirmed) : Number.isInteger(r.result.confirmed)
    ck(fieldsOk(r) && typed && extra(r.result), 'ledger: every exit path carries the ledger: ' + what)
    regradedSeen++
    if (what === 'complete' ? !Array.isArray(r.result.regraded) : 'regraded' in r.result) regradedWrong.push(what)
    shapeSeen++
    const sh = typeof r.result.shape === 'string' ? r.result.shape : ''
    if (!SHAPE_RE.test(sh) || sh.indexOf(' at=' + shapeStage[what] + ' ') === -1 || r.logs.indexOf(sh) === -1) shapeWrong.push(what)
    if (what === 'complete') {
      const sp = r.trace.find((t) => t.label === 'synth')
      synthPromptShape = !!sp && sh.length > 0 && sp.prompt.indexOf('<<<SHAPE\n' + sh + '\nSHAPE>>>') !== -1 &&
        sh.indexOf(' raw=5 confirmed=5 refuted=0 merged=0 unverified=0 ') !== -1 && sh.indexOf(' agents=11 ') !== -1
    }
  }
  ck(regradedSeen === 6 && regradedWrong.length === 0,
    'severity: regraded is returned only where a synthesis ran, over the six exit paths' + (regradedWrong.length ? ' — wrong on: ' + regradedWrong.join(', ') : ''))
  ck(shapeSeen === 6 && shapeWrong.length === 0,
    'shape: every exit returns and logs a review-shape line at the stage it reached, out-tokens unknown under the stub' + (shapeWrong.length ? ' — wrong on: ' + shapeWrong.join(', ') : ''))
  ck(synthPromptShape, 'shape: the synthesis is handed the at=synth line the complete return carries, with the run\'s counts')

  // ==== TOOL-aEvidencedLens-3 — the spec skeptic confirms by the rubric, re-runs the evidence, and an
  // ==== ORPHANED duplicate is demoted. One finding per lens carries one-line, two-line or no evidence;
  // ==== two per lens put ids 1 and 2 in one batch, verify:batch-1.
  const EVID = { coherence: 'cmd: grep -c x a.md -> 0', grounding: 'line one\nline two' }
  const buildEvidenceLens = (label) => {
    const out = buildLensReturn(label)
    if (EVID[out.lens]) out.findings[0].evidence = EVID[out.lens]
    return out
  }
  const buildPairLens = (label) => {
    const lens = label.slice('find:'.length)
    const mk = (n) => ({ file: lens + '.md', line: n, where: 'section ' + n, severity: 'medium', claim: lens + ' claim ' + n, impact: 'i', fix: 'f', evidence: 'read: x.md:' + n })
    return { lens: lens, path: '/p', findings: [mk(1), mk(2)] }
  }
  const buildSkepticAnswers = (over) => (label, prompt) => {
    const m = /ids ([0-9, ]+)\)/.exec(prompt)
    const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
    return { path: '/v', verdicts: ids.map((id) => Object.assign({ id: id, verdict: 'confirmed', reason: 'r', severity: 'medium', fixVerdict: 'sound' }, over[id] || {})) }
  }
  const extractProbeSlice = (p) => { const at = p.indexOf('PROBE POLICY'); return at === -1 ? null : p.slice(at, p.indexOf('\n\n', at)) }
  r = await runReview(SPEC, buildStubs({ 'find:': buildEvidenceLens }))
  if (checkNoThrow(r, 'spec skeptic evidence run')) {
    const sv = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
    const sfp = r.trace.filter((t) => t.label.indexOf('find:') === 0)
    const marks = ['AT ANY RUBRIC SEVERITY', 'NON-GOAL', 'ALREADY SAYS', 'FALSE ON RE-PROBE', 'BY DESIGN', 'duplicate of id=', 'duplicate of prior', 'PREFERENCE',
      'could not run inside its bound', "apply the default by the finder's grade", 'a claim about code or a record is checked against that code or record',
      "re-run the finding's evidence", "never confirm on the finder's word"]
    ck(sv.length === 5 && sv.every((t) => marks.every((w) => t.prompt.indexOf(w) !== -1) && t.prompt.indexOf('unbuildable or wrong') === -1 && t.prompt.indexOf('not a refutation') === -1),
      'spec skeptic: every verify prompt confirms at any rubric severity, names the six refutation cases and the grade default, and drops the old test')
    const lineOf = (id) => sv.map((t) => t.prompt.split('\n').find((l) => l.indexOf('id=' + id + ' [') === 0)).find(Boolean) || ''
    ck(/ \| fix: f \| evidence: cmd: grep -c x a\.md -> 0$/.test(lineOf(1)) && / \| fix: f \| evidence: line one line two$/.test(lineOf(2)) &&
      / \| fix: f \| evidence: -$/.test(lineOf(3)) && !sv.some((t) => /^line two/m.test(t.prompt)),
      'spec skeptic: one-line, two-line and absent evidence ride the verify line after fix, folded to one line, absent as -')
    const fslice = sfp.length ? extractProbeSlice(sfp[0].prompt) : null
    ck(!!fslice && sv.every((t) => extractProbeSlice(t.prompt) === fslice && t.prompt.indexOf('PROBE POLICY') < t.prompt.indexOf('Findings to judge:')),
      'spec skeptic: the verify prompt carries the finders\' PROBE POLICY bytes, before Findings to judge:')
  }
  // ==== TOOL-aEvidencedLens-12 — the skeptic RE-RUNS the evidence, so it is folded by renderPromptLine:
  // ==== line breaks only. RED against the unit's predecessor render, whose renderCell wrote `\|`.
  const PIPED = { coherence: 'cmd: git ls-files | grep -c spec -> 11', grounding: 'cmd: git ls-files | grep x\n-> 2', reuse: '\n' }
  r = await runReview(SPEC, buildStubs({ 'find:': (label) => { const out = buildLensReturn(label); if (PIPED[out.lens] !== undefined) out.findings[0].evidence = PIPED[out.lens]; return out } }))
  if (checkNoThrow(r, 'spec evidence: pipe run')) {
    const pv = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
    const pline = (id) => pv.map((t) => t.prompt.split('\n').find((l) => l.indexOf('id=' + id + ' [') === 0)).find(Boolean) || ''
    ck(pline(1).endsWith(' | fix: f | evidence: cmd: git ls-files | grep -c spec -> 11') && pline(2).endsWith(' | evidence: cmd: git ls-files | grep x -> 2') &&
      !pv.some((t) => t.prompt.indexOf('\\|') !== -1 || /^-> 2/m.test(t.prompt)),
      'spec evidence: a pipe in evidence reaches the verify line unescaped, byte for byte, and a line break folds to one space')
    ck(pline(3).endsWith(' | fix: f | evidence: -'), 'spec evidence: evidence that is only a line break reads | evidence: -')
  }
  r = await runReview(SPEC, buildStubs({ 'find:': buildPairLens, 'verify:': buildSkepticAnswers({ 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }) }))
  if (checkNoThrow(r, 'spec skeptic kept duplicate')) {
    const row = (r.result.ledger || []).find((e) => e.id === 2) || {}
    ck(r.trace.some((t) => t.label === 'verify:batch-1') && row.verdict === 'refuted' && row.reason === 'duplicate of id=1' && !r.logs.some((l) => /DUPLICATE of an id/.test(l)),
      'spec skeptic: a duplicate of a confirmed survivor in its batch stays refuted, unannounced')
  }
  // TOOL-dFairHearing-5 S2 - the kind is a parameter, so the diff kind's orphans run the same arm (AC4).
  const runOrphanArm = async (over, what, args, kname) => {
    r = await runReview(args || SPEC, buildStubs({ 'find:': buildPairLens, 'verify:': buildSkepticAnswers(over) }))
    if (!checkNoThrow(r, (kname || 'spec') + ' skeptic orphan ' + what)) return
    const row = (r.result.ledger || []).find((e) => e.id === 2) || {}
    const sp = r.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(r.result.unverified >= 1 && row.verdict === 'unverified' && row.reason === 'duplicate of an unconfirmed id' &&
      r.logs.some((l) => l.indexOf('WARNING:') === 0 && /DUPLICATE of an id/.test(l) && / ids 2$/.test(l)) &&
      ri.indexOf('1 orphaned duplicate refutation(s) demoted to unverified') !== -1,
      (kname || 'spec') + ' skeptic: a duplicate of ' + what + ' is demoted to unverified, ledgered, warned and counted in RUN INTEGRITY')
  }
  await runOrphanArm({ 1: { verdict: 'refuted', reason: 'r' }, 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }, 'a refuted survivor')
  await runOrphanArm({ 2: { verdict: 'refuted', reason: 'duplicate of id=2' } }, 'its own id')
  await runOrphanArm({ 2: { verdict: 'refuted', reason: 'duplicate of id=3' } }, 'an id in another batch')
  r = await runReview(DIFF, buildStubs({ 'find:': buildPairLens, 'verify:': buildSkepticAnswers({ 1: { verdict: 'refuted', reason: 'r' }, 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }) }))
  if (checkNoThrow(r, 'spec skeptic diff kind')) {
    const row = (r.result.ledger || []).find((e) => e.id === 2) || {}
    const dv = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
    // TOOL-dFairHearing-5 S2 - inverted: the base harness skipped the diff kind's orphan check.
    ck(dv.length > 0 && dv.every((t) => t.prompt.indexOf(' | evidence: ') === -1 && t.prompt.indexOf('PROBE POLICY') === -1) &&
      row.verdict === 'unverified' && r.logs.some((l) => /DUPLICATE of an id/.test(l)),
      'spec skeptic: a diff-kind verify prompt carries no evidence field and no probe policy, and its orphaned duplicate refutation is scanned')
  }

  // ==== TOOL-dFairHearing-5 — a same-batch duplicate counts as a MERGED confirmation on both kinds, and
  // ==== the orphan check runs on the diff kind. RED against the base harness, which defines no
  // ==== extractDuplicateTarget, counts the duplicate as refuted, skips the diff kind's orphan check
  // ==== and gives the diff skeptic no duplicate form. buildPairLens puts ids 1 and 2 in verify:batch-1.
  // AC4 - the diff kind's orphans, through the spec arm's own runner.
  await runOrphanArm({ 2: { verdict: 'refuted', reason: 'duplicate of id=3' } }, 'an id in another batch', DIFF, 'diff')
  await runOrphanArm({ 1: { verdict: 'refuted', reason: 'r' }, 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }, 'a refuted survivor', DIFF, 'diff')
  // AC1 - the reason form, read from the prelude.
  {
    let dt = null
    try { dt = new Function('args', 'log', 'parallel', 'agent', 'phase', body + '\nreturn extractDuplicateTarget')(base, () => {}, null, null, null) } catch (e) { console.log('HARNESS-BROKEN merged: ' + e.message) }
    const got = dt ? ['duplicate of id=4', '  Duplicate of id=12: same claim', 'duplicate of prior a.js:3', 'dup of id=4', '', undefined].map((x) => dt(x)) : []
    ck(JSON.stringify(got) === '[4,12,null,null,null,null]', 'merged: extractDuplicateTarget reads id=4 and a cased, padded id=12, and a prior ref, another word, empty and undefined as null: ' + JSON.stringify(got))
  }
  for (const [kname, kargs] of [['diff', DIFF], ['spec', SPEC]]) {
    // AC2, AC3, AC6 - id 2 refuted as a duplicate of id 1, its confirmed batch-mate.
    r = await runReview(kargs, buildStubs({ 'find:': buildPairLens, 'verify:': buildSkepticAnswers({ 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }) }))
    if (checkNoThrow(r, 'merged ' + kname)) {
      const x = r.result
      const row = (x.ledger || []).find((e) => e.id === 2) || {}
      const yr = (x.lensYield || []).find((e) => e.lens === row.lens) || {}
      ck(x.confirmed === 9 && x.merged === 1 && x.refuted === 0 && x.precision === 1 && String(x.shape).indexOf(' refuted=0 merged=1 ') !== -1 &&
        yr.merged === 1 && yr.refuted === 0 && yr.precision === 1,
        'merged: ' + kname + ' — a same-batch duplicate reads confirmed 9, merged 1, refuted 0, precision 1, in the shape and its lens\'s yield row')
      const arow = String(x.appendix || '').split('\n').find((l) => l.indexOf('| 2 |') === 0) || ''
      ck(row.verdict === 'refuted' && row.reason === 'duplicate of id=1' && arow.indexOf('| refuted | duplicate of id=1 |') !== -1,
        'merged: ' + kname + ' — the ledger and appendix keep the skeptic\'s refuted verdict and duplicate reason')
      const sp = r.trace.find((t) => t.label === 'synth')
      const conf = sp ? sp.prompt.split('UNVERIFIED findings')[0] : 'id=2 ['
      const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
      ck(!(x.confirmedFindings || []).some((f) => f.id === 2) && conf.indexOf('id=2 [') === -1 && x.blockers === 0 && x.highs === 9 &&
        ri.indexOf('1 duplicate refutation(s) counted as merged confirmations') !== -1 && sp.prompt.indexOf(', refuted 0, merged 1, ') !== -1,
        'merged: ' + kname + ' — the merged id stays out of the confirmed set and the CONFIRMED list, the tally holds, and the synthesis states merged')
    }
    // AC3 - a duplicate of a prior round's finding is no merge.
    r = await runReview(kargs, buildStubs({ 'find:': buildPairLens, 'verify:': buildSkepticAnswers({ 2: { verdict: 'refuted', reason: 'duplicate of prior a.js:3' } }) }))
    if (checkNoThrow(r, 'merged prior ' + kname)) {
      ck(r.result.merged === 0 && r.result.refuted === 1, 'merged: ' + kname + ' — a `duplicate of prior` refutation stays refuted, merged 0')
    }
  }
  // AC5 - the diff skeptic is given the duplicate form, on every batch.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'merged diff prompt')) {
    const dv = r.trace.filter((t) => t.label.indexOf('verify:') === 0)
    ck(dv.length === 5 && dv.every((t) => t.prompt.indexOf('duplicate of id=<n>') !== -1), 'merged: every diff verify prompt carries the `duplicate of id=<n>` form')
  }

  // ==== TOOL-aEvidencedLens-4 — a spec fold round reads its diff, and a moved subject is graded, not
  // ==== fixed at BLOCKER. Every arm is RED against the parent render, which prints no FOLD DIFF, no
  // ==== DEGRADED, no `move check:` clause and asks the probe for no hash.
  const extractIntegrity = (run) => { const sp = run.trace.find((t) => t.label === 'synth'); return sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : '' }
  const P40 = 'a'.repeat(40)
  const D40 = 'd'.repeat(40)
  const E40 = 'e'.repeat(40)
  const THREE = [{ path: 'memory/builds/dX/spec/one.md', blob: D40, id: 'TOOL-x-1', rev: 1, prevBlob: P40 }, { path: 'memory/builds/dX/spec/two.md', blob: E40, id: 'TOOL-x-2', rev: 1, prevBlob: E40.slice(0, 9) }, { path: 'memory/builds/dX/spec/three.md', blob: 'abc1234', id: 'TOOL-x-3', rev: 1 }]
  r = await runReview(Object.assign({}, SPEC, { round: 2, subjects: THREE, priorFindings: [{ ref: 'one.md:section 2', claim: 'PRIOR' }] }), ALL_OK)
  if (checkNoThrow(r, 'fold three shapes')) {
    const fv = scanPrompts(r, 'find:').concat(scanPrompts(r, 'verify:'))
    const extractFoldLine = (p, path) => p.split('\n').find((l) => l.indexOf('  - ' + path + ': ') === 0) || ''
    ck(fv.length === 10 && fv.every((t) => t.prompt.indexOf('FOLD DIFF') !== -1 && t.prompt.indexOf('first-round') === -1 &&
      extractFoldLine(t.prompt, 'memory/builds/dX/spec/one.md') === '  - memory/builds/dX/spec/one.md: git -C "/tmp/r" diff ' + P40 + ' ' + D40 &&
      extractFoldLine(t.prompt, 'memory/builds/dX/spec/two.md') === '  - memory/builds/dX/spec/two.md: unchanged since the previous round' &&
      extractFoldLine(t.prompt, 'memory/builds/dX/spec/three.md') === '  - memory/builds/dX/spec/three.md: no prevBlob was supplied - review this file whole'),
      'fold: a round-2 spec run carries each subject\'s FOLD DIFF line in every find: and verify: prompt')
    ck(r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('three.md') !== -1) && !r.logs.some((l) => l.indexOf('WARNING:') === 0 && /\b(one|two)\.md/.test(l)) &&
      extractIntegrity(r).indexOf('fold diff: 2 of 3 subject(s) carried prevBlob.') !== -1,
      'fold: a WARNING names the subject lacking prevBlob, and RUN INTEGRITY says 2 of 3')
  }
  r = await runReview(Object.assign({}, SPEC, { round: 2 }), ALL_OK)
  if (checkNoThrow(r, 'fold degraded')) {
    const ff = scanPrompts(r, 'find:')
    ck(ff.length === 5 && r.trace.every((t) => t.prompt.indexOf('first-round review') === -1) &&
      ff.every((t) => t.prompt.indexOf('DEGRADED fold review') !== -1 && t.prompt.indexOf('none supplied for this round-2 review') !== -1 && t.prompt.indexOf('FOLD DIFF') === -1) &&
      r.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('DEGRADED') !== -1) && extractIntegrity(r).indexOf('DEGRADED') !== -1,
      'fold: a round-2 run with neither input is a DEGRADED fold review, warned and in RUN INTEGRITY, never first-round')
  }
  const MOVED40 = 'f0' + '1'.repeat(38)
  const TWO = Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/spec/m.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1 }, { path: 'memory/builds/dX/spec/u.md', blob: 'abc9999', id: 'TOOL-x-2', rev: 1 }] })
  r = await runReview(TWO, buildStubs({ 'resume:probe': Object.assign(buildProbe(), { blobs: [{ path: 'memory/builds/dX/spec/m.md', now: MOVED40 }, { path: 'memory/builds/dX/spec/u.md', now: '' }] }) }))
  if (checkNoThrow(r, 'fold moved')) {
    const ri = extractIntegrity(r)
    ck(r.logs.some((l) => l.indexOf('WARNING: memory/builds/dX/spec/m.md MOVED') === 0 && l.indexOf('abc1234') !== -1 && l.indexOf(MOVED40) !== -1) && !r.logs.some((l) => l.indexOf('u.md MOVED') !== -1) &&
      scanPrompts(r, 'find:').length === 5 && scanPrompts(r, 'find:').every((t) => t.prompt.indexOf('  - memory/builds/dX/spec/m.md  blob abc1234  MOVED since pinned, now ' + MOVED40) !== -1 && t.prompt.indexOf('  - memory/builds/dX/spec/u.md  blob abc9999\n') !== -1) &&
      ri.indexOf('m.md MOVED from pinned abc1234 to ' + MOVED40) !== -1 && ri.indexOf('UNCHECKED, no usable current blob: memory/builds/dX/spec/u.md.') !== -1,
      'fold: a moved and an unusable blob: the WARNING, the MOVED SUBJECT line and RUN INTEGRITY name each')
    const pp = r.trace.find((t) => t.label === 'resume:probe')
    ck(!!pp && pp.prompt.indexOf('hash-object') !== -1 && pp.prompt.indexOf('  - memory/builds/dX/spec/m.md') !== -1 && pp.prompt.indexOf('  - memory/builds/dX/spec/u.md') !== -1 &&
      !!pp.schema.properties.blobs && pp.schema.required.indexOf('blobs') === -1 &&
      r.trace.every((t) => t.prompt.indexOf('as a BLOCKER finding') === -1 && t.prompt.indexOf('diff -u - ') === -1) &&
      scanPrompts(r, 'find:').every((t) => t.prompt.indexOf('diff <blob> -- <path>') !== -1 && t.prompt.indexOf('SEVERITY RUBRIC') !== -1),
      'fold: the spec probe asks for hash-object per subject with blobs optional, and no prompt carries the fixed BLOCKER')
  }
  r = await runReview(TWO, buildStubs({ 'resume:probe': null }))
  if (checkNoThrow(r, 'fold null probe')) ck(extractIntegrity(r).indexOf('move check: the resume probe died') !== -1, 'fold: a null probe reads as the resume probe died, never as no move')
  r = await runReview(TWO, ALL_OK)
  if (checkNoThrow(r, 'fold no blobs key')) {
    const ri = extractIntegrity(r)
    ck(ri.indexOf('UNCHECKED, no usable current blob: memory/builds/dX/spec/m.md, memory/builds/dX/spec/u.md.') !== -1 && ri.indexOf('the resume probe died') === -1,
      'fold: a live probe with no blobs key leaves every subject UNCHECKED, not died')
  }
  // TOOL-aEvidencedLens-21 AC9 (closing review L2) - the NOT-MOVED arm: a 40-hex `now` that BEGINS with the
  // pin is the same blob. Red on a render copy whose MOVED predicate always holds.
  const SAME40 = 'abc1234' + '0'.repeat(33)
  const PAIR = Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/spec/m.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1 }, { path: 'memory/builds/dX/spec/v.md', blob: 'abc9999', id: 'TOOL-x-2', rev: 1 }] })
  r = await runReview(PAIR, buildStubs({ 'resume:probe': Object.assign(buildProbe(), { blobs: [{ path: 'memory/builds/dX/spec/m.md', now: SAME40 }, { path: 'memory/builds/dX/spec/v.md', now: MOVED40 }] }) }))
  if (checkNoThrow(r, 'fold unmoved beside moved')) {
    ck(!r.logs.some((l) => l.indexOf('m.md MOVED') !== -1) && r.logs.some((l) => l.indexOf('WARNING: memory/builds/dX/spec/v.md MOVED') === 0) &&
      scanPrompts(r, 'find:').length === 5 && scanPrompts(r, 'find:').every((t) => t.prompt.indexOf('  - memory/builds/dX/spec/m.md  blob abc1234\n') !== -1),
      'fold: a now beginning with the pin is NOT MOVED beside a moved subject: no WARNING and no MOVED suffix')
  }
  r = await runReview(Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/spec/m.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1 }] }),
    buildStubs({ 'resume:probe': Object.assign(buildProbe(), { blobs: [{ path: 'memory/builds/dX/spec/m.md', now: SAME40 }] }) }))
  if (checkNoThrow(r, 'fold unmoved alone')) {
    ck(!r.logs.some((l) => l.indexOf('m.md MOVED') !== -1) && scanPrompts(r, 'find:').length === 5 &&
      scanPrompts(r, 'find:').every((t) => t.prompt.indexOf('  - memory/builds/dX/spec/m.md  blob abc1234\n') !== -1) && extractIntegrity(r).indexOf('no checked subject moved') !== -1,
      'fold: the sole subject, unmoved, reads no checked subject moved in RUN INTEGRITY')
  }
  const deriveFoldKey = async (pb) => {
    const x = await runReview(Object.assign({}, SPEC, { round: 2, priorFindings: [{ ref: 'a', claim: 'b' }], subjects: [{ path: 'memory/builds/dX/spec/s.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1, prevBlob: pb }] }), ALL_OK)
    return x.result ? x.result.key : 'threw'
  }
  const k0 = await deriveFoldKey(undefined)
  const k1 = await deriveFoldKey('abc1230')
  const k2b = await deriveFoldKey('abc1231')
  ck(k1 !== 'threw' && k0 !== k1 && k1 !== k2b && k0 !== k2b, 'fold: the review key moves with prevBlob')
  await runLensYieldArms()
  await runRolesArms()
  await runEffortsArms()
  await runAddressArms()
  await runGradesArms()
  await runTwinArms()
  await runPresetArms()
  await runOptInArms()
  await runTypedStageArms()
  await runTwinRunArms()
  await runDispositionArms()
  await runRoundStateArms()
  await runWalkArms()
}

// ==== TOOL-dFairHearing-17 AC5 — the round state on the returns and in the synthesis prompt ====
// Red against the base harness, whose returns carry no roundState and whose prompt carries no ROUND block.
async function runRoundStateArms() {
  // One finding confirmed at high, the rest refuted: the count is 1, round 3 sits at its limit of 3.
  const confirmOne = (label, prompt) => {
    const m = /ids ([0-9, ]+)\)/.exec(prompt)
    const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
    return { path: '/cd/v.json', verdicts: ids.map((id) => ({ id: id, verdict: id === 1 ? 'confirmed' : 'refuted', reason: 'r' })) }
  }
  const RS = Object.assign({}, DIFF, { round: 3, priorCounts: [4, 2], roundLimit: 3 })
  let r = await runReview(RS, buildStubs({ 'verify:': confirmOne }))
  if (checkNoThrow(r, 'round state stub run')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(r.result.exit === 'complete' && r.result.roundState === 'BOUNDED' && r.result.roundCount === 1,
      'round state: a complete round 3 at limit 3 after [4, 2] with one high returns BOUNDED and count 1: ' + r.result.roundState + ' ' + r.result.roundCount)
    ck(!!sp && sp.prompt.indexOf('<<<ROUND\nreview-round round=3 limit=3 prior=4,2 count=1 state=BOUNDED\nROUND>>>') !== -1,
      'round state: the synthesis prompt carries the review-round line between the ROUND markers')
  }
  r = await runReview(RS, buildStubs({ 'verify:': confirmOne, 'find:seams': null }))
  ck(!r.threw && r.result.exit === 'deferred-platform' && r.result.roundState === null && r.result.roundCount === null,
    'round state: a run with a dead lens defers and reports no state: ' + (r.result && r.result.roundState))
  r = await runReview(Object.assign({}, DIFF, { round: 2 }), ALL_OK)
  ck(!r.threw && r.result.roundState === null && Number.isInteger(r.result.roundCount) &&
    r.logs.some((l) => l.indexOf('WARNING') === 0 && l.indexOf('priorCounts') !== -1),
    'round state: round 2 with no priorCounts returns a null state, an integer count, and a WARNING naming priorCounts')
  r = await runReview(DIFF, buildStubs({ 'find:': buildEmptyLens }))
  ck(!r.threw && r.result.exit === 'complete' && r.result.roundState === 'CONVERGED' && r.result.roundCount === 0,
    'round state: a round whose lenses raise nothing returns CONVERGED and count 0: ' + (r.result && r.result.roundState))
}

// ==== TOOL-dFairHearing-18 AC4-AC6 — the whole-design walk over stub walkers ====================================
// Each walker stub returns one row per CELLS line of its own prompt, every field `=` and the verdict holds, plus
// the findings asked for, the first cell of a walker with a finding reading `finding`. Against the base harness,
// which refuses the preset, no run completes and every arm reds.
async function runWalkArms() {
  const KEY = 'e'.repeat(64)
  const SCEN = ['S1', 'S2', 'S3', 'S4', 'S5'].map((id) => ({ id: id, name: 'name ' + id, walks: 'walks ' + id }))
  const ITEMS = ['plan.input', 'plan.output', 'act.spawn', 'act.reap'].map((t, i) => ({ tag: t, step: 's' + (i >> 1) }))
  const WD = Object.assign({}, SPEC, { preset: 'whole-design', subjects: [{ path: 'memory/builds/dX/build/d.md', blob: 'abc1234', id: 'PLAY-dX-1' }],
    walk: { items: ITEMS, scenarios: SCEN, run: 1, keySha: KEY } })
  const readCells = (prompt) => {
    const at = prompt.indexOf('CELLS of your slice')
    return at === -1 ? [] : prompt.slice(at).split('\n').slice(1).filter((l) => l.indexOf('  - ') === 0).map((l) => l.slice(4).split(' · '))
  }
  const buildWalker = (over) => (label, prompt) => {
    const o = over || {}
    const lens = label.slice('find:'.length)
    const n = typeof o.findings === 'function' ? o.findings(lens) : o.findings || 0
    const findings = Array.from({ length: n }, (_, k) => ({ file: 'd.md', where: '[plan] ' + lens, severity: 'high', claim: lens + ' claim ' + k, impact: 'i', fix: 'f', evidence: 'read: d.md:1' }))
    const walk = readCells(prompt).map((c, i) => ({ item: c[0], scenario: c[1], actor: '=', needs: '=', witness: o.blank === lens && i === 0 ? '  ' : '=', route: '=',
      verdict: n && i === 0 ? 'finding' : 'holds', findings: n && i === 0 ? [0] : [] }))
    return { lens: lens, path: '/cd/review-lenses/k/find-' + lens + '.json', findings: findings, walk: walk }
  }
  const WALK_OK_STUBS = buildStubs({ 'resume:probe': buildProbe(), 'find:': buildWalker({ findings: 1 }) })
  // ---- AC4: the complete walk's synthesis prompt carries the WALK TABLE block, and the return no gap.
  let r = await runReview(WD, WALK_OK_STUBS)
  if (checkNoThrow(r, 'walk: complete run')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(!!sp && sp.prompt.indexOf('<<<WALK TABLE\n## Walk table — run 1 of 2, sliced by scenario\nwalk-seed mode=reverted-escapes key-sha256=' + KEY +
      '\n\n| Item | Scenario | Actor | Needs | Witness | Route | Verdict |\n') !== -1,
      'walk: the synthesis prompt carries the WALK TABLE block, its heading, the walk-seed line and the table header')
    ck(r.result.exit === 'complete' && JSON.stringify(r.result.walkGaps) === '[]' && Array.isArray(r.result.walkTable) && r.result.walkTable.length === 20,
      'walk: a complete walk returns walkGaps [] beside its 20 walkTable rows: ' + JSON.stringify(r.result.walkGaps))
  }
  // The planted empty cell: walker slot 3's first witness is whitespace.
  r = await runReview(WD, buildStubs({ 'resume:probe': buildProbe(), 'find:': buildWalker({ findings: 1, blank: 'walk-3' }) }))
  if (checkNoThrow(r, 'walk: planted empty cell')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(r.result.walkGaps.length === 1 && !!sp && sp.prompt.indexOf(r.result.walkGaps[0]) !== -1 && /`## Verdict:` token is BLOCKED/.test(sp.prompt),
      'walk: the planted empty cell is one gap, named in the synthesis prompt, which says the verdict is BLOCKED: ' + JSON.stringify(r.result.walkGaps))
  }
  // The red case: a walk raising no finding still dispatches one cell-only batch and still synthesizes.
  r = await runReview(WD, buildStubs({ 'resume:probe': buildProbe(), 'find:': buildWalker({ findings: 0 }) }))
  if (checkNoThrow(r, 'walk: no finding')) {
    const vs = r.trace.filter((t) => t.label.indexOf('verify:') === 0).map((t) => t.label)
    ck(JSON.stringify(vs) === '["verify:cells"]' && r.trace.some((t) => t.label === 'synth') && r.result.exit === 'complete',
      'walk: a walk raising no finding dispatches one verify:cells batch and the synthesis: ' + JSON.stringify(vs))
    // ---- TOOL-dFairHearing-20 AC2: the complete no-finding walk keeps its integer counts and CONVERGED.
    const csp = r.trace.find((t) => t.label === 'synth')
    ck(JSON.stringify(r.result.walkGaps) === '[]' && r.result.blockers === 0 && r.result.highs === 0 && r.result.roundCount === 0 &&
      r.result.roundState === 'CONVERGED' && !!csp && !/token is BLOCKED/.test(csp.prompt),
      'walk red: a complete no-finding walk returns blockers 0, highs 0, count 0 and CONVERGED, its prompt no BLOCKED sentence: ' + r.result.roundState)
    // TOOL-dFairHearing-27 AC20: the absence half reads the gap sentence, never the static verdict list's `BLOCKED`.
    ck(!!csp && !csp.prompt.split('\n').some((l) => /the walk table has [0-9]+ gap/.test(l)),
      'FH27 AC20 walk red: the complete walk\'s synthesis prompt carries no `the walk table has <n> gap` line')
  }
  // ---- TOOL-dFairHearing-20 AC1/AC3: the same no-finding walk with one planted empty cell. Against the harness at
  // TOOL-dFairHearing-18's commit it returns roundState CONVERGED and blockers 0 beside the gap, and both arms red.
  r = await runReview(WD, buildStubs({ 'resume:probe': buildProbe(), 'find:': buildWalker({ findings: 0, blank: 'walk-3' }) }))
  if (checkNoThrow(r, 'walk red: planted empty cell, no finding')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    ck(r.result.walkGaps.length === 1 && r.result.blockers === null && r.result.highs === null && r.result.roundCount === null &&
      r.result.roundState === null && r.result.note.indexOf('BLOCKED: the walk table has 1 gap(s)') === 0,
      'walk red: a gapped no-finding walk nulls blockers, highs, roundCount and roundState, its note opening BLOCKED: ' + r.result.roundState + ' ' + r.result.blockers)
    ck(!!sp && /<<<ROUND\nreview-round [^\n]* count=- state=-\nROUND>>>/.test(sp.prompt),
      'walk red: the gapped walk\'s round line reads count=- and state=-')
    ck(!!sp && sp.prompt.split('\n').filter((l) => /the walk table has [0-9]+ gap/.test(l)).length === 1,
      'FH27 AC20 walk red: the gapped walk\'s synthesis prompt carries one `the walk table has <n> gap` line')
  }
  ck(src.split('\n').filter((l) => /\bconst walkRed\b/.test(l)).length === 1, 'walk red: the harness defines walkRed once')
  // ---- AC5: 40 clean cells of 42 over two skeptic batches, walkers 1 and 2 raising one finding each.
  const IT6 = Array.from({ length: 6 }, (_, i) => ({ tag: 'it' + i, step: 's' }))
  const SC7 = Array.from({ length: 7 }, (_, j) => ({ id: 'S' + (j + 1), name: 'n', walks: 'w' }))
  const WD40 = Object.assign({}, WD, { walk: { items: IT6, scenarios: SC7, run: 1, keySha: KEY } })
  const CELL_LINE = /^- it\d · S\d — /
  const judgeCells = (label, prompt) => {
    const v = buildVerdicts('confirmed')(label, prompt)
    v.cells = prompt.split('\n').filter((l) => CELL_LINE.test(l)).map((l, i) => ({ cell: l.slice(2).split(' — ')[0],
      verdict: label === 'verify:batch-1' && i === 0 ? 'refuted' : 'holds', reason: 'it fails there', file: 'd.md', where: '[act]', severity: 'high' }))
    return v
  }
  const stubs40 = buildStubs({ 'resume:probe': buildProbe(), 'find:': buildWalker({ findings: (lens) => (lens === 'walk-1' || lens === 'walk-2' ? 1 : 0) }), 'verify:': judgeCells })
  const a1 = await runReview(WD40, stubs40)
  const a2 = await runReview(WD40, stubs40)
  if (checkNoThrow(a1, 'walk: clean-cell sample') && checkNoThrow(a2, 'walk: clean-cell sample, second render')) {
    const cellsOf = (run) => run.trace.filter((t) => t.label.indexOf('verify:') === 0).map((t) => t.prompt.split('\n').filter((l) => CELL_LINE.test(l)).map((l) => l.slice(2).split(' — ')[0]))
    const s1 = cellsOf(a1)
    ck(s1.length === 2 && s1.every((g) => g.length === 8) && s1[0].every((c) => s1[1].indexOf(c) === -1) && JSON.stringify(s1) === JSON.stringify(cellsOf(a2)),
      'walk: each of two skeptic prompts carries eight clean cells, the sets disjoint and identical on a second render: ' + s1.map((g) => g.length).join(' '))
    const holds = new Set(a1.result.walkTable.filter((x) => x.verdict === 'holds').map((x) => x.item + ' · ' + x.scenario))
    ck(holds.size === 40 && s1.flat().every((c) => holds.has(c)), 'walk: every sampled cell is one of the 40 whose verdict is holds: ' + holds.size)
    ck(a1.result.cellsSampled === 16 && a1.result.cellsRefuted === 1 && a1.result.ledger.some((e) => e.lens === 'cell-sample' && e.verdict === 'unverified'),
      'walk: one refuted cell returns cellsSampled 16, cellsRefuted 1 and an unverified cell-sample ledger entry: ' + a1.result.cellsSampled + ' ' + a1.result.cellsRefuted)
  }
  // ---- AC6: each walker prompt names its own scenario and no other slot's, carries the rules and, seeded, the key's SHA-256.
  r = await runReview(WD, WALK_OK_STUBS)
  const finds = r.trace.filter((t) => t.label.indexOf('find:') === 0)
  ck(finds.length === 5 && finds.every((t, w) => t.prompt.indexOf('WALK RULES:\n- ') !== -1 && t.prompt.indexOf(KEY) !== -1 &&
    SCEN.every((s, j) => (t.prompt.indexOf('  - ' + s.id + ' — ') !== -1) === (j === w))),
    'walk: each walker prompt names its own scenario alone, carries WALK_RULES and the key\'s SHA-256: ' + finds.length + ' walker(s)')
  r = await runReview(Object.assign({}, WD, { walk: { items: ITEMS, scenarios: SCEN, run: 1, seed: 'none' } }), WALK_OK_STUBS)
  const unseeded = r.trace.filter((t) => t.label.indexOf('find:') === 0)
  ck(unseeded.length === 5 && unseeded.every((t) => t.prompt.indexOf('SHA-256') === -1 && !/[0-9a-f]{64}/.test(t.prompt)),
    'walk: under seed none no walker prompt carries a SHA-256: ' + unseeded.length + ' walker(s)')
  ck(src.split('\n').filter((l) => /\bconst WALK_RULES\b/.test(l)).length === 1, 'walk: the harness defines WALK_RULES once')
  // ---- TOOL-dFairHearing-43 AC7: the spaced-repo quoting over every preset the harness ships, here beside WD and its
  // walker stubs: each run holds a `git -C` and every one is quoted. The diff kind is the `FH40 AC19` arm. The round-2
  // fold's subject is the THREE fixture's first, `prevBlob` unequal to its blob. RED on the quotes stripped from the
  // probe's hash-object command alone, then from the acquire sentence's alone.
  const SPACED = 'git -C "C:/x y/z"'
  const FOLD = { round: 2, subjects: [{ path: 'memory/builds/dX/spec/one.md', blob: 'd'.repeat(40), id: 'TOOL-x-1', rev: 1, prevBlob: 'a'.repeat(40) }], priorFindings: [{ ref: 'one.md:section 2', claim: 'PRIOR' }] }
  for (const [preset, args, stubs] of [['unit-spec at round 1', SPEC, ALL_OK], ['the unit-spec round-2 fold', Object.assign({}, SPEC, FOLD), ALL_OK],
    ['design-audit', Object.assign({}, DESIGN, { preset: 'design-audit' }), ALL_OK], ['whole-design', WD, WALK_OK_STUBS]]) {
    const rq = await runReview(Object.assign({}, args, { repo: 'C:/x y/z' }), stubs)
    const named = rq.trace.map((t) => t.prompt).join('\n').match(/git -C (?:"[^"]*"|[^\s`]+)/g) || []
    ck(!rq.threw && named.length > 0 && named.every((g) => g === SPACED),
      'FH43 AC7 ' + preset + ' reaches every prompt as ' + SPACED + ': ' + named.length + ' git -C command(s), ' + JSON.stringify(named.filter((g) => g !== SPACED).slice(0, 3)) + (rq.threw ? ' threw ' + rq.threw : ''))
    if (args !== SPEC) continue
    const holds = (t, c) => t.prompt.indexOf(SPACED + ' ' + c) !== -1
    const probeSpawn = rq.trace.find((t) => t.label === 'resume:probe') || { prompt: '' }
    const others = rq.trace.filter((t) => t !== probeSpawn)
    ck(holds(probeSpawn, 'hash-object <path>') && others.some((t) => holds(t, 'hash-object <path>')) && others.some((t) => holds(t, 'diff <blob> -- <path>')),
      'FH43 AC7 unit-spec at round 1 carries the probe\'s hash-object command and the acquire sentence\'s hash-object and diff commands')
  }
}

// ==== TOOL-dFairHearing-2 — the design-audit preset: its lenses, its review key and its announcements ====
// Every arm is RED against the base harness, which reads no `preset`: a design-audit run fans over
// SPEC_LENSES, derives the default run's key, logs nothing and carries no `preset` on any return. The
// briefs are read off the live harness's own literals, and each check carries its count of five.
async function runPresetArms() {
  const readLiteral = (name) => {
    const ls = src.split('\n')
    const at = ls.findIndex((l) => l.startsWith('const ' + name + ' = ['))
    const end = ls.findIndex((l, i) => i > at && l === ']')
    // TOOL-dFairHearing-3 - each slot is a `deriveSlotLens(<literal>, L)` call; read here as L itself.
    return at === -1 || end === -1 ? [] : new Function('deriveSlotLens', 'return [' + ls.slice(at + 1, end).join('\n') + ']')((lit, L) => L)
  }
  const DL = readLiteral('DESIGN_LENSES')
  const SL = readLiteral('SPEC_LENSES')
  const scanFinds = (run) => run.trace.filter((t) => t.label.indexOf('find:') === 0)
  const checkBriefs = (finds, lenses) => finds.length === 5 && lenses.length === 5 &&
    finds.every((t, i) => t.label === 'find:' + lenses[i].key && t.prompt.indexOf('LENS: ' + lenses[i].brief + '\n') !== -1)
  const rd = await runReview(Object.assign({}, DESIGN, { preset: 'design-audit' }), ALL_OK)
  const ru = await runReview(DESIGN, ALL_OK)
  const rx = await runReview(Object.assign({}, DESIGN, { preset: 'unit-spec' }), ALL_OK)
  if (checkNoThrow(rd, 'preset design-audit run') && checkNoThrow(ru, 'preset default run') && checkNoThrow(rx, 'preset explicit unit-spec run')) {
    // ---- AC3: the design-audit run's five finders carry the design briefs; the default run's, the spec briefs.
    ck(DL.map((L) => L.key).join(' ') === 'coherence grounding reuse failure-envelope alternatives-and-cost' && checkBriefs(scanFinds(rd), DL),
      'preset: a design-audit run fans over DESIGN_LENSES, each finder carrying its design brief: ' + rd.scanSpawned('find:').join(' '))
    ck(checkBriefs(scanFinds(ru), SL) && checkBriefs(scanFinds(rx), SL),
      'preset: a run without it, or naming unit-spec, fans over SPEC_LENSES with the spec briefs: ' + ru.scanSpawned('find:').join(' '))
    ck(DL.length === 5 && DL.every((L) => !/\bsections? \d/.test(L.brief)),
      'preset: no design brief names a unit spec\'s numbered section')
    // ---- TOOL-dFairHearing-2 AC4: the preset joins the key off its default only.
    ck(rd.result.key !== ru.result.key, 'preset: a design-audit run and a default run over the same subjects derive different keys')
    ck(ru.result.key === rx.result.key && ru.result.key.indexOf('spec-audit-r1-') === 0,
      'preset: unit-spec, absent or named, derives one key, so a caller without the argument keeps its key: ' + ru.result.key)
    // ---- AC6: the preset on the complete return and on the no-finding return, in RUN INTEGRITY and in the log.
    const re = await runReview(Object.assign({}, DESIGN, { preset: 'design-audit' }), buildStubs({ 'find:': buildEmptyLens }))
    ck(rd.result.preset === 'design-audit' && !re.threw && re.result.note === 'clean: 0 findings' && re.result.preset === 'design-audit',
      'preset: the complete and the no-finding return of a design-audit run carry preset design-audit')
    const sp = rd.trace.find((t) => t.label === 'synth')
    const ri = sp ? sp.prompt.slice(sp.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(/\npreset: design-audit - /.test(ri) && rd.logs.some((l) => l.indexOf('preset design-audit') === 0) && !ru.logs.some((l) => l.indexOf('preset ') === 0),
      'preset: RUN INTEGRITY names design-audit, and only a run off the default logs its preset')
    const rdf = await runReview(DIFF, ALL_OK)
    ck(ru.result.preset === 'unit-spec' && !!rdf.result && !Object.prototype.hasOwnProperty.call(rdf.result, 'preset'),
      'preset: a default spec audit returns preset unit-spec, and a diff review carries no preset field')
  }
}

// ==== TOOL-dFairHearing-3 — the opt-in swap over scratch renders, and review_pin.py (AC2-AC5, AC7, AC8) ====
// The shipped catalogue ships no opt-in, so each swap arm renders the TEMPLATE over a scratch copy of
// `lenses.toml` with the named opt-in rows flipped to `optin = true`, fills `{{FANOUT_CAP}}` with the
// live harness's cap, and runs that render whole. Every arm is RED against the base harness, which
// reads no `optIn` and renders no `deriveSlotLens`, and against a tree with no `review_pin.py`. The
// python is the one this shell resolved, so an absent one reds these arms by name.
async function runOptInArms() {
  const path = require('path')
  const { spawnSync } = require('child_process')
  const kit = path.dirname(FILE)
  const py = process.argv[5] || ''
  const tpl = fs.readFileSync(path.join(kit, 'tier2-review.template.js'), 'utf8')
  const cap = (/async function boundedParallel\(thunks, cap = (\d+)\)/.exec(src) || [])[1]
  const scratch = fs.mkdtempSync(path.join(require('os').tmpdir(), 'optin-'))
  // A scratch render with `keys` shipped as opt-ins, or the refusal that stopped it, as `why`.
  const renderOptIns = (keys) => {
    let text = fs.readFileSync(path.join(kit, 'lenses.toml'), 'utf8')
    for (const k of keys) {
      const re = new RegExp('(key = "' + k + '"\\r?\\n(?:[^\\n]*\\n){2}default_in = \\[\\]\\r?\\n)optin = false')
      if (!re.test(text)) return { why: 'no opt-in row `' + k + '` to flip in lenses.toml' }
      text = text.replace(re, '$1optin = true')
    }
    if (!py) return { why: 'no python was resolved' }
    if (!cap) return { why: 'no `cap = <n>` in the live harness to fill {{FANOUT_CAP}} with' }
    const cat = path.join(scratch, keys.join('_') + '.toml')
    fs.writeFileSync(cat, text)
    const r = spawnSync(py, ['-B', path.join(kit, 'render_lenses.py'), cat], { input: tpl, encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }) })
    if (r.status !== 0) return { why: 'the render exited ' + r.status + ': ' + (r.stderr || String(r.error)) }
    return { src: r.stdout.split('{{FANOUT_CAP}}').join(cap).replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =') }
  }
  const readSlots = (text, name) => {
    const ls = text.split('\n')
    const at = ls.findIndex((l) => l.startsWith('const ' + name + ' = ['))
    const end = ls.findIndex((l, i) => i > at && l === ']')
    return at === -1 || end === -1 ? [] : new Function('deriveSlotLens', 'return [' + ls.slice(at + 1, end).join('\n') + ']')((lit, L) => L)
  }
  const scanFinds = (run) => run.trace.filter((t) => t.label.indexOf('find:') === 0)
  const SWAP = Object.assign({}, SPEC, { optIn: { topology: 'blast-radius' } })
  const top = renderOptIns(['topology'])
  ck(!!top.src, 'optIn: the scratch render with topology shipped as an opt-in exists' + (top.why ? ' (' + top.why + ')' : ''))
  if (top.src) {
    // ---- AC2: topology runs in blast-radius's slot, the other four in place, five finders in order.
    const SL = readSlots(src, 'SPEC_LENSES')
    const OL = readSlots(top.src, 'OPTIN_LENSES')
    const want = SL.length === 5 && OL.length === 1 ? [SL[0], SL[1], SL[2], OL[0], SL[4]] : []
    const r2 = await runReview(SWAP, ALL_OK, top.src)
    const f2 = scanFinds(r2)
    ck(!r2.threw && want.length === 5 && f2.length === 5 && f2.every((t, i) => t.label === 'find:' + want[i].key && t.prompt.indexOf('LENS: ' + want[i].brief + '\n') !== -1) &&
      want.map((L) => L.key).join(' ') === 'coherence grounding reuse topology failure-envelope',
      'optIn: AC2 a unit-spec swap runs topology in the blast-radius slot, five finders in order: ' + (r2.threw || f2.map((t) => t.label).join(' ')))
    const sp2 = r2.trace.find((t) => t.label === 'synth')
    const ri2 = sp2 ? sp2.prompt.slice(sp2.prompt.indexOf('RUN INTEGRITY')) : ''
    ck(!!r2.result && JSON.stringify(r2.result.optIn) === '{"topology":"blast-radius"}' &&
      r2.logs.some((l) => l.indexOf('optIn: topology runs in the slot of blast-radius') === 0) &&
      /\noptIn: topology ran in the slot of blast-radius - /.test(ri2),
      'optIn: AC2 the return carries the swap, and the log and RUN INTEGRITY name the dropped default')
    // ---- AC3: the four named refusals, each before the stub agent is called.
    const both = renderOptIns(['topology', 'adopter-migration'])
    for (const [render, v, word] of [[top, { coherence: 'reuse' }, 'already a lens'], [top, { portability: 'reuse' }, 'no opt-in of `unit-spec`'],
      [top, { topology: 'nope' }, 'no default `nope`'], [both, { topology: 'reuse', 'adopter-migration': 'reuse' }, '`reuse` replaced twice']]) {
      const r = render.src ? await runReview(Object.assign({}, SPEC, { optIn: v }), ALL_OK, render.src) : { threw: render.why, trace: [] }
      ck(typeof r.threw === 'string' && r.threw.indexOf('tier2-review: `optIn`') === 0 && r.threw.indexOf(word) !== -1 && r.trace.length === 0,
        'optIn: AC3 ' + JSON.stringify(v) + ' refuses before any agent, naming "' + word + '": ' + r.threw)
    }
    // ---- TOOL-dFairHearing-3 AC5: the key moves with a swap, and without one equals the live harness's key.
    const k0 = await runReview(SPEC, ALL_OK)
    const k1 = await runReview(SPEC, ALL_OK, top.src)
    ck(!!k0.result && !!k1.result && !!r2.result && k1.result.key === k0.result.key && r2.result.key !== k1.result.key,
      'optIn: AC5 a swap moves the review key, and a run without one keeps the key: ' + (k1.result && k1.result.key) + ' / ' + (r2.result && r2.result.key))
    // ---- TOOL-dFairHearing-9 AC5: a note keyed to the default the swap displaced proceeds and is reported
    // ---- unread; the swapped-in lens's note reaches its prompt. RED against the harness TOOL-dFairHearing-3
    // ---- left, whose check throws on the replaced key.
    const r9 = await runReview(Object.assign({}, SWAP, { lensNotes: { 'blast-radius': 'FH9-B', topology: 'FH9-T' } }), ALL_OK, top.src)
    const sp9 = r9.trace.find((t) => t.label === 'synth')
    const ri9 = sp9 ? sp9.prompt.slice(sp9.prompt.indexOf('RUN INTEGRITY')) : ''
    const carry9 = (mark) => r9.trace.filter((t) => t.prompt.indexOf(mark) !== -1).map((t) => t.label).join(' ')
    ck(!r9.threw && scanFinds(r9).length === 5 && carry9('FH9-T') === 'find:topology' && carry9('FH9-B') === '' &&
      ri9.indexOf('lens notes supplied for: topology; lens notes for skipped lenses, unread: blast-radius.') !== -1 &&
      r9.logs.some((l) => l.indexOf('WARNING:') === 0 && l.indexOf('unread: blast-radius') !== -1),
      'lens notes: AC5 a note for the replaced default is unread in the log and RUN INTEGRITY, the opt-in\'s reaches find:topology: ' + (r9.threw || carry9('FH9-T')))
  }
  // ---- AC4: a light diff run takes a swap into a light slot, and skips by the default keys.
  const port = renderOptIns(['portability'])
  const r4 = port.src ? await runReview(Object.assign({}, DIFF, { intensity: 'light', optIn: { portability: 'seams' } }), ALL_OK, port.src) : { threw: port.why, trace: [] }
  ck(!r4.threw && scanFinds(r4).map((t) => t.label).join(' ') === 'find:correctness find:portability find:verification' &&
    !!r4.result && r4.result.skippedLenses.join(' ') === 'security intent',
    'optIn: AC4 a light swap runs portability in the seams slot and skips security and intent: ' + (r4.threw || scanFinds(r4).map((t) => t.label).join(' ')))
  // ---- AC7/AC8: review_pin.py prints one call's arguments, and refuses a malformed one by name.
  const pin = path.join(kit, 'review_pin.py')
  const runPin = (argv, at) => {
    if (!py) return { status: -1, stdout: '', stderr: 'no python was resolved' }
    const r = spawnSync(py, ['-B', at || pin].concat(argv), { encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }) })
    return { status: r.status, stdout: r.stdout || '', stderr: (r.stderr || '') + (r.error ? String(r.error) : '') }
  }
  // AC7's no-flag design preset is the module's DESIGN_RECORD_PRESET, read off the module, never typed here.
  const dflt = (/^DESIGN_RECORD_PRESET = "([a-z-]+)"/m.exec(fs.existsSync(pin) ? fs.readFileSync(pin, 'utf8') : '') || [])[1]
  const S1 = 'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md'
  const D = ['--subject', 'memory/builds/dX/build/a.md', '--subject', 'memory/builds/dX/build/b.md']
  for (const [what, argv, want] of [
    ['one spec subject', ['--subject', S1], '{"preset": "unit-spec"}'],
    ['two design subjects', D, '{"preset": "' + dflt + '"}'],
    ['two design subjects under the design-audit flag', D.concat(['--design-record-preset', 'design-audit']), '{"preset": "design-audit"}'],
    ['a mixed set under that flag', ['--subject', 'memory/builds/dX/build/a.md', '--subject', S1, '--design-record-preset', 'design-audit'], '{"preset": "unit-spec"}'],
    ['the spec subject with an opt-in', ['--subject', S1, '--opt-in', '{"unit-spec": {"topology": "blast-radius"}}'], '{"preset": "unit-spec", "optIn": {"topology": "blast-radius"}}'],
  ]) {
    const r = runPin(argv)
    ck(!!dflt && r.status === 0 && r.stdout === want + '\n', 'pin: AC7 ' + what + ' prints ' + want + ' (got ' + r.status + ': ' + (r.stdout || r.stderr).trim() + ')')
  }
  const lone = path.join(scratch, 'pin')
  fs.mkdirSync(lone)
  if (fs.existsSync(pin)) fs.copyFileSync(pin, path.join(lone, 'review_pin.py'))
  fs.writeFileSync(path.join(lone, 'tier2-review.js'), 'const NOT_THE_PREDICATE = 1\n')
  for (const [what, argv, at, word] of [['a harness with no SPEC_SUBJECT_PATH line', ['--subject', S1], path.join(lone, 'review_pin.py'), 'SPEC_SUBJECT_PATH'],
    ['--opt-in [1]', ['--subject', S1, '--opt-in', '[1]'], null, '--opt-in'], ['no --subject', [], null, '--subject']]) {
    const r = runPin(argv, at)
    ck(r.status === 2 && r.stdout === '' && r.stderr.indexOf(word) !== -1, 'pin: AC8 ' + what + ' exits 2 naming ' + word + ' (got ' + r.status + ': ' + r.stderr.trim().split('\n').pop() + ')')
  }
  fs.rmSync(scratch, { recursive: true, force: true })
}

// ==== TOOL-dFoldedAudit-5 — THE ADDRESS, each spec-kind BLOCKER or HIGH naming the specs its fix changes ====
// The failing case is staged by dropping the `isSpec` clause from the tally, which reds the diff-kind
// control, and by dropping the clause's body, which reds AC2: both observed at the close, not by the pass
// that wrote this. An arm reads the return, the prompt and the render; none proves a live synthesis obeys.
// TOOL-dFoldedAudit-15 S8: the address is owed under a declared `disposal` alone, so these arms declare one,
// and the last runs without it. Its failing case, observed at the close and not by the pass that wrote this:
// `addressOwed` reading `isSpec` nulls that arm's counts.
async function runAddressArms() {
  const SPEC_DECLARED = Object.assign({}, SPEC, { disposal: 'by-nature' })
  const buildSynthItem = (over) => (label, prompt) => {
    const it = Object.assign({ severity: 'HIGH', ids: [...prompt.split('UNVERIFIED findings')[0].matchAll(/id=(\d+) \[/g)].map((x) => parseInt(x[1], 10)) }, over)
    return { path: 'memory/reviews/r.md', summary: 's', items: [Object.assign(it, { grades: buildGrades(it.ids, it.severity) })] }
  }
  const scanSynth = (run) => run.trace.filter((t) => t.label.indexOf('synth') === 0)[0].prompt
  // ---- AC1: the item's address comes back beside the counts, and the prompt asks for the line.
  let r = await runReview(SPEC_DECLARED, buildStubs({ synth: buildSynthItem({ specs: ['TOOL-x-1'] }) }))
  if (checkNoThrow(r, 'address carried')) {
    const a = r.result.addresses
    ck(Array.isArray(a) && a.length === 1 && a[0].severity === 'HIGH' && a[0].ids.length === 5 && a[0].specs.join() === 'TOOL-x-1',
      'address: the return carries the item\'s ids, severity and specs: ' + JSON.stringify(a))
    ck(r.result.highs === 5, 'address: an addressed HIGH item counts its raw ids')
    ck(scanSynth(r).indexOf('**Specs:**') !== -1, 'address: the spec-kind synthesis prompt orders the **Specs:** line')
  }
  // ---- AC2: a HIGH with no well-formed address is a tally fault, in three spellings, and a minor owes none.
  for (const [name, over] of [['an empty list', { specs: [] }], ['no key', {}], ['a token that is no id', { specs: ['not an id'] }]]) {
    r = await runReview(SPEC_DECLARED, buildStubs({ synth: buildSynthItem(over) }))
    if (checkNoThrow(r, 'address ' + name))
      ck(r.result.blockers === null && r.result.highs === null && /^UNVERIFIED/.test(r.result.note) && r.result.addresses.length === 0,
        'address: ' + name + ' nulls both counts, and the note opens UNVERIFIED: ' + r.result.note)
  }
  r = await runReview(SPEC_DECLARED, buildStubs({ synth: buildSynthItem({ severity: 'MEDIUM' }) }))
  if (checkNoThrow(r, 'address minor'))
    ck(r.result.blockers === 0 && r.result.highs === 0 && r.result.addresses.length === 0, 'address: a MEDIUM with no specs returns integer counts')
  // ---- AC3: a diff review's HIGH owes none, and neither its prompt nor its return moves.
  r = await runReview(DIFF, buildStubs({ synth: buildSynthItem({}) }))
  if (checkNoThrow(r, 'address diff kind')) {
    ck(r.result.blockers === 0 && r.result.highs === 5, 'address: a diff review\'s HIGH with no specs counts')
    ck(scanSynth(r).indexOf('**Specs:**') === -1, 'address: the diff prompt carries no **Specs:** line')
    ck(!Object.prototype.hasOwnProperty.call(r.result, 'addresses'), 'address: a diff review\'s return has no `addresses` key')
  }
  ck(src.indexOf('**Specs:**') !== -1, 'address: the render moved with its template')
  // ---- FA15 AC10: an undeclared spec audit keeps today's synthesis: a HIGH with no address counts, and
  // ---- neither the prompt nor the schema asks for one.
  r = await runReview(SPEC, buildStubs({ synth: buildSynthItem({}) }))
  if (checkNoThrow(r, 'address undeclared')) {
    ck(r.result.blockers === 0 && r.result.highs === 5, 'address: an undeclared spec audit\'s HIGH with no specs counts')
    ck(scanSynth(r).indexOf('**Specs:**') === -1, 'address: the undeclared prompt carries no **Specs:** line')
    ck(Array.isArray(r.result.addresses) && r.result.addresses.length === 0, 'address: an undeclared return\'s `addresses` stays empty')
  }
}

// ==== TOOL-dFairHearing-6 — `grades`, one item per defect, each confirmed id counted at its own grade ====
// Skeptics confirm id 1 at blocker and id 2 at medium and refute ids 3 to 5; the synthesis stub hands back
// the items it is given. RED against the base harness, whose tally places each id at its item's severity
// and whose prompt still merges findings of one binding grade only: observed at the close, not by this pass.
async function runGradesArms() {
  const buildMixedVerdicts = (label, prompt) => {
    const m = /ids ([0-9, ]+)\)/.exec(prompt)
    const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
    return { path: '/v', verdicts: ids.map((id) => (id === 1 ? { id: id, verdict: 'confirmed', reason: 'r', severity: 'blocker' }
      : id === 2 ? { id: id, verdict: 'confirmed', reason: 'r', severity: 'medium' } : { id: id, verdict: 'refuted', reason: 'r' })) }
  }
  const runItems = (items) => runReview(DIFF, buildStubs({ 'verify:': buildMixedVerdicts, synth: { path: 'memory/reviews/r.md', summary: 's', items: items } }))
  const MIXED = { severity: 'BLOCKER', ids: [1, 2], grades: { 1: 'BLOCKER', 2: 'MEDIUM' } }
  const scanWarn = (run, text) => run.logs.filter((l) => l.indexOf('WARNING:') === 0 && l.indexOf(text) !== -1)
  // ---- AC1: one mixed item counts each id at its own grade; a repeated id still nulls both counts.
  let r = await runItems([MIXED])
  if (checkNoThrow(r, 'grades mixed item')) {
    ck(r.result.blockers === 1 && r.result.highs === 0 && Array.isArray(r.result.regraded) && r.result.regraded.length === 0 &&
      !r.logs.some((l) => l.indexOf('other than their binding one') !== -1),
      'grades: one item holding a blocker and a medium counts blockers 1, highs 0 and regrades none')
  }
  r = await runItems([MIXED, { severity: 'BLOCKER', ids: [1], grades: { 1: 'BLOCKER' } }])
  if (checkNoThrow(r, 'grades repeated id'))
    ck(r.result.blockers === null && r.result.highs === null, 'grades: an id in two items still nulls both counts')
  // ---- AC2: a per-id grade off the binding one is regraded by id.
  r = await runItems([{ severity: 'BLOCKER', ids: [1, 2], grades: { 1: 'BLOCKER', 2: 'HIGH' } }])
  if (checkNoThrow(r, 'grades regraded'))
    ck(r.result.highs === 1 && Array.isArray(r.result.regraded) && r.result.regraded.join(' ') === '2',
      'grades: id 2 graded HIGH reads highs 1 and regraded [2]')
  // ---- AC3: an absent and an illegal grade each fall back to the item's severity, named.
  for (const [name, grades] of [['an absent grade', { 1: 'BLOCKER' }], ['an illegal grade', { 1: 'BLOCKER', 2: 'severe' }]]) {
    r = await runItems([{ severity: 'BLOCKER', ids: [1, 2], grades: grades }])
    if (checkNoThrow(r, 'grades ' + name))
      ck(r.result.blockers === 2 && scanWarn(r, 'no legal grade').some((l) => /ids 2$/.test(l)),
        'grades: ' + name + ' places id 2 at the item\'s BLOCKER and names it')
  }
  // ---- TOOL-dFairHearing-23 AC21: an item with no `grades`, and one with `grades: null`, place each id at the item's
  // severity, one WARNING naming the item. RED against the parent, whose `it.grades[String(id)]` throws a TypeError.
  for (const [name, item] of [['no grades', { severity: 'BLOCKER', ids: [1, 2] }], ['grades null', { severity: 'BLOCKER', ids: [1, 2], grades: null }]]) {
    r = await runItems([item])
    if (checkNoThrow(r, 'FH23 AC21 ' + name)) {
      const w = scanWarn(r, 'carries no grades object')
      ck(r.result.blockers === 2 && w.length === 1 && w[0].indexOf('holding ids 1, 2 ') !== -1,
        'FH23 AC21 an item with ' + name + ' places ids 1 and 2 at its BLOCKER, one WARNING naming it: ' + w.join(' / '))
    }
  }
  // ---- AC4: an item whose severity is not its highest grade is named, and the counts stay per id.
  r = await runItems([Object.assign({}, MIXED, { severity: 'MEDIUM' })])
  if (checkNoThrow(r, 'grades misranked'))
    ck(r.result.blockers === 1 && scanWarn(r, 'other than the highest grade').some((l) => /items holding ids 1$/.test(l)),
      'grades: a MEDIUM item holding a BLOCKER grade counts blockers 1 and is named')
  // ---- AC5: the old merge rule is gone from both files; the prompt and the schema carry the new one.
  const tpl = fs.readFileSync(require('path').join(require('path').dirname(FILE), 'tier2-review.template.js'), 'utf8')
  ck(src.indexOf('merge findings of one binding grade only') === -1 && tpl.indexOf('merge findings of one binding grade only') === -1,
    'grades: neither the template nor the render says merge findings of one binding grade only')
  r = await runItems([MIXED])
  if (checkNoThrow(r, 'grades prompt')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const req = sp && sp.schema && sp.schema.properties.items.items.required
    ck(!!sp && sp.prompt.indexOf('one item per defect') !== -1 && sp.prompt.indexOf('`grades`') !== -1,
      'grades: the synthesis prompt asks for one item per defect and its `grades`')
    ck(Array.isArray(req) && req.indexOf('grades') !== -1, 'grades: the synthesis schema requires `grades` on each item')
  }
}

// ==== TOOL-dFairHearing-7 — twins: refuted claims and same-address pairs handed to the synthesis ====
// The `security` lens, first in the diff literal, raises ids 1 and 2 at a.js lines 10 and 12, so both meet
// one skeptic in verify:batch-1; `seams` raises id 5 at c.js; every other finding cites its lens's own file
// at lines 1 and 50, which pairs with nothing. Skeptics confirm every id `over` does not name. RED against
// the base harness, which reads no `addressTwins`: the shown run hands neither block, its schema has no
// `twinFlags`, and its return carries neither `twinPairs` nor `twinFlags`. Observed at the close.
async function runTwinArms() {
  const buildTwinLens = (label) => {
    const lens = label.slice('find:'.length)
    const mk = (file, line) => ({ file: file, line: line, severity: 'high', claim: lens + ' claim at ' + file + ':' + line, impact: 'i', fix: 'f' })
    return { lens: lens, path: '/p', findings: lens === 'security' ? [mk('a.js', 10), mk('a.js', 12)]
      : lens === 'seams' ? [mk('c.js', 1), mk('seams.js', 50)] : [mk(lens + '.js', 1), mk(lens + '.js', 50)] }
  }
  const buildTwinVerdicts = (over) => (label, prompt) => {
    const m = /ids ([0-9, ]+)\)/.exec(prompt)
    const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
    return { path: '/v', verdicts: ids.map((id) => Object.assign({ id: id, verdict: 'confirmed', reason: 'r' }, over[id] || {})) }
  }
  const runTwins = (twins, over, flags) => runReview(Object.assign({}, DIFF, twins === undefined ? {} : { addressTwins: twins }),
    buildStubs({ 'find:': buildTwinLens, 'verify:': buildTwinVerdicts(over),
      synth: (label, prompt) => Object.assign(buildSynth(null)(label, prompt), flags ? { twinFlags: flags } : {}) }))
  const scanSynthCall = (run) => run.trace.find((t) => t.label === 'synth') || { prompt: '', schema: { required: [], properties: {} } }
  const FLAGS = [{ refuted: 2, confirmed: 1 }, { refuted: 2, confirmed: 1 }, { refuted: 1, confirmed: 2 }, { refuted: 9, confirmed: 1 }]
  const BY_DESIGN = { 2: { verdict: 'refuted', reason: 'by design' } }
  // ---- AC3: the shown prompt carries both blocks and the schema requires twinFlags; the hidden one carries neither.
  const rs = await runTwins('shown', BY_DESIGN, FLAGS)
  const rh = await runTwins('hidden', BY_DESIGN, FLAGS)
  if (checkNoThrow(rs, 'twins shown') && checkNoThrow(rh, 'twins hidden')) {
    const ss = scanSynthCall(rs)
    const sh = scanSynthCall(rh)
    const refBlock = ss.prompt.slice(ss.prompt.indexOf('REFUTED findings'), ss.prompt.indexOf('SAME-ADDRESS PAIRS'))
    ck(refBlock.indexOf('- id=2 [high] lens=security a.js:12 — security claim at a.js:12 | refuted because: by design') !== -1 &&
      ss.prompt.indexOf('- confirmed id=1 and refuted id=2, both at a.js 10') !== -1 &&
      ss.prompt.indexOf('refuted findings shown: 1; same-address pairs shown: 1.') !== -1 &&
      ss.schema.required.indexOf('twinFlags') !== -1 && !!ss.schema.properties.twinFlags,
      'twins: a shown run hands id 2\'s claim and reason, the pair 1/2, both counts in RUN INTEGRITY, and a schema requiring twinFlags')
    ck(sh.prompt.length > 0 && sh.prompt.indexOf('REFUTED findings') === -1 && sh.prompt.indexOf('SAME-ADDRESS PAIRS') === -1 &&
      sh.prompt.indexOf('twinFlags') === -1 && sh.schema.required.indexOf('twinFlags') === -1 && !('twinFlags' in sh.schema.properties) &&
      !('twinFlags' in rh.result) && !('twinPairs' in rh.result),
      'twins: the hidden run hands neither block, a schema without twinFlags, and returns neither field')
    // ---- AC4: one flag kept, its repeat dropped, the two naming a wrong verdict discarded and named.
    ck(JSON.stringify(rs.result.twinFlags) === JSON.stringify([{ refuted: 2, confirmed: 1, sameAddress: true }]) && rs.result.twinPairs === 1 &&
      rs.logs.some((l) => l.indexOf('WARNING: 2 twin flag(s)') === 0 && l.indexOf('discarded: 1/2, 9/1') !== -1),
      'twins: of four flags 2/1 is kept at sameAddress true, its repeat dropped, and 1/2 and 9/1 named as discarded: ' + JSON.stringify(rs.result.twinFlags))
    // ---- AC5: no flag moves a verdict, a grade, an item or a count.
    const FIELDS = ['confirmed', 'refuted', 'merged', 'precision', 'blockers', 'highs', 'confirmedFindings', 'ledger']
    ck(rs.result.refuted === 1 && FIELDS.every((k) => JSON.stringify(rs.result[k]) === JSON.stringify(rh.result[k])),
      'twins: the hidden and shown runs agree on ' + FIELDS.join(', '))
  }
  const r5 = await runTwins('shown', Object.assign({ 5: { verdict: 'refuted', reason: 'r' } }, BY_DESIGN), [{ refuted: 5, confirmed: 1 }])
  if (checkNoThrow(r5, 'twins off-address'))
    ck(JSON.stringify(r5.result.twinFlags) === JSON.stringify([{ refuted: 5, confirmed: 1, sameAddress: false }]) && r5.result.twinPairs === 1,
      'twins: a refuted id 5 at c.js flagged against id 1 is kept at sameAddress false: ' + JSON.stringify(r5.result.twinFlags))
  // ---- AC6: a merged duplicate is no twin of its own original.
  const rd = await runTwins('shown', { 2: { verdict: 'refuted', reason: 'duplicate of id=1' } }, [])
  if (checkNoThrow(rd, 'twins merged'))
    ck(rd.result.merged === 1 && rd.result.twinPairs === 0 &&
      scanSynthCall(rd).prompt.indexOf('SAME-ADDRESS PAIRS (a confirmed and a refuted finding citing one address):\n  (none)') !== -1,
      'twins: id 2 refuted as a duplicate of id 1 hands no pair, and the block reads (none)')
}

// ==== TOOL-dFairHearing-11 — every spawn typed from a declared stage (AC1-AC4) ======================
// RED against the parent render: its probe passes no stage options, its synthesis and a `none` run's
// judges carry no agentType, `roles.probe` is an unknown key, and the code-reading arm names the probe's
// agent( call. WHAT IT DOES NOT CHECK: that the platform spawns a type the options name; and the code
// arm reads the template's agent( calls only, an `agent` reached under another name being invisible to it.
const STAGE_OPTS = ['probeOpts', 'findOpts', 'verifyOpts', 'synthOpts']
// The code with every string, template text, comment and regex literal blanked, lengths and newlines
// kept, so a paren, a comma or an `agent(` inside one is never read; a `${...}` body stays code.
function blankStrings(s) {
  const out = s.split('')
  const blank = (a, b) => { for (let k = a; k < b && k < s.length; k++) if (out[k] !== '\n') out[k] = ' ' }
  const tpl = [] // the brace depth each open template literal's `${` returns to
  let depth = 0
  let lastCh = ''
  let lastWord = ''
  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    if (tpl.length && depth === tpl[tpl.length - 1]) { // template text, up to its close or a `${`
      const st = i
      while (i < s.length && s[i] !== '`' && !(s[i] === '$' && s[i + 1] === '{')) i += s[i] === '\\' ? 2 : 1
      blank(st, i)
      if (s[i] === '`') { out[i] = ' '; tpl.pop(); lastCh = ')'; lastWord = '' } else { i++; depth++; lastCh = '{'; lastWord = '' }
      continue
    }
    if (c === '/' && s[i + 1] === '/') { const e = s.indexOf('\n', i); const end = e === -1 ? s.length : e; blank(i, end); i = end - 1; continue }
    if (c === '/' && s[i + 1] === '*') { const e = s.indexOf('*/', i + 2); const end = e === -1 ? s.length : e + 2; blank(i, end); i = end - 1; continue }
    if (c === '\'' || c === '"' || (c === '/' && (lastCh === '' || '(,=:[!&|?{};+-*%<>~^'.indexOf(lastCh) !== -1 || lastWord === 'return'))) {
      let j = i + 1
      let cls = false
      while (j < s.length && s[j] !== '\n' && (cls || s[j] !== c)) {
        if (s[j] === '\\') j++
        else if (c === '/' && s[j] === '[') cls = true
        else if (c === '/' && s[j] === ']') cls = false
        j++
      }
      blank(i, j + 1); i = j; lastCh = ')'; lastWord = ''; continue
    }
    if (c === '`') { out[i] = ' '; tpl.push(depth); continue }
    if (c === '{') depth++
    else if (c === '}') depth--
    if (/\s/.test(c)) continue
    lastWord = /[\w$]/.test(c) ? (/[\w$]/.test(s[i - 1] || '') ? lastWord + c : c) : ''
    lastCh = c
  }
  return out.join('')
}
// Every agent( call outside a string or comment: its line, and its second top-level argument as code and as written.
function scanAgentCalls(text) {
  const code = blankStrings(text)
  const calls = []
  const re = /(^|[^.\w$])agent\s*\(/g
  let m
  while ((m = re.exec(code))) {
    const open = m.index + m[0].length - 1
    let d = 0
    let k = open
    const commas = []
    for (; k < code.length; k++) {
      const ch = code[k]
      if (ch === '(' || ch === '[' || ch === '{') d++
      else if (ch === ')' || ch === ']' || ch === '}') { if (--d === 0) break }
      else if (ch === ',' && d === 1) commas.push(k)
    }
    const end = commas.length > 1 ? commas[1] : k
    calls.push({ line: code.slice(0, open).split('\n').length, opts: commas.length ? code.slice(commas[0] + 1, end) : '',
      raw: commas.length ? text.slice(commas[0] + 1, end) : '' })
  }
  return calls
}
// The arm's predicate: an agent( call whose options name none of the four stage option constants is untyped.
function checkStageOpts(text) {
  const calls = scanAgentCalls(text)
  const bad = calls.filter((c) => !STAGE_OPTS.some((n) => new RegExp('(?<![\\w$])' + n + '(?![\\w$])').test(c.opts)))
  return { calls: calls, bad: bad }
}
async function runTypedStageArms() {
  const path = require('path')
  const tpl = fs.readFileSync(path.join(path.dirname(FILE), 'tier2-review.template.js'), 'utf8')
  // ---- S3/AC4: every agent( call of the template takes a stage constant; a copy without the probe's names it.
  const live = checkStageOpts(tpl)
  ck(live.calls.length >= 5 && live.bad.length === 0, 'stage: all ' + live.calls.length + ' agent( calls of the template take one of ' + STAGE_OPTS.join(', ') +
    ' as their options' + (live.bad.length ? ' — untyped at L' + live.bad.map((c) => c.line).join(', L') : ''))
  const PROBE_OPTS = '  }, probeOpts), // TOOL-dFairHearing-11 S1'
  const planted = checkStageOpts(tpl.replace(PROBE_OPTS, '  }), // TOOL-dFairHearing-11 S1'))
  ck(tpl.indexOf(PROBE_OPTS) !== -1 && planted.bad.length === 1 && planted.bad[0].raw.indexOf('\'resume:probe\'') !== -1,
    'stage: a copy with the probe\'s probeOpts removed names exactly the probe\'s agent( call: ' + planted.bad.map((c) => 'L' + c.line).join(' '))
  const SYNTH_TYPE = 'const synthType = roles.synthesis || PLATFORM_TYPE'
  const re = whole.indexOf(SYNTH_TYPE) === -1 ? { threw: 'the stage table line moved', trace: [] }
    : await runReview(DIFF, ALL_OK, whole.replace(SYNTH_TYPE, 'const synthType = roles.synthesis || \'\''))
  ck(!!re.threw && re.threw.indexOf('the stage synthesis resolves to no agent type') !== -1 && re.trace.length === 0,
    'stage: a stage table resolving synthesis to an empty string refuses by name before the probe: ' + re.threw)
  // ---- AC1: roles.probe types the probe, Plan without it, and `none` is refused like any roles value.
  const probeOf = (x) => x.trace.find((t) => t.label === 'resume:probe') || {}
  let r = await runReview(Object.assign({}, DIFF, { roles: { probe: 'gov-orienter' } }), ALL_OK)
  ck(!r.threw && probeOf(r).agentType === 'gov-orienter' && r.logs.indexOf('role probe: gov-orienter — roles.probe') !== -1,
    'stage: roles.probe types the resume probe, and its log line names the source')
  r = await runReview(Object.assign({}, DIFF, { roles: { probe: 'none' } }), ALL_OK)
  ck(!!r.threw && r.threw.indexOf('tier2-review: `roles` key probe') === 0 && r.trace.length === 0, 'stage: roles.probe none is refused before any spawn')
  r = await runReview(Object.assign({}, DIFF, { efforts: { probe: 'low' } }), ALL_OK)
  ck(!r.threw && probeOf(r).effort === 'low' && r.logs.indexOf('effort probe: low — efforts.probe') !== -1, 'stage: efforts.probe sets the probe\'s effort')
  // ---- AC2: under `none` every judge and the synthesis take general-purpose; absent, the judges Plan.
  const rn = await runReview(DIFF, ALL_OK)
  const ABSW = Object.assign({}, DIFF); delete ABSW.workerType
  const ra = await runReview(ABSW, ALL_OK)
  const typesOf = (x, re2) => x.trace.filter((t) => re2.test(t.label)).map((t) => t.agentType)
  ck(!rn.threw && probeOf(rn).agentType === 'Plan' && typesOf(rn, /^(find|verify):|^synth$/).length === 11 &&
    typesOf(rn, /^(find|verify):|^synth$/).every((t) => t === 'general-purpose'), 'stage: none, the five finders, five batches and the synthesis are general-purpose and the probe Plan')
  ck(!ra.threw && probeOf(ra).agentType === 'Plan' && typesOf(ra, /^(find|verify):/).length === 10 && typesOf(ra, /^(find|verify):/).every((t) => t === 'Plan') &&
    typesOf(ra, /^synth$/).join() === 'general-purpose' && ra.trace.every((t) => typeof t.agentType === 'string' && t.agentType !== ''),
    'stage: workerType absent, the judges are Plan, the synthesis general-purpose, and every spawn typed: ' + ra.trace.length)
  // ---- AC3: `durable` follows the judge stages' resolution to PLATFORM_TYPE, not the explicit type.
  ck(rn.result.durable === true && rn.trace.filter((t) => t.label.indexOf('find:') === 0).every((t) => t.prompt.indexOf('DURABILITY') !== -1) &&
    ra.result.durable === false, 'stage: none is durable with every finder told DURABILITY, and Plan is not durable')
}

// ==== TOOL-dFairHearing-11 — `twin`, run b and the twin merge (AC5-AC10) =============================
// RED against the parent render: it reads no `twin`, refuses no value, dispatches five finders on every
// run, hands no TWIN RUN block or review-twin line, and returns no `twin`. WHAT IT DOES NOT CHECK: that a
// live synthesis merges the two runs as told or copies the line; the return's `twin` is the source a caller
// compares against.
async function runTwinRunArms() {
  const finds = (x) => x.trace.filter((t) => t.label.indexOf('find:') === 0)
  // ---- AC5: a closed set, refused outside it before any spawn; each member starts.
  let r = await runReview(Object.assign({}, DIFF, { twin: 'sometimes' }), ALL_OK)
  ck(!!r.threw && r.threw.indexOf('tier2-review: `twin` must be one of never | design-records | design-and-landing | always') === 0 && r.trace.length === 0,
    'twin: sometimes is refused before any spawn, naming the four values')
  const started = []
  for (const v of ['never', 'design-records', 'design-and-landing', 'always']) {
    r = await runReview(Object.assign({}, DIFF, { twin: v }), ALL_OK)
    if (!r.threw && r.result && r.result.exit === 'complete') started.push(v)
  }
  ck(started.length === 4, 'twin: each of the four values starts and completes: ' + started.join(' '))
  // ---- AC6: ten finders exactly where S5 says; ten is twice the five-slot literal.
  const CASES = { diff: DIFF, 'unit-spec audit': SPEC, 'design-audit preset': Object.assign({}, SPEC, { preset: 'design-audit' }),
    'design-subject audit': Object.assign({}, SPEC, { subjects: [{ path: 'memory/builds/dX/build/a.md', blob: 'abc1234', id: 'PLAY-dX-1' }] }) }
  const WANT = { never: [], 'design-records': ['design-audit preset', 'design-subject audit'], 'design-and-landing': ['diff', 'design-audit preset', 'design-subject audit'],
    always: ['diff', 'unit-spec audit', 'design-audit preset', 'design-subject audit'] }
  for (const t of Object.keys(WANT)) {
    const got = []
    for (const c of Object.keys(CASES)) {
      const x = await runReview(Object.assign({}, CASES[c], { twin: t }), ALL_OK)
      got.push(x.threw ? c + ' threw' : finds(x).length === 10 ? c : finds(x).length === 5 ? null : c + ' at ' + finds(x).length)
    }
    ck(got.filter(Boolean).join(', ') === WANT[t].join(', '), 'twin: ' + t + ' dispatches ten finders on ' + (got.filter(Boolean).join(', ') || 'no run'))
  }
  // ---- AC7: run a two findings a lens, run b one; ids run 1-10 then 11-15, and the batch count is an
  // untwinned fifteen-finding run's.
  const buildRunLens = (label) => {
    const lens = label.slice('find:'.length).replace(/:b$/, '')
    const b = /:b$/.test(label)
    const mk = (n) => ({ file: lens + '.js', line: n, severity: 'high', claim: lens + ' ' + n + (b ? ' b' : ' a'), impact: 'i', fix: 'f' })
    return { lens: lens, path: '/p', findings: b ? [mk(1)] : [mk(1), mk(40)] }
  }
  const buildFifteen = (label) => ({ lens: label.slice('find:'.length), path: '/p', findings: [1, 2, 3].map((n) => ({ file: 'f.js', line: n * 10, severity: 'high', claim: 'c' + n, impact: 'i', fix: 'f' })) })
  const buildTwinSynth = (drop) => (label, prompt) => {
    const ids = [...prompt.split('UNVERIFIED findings')[0].matchAll(/id=(\d+) \[/g)].map((x) => parseInt(x[1], 10)).filter((id) => id !== drop && id !== 12)
    return { path: 'memory/reviews/r.md', summary: 's', items: ids.map((id) => {
      const hold = id === 3 ? [3, 12] : [id]
      return { severity: 'HIGH', ids: hold, grades: buildGrades(hold, 'HIGH') }
    }) }
  }
  const TW = Object.assign({}, DIFF, { twin: 'always' })
  const rt = await runReview(TW, buildStubs({ 'find:': buildRunLens, synth: buildTwinSynth(null) }))
  const ru = await runReview(DIFF, buildStubs({ 'find:': buildFifteen }))
  if (checkNoThrow(rt, 'twin run') && checkNoThrow(ru, 'untwinned fifteen')) {
    const fb = finds(rt).slice(5)
    ck(rt.result.ledger.map((e) => e.id).join(',') === '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15' &&
      rt.result.ledger.every((e) => / (a|b)$/.exec(e.claim)[1] === (e.id <= 10 ? 'a' : 'b')) &&
      fb.length === 5 && fb.every((t) => /:b$/.test(t.label) && t.prompt.indexOf('/find-' + t.label.slice(5, -2) + '-b.json') !== -1),
      'twin: run a takes ids 1-10 and run b 11-15, run b\'s labels ending :b and its files -b: ' + fb.map((t) => t.label).join(' '))
    const vb = (x) => x.trace.filter((t) => t.label.indexOf('verify:') === 0).length
    ck(vb(rt) === vb(ru) && ru.result.raw === 15 && rt.result.raw === 15 && rt.result.agents === 10 + vb(rt) + 1 && rt.result.lensesRun === 10 &&
      / raw=15 .* agents=16 /.test(rt.result.shape), 'twin: the verify stage dispatches ' + vb(rt) + ' batches as an untwinned fifteen does, and agents, raw and the shape line count both runs: ' + rt.result.shape)
    // ---- AC8: the figures come from the items; the prompt carries the block and the line; an untwinned run neither.
    const tw = rt.result.twin || {}
    ck(tw.agreed === 1 && tw.onlyA === 9 && tw.onlyB === 4 && (tw.a || []).join(',') === '1,2,3,4,5,6,7,8,9,10' && (tw.b || []).join(',') === '11,12,13,14,15',
      'twin: ids 3 and 12 in one item read agreed 1, and a and b list each run\'s confirmed ids: ' + JSON.stringify(rt.result.twin))
    const sp = (rt.trace.find((t) => t.label === 'synth') || { prompt: '' }).prompt
    ck(sp.indexOf('\n\nTWIN RUN - ') !== -1 && sp.indexOf('<<<TWIN\nreview-twin runs=2 a=1-10 b=11-15\nTWIN>>>') !== -1 && sp.indexOf(' lens=correctness run=a correctness.js:1 — ') !== -1 &&
      sp.indexOf('- run a id=3 and run b id=12, both at correctness.js 1') !== -1, 'twin: the synthesis prompt carries the TWIN RUN block, each finding\'s run, the pair 3/12 and the review-twin line between markers')
    const su = (ru.trace.find((t) => t.label === 'synth') || { prompt: '' }).prompt
    ck(su.length > 0 && su.indexOf('TWIN RUN') === -1 && su.indexOf('review-twin') === -1 && su.indexOf(' run=') === -1 && ru.result.twin === null,
      'twin: an untwinned run\'s synthesis prompt carries neither the block nor the line, and its return reads twin null')
  }
  // ---- AC9: a run-b confirmed id in no item nulls blockers and twin, and the note names it.
  r = await runReview(TW, buildStubs({ 'find:': buildRunLens, synth: buildTwinSynth(14) }))
  ck(!r.threw && r.result.blockers === null && r.result.twin === null && r.result.note.indexOf('confirmed id(s) 14 sit in no item') !== -1,
    'twin: an unplaced run-b id 14 nulls blockers and twin, and the note names it')
  // ---- AC10: a twinned run keys apart; `never` keys as an absent value.
  const deriveTwinKey = async (v) => {
    const x = await runReview(v === undefined ? DIFF : Object.assign({}, DIFF, { twin: v }), ALL_OK)
    return x.result ? x.result.key : 'threw: ' + x.threw
  }
  const kAbsent = await deriveTwinKey(undefined)
  const kNever = await deriveTwinKey('never')
  const kAlways = await deriveTwinKey('always')
  ck(kAbsent.indexOf('threw') !== 0 && kAbsent === kNever && kAlways !== kAbsent, 'twin: always moves the key and never keeps it: ' + [kAbsent, kNever, kAlways].join(' '))
  // ---- a dead run-b lens defers by its :b label.
  r = await runReview(TW, buildStubs({ 'find:seams:b': null }))
  ck(!r.threw && r.result.exit === 'deferred-platform' && JSON.stringify(r.result.pending) === '["find:seams:b"]', 'twin: a dead run-b lens defers, pending find:seams:b: ' + JSON.stringify(r.result && r.result.pending))
  // ---- AC5's stand-in half: review_pin.py prints the pin argument, and refuses a value off the set by name.
  const py = process.argv[5] || ''
  const { spawnSync } = require('child_process')
  const pin = require('path').join(require('path').dirname(FILE), 'review_pin.py')
  const runPin = (argv) => {
    if (!py) return { status: -1, stdout: '', stderr: 'no python was resolved' }
    const x = spawnSync(py, ['-B', pin].concat(argv), { encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }) })
    return { status: x.status, stdout: x.stdout || '', stderr: (x.stderr || '') + (x.error ? String(x.error) : '') }
  }
  const p1 = runPin(['--subject', 'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md', '--twin', 'always'])
  ck(p1.status === 0 && p1.stdout === '{"preset": "unit-spec", "twin": "always"}\n', 'twin: review_pin.py --twin always prints twin always (got ' + p1.status + ': ' + (p1.stdout || p1.stderr).trim() + ')')
  const p2 = runPin(['--subject', 'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md', '--twin', 'sometimes'])
  ck(p2.status === 2 && p2.stdout === '' && p2.stderr.indexOf('--twin') !== -1, 'twin: review_pin.py --twin sometimes exits 2 naming --twin (got ' + p2.status + ')')
  // ---- TOOL-dFairHearing-8 AC4's stand-in half, on this runner: `--unclassed` printed, and refused off its three values.
  const p3 = runPin(['--subject', 'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md', '--unclassed', 'reason'])
  ck(p3.status === 0 && p3.stdout === '{"preset": "unit-spec", "unclassed": "reason"}\n', 'unclassed: review_pin.py --unclassed reason prints unclassed reason (got ' + p3.status + ': ' + (p3.stdout || p3.stderr).trim() + ')')
  const p4 = runPin(['--subject', 'memory/builds/dX/spec/2026-01-01-spec-TOOL-dX-1.md', '--unclassed', 'maybe'])
  ck(p4.status === 2 && p4.stdout === '' && p4.stderr.indexOf('--unclassed') !== -1, 'unclassed: review_pin.py --unclassed maybe exits 2 naming --unclassed (got ' + p4.status + ')')
}

// ==== TOOL-dFairHearing-8 — the class fix judge, and every confirmed finding's disposition (AC1-AC9) ======
// RED against the parent render: it reads no `fixJudge`, `unclassed` or `gateManifest`, so none refuses; its
// skeptics are never asked the class question; its probe reads no leg manifest; its synthesis is handed no
// DISPOSITIONS block and its schema requires no `dispositions`; its appendix has nine columns; and its return
// carries no `dispositions`, `dispositionFault` or `ownerItems`. WHAT IT DOES NOT CHECK: that a live skeptic
// judges a fix by its class, or that a live synthesis writes the disposition cells it is told to; the return's
// `appendix` is the source a caller compares the record against. AC2's byte-equality to the parent render is
// the pass's probe, since this suite reads one render; here `class` and an absent value agree, the default
// TOOL-dFairHearing-1 S9 flipped, so the absent arms run DIFF with its `fixJudge` pin deleted.
async function runDispositionArms() {
  const skepticPrompts = (x) => x.trace.filter((t) => t.label.indexOf('verify:') === 0).map((t) => t.prompt)
  const synthCall = (x) => x.trace.find((t) => t.label === 'synth') || { prompt: '', schema: { required: [], properties: {} } }
  const probeCall = (x) => x.trace.find((t) => t.label === 'resume:probe') || { prompt: '' }
  // A synthesis placing every confirmed id in one HIGH item, returning `pick(ids)` as its dispositions.
  const buildDisposingSynth = (pick) => (label, prompt) => Object.assign(buildSynth(null)(label, prompt),
    { dispositions: pick([...prompt.split('UNVERIFIED findings')[0].matchAll(/id=(\d+) \[/g)].map((x) => parseInt(x[1], 10))) })
  // ---- AC1: a closed set, refused outside it before any spawn; each member and the absent value start.
  let r = await runReview(Object.assign({}, DIFF, { fixJudge: 'both' }), ALL_OK)
  ck(!!r.threw && r.threw.indexOf('tier2-review: `fixJudge` must be one of instance | class') === 0 && r.trace.length === 0,
    'fixJudge: both is refused before any spawn, naming the two values')
  const UNJUDGED = Object.assign({}, DIFF)
  delete UNJUDGED.fixJudge
  const started = []
  for (const v of [undefined, 'instance', 'class']) {
    r = await runReview(v === undefined ? UNJUDGED : Object.assign({}, DIFF, { fixJudge: v }), ALL_OK)
    if (!r.threw && r.result && r.result.exit === 'complete') started.push(String(v))
  }
  ck(started.length === 3, 'fixJudge: absent, instance and class each start and complete: ' + started.join(' '))
  // ---- AC2: `class` keeps the absent run's skeptic prompts and key; `instance` asks the instance question and keys apart.
  const ra = await runReview(UNJUDGED, ALL_OK)
  const ri = await runReview(Object.assign({}, DIFF, { fixJudge: 'instance' }), ALL_OK)
  const rc = await runReview(Object.assign({}, DIFF, { fixJudge: 'class' }), ALL_OK)
  if (checkNoThrow(ra, 'fixJudge absent') && checkNoThrow(ri, 'fixJudge instance') && checkNoThrow(rc, 'fixJudge class')) {
    ck(skepticPrompts(ri).length === 5 && skepticPrompts(ri).every((p) => p.indexOf('"instance"') === -1 && p.indexOf('fixVerdict:"sound"|"unsound"|"none", fixNote') !== -1) &&
      ri.result.key !== ra.result.key,
      'fixJudge: instance asks every skeptic the instance question, with no instance verdict, and moves the key: ' + ri.result.key)
    ck(skepticPrompts(ra).length === 5 && JSON.stringify(skepticPrompts(rc)) === JSON.stringify(skepticPrompts(ra)) && rc.result.key === ra.result.key &&
      skepticPrompts(ra).every((p) => p.indexOf('judge its proposed fix by the defect\'s CLASS') !== -1 &&
      p.indexOf('"instance" when it cures the cited instance and leaves another of its class standing') !== -1 &&
      p.indexOf('fixVerdict:"sound"|"unsound"|"none"|"instance", fixNote') !== -1),
      'fixJudge: class hands the absent run\'s skeptic prompts, the class question with the instance verdict, and derives its key')
  }
  // ---- AC3: an instance verdict with a note is the fix under `class`, and not judged under `instance`.
  const buildInstanceVerdicts = (label, prompt) => {
    const v = buildVerdicts('confirmed')(label, prompt)
    for (const x of v.verdicts) Object.assign(x, x.id === 2 ? { fixVerdict: 'instance', fixNote: 'cure every instance' } : { fixVerdict: 'sound' })
    return v
  }
  const r3c = await runReview(Object.assign({}, DIFF, { fixJudge: 'class' }), buildStubs({ 'verify:': buildInstanceVerdicts }))
  const r3i = await runReview(DIFF, buildStubs({ 'verify:': buildInstanceVerdicts }))
  if (checkNoThrow(r3c, 'instance under class') && checkNoThrow(r3i, 'instance under instance')) {
    const c2 = r3c.result.confirmedFindings.find((e) => e.id === 2) || {}
    const i2 = r3i.result.confirmedFindings.find((e) => e.id === 2) || {}
    ck(c2.fix === 'cure every instance' && c2.fixVerdict === 'instance' &&
      synthCall(r3c).prompt.indexOf('fixes on confirmed findings: 4 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY') !== -1 &&
      synthCall(r3c).prompt.indexOf('fix: judged INSTANCE-ONLY by the skeptic, whose class-level fix is: cure every instance') !== -1,
      'fixJudge: under class an instance fix gives way to its note, and RUN INTEGRITY counts one instance-only fix')
    ck(i2.fix === 'f' && i2.fixVerdict === null && synthCall(r3i).prompt.indexOf('INSTANCE-ONLY') === -1 &&
      synthCall(r3i).prompt.indexOf('4 judged sound, 0 judged UNSOUND, 0 none proposed, 1 NOT JUDGED') !== -1,
      'fixJudge: under instance the same answer counts as a fix not judged')
  }
  // ---- AC4: `unclassed`, a closed set, and `refuse` stated when absent.
  r = await runReview(Object.assign({}, DIFF, { unclassed: 'maybe' }), ALL_OK)
  ck(!!r.threw && r.threw.indexOf('tier2-review: `unclassed` must be one of refuse | reason | owner-rules') === 0 && r.trace.length === 0,
    'unclassed: maybe is refused before any spawn, naming the three values')
  ck(synthCall(ra).prompt.indexOf('\nunclassed: refuse - none is refused') !== -1, 'unclassed: absent, the synthesis prompt states refuse')
  // ---- AC5: `gateManifest` refused on the specs rule, rendered into the probe, and no legs refusing every gate:.
  r = await runReview(Object.assign({}, DIFF, { gateManifest: '../x.json' }), ALL_OK)
  ck(!!r.threw && r.threw.indexOf('tier2-review: `gateManifest` must be a repo-relative path') === 0 && r.trace.length === 0,
    'gateManifest: ../x.json is refused before any spawn')
  ck(probeCall(ra).prompt.indexOf('gate-legs.json, the leg manifest') !== -1 && probeCall(ra).prompt.indexOf('{{TOOL_ROOT}}') === -1,
    'gateManifest: absent, the probe is told to read the rendered default gate-legs.json')
  const r5 = await runReview(DIFF, buildStubs({ synth: buildDisposingSynth((ids) => ids.map((id) => ({ id: id, disposition: 'gate:memory hygiene' }))) }))
  if (checkNoThrow(r5, 'no legs'))
    ck(r5.logs.some((l) => l.indexOf('WARNING: no leg manifest was read from ') === 0) && synthCall(r5).prompt.indexOf('Leg names: no leg manifest was read') !== -1 &&
      r5.result.dispositions === null && r5.result.dispositionFault.indexOf('id 1 is "gate:memory hygiene", and no leg manifest was read') !== -1,
      'gateManifest: a probe returning no legs is logged and stated, and gate:memory hygiene is refused')
  // ---- AC6: two slug-led items and one with no slug; one leg; the four forms; the schema requires the field.
  const CL = Object.assign({}, DIFF, { checklist: ['[ ] alpha-one (universal)', 'beta-two the second', 'Not slug-led'] })
  const LEGS = { 'resume:probe': Object.assign(buildProbe(), { legs: ['memory hygiene'], legCount: 1 }) }
  const r6 = await runReview(CL, buildStubs(LEGS))
  if (checkNoThrow(r6, 'dispositions block')) {
    const s6 = synthCall(r6)
    ck(s6.prompt.indexOf('Class slugs (2): alpha-one, beta-two.') !== -1 && s6.prompt.indexOf('Leg names (1), one per line:\n  - memory hygiene\n') !== -1 &&
      ['class:<slug>', 'gate:<leg>', 'new:<slug>', 'none'].every((f) => s6.prompt.indexOf('\n- ' + f + ' - ') !== -1) &&
      s6.schema.required.indexOf('dispositions') !== -1 && !!s6.schema.properties.dispositions,
      'dispositions: the synthesis is handed two slugs, no C<n>, one leg and the four forms, and its schema requires dispositions')
  }
  // ---- AC7: a legal set is accepted; each of six planted faults refuses it, names the id, and keeps the counts.
  const GOOD = { 1: 'class:alpha-one', 2: 'gate:memory hygiene', 3: 'new:fresh-class', 4: 'class:beta-two', 5: 'new:other-class' }
  const buildSet = (map, extra) => (ids) => ids.filter((id) => map[id] !== undefined).map((id) => ({ id: id, disposition: map[id] })).concat(extra || [])
  const r7 = await runReview(CL, buildStubs(Object.assign({ synth: buildDisposingSynth(buildSet(GOOD)) }, LEGS)))
  if (checkNoThrow(r7, 'dispositions accepted'))
    ck(Array.isArray(r7.result.dispositions) && r7.result.dispositions.map((x) => x.disposition).join(',') === [1, 2, 3, 4, 5].map((n) => GOOD[n]).join(',') &&
      r7.result.dispositionFault === '' && r7.result.note === 'complete', 'dispositions: class:, gate: and new: over the handed names are accepted, the fault empty')
  const FAULTS = [['class:C3', Object.assign({}, GOOD, { 1: 'class:C3' }), [], 'id 1 '], ['gate:no such leg', Object.assign({}, GOOD, { 1: 'gate:no such leg' }), [], 'id 1 '],
    ['new: a handed slug', Object.assign({}, GOOD, { 1: 'new:alpha-one' }), [], 'id 1 '], ['a repeated id', GOOD, [{ id: 2, disposition: 'new:x' }], 'id 2 is disposed more than once'],
    ['an id not confirmed', GOOD, [{ id: 99, disposition: 'new:x' }], 'id 99 is not a confirmed id'], ['a confirmed id with none', Object.assign({}, GOOD, { 5: undefined }), [], 'id 5 has no disposition']]
  for (const [what, map, extra, names] of FAULTS) {
    const x = await runReview(CL, buildStubs(Object.assign({ synth: buildDisposingSynth(buildSet(map, extra)) }, LEGS)))
    ck(!x.threw && x.result.dispositions === null && x.result.dispositionFault.indexOf(names) !== -1 && x.result.blockers === 0 && x.result.highs === 5 &&
      x.result.note.indexOf('the DISPOSITIONS were refused') !== -1 && x.result.appendix.split('\n').slice(4).every((l) => l.endsWith(' | - |')),
      'dispositions: ' + what + ' refuses the set naming "' + names.trim() + '", keeps the counts and returns - cells: ' + (x.threw || x.result.dispositionFault))
  }
  // ---- AC8: `none` with a reason under each `unclassed` value, and `none` with an empty reason under all three.
  for (const u of ['refuse', 'reason', 'owner-rules']) {
    const buildNone = (reason) => buildDisposingSynth((ids) => ids.map((id) => (id === 1 ? { id: id, disposition: 'none', reason: reason } : { id: id, disposition: 'new:fresh-class' })))
    const x = await runReview(Object.assign({}, DIFF, { unclassed: u }), buildStubs({ synth: buildNone('no home') }))
    const y = await runReview(Object.assign({}, DIFF, { unclassed: u }), buildStubs({ synth: buildNone('') }))
    ck(!x.threw && !y.threw && (u === 'refuse' ? x.result.dispositions === null : Array.isArray(x.result.dispositions)) &&
      JSON.stringify(x.result.ownerItems) === (u === 'owner-rules' ? '[1]' : '[]') && y.result.dispositions === null && y.result.dispositionFault.indexOf('id 1 ') === 0,
      'dispositions: under ' + u + ' none with a reason is ' + (u === 'refuse' ? 'refused' : 'accepted') + ', ownerItems ' + JSON.stringify(x.result && x.result.ownerItems) +
      ', and none with an empty reason is refused')
  }
  // ---- TOOL-dFairHearing-43 AC2: `renderCell` is the one encoder of the returned appendix, so a `none` reason is plain
  // text: a raw `|` and a line break are each accepted, and `parse_appendix_rows` reads id 1's cell back. The agent writes
  // the record's own cell, so the appendix paragraph states the escape. RED against the render at unit 40, which refuses
  // both reasons and states no such sentence.
  {
    const py = process.argv[5] || ''
    const { spawnSync } = require('child_process')
    const buildReason = (reason) => buildDisposingSynth((ids) => ids.map((id) => (id === 1 ? { id: id, disposition: 'none', reason: reason } : { id: id, disposition: 'new:fresh-class' })))
    const readCell = (x) => {
      if (x.threw || !py) return 'no read-back: ' + (x.threw || 'no python was resolved')
      const p = spawnSync(py, ['-B', '-c', 'import json, sys\nsys.path.insert(0, sys.argv[1])\nimport replay_scorer\nrows, err = replay_scorer.parse_appendix_rows(sys.stdin.read())\n' +
        'print(json.dumps(err or [r["disposition"] for r in rows if r["id"] == "1"][0]))', require('path').dirname(FILE)],
      { input: 'confirmed ' + x.result.confirmed + '\n' + x.result.appendix, encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }) })
      try { return JSON.parse(p.stdout) } catch { return 'no read-back: ' + p.stdout + p.stderr }
    }
    const raw = await runReview(Object.assign({}, DIFF, { unclassed: 'reason' }), buildStubs({ synth: buildReason('a | b') }))
    const brk = await runReview(Object.assign({}, DIFF, { unclassed: 'reason' }), buildStubs({ synth: buildReason('a\nb') }))
    ck(!raw.threw && Array.isArray(raw.result.dispositions) && readCell(raw) === 'none — a | b',
      'FH43 AC2 a reason holding a raw | is accepted and reads back whole: ' + readCell(raw))
    ck(!brk.threw && Array.isArray(brk.result.dispositions) && readCell(brk) === 'none — a b',
      'FH43 AC2 a reason holding a line break is accepted and reads back as one space: ' + readCell(brk))
    const ask = synthCall(raw).prompt
    const paragraph = ask.slice(ask.indexOf('APPENDIX - the report\'s LAST section'))
    ck(ask.indexOf('a pipe written as') === -1 && paragraph.indexOf('APPENDIX - ') === 0 && paragraph.indexOf('which you write and the harness does not encode') !== -1,
      'FH43 AC2 the prompt asks for no escape in the returned reason, and the appendix paragraph states it for the record\'s cell')
  }
  // ---- TOOL-dFairHearing-23 AC22: the leg list is used whole or not at all. RED against the parent render, whose filter keeps a
  // truncated list and an empty one as the manifest, so the short list admits the gate and the empty one names no missing manifest.
  {
    const GATED = buildSet({ 1: 'gate:memory hygiene', 2: 'new:fresh-class', 3: 'new:fresh-class', 4: 'new:fresh-class', 5: 'new:fresh-class' })
    for (const [what, legs, legCount] of [['an empty list', [], 0], ['a list one short of legCount', ['memory hygiene'], 2],
      ['a duplicate', ['memory hygiene', 'memory hygiene'], 2], ['a non-string', ['memory hygiene', 7], 2]]) {
      const x = await runReview(CL, buildStubs({ 'resume:probe': Object.assign(buildProbe(), { legs: legs, legCount: legCount }), synth: buildDisposingSynth(GATED) }))
      ck(!x.threw && x.logs.some((l) => l.indexOf('WARNING: no leg manifest was read from ') === 0) && x.result.dispositions === null &&
        x.result.dispositionFault.indexOf('id 1 is "gate:memory hygiene", and no leg manifest was read') !== -1,
        'FH23 AC22 ' + what + ' reads as no leg manifest and admits no gate: disposition: ' + (x.threw || x.result.dispositionFault))
    }
    const whole = await runReview(CL, buildStubs(Object.assign({ synth: buildDisposingSynth(GATED) }, LEGS)))
    ck(!whole.threw && Array.isArray(whole.result.dispositions) && whole.result.dispositions[0].disposition === 'gate:memory hygiene',
      'FH23 AC22 a whole list matching legCount admits the valid gate: ' + (whole.threw || whole.result.dispositionFault))
  }
  // ---- AC9: two confirmed and three refuted; the handed appendix has ten columns and two placeholders; the return the dispositions.
  const r9 = await runReview(Object.assign({}, DIFF, { unclassed: 'reason' }), buildStubs({
    'verify:': (label, prompt) => { const v = buildVerdicts('confirmed')(label, prompt); for (const z of v.verdicts) if (z.id > 2) z.verdict = 'refuted'; return v },
    synth: buildDisposingSynth((ids) => ids.map((id) => (id === 1 ? { id: id, disposition: 'new:fresh-class' } : { id: id, disposition: 'none', reason: 'no home' }))) }))
  if (checkNoThrow(r9, 'disposition column')) {
    const handed = (synthCall(r9).prompt.split('<<<APPENDIX\n')[1] || '').split('\nAPPENDIX>>>')[0].split('\n')
    ck(handed[2] === '| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |' &&
      handed.length === 9 && handed[4].endsWith(' | (synthesis) |') && handed[5].endsWith(' | (synthesis) |') && handed.slice(6).every((l) => l.endsWith(' | - |')),
      'dispositions: the handed appendix ends classes | disposition, (synthesis) on the two confirmed rows and - on the refuted ones')
    const back = r9.result.appendix.split('\n')
    ck(back[4].endsWith(' | new:fresh-class |') && back[5].endsWith(' | none — no home |') && back.slice(6).every((l) => l.endsWith(' | - |')) &&
      r9.result.ledger[0].disposition === 'new:fresh-class' && r9.result.ledger[2].disposition === '-' && r9.result.confirmedFindings[1].disposition === 'none',
      'dispositions: the returned appendix, ledger and confirmed set carry the accepted dispositions, a none cell with its reason')
  }
}

// ==== TOOL-aOrientedCast-10 — `efforts`, each stage spawned at the reasoning effort its caller names ====
// Every arm is RED against the parent render, which reads no `efforts`: no refusal fires, no spawn's
// options carry an `effort` key and no `effort ` line is logged. A green arm says the routing follows
// the argument; it does not prove the platform honours `opts.effort`, which the unit's live probe does.
async function runEffortsArms() {
  const scanStage = (run, p) => run.trace.filter((t) => t.label.indexOf(p) === 0)
  const checkEvery = (xs, f) => xs.length > 0 && xs.every(f)
  // ---- every malformed `efforts` refuses before any spawn, naming the argument.
  for (const [lbl, v] of [['an array', []], ['an unknown key', { finder: 'high' }], ['a value off the shape', { skeptic: 'High' }]]) {
    const x = await runReview(Object.assign({}, DIFF, { efforts: v }), ALL_OK)
    ck(!!x.threw && x.threw.indexOf('tier2-review: `efforts`') === 0 && x.trace.length === 0,
      'efforts: ' + lbl + ' is refused before any spawn' + (x.threw ? '' : ' (it proceeded)'))
  }
  // ---- a spec audit's three keys reach the finders, the skeptics and the synthesis; never the probe.
  let r = await runReview(Object.assign({}, SPEC, { efforts: { specFinder: 'medium', skeptic: 'medium', synthesis: 'medium' } }), ALL_OK)
  if (checkNoThrow(r, 'efforts spec')) {
    for (const p of ['find:', 'verify:', 'synth'])
      ck(checkEvery(scanStage(r, p), (t) => t.effort === 'medium'), 'efforts: every ' + p + ' spawn of a spec audit carries effort medium')
    ck(scanStage(r, 'resume:probe').length === 1 && !scanStage(r, 'resume:probe')[0].hasEffort, 'efforts: the resume probe carries no effort key')
    ck(r.logs.indexOf('effort specFinder: medium — efforts.specFinder') !== -1, 'efforts: the log names the finder level and its source')
  }
  // ---- a diff review's finder key moves the finders alone; an unnamed stage carries no key.
  r = await runReview(Object.assign({}, DIFF, { efforts: { diffFinder: 'high', specFinder: 'low' } }), ALL_OK)
  if (checkNoThrow(r, 'efforts diff')) {
    ck(scanStage(r, 'find:').length === 5 && checkEvery(scanStage(r, 'find:'), (t) => t.effort === 'high'), 'efforts: every diff find: spawn carries effort high')
    ck(checkEvery(scanStage(r, 'verify:'), (t) => !t.hasEffort) && checkEvery(scanStage(r, 'synth'), (t) => !t.hasEffort),
      'efforts: a stage efforts does not name carries no effort key')
    ck(r.logs.some((l) => l.indexOf('effort skeptic: the agent type') === 0 && l.indexOf('no efforts.skeptic') !== -1) &&
      r.logs.indexOf('effort specFinder: efforts.specFinder is not read on a diff-review') !== -1,
      'efforts: the log says an unnamed stage runs at its type\'s level, and the other kind\'s finder key is not read')
  }
  // ---- independent of `roles`: an untyped skeptic still takes its level.
  r = await runReview(Object.assign({}, DIFF, { efforts: { skeptic: 'max' } }), ALL_OK)
  if (checkNoThrow(r, 'efforts untyped skeptic'))
    ck(checkEvery(scanStage(r, 'verify:'), (t) => t.effort === 'max' && t.agentType === 'general-purpose'), 'efforts: a skeptic no role names spawns at its level')
  // ---- absent, no spawn's options carry the key: the call is today's byte for byte.
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'efforts absent'))
    ck(r.trace.length > 0 && r.trace.every((t) => !t.hasEffort), 'efforts: absent, no spawn carries an effort key')
}

// ==== TOOL-aEvidencedLens-6 — `lensYield`, one row per running lens, unique defects counted by ITEM ====
// Every arm is RED against the parent render, which returns no `lensYield` on any path, logs no
// `lens yield:` line and puts no LENS YIELD block in the synthesis prompt.
async function runLensYieldArms() {
  const LORDER = ['security', 'correctness', 'seams', 'verification', 'intent']
  const scanYield = (run, n) => !!run.result && Array.isArray(run.result.lensYield) && run.result.lensYield.length === n
  const buildSynthOwn = (label, prompt) => ({ path: 'memory/reviews/r.md', summary: 's',
    items: [...prompt.split('UNVERIFIED findings')[0].matchAll(/id=(\d+) \[/g)].map((x) => ({ severity: 'HIGH', ids: [parseInt(x[1], 10)], grades: { [x[1]]: 'HIGH' }, specs: ['TOOL-x-1'] })) })
  const buildVerdictById = (pick) => (label, prompt) => {
    const m = /ids ([0-9, ]+)\)/.exec(prompt)
    const ids = m ? m[1].split(',').map((x) => parseInt(x, 10)) : []
    return { path: '/cd/v.json', verdicts: ids.map((id) => ({ id: id, verdict: pick(id), reason: 'r' })) }
  }
  // ---- AC1: each id in its own item credits every lens one unique defect; one item holding all five
  // ---- credits none, which a raw-finding `unique` would credit five times.
  let r = await runReview(DIFF, buildStubs({ synth: buildSynthOwn }))
  if (checkNoThrow(r, 'lens yield own items')) {
    ck(scanYield(r, 5) && r.result.lensYield.every((e, i) => e.lens === LORDER[i] && e.returned === true && e.raw === 1 && e.confirmed === 1 &&
      e.precision === 1 && e.defects === 1 && e.unique === 1), 'lens yield: each id in its own item reads raw, confirmed, precision, defects and unique 1 per lens')
  }
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'lens yield shared item')) {
    ck(scanYield(r, 5) && r.result.lensYield.every((e) => e.defects === 1 && e.unique === 0), 'lens yield: one item holding all five ids reads defects 1 and unique 0 on every row')
  }
  // ---- AC2: a refuted lens reads precision 0; an uncertain one reads precision null, and unverified holds it.
  r = await runReview(DIFF, buildStubs({ 'verify:': buildVerdictById((id) => (id === 1 ? 'refuted' : id === 2 ? 'uncertain' : 'confirmed')) }))
  if (checkNoThrow(r, 'lens yield mixed verdicts')) {
    const y = scanYield(r, 5) ? r.result.lensYield : []
    ck(y.length === 5 && y[0].refuted === 1 && y[0].precision === 0 && y[0].defects === 0 &&
      y[1].uncertain === 1 && y[1].unverified === 1 && y[1].precision === null && y[1].raw === 1,
      'lens yield: a refuted lens reads precision 0 and defects 0, an uncertain one unverified 1 and precision null')
  }
  // ---- AC3: a tally fault nulls defects and unique on every row; confirmed stays an integer.
  r = await runReview(DIFF, buildStubs({ synth: buildSynth(3) }))
  if (checkNoThrow(r, 'lens yield tally fault')) {
    ck(r.logs.some((l) => l.indexOf('WARNING: the synthesis item list') === 0) && scanYield(r, 5) &&
      r.result.lensYield.every((e) => e.defects === null && e.unique === null && Number.isInteger(e.confirmed)),
      'lens yield: a tally fault nulls defects and unique on every row rather than guessing a split')
  }
  // ---- AC4: a dead synthesis keeps the ledger counts and nulls the item figures; a dead lens keeps its row.
  r = await runReview(DIFF, buildStubs({ synth: null }))
  if (checkNoThrow(r, 'lens yield dead synth')) {
    ck(scanYield(r, 5) && r.result.exit === 'deferred-platform' && r.result.lensYield.every((e) => e.confirmed === 1 && e.defects === null && e.unique === null),
      'lens yield: a dead synthesis returns the ledger counts and null defects and unique')
  }
  r = await runReview(DIFF, buildStubs({ 'find:seams': null }))
  if (checkNoThrow(r, 'lens yield dead lens')) {
    ck(scanYield(r, 5) && r.result.exit === 'deferred-platform' && r.result.lensYield[2].lens === 'seams' && r.result.lensYield[2].returned === false &&
      r.result.lensYield[2].raw === 0 && r.result.lensYield[0].returned === true, 'lens yield: a dead lens keeps its row, returned false, on the deferred return')
  }
  // ---- AC5: the no-finding, every-refuted and every-lens-dead exits each carry one row per running lens.
  r = await runReview(DIFF, buildStubs({ 'find:': buildEmptyLens }))
  if (checkNoThrow(r, 'lens yield no finding')) {
    ck(scanYield(r, 5) && r.result.note === 'clean: 0 findings' && r.result.lensYield.every((e) => e.returned && e.raw === 0 && e.defects === null),
      'lens yield: the no-finding exit carries a row per lens')
  }
  r = await runReview(DIFF, buildStubs({ 'verify:': buildVerdicts('refuted') }))
  if (checkNoThrow(r, 'lens yield every refuted')) {
    ck(scanYield(r, 5) && r.result.note === 'all findings adjudicated and refuted' && r.result.lensYield.every((e) => e.refuted === 1 && e.precision === 0 && e.defects === null),
      'lens yield: the every-refuted exit carries a row per lens')
  }
  r = await runReview(DIFF, buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'lens yield every lens dead')) {
    ck(scanYield(r, 5) && r.result.lensYield.every((e) => e.returned === false && e.raw === 0 && e.confirmed === 0 && e.precision === null),
      'lens yield: the every-lens-dead exit carries a returned-false row of zeros per lens')
  }
  // ---- AC6: the spec synthesis prompt carries the block after the review-shape sentence, and the log a line per lens.
  r = await runReview(SPEC, ALL_OK)
  if (checkNoThrow(r, 'lens yield spec block')) {
    const sp = r.trace.find((t) => t.label === 'synth')
    const at = sp ? sp.prompt.indexOf('<<<LENS YIELD\n') : -1
    const end = at === -1 ? -1 : sp.prompt.indexOf('\nLENS YIELD>>>', at)
    const block = end === -1 ? '' : sp.prompt.slice(at, end)
    const keys = scanYield(r, 5) ? r.result.lensYield.map((e) => e.lens) : []
    ck(keys.length === 5 && block !== '' && sp.prompt.indexOf('precision 1.00. \n\nLENS YIELD') !== -1 &&
      keys.every((k) => block.indexOf('| ' + k + ' | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |') !== -1),
      'lens yield: the spec synthesis prompt carries the marked block, a row per running lens with its precision')
    const yl = r.logs.filter((l) => l.indexOf('lens yield: ') === 0)
    ck(yl.length === 5 && keys.every((k) => yl.some((l) => l.indexOf('lens yield: ' + k + ' returned yes') === 0 && l.indexOf('defects 1') !== -1 && l.indexOf('unique 0') !== -1)),
      'lens yield: one log line per lens names defects and unique')
  }
  // ---- AC9: a light run has no row for a skipped lens.
  r = await runReview(Object.assign({}, DIFF, { intensity: 'light' }), ALL_OK)
  if (checkNoThrow(r, 'lens yield light')) {
    ck(scanYield(r, 3) && r.result.skippedLenses.length === 2 && r.result.lensYield.every((e) => r.result.skippedLenses.indexOf(e.lens) === -1),
      'lens yield: a light run carries a row per running lens and none for a skipped one')
  }
}

// ==== TOOL-aOrientedCast-5 — `roles`, each stage spawned as the catalogue role its caller names =====
// Every arm is RED against the parent render, which reads no `roles`: no refusal fires, every stage
// keeps the `workerType` type, the posture sentences stay, the key never moves and no `role ` line is
// logged. A green arm here says the routing, the prompt variants and the key follow the argument; no
// live agent of a rendered role type is spawned, so nothing here proves the platform runs one.
async function runRolesArms() {
  const FULL = { diffFinder: 'gov-diff-reviewer', specFinder: 'gov-spec-reviewer', skeptic: 'gov-skeptic', synthesis: 'gov-synthesizer' }
  const ABSW = Object.assign({}, DIFF); delete ABSW.workerType
  const scanStage = (run, p) => run.trace.filter((t) => t.label.indexOf(p) === 0)
  const scanTypes = (run, p) => scanStage(run, p).map((t) => t.agentType)
  const checkAll = (xs, v) => xs.length > 0 && xs.every((x) => x === v)
  // ---- S1: every malformed `roles` refuses before any spawn, naming the offending key or value.
  for (const [lbl, v, named] of [['null', null, 'null'], ['an array', [], '[]'], ['a string', 'gov-skeptic', '"gov-skeptic"'],
    ['an unknown key', { finder: 'x' }, '"finder"'], ['an empty value', { skeptic: '' }, 'skeptic'], ['a value off the shape', { skeptic: '1bad' }, '"1bad"'],
    ['the none literal', { skeptic: 'none' }, '"none"'], ['a number', { skeptic: 7 }, 'Got 7'], ['a value with a space', { synthesis: 'a b' }, '"a b"']]) {
    const x = await runReview(Object.assign({}, ABSW, { roles: v }), ALL_OK)
    ck(!!x.threw && x.threw.indexOf('tier2-review: `roles`') === 0 && x.threw.indexOf(named) !== -1 && x.trace.length === 0,
      'roles: ' + lbl + ' is refused before any spawn, naming ' + named + (x.threw ? '' : ' (it proceeded)'))
  }
  let r = await runReview(Object.assign({}, ABSW, { roles: {} }), ALL_OK)
  ck(!r.threw && r.result && r.result.exit === 'complete', 'roles: an empty object proceeds' + (r.threw ? ' (threw: ' + r.threw + ')' : ''))
  // ---- S3: each stage spawns as the type its key names, and the probe as Plan when no key names it.
  r = await runReview(Object.assign({}, ABSW, { roles: FULL }), ALL_OK)
  if (checkNoThrow(r, 'roles full diff')) {
    ck(checkAll(scanTypes(r, 'find:'), 'gov-diff-reviewer') && checkAll(scanTypes(r, 'verify:'), 'gov-skeptic') &&
      checkAll(scanTypes(r, 'synth'), 'gov-synthesizer') && checkAll(scanTypes(r, 'resume:probe'), 'Plan'),
      'roles: a full diff set spawns finders, skeptics and the synthesis as their roles, and the probe as Plan')
  }
  const rsf = await runReview(Object.assign({}, SPEC, { roles: FULL }), ALL_OK)
  if (checkNoThrow(rsf, 'roles full spec'))
    ck(checkAll(scanTypes(rsf, 'find:'), 'gov-spec-reviewer') && checkAll(scanTypes(rsf, 'verify:'), 'gov-skeptic'),
      'roles: a spec audit spawns its finders as specFinder, never diffFinder')
  const rsk = await runReview(Object.assign({}, ABSW, { roles: { skeptic: 'gov-skeptic' } }), ALL_OK)
  if (checkNoThrow(rsk, 'roles skeptic only'))
    ck(checkAll(scanTypes(rsk, 'find:'), 'Plan') && checkAll(scanTypes(rsk, 'verify:'), 'gov-skeptic') && checkAll(scanTypes(rsk, 'synth'), 'general-purpose'),
      'roles: a skeptic key alone moves the skeptics; the finders keep workerType\'s Plan and the synthesis stays general-purpose')
  const rsy = await runReview(Object.assign({}, DIFF, { roles: { synthesis: 'gov-synthesizer' } }), ALL_OK)
  if (checkNoThrow(rsy, 'roles synthesis only'))
    ck(checkAll(scanTypes(rsy, 'find:'), 'general-purpose') && checkAll(scanTypes(rsy, 'verify:'), 'general-purpose') && checkAll(scanTypes(rsy, 'synth'), 'gov-synthesizer'),
      'roles: a synthesis key under workerType none moves the synthesis alone')
  // ---- S4: a roled judge makes the whole run not durable; a synthesis role does not.
  const rdf = await runReview(Object.assign({}, DIFF, { roles: { diffFinder: 'gov-diff-reviewer' } }), ALL_OK)
  if (checkNoThrow(rdf, 'roles finder only')) {
    const judges = scanStage(rdf, 'find:').concat(scanStage(rdf, 'verify:'))
    ck(judges.length === 10 && judges.every((t) => t.prompt.indexOf('Write no file') !== -1 && t.prompt.indexOf('DURABILITY') === -1),
      'roles: under a finder role, every finder and every untyped skeptic is told to write no file')
  }
  r = await runReview(Object.assign({}, DIFF, { roles: { diffFinder: 'gov-diff-reviewer' } }), buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'roles finder only, lenses dead'))
    ck(r.result.durable === false && r.result.note.indexOf('dispatches every finder and skeptic again') !== -1,
      'roles: a finder role with every lens dead returns durable false, and the note re-dispatches every judge')
  if (rsy.result) {
    const judges = scanStage(rsy, 'find:').concat(scanStage(rsy, 'verify:'))
    ck(judges.length === 10 && judges.every((t) => t.prompt.indexOf('DURABILITY') !== -1), 'roles: a synthesis role leaves every judge its DURABILITY clause')
  }
  r = await runReview(Object.assign({}, DIFF, { roles: { synthesis: 'gov-synthesizer' } }), buildStubs({ 'find:': null }))
  if (checkNoThrow(r, 'roles synthesis only, lenses dead'))
    ck(r.result.durable === true, 'roles: a synthesis role with every lens dead returns durable true')
  // ---- S5: a roled stage omits its role's posture and keeps every protocol sentence.
  const scanPosture = (run) => scanStage(run, 'find:').every((t) => t.prompt.indexOf('You are the ') === -1 && t.prompt.indexOf('No speculation, no style nits') === -1) &&
    scanStage(run, 'verify:').every((t) => t.prompt.indexOf('You are an adversarial skeptic') === -1 && t.prompt.indexOf('try hard to REFUTE') === -1)
  const scanProtocol = (run) => scanStage(run, 'verify:').length > 0 &&
    scanStage(run, 'verify:').every((t) => t.prompt.indexOf('SEVERITY RUBRIC') !== -1 && t.prompt.indexOf('WHEN YOU CANNOT ESTABLISH A FINDING') !== -1)
  if (rsf.result) {
    const full = await runReview(Object.assign({}, ABSW, { roles: FULL }), ALL_OK)
    ck(!full.threw && scanPosture(full) && scanPosture(rsf), 'roles: no roled finder or skeptic prompt restates its role\'s posture, on either kind')
    ck(!full.threw && scanProtocol(full) && scanProtocol(rsf) && scanStage(full, 'find:').length === 5 &&
      scanStage(full, 'find:').every((t) => t.prompt.indexOf('Review ONLY the diff named under SUBJECT above') !== -1 && t.prompt.indexOf('Nothing outside the diff.') !== -1) &&
      scanStage(rsf, 'find:').every((t) => t.prompt.indexOf('For EACH subject listed under SUBJECT above') !== -1 && t.prompt.indexOf('PROBE POLICY') !== -1),
      'roles: every roled prompt keeps the acquire step, the probe policy, the rubric and the cannot-establish rule')
  }
  if (rsk.result)
    ck(scanStage(rsk, 'find:').length === 5 && scanStage(rsk, 'find:').every((t) => t.prompt.indexOf('You are the ') !== -1),
      'roles: a skeptic role alone leaves every finder its identity sentence')
  // ---- S6: only a judge role joins the key, as { find, verify }.
  const deriveRolesKey = async (v) => {
    const x = await runReview(v === undefined ? DIFF : Object.assign({}, DIFF, { roles: v }), ALL_OK)
    return x.result ? x.result.key : 'threw: ' + x.threw
  }
  const kAbsent = await deriveRolesKey(undefined)
  const kEmpty = await deriveRolesKey({})
  const kSynth = await deriveRolesKey({ synthesis: 'gov-synthesizer' })
  const kOther = await deriveRolesKey({ specFinder: 'gov-spec-reviewer' })
  const kSkeptic = await deriveRolesKey({ skeptic: 'gov-skeptic' })
  const kFullA = await deriveRolesKey(FULL)
  const kFullB = await deriveRolesKey(Object.assign({}, FULL, { diffFinder: 'gov-other-reviewer' }))
  ck(kAbsent.indexOf('threw') !== 0 && kAbsent === kEmpty && kAbsent === kSynth && kAbsent === kOther,
    'roles: absent, empty, a synthesis role and the other kind\'s finder key all keep the classic key')
  ck(kSkeptic.indexOf('threw') !== 0 && kSkeptic !== kAbsent && kFullA !== kFullB && kFullA.indexOf('threw') !== 0,
    'roles: a skeptic role moves the key, and so does a different finder role')
  // ---- S7: one log line per stage on every run, naming the type and its source.
  r = await runReview(Object.assign({}, ABSW, { roles: { skeptic: 'gov-skeptic', specFinder: 'x' } }), ALL_OK)
  if (checkNoThrow(r, 'roles logs')) {
    ck(r.logs.indexOf('role find: Plan — workerType') !== -1 &&
      r.logs.some((l) => l.indexOf('role verify: gov-skeptic') === 0 && l.indexOf('roles.skeptic') !== -1) &&
      r.logs.some((l) => l.indexOf('role synthesis: ') === 0 && l.indexOf('no roles.synthesis') !== -1) &&
      r.logs.indexOf('role find: roles.specFinder is not read on a diff-review') !== -1,
      'roles: the log names each stage\'s type and source, and the other kind\'s finder key as not read')
    ck(r.logs.some((l) => l.indexOf('judges under a named type') === 0 && l.indexOf('NOT durable') !== -1) && !r.logs.some((l) => l.indexOf('worker type') === 0),
      'roles: a roled judge replaces the worker type line with the not-durable judges line')
  }
  r = await runReview(DIFF, ALL_OK)
  if (checkNoThrow(r, 'roles classic logs'))
    ck(r.logs.filter((l) => /^role (probe|find|verify|synthesis): /.test(l)).length === 4 && r.logs.indexOf('role synthesis: general-purpose — no roles.synthesis, so PLATFORM_TYPE') !== -1 &&
      r.logs.indexOf('role probe: Plan — no roles.probe, so Plan') !== -1,
      'roles: a classic run logs the four stage lines too, the probe\'s and the synthesis\'s naming their default type')
  // ---- S8: the synthesis record says the run ran under roles; a classic run's prompt carries no clause.
  const extractSynthPrompt = (run) => (scanStage(run, 'synth')[0] || { prompt: '' }).prompt
  if (rsy.result) {
    const p = extractSynthPrompt(rsy)
    ck(p.split('Roles: finders').length === 2 && p.indexOf('lens notes') !== -1 && p.indexOf('lens notes') < p.indexOf('Roles: finders'),
      'roles: a synthesis role puts one Roles clause after the lens-notes clause')
  }
  ck(extractSynthPrompt(r).length > 0 && extractSynthPrompt(r).indexOf('Roles:') === -1, 'roles: a classic run\'s synthesis prompt carries no Roles clause')
}

// ---- TOOL-dFairHearing-13: the lens catalogue and its render (AC1, AC4, AC7) ---------------------
// The lens literals are rendered from `lenses.toml` by `render_lenses.py`, both beside the harness.
// The python is the one this shell resolved, passed in, so an absent one reds these arms rather
// than skipping them. Synchronous, and ahead of the whole-script arms, so no early exit strands it.
function runLensArms() {
  const path = require('path')
  const { spawnSync } = require('child_process')
  const kit = path.dirname(FILE)
  const py = process.argv[5] || ''
  const renderer = path.join(kit, 'render_lenses.py')
  const tpl = fs.readFileSync(path.join(kit, 'tier2-review.template.js'))
  const runRender = (catalogue, input) => {
    if (!py) return { status: -1, stdout: '', stderr: 'no python was resolved' }
    const r = spawnSync(py, ['-B', renderer, catalogue], { input, encoding: 'utf8', env: Object.assign({}, process.env, { PYTHONUTF8: '1' }) })
    return { status: r.status, stdout: r.stdout || '', stderr: (r.stderr || '') + (r.error ? String(r.error) : '') }
  }
  // A literal's body: the lines between its opening line and the `]` that closes it, the marker
  // comment ignored, so the live harness and the render compare on the lens text alone.
  const extractLensBody = (text, name) => {
    const ls = text.split('\n')
    const at = ls.findIndex((l) => l.startsWith('const ' + name + ' = ['))
    const end = ls.findIndex((l, i) => i > at && l === ']')
    return at === -1 || end === -1 ? null : ls.slice(at + 1, end).join('\n')
  }
  const shipped = runRender(path.join(kit, 'lenses.toml'), tpl)
  ck(shipped.status === 0 && shipped.stdout.indexOf('{{LENS_SLOTS}}') === -1, 'lens: the shipped catalogue renders the template, every slot token filled (' + shipped.stderr.trim() + ')')
  for (const name of ['DIFF_LENSES', 'SPEC_LENSES']) {
    const want = extractLensBody(src, name)
    ck(want !== null && want.split('\n').length === 25 && extractLensBody(shipped.stdout, name) === want,
      'lens: the rendered ' + name + ' holds the live harness\'s five lenses byte for byte')
  }
  const scratch = fs.mkdtempSync(path.join(require('os').tmpdir(), 'lens-'))
  const writeCatalogue = (name, text) => { const p = path.join(scratch, name + '.toml'); fs.writeFileSync(p, text); return p }
  const optin = '\n[[lens]]\nkey = "extra-lens"\nkinds = ["diff-review", "spec-audit"]\npresets = ["unit-spec", "diff-review"]\n' +
    'default_in = []\noptin = true\nbrief = "An opt-in lens nothing selects by default."\n'
  const withOptin = runRender(writeCatalogue('optin', fs.readFileSync(path.join(kit, 'lenses.toml'), 'utf8') + optin), tpl)
  // TOOL-dFairHearing-3 - the row now renders under the opt-in marker, and still into no slot literal.
  ck(withOptin.status === 0 && shipped.status === 0 && ['DIFF_LENSES', 'SPEC_LENSES', 'DESIGN_LENSES'].every((n) =>
    extractLensBody(shipped.stdout, n) !== null && extractLensBody(withOptin.stdout, n) === extractLensBody(shipped.stdout, n)) &&
    extractLensBody(shipped.stdout, 'OPTIN_LENSES') === '' && extractLensBody(withOptin.stdout, 'OPTIN_LENSES').indexOf("key: 'extra-lens'") !== -1,
    'lens: an opt-in row added as data changes no marked literal, and renders into OPTIN_LENSES alone')
  // One scratch catalogue per refusal rule, over a two-literal template: each exits 2, writes
  // nothing, and names its rule and its subject.
  const TPL = 'const D = [ // gov:lens-slots diff-review\n{{LENS_SLOTS}}\n]\nconst S = [ // gov:lens-slots unit-spec\n{{LENS_SLOTS}}\n]\n'
  const row = (o) => '[[lens]]\n' + Object.entries(Object.assign({ key: 'k', kinds: ['diff-review'], presets: ['diff-review'],
    default_in: ['diff-review'], optin: false, brief: 'b' }, o)).filter(([, v]) => v !== undefined)
    .map(([k, v]) => k + ' = ' + JSON.stringify(v)).join('\n') + '\n'
  const SPEC = row({ key: 's', kinds: ['spec-audit'], presets: ['unit-spec'], default_in: ['unit-spec'] })
  const cases = [
    ['the parse', 'this is = = not toml\n', TPL, 'rule 1: the lens catalogue', 'is not TOML'],
    ['the field', row({ optin: undefined }) + SPEC, TPL, 'rule 2: row `k`', 'optin'],
    ['the kind set', row({ kinds: ['full-review'] }) + SPEC, TPL, 'rule 3: row `k`', 'full-review'],
    ['default_in', row({ default_in: ['unit-spec'] }) + SPEC, TPL, 'rule 4: row `k`', 'default_in'],
    ['the kind disagreement', row({ kinds: ['spec-audit'] }) + SPEC, TPL, 'rule 5: row `k`', 'kinds'],
    ['the duplicated key and literal', row({}) + row({}) + SPEC, TPL, 'rule 6:', 'key `k` and the literal diff-review'],
    ['the key equal to diff-review', row({ key: 'diff-review' }) + SPEC, TPL, 'rule 7: row `diff-review`', 'literal name'],
    ['the unknown literal', row({}) + SPEC + row({ key: 'x', kinds: ['spec-audit'], presets: ['design-audit'], default_in: [] }), TPL, 'rule 8: row `x`', 'design-audit'],
    ['the unfilled literal', row({}), TPL, 'rule 9:', 'unit-spec'],
    ['the opt-in with nowhere to go', row({ optin: true }) + SPEC, TPL, 'rule 10: row `k`', 'optin = true'],
    ['the orphan token', row({}) + SPEC, TPL + '{{LENS_SLOTS}}\n', 'rule 11:', 'without a `gov:lens-slots` marker'],
    // TOOL-dFairHearing-3 S6 - rule 11 covers the opt-in marker too.
    ['the opt-in marker with no token', row({}) + SPEC, TPL + 'const O = [ // gov:lens-optins\n]\n', 'rule 11:', 'gov:lens-optins'],
  ]
  for (const [subject, text, template, rule, word] of cases) {
    const r = runRender(writeCatalogue(subject.replace(/\W+/g, '-'), text), template)
    ck(r.status === 2 && r.stdout === '' && r.stderr.indexOf(rule) !== -1 && r.stderr.indexOf(word) !== -1,
      'lens: ' + subject + ' refuses, exit 2, naming ' + rule.replace(/:.*/, '') + ' (got ' + r.status + ': ' + r.stderr.trim() + ')')
  }
  fs.rmSync(scratch, { recursive: true, force: true })
}
runLensArms()

runWholeScriptArms().then(() => {
  console.log('---- ' + pass + ' passed, ' + fail + ' failed ----')
  process.exit(fail ? 1 : 0)
}, (e) => {
  console.log('HARNESS-BROKEN the whole-script arms threw: ' + e.message)
  console.log('---- ' + pass + ' passed, ' + (fail + 1) + ' failed ----')
  process.exit(2)
})
JSEOF

# ---- TOOL-aGraftedHelix-29 S10: the REAL checker over a range that ADDS an invariant, fed to the harness.
# A typed copy of the checker's new output would pass on the parent as well, because the harness reads
# any `- ` line as an item whatever it says (the unit's spec, section 8 F2). So this block runs the
# memory-tree kit's own gotchas.py `--for-diff` over a two-commit fixture whose second commit adds
# invariant `bd-new` beside the base's `bd-base`, both anchored on the script it edits, and the
# whole-script arms feed that stdout to the harness as `checklist`. The producer is found the way the
# parity leg finds it: the `MEMORY_TREE_DIR` override, else the sibling-kit resolver. A producer that
# cannot be resolved or run FAILS those arms and names why rather than skipping: this kit's self-tests
# ship nowhere (`kit.toml` withholds them), so the one tree that runs this suite holds that kit.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
BD_OUT="$TMP/bd-range.out"; BD_FX="$TMP/bd-fx"; bd_why=""; bd_mtd=""
bd_py=$(resolve_python 2>&1) || bd_why="no usable python: $(printf '%s\n' "$bd_py" | head -1)"
if [ -z "$bd_why" ]; then
  if [ -n "${MEMORY_TREE_DIR:-}" ]; then bd_mtd=${MEMORY_TREE_DIR%/}
  elif ! bd_mtd=$(resolve_kit_dir "$bd_py" memory-tree gotchas.py "$HERE" 2>&1); then
    bd_why="the memory-tree kit did not resolve: $bd_mtd"
  fi
  # The producer runs inside the fixture, so a repo-relative answer is made absolute here.
  case "$bd_mtd" in /*|?:[/\\]*) ;; *) bd_mtd="$ROOT/$bd_mtd" ;; esac
fi
[ -n "$bd_why" ] || [ -f "$bd_mtd/gotchas.py" ] || bd_why="'$bd_mtd/gotchas.py' is not a file"
build_bd_record() { # name · looks-wrong text -> an invariant record anchored on the fixture script
  printf -- '---\nname: %s\ndescription: a fixture invariant\nkind: invariant\ndecision: TOOL-x-1\n---\n\n## Looks wrong\n%s in `bd-fixture.sh`.\n\n## Actually\nIt is the ruling.\n\n## Do\nKeep it.\n\n## Do not\nChange it.\n\n## Guarded by\nno machine gate\n' "$1" "$2"
}
if [ -z "$bd_why" ]; then
  mkdir -p "$BD_FX/memory/gotchas"
  printf 'MEMORY_ROOT=memory\n' > "$BD_FX/.memory-tree.conf"
  printf '#!/usr/bin/env bash\necho one\n' > "$BD_FX/bd-fixture.sh"
  build_bd_record bd-base BDBASELOOKS > "$BD_FX/memory/gotchas/bd-base.md"
  ( cd "$BD_FX" && git init -q . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false && git config core.hooksPath .git/no-hooks \
      && git add -A && git commit -q -m base ) >/dev/null 2>&1 || bd_why="the fixture's base commit failed"
fi
if [ -z "$bd_why" ]; then
  printf 'echo two\n' >> "$BD_FX/bd-fixture.sh"
  build_bd_record bd-new BDNEWLOOKS > "$BD_FX/memory/gotchas/bd-new.md"
  ( cd "$BD_FX" && git add -A && git commit -q -m add ) >/dev/null 2>&1 || bd_why="the fixture's second commit failed"
fi
if [ -z "$bd_why" ]; then
  ( cd "$BD_FX" && "$bd_py" "$bd_mtd/gotchas.py" --for-diff HEAD~1..HEAD ) > "$BD_OUT" 2>&1 \
    || bd_why="gotchas.py --for-diff exited non-zero: $(head -1 "$BD_OUT")"
fi
[ -z "$bd_why" ] || printf 'PRODUCER-FAILED %s\n' "$bd_why" > "$BD_OUT"

# The lens arms (TOOL-dFairHearing-13) run the renderer with the python resolved above, or with none,
# which reds them by name rather than skipping them.
case "$bd_why" in "no usable python"*) lens_py="" ;; *) lens_py=$bd_py ;; esac

# ---- TOOL-dFairHearing-17 S5: the driver's `review_state()` and its `RUNAWAY_CEILING=` line, sliced out of the
# unattended kit beside this one and run over the parity domain, one `<priors>|<count>|<limit>|<token>` row each.
# The runner compares every row with deriveRoundState; a driver that cannot be read or sliced writes
# PRODUCER-FAILED, which reds the arm by name rather than skipping it.
RS_OUT="$TMP/review-state.out"; rs_why=""; rs_src=""
# A refusal leaves RS_DRIVER empty, so the arm below reds naming no driver rather than slicing one.
RS_DRIVER=$(resolve_kit_dir "$bd_py" unattended unattended.sh "$HERE" 2>/dev/null) && RS_DRIVER="$ROOT/$RS_DRIVER/unattended.sh" || RS_DRIVER=""
if [ ! -f "$RS_DRIVER" ]; then rs_why="the driver '$RS_DRIVER' is not a file: the unattended kit did not resolve to one"
else
  rs_src=$(tr -d '\r' < "$RS_DRIVER" | sed -n -e '/^RUNAWAY_CEILING=/p' -e '/^review_state() {/,/^}$/p')
  case "$rs_src" in RUNAWAY_CEILING=*'review_state() {'*) ;; *) rs_why="could not slice RUNAWAY_CEILING= and review_state() out of $RS_DRIVER" ;; esac
fi
if [ -z "$rs_why" ]; then
  ( eval "$rs_src" || exit 1
    for l in 1 2 3 4; do for c in 0 1 2 3; do
      printf '|%s|%s|%s\n' "$c" "$l" "$(review_state "" "$c" "$l")"
      for p1 in 0 1 2 3; do
        [ "$l" -ge 2 ] && printf '%s|%s|%s|%s\n' "$p1" "$c" "$l" "$(review_state "$p1" "$c" "$l")"
        for p2 in 0 1 2 3; do
          [ "$l" -ge 3 ] && printf '%s %s|%s|%s|%s\n' "$p1" "$p2" "$c" "$l" "$(review_state "$p1 $p2" "$c" "$l")"
          for p3 in 0 1 2 3; do
            [ "$l" -ge 4 ] && printf '%s %s %s|%s|%s|%s\n' "$p1" "$p2" "$p3" "$c" "$l" "$(review_state "$p1 $p2 $p3" "$c" "$l")"
          done
        done
      done
    done; done; exit 0 ) > "$RS_OUT" 2>&1 || rs_why="the sliced review_state() did not run: $(head -1 "$RS_OUT")"
fi
[ -z "$rs_why" ] || printf 'PRODUCER-FAILED %s\n' "$rs_why" > "$RS_OUT"
out=$(node "$TMP/run.js" "$ROOT/$FILE" "$BD_OUT" "$bd_mtd" "$lens_py" "$RS_OUT"); rc=$?
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
# RAISED 181 -> 183 by TOOL-aMendedFleet-18: 2 assertions, counted off the block — every exit's
# review-shape line at its stage (1) and the synthesis prompt carrying the complete return's line (1).
# RAISED 183 -> 188 by TOOL-aMendedFleet-111: 5 assertions, counted off the block — `durable` and the
# deferred note under an absent and a `none` workerType, for dead lenses (2) and a dead synthesis (2),
# and the synthesis-died log under the absent type (1).
# RAISED 188 -> 200 by TOOL-aMendedFleet-67: 12 assertions, counted off the block — the `workerType`
# arms whose absent-type half TOOL-aMendedFleet-93 rewrote: the default run's judges (1), the absent
# run (1), the explicit Plan run (7) and the refusal loop's one call over three values (3). Landed
# unpriced; TOOL-aMendedFleet-112 priced it, and no suite ran in that pass.
# RAISED 180 -> 186 by TOOL-aGraftedHelix-3: 6 assertions, counted off the block — the block logged and
# in RUN INTEGRITY (1), the entry as intended behaviour and never an item (1), a caller byDesign beside a
# block, logged and named (1) and under its own label (1), the count refusal (1) and the header-only
# remainder with its block of 0 (1).
# RAISED 180 -> 182 by TOOL-aEvidencedLens-1: 2 assertions, counted off the block — the retired spec
# key refused by lensNotes (1) and the five spec lenses in catalogue order (1).
# RAISED 182 -> 197 by TOOL-aEvidencedLens-2: 15 assertions, counted off the block — eleven prelude
# `spec scratch:` arms (11), the probe policy under LENS: (1), the evidence field on the spec kind only
# (1), the print moving with the rules and not with scratch (1) and the folded Windows scratch (1).
# RAISED 197 -> 205 by TOOL-aEvidencedLens-3: 8 assertions, counted off the block — the skeptic sentence
# (1), the evidence on the verify line (1), the shared probe-policy bytes (1), a kept duplicate (1), three
# orphaned duplicates (3) and the untouched diff kind (1).
# RAISED 205 -> 217 by TOOL-aEvidencedLens-4: 12 assertions, counted off the block — four prelude `fold:`
# prevBlob arms (4), the three FOLD DIFF shapes and their WARNING and count (2), the DEGRADED round (1),
# the moved and unusable blobs and the probe's hash-object ask (2), a null probe (1), a probe with no
# blobs key (1) and the key over prevBlob (1).
# RAISED 217 -> 229 by TOOL-aEvidencedLens-6: 12 assertions, counted off the block — own and shared items (2),
# mixed verdicts (1), a tally fault (1), a dead synthesis and a dead lens (2), the no-finding, every-refuted
# and every-lens-dead exits (3), the spec synthesis block and its log lines (2) and a light run (1).
# RAISED 229 -> 231 by TOOL-aEvidencedLens-12: 2 assertions, counted off the `spec evidence:` block — a
# piped one-line and two-line evidence unescaped on one line (1) and line-break-only evidence as - (1).
# RAISED 231 -> 240 by TOOL-aEvidencedLens-21: 9 assertions, counted off the block — six prelude `spec
# scratch:` arms for a relative repo, both MSYS spellings, a .. segment and two controls (6), the per-role
# scratch rule (1) and the unmoved subject beside a moved one and alone (2).
# MERGED 180 -> 260 (origin/main side): both builds raised from 180, aMendedFleet by 20 and
# aEvidencedLens by 60, so the merge carries the sum of the two raises above.
# MERGED at the second reconcile with origin/main (aGraftedHelix side): this side 186 plus main's 60
# over 180 = 246.
# RAISED 246 -> 250 by TOOL-aGraftedHelix-29: 4 assertions, counted off the block — the real checker
# ran over the fixture range (1), one invariant logged (1), bd-base as intended behaviour with no
# prompt carrying bd-new's ruling (1) and the added invariant swept as one lens's item (1).
# MERGED 240 -> 270 at the reconcile of local main into origin/main: base 240, plus aMendedFleet's 20
# (260) and aGraftedHelix's 10 (250).
# 270 -> 273, TOOL-dLadderedRemote-4: the three required-base arms, counted off a run of 273.
# RAISED 273 -> 301 by TOOL-aOrientedCast-5: 28 assertions, counted off the `roles:` block — nine
# refusals and the empty object (10), the stage routing (4), durability (4), the prompt variants (3),
# the key (2), the logs (3) and the synthesis record's Roles clause (2).
# RAISED 301 -> 314 by TOOL-aOrientedCast-10: 13 assertions, counted off the `efforts:` block — three
# refusals (3), the spec audit's routing, probe and log (5), the diff routing and log (3), the untyped
# skeptic (1) and the absent argument (1). Counted by hand, not by a run: the pass runs no suite.
# RAISED 314 -> 322 by TOOL-aOrientedCast-27: 8 assertions, counted off the `OC27` block — the whole
# labels (5) and the run's identity (3). Counted by hand, not by a run: the pass runs no suite.
# RAISED 322 -> 333 by TOOL-dTrueNorth-5: 11 assertions, counted off the `pin:` arms — eight prelude
# refusals and their control (8), the rendered binding line (1), the args header's subject fields (1)
# and the synthesis prompt's pinned line (1). Counted by hand, not by a run: the pass runs no suite.
# RAISED 333 -> 342 by TOOL-dTrueNorth-13: 9 assertions, counted off the `design:` arms — four prelude
# subject-class arms (4), the mixed binding, the subjects line and the pin over a bare first sight (3),
# the synthesis prompt's rendered Reviewed: line (1) and a whole design audit's synthesis (1). Counted
# by hand, not by a run: the pass runs no suite.
# RAISED 342 -> 343 by TOOL-dTrueNorth-20: 1 assertion, the `mark:` arm, the harness defining the function
# gen_build_index.py's AUDIT_WRITER_MARK names. Counted by hand, not by a run: the pass runs no suite.
# RAISED 343 -> 354 by TOOL-dFoldedAudit-5: 11 assertions, counted off the `address:` arms — the carried
# item (3), the three malformed items (3), the minor (1), the diff kind (3) and the render (1). Counted by
# hand, not by a run: the pass runs no suite.
# RAISED 354 -> 357 by TOOL-dFoldedAudit-15: the undeclared spec audit's three `ck` sites beside the address
# arms. Not measured by a run: the pass that wrote it runs no suite.
# RAISED 357 -> 372 by TOOL-dFairHearing-13: 15 assertions, counted off the `lens:` arms — the shipped
# render (1), its two literals against the live harness (2), the opt-in row (1) and the eleven refusal
# rules (11). Counted by hand and by a probe of the block alone: the pass runs no suite.
# RAISED 372 -> 387 by TOOL-dFairHearing-2: 15 assertions, counted off the `preset:` arms — seven prelude
# arms, three proceeding and four refusals (7), the two lens sets and the briefs (3), the key (2), the
# returns, RUN INTEGRITY and the log (2) and the default and diff returns (1). Counted by hand, not by a
# run: the pass runs no suite.
# RAISED 387 -> 410 by TOOL-dFairHearing-3: 23 assertions, counted off the `optIn:` and `pin:` arms — six
# prelude shape arms (6), the scratch render (1), the swap's finders and its return and log (2), the four
# named refusals (4), the key (1), the light swap (1), five review_pin.py prints (5) and three refusals (3).
# Counted by hand, not by a run: the pass runs no suite.
# RAISED 410 -> 411 by TOOL-dFairHearing-3's checklist follow-up: the opt-in marker's rule-11 refusal (1);
# RUN INTEGRITY's swap line joined the AC2 log arm, adding none. Counted by hand, not by a run.
# RAISED 411 -> 418 by TOOL-dFairHearing-9: 7 assertions, counted off the `lens notes:` arms — AC4's loop
# over two presets (2), AC6's loop over three refusals (3), the AC7 key (1) and the AC5 replaced-default
# note (1). Counted by hand, not by a run: the pass runs no suite.
# RAISED 418 -> 439 by TOOL-dFairHearing-4: 21 assertions, counted off the `address:`, `batchBy:` and
# `batch:` arms — seven address-key arms (7), six batchBy arms (6), five batch-order arms (5) and three
# reuse arms (3). The 25 renamed `verify:batch-<n>` references add none. Counted by hand, not by a run:
# the pass runs no suite.
# RAISED 439 -> 451 by TOOL-dFairHearing-5: 12 assertions, counted off the `merged:` block and its diff
# orphans — two diff-kind orphan arms (2), the reason form (1), per kind the merged counts, the kept
# verdict, the untouched confirmed set and the prior duplicate (8), and the diff prompt's form (1). The
# inverted diff-kind arm adds none. Counted by hand, not by a run: the pass runs no suite.
# RAISED 451 -> 460 by TOOL-dFairHearing-6: 9 assertions, counted off the `grades:` arms — the mixed item
# and the repeated id (2), the regraded id (1), the absent and the illegal grade (2), the misranked item
# (1) and the old sentence, the prompt and the schema (3). The stubs gaining `grades` add none. Counted
# by hand, not by a run: the pass runs no suite.
# RAISED 460 -> 473 by TOOL-dFairHearing-7: 13 assertions, counted off the `twins:` and `addressTwins:`
# arms — the diff and spec pairs (2), five addressTwins arms (5), the shown and default prompts (2), the
# kept and discarded flags (1), the agreeing counts (1), the off-address flag (1) and the merged duplicate
# (1). armBatchBy becoming armClosedSet adds none. Counted by hand, not by a run: the pass runs no suite.
# RAISED 473 -> 498 by TOOL-dFairHearing-11: 25 assertions, counted off the `stage:` and `twin:` arms — the
# code-reading arm and its planted copy (2), the emptied synthesis type (1), the probe's role, refusal and
# effort (3), the two type tables and durability (3), the twin refusal and its four starts (2), AC6's loop
# over four values (4), the two run ranges and counts (2), the figures and both prompts (3), the unplaced id
# (1), the key (1), the dead run-b lens (1) and two review_pin.py --twin arms (2). The six re-pinned type
# arms add none. Counted by hand, not by a run: the pass runs no suite.
# RAISED 498 -> 524 by TOOL-dFairHearing-8: 26 assertions, counted off the `fixJudge:`, `unclassed:`,
# `gateManifest:` and `dispositions:` arms — the fixJudge refusal and its three starts (2), the instance and
# class prompts and keys (2), the instance verdict under each judge (2), the unclassed refusal and its default
# (2), the gateManifest refusal, its rendered default and the no-legs run (3), the DISPOSITIONS block (1), the
# accepted set and six planted faults (7), AC8's loop over three values (3), the handed and returned appendix
# (2) and two review_pin.py --unclassed arms (2). The four re-pinned ten-column appendix arms add none.
# Counted by hand, not by a run: the pass runs no suite.
# HELD at 524 by TOOL-dFairHearing-1 S9, whose two default flips re-point arms and add none: DIFF and SPEC
# pin `addressTwins: 'hidden'` and `fixJudge: 'instance'`, the absent addressTwins arm resolves to shown,
# the twins arm's second run is the hidden one, and the fixJudge absent arms delete the pin and agree with
# class. Counted by hand, not by a run: the pass runs no suite.
# RAISED 524 -> 534 by TOOL-dFairHearing-15: 10 assertions, counted off the `FH15` arms — AC1's agent, items
# and acquired line (3), AC2 (1), AC3's loop over three outcomes (3), AC4 (1) and AC5's order and block (2).
# The re-pointed first-agent, orchestrator-type and absent-checklist arms add none. Counted by hand, not by
# a run: the pass runs no suite.
# RAISED 534 -> 564 by TOOL-dFairHearing-17: 30 assertions, counted off the `round state:` arms — AC1 to AC3's
# thirteen rule rows (13), the absent-value line (1), AC4's six refusals, the disagreeing round, the proceeding
# round and the inferred one (9), AC6's parity rows and token set (2) and AC5's stub runs (5). Counted by hand
# and by a scratch probe of the same calls, not by a run: the pass runs no suite.
# RAISED 564 -> 598 by TOOL-dFairHearing-18: 34 assertions, counted off the `walk:` arms — AC1's eleven refusals and
# the proceeding walk (12), AC2's three runs and the three-scenario deal (4), AC3's complete table, the planted
# witness and six planted defects (8), AC4's block, return, planted gap and no-finding run (4), AC5's sample,
# holds-only draw and counts (3), and AC6's walker prompts, unseeded prompts and the one WALK_RULES definition (3).
# The re-pointed unknown-preset arm adds none. Counted by hand and by scratch probes of the same calls, not by a
# run: the pass runs no suite.
# RAISED 598 -> 602 by TOOL-dFairHearing-20: 4 assertions, counted off the `walk red:` arms — AC2's complete walk (1),
# AC1's nulled return (1), AC3's round line (1) and the one walkRed definition (1). Counted by hand and by a scratch
# probe of the same calls, not by a run: the pass runs no suite.
# RAISED 602 -> 620 by TOOL-dFairHearing-23: 18 assertions, counted off the `FH23` arms — AC39's address key (1), AC40's
# three refusals and three limits (6), AC21's two ungraded items (2), AC27's three cut returns (3), AC23's reason cell
# (1) and AC22's four short lists and the whole one (5). The ACQ stub gaining its by-design head, LEGS its legCount
# and the gateManifest rename add none. Counted by hand, not by a run: the pass runs no suite.
# RAISED 620 -> 624 by TOOL-dFairHearing-27: 4 assertions, counted off the `FH27` arms — AC19's run-2 refusal and its
# run-1 control (2) and AC20's complete-walk absence and gapped-walk presence (2). The two re-labelled key-pinning
# headers add none. Counted by hand, not by a run: the pass runs no suite.
# RAISED 624 -> 626 by TOOL-dFairHearing-32: 2 assertions, the `FH32` arms — AC1's resume:probe prompt (1) and AC2's
# five section forms (1). AC11's arm reads DESIGN_RECORD_PRESET already and adds none. Counted by hand, not by a
# run: the pass runs no suite.
# RAISED 626 -> 627 by TOOL-dFairHearing-37: 1 assertion, the `FH37` arm — AC6's backslashed repo (1). Counted by
# hand and by a scratch probe of the same call, not by a run: the pass runs no suite.
# RAISED 627 -> 629 by TOOL-dFairHearing-40: 2 assertions, the `FH40` arms — AC19's spaced repo (1) and its three
# refused characters (1). The three quoted expectations it rewrites add none. Counted by hand and by a scratch
# probe of the same calls, not by a run: the pass runs no suite.
# RAISED 629 -> 638 by TOOL-dFairHearing-43: 9 assertions, the `FH43` arms — AC1's refusals and admissions (2), AC2's
# three in place of the one it moved (2 net), and AC7's four runs and its command check (5). Counted by hand and by
# scratch probes of the same calls, not by a run: the pass runs no suite.
FLOOR_ASSERTIONS=638
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

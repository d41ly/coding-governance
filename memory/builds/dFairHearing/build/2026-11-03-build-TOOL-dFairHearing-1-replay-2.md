# TOOL-dFairHearing-1 — replay 2: the verify stage's batches under `batchBy`, by the harness's own code

**Serves:** research TOOL-dFairHearing-1

Replay 2 (spec S6, §4 Batches, AC6), run in pass (a) by its deterministic probe, with no agent. Pass (b)
writes the verdict against the bar; this record holds the figures and the raw output.

## The bar

A59 joins A38 in one batch, and at least 4 of the 8 verified same-run twins meet one skeptic, under
`batchBy` `address`.

## The figures

- **Under `batchBy` `address`:** 4 of the 8 twins share a batch: B61 with B43, aGraftedHelix #8 with #14,
  aSightedSkeptic #7 with #11, and aPairedSlots #18 with #8 and #29. A59 is in batch 5 and A38 in batch 4:
  both are `[supervise]`, and the long `[supervise]` run of run A's report is cut at a batch boundary.
- **Under `batchBy` `id`:** 0 of the 8 share a batch, the research's figure
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md`).
- **Against the bar:** the count meets 4; A59 does not join A38. The figures equal the ones spec §4
  Batches records from the builder's measurement of 2026-11-03.

## How it ran

`node fh1-batches.js tools/workflows/tier2-review.js`, from the repository root at the commit that adds
this record. It slices the template's prelude the way `tier2-review.test.sh` does and runs the harness's
own `const verifyOrder` and `const batches = chunk(...)` lines verbatim, over every appendix row of the
five reports holding the 8 twins, each at its own batch count of 5, each row handed as the find stage
hands a finding: its integer id, its lens, and its ref split into `file` and `where` (spec kind) or `line`
(diff kind).

The probe's two arms differ only in `batchBy`, so the `id` arm is the liveness check AC6 names: a probe
slicing by id under both values would print 0 under both.

### fh1-batches.js

~~~~js
// Replay 2 (TOOL-dFairHearing-1 S6): the verify stage's batches under `batchBy`, by the harness's own code.
// node fh1-batches.js <tier2-review.js>   (run from the repository root; reads the five reports there)
const fs = require('fs')
const FILE = process.argv[2]
const lines = fs.readFileSync(FILE, 'utf8').split('\n')
// The prelude, sliced as tier2-review.test.sh slices it: after `meta`'s `}` to the `}` closing the base ladder.
const metaEnd = lines.findIndex((l) => l === '}')
const ladder = lines.findIndex((l) => l.startsWith('const baseLooksPinned'))
const stop = lines.findIndex((l, i) => i > ladder && l === '}') + 1
if (metaEnd === -1 || ladder === -1 || stop <= metaEnd) throw new Error('the prelude anchors moved')
const body = lines.slice(metaEnd + 1, stop).join('\n')
// The batching code, verbatim: the three lines from `const MAX_VERIFIERS` to `const batches`.
const mv = lines.findIndex((l) => l.startsWith('const MAX_VERIFIERS = '))
if (mv === -1 || !lines[mv + 1].startsWith('const verifyOrder = ') || !lines[mv + 2].startsWith('const batches = chunk('))
  throw new Error('the batching lines moved')
const batching = lines.slice(mv + 1, mv + 3).join('\n')

const SHA = 'a'.repeat(40)
const BASE = { repo: '/tmp/r', reviewDir: 'memory/reviews', unitIds: ['TOOL-x-1'], base: SHA, head: SHA, scratch: '/tmp/s' }
const SPEC = { kind: 'spec-audit', round: 1, subjects: [{ path: 'memory/builds/dX/spec/a.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 1 }] }

function readAppendix(path) {
  const text = fs.readFileSync(path, 'utf8').replace(/\r\n/g, '\n')
  const at = text.split('\n').findIndex((l) => l.trim() === '## Appendix — every finding')
  const rows = []
  let header = null
  for (const l of text.split('\n').slice(at + 1)) {
    if (!l.trim().startsWith('|')) { if (header) break; continue }
    const cells = l.trim().split(/(?<!\\)\|/).slice(1, -1).map((c) => c.trim())
    if (!header) { header = cells; continue }
    if (/^-+$/.test(cells[0])) continue
    rows.push(Object.fromEntries(header.map((h, i) => [h, cells[i]])))
  }
  const m = /(\w+|\d+) skeptic batches/i.exec(text) || /Skeptic batches:? (\d+)/i.exec(text)
  const words = { five: 5, four: 4, three: 3, two: 2, one: 1 }
  const n = m ? (words[m[1].toLowerCase()] || Number(m[1])) : null
  if (!rows.length || !n) throw new Error(path + ': no appendix rows or no batch count')
  return { rows, batches: n }
}

function measure(report, spec, batchBy) {
  const { rows, batches: n } = readAppendix(report)
  // A finding as the find stage hands it: integer id, lens, file, and the spec kind's `where` or the diff kind's `line`.
  const findings = rows.map((r) => {
    const i = r.ref.indexOf(':')
    const file = r.ref.slice(0, i)
    const rest = r.ref.slice(i + 1)
    return spec ? { id: Number(r.id), lens: r.lens, file, where: rest } : { id: Number(r.id), lens: r.lens, file, line: /^\d+/.test(rest) ? Number(/^\d+/.exec(rest)[0]) : undefined }
  })
  const src = body + '\nconst MAX_VERIFIERS = ' + n + '\nconst allFindings = __findings\n' + batching + '\nreturn batches'
  const out = new Function('args', 'log', 'parallel', 'agent', 'phase', '__findings', src)(
    Object.assign({}, BASE, spec ? SPEC : {}, { batchBy }), () => {}, null, null, null, findings)
  const where = new Map()
  out.forEach((g, b) => g.forEach((f) => where.set(f.id, b)))
  return { n, count: findings.length, where }
}

const R = 'memory/builds/'
const TWINS = [
  ['runtime-a', R + 'dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md', true, [[59, [38]]]],
  ['runtime-b', R + 'dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md', true, [[61, [43]]]],
  ['aGraftedHelix-1 closing', R + 'aGraftedHelix/reviews/2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md', false, [[8, [14]], [24, [14]]]],
  ['aSightedSkeptic closing', R + 'aSightedSkeptic/reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md', false, [[10, [5, 21]], [7, [11]]]],
  ['aPairedSlots-1-9', R + 'aPairedSlots/reviews/2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md', false, [[18, [8, 29]], [21, [7]]]],
]
for (const batchBy of ['id', 'address']) {
  let met = 0
  let total = 0
  console.log('== batchBy ' + batchBy)
  for (const [label, path, spec, twins] of TWINS) {
    const { n, count, where } = measure(path, spec, batchBy)
    for (const [refuted, confirmed] of twins) {
      total++
      const joined = confirmed.filter((c) => where.get(c) === where.get(refuted))
      if (joined.length) met++
      console.log(`${label} (${count} findings, ${n} batches): refuted #${refuted} in batch ${where.get(refuted) + 1}; ` +
        confirmed.map((c) => `#${c} in batch ${where.get(c) + 1}`).join(', ') + ` -> ${joined.length ? 'MEETS #' + joined.join(', #') : 'apart'}`)
    }
  }
  console.log(`twins meeting one skeptic under ${batchBy}: ${met} of ${total}`)
}
~~~~

### Output: node fh1-batches.js tools/workflows/tier2-review.js

~~~~text
== batchBy id
runtime-a (60 findings, 5 batches): refuted #59 in batch 5; #38 in batch 4 -> apart
runtime-b (61 findings, 5 batches): refuted #61 in batch 5; #43 in batch 4 -> apart
aGraftedHelix-1 closing (28 findings, 5 batches): refuted #8 in batch 2; #14 in batch 3 -> apart
aGraftedHelix-1 closing (28 findings, 5 batches): refuted #24 in batch 4; #14 in batch 3 -> apart
aSightedSkeptic closing (22 findings, 5 batches): refuted #10 in batch 2; #5 in batch 1, #21 in batch 5 -> apart
aSightedSkeptic closing (22 findings, 5 batches): refuted #7 in batch 2; #11 in batch 3 -> apart
aPairedSlots-1-9 (38 findings, 5 batches): refuted #18 in batch 3; #8 in batch 1, #29 in batch 4 -> apart
aPairedSlots-1-9 (38 findings, 5 batches): refuted #21 in batch 3; #7 in batch 1 -> apart
twins meeting one skeptic under id: 0 of 8
== batchBy address
runtime-a (60 findings, 5 batches): refuted #59 in batch 5; #38 in batch 4 -> apart
runtime-b (61 findings, 5 batches): refuted #61 in batch 4; #43 in batch 4 -> MEETS #43
aGraftedHelix-1 closing (28 findings, 5 batches): refuted #8 in batch 1; #14 in batch 1 -> MEETS #14
aGraftedHelix-1 closing (28 findings, 5 batches): refuted #24 in batch 2; #14 in batch 1 -> apart
aSightedSkeptic closing (22 findings, 5 batches): refuted #10 in batch 2; #5 in batch 1, #21 in batch 1 -> apart
aSightedSkeptic closing (22 findings, 5 batches): refuted #7 in batch 4; #11 in batch 4 -> MEETS #11
aPairedSlots-1-9 (38 findings, 5 batches): refuted #18 in batch 4; #8 in batch 4, #29 in batch 4 -> MEETS #8, #29
aPairedSlots-1-9 (38 findings, 5 batches): refuted #21 in batch 2; #7 in batch 1 -> apart
twins meeting one skeptic under address: 4 of 8
~~~~

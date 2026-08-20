export const meta = {
  name: 'drift-audit-code',
  version: '1.5',
  description:
    'Drift audit Tier 2, wave 1: dead / inefficient / unwired / duplicated code + instrument integrity. Project-agnostic; all repo facts arrive via args.',
  whenToUse:
    'After Tier 0 (drift_report.py) and only when the question is about CODE rather than records. Run wave 1 and wave 2 sequentially, never together — the concurrency cap is fleet-wide.',
  phases: [
    { title: 'Find', detail: '5 primed lenses over the whole repo, bounded fan-out' },
    { title: 'Verify', detail: 'batched default-refute skeptics, keyed by integer index' },
    { title: 'Synthesize', detail: 'one pass -> report file' },
  ],
}

// gov:kit drift-audit@1.5
// --- bounded fan-out (inlined; workflow scripts cannot import) ------------
// The cap is on CONCURRENCY *and*, for the verify stage, on TOTAL agents. Concurrency is not a
// budget: N findings fanned one-skeptic-each still spawn N agents, five at a time.
// BOTH ARE BARE LITERALS AND NEITHER IS CALLER-SETTABLE. The retired form bound each of them from
// an `<expr> || 5` fallback, which read as a constant to the guard and as a knob to the runtime — so
// a caller raised this harness's own agent count past the cap with every gate green. agent-cap.js
// now RESOLVES the bound and refuses that binder form outright. (The spelling itself is paraphrased
// here on purpose: the acceptance grep for it is repo-wide and would match the comment explaining it.)
const CAP = 5
async function boundedParallel(thunks, cap = CAP) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
function chunk(a, n) {
  const out = []
  for (let i = 0; i < a.length; i += n) out.push(a.slice(i, i + n))
  return out
}

// --- inputs (via Workflow `args`) ----------------------------------------
// {
//   repo: "/c/projects/<repo>",            // forward slashes
//   base: "<immutable SHA>",               // what "ships" means
//   outDir: "<repo>/memory/.../reviews",   // where lens writeups + the report land
//   stack: "one paragraph: languages, frameworks, layout, entrypoints",
//   productGlobs: ["src", "packages"],     // what counts as product source
//   frameworkExports: "which exports a framework references by convention, not by import",
//   measured: "the Tier-0 numbers already established — agents must interrogate, not re-derive",
//   byDesign: "recorded/backlogged issues reviewers must NOT re-report as new",
// }
const a = args || {}
const REPO = a.repo || '.'
const BASE = a.base || 'HEAD'
const OUT = a.outDir || `${REPO}/memory`
const MAX_VERIFIERS = 5

const COMMON = `
You are auditing the repo at ${REPO}. Treat ${BASE} as "what ships".

STACK: ${a.stack || 'not supplied — infer it from the tree before you start, and say what you inferred.'}

PRODUCT SOURCE: ${(a.productGlobs || ['(not supplied — infer it)']).join(', ')}

SCOPE: the WHOLE repo at ${BASE}, not a diff. Ignore vendored/submodule trees — they have their own
records and their own drift.

MEASURED BASELINES (already established; do not re-derive, DO interrogate — a number that cannot move
is the failure mode this audit exists to catch):
${a.measured || '(none supplied — establish your own and show the command that produced each)'}

ALREADY KNOWN — DO NOT RE-REPORT AS NEW. You MAY report that one is still live, got worse, or that
its recorded description is now wrong:
${a.byDesign || '(none supplied — assume nothing is known and expect a lower precision)'}

EVIDENCE RULES (these decide whether your finding survives the skeptic):
- Every finding needs a real path:line you actually read. Forward slashes only, never backslashes.
- "Dead"/"unused" requires that you ACTUALLY searched for consumers across ALL of: direct imports,
  re-exports through barrels/index files, dynamic imports, framework file-convention exports,
  string-keyed registries, generated artifacts, decorators/annotations that register a symbol at
  import time, CLI entrypoints, tests, and fixture/seed data. Say WHICH searches you ran. An
  unsearched claim will be refuted.
  Framework-referenced exports in this repo: ${a.frameworkExports || '(not supplied — determine them yourself and list them)'}
- Prefer few high-confidence findings over many speculative ones. Precision is the metric.
- Severity: blocker = breaks a merge-bar gate or ships a live defect; high = real user-visible or
  data-integrity impact; medium = real debt with a concrete cost; low = tidy-up.

OUTPUT: Write your full prose writeup (evidence, commands run, per-finding detail) to
${OUT}/wave1-<yourLensSlug>.md and return ONLY the structured object. Keep each structured field
under ~300 chars; long detail belongs in the file.
Required keys on the returned object: lens, path, summary, findings.
Each finding requires: file, line, severity, claim, impact, fix.
`

const FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'path', 'summary', 'findings'],
  properties: {
    lens: { type: 'string' },
    path: { type: 'string' },
    summary: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['file', 'line', 'severity', 'claim', 'impact', 'fix'],
        properties: {
          file: { type: 'string' },
          line: { type: 'integer' },
          severity: { type: 'string', enum: ['blocker', 'high', 'medium', 'low'] },
          claim: { type: 'string' },
          impact: { type: 'string' },
          fix: { type: 'string' },
        },
      },
    },
  },
}

const LENSES = [
  {
    slug: 'dead-code',
    label: 'find:dead-code',
    brief: `LENS 1 — DEAD CODE, trustworthy this time.
Any fan-in / unused-export metric this repo reports is a HINT computed from a symbol table, and it is
wrong in BOTH directions. Turn it into a list someone can act on.
First read whatever computes it and learn exactly what it structurally cannot see. Then produce:
 (a) FALSE POSITIVES: classes of symbol the number wrongly includes, with counts and examples. If a
     large fraction is framework-referenced, the number is decorative and THAT is the finding.
 (b) TRUE DEAD CODE you verified has no consumer by exhaustive search. Whole dead FILES and dead
     FEATURES are worth far more than dead one-line exports.
Also hunt what a fan-in metric cannot see at all: branches behind a flag that no longer exists,
retired-feature tombstones still carrying live paths, modules kept alive only by their own tests, and
schema/migrations for columns nothing reads.`,
  },
  {
    slug: 'unwired',
    label: 'find:unwired',
    brief: `LENS 2 — UNWIRED FUNCTIONALITY (built, shipped, never reachable).
Hunt end-to-end reachability gaps in BOTH directions:
 - an endpoint/handler with no caller in any client, CLI, or automation surface;
 - a service function no adapter reaches;
 - a tool/command registered but unreachable, or gated by a flag nothing can set;
 - a feature flag or setting that gates nothing, or whose gate is unreachable;
 - a registered unit (block/plugin/component) missing from one of the several places registration
   requires — enumerate ALL of them for this repo and check every unit against every place;
 - a stored field written but never read, or read but never written;
 - a screen with no navigation entry, or a route nothing links to;
 - a docs page describing a control that does not exist — name the control a reader would click;
 - the inverse: a shipped user-facing capability with no docs page at all.
This class has a documented shape: computed -> serialized -> passed -> never read. The docs face of it
is a page promising a capability whose service, endpoint and client all exist while NO UI calls any.`,
  },
  {
    slug: 'duplication',
    label: 'find:duplication',
    brief: `LENS 3 — duplication and reinvention beyond whatever is already recorded.
Clone detectors catch verbatim copies. The MODAL reinvention class is semantic near-duplication and
ORCHESTRATION duplication — differently-strung calls to the same primitives — which no clone detector
and no name-keyed index can see. Leaf helpers get reused well; what stays duplicated is the
orchestration stringing them together.
So do NOT just run a clone detector.
 - Identify this repo's high-fan-in seams, then ask of each: does a second implementation of this
   BEHAVIOUR exist that does not wire through the seam?
 - Concentrate where orchestration lives: service-layer flows, tool/command bodies, CRUD page
   composition, router preludes (error/permission/flag handling), install/seed loops, fetch wrappers.
 - Report duplication that has DRIFTED (the copies now disagree) at HIGHER severity than duplication
   that is merely repeated. Drift is a live bug; repetition is debt.`,
  },
  {
    slug: 'inefficient',
    label: 'find:inefficient',
    brief: `LENS 4 — INEFFICIENT code, on paths that actually run.
 - N+1 queries and per-row awaits, especially on list/index paths;
 - blocking synchronous work on an async event loop (DNS, sockets, file IO, subprocess, crypto);
 - an index that cannot serve its query — an inequality-led composite or wrong column order cannot
   seek or sort; read the migrations AND the query sites;
 - unbounded queries with no limit on a surface that grows;
 - render-path waste: a component defined inside a render body (new type per parent render, remount
   per keystroke), missing memoization on an expensive list, effects that refetch every render,
   client bundles pulling in code meant to stay server-side or editor-only;
 - the gate suite itself: is any leg redundant, vacuous, or pathologically slow for what it proves?
Prefer measured or clearly-reasoned impact over "this looks slow". An unmeasured perf claim will be
downgraded, and rightly.`,
  },
  {
    slug: 'instruments',
    label: 'find:instrument-integrity',
    brief: `LENS 5 — ARE THE INSTRUMENTS LYING? (the highest-value lens — be ruthless)
The reason anyone commissions this audit is that state feels uncertain. Gates and metrics that report
green or zero while BLIND are how that happens, and they are invisible by construction.
Known shapes of this failure, all observed in real repos:
 - a gate comparing two values neither of which is what ships (e.g. two tokens while the painted
   surface is translucent), whose empty offender list reads as all-clear;
 - a --check freshness gate that is vacuous because the generator's correct output is always
   "unchanged";
 - a test that runs in NEITHER CI leg because it opts into a resource outside the marker mechanism;
 - an assertion whose two operands come from the same generator run;
 - a metric structurally pinned at zero, whose zero reads as "converged";
 - a review harness whose verdict lookup never matches, reporting precision 0.00 as a clean bill.
Targets:
 1. For EVERY number this repo reports about itself, determine whether it CAN move. Try to make it
    move: construct the minimal input it should flag and check that it flags it. A number that cannot
    move is a blocker-class finding regardless of how reassuring it looks.
 2. For every gate leg: can it fail? Is any leg scope-gated so it never runs where the work happens?
    Is any assertion vacuous?
 3. Are any exemption/baseline lists being used to silence real findings rather than sanctioned ones?
    How large are they, and when did each last shrink?
 4. Is the gate suite's own declared leg set the same as what CI actually runs?
Demonstrate, do not assert — run the tool and show the output for every claim.`,
  },
]

phase('Find')
const finderResults = await boundedParallel(
  LENSES.map((L) => () =>
    agent(`${COMMON}\n\n${L.brief}`, { label: L.label, phase: 'Find', schema: FINDING_SCHEMA })
  ),
  CAP
)

const lensOut = finderResults.filter(Boolean)
// Orchestrator-assigned INTEGER index — the verdict join key. A model can echo a small integer
// reliably; it cannot echo "file.py:1234 — long claim text" byte-identically, and every miss
// silently became "refuted" in the ref-keyed harness this replaces.
const indexed = []
lensOut.forEach((r) => {
  ;(r.findings || []).forEach((f) => indexed.push({ id: indexed.length + 1, lens: r.lens, ...f }))
})
log(`Find: ${lensOut.length}/${LENSES.length} lenses returned, ${indexed.length} raw findings`)

const VERDICT_SCHEMA = {
  type: 'object',
  required: ['verdicts'],
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'verdict', 'reason'],
        properties: {
          id: { type: 'integer' },
          verdict: { type: 'string', enum: ['confirmed', 'refuted', 'partial'] },
          reason: { type: 'string' },
          severityCorrection: { type: 'string' },
        },
      },
    },
  },
}

phase('Verify')
// <= MAX_VERIFIERS agents TOTAL. Batch size grows with the finding count; agent count never does.
const batches = indexed.length ? chunk(indexed, Math.ceil(indexed.length / MAX_VERIFIERS)) : [] // gov:fixed-verifiers
const verdictBatches = await boundedParallel(
  batches.map((b, bi) => () =>
    agent(
      `You are a DEFAULT-REFUTE skeptic auditing findings from a whole-repo drift audit of ${REPO}
(ships at ${BASE}). Your job is to REFUTE. Assume each finding is wrong until its evidence forces you
to agree. Open the cited file:line yourself and run the searches the finder claims to have run.

Refute when ANY of these hold:
- the cited file:line does not say what the finding claims;
- a consumer/caller/reference DOES exist that the finder missed — check barrels, re-exports, dynamic
  imports, framework file conventions, string-keyed registries, generated artifacts, decorators, CLI
  entrypoints, tests and seed data;
- the "duplication" is a sanctioned or justified twin rather than reinvention;
- the claim is already recorded/backlogged and adds nothing new;
- the impact does not follow even if the fact is true (debt asserted as a live defect);
- the finding is speculative, unmeasured, or an aesthetic preference.
Mark "partial" when the underlying fact is real but severity or impact is overstated, and give the
corrected severity in severityCorrection.

Return ONE verdict per id below. Required keys: id (integer), verdict
(confirmed|refuted|partial), reason. Optional: severityCorrection.
Echo the id EXACTLY as an integer. Return every id in this batch, even if unsure — if you cannot
reach a judgement use "partial" and say why. Do not invent ids not in this batch.

ALREADY KNOWN (a finding that merely restates one of these is refuted):
${a.byDesign || '(none supplied)'}

FINDINGS BATCH ${bi + 1}:
${JSON.stringify(b, null, 1)}`,
      { label: `verify:batch${bi + 1}`, phase: 'Verify', schema: VERDICT_SCHEMA }
    )
  ),
  CAP
)

const vmap = new Map()
verdictBatches.filter(Boolean).forEach((vb) => {
  ;(vb.verdicts || []).forEach((v) => {
    if (typeof v.id === 'number' && !vmap.has(v.id)) vmap.set(v.id, v)
  })
})
// A finding with NO verdict is UNVERIFIED, never refuted. Two prior runs reported a hard zero
// because the join matched nothing, and a hard zero reads as a clean bill of health.
const judged = indexed.map((f) => {
  const v = vmap.get(f.id)
  return {
    ...f,
    verdict: v ? v.verdict : 'unverified',
    reason: v ? v.reason : 'no verdict returned',
    severityCorrection: v && v.severityCorrection,
  }
})
const confirmed = judged.filter((f) => f.verdict === 'confirmed')
const partial = judged.filter((f) => f.verdict === 'partial')
const refuted = judged.filter((f) => f.verdict === 'refuted')
const unverified = judged.filter((f) => f.verdict === 'unverified')
const precision =
  confirmed.length + refuted.length ? confirmed.length / (confirmed.length + refuted.length) : null
const downgrades = judged.filter((f) => f.verdict === 'partial' && f.severityCorrection).length
log(
  `Verify: ${confirmed.length} confirmed, ${partial.length} partial, ${refuted.length} refuted, ` +
    `${unverified.length} UNVERIFIED, precision ${precision === null ? 'n/a' : precision.toFixed(2)}`
)

phase('Synthesize')
const synth = await agent(
  `Synthesize a whole-repo code-drift audit of ${REPO} (ships at ${BASE}) into ONE report at
${OUT}/drift-audit-wave1-code.md.

The commissioning question was: is the build drifting — is there dead or inefficient code, unwired
functionality, duplicate or reinvented functionality?

Write it so a tired reader has the answer in the first ten lines. Structure:
1. Verdict up front: is there drift, how much, and what is the single worst thing.
2. Severity-ordered table of CONFIRMED findings (id, severity, file:line, one-line claim).
3. PARTIAL findings, with the corrected severity beside the original.
4. UNVERIFIED findings listed explicitly — NOT refuted, NOT cleared. State plainly that no skeptic
   reached them. If the count is zero, say so and say why that is positive evidence.
5. Refuted findings, one line each, so the reader knows what was checked and dismissed.
6. Instrument integrity — a dedicated section on whether this repo's own drift metrics can be
   trusted. If a metric cannot move or a gate cannot fail, say so loudly and early.
7. Cross-cutting themes: what the findings say collectively about HOW drift enters this codebase —
   the mechanism, not the instances.
8. A prioritized do-this-next list, cheapest-high-value first, each item naming the file to touch.

Rules: every claim keeps its file:line. Do not soften or round. Do not invent findings not in the
data. Report precision and the raw/confirmed/partial/refuted/unverified counts honestly, and state
the correction DIRECTION beside precision — precision 1.00 with zero refutations means nothing was
fabricated, not that the severities were right. Where findings contradict each other, say so rather
than silently picking one.

Return {path, summary} only — the prose goes in the file. Forward slashes in the path.

DATA:
counts: raw ${indexed.length}, confirmed ${confirmed.length}, partial ${partial.length}, refuted ${refuted.length}, unverified ${unverified.length}, precision ${precision === null ? 'n/a' : precision.toFixed(2)}, severity corrections ${downgrades}
lens writeups: ${JSON.stringify(lensOut.map((r) => ({ lens: r.lens, path: r.path, summary: r.summary })), null, 1)}
judged findings: ${JSON.stringify(judged, null, 1)}`,
  {
    label: 'synth:code-drift',
    phase: 'Synthesize',
    schema: {
      type: 'object',
      required: ['path', 'summary'],
      properties: { path: { type: 'string' }, summary: { type: 'string' } },
    },
  }
)

return {
  wave: 'code-drift',
  counts: {
    raw: indexed.length,
    confirmed: confirmed.length,
    partial: partial.length,
    refuted: refuted.length,
    unverified: unverified.length,
  },
  precision,
  severityCorrections: downgrades,
  report: synth && synth.path,
  summary: synth && synth.summary,
  confirmedTop: confirmed
    .filter((f) => f.severity === 'blocker' || f.severity === 'high')
    .map((f) => `[${f.severity}] ${f.file}:${f.line} — ${f.claim}`),
  unverifiedList: unverified.map((f) => `${f.file}:${f.line} — ${f.claim}`),
}

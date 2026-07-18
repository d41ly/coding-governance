export const meta = {
  name: 'tier2-review',
  version: '1.0', // gov:kit tier2-review@1.0 — engine identity (deployed verbatim; this field is the deployer's version marker)
  description:
    'Consolidated, concurrency-capped (≤6) Tier-2 adversarial review: find → batched-verify → synth. Replaces the big-fan-out review that trips the server rate limiter. Project-agnostic — parameterize via `args`.',
  phases: [
    { title: 'Find', detail: '4 finder lenses, one wave, ≤6 concurrent' },
    { title: 'Verify', detail: 'skeptics refute findings in BATCHES, ≤6 concurrent' },
    { title: 'Synthesize', detail: 'one pass → report file' },
  ],
}

// --- cap-6 fan-out (inlined; workflow scripts can't import) --------------
// Passes agent-cap: the only raw primitive call is the marked helper line.
async function boundedParallel(thunks, cap = 6) {
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

// --- inputs (via Workflow `args`) ---------------------------------------
// { base: "<immutable SHA>", head: "HEAD", repo: "/path/to/worktree",
//   context: "what this diff does + the security model + what's by-design",
//   byDesign: "known/tracked issues reviewers must NOT re-report",
//   reviewDir: "where synth writes the report (repo-relative)" }
const a = args || {}
const base = a.base || 'origin/main'
const head = a.head || 'HEAD'
const repo = a.repo || '.'
const context = a.context || 'the cumulative diff landing on main'
const byDesign = a.byDesign || 'none supplied'
const reviewDir = a.reviewDir || 'reviews/'
const diffCmd = `git -C ${repo} diff ${base}...${head}`

const FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'findings'],
  properties: {
    lens: { type: 'string' },
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

const VERDICT_SCHEMA = {
  type: 'object',
  required: ['verdicts'],
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        required: ['ref', 'verdict', 'reason'],
        properties: {
          ref: { type: 'string' }, // "file:line"
          verdict: { type: 'string', enum: ['confirmed', 'refuted'] },
          reason: { type: 'string' },
        },
      },
    },
  },
}

// --- Phase 1: FIND — 4 consolidated lenses, ONE ≤6-wide wave ------------
phase('Find')
const LENSES = [
  {
    key: 'security',
    brief:
      'Security + data-integrity: auth/RBAC gaps, sanitization/SSRF/egress, injection, secrets on the wrong surface, optimistic-concurrency clobbers, check-then-mutate races.',
  },
  {
    key: 'correctness',
    brief:
      'Correctness: logic bugs, wrong conditionals/edge cases, client/server validation divergence, error/empty/loading states, off-by-one, coercion drift.',
  },
  {
    key: 'seams',
    brief:
      'Integration seams + dead plumbing: values computed→passed→never read, stale caches not reset on every mutation path, indexes that don\'t serve their query, half-applied merges, cross-language catalog drift.',
  },
  {
    key: 'regressions',
    brief:
      'Recurring-bug-class sweep: run the PROJECT\'s recurring-bug-classes checklist against the diff and report only fresh hits.',
  },
]

const finderResults = await boundedParallel(
  LENSES.map((L) => () =>
    agent(
      `You are the ${L.key} reviewer. Review ONLY this diff (run \`${diffCmd}\`, then Read/Grep the touched files + their immediate callers):\n\n` +
        `CONTEXT: ${context}\n` +
        `BY DESIGN (do NOT re-report these): ${byDesign}\n\n` +
        `LENS: ${L.brief}\n\n` +
        `Emit CONCRETE findings only — each needs file, line, severity (blocker|high|medium|low), a one-line claim, the impact, and a proposed fix. No speculation, no style nits, nothing outside the diff. If nothing real, return findings: [].\n` +
        `Return JSON {lens:"${L.key}", findings:[{file,line,severity,claim,impact,fix}]}.`,
      { label: `find:${L.key}`, phase: 'Find', schema: FINDING_SCHEMA },
    ),
  ),
)

const allFindings = finderResults
  .filter(Boolean)
  .flatMap((r) => (r.findings || []).map((f) => ({ ...f, ref: `${f.file}:${f.line}` })))

if (allFindings.length === 0) {
  log('No findings from any lens — nothing to verify.')
  return { confirmed: [], report: null, note: 'clean: 0 findings' }
}
log(`${allFindings.length} raw findings across ${LENSES.length} lenses — verifying in batches.`)

// --- Phase 2: VERIFY — batched skeptics (NOT one agent per finding) -----
phase('Verify')
const BATCH = 5 // findings per skeptic — consolidation: ceil(N/5) agents, not 2N
const batches = chunk(allFindings, BATCH)

const verdictResults = await boundedParallel(
  batches.map((group, gi) => () =>
    agent(
      `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate). Default to refuted when uncertain.\n\n` +
        `Findings to judge:\n` +
        group
          .map((f, i) => `${i + 1}. [${f.severity}] ${f.ref} — ${f.claim} | impact: ${f.impact}`)
          .join('\n') +
        `\n\nReturn JSON {verdicts:[{ref:"file:line", verdict:"confirmed"|"refuted", reason}]} — one verdict per finding above, ref copied EXACTLY.`,
      { label: `verify:batch${gi + 1}`, phase: 'Verify', schema: VERDICT_SCHEMA },
    ),
  ),
)

const verdictByRef = {}
for (const r of verdictResults.filter(Boolean))
  for (const v of r.verdicts || []) verdictByRef[v.ref] = v

const confirmed = allFindings.filter((f) => verdictByRef[f.ref]?.verdict === 'confirmed')
const refuted = allFindings.length - confirmed.length
const precision = allFindings.length ? confirmed.length / allFindings.length : 0
log(
  `confirmed ${confirmed.length} / refuted ${refuted} — precision ${precision.toFixed(2)}` +
    (precision < 0.5 ? ' (below 0.5 — tighten scope/priming next time, don\'t add agents)' : ''),
)

if (confirmed.length === 0)
  return { confirmed: [], report: null, precision, note: 'all findings refuted' }

// --- Phase 3: SYNTHESIZE — one agent writes the report ------------------
phase('Synthesize')
const synth = await agent(
  `Write the Tier-2 review report for: ${context}\n\n` +
    `Confirmed findings (skeptic-survived):\n` +
    confirmed
      .map(
        (f) =>
          `- [${f.severity}] ${f.ref} — ${f.claim}\n  impact: ${f.impact}\n  fix: ${f.fix}\n  why-real: ${verdictByRef[f.ref]?.reason || ''}`,
      )
      .join('\n') +
    `\n\nWrite a markdown report (severity-ranked, blockers first, each with file:line + fix + a left-shift gate suggestion) to a file under ${repo}/${reviewDir}. ` +
    `Return JSON {path, blockers, highs, summary} with a FORWARD-SLASH path.`,
  {
    label: 'synth',
    phase: 'Synthesize',
    schema: {
      type: 'object',
      required: ['path', 'summary'],
      properties: {
        path: { type: 'string' },
        blockers: { type: 'integer' },
        highs: { type: 'integer' },
        summary: { type: 'string' },
      },
    },
  },
)

return {
  confirmed: confirmed.length,
  refuted,
  precision,
  agents: LENSES.length + batches.length + 1, // finders + batched skeptics + synth
  report: synth?.path || null,
  summary: synth?.summary || '',
}

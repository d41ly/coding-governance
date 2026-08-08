export const meta = {
  name: 'tier2-review',
  version: '1.2', // gov:kit tier2-review@1.2 — engine identity (deployed verbatim; this field is the deployer's version marker)
  description:
    'Consolidated, concurrency-capped (≤5) Tier-2 adversarial review, ≤5 verify agents TOTAL: find → batched-verify → synth, joined on an ORCHESTRATOR-ASSIGNED INTEGER id. Replaces the big-fan-out review that trips the server rate limiter. Project-agnostic — parameterize via `args`.',
  phases: [
    { title: 'Find', detail: '4 finder lenses, one wave, ≤5 concurrent' },
    { title: 'Verify', detail: 'skeptics refute findings in ≤5 BATCHES — agent count fixed' },
    { title: 'Synthesize', detail: 'one pass → report file' },
  ],
}

// --- cap-5 fan-out (inlined; workflow scripts can't import) --------------
// Passes agent-cap: the only raw primitive call is the marked helper line.
async function boundedParallel(thunks, cap = 5) {
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
// S5 (TOOL-aGuardedTally-1): args MUST be a structured object. Passing a prose string used to
// degrade silently to `repo = '.'`, i.e. "review whatever directory this process happens to be
// standing in" -- which twice made this harness audit a DIFFERENT repository than the one it was
// briefed on, and return confident, well-evidenced findings about code nobody asked about. A dead
// review returns nothing; a misdirected one returns something worse. Refuse instead of guessing.
// The Workflow tool delivers `args` as a STRING even when the caller hands it JSON, so parse first
// and validate second. The first cut of this guard tested `typeof a !== 'object'` and therefore
// refused every legitimate caller -- the same defect one level up: asserting on the shape I assumed
// instead of the shape that actually arrives, and never observing the guard's PASSING case.
let cfg = args
if (typeof cfg === 'string') {
  try {
    cfg = JSON.parse(cfg)
  } catch (e) {
    throw new Error(
      'tier2-review: args must be JSON carrying an explicit `repo`; could not parse the string ' +
        'given (' + e.message + '). Refusing to default the review root to the process cwd — ' +
        'that is how this harness reviewed the wrong repository twice.',
    )
  }
}
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg) || !cfg.repo) {
  throw new Error(
    'tier2-review: args must carry an explicit `repo`. Got ' +
      (Array.isArray(cfg) ? 'array' : typeof cfg) +
      '. Refusing to default the review root to the process cwd — that is how this harness ' +
      'reviewed the wrong repository twice.',
  )
}
// H2/AC5: requiring a root is not verifying one. Prove it resolves to a real git worktree before a
// single agent spawns, so a typo'd or stale path fails in milliseconds instead of producing a
// confident review of an empty diff.
const a = cfg
const base = a.base || 'origin/main'
const head = a.head || 'HEAD'
const repo = a.repo || '.'
const context = a.context || 'the cumulative diff landing on main'
const byDesign = a.byDesign || 'none supplied'
const reviewDir = a.reviewDir || 'reviews/'
const diffCmd = `git -C ${repo} diff ${base}...${head}`
// H2/AC5, HONEST LIMIT: the harness CANNOT verify its own root. Workflow scripts have no
// filesystem and no Node/Bun API, so there is no way to prove `repo` resolves to a git worktree
// from in here — a probe was written, then removed rather than shipped unverified. What it can do
// is make the given root impossible to miss: logged before any agent spawns, injected into the
// synth prompt, and returned on every exit path. Verifying it belongs to the CALLER.
log(`review root (unverified — see note): ${repo} — diff ${base}...${head}`)

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

// U6 (TOOL-aFoldedQuarry-2): the join key is an INTEGER the ORCHESTRATOR assigns, never a string the
// skeptic reproduces. Two defects died with the old `ref` key. (a) Echo drift — a re-wrapped path, a
// re-derived line number or a trailing space missed the join, and the finding fell out of the count.
// (b) COLLISION — two findings at one file:line are entirely normal when two lenses read the same
// function, and a plain `map[v.ref] = v` collapsed them so BOTH inherited whichever verdict landed
// last. A model can echo a small integer reliably; it cannot re-type a path byte-identically, and an
// integer cannot collide with another finding's.
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
          id: { type: 'integer' }, // the orchestrator-assigned finding id, echoed back
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

// S1 (TOOL-aGuardedTally-1): a dead lens returns null and filter(Boolean) drops it silently, so an
// all-dead run used to be indistinguishable from an all-clean one. Observed live: a review returned
// `clean: 0 findings` with agents_done 0, four ENOTFOUND errors, and a journal of four `started`
// lines and zero `result` lines. Count what actually came back and never call absence cleanliness.
const liveResults = finderResults.filter(Boolean)
const lensesDead = LENSES.length - liveResults.length
// `ref` is DISPLAY ONLY from here on — it rides the prompts and the report lines and is never a map
// key. `id` is assigned once, after every lens has returned, and is the only join key.
const allFindings = liveResults
  .flatMap((r) => (r.findings || []).map((f) => ({ ...f, ref: `${f.file}:${f.line}` })))
  .map((f, i) => ({ ...f, id: i + 1 }))

if (lensesDead === LENSES.length) {
  log(`UNVERIFIED — all ${LENSES.length} lenses failed to return. Nothing was reviewed.`)
  return {
    confirmed: [], report: null, root: repo, lensesRun: 0, lensesDead,
    note: `UNVERIFIED: no lens completed (${lensesDead}/${LENSES.length} died) — nothing was reviewed`,
  }
}
if (allFindings.length === 0) {
  const note = lensesDead > 0
    ? `partial: ${lensesDead}/${LENSES.length} lenses died, survivors found nothing`
    : 'clean: 0 findings'
  log(note)
  return { confirmed: [], report: null, root: repo, lensesRun: liveResults.length, lensesDead, note }
}
log(`${allFindings.length} raw findings across ${LENSES.length} lenses — verifying in batches.`)

// --- Phase 2: VERIFY — batched skeptics (NOT one agent per finding) -----
phase('Verify')
// THE VERIFIER COUNT IS A CONSTANT. `chunk(allFindings, 5)` bounded the GROUP SIZE, so 70 findings
// bought 14 skeptics — still linear, which the protocol says is not enough. Bounding the group COUNT
// makes the batch grow and the agent count stand still. `chunk` slices contiguously, so a batch
// labelled `verify:ids-1-14` really does contain ids 1..14, and Math.ceil never yields an empty
// group: at N < MAX_VERIFIERS it produces exactly N groups of one.
const MAX_VERIFIERS = 5
const batches = chunk(allFindings, Math.ceil(allFindings.length / MAX_VERIFIERS)) // gov:fixed-verifiers
log(`${allFindings.length} finding(s) -> ${batches.length} verifier(s) (cap ${MAX_VERIFIERS})`)

const verdictResults = await boundedParallel(
  batches.map((group, gi) => () =>
    agent(
      `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate). Default to refuted when uncertain.\n\n` +
        `Findings to judge:\n` +
        group
          .map((f) => `id=${f.id} [${f.severity}] ${f.ref} — ${f.claim} | impact: ${f.impact}`)
          .join('\n') +
        `\n\nReturn JSON {verdicts:[{id:<the integer id shown above>, verdict:"confirmed"|"refuted", reason}]}. ` +
        `Emit EXACTLY one verdict per finding above (${group.length} verdicts, ids ${group.map((f) => f.id).join(', ')}). ` +
        `Copy the integer id — do NOT re-type the file path, and do not renumber.`,
      { label: `verify:ids-${group[0].id}-${group[group.length - 1].id}`, phase: 'Verify', schema: VERDICT_SCHEMA },
    ),
  ),
)

// S2/AC4 (TOOL-aGuardedTally-1): count the verdicts back. `refuted = total - confirmed` scored a
// finding with NO verdict as refuted, and a dead skeptic batch was dropped by filter(Boolean)
// uncounted -- so an all-skeptics-dead run returned `all findings refuted` at precision 0.00 with
// lensesDead 0. That is the same false-all-clear S1 fixes at the FINDER stage, one stage downstream:
// absence scored as a negative result. A finding nobody judged is UNVERIFIED, never refuted.
const liveVerdicts = verdictResults.filter(Boolean)
const skepticsDead = verdictResults.length - liveVerdicts.length
// U6: a Map keyed on the assigned integer, populated ONLY for an id this run actually handed out.
// Three degraded shapes get their own counter instead of silently rewriting a verdict:
//   spurious   — an id nobody assigned (a hallucinated or renumbered verdict); ignored, counted.
//   duplicate  — a repeat that AGREES with the standing verdict; idempotent, counted.
//   conflict   — a repeat that DISAGREES; the finding is demoted to UNVERIFIED, because "two
//                skeptics said opposite things" is precisely the state where this harness does not
//                know. Last-write-wins here is the collision class this unit exists to kill.
const assignedIds = new Set(allFindings.map((f) => f.id))
const verdictById = new Map()
const conflicts = new Set()
let duplicates = 0
let spurious = 0
for (const r of liveVerdicts)
  for (const v of r.verdicts || []) {
    if (!Number.isInteger(v.id) || !assignedIds.has(v.id)) { spurious++; continue }
    const prev = verdictById.get(v.id)
    if (!prev) { verdictById.set(v.id, v); continue }
    if (prev.verdict === v.verdict) duplicates++
    else conflicts.add(v.id)
  }
for (const id of conflicts) verdictById.delete(id)

const confirmed = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'confirmed')
const refuted = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'refuted')
const unverified = allFindings.filter((f) => !verdictById.has(f.id))
// precision is confirmed/(confirmed+refuted): an unjudged finding is not evidence either way.
const judged = confirmed.length + refuted.length
const precision = judged ? confirmed.length / judged : 0
if (unverified.length)
  log(`WARNING: ${unverified.length} finding(s) came back with NO usable verdict — counted UNVERIFIED, not refuted: ids ${unverified.map((f) => f.id).join(', ')}`)
if (conflicts.size)
  log(`WARNING: ${conflicts.size} finding(s) got CONTRADICTORY verdicts — demoted to UNVERIFIED: ids ${[...conflicts].join(', ')}`)
if (duplicates) log(`note: ${duplicates} repeat verdict(s) agreed with the standing one — idempotent.`)
if (spurious) log(`WARNING: ${spurious} verdict(s) carried an id this run never assigned — discarded.`)
if (skepticsDead)
  log(`WARNING: ${skepticsDead}/${verdictResults.length} skeptic batch(es) died — verification is PARTIAL.`)
log(
  `confirmed ${confirmed.length} / refuted ${refuted.length} / unverified ${unverified.length} — precision ${precision.toFixed(2)}` +
    (judged === 0
      ? ' (NOTHING was judged — the number is a placeholder, not a result)'
      : precision < 0.5 ? ' (below 0.5 — tighten scope/priming next time, don\'t add agents)' : ''),
)

// U6/S7: the run that most needs a written report is the one where findings were raised and nothing
// came back to judge them. The old `judged === 0` early return returned WITHOUT a report in exactly
// that case. One test governs now: anything still outstanding — confirmed or unverified — is
// synthesized. Only a fully-adjudicated, fully-refuted run exits here.
// S2: a refutation reached with dead skeptics is not a refutation. Carry the lens counts so a
// caller can tell "every finding was refuted" from "the verify stage was degraded".
if (confirmed.length + unverified.length === 0)
  return {
    confirmed: [], report: null, precision, root: repo,
    lensesRun: liveResults.length, lensesDead, skepticsDead, unverified: 0,
    conflicts: conflicts.size, duplicates, spurious,
    note: lensesDead > 0
      ? `all findings refuted, but ${lensesDead}/${LENSES.length} lenses died — treat as partial`
      : 'all findings adjudicated and refuted',
  }

// --- Phase 3: SYNTHESIZE — one agent writes the report ------------------
phase('Synthesize')
const synth = await agent(
  `Write the Tier-2 review report for: ${context}\n\n` +
    `CONFIRMED findings (survived an adversarial skeptic):\n` +
    (confirmed.length
      ? confirmed
          .map(
            (f) =>
              `- id=${f.id} [${f.severity}] ${f.ref} — ${f.claim}\n  impact: ${f.impact}\n  fix: ${f.fix}\n  why-real: ${verdictById.get(f.id)?.reason || ''}`,
          )
          .join('\n')
      : '  (none)') +
    `\n\nUNVERIFIED findings (no usable skeptic verdict came back — OUTSTANDING, not cleared; read the code yourself before classifying each):\n` +
    (unverified.length
      ? unverified
          .map((f) => `- id=${f.id} [${f.severity}] ${f.ref} — ${f.claim}\n  impact: ${f.impact}\n  fix: ${f.fix}`)
          .join('\n')
      : '  (none)') +
    `\n\nWrite a markdown report (severity-ranked, blockers first, each with file:line + fix + a left-shift gate suggestion) to a file under ${repo}/${reviewDir}. ` +
    `State the review shape near the top — raw ${allFindings.length}, confirmed ${confirmed.length}, refuted ${refuted.length}, unverified ${unverified.length}, precision ${precision.toFixed(2)}. ` +
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

// H1: the SUCCESS return carries the same trust counts as the early ones. A caller that only ever
// sees {confirmed, precision} cannot tell a full review from one where half the lenses died.
return {
  root: repo,
  raw: allFindings.length,
  confirmed: confirmed.length,
  refuted: refuted.length,
  unverified: unverified.length,
  conflicts: conflicts.size,
  duplicates,
  spurious,
  precision,
  lensesRun: liveResults.length,
  lensesDead,
  skepticsDead,
  agents: LENSES.length + batches.length + 1, // finders + batched skeptics + synth
  report: synth?.path || null,
  summary: synth?.summary || '',
  note:
    judged === 0
      ? `UNVERIFIED: ${allFindings.length} finding(s) raised, none judged (${skepticsDead}/${verdictResults.length} skeptic batches died) — the report lists them as outstanding`
      : lensesDead || skepticsDead || unverified.length
        ? `PARTIAL: ${lensesDead} lens(es) and ${skepticsDead} skeptic batch(es) died, ${unverified.length} finding(s) unverified`
        : 'complete',
}

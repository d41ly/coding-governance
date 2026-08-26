export const meta = {
  name: 'tier2-review',
  version: '1.3', // gov:kit tier2-review@1.3 — engine identity (deployed verbatim; this field is the deployer's version marker)
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
// TOOL-aBoundedVerdict-14 S1/S2 - the fold-scoping inputs. `priorFindings` is deliberately NOT merged
// into `byDesign`: they are different instructions. byDesign says "this is intended, do not report
// it"; a prior finding says "this was reported and FIXED - check the fix, and do not re-raise the
// original". Collapsing them loses the second half, which is the half this unit exists for. Measured
// before building: byDesign is supplied by no caller anywhere in the tree, so smuggling load-bearing
// content through it would put it in a field with a zero-use history.
const priorFindings = Array.isArray(a.priorFindings) ? a.priorFindings : []
// F1 resolved: accept an explicit integer AND infer 2 when prior findings arrive without one, so a
// caller cannot silently get a round-1 brief while handing over a previous round's confirmed set.
const round = Number.isInteger(a.round) && a.round > 0 ? a.round : priorFindings.length ? 2 : 1
// S3 - a base that is not an immutable sha is REFUSED at round > 1 and warned at round 1. The
// harness has no filesystem and cannot resolve a ref, so this is a STRING check on the shape of what
// it was handed: the caller resolves, and the harness refuses anything that does not look resolved.
// F2 resolved at 7+ hex, the same floor the driver's own review-record join uses and the shortest
// abbreviation git produces here - not 40, which would refuse the spelling the corpus actually uses.
const baseLooksPinned = /^[0-9a-f]{7,40}$/.test(String(base))
if (!baseLooksPinned) {
  const why =
    'tier2-review: `base` must be an immutable sha (7-40 hex), not a moving ref. Got ' +
    JSON.stringify(base) +
    '. M8 forbids a moving ref two paragraphs above the invocation it documents, and the default here ' +
    'is `origin/main` - so a caller who lets it stand records provenance that points at whatever main ' +
    'happened to be. Resolve it: git rev-parse <ref>.'
  if (round > 1) throw new Error(why)
  log('WARNING: ' + why)
}
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
        `REVIEW ROUND: ${round}${round > 1 ? ' - this is a FOLD review. The diff above is what the previous round\'s fixes introduced, not the whole build.' : ''}\n` +
        `BY DESIGN (do NOT re-report these): ${byDesign}\n` +
        (priorFindings.length
          ? `PRIOR ROUND'S CONFIRMED FINDINGS - these were RAISED AND FIXED. Judge the FIX, and do not re-raise the original:\n` +
            priorFindings
              .map((f) => `  - ${f.ref || '(no ref)'} - ${f.claim || f.title || '(no claim)'}`)
              .join('\n') +
            `\n\n`
          : `PRIOR ROUND'S FINDINGS: none - this is a first-round review of the whole diff.\n\n`) +
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
    // TOOL-dTieredTribunal-1 S3 - null, never 0. No synthesis ran, so there is no adjudicated count.
    confirmed: [], report: null, root: repo, blockers: null, highs: null, lensesRun: 0, lensesDead,
    note: `UNVERIFIED: no lens completed (${lensesDead}/${LENSES.length} died) — nothing was reviewed`,
  }
}
if (allFindings.length === 0) {
  const note = lensesDead > 0
    ? `partial: ${lensesDead}/${LENSES.length} lenses died, survivors found nothing`
    : 'clean: 0 findings'
  log(note)
  // TOOL-dTieredTribunal-1 S3 - null, never 0: no synthesis ran on this path either.
  return { confirmed: [], report: null, root: repo, blockers: null, highs: null, lensesRun: liveResults.length, lensesDead, note }
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
    // TOOL-dTieredTribunal-1 S3 - null, never 0. Every finding was refuted, which is a RESULT, but
    // no synthesis pass ran to adjudicate a blocker count, so there is none to report.
    confirmed: [], report: null, precision, root: repo, blockers: null, highs: null,
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
    // The range line is what the unattended kit's `closing-review-recorded` joins on, so the value
    // reaches the record without a human remembering to type it. HONEST LIMIT: `base` defaults to
    // the REF 'origin/main', and a caller who lets it stand writes a line carrying no sha, which
    // satisfies nothing. The harness cannot tell whether a mandate is in force — it has no
    // filesystem and no repo access — so M8 spelling the invocation with the pinned sha is what
    // makes this work, and the failure surfaces as an unmet DoD item naming the run's own record.
    `Open the report with a line naming the reviewed range as ${base}...${head}, and state the ROUND as ${round}. ` +
    // TOOL-dTieredTribunal-1 S4 - the record's opening ORDER. THREE sentences in this prompt each
    // claim the record's opening: the binding line below, the range line above, and the verdict
    // heading this unit adds. Instructing a second "first line" leaves the agent to resolve the
    // collision, so the order is stated once, here, and names all three. Keeping the binding line
    // first is also what satisfies check 21's 12-line binding-head window by construction.
    // S4b - the token set is READ from the carrier that ENFORCES it on a diff-review record, which
    // is hygiene check 22 in check-memory-hygiene.sh (gated by REVIEW_VERDICT_CUTOFF). It is not a
    // new rule invented here, and the build method is not the enforcing carrier for this kind.
    `THE RECORD'S OPENING IS ORDERED, and these four things precede the body, in this order. ` +
    `First the \`**Serves:**\` binding line described below. Then the report's title and provenance. ` +
    `Then the range line named above. Then, as a heading of its own, the literal \`## Verdict: \` ` +
    `followed by exactly ONE token from the CLOSED set CLEAN, CLEAN WITH FIXES, BLOCKED. ` +
    `The set is closed: no fourth token, no tally appended to the line, no qualifier on it. ` +
    `A count or a caveat goes in the paragraph beneath that heading, never on it. ` +
    // TOOL-aBoundedVerdict-14 S7 - the record's BINDING LINE, instructed here because the harness does
    // not write the record: the synth AGENT does. Rev-1 said the harness writes one lacking a kind
    // token; `grep -ni serves` over this file returned NOTHING, so it wrote no binding line at all and
    // the premise was wrong in both halves. It must carry a kind AND at least one id: a kind with no
    // id is MALFORMED under memory/HYGIENE.md's grammar, so emitting the kind alone would trade a
    // missing line for an unparseable one. The FILENAME's id projection stays with M8's rename, which
    // check 21's fourth branch also requires and which a harness with no repo access cannot perform.
    `The report's FIRST line must be the record's binding line, exactly: **Serves:** diff-review ` +
    `followed by every unit id in the diff, space-separated. A kind with no id is malformed under the ` +
    `project's record-binding grammar, so never emit the kind alone. ` +
    // TOOL-dTieredTribunal-1 S5 - BOTH integers are defined, not just one. S1 makes both REQUIRED,
    // so a definition for one and silence on the other ships a mandatory integer with no stated
    // population. What this buys, stated exactly: ONE agent writes the record and returns the
    // integers, from one adjudication, in one turn. Nothing re-counts the record, so the agreement
    // is a property of this prompt and not of a mechanism.
    `\`blockers\` is the number of CONFIRMED findings you classified at BLOCKER severity, and ` +
    `\`highs\` the number at HIGH severity. In both cases the severity meant is the one YOU ` +
    `adjudicated in this report, so the integers you return and the table you wrote agree. ` +
    `Return JSON {path, blockers, highs, summary} with a FORWARD-SLASH path.`,
  {
    label: 'synth',
    phase: 'Synthesize',
    schema: {
      type: 'object',
      // TOOL-dTieredTribunal-1 S1 - `blockers` and `highs` were requested and schemad from the
      // start and were never required and never read. Requiring them is what makes a synthesis that
      // omits one fail loudly at validation instead of returning a partial object nobody notices.
      required: ['path', 'summary', 'blockers', 'highs'],
      properties: {
        path: { type: 'string' },
        blockers: { type: 'integer' },
        highs: { type: 'integer' },
        summary: { type: 'string' },
      },
    },
  },
)

// TOOL-aBoundedVerdict-14 S6 - the SYNTH-DEATH hole. Lens deaths and skeptic deaths are both counted
// and reported; a dead synthesis was not, so `synth === null` returned report:null with a note reading
// `complete` and every confirmed finding was lost with nothing logged. The findings exist here in
// memory - the only thing missing was saying so before the return threw them away.
if (!synth) {
  log(`WARNING: the synthesis agent DIED. No report was written, and the ${confirmed.length} confirmed finding(s) below exist only in this log:`)
  for (const f of confirmed)
    log(`  CONFIRMED [${f.severity}] ${f.ref} - ${f.claim} | fix: ${f.fix}`)
  for (const f of unverified) log(`  UNVERIFIED [${f.severity}] ${f.ref} - ${f.claim}`)
}

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
  // TOOL-dTieredTribunal-1 S2/S3b - the counts the synthesis pass adjudicated, returned rather than
  // dropped. The ternary is deliberate and none of the shorter spellings is correct here.
  // `synth.blockers` THROWS on a dead synthesis. `synth?.blockers` yields `undefined`, which
  // serializes as an absent key rather than as a stated absence. `synth?.blockers || 0` fabricates a
  // clean bill on a dead synthesis, which is the false-clean class this file exists to refuse. And
  // `synth?.blockers || null` maps a real adjudicated 0 to null, because after S1 the field is
  // required and a returned 0 is a result. So: the value when a synthesis ran, null when none did.
  blockers: synth ? synth.blockers : null,
  highs: synth ? synth.highs : null,
  // TOOL-dTieredTribunal-1, closing-review D1 - a dead synthesis was tested LAST, so it was
  // reportable only when nothing else was degraded and the most serious note was the least reachable
  // one. Worst outcome first. Found by the closing review of the build that ported this ternary into
  // the two drift-audit siblings, where the same ordering had been copied.
  note:
    !synth
      ? `UNVERIFIED: the synthesis agent died, so NO report was written; ${confirmed.length} confirmed finding(s) are in the run log only`
      : judged === 0
        ? `UNVERIFIED: ${allFindings.length} finding(s) raised, none judged (${skepticsDead}/${verdictResults.length} skeptic batches died) — the report lists them as outstanding`
        : lensesDead || skepticsDead || unverified.length
          ? `PARTIAL: ${lensesDead} lens(es) and ${skepticsDead} skeptic batch(es) died, ${unverified.length} finding(s) unverified`
          : 'complete',
  round,
  priorFindings: priorFindings.length,
}

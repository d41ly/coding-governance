export const meta = {
  name: 'unattended-build',
  version: '1.0', // gov:kit unattended-build@1.0 — engine identity (deployed verbatim)
  description:
    'Drives a build SPEC -> AUDIT -> BUILD as ordered stages of ONE program, so pass order is a property of control flow rather than of an agent recollection across a context that compacts. BUILD is unreachable unless the audit verdict is terminal.',
  phases: [
    { title: 'Spec', detail: 'author every missing spec, in the declared order, no code' },
    { title: 'Audit', detail: 'delegate to tier2-review.js as a spec-audit; record the round' },
    { title: 'Build', detail: 'the units, one at a time, each from its brief and its spec' },
  ],
}

// ---------------------------------------------------------------------------------------------
// WHAT THIS BUYS AND WHAT IT CANNOT BUY, first, because the second half is the one a reader will
// otherwise assume away.
//
// IT BUYS STAGE ORDER. The SPEC stage's await completes before the AUDIT stage begins, and BUILD is
// unreachable except through both AND through a terminal audit verdict. That is JS control flow, not
// a rule anybody remembers, and it is the whole mechanism: a unit cannot be built before it is
// specced inside a harnessed run. It is the defect the owner's prompt reports — "build can run
// BEFORE they are specced with spec written postfactum" — and the one this file closes.
//
// IT CANNOT BUY ENFORCEMENT. A Workflow script has NO FILESYSTEM. Every observation it makes is a
// claim its own agent returned, so nothing here can verify that a spec exists, that a gate passed, or
// that a commit happened. The refusal that makes the order real lives in the driver, where the tree
// is readable: `--dispatch` refuses a MISSING, THIN or out-of-order unit, and the `pass-order
// history` leg refuses a unit whose build commit predates its spec. A stage in this file claiming to
// VERIFY the tree would be the could-not-fail shape this repo names.
//
// IT DOES NOT COVER orientation, preflight, the owner turn, closing, landing or the keepalive. Those
// are main-loop acts by construction: the scheduling store is in-memory and session-scoped, and
// `--close` and `--landed` run after this returns.
//
// DISPATCH IS STRICTLY SEQUENTIAL, including within a shared `order` value. `TOOL-cBriefedPilot-21`
// ratified `parallelism route: none`; the Workflow-sidechain route is that hunt's R2, which cleared
// E1 and E2 and FAILED E3 and E4 — E4 being that two passes can commit without racing one index.
// `TOOL-cBriefedPilot-28` is open and names those two experiments as never run. A shared order value
// is therefore RECORDED and not acted on, which keeps the declaration for whoever re-opens it.
//
// ---------------------------------------------------------------------------------------------
// TWO SHAPES HERE ARE FORCED RATHER THAN CHOSEN, and both come from one denial.
// `tools/hooks/agent-cap.js` refuses an `agent()` inside ANY loop body, unconditionally: its
// whitelist is closed and names no marker for the case. So the only shapes it admits are a bounded
// PARALLEL fan — which the ratified verdict above forbids — and a SINGLE call. Measured by running
// the hook's own predicate over two earlier drafts of this file; it denied every loop site, calling
// a strictly sequential `await agent(...)` "a loop-built thunk array". The conflict is PARKED for
// the owner rather than worked around, because restructuring a call into a helper the loop invokes
// would be textually indistinguishable from the evasion the rule names.
//
//   1. EACH STAGE IS ONE AGENT holding the ordered unit list, rather than one agent per unit. The
//      stage order stays structural; per-unit order moves onto `--dispatch`'s refusal, which reads
//      the tree and is therefore a STRONGER check than a JS loop rather than a weaker one.
//
//   2. THE CONVERGENCE LOOP LIVES IN THE CALLER, and this file holds the GATE. A convergence loop's
//      iteration count is data-dependent by definition, so unlike case 1 there is no bounded unroll.
//      What had to be structural still is: a `CONVERGING` verdict RETURNS without reaching BUILD, so
//      no caller error can build on a spec set the review is still working through. The owner's
//      2026-09-01 ruling survives in the half that matters — the verdict decides, and NO round cap
//      exists anywhere in this file.

// --- inputs (via Workflow `args`) --------------------------------------------------------------
// { repo: "/abs/path/to/worktree",                 // REQUIRED
//   slug: "<build slug>",                           // REQUIRED
//   base: "<immutable sha>",                        // the review anchor, for the record
//   units: [{ id, order, specPath, briefPath }],    // ORDERED by the caller, from --plan
//   briefDir: "memory/builds/<slug>/prompts",
//   reviewDir: "memory/builds/<slug>/reviews",
//   round: <integer>                                // which audit round this invocation is
// }
//
// `units` ARRIVES PRE-ORDERED and that is load-bearing. The caller runs `--plan`, which takes its set
// and order from the generated units region, so the harness and the driver cannot disagree about what
// "next" means. This runtime has no filesystem and could not derive it even if it wanted to.
//
// ARGS MUST BE A STRUCTURED OBJECT, and the Workflow tool delivers it as a STRING even when the
// caller hands it JSON, so this parses first and validates second. Ported deliberately from
// `tier2-review.js`, which added the guard after that harness twice reviewed a DIFFERENT repository
// than the one it was briefed on; `TOOL-dTieredTribunal-4` records that the two drift-audit siblings
// still lack it. The first cut of that guard tested `typeof a !== 'object'` and refused every
// legitimate caller, which is why the PASSING case is armed here too.
let cfg = args
if (typeof cfg === 'string') {
  try {
    cfg = JSON.parse(cfg)
  } catch (e) {
    throw new Error(
      'unattended-build: args must be JSON carrying an explicit `repo` and `slug`; could not parse ' +
        'the string given (' + e.message + '). Refusing to default the build root to the process ' +
        'cwd — that is how a sibling harness reviewed the wrong repository twice.',
    )
  }
}
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg) || !cfg.repo) {
  throw new Error(
    'unattended-build: args must carry an explicit `repo`. Got ' +
      (Array.isArray(cfg) ? 'array' : typeof cfg) +
      '. Refusing to default the build root to the process cwd.',
  )
}
if (!cfg.slug) {
  throw new Error(
    'unattended-build: args must carry an explicit `slug`. Every driver verb below is slug-addressed, ' +
      'and a harness that guessed one would record a run against a build nobody asked about.',
  )
}
const a = cfg
const repo = a.repo
const slug = a.slug
const base = a.base || ''
const briefDir = a.briefDir || 'memory/builds/' + slug + '/prompts'
const reviewDir = a.reviewDir || 'memory/builds/' + slug + '/reviews'
const units = Array.isArray(a.units) ? a.units : []
if (!units.length) {
  throw new Error(
    'unattended-build: args carries no `units`. The caller derives them from `--plan`, which takes ' +
      'its set and ORDER from the generated units region; a harness with an empty set would report a ' +
      'clean run over nothing, which is the vacuous-selector shape this repo refuses.',
  )
}
const roundNo = Number.isInteger(a.round) && a.round > 0 ? a.round : 1

const DRIVER = 'bash tools/unattended/unattended.sh'
const ordered = units.slice().sort(function (x, y) {
  const ox = Number.isInteger(x.order) ? x.order : 1e9
  const oy = Number.isInteger(y.order) ? y.order : 1e9
  if (ox !== oy) return ox - oy
  return String(x.id) < String(y.id) ? -1 : 1
})
// A TOP-LEVEL FUNCTION, and not only for tidiness: the codebase map's `kit-js` layer RAISES on a JS
// file yielding no top-level definition rather than indexing less of it, which is how that layer
// once went 30-to-3 unseen. Named with `render` from the declared lexicon table; `produce` and
// `format` are not in it.
function renderRoster(list, buildSlug, briefRoot) {
  return list
    .map(function (u) {
      return '  ' + (Number.isInteger(u.order) ? 'order ' + u.order : 'unordered') + ' | ' + u.id +
        ' | spec ' + (u.specPath || '(to be authored under memory/builds/' + buildSlug + '/spec/)') +
        ' | brief ' + (u.briefPath || '(to be written under ' + briefRoot + ')')
    })
    .join('\n')
}
const roster = renderRoster(ordered, slug, briefDir)
const allIds = ordered.map(function (u) { return u.id })

// --- the stage return schemas -----------------------------------------------------------------
// EVERY stage agent returns a schema-validated object, so a stage that cannot answer REFUSES rather
// than defaulting. Two properties are deliberate.
//
// A REFUSED/UNBUILT LIST IS ITS OWN REQUIRED FIELD, never an absence. `degradation-known-but-
// unreported` is the class where a pipeline computes how badly its own run degraded and then does
// not say so, and an empty `authored` list with no `refused` list is indistinguishable from a clean
// run over nothing.
//
// AUDIT's `verdict` is REQUIRED for one specific reason: an absent verdict would otherwise read as
// "nothing blocking", which is the one absence that would let this harness build on an unreviewed
// spec set.
const SPEC_SCHEMA = {
  type: 'object',
  required: ['authored', 'alreadyPresent', 'refused', 'summary'],
  additionalProperties: true,
  properties: {
    authored: { type: 'array', items: { type: 'string' } },
    alreadyPresent: { type: 'array', items: { type: 'string' } },
    refused: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}
const AUDIT_SCHEMA = {
  type: 'object',
  required: ['verdict', 'blockers', 'reportPath', 'summary'],
  additionalProperties: true,
  properties: {
    verdict: { type: 'string', enum: ['CONVERGING', 'CONVERGED', 'NON-CONVERGENT', 'CEILING'] },
    blockers: { type: 'integer' },
    reportPath: { type: 'string' },
    summary: { type: 'string' },
  },
}
const BUILD_SCHEMA = {
  type: 'object',
  required: ['committed', 'unbuilt', 'summary'],
  additionalProperties: true,
  properties: {
    committed: { type: 'array', items: { type: 'string' } },
    unbuilt: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

const GROUND =
  'You are one stage of a harnessed unattended build in the repository at ' + repo + '. ' +
  'Read `memory/guides/BUILD-METHOD.md` WHOLE before acting; it is the procedure you are bound by. ' +
  'The build is `' + slug + '` and its record is `memory/builds/' + slug + '/`. ' +
  'Speak only in your return value: nobody reads a transcript under a mandate. '

// ============================================================== STAGE 1 — SPEC
phase('Spec')
log('spec stage: ' + ordered.length + ' unit(s), in the order the caller derived from --plan')
const specced = await agent(
  GROUND +
    'SPEC every unit below, IN THIS ORDER:\n' + roster + '\n\n' +
    'For each: if a conforming spec already carries that id, leave it alone and count it in ' +
    'alreadyPresent. Otherwise author it against `memory/TEMPLATE-SPEC.md` at the tier the kickoff ' +
    'engine assigns, satisfy its section 10 reuse obligation with a real probe rather than a claim, ' +
    'and give its status header the `order` verb this roster names. ' +
    'DO NOT WRITE PRODUCT CODE in this stage. It authors designs and nothing else — a unit built ' +
    'here would be the exact defect this harness exists to remove. ' +
    'NAME every unit you could not spec, in `refused`, with the reason in your summary.',
  { label: 'spec:' + slug, phase: 'Spec', schema: SPEC_SCHEMA },
)
if (!specced) {
  throw new Error(
    'unattended-build: the SPEC stage returned nothing, so no unit is known to have a design. That ' +
      'is a refusal and not an empty pass: continuing would put the BUILD stage on a spec set ' +
      'nothing confirmed exists.',
  )
}
const specRefused = Array.isArray(specced.refused) ? specced.refused : []
const speccedCount =
  (Array.isArray(specced.authored) ? specced.authored.length : 0) +
  (Array.isArray(specced.alreadyPresent) ? specced.alreadyPresent.length : 0)
if (specRefused.length) log('spec stage: ' + specRefused.length + ' unit(s) REFUSED — ' + specRefused.join(', '))

// ================================================ STAGE 2 — AUDIT, and the gate on its verdict
// ONE ROUND HERE, THE LOOP IN THE CALLER — see the header for why that split is forced.
//
// THE BLOCKER COUNT COMES FROM THE SYNTHESIS RETURN, which is the only site in `tier2-review.js`
// that yields an INTEGER. Its degraded-path returns yield `blockers: null` BY DESIGN — null, never
// 0, so a stated absence cannot be read as a clean bill — and `unattended.sh` emits CONVERGED only
// on a count of 0 while refusing a non-integer. Routing this through a null-yielding site would make
// the CONVERGED exit unreachable and every audit look degraded.
phase('Audit')
const au = await agent(
  GROUND +
    'AUDIT round ' + roundNo + ' over this build spec set:\n' + roster + '\n\n' +
    'Run the shipped harness as a Workflow — not as direct Agent spawns, whose budget is keyed per ' +
    'user prompt and which an unattended run cannot reset — with ' +
    '`scriptPath: tools/workflows/tier2-review.js` and args carrying `kind: "spec-audit"`, `repo`, ' +
    '`round: ' + roundNo + '`, `reviewDir: "' + reviewDir + '"`, and one `subjects` entry per spec ' +
    'pinned at its blob. The `kind` is MANDATORY: an absent one defaults to `diff-review`, which ' +
    'primes code-shaped lenses at a spec and reports it as a review. ' +
    'Take the CONFIRMED BLOCKER COUNT from that run synthesis return, which is the only site ' +
    'yielding an integer; a `null` there is a DEGRADED run and you must return that fact rather than ' +
    'a number you invented. Then record the round with `' + DRIVER + ' --review ' + slug +
    ' --subject ' + slug + '-spec-set --verdict <CLEAN|CLEAN WITH FIXES|BLOCKED> --blockers <N>` ' +
    'and return the driver own verdict token verbatim.',
  { label: 'audit:r' + roundNo, phase: 'Audit', schema: AUDIT_SCHEMA },
)
if (!au) {
  // A dead AUDIT stage is a REFUSAL, never a silent exit to BUILD. This is the absence that would
  // otherwise let the harness build on an unreviewed spec set.
  throw new Error(
    'unattended-build: the AUDIT stage returned nothing at round ' + roundNo + '. That is a refusal ' +
      'and not a convergence: an absent verdict must never read as CONVERGED, because that token is ' +
      'the only thing between this harness and building on an unreviewed spec set.',
  )
}
const verdict = au.verdict
const lastReport = au.reportPath || ''
log('audit round ' + roundNo + ': ' + verdict + ' · blockers ' + au.blockers)

// THE GATE. `CONVERGING` means the review loop has not ended, so BUILD is UNREACHABLE and this
// returns to the caller with what it needs to fold and come back. The three terminal states admit
// it, and on the two non-clean ones every standing blocker is PROMOTED to a unit rather than carried
// into code, which is what `BUILD-METHOD.md` M4 requires at the exit.
if (verdict === 'CONVERGING') {
  log('audit is still CONVERGING — BUILD is not reachable this invocation; fold, then re-invoke at round ' + (roundNo + 1))
  return {
    slug: slug,
    base: base,
    round: roundNo,
    units: ordered.length,
    specced: speccedCount,
    specRefused: specRefused,
    verdict: verdict,
    blockers: au.blockers,
    lastReport: lastReport,
    built: 0,
    unbuilt: allIds,
    nextAction:
      'FOLD the confirmed findings in ' + lastReport + ' as rev-N bumps with their section 9 lines, ' +
      'then re-invoke this harness with round: ' + (roundNo + 1) + '. Do not build.',
    note: 'HELD AT AUDIT — the review loop has not ended, so no unit was built',
  }
}

// ============================================================== STAGE 3 — BUILD
// ONE AGENT holding the ordered list. Sequential is still the contract and the agent is told so
// explicitly; what ENFORCES it is `--dispatch`, which reads the tree and refuses a unit that is
// MISSING, THIN or out of the build's declared order.
phase('Build')
log('build stage: ' + ordered.length + ' unit(s), one at a time, each from its brief and its spec')
const built = await agent(
  GROUND +
    'BUILD every unit below, ONE AT A TIME and IN THIS ORDER. Never start one before the previous ' +
    'has committed:\n' + roster + '\n\n' +
    'For each unit you are handed exactly two documents and you read both before touching code: its ' +
    'BRIEF and its SPEC, both named in the roster. The spec is the design; where you must diverge ' +
    'from it, CHANGE THE SPEC FIRST as a `rev-N` bump with its section 9 line, then write the code. ' +
    'Before writing, declare the write set with `' + DRIVER + ' --dispatch ' + slug +
    ' --pass <unit-id> --writes <path>`, and record what you were handed with `' + DRIVER +
    ' --brief ' + slug + ' --unit <unit-id> --path <the brief>`. THAT DISPATCH IS THE ORDER GATE: it ' +
    'refuses a unit that is MISSING, THIN or out of the declared order, and a refusal is this ' +
    'harness telling you the order is wrong. Read it and stop — do not work around it. ' +
    'Commit at the end of each pass with the unit id in the subject, then run ' +
    '`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names before ' +
    'the next unit begins. NAME every unit you did not commit, in `unbuilt`, and why.',
  { label: 'build:' + slug, phase: 'Build', schema: BUILD_SCHEMA },
)
if (!built) {
  throw new Error(
    'unattended-build: the BUILD stage returned nothing, so no unit is known to have been built and ' +
      'none is known to have been skipped. Reported as a refusal rather than as zero units built.',
  )
}
const unbuilt = Array.isArray(built.unbuilt) ? built.unbuilt : []

// THE RUN-INTEGRITY BLOCK. `memory/gotchas/degradation-known-but-unreported` is the class where a
// pipeline computes how badly its own run degraded and then fails to say so where it matters. Every
// count below is carried OUT of this harness rather than left in a log nobody reads.
return {
  slug: slug,
  base: base,
  round: roundNo,
  units: ordered.length,
  specced: speccedCount,
  specRefused: specRefused,
  verdict: verdict,
  blockers: au.blockers,
  lastReport: lastReport,
  built: Array.isArray(built.committed) ? built.committed.length : 0,
  unbuilt: unbuilt,
  note:
    specRefused.length || unbuilt.length || verdict === 'CEILING'
      ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused, ' + unbuilt.length +
        ' unit(s) unbuilt, verdict ' + verdict
      : 'complete',
}

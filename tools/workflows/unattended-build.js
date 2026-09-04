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
// `tools/hooks/agent-cap.js` refused an `agent()` inside ANY loop body when this file was written,
// with a closed whitelist naming no marker for the case. `TOOL-dFoldedVerdict-4` has since added
// `gov:sequential-agents(<K>)`, so a bounded sequential loop over a proven-bounded identifier is now
// admissible and these are no longer the only shapes. Both are KEPT because both remain correct:
// stage order is structural either way, and a convergence loop's iteration count is data-dependent,
// so it has no bounded receiver to name and the marker cannot reach it. The shapes it admitted were
// a bounded
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
// The resolver stage's return. `blob` is a pattern rather than a bare string because an agent that
// cannot resolve one is likelier to answer with a plausible-looking placeholder than to omit the
// entry, and a subject pinned at an invented blob audits nothing while looking pinned.
// The recorder agent's return. `token` is the DRIVER's word, not the agent's opinion, which is why
// the prompt says verbatim and the enum is re-checked on this side regardless.
const REVIEW_RECORD_SCHEMA = {
  type: 'object',
  properties: {
    token: { type: 'string' },
    exitCode: { type: 'integer' },
    stderr: { type: 'string' },
  },
  required: ['token'],
}

const SUBJECTS_SCHEMA = {
  type: 'object',
  properties: {
    subjects: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          path: { type: 'string' },
          blob: { type: 'string', pattern: '^[0-9a-f]{7,40}$' },
        },
        required: ['path', 'blob'],
      },
    },
  },
  required: ['subjects'],
}

// `AUDIT_SCHEMA` LIVED HERE AND IS GONE. It bound the AGENT return that no longer exists, and
// leaving it would be a declaration nothing reads — but its `enum` was load-bearing, so that
// moved to `REVIEW_TOKENS` at the check rather than being lost with the constant. Deleting a
// dead schema and silently dropping its enum is how a check gets weaker while looking tidier.
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
// ============================ TOOL-dRatifiedSeam-1 S1 — THE SPAWN MOVED TO WHERE THE TOOL IS ====
// WHAT WAS WRONG. This stage used to spawn an AGENT whose prompt said: run the shipped harness as
// a Workflow, with `scriptPath: tools/workflows/tier2-review.js`. That agent is a SIDECHAIN agent,
// and a sidechain holds neither `Workflow` nor `Agent` — the capability is ABSENT, not policed, as
// `AGENTS.md` §8 states and as the stage agent proved by searching the deferred registry three
// times, refusing to fabricate a verdict, and writing nothing. It was right on every count. The
// stage could never complete, so BUILD was unreachable through this harness and the
// `passes-harnessed` directive named a route that did not run.
//
// THE FIX IS NOT A BETTER PROMPT. No wording gives an agent a tool it does not hold. But THIS FILE
// is a workflow script, and the script runtime provides `workflow({scriptPath}, args)` for running
// another workflow inline as a sub-step. So the spawn does not need to leave the harness — it needs
// to stop being delegated to something that cannot perform it. Nesting is one level deep and this
// harness is invoked at the top by the main loop, so the one level is available and is spent here.
//
// FIRST CALLER IN THE REPO. `grep -rnE '\bworkflow\(' tools/workflows/*.js` returned nothing before
// this line, which is why S4 OBSERVES the route end to end rather than asserting it.
//
// THE SPLIT IS FORCED, NOT CHOSEN, and measuring it is what produced this shape. `tier2-review.js`
// REFUSES a spec-audit whose `subjects` is not a non-empty array of `{path, blob}` with a 7-40 hex
// blob per subject. A workflow script has no filesystem and no git, so it cannot resolve a blob;
// an agent can. So the agent does what only an agent can — read the tree and pin each spec at its
// blob — and the SCRIPT does what only the script can, which is hold `Workflow`. The old code gave
// the agent BOTH jobs, and the second one is the one it could not do.
//
// A CALLER-SUPPLIED SET WINS. `--plan` already knows the spec set, so a caller that pinned the
// blobs itself is authoritative and the resolver stage is skipped rather than run for a second
// opinion about the same files.
let subjects = Array.isArray(a.subjects) ? a.subjects : null
if (!subjects) {
  const res = await agent(
    GROUND +
      'Resolve the blob of every spec in this build so an audit can be pinned at immutable bytes.\n' +
      roster + '\n\n' +
      'For each unit above that HAS a spec path, run `git rev-parse HEAD:<specPath>` in ' + repo +
      ' and return one entry per spec. Return ONLY units whose spec exists and whose blob resolves; ' +
      'an unspecced unit is not a subject and must be omitted rather than given an invented blob. ' +
      'Paths are repo-relative and forward-slashed.',
    { label: 'audit:subjects:r' + roundNo, phase: 'Audit', schema: SUBJECTS_SCHEMA },
  )
  subjects = (res && Array.isArray(res.subjects)) ? res.subjects : []
}
// REFUSED HERE RATHER THAN DOWNSTREAM. `tier2-review.js` would refuse an empty set too, but its
// message is about its own arguments; this one can say which stage failed to produce them, which is
// the difference between a diagnosable refusal and a puzzling one.
if (!subjects.length) {
  throw new Error(
    'unattended-build: no spec subjects could be pinned at round ' + roundNo + '. A spec-audit over ' +
      'an empty subject set would grade nothing and report it as a clean round, which is the exact ' +
      'shape this stage exists to prevent.',
  )
}
const badSubject = subjects.findIndex(function (s) {
  return !s || typeof s.path !== 'string' || !s.path || !/^[0-9a-f]{7,40}$/.test(String(s.blob || ''))
})
if (badSubject !== -1) {
  throw new Error(
    'unattended-build: subject ' + badSubject + ' is not a {path, blob} with a 7-40 hex blob: ' +
      JSON.stringify(subjects[badSubject]) + '. An unpinned subject is an audit of whatever the ' +
      'file happens to say when the lens reads it, which is not a review of anything in particular.',
  )
}

const auRaw = await workflow(
  { scriptPath: 'tools/workflows/tier2-review.js' },
  {
    kind: 'spec-audit',
    repo: repo,
    round: roundNo,
    reviewDir: reviewDir,
    subjects: subjects,
  },
)

// ===================== THE ADAPTER, REBUILT AGAINST THE CALLEE'S ACTUAL CONTRACT =============
// MY FIRST CUT READ `auRaw.verdict` AND `tier2-review.js` HAS NEVER RETURNED ONE. Its four returns
// yield `{blockers, report, highs, note, precision, confirmed, refuted, …}`; the only `verdict` in
// that file is per-FINDING. So the check below fired on every real invocation and the stage still
// could not complete — the failure had merely moved from an agent that refuses to a script that
// throws. The 28 suite arms were green because the test double returned a `verdict` and a
// `reportPath` I had invented, which is the fixture grading the fixture.
//
// WHO OWNS THE VERDICT VOCABULARY. `CONVERGING|CONVERGED|NON-CONVERGENT|CEILING` is produced by
// `unattended.sh`'s `review_state()` from the PRIOR round's counts — no JS can compute it, because
// convergence is a property of the sequence and not of this round. The old prompt ran the driver's
// `--review` and returned its token; that call was deleted with the agent and nothing replaced it,
// so no round was recorded either and the DoD leg that reads the last round found none.
//
// So the split is three ways, each part where its capability lives: the SCRIPT holds `Workflow`
// and calls the review; an AGENT holds a shell and records the round; the DRIVER owns the token.
// AN EMPTY OBJECT IS 'NOTHING', TOO. A dead sub-workflow yields `{}`, which is an object, so a
// bare type test let it through to the blocker check and the operator got a message about an
// integer when the real fact was that the stage produced nothing at all.
if (!auRaw || typeof auRaw !== 'object' ||
    (!Object.prototype.hasOwnProperty.call(auRaw, 'blockers') && !auRaw.report)) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned nothing at round ' + roundNo + '. That is a ' +
      'refusal and not a convergence: an absent verdict must never read as CONVERGED, because that ' +
      'token is the only thing between this harness and building on an unreviewed spec set.',
  )
}
// THE BLOCKER COUNT MUST BE AN INTEGER, and `null` is the DEGRADED signal `tier2-review.js` yields
// by design — null, never 0, so a stated absence cannot be read as a clean bill. Reading a null as
// 0 would make every degraded audit look clean, since 0 is the only count that converges.
if (!Number.isInteger(auRaw.blockers)) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned a non-integer blocker count (' +
      JSON.stringify(auRaw.blockers) + ') at round ' + roundNo + '. That is a DEGRADED run and it ' +
      'is reported as one; it is never rounded to zero.',
  )
}
const lastReport = auRaw.report || ''
// `report`, NOT `reportPath` — the second name was mine and matched nothing, so `lastReport` was
// always '' and every disposal instruction named an empty path.
if (!lastReport) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned no report path at round ' + roundNo +
      '. The fold instruction the caller receives would name nothing to fold from.',
  )
}

// THE ROUND IS RECORDED BY THE DRIVER, and the driver's answer is the verdict. An agent runs it
// because a workflow script has no shell; what the agent may NOT do is invent the token, so it is
// told to return the driver's own output verbatim and the enum below refuses anything else.
const rv = await agent(
  GROUND +
    'Record AUDIT round ' + roundNo + ' with the driver and return its convergence token.\n\n' +
    'Run exactly:\n  ' + DRIVER + ' --review ' + slug + ' --subject ' + slug + '-spec-set' +
    ' --verdict ' + (auRaw.blockers > 0 ? '"BLOCKED"' : '"CLEAN"') +
    ' --blockers ' + auRaw.blockers + '\n\n' +
    'Return the CONVERGENCE token it prints — one of CONVERGING, CONVERGED, NON-CONVERGENT, ' +
    'CEILING — verbatim, and the command\'s exit code. Do not infer the token from the blocker ' +
    'count: it is a property of the SEQUENCE of rounds, which only the driver can see. If the ' +
    'command fails, return its stderr rather than a token.',
  { label: 'audit:record:r' + roundNo, phase: 'Audit', schema: REVIEW_RECORD_SCHEMA },
)
if (!rv || typeof rv.token !== 'string') {
  throw new Error(
    'unattended-build: the round was not recorded at round ' + roundNo + ' (driver said: ' +
      JSON.stringify(rv && rv.stderr) + '). An unrecorded round leaves the convergence predicate ' +
      'with no predecessor to shrink against, and the Definition of Done leg that reads the last ' +
      'round finds nothing.',
  )
}
// THE ENUM IS RESTORED. `AUDIT_SCHEMA` carried it and my replacement checked only that the verdict
// was a non-empty string, so `"ok"` would have passed, failed the `=== 'CONVERGING'` test, and
// fallen straight through to BUILD. That is weaker than what it replaced, in the direction that
// matters.
const REVIEW_TOKENS = ['CONVERGING', 'CONVERGED', 'NON-CONVERGENT', 'CEILING']
if (REVIEW_TOKENS.indexOf(rv.token) === -1) {
  throw new Error(
    'unattended-build: the driver returned "' + rv.token + '", which is not one of ' +
      REVIEW_TOKENS.join(', ') + '. An unknown token is not CONVERGING, so it would fall through ' +
      'to BUILD — refusing instead.',
  )
}
const au = { verdict: rv.token, blockers: auRaw.blockers, reportPath: lastReport }
// S3 — THE IMPOSSIBLE PAIRING IS A REFUSAL BY NAME. CONVERGING with zero blockers is this repo's
// signature for a record no verb produced: a loop with nothing left to converge on has converged.
// The dead stage returned exactly this pairing, and it was the tell.
if (au.verdict === 'CONVERGING' && au.blockers === 0) {
  throw new Error(
    'unattended-build: the AUDIT stage returned CONVERGING paired with 0 blockers at round ' +
      roundNo + '. Those two cannot both be true, and this pairing is this repo\'s signature for a ' +
      'record no verb produced. REFUSING rather than emitting it.',
  )
}
const verdict = au.verdict
log('audit round ' + roundNo + ': ' + verdict + ' · blockers ' + au.blockers)

// THE GATE. `CONVERGING` means the review loop has not ended, so BUILD is UNREACHABLE and this
// returns to the caller with what it needs to fold and come back. The three terminal states admit
// it; what the two NON-CLEAN ones additionally carry is M4's disposal instruction, built into the
// BUILD prompt below rather than asserted here. An earlier revision of this comment claimed the
// promotion happened and no line of the program did it.
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
//
// ON A NON-CLEAN TERMINAL VERDICT THE BLOCKERS ARE DISPOSED FIRST, and that instruction is CARRIED
// rather than asserted. The comment above the gate used to claim promotion happened at the exit and
// nothing did it: control fell from a CONVERGING-only early return straight into this stage, the
// report path was computed and discarded, and the BUILD prompt never mentioned a blocker. So on
// `NON-CONVERGENT` and `CEILING` — the two states that structurally guarantee standing blockers,
// since the driver emits CONVERGED only at a count of 0 — the harness built a spec set with open
// blockers. This build itself exited NON-CONVERGENT at round 3, so the path is reached rather than
// hypothetical.
const disposal =
  verdict === 'CONVERGED'
    ? ''
    : 'BEFORE ANY UNIT IS BUILT, DISPOSE of every blocker still standing in `' + lastReport + '` — ' +
      'the audit exited ' + verdict + ' with ' + au.blockers + ' confirmed. BUILD-METHOD M4 admits ' +
      'exactly two dispositions and no third: FOLD one that is a defect in a document the review ' +
      'already read, as a rev-N bump with its section 9 line; PROMOTE one needing a MECHANISM this ' +
      'build lacks, through `' + DRIVER + ' --rescope ' + slug + ' --act add --item <id>`, then spec ' +
      'it at its tier and build it like any other. Never parked, never waived, never retired, never ' +
      're-reviewed. Report what you did with each. '
phase('Build')
log('build stage: ' + ordered.length + ' unit(s), one at a time, each from its brief and its spec')
const built = await agent(
  GROUND +
    disposal +
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
    specRefused.length || unbuilt.length || verdict !== 'CONVERGED'
      ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused, ' + unbuilt.length +
        ' unit(s) unbuilt, verdict ' + verdict
      : 'complete',
}

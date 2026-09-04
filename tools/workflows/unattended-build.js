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
// ---------------------------------------------------------------------------------------------
// ATTENDED MODE — WHAT IT BUYS AND WHAT IT LOSES (TOOL-aStagedLane-2)
//
// A CLOSED PAIR, DEFAULTING TO `unattended`, so every existing caller is unchanged and none has
// to be migrated. Making `attended` the default would silently weaken all of them.
//
// WHAT ATTENDED MODE BUYS: the STAGE ORDER, which is JS control flow and does not touch the
// driver at all. That is the property this harness exists to provide, and it is the whole of what
// survives without a run-state file.
//
// WHAT IT LOSES — five things, and they are NOT all refusals, which is why they are listed apart:
//   1. the `--review` ROUND RECORD. Nothing records that an audit round happened; the review
//      artifact under the build's reviews folder is the only trace, and nothing here refuses a run
//      that never files one.
//   2. `--dispatch`'s ORDER REFUSAL — the tree-reading check that a unit is not MISSING, THIN or
//      out of order. What replaces it is weaker BY CONSTRUCTION: an agent's claim about a state
//      the caller resolved, not a refusal the driver made against the tree.
//   3. `--dispatch`'s WRITE-SET RECORD. No declaration of what a pass will write exists.
//   4. `--brief`'s record of what each pass was handed.
//   5. `--rescope`'s amendment row.
//
// AND M4's BLOCKER-DISPOSAL CLAUSE IS UNREACHABLE HERE. `disposal` below is composed only for a
// non-CONVERGED verdict, and attended mode reaches BUILD only at zero blockers, which is the
// terminal one. So a run that must PROMOTE a standing blocker has no route through this mode.
//
// THE S7 WARNING DEPENDS ON THE CALLER AND NOT ON DETECTION. A workflow script has no filesystem,
// so this file cannot see whether a run-state file exists; `runStateExists` is a fact the caller
// supplies, and a caller that supplies nothing gets NO WARNING. That is a real hole and it is
// named here rather than left for a reader to assume away.
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
//   1. THE BUILD STAGE IS ONE AGENT holding the ordered unit list, rather than one agent per unit.
//      The stage order stays structural; per-unit order moves onto `--dispatch`'s refusal, which
//      reads the tree and is therefore a STRONGER check than a JS loop rather than a weaker one.
//      SCOPED TO BUILD AT TOOL-aStagedLane-3, which made the SPEC stage a bounded parallel fan of
//      writers over groups of slices. That does not contradict the ratified `parallelism route:
//      none` above: the verdict failed on E4, two passes COMMITTING without racing one index, and
//      the spec writers author and never commit — the caller commits once after they return.
//      Leaving this claim unscoped would have left the file's own header describing a shape it no
//      longer has, which is the drift class this repository gates for.
//
//   2. THE CONVERGENCE LOOP LIVES IN THE CALLER, and this file holds the GATE. A convergence loop's
//      iteration count is data-dependent by definition, so unlike case 1 there is no bounded unroll.
//      What had to be structural still is: a `CONVERGING` verdict RETURNS without reaching BUILD, so
//      no caller error can build on a spec set the review is still working through. The owner's
//      2026-09-01 ruling survives in the half that matters — the verdict decides, and NO round cap
//      exists anywhere in this file.

// --- cap-5 fan-out, INLINED FROM `tools/workflows/tier2-review.js` (TOOL-aStagedLane-3 S2) ------
// NOT A REUSE — A COPY, and the difference cost this spec two review rounds. `boundedParallel` was
// never in this file: it lives at `tier2-review.js:17` and the copies elsewhere are in the two
// drift-audit workflows. Workflow scripts cannot import, so a second marked copy is the only shape
// available, and `tier2-review.js` REMAINS THE OWNER of the cap literal — this one carries the same
// value and names that file so the two are one figure with a stated source rather than two
// declarations drifting apart.
//
// The marker on the slice line below is what `agent-cap.js` reads to admit the raw primitive. Do not
// spell that token anywhere else in this file, including in prose: the hook scans line by line and
// treats any line carrying it as a marked one, so a comment ABOUT the marker is read as a marker
// claiming a bound over nothing, and denies the whole file. Learned here. Grammar:
// `tools/hooks/README.md`.
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

// TOOL-aStagedLane-2 — the mode argument. What each mode buys and loses is in this file's
// HEADER, above, because that is where a reader looking for the honesty statement goes.
const MODES = ['unattended', 'attended']
const mode = a.mode === undefined ? 'unattended' : a.mode
if (MODES.indexOf(mode) === -1) {
  throw new Error(
    'unattended-build: `mode` must be one of ' + MODES.join(', ') + ', got ' + JSON.stringify(a.mode) +
      '. Refusing rather than defaulting: the mode selects which refusals run, so a typo that fell\n' +
      'back to a default would hand the caller fewer checks than they asked for.',
  )
}
const attended = mode === 'attended'
// S7 - warn and continue, which is the owner's ruling AGAINST this file's own recommendation to
// refuse. A run under a mandate does not get to opt out of the mandate's enforcement by passing an
// argument, but the owner ruled that saying so loudly beats refusing.
if (attended && a.runStateExists === true) {
  log(
    'WARNING: attended mode was requested for `' + slug + '`, and the caller reports a run-state ' +
      'file EXISTS for it. Continuing, but these are skipped: the --review round record, ' +
      "--dispatch's order refusal and write-set record, --brief's record, and --rescope's " +
      'amendment row. If this run is under a mandate, it is now weaker than the mandate requires.',
  )
}

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

// S4c - MODE-AWARE, and this is not cosmetic. In this repository a mandate is precisely the
// authority to merge and push with no owner turn, so a preamble telling an attended run's agents
// they hold one is a falsehood this file would otherwise manufacture — and it prefixed EVERY agent
// in both stages.
const GROUND =
  'You are one stage of a harnessed ' + (attended ? 'ATTENDED' : 'unattended') + ' build in the ' +
  'repository at ' + repo + '. ' +
  'Read `memory/guides/BUILD-METHOD.md` WHOLE before acting; it is the procedure you are bound by. ' +
  'The build is `' + slug + '` and its record is `memory/builds/' + slug + '/`. ' +
  (attended
    ? 'There is an OWNER in the loop: this run holds no mandate, and the driver\'s recording verbs ' +
      'are unavailable because there is no run-state file to record against. '
    : 'Speak only in your return value: nobody reads a transcript under a mandate. ')

// ============================================================== STAGE 1 — SPEC
// TOOL-aStagedLane-3 — A FAN OVER GROUPS OF SLICES, not one agent holding every unit.
//
// WHY IT IS PERMITTED. The parallelism rule requires concurrency where disjointness is PROVEN, in
// three clauses. (1) The write sets are the spec file paths, one per unit, and they do not
// intersect. (2) No writer reads another's output and no spec is a contract input to a sibling.
// (3) No writer touches a shared mutable record — which needs BOTH the generator prohibition in
// each prompt AND the rule that writers AUTHOR and never COMMIT, since every writer is told to
// read BUILD-METHOD whole and M6 orders a commit at the end of every pass. N writers committing
// would contend on one git index, which is the recorded experiment E4 that
// `TOOL-cBriefedPilot-21` ratified `parallelism route: none` on and `TOOL-cBriefedPilot-28`
// records as never actually run. Authoring-only keeps this stage clear of that verdict instead of
// contradicting it unremarked; BUILD dispatch stays strictly sequential.
//
// SLICES COME FROM THE CALLER, grouped by the declared `order` verb — this runtime has no
// filesystem and cannot derive a grouping. The caller's slice count bounds NOTHING, so the slices
// are re-split into at most `SPEC_WRITERS` groups: that bounds the agent TOTAL, which is the
// second of the two rules the charter insists are not one rule, and it is the receiver shape
// `agent-cap.js` can prove bounded.
//
// SO A WRITER HOLDS A GROUP, WHICH ABOVE THE CAP IS MORE THAN ONE SLICE. At seven slices and a cap
// of five there are five groups, two of them carrying two slices. The unit's headline property is
// that a writer holds ITS OWN group's briefs and nothing outside it — not that it holds exactly
// one slice.
phase('Spec')
const SPEC_WRITERS = 5 // the cap `tier2-review.js` owns; this copy carries the same value
const sliceKeys = []
for (const u of ordered) {
  const k = Number.isInteger(u.order) ? String(u.order) : 'unordered'
  if (sliceKeys.indexOf(k) === -1) sliceKeys.push(k)
}
const slices = sliceKeys.map(function (k) {
  return ordered.filter(function (u) {
    return (Number.isInteger(u.order) ? String(u.order) : 'unordered') === k
  })
})
// gov:fixed-verifiers — the bounded receiver. `chunk(x, Math.ceil(x.length / K))` with a resolvable
// K is the sanctioned spelling; the group COUNT is what stands still while the batch grows.
const specGroups = chunk(slices, Math.ceil(slices.length / SPEC_WRITERS)) // gov:fixed-verifiers
log('spec stage: ' + ordered.length + ' unit(s) in ' + slices.length + ' slice(s) -> ' +
    specGroups.length + ' writer(s), each holding only its own group')
// S7 — a unit with no `specBriefPath` falls back to the shared prompt, and SAYS SO. A silent
// fallback and a deliberate omission are otherwise indistinguishable, and a mistyped key would
// hand back the old behaviour with no signal at all.
for (const u of ordered) {
  if (!u.specBriefPath) log('spec stage: ' + u.id + ' has no specBriefPath — falling back to the shared prompt')
}
const specResults = await boundedParallel(
  specGroups.map(function (grp, gi) {
    return function () {
      const gUnits = [].concat.apply([], grp)
      const gRoster = renderRoster(gUnits, slug, briefDir)
      const briefs = gUnits
        .filter(function (u) { return u.specBriefPath })
        .map(function (u) { return u.id + ' -> ' + u.specBriefPath })
      return agent(
        GROUND +
          'SPEC every unit below, IN THIS ORDER. This is YOUR GROUP and it is all you are ' +
          'responsible for; other writers hold the rest of this build concurrently.\n' + gRoster +
          '\n\n' +
          (briefs.length
            ? 'Read the brief for each unit that names one, and no other brief:\n  ' +
              briefs.join('\n  ') + '\n\n'
            : '') +
          'For each: if a conforming spec already carries that id, leave it alone and count it in ' +
          'alreadyPresent. Otherwise author it against `memory/TEMPLATE-SPEC.md` at the tier the ' +
          'kickoff engine assigns, satisfy its section 10 reuse obligation with a real probe rather ' +
          'than a claim, and give its status header the `order` verb this roster names. ' +
          'DO NOT WRITE PRODUCT CODE in this stage. It authors designs and nothing else — a unit ' +
          'built here would be the exact defect this harness exists to remove. ' +
          'AUTHOR ONLY — DO NOT COMMIT, and do not run the build-index generator. You are one of ' +
          'several writers running at once: the caller commits once after all of you return, and ' +
          'regenerates the index once. A writer that commits contends with its siblings on one git ' +
          'index, which is the experiment this repository has NOT run. ' +
          'NAME every unit you could not spec, in `refused`, with the reason in your summary.',
        { label: 'spec:' + slug + ':g' + gi, phase: 'Spec', schema: SPEC_SCHEMA },
      )
    }
  }),
  SPEC_WRITERS,
)
// THE MERGE, and its refusal. A dead writer returns null and its units are REFUSED rather than
// dropped — `degradation-known-but-unreported` is the class where a stage computes its own losses
// and does not report them.
//
// AND AN ALL-DEAD FAN THROWS. The old guard was `if (!specced) throw` on a falsy return; a merged
// object is always truthy, so without this an entirely dead spec stage would present as a clean
// object with empty arrays and reach AUDIT and BUILD on whatever specs already existed. That is
// the refusal this file spends six lines justifying, deleted by accident.
const specced = { authored: [], alreadyPresent: [], refused: [], summary: '' }
let liveWriters = 0
specResults.forEach(function (r, gi) {
  const gUnits = [].concat.apply([], specGroups[gi] || [])
  if (!r) {
    gUnits.forEach(function (u) { specced.refused.push(u.id) })
    specced.summary += 'group ' + gi + ' returned nothing; '
    return
  }
  liveWriters++
  ;['authored', 'alreadyPresent', 'refused'].forEach(function (k) {
    if (Array.isArray(r[k])) specced[k] = specced[k].concat(r[k])
  })
  specced.summary += 'group ' + gi + ': ' + (r.summary || '(no summary)') + '; '
})
if (!specResults.length || liveWriters === 0) {
  throw new Error(
    'unattended-build: EVERY spec writer returned nothing (' + specGroups.length + ' group(s)), so ' +
      'no unit is known to have a design. That is a refusal and not an empty pass: continuing ' +
      'would put the BUILD stage on a spec set nothing confirmed exists. A merged return is always ' +
      'truthy, so this is checked on the LIVE WRITER COUNT and not on the object.',
  )
}
if (liveWriters < specGroups.length) {
  log('spec stage: DEGRADED — ' + (specGroups.length - liveWriters) + ' of ' + specGroups.length +
      ' writer(s) returned nothing; their units are in `refused`')
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
// S2/S3 - IN ATTENDED MODE THE DRIVER IS NOT REACHED, so no agent is spawned to record the round.
// The verdict is computed from the blocker count alone: 0 is terminal, a positive integer is
// converging. That is a PER-ROUND verdict and not the driver's SEQUENCE-derived one — convergence
// is a property of the sequence of rounds and no JS here can see it — so the tokens are the two
// this mode can honestly produce and no more.
//
// `CONVERGED` AT ZERO IS THE ONLY TERMINAL THIS MODE HAS. `NON-CONVERGENT` and `CEILING` are
// sequence verdicts, so a run needing M4's blocker disposal cannot get one here, which is what the
// header means by the disposal clause being unreachable.
//
// The non-integer case is already refused above, in BOTH modes, and must stay so: `tier2-review.js`
// yields `blockers: null` on its degraded paths BY DESIGN, and reading null as 0 would make every
// degraded audit look clean.
const rv = attended
  ? { token: auRaw.blockers === 0 ? 'CONVERGED' : 'CONVERGING', exitCode: 0 }
  : await agent(
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
if (attended) log('attended mode: verdict computed from the blocker count; no round was recorded')
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
// S4/S4b - THE PER-UNIT REFUSAL, and in attended mode it happens HERE rather than at `--dispatch`.
// Three verbs the unattended prompt names hard-refuse without a run-state file — `--dispatch`
// (fail 49), `--brief` (fail 49) and `--rescope` (fail 48) — and the prompt tells the agent that a
// refusal means the order is wrong and to STOP. Left unchanged, attended mode would halt at unit
// one AFTER units were already being written: strictly worse than the refusal it traded away.
//
// THE STATE COMES FROM THE CALLER, resolved ONCE from `--plan` at entry, because this script has
// no shell and there is no point between the stages at which a caller could re-run it.
//
// MATCHED AS A PREFIX ON `DONE`, never against a closed token set. `--plan` prints `DONE ($state)`
// for a terminal unit whose underlying grade is not READY, so the live vocabulary includes
// `DONE (THIN)` and `DONE (FORKED)`. A five-token allow-list halts on the first such unit.
//
// AND THE ENTRY-TIME VALUE IS STALE BY CONSTRUCTION for the units stage 1 authors: a fresh build
// reports MISSING for every one of them. So a unit this invocation SPECCED is treated as READY
// whatever it reported at entry — otherwise the stage refuses the build it just specced.
const speccedNow = []
  .concat(Array.isArray(specced.authored) ? specced.authored : [])
  .concat(Array.isArray(specced.alreadyPresent) ? specced.alreadyPresent : [])
let planRefusal = ''
const skippedDone = []
if (attended) {
  for (const u of ordered) {
    if (speccedNow.indexOf(u.id) !== -1) continue
    const st = u.planState
    if (typeof st !== 'string' || !st) {
      planRefusal =
        'unattended-build: attended mode requires a `planState` on every units[] entry, resolved by ' +
        'the caller from `' + DRIVER + ' --plan ' + slug + '`, and ' + u.id + ' carries none. ' +
        'Refusing rather than defaulting: a defaulted state puts the refusal predicate to work on a ' +
        'value nobody supplied.'
      break
    }
    if (st.indexOf('DONE') === 0) { skippedDone.push(u.id); continue }
    if (st === 'READY') continue
    if (st === 'MISSING' || st === 'THIN' || st === 'FORKED') {
      planRefusal =
        'unattended-build: attended mode refuses ' + u.id + ' — `--plan` grades it ' + st + ', and ' +
        'this stage builds only a unit that is READY or already terminal. This is the refusal ' +
        '`--dispatch` would have made against the tree; here it is a claim about a state the caller ' +
        'resolved, which is weaker.'
      break
    }
    planRefusal =
      'unattended-build: attended mode does not recognise the state ' + JSON.stringify(st) + ' for ' +
      u.id + '. Neither building nor skipping an unknown state is safe, so it refuses by name.'
    break
  }
  if (planRefusal) throw new Error(planRefusal)
  if (skippedDone.length) log('attended mode: SKIPPING ' + skippedDone.length + ' terminal unit(s) — ' + skippedDone.join(', '))
}
const driverSteps = attended
  ? 'This run has NO run-state file, so the driver\'s recording verbs are unavailable and you must ' +
    'not call them: --dispatch, --brief and --rescope all refuse without one. Write down the paths ' +
    'each pass will touch before you touch them anyway — the declaration is what makes disjointness ' +
    'checkable, and here only you can check it. '
  : 'Before writing, declare the write set with `' + DRIVER + ' --dispatch ' + slug +
    ' --pass <unit-id> --writes <path>`, and record what you were handed with `' + DRIVER +
    ' --brief ' + slug + ' --unit <unit-id> --path <the brief>`. THAT DISPATCH IS THE ORDER GATE: it ' +
    'refuses a unit that is MISSING, THIN or out of the declared order, and a refusal is this ' +
    'harness telling you the order is wrong. Read it and stop — do not work around it. '
const built = await agent(
  GROUND +
    disposal +
    'BUILD every unit below, ONE AT A TIME and IN THIS ORDER. Never start one before the previous ' +
    'has committed:\n' + roster + '\n\n' +
    'For each unit you are handed exactly two documents and you read both before touching code: its ' +
    'BRIEF and its SPEC, both named in the roster. The spec is the design; where you must diverge ' +
    'from it, CHANGE THE SPEC FIRST as a `rev-N` bump with its section 9 line, then write the code. ' +
    driverSteps +
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
  mode: mode,
  base: base,
  round: roundNo,
  units: ordered.length,
  specced: speccedCount,
  specRefused: specRefused,
  verdict: verdict,
  blockers: au.blockers,
  lastReport: lastReport,
  skippedTerminal: skippedDone,
  built: Array.isArray(built.committed) ? built.committed.length : 0,
  unbuilt: unbuilt,
  // THE MODE IS PART OF THE RUN-INTEGRITY REPORT, not decoration. `degradation-known-but-unreported`
  // is the class where a pipeline computes how weak its own run was and then does not say so where a
  // reader looks. An attended run that returns a bare 'complete' has skipped five checks an
  // unattended one performs, and the caller cannot tell the two apart from this field.
  note:
    specRefused.length || unbuilt.length || verdict !== 'CONVERGED'
      ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused, ' + unbuilt.length +
        ' unit(s) unbuilt, verdict ' + verdict + (attended ? ' · ATTENDED, so no driver-side check ran' : '')
      : attended
        ? 'complete for ATTENDED mode — stage order held, and none of the five driver-side records or ' +
          'refusals ran; this is NOT the guarantee an unattended run gives'
        : 'complete',
}

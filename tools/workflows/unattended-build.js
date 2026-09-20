export const meta = {
  name: 'unattended-build',
  version: '1.2', // gov:kit unattended-build@1.2 — engine identity (the .template.js is the source; the .js beside it is RENDERED by check-protocol-parity.test.sh --render)
  description:
    'Runs a build SPEC -> AUDIT -> DISPOSAL as ordered stages of ONE program, then hands the caller an ordered roster and stops. Stage order is a property of control flow rather than of an agent recollection across a context that compacts, and the roster is unreachable unless the audit verdict is terminal. AUDIT is opt-in: with no `specAudit` arg the stage announces itself OFF by declaration and the roster follows SPEC completion.',
  phases: [
    { title: 'Spec', detail: 'author every missing spec, in the declared order, no code' },
    { title: 'Audit', detail: 'delegate to tier2-review.js as a spec-audit; record the round, after the disposal at zero blockers so the disposition field is what was promoted. Only when `specAudit` is declared: absent, the stage logs OFF by declaration and delegates nothing' },
    { title: 'Disposal', detail: 'dispose every confirmed and unverified finding by severity over the whole spec set, then hand out the roster, withheld on a clean round until its spec-audit record exists' },
  ],
}

// ---------------------------------------------------------------------------------------------
// WHAT THIS BUYS AND WHAT IT CANNOT BUY, first, because the second half is the one a reader will
// otherwise assume away.
//
// IT BUYS STAGE ORDER. The SPEC stage's await completes before the AUDIT stage begins, and the
// ROSTER HAND-OUT is unreachable except through both AND through a terminal audit verdict. That is
// JS control flow, not a rule anybody remembers, and it is the whole mechanism: a unit cannot be
// dispatched before it is specced inside a harnessed run. It is the defect the owner's prompt reports — "build can run
// BEFORE they are specced with spec written postfactum" — and the one this file closes.
// THE AUDIT STAGE IS OPT-IN (TOOL-aBlindedTrial-3). It runs only when `args.specAudit` carries the
// `spec-audit: <date>` override the driver's preflight read off the build README; absent, the stage
// logs OFF by declaration, awaits nothing, and the hand-out follows SPEC. The owner's ruling of
// 2026-09-20 is "forbidden unless overridden", so a default that audited when nobody asked would be
// the behaviour being retired — and a runtime with no filesystem cannot read the README itself, so
// the fact arrives as an argument like `runStateExists` does.
//
// IT CANNOT BUY ENFORCEMENT. A Workflow script has NO FILESYSTEM. Every observation it makes is a
// claim its own agent returned, so nothing here can verify that a spec exists, that a gate passed, or
// that a commit happened. The refusal that makes the order real lives in the driver, where the tree
// is readable — and it refuses LESS than this sentence used to claim. `--dispatch` refuses a unit no
// tracked spec defines (MISSING) and one whose spec grades THIN, both unconditionally; it grades
// ORDER only where THIS unit AND the sibling ahead of it BOTH carry an `order` verb, so the order arm
// is CONDITIONAL and a sibling carrying none stops blocking. The `pass-order history` leg refuses a
// CLOSED unit whose build commit predates a conforming spec for it. A stage in this file claiming to
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
//   2. `--dispatch`'s SPEC-STATE AND ORDER REFUSAL — the tree-reading checks that a unit is neither
//      MISSING nor THIN, plus an order check that fires only where this unit and the sibling ahead
//      of it BOTH carry an `order` verb. What replaces it is weaker BY CONSTRUCTION: an agent's
//      claim about a state the caller resolved, not a refusal the driver made against the tree.
//   3. `--dispatch`'s WRITE-SET RECORD. No declaration of what a pass will write exists.
//   4. `--brief`'s record of what each pass was handed.
//   5. `--rescope`'s amendment row.
//
// AND M4's DISPOSAL CLAUSE IS REACHABLE HERE SINCE TOOL-aProbedUnit-7. The DISPOSAL STAGE below
// runs on the CONFIRMED COUNT and not on the verdict, so attended mode — whose verdict is computed
// from the blocker count and reaches the hand-out only at zero blockers, the CONVERGED one — still
// reaches the stage whenever highs, mediums or lows stand confirmed. What it loses there is the
// `--rescope` row: a promotion in this mode is a README roster row and a spec, with no amendment
// record behind it.
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
// The `agent-cap.js` hook refused an `agent()` inside ANY loop body when this file was written,
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
//   1. THE DISPOSAL STAGE IS ONE AGENT over the whole spec set, rather than one per blocker — and
//      since TOOL-aHoistedPass-6 it is the ONLY stage the one-agent shape applies to. The BUILD
//      stage that held the ordered unit list is GONE: the units are handed back to the caller as an
//      ordered roster, and the caller makes one main-loop `Workflow` call per unit, which is a call
//      the fan-out hook actually sees. Per-unit order rests on `--dispatch`'s refusal, which reads
//      the tree — stronger than a JS loop where it fires, and CONDITIONAL on both this unit and the
//      sibling ahead of it carrying an `order` verb.
//      THE SPEC STAGE IS A BOUNDED PARALLEL FAN at TOOL-aStagedLane-3, of writers over groups of
//      slices. That does not contradict the ratified `parallelism route:
//      none` above: the verdict failed on E4, two passes COMMITTING without racing one index, and
//      the spec writers author and never commit — the caller commits once after they return.
//      Leaving this claim unscoped would have left the file's own header describing a shape it no
//      longer has, which is the drift class this repository gates for.
//
//   2. THE CONVERGENCE LOOP LIVES IN THE CALLER, and this file holds the GATE. A convergence loop's
//      iteration count is data-dependent by definition, so unlike case 1 there is no bounded unroll.
//      What had to be structural still is: a `CONVERGING` verdict RETURNS an EMPTY roster, so no
//      caller error can build on a spec set the review is still working through. The owner's
//      2026-09-01 ruling survives in the half that matters — the verdict decides, and NO round cap
//      exists anywhere in this file.

// --- cap-5 fan-out, INLINED FROM THE SIBLING REVIEW HARNESS (TOOL-aStagedLane-3 S2) ----------
// NOT A REUSE — A COPY, and the difference cost this spec two review rounds. `boundedParallel` was
// never in this file: it lives at that harness's line 17 and the copies elsewhere are in the two
// drift-audit workflows. Workflow scripts cannot import, so a second marked copy is the only shape
// available, and `tier2-review.js` REMAINS THE OWNER of the cap literal — this one carries the same
// value and names that file so the two are one figure with a stated source rather than two
// declarations drifting apart.
//
// The marker on the slice line below is what `agent-cap.js` reads to admit the raw primitive. Do not
// spell that token anywhere else in this file, including in prose: the hook scans line by line and
// treats any line carrying it as a marked one, so a comment ABOUT the marker is read as a marker
// claiming a bound over nothing, and denies the whole file. Learned here. Grammar:
// the hooks kit's own README.
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
//   scratch: "<absolute session scratchpad>",       // REQUIRED — the path the caller's OWN system prompt names
//   base: "<immutable sha>",                        // the review anchor, for the record
//   units: [{ id, order, specPath, briefPath,      // ORDERED by the caller, from --plan
//            specBriefPath,                        //   optional: the per-unit SPEC brief
//            planState }],                         //   REQUIRED in attended mode, from --plan
//   mode: "unattended" | "attended",              // DEFAULTS to "unattended"
//   runStateExists: <bool>,                         // caller-supplied; this script cannot detect it
//   specAudit: "<YYYY-MM-DD>",                      // the README front-matter `spec-audit:` override the
//                                                   //   driver's preflight pinned; ABSENT = the audit is
//                                                   //   OFF by declaration and the roster follows SPEC
//   briefDir: "memory/builds/<slug>/prompts",
//   reviewDir: "memory/builds/<slug>/reviews",
//   round: <integer>,                               // which audit round this invocation is
//   auditIds: [<unit id>],                          // AFTER A DISPOSAL: the `promotedIds` the previous
//                                                   //   hand-out returned — the specs no spec-audit record
//                                                   //   names yet; the audit is scoped to them
//   subjectRound: <integer>                         // ON A FOLD RE-INVOKE: the round the current subject
//                                                   //   set was first audited at, copied from the CONVERGING
//                                                   //   return; keeps the driver's sequence on ONE subject
// }
//
// THE REVIEW SUBJECT IS KEYED PER SPEC-SET GENERATION (closing review round 1, cluster B). It was the
// literal `<slug>-spec-set`, so a unit the DISPOSAL stage promoted had no audit route: the subject
// was terminal after its one round, `verb_review` refused a second, and the promoted spec was built
// unaudited. The key is `<slug>-spec-set-r<N>` where N is the round the generation was FIRST audited
// at — `subjectRound` when the caller carries it, this invocation's round otherwise. Keying on the
// invocation round ALONE would reset the driver's sequence on every fold under `REVIEW_ROUNDS` > 1,
// so BOUNDED and NON-CONVERGENT could never fire and the loop had no end; the CONVERGING return
// carries `subjectRound` back so the caller copies it rather than derives it.
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
// TOOL-aProbedUnit-4 — the session scratchpad is in the CALLER's system prompt and nowhere a
// workflow script can read, so it arrives as an argument and is refused by SHAPE: absolute means
// `/` or a drive letter and a separator, which is the only test a runtime with no filesystem can
// make. Folded to forward slashes ONCE, here, because the value crosses into a bash-quoted prompt
// and a hand-out JSON object and a backslash survives neither reliably; every carrier below reads
// the folded const.
if (typeof cfg.scratch !== 'string' || !/^(\/|[A-Za-z]:[\\/])/.test(cfg.scratch)) {
  throw new Error(
    'unattended-build: args must carry an explicit `scratch`, an ABSOLUTE path to the session ' +
      'scratchpad — the one the caller\'s own system prompt names. Got ' + JSON.stringify(cfg.scratch) +
      '. Refusing to default it: a defaulted scratch root is the floating temp dir this argument exists to end.',
  )
}
const scratch = cfg.scratch.replace(/\\/g, '/')
const a = cfg
const repo = a.repo
const slug = a.slug
const base = a.base || ''
const briefDir = a.briefDir || 'memory/builds/' + slug + '/prompts'
const reviewDir = a.reviewDir || 'memory/builds/' + slug + '/reviews'
const units = Array.isArray(a.units) ? a.units : []
if (!units.length) {
  throw new Error(
    'unattended-build: args carries no `units`. The caller derives them from `--plan <slug> --paths`, ' +
      'which takes its set and ORDER from the generated units region and emits each unit\'s spec ' +
      'path beside it; a harness with an empty set would report a clean run over nothing, which is ' +
      'the vacuous-selector shape this repo refuses.',
  )
}
// PRESENT-BUT-WRONG-TYPED REFUSES BY NAME (closing review round 2, cluster G), like `mode`, `scratch`
// and `units` below. These three used to fold to their defaults: a string `subjectRound` — the `"2"` an
// agent copying a log line produces — became the invocation round, which keys a FRESH subject on every
// fold and resets the driver's sequence, so under `REVIEW_ROUNDS` > 1 BOUNDED and NON-CONVERGENT could
// never fire; a string `auditIds` became the whole set, re-auditing the subject a terminal round closed.
// `specAudit` joins the table (TOOL-aBlindedTrial-3): a truthy non-string — `true`, `1`, the
// `"later"` a README typo produces — must refuse rather than switch the audit ON, and a string that is
// not a date is the same class; the driver refuses the same shape at preflight.
const TYPED = [
  ['round', Number.isInteger(a.round) && a.round > 0, 'a positive integer'],
  ['subjectRound', Number.isInteger(a.subjectRound) && a.subjectRound > 0, 'a positive integer'],
  ['auditIds', Array.isArray(a.auditIds), 'an array of unit ids'],
  ['specAudit', typeof a.specAudit === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(a.specAudit), 'a YYYY-MM-DD date string'],
]
for (const t of TYPED) {
  if (a[t[0]] !== undefined && !t[1]) {
    throw new Error(
      'unattended-build: `' + t[0] + '` must be ' + t[2] + ' when present, got ' + JSON.stringify(a[t[0]]) +
        '. Refusing rather than defaulting: a defaulted value puts the subject key and the audit scope to ' +
        'work on a value nobody supplied.',
    )
  }
}
const roundNo = a.round === undefined ? 1 : a.round
const subjectRound = a.subjectRound === undefined ? roundNo : a.subjectRound
const subject = slug + '-spec-set-r' + subjectRound
const auditIds = a.auditIds === undefined ? [] : a.auditIds
// THE AUDIT IS OPT-IN, and absent means OFF (TOOL-aBlindedTrial-3, F1 resolved). Every audit-shaped
// argument beside no declaration is an IMPOSSIBLE PAIRING, refused by name like the others below: a
// caller-pinned subject set, a post-disposal scope and a fold re-invoke each presuppose a round that,
// with the audit off, never ran — so the shape is a re-invoke of an audit that did not happen, and a
// runtime that cannot read the README cannot tell which half the caller meant.
const specAudit = a.specAudit !== undefined
const auditShaped = ['subjects', 'auditIds', 'subjectRound'].filter(function (k) { return a[k] !== undefined })
if (!specAudit && auditShaped.length) {
  throw new Error(
    'unattended-build: `' + auditShaped.join('` and `') + '` is present beside no `specAudit`. Those ' +
      'arguments exist only for an audit round, and with the audit OFF by declaration none ran, so ' +
      'this is a re-invoke of an audit that never happened. Drop them, or pass the build README\'s ' +
      '`spec-audit: <date>` value as `specAudit` — the driver\'s preflight line names which the build declared.',
  )
}
if (subjectRound > roundNo) {
  throw new Error(
    'unattended-build: `subjectRound` ' + subjectRound + ' is above `round` ' + roundNo + '. A subject ' +
      'set cannot have been first audited at a round that has not happened; copy the value the ' +
      'CONVERGING return handed back rather than composing one.',
  )
}
const strayAudit = auditIds.filter(function (id) {
  return !units.some(function (u) { return u.id === id })
})
if (strayAudit.length) {
  throw new Error(
    'unattended-build: `auditIds` names ' + strayAudit.join(', ') + ', which `units` does not carry. ' +
      'The audit is scoped to those ids, so a promoted unit missing from the roster would be ' +
      'silently dropped from the one audit it is owed; re-read `--plan <slug> --paths` and pass ' +
      'every unit.',
  )
}
// `auditIds` OR `subjects`, NEVER BOTH (closing review round 2, cluster C). A caller-supplied subject
// set skips the resolver, and the resolver is the ONLY place the scoping applies: with both present
// the audit ran over the caller's set under the fresh key, logged `scoped to`, and rostered the
// promoted unit with its spec never audited. A runtime with no filesystem cannot intersect the two —
// it cannot read which spec a unit has — so it refuses the pair rather than guessing.
if (auditIds.length && Array.isArray(a.subjects)) {
  throw new Error(
    'unattended-build: pass `auditIds` OR `subjects`, never both — a supplied subject set cannot be ' +
      'scoped to the promoted units by a runtime that cannot read their specs. Drop `subjects` and ' +
      'the resolver stage pins ' + auditIds.join(', ') + ' itself.',
  )
}

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
// THE BUG-CLASS CHECKLIST TRAVELS IN `dispatch.args`. It used to be spelled inside the BUILD prompt
// this unit deletes, and the child cannot carry it: a shipped kit file names nothing outside itself
// by literal, so it lives in the parent, whose install paths are filled in when it is rendered.
const CHECKLIST = 'python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD'
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
// the prompt says verbatim and the enum is re-checked on this side regardless. `terminalSubject` is
// the ONE refusal that comes back as its own outcome rather than as stderr: the driver refusing a
// round on a subject that already exited means the harness re-keyed nothing, and the throw must say
// that, not "the round was not recorded" (closing review round 1, cluster B).
const REVIEW_RECORD_SCHEMA = {
  type: 'object',
  properties: {
    token: { type: 'string' },
    exitCode: { type: 'integer' },
    stderr: { type: 'string' },
    terminalSubject: { type: 'boolean' },
  },
  // `token` is no longer REQUIRED by the schema, because the terminal-subject refusal has none to
  // return; the check on this side refuses a missing token by name, so nothing is weaker.
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
// THE BUILD STAGE'S RETURN SCHEMA LIVED HERE AND IS GONE TOO (TOOL-aHoistedPass-6), for the same
// reason: it bound an AGENT return this program no longer produces. Unlike the one above, nothing
// of it was load-bearing — the roster is a plain return and the caller's own child validates its
// unit — so there is no enum to rescue. Its identifier is deliberately NOT spelled here: an absence
// grep over it is what proves no `schema:` option still points at a constant that is gone.
//
// The DISPOSAL stage's return follows the rule two paragraphs up: the list of what it did NOT do is
// its own required field, never an absence. An empty `standing` with no key at all is
// indistinguishable from a stage that disposed everything. `promoted` and `folded` are COUNTS OF
// FINDINGS by report id, and the guard below reconciles the three against the confirmed and
// unverified findings together, AND splits them by severity: a return whose numbers do not add up
// is the `{disposed: true, standing: ['b1']}` contradiction with the contradiction moved into two
// integers, and `minimum: 0` refuses a negative one at validation. `promotedIds` names the UNITS
// the promotions became, so the caller can scope the next audit to them (cluster B). `refuted` is
// OPTIONAL and counts UNVERIFIED findings only (closing review round 2, cluster F): the stage stands
// in for the skeptic a dead batch never ran, and a skeptic's one verdict the severity rule cannot
// supply is "not a defect" — without it a false positive had to become a unit, a false rev-N line,
// or a standing item that stalled the run. The guard bounds it by `unverified`.
const DISPOSAL_SCHEMA = {
  type: 'object',
  required: ['disposed', 'standing', 'promoted', 'folded', 'promotedIds', 'summary'],
  additionalProperties: true,
  properties: {
    disposed: { type: 'boolean' },
    standing: { type: 'array', items: { type: 'string' } },
    promoted: { type: 'integer', minimum: 0 },
    folded: { type: 'integer', minimum: 0 },
    refuted: { type: 'integer', minimum: 0 },
    promotedIds: { type: 'array', items: { type: 'string' } },
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
  'No stage of this program runs the merge bar or a self-test suite, and neither does any agent it ' +
  'spawns; a unit verifies with the direct check its spec names, and the bar runs once at the main ' +
  'loop after the last unit is terminal. ' +
  'The build is `' + slug + '` and its record is `memory/builds/' + slug + '/`. ' +
  // TOOL-aProbedUnit-4 — ONE sentence, in GROUND so it reaches every agent this file spawns and
  // every child it dispatches through `cfg.ground`. OTHER is load-bearing: the scratchpad is itself
  // outside the repository, so without it the last clause forbids the destination the first names.
  // The exception is unit 3's discovery: a clone under a ~170-character scratchpad exceeds MAX_PATH
  // on Windows whatever git's long-path setting says, and the fallback it took was an untracked dir INSIDE
  // the worktree, which a stray `git add -A` commits.
  'Every temporary file, backup, probe or log this run makes goes under ' + scratch +
  ', spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp, a bare mktemp, or any OTHER path outside the repository. ' +
  'The ONE exception is a git clone or a fixture repository, which needs a SHORT path on Windows because ' +
  'that scratchpad path is long enough that a clone under it fails with Filename too long: it goes under ' +
  '%TEMP%/<short-name>, never inside the worktree and never at a drive root. ' +
  (attended
    ? 'There is an OWNER in the loop: this run holds no mandate, and the driver\'s recording verbs ' +
      'are unavailable because there is no run-state file to record against. '
    : 'Speak only in your return value: nobody reads a transcript under a mandate. ') +
  // TOOL-aProbedUnit-1 — mode-independent, and it reaches the SPEC writers, who write section 7 and
  // are not children. No path: this travels in `dispatch.args`, which arm (v) scans.
  'No gate, suite or bar runs inside a unit pass: the merge bar runs ONCE, at the close, so a ' +
  'spec\'s section 7 lists what the close runs, and a pass verifies with the one check that ' +
  'exercises its change. '

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
// contradicting it unremarked; PER-UNIT DISPATCH IS STRICTLY SEQUENTIAL and is the caller's, made
// one main-loop `Workflow` call at a time off the roster this program returns.
//
// SLICES COME FROM THE CALLER, grouped by the declared `order` verb — this runtime has no
// filesystem and cannot derive a grouping. The caller's slice count bounds NOTHING, so the slices
// are re-split into at most `SPEC_WRITERS` groups: that bounds the agent TOTAL, which is the
// second of the two rules the charter insists are not one rule, and it is the receiver shape
// `agent-cap.js` can prove bounded.
//
// SO A WRITER HOLDS A GROUP, WHICH ABOVE THE CAP IS MORE THAN ONE SLICE. `chunk` splits by SIZE
// `ceil(N/K)`, so the group COUNT is at most K and is often less: at seven slices and a cap of five
// the size is two, giving FOUR groups of 2, 2, 2 and 1. The guarantee is the bound, not the
// equality — and the headline property is that a writer holds ITS OWN group's briefs and nothing
// outside it, never that it holds exactly one slice.
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
          'Every acceptance criterion names a DIRECT observation with its command — a checker on a staged ' +
          'break, a `--selftest` flag, a fixture, a grep over a rendered file — never the merge bar, a ' +
          'GATE_*= prefix or a *.test.sh suite: a unit whose criterion names one runs it and stalls for hours. ' +
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
// object with empty arrays and reach AUDIT and the hand-out on whatever specs already existed. That is
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
      'hand out a roster over a spec set nothing confirmed exists. A merged return is always ' +
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
// that yields an INTEGER. Its other returns yield `blockers: null` BY DESIGN — null, never 0, so a
// stated absence cannot be read as a clean bill — and `unattended.sh` emits CONVERGED only on a
// count of 0 while refusing a non-integer. Which of those null returns is a clean RESULT and which
// a degraded run is decided below on the callee's own `lensesDead` and `unverified` fields, never
// by reading the null as 0.
phase('Audit')
// THE STAGE IS OPT-IN, AND OFF IS LOUD (TOOL-aBlindedTrial-3). The phase still opens, because a phase
// that silently vanished would be indistinguishable from a harness that forgot it; what it does with
// the audit off is announce that, once, and then every `specAudit &&` guard below keeps the resolver,
// the sub-workflow, the adapter's refusals, the round record and the disposal agent from running. The
// counts they would have produced are stated NULLS on the return, never zeros: nothing was counted.
if (!specAudit) {
  log('audit stage: OFF by declaration — no spec-audit: key on the build README (TOOL-aBlindedTrial-6); ' +
    'the roster is handed out on SPEC completion. No sub-workflow is awaited, no round is recorded, and ' +
    'the verdict below reads NOT-OWED rather than a clean bill nothing earned.')
}
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
// to stop being delegated to something that cannot perform it. Nesting is a DEPTH limit and not a
// ration one caller uses up: a parent may make several sequential nested calls at the same depth.
// The evidence is `wf_9b984206-816`, whose three sequential `await workflow()` calls all returned —
// CARRIED from an earlier pass and NOT re-run here, which is said rather than asserted as measured.
// Under the roster hand-out the point is close to moot, since each unit is dispatched by the caller
// at depth zero; which is exactly why a stale sentence about it would sit unread until it misled
// somebody.
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
// SCOPED AFTER A DISPOSAL. With `auditIds` the resolver sees only the promoted units, so the audit
// reads the specs no spec-audit record names yet and not the whole set a terminal round already
// closed; the subject key above is what lets the driver accept that round at all.
const auditUnits = auditIds.length
  ? ordered.filter(function (u) { return auditIds.indexOf(u.id) !== -1 })
  : ordered
if (specAudit && !subjects) {
  // LOGGED HERE, where the scoping is APPLIED, and not beside the filter above: the line used to fire
  // on `auditIds.length` alone and asserted a scoping a supplied `subjects` had bypassed. The pair is
  // refused at the args block now, so this branch is the only one `auditIds` can reach.
  if (auditIds.length) log('audit round ' + roundNo + ': scoped to ' + auditIds.length + ' promoted unit(s) — ' + auditIds.join(', ') + ' · subject ' + subject)
  const res = await agent(
    GROUND +
      'Resolve the blob of every spec in this build so an audit can be pinned at immutable bytes.\n' +
      renderRoster(auditUnits, slug, briefDir) + '\n\n' +
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
if (specAudit && !subjects.length) {
  throw new Error(
    'unattended-build: no spec subjects could be pinned at round ' + roundNo + '. A spec-audit over ' +
      'an empty subject set would grade nothing and report it as a clean round, which is the exact ' +
      'shape this stage exists to prevent.',
  )
}
const badSubject = !specAudit ? -1 : subjects.findIndex(function (s) {
  return !s || typeof s.path !== 'string' || !s.path || !/^[0-9a-f]{7,40}$/.test(String(s.blob || ''))
})
if (badSubject !== -1) {
  throw new Error(
    'unattended-build: subject ' + badSubject + ' is not a {path, blob} with a 7-40 hex blob: ' +
      JSON.stringify(subjects[badSubject]) + '. An unpinned subject is an audit of whatever the ' +
      'file happens to say when the lens reads it, which is not a review of anything in particular.',
  )
}

// `null` WITH THE AUDIT OFF, and null is the right word: the adapter below reads `auRaw` as the callee's
// return, and the callee was never called. Every check it runs is guarded on `specAudit`, so a null
// here is never mistaken for the dead sub-workflow the first guard refuses.
const auRaw = !specAudit ? null : await workflow(
  { scriptPath: 'tools/workflows/tier2-review.js' },
  {
    kind: 'spec-audit',
    repo: repo,
    // THE CALLEE'S ROUND IS THE SUBJECT'S, NOT THE INVOCATION'S (closing review round 2, cluster E).
    // `tier2-review.js` primes every lens as a FOLD review at any round above 1 and labels its report
    // with it, and under the kit default every promoted-spec audit lands at an invocation round of 2
    // or more — over a spec nobody has reviewed. 1 for a fresh generation, N for its Nth fold;
    // `roundNo` stays the harness's own label.
    round: roundNo - subjectRound + 1,
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
// WHO OWNS THE VERDICT VOCABULARY. `CONVERGING|CONVERGED|NON-CONVERGENT|CEILING|BOUNDED` is produced by
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
if (specAudit && (!auRaw || typeof auRaw !== 'object' ||
    (!Object.prototype.hasOwnProperty.call(auRaw, 'blockers') && !auRaw.report))) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned nothing at round ' + roundNo + '. That is a ' +
      'refusal and not a convergence: an absent verdict must never read as CONVERGED, because that ' +
      'token is the only thing between this harness and building on an unreviewed spec set.',
  )
}
// THE CALLEE'S EARLY RETURNS CARRY `confirmed: []` AND `blockers: null`, and they are NOT all
// degraded (closing review round 1, cluster F). `tier2-review.js` returns that pairing on four
// paths: every lens dead; no lens raised a finding; every finding refuted; and, with `confirmed` an
// INTEGER, a dead synthesis. Only the last three lines of that file's own `note` say which; its
// FIELDS say it too, and those are what is read here. An empty confirmed ARRAY beside `lensesDead`
// 0 and no unverified finding is the cleanest audit there is — a RESULT at 0 — and this harness
// used to halt it as "a DEGRADED run". `unverified` is absent on the zero-findings path, because no
// verify phase ran to leave one, and `0` on the all-refuted path; both are read, and nothing else
// is. A dead lens beside the same pairing is the one degraded shape, and it keeps the throw below.
// AND A CLEAN ROUND NEEDS AN AUDIT TO HAVE RUN. With the audit off there is no callee return to read,
// and `false` here is what keeps the OFF path off the clean-round log, the record-at-0 and the
// withheld hand-out below: an audit that did not run is not a clean one.
const cleanRound = specAudit && Array.isArray(auRaw.confirmed) && auRaw.confirmed.length === 0 &&
  auRaw.blockers === null && auRaw.lensesDead === 0 &&
  (auRaw.unverified === 0 || auRaw.unverified === undefined)
if (cleanRound) {
  log('audit round ' + roundNo + ': the callee confirmed nothing and no lens died — a clean round at 0' +
    ', with no report written (' + (typeof auRaw.note === 'string' ? auRaw.note : 'no note') + ')')
}
// THE BLOCKER COUNT MUST BE AN INTEGER, and `null` is the DEGRADED signal `tier2-review.js` yields
// by design — null, never 0, so a stated absence cannot be read as a clean bill. Reading a null as
// 0 would make every degraded audit look clean, since 0 is the only count that converges. The throw
// names the lens and skeptic deaths the callee counted, so the operator reads WHY and not only THAT.
if (specAudit && !cleanRound && !Number.isInteger(auRaw.blockers)) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned a non-integer blocker count (' +
      JSON.stringify(auRaw.blockers) + ') at round ' + roundNo + ' — lensesDead ' +
      JSON.stringify(auRaw.lensesDead) + ', skepticsDead ' + JSON.stringify(auRaw.skepticsDead) +
      ', note ' + JSON.stringify(auRaw.note) + '. That is a DEGRADED run and it ' +
      'is reported as one; it is never rounded to zero.',
  )
}
// THE COUNTS THE DISPOSAL STAGE DECIDES ON ARE READ, NOT ASSUMED. `tier2-review.js` returns
// `confirmed` as the size of the skeptic-confirmed set, `unverified` as the size of the set no
// usable skeptic verdict came back for — OUTSTANDING, not cleared, in the callee's own words — and
// `blockers`/`highs` as the synthesis pass's counts WITHIN the confirmed set, so each is an integer
// and the two severities sum to at most the set. This is written for the callee that CHANGES,
// because `undefined > 0` is `false` and a `confirmed` or `unverified` key that quietly went
// missing would skip the stage on every round — the false-clean shape this file refuses by name
// three times over. One refusal for four conditions, because they have one remedy: the return
// cannot be read as the contract it declares.
if (specAudit && !cleanRound && (!Number.isInteger(auRaw.confirmed) || !Number.isInteger(auRaw.highs) ||
    !Number.isInteger(auRaw.unverified) || auRaw.blockers + auRaw.highs > auRaw.confirmed)) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned confirmed ' + JSON.stringify(auRaw.confirmed) +
      ', unverified ' + JSON.stringify(auRaw.unverified) +
      ', blockers ' + auRaw.blockers + ', highs ' + JSON.stringify(auRaw.highs) + ' at round ' +
      roundNo + '. `blockers` and `highs` count CONFIRMED findings, so each is an integer and their ' +
      'sum is at most `confirmed`, and `unverified` is the integer the callee counted; a count that ' +
      'cannot be read is a DEGRADED run and is never rounded to zero.',
  )
}
const lastReport = specAudit ? (auRaw.report || '') : ''
// `report`, NOT `reportPath` — the second name was mine and matched nothing, so `lastReport` was
// always '' and every disposal instruction named an empty path. A CLEAN round has none to name and
// nothing to fold from, so it is the one shape that passes here with an empty path.
if (specAudit && !lastReport && !cleanRound) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned no report path at round ' + roundNo +
      '. The fold instruction the caller receives would name nothing to fold from.',
  )
}
// ONE SHAPE PAST THIS LINE. The clean round is folded into the integers every later line reads — and
// the OFF path into NULLS, by this file's own rule three paragraphs up: a count nobody produced is a
// stated absence, never a zero, because 0 is the one value that reads as a clean bill.
const auBlockers = !specAudit ? null : cleanRound ? 0 : auRaw.blockers
const auConfirmed = !specAudit ? null : cleanRound ? 0 : auRaw.confirmed
const auHighs = !specAudit ? null : cleanRound ? 0 : auRaw.highs
const auUnverified = !specAudit ? null : cleanRound ? 0 : auRaw.unverified

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
// sequence verdicts and this mode never produces one; a run needing M4's disposal reaches it
// through the confirmed count and not through the verdict, which is what the header means by the
// clause being reachable here.
//
// The non-integer case is already refused above, in BOTH modes, and must stay so: `tier2-review.js`
// yields `blockers: null` on its degraded paths BY DESIGN, and reading null as 0 would make every
// degraded audit look clean.
//
// THE DISPOSITION FIELD IS DERIVED FROM WHAT WAS PROMOTED, NOT PREDICTED FROM THE SYNTHESIS COUNTS
// (closing review round 2, cluster B). The first cut appended `--disposition promote` at zero
// blockers iff `auHighs > 0`, and `auHighs` counts CONFIRMED findings only; the disposal stage
// below runs over the UNVERIFIED population too and may promote one the synthesis never graded, so
// `blockers 0, highs 0, unverified N` recorded a bare CONVERGED row and then promoted a unit the
// merge bar could not see — check 2 enters a CONVERGED subject into `needs` only on a `disposition`
// field. Zero blockers is CONVERGED unconditionally in the driver's `review_state`, so the harness
// knows that exit before the driver names it: at zero blockers with something to dispose, the
// DISPOSAL stage runs FIRST and the record carries `promote` iff `promotedIds` is non-empty. At a
// positive count the driver's token decides whether the loop even ended, so the record comes first
// there, and every such terminal exit records `promote` on the driver's own refusal-and-retry.
// The record is therefore a function, called at one of two points.
async function writeRound(disposition) {
  const rv = attended
    ? { token: au.blockers === 0 ? 'CONVERGED' : 'CONVERGING', exitCode: 0 }
    : await agent(
    GROUND +
      'Record AUDIT round ' + roundNo + ' with the driver and return its convergence token.\n\n' +
      'Run exactly:\n  ' + DRIVER + ' --review ' + slug + ' --subject ' + subject +
      ' --verdict ' + (au.blockers > 0 ? '"BLOCKED"' : '"CLEAN"') +
      ' --blockers ' + au.blockers + disposition + '\n\n' +
      'Return the CONVERGENCE token it prints — one of CONVERGING, CONVERGED, NON-CONVERGENT, ' +
      'CEILING, BOUNDED — verbatim, and the command\'s exit code. Do not infer the token from the ' +
      'blocker count: it is a property of the SEQUENCE of rounds, which only the driver can see. ' +
      'If the command REFUSES naming --disposition, this round is a terminal exit: run the SAME ' +
      'command once more with --disposition promote appended, and return THAT run\'s token and ' +
      'exit code. If the command REFUSES saying the subject already carries a terminal review ' +
      'round, return terminalSubject: true with its stderr and no token — do not retry under another ' +
      'subject. If the command fails for any other reason, return its stderr rather than a token.',
    { label: 'audit:record:r' + roundNo, phase: 'Audit', schema: REVIEW_RECORD_SCHEMA },
  )
  if (attended) log('attended mode: verdict computed from the blocker count; no round was recorded')
  // THE TERMINAL-SUBJECT REFUSAL IS ITS OWN THROW. It used to surface as "the round was not
  // recorded", which names the symptom; the cause is a subject key that was not re-keyed after a
  // disposal, and the remedy is in the args block at the top of this file.
  if (rv && rv.terminalSubject === true) {
    throw new Error(
      'unattended-build: the driver refused round ' + roundNo + ' because the subject is terminal, ' +
        're-key it: `' + subject + '` already carries a terminal review round. A re-invocation after ' +
        'a disposal passes the hand-out\'s `promotedIds` as `auditIds`, no `subjectRound` and no ' +
        '`subjects`, so the promoted specs are audited under a fresh subject; a fold re-invoke passes ' +
        'the `subjectRound` the CONVERGING return handed back (driver said: ' + JSON.stringify(rv.stderr) + ').',
    )
  }
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
  // fallen straight through to the hand-out. That is weaker than what it replaced, in the direction that
  // matters.
  const REVIEW_TOKENS = ['CONVERGING', 'CONVERGED', 'NON-CONVERGENT', 'CEILING', 'BOUNDED']
  if (REVIEW_TOKENS.indexOf(rv.token) === -1) {
    throw new Error(
      'unattended-build: the driver returned "' + rv.token + '", which is not one of ' +
        REVIEW_TOKENS.join(', ') + '. An unknown token is not CONVERGING, so it would fall through ' +
        'to DISPOSAL and the hand-out — refusing instead.',
    )
  }
  // S3 — THE IMPOSSIBLE PAIRING IS A REFUSAL BY NAME, in both directions. The driver's `review_state`
  // returns CONVERGED for a count of 0 and for nothing else, so CONVERGING with zero blockers is this
  // repo's signature for a record no verb produced — a loop with nothing left to converge on has
  // converged, and the dead stage returned exactly this pairing — and CONVERGED beside a positive
  // count is a token no driver printed. The second direction is what makes the ordering above hold:
  // a CONVERGED exit is never reached on the record-first path, so a disposition it owed is never
  // left off the row.
  if ((rv.token === 'CONVERGED') !== (au.blockers === 0)) {
    throw new Error(
      'unattended-build: the AUDIT stage returned ' + rv.token + ' paired with ' + au.blockers +
        ' blockers at round ' + roundNo + '. Those two cannot both be true — the driver converges at 0 ' +
        'and only at 0 — and this pairing is this repo\'s signature for a record no verb produced. ' +
        'REFUSING rather than emitting it.',
    )
  }
  return rv.token
}
const au = { blockers: auBlockers, confirmed: auConfirmed, highs: auHighs, unverified: auUnverified, reportPath: lastReport }
// OUTSTANDING is the callee's word and covers two populations (see the DISPOSAL stage). It decides
// the ORDER here: zero blockers with something to dispose records AFTER the disposal; every other
// shape records first, because at a positive count only the driver knows whether the loop ended.
const outstanding = specAudit ? au.confirmed + au.unverified : 0
const disposeFirst = au.blockers === 0 && outstanding > 0
// `NOT-OWED` IS THE OFF PATH'S VERDICT, and it is deliberately NOT in `REVIEW_TOKENS`: the driver
// never prints it, because no round was recorded for it to grade. It is a harness word for "no audit
// was declared", distinct from every terminal token so nothing downstream can read it as CONVERGED.
const verdict = !specAudit ? 'NOT-OWED' : disposeFirst ? 'CONVERGED' : await writeRound('')
log(!specAudit
  ? 'audit round ' + roundNo + ': NOT-OWED — off by declaration, so no round was recorded and no count exists'
  : 'audit round ' + roundNo + ': ' + verdict + ' · blockers ' + au.blockers + ' · unverified ' + au.unverified +
    (disposeFirst ? ' — the driver records this exit AFTER the disposal, so its disposition field is what was promoted' : ''))
// THE AUDIT OBJECT EVERY NON-THROWING RETURN CARRIES (TOOL-aBlindedTrial-3). `ran` is the fact the
// top-level `verdict` and `blockers` used to leave implicit, and it is what a caller reads to tell a
// declared audit from an undeclared one; the counts beside it are the callee's integers, or the
// stated nulls of an audit that never ran. One object, built once, placed on every return.
const audit = { ran: specAudit, verdict: verdict, blockers: au.blockers, highs: au.highs, unverified: au.unverified }

// THE GATE. `CONVERGING` means the review loop has not ended, so the ROSTER IS EMPTY and this
// returns to the caller with what it needs to fold and come back. Every terminal state admits the
// hand-out, and each of them first passes M4's disposal, which is the DISPOSAL STAGE below rather
// than a claim asserted here and runs on the confirmed count rather than on the verdict. An earlier
// revision of this comment claimed the promotion happened and no line of the program did it.
if (verdict === 'CONVERGING') {
  log('audit is still CONVERGING — no roster this invocation; fold, then re-invoke at round ' + (roundNo + 1))
  return {
    slug: slug,
    // THE MODE TRAVELS ON THIS RETURN TOO. It is the path an attended run takes on every
    // non-terminal round, and the terminal return's own comment says the field exists so a caller
    // can tell the modes apart — which it could not do here.
    mode: mode,
    base: base,
    round: roundNo,
    units: ordered.length,
    specced: speccedCount,
    specRefused: specRefused,
    verdict: verdict,
    audit: audit,
    blockers: au.blockers,
    unverified: au.unverified,
    lastReport: lastReport,
    skippedTerminal: [],
    // THE SUBJECT KEY TRAVELS BACK, so the fold re-invoke lands on the SAME driver subject and the
    // sequence keeps its predecessor to shrink against; `auditIds` rides with it for the same reason.
    subjectRound: subjectRound,
    auditIds: auditIds,
    // EVERY NON-THROWING EXIT CARRIES `roster`, so `roster.length === 0` is the caller's whole stop
    // condition. This return carried no such key at all, while the Skill bullet told the run that an
    // empty roster is the refusal — a caller reading `roster.length` read a property of `undefined`
    // and threw. `built` and `unbuilt` left with the stage that produced them.
    roster: [],
    nextAction:
      'FOLD the confirmed findings in ' + lastReport + ' as rev-N bumps with their section 9 lines, ' +
      'then re-invoke this harness with round: ' + (roundNo + 1) + ', subjectRound: ' + subjectRound +
      (auditIds.length ? ', auditIds: ' + JSON.stringify(auditIds) : '') + '. Do not build.',
    note: 'HELD AT AUDIT — the review loop has not ended, so no unit was built' +
      (attended ? ' · ATTENDED, so no driver-side check ran' : ''),
  }
}

// ============================================================== STAGE 3 — DISPOSAL
// A WHOLE-SET ACT, and that is why it is its own stage rather than an instruction carried into the
// first unit's pass. Disposal is authority over EVERY unit's spec, not over one unit's: carrying it
// into the first child would place it on whichever unit happens to be first, and a resumed run whose
// first roster element is already built would place it on a child that does nothing.
//
// The instruction used to be a string prepended to the BUILD prompt, so it was carried by the agent
// TOOL-aHoistedPass-6 deletes. Before that it was not carried at all: the comment above the gate
// claimed promotion happened at the exit and no line of the program did it. Then the stage ran on
// the VERDICT — `NON-CONVERGENT` and `CEILING` only, the two states that guarantee standing
// blockers — and disposed by NATURE, fold or promote by what the finding was. That is a predicate
// on the wrong integer: `CONVERGED` means zero BLOCKERS this round and says nothing about highs,
// mediums or lows, so a round that converged with eight highs, six mediums and one low (the
// recorded shape in the `aCollapsedScan` round-1 audit) disposed nothing and handed the roster out
// over fifteen confirmed findings.
//
// THE STAGE RUNS ON ANY OUTSTANDING FINDING AND DISPOSES BY SEVERITY (TOOL-aProbedUnit-7): a BLOCKER
// or HIGH is PROMOTED to a unit, a MEDIUM or LOW is FOLDED into its spec. OUTSTANDING is the
// callee's word and it covers two populations: the CONFIRMED findings and the UNVERIFIED ones, which
// came back with no usable skeptic verdict and are not cleared — a verify stage degraded by dead
// skeptic batches used to read as clean here, because only `confirmed` was counted (closing review
// round 1, cluster F). On a count of zero across both it announces the skip. A skip that looks like
// a pass is indistinguishable from coverage, and an absent `agent:dispose:` line alone would read
// the same over a stage that was never written.
phase('Disposal')
// WHAT STOOD IS HOISTED OUT OF THE STAGE so the hand-out can report it. It never reached the return
// at all, which is `degradation-known-but-unreported` — the class this file names three times in
// its own comments and then committed one screen below. `promoted` and `folded` ride the same
// hoist: honest zeros on the skip path, the stage's own integers past it, `null` where the stage
// returned no integer — a stated absence, never a zero, the audit adapter's own rule. `promotedIds`
// is the hoist's third rider: the units the promotions became, which the caller passes back as
// `auditIds` so the next invocation audits them before anything builds them.
let stood = [], promoted = 0, folded = 0, refuted = 0, promotedIds = []
// TWO SKIPS, TWO REASONS, said apart: "confirmed no finding" is a fact about a round that ran, and
// saying it over a round that did not would be the audit-that-never-ran reading as a clean one.
if (!specAudit) {
  log('disposal: skipped — the spec audit is OFF by declaration, so nothing was audited to dispose')
} else if (outstanding === 0) {
  log('disposal: skipped — round ' + roundNo + ' confirmed no finding and left none unverified, so nothing stands to dispose')
} else {
  log('disposal: ' + au.confirmed + ' confirmed and ' + au.unverified + ' unverified finding(s) stand at a ' +
    verdict + ' exit · blockers ' + au.blockers + ' · highs ' + au.highs + ' — disposing by severity' +
    (verdict === 'CONVERGED' ? ', on CONVERGED too' : ''))
  // MODE-AWARE IN ONE CLAUSE, on the same `attended` the file already branches GROUND on: `--rescope`
  // `fail 48`s without a run-state file, which is the state attended mode is DEFINED by, so the
  // attended promotion is a README roster row. Until the predicate moved off the verdict this stage
  // was unreachable in that mode and the contradiction was never live.
  const d = await agent(
    GROUND +
      'BEFORE ANY UNIT IS DISPATCHED, DISPOSE of every CONFIRMED and every UNVERIFIED finding in `' +
      lastReport + '` — the audit exited ' + verdict + ' with ' + au.confirmed + ' confirmed, ' +
      au.blockers + ' at BLOCKER and ' + au.highs + ' at HIGH, and ' + au.unverified +
      ' unverified. Open the report and take each confirmed finding at the severity the report ' +
      'gives it. Every count above is of RAW findings by report id and never of the items a report ' +
      'may merge them into, so a finding merged into an item takes that item\'s severity and still ' +
      'counts once, by its own id. An UNVERIFIED finding came back with no usable skeptic verdict and is OUTSTANDING, ' +
      'not cleared — read the code yourself and take it at the severity you adjudicate. ' +
      'BUILD-METHOD M4 disposes BY SEVERITY and admits no third ' +
      'route. PROMOTE every BLOCKER and every HIGH: ' +
      (attended
        ? 'add its row to the build README\'s authored Units table, because the recording verbs are ' +
          'unavailable with no run-state file, '
        : 'run `' + DRIVER + ' --rescope ' + slug + ' --act add --item <id> --reason <text>`, the ' +
          'reason being the report id and severity of the finding it closes, ') +
      'then author its spec at its tier with a mechanism that CLOSES the finding — the change to the ' +
      'design and the artifact that proves it — so the next invocation of this harness audits it ' +
      'as a spec, under `auditIds`, before it is built like any other. FOLD every MEDIUM and every ' +
      'LOW into the spec it belongs to, as a rev-N bump with its ' +
      'section 9 line. You may REFUTE an UNVERIFIED finding — never a CONFIRMED one — where your ' +
      'own reading finds no defect, with a one-line reason per refuted finding in `summary`, and ' +
      'count it in `refuted`. Never parked, never waived, never retired, never re-reviewed. Return ' +
      '`promoted`, `folded` and `refuted` as counts of FINDINGS by report id, each id counted exactly once ' +
      'across the three and `standing`; name every promoted unit id in `promotedIds` and in ' +
      '`summary`; and NAME in `standing` every finding you did NOT dispose.',
    { label: 'dispose:' + slug, phase: 'Disposal', schema: DISPOSAL_SCHEMA },
  )
  // NO PARTIAL HAND-OUT. Deciding which units a standing finding touches needs the tree, which this
  // runtime does not have, so an empty roster is the honest refusal. `d.disposed !== true` covers a
  // dead stage and a negative answer alike.
  //
  // AND A NON-EMPTY `standing` REFUSES TOO, WHATEVER `disposed` CLAIMS. `{disposed: true, standing:
  // ['b1']}` validates against DISPOSAL_SCHEMA, and on the disposed-only test it cleared this guard,
  // logged done and handed out the FULL roster over an undisposed blocker — under a prompt whose own
  // words are NAME in `standing` every finding you did NOT dispose. The pairing is self-contradictory
  // and the stage's report of what it did NOT do outranks its summary of what it did. This is the
  // third impossible pairing this file refuses by name; the other two are twelve lines above the
  // audit gate, and this guard simply did not get the pattern.
  //
  // AND THE COUNTS MUST RECONCILE, IN SUM AND IN SPLIT. Every outstanding finding is promoted,
  // folded or named standing — the prompt says so — so a return whose three numbers do not add to
  // confirmed + unverified is the same self-contradiction with the contradiction moved into two
  // integers. The sum alone was `containment-tested-one-way` (closing review round 1, cluster D):
  // `promoted 0, folded 10` reconciled against confirmed 10 with two blockers and three highs in
  // it, and the roster went out over two blockers folded into prose. The severity rule implies the
  // split: every BLOCKER and HIGH is promoted, so `promoted` is AT LEAST `blockers + highs` and
  // `folded` AT LEAST the confirmed rest — equalities when nothing is unverified, floors when an
  // unverified finding was adjudicated into either. The reason is chosen in the order the existing
  // arms read it; the refusal keeps their shape, an empty roster and a note.
  //
  // AND A PROMOTION NAMES ITS UNIT. `promoted` above zero beside an empty `promotedIds` is a
  // promotion the caller cannot route to an audit; a named unit beside `promoted` 0 is a unit no
  // finding produced. Both refuse.
  //
  // AND `refuted` IS BOUNDED BY THE UNVERIFIED COUNT (closing review round 2, cluster F). It is the
  // one verdict a dead skeptic batch left unsupplied, so it may cover the UNVERIFIED population and
  // nothing else; a `refuted` above `unverified` has refuted a CONFIRMED finding, which is the
  // re-review M4 forbids. It joins the sum and leaves the severity floors alone: a confirmed
  // BLOCKER or HIGH is still promoted, and a confirmed MEDIUM or LOW still folded.
  stood = Array.isArray(d && d.standing) ? d.standing : []
  const counted = Number.isInteger(d && d.promoted) && Number.isInteger(d && d.folded)
  promoted = counted ? d.promoted : null
  folded = counted ? d.folded : null
  refuted = d && d.refuted !== undefined ? d.refuted : 0
  promotedIds = Array.isArray(d && d.promotedIds) ? d.promotedIds : []
  // ONE UNIT ON BOTH SIDES OF THE SUBTRACTION (TOOL-dMergedTally-1). `confirmed` counts RAW findings,
  // so `blockers` and `highs` must too, or `mustFold` is raw minus items and demands more folds than
  // the MEDIUM and LOW findings exist to fill. The synthesis used to type both integers and counted
  // the ITEMS it merged raw findings into: 13 confirmed in 10 items read blockers 1, highs 5 against a
  // raw 3 and 6, and no honest disposal passed. `tier2-review.js` now derives both from the raw ids
  // each item lists, and returns null when an id is placed in no item or in two.
  const mustPromote = au.blockers + au.highs
  const mustFold = au.confirmed - mustPromote
  const refutedOk = Number.isInteger(refuted) && refuted >= 0 && refuted <= au.unverified
  if (!d || d.disposed !== true || stood.length || !counted || !refutedOk ||
      d.promoted + d.folded + refuted + stood.length !== outstanding ||
      d.promoted < mustPromote || d.folded < mustFold ||
      (d.promoted > 0) !== (promotedIds.length > 0)) {
    const why = !d ? 'the disposal stage returned nothing at all'
      : stood.length ? stood.join(', ')
      : !counted ? 'the stage returned no integer promoted/folded counts'
      : d.disposed !== true ? 'the stage answered disposed:false with nothing standing'
      : !refutedOk
        ? 'refuted ' + JSON.stringify(refuted) + ' is above the ' + au.unverified + ' unverified — a ' +
          'refutation covers the UNVERIFIED population only, and a CONFIRMED finding is never re-reviewed'
      : d.promoted + d.folded + refuted + stood.length !== outstanding
        ? 'the counts do not reconcile — promoted ' + d.promoted + ' + folded ' + d.folded +
          ' + refuted ' + refuted + ' + standing ' + stood.length + ' is not confirmed ' + au.confirmed +
          ' + unverified ' + au.unverified
      : d.promoted < mustPromote || d.folded < mustFold
        ? 'the counts do not split by severity — promoted ' + d.promoted + ' is below blockers ' +
          au.blockers + ' + highs ' + au.highs + ', or folded ' + d.folded + ' is below the ' +
          mustFold + ' confirmed at MEDIUM or LOW'
      : 'promoted ' + d.promoted + ' beside promotedIds ' + JSON.stringify(promotedIds) +
        ' — a promotion names the unit it became, and a unit names the finding that made it'
    log('disposal: NOT done — ' + why)
    return {
      slug: slug, mode: mode, base: base, round: roundNo, units: ordered.length,
      specced: speccedCount, specRefused: specRefused, verdict: verdict, audit: audit, blockers: au.blockers,
      unverified: au.unverified,
      lastReport: lastReport, skippedTerminal: [],
      roster: [],
      // THE ONE PATH WHERE `stood` CAN BE NON-EMPTY, and it is the one the field was missing from.
      // F4 added `standing` to the hand-out alone, where the guard above proves it always `[]` — the
      // field was placed exactly where it can never say anything and omitted exactly where it
      // carries the payload. A caller applying the hand-out's own stated rule reads `undefined`
      // here and concludes disposal never ran, which is the inverted reading the key exists to
      // prevent. Round-2 finding 1.
      standing: stood,
      promoted: promoted,
      folded: folded,
      refuted: refuted,
      promotedIds: promotedIds,
      note: 'DEGRADED — findings were not disposed: ' + why + '. No roster is handed out: a ' +
        'roster minus the units a finding touches is a judgement this runtime cannot make.' +
        // THE RECORD-AFTER-DISPOSAL PATH HAS NOTHING TO RECORD YET, and says so rather than writing a
        // CONVERGED row with no disposition over findings nobody disposed — the blindness the ordering
        // exists to end. The subject is not terminal, so the caller's route back is the driver's own verb.
        (disposeFirst
          ? ' The round was NOT recorded: at zero blockers the driver\'s row follows the disposal so its ' +
            'disposition field is what was promoted. Dispose the findings by hand under BUILD-METHOD M4, ' +
            'then record it yourself — `' + DRIVER + ' --review ' + slug + ' --subject ' + subject +
            ' --verdict "CLEAN" --blockers 0`, with ` --disposition promote` appended iff any finding ' +
            'became a unit — and dispatch from `' + DRIVER + ' --plan ' + slug + ' --paths`, the resume route.'
          : ''),
    }
  }
  log('disposal: done — promoted ' + promoted + ' · folded ' + folded + ' · refuted ' + refuted +
    (promotedIds.length ? ' · units ' + promotedIds.join(', ') : '') + ' — ' +
    (typeof d.summary === 'string' ? d.summary : ''))
}
// THE RECORD FOLLOWS THE DISPOSAL AT ZERO BLOCKERS (cluster B, above): the field is derived from what
// was actually promoted, so a unit the stage made out of an UNVERIFIED finding reaches check 2.
if (disposeFirst) await writeRound(promotedIds.length ? ' --disposition promote' : '')
// ==================================================== THE HAND-OUT, and what is graded before it
// S4/S4b - THE PER-UNIT REFUSAL, and in attended mode it happens HERE rather than at `--dispatch`.
// IT DID NOT LEAVE WITH THE BUILD AGENT (TOOL-aHoistedPass-6): it grades which units may be
// DISPATCHED, so it belongs to the hand-out and moved ahead of it.
// Three verbs an unattended pass is told to call hard-refuse without a run-state file — `--dispatch`
// (fail 49), `--brief` (fail 49) and `--rescope` (fail 48) — and a refusal means the order is wrong
// and the pass must STOP. Left ungraded here, attended mode would halt at unit one AFTER units were
// already being written: strictly worse than the refusal it traded away. THE INSTRUCTION now sits in
// the child rather than in a prompt of this file's, which is why this comment names the verbs and no
// longer names a prompt that carried them.
//
// THE STATE COMES FROM THE CALLER, resolved ONCE from `--plan` at entry, because this script has
// no shell and there is no point between the stages at which a caller could re-run it. A caller that
// re-resolves it — `--plan <slug> --paths` between dispatches — gets a fresher answer than this
// grading, which is what the resume contract does and what this file cannot do for it.
//
// MATCHED AS A PREFIX ON `DONE`, never against a closed token set. `--plan` prints `DONE ($state)`
// for a terminal unit whose underlying grade is not READY, so the live vocabulary includes
// `DONE (THIN)` and `DONE (FORKED)`. A five-token allow-list halts on the first such unit.
//
// AND THE ENTRY-TIME VALUE IS STALE BY CONSTRUCTION for the units stage 1 authors: a fresh build
// reports MISSING for every one of them. So a unit this invocation SPECCED is treated as READY
// whatever it reported at entry — otherwise the stage refuses the build it just specced.
// `authored` ALONE, and the distinction is the whole point of the exemption. Only the units THIS
// invocation wrote have a stale entry-time state; a unit the stage reported as `alreadyPresent` is
// one it did NOT touch, so its entry-time grade is current and exempting it would bypass the
// THIN/FORKED refusal on an agent's say-so.
const speccedNow = Array.isArray(specced.authored) ? specced.authored : []
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
        'this stage rosters only a unit that is READY or already terminal. This is the refusal ' +
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
// `driverSteps` IS RE-HOMED IN THE CHILD, both branches. This comment used to say its ATTENDED
// branch — write down the paths you will touch, because the recording verbs are unavailable with no
// run-state file — was LOST rather than moved, and understated what had actually gone: the child was
// handed the UNATTENDED branch in both modes, so an attended run was ordered to call two verbs that
// `fail 49` without a run-state file, under a prompt saying a refusal is binding. What this file owes
// the child is the MODE, which now travels in `dispatch.args` below; the two texts are the child's.
//
// THE SKIP HAS TO REACH THE ROSTER. `skippedDone` was computed, logged as SKIPPING and returned in
// `skippedTerminal`, and then the BUILD agent was handed the UNFILTERED roster — so an attended run
// told its operator it had skipped the terminal units and told its agent to build them. The handed-
// out roster maps THIS array and never `ordered`, or the same defect returns one layer over, in a
// per-unit dispatch loop. The full prose roster stays with the subject resolver, which legitimately
// wants every spec.
const buildUnits = ordered.filter(function (u) { return skippedDone.indexOf(u.id) === -1 })
if (attended && !buildUnits.length) {
  log('attended mode: every unit is already terminal — nothing to build')
  return {
    slug: slug, mode: mode, base: base, round: roundNo, units: ordered.length,
    specced: speccedCount, specRefused: specRefused, verdict: verdict, audit: audit, blockers: au.blockers,
    unverified: au.unverified,
    lastReport: lastReport, skippedTerminal: skippedDone, roster: [],
    // POST-DISPOSAL, so `stood` is in scope and the key belongs here for the same reason it belongs
    // on the DEGRADED return: every non-throwing exit past the stage says what stood, out loud —
    // and what it promoted and folded, as stated zeros rather than missing keys.
    standing: stood,
    promoted: promoted,
    folded: folded,
    refuted: refuted,
    promotedIds: promotedIds,
    // THE DEGRADED TERM IS NOT SKIPPED HERE. This return was written with a hard-coded clean note,
    // which bypasses the composition the main return performs — and `specRefused` is live on this
    // path, so a run that refused specs and then found nothing to build reported 'complete'.
    note:
      (specRefused.length
        ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused. '
        : '') +
      'complete for ATTENDED mode — every unit was already terminal, so the roster is empty by ' +
      'FILTERING rather than by this program finding nothing',
  }
}
// THE RUN-INTEGRITY BLOCK. `memory/gotchas/degradation-known-but-unreported` is the class where a
// pipeline computes how badly its own run degraded and then fails to say so where it matters. Every
// count below is carried OUT of this harness rather than left in a log nobody reads.
//
// `units` COUNTS `ordered` AND `roster` MAPS `buildUnits`, on purpose. The first is the SET SIZE and
// the second is the WORK LIST, and they differ exactly when attended mode has some-but-not-all
// terminal units.
//
// `specPath` IS EMPTY FOR EVERY UNIT THE SPEC STAGE JUST AUTHORED, and this program cannot fix it:
// `units` arrives in `args` and nothing here writes the field back. It is carried so a caller that
// already had a path does not lose it, and `resolvePathsWith` names the command that resolves the
// rest. A run that dispatches straight off this array hands a child an empty spec path.
const handOut = {
  slug: slug,
  mode: mode,
  base: base,
  round: roundNo,
  units: ordered.length,
  specced: speccedCount,
  specRefused: specRefused,
  verdict: verdict,
  audit: audit,
  blockers: au.blockers,
  unverified: au.unverified,
  lastReport: lastReport,
  skippedTerminal: skippedDone,
  // WHAT STOOD, and it is REQUIRED rather than conditional. The guard above means this is always
  // empty by the time the hand-out is reached — that is the point: an empty list said out loud is a
  // different fact from a missing key, which is indistinguishable from a disposal stage that never
  // ran. Same rule DISPOSAL_SCHEMA applies to the stage's own return, applied to this one.
  // `promoted` and `folded` are the stage's counts of findings by report id; `promotedIds` are the
  // UNITS those promotions became, carried here because the caller's next act depends on them: a
  // promoted spec is audited by re-invoking this harness with them as `auditIds` BEFORE it is
  // built, and a caller re-reading `--plan` for them would find them READY and build them unaudited.
  standing: stood,
  promoted: promoted,
  folded: folded,
  refuted: refuted,
  promotedIds: promotedIds,
  nextAction: promotedIds.length
    ? 'AUDIT the promoted specs before any of them is dispatched: re-invoke this harness with round: ' +
      (roundNo + 1) + ', auditIds: ' + JSON.stringify(promotedIds) + ' and no subjectRound and no ' +
      '`subjects`, so they take a fresh subject and the resolver scopes to them; dispatch the roster ' +
      'below for every unit that is not one of them.'
    : 'dispatch the roster below, one main-loop Workflow call per unit',
  roster: buildUnits.map(function (u) {
    return { id: u.id, order: u.order, specPath: u.specPath || '', briefPath: u.briefPath || '' }
  }),
  // WHAT THE CALLER DISPATCHES, and what each child is given. `args` carries the INVARIANTS and
  // `perUnit` names the three fields that vary — the roster is not among them, which is the whole
  // shape change: a child receives its own unit and never the list. Nothing beyond a unit's spec
  // reaches it except through its BRIEF file, because `--brief` is the only carrier that hashes
  // anything; nothing hashes a prompt string.
  dispatch: {
    scriptPath: 'tools/workflows/unattended-unit.js',
    // THE MODE IS AN INVARIANT AND IT TRAVELS. Left off, the child was mode-blind and ordered
    // `--dispatch` and `--brief` unconditionally — both `fail 49` without a run-state file, which is
    // the state attended mode is DEFINED by, under a child prompt saying a refusal is BINDING. So
    // attended runs halted at unit one: the exact failure the plan-state grading above was moved
    // forward to prevent, one layer down. `GROUND` already tells an attended child those verbs are
    // unavailable, so without this key the child received two contradictory instructions in one
    // prompt.
    // `scratch` travels for the same reason: the child refuses without it AND refuses a `ground`
    // that does not name it, so a caller copying this object hands the pair the child joins.
    args: { repo: repo, slug: slug, scratch: scratch, mode: mode, driver: DRIVER, ground: GROUND, checklist: CHECKLIST },
    perUnit: ['unitId', 'specPath', 'briefPath'],
    resolvePathsWith: DRIVER + ' --plan ' + slug + ' --paths',
  },
  // THE MODE IS PART OF THE RUN-INTEGRITY REPORT, not decoration. `degradation-known-but-unreported`
  // is the class where a pipeline computes how weak its own run was and then does not say so where a
  // reader looks. An attended run that returns a bare 'complete' has skipped five checks an
  // unattended one performs, and the caller cannot tell the two apart from this field.
  // BOUNDED IS NOT A DEGRADATION (closing review round 1, cluster E): it is the routine spec-subject
  // exit whenever a blocker is confirmed at round 1 under the kit default, and labelling it DEGRADED
  // made a by-design exit unreadable from a dead writer. NON-CONVERGENT and CEILING stay: the
  // driver's own CEILING line calls it a defect.
  // NOT-OWED IS NOT A DEGRADATION EITHER (TOOL-aBlindedTrial-3), and it is not clean: the audit was
  // declared off, so the note says that in its own clause rather than either grading it. Without the
  // exemption every undeclared run read DEGRADED; without the clause it read like one that reviewed.
  note:
    (specRefused.length || (verdict !== 'CONVERGED' && verdict !== 'BOUNDED' && verdict !== 'NOT-OWED')
      ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused, verdict ' + verdict +
        (attended ? ' · ATTENDED, so no driver-side check ran' : '') + ' · '
      : attended
        ? 'ATTENDED mode — stage order held, and none of the five driver-side records or refusals ' +
          'ran; this is NOT the guarantee an unattended run gives · '
        : '') +
    (specAudit ? '' : 'spec audit OFF by declaration — NOT-OWED, no round reviewed or recorded · ') +
    'prologue complete; ' + buildUnits.length + ' unit(s) to dispatch',
}
// A CLEAN ROUND LEAVES NO RECORD, AND THE ROSTER IS WITHHELD UNTIL ONE EXISTS (closing review round
// 2, cluster D). `tier2-review.js` returns `report: null` on both clean paths — zero findings, every
// finding refuted — and writes the `**Serves:** spec-audit` binding line only in the synthesis pass
// those paths skip. `specs-audited` is a machine DoD term at `--close` WHEN THE BUILD DECLARED THE
// AUDIT (opt-in since TOOL-aBlindedTrial-3; `cleanRound` is false with it off, so this block is never
// entered then): it joins every CLOSED unit id
// against a tracked record carrying that line, and with none at all refuses the whole build. So the
// cleanest audit there is used to build every unit and then could not close, with nothing to point
// the override at. This runtime cannot write the record — it has no filesystem — and cannot see
// one; what it can do is refuse to hand out a roster over the gap and name the ids the record must
// carry. The caller writes it, commits it, and dispatches from the resume route the Skill already
// prescribes, which is why `dispatch` stays on this return. Unattended only: an attended run has an
// owner in the loop and no DoD term reading it.
if (cleanRound && !attended) {
  // OWED IS WHAT THE CALLEE READ, never the roster. `subjects` is what `tier2-review.js` was handed
  // — caller-supplied, or resolver-returned only for units whose spec path resolves at HEAD — and a
  // unit the spec stage just authored has no `specPath` yet (its own comment above the hand-out
  // says so), so the roster minus the refused set names units no audit opened. A binding line over
  // those would certify an audit that never read them. Round-3 cluster B of aProbedUnit.
  const owed = auditUnits
    .filter(function (u) {
      return specRefused.indexOf(u.id) === -1 && u.specPath &&
        subjects.some(function (s) { return s.path === u.specPath })
    })
    .map(function (u) { return u.id })
  if (!owed.length) {
    throw new Error(
      'unattended-build: the clean round at ' + roundNo + ' covered NO unit — none of the audit ' +
        'units has a spec path among the subjects the callee was handed — so there is nothing a ' +
        'spec-audit record could bind. Commit the authored specs and re-invoke; a clean round ' +
        'over nothing certifies nothing.',
    )
  }
  const uncovered = auditUnits
    .filter(function (u) { return specRefused.indexOf(u.id) === -1 && owed.indexOf(u.id) === -1 })
    .map(function (u) { return u.id })
  const subjectLines = subjects.map(function (s) { return s.path + '@' + s.blob }).join(', ')
  handOut.roster = []
  handOut.nextAction =
    'WRITE the spec-audit record this clean round left unwritten, BEFORE any unit is dispatched: the ' +
    'callee wrote no report, so no tracked record carries `**Serves:** spec-audit ' + owed.join(' ') +
    '` and `specs-audited` refuses every one of those units at --close. Author `' + reviewDir +
    '/<date>-review-' + owed[0] + '-spec-audit-round' + (roundNo - subjectRound + 1) +
    '.md` in this order, which is the order the callee\'s own synthesis writes and hygiene check 22 ' +
    'reads: line 1 exactly `**Serves:** spec-audit ' + owed.join(' ') + '`; a title line; a line naming ' +
    'the reviewed subjects `' + subjectLines + '` and the round; then a heading that is exactly ' +
    '`## Verdict: CLEAN`; then the body quoting the callee (the callee said: ' +
    (typeof auRaw.note === 'string' ? auRaw.note : 'no note') + '). ' +
    (uncovered.length
      ? 'NOT covered by this round and NOT to be named on that line: ' + uncovered.join(', ') +
        ' — each owes a later audit once its spec is committed. '
      : '') +
    'Commit the record, then dispatch every unit `' + DRIVER + ' --plan ' + slug + ' --paths` lists as READY, ' +
    'one main-loop Workflow call each, with `dispatch` below. No roster is handed out here: a roster ' +
    'over an unrecorded audit is the build `specs-audited` cannot close.'
  handOut.note = 'HELD AT HAND-OUT — a clean round with no tracked spec-audit record; the roster is ' +
    'withheld until one names ' + owed.join(', ') +
    (specRefused.length ? ' · DEGRADED — ' + specRefused.length + ' spec(s) refused' : '')
  log('hand-out: WITHHELD — the clean round at ' + roundNo + ' left no spec-audit record; one naming ' +
    owed.join(', ') + ' is owed before any unit is dispatched')
} else {
  log('hand-out: ' + buildUnits.length + ' unit(s) to dispatch, one main-loop Workflow call each')
}
return handOut

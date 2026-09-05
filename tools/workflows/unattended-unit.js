// unattended-unit.js — ONE unit, ONE agent, oriented in that unit's spec and brief and nothing else.
//
// IT IS A BARE TOP-LEVEL SCRIPT, not a module. The Workflow runtime evaluates the body as an async
// function with the hooks injected as parameters, so `export default` never runs and never parses:
// the workflow-syntax gate beside this file says so in its own header, and its strip regex does not
// match `export default`. `export const meta` is the one export the dialect keeps.
//
// `export const meta` IS A SELECTOR, NOT A REQUIREMENT. Both readers of this file pick their
// population by that exact marker — check-verifier-fanout.sh and check-workflow-syntax.js — so
// deleting it does not fail either gate, it removes this file from both. Their vacuity guards fire
// only when the WHOLE population is empty, and other workflow scripts keep it non-empty. Asserted
// once, at landing, and held by review after that.
//
// IT NEVER NESTS, AND NOTHING CHECKS THAT. The fan-out guard contains no occurrence of the nesting
// primitive's call form at all, so it does not look at nesting; a nested call here would be legal
// at the hook, and one fired from inside this sidechain reaches no hook either. Asserted once, when
// the file lands. Held after that by review alone.
//
// IT IS NEARLY ONE STRAIGHT LINE — A STYLE RULE WITH NO ENFORCER, AND ONE DELIBERATE EXCEPTION. No
// loop, no array method, no Promise combinator and no arrow, so the one spawn below is visible in a
// single screen. What it DOES carry is exactly one top-level definition, and that is not a lapse:
// the codebase-map JS liveness floor raises on any `.js` under the tool root yielding no definition
// at all, and `codebase-map coverage + freshness` runs unguarded on every bar. The child yields to
// the floor rather than the floor to the child — widening a fail-closed check so a style preference
// can survive is the trade this build exists to stop making.
//
// ITS NAME IS `check` AND THAT IS THE MERGE BAR, NOT TASTE. `.lexicon.conf` declares this suffix as
// a probe layer, so its functions pattern grades the definition below, and the declared verb table
// carries `check` — assert a predicate and return a verdict, which is what the eight refusals do.
// The pin sat AT its ceiling with zero headroom when this landed, so a definition named outside the
// table would have redded the bar; raising the pin instead would have made the table a synonym list.
//
// Measured against the shipped hook: `function`, `=>` and a non-receiver `.map` all ADMIT at exit 0.
// What the hook DOES deny, per dispatch, is a loop around a spawn, a fan-out receiver it cannot
// size, a raw fan-out primitive, an unresolvable bound and a ref-keyed verdict join. Keep this file
// that shape anyway, and do not mistake the shape for a guarantee.
//
// IT SPELLS NO PATHS. The driver spelling, the ground text, the per-pass checklist command and both
// document paths arrive in `args`, so this file carries no install-prefix literal and needs no
// ratchet row and no method-carriers row.
export const meta = {
  name: 'unattended-unit',
  version: '1.0', // gov:kit unattended-unit@1.0 — engine identity (deployed verbatim)
  description:
    'Builds exactly ONE unit of an unattended build, in a sidechain whose orientation is that unit spec and that unit brief. The roster is not in scope here; the parent holds it and holds the order.',
  phases: [{ title: 'Unit', detail: 'read the brief and the spec, declare the write set, build, commit' }],
}

// ARGS ARRIVE AS A STRING even when the caller hands the tool JSON, so this parses first and
// validates second — ported from unattended-build.js, which added the guard after a sibling harness
// twice reviewed a DIFFERENT repository than the one it was briefed on.
let cfg = args
if (typeof cfg === 'string') {
  try {
    cfg = JSON.parse(cfg)
  } catch (e) {
    throw new Error(
      'unattended-unit: args must be JSON carrying repo, slug, unitId, specPath and briefPath; could not parse the string given (' +
        e.message + '). Refusing to default any of them.',
    )
  }
}
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) {
  throw new Error('unattended-unit: args must be an object carrying every key below. Refusing to default any of them.')
}

// THE ONE TOP-LEVEL DEFINITION. Eight near-identical refusals collapse into one predicate, and each
// caller supplies the REASON the key is not defaultable — a refusal that names only the missing key
// tells the caller what to add and never why it was never optional.
function check(key, why) {
  if (!cfg[key]) throw new Error('unattended-unit: args must carry an explicit `' + key + '`. ' + why)
}

check('repo', 'Defaulting the build root to the process cwd is how a sibling harness reviewed the wrong repository, twice.')
check('slug', 'Every driver verb in the prompt below is slug-addressed.')
check('unitId', 'This script builds one unit and cannot pick it.')
check('specPath', 'A unit built without its spec in hand is the defect this harness exists to close.')
check('briefPath', 'The brief is the only carrier the driver hashes; nothing hashes a prompt string.')
check('driver', 'The driver invocation is the caller\'s to spell, because this file spells no install path.')
check('ground', 'The grounding preamble is the parent\'s; the child does not re-derive it.')
check('checklist', 'The per-pass bug-class command is owed after every commit, and a sidechain agent does not inherit the unattended Skill.')

// `mode` IS NOT A `check()` CALL, and the closed set is the reason. `check` asserts truthiness, and
// truthiness is satisfied by `"atttended"` — which would then select the UNATTENDED text by falling
// through a ternary, silently, which is the defect this key exists to close. The parent refuses an
// unknown mode against this same pair; that guard does not travel to a child the caller composes
// args for, so the child makes it again rather than trusting it. One refusal, stronger than the
// contract above, and no second definition.
if (cfg.mode !== 'attended' && cfg.mode !== 'unattended') {
  throw new Error(
    'unattended-unit: args must carry an explicit `mode` of either attended or unattended, got ' +
      JSON.stringify(cfg.mode) + '. It decides which driver verbs this unit is ordered to call, and ' +
      'the two sets are not compatible: `--dispatch` and `--brief` both refuse without a run-state ' +
      'file, which is the state attended mode is defined by. Refusing rather than defaulting.',
  )
}

// `why` is REQUIRED and is never an absence: an empty result with no reason is indistinguishable
// from a clean pass over nothing.
const UNIT_SCHEMA = {
  type: 'object',
  required: ['committed', 'sha', 'why', 'summary'],
  additionalProperties: true,
  properties: {
    committed: { type: 'boolean' },
    sha: { type: 'string' },
    why: { type: 'string' },
    summary: { type: 'string' },
  },
}

phase('Unit')

// THE DRIVER STEPS ARE MODE-BRANCHED, and this is the one thing in this file that is not optional.
// `--dispatch` and `--brief` both `fail 49` without a run-state file, and attended mode's DEFINING
// premise is that no run-state file exists — so an unconditional order to call them, under the next
// sentence's rule that a refusal is BINDING, halts every attended run at unit one. It did.
//
// BOTH TEXTS ARE RECOVERED from the `driverSteps` ternary `TOOL-aHoistedPass-6` deleted from the
// parent, not re-invented: the attended branch is verbatim, because it was reviewed once already.
// The unattended branch keeps the CORRECTED order-gate wording this build wrote and not the deleted
// spelling, which claimed `--dispatch` refuses an out-of-order unit unconditionally — the false
// claim the same unit fixed. Restoring the old bytes there would re-open a closed finding.
//
// It is a ternary and not a second definition: the codebase-map JS liveness floor counts the one
// definition above, and this file keeps exactly one.
const DRIVER_STEPS =
  cfg.mode === 'attended'
    ? 'This run has NO run-state file, so the driver\'s recording verbs are unavailable and you must ' +
      'not call them: --dispatch, --brief and --rescope all refuse without one. Write down the paths ' +
      'each pass will touch before you touch them anyway — the declaration is what makes disjointness ' +
      'checkable, and here only you can check it.\n'
    : 'Declare the write set with `' + cfg.driver + ' --dispatch ' + cfg.slug + ' --pass ' + cfg.unitId +
      ' --writes <path>` before you write anything. A REFUSAL FROM IT IS BINDING — read it and stop. ' +
      'ITS SILENCE IS NOT A CLEARANCE: it refuses this unit only for having no tracked spec or a THIN ' +
      'one, plus the shape of the paths you declared; its ORDER gate runs only where this unit AND the ' +
      'blocking sibling both carry an `order` verb, and a sibling that merely declared a dispatch stops ' +
      'blocking whether or not it was ever built. Order is the parent roster you were dispatched from, ' +
      'not something this verb proves.\n' +
      'Record what you were handed with `' + cfg.driver + ' --brief ' + cfg.slug + ' --unit ' + cfg.unitId +
      ' --path ' + cfg.briefPath + '`.\n'

const PROMPT =
  cfg.ground +
  '\n\nBuild exactly ONE unit: ' + cfg.unitId + '. You are handed two documents and you read both ' +
  'whole before you touch code: the BRIEF at ' + cfg.briefPath + ' and the SPEC at ' + cfg.specPath +
  '. The spec is the design; where you must diverge, CHANGE THE SPEC FIRST as a rev-N bump with its ' +
  'section 9 line, then write the code.\n' +
  DRIVER_STEPS +
  'Commit with the unit id in the subject. IN THAT SAME COMMIT, set this unit\'s spec status header ' +
  'to CLOSED — or to WONTDO with a reason. That header is the only fact the driver\'s --plan verb ' +
  'reads to decide a unit is finished, so a unit built without it leaves the run\'s own loop counter ' +
  'naming this unit again, forever.\n' +
  'Then run `' + cfg.checklist + '` and act on what it names ' +
  'before you return. Return committed:false with a `why` rather than a commit you cannot stand behind.'

const r = await agent(PROMPT, { label: 'unit:' + cfg.unitId, schema: UNIT_SCHEMA })

log('unit ' + cfg.unitId + ': committed=' + String(!!(r && r.committed)) + ' sha=' + ((r && r.sha) || '-'))

return {
  committed: !!(r && r.committed),
  sha: (r && r.sha) || '',
  why: (r && r.why) || '',
  summary: (r && r.summary) || '',
}

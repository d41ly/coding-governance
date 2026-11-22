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
// at the hook, and one fired from inside this sidechain is not a tool call, so no matcher sees it
// either — hooks DO reach a sidechain (measured 2026-09-12); they simply have nothing here to match.
// Asserted once, when the file lands. Held after that by review alone.
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
//
// `prebuild` IS OPTIONAL AND OFF BY DEFAULT (TOOL-aMendedFleet-74). A caller that passes it — today
// the command is `python <prefix>/memory-tree/gotchas.py --for-paths` — hands the unit agent the
// bug-class checklist over its declared write set BEFORE it writes code, beside the post-commit one
// it always gets. With the key absent the prompt, options and log are byte-identical to the file
// without it. It stays off until a build has measured whether it cuts checklist-fix commits against
// builds without it; whichever unit flips that default also gives the parent a switch. Its budget is
// the checklist's own tiered cut, not a cap chosen here: two budgets would be two answers to one
// question. The value is refused unless it is a non-empty single-line string with no backtick, since
// it is spelled into the prompt inside backticks.
//
// `roles` IS OPTIONAL (TOOL-aOrientedCast-4), and its one legal key is `builder`, the catalogue's agent
// type for this stage, which the parent forwards in `dispatch.args`. Given, the agent spawns as that
// type, its prompt carries one sentence naming it, leaves out the reading craft the builder role
// carries, and HANDS A DIVERGENCE BACK instead of ordering a spec rev bump: the builder makes one spec
// edit, the status flip, and returns `why` opening `DIVERGENCE:`, which the return's `diverged` field
// carries so a caller branches on a field and has the spec writer revise the spec. Absent, the prompt
// and the spawn options are byte-identical to the file without it, and a log line says it is untyped.
// The shape is a COPY of the review harness's `workerType` test, because the parent's guard does not
// travel to a child a caller composes args for; the protocol-parity leg holds the copies to one.
//
// `facts` IS REQUIRED WHERE `roles.builder` TRAVELS (TOOL-dBoundRoles-13 S6), and optional elsewhere: the
// list `handoff.py facts` prints for the brief and the spec, `[{name, key, class, text}]`. Given, the
// prompt hands both documents as their content under their keys and classes, in place of their paths,
// and a list missing either input, or naming a path other than `briefPath` or `specPath`, is refused.
// Absent on an untyped call, the prompt and options are byte-identical to the file without it.
//
// `efforts` IS OPTIONAL (TOOL-aOrientedCast-10), with the same one key: `builder`, the reasoning
// effort the builder spawns at, which the parent forwards in `dispatch.args` beside `roles`.
//
// `passLegs` IS OPTIONAL (TOOL-aNimbleMend-7): a one-line command the parent hands out in
// `dispatch.args`. Given, and the builder committed, the return carries a `nextAction` ordering the
// main loop to run it over the pass's commits, from the `base` the builder returns
// (TOOL-aNimbleMend-15). Absent, the return, log, prompt and options are unchanged.
//
// `passBase` IS OPTIONAL (TOOL-aTwinnedPass-1): the commit this pass starts from. Given, the agent
// runs in a worktree the runtime cuts for it, which may sit on the default branch's tip, so the
// prompt's first order is a hard reset to `passBase` and its confirmation. `writes`, the write set
// the main loop declared, travels with it in unattended mode and nowhere else, and the builder then
// orders neither recording verb, because `--dispatch` and `--brief` both write the run-state file a
// pass running beside another must not touch. The return carries `branch` and `worktree` after a
// shape check, and `nextAction` takes its base from `passBase` and names that worktree. Absent, the
// prompt, options, log and return are unchanged.
export const meta = {
  name: 'unattended-unit',
  version: '1.2', // gov:kit unattended-unit@1.2 — engine identity (deployed verbatim)
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
// TOOL-aProbedUnit-4 — `scratch` is not a dead key: the join below is what it is for. The child's
// PROMPT opens with `cfg.ground`, so the sentence the parent built with this same path is the first
// paragraph the unit agent reads and no second copy is spelled here; a hand-composed dispatch that
// drops either key, or hands a child a different path from the one its ground names, meets a
// refusal naming the other. Compared unfolded: the parent hands out the folded string in both.
check('scratch', 'Every temporary file this unit makes goes there, and a child that guessed a root would guess the empty $TMPDIR the parent exists to replace.')
if (String(cfg.ground).indexOf(cfg.scratch) === -1) {
  throw new Error(
    'unattended-unit: the `ground` text names no `' + cfg.scratch + '`, so the scratch root this child was ' +
      'handed is not the one its grounding sentence tells the agent to use. The parent hands out both in ' +
      'dispatch.args; pass them together.',
  )
}

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

// `prebuild` IS NOT A `check()` CALL EITHER: `check` asserts presence and this key is optional. When
// present it must be one line with no backtick, or one value could rewrite the prompt around it.
if (
  cfg.prebuild !== undefined &&
  (typeof cfg.prebuild !== 'string' || cfg.prebuild === '' || /[\r\n`]/.test(cfg.prebuild))
) {
  throw new Error(
    'unattended-unit: args `prebuild` must be a non-empty single-line string with no backtick, got ' +
      JSON.stringify(cfg.prebuild) + '. Omit the key to leave the pre-build checklist off.',
  )
}

// `passLegs` IS OPTIONAL TOO (TOOL-aNimbleMend-7), graded by the same three-part test because it is
// spelled inside backticks as well: in the RETURN's `nextAction`, never in the prompt. The builder is
// not told the command, since a role agent's pass runs no gate; the main loop runs it after the commit.
if (
  cfg.passLegs !== undefined &&
  (typeof cfg.passLegs !== 'string' || cfg.passLegs === '' || /[\r\n`]/.test(cfg.passLegs))
) {
  throw new Error(
    'unattended-unit: args `passLegs` must be a non-empty single-line string with no backtick, got ' +
      JSON.stringify(cfg.passLegs) + '. Omit the key and the return names no pass-leg run.',
  )
}

// TOOL-aNimbleMend-15 - A COMMIT NAME AN AGENT RETURNED reaches `nextAction` only through this shape.
// `nextAction` is an instruction to the main loop, which holds grants the builder lacks, and `sha` and
// `base` are a role agent's free text. The return's own `sha` field and the log line keep the raw value.
// It also grades `passBase` (TOOL-aTwinnedPass-1), which is spelled into a shell order in the prompt.
const COMMIT_SHAPE = /^[0-9a-f]{7,64}$/

// `passBase` IS GRADED BY THE COMMIT SHAPE (TOOL-aTwinnedPass-1): the commit this pass starts from. It
// is spelled into a shell order in the prompt, so it is graded by the commit shape and nothing else passes.
if (cfg.passBase !== undefined && (typeof cfg.passBase !== 'string' || !COMMIT_SHAPE.test(cfg.passBase))) {
  throw new Error(
    'unattended-unit: args `passBase` must be a commit sha of 7 to 64 lower-case hex digits, got ' +
      JSON.stringify(cfg.passBase) + '. Omit the key and the pass builds in the caller\'s own tree.',
  )
}
if (
  cfg.writes !== undefined &&
  (typeof cfg.writes !== 'string' || cfg.writes === '' || /[\r\n`]/.test(cfg.writes))
) {
  throw new Error(
    'unattended-unit: args `writes` must be a non-empty single-line string with no backtick, got ' +
      JSON.stringify(cfg.writes) + '. It is the write set the main loop declared with --dispatch for this pass.',
  )
}
if ((cfg.passBase !== undefined && cfg.mode === 'unattended') !== (cfg.writes !== undefined)) {
  throw new Error(
    'unattended-unit: args `writes` travels with `passBase` in unattended mode and nowhere else: it is the ' +
      'write set the main loop declared for a pass building in its own worktree, which that builder ' +
      'then does not declare. Got `passBase` ' + JSON.stringify(cfg.passBase) + ', `mode` ' +
      JSON.stringify(cfg.mode) + ' and `writes` ' + JSON.stringify(cfg.writes) + '.',
  )
}

// `roles` IS NOT A `check()` CALL: it is optional, and its key set is closed. The joined key list is
// compared with the two legal spellings, so the test needs no loop and no arrow.
const AGENT_TYPE_SHAPE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/ // owner: tier2-review.template.js `workerType`
const roles = cfg.roles === undefined ? {} : cfg.roles
if (!roles || typeof roles !== 'object' || Array.isArray(roles)) {
  throw new Error(
    'unattended-unit: `roles` must be a plain object mapping a stage key to an agent type, got ' +
      (Array.isArray(roles) ? 'array' : roles === null ? 'null' : typeof roles) + '.',
  )
}
const roleKeys = Object.keys(roles).join(',')
if (roleKeys !== '' && roleKeys !== 'builder') {
  throw new Error(
    'unattended-unit: `roles` carries `' + roleKeys + '`, and the one stage key of this harness is builder. ' +
      'Refusing rather than ignoring it: a misspelt stage would spawn untyped with nobody told.',
  )
}
if (roleKeys === 'builder' && (typeof roles.builder !== 'string' || !AGENT_TYPE_SHAPE.test(roles.builder))) {
  throw new Error(
    'unattended-unit: `roles.builder` must be an agent type name matching ^[A-Za-z][A-Za-z0-9_-]{0,63}$. Got ' +
      JSON.stringify(roles.builder) + '.',
  )
}
if (roles.builder === 'none') {
  throw new Error(
    'unattended-unit: `roles.builder` is `none`, the review harness\'s reserved untyped literal. An untyped ' +
      'builder is spelled by leaving its key out of `roles`, as the review harness\'s own `roles` refusal says.',
  )
}
const builder = roleKeys === 'builder' ? roles.builder : ''

// TOOL-dBoundRoles-13 S6 - `facts` HANDS THE BRIEF AND THE SPEC AS CONTENT: the JSON list the roles kit's
// `handoff.py facts` prints for `--input prompt=<briefPath> --input spec=<specPath>`, cut by the main loop
// immediately before this call, after its `--dispatch`, so the call is the unit's act launch. This file
// cannot read a file, so it compares the paths the keys name and trusts the cut, as it trusts `briefPath`.
// REQUIRED WHERE `roles.builder` TRAVELS and nowhere else: the roles kit that prints it is the one that
// names a builder role. `briefPath` stays, since the `--brief` order hashes the brief at it.
const facts = cfg.facts === undefined ? null : cfg.facts
const FACT_CUT = '`handoff.py facts --build ' + cfg.slug + ' --unit ' + cfg.unitId + ' --input prompt=' +
  cfg.briefPath + ' --input spec=' + cfg.specPath + '`'
if (builder && facts === null) {
  throw new Error(
    'unattended-unit: args must carry `facts` where `roles.builder` travels: the JSON list ' + FACT_CUT +
      ' prints, cut immediately before this call. Refusing rather than handing the two documents by path.',
  )
}
const FACT_KEY = /^record:(.+)@[0-9a-f]{12}$/
const FACT_CLASS = /^(witnessed|decided|claimed)$/
const fact0 = facts && facts[0]
const fact1 = facts && facts[1]
const briefFact = fact0 && fact0.name === 'input:prompt' ? fact0 : fact1 && fact1.name === 'input:prompt' ? fact1 : null
const specFact = fact0 && fact0.name === 'input:spec' ? fact0 : fact1 && fact1.name === 'input:spec' ? fact1 : null
if (facts !== null && (!Array.isArray(facts) || facts.length !== 2 || !briefFact || !specFact)) {
  throw new Error(
    'unattended-unit: `facts` must be the list of two, `input:prompt` and `input:spec`, that ' + FACT_CUT +
      ' prints; got ' + JSON.stringify(facts).slice(0, 200) + '.',
  )
}
if (facts !== null && (
  typeof briefFact.key !== 'string' || !FACT_KEY.test(briefFact.key) || !FACT_CLASS.test(String(briefFact.class)) ||
  typeof briefFact.text !== 'string' || typeof specFact.key !== 'string' || !FACT_KEY.test(specFact.key) ||
  !FACT_CLASS.test(String(specFact.class)) || typeof specFact.text !== 'string')) {
  throw new Error(
    'unattended-unit: each `facts` entry must carry a `record:<path>@<12 hex>` key, a class of witnessed, ' +
      'decided or claimed, and its text, as ' + FACT_CUT + ' prints them.',
  )
}
const briefCut = facts === null ? '' : FACT_KEY.exec(briefFact.key)[1]
const specCut = facts === null ? '' : FACT_KEY.exec(specFact.key)[1]
if (facts !== null && (briefCut !== cfg.briefPath || specCut !== cfg.specPath)) {
  throw new Error(
    'unattended-unit: `facts` was cut from the brief ' + briefCut + ' and the spec ' + specCut + ', and this ' +
      'call names the brief ' + cfg.briefPath + ' and the spec ' + cfg.specPath + '. Cut them again with ' + FACT_CUT + '.',
  )
}
// The two handed blocks, each under its `reads` heading with the fact line the renderer writes atop it.
const HANDED = facts === null ? ''
  : '### input:prompt\n\n<!-- gov:fact key=' + briefFact.key + ' class=' + briefFact.class + ' -->\n\n' +
    briefFact.text + '\n\n### input:spec\n\n<!-- gov:fact key=' + specFact.key + ' class=' + specFact.class +
    ' -->\n\n' + specFact.text + '\n\n'

// `efforts` IS OPTIONAL TOO (TOOL-aOrientedCast-10), keyed as `roles` is and independent of it: an
// untyped builder still takes its level. Its one legal key is `builder`, a level of lower-case letters
// the parent forwards in `dispatch.args`. The vocabulary is the roles library's; this file grades the
// shape only. Absent, the spawn options are byte-identical to the file without it.
const efforts = cfg.efforts === undefined ? {} : cfg.efforts
if (!efforts || typeof efforts !== 'object' || Array.isArray(efforts)) {
  throw new Error(
    'unattended-unit: `efforts` must be a plain object mapping a stage key to an effort level, got ' +
      (Array.isArray(efforts) ? 'array' : efforts === null ? 'null' : typeof efforts) + '.',
  )
}
const effortKeys = Object.keys(efforts).join(',')
if (effortKeys !== '' && effortKeys !== 'builder') {
  throw new Error(
    'unattended-unit: `efforts` carries `' + effortKeys + '`, and the one stage key of this harness is builder. ' +
      'Refusing rather than ignoring it: a misspelt stage would run at the wrong level with nobody told.',
  )
}
if (effortKeys === 'builder' && (typeof efforts.builder !== 'string' || !/^[a-z]+$/.test(efforts.builder))) {
  throw new Error(
    'unattended-unit: `efforts` key builder must be an effort level matching ^[a-z]+$ (leave the key out to run ' +
      'at the agent type\'s own level). Got ' + JSON.stringify(efforts.builder) + '.',
  )
}
const effort = effortKeys === 'builder' ? efforts.builder : ''

// `why` is REQUIRED and is never an absence: an empty result with no reason is indistinguishable
// from a clean pass over nothing.
const UNIT_SCHEMA = {
  type: 'object',
  // TOOL-aTwinnedPass-1 - two literal lists and not a `concat`: this file carries no array method.
  required: cfg.passBase === undefined
    ? ['committed', 'sha', 'why', 'summary']
    : ['committed', 'sha', 'why', 'summary', 'branch', 'worktree'],
  additionalProperties: true,
  properties: Object.assign({
    committed: { type: 'boolean' },
    sha: { type: 'string' },
    base: { type: 'string' },
    why: { type: 'string' },
    summary: { type: 'string' },
  }, cfg.passBase === undefined ? {} : { branch: { type: 'string' }, worktree: { type: 'string' } }),
}

// TOOL-aOrientedCast-27 - the builder's label and the run's identity, one string: its first log line
// and the first key of its return. Spelled here rather than through a helper, under the one-definition
// rule above; the two harness templates each define `renderAgentLabel` for theirs.
const identity = cfg.slug + ' · ' + cfg.unitId + ' · build'
log(identity)

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
//
// TOOL-aTwinnedPass-1 - a third branch, for a pass building in its own worktree in unattended mode.
// It spells neither `cfg.driver` nor `cfg.slug`, so the prompt carries no runnable recording verb.
const DRIVER_STEPS =
  cfg.mode === 'attended'
    ? 'This run has NO run-state file, so the driver\'s recording verbs are unavailable and you must ' +
      'not call them: --dispatch, --brief and --rescope all refuse without one. Write down the paths ' +
      'each pass will touch before you touch them anyway — the declaration is what makes disjointness ' +
      'checkable, and here only you can check it.\n'
    : cfg.passBase !== undefined
    ? 'The main loop declared this pass\'s write set with --dispatch and recorded this brief with ' +
      '--brief, on the run\'s branch at `' + cfg.passBase + '`, the commit you reset to, so you call ' +
      'neither: both write the run-state file, which a pass running beside another must not touch. The ' +
      'declared write set is `' + cfg.writes + '`. Write no path outside it. Where you need one, stop, ' +
      'restore every path you changed, commit nothing, and return committed:false with a why naming each ' +
      'such path: a declaration widens only before its pass commits, and only the main loop may widen ' +
      'this one.\n'
    : "The main loop declared this unit's write set with `" + cfg.driver + ' --dispatch ' + cfg.slug +
      ' --pass ' + cfg.unitId + ' --writes <path>` before it spawned you, from the spec\'s Files touched ' +
      'estimate. Before you write a path outside that set, declare it with the same command, naming ' +
      'only the paths you add. A REFUSAL FROM IT IS BINDING — read it and stop. ' +
      'ITS SILENCE IS NOT A CLEARANCE: it refuses this unit only for having no tracked spec or a THIN ' +
      'one, plus the shape of the paths you declared; its ORDER gate runs only where this unit AND the ' +
      'blocking sibling both carry an `order` verb, and a sibling that merely declared a dispatch stops ' +
      'blocking whether or not it was ever built. Order is the parent roster you were dispatched from, ' +
      'not something this verb proves.\n' +
      'Record what you were handed with `' + cfg.driver + ' --brief ' + cfg.slug + ' --unit ' + cfg.unitId +
      ' --path ' + cfg.briefPath + '`.\n'

// TOOL-aOrientedCast-4 S7 - with `roles.builder` the stamp follows the ground text, the reading craft
// the role carries is left out, and the two sentences on editing the spec become the hand-back.
const PROMPT =
  cfg.ground +
  (builder
    ? 'This stage runs as the ' + builder + ' agent type: your role is your system prompt, and this message is your task. '
    : '') +
  // TOOL-aTwinnedPass-1 - ahead of every order, so the reset is the first command the agent runs.
  (cfg.passBase === undefined
    ? ''
    : '\n\nTHIS PASS BUILDS IN A WORKTREE OF ITS OWN, which the runtime cut for this agent and which may ' +
      'sit on another commit. BEFORE ANY OTHER COMMAND, run `git reset --hard ' + cfg.passBase + '` there, ' +
      'then confirm `git rev-parse HEAD` prints a sha beginning with `' + cfg.passBase + '`, the commit ' +
      'this pass was dispatched from; if it does not, commit nothing and return committed:false with a ' +
      'why naming what it printed. Run every shell command with its working directory there, resolve ' +
      'every relative path in this message under it, the brief and the spec included, and write and ' +
      'commit only there, on the branch it has checked out, never in any other tree. Return that branch ' +
      'as `branch`, as `git branch --show-current` prints it, and the worktree\'s path as `worktree`, as ' +
      '`git rev-parse --show-toplevel` prints it.') +
  '\n\nBuild exactly ONE unit: ' + cfg.unitId + '. You are handed two documents' +
  (builder ? '' : ' and you read both whole before you touch code') +
  // TOOL-dBoundRoles-13 S6 - with `facts`, each as its content under its key and class, not by its path.
  (facts === null
    ? ': the BRIEF at ' + cfg.briefPath + ' and the SPEC at ' + cfg.specPath + '. '
    : ', each below as its content under its key and class: the BRIEF, cut from ' + cfg.briefPath +
      ', and the SPEC, cut from ' + cfg.specPath + '.\n\n' + HANDED) +
  // TOOL-aLightenedLoop-4 - the feasibility check is reading craft: the role carries it for a typed builder, and the untyped arm carries it inline.
  (builder
    ? 'The spec is the design and you do not edit it. Where the code you are about to write would diverge ' +
      'from it, stop before writing that code, restore every path you changed, commit nothing, and return ' +
      'committed:false with a why that opens DIVERGENCE: and names the spec section and what it would have ' +
      'to say. The caller has the spec revised by the spec-writer role and dispatches this unit again.\n'
    : 'Before your first product edit, check that the spec can be built as written: probe each claim it ' +
      'makes about current code against the tree, cross-read its scope, design and acceptance for two ' +
      'statements that cannot both hold, and check that its files-touched list holds every path the ' +
      'change and the commit hooks will need. ' +
      'The spec is the design; where you must diverge, CHANGE THE SPEC FIRST as a rev-N bump with its ' +
      'section 9 line, then write the code.\n') +
  // TOOL-aNimbleMend-15 - asked in BOTH modes and with or without `passLegs`, so the prompt stays the
  // same either way: a pass can make more than one commit, and only the builder saw where it started.
  // AHEAD of the driver steps, never after them: the pre-build paragraph follows the `--brief` order
  // and precedes the no-gate paragraph, and the suite pins both joins.
  'Before your first write, read `git rev-parse HEAD` and return what it prints as `base`: the commit ' +
  'this pass started from.\n' +
  DRIVER_STEPS +
  // TOOL-aMendedFleet-74 — empty unless the caller passed `prebuild`, so a default prompt is unchanged.
  // FILE paths, never a directory: a directory selects the whole catalogue, not a checklist.
  (cfg.prebuild === undefined
    ? ''
    : 'Once your write set is ' + (cfg.mode === 'attended' ? 'written down' : 'declared') +
      ', and before you write any code, run `' + cfg.prebuild + '` followed by every FILE path in that ' +
      'write set, never a directory. An item the checklist prints in full is a bug class to design ' +
      'against now. A one-line item is a pointer: read it when its class matches what you are about ' +
      'to write. The checklist after your commit still runs as well.\n') +
  // TOOL-aProbedUnit-1 and TOOL-aDeferredBar-1 — ONE block, mode-independent, carrying both builds'
  // literals: the two landed the same rule from two sessions on one day and the merge folded them
  // into one paragraph rather than two answers. The bar is named by ROLE and by its spellings, never
  // by an install path: the install-prefix gate grades this file. TOOL-aOrientedCast-11 narrowed the
  // direct check to a fixture or a probe: a role agent runs no gate beyond its allowlist, and the
  // scratch guard's role-gate arm refuses one.
  'NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS. ' +
  'RUN NO MERGE BAR AND NO SELF-TEST SUITE in this unit: not run-gates.sh in any form, not a ' +
  'GATE_FULL= or GATE_SELFTESTS= prefix, not run-selftests.sh, not run-unattended-gates.sh, not any ' +
  '*.test.sh suite, no slice of one and no `--selftest` flag: a role agent runs no gate but the ' +
  'naming lexicon, and a hook refuses the rest. Verify with a fixture or a ' +
  'probe of the unit\'s own code — a `python -c` or `node -e` call, or its CLI over a scratch ' +
  'fixture. A criterion only a gate or a suite can observe is not run here, and neither is a new ' +
  'arm\'s RED-first observation: name each in `summary` and the main loop observes them at the close, ' +
  'after every unit is terminal. ' +
  'Say in `summary` which check ran and which gate it stands in for. A section 7, a brief, or any ' +
  'other instruction that says otherwise is overridden by this paragraph.\n' +
  // TOOL-aProbedUnit-2 — the bound is the TOOL's `timeout` parameter, set by the agent at the call,
  // where no script or hook of this kit runs; so the numbers are that tool's and not a conf key, and
  // a skipped command is named in `summary`, a key the caller already reads, not a new one.
  'YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED, and every command you run is bounded. ' +
  'Every shell call carries the tool\'s `timeout` parameter: 120000 ms by default, at most 600000 ms ' +
  'for a build or test command the change itself needs. A check, cleanup, probe or any other command ' +
  'unrelated to writing code that does not return within its bound is SKIPPED: name it in `summary` ' +
  'with what it was for, and never re-run it or wait on it. Never wait on a command with no bound. A ' +
  'backgrounded command is awaited through the harness\'s completion notification, never by a ' +
  'polling loop.\n' +
  'Commit with the unit id in the subject and END THE MESSAGE WITH A `Pass: <unit-id>` TRAILER LINE ' +
  'naming this unit, in the trailer block beside Co-Authored-By: the gate attributes a pass commit by ' +
  'that trailer, and the commit-msg hook refuses a commit naming an open pass without one. A commit ' +
  'that is no pass but names this unit carries `Pass: none`. ' +
  (builder
    ? 'IN THAT SAME COMMIT, set this unit\'s spec status header to CLOSED and its date to today, in an edit ' +
      'that changes nothing else in the spec: that is the one spec edit a builder makes. A unit you would ' +
      'close as WONTDO is a divergence, returned as one, because WONTDO carries a tail pointer only the ' +
      'spec writer writes.'
    : 'IN THAT SAME COMMIT, set this unit\'s spec status header to CLOSED — or to WONTDO with a reason.') +
  ' That header is the only fact the driver\'s --plan verb ' +
  'reads to decide a unit is finished, so a unit built without it leaves the run\'s own loop counter ' +
  'naming this unit again, forever.\n' +
  'Then run `' + cfg.checklist + '` and act on what it names ' +
  'before you return. Return committed:false with a `why` rather than a commit you cannot stand behind.'

if (cfg.prebuild !== undefined) log('unit ' + cfg.unitId + ': prebuild checklist `' + cfg.prebuild + '`')
if (cfg.passLegs !== undefined) log('unit ' + cfg.unitId + ': pass legs `' + cfg.passLegs + '`')
if (cfg.passBase !== undefined) log('unit ' + cfg.unitId + ': own worktree from `' + cfg.passBase + '`' +
  (cfg.writes === undefined ? '' : ', declared writes `' + cfg.writes + '`'))

if (facts !== null) log('unit ' + cfg.unitId + ': handed as content `' + briefFact.key + '` and `' + specFact.key + '`')

log('unit ' + cfg.unitId + ': builder ' + (builder
  ? 'spawns as the ' + builder + ' agent type'
  : 'is untyped: no roles.builder was passed, so it spawns untyped with its role prose inline'))
log(effort ? 'effort builder: ' + effort + ' — efforts.builder'
  : 'effort builder: the agent type\'s own, else the session\'s — no efforts.builder')

const r = await agent(
  PROMPT,
  Object.assign({ label: identity, schema: UNIT_SCHEMA },
    builder ? { agentType: builder } : {}, effort ? { effort: effort } : {},
    cfg.passBase === undefined ? {} : { isolation: 'worktree' }),
)

log('unit ' + cfg.unitId + ': committed=' + String(!!(r && r.committed)) + ' sha=' + ((r && r.sha) || '-'))
if (cfg.passBase !== undefined) log('unit ' + cfg.unitId + ': branch=' + ((r && r.branch) || '-') + ' worktree=' + ((r && r.worktree) || '-'))

// TOOL-aTwinnedPass-1 - THE BRANCH AND WORKTREE AN AGENT RETURNED reach the return and `nextAction`
// only through these shapes, as `sha` and `base` reach `nextAction` only through COMMIT_SHAPE. An
// empty string is the shape check's refusal; the log line above keeps the raw values.
// TOOL-aTwinnedPass-4 - the shapes are the runtime's own spelling; TREE_SHAPE's lookahead is the
// template's `..` test, copied, as a workflow script is evaluated alone.
// TOOL-aTwinnedPass-11 - the runtime cuts two spellings. The Agent tool cuts `agent-<id>` at
// `<primary tree>/.claude/worktrees/agent-<id>` on `worktree-agent-<id>`. A Workflow cuts
// `wf_<run id>-<n>` at `<primary tree>/.claude/worktrees/wf_<run id>-<n>` on `worktree-wf_<run id>-<n>`.
// PASS_NAME states that name once for both shapes. `pass-tree.sh`'s `check_pass_branch` spells the
// same alternation, held to this one by no gate, owed under ask TOOL-aTwinnedPass-7.
// owner of the absolute prefix: unattended-build.template.js `scratch`
const PASS_NAME = 'agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+'
const TREE_SHAPE = new RegExp(/^(?!.*(^|[\\/])\.\.([\\/]|$))(\/|[A-Za-z]:[\\/])([A-Za-z0-9._ -]+[\\/])*\.claude[\\/]worktrees[\\/]/.source + '(?:' + PASS_NAME + ')$')
const BRANCH_SHAPE = new RegExp('^worktree-(?:' + PASS_NAME + ')$')
const ownBranch = r && typeof r.branch === 'string' && BRANCH_SHAPE.test(r.branch) ? r.branch : ''
const ownTree = r && typeof r.worktree === 'string' && TREE_SHAPE.test(r.worktree) ? r.worktree : ''

// S8 - `diverged` is a field, so a caller branches on it rather than on the prose of `why`.
return {
  identity: identity,
  committed: !!(r && r.committed),
  sha: (r && r.sha) || '',
  why: (r && r.why) || '',
  summary: (r && r.summary) || '',
  diverged: !!(r && r.committed === false && typeof r.why === 'string' && r.why.indexOf('DIVERGENCE:') === 0),
  // TOOL-aTwinnedPass-1 - on every return of a `passBase` call, `committed:false` included, because
  // the worktree outlives the pass either way.
  ...(cfg.passBase === undefined ? {} : { branch: ownBranch, worktree: ownTree }),
  // TOOL-aNimbleMend-7 - THE RUN POINT. Present only when the caller handed `passLegs` AND a commit
  // exists to run it over; it orders the main loop, and says nothing about how a red is fixed.
  // TOOL-aNimbleMend-15 - the command's base is the commit the builder STARTED from, never a relative
  // rev: a pass can make two commits. A `base` that fails the shape, or that names the pass commit
  // itself (one a prefix of the other), is not used, and the sentence hands the main loop the rev it
  // read before the dispatch. A `sha` that fails the shape names no commit here.
  // TOOL-aTwinnedPass-1 - with `passBase` the base is `passBase`, always: the main loop chose it and
  // checked its shape, and a builder that skipped the reset would hand back the default branch's tip.
  // The command then runs in the returned worktree, where the pass commit is HEAD, before the merge.
  ...(cfg.passLegs !== undefined && r && r.committed
    ? {
        nextAction:
          'Run `' + cfg.passLegs + ' --base ' +
          (cfg.passBase !== undefined
            ? cfg.passBase + '`'
            : typeof r.base === 'string' && COMMIT_SHAPE.test(r.base) &&
              String(r.sha || '').indexOf(r.base) !== 0 && r.base.indexOf(String(r.sha || '')) !== 0
            ? r.base + '`'
            : '<rev>`, where the builder returned no usable base, so `<rev>` is the commit HEAD named ' +
              'before the dispatch,') +
          (cfg.passBase === undefined
            ? ' at the main loop before the next dispatch and before any later commit,'
            : ' at the main loop with its working directory at ' +
              (ownTree ? '`' + ownTree + '`' : 'the worktree this pass built in, whose path the builder returned unusable') +
              ', before that worktree is merged back,') +
          ' where that file exists. The pass commit is ' +
          (typeof r.sha === 'string' && COMMIT_SHAPE.test(r.sha) ? r.sha + ', which is HEAD ' : 'HEAD ') +
          (cfg.passBase === undefined ? '' : 'there ') +
          'when the command runs. Act on its exit status and on every finding line it prints. The ' +
          'command runs nothing where `pass.fast-legs` is `off`.',
      }
    : {}),
}

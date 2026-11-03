export const meta = {
  name: 'tier2-review',
  version: '1.56', // gov:kit tier2-review@1.56 // gov:kit review-harness@1.56 — BOTH ids: the
  // second is this entry's REGISTRY id, and without it a deployer grepping the id the
  // registry uses finds nothing. DEPL-dGaugedVintage-5. — engine identity (deployed verbatim; this field is the deployer's version marker)
  description:
    'Consolidated, concurrency-capped (≤6) Tier-2 adversarial review, at most the agent-cap hook\'s MAX_VERIFIERS verify agents TOTAL: find → batched-verify → synth, joined on an ORCHESTRATOR-ASSIGNED INTEGER id. Replaces the big-fan-out review that trips the server rate limiter. Project-agnostic — parameterize via `args`.',
  phases: [
    { title: 'Resume', detail: 'one probe reads the key directory; a lens or batch whose file carries the key is reused' },
    { title: 'Find', detail: '5 finder lenses on either kind (3 on a light diff run), one wave, ≤6 concurrent' },
    { title: 'Verify', detail: 'skeptics refute findings in at most MAX_VERIFIERS BATCHES — agent count fixed' },
    { title: 'Synthesize', detail: 'one pass → report file' },
  ],
}

// --- cap-6 fan-out (inlined; workflow scripts can't import) --------------
// The only raw primitive call is the marked helper line; its width is the agent limit, rendered.
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

// --- TOOL-dDerivedDocket-29 — the review KEY, derived from the inputs and nothing else ----------
// Under `workerType: 'none'` a lens or a skeptic batch writes its result to
// `<git-common-dir>/review-lenses/<key>/` BEFORE it returns, so a fan that dies on a session limit
// keeps every result that came back, and a re-run with the same inputs dispatches only what is
// missing; under a named type no judge writes one and a re-run dispatches every judge again. The key is what makes "the same inputs" a test and
// not a hope: a file is reused only when its own `key` field equals the string computed here.
// FNV-1a over UTF-16 code units, with `Math.imul` because the script runtime refuses the clock and
// randomness and nothing else; the human-readable prefix means a collision needs the same kind,
// round and subject as well as a 32-bit match.
function deriveFnv1a(text) {
  let h = 0x811c9dc5
  for (let i = 0; i < text.length; i++) {
    h ^= text.charCodeAt(i)
    h = Math.imul(h, 0x01000193)
  }
  return (h >>> 0).toString(16).padStart(8, '0')
}
// Canonical JSON: object keys sorted at every depth, so two callers handing the same values in a
// different key order get one fingerprint.
function renderCanonical(v) {
  if (Array.isArray(v)) return '[' + v.map(renderCanonical).join(',') + ']'
  if (v && typeof v === 'object')
    return '{' + Object.keys(v).sort().map((k) => JSON.stringify(k) + ':' + renderCanonical(v[k])).join(',') + '}'
  return v === undefined ? 'null' : JSON.stringify(v)
}
// A diff review's subject is the RESOLVED pair. A ref that did not resolve to a full sha gets a
// subject no resolved run can ever produce, so its files are written and never reused: a moving ref
// is exactly the input that must not answer a later question.
const FULL_SHA = /^[0-9a-f]{40}([0-9a-f]{24})?$/
function deriveSubjectPair(b, h) {
  return FULL_SHA.test(String(b)) && FULL_SHA.test(String(h))
    ? String(b).slice(0, 12) + '-' + String(h).slice(0, 12)
    : 'unresolved-' + deriveFnv1a(String(b) + '...' + String(h))
}
// The probe's item schema is the lens or verdict schema plus the fields a FILE carries and a return
// does not, so a malformed file fails validation instead of being trusted.
function buildKeyedSchema(schema, extra) {
  return {
    type: 'object',
    required: ['name', 'key'].concat(extra, schema.required),
    properties: Object.assign({ name: { type: 'string' }, key: { type: 'string' }, batch: { type: 'string' },
      ids: { type: 'array', items: { type: 'integer' } } }, schema.properties),
  }
}

// --- TOOL-aMendedFleet-18 — the REVIEW-SHAPE line, one byte-stable record line per exit ----------
// Pure, so a `node` slice evaluates it alone. A count the run has not produced at that stage arrives
// null or absent and prints `-`, never `0`: a zero is a result and an absence is not. `key=value`
// fields and no head from the chat micro-format set, because this is a RECORD line.
// TOOL-dFairHearing-5 S4 - `merged` after `refuted`, so a stage before verify prints `merged=-`.
function renderShapeLine(fields) {
  return `review-shape kind=${fields.kind} round=${fields.round} intensity=${fields.intensity} at=${fields.at} ` +
    ['raw', 'confirmed', 'refuted', 'merged', 'unverified', 'blocker', 'high', 'medium', 'low']
      .map((k) => `${k}=${fields[k] === null || fields[k] === undefined ? '-' : fields[k]}`).join(' ') +
    ` agents=${fields.agents} out-tokens=${fields.outTokens === null || fields.outTokens === undefined ? 'unknown' : fields.outTokens}`
}
// TOOL-dFairHearing-17 S1 - THE ROUND STATE, pure: this round's blocker-and-high count against the rounds
// before it, in the driver's `review_state` test order — zero, then the non-decrease test against the round
// before alone, then the ceiling one run past the caller's limit, then the bound at it. A null limit
// reaches neither. The suite's parity arm holds it equal to `review_state` over the domain both see.
function deriveRoundState(priorCounts, count, roundLimit) {
  const round = priorCounts.length + 1
  if (count === 0) return 'CONVERGED'
  if (priorCounts.length && count >= priorCounts[priorCounts.length - 1]) return 'NON-CONVERGENT'
  if (roundLimit !== null && round > roundLimit) return 'CEILING'
  if (roundLimit !== null && round === roundLimit) return 'BOUNDED'
  return 'CONVERGING'
}
// S4 - the record's `review-round` line, rendered before the synthesis and copied by it; `-` is an absent
// value, never a 0, and an empty prior sequence is absent too.
function renderRoundLine(fields) {
  return `review-round round=${fields.round} ` +
    ['roundLimit', 'priorCounts', 'roundCount', 'roundState'].map((k, i) => ['limit', 'prior', 'count', 'state'][i] + '=' +
      (fields[k] === null || fields[k] === undefined || (Array.isArray(fields[k]) && !fields[k].length) ? '-' : String(fields[k]))).join(' ')
}
// The runtime's `budget.spent()` is the OUTPUT tokens spent this turn across the main loop and every
// workflow, a shared pool, so only a delta isolates a run. Read through a `typeof` guard: the harness's
// own suite and a `node` slice have no `budget`, and an absent counter is `null`, never a number.
function readOutputTokens() {
  return typeof budget === 'object' && budget !== null && typeof budget.spent === 'function' ? budget.spent() : null
}

// --- inputs (via Workflow `args`) ---------------------------------------
// { base: "<immutable SHA>",   // REQUIRED on a diff review (TOOL-dLadderedRemote-4); a spec audit ignores it
//   head: "HEAD", repo: "/path/to/worktree",
//   context: "what this diff does + the security model + what's by-design",
//   byDesign: "known/tracked issues reviewers must NOT re-report",
//   reviewDir: "where synth writes the report (repo-relative)",
//   kind: "diff-review" | "spec-audit",   // DEFAULTS to "diff-review" when absent
//   disposal: "by-nature" | "promote-all", // spec-audit ONLY: the caller's declared `spec-disposal:` value.
//                                         // Present, each BLOCKER or HIGH item owes its `specs`; absent, none does
//   subjects: [{ path, blob, id, rev, prevBlob }], // spec-audit ONLY; blob is 7-40 hex, per subject; id,
//                                         // REQUIRED at every round, is the unit id the spec defines and
//                                         // rev the integer N of the rev-N its status header carries at
//                                         // that blob, so the record's binding line pins `<id>@rev-<N>`;
//                                         // that is a SPEC subject, one whose path holds a
//                                         // builds/<slug>/spec/ segment. Any other path is a DESIGN
//                                         // subject: id required, rev refused, its id served bare and
//                                         // free to repeat; prevBlob, optional
//                                         // and legal at round > 1 only, is the 7-40 hex blob of that path
//                                         // the previous round audited, and names the fold diff
//   scratch: "<absolute session scratchpad>", // spec-audit ONLY and REQUIRED there: where a probing lens
//                                         // writes its temporary files; refused if relative, multi-line,
//                                         // carrying a .. segment, or equal to or under `repo` once both
//                                         // fold /c/ to c:/, so this kind also needs an ABSOLUTE `repo`;
//                                         // an 8.3 name or a link aliasing `repo` is not seen; a diff
//                                         // review never reads it
//   round: <integer>,                     // inferred as priorCounts.length + 1 from a non-empty priorCounts,
//                                         // else as 2 when priorFindings arrive without one; refused when it
//                                         // disagrees with a given priorCounts
//   priorFindings: [ ... ],               // a previous round's confirmed set
//   roundLimit: <integer >= 1>,           // absent -> null, no limit: BOUNDED and CEILING unreachable. The round
//                                         // at it reads BOUNDED, one past it CEILING (TOOL-dFairHearing-17)
//   priorCounts: [<integer >= 0>, ...],   // each earlier round's `roundCount`, in round order; absent at a round
//                                         // above 1 -> `roundState` null and a WARNING
//   specs: ["<repo-relative path>", ...], // intent documents: a diff review's statement of intent, a spec audit's
//                                         // sibling context; absent -> [], and with no context a WARNING
//   lensNotes: { "<lens key>": "<note>" }, // project addendum per lens of THIS kind; absent -> {} and a WARNING;
//                                         // or per preset, { "<literal name>": { "<lens key>": "<note>" } },
//                                         // keyed by diff-review or a PRESETS member, the run reading its own
//                                         // literal's entry only; a note for a default a swap displaced is unread
//   intensity: "full" | "light",          // DEFAULTS to "full"; only the CALLER picks light, which runs
//                                         // LIGHT_LENSES and names the lenses it skipped; a spec-audit refuses light
//   preset: "unit-spec" | "design-audit" | "whole-design", // spec-audit ONLY, DEFAULTS to "unit-spec": the
//                                         // CALLER's choice of lens literal, design-audit running DESIGN_LENSES,
//                                         // aimed at a design or architecture record, and whole-design the five
//                                         // walkers of WHOLE_DESIGN_LENSES; refused outside the set and on a diff review
//   walk: { items: [{ tag, step }], scenarios: [{ id, name, walks }], runs, run, seed, keySha }, // REQUIRED
//                                         // under preset whole-design and refused under any other: the design's
//                                         // item-by-scenario grid; runs is review.design-audit.runs (1-3, absent 2),
//                                         // run this invocation's run (1 to runs), seed review.design-audit.seed
//                                         // (reverted-escapes | synthetic | none, absent reverted-escapes), keySha
//                                         // the key's 64-hex SHA-256, required unless seed is none (TOOL-dFairHearing-18)
//   batchBy: "id" | "address",           // DEFAULTS to "id": the order the findings are sliced into skeptic
//                                         // batches in, "address" sorting them by deriveAddressKey so two
//                                         // lenses citing one place meet one skeptic; refused outside the set
//   addressTwins: "hidden" | "shown",    // DEFAULTS to "shown": it hands the synthesis every refuted
//                                         // finding's claim and reason and each confirmed/refuted pair at one
//                                         // address, and has it return `twinFlags`; refused outside the set
//   twin: "never" | "design-records" | "design-and-landing" | "always", // DEFAULTS to "never": the
//                                         // `review.twin` key, passed as a pin argument. A run it twins dispatches
//                                         // a second finder run, run b, and the synthesis merges the two; refused
//                                         // outside the set (TOOL-dFairHearing-11)
//   fixJudge: "instance" | "class",      // DEFAULTS to "class": it has the skeptic judge each fix by the
//                                         // defect's class and adds the fix verdict `instance`; refused outside
//                                         // the set, and it joins the review key under "class" only
//   unclassed: "refuse" | "reason" | "owner-rules", // DEFAULTS to "refuse": the `review.unclassed` key, passed
//                                         // as a pin argument, naming which `none` dispositions the check admits
//   legManifest: "<repo-relative path>",  // DEFAULTS to "tools/gate-legs.json": the leg manifest the resume
//                                         // probe reads the `gate:` leg names from; refused on the `specs` rule
//                                         // (TOOL-dFairHearing-8)
//   optIn: { "<opt-in lens key>": "<default lens key>" }, // DEFAULTS to {}: the CALLER's swap. Each key is a
//                                         // shipped opt-in lens (OPTIN_LENSES) offered for the run's literal, run
//                                         // in the slot of the default it names, so the literal keeps five. Refused
//                                         // before any agent when not an object of lens keys, and by name on a key
//                                         // already a lens, one no row offers, a default the literal lacks, or one
//                                         // default named twice; logged, in RUN INTEGRITY, and in the key when set
//   checklist: "<preamble>\n- <item>\n  <continuation>" | ["<item>", ...], // the project's recurring
//                                         // bug classes, each item swept by exactly one lens; absent on a diff review ->
//                                         // the harness acquires it (`resume:checklist`), on a spec audit -> a WARNING.
//                                         // The STRING form may carry the by-design block the checker prints
//                                         // after its items (`# by design — <n> invariant(s) this selection
//                                         // touches`, then `- ` lines): it is cut out before the items are
//                                         // parsed and joins `byDesign`. The array form carries no block.
//   workerType: "<agent type>" | "none",  // the type every finder and skeptic spawns as; absent -> Plan,
//                                         // "none" -> PLATFORM_TYPE. Under any other type no judge writes a lens file,
//                                         // so a deferred return's `durable` is false and a re-run re-dispatches every judge
//   roles: { probe, diffFinder, specFinder, skeptic, synthesis }, // TOOL-aOrientedCast-5: each an agent type
//                                         // name, never "none"; absent -> {}. A key names the type ITS stage spawns
//                                         // as and wins over `workerType`, which keeps every judge stage no key
//                                         // names; the synthesis takes its key or PLATFORM_TYPE, and the resume probe
//                                         // its key or Plan (TOOL-dFairHearing-11). Only this kind's finder key is
//                                         // read. Any judge off PLATFORM_TYPE makes the run not durable.
//   efforts: { probe, diffFinder, specFinder, skeptic, synthesis } } // TOOL-aOrientedCast-10: each a reasoning
//                                         // effort level, lower-case letters; absent -> {}. A key sets ITS stage's
//                                         // `effort` option, independent of `roles`; an unnamed stage runs at its
//                                         // agent type's level, else the session's. The caller passes what
//                                         // `handoff.py stage-efforts <workflow>` prints.
// D9 - `kind` and `subjects` were added without extending this block, and BUILD-METHOD M4 sends a
// reader HERE for the spec-audit spelling. An absent `kind` does not refuse - it defaults - so a
// header missing the field buys exactly the failure M4 exists to prevent: a code-shaped review of a
// spec, reported as a review. A pointer is only as true as the block it points at, and this one is
// asserted against the fields actually read, in <prefix>/workflows/tier2-review.test.sh.
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
const base = a.base
const head = a.head || 'HEAD'
const repo = a.repo || '.'
// TOOL-dTieredTribunal-11 S1 - the SUBJECT DESCRIPTOR. One field carries the review kind, and six
// things below become per-kind: the acquire sentence, the lens catalogue, the context default, the
// anchor predicate, the finding schema's address field, and the record's kind token.
//
// The legal set is CLOSED at two and a value outside it is REFUSED, never defaulted. A silent
// fallback to the diff kind would make a typo'd kind produce a confident review of the wrong shape
// against the wrong subject - which is the defect class the `repo` guard above exists for, one field
// over. Both members are also members of the record-kind vocabulary the memory tree closes, so the
// token this engine emits cannot leave that vocabulary without this refusal firing first.
const KINDS = ['diff-review', 'spec-audit']
const kind = a.kind === undefined ? 'diff-review' : String(a.kind)
if (KINDS.indexOf(kind) === -1) {
  throw new Error(
    'tier2-review: `kind` must be one of ' + KINDS.join(' | ') + '. Got ' + JSON.stringify(a.kind) +
      '. Refusing to default to a diff review - a typo would review the wrong subject and return ' +
      'confident, well-evidenced findings about it.',
  )
}
const isSpec = kind === 'spec-audit'
// TOOL-dFoldedAudit-15 S8 - THE ADDRESS IS OWED ON A DECLARED `disposal` ALONE, the caller's own copy of the
// `spec-disposal:` line. Only the chain reads an address, so an undeclared spec audit keeps today's
// synthesis and meets no tally fault it was never told about.
const addressOwed = isSpec && a.disposal !== undefined
// TOOL-dLadderedRemote-4 - a DIFF review's base is REQUIRED, and refused before any agent when absent.
// It defaulted to a literal remote ref, which names nothing on a node whose remote is not called
// that, and this runtime has no git to resolve the right one. A spec audit has no range and owes none.
if (!isSpec && !String(base || '').trim()) {
  throw new Error(
    'tier2-review: a diff review needs `base`, the immutable sha the diff starts from. It has no ' +
      'default: this harness cannot read which remote the repository lands on. Pin one with ' +
      'git rev-parse <the default branch>.',
  )
}
// TOOL-aSightedSkeptic-7 S1/S2 - `intensity`, the CALLER's choice of a full or a light review. A
// closed set refused outside it, like `kind`, and the harness never picks light itself. A spec audit
// has no light lens subset (spec F2), so light refuses there rather than buying a full audit silently.
const intensity = a.intensity === undefined ? 'full' : a.intensity
if (typeof intensity !== 'string' || ['full', 'light'].indexOf(intensity) === -1)
  throw new Error('tier2-review: `intensity` must be one of full | light. Got ' + JSON.stringify(a.intensity) + '.')
if (isSpec && intensity === 'light')
  throw new Error('tier2-review: a spec-audit has no light lens subset; `intensity` must be full or absent. Got "light".')
// TOOL-dFairHearing-4 S3 - `batchBy`, the order the verify stage slices its batches in, in the shape of
// `intensity`: a closed set refused outside it before any agent. It ships dark at `id` until the replay
// records a hit; `address` sorts by deriveAddressKey below. It joins no review key: a verify file is
// reused only for the exact members its batch print covers.
const batchBy = a.batchBy === undefined ? 'id' : a.batchBy
if (typeof batchBy !== 'string' || ['id', 'address'].indexOf(batchBy) === -1)
  throw new Error('tier2-review: `batchBy` must be one of id | address. Got ' + JSON.stringify(a.batchBy) + '.')
// TOOL-dFairHearing-7 S2 - `addressTwins`, in the shape of `batchBy`: a closed set refused outside it before
// any agent, `shown` by default since TOOL-dFairHearing-1's replay 3 met its bar. It joins no review key:
// the synthesis it changes writes no keyed file.
const addressTwins = a.addressTwins === undefined ? 'shown' : a.addressTwins
if (typeof addressTwins !== 'string' || ['hidden', 'shown'].indexOf(addressTwins) === -1)
  throw new Error('tier2-review: `addressTwins` must be one of hidden | shown. Got ' + JSON.stringify(a.addressTwins) + '.')
// TOOL-dFairHearing-11 S4 - `twin`, the policy key `review.twin` passed as a pin argument until dDeclaredLoop's
// `review.trigger` lands, in the shape of `intensity`: a closed set refused outside it before any agent.
// Which runs it twins is `twinned`, derived below once the subjects and the preset are read.
const TWINS = ['never', 'design-records', 'design-and-landing', 'always']
const twin = a.twin === undefined ? 'never' : a.twin
if (typeof twin !== 'string' || TWINS.indexOf(twin) === -1)
  throw new Error('tier2-review: `twin` must be one of ' + TWINS.join(' | ') + '. Got ' + JSON.stringify(a.twin) + '.')
// TOOL-dFairHearing-8 S1 - `fixJudge`, in the shape of `intensity`: a closed set refused outside it before any agent,
// `class` by default since TOOL-dFairHearing-1's replay 4 met its bar. `class` adds the fix verdict `instance` to
// FIX_VERDICTS below and joins the review key; `instance` leaves every skeptic prompt and the key as they were.
const fixJudge = a.fixJudge === undefined ? 'class' : a.fixJudge
if (typeof fixJudge !== 'string' || ['instance', 'class'].indexOf(fixJudge) === -1)
  throw new Error('tier2-review: `fixJudge` must be one of instance | class. Got ' + JSON.stringify(a.fixJudge) + '.')
// S3 - `unclassed`, the policy key `review.unclassed` passed as a pin argument until dDeclaredLoop's `review.trigger`
// lands, in the same shape: which `none` dispositions the disposition check admits.
const UNCLASSED = ['refuse', 'reason', 'owner-rules']
const unclassed = a.unclassed === undefined ? 'refuse' : a.unclassed
if (typeof unclassed !== 'string' || UNCLASSED.indexOf(unclassed) === -1)
  throw new Error('tier2-review: `unclassed` must be one of ' + UNCLASSED.join(' | ') + '. Got ' + JSON.stringify(a.unclassed) + '.')
// TOOL-dFairHearing-2 S1 - `preset`, the CALLER's choice of a spec audit's lens literal, in the shape of
// `intensity` above: a closed set refused by name outside it, and refused beside the diff kind, which
// has one literal and so no preset. Each member but the default names the `gov:lens-slots` literal it
// selects below. It ships dark: no caller in this kit passes `design-audit` until the replay's verdict.
const PRESETS = ['unit-spec', 'design-audit', 'whole-design']
const preset = a.preset === undefined ? 'unit-spec' : a.preset
if (!isSpec && a.preset !== undefined)
  throw new Error('tier2-review: `preset` picks a spec-audit lens literal, and a diff-review has none; leave it out. Got ' + JSON.stringify(a.preset) + '.')
if (typeof preset !== 'string' || PRESETS.indexOf(preset) === -1)
  throw new Error('tier2-review: `preset` must be one of ' + PRESETS.join(' | ') + '. Got ' + JSON.stringify(a.preset) + '.')
// TOOL-dFairHearing-18 S1 - `walk`, the whole-design walk's grid, checked ONCE, here, before the resume probe:
// required under `whole-design` and refused under any other preset, each refusal naming its field. The anchored
// shapes keep a newline, a pipe and a backtick out of every prompt line and table cell a tag, step or id reaches;
// `name` and `walks` reach the prompts through renderPromptLine's line-break fold. One invocation is one run
// (spec section 8 F3): `review.pin` invokes the harness `runs` times, `run` 1 to `runs`.
const isWalk = preset === 'whole-design'
const WALK_TAG = /^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$/
const WALK_SCENARIO_ID = /^[A-Za-z0-9][A-Za-z0-9._-]{0,31}$/
const WALK_SEEDS = ['reverted-escapes', 'synthetic', 'none']
const WALK_SLICING = ['scenario', 'step', 'diagonal'] // run 1, 2 and 3
const WALK_VERDICTS = ['holds', 'finding', 'not-on-path']
function checkWalk(w) {
  const buildRefusal = (field, rule, got) => new Error('tier2-review: `' + field + '` ' + rule + '. Got ' + JSON.stringify(got) + '.')
  if (!w || typeof w !== 'object' || Array.isArray(w))
    throw buildRefusal('walk', 'must be an object {items, scenarios, runs, run, seed, keySha}', w)
  const items = w.items
  if (!Array.isArray(items) || !items.length) throw buildRefusal('walk.items', 'must be a non-empty array of {tag, step}', items)
  const badItem = items.findIndex((x) => !x || typeof x !== 'object' || typeof x.tag !== 'string' || !WALK_TAG.test(x.tag) ||
    typeof x.step !== 'string' || !WALK_TAG.test(x.step))
  if (badItem !== -1) throw buildRefusal('walk.items', 'member ' + badItem + ' must be {tag, step}, each a string matching ' + WALK_TAG.source, items[badItem])
  const twiceTag = items.findIndex((x, i) => items.findIndex((y) => y.tag === x.tag) !== i)
  if (twiceTag !== -1) throw buildRefusal('walk.items', 'member ' + twiceTag + ' repeats the tag ' + items[twiceTag].tag + ', and tags are unique', items[twiceTag])
  const scenarios = w.scenarios
  if (!Array.isArray(scenarios) || !scenarios.length) throw buildRefusal('walk.scenarios', 'must be a non-empty array of {id, name, walks}', scenarios)
  const badScenario = scenarios.findIndex((x) => !x || typeof x !== 'object' || typeof x.id !== 'string' || !WALK_SCENARIO_ID.test(x.id) ||
    typeof x.name !== 'string' || !x.name.trim() || typeof x.walks !== 'string' || !x.walks.trim())
  if (badScenario !== -1)
    throw buildRefusal('walk.scenarios', 'member ' + badScenario + ' must be {id, name, walks}, id matching ' + WALK_SCENARIO_ID.source + ' and name and walks non-empty strings', scenarios[badScenario])
  const twiceId = scenarios.findIndex((x, i) => scenarios.findIndex((y) => y.id === x.id) !== i)
  if (twiceId !== -1) throw buildRefusal('walk.scenarios', 'member ' + twiceId + ' repeats the id ' + scenarios[twiceId].id + ', and ids are unique', scenarios[twiceId])
  const runs = w.runs === undefined ? 2 : w.runs
  if ([1, 2, 3].indexOf(runs) === -1) throw buildRefusal('walk.runs', 'must be review.design-audit.runs, 1, 2 or 3, or absent for 2', w.runs)
  if (!Number.isInteger(w.run) || w.run < 1 || w.run > runs)
    throw buildRefusal('walk.run', 'must be the integer from 1 to walk.runs (' + runs + ') naming which run this invocation is', w.run)
  const seed = w.seed === undefined ? 'reverted-escapes' : w.seed
  if (WALK_SEEDS.indexOf(seed) === -1) throw buildRefusal('walk.seed', 'must be review.design-audit.seed, one of ' + WALK_SEEDS.join(' | ') + ', or absent for reverted-escapes', w.seed)
  if ((w.keySha !== undefined && (typeof w.keySha !== 'string' || !/^[0-9a-f]{64}$/.test(w.keySha))) || (w.keySha === undefined && seed !== 'none'))
    throw buildRefusal('walk.keySha', 'must be the key\'s SHA-256, 64 lower-case hex, and is required unless walk.seed is none', w.keySha)
  return { items: items.map((x) => ({ tag: x.tag, step: x.step })), scenarios: scenarios.map((x) => ({ id: x.id, name: x.name, walks: x.walks })),
    runs: runs, run: w.run, seed: seed, keySha: w.keySha === undefined ? null : w.keySha }
}
if (isWalk && a.walk === undefined)
  throw new Error('tier2-review: `walk` is required under preset whole-design: the design\'s items and scenarios, and which run this is. Got undefined.')
if (!isWalk && a.walk !== undefined)
  throw new Error('tier2-review: `walk` is read under preset whole-design alone; leave it out under ' + (isSpec ? 'preset ' + preset : 'a diff-review') + '. Got ' + JSON.stringify(a.walk) + '.')
const walk = isWalk ? checkWalk(a.walk) : null
// TOOL-aSightedSkeptic-4 S2-S6 - THE SPLIT. Item n goes to keys[(n - 1) % K], so every item is in
// exactly one share and the split is a pure function of the items and the keys: a reused lens file
// (S7) held the share this run would hand it. Round-robin, not contiguous `chunk`: a contiguous split
// hands one lens a run of neighbouring classes and the last lens the short remainder (spec F1 and §10).
// It runs over the keys of the lenses that RUN (S7 below), never by reshaping the LENSES receiver the fan-out leg sizes.
// TOOL-dFairHearing-18 S2 - moved up from beside the checklist split, unchanged, so the prelude's walk slicer reaches it.
function deriveChecklistShares(items, keys) {
  const shares = {}
  for (const k of keys) shares[k] = []
  items.forEach((text, i) => shares[keys[i % keys.length]].push({ n: i + 1, text: text }))
  return shares
}
// TOOL-dFairHearing-18 S2 - THE SLICES, pure: every cell `[itemTag, scenarioId]` of the item-by-scenario grid in
// exactly one of the five walker slots, in item-then-scenario order. Run 1 deals the scenarios round-robin through
// deriveChecklistShares, keyed by slot position, the order the walker lenses fill WHOLE_DESIGN_LENSES in; run 2
// cuts the steps, in first-seen item order, into contiguous bands; run 3 deals cell (i, j) to (i + j) mod 5
// (spec section 8 F4). An empty slice is a walker slot this run does not dispatch.
// ponytail: run 2 places each step's band at its item-count midpoint, which is even to within a step; an exact
// partition search if a design ever needs the bands evener than that.
function deriveWalkSlices(items, scenarios, run) {
  const slots = [0, 1, 2, 3, 4]
  const dealt = deriveChecklistShares(scenarios.map((s) => s.id), slots)
  const scenarioSlot = new Map()
  for (const w of slots) for (const x of dealt[w]) scenarioSlot.set(x.text, w)
  const stepCount = new Map()
  for (const x of items) stepCount.set(x.step, (stepCount.get(x.step) || 0) + 1)
  const stepSlot = new Map()
  let before = 0
  for (const [step, n] of stepCount) {
    stepSlot.set(step, Math.min(4, Math.floor(((before + n / 2) * 5) / items.length)))
    before += n
  }
  const slices = slots.map(() => [])
  items.forEach((x, i) => scenarios.forEach((s, j) => {
    const w = run === 1 ? scenarioSlot.get(s.id) : run === 2 ? stepSlot.get(x.step) : (i + j) % 5
    slices[w].push([x.tag, s.id])
  }))
  return slices
}
// TOOL-dFairHearing-18 S4 - THE GAPS, pure: one `<item> · <scenario> — <what>` per defect of a walker's table
// against its slice. `returns[w]` is slot w's walker return, null where none came back. A cell of the slice with
// no row or with two, a row outside the slice, an actor, needs, witness or route empty once trimmed, a verdict
// outside the three, `finding` with no index or one past the walker's findings, `not-on-path` with an empty
// reason, and `holds` carrying an index are each a gap. A run with any gap is red.
function deriveWalkGaps(slices, returns) {
  const gaps = []
  slices.forEach((cells, w) => {
    const r = returns[w]
    const rows = r && Array.isArray(r.walk) ? r.walk : []
    const n = r && Array.isArray(r.findings) ? r.findings.length : 0
    const mine = new Set(cells.map((c) => c[0] + ' · ' + c[1]))
    const byCell = new Map()
    for (const x of rows) {
      const cell = String(x && x.item) + ' · ' + String(x && x.scenario)
      if (!mine.has(cell)) gaps.push(cell + ' — a row outside walker slot ' + (w + 1) + '\'s slice')
      else byCell.set(cell, (byCell.get(cell) || []).concat([x]))
    }
    for (const cell of mine) {
      const got = byCell.get(cell) || []
      if (got.length !== 1) {
        gaps.push(cell + ' — ' + (got.length ? got.length + ' rows' : 'no row'))
        continue
      }
      const x = got[0]
      for (const k of ['actor', 'needs', 'witness', 'route'])
        if (typeof x[k] !== 'string' || !x[k].trim()) gaps.push(cell + ' — ' + k + ' is empty')
      const idx = Array.isArray(x.findings) ? x.findings : []
      const past = idx.filter((k) => !Number.isInteger(k) || k < 0 || k >= n)
      if (WALK_VERDICTS.indexOf(x.verdict) === -1) gaps.push(cell + ' — verdict ' + JSON.stringify(x.verdict) + ' is none of ' + WALK_VERDICTS.join(' | '))
      else if (x.verdict === 'finding' && !idx.length) gaps.push(cell + ' — verdict finding names no finding index')
      else if (x.verdict === 'finding' && past.length) gaps.push(cell + ' — finding index ' + past.join(', ') + ' names none of the walker\'s ' + n + ' finding(s)')
      else if (x.verdict === 'not-on-path' && (typeof x.reason !== 'string' || !x.reason.trim())) gaps.push(cell + ' — not-on-path with an empty reason')
      else if (x.verdict === 'holds' && idx.length) gaps.push(cell + ' — holds carrying a finding index')
    }
  })
  return gaps
}
// TOOL-dFairHearing-3 S1 - `optIn`, the CALLER's swap of an opt-in lens into a default slot of the run's
// literal, `{ "<opt-in>": "<default it replaces>" }`, absent meaning {}. Its SHAPE is refused here, beside
// `intensity` and `preset`, before the literals read it; its MEMBERSHIP is checked once beside `lensNotes`
// below, because that needs the literal's default keys. A lens key has the catalogue's key grammar.
const LENS_KEY_SHAPE = /^[a-z][a-z0-9-]*$/
const optIn = a.optIn === undefined ? {} : a.optIn
if (!optIn || typeof optIn !== 'object' || Array.isArray(optIn) ||
    Object.keys(optIn).some((k) => !LENS_KEY_SHAPE.test(k) || typeof optIn[k] !== 'string' || !LENS_KEY_SHAPE.test(optIn[k])))
  throw new Error('tier2-review: `optIn` must be an object mapping an opt-in lens key to the default lens key it replaces, ' +
    'each matching ' + LENS_KEY_SHAPE.source + '. Got ' + JSON.stringify(a.optIn) + '.')
// TOOL-aMendedFleet-67 S1/S2 - `workerType`, the agent type the JUDGES spawn as: every finder and every
// skeptic, never the resume probe or the synthesis, which read and write the lens files and the report.
// Shape-checked here, before any spawn. The built-in types that omit the charter hold no Write tool,
// so under one the judges get no DURABILITY instruction and the run says its results are not durable.
// TOOL-aMendedFleet-93 S4 - absent reads as `Plan`, the default the charter A/B's reading set; the
// reserved literal `none` spawns as before the default, durability instructions and review key included.
// TOOL-aOrientedCast-5 S2 - the agent-type shape is ONE constant both refusals below test; the
// protocol-parity leg's agent-type shape arm reads this declaration as the kit's one owner literal.
const AGENT_TYPE_SHAPE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/
const workerType = a.workerType === undefined ? 'Plan' : a.workerType === 'none' ? '' : a.workerType
if (a.workerType !== undefined && (typeof a.workerType !== 'string' || !AGENT_TYPE_SHAPE.test(a.workerType)))
  throw new Error('tier2-review: `workerType` must be an agent type name matching ' + AGENT_TYPE_SHAPE.source + '. Got ' + JSON.stringify(a.workerType) + '.')
// TOOL-aOrientedCast-5 S1/S3 - `roles`, the catalogue role each STAGE spawns as. Refused before any
// agent when it is not a plain object, carries a key outside ROLE_KEYS, or a value that is not a type
// name; `none` is refused too, since an untyped stage is spelled by leaving its key out. A key names
// its own stage and wins over `workerType`, which keeps every judge stage no key names (spec section 8
// F1); the synthesis, which `workerType` never governed, takes its key or PLATFORM_TYPE, and the resume
// probe its key or Plan (TOOL-dFairHearing-11 S1/S2). Only this kind's finder key is read.
const ROLE_KEYS = ['probe', 'diffFinder', 'specFinder', 'skeptic', 'synthesis']
const roles = a.roles === undefined ? {} : a.roles
if (!roles || typeof roles !== 'object' || Array.isArray(roles) || Object.prototype.toString.call(roles) !== '[object Object]')
  throw new Error('tier2-review: `roles` must be an object mapping a stage key to an agent type name; legal keys: ' + ROLE_KEYS.join(' | ') +
    ', each value matching ' + AGENT_TYPE_SHAPE.source + ' and not none. Got ' + JSON.stringify(a.roles) + '.')
for (const k of Object.keys(roles)) {
  if (ROLE_KEYS.indexOf(k) === -1)
    throw new Error('tier2-review: `roles` carries the key ' + JSON.stringify(k) + ', which names no stage; legal keys: ' + ROLE_KEYS.join(' | ') + '.')
  if (typeof roles[k] !== 'string' || !AGENT_TYPE_SHAPE.test(roles[k]) || roles[k] === 'none')
    throw new Error('tier2-review: `roles` key ' + k + ' must be an agent type name matching ' + AGENT_TYPE_SHAPE.source +
      ', and not none (leave the key out for an untyped stage); legal keys: ' + ROLE_KEYS.join(' | ') + '. Got ' + JSON.stringify(roles[k]) + '.')
}
const finderKey = isSpec ? 'specFinder' : 'diffFinder'
const otherFinderKey = isSpec ? 'diffFinder' : 'specFinder'
// TOOL-dFairHearing-11 S2 - THE STAGE TABLE: every stage resolves an explicit type. PLATFORM_TYPE, the Agent
// tool's own default, is the type a stage takes where it took none before: the synthesis with no role, and a
// judge stage under `workerType: 'none'` that no role names. The probe judges and writes nothing, so it takes
// Plan, which holds no Write tool (spec section 8 F3).
const PLATFORM_TYPE = 'general-purpose'
const probeType = roles.probe || 'Plan'
const findType = roles[finderKey] || workerType || PLATFORM_TYPE
const verifyType = roles.skeptic || workerType || PLATFORM_TYPE
const synthType = roles.synthesis || PLATFORM_TYPE
// S3 - no agent spawns untyped: a stage that resolves to no type is refused by name before the probe.
const STAGE_TYPES = { probe: probeType, [finderKey]: findType, skeptic: verifyType, synthesis: synthType }
for (const k of Object.keys(STAGE_TYPES))
  if (!STAGE_TYPES[k]) throw new Error('tier2-review: the stage ' + k + ' resolves to no agent type, and no agent spawns untyped; name one as roles.' + k + '.')
const roledJudges = !!(roles[finderKey] || roles.skeptic)
// TOOL-aOrientedCast-10 S7 - `efforts`, the reasoning effort each STAGE spawns at, keyed as `roles`
// is. Refused before any agent when it is not a plain object, carries a key outside ROLE_KEYS, or a
// value that is not lower-case letters. The level vocabulary is the roles library's, which the caller
// read it from; this file grades the shape only, so no second copy of the vocabulary exists here.
const EFFORT_SHAPE = /^[a-z]+$/
const efforts = a.efforts === undefined ? {} : a.efforts
if (!efforts || typeof efforts !== 'object' || Array.isArray(efforts) || Object.prototype.toString.call(efforts) !== '[object Object]')
  throw new Error('tier2-review: `efforts` must be an object mapping a stage key to an effort level; legal keys: ' + ROLE_KEYS.join(' | ') +
    ', each value matching ' + EFFORT_SHAPE.source + '. Got ' + JSON.stringify(a.efforts) + '.')
for (const k of Object.keys(efforts)) {
  if (ROLE_KEYS.indexOf(k) === -1)
    throw new Error('tier2-review: `efforts` carries the key ' + JSON.stringify(k) + ', which names no stage; legal keys: ' + ROLE_KEYS.join(' | ') + '.')
  if (typeof efforts[k] !== 'string' || !EFFORT_SHAPE.test(efforts[k]))
    throw new Error('tier2-review: `efforts` key ' + k + ' must be an effort level matching ' + EFFORT_SHAPE.source +
      ' (leave the key out to run at the agent type\'s own level); legal keys: ' + ROLE_KEYS.join(' | ') + '. Got ' + JSON.stringify(efforts[k]) + '.')
}
function renderStageOpts(type, key) {
  return Object.assign(type ? { agentType: type } : {}, efforts[key] ? { effort: efforts[key] } : {})
}
const findOpts = renderStageOpts(findType, finderKey)
const verifyOpts = renderStageOpts(verifyType, 'skeptic')
const synthOpts = renderStageOpts(synthType, 'synthesis')
const probeOpts = renderStageOpts(probeType, 'probe')
// TOOL-aMendedFleet-111 S6 - whether the judges' results outlive this run. Under a named type no judge
// writes its file, so every deferred note says a re-run dispatches every finder and skeptic again, and
// every return carrying `pending` carries `durable` too, so a caller reads the fact, not the prose.
// TOOL-aOrientedCast-5 S4 - it reads the judge stages' RESOLVED types, so a roled judge counts as a
// named type, and a mixed run's untyped judge stage is told to write no file as well (spec section 8 F3).
// TOOL-dFairHearing-11 S2 - both judge stages at PLATFORM_TYPE, the case an empty type covered before.
const durable = findType === PLATFORM_TYPE && verifyType === PLATFORM_TYPE
function renderRerunTail(only, synthToo) {
  return durable
    ? `re-run with identical args to dispatch only ${only}`
    : `this run wrote no result file, so a re-run with identical args dispatches every finder and skeptic again${synthToo ? ', plus the synthesis' : ''}`
}
// TOOL-aBoundedVerdict-14 S1/S2 - the fold-scoping inputs. `priorFindings` is deliberately NOT merged
// into `byDesign`: they are different instructions. byDesign says "this is intended, do not report
// it"; a prior finding says "this was reported and FIXED - check the fix, and do not re-raise the
// original". Collapsing them loses the second half, which is the half this unit exists for. When
// that unit measured, no caller filled `byDesign`; the checklist's by-design block now does, and it is
// intended behaviour, never a fixed defect, so the two stay apart.
const priorFindings = Array.isArray(a.priorFindings) ? a.priorFindings : []
// F1 resolved: accept an explicit integer AND infer 2 when prior findings arrive without one, so a
// caller cannot silently get a round-1 brief while handing over a previous round's confirmed set.
// TOOL-dFairHearing-17 S2 - `roundLimit` and `priorCounts`, checked here beside `round`, before any agent, so no
// string reaches a prompt from them; neither joins the review key, as no lens or skeptic prompt reads either.
const roundLimit = a.roundLimit === undefined ? null : a.roundLimit
if (roundLimit !== null && !(Number.isInteger(roundLimit) && roundLimit >= 1))
  throw new Error('tier2-review: `roundLimit` must be an integer of 1 or more, or absent for no limit. Got ' + JSON.stringify(a.roundLimit) + '.')
const priorCounts = a.priorCounts === undefined ? null : a.priorCounts
if (priorCounts !== null && !(Array.isArray(priorCounts) && priorCounts.every((c) => Number.isInteger(c) && c >= 0)))
  throw new Error('tier2-review: `priorCounts` must be an array of integers of 0 or more, each an earlier round\'s roundCount in round order. Got ' + JSON.stringify(a.priorCounts) + '.')
const explicitRound = Number.isInteger(a.round) && a.round > 0
if (explicitRound && priorCounts !== null && a.round !== priorCounts.length + 1)
  throw new Error('tier2-review: `round` ' + a.round + ' disagrees with `priorCounts` ' + JSON.stringify(priorCounts) + ', whose ' +
    priorCounts.length + ' earlier round(s) make this round ' + (priorCounts.length + 1) + '.')
const round = explicitRound ? a.round : priorCounts !== null && priorCounts.length ? priorCounts.length + 1 : priorFindings.length ? 2 : 1
// S3 / F6 - the rule runs only where the prior sequence matches the round: round 1 with none reads as [],
// and a later round with none, or with a sequence that cannot be its own, has no state rather than a guessed one.
const roundStateKnown = priorCounts === null ? round === 1 : priorCounts.length + 1 === round
function deriveRoundFields(count) {
  return { roundCount: count, roundState: count !== null && roundStateKnown ? deriveRoundState(priorCounts || [], count, roundLimit) : null }
}
const reviewDir = a.reviewDir || 'reviews/'
// TOOL-aOrientedCast-27 S3/S9 - every agent's label and the run's identity, `<slug> · <scope> · <stage>`.
// The slug is the segment after a `builds/` segment of `reviewDir` when it is letters only, else none,
// so a review outside a build folder carries no slug part. The stage is the label a spawn carried
// before, so `pending`, the log lines and every reader of a stage keep their spelling. The build
// harness holds its own copy of the function, because a workflow script imports nothing.
const reviewSlug = (/(?:^|\/)builds\/([A-Za-z]+)(?:\/|$)/.exec(String(reviewDir).replace(/\\/g, '/')) || [])[1] || ''
const reviewScope = kind + ' round ' + round
function renderAgentLabel(scope, stage) {
  return [reviewSlug, scope, stage].filter(Boolean).join(' · ')
}
// TOOL-dTrueNorth-5 S1 - a spec audit's binding line, RENDERED here and copied by the synthesis agent:
// each spec subject's `<id>@rev-<rev>` in subject order, so the record pins the revision of every spec it
// read and a revision past that pin reads as unaudited. Pure, and reached only with subjects the pin
// refusal below has passed, so each id matches an anchored grammar and carries no newline.
// TOOL-dTrueNorth-13 S1/S2 - TWO subject classes, told apart by PATH and never by id: one id can name
// both a spec and the design document it carries. A SPEC subject's path holds a builds/<slug>/spec/
// segment and its id is pinned; every other subject is a DESIGN subject, served bare, because a design
// document has no rev header to pin. Each id is rendered once, in first-seen order, and an id a spec
// subject pins is never repeated bare beside its pin.
const SPEC_SUBJECT_PATH = /(?:^|\/)builds\/[^/]+\/spec\//
function renderAuditBinding(subjects) {
  const pins = {}
  const ids = []
  subjects.forEach(function (x) {
    if (SPEC_SUBJECT_PATH.test(String(x.path))) pins[x.id] = x.rev
    if (ids.indexOf(x.id) === -1) ids.push(x.id)
  })
  return '**Serves:** spec-audit ' + ids.map(function (id) {
    return Object.prototype.hasOwnProperty.call(pins, id) ? id + '@rev-' + pins[id] : id
  }).join(' ')
}
// TOOL-dTrueNorth-13 S3 - the record's SUBJECTS line, rendered here too, so its reader has one spelling
// to read: `Reviewed: <path>@<blob>, ...` in subject order. The memory tree's pin grading reads which
// paths a spec audit reviewed off this line, and the corpus spelled it three ways while an agent
// composed it.
function renderReviewedLine(subjects) {
  return 'Reviewed: ' + subjects.map(function (x) { return x.path + '@' + x.blob }).join(', ')
}
// TOOL-dFairHearing-4 S1 - THE ADDRESS KEY, one reading of where a finding points, pure. `file` is
// slash-folded with one leading ./ dropped; `at` is the diff kind's integer line, or the spec kind's
// first [tag] in `where`, else its LEFTMOST whole-word section token (section <n> and § <n> as §<n>,
// S<n> and AC<n> upper-cased), else null. It never reads `ref`, so nothing is keyed on a ref string.
const ADDRESS_TAG = /\[([a-z][a-z0-9-]*)\]/
const ADDRESS_SECTION = /\bsection ?(\d+)\b|§ ?(\d+)\b|\b(S|AC)(\d+)\b/i
function deriveAddressKey(f) {
  const file = String(f.file).trim().replace(/\\/g, '/').replace(/^\.\//, '')
  let at = null
  if (!isSpec) at = Number.isInteger(f.line) ? f.line : null
  else {
    const where = String(f.where === undefined || f.where === null ? '' : f.where)
    const tag = ADDRESS_TAG.exec(where)
    const sec = tag ? null : ADDRESS_SECTION.exec(where)
    if (tag) at = '[' + tag[1] + ']'
    else if (sec) at = sec[3] ? sec[3].toUpperCase() + sec[4] : '§' + (sec[1] || sec[2])
  }
  return { file: file, at: at, lens: f.lens, id: f.id }
}
// S1 - two keys name one address when the files match, neither `at` is null, and the lines differ by at
// most ADDRESS_LINE_SLACK or the tokens are equal. The slack lives here, never in the sort: equality
// within a tolerance is not transitive, so it cannot be a sort key (spec section 8 F2).
const ADDRESS_LINE_SLACK = 3
function checkSameAddress(x, y) {
  if (x.file !== y.file || x.at === null || y.at === null) return false
  return typeof x.at === 'number' && typeof y.at === 'number' ? Math.abs(x.at - y.at) <= ADDRESS_LINE_SLACK : x.at === y.at
}
// TOOL-dFairHearing-7 S1 - THE TWIN PAIRS, pure: each confirmed and refuted finding checkSameAddress reads as
// one address, in confirmed-id then refuted-id order. The caller hands `refuted` without a merged duplicate.
// ponytail: O(confirmed x refuted), tens by tens on a review; sort by address key if a run ever holds thousands.
function deriveTwinPairs(confirmed, refuted) {
  const out = []
  for (const c of confirmed)
    for (const r of refuted)
      if (checkSameAddress(deriveAddressKey(c), deriveAddressKey(r))) out.push({ confirmed: c.id, refuted: r.id })
  return out
}
// S2 - a sorted COPY: file, then `at` (lines by value, tokens by code unit, null after every address of
// its file), then lens, then id. The argument keeps id order for the ledger, the appendix and the yield.
function deriveAddressOrder(findings) {
  const cmp = (p, q) => (p === q ? 0 : p < q ? -1 : 1)
  const cmpAt = (p, q) => (p === q ? 0 : p === null ? 1 : q === null ? -1 : typeof p === 'number' && typeof q === 'number' ? p - q : cmp(String(p), String(q)))
  return findings
    .map((f) => [deriveAddressKey(f), f])
    .sort((u, v) => cmp(u[0].file, v[0].file) || cmpAt(u[0].at, v[0].at) || cmp(String(u[0].lens), String(v[0].lens)) || u[0].id - v[0].id)
    .map((pair) => pair[1])
}
// TOOL-dFairHearing-5 S1 - THE DUPLICATE REASON FORM, read once: the id a refutation opening
// `duplicate of id=<n>` names, else null. The orphan check, the merged count and the lens yield all
// read it here; `duplicate of prior <ref>` names a previous round's finding and reads null.
const DUPLICATE_REASON = /^duplicate of id=(\d+)/i
function extractDuplicateTarget(reason) {
  const m = DUPLICATE_REASON.exec(String(reason || '').trim())
  return m ? Number(m[1]) : null
}
// The run's identity is its first log line and the first key of every return: the tool titles the
// run with `meta.name` alone.
const identity = renderAgentLabel(reviewScope, 'review')
log(identity)
if (!durable && workerType && !roledJudges)
  log(`worker type ${workerType} — every finder and skeptic spawns as it and writes no find-*.json or verify-*.json, so this run's lens and batch results are NOT durable and a resume re-dispatches them`)
if (!durable && roledJudges)
  log(`judges under a named type — no finder or skeptic writes a find-*.json or verify-*.json, so this run's lens and batch results are NOT durable and a resume re-dispatches them`)
// TOOL-aOrientedCast-5 S7 - one line per stage on every run, naming its type and where it came from.
// TOOL-dFairHearing-11 S1 - the probe's included.
log(`role probe: ${probeType} — ${roles.probe ? 'roles.probe' : 'no roles.probe, so Plan'}`)
log(`role find: ${findType} — ${roles[finderKey] ? `roles.${finderKey}` : workerType ? 'workerType' : `no roles.${finderKey}, and workerType is none`}`)
log(`role verify: ${verifyType} — ${roles.skeptic ? 'roles.skeptic' : workerType ? 'workerType' : 'no roles.skeptic, and workerType is none'}`)
log(`role synthesis: ${synthType} — ${roles.synthesis ? 'roles.synthesis' : 'no roles.synthesis, so PLATFORM_TYPE'}`)
if (roles[otherFinderKey] !== undefined)
  log(`role find: roles.${otherFinderKey} is not read on a ${kind}`)
// TOOL-dFairHearing-17 S2 - each degraded round-state input said once, before the first agent (spec section 8 F5, F6).
if (roundLimit === null) log('round state: no roundLimit was passed, so this round can read neither BOUNDED nor CEILING')
if (!roundStateKnown)
  log(`WARNING: round ${round} with ${priorCounts === null ? 'no priorCounts' : 'priorCounts ' + JSON.stringify(priorCounts)}, ` +
    'so roundState is null: pass each earlier round\'s roundCount as priorCounts to compute it')
// TOOL-aOrientedCast-10 S7 - one line per stage on every run, naming its effort and where it came from.
for (const k of ['probe', finderKey, 'skeptic', 'synthesis'])
  log(efforts[k] ? `effort ${k}: ${efforts[k]} — efforts.${k}` : `effort ${k}: the agent type's own, else the session's — no efforts.${k}`)
if (efforts[otherFinderKey] !== undefined)
  log(`effort ${otherFinderKey}: efforts.${otherFinderKey} is not read on a ${kind}`)
// S7 - the context default is per-kind, and each is wrong if the other kind inherits it.
const context = a.context || (isSpec ? 'the spec set under audit' : 'the cumulative diff landing on main')
// `byDesign` is RESOLVED below, after the checklist's by-design block is cut out (TOOL-aGraftedHelix-3).
// S3 - a base that is not an immutable sha is REFUSED at round > 1 and warned at round 1. The
// harness has no filesystem and cannot resolve a ref, so this is a STRING check on the shape of what
// it was handed: the caller resolves, and the harness refuses anything that does not look resolved.
// F2 resolved at 7+ hex, the same floor the driver's own review-record join uses and the shortest
// abbreviation git produces here - not 40, which would refuse the spelling the corpus actually uses.
// TOOL-dTieredTribunal-11 S5 - the anchor dispatches per kind, and it is ONE predicate over two
// populations. A spec has no commit range, so the spec kind pins a BLOB per subject: a blob changes
// with every fold, where the spec's own `base` header is identical across every rev and would
// satisfy any string test - a check that cannot fail, in a unit whose subject is checks that cannot
// fail. The orchestrator cannot tell a commit sha from a blob sha, so S6 pushes the VERIFICATION
// into the lens, which is the only actor here holding a filesystem.
// AC5 - ONE spelling of the anchor shape, because two arms testing the same property from two
// copies of one regex is the drift this build spent a unit on. Both the per-subject blob and the
// `base` sha are "an immutable 7-40 hex object id", which is one question with one answer.
const PINNED_SHA = /^[0-9a-f]{7,40}$/
// `expand_id_runs`' id grammar, anchored: a subject's pin below and a finding's address in the tally.
const PIN_ID = /^[A-Z]+-[A-Za-z0-9]+-[0-9]+$/
const subjects = Array.isArray(a.subjects) ? a.subjects : []
if (isSpec) {
  // D6 - `find(pred) || null` collapsed a FALSY offender back onto the pass sentinel, so the `!x`
  // arm - the only arm of this predicate that can return a falsy value - could never fire the
  // refusal it was written for. `[null]`, `[undefined]`, `[0]`, `['']` and `[false]` all skipped
  // both the round-1 warning and the round>1 throw, and because `find` returns the FIRST match, a
  // genuinely bad subject sitting after a falsy one was masked along with them. An INDEX sentinel
  // cannot collide with a value the predicate is allowed to select, which is the general shape:
  // never sentinel on a value the thing you are testing may legitimately return.
  const badIdx = subjects.findIndex(
    (x) => !x || typeof x !== 'object' || typeof x.path !== 'string' || !PINNED_SHA.test(String(x.blob))
  )
  // ...and the BRANCH is on the index, never on the value. Restoring a `badSubject !== null` test
  // here would have reintroduced the identical collapse one line further down, because a `[null]`
  // element makes that value null all over again - which is exactly the shape the review that
  // found the original defect proposed as its fix. The self-test's two null arms caught it on the
  // first run. The value below is carried for the MESSAGE and decides nothing.
  const noSubjects = subjects.length === 0
  if (noSubjects || badIdx !== -1) {
    const badSubject = noSubjects ? 'none supplied' : subjects[badIdx]
    const why =
      'tier2-review: a spec-audit needs `subjects`, a non-empty array of {path, blob, id, rev}, where blob is ' +
      'an immutable 7-40 hex object id. Got ' + JSON.stringify(badSubject) + '. The anchor is what ' +
      'makes "which rev was reviewed" answerable from the record; a spec header base is the same on ' +
      'every rev and would prove nothing. Resolve one: git hash-object <path>.'
    // M8 closing review, BLOCKER: an EMPTY subject set is not a degraded run, it is an empty one,
    // and the round-1 warn let it through. Four lenses were then handed nothing to read, found
    // nothing, and the run returned `clean: 0 findings` - a degraded run reporting a clean bill,
    // which is the degradation-known-but-unreported family this same diff added to the catalogue,
    // inside one of that record's own anchors. A MALFORMED blob keeps the warn-then-refuse ladder,
    // because there a caller has named a subject and got its anchor wrong, and round 1 is where a
    // caller is still resolving them. Nothing to review at all is refused at every round.
    if (noSubjects) {
      throw new Error(why + ' A spec audit with no subject reviews nothing, and a run that reviewed nothing may not report a clean bill.')
    }
    if (round > 1) throw new Error(why)
    log('WARNING: ' + why)
  }
  // TOOL-dTrueNorth-5 S1 - THE PIN, refused at EVERY round. The record's binding line names each spec
  // it read as `<id>@rev-<N>` (`renderAuditBinding`), so a subject with no well-formed `id`, or a spec
  // subject with no well-formed `rev`, leaves the record nothing to pin. Round 1 refuses too, unlike a malformed blob: the record is the
  // point of the run, and an unpinned one is what this refusal exists to stop. The id grammar is
  // `PIN_ID`, hoisted above, which also keeps a newline out of the prompt line the id reaches.
  const pinWhy = ' The pin is what makes a revision of that spec past it read as unaudited.'
  const pinnedIds = []
  for (let i = 0; i < subjects.length; i++) {
    const x = subjects[i] && typeof subjects[i] === 'object' ? subjects[i] : {}
    if (typeof x.id !== 'string' || !PIN_ID.test(x.id))
      throw new Error('tier2-review: spec-audit subject ' + i + "'s `id` must be the unit id its spec defines, matching " +
        String(PIN_ID) + '. Got ' + JSON.stringify(x.id) + '.' + pinWhy)
    // TOOL-dTrueNorth-13 S1 - a DESIGN subject, any path with no builds/<slug>/spec/ segment, carries
    // its id bare: a `rev` on it is refused by name, since no rev header exists to pin, and it is exempt
    // from the repeat refusal below, so two design documents of one id, or a design document beside its
    // spec, audit together. This supersedes the refusal of every subject without a `rev`.
    if (!SPEC_SUBJECT_PATH.test(String(x.path))) {
      if (x.rev !== undefined)
        throw new Error('tier2-review: spec-audit subject ' + i + "'s `rev` is refused: its path " + JSON.stringify(x.path) +
          ' holds no builds/<slug>/spec/ segment, so it is a design-document subject, whose id the binding line ' +
          'serves bare. Got ' + JSON.stringify(x.rev) + '. Drop the rev, or name the spec file the rev belongs to.')
      continue
    }
    if (!Number.isInteger(x.rev) || x.rev < 1)
      throw new Error('tier2-review: spec-audit subject ' + i + "'s `rev` must be the integer N of the rev-N its spec's " +
        'status header carries at that blob, 1 or more. Got ' + JSON.stringify(x.rev) + '.' + pinWhy)
    if (pinnedIds.indexOf(x.id) !== -1)
      throw new Error('tier2-review: spec-audit subject ' + i + "'s `id` " + x.id + ' repeats subject ' + pinnedIds.indexOf(x.id) +
        "'s, and a binding line carries one pin per id." + pinWhy)
    // At the SUBJECT's index, so the repeat message names the subject: a design subject skipped above
    // leaves a hole, and `indexOf` skips holes.
    pinnedIds[i] = x.id
  }
  // TOOL-aEvidencedLens-4 S1 - `prevBlob`, the blob the previous round audited. Refused when malformed
  // and refused at round 1 at any shape (spec F1): it has no meaning there, so it is a caller error, and
  // ignoring it would drop the caller's input silently. The diff kind never reads it.
  const prevBadIdx = subjects.findIndex(
    (x) => !!x && typeof x === 'object' && x.prevBlob !== undefined && (round === 1 || !PINNED_SHA.test(String(x.prevBlob)))
  )
  if (prevBadIdx !== -1)
    throw new Error('tier2-review: subject ' + prevBadIdx + "'s `prevBlob` must be an immutable 7-40 hex object id, the blob " +
      'of that path the previous round audited, and is legal at round > 1 only. Got ' +
      JSON.stringify(subjects[prevBadIdx].prevBlob) + ' at round ' + round + '.')
}
// S3 - how many subjects name their fold diff, and whether a fold round has nothing naming its fold text.
const prevBlobCount = isSpec ? subjects.filter((x) => !!x && typeof x === 'object' && x.prevBlob !== undefined).length : 0
const foldDegraded = isSpec && round > 1 && prevBlobCount === 0 && priorFindings.length === 0
if (foldDegraded)
  log('WARNING: a DEGRADED fold review: round ' + round + ' with no subject carrying prevBlob and no priorFindings, so nothing ' +
    "names the text the previous round's fixes introduced; every subject is reviewed whole")
else if (isSpec && round > 1 && prevBlobCount < subjects.length)
  log('WARNING: no prevBlob was supplied for ' + subjects.filter((x) => !x || typeof x !== 'object' || x.prevBlob === undefined)
    .map((x) => (x && typeof x === 'object' ? x.path : String(x))).join(', ') + ', so the fold diff of each is unknown and it is reviewed whole')
// TOOL-aEvidencedLens-2 S4 - `scratch`, the one place a PROBING spec lens may write. REQUIRED on the
// spec kind (spec F1: a lens briefed to probe with no scratch has nowhere legal to write, and owner
// ruling TOOL-aProbedUnit-10 makes it required on every harness agent), refused by the build harness's
// own SHAPE test (TOOL-aProbedUnit-4), plus two refusals of its own (spec F2): a control character,
// because the value reaches a prompt line and a newline would start a forged one (the `specs` rule's L1
// precedent below), and a path equal to or under `repo`, because a lens writing there writes the tree.
// That comparison folds slashes, case, a trailing slash and an MSYS `/<letter>/` to `<letter>:/`, so it
// errs toward refusing. It is TEXTUAL, so two more refusals make it answerable (TOOL-aEvidencedLens-21
// S1): on this kind `repo` must be absolute too, since `"."` cannot be compared in a runtime with no
// filesystem, and a `..` segment in either value is refused, since `/tmp/q/../r/x` resolves under
// `/tmp/r`. An 8.3 short name or a link aliasing `repo` is still not seen. The diff kind never reads
// `a.scratch`, and its `repo` stays as accepted.
const scratchRule = 'an ABSOLUTE path (a leading / or a drive letter and a separator) with no control character and no .. segment, not equal to or under `repo`'
if (isSpec && (typeof a.scratch !== 'string' || !/^(\/|[A-Za-z]:[\\/])/.test(a.scratch)))
  throw new Error('tier2-review: a spec-audit needs `scratch`, ' + scratchRule + '. Got ' + JSON.stringify(a.scratch) +
    '. Refusing to default it: a probing lens with no scratch directory has nowhere legal to write.')
if (isSpec && /[\x00-\x1f]/.test(a.scratch))
  throw new Error('tier2-review: `scratch` must be ' + scratchRule + '. Got ' + JSON.stringify(a.scratch) +
    ', which carries a control character; it reaches a prompt line, where a newline would start a forged one.')
if (isSpec && !/^(\/|[A-Za-z]:[\\/])/.test(String(repo)))
  throw new Error('tier2-review: a spec-audit needs an ABSOLUTE `repo` (a leading / or a drive letter and a separator). Got ' +
    JSON.stringify(repo) + '; `scratch` is refused when it is under `repo`, and a relative `repo` cannot be compared in a runtime with no filesystem.')
if (isSpec && /(^|[\\/])\.\.([\\/]|$)/.test(a.scratch + '\n' + String(repo)))
  throw new Error('tier2-review: `scratch` and `repo` must carry no .. segment. Got `scratch` ' + JSON.stringify(a.scratch) +
    ' beside `repo` ' + JSON.stringify(repo) + '; the under-`repo` test is textual, and a .. segment resolves where the text does not say.')
const scratchFold = isSpec ? a.scratch.replace(/\\/g, '/').toLowerCase().replace(/\/+$/, '').replace(/^\/([a-z])(?=\/|$)/, '$1:') : ''
const repoFold = String(repo).replace(/\\/g, '/').toLowerCase().replace(/\/+$/, '').replace(/^\/([a-z])(?=\/|$)/, '$1:')
if (isSpec && (scratchFold === repoFold || scratchFold.indexOf(repoFold + '/') === 0))
  throw new Error('tier2-review: `scratch` must be ' + scratchRule + '. Got ' + JSON.stringify(a.scratch) + ' beside `repo` ' +
    JSON.stringify(repo) + '; a lens writing its temporary files there writes the tree the read-only rule exists to protect.')
// Folded to forward slashes ONCE, here, as the build harness folds its own; never lowercased, so the
// prompt names the directory the caller spelled.
const scratch = isSpec ? a.scratch.replace(/\\/g, '/') : ''
// TOOL-aSightedSkeptic-3 S1/S3 - `specs`, the intent documents the caller names. Validated here,
// before the base-shape ladder and the first agent, so a bad value refuses in milliseconds. A path
// reaches a prompt as text an agent then reads, so anything that could point a reviewer outside the
// repository - absolute, home-relative (`~`), drive-lettered, backslashed or `..` - is refused rather
// than normalized, and so is a control character, which would start a forged line in the brief
// (closing review round 1, L1). The offender is an INDEX, never a value: `''` is one of the values
// refused (the D6 class above).
const SPECS = a.specs === undefined ? [] : a.specs
const specsRule = 'an array of repo-relative paths, each a non-empty string with no backslash, no leading / or ~, no drive letter, no .. segment and no control character'
if (!Array.isArray(SPECS))
  throw new Error('tier2-review: `specs` must be ' + specsRule + '. Got ' + JSON.stringify(a.specs) + ', which is not an array.')
// TOOL-dFairHearing-8 S4 - the rule as one predicate, since `legManifest` below is refused by it too.
function checkRepoPath(s) {
  return typeof s === 'string' && !!s && s.indexOf('\\') === -1 && s[0] !== '/' && s[0] !== '~' && !/[\x00-\x1f]/.test(s) &&
    !/^[A-Za-z]:/.test(s) && s.split('/').indexOf('..') === -1
}
const specsBadIdx = SPECS.findIndex((s) => !checkRepoPath(s))
if (specsBadIdx !== -1)
  throw new Error('tier2-review: `specs` must be ' + specsRule + '. Member ' + specsBadIdx + ' is ' + JSON.stringify(SPECS[specsBadIdx]) + '.')
// TOOL-dFairHearing-8 S4 - `legManifest`, the leg manifest the resume probe reads the `gate:` leg names from. It
// reaches the probe's prompt as a path an agent reads, so it is refused on the `specs` rule; the default is rendered.
const legManifest = a.legManifest === undefined ? 'tools/gate-legs.json' : a.legManifest
if (!checkRepoPath(legManifest))
  throw new Error('tier2-review: `legManifest` must be a repo-relative path, a non-empty string with no backslash, no leading / or ~, ' +
    'no drive letter, no .. segment and no control character. Got ' + JSON.stringify(a.legManifest) + '.')
// S3 - on a spec audit `specs` is sibling context, NOT under audit, so one document cannot be both.
const specsOverlap = isSpec ? SPECS.find((p) => subjects.some((x) => x && x.path === p)) : undefined
if (specsOverlap !== undefined)
  throw new Error('tier2-review: `specs` names ' + JSON.stringify(specsOverlap) + ', which is also a subject of this spec audit; a document cannot be both under audit and sibling context to it.')
// TOOL-aSightedSkeptic-4 S1 - `checklist`, the project's recurring bug classes. A caller's value wins;
// on a diff review with none the harness acquires `gotchas.py --for-diff` stdout itself (TOOL-dFairHearing-15,
// at the split below). Parsed after every other refusal and before the first agent a caller's value leaves
// to spawn, so a bad value refuses in milliseconds. A non-blank
// string with no `- ` item line REFUSES rather than becoming one item: one item lands on one lens,
// which is the whole-checklist-on-one-agent defect this argument exists to remove (spec F2).
function parseChecklist(v) {
  // Closing review round 1, L5 - the text says what the loop below does: ANY later line not starting
  // "- " continues the item above it, indented or not (spec S1, and the kit README).
  const rule = 'a string whose items are lines starting "- " (lines before the first item are a preamble; ' +
    'every later line not starting "- " continues the item above it, indented or not) or an array of non-empty strings'
  if (v === undefined) return { preamble: '', items: [] }
  if (typeof v === 'string') {
    const pre = []
    const items = []
    for (const raw of v.replace(/\r\n/g, '\n').split('\n')) {
      const line = raw.replace(/\s+$/, '')
      if (!line) continue
      if (line.indexOf('- ') === 0) items.push(line.slice(2))
      else if (items.length) items[items.length - 1] += '\n' + line
      else pre.push(line)
    }
    // A remainder of `# ` header lines alone is ZERO items, not prose (TOOL-aGraftedHelix-3 S8): it is
    // what the checker prints when it selects no class, once its by-design block is cut out, and it
    // is announced below as supplied with no item. Prose with no item still refuses.
    if (!items.length && pre.some((l) => l.indexOf('# ') !== 0))
      throw new Error('tier2-review: `checklist` must be ' + rule + '. Got a string with no line starting "- ": ' +
        JSON.stringify(v.slice(0, 80)) + '. Pass the items as an array instead.')
    return { preamble: pre.join('\n'), items: items }
  }
  if (!Array.isArray(v))
    throw new Error('tier2-review: `checklist` must be ' + rule + '. Got ' + JSON.stringify(v) + '.')
  const bad = v.findIndex((x) => typeof x !== 'string' || !x.trim())
  if (bad !== -1)
    throw new Error('tier2-review: `checklist` must be ' + rule + '. Member ' + bad + ' is ' + JSON.stringify(v[bad]) + '.')
  return { preamble: '', items: v.slice() }
}
// TOOL-aGraftedHelix-3 S8 - the BY-DESIGN BLOCK (I4) the checker prints after its items: the head
// `# by design — <n> invariant(s) this selection touches`, then one `- ` line per invariant the
// selection touches, blank lines skipped, ending at the first other line. CUT OUT before the items are
// parsed, because `parseChecklist` would sweep every entry as a bug class and every lens would hunt
// intended behaviour. A head whose count disagrees with its entries REFUSES before any agent spawns:
// a truncated block hands the lenses a partial list that reads as a whole one. String form only.
const BY_DESIGN_HEAD = /^# by design — (\d+) invariant\(s\) this selection touches$/
function extractByDesign(v) {
  if (typeof v !== 'string') return { remainder: v, entries: null }
  const lines = v.replace(/\r\n/g, '\n').split('\n')
  const at = lines.findIndex((l) => BY_DESIGN_HEAD.test(l.replace(/\s+$/, '')))
  if (at === -1) return { remainder: v, entries: null }
  const claimed = Number(BY_DESIGN_HEAD.exec(lines[at].replace(/\s+$/, ''))[1])
  const entries = []
  let end = at + 1
  for (; end < lines.length; end++) {
    const line = lines[end].replace(/\s+$/, '')
    if (!line) continue
    if (line.indexOf('- ') !== 0) break
    entries.push(line.slice(2))
  }
  if (entries.length !== claimed)
    throw new Error('tier2-review: the checklist\'s by-design block claims ' + claimed + ' invariant(s) and carries ' +
      entries.length + ' entry line(s). A truncated block would hand every lens a partial by-design list that reads ' +
      'as a whole one; pass the checker\'s stdout whole.')
  return { remainder: lines.slice(0, at).concat(lines.slice(end)).join('\n'), entries: entries }
}
const baseLooksPinned = isSpec || PINNED_SHA.test(String(base))
if (!baseLooksPinned) {
  const why =
    'tier2-review: `base` must be an immutable sha (7-40 hex), not a moving ref. Got ' +
    JSON.stringify(base) +
    '. M8 forbids a moving ref two paragraphs above the invocation it documents: a ref records ' +
    'provenance that points at whatever that branch happened to be. Resolve it: git rev-parse <ref>.'
  if (round > 1) throw new Error(why)
  log('WARNING: ' + why)
}
// `diffCmd` is built AFTER the resume probe now, from the shas it resolves (TOOL-dDerivedDocket-29 S3).
// H2/AC5, HONEST LIMIT: the harness CANNOT verify its own root. Workflow scripts have no
// filesystem and no Node/Bun API, so there is no way to prove `repo` resolves to a git worktree
// from in here — a probe was written, then removed rather than shipped unverified. What it can do
// is make the given root impossible to miss: logged before any agent spawns, injected into the
// synth prompt, and returned on every exit path. Verifying it belongs to the CALLER.
log(`review root (unverified — see note): ${repo} — ${kind} — ` +
  (isSpec ? `${subjects.length} subject(s)` : `diff ${base}...${head}`))

// TOOL-dTieredTribunal-11 S3 - two SIBLING schemas, not one loosened schema. A spec finding is often
// the ABSENCE of a line, so it addresses a section; making `line` merely optional on a shared schema
// would buy the spec kind an address by removing the diff kind's, and the charter requires a finder
// to emit a concrete address on both.
// TOOL-dDerivedDocket-29 S1 - `path` is REQUIRED on all three agent schemas: the file the agent wrote
// its result to before returning. A required field is what makes an agent that skipped the write fail
// validation loudly instead of returning cleanly with nothing on disk behind it. `key` is carried by
// the FILE and optional on the return.
const FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'path', 'findings'],
  properties: {
    lens: { type: 'string' },
    path: { type: 'string' },
    key: { type: 'string' },
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
// TOOL-aSightedSkeptic-2 S1 - the skeptic also judges the finding's proposed FIX, as a second and
// separate question. Both fields stay OPTIONAL: a skeptic that omits them degrades to "unjudged" and
// never fails its batch into regeneration, and `id` stays the only join key. The harness tests
// membership in FIX_VERDICTS again after the join, because a reused file and a stub reach it without
// the platform's schema validation.
// TOOL-aSightedSkeptic-6 S3 - `uncertain` is a third verdict, and the skeptic's `severity` is OPTIONAL
// and read on a confirmed verdict only. The harness tests membership in SEVERITIES itself, for the
// same reason it tests FIX_VERDICTS.
// TOOL-dFairHearing-8 S2 - `instance`, the fix that cures the cited instance and leaves another of its class
// standing, is a verdict under `fixJudge: 'class'` alone: outside this set it reads as unjudged at every reader.
const FIX_VERDICTS = ['sound', 'unsound', 'none'].concat(fixJudge === 'class' ? ['instance'] : [])
const SEVERITIES = ['blocker', 'high', 'medium', 'low']
const VERDICT_SCHEMA = {
  type: 'object',
  required: ['path', 'verdicts'],
  properties: {
    path: { type: 'string' },
    key: { type: 'string' },
    batch: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'verdict', 'reason'],
        properties: {
          id: { type: 'integer' }, // the orchestrator-assigned finding id, echoed back
          verdict: { type: 'string', enum: ['confirmed', 'refuted', 'uncertain'] },
          reason: { type: 'string' },
          fixVerdict: { type: 'string', enum: FIX_VERDICTS },
          fixNote: { type: 'string' },
          severity: { type: 'string', enum: SEVERITIES },
        },
      },
    },
  },
}
// TOOL-dFairHearing-18 S6 - a whole-design skeptic's schema: VERDICT_SCHEMA plus an OPTIONAL `cells`, one verdict per
// clean cell handed, used on this preset alone. A refuted cell carries the skeptic's address and grade.
const WALK_VERDICT_SCHEMA = {
  type: 'object',
  required: VERDICT_SCHEMA.required,
  properties: Object.assign({}, VERDICT_SCHEMA.properties, {
    cells: {
      type: 'array',
      items: {
        type: 'object',
        required: ['cell', 'verdict', 'reason'],
        properties: {
          cell: { type: 'string' },
          verdict: { type: 'string', enum: ['holds', 'refuted'] },
          reason: { type: 'string' },
          file: { type: 'string' },
          where: { type: 'string' },
          severity: { type: 'string', enum: SEVERITIES },
        },
      },
    },
  }),
}

// TOOL-aSightedSkeptic-6 S1/S2 - ONE severity rubric, graded by CONSEQUENCE. Severity drives the
// costliest disposal there is (a BLOCKER or HIGH is promoted to a unit, TOOL-aProbedUnit-9), and no
// prompt defined a grade. It is interpolated byte-identically into every finder, verify and synthesis
// prompt of the run and restated nowhere; the spec kind reads each grade as what the design would do.
const SEVERITY_RUBRIC =
  `SEVERITY RUBRIC - grade every finding by its CONSEQUENCE. ` +
  `blocker: ${isSpec ? 'the design, built as written, would ship' : 'on a reachable path it ships'} a wrong result, a security hole or data loss, or a check that certifies what it does not check. ` +
  `high: ${isSpec ? 'the design, built as written, would cause ' : ''}the same consequence on a narrow or unlikely path, or a defect that will mislead the next change. ` +
  `medium: ${isSpec ? 'the design, built as written, would ship ' : ''}a real defect whose effect is contained. ` +
  `low: ${isSpec ? 'the design, built as written, would differ only cosmetically or in a comment' : 'cosmetic, or a comment'}, with no effect on behaviour. ` +
  `A grade follows the consequence, never the confidence or how alarming the defect looks.`

// TOOL-aEvidencedLens-2 S2 - the PROBE POLICY, spec-kind data. A spec lens may now establish a claim
// from anywhere in the tree, read-only: about two in five of the defects that got past the audit needed
// a command run, a consumer grepped or a goal timed (measured 2026-10-05, session study). The rules
// interpolate NOTHING, so they join the input print; the block's header line carries `scratch`, which
// changes every session and therefore does not (a resumed run must reuse its lens files). The one write
// the READ-ONLY rule excepts is the DURABILITY file the same prompt demands two lines later.
const PROBE_RULES = [
  'Establish every claim with a read-only command, and record the command and what it printed.',
  'Run each section-6 criterion\'s own command or check when it is read-only and bounded, and record what it printed: a criterion already green before the unit is built cannot fail.',
  'Grep the consumers of every name, value or path the spec renames, retires or changes.',
  'Time a stated wall-clock goal once, when one run of it is bounded.',
  'READ-ONLY: write nothing under the repository, with ONE exception, the DURABILITY file this prompt names. Never run a command that writes the tree or the index: no --write, --render, --fix or --in-place, no git add, commit, checkout, switch, reset, restore, stash, merge, rebase, clone or worktree, and no redirect into the repository. Read another revision with git show <rev>:<path>.',
  'Every temporary file goes under the scratch directory named above, spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp or a bare mktemp.',
  // TOOL-aEvidencedLens-21 S5 (replay id 37): every probing agent shares that one directory, so two lenses
  // writing a same-named probe file overwrote each other. Constant text, so the print and the two slices hold.
  'Write temporary files only under a subdirectory of the scratch directory named for your own role, <lens key> for a finder or verify-<batch> for a skeptic, created on first use.',
  'Bound every command at 120 seconds. Never run a merge bar, a *.test.sh suite or a self-test runner, a --selftest flag included.',
  'A probe that needs a write, such as a staged break, or one of the runs banned above, is DESCRIBED in the finding\'s fix as the probe the build must run. It is never performed.',
]
// TOOL-dFairHearing-18 S3 - THE WALK RULES, what every whole-design walker is told, held once and interpolated
// into each walker prompt above that walker's own slice. They interpolate nothing, so they join the input print
// on a whole-design run alone; the slice, the scenarios and the seed line are rendered per walker.
const WALK_RULES = [
  'Walk ONLY the cells listed under CELLS below: each is one item read through one scenario, whose line under SCENARIOS says what it walks.',
  'Open with a PRE-MORTEM: the design shipped and failed inside your slice. Write down why, then walk the cells to find out whether it would.',
  'Read each item a failure reaches for its failure mode, its effect and how the failure is detected, and each data flow crossing a trust boundary for its threats.',
  'For EACH cell return one walk row: the actor, the needs, the witness and the route the scenario finds there, each `=` where it reads as the design declares it and NEVER empty, and the verdict: holds; finding, with `findings` listing the zero-based indexes of the findings in your own findings array that the cell raised; or not-on-path, with a reason saying why the scenario never reaches the item.',
  'Address each finding by `file` and a `where` naming the [section tag] it sits under, with the clause id or the item tag that carries it.',
  'A cell with no row or two, a row for a cell outside your slice, an empty field, or a verdict outside the three is a GAP, and the harness reds the run on any gap.',
]
// Built once, after `scratch` is validated; '' on the diff kind, whose prompts stay byte-identical.
const probeBlock = isSpec
  ? `PROBE POLICY — repository ${repo}, scratch directory ${scratch}.\n- ` + PROBE_RULES.join('\n- ') + `\n`
  : ''

// S3 - the spec kind's schema. `where` replaces `line` and is REQUIRED, so the address obligation is
// machine-enforced on both kinds rather than relaxed on one.
const SPEC_FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'path', 'findings'],
  properties: {
    lens: { type: 'string' },
    path: { type: 'string' },
    key: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        // TOOL-aEvidencedLens-2 S3 - `evidence` is REQUIRED: what a skeptic re-runs to check the claim.
        required: ['file', 'where', 'severity', 'claim', 'impact', 'fix', 'evidence'],
        properties: {
          file: { type: 'string' },
          where: { type: 'string' },
          severity: { type: 'string', enum: ['blocker', 'high', 'medium', 'low'] },
          claim: { type: 'string' },
          impact: { type: 'string' },
          fix: { type: 'string' },
          evidence: { type: 'string' },
        },
      },
    },
  },
}
// TOOL-dFairHearing-18 S4 - a whole-design walker's schema: the spec kind's plus a REQUIRED `walk`, one row per cell.
// `findings` holds zero-based indexes into the walker's own findings; the harness maps each to its assigned id.
// Every other preset keeps SPEC_FINDING_SCHEMA itself, and LENS_SCHEMA is the one each finder and the probe read.
const WALK_FINDING_SCHEMA = {
  type: 'object',
  required: SPEC_FINDING_SCHEMA.required.concat(['walk']),
  properties: Object.assign({}, SPEC_FINDING_SCHEMA.properties, {
    walk: {
      type: 'array',
      items: {
        type: 'object',
        required: ['item', 'scenario', 'actor', 'needs', 'witness', 'route', 'verdict', 'findings'],
        properties: {
          item: { type: 'string' },
          scenario: { type: 'string' },
          actor: { type: 'string' },
          needs: { type: 'string' },
          witness: { type: 'string' },
          route: { type: 'string' },
          verdict: { type: 'string', enum: WALK_VERDICTS },
          findings: { type: 'array', items: { type: 'integer' } },
          reason: { type: 'string' },
        },
      },
    },
  }),
}
const LENS_SCHEMA = !isSpec ? FINDING_SCHEMA : isWalk ? WALK_FINDING_SCHEMA : SPEC_FINDING_SCHEMA

// --- Phase 1: FIND — one wave of primed lenses, at the width boundedParallel defaults to ----
// TOOL-dTieredTribunal-11 S11: this said `ONE <=6-wide wave` while the helper above defaults to
// the file constant and the meta line said <=5 concurrent. Three carriers, two numbers, and the
// code fanned at neither six nor a spelled digit. No digit is written here now: the width is
// whatever `boundedParallel`'s default parameter resolves to, which is the one place that owns
// it. Closes TOOL-aDeclaredBound-6, whose own row cites the wrong line for this text.
// The `phase('Find')` call moved below the resume probe (TOOL-dDerivedDocket-29 S3).
// TOOL-aSightedSkeptic-5 - FIVE lenses, the owner's set. `regressions` is retired: it was told to run
// "the PROJECT's checklist" and was handed none, and its sweep is now split over these five through
// `args.checklist`. `verification` hunts the defect this repo finds most, a check that cannot fail,
// which no brief named. No brief names a web surface. Five is the most the verifier fan-out leg's
// check-verifier-fanout.js admits on an array-literal receiver, so a sixth lens reds the merge bar
// rather than being chosen against.
// TOOL-dFairHearing-13 - the catalogue, this kit's `lenses.toml`, is the source of every lens, and
// each lens literal here is its RENDER: render_lenses.py fills the slot token under a literal's
// lens-slots marker with the rows whose `default_in` names it, at install and in the parity leg,
// because this script has no filesystem to read the catalogue from. A lens is added or swapped as a
// row there, never by an edit here. The fan-out leg holds every marked literal to exactly five slots.
// TOOL-dFairHearing-3 S2 - THE SWAP. Every default slot renders as `deriveSlotLens('<literal>', {...})`,
// which, when the slot belongs to the run's literal, records its default key and returns the shipped
// opt-in row `optIn` maps to that default, carrying `replaces`, and the slot unchanged otherwise. So the
// literal keeps five elements after every swap, and every reader keyed on `L.key` names the lens that
// ran. OPTIN_LENSES is the render of the catalogue's `optin = true` rows; nothing fans over it. Declared
// above the literals, because each slot calls in here when its literal is evaluated.
const OPTIN_LENSES = [ // gov:lens-optins
]
const SLOT_LITERAL = isSpec ? preset : 'diff-review'
const SLOT_DEFAULTS = [] // the run literal's default keys, in slot order
function deriveSlotLens(literal, L) {
  if (literal !== SLOT_LITERAL) return L
  SLOT_DEFAULTS.push(L.key)
  const k = Object.keys(optIn).find((x) => optIn[x] === L.key)
  const row = k && OPTIN_LENSES.find((r) => r.key === k && r.presets.indexOf(literal) !== -1)
  return row ? { key: row.key, brief: row.brief, replaces: L.key } : L
}
const DIFF_LENSES = [ // gov:lens-slots diff-review
  deriveSlotLens('diff-review', {
    key: 'security',
    brief:
      'Security: trust boundaries for THIS kind of code. Commands built from interpolated input (shell, SQL, regex, paths), path traversal and symlinks, secrets reaching logs or output, authorization or enforcement that can be bypassed, and output from another program or agent trusted without validation.',
  }),
  deriveSlotLens('diff-review', {
    key: 'correctness',
    brief:
      'Correctness: logic bugs, wrong conditionals and edge cases, off-by-one, type and encoding coercion drift, error and empty-input paths, and two copies of one rule that disagree.',
  }),
  deriveSlotLens('diff-review', {
    key: 'seams',
    brief:
      'Integration seams + dead plumbing: values computed→passed→never read, stale caches not reset on every mutation path, indexes that don\'t serve their query, half-applied merges, cross-language catalog drift.',
  }),
  deriveSlotLens('diff-review', {
    key: 'verification',
    brief:
      'Verification: does every behaviour this diff changes have a check that can FAIL? Report a test or gate whose fixture never triggers the rule, a predicate that matches nothing, a skip that reads as a pass, and a changed behaviour with no check at all.',
  }),
  deriveSlotLens('diff-review', {
    key: 'intent',
    brief:
      'Intent: does the diff do what its stated intent says? Read the range\'s commit messages and any spec or design document the diff touches or those messages name, then report an acceptance criterion with no code behind it, a stated mechanism that is not the one built, and scope beyond what was asked.',
  }),
]
// TOOL-aSightedSkeptic-7 S3 - a LIGHT diff review's lenses, as KEYS (spec F1: 70 of the 76 classed
// findings in the owner's sample). Not a third lens set: the skip happens inside the Find thunk, so
// the receiver the verifier fan-out leg sizes keeps its shape.
const LIGHT_LENSES = ['correctness', 'seams', 'verification']

// TOOL-aEvidencedLens-1 - this array holds the M4 spec-audit lenses. The method and the memory-tree
// README point here rather than list lens names, so there is no second copy to drift. Since
// TOOL-dFairHearing-13 its source is the `unit-spec` rows of this kit's `lenses.toml`, and this
// literal is their render. Five lenses aimed at the measured escape classes; `coherence` keeps the
// first slot so a fixture keyed on the first lens keeps its ids.
const SPEC_LENSES = [ // gov:lens-slots unit-spec
  deriveSlotLens('unit-spec', {
    key: 'coherence',
    brief:
      'Coherence: does the spec set agree with itself, and can its acceptance decide anything? Report a section-2 item no section-6 criterion observes; a criterion whose observation cannot FAIL on today\'s tree, because it is already green before the unit is built; a criterion that cannot PASS on a correct build, because it demands what the design does not produce or a figure the build cannot reach; section 2 against section 3; section 4 Design against section 7 Gates; and, across the subjects and the sibling context, the four axes scope, interface, ordering and acceptance: a name, path or key spelled two ways, a unit depending on one ordered after it, two units claiming one file or one landing slot, and an overview acceptance no unit\'s criteria imply.',
  }),
  deriveSlotLens('unit-spec', {
    key: 'grounding',
    brief:
      'Grounding: is every claim sections 4 and 10 make about the world TRUE where the subjects stand? Check each claim about existing code, a tool\'s flags or output, a record, a count, a platform behaviour or a cost against the source, never against the spec. Hunt the traps this platform sets: MSYS argument and path rewriting, drive-letter and backslash paths, CRLF in a working copy and a text-mode read that drops a CR, and a stated wall-clock goal nobody timed. A claim marked UNVERIFIED is a finding only where the design rests on it.',
  }),
  deriveSlotLens('unit-spec', {
    key: 'reuse',
    brief:
      'Reuse: functionality is reused and extended, never rebuilt. Report a design that builds what already exists, such as a function, a checker, a gate leg, a driver verb or a record shape, instead of extending it; a section-10 seam that is cited but is not the one section 4 extends, or that does not exist; and a question a decision record or an ask already decided, decided asks included. Probe before you claim: the codebase-map kit\'s reuse_lookup.py with a behaviour phrase, the memory-recall kit\'s query.py with a plain-English question and 8-14 --terms in this corpus\'s own jargon, and grep, because the lookup cannot see every layer and prints the ones it skipped. Locate each tool with git ls-files; where one is absent, say so in the finding and use grep. Read the asks through the memory-tree kit\'s gen_build_index.py --asks --json --all --path <every path the spec\'s Files touched estimate names>, falling back to the backlog shards when its mode field says shards. THE BAR: a reuse finding names the existing seam or record by path or id AND quotes the spec text that duplicates or contradicts it. That a related record exists is not a finding.',
  }),
  deriveSlotLens('unit-spec', {
    key: 'blast-radius',
    brief:
      'Blast radius: what does this change trip that the spec does not list? For every name, value or rule the spec renames, retires or changes, grep the name AND the value, and report each consumer, carrier, test arm or document the spec does not name. Join section 4\'s files-touched list against the gate-leg manifest (gate-legs.json, where the project keeps one) and report a guarded leg section 7 omits; report a declared size or time budget the change will cross; and report the repo\'s own machinery the spec forgets: version carriers, codebase-map keys, record and filename rules, a --dispatch write set, and a render an adopter regenerates.',
  }),
  deriveSlotLens('unit-spec', {
    key: 'failure-envelope',
    brief:
      'Failure envelope: what will the built thing meet that the spec never says it handles? Report the input classes the design is silent on (empty, malformed, multi-line, unterminated, huge, concurrent), signals, partial failure and a dead dependency; a security or write surface section 5 did not price; and a spec that names one INSTANCE where the class was meant, such as one file of two or one caller of three. A spec is built as a ceiling: in this kit\'s own trial (aBlindedTrial, report section 4.3), when a spec named the class for one input file and not the other, the builder handled exactly the file it named.',
  }),
]

// TOOL-dFairHearing-2 S2/S3 - the `design-audit` preset's lenses, for a design or architecture record,
// whose sections are not a unit spec's: the `design-audit` rows of `lenses.toml`, `coherence`,
// `grounding`, `reuse` and `failure-envelope` in design briefs of their own, and `alternatives-and-cost`
// in the slot `blast-radius` holds above. `PRESETS` in the argument checks names it.
const DESIGN_LENSES = [ // gov:lens-slots design-audit
  deriveSlotLens('design-audit', {
    key: 'coherence',
    brief:
      'Coherence: does the design record agree with itself and with the records it cites? Report a stated goal, requirement or invariant no mechanism in the record delivers; one rule, name, path, key or number stated two ways; a step that depends on one ordered after it; two mechanisms claiming one file, one owner or one landing slot; and, across the subjects and the sibling context, a decision one record takes that another contradicts.',
  }),
  deriveSlotLens('design-audit', {
    key: 'grounding',
    brief:
      'Grounding: is every claim the design makes about the world TRUE where the subjects stand? Check each claim about existing code, a tool\'s flags or output, a record, a count, a platform behaviour or a cost against the source, never against the design. Flag every load-bearing claim that rests on a docs line or a single observation as an untested assumption, name the observation that would overturn it, and probe it where the probe rules allow. Hunt the traps this platform sets: MSYS argument and path rewriting, drive-letter and backslash paths, CRLF in a working copy and a text-mode read that drops a CR, and a stated wall-clock goal nobody timed.',
  }),
  deriveSlotLens('design-audit', {
    key: 'reuse',
    brief:
      'Reuse and precedent: functionality is reused and extended, never rebuilt, and every choice keeps faith with what was decided. Report a mechanism that rebuilds an existing function, checker, gate leg, driver verb or record shape; and a choice that re-opens a decision row, an owner ruling or a decided ask, or drops a condition a ruling rested on, naming the id and quoting both texts. Probe before you claim: the codebase-map kit\'s reuse_lookup.py with a behaviour phrase, the memory-recall kit\'s query.py with a plain-English question and 8-14 --terms in this corpus\'s own jargon, and grep. THE BAR: a finding names the existing seam, record or ruling by path or id AND quotes the design text that duplicates or contradicts it.',
  }),
  deriveSlotLens('design-audit', {
    key: 'failure-envelope',
    brief:
      'Failure envelope and trust boundaries: what will the built system meet that the design never says it handles? Report the input classes it is silent on (empty, malformed, multi-line, unterminated, huge, concurrent), signals, partial failure and a dead dependency; every trust boundary the design creates or relies on, an enforcement a rule, a setting, a second path or a dead dependency bypasses, input trusted without validation, and a guarded action left allowed on failure; and a design that names one instance where the class was meant.',
  }),
  deriveSlotLens('design-audit', {
    key: 'alternatives-and-cost',
    brief:
      'Alternatives and cost: is there a materially simpler or cheaper mechanism meeting the same contract, and what does this one cost? Report an existing seam, a checker in place of an agent, or one process in place of many that meets the same requirement or invariant, saying which; and every agent, session, spawn, token and wall-clock cost the design adds that carries no ceiling, no enforcer, or a ceiling nobody measured.',
  }),
]

// TOOL-dFairHearing-18 S3 - the `whole-design` preset's five walkers, `walk-1` to `walk-5`, the `whole-design` rows
// of `lenses.toml`, each brief naming its slot alone (spec section 8 F2); what every walker is told is WALK_RULES.
// A slot's position here is its walker slot, the position deriveWalkSlices deals cells to.
const WHOLE_DESIGN_LENSES = [ // gov:lens-slots whole-design
  deriveSlotLens('whole-design', {
    key: 'walk-1',
    brief:
      'Walker slot 1 of 5 of the whole-design walk: walk the cells of your slice under the WALK RULES below.',
  }),
  deriveSlotLens('whole-design', {
    key: 'walk-2',
    brief:
      'Walker slot 2 of 5 of the whole-design walk: walk the cells of your slice under the WALK RULES below.',
  }),
  deriveSlotLens('whole-design', {
    key: 'walk-3',
    brief:
      'Walker slot 3 of 5 of the whole-design walk: walk the cells of your slice under the WALK RULES below.',
  }),
  deriveSlotLens('whole-design', {
    key: 'walk-4',
    brief:
      'Walker slot 4 of 5 of the whole-design walk: walk the cells of your slice under the WALK RULES below.',
  }),
  deriveSlotLens('whole-design', {
    key: 'walk-5',
    brief:
      'Walker slot 5 of 5 of the whole-design walk: walk the cells of your slice under the WALK RULES below.',
  }),
]

// The ONE dialect <prefix>/workflows/check-verifier-fanout.js admits here: sibling top-level array
// literals and a marked ternary. A map, object or registry of lens sets reds the fan-out leg, so this shape
// is fixed by the enforcement point rather than chosen. TOOL-dTieredTribunal-13 tightened the branch
// this line sits on to require EVERY value branch bounded, and all four branches here are literals,
// the spec kind's three picked by `preset` (TOOL-dFairHearing-2, -18). All are rendered from the lens catalogue
// (TOOL-dFairHearing-13), and a render keeps this shape: the rows fill each literal's body, never its
// name or this receiver.
const LENSES = !isSpec ? DIFF_LENSES : preset === 'design-audit' ? DESIGN_LENSES : preset === 'whole-design' ? WHOLE_DESIGN_LENSES : SPEC_LENSES // gov:fixed-verifiers
// S3 - checked on EVERY run of either kind, before the resume probe: a renamed lens would otherwise
// empty the light set, and a light run would review nothing while reporting clean. An INDEX names the
// offender, since `''` is itself a key this refuses (the D6 class).
// TOOL-dFairHearing-3 S4 - against the diff literal's DEFAULT keys, so a swap that put an opt-in in a
// light slot never reds this check.
const lightBadIdx = LIGHT_LENSES.findIndex((k) => !DIFF_LENSES.some((L) => (L.replaces || L.key) === k))
if (!LIGHT_LENSES.length)
  throw new Error('tier2-review: LIGHT_LENSES is empty, so a light run would review nothing while reporting clean.')
if (lightBadIdx !== -1)
  throw new Error('tier2-review: LIGHT_LENSES names ' + JSON.stringify(LIGHT_LENSES[lightBadIdx]) + ', which DIFF_LENSES does not carry as a default.')

// TOOL-aSightedSkeptic-5 S4/S6 - `lensNotes`, a project addendum per lens. It is validated HERE,
// against the CURRENT kind's keys and before the resume probe, the first agent, so a typo'd key
// refuses in milliseconds instead of reviewing on the generic brief while looking customised. Absent
// defaults to {} and is ANNOUNCED, in the log now and in the synthesis's RUN INTEGRITY block, because
// a silent default is how a degraded run reads as a full one.
// The offence is carried by a FLAG, never by a sentinel value: `null` is itself one of the values
// refused here, so `got === null` could not tell "nothing wrong" from "handed null" (the D6 class).
const LENS_KEYS = LENSES.map((L) => L.key)
// TOOL-dFairHearing-9 S2 - the PER-PRESET form: an object whose every key is a literal name maps each
// to a flat note map, and the run reads only its own literal's entry, `runNotes`, absent meaning {}.
// Only that entry is checked; another preset's is checked when that preset runs. No lens key equals a
// literal name (TOOL-dFairHearing-13's catalogue rule), so a key tells the forms apart, and an object
// mixing them is refused naming both. Any other value is the flat form, checked as before.
const LITERAL_NAMES = ['diff-review'].concat(PRESETS)
const lensNotes = a.lensNotes === undefined ? {} : a.lensNotes
const lensNotesKeys = lensNotes && typeof lensNotes === 'object' && !Array.isArray(lensNotes) ? Object.keys(lensNotes) : []
const literalNoteKeys = lensNotesKeys.filter((k) => LITERAL_NAMES.indexOf(k) !== -1)
if (literalNoteKeys.length && literalNoteKeys.length !== lensNotesKeys.length)
  throw new Error('tier2-review: `lensNotes` mixes the per-preset form, keyed by literal name (' + LITERAL_NAMES.join(' | ') +
    '), with the flat form, keyed by lens; pass one form. Got ' + JSON.stringify(lensNotes) + '.')
const perPreset = literalNoteKeys.length > 0
const runNotes = !perPreset ? lensNotes : lensNotes[SLOT_LITERAL] === undefined ? {} : lensNotes[SLOT_LITERAL]
// TOOL-dFairHearing-9 S3 - the legal keys are the run literal's DEFAULT keys plus the opt-ins swapped
// in, so a note keyed to a default a swap displaced is accepted here and reported unread below.
const LEGAL_NOTE_KEYS = SLOT_DEFAULTS.concat(LENS_KEYS.filter((k) => SLOT_DEFAULTS.indexOf(k) === -1))
let lensNotesBad = false
let lensNotesGot = perPreset ? runNotes : a.lensNotes
if (!runNotes || typeof runNotes !== 'object' || Array.isArray(runNotes)) lensNotesBad = true
else
  for (const k of Object.keys(runNotes)) {
    if (LEGAL_NOTE_KEYS.indexOf(k) !== -1 && typeof runNotes[k] === 'string' && runNotes[k]) continue
    lensNotesBad = true
    lensNotesGot = LEGAL_NOTE_KEYS.indexOf(k) === -1 ? k : { [k]: runNotes[k] }
    break
  }
if (lensNotesBad) {
  throw new Error(
    'tier2-review: `lensNotes`' + (perPreset ? ' entry `' + SLOT_LITERAL + '`' : '') + ' must be an object mapping a ' + kind + ' lens key to a non-empty string; ' +
      'legal keys: ' + LEGAL_NOTE_KEYS.join(' | ') + '. Got ' + JSON.stringify(lensNotesGot) + '.',
  )
}
// TOOL-dFairHearing-3 S3 - `optIn`'s MEMBERSHIP, checked once, here, against what evaluating the literals
// recorded: SLOT_DEFAULTS, the run literal's default keys, and OPTIN_LENSES, the shipped opt-in rows.
// Nothing it reads is an agent's output, so it still refuses before the first spawn. One rule at a
// time, in this order, so the refusal names the first rule broken.
const optInKeys = Object.keys(optIn)
const buildOptInError = (why) => new Error('tier2-review: `optIn` ' + why + '. Got ' + JSON.stringify(optIn) + '.')
for (const k of optInKeys)
  if (SLOT_DEFAULTS.indexOf(k) !== -1) throw buildOptInError('names ' + k + ', which is already a lens of `' + SLOT_LITERAL + '`; an opt-in takes a default\'s slot and never doubles one')
const offeredOptIns = OPTIN_LENSES.filter((r) => r.presets.indexOf(SLOT_LITERAL) !== -1).map((r) => r.key)
for (const k of optInKeys)
  if (offeredOptIns.indexOf(k) === -1)
    throw buildOptInError('names ' + k + ', and no shipped row offers it: there is no opt-in of `' + SLOT_LITERAL + '` by that key (shipped: ' + (offeredOptIns.join(' | ') || 'none') + ')')
for (const k of optInKeys)
  if (SLOT_DEFAULTS.indexOf(optIn[k]) === -1)
    throw buildOptInError('swaps ' + k + ' for ' + optIn[k] + ', and `' + SLOT_LITERAL + '` has no default `' + optIn[k] + '` (its defaults: ' + SLOT_DEFAULTS.join(' | ') + ')')
const twiceKey = optInKeys.find((k, i) => optInKeys.findIndex((x) => optIn[x] === optIn[k]) !== i)
if (twiceKey !== undefined) throw buildOptInError('has `' + optIn[twiceKey] + '` replaced twice; a default slot takes one opt-in')
// S5 - each swap ANNOUNCED before the first agent, naming the default whose coverage this run drops.
const swappedLenses = LENSES.filter((L) => L.replaces)
for (const L of swappedLenses)
  log(`optIn: ${L.key} runs in the slot of ${L.replaces} — this run drops the ${L.replaces} lens's coverage`)
// TOOL-dFairHearing-2 S5 - a spec audit off the default preset says so before the first agent.
if (preset !== 'unit-spec')
  log(`preset ${preset} — this spec audit runs the ${preset} lenses, not the unit-spec ones: ${LENS_KEYS.join(', ')}`)
// TOOL-dFairHearing-11 S5 - WHICH RUNS TWIN. A design-record audit is a spec audit whose subjects are all design
// subjects by SPEC_SUBJECT_PATH, or whose preset is off `unit-spec`; every diff review is a landing review, the
// closing review over the cumulative diff (spec section 8 F5).
const designRecordAudit = isSpec && (preset !== 'unit-spec' || subjects.every((x) => !SPEC_SUBJECT_PATH.test(String(x && x.path))))
// TOOL-dFairHearing-18 - a whole-design run is never twinned: its second reading is `walk.runs`, one invocation per run,
// each walking the grid its own way, and a twin's run b would walk the same slices again.
const twinned = !isWalk && (twin === 'always' || (twin === 'design-records' && designRecordAudit) || (twin === 'design-and-landing' && (designRecordAudit || !isSpec)))
if (isWalk && twin !== 'never')
  log(`twin ${twin} — a whole-design run is not twinned: its runs are walk.runs, one invocation each, so the finder lenses run once`)
if (twinned)
  log(`twin ${twin} — this ${kind} runs its finder lenses twice, as run a and run b, and the synthesis merges the two runs`)
if (fixJudge === 'class')
  log('fixJudge class — every skeptic judges each fix by the defect\'s class, and a fix curing the cited instance alone is judged instance')
const notedLenses = Object.keys(runNotes)
if (!notedLenses.length)
  log('WARNING: no `lensNotes` supplied — every lens runs on the kit\'s generic brief, with no project addendum')
// TOOL-aSightedSkeptic-3 S4 - a run told nothing about what its subject is FOR is announced, on both
// kinds: here before the first agent, and in the synthesis's RUN INTEGRITY block on every run.
const intentAbsent = !a.context && !SPECS.length
if (intentAbsent)
  log('WARNING: neither `specs` nor `context` was supplied — the lenses were told nothing about what this ' +
    (isSpec ? 'spec set' : 'change') + ' is for' + (isSpec ? '' : ', beyond the range\'s commit messages') +
    '; pass the intent documents as `specs` or describe the change in `context`')
// TOOL-aSightedSkeptic-7 S4/S6 - the lenses a light run SKIPS, in LENSES order; [] on a spec audit and
// on a full run. Derived once, announced here before the first agent, and read by the Find thunk, the
// reuse loop, the counts and the checklist split, which runs over the lenses that RUN (S7).
// TOOL-dFairHearing-3 S4 - selected by each slot's DEFAULT key, so a swap into a light slot runs there.
// TOOL-dFairHearing-18 S2 - on a whole-design run, the walker slots whose slice is empty: a slot with no cell is not
// dispatched, and RUN INTEGRITY reads it as an idle walker slot, never as a light run.
const walkSlices = isWalk ? deriveWalkSlices(walk.items, walk.scenarios, walk.run) : null
const skippedLenses = isWalk ? LENSES.filter((L, i) => !walkSlices[i].length).map((L) => L.key)
  : !isSpec && intensity === 'light' ? LENSES.filter((L) => LIGHT_LENSES.indexOf(L.replaces || L.key) === -1).map((L) => L.key) : []
const runningLensKeys = LENS_KEYS.filter((k) => skippedLenses.indexOf(k) === -1)
const lensesRunning = runningLensKeys.length
// TOOL-dFairHearing-11 S6 - every finder agent the run dispatches, both runs on a twinned one.
const findersRunning = lensesRunning * (twinned ? 2 : 1)
if (skippedLenses.length && !isWalk)
  log(`WARNING: intensity light — the ${skippedLenses.join(', ')} lens(es) were NOT run; their classes are swept only through the checklist shares`)
if (isWalk)
  log(`walk: run ${walk.run} of ${walk.runs}, sliced by ${WALK_SLICING[walk.run - 1]}, seed ${walk.seed} — ` +
    `${walk.items.length * walk.scenarios.length} cell(s), ${walk.items.length} item(s) through ${walk.scenarios.length} scenario(s); ` +
    LENSES.map((L, i) => `${L.key} ${walkSlices[i].length}`).join(', ') +
    (skippedLenses.length ? `; walker slot(s) with no slice, not dispatched: ${skippedLenses.join(', ')}` : ''))
// Closing review round 1, L6 - a note for a lens this run skips reaches no prompt, so the log and RUN
// INTEGRITY report it apart, as UNREAD. Wording only: the check above still accepts the key (spec 7's
// non-goal), and the review key still carries it.
// TOOL-dFairHearing-9 S3 - and so is a note for a default a swap displaced: that lens does not run either.
const unreadNotes = notedLenses.filter((k) => skippedLenses.indexOf(k) !== -1 || swappedLenses.some((L) => L.replaces === k))
const readNotes = notedLenses.filter((k) => unreadNotes.indexOf(k) === -1)
if (unreadNotes.length)
  log(`WARNING: lens notes were supplied for skipped lens(es), unread: ${unreadNotes.join(', ')}`)
// ---- TOOL-dFairHearing-15 S1-S3 — THE CHECKLIST AGENT, the first spawn of a diff review given no `checklist` ----
// AFTER every refusal above, so a refused call still spawns nothing, and BEFORE the input print and the
// resume probe, because the parsed checklist joins the review key and the probe's directory name carries
// that key. The checker is found at run time over the nested and the flat spelling, never guessed; the
// stdout takes the path a caller's string takes, `extractByDesign` then `parseChecklist` with their
// refusals, so the checker's order is the C<n> order. A caller's `checklist` wins and nothing spawns;
// the spec kind never acquires, since `unattended-build`'s resolver already hands it a `--for-paths` one.
// WHAT THIS DOES NOT CHECK: that the agent ran the command it was told to and returned stdout unaltered;
// the by-design head-count refusal catches a truncated block, as the resolver's comment says of its own.
phase('Resume')
let acquiredChecklist = null
let checklistWhy = null
if (!isSpec && a.checklist === undefined) {
  const res = await agent(
    `You are the CHECKLIST AGENT of a Tier-2 review. You run one command and report its output. You judge ` +
      `nothing, review nothing and write nothing.\n\n` +
      `1. Run \`git -C ${repo} ls-files --error-unmatch tools/memory-tree/gotchas.py\`; when it fails, run ` +
      `\`git -C ${repo} ls-files --error-unmatch tools/gotchas.py\`. The checker is the first of the two that is ` +
      `tracked; when neither is, return NO checklist and checklistError \`no checker tracked\`.\n` +
      `2. In ${repo}, run \`python <checker> --for-diff ${base}..${head}\` with a 120-second timeout.\n` +
      `3. Return its stdout VERBATIM as checklist. Return NO checklist and a checklistError naming why instead when ` +
      `it exits non-zero (name the code), it times out, or its stdout carries no line starting \`- \` (write ` +
      `\`no bug class selected\`).\n` +
      `Return JSON {checklist} or {checklistError}.`,
    Object.assign({
      label: renderAgentLabel(reviewScope, 'resume:checklist'),
      phase: 'Resume',
      // The resolver's three optional fields, copied (`unattended-build`'s SUBJECTS_SCHEMA): none required, so
      // an agent that cannot produce a checklist still validates and its reason is read below.
      schema: { type: 'object', properties: { checklist: { type: 'string' }, checklistPaths: { type: 'array', items: { type: 'string' } }, checklistError: { type: 'string' } } },
    }, probeOpts), // the probe's stage and type, as the resume probe takes them
  )
  // The resolver's `- ` item rule: a checklist reaches the parse only when it carries an item, and every
  // other outcome is a reason, announced below and never passed as an empty checklist.
  if (res && typeof res.checklist === 'string' && /^- /m.test(res.checklist)) acquiredChecklist = res.checklist
  else checklistWhy = !res ? 'the checklist agent died'
    : typeof res.checklist === 'string' && res.checklist.trim() ? 'no bug class selected'
      : (typeof res.checklistError === 'string' && res.checklistError) || 'the checklist agent returned neither `checklist` nor `checklistError`'
  log(acquiredChecklist !== null ? `checklist from --for-diff ${base}..${head}`
    : `WARNING: no checklist was acquired — ${checklistWhy}; no lens sweeps the project's recurring bug classes`)
}
const byDesignBlock = extractByDesign(acquiredChecklist !== null ? acquiredChecklist : a.checklist)
const checklist = parseChecklist(byDesignBlock.remainder)
const CHECKLIST_ITEMS = checklist.items
// `byDesign` is the caller's KNOWN AND TRACKED issues THEN the block's INTENDED BEHAVIOUR, each under its
// own label, so neither displaces the other: a caller's tracked list never erases the invariants, and a
// block can never override what a caller said. `byDesignSources` is what the log and RUN INTEGRITY say.
const BY_DESIGN_ENTRIES = byDesignBlock.entries || []
const byDesignParts = []
const byDesignSources = []
if (a.byDesign) {
  byDesignParts.push('Known and tracked — do not re-report:\n' + a.byDesign)
  byDesignSources.push('the caller\'s byDesign')
}
if (BY_DESIGN_ENTRIES.length) {
  byDesignParts.push('Intended behaviour — invariants this change touches:\n' + BY_DESIGN_ENTRIES.join('\n'))
  byDesignSources.push(BY_DESIGN_ENTRIES.length + ' invariant(s) from the checklist\'s by-design block')
}
const byDesign = byDesignParts.length ? byDesignParts.join('\n') : 'none supplied'
if (!byDesignSources.length)
  byDesignSources.push('none supplied — no caller byDesign and ' + (byDesignBlock.entries ? 'a block of 0' : 'no block'))
for (const s of byDesignSources) log('by-design: ' + s)
// What RUN INTEGRITY's `Checklist:` line says where nothing was swept, worded per cause.
const checklistAbsence = checklistWhy !== null ? 'not acquired: ' + checklistWhy
  : acquiredChecklist !== null ? 'acquired with no item' : a.checklist === undefined ? 'absent' : 'supplied with no item'
// TOOL-aSightedSkeptic-4 S2-S6 - THE SPLIT, deriveChecklistShares, defined in the prelude beside the walk slicer.
// TOOL-aSightedSkeptic-7 S7 - over the RUNNING keys, so a skipped lens takes no share and no item is
// lost with it. On a full run these are LENS_KEYS, and the split is unchanged.
const checklistShares = deriveChecklistShares(CHECKLIST_ITEMS, runningLensKeys)
const checklistSubject = isSpec ? 'the spec set' : 'the diff'
// One block per lens, built here rather than in the prompt. Skeptics get none (S3).
const checklistBlock = {}
for (const k of runningLensKeys) {
  const share = checklistShares[k]
  checklistBlock[k] = !CHECKLIST_ITEMS.length
    ? ''
    : `CHECKLIST — the project's recurring bug classes, split across the lenses so each is swept once.\n` +
      (checklist.preamble ? checklist.preamble + '\n' : '') +
      (share.length
        ? `This lens holds ${share.length} of the ${CHECKLIST_ITEMS.length} items; the others hold the rest.\n` +
          share.map((x) => `C${x.n} ${x.text}`).join('\n') + '\n' +
          `Sweep EACH class above against ${checklistSubject} and report only a FRESH hit: a defect of that class ` +
          `${checklistSubject} introduces or touches. Begin such a finding's claim with its C<n> label. A class with no hit needs no finding.\n`
        : `This lens holds none of the ${CHECKLIST_ITEMS.length} items; the other lenses hold them all.\n`)
}
// S4/S5 - the assignment is recoverable from the log; an absence is ANNOUNCED, worded per cause.
if (CHECKLIST_ITEMS.length)
  log(`checklist: ${CHECKLIST_ITEMS.length} item(s) over ${lensesRunning} lens(es), each swept by exactly one — ` +
    runningLensKeys.map((k) => k + ' ' + (checklistShares[k].length ? checklistShares[k].map((x) => 'C' + x.n).join(' ') : 'none')).join('; '))
// A reason the checklist agent gave was announced where it returned, so it is not announced twice.
else if (checklistAbsence === 'absent')
  log('WARNING: no `checklist` was supplied — no lens sweeps the project\'s recurring bug classes; pass the caller\'s checklist output as `checklist`')
else if (checklistWhy === null) log(`WARNING: \`checklist\` was ${checklistAbsence} — no lens sweeps the project's recurring bug classes`)

// ---- TOOL-dDerivedDocket-29 S2/S3 — THE RESUME PROBE, one agent, before the Find phase ----------
// WHY ONE AGENT. The script has no filesystem, so something with one has to read the key directory.
// A reader per reused lens would spend a spawn per lens on a platform that has just been refusing
// spawns, and a caller-supplied reuse list would put the burden on every caller, including the build
// harness, which has no filesystem either. The probe re-emits each file's JSON under a schema whose
// items ARE the lens and verdict schemas, so a malformed file fails validation instead of being
// trusted. It is trusted exactly as far as a lens is: everything a reused lens returns still passes
// through the skeptics.
//
// THE KEY: kind, round, the pinned subject, and a fingerprint over `context`, `byDesign`,
// `priorFindings`, `lensNotes`, `specs`, `checklist`, `intensity` and the REVIEW_SHAPE literal - every input a lens prompt interpolates,
// and the prompts' own shape, except `repo`, which is left out on
// purpose: the common dir is shared by every worktree on the node, and a take-over from another
// worktree of the same commits is exactly the re-run this exists for. The reuse holds only for a
// `workerType: 'none'` run: under a named type no judge wrote a file, so the key directory is empty
// and a re-run dispatches every judge again (TOOL-aMendedFleet-111 S6). A judge `roles` key is such a
// type and joins the print; the synthesis role does not, since no keyed file is the synthesis's to
// make stale (TOOL-aOrientedCast-5 S6). A spec audit's subject is every
// `path@blob` in the order given; a diff review's is the RESOLVED base and head (F5), so a review
// commissioned against `origin/main` is pinned to the sha that ref named, and a moved ref is a
// different key rather than a stale answer.
// TOOL-aSightedSkeptic-5 S3/S5 - `lensNotes` is an input the finder prompts interpolate, and
// REVIEW_SHAPE is a literal standing for the prompts and schemas themselves: a lens
// file written by OLD prompts under the same inputs must not be reused by new ones. ONE bump for the
// whole aSightedSkeptic build (its shared invariant 5); a later change to a prompt, a schema or the
// lens set moves this literal again. It rides the print rather than the key's string, so the probe
// prompt's hand-spelled directory follows without a second edit.
// TOOL-aEvidencedLens-1 S3 - r2, ONE bump for the whole aEvidencedLens build (its shared invariant 5).
// r3 at the reconcile of aMendedFleet with origin/main: the merged reuse lens and the workerType-aware
// re-run texts differ from both sides' prompts, so neither side's lens files may answer the merge.
// TOOL-dFairHearing-5 S5 - r4, ONE bump for the whole dFairHearing build: the diff skeptic's prompt
// gains the `duplicate of id=<n>` form, so no verify file judged under the old prompt is reused.
const REVIEW_SHAPE = 'lenses5-r4'
// TOOL-aSightedSkeptic-3 S5 - `specs` is interpolated by renderIntent(), so it joins the print too.
// TOOL-aSightedSkeptic-4 S7 - so does the PARSED checklist: a CRLF string and its LF twin are one key,
// and a lens swept under one checklist is never reused under another.
// TOOL-aSightedSkeptic-7 S8 - and so does `intensity`: a light run and a full run never share a lens file.
// TOOL-aMendedFleet-67 S2 - and so does `workerType`, only when it names a type, so a `none` key equals
// every pre-type key and a run under a type is never answered from a `none` run's lens files.
// TOOL-aEvidencedLens-2 S5 - and, on the spec kind only, PROBE_RULES, spread so the diff print object is
// unchanged. `scratch` is a location, not content, and stays out: a resumed run has a new scratchpad.
// TOOL-aEvidencedLens-4 S7 - and `prevBlobs`, one per subject in order, null where absent, ONLY when some
// subject carries one: a run carrying none, the diff kind included, keeps its print and so its key.
// TOOL-aOrientedCast-5 S6 - and `roles` as `{ find, verify }`, the types this run's finders and skeptics
// took from it, ONLY when one of the two is set, so a run whose judges took no role keeps its key. The
// synthesis role and the other kind's finder key stay out: the synthesis writes no keyed file, so its
// role cannot make one stale, and the other finder key is never read.
// TOOL-dFairHearing-2 S4 - and `preset`, ONLY off its `unit-spec` default, so a design-audit run never
// reuses a unit-spec run's lens files on the same subjects and every key a run without it derives holds.
// TOOL-dFairHearing-3 S5 - and `optIn`, ONLY when not empty, so a swapped run never resumes an unswapped
// one's lens files and every key a run without it derives holds.
// TOOL-dFairHearing-9 S4 - the notes print as the run's own, `runNotes`, so a flat-form caller and a
// per-preset caller passing the same notes derive one key, and every flat-form key holds.
// TOOL-dFairHearing-11 S8 - and `twin: true` ONLY on a twinned run, so it never reuses an untwinned run's lens
// or verify files, and every untwinned key holds. The probe's type stays out: it writes no keyed file.
// TOOL-dFairHearing-8 S2 - and `fixJudge` ONLY under `class`, so a class-judged verify file is never reused by an
// `instance` run and every key a run without it derives holds. `unclassed` and `legManifest` reach the synthesis alone, and stay out.
const inputPrint = deriveFnv1a(renderCanonical(Object.assign({ shape: REVIEW_SHAPE, context: context, byDesign: byDesign, priorFindings: priorFindings, lensNotes: runNotes, specs: SPECS, checklist: checklist, intensity: intensity, ...(isSpec ? { probeRules: PROBE_RULES } : {}),
  ...(prevBlobCount ? { prevBlobs: subjects.map((x) => (x && typeof x === 'object' && x.prevBlob !== undefined ? x.prevBlob : null)) } : {}) }, workerType ? { workerType: workerType } : {},
  roledJudges ? { roles: { find: roles[finderKey] || null, verify: roles.skeptic || null } } : {}, preset !== 'unit-spec' ? { preset: preset } : {},
  optInKeys.length ? { optIn: optIn } : {}, twinned ? { twin: true } : {}, fixJudge === 'class' ? { fixJudge: fixJudge } : {},
  // TOOL-dFairHearing-18 S1 - and the checked `walk` with WALK_RULES on a whole-design run alone, since the walker
  // prompts interpolate both, so every other run's key holds and each run of a walk keys apart.
  isWalk ? { walk: walk, walkRules: WALK_RULES } : {})))
const specSubject = isSpec
  ? deriveFnv1a(subjects.map((x) => (x && typeof x === 'object' ? `${x.path}@${x.blob}` : String(x))).join('\n'))
  : ''
function deriveReviewKey(b, h) {
  return `${kind}-r${round}-${isSpec ? specSubject : deriveSubjectPair(b, h)}-${inputPrint}`
}
// TOOL-aMendedFleet-18 S2/S3 - the token counter is read ONCE before the first agent, and a stage's
// line is the delta to its own read. `agents` follows the final return's formula through the stage
// reached (spec rev-3): finders at find, plus skeptic batches at verify, plus the synthesis at synth.
const tokensAtStart = readOutputTokens()
function renderStageShape(at, counts, agents) {
  const now = readOutputTokens()
  return renderShapeLine(Object.assign({ kind: kind, round: round, intensity: intensity, at: at, agents: agents,
    outTokens: tokensAtStart === null || now === null ? null : now - tokensAtStart }, counts))
}
// `phase('Resume')` opened above the checklist agent (TOOL-dFairHearing-15 S1).
const probe = await agent(
  `You are the RESUME PROBE of a Tier-2 review. You read files and report them. You judge nothing, ` +
    `review nothing and write nothing.\n\n` +
    `1. Run \`git -C ${repo} rev-parse --git-common-dir\`. Turn the answer into an ABSOLUTE path with ` +
    `forward slashes (a relative answer is relative to ${repo}) and return it as commonDir.\n` +
    (isSpec
      // TOOL-aEvidencedLens-4 S4 - the move check's read half. The probe reports; the HARNESS compares.
      ? `2. For EACH path below, run \`git -C ${repo} hash-object <path>\` and return blobs: one {path, now} per path, ` +
        `now being the hash it prints, or an empty string when the command fails. Compare nothing:\n` +
        subjects.map((x) => `  - ${x && typeof x === 'object' ? x.path : String(x)}`).join('\n') + `\n`
      : `2. Run \`git -C ${repo} rev-parse --verify ${base}^{commit}\` and \`git -C ${repo} rev-parse --verify ${head}^{commit}\` ` +
        `and return the two FULL shas as base and head. Return an empty string for one that does not resolve.\n`) +
    `3. The review directory is <commonDir>/review-lenses/` +
    (isSpec
      ? deriveReviewKey('', '')
      : `${kind}-r${round}-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`) +
    `/ . If it does not exist, return finds: [] and verifies: [] - that is the normal first run.\n` +
    `4. Otherwise Read every file in it named find-<lens>.json or verify-batch-<n>.json. Return each ` +
    `find file's JSON in finds and each verify file's JSON in verifies, EXACTLY as it is on disk plus ` +
    `a name field holding its file name. Do not repair, complete or re-judge anything: a file that ` +
    `does not parse, or lacks a field the schema requires, is left out and its name listed in skipped.\n` +
    // TOOL-dFairHearing-8 S4 - the leg manifest, read here because the harness has no filesystem (spec section 8 F4).
    `5. Whatever steps 3 and 4 found, Read ${repo}/${legManifest}, the leg manifest. When it parses as JSON whose top level ` +
    `is an array, return legs: the name field of every object in that array, in file order. When it is absent, does not ` +
    `parse, or its top level is not an array, leave legs out.\n` +
    `Return JSON {commonDir, ${isSpec ? 'blobs:[...], ' : 'base, head, '}finds:[...], verifies:[...], skipped:[...], legs:[...]}.`,
  Object.assign({
    label: renderAgentLabel(reviewScope, 'resume:probe'),
    phase: 'Resume',
    schema: {
      type: 'object',
      required: ['commonDir', 'finds', 'verifies'],
      properties: {
        commonDir: { type: 'string' },
        base: { type: 'string' },
        head: { type: 'string' },
        finds: { type: 'array', items: buildKeyedSchema(LENS_SCHEMA, []) },
        verifies: { type: 'array', items: buildKeyedSchema(isWalk ? WALK_VERDICT_SCHEMA : VERDICT_SCHEMA, ['batch', 'ids']) },
        skipped: { type: 'array', items: { type: 'string' } },
        // TOOL-dFairHearing-8 S4 - optional: a probe that omits it reads as no leg manifest read.
        legs: { type: 'array', items: { type: 'string' } },
        // Optional (spec F2): a probe that omits it reads as every subject UNCHECKED, never as none moved.
        ...(isSpec ? { blobs: { type: 'array', items: { type: 'object', required: ['path', 'now'], properties: { path: { type: 'string' }, now: { type: 'string' } } } } } : {}),
      },
    },
  }, probeOpts), // TOOL-dFairHearing-11 S1 - the probe's stage, typed like the other three
)
// A DEAD PROBE REUSES NOTHING, and says so. Reading a null as "every file present" would dispatch no
// lens and return an empty review; reading it as "nothing present" costs a full re-run, which is
// correct. The refs go to the lenses as given, and the key they write under is one no later resolved
// run produces for a moving ref, so nothing written here answers a later, different question.
const probeLive = !!(probe && typeof probe.commonDir === 'string' && probe.commonDir)
let baseSha = base
let headSha = head
if (!isSpec && probeLive && FULL_SHA.test(String(probe.base)) && FULL_SHA.test(String(probe.head))) {
  baseSha = String(probe.base)
  headSha = String(probe.head)
} else if (!isSpec && probeLive) {
  log(`WARNING: the resume probe did not resolve ${base}...${head} to two full shas — nothing can be reused, and the lenses are handed the refs as given`)
}
if (!probeLive) log('WARNING: the resume probe died — nothing could be reused, so every lens is dispatched with the refs as given')
// TOOL-dFairHearing-8 S4 - the leg names a `gate:` disposition may name, or null: a dead probe or one returning no
// `legs` read no manifest, and then every `gate:` disposition is refused and the log and RUN INTEGRITY say so.
const legs = probeLive && Array.isArray(probe.legs) ? probe.legs.filter((x) => typeof x === 'string' && x) : null
log(legs ? `leg manifest: ${legs.length} leg name(s) read from ${legManifest}`
  : `WARNING: no leg manifest was read from ${legManifest} — every gate: disposition is refused`)
// TOOL-aEvidencedLens-4 S4/S6 - the move check's judging half. A subject is MOVED when the probe read a
// 40-hex hash that does not begin with the pinned blob, and UNCHECKED when no usable hash came back: a
// dead probe, a missing `blobs` key or row, or an empty `now` never reads as "none moved".
const probeBlobs = isSpec && probeLive && Array.isArray(probe.blobs) ? probe.blobs : []
const movedSubjects = []
const uncheckedSubjects = []
for (const x of isSpec ? subjects : []) {
  if (!x || typeof x !== 'object') continue
  const row = probeBlobs.find((b) => b && b.path === x.path)
  const now = row && typeof row.now === 'string' ? row.now : ''
  if (!/^[0-9a-f]{40}$/.test(now)) uncheckedSubjects.push(x.path)
  else if (now.indexOf(String(x.blob)) !== 0) movedSubjects.push({ path: x.path, blob: x.blob, now: now })
}
for (const m of movedSubjects)
  log(`WARNING: ${m.path} MOVED since it was pinned: pinned ${m.blob}, now ${m.now} — every lens reviews it as it now stands and reads the moved text as unreviewed fold text`)
const reviewKey = deriveReviewKey(baseSha, headSha)
const keyDir = probeLive
  ? `${String(probe.commonDir).replace(/\\/g, '/').replace(/\/+$/, '')}/review-lenses/${reviewKey}`
  : `<common-dir>/review-lenses/${reviewKey}`
const keyDirHow = probeLive
  ? ''
  : ` <common-dir> is the absolute, forward-slash form of what \`git -C ${repo} rev-parse --git-common-dir\` prints.`
const diffCmd = `git -C ${repo} diff ${baseSha}...${headSha}`
const presentFinds = probeLive && Array.isArray(probe.finds) ? probe.finds : []
const presentVerifies = probeLive && Array.isArray(probe.verifies) ? probe.verifies : []
log(`review key ${reviewKey} — ${presentFinds.length} lens file(s) and ${presentVerifies.length} verify file(s) present`)
// A file the probe could not re-emit under the schema is left out and NAMED, and its agent is
// dispatched. Saying so here is what keeps a skipped file from reading as an absent one.
if (probeLive && Array.isArray(probe.skipped) && probe.skipped.length)
  log(`WARNING: the resume probe skipped ${probe.skipped.length} unreadable or malformed file(s), each dispatched rather than reused: ${probe.skipped.join(', ')}`)
// REUSE COMPARES THE FILE'S OWN `key` FIELD with the string computed above, never the directory name
// alone: the probe composed the directory, and a probe that composed it wrong must not turn a stale
// file into a current answer.
// TOOL-dFairHearing-11 S6 - a finder run's stage key and file name: run a's as before, run b's suffixed `:b`
// and `-b`, so run b reuses only its own file. `reusedLens` is keyed by the file name.
function renderLensStage(L, run) {
  return `find:${L.key}${run === 'b' ? ':b' : ''}`
}
function renderLensFileName(L, run) {
  return `find-${L.key}${run === 'b' ? '-b' : ''}.json`
}
const FINDER_RUNS = twinned ? ['a', 'b'] : ['a']
const reusedLens = new Map()
for (const run of FINDER_RUNS)
  for (const L of LENSES) {
    if (skippedLenses.indexOf(L.key) !== -1) continue // S4 - no `reused` line names a lens that will not run
    const name = renderLensFileName(L, run)
    const file = presentFinds.find((f) => f && f.name === name && f.lens === L.key && Array.isArray(f.findings))
    if (file && file.key === reviewKey) {
      reusedLens.set(name, file)
      log(`reused ${renderLensStage(L, run)} from ${keyDir}/${name} — not dispatched`)
    } else if (file) {
      log(`${renderLensStage(L, run)}: a file is present under another key (${file.key}) — dispatched`)
    }
  }

// TOOL-aSightedSkeptic-1 - THE BRIEF, one copy, opening every finder AND every skeptic prompt. The
// skeptic used to be handed none of it, so it read whatever checkout its working directory was and
// was told "by-design" refutes without being shown what is. Read at CALL time: the subject line
// needs the shas the resume probe resolved. Two lines are worded by role, and a diff skeptic gets
// one more, SCOPE; a spec audit has no range, so nothing in it is older than the review (spec F2).
// TOOL-aSightedSkeptic-3 S2/S3 - THE INTENT BLOCK, inside the brief so finders and skeptics share it.
// The diff kind ALWAYS names the range's commit log over the RESOLVED shas (two dots: `log a..b`
// lists the commits `diff a...b` introduces), with or without `specs` (spec F2). The harness has no
// filesystem, so a listed document that is missing is the lens's to report. A spec audit has no
// range: its `specs` are sibling context, read for agreement and never reported against.
function renderIntent() {
  const listed = SPECS.map((p) => `  - ${p}`).join('\n')
  if (isSpec)
    return SPECS.length
      ? `SIBLING CONTEXT — documents NOT under audit, named by the caller as what the subjects must agree with. Read them for agreement and report nothing against them:\n${listed}`
      : `SIBLING CONTEXT — none supplied; the subjects are their own statement of intent.`
  return `INTENT — what this change was meant to do.\n` +
    (SPECS.length
      ? `The caller named these documents as its statement of intent:\n${listed}\n` +
        `Read the ones your lens or your finding touches; the intent lens reads every one WHOLE before it reads the diff. ` +
        `A listed document that does not exist in ${repo} is itself a finding against its path.\n`
      : '') +
    `Read the range's commit messages, \`git -C ${repo} log --format=%B ${baseSha}..${headSha}\`, and any spec or design document the diff touches or those messages name.` +
    (SPECS.length ? '' : ' No spec was supplied, so these are the statement of intent.')
}

function renderBrief(role) {
  const skeptic = role === 'skeptic'
  const lines = [
    `REPO: ${repo} — run every git command as \`git -C ${repo} …\`; every path below is relative to it.`,
    isSpec
      ? `SUBJECT: the spec set, each file at its pinned blob:\n` + subjects.map((x) => {
        const mv = movedSubjects.find((m) => m.path === x.path)
        return `  - ${x.path}  blob ${x.blob}` + (mv ? `  MOVED since pinned, now ${mv.now}` : '')
      }).join('\n')
      : `SUBJECT: the diff \`${diffCmd}\`.`,
    `CONTEXT: ${context}`,
    renderIntent(),
    // TOOL-aEvidencedLens-4 S2/S3 - a spec fold round NAMES its fold text: one diff per subject from the
    // blob the previous round audited, or says plainly that nothing names it. Round 1 is unchanged.
    `REVIEW ROUND: ${round}${round > 1
      ? (isSpec
        ? (foldDegraded
          ? ' - a DEGRADED fold review: no subject carries prevBlob and no priorFindings were supplied, so nothing names the text the previous round\'s fixes introduced. Review every subject whole.'
          : ' - this is a FOLD review.\nFOLD DIFF - the PRIMARY subject is the text the previous round\'s fixes introduced. Read each diff\n' +
            'below FIRST, then each file whole for agreement. A diff command that fails means its file is\nreviewed whole.\n' +
            subjects.map((x) => `  - ${x.path}: ` + (x.prevBlob === undefined
              ? 'no prevBlob was supplied - review this file whole'
              : String(x.prevBlob).indexOf(String(x.blob)) === 0 || String(x.blob).indexOf(String(x.prevBlob)) === 0
                ? 'unchanged since the previous round'
                : `git -C ${repo} diff ${x.prevBlob} ${x.blob}`)).join('\n'))
        : ' - this is a FOLD review. The diff above is what the previous round\'s fixes introduced, not the whole build.')
      : ''}`,
  ]
  if (skeptic && !isSpec)
    lines.push(`SCOPE: a finding is in scope only if this diff introduced its defect or made it reachable. A defect present unchanged at the base is PRE-EXISTING: refute it. Check with \`git -C ${repo} show ${baseSha}:<path>\`.`)
  lines.push(skeptic ? `BY DESIGN (refute any finding one of these covers): ${byDesign}` : `BY DESIGN (do NOT re-report these): ${byDesign}`)
  lines.push(priorFindings.length
    ? (skeptic
      ? `PRIOR ROUND'S CONFIRMED FINDINGS - these were RAISED AND FIXED. A finding that re-raises one of these originals, rather than a defect in its fix, is refuted as a duplicate:\n`
      : `PRIOR ROUND'S CONFIRMED FINDINGS - these were RAISED AND FIXED. Judge the FIX, and do not re-raise the original:\n`) +
      priorFindings.map((f) => `  - ${f.ref || '(no ref)'} - ${f.claim || f.title || '(no claim)'}`).join('\n')
    : isSpec && round > 1
      ? `PRIOR ROUND'S FINDINGS: none supplied for this round-${round} review.`
      : `PRIOR ROUND'S FINDINGS: none - this is a first-round review of ${isSpec ? 'the whole spec set' : 'the whole diff'}.`)
  return lines.join('\n') + '\n\n'
}

// TOOL-dFairHearing-11 S6 - ONE LENS'S CALL, for either finder run: its prompt, every option but its stage's,
// and `ready`, what a skipped or reused lens resolves to without a spawn, else null. Both fans below call it
// at call time, since the brief needs the shas the probe resolved, and keep their agent( call inline.
// TOOL-dFairHearing-18 S3 - ONE WALKER'S BRIEF: its run's slicing, WALK_RULES, the scenarios and items its slice
// holds and no other slot's, its cells, and the seed line, which names the key's SHA-256 only when the walk is seeded.
function renderWalkBrief(w) {
  const cells = walkSlices[w]
  const ids = cells.map((c) => c[1]).filter((x, i, all) => all.indexOf(x) === i)
  const tags = cells.map((c) => c[0]).filter((x, i, all) => all.indexOf(x) === i)
  return `WALK — run ${walk.run} of ${walk.runs}, sliced by ${WALK_SLICING[walk.run - 1]}. You are walker slot ${w + 1} of 5, and your slice is ` +
    `${cells.length} cell(s): ${tags.length} item(s) through ${ids.length} scenario(s).\n` +
    `WALK RULES:\n- ` + WALK_RULES.join('\n- ') + `\n` +
    `SCENARIOS of your slice, each with what it walks:\n` +
    walk.scenarios.filter((s) => ids.indexOf(s.id) !== -1).map((s) => `  - ${s.id} — ${renderPromptLine(s.name)}: ${renderPromptLine(s.walks)}`).join('\n') + `\n` +
    `ITEMS of your slice, each with its step:\n` +
    walk.items.filter((x) => tags.indexOf(x.tag) !== -1).map((x) => `  - ${x.tag} (step ${x.step})`).join('\n') + `\n` +
    `CELLS of your slice, one walk row each:\n` + cells.map((c) => `  - ${c[0]} · ${c[1]}`).join('\n') + `\n` +
    (walk.seed === 'none'
      ? `SEED: none — this walk is not seeded.\n`
      : `SEED: ${walk.seed} — the design carries planted defects, and the key naming them has the SHA-256 ${walk.keySha}. ` +
        `The key is sealed: never open, search for or ask for it.\n`)
}
function buildLensCall(L, run) {
  const name = renderLensFileName(L, run)
  // TOOL-aSightedSkeptic-7 S4 - a skipped lens resolves to a SENTINEL and dispatches nothing. Never
  // null: null is how a dead agent reaches the script, and every light run would defer forever.
  const ready = skippedLenses.indexOf(L.key) !== -1 ? { lens: L.key, path: '', findings: [], skipped: true } : reusedLens.get(name) || null
  return {
    ready: ready,
    opts: { label: renderAgentLabel(reviewScope, renderLensStage(L, run)), phase: 'Find', schema: LENS_SCHEMA },
    prompt:
      renderBrief('finder') +
      (isSpec
        // S6 - the spec kind's acquire sentence. The lens holds a filesystem and the orchestrator does
        // not, so the BLOB COMPARISON happens here. Without it S5 is a string test any caller
        // satisfies. TOOL-aEvidencedLens-4 S5 - the move is no longer a fixed BLOCKER: the resume probe
        // reports it to RUN INTEGRITY, and a defect IN the moved text is graded by the rubric like any other.
        // TOOL-aOrientedCast-5 S5 - under a role, the identity and posture sentences are the role's block.
        ? (roles[finderKey] ? '' : `You are the ${L.key} reviewer of a SPEC SET. `) +
          `For EACH subject listed under SUBJECT above: first run ` +
          `\`git -C ${repo} hash-object <path>\` and compare the result to the pinned blob. A mismatch ` +
          `means the spec MOVED since this review was commissioned: review the file as it now stands, and read ` +
          `the moved text with \`git -C ${repo} diff <blob> -- <path>\` as unreviewed fold text. Report a defect IN ` +
          `that text as a finding graded by the SEVERITY RUBRIC below; the move itself is not a finding. ` +
          `Then Read the file WHOLE.\n\n`
        : (roles[finderKey] ? '' : `You are the ${L.key} reviewer. `) + `Review ONLY the diff named under SUBJECT above (run \`${diffCmd}\`, then Read/Grep the touched files + their immediate callers).\n\n`) +
        `LENS: ${L.brief}\n` +
        // TOOL-aEvidencedLens-2 S2 - the probe policy directly under the brief; '' on the diff kind.
        probeBlock +
        // TOOL-dFairHearing-18 S3 - a walker's WALK_RULES and its own slice, under the probe policy; '' on every other preset.
        (isWalk ? renderWalkBrief(LENSES.indexOf(L)) : '') +
        // TOOL-aSightedSkeptic-5 S5 - this lens's note and no other's, directly under its brief.
        (notedLenses.indexOf(L.key) !== -1 ? `PROJECT NOTE FOR THIS LENS (from the caller's lensNotes): ${runNotes[L.key]}\n` : '') +
        // TOOL-aSightedSkeptic-4 S3 - this lens's checklist share, and no other's.
        checklistBlock[L.key] +
        `\n` +
        (isSpec
          ? `Emit CONCRETE findings only — each needs file, where, severity (blocker|high|medium|low), with "where" being the section address, e.g. "section 2 S5", a one-line claim, the impact, a proposed fix, and evidence: the command you ran and what it printed, or read: <path>:<line> for a finding that rests on reading alone. A spec finding is often the ABSENCE of a line, so address it by section. Every finding is ABOUT the spec set; its evidence may come from anywhere in ${repo} at HEAD.` +
            (roles[finderKey] ? '' : ` No speculation, no style nits.`) + ` If nothing real, return findings: [].\n`
          : `Emit CONCRETE findings only — each needs file, line, severity (blocker|high|medium|low), a one-line claim, the impact, and a proposed fix. ` +
            (roles[finderKey] ? `Nothing outside the diff.` : `No speculation, no style nits, nothing outside the diff.`) + ` If nothing real, return findings: [].\n`) +
        // TOOL-aSightedSkeptic-6 S2 - the rubric beside the instruction that asks for a severity.
        SEVERITY_RUBRIC + `\n` +
        // TOOL-dDerivedDocket-29 S1 - WRITE BEFORE RETURN. A fan that dies on a session limit loses
        // every structured return with it; a file on disk survives, and the next run's probe reuses it.
        // TOOL-aMendedFleet-67 S2 - a judge under `workerType` holds no Write tool, so it is told none.
        // TOOL-aOrientedCast-5 S4 - nor under a role, and a mixed run's untyped judges follow `durable`.
        (!durable
          ? `\nWrite no file. Set path to an empty string.\n`
          : `\nDURABILITY — BEFORE you return, whatever you found, Write the exact JSON object you are about to return, plus one more field "key":"${reviewKey}", to ${keyDir}/${name}, creating the directory if it is missing.${keyDirHow} Set path to that file's absolute, forward-slash path.\n`) +
        (isWalk
          ? `Return JSON {lens:"${L.key}", path, findings:[{file,where,severity,claim,impact,fix,evidence}], walk:[{item,scenario,actor,needs,witness,route,verdict,findings,reason}]}.`
          : isSpec
          ? `Return JSON {lens:"${L.key}", path, findings:[{file,where,severity,claim,impact,fix,evidence}]}.`
          : `Return JSON {lens:"${L.key}", path, findings:[{file,line,severity,claim,impact,fix}]}.`),
  }
}
phase('Find')
const finderResults = await boundedParallel(
  LENSES.map((L) => () => {
    const c = buildLensCall(L, 'a')
    return c.ready ? Promise.resolve(c.ready) : agent(c.prompt, Object.assign(c.opts, findOpts))
  }),
)
// TOOL-dFairHearing-11 S6 - RUN B, a second awaited fan over the same literal after run a's, never a loop, so
// each fan stays one call over the bounded literal. An untwinned run dispatches nothing here.
const finderResultsB = !twinned ? [] : await boundedParallel(
  LENSES.map((L) => () => {
    const c = buildLensCall(L, 'b')
    return c.ready ? Promise.resolve(c.ready) : agent(c.prompt, Object.assign(c.opts, findOpts))
  }),
)
// Every finder slot, run a's then run b's, beside the return each one gave: what every count below reads.
const FINDER_SLOTS = FINDER_RUNS.flatMap((run) => LENSES.map((L) => ({ L: L, run: run })))
const finderReturns = finderResults.concat(finderResultsB)

// S1 (TOOL-aGuardedTally-1): a dead lens returns null and filter(Boolean) drops it silently, so an
// all-dead run used to be indistinguishable from an all-clean one. Observed live: a review returned
// `clean: 0 findings` with agents_done 0, four ENOTFOUND errors, and a journal of four `started`
// lines and zero `result` lines. Count what actually came back and never call absence cleanliness.
// TOOL-aSightedSkeptic-7 S5 - a skipped lens is neither live nor dead. Membership in skippedLenses
// decides it, never the sentinel's own field, which a reused file could also carry.
const liveResults = finderReturns.filter((x, i) => x && skippedLenses.indexOf(FINDER_SLOTS[i].L.key) === -1)
const lensesDead = finderReturns.filter((x) => !x).length
// TOOL-dDerivedDocket-29 S5 - the LABEL of every agent that did not return, so a caller can say what a
// re-run will dispatch. The harness cannot tell a user's mid-run skip from a death, because both
// return null, and both defer: an unjudged finding was never a result. Run b's carry `:b`.
const deadLensLabels = FINDER_SLOTS.filter((s, i) => !finderReturns[i]).map((s) => renderLensStage(s.L, s.run))
// `ref` is DISPLAY ONLY from here on — it rides the prompts and the report lines and is never a map
// key. `id` is assigned once, after every lens has returned, and is the only join key.
// TOOL-aSightedSkeptic-8 S1 - derived from finderResults BY INDEX, so each finding carries `lens`, the
// key the harness DISPATCHED (spec F1), never the agent's echo. Same members, same order as
// liveResults, so ids and batch membership do not move.
// TOOL-dFairHearing-11 S6 - and `run`, the finder run it came from: run a's findings number first, then run
// b's, so each run is one contiguous id range.
// TOOL-dFairHearing-18 S4 - on a whole-design run each finding also carries its walker `slot` and its `local` index
// in that walker's findings array, which is what a walk row's `findings` names.
const allFindings = finderReturns
  .flatMap((r, i) => (!r || skippedLenses.indexOf(FINDER_SLOTS[i].L.key) !== -1 ? [] : (r.findings || []).map((f, k) =>
    ({ ...f, lens: FINDER_SLOTS[i].L.key, run: FINDER_SLOTS[i].run, ref: `${f.file}:${isSpec ? f.where : f.line}`, ...(isWalk ? { slot: i, local: k } : {}) }))))
  .map((f, i) => ({ ...f, id: i + 1 }))

// ---- TOOL-dFairHearing-18 S4/S5 — THE WALK TABLE, joined from the walkers' returns, and its gaps ----------------
// A dead walker leaves its slice gapped, and the run defers before any synthesis as every lens death does.
const walkReturns = isWalk ? finderReturns.map((r, i) => (r && skippedLenses.indexOf(FINDER_SLOTS[i].L.key) === -1 ? r : null)) : []
const walkGaps = isWalk ? deriveWalkGaps(walkSlices, walkReturns) : []
// One row per cell of the grid, item by item in the order given, each through the scenarios in order: the owning
// walker's one row for the cell, its fields `null` where it gave none or two, and the verdict as the record reads
// it: `holds`, the finding ids `<R><w>-F<id>`, or `not on path: <reason>`.
function deriveWalkRows() {
  const owner = new Map()
  walkSlices.forEach((cells, w) => cells.forEach((c) => owner.set(c[0] + ' · ' + c[1], w)))
  const rows = []
  for (const it of walk.items)
    for (const sc of walk.scenarios) {
      const w = owner.get(it.tag + ' · ' + sc.id)
      const r = walkReturns[w]
      const mine = r && Array.isArray(r.walk) ? r.walk.filter((x) => x && x.item === it.tag && x.scenario === sc.id) : []
      const x = mine.length === 1 ? mine[0] : null
      const ids = x && x.verdict === 'finding' && Array.isArray(x.findings)
        ? x.findings.map((k) => allFindings.find((f) => f.slot === w && f.local === k)).filter(Boolean)
          .map((f) => 'ABC'[walk.run - 1] + (w + 1) + '-F' + f.id).join(', ')
        : ''
      rows.push({ item: it.tag, scenario: sc.id, actor: x ? x.actor : null, needs: x ? x.needs : null, witness: x ? x.witness : null,
        route: x ? x.route : null,
        verdict: !x ? null : x.verdict === 'holds' ? 'holds' : x.verdict === 'finding' ? ids || null : x.verdict === 'not-on-path' ? 'not on path: ' + String(x.reason) : String(x.verdict) })
    }
  return rows
}
const walkRows = isWalk ? deriveWalkRows() : []
if (walkGaps.length)
  log(`WARNING: the walk table has ${walkGaps.length} gap(s) — the walk is RED and the synthesis is told its verdict is BLOCKED: ${walkGaps.join('; ')}`)
else if (isWalk) log(`walk table: ${walkRows.length} cell(s), no gap`)
// The cells handed to and refuted by the skeptics, null until the verify stage hands them.
let cellsSampled = null
let cellsRefuted = null
// What every return past the find stage carries on a whole-design run, read at call time.
function buildWalkFields() {
  return isWalk ? { walkTable: walkRows, walkGaps: walkGaps, cellsSampled: cellsSampled, cellsRefuted: cellsRefuted } : {}
}

// TOOL-aEvidencedLens-6 - THE PER-LENS YIELD, one row per lens that RAN, in dispatch order. `rows` is
// the ledger (or [] before the verify stage); `items` the synthesis's item list, or null when none can
// be trusted (no synthesis, a dead one, or a tally fault), which nulls `defects` and `unique` rather
// than guessing a split the tally itself refused. Items are read with the tally's own rules: a
// severity outside the closed four skips its item, and an id that is not confirmed is ignored.
// `unique` counts ITEMS whose every confirmed id is this lens's, so two lenses confirming one defect
// are one shared item and neither is credited. `precision` is null, never 0, where nothing was judged.
// TOOL-dFairHearing-5 S4 - `merged` is a refuted row whose reason names a duplicate target; an orphan's
// row reads unverified, so this selects exactly the verify stage's merged set. It leaves `refuted` and
// joins precision's numerator and denominator.
function deriveLensYield(rows, items) {
  const confirmedLens = new Map(rows.filter((e) => e.verdict === 'confirmed').map((e) => [e.id, e.lens]))
  const defects = {}
  const unique = {}
  for (const it of Array.isArray(items) ? items : []) {
    if (['BLOCKER', 'HIGH', 'MEDIUM', 'LOW'].indexOf(it ? String(it.severity).toUpperCase() : '') === -1) continue
    const owners = new Set((Array.isArray(it.ids) ? it.ids : []).filter((id) => confirmedLens.has(id)).map((id) => confirmedLens.get(id)))
    for (const k of owners) defects[k] = (defects[k] || 0) + 1
    if (owners.size === 1) for (const k of owners) unique[k] = (unique[k] || 0) + 1
  }
  return runningLensKeys.map((k) => {
    const mine = rows.filter((e) => e.lens === k)
    const n = { confirmed: 0, refuted: 0, merged: 0, uncertain: 0, unverified: 0 }
    for (const e of mine) n[e.verdict === 'refuted' && extractDuplicateTarget(e.reason) !== null ? 'merged' : e.verdict]++
    const judged = n.confirmed + n.merged + n.refuted
    return {
      // TOOL-dFairHearing-11 S6 - a twinned lens returned when both its runs did.
      lens: k, returned: FINDER_SLOTS.every((s, i) => s.L.key !== k || !!finderReturns[i]), raw: mine.length, confirmed: n.confirmed, refuted: n.refuted, merged: n.merged,
      uncertain: n.uncertain, unverified: mine.length - judged,
      precision: judged ? (n.confirmed + n.merged) / judged : null,
      defects: items ? defects[k] || 0 : null, unique: items ? unique[k] || 0 : null,
    }
  })
}
// The counts known BEFORE the synthesis, as the verbatim block its prompt carries; `defects` and
// `unique` need its items, so they are returned and logged and never in the report.
function renderLensYield(rows) {
  const cols = ['lens', 'returned', 'raw', 'confirmed', 'refuted', 'merged', 'uncertain', 'unverified', 'precision']
  return ['| ' + cols.join(' | ') + ' |', '|' + cols.map(() => '---').join('|') + '|']
    .concat(rows.map((e) => '| ' + [e.lens, e.returned ? 'yes' : 'no', e.raw, e.confirmed, e.refuted, e.merged, e.uncertain, e.unverified,
      e.precision === null ? '-' : e.precision.toFixed(2)].join(' | ') + ' |'))
    .join('\n')
}
function printLensYield(rows) {
  for (const e of rows)
    log(`lens yield: ${e.lens} returned ${e.returned ? 'yes' : 'no'} · raw ${e.raw} · confirmed ${e.confirmed} · refuted ${e.refuted} · merged ${e.merged} · ` +
      `uncertain ${e.uncertain} · unverified ${e.unverified} · precision ${e.precision === null ? '-' : e.precision.toFixed(2)} · ` +
      `defects ${e.defects === null ? '-' : e.defects} · unique ${e.unique === null ? '-' : e.unique}`)
}

// ---- TOOL-dDerivedDocket-29 S5 — THE `exit` FIELD, on every return. `complete` when every agent
// ---- returned, `deferred-platform` when any lens, skeptic batch or the synthesis came back null. A
// ---- deferred return always carries `blockers: null`, the key, and `pending`: the labels a re-run
// ---- with identical args will dispatch, everything else being reused from the key directory when
// ---- `durable` is true, the `workerType: 'none'` case; when it is false a re-run dispatches all. The
// ---- one null `blockers` that is NOT a death, the tally fault below, stays `complete`: a re-run
// ---- cannot repair an adjudication, so that path keeps the refusal its callers already make.
if (lensesDead === findersRunning) {
  log(`UNVERIFIED — all ${findersRunning} lenses failed to return. Nothing was reviewed. Deferred: re-run with identical args.`)
  // TOOL-aMendedFleet-18 S3 - no lens returned, so even `raw` was never produced (spec rev-3).
  const shapeLine = renderStageShape('find', {}, findersRunning)
  log(shapeLine)
  const lensYield = deriveLensYield([], null) // TOOL-aEvidencedLens-6 S5 - every row returned: false, zeros
  printLensYield(lensYield)
  return {
    identity,
    shape: shapeLine,
    // TOOL-dTieredTribunal-1 S3 - null, never 0. No synthesis ran, so there is no adjudicated count.
    exit: 'deferred-platform', key: reviewKey, pending: deadLensLabels, durable,
    confirmed: [], report: null, root: repo, blockers: null, highs: null, lensesRun: 0, lensesDead,
    lensesReused: reusedLens.size,
    note: `DEFERRED: no lens completed (${lensesDead}/${findersRunning} died) — nothing was reviewed; ${renderRerunTail(deadLensLabels.join(', '), false)}`,
    round, ...deriveRoundFields(null), priorFindings: priorFindings.length, intensity, optIn, ...(isSpec ? { preset } : {}), skippedLenses, twin: null,
    // TOOL-aSightedSkeptic-8 S5 - nothing was judged on this path.
    ledger: [], confirmedFindings: [], appendix: '', lensYield, ...buildWalkFields(),
  }
}
if (allFindings.length === 0 && !isWalk) {
  // A ZERO FROM A PARTIAL FAN IS NOT A CLEAN BILL. It used to return `partial: … survivors found
  // nothing`, which the build harness's clean-round test cannot tell from a result; it defers now.
  const deferred = lensesDead > 0
  const note = deferred
    ? `DEFERRED: ${lensesDead}/${findersRunning} lenses died and the survivors found nothing — ${renderRerunTail(deadLensLabels.join(', '), false)}`
    : 'clean: 0 findings'
  log(note)
  const shapeLine = renderStageShape('find', { raw: 0 }, findersRunning)
  log(shapeLine)
  const lensYield = deriveLensYield([], null) // TOOL-aEvidencedLens-6 S5
  printLensYield(lensYield)
  // TOOL-dTieredTribunal-1 S3 - null, never 0: no synthesis ran on this path either.
  return {
    identity,
    shape: shapeLine,
    exit: deferred ? 'deferred-platform' : 'complete', key: reviewKey, pending: deadLensLabels, durable,
    confirmed: [], report: null, root: repo, blockers: null, highs: null, lensesRun: liveResults.length, lensesDead,
    lensesReused: reusedLens.size, note, round, ...deriveRoundFields(deferred ? null : 0), priorFindings: priorFindings.length, intensity, optIn, ...(isSpec ? { preset } : {}), skippedLenses, twin: null,
    ledger: [], confirmedFindings: [], appendix: '', lensYield, ...buildWalkFields(), // TOOL-aSightedSkeptic-8 S5 - no finding raised
  }
}
log(`${allFindings.length} raw findings across ${findersRunning} lenses — verifying in batches.`)

// --- Phase 2: VERIFY — batched skeptics (NOT one agent per finding) -----
phase('Verify')
// THE VERIFIER COUNT IS A CONSTANT. `chunk(allFindings, 5)` bounded the GROUP SIZE, so 70 findings
// bought 14 skeptics — still linear, which the protocol says is not enough. Bounding the group COUNT
// makes the batch grow and the agent count stand still. `chunk` slices `verifyOrder` contiguously, in
// the order `batchBy` picks: id order, or address order so two lenses citing one place meet one
// skeptic (TOOL-dFairHearing-4), and Math.ceil never yields an empty
// group: at N < MAX_VERIFIERS it produces exactly N groups of one. The total is the agent-cap hook's
// own MAX_VERIFIERS, the review protocol's verify total, and never the agent limit the concurrency
// width above renders, which bounds how many run at once (TOOL-dGroundRules-10 F3).
const MAX_VERIFIERS = 5
const verifyOrder = batchBy === 'address' ? deriveAddressOrder(allFindings) : allFindings
// TOOL-dFairHearing-18 S6 - a whole-design walk that raised no finding still dispatches ONE batch, of clean cells
// alone, labelled `verify:cells`; every other run's batches are the bounded split as before.
const batches = verifyOrder.length || !isWalk ? chunk(verifyOrder, Math.ceil(verifyOrder.length / MAX_VERIFIERS)) : [[]] // gov:fixed-verifiers
log(`${allFindings.length} finding(s) -> ${batches.length} verifier(s) (cap ${MAX_VERIFIERS}) by ${batchBy}`)
// TOOL-dFairHearing-18 S6 - THE CLEAN CELLS each batch is handed on a whole-design run: eight per batch, the audit's
// number (spec section 8 F7), from the cells whose verdict is `holds`, sorted by `<item> · <scenario>`, drawn at an
// even stride and dealt round-robin. A pure function of the table, so a re-run hands the same cells.
function deriveCellSample(rows, batchCount) {
  const renderCellKey = (x) => x.item + ' · ' + x.scenario
  const clean = rows.filter((x) => x.verdict === 'holds').sort((p, q) => (renderCellKey(p) < renderCellKey(q) ? -1 : renderCellKey(p) > renderCellKey(q) ? 1 : 0))
  const n = Math.min(8 * batchCount, clean.length)
  const out = Array.from({ length: batchCount }, () => [])
  for (let k = 0; k < n; k++) out[k % batchCount].push(clean[Math.floor((k * clean.length) / n)])
  return out
}
const batchCells = isWalk ? deriveCellSample(walkRows, batches.length) : batches.map(() => [])
if (isWalk) {
  cellsSampled = batchCells.reduce((s, g) => s + g.length, 0)
  log(`clean cells: ${cellsSampled} of ${walkRows.filter((x) => x.verdict === 'holds').length} sampled over ${batches.length} skeptic batch(es)`)
}
// TOOL-dDerivedDocket-29 S4 - A BATCH IS REUSED ONLY FOR THE EXACT FINDINGS IT JUDGED. Its file must
// carry the run's key AND a fingerprint over the batch's own ids and claims together. The batch number
// alone is not enough: when a dead lens is re-dispatched the ids after it shift, and a name-keyed
// match would pair old verdicts with new findings. When every lens is reused the ids, the batches and
// their prints come out identical, which is what lets a dead synthesis re-run alone.
// TOOL-aSightedSkeptic-2 S5 - the FIX joins the print, since the skeptic now judges it: a verify file
// judged against one fix is never reused for a finding carrying another under the same claim.
// TOOL-dFairHearing-18 S6 - on a whole-design run the batch's clean cells join its print.
const batchPrints = batches.map((g, gi) => deriveFnv1a(renderCanonical(isWalk
  ? { findings: g.map((f) => [f.id, String(f.claim), String(f.fix)]), cells: batchCells[gi].map((x) => x.item + ' · ' + x.scenario) }
  : g.map((f) => [f.id, String(f.claim), String(f.fix)]))))
// TOOL-dFairHearing-4 S5 - a label no longer tells its ids, so the file carries them as `ids`, and a
// file without them, the old shape, is never reused. TOOL-dFairHearing-18 S6 - the cell-only batch is
// `verify:cells`, a label neither scheme produces.
const batchLabels = batches.map((g, gi) => (g.length ? `verify:batch-${gi + 1}` : 'verify:cells'))
const reusedBatch = batches.map((g, gi) => {
  const name = `verify-batch-${gi + 1}.json`
  const file = presentVerifies.find((v) => v && v.name === name && Array.isArray(v.verdicts) && Array.isArray(v.ids))
  if (file && file.key === reviewKey && file.batch === batchPrints[gi]) {
    log(`reused ${batchLabels[gi]} from ${keyDir}/${name} — not dispatched`)
    return file
  }
  if (file) log(`${batchLabels[gi]}: a file is present for another key or another set of claims — dispatched`)
  return null
})

const verdictResults = await boundedParallel(
  batches.map((group, gi) => () =>
    reusedBatch[gi]
      ? Promise.resolve(reusedBatch[gi])
      : agent(
      renderBrief('skeptic') +
      // TOOL-aEvidencedLens-3 S1-S5 - the spec skeptic confirms by the rubric, at any grade, re-runs the
      // finder's evidence under the SAME probe-policy bytes the finders read (spec section 8 F3: one copy
      // of one rule), and refutes in six named cases only. The old test, "unbuildable or wrong", made a
      // LOW unreachable beside a rubric that defines one. The diff kind is untouched (shared invariant 2).
      (isSpec
        ? probeBlock + `\n` +
          // TOOL-aOrientedCast-5 S5 - under a role, the try-to-refute stance is the role's block.
          (roles.skeptic ? `For EACH finding below, read` : `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it. Read`) +
          ` the cited spec at the cited section and the siblings it names; ` +
          `a claim about code or a record is checked against that code or record, never against the spec's account of it. ` +
          `Then re-run the finding's evidence under the PROBE POLICY above: run the command it names, or re-read the path and line it names, and say in \`reason\` what you observed.\n` +
          `"confirmed" when the claim is TRUE of the spec set, and of the tree where it makes a claim about the tree, AT ANY RUBRIC SEVERITY: the rubric grades it, confirmation does not.\n` +
          `"refuted" in these cases only: (1) a NON-GOAL or a PARKED FORK withholds what it asks; (2) the cited section ALREADY SAYS it; ` +
          `(3) the premise is FALSE ON RE-PROBE, including evidence that does not reproduce, meaning what you observed contradicts the claim; ` +
          `(4) BY DESIGN, a case the BY DESIGN block covers; (5) a DUPLICATE, opening \`reason\` with \`duplicate of id=<n>\` for another finding in this batch that you CONFIRM in this same answer, ` +
          `or \`duplicate of prior <ref>\` for a prior round's original; (6) a PREFERENCE that names no defect the rubric grades, not even a low.\n` +
          `Evidence that reads \`-\` was not recorded: probe the claim yourself and never confirm on the finder's word. ` +
          `A probe you could not run inside its bound is a finding you cannot establish; apply the default by the finder's grade, and never call it evidence that does not reproduce.\n\n`
        : (roles.skeptic ? `For EACH finding below, ` : `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — `) + `read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate).\n` +
          // TOOL-dFairHearing-5 S3 - the spec skeptic's case (5) form, so a diff duplicate is read as one.
          `A DUPLICATE opens \`reason\` with \`duplicate of id=<n>\` for another finding in this batch that you CONFIRM in this same answer.\n\n`) +
        // TOOL-aSightedSkeptic-6 S4 - the default follows the FINDER's grade (spec section 8 F3). An
        // unsure skeptic refuting a real blocker loses the defect; one answering uncertain on every
        // low-precision nit floods disposal. So only a costly finding is left outstanding.
        `WHEN YOU CANNOT ESTABLISH A FINDING either way: one the finder graded medium or low (the bracketed grade) is "refuted"; ` +
        `one the finder graded blocker or high is answered "uncertain", and its reason says what you could not establish. ` +
        `"uncertain" is never a substitute for a judgment you can make.\n\n` +
        SEVERITY_RUBRIC + `\n` +
        `For each finding you CONFIRM, also return \`severity\`, graded by this rubric against what you read, independent of the finder's bracketed grade.\n\n` +
        `Findings to judge:\n` +
        // TOOL-aSightedSkeptic-8 S2 - `lens=` after the grade; `id=<n> [` stays first for the stubs' id pattern.
        // TOOL-aEvidencedLens-3 S3 - the spec kind appends the finder's evidence, folded to one line
        // (absent or blank reads `-`). TOOL-aEvidencedLens-12 S2 - renderPromptLine, never renderCell:
        // the skeptic RE-RUNS this command, so a pipe in it must reach the prompt unescaped.
        (group.length ? '' : `  (none — this batch judges the clean cells below alone)`) +
        group
          .map((f) => `id=${f.id} [${f.severity}] lens=${f.lens} ${f.ref} — ${f.claim} | impact: ${f.impact} | fix: ${f.fix}` +
            (isSpec ? ` | evidence: ${renderPromptLine(f.evidence)}` : ''))
          .join('\n') +
        // TOOL-dFairHearing-18 S6 - a whole-design batch's clean cells, a third question; '' on every other run.
        (batchCells[gi].length
          ? `\n\nCLEAN CELLS, A THIRD QUESTION - the walkers read each cell below as holding, \`=\` meaning the item reads there ` +
            `as the design declares it. Try hard to REFUTE each: walk the item through the scenario yourself, against the design ` +
            `and the tree. Return \`cells\`, one {cell, verdict, reason, file, where, severity} per cell below, \`cell\` copied ` +
            `exactly as it is written before its first " — ": "holds" when it does; "refuted" when you can show it does not, with ` +
            `file and where addressing the defect, severity graded by the rubric, and reason saying what fails there.\n` +
            batchCells[gi].map((x) => `- ${x.item} · ${x.scenario} — actor ${renderPromptLine(x.actor)} | needs ${renderPromptLine(x.needs)} | ` +
              `witness ${renderPromptLine(x.witness)} | route ${renderPromptLine(x.route)}`).join('\n')
          : '') +
        // TOOL-aSightedSkeptic-2 S2 - the fix is judged as a SECOND, separate question. It never moves
        // the claim's verdict (spec section 8 F1): a real defect with a bad fix is still a real defect.
        // TOOL-dFairHearing-8 S2 - under `fixJudge: 'class'` the second variant, judged by the defect's class; the
        // first keeps the pre-switch bytes, so an `instance` run's verify prompt is unchanged.
        (fixJudge === 'class'
          ? `\n\nTHE FIX, A SECOND AND SEPARATE QUESTION. For each finding also judge its proposed fix by the defect's CLASS, as \`fixVerdict\`: ` +
            `"sound" when applying it cures the defect's class, every instance of the pattern the claim names in the subject and the code ` +
            `or specs it reaches, and introduces none you can see; ` +
            `"instance" when it cures the cited instance and leaves another of its class standing; ` +
            `"unsound" when it does not cure the cited instance, breaks a caller, an invariant or a sibling path, or introduces a defect of its own; ` +
            `"none" when no fix was proposed. For "unsound", \`fixNote\` holds ONLY the corrected fix, and for "instance" ONLY the ` +
            `class-level fix; either is empty when you have none. Say why in \`reason\`, never in \`fixNote\`. `
          : `\n\nTHE FIX, A SECOND AND SEPARATE QUESTION. For each finding also judge its proposed fix, as \`fixVerdict\`: ` +
            `"sound" when applying it cures the defect and introduces none you can see in the ${isSpec ? 'spec' : 'code'} it touches; ` +
            `"unsound" when it does not cure the defect, breaks a caller, an invariant or a sibling path, or introduces a defect of its own; ` +
            // Closing review round 1, M3 - fixNote carries the CORRECTION and nothing else, so an empty note
            // is the one way to say "no correction", and the harness branches on exactly that.
            `"none" when no fix was proposed. For "unsound", \`fixNote\` holds ONLY the corrected fix, and is empty when you have none; ` +
            `say why the fix is unsound in \`reason\`, never in \`fixNote\`. `) +
        `The fix verdict NEVER changes the finding's verdict: judge the claim on its own, then the fix on its own.` +
        (!durable
          ? `\n\nWrite no file. Set path to an empty string.`
          : `\n\nDURABILITY — BEFORE you return, Write the exact JSON object you are about to return, plus three more fields ` +
            `"key":"${reviewKey}", "batch":"${batchPrints[gi]}" and "ids":[${group.map((f) => f.id).join(',')}], to ${keyDir}/verify-batch-${gi + 1}.json, ` +
            `creating the directory if it is missing.${keyDirHow} Set path to that file's absolute, forward-slash path.`) +
        `\n\nReturn JSON {path, verdicts:[{id:<the integer id shown above>, verdict:"confirmed"|"refuted"|"uncertain", reason, severity:"blocker"|"high"|"medium"|"low" (on a confirmed verdict), fixVerdict:"sound"|"unsound"|"none"${fixJudge === 'class' ? '|"instance"' : ''}, fixNote}]}. ` +
        `Emit EXACTLY one verdict per finding above (${group.length} verdicts, ids ${group.map((f) => f.id).join(', ')}). ` +
        `Copy the integer id — do NOT re-type the file path, and do not renumber.` +
        (batchCells[gi].length ? ` Beside verdicts, return cells:[{cell, verdict:"holds"|"refuted", reason, file, where, severity}], one per clean cell above.` : ''),
        Object.assign({ label: renderAgentLabel(reviewScope, batchLabels[gi]), phase: 'Verify', schema: isWalk ? WALK_VERDICT_SCHEMA : VERDICT_SCHEMA }, verifyOpts),
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
const deadBatchLabels = batchLabels.filter((lbl, gi) => !verdictResults[gi])
const batchesReused = reusedBatch.filter(Boolean).length
// TOOL-dFairHearing-18 S6 - A REFUTED CLEAN CELL becomes a finding of the lens `cell-sample`: the skeptic's address,
// its reason as the claim, and its grade, numbered after every walker finding. One skeptic raised it and none judged
// it, so it stands UNVERIFIED (spec section 8 F8). Only a cell its batch was handed counts, once.
const cellFindings = []
if (isWalk)
  verdictResults.forEach((r, gi) => {
    const handed = batchCells[gi].map((x) => x.item + ' · ' + x.scenario)
    const seen = []
    for (const c of r && Array.isArray(r.cells) ? r.cells : []) {
      const cell = c && typeof c.cell === 'string' ? c.cell.trim() : ''
      if (handed.indexOf(cell) === -1 || seen.indexOf(cell) !== -1) continue
      seen.push(cell)
      if (c.verdict !== 'refuted') continue
      const file = String(c.file || '')
      const where = String(c.where || '')
      // A grade outside the closed four, reachable from a reused file or a stub, reads medium.
      const severity = SEVERITIES.indexOf(c.severity) !== -1 ? c.severity : 'medium'
      cellFindings.push({ file: file, where: where, severity: severity, claim: String(c.reason || ''),
        impact: `the walk read the cell ${cell} as holding, and a skeptic refuted it`, fix: '(none proposed: a refuted clean cell)',
        evidence: String(c.reason || ''), lens: 'cell-sample', run: 'a', ref: `${file}:${where}`, cell: cell })
    }
  })
for (const f of cellFindings) allFindings.push(Object.assign(f, { id: allFindings.length + 1 }))
if (isWalk) {
  cellsRefuted = cellFindings.length
  log(`clean cells: ${cellsRefuted} of ${cellsSampled} refuted` + (cellsRefuted ? ` — UNVERIFIED cell-sample finding(s), ids ${cellFindings.map((f) => f.id).join(', ')}` : ''))
}
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
// TOOL-aEvidencedLens-3 S6 - an ORPHANED duplicate (spec section 8 F2). A refutation
// opening `duplicate of id=<n>` drops the finding on the strength of another one, so it holds only when
// <n> is a DIFFERENT id in the SAME batch that stands CONFIRMED after the conflict demotion above.
// Otherwise the defect would leave the confirmed set with nothing kept in its place: it is demoted to
// UNVERIFIED exactly as a contradicted verdict is. TOOL-dFairHearing-5 S2 - on both kinds, since the
// diff skeptic is now given the same duplicate form.
const orphanDuplicates = new Set()
for (const group of batches) {
  const batchIds = new Set(group.map((f) => f.id))
  for (const f of group) {
    const v = verdictById.get(f.id)
    const n = v && v.verdict === 'refuted' ? extractDuplicateTarget(v.reason) : null
    if (n === null) continue
    if (n === f.id || !batchIds.has(n) || verdictById.get(n)?.verdict !== 'confirmed') orphanDuplicates.add(f.id)
  }
}
for (const id of orphanDuplicates) verdictById.delete(id)
// TOOL-dFairHearing-5 S4 - MERGED: a duplicate refutation that survived the orphan check above. Its
// verdict stays `refuted` in the ledger and the appendix, which are the skeptic's record; it leaves the
// `refuted` count and joins precision as a confirmation, and never the confirmed set or the items.
const merged = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'refuted' &&
  extractDuplicateTarget(verdictById.get(f.id).reason) !== null)
const mergedIds = new Set(merged.map((f) => f.id))

// TOOL-aSightedSkeptic-2 S3/S6 - a confirmed finding's fix as the synthesis and the death log carry it.
// Read at call time, so it is called only after the join above. Absent or outside FIX_VERDICTS is
// UNJUDGED, and the finder's fix is then marked as the finder's proposal and nothing more.
function renderFixLine(f) {
  const v = verdictById.get(f.id) || {}
  const note = String(v.fixNote || '').trim()
  // TOOL-dFairHearing-8 S2 - an instance-only fix gives way to its class-level note, as an unsound one gives way to
  // its correction; outside `fixJudge: 'class'` the verdict is not in FIX_VERDICTS and falls through to NOT JUDGED.
  if (v.fixVerdict === 'instance' && FIX_VERDICTS.indexOf('instance') !== -1)
    return (note
      ? `fix: judged INSTANCE-ONLY by the skeptic, whose class-level fix is: ${note}`
      : `fix: judged INSTANCE-ONLY by the skeptic, who gave no class-level fix - the class fix is STILL TO BE DESIGNED`) +
      ` (the finder's proposal, which cures the cited instance and leaves its class standing: ${f.fix})`
  if (v.fixVerdict === 'sound') return `fix (judged SOUND by the skeptic): ${f.fix}`
  if (v.fixVerdict === 'none') return `fix: none proposed${f.fix ? ` (the finder wrote: ${f.fix})` : ''}`
  if (v.fixVerdict === 'unsound')
    return (note
      ? `fix: REJECTED by the skeptic, whose corrected fix is: ${note}`
      : `fix: REJECTED by the skeptic, who gave no correction - the fix is STILL TO BE DESIGNED`) +
      ` (the finder's rejected proposal, never to be written as the fix: ${f.fix})`
  return `fix (NOT JUDGED - the finder's proposal only): ${f.fix}`
}

// TOOL-aSightedSkeptic-6 S5 - the BINDING grade: the skeptic's on a confirmed verdict when it is in
// the closed set, else the finder's. Read at call time, so it is called only after the join above.
function deriveBindingSeverity(f) {
  const v = verdictById.get(f.id)
  return v && v.verdict === 'confirmed' && SEVERITIES.indexOf(v.severity) !== -1 ? v.severity : f.severity
}

const confirmed = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'confirmed')
const refuted = allFindings.filter((f) => verdictById.get(f.id)?.verdict === 'refuted' && !mergedIds.has(f.id))
// TOOL-dFairHearing-7 S1 - read only under `addressTwins: 'shown'`; `refuted` already holds no merged duplicate.
const twinPairs = deriveTwinPairs(confirmed, refuted)
// TOOL-dFairHearing-11 S7 - THE TWIN RUN's hand-off: the cross-run candidate pairs, each confirmed finding of
// run a and one of run b that deriveTwinPairs, read with its two arguments as the two runs, places at one
// address; and the record line, rendered here and copied by the synthesis. Both read only on a twinned run.
const crossRunPairs = deriveTwinPairs(confirmed.filter((f) => f.run === 'a'), confirmed.filter((f) => f.run === 'b'))
  .map((p) => ({ a: p.confirmed, b: p.refuted }))
function renderTwinRange(findings) {
  return findings.length ? findings[0].id + '-' + findings[findings.length - 1].id : '-'
}
const twinLine = `review-twin runs=2 a=${renderTwinRange(allFindings.filter((f) => f.run === 'a'))} b=${renderTwinRange(allFindings.filter((f) => f.run === 'b'))}`
if (twinned) log(twinLine)
// TOOL-aSightedSkeptic-6 S8 - UNVERIFIED is every finding with neither a confirmed nor a refuted
// verdict: those a skeptic answered `uncertain`, and those with no usable verdict at all. The two are
// counted apart, so a run whose skeptics all answered never reads as one where none returned.
const unverified = allFindings.filter((f) => ['confirmed', 'refuted'].indexOf(verdictById.get(f.id)?.verdict) === -1)
const uncertainFindings = unverified.filter((f) => verdictById.get(f.id)?.verdict === 'uncertain')
// TOOL-dFairHearing-18 S6 - a refuted clean cell is unverified by design, not for want of a verdict, so it is counted
// apart, as `cellsRefuted`.
const noVerdict = unverified.filter((f) => verdictById.get(f.id)?.verdict !== 'uncertain' && f.lens !== 'cell-sample')
// precision is (confirmed+merged)/(confirmed+merged+refuted): an unjudged or uncertain finding is not
// evidence either way, and a merged duplicate is a confirmation of its original (TOOL-dFairHearing-5 S4).
const judged = confirmed.length + merged.length + refuted.length
const precision = judged ? (confirmed.length + merged.length) / judged : 0
if (uncertainFindings.length)
  log(`WARNING: ${uncertainFindings.length} finding(s) answered UNCERTAIN by a skeptic — counted UNVERIFIED, neither confirmed nor refuted: ids ${uncertainFindings.map((f) => f.id).join(', ')}`)
if (noVerdict.length)
  log(`WARNING: ${noVerdict.length} finding(s) came back with NO usable verdict — counted UNVERIFIED, not refuted: ids ${noVerdict.map((f) => f.id).join(', ')}`)
if (conflicts.size)
  log(`WARNING: ${conflicts.size} finding(s) got CONTRADICTORY verdicts — demoted to UNVERIFIED: ids ${[...conflicts].join(', ')}`)
if (orphanDuplicates.size)
  log(`WARNING: ${orphanDuplicates.size} finding(s) refuted as a DUPLICATE of an id that is not a confirmed survivor in their batch — demoted to UNVERIFIED: ids ${[...orphanDuplicates].join(', ')}`)
if (duplicates) log(`note: ${duplicates} repeat verdict(s) agreed with the standing one — idempotent.`)
if (spurious) log(`WARNING: ${spurious} verdict(s) carried an id this run never assigned — discarded.`)
// TOOL-aSightedSkeptic-2 S4 - the fix verdicts over CONFIRMED findings only, since a refuted
// finding's fix is never applied. The four counts sum to confirmed.length.
// TOOL-dFairHearing-8 S2 - `instance` moves only under `fixJudge: 'class'`, where FIX_VERDICTS holds it.
const fixCounts = { sound: 0, unsound: 0, none: 0, instance: 0 }
const unjudgedFixIds = []
for (const f of confirmed) {
  const fv = verdictById.get(f.id).fixVerdict
  if (FIX_VERDICTS.indexOf(fv) !== -1) fixCounts[fv]++
  else unjudgedFixIds.push(f.id)
}
if (unjudgedFixIds.length)
  log(`WARNING: ${unjudgedFixIds.length} confirmed finding(s) carry a fix no skeptic judged — ids ${unjudgedFixIds.join(', ')}`)
// TOOL-aSightedSkeptic-6 S5 - UNGRADED (no legal skeptic grade, so the finder's binds) and RE-GRADED
// (the skeptic's grade differs from the finder's, and binds). The finding's own `severity` stays the
// finder's grade; deriveBindingSeverity is the only reader of the skeptic's.
const ungradedIds = []
const skepticRegradedIds = []
for (const f of confirmed) {
  if (SEVERITIES.indexOf(verdictById.get(f.id).severity) === -1) ungradedIds.push(f.id)
  else if (deriveBindingSeverity(f) !== f.severity) skepticRegradedIds.push(f.id)
}
if (ungradedIds.length)
  log(`WARNING: ${ungradedIds.length} confirmed finding(s) carry no skeptic grade — UNGRADED, bound at the finder's grade: ids ${ungradedIds.join(', ')}`)
if (skepticRegradedIds.length)
  log(`note: ${skepticRegradedIds.length} confirmed finding(s) RE-GRADED by the skeptic, whose grade binds: ids ${skepticRegradedIds.join(', ')}`)
if (skepticsDead)
  log(`WARNING: ${skepticsDead}/${verdictResults.length} skeptic batch(es) died — verification is PARTIAL.`)
log(
  `confirmed ${confirmed.length} / refuted ${refuted.length} / merged ${merged.length} / unverified ${unverified.length} (${uncertainFindings.length} uncertain) — precision ${precision.toFixed(2)}` +
    (judged === 0
      ? ' (NOTHING was judged — the number is a placeholder, not a result)'
      : precision < 0.5 ? ' (below 0.5 — tighten scope/priming next time, don\'t add agents)' : ''),
)

// TOOL-aMendedFleet-17 S1 - the class names a claim's HEAD labels denote. Only the leading run of
// `C<n>`, `[C<n>]`, each optionally followed by `:` or `,`, is read, so a `C3` in the prose is not
// a label. Label n names item n's first token after an optional `[ ]`/`[x]` box when that token is a
// lowercase slug; otherwise, and for an n outside the items, the label itself, which no slug spells.
// TOOL-dFairHearing-8 S5 - THE CLASS SLUG GRAMMAR, one constant: an item's slug is read by it here, and the
// disposition check tests a `new:` slug against it, so the classes a run hands over are the ones `classes` names.
const CLASS_SLUG = '[a-z][a-z0-9]*(?:-[a-z0-9]+)*'
const ITEM_SLUG = new RegExp('^(?:\\[[ x]\\]\\s+)?(' + CLASS_SLUG + ')(?=\\s|$)')
function extractItemSlug(item) {
  const m = typeof item === 'string' ? ITEM_SLUG.exec(item) : null
  return m ? m[1] : null
}
function extractFindingClasses(claim, items) {
  const names = []
  let rest = String(claim || '')
  let m
  while ((m = /^\s*(?:\[C(\d+)\]|C(\d+))[:,]?(?=\s|$)/.exec(rest))) {
    rest = rest.slice(m[0].length)
    const n = m[1] || m[2]
    const name = extractItemSlug(items[n - 1]) || 'C' + n
    if (names.indexOf(name) === -1) names.push(name)
  }
  return names
}
// The class slugs the disposition check hands over: each slug-led item's, once, in item order. A `C<n>` is no class.
const classSlugs = CHECKLIST_ITEMS.map(extractItemSlug).filter((s, i, all) => s && all.indexOf(s) === i)

// TOOL-aSightedSkeptic-8 S3 - THE LEDGER, every finding and its verdict in id order, refuted ones
// included: the only place a refuted finding reaches a record. Read through verdictById by the
// integer id, never by `ref` (two findings at one file:line would collapse into one row).
const ledger = allFindings.map((f) => {
  const v = verdictById.get(f.id)
  return {
    id: f.id,
    lens: f.lens,
    ref: f.ref,
    severity: f.severity,
    skepticSeverity: v && SEVERITIES.indexOf(v.severity) !== -1 ? v.severity : null,
    verdict: v && ['confirmed', 'refuted', 'uncertain'].indexOf(v.verdict) !== -1 ? v.verdict : 'unverified',
    reason: conflicts.has(f.id) ? 'contradictory verdicts' : orphanDuplicates.has(f.id) ? 'duplicate of an unconfirmed id' : v ? String(v.reason || '') : '',
    fixVerdict: v && FIX_VERDICTS.indexOf(v.fixVerdict) !== -1 ? v.fixVerdict : null,
    claim: f.claim,
    // TOOL-aMendedFleet-17 S2 - empty with no checklist, where no label can denote a class.
    classes: CHECKLIST_ITEMS.length ? extractFindingClasses(f.claim, CHECKLIST_ITEMS) : [],
    // TOOL-dFairHearing-8 S8 - the accepted disposition, set on a confirmed entry after the check below; `-` otherwise.
    disposition: '-',
  }
})
// S4 - the confirmed set in the shape `priorFindings` reads, so round N+1 is handed it rather than a
// re-typed copy. A rejected fix is replaced by the skeptic's correction when one was given; with none,
// the finder's fix stays, and `fixVerdict: 'unsound'` beside it marks it rejected.
const confirmedFindings = confirmed.map((f) => {
  const v = verdictById.get(f.id)
  const fixVerdict = FIX_VERDICTS.indexOf(v.fixVerdict) !== -1 ? v.fixVerdict : null
  const note = String(v.fixNote || '').trim()
  // TOOL-dFairHearing-8 S2 - an instance-only fix gives way to its class-level note as an unsound one does.
  return { id: f.id, lens: f.lens, ref: f.ref, claim: f.claim, severity: deriveBindingSeverity(f),
    fix: (fixVerdict === 'unsound' || fixVerdict === 'instance') && note ? note : f.fix, fixVerdict, disposition: '-' }
})
// S6 - one cell: absent as `-`, a pipe escaped, and a run of any character Python's str.splitlines
// breaks on folded to one space, so no claim or reason can forge or cut a row in the table
// TOOL-aSightedSkeptic-9 parses (closing review round 1, L2: CR/LF alone let a U+2028 cut one).
// TOOL-aEvidencedLens-12 S1 - the line-break fold alone, for a prompt line: nothing else is rewritten,
// and a value blank once folded reads `-` like an absent one. renderCell is this plus the pipe escape.
function renderPromptLine(v) {
  if (v === null || v === undefined) return '-'
  const s = String(v).replace(/[\r\n\x0b\x0c\x1c-\x1e\x85\u2028\u2029]+/g, ' ')
  return s.trim() === '' ? '-' : s
}
function renderCell(v) {
  return renderPromptLine(v).replace(/\|/g, '\\|')
}
// The first eight columns are the hand-off to TOOL-aSightedSkeptic-9; `claim` rides the ledger only
// (spec F4). TOOL-aMendedFleet-17 S3 - `classes` is the ninth, its names joined by one space.
// TOOL-dFairHearing-8 S8 - `disposition` is the tenth, each row's `disposition` field.
function renderAppendix(rows) {
  if (!rows.length) return ''
  const cols = ['id', 'lens', 'ref', 'severity', 'skepticSeverity', 'verdict', 'reason', 'fixVerdict', 'classes', 'disposition']
  return ['## Appendix — every finding', '', '| ' + cols.join(' | ') + ' |', '|' + cols.map(() => '---').join('|') + '|']
    .concat(rows.map((e) => '| ' + cols.map((c) => renderCell(c === 'classes' ? (e.classes || []).join(' ') : e[c])).join(' | ') + ' |'))
    .join('\n')
}
// TOOL-dFairHearing-18 S5 - THE WALK TABLE BLOCK, pure, in the whole-design audit's `[walk-table]` grammar: the heading,
// the `walk-seed` pin the design grade reads, then one row per cell through renderCell, the item backticked.
function renderWalkTable(w, rows) {
  return [`## Walk table — run ${w.run} of ${w.runs}, sliced by ${WALK_SLICING[w.run - 1]}`,
    `walk-seed mode=${w.seed} key-sha256=${w.seed === 'none' || !w.keySha ? '-' : w.keySha}`, '',
    '| Item | Scenario | Actor | Needs | Witness | Route | Verdict |', '|---|---|---|---|---|---|---|']
    .concat(rows.map((x) => '| `' + x.item + '` | ' + [x.scenario, x.actor, x.needs, x.witness, x.route, x.verdict].map(renderCell).join(' | ') + ' |'))
    .join('\n')
}
// `-` in every disposition cell: what an exit with no accepted set returns. The synthesis is handed its copy with a
// `(synthesis)` cell on each confirmed row, the one cell it writes (spec section 8 F2).
const appendix = renderAppendix(ledger)
const synthAppendix = renderAppendix(ledger.map((e) => (e.verdict === 'confirmed' ? Object.assign({}, e, { disposition: '(synthesis)' }) : e)))
// TOOL-aMendedFleet-18 S1 - every count the verify stage produced, the four severities over RAW
// confirmed findings by binding grade; a grade outside the closed four is counted in none.
const verifiedCounts = { raw: allFindings.length, confirmed: confirmed.length, refuted: refuted.length, merged: merged.length,
  unverified: unverified.length, blocker: 0, high: 0, medium: 0, low: 0 }
for (const f of confirmed) {
  const g = deriveBindingSeverity(f)
  if (SEVERITIES.indexOf(g) !== -1) verifiedCounts[g]++
}

// U6/S7: the run that most needs a written report is the one where findings were raised and nothing
// came back to judge them. The old `judged === 0` early return returned WITHOUT a report in exactly
// that case. One test governs now: anything still outstanding — confirmed or unverified — is
// synthesized. Only a fully-adjudicated, fully-refuted run exits here.
// S2: a refutation reached with dead skeptics is not a refutation. Carry the lens counts so a
// caller can tell "every finding was refuted" from "the verify stage was degraded".
// TOOL-dDerivedDocket-29 S5 - every agent label that did not return, lenses first, in dispatch order.
const pendingLabels = deadLensLabels.concat(deadBatchLabels)
if (confirmed.length + unverified.length === 0 && !isWalk) {
  // A REFUTATION OVER A PARTIAL FAN DEFERS. It used to return `… treat as partial` beside a null
  // count, which a caller had to parse prose to tell from the clean result on the line below it.
  const deferred = pendingLabels.length > 0
  const shapeLine = renderStageShape('verify', verifiedCounts, findersRunning + batches.length)
  log(shapeLine)
  const lensYield = deriveLensYield(ledger, null) // TOOL-aEvidencedLens-6 S4 - no synthesis, no items
  printLensYield(lensYield)
  return {
    identity,
    shape: shapeLine,
    exit: deferred ? 'deferred-platform' : 'complete', key: reviewKey, pending: pendingLabels, durable,
    // TOOL-dTieredTribunal-1 S3 - null, never 0. Every finding was refuted, which is a RESULT, but
    // no synthesis pass ran to adjudicate a blocker count, so there is none to report.
    confirmed: [], report: null, precision, root: repo, blockers: null, highs: null,
    lensesRun: liveResults.length, lensesDead, skepticsDead, unverified: 0, uncertain: 0, merged: merged.length,
    conflicts: conflicts.size, duplicates, spurious, lensesReused: reusedLens.size, batchesReused,
    note: deferred
      ? `DEFERRED: every finding raised was refuted, but ${lensesDead}/${findersRunning} lenses died — ${renderRerunTail(pendingLabels.join(', '), false)}`
      : 'all findings adjudicated and refuted',
    round, ...deriveRoundFields(deferred ? null : 0), priorFindings: priorFindings.length, intensity, optIn, ...(isSpec ? { preset } : {}), skippedLenses, twin: null,
    // TOOL-aSightedSkeptic-8 S5 - no report is written on this path (spec F3), so the return is the
    // only place this ledger and appendix exist; a caller may write them.
    ledger, confirmedFindings, appendix, lensYield, ...buildWalkFields(),
  }
}

// TOOL-dDerivedDocket-29 S5 - THE SYNTHESIS IS NOT RUN ON A PARTIAL FAN. A dead lens means a finding
// set that is incomplete, and a dead skeptic batch means findings nobody judged; either way the report
// would be rewritten by the re-run, and a report over a half-judged set is the one document that must
// not call the run finished. The BASE `PARTIAL` path returned an INTEGER `blockers` over exactly that
// set. Under `workerType: 'none'` every result that did come back is on disk under the key, so the
// re-run pays only for the dead; under a named type nothing is, and it pays for every judge again.
if (pendingLabels.length) {
  log(`WARNING: ${pendingLabels.length} agent(s) did not return (${pendingLabels.join(', ')}) — DEFERRED, and no synthesis runs over a partial set. ` +
    `The ${confirmed.length} confirmed and ${unverified.length} unverified finding(s) so far:`)
  for (const f of confirmed) log(`  CONFIRMED [${deriveBindingSeverity(f)}] lens=${f.lens} ${f.ref} - ${f.claim}`)
  for (const f of unverified) log(`  UNVERIFIED [${f.severity}] lens=${f.lens} ${f.ref} - ${f.claim}`)
  const shapeLine = renderStageShape('verify', verifiedCounts, findersRunning + batches.length)
  log(shapeLine)
  const lensYield = deriveLensYield(ledger, null) // TOOL-aEvidencedLens-6 S4/S5 - a dead lens's row reads returned: false
  printLensYield(lensYield)
  return {
    identity,
    shape: shapeLine,
    exit: 'deferred-platform', key: reviewKey, pending: pendingLabels, durable,
    root: repo, raw: allFindings.length, confirmed: confirmed.length, refuted: refuted.length, merged: merged.length,
    unverified: unverified.length, uncertain: uncertainFindings.length, conflicts: conflicts.size, duplicates, spurious, precision,
    lensesRun: liveResults.length, lensesDead, skepticsDead, lensesReused: reusedLens.size, batchesReused,
    report: null, summary: '', blockers: null, highs: null,
    note: `DEFERRED: ${lensesDead} lens(es) and ${skepticsDead} skeptic batch(es) did not return — ${renderRerunTail(pendingLabels.join(', '), false)}`,
    round, ...deriveRoundFields(null), priorFindings: priorFindings.length, intensity, optIn, ...(isSpec ? { preset } : {}), skippedLenses, twin: null,
    ledger, confirmedFindings, appendix, lensYield, ...buildWalkFields(), // TOOL-aSightedSkeptic-8 S5 - what was judged so far; `exit` says partial
  }
}

// --- Phase 3: SYNTHESIZE — one agent writes the report ------------------
// TOOL-aMendedFleet-18 S3/S4 - rendered BEFORE the synthesis, because that agent writes the record and
// this script cannot: the line the record copies and the line the final return carries are one string.
// Its `out-tokens` therefore excludes the synthesis agent's own spend (spec section 3).
const synthShape = renderStageShape('synth', verifiedCounts, findersRunning + batches.length + 1)
log(synthShape)
// TOOL-dFairHearing-17 S3/S4 - the count is the binding grades' blockers and highs, known before the synthesis
// (spec section 8 F2), so the record line it copies and the final return carry one state.
const synthRound = deriveRoundFields(verifiedCounts.blocker + verifiedCounts.high)
const roundLine = renderRoundLine({ round: round, roundLimit: roundLimit, priorCounts: priorCounts, roundCount: synthRound.roundCount, roundState: synthRound.roundState })
log(roundLine)
// TOOL-aEvidencedLens-6 S6 - the per-lens counts that exist before the synthesis, for its verbatim block.
const preSynthYield = deriveLensYield(ledger, null)
phase('Synthesize')
// TOOL-dFairHearing-18 S4/S5 - the walk's red is the harness's computed fact, and the agent states it.
const walkTableText = isWalk ? renderWalkTable(walk, walkRows) : ''
const synth = await agent(
  `Write the Tier-2 review report for: ${context}\n\n` +
    (walkGaps.length
      ? `WALK GAPS - the harness checked each walker's walk table against its slice, and the walk table has ${walkGaps.length} gap(s): ` +
        `a cell with no row or two, a row outside its slice, an empty field, or a malformed verdict. The walk is RED. The report ` +
        `lists each gap below FIRST, before any finding, and its \`## Verdict:\` token is BLOCKED.\n` +
        walkGaps.map((g) => `- ${renderPromptLine(g)}`).join('\n') + `\n\n`
      : '') +
    // TOOL-aSightedSkeptic-6 S6 - the bracket is the BINDING grade, and both grades follow it when the
    // skeptic's differs from the finder's.
    `CONFIRMED findings (survived an adversarial skeptic; the bracketed grade is BINDING):\n` +
    (confirmed.length
      ? confirmed
          .map((f) => {
            const g = deriveBindingSeverity(f)
            const grades = g !== f.severity
              ? ` (finder graded ${f.severity}, skeptic graded ${g})`
              : ungradedIds.indexOf(f.id) !== -1 ? ` (no skeptic grade - the finder's binds)` : ''
            // TOOL-dFairHearing-11 S7 - a twinned run names each confirmed finding's run.
            return `- id=${f.id} [${g}]${grades} lens=${f.lens}${twinned ? ' run=' + f.run : ''} ${f.ref} — ${f.claim}\n  impact: ${f.impact}\n  ${renderFixLine(f)}\n  why-real: ${verdictById.get(f.id)?.reason || ''}`
          })
          .join('\n')
      : '  (none)') +
    // TOOL-aSightedSkeptic-6 S8 - each UNVERIFIED finding says which of the two kinds it is.
    `\n\nUNVERIFIED findings (no confirmed or refuted verdict — OUTSTANDING, not cleared; read the code yourself before classifying each):\n` +
    (unverified.length
      ? unverified
          .map((f) => `- id=${f.id} [${f.severity}] lens=${f.lens} ${f.ref} — ${f.claim}\n  impact: ${f.impact}\n  fix: ${f.fix}\n  ` +
            (verdictById.get(f.id)?.verdict === 'uncertain'
              ? `status: UNCERTAIN - the skeptic could not establish it: ${verdictById.get(f.id).reason || '(no reason given)'}`
              : f.lens === 'cell-sample'
                ? `status: a CLEAN CELL a skeptic refuted (${f.cell}), raised by one skeptic and judged by none`
                : `status: NO USABLE VERDICT came back`))
          .join('\n')
      : '  (none)') +
    // TOOL-dFairHearing-7 S3 - under `shown` only, the refuted claims and the same-address pairs, so a refuted
    // twin of a confirmed finding can be flagged; a flag moves nothing. Every agent string through renderPromptLine.
    (addressTwins === 'shown'
      ? `\n\nREFUTED findings (refuted by an adversarial skeptic, and shown ONLY so a twin of a confirmed finding can be ` +
        `seen: none may be reinstated, regraded or counted):\n` +
        (refuted.length
          ? refuted.map((f) => `- id=${f.id} [${f.severity}] lens=${f.lens} ${f.ref} — ${renderPromptLine(f.claim)} | refuted because: ${renderPromptLine(verdictById.get(f.id).reason)}`).join('\n')
          : '  (none)') +
        `\n\nSAME-ADDRESS PAIRS (a confirmed and a refuted finding citing one address):\n` +
        (twinPairs.length
          ? twinPairs.map((p) => {
              const k = deriveAddressKey(confirmed.find((f) => f.id === p.confirmed))
              return `- confirmed id=${p.confirmed} and refuted id=${p.refuted}, both at ${k.file} ${k.at}`
            }).join('\n')
          : '  (none)') +
        `\n\nFor each pair above, and for any refuted finding whose claim reads as the same defect as a confirmed one, ` +
        `decide whether the two describe one defect. Where they do, note the refuted one as a twin beside the confirmed ` +
        `finding in the report and return the pair in \`twinFlags\` as {refuted, confirmed}. Two different defects at one ` +
        `address are not twins and get no flag. A flag changes no verdict, grade, item or count.`
      : '') +
    // TOOL-dFairHearing-11 S7 - THE TWIN MERGE, on a twinned run only, so an untwinned prompt is byte-identical.
    // A different block from the same-address twins above: those are one run's refuted twins, these two runs.
    (twinned
      ? `\n\nTWIN RUN - this review ran its finder lenses twice over one subject, as run a and run b, and each ` +
        `CONFIRMED finding above names its run. Merge the two runs into one report: make one item per defect, its ids ` +
        `from either run or both, so a defect both runs found is ONE item holding an id of each run.\n` +
        `CROSS-RUN CANDIDATE PAIRS (a confirmed finding of each run citing one address):\n` +
        (crossRunPairs.length
          ? crossRunPairs.map((p) => {
              const k = deriveAddressKey(confirmed.find((f) => f.id === p.a))
              return `- run a id=${p.a} and run b id=${p.b}, both at ${k.file} ${k.at}`
            }).join('\n')
          : '  (none)') +
        `\nA pair is a candidate only: where its two findings describe different defects, they are two items.`
      : '') +
    `\n\n` + SEVERITY_RUBRIC + ` ` +
    // TOOL-dFairHearing-6 S2 - one item per defect whatever its findings' grades: the grade is carried per id
    // in `grades`, so a mixed-grade defect no longer splits into one item per grade.
    `Each CONFIRMED finding's bracketed grade is its BINDING grade under this rubric. Make one item per defect: the ` +
    `findings on one defect form one item whatever their grades. Give each item \`grades\`, mapping each confirmed id it ` +
    `holds to the grade that id takes, its binding grade unless you judge another grade right, and then write the reason ` +
    `in the report beside that finding. Set the item's severity to the highest of its grades, and rank the report's items ` +
    `by that severity, blockers first.` +
    `\n\nWrite a markdown report (severity-ranked, blockers first, each with ${isSpec ? 'its file and section address' : 'file:line'} + fix + a left-shift gate suggestion) to a file under ${repo}/${reviewDir}. ` +
    // TOOL-aSightedSkeptic-2 S3 - a REJECTED fix never reaches the report as the fix.
    `Each CONFIRMED finding's fix line says whether a skeptic judged its fix. Where it is REJECTED, write the skeptic's ` +
    `corrected fix into the report, never the rejected one; where the note gives no correction, say the fix is still to be ` +
    `designed. Where it is NOT JUDGED, present it as the finder's proposal only. ` +
    // TOOL-dFairHearing-8 S2 - an instance-only fix, under `fixJudge: 'class'` alone.
    (fixJudge === 'class'
      ? `Where it is judged INSTANCE-ONLY, write the skeptic's class-level fix into the report as the fix, and name the ` +
        `finder's proposal as curing the cited instance alone; where the note gives no class-level fix, say the class fix is still to be designed. `
      : '') +
    // TOOL-aSightedSkeptic-7 S6 - the intensity, in the review-shape sentence, on every run.
    `State the review shape near the top — intensity ${intensity}, raw ${allFindings.length}, confirmed ${confirmed.length}, refuted ${refuted.length}, merged ${merged.length}, unverified ${unverified.length} (${uncertainFindings.length} uncertain), precision ${precision.toFixed(2)}. ` +
    // TOOL-aEvidencedLens-6 S6 - copied, as the appendix is, and not verified; the return holds the rows.
    `\n\nLENS YIELD - the table between the two marker lines below goes into the report directly after the review-shape ` +
    `sentence, copied VERBATIM: unedited, no row added, dropped, reordered or reworded, and neither marker line copied.\n` +
    `<<<LENS YIELD\n${renderLensYield(preSynthYield)}\nLENS YIELD>>>` +
    // TOOL-aWeldedTribunal-4 — RUN INTEGRITY. This harness computes every counter below and logged
    // them to stdout, which is not the record; the AGENT writes the record, so a run whose lenses
    // half died wrote a durable report that could not say so. The two drift-audit siblings were
    // given this block by TOOL-dTieredTribunal-3 and the reference harness they were copied from
    // was not. Class: memory/gotchas/degradation-known-but-unreported.md.
    //
    // THE TWO SENTENCES ARE THE POINT, not the numbers. A report that prints every counter and still
    // opens with "no issues found" has reported nothing, so the instruction not to call the run
    // complete and the clause that a zero is not evidence of absence both ship with the counts.
    //
    // `conflicts` is here and `downgrades` is not: this file computes the first (line ~434, findings
    // whose skeptics disagreed and were demoted to UNVERIFIED) and does not compute the second.
    // Interpolating a counter nothing derives would put an invented number in a durable record.
    `\n\nRUN INTEGRITY - state these in the report and do NOT describe this run as complete if any is non-zero:\n` +
    `lenses ${liveResults.length}/${findersRunning} returned, ${lensesDead} DIED; ` +
    `skeptic batches ${batches.length - skepticsDead}/${batches.length} returned, ${skepticsDead} DIED; ` +
    `${conflicts.size} contradictory verdict(s) demoted to unverified, ` +
    // TOOL-aEvidencedLens-3 S6 - TOOL-dFairHearing-5 S2/S4: on both kinds, the diff prompt's bytes moving here.
    `${orphanDuplicates.size} orphaned duplicate refutation(s) demoted to unverified, ` +
    `${merged.length} duplicate refutation(s) counted as merged confirmations, ` +
    `${spurious} spurious verdict(s) discarded, ${duplicates} duplicate(s); ` +
    // TOOL-aSightedSkeptic-2 S4 - how many confirmed fixes a skeptic actually judged.
    `fixes on confirmed findings: ${fixCounts.sound} judged sound, ${fixCounts.unsound} judged UNSOUND, ` +
    // TOOL-dFairHearing-8 S2 - the instance-only count, under `fixJudge: 'class'` alone.
    (fixJudge === 'class' ? `${fixCounts.instance} judged INSTANCE-ONLY, curing the cited instance and leaving its class standing, ` : '') +
    `${fixCounts.none} none proposed, ${unjudgedFixIds.length} NOT JUDGED - an unjudged fix is the finder's proposal and nothing more; ` +
    // TOOL-aSightedSkeptic-6 S5/S8 - the grades, and the two kinds of unverified finding, apart.
    `severity on confirmed findings: ${ungradedIds.length} UNGRADED by the skeptic (bound at the finder's grade), ` +
    `${skepticRegradedIds.length} RE-GRADED by the skeptic; ` +
    `unverified findings: ${uncertainFindings.length} answered UNCERTAIN by a skeptic, ${noVerdict.length} with NO usable verdict; ` +
    (notedLenses.length
      ? `lens notes supplied for: ${readNotes.length ? readNotes.join(', ') : 'no lens that ran'}` +
        (unreadNotes.length ? `; lens notes for skipped lenses, unread: ${unreadNotes.join(', ')}` : '') + `.\n`
      : `lens notes: none supplied, so every lens ran on the kit's generic brief.\n`) +
    // TOOL-aOrientedCast-5 S8 - a run where `roles` named a stage it reads says so; a classic run carries no clause.
    (roles[finderKey] || roles.skeptic || roles.synthesis
      ? `Roles: finders ${findType}, skeptic batches ${verifyType}, synthesis ${synthType}.\n`
      : '') +
    // TOOL-dFairHearing-2 S5 - spec kind only, so the report says which lens literal ran.
    (isSpec ? `preset: ${preset} - the ${preset} lenses ran: ${LENS_KEYS.join(', ')}.\n` : '') +
    // TOOL-dFairHearing-18 S2/S6 - the walk's run, its idle walker slots, the clean cells and the gaps; '' off the preset.
    (isWalk
      ? `walk: run ${walk.run} of ${walk.runs}, sliced by ${WALK_SLICING[walk.run - 1]}, seed ${walk.seed}; ${walkRows.length} cell(s); ` +
        (skippedLenses.length ? `walker slot(s) with no slice, so not dispatched: ${skippedLenses.join(', ')}` : 'every walker slot had a slice') +
        `; clean cells sampled ${cellsSampled}, refuted ${cellsRefuted}; walk gaps ${walkGaps.length}` +
        (walkGaps.length ? ' - the walk is RED' : '') + `.\n`
      : '') +
    // TOOL-dFairHearing-3 S5 - a run where a swap ran names each, and the default whose coverage it dropped.
    (swappedLenses.length
      ? `optIn: ${swappedLenses.map((L) => `${L.key} ran in the slot of ${L.replaces}`).join(', ')} - the replaced lens(es) did NOT run, so their classes went unswept.\n`
      : '') +
    // TOOL-aSightedSkeptic-7 S6 - a light run names every skipped lens; a full run carries no clause.
    (skippedLenses.length && !isWalk
      ? `Intensity: light - the ${skippedLenses.join(', ')} lens(es) were NOT run, so their classes were swept only ` +
        `through the checklist shares; do NOT describe this run as a full review.\n`
      : '') +
    // TOOL-aSightedSkeptic-3 S4 - where intent came from, stated on EVERY run.
    (SPECS.length
      ? `Intent: ${SPECS.length} spec document(s) supplied as \`specs\`${isSpec ? ', as sibling context' : ', beside the range\'s commit messages'}.\n`
      : a.context
        ? `Intent: no spec was supplied; \`context\` was the caller's statement${isSpec ? '' : ', beside the range\'s commit messages'}.\n`
        : `Intent: NEITHER \`specs\` nor \`context\` was supplied${isSpec ? '' : ', so the lenses had only the range\'s commit messages'} - the report must say so.\n`) +
    // TOOL-aSightedSkeptic-4 S4/S5 - which lens held which share, or that nothing was swept.
    (CHECKLIST_ITEMS.length
      ? `Checklist: ${CHECKLIST_ITEMS.length} item(s)${acquiredChecklist !== null ? `, acquired by the harness from --for-diff ${base}..${head}` : ''}, ` +
        `each assigned to exactly one of ${lensesRunning} lens(es): ` +
        runningLensKeys.map((k) => `${k} ${checklistShares[k].length}`).join(', ') + `.\n`
      // TOOL-dFairHearing-15 S3 - a checklist the agent did not hand over is named by its reason, never as absent.
      : `Checklist: NONE swept — ${checklistAbsence}; a zero count is not ` +
        `evidence the project's recurring bug classes are absent.\n`) +
    // TOOL-aGraftedHelix-3 S8 - where the by-design list came from, in the words the log used.
    `By design: ${byDesignSources.join('; ')}.\n` +
    // TOOL-aEvidencedLens-4 S6 - spec kind only: the move check, and at round > 1 how the fold text was named.
    (isSpec
      ? `move check: ` + (!probeLive
        ? 'the resume probe died, so no subject\'s current blob was checked.\n'
        : (movedSubjects.length ? movedSubjects.map((m) => `${m.path} MOVED from pinned ${m.blob} to ${m.now}`).join('; ') : 'no checked subject moved') +
          (uncheckedSubjects.length ? `; UNCHECKED, no usable current blob: ${uncheckedSubjects.join(', ')}` : '') + `.\n`) +
        (round > 1
          ? `fold diff: ${prevBlobCount} of ${subjects.length} subject(s) carried prevBlob` +
            (foldDegraded ? ` - a DEGRADED fold review: no priorFindings either, so nothing named the text the previous round's fixes introduced and every subject was reviewed whole` : '') + `.\n`
          : '')
      : '') +
    // TOOL-dFairHearing-7 S3 - what the twin blocks held, so a run that flagged nothing is told from one handed nothing.
    (addressTwins === 'shown' ? `refuted findings shown: ${refuted.length}; same-address pairs shown: ${twinPairs.length}.\n` : '') +
    // TOOL-dFairHearing-8 S4-S6 - what the disposition check below is handed, on every run.
    `dispositions: unclassed ${unclassed}; ${classSlugs.length} class slug(s) handed; ` +
    (legs ? `${legs.length} leg name(s) read from ${legManifest}.\n` : `no leg manifest was read from ${legManifest}, so every gate: disposition is refused.\n`) +
    `If lenses died, the finding set is INCOMPLETE and a zero count is not evidence of absence. ` +
    `Say so where you would otherwise call a zero positive evidence.\n\n` +
    // TOOL-dFairHearing-8 S6 - THE DISPOSITIONS, `review.report`'s grammar, the report step's to assign (spec section 8
    // F1). The harness checks what comes back against exactly what this block names.
    `DISPOSITIONS - give EVERY CONFIRMED finding above exactly one disposition, in one of these four forms, and return ` +
    `them as \`dispositions\`, one {id, disposition, reason} per confirmed id:\n` +
    `- class:<slug> - an instance of a recurring class this run was handed, <slug> being one of the class slugs below;\n` +
    `- gate:<leg> - a defect an existing gate leg should catch, <leg> being one of the leg names below, spelled exactly;\n` +
    `- new:<slug> - a recurring class no slug below names, <slug> matching ${CLASS_SLUG};\n` +
    `- none - nothing above homes it, with a non-empty reason, and only as the unclassed value admits.\n` +
    `unclassed: ${unclassed} - ` + (unclassed === 'refuse'
      ? 'none is refused: home every confirmed finding as class:, gate: or new:.'
      : unclassed === 'reason'
        ? 'none is admitted with a non-empty reason.'
        : 'none is admitted with a non-empty reason, and each id disposed none is raised for the owner to rule.') + `\n` +
    (classSlugs.length
      ? `Class slugs (${classSlugs.length}): ${classSlugs.join(', ')}.\n`
      : `Class slugs: none handed, as no checklist item is slug-led, so every class: disposition is refused.\n`) +
    (legs
      ? `Leg names (${legs.length}), one per line:\n` + legs.map((x) => `  - ${renderPromptLine(x)}`).join('\n') + `\n`
      : `Leg names: no leg manifest was read from ${legManifest}, so every gate: disposition is refused.\n`) +
    `A set that leaves a confirmed id with no disposition, gives one twice, names an id that is not confirmed, or uses a ` +
    `form or a name outside these is refused whole.\n\n` +
    // The range line is what the unattended kit's `closing-review-recorded` joins on, so the value
    // reaches the record without a human remembering to type it. HONEST LIMIT: `base` is required
    // but may still be a REF, and a caller who passes one at round 1 writes a line carrying no sha,
    // which satisfies nothing. The harness cannot tell whether a mandate is in force — it has no
    // filesystem and no repo access — so M8 spelling the invocation with the pinned sha is what
    // makes this work, and the failure surfaces as an unmet DoD item naming the run's own record.
    (isSpec
      // S9 - a spec audit has no range. Its anchor is the pinned blob per subject, which is what
      // makes "which rev was reviewed" answerable from the record instead of from recollection.
      // TOOL-dTrueNorth-13 S3 - the subjects line is the HARNESS'S literal, copied like the binding line:
      // the memory tree's pin grading reads its paths, so a word added to it reads as one more path.
      ? `The report's subjects line is the harness's value too, rendered from each subject's path and pinned ` +
        `blob: copy the line between the two marker lines below VERBATIM, alone on its own line, neither marker ` +
        `line copied and nothing added to it, and state the ROUND as ${round} on a line of its own after it.\n` +
        `<<<REVIEWED\n${renderReviewedLine(subjects)}\nREVIEWED>>>\n`
      : `Open the report with a line naming the reviewed range as ${baseSha}...${headSha}, and state the ROUND as ${round}. `) +
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
    // TOOL-dTieredTribunal-11 S8 - the kind token is the PARAMETER, not a hardcoded string. S1 closes
    // the legal set to two, and both are members of the memory tree's closed record-kind vocabulary,
    // so this token cannot leave that vocabulary without S1's refusal firing first.
    // TOOL-dTrueNorth-5 S1 - on the spec kind the line is the HARNESS'S value, rendered from each
    // subject's pin, and the agent copies it: an agent composing the id list cannot know the revision
    // each spec's header carried at its blob, and a prompt-held list did not hold under a merging
    // synthesis (the TOOL-dMergedTally-1 note below). The diff kind keeps its sentence.
    (isSpec
      ? `The report's FIRST line must be the record's binding line, which the harness rendered from each ` +
        `subject's pinned revision: copy the line between the two marker lines below VERBATIM, alone on its ` +
        `own line, neither marker line copied, and add, drop or reorder no id on it.\n` +
        `<<<SERVES\n${renderAuditBinding(subjects)}\nSERVES>>>\n`
      : `The report's FIRST line must be the record's binding line, exactly: **Serves:** ${kind} ` +
        `followed by every unit id in the diff, space-separated. A kind with no id is malformed under the ` +
        `project's record-binding grammar, so never emit the kind alone. `) +
    // TOOL-dMergedTally-1 - THE AGENT RETURNS IDS AND THIS FILE COUNTS THEM. TOOL-dTieredTribunal-1
    // S5 defined `blockers` and `highs` as the CONFIRMED findings at each severity and had the agent
    // type both integers, and its own note said the agreement was a property of this prompt and not
    // of a mechanism. The prompt did not hold: a synthesis that MERGES several raw findings into one
    // adjudicated item counts ITEMS, while `confirmed` counts RAW findings and the build harness's
    // disposal guard subtracts one from the other. Measured on dLoggedFlight's round-1 spec audit of
    // units 14 and 15: 13 confirmed merged into 10 items came back as blockers 1 and highs 5 against
    // a raw split of 3 and 6, so the guard demanded 7 folds of 4 raw MEDIUMs and no honest disposal
    // could pass. The sentence already said CONFIRMED findings, so rewording it is the fix that had
    // already failed. The item list below carries the raw ids, and the counts are derived from it.
    `Return \`items\`, one entry per item AS YOU ADJUDICATED IT in the report: \`severity\` is ` +
    `BLOCKER, HIGH, MEDIUM or LOW, and \`ids\` lists the integer id of every CONFIRMED finding that ` +
    `item covers, and \`grades\` maps each of those ids, as a string key, to the BLOCKER, HIGH, MEDIUM or ` +
    `LOW grade it takes. When you merge several findings into one item, that item lists all of their ids. ` +
    `Every CONFIRMED id above appears in EXACTLY ONE item; an UNVERIFIED id you list is not counted. ` +
    `The harness counts \`blockers\` and \`highs\` from the per-id grades in \`grades\`, so both count ` +
    `RAW confirmed findings and never items, and a list that leaves a confirmed ` +
    `id out or names one twice returns neither count. In the review shape, state the adjudicated ` +
    `tally BOTH ways, by item and by raw confirmed finding, so the table you wrote and the ids you ` +
    `return agree. ` +
    // TOOL-dFoldedAudit-5 S1 - THE ADDRESS, on a spec subject alone. A spec audit's chain stops when every
    // high sits in the previous round's own work, which cannot be derived from a record naming no spec a
    // high would change. A diff review has no such chain, so its prompt holds no byte of this, and neither
    // does an undeclared spec audit's (TOOL-dFoldedAudit-15 S8).
    (addressOwed
      ? `On each BLOCKER or HIGH item also return \`specs\`, the unit ids whose spec the item's fix would ` +
        `change, naming every one of them, because a narrower list can stop the audit's chain early. In the ` +
        `report, put one line directly under each BLOCKER or HIGH item, exactly \`**Specs:** <unit id> <unit id>\`, ` +
        `listing the same ids. A BLOCKER or HIGH item holding a confirmed id with no well-formed \`specs\` ` +
        `returns neither count. `
      : '') +
    // TOOL-aSightedSkeptic-8 S7 - the harness renders the appendix and the agent only copies it: a
    // table composed from these lines would miss every refuted finding, which no line above shows.
    // The copy is NOT verified here (spec F2); the return's `appendix` holds the exact text.
    // TOOL-aMendedFleet-18 S4 - the shape line rides the same copy instruction; the return's `shape` holds it.
    `\n\nREVIEW-SHAPE LINE - copy the review-shape line between the two marker lines below VERBATIM, alone on its own line, immediately above the appendix heading, and neither marker line copied.\n` +
    `<<<SHAPE\n${synthShape}\nSHAPE>>>` +
    // TOOL-dFairHearing-17 S4 - the round line rides the same copy instruction; the return's `roundState` holds it.
    `\n\nREVIEW-ROUND LINE - copy the review-round line between the two marker lines below VERBATIM, alone on its own line, ` +
    `directly below the review-shape line, and neither marker line copied.\n<<<ROUND\n${roundLine}\nROUND>>>` +
    // TOOL-dFairHearing-11 S7 - the twin record line rides beside the shape line, copied the same way.
    (twinned
      ? `\n\nREVIEW-TWIN LINE - copy the review-twin line between the two marker lines below VERBATIM, alone on its own line, ` +
        `directly below the review-shape line, and neither marker line copied.\n<<<TWIN\n${twinLine}\nTWIN>>>`
      : '') +
    // TOOL-dFairHearing-18 S5 - the walk table rides the same copy instruction, directly before the appendix; the
    // return's `walkTable` holds its rows, and the copy is not verified, as the appendix's is not.
    (isWalk
      ? `\n\nWALK TABLE - the block between the two marker lines below goes into the report directly BEFORE the appendix, ` +
        `copied VERBATIM: unedited, no row added, dropped, reordered or reworded, and neither marker line copied.\n` +
        `<<<WALK TABLE\n${walkTableText}\nWALK TABLE>>>`
      : '') +
    // TOOL-dFairHearing-8 S8 - the one exception to the copy: each `(synthesis)` cell, written with its disposition.
    (synthAppendix
      ? `\n\nAPPENDIX - the report's LAST section, after everything else, is the text between the two marker lines ` +
        `below, copied VERBATIM: unedited, no row added, dropped, reordered or reworded, and neither marker line copied. ` +
        `The one exception is each \`(synthesis)\` cell of the disposition column: write it as the disposition you return ` +
        `for that row's id, a none as \`none — <reason>\`.\n` +
        `<<<APPENDIX\n${synthAppendix}\nAPPENDIX>>>\n\n`
      : '') +
    `Return JSON {path, items, summary${addressTwins === 'shown' ? ', twinFlags' : ''}} with a FORWARD-SLASH path, and ` +
    `\`dispositions\` beside them as the DISPOSITIONS block asks.`,
  {
    ...synthOpts,
    label: renderAgentLabel(reviewScope, 'synth'),
    phase: 'Synthesize',
    schema: {
      type: 'object',
      // TOOL-dTieredTribunal-1 S1 - the counts were requested and schemad from the start and were
      // never required and never read. Requiring the field they come from is what makes a synthesis
      // that omits it fail loudly at validation instead of returning a partial object nobody notices.
      // TOOL-dMergedTally-1 - that field is `items` now; the two integers are derived below.
      // TOOL-dFairHearing-7 S3 - `twinFlags` joins the schema under `addressTwins: 'shown'` alone.
      // TOOL-dFairHearing-8 S6 - `dispositions` is required on every run; the check below grades its members.
      required: ['path', 'summary', 'items', 'dispositions', ...(addressTwins === 'shown' ? ['twinFlags'] : [])],
      properties: {
        path: { type: 'string' },
        dispositions: { type: 'array', items: { type: 'object', required: ['id', 'disposition'],
          properties: { id: { type: 'integer' }, disposition: { type: 'string' }, reason: { type: 'string' } } } },
        ...(addressTwins === 'shown'
          ? { twinFlags: { type: 'array', items: { type: 'object', required: ['refuted', 'confirmed'], properties: { refuted: { type: 'integer' }, confirmed: { type: 'integer' } } } } }
          : {}),
        items: {
          type: 'array',
          items: {
            type: 'object',
            // TOOL-dFairHearing-6 S1 - `grades` maps each confirmed id to its grade. Typed only as an object,
            // as no schema in this kit uses an `additionalProperties` map; the tally checks each entry.
            required: ['severity', 'ids', 'grades'],
            properties: {
              severity: { type: 'string', enum: ['BLOCKER', 'HIGH', 'MEDIUM', 'LOW'] },
              ids: { type: 'array', items: { type: 'integer' } },
              grades: { type: 'object' },
              // TOOL-dFoldedAudit-5 S1 - optional, because this object is shared with the diff kind, whose
              // schema stays as it was. The tally below is what requires it, on a BLOCKER or HIGH item.
              ...(addressOwed ? { specs: { type: 'array', items: { type: 'string' } } } : {}),
            },
          },
        },
        summary: { type: 'string' },
      },
    },
  },
)

// TOOL-dMergedTally-1 - THE COUNTS, DERIVED OVER RAW CONFIRMED IDS. Each confirmed id must sit in
// exactly one item. A missing id or a repeated one leaves the synthesis's split unknowable, and
// guessing it is an adjudication this file has no standing to make: taking the higher severity of a
// repeat would promote a finding the report folded, and dropping a missing one would fold a finding
// nobody graded. Both counts are then null, the stated absence the callers already refuse, and the
// note below names the ids. An id that is not confirmed is ignored: the prompt permits UNVERIFIED
// ones, and neither count is defined over anything else.
//
// TOOL-dFoldedAudit-5 S2 and S3 - ON A SPEC SUBJECT UNDER A DECLARED `disposal`, A BLOCKER OR HIGH ITEM
// HOLDING A CONFIRMED ID CARRIES ITS ADDRESS, and one with no well-formed `specs` is a tally fault: the path
// a misplaced id takes, so both counts go null and the build harness refuses the stated absence. Only the
// SHAPE is tested, the id grammar, because this file holds the subjects alone and a high may name an older
// spec; the harness tests the roster. `addresses` is `[]` wherever the tally did not accept the items, and
// on every undeclared spec audit.
let blockers = null
let highs = null
let tallyFault = ''
let addresses = []
const regraded = []
const twinFlags = []
if (synth) {
  const confirmedIds = new Set(confirmed.map((f) => f.id))
  const severityById = new Map()
  const repeated = new Set()
  const addressed = []
  const unaddressed = []
  const perItem = { BLOCKER: 0, HIGH: 0, MEDIUM: 0, LOW: 0 }
  const perRaw = { BLOCKER: 0, HIGH: 0, MEDIUM: 0, LOW: 0 }
  // TOOL-dFairHearing-6 S3 and S4 - each confirmed id is placed at its OWN grade from the item's `grades`;
  // one with no legal grade there takes the item's severity and is named. An item whose severity is not
  // the highest grade it placed is named too, and the counts stay per id. SEVERITIES ranks the four,
  // highest first.
  const gradesDefaulted = []
  const itemsMisranked = []
  // The severity is tested against the closed list. An unknown one skips its item, so its ids surface
  // as unplaced rather than counting as placed while moving neither count. Case is folded because the
  // finders' own schema spells the same four words in lowercase.
  for (const it of Array.isArray(synth.items) ? synth.items : []) {
    const sev = it ? String(it.severity).toUpperCase() : ''
    if (['BLOCKER', 'HIGH', 'MEDIUM', 'LOW'].indexOf(sev) === -1) continue
    let holdsConfirmed = false
    let first = null
    let top = 'LOW'
    for (const id of Array.isArray(it.ids) ? it.ids : []) {
      if (!confirmedIds.has(id)) continue
      if (!holdsConfirmed) first = id
      holdsConfirmed = true
      let grade = String(it.grades[String(id)]).toUpperCase()
      if (SEVERITIES.indexOf(grade.toLowerCase()) === -1) {
        grade = sev
        gradesDefaulted.push(id)
      }
      if (SEVERITIES.indexOf(grade.toLowerCase()) < SEVERITIES.indexOf(top.toLowerCase())) top = grade
      if (severityById.has(id)) repeated.add(id)
      else severityById.set(id, grade)
    }
    if (holdsConfirmed) perItem[sev]++
    if (holdsConfirmed && top !== sev) itemsMisranked.push(first)
    if (addressOwed && holdsConfirmed && (sev === 'BLOCKER' || sev === 'HIGH')) {
      const held = it.ids.filter((id) => confirmedIds.has(id))
      if (Array.isArray(it.specs) && it.specs.length && it.specs.every((s) => typeof s === 'string' && PIN_ID.test(s)))
        addressed.push({ ids: held, severity: sev, specs: it.specs })
      else unaddressed.push(...held)
    }
  }
  if (gradesDefaulted.length)
    log(`WARNING: the synthesis gave ${gradesDefaulted.length} confirmed finding(s) no legal grade in their item's grades — placed at the item's severity: ids ${gradesDefaulted.join(', ')}`)
  if (itemsMisranked.length)
    log(`WARNING: ${itemsMisranked.length} synthesis item(s) carry a severity other than the highest grade they place — counts read the per-id grades: items holding ids ${itemsMisranked.join(', ')}`)
  const missing = [...confirmedIds].filter((id) => !severityById.has(id))
  if (missing.length || repeated.size || unaddressed.length) {
    tallyFault =
      (missing.length ? `confirmed id(s) ${missing.join(', ')} sit in no item` : '') +
      (missing.length && repeated.size ? '; ' : '') +
      (repeated.size ? `confirmed id(s) ${[...repeated].join(', ')} sit in more than one item` : '') +
      ((missing.length || repeated.size) && unaddressed.length ? '; ' : '') +
      (unaddressed.length ? `BLOCKER or HIGH id(s) ${unaddressed.join(', ')} carry no well-formed \`specs\`` : '')
    log(`WARNING: the synthesis item list does not place every confirmed finding exactly once — ${tallyFault}. blockers and highs are NULL.`)
  } else {
    for (const sev of severityById.values()) perRaw[sev]++
    blockers = perRaw.BLOCKER
    highs = perRaw.HIGH
    addresses = addressed
    log(`adjudicated BLOCKER/HIGH/MEDIUM/LOW — by item ${perItem.BLOCKER}/${perItem.HIGH}/${perItem.MEDIUM}/${perItem.LOW}, ` +
      `by raw confirmed finding ${perRaw.BLOCKER}/${perRaw.HIGH}/${perRaw.MEDIUM}/${perRaw.LOW}`)
  }
  // TOOL-aSightedSkeptic-6 S7 - the counts above stay derived from the items (spec section 8 F2); a
  // placement off the binding grade is reported, never a tally fault and never silently re-counted.
  for (const f of confirmed)
    if (severityById.has(f.id) && severityById.get(f.id) !== String(deriveBindingSeverity(f)).toUpperCase()) regraded.push(f.id)
  if (regraded.length)
    log(`WARNING: the synthesis placed ${regraded.length} confirmed finding(s) at a grade other than their binding one: ids ${regraded.join(', ')}`)
  // TOOL-dFairHearing-7 S4/S5 - a flag is KEPT when its refuted id stands refuted and its confirmed id confirmed,
  // a repeat dropped, and marked `sameAddress` when deriveTwinPairs handed that pair; every other flag is
  // discarded and named. Read after the tally and by nothing it feeds, so no flag moves a verdict or a count.
  if (addressTwins === 'shown') {
    const refutedIds = new Set(refuted.map((f) => f.id))
    const handed = new Set(twinPairs.map((p) => p.refuted + '/' + p.confirmed))
    const discarded = []
    for (const fl of Array.isArray(synth.twinFlags) ? synth.twinFlags : []) {
      const pair = (fl ? fl.refuted : fl) + '/' + (fl ? fl.confirmed : fl)
      if (!fl || !refutedIds.has(fl.refuted) || !confirmedIds.has(fl.confirmed)) discarded.push(pair)
      else if (!twinFlags.some((k) => k.refuted === fl.refuted && k.confirmed === fl.confirmed))
        twinFlags.push({ refuted: fl.refuted, confirmed: fl.confirmed, sameAddress: handed.has(pair) })
    }
    if (discarded.length)
      log(`WARNING: ${discarded.length} twin flag(s) named an id that is not refuted or not confirmed — discarded: ${discarded.join(', ')}`)
  }
}

// TOOL-dFairHearing-8 S7 - THE DISPOSITION CHECK, after the tally, over confirmed ids only. One disposition's fault,
// '' when it is legal: `class:` a handed slug, `gate:` a handed leg name, `new:` a slug in the grammar that is no handed
// slug, or `none` where `unclassed` admits it, with a non-empty reason.
const NEW_SLUG = new RegExp('^' + CLASS_SLUG + '$')
function checkDisposition(d) {
  const s = typeof d.disposition === 'string' ? d.disposition : ''
  const at = s.indexOf(':')
  const form = at === -1 ? s : s.slice(0, at)
  const name = at === -1 ? '' : s.slice(at + 1)
  const said = JSON.stringify(d.disposition)
  if (s === 'none') return unclassed === 'refuse' ? 'is none, which unclassed refuse does not admit'
    : typeof d.reason === 'string' && d.reason.trim() ? '' : 'is none with an empty reason'
  if (form === 'class') return classSlugs.indexOf(name) !== -1 ? '' : `is ${said}, and ${JSON.stringify(name)} is no class slug this run handed`
  if (form === 'gate') return !legs ? `is ${said}, and no leg manifest was read, so no gate: disposition is legal`
    : legs.indexOf(name) !== -1 ? '' : `is ${said}, and ${JSON.stringify(name)} is no leg of ${legManifest}`
  if (form === 'new') return !NEW_SLUG.test(name) ? `is ${said}, and ${JSON.stringify(name)} is no slug matching ${CLASS_SLUG}`
    : classSlugs.indexOf(name) !== -1 ? `is ${said}, a handed class slug, so it is class:${name}` : ''
  return `is ${said}, outside the forms class:<slug> | gate:<leg> | new:<slug> | none`
}
// The set is accepted whole or refused whole (spec section 8 F3): refused, `dispositions` is null and every failing id
// is named in `dispositionFault`, while `blockers` and `highs` keep the tally's derivation above. No synthesis, no set.
let dispositions = null
let dispositionFault = ''
let ownerItems = []
if (synth) {
  const confirmedIds = new Set(confirmed.map((f) => f.id))
  const byId = new Map()
  const faults = Array.isArray(synth.dispositions) ? [] : ['no dispositions list was returned']
  for (const d of Array.isArray(synth.dispositions) ? synth.dispositions : []) {
    const id = d && typeof d === 'object' ? d.id : d
    if (!confirmedIds.has(id)) faults.push(`id ${JSON.stringify(id)} is not a confirmed id`)
    else if (byId.has(id)) faults.push(`id ${id} is disposed more than once`)
    else {
      byId.set(id, d)
      const why = checkDisposition(d)
      if (why) faults.push(`id ${id} ${why}`)
    }
  }
  for (const f of confirmed) if (!byId.has(f.id)) faults.push(`id ${f.id} has no disposition`)
  if (faults.length) {
    dispositionFault = faults.join('; ')
    log(`WARNING: the synthesis dispositions were REFUSED — ${dispositionFault}. dispositions is NULL; blockers and highs stand.`)
  } else {
    dispositions = confirmed.map((f) => ({ id: f.id, disposition: byId.get(f.id).disposition,
      reason: typeof byId.get(f.id).reason === 'string' ? byId.get(f.id).reason : '' }))
    ownerItems = unclassed === 'owner-rules' ? dispositions.filter((x) => x.disposition === 'none').map((x) => x.id) : []
    log(`dispositions: ${dispositions.length} confirmed finding(s) disposed, unclassed ${unclassed}` +
      (ownerItems.length ? ` — ${ownerItems.length} none raised for the owner: ids ${ownerItems.join(', ')}` : ''))
  }
}
// S8 - an accepted set reaches the ledger, the confirmed set and the appendix, a `none` cell as `none — <reason>`.
const dispositionById = new Map((dispositions || []).map((x) => [x.id, x]))
for (const e of ledger.concat(confirmedFindings)) if (dispositionById.has(e.id)) e.disposition = dispositionById.get(e.id).disposition
const returnedAppendix = !dispositions ? appendix : renderAppendix(ledger.map((e) => {
  const x = dispositionById.get(e.id)
  return x && x.disposition === 'none' ? Object.assign({}, e, { disposition: 'none — ' + x.reason }) : e
}))

// TOOL-aBoundedVerdict-14 S6 - the SYNTH-DEATH hole. Lens deaths and skeptic deaths are both counted
// and reported; a dead synthesis was not, so `synth === null` returned report:null with a note reading
// `complete` and every confirmed finding was lost with nothing logged. The findings exist here in
// memory - the only thing missing was saying so before the return threw them away.
// TOOL-dDerivedDocket-29 - and the findings are ALSO on disk now: every lens and batch that returned
// wrote its file under the key, so a re-run reuses all of them and dispatches the synthesis alone -
// under `workerType: 'none'` only; under a named type none wrote one (TOOL-aMendedFleet-111 S6).
if (!synth) {
  log(`WARNING: the synthesis agent DIED. No report was written, and the ${confirmed.length} confirmed finding(s) below are in this log${durable ? ` and in ${keyDir}` : ''}; ${durable ? 'a re-run with identical args dispatches only the synthesis' : renderRerunTail('', true)}:`)
  for (const f of confirmed)
    log(`  CONFIRMED [${deriveBindingSeverity(f)}] lens=${f.lens} ${f.ref} - ${f.claim} | ${renderFixLine(f)}`)
  for (const f of unverified) log(`  UNVERIFIED [${f.severity}] lens=${f.lens} ${f.ref} - ${f.claim}`)
}

// TOOL-dFairHearing-11 S7 - THE TWIN FIGURES, derived from the items and only over a list the tally accepted,
// so an unplaced id nulls `twin` rather than skewing `agreed`. Each counts ITEMS: `agreed` holds a confirmed id
// of each run, `onlyA` and `onlyB` of one run alone. `a` and `b` list each run's confirmed ids.
function deriveTwinFigures(items) {
  const runOf = new Map(confirmed.map((f) => [f.id, f.run]))
  const n = { agreed: 0, onlyA: 0, onlyB: 0 }
  for (const it of items) {
    const runs = new Set((it && Array.isArray(it.ids) ? it.ids : []).filter((id) => runOf.has(id)).map((id) => runOf.get(id)))
    if (runs.size === 2) n.agreed++
    else if (runs.has('a')) n.onlyA++
    else if (runs.has('b')) n.onlyB++
  }
  return { a: confirmed.filter((f) => f.run === 'a').map((f) => f.id), b: confirmed.filter((f) => f.run === 'b').map((f) => f.id),
    agreed: n.agreed, onlyA: n.onlyA, onlyB: n.onlyB }
}
const twinFigures = twinned && synth && !tallyFault ? deriveTwinFigures(Array.isArray(synth.items) ? synth.items : []) : null
if (twinFigures)
  log(`twin: run a ${twinFigures.a.length} confirmed, run b ${twinFigures.b.length} confirmed — items agreed ${twinFigures.agreed}, only a ${twinFigures.onlyA}, only b ${twinFigures.onlyB}`)
// TOOL-aEvidencedLens-6 S4 - defects and unique only over an item list the tally accepted.
const lensYield =deriveLensYield(ledger, synth && !tallyFault ? synth.items || [] : null)
printLensYield(lensYield)
// H1: the SUCCESS return carries the same trust counts as the early ones. A caller that only ever
// sees {confirmed, precision} cannot tell a full review from one where half the lenses died.
// TOOL-dDerivedDocket-29 S5 - past the partial-fan return above, the synthesis is the only agent left
// that can have died, so it alone decides `exit` here. The tally fault stays `complete`.
return {
  identity,
  shape: synthShape, // TOOL-aMendedFleet-18 S3 - the line handed to the synthesis, unchanged
  exit: synth ? 'complete' : 'deferred-platform',
  key: reviewKey,
  pending: synth ? [] : ['synth'],
  durable,
  lensesReused: reusedLens.size,
  batchesReused,
  root: repo,
  raw: allFindings.length,
  confirmed: confirmed.length,
  refuted: refuted.length,
  merged: merged.length,
  unverified: unverified.length,
  uncertain: uncertainFindings.length,
  conflicts: conflicts.size,
  duplicates,
  spurious,
  precision,
  lensesRun: liveResults.length,
  lensesDead,
  skepticsDead,
  agents: findersRunning + batches.length + 1, // finders + batched skeptics + synth
  report: synth?.path || null,
  summary: synth?.summary || '',
  // TOOL-dTieredTribunal-1 S2/S3b - the counts the synthesis pass adjudicated, returned rather than
  // dropped: an integer when a synthesis ran, null when none did, never a fabricated 0 and never an
  // absent key. TOOL-dMergedTally-1 - both are derived above from the item list, over RAW confirmed
  // ids, and are null as well when that list does not place every confirmed id exactly once.
  blockers,
  highs,
  // TOOL-dFoldedAudit-5 S3 - one `{ids, severity, specs}` per BLOCKER or HIGH item, on a spec subject only.
  ...(isSpec ? { addresses } : {}),
  // TOOL-aSightedSkeptic-6 S7 - absent where no synthesis ran, as no adjudicated count exists there.
  ...(synth ? { regraded } : {}),
  // TOOL-dFairHearing-7 S4 - under `shown` alone: the pairs handed and the flags kept, `[]` when none or no synthesis.
  ...(addressTwins === 'shown' ? { twinPairs: twinPairs.length, twinFlags } : {}),
  // TOOL-dFairHearing-11 S7 - null on an untwinned run, and where the tally refused the items or no synthesis ran.
  twin: twinFigures,
  // TOOL-dFairHearing-8 S7 - the checked set, null when refused or when no synthesis ran; the fault, '' when none;
  // and the ids disposed `none` under `unclassed: 'owner-rules'`, [] otherwise.
  dispositions,
  dispositionFault,
  ownerItems,
  // TOOL-dTieredTribunal-1, closing-review D1 - a dead synthesis was tested LAST, so it was
  // reportable only when nothing else was degraded and the most serious note was the least reachable
  // one. Worst outcome first. Found by the closing review of the build that ported this ternary into
  // the two drift-audit siblings, where the same ordering had been copied.
  // TOOL-dFairHearing-8 S7 - a refused disposition set says so after whichever note the run earned.
  note: (
    // Lens and skeptic deaths never reach this return (TOOL-dDerivedDocket-29), so the last two arms
    // speak of UNUSABLE verdicts: a batch that returned with an id missing, spurious or contradicted.
    !synth
      ? `DEFERRED: the synthesis agent died, so NO report was written; ${confirmed.length} confirmed finding(s) are in the run log${durable ? ' and on disk' : ''} — ${durable ? 're-run with identical args to dispatch only the synthesis' : renderRerunTail('', true)}`
      : tallyFault
        ? `UNVERIFIED: the report was written, but its item list does not place every confirmed finding exactly once (${tallyFault}), so blockers and highs are null`
        // TOOL-aSightedSkeptic-6 S8 - the uncertain count apart from the no-verdict count, so a run whose
        // skeptics all answered never reads as one where none returned.
        // TOOL-dFairHearing-18 S6 - a walk whose walkers raised nothing has nothing to judge, so it falls through to the
        // arms below, and a refuted clean cell reads as the unverified finding it is.
        : allFindings.length > cellFindings.length && judged === 0 && !uncertainFindings.length
          ? `UNVERIFIED: ${allFindings.length} finding(s) raised, none judged — no skeptic batch returned a usable verdict — the report lists them as outstanding`
          : allFindings.length > cellFindings.length && judged === 0
            ? `UNVERIFIED: ${allFindings.length} finding(s) raised, none confirmed or refuted — ${uncertainFindings.length} answered uncertain by a skeptic, ${noVerdict.length} with no usable verdict — the report lists them as outstanding`
            : unverified.length
              ? `PARTIAL: ${unverified.length} finding(s) are unverified — ${uncertainFindings.length} answered uncertain by a skeptic, ${noVerdict.length} with no usable verdict`
              : 'complete') +
    (dispositionFault ? `; the DISPOSITIONS were refused (${dispositionFault}), so dispositions is null and blockers and highs stand` : ''),
  round,
  // TOOL-dFairHearing-17 S3 - the state the record line carries, both null where the synthesis died.
  ...(synth ? synthRound : deriveRoundFields(null)),
  priorFindings: priorFindings.length,
  // TOOL-aSightedSkeptic-7 S6 - on every exit path, so a light run is never read as a full one.
  intensity,
  // TOOL-dFairHearing-3 S5 - beside `intensity` on every exit path, the swaps the caller asked for; {} when none.
  optIn,
  // TOOL-dFairHearing-2 S5 - beside `intensity` on every exit path of the spec kind, which lens literal ran.
  ...(isSpec ? { preset } : {}),
  skippedLenses,
  // TOOL-aSightedSkeptic-8 S5 - every finding and its verdict, the confirmed set as round N+1's
  // `priorFindings`, and the appendix the synthesis was told to copy, for a caller to compare.
  // TOOL-dFairHearing-8 S8 - each carrying the accepted dispositions, or `-` in every cell when none was accepted.
  ledger,
  confirmedFindings,
  appendix: returnedAppendix,
  // TOOL-aEvidencedLens-6 S5 - on every return; README "return fields" states the row shape.
  lensYield,
  // TOOL-dFairHearing-18 S5/S6 - on a whole-design run: the joined walk table's rows, its gaps, and the clean cells
  // handed to the skeptics and refuted by them.
  ...buildWalkFields(),
}

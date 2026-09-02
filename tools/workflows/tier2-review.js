export const meta = {
  name: 'tier2-review',
  version: '1.5', // gov:kit tier2-review@1.5 // gov:kit review-harness@1.5 — BOTH ids: the
  // second is this entry's REGISTRY id, and without it a deployer grepping the id the
  // registry uses finds nothing. DEPL-dGaugedVintage-5. — engine identity (deployed verbatim; this field is the deployer's version marker)
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
//   reviewDir: "where synth writes the report (repo-relative)",
//   kind: "diff-review" | "spec-audit",   // DEFAULTS to "diff-review" when absent
//   subjects: [{ path, blob }],           // spec-audit ONLY; blob is 7-40 hex, per subject
//   round: <integer>,                     // inferred as 2 when priorFindings arrive without one
//   priorFindings: [ ... ] }              // a previous round's confirmed set
// D9 - `kind` and `subjects` were added without extending this block, and BUILD-METHOD M4 sends a
// reader HERE for the spec-audit spelling. An absent `kind` does not refuse - it defaults - so a
// header missing the field buys exactly the failure M4 exists to prevent: a code-shaped review of a
// spec, reported as a review. A pointer is only as true as the block it points at, and this one is
// asserted against the fields actually read, in tools/workflows/tier2-review.test.sh.
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
// S7 - the context default is per-kind, and each is wrong if the other kind inherits it.
const context = a.context || (isSpec ? 'the spec set under audit' : 'the cumulative diff landing on main')
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
      'tier2-review: a spec-audit needs `subjects`, a non-empty array of {path, blob}, where blob is ' +
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
}
const baseLooksPinned = isSpec || PINNED_SHA.test(String(base))
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
log(`review root (unverified — see note): ${repo} — ${kind} — ` +
  (isSpec ? `${subjects.length} subject(s)` : `diff ${base}...${head}`))

// TOOL-dTieredTribunal-11 S3 - two SIBLING schemas, not one loosened schema. A spec finding is often
// the ABSENCE of a line, so it addresses a section; making `line` merely optional on a shared schema
// would buy the spec kind an address by removing the diff kind's, and the charter requires a finder
// to emit a concrete address on both.
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

// S3 - the spec kind's schema. `where` replaces `line` and is REQUIRED, so the address obligation is
// machine-enforced on both kinds rather than relaxed on one.
const SPEC_FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'findings'],
  properties: {
    lens: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['file', 'where', 'severity', 'claim', 'impact', 'fix'],
        properties: {
          file: { type: 'string' },
          where: { type: 'string' },
          severity: { type: 'string', enum: ['blocker', 'high', 'medium', 'low'] },
          claim: { type: 'string' },
          impact: { type: 'string' },
          fix: { type: 'string' },
        },
      },
    },
  },
}

// --- Phase 1: FIND — one wave of primed lenses, at the width boundedParallel defaults to ----
// TOOL-dTieredTribunal-11 S11: this said `ONE <=6-wide wave` while the helper above defaults to
// the file constant and the meta line said <=5 concurrent. Three carriers, two numbers, and the
// code fanned at neither six nor a spelled digit. No digit is written here now: the width is
// whatever `boundedParallel`'s default parameter resolves to, which is the one place that owns
// it. Closes TOOL-aDeclaredBound-6, whose own row cites the wrong line for this text.
phase('Find')
const DIFF_LENSES = [
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

// TOOL-dTieredTribunal-11 S2 - the M4 spec-audit catalogue, COPIED from tools/memory-tree/README.md
// rather than re-invented, so the method and the engine cannot drift into two answers.
const SPEC_LENSES = [
  {
    key: 'underspecification',
    brief:
      'Underspecification: which section-2 item has no section-6 criterion, and which section-6 criterion names no observation that could fail.',
  },
  {
    key: 'contradiction',
    brief:
      'Contradiction: section 2 against section 3; a sub-spec against the main spec on the four axes scope, interface, ordering and acceptance; section 4 Design against section 7 Gates.',
  },
  {
    key: 'unstated-assumption',
    brief:
      'Unstated assumption: what must be true of existing code for section 4 to work that section 4 never says and section 10 never checked.',
  },
  {
    key: 'prior-art',
    brief:
      'Prior art: has a record already decided this? That is the recall probe — search the decision logs, the backlog shards and the build records before accepting a design as new.',
  },
]

// The ONE dialect tools/hooks/agent-cap.js admits here: two sibling top-level array literals and a
// marked ternary. A map, object or registry of lens sets is DENIED at the tool call, so this shape
// is fixed by the enforcement point rather than chosen. TOOL-dTieredTribunal-13 tightened the branch
// this line sits on to require EVERY value branch bounded, and both branches here are literals.
const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers

const finderResults = await boundedParallel(
  LENSES.map((L) => () =>
    agent(
      (isSpec
        // S6 - the spec kind's acquire sentence. The lens holds a filesystem and the orchestrator does
        // not, so the BLOB COMPARISON happens here. Without it S5 is a string test any caller
        // satisfies; with it, a spec that moved since the caller pinned it is a blocker finding.
        ? `You are the ${L.key} reviewer of a SPEC SET. For EACH subject below: first run ` +
          `\`git hash-object <path>\` in ${repo} and compare the result to the pinned blob. A mismatch ` +
          `means the spec MOVED since this review was commissioned — report it as a BLOCKER finding ` +
          `and review the file as it now stands. Then Read the file WHOLE.\n\nSUBJECTS:\n` +
          subjects.map((x) => `  - ${x.path}  blob ${x.blob}`).join('\n') + `\n\n`
        : `You are the ${L.key} reviewer. Review ONLY this diff (run \`${diffCmd}\`, then Read/Grep the touched files + their immediate callers):\n\n`) +
        `CONTEXT: ${context}\n` +
        `REVIEW ROUND: ${round}${round > 1 ? (isSpec ? ' - this is a FOLD review. Aim at the text the previous round\'s fixes introduced, which is the only text in these documents nobody has reviewed.' : ' - this is a FOLD review. The diff above is what the previous round\'s fixes introduced, not the whole build.') : ''}\n` +
        `BY DESIGN (do NOT re-report these): ${byDesign}\n` +
        (priorFindings.length
          ? `PRIOR ROUND'S CONFIRMED FINDINGS - these were RAISED AND FIXED. Judge the FIX, and do not re-raise the original:\n` +
            priorFindings
              .map((f) => `  - ${f.ref || '(no ref)'} - ${f.claim || f.title || '(no claim)'}`)
              .join('\n') +
            `\n\n`
          : `PRIOR ROUND'S FINDINGS: none - this is a first-round review of ${isSpec ? 'the whole spec set' : 'the whole diff'}.\n\n`) +
        `LENS: ${L.brief}\n\n` +
        (isSpec
          ? `Emit CONCRETE findings only — each needs file, where, severity (blocker|high|medium|low), with "where" being the section address, e.g. "section 2 S5", a one-line claim, the impact, and a proposed fix. A spec finding is often the ABSENCE of a line, so address it by section. No speculation, no style nits, nothing outside the spec set. If nothing real, return findings: [].\n` +
            `Return JSON {lens:"${L.key}", findings:[{file,where,severity,claim,impact,fix}]}.`
          : `Emit CONCRETE findings only — each needs file, line, severity (blocker|high|medium|low), a one-line claim, the impact, and a proposed fix. No speculation, no style nits, nothing outside the diff. If nothing real, return findings: [].\n` +
            `Return JSON {lens:"${L.key}", findings:[{file,line,severity,claim,impact,fix}]}.`),
      { label: `find:${L.key}`, phase: 'Find', schema: isSpec ? SPEC_FINDING_SCHEMA : FINDING_SCHEMA },
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
  .flatMap((r) => (r.findings || []).map((f) => ({ ...f, ref: `${f.file}:${isSpec ? f.where : f.line}` })))
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
      (isSpec
        ? `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — Read the cited spec at the cited section, and the siblings it names, and decide "confirmed" (real, and it makes the spec unbuildable or wrong) or "refuted" (asks for detail a non-goal withholds / cites a section that says what the finding claims it does not / is a style preference). Default to refuted when uncertain.\n\n`
        : `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate). Default to refuted when uncertain.\n\n`) +
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
    `\n\nWrite a markdown report (severity-ranked, blockers first, each with ${isSpec ? 'its file and section address' : 'file:line'} + fix + a left-shift gate suggestion) to a file under ${repo}/${reviewDir}. ` +
    `State the review shape near the top — raw ${allFindings.length}, confirmed ${confirmed.length}, refuted ${refuted.length}, unverified ${unverified.length}, precision ${precision.toFixed(2)}. ` +
    // The range line is what the unattended kit's `closing-review-recorded` joins on, so the value
    // reaches the record without a human remembering to type it. HONEST LIMIT: `base` defaults to
    // the REF 'origin/main', and a caller who lets it stand writes a line carrying no sha, which
    // satisfies nothing. The harness cannot tell whether a mandate is in force — it has no
    // filesystem and no repo access — so M8 spelling the invocation with the pinned sha is what
    // makes this work, and the failure surfaces as an unmet DoD item naming the run's own record.
    (isSpec
      // S9 - a spec audit has no range. Its anchor is the pinned blob per subject, which is what
      // makes "which rev was reviewed" answerable from the record instead of from recollection.
      ? `Open the report with a line naming each reviewed subject and the blob it was pinned at — ` +
        subjects.map((x) => `${x.path}@${x.blob}`).join(', ') + `, and state the ROUND as ${round}. `
      : `Open the report with a line naming the reviewed range as ${base}...${head}, and state the ROUND as ${round}. `) +
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
    `The report's FIRST line must be the record's binding line, exactly: **Serves:** ${kind} ` +
    `followed by every unit id ${isSpec ? 'the reviewed spec set defines' : 'in the diff'}, space-separated. A kind with no id is malformed under the ` +
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

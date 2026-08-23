export const meta = {
  name: 'drift-audit-state',
  version: '1.6',
  description:
    "Drift audit Tier 1/2: are this repo's own records still true? Stale maps, stale memory, charter drift, work-state uncertainty, record-gate integrity. Project-agnostic; all repo facts arrive via args.",
  whenToUse:
    'Tier 1: narrow LENSES to the one Tier-0 signal that moved, plus the standing record-gate lens. Tier 2: run all five, sequentially after drift-audit-code (the concurrency cap is fleet-wide).',
  phases: [
    { title: 'Find', detail: 'primed lenses over the memory tree, charter and generated build index' },
    { title: 'Verify', detail: 'batched default-refute skeptics, keyed by integer index' },
    { title: 'Synthesize', detail: 'one pass -> report file' },
  ],
}

// gov:kit drift-audit@1.6
// --- bounded fan-out (inlined; workflow scripts cannot import) ------------
// BOTH THE CONCURRENCY CAP AND THE VERIFIER TOTAL ARE BARE LITERALS, and neither is caller-settable.
// The retired form bound each of them from an `<expr> || 5` fallback, which read as a constant to the
// guard and as a knob to the runtime — so a caller raised this harness's own agent count past the cap
// with every gate green. agent-cap.js now RESOLVES the bound and refuses that binder form outright.
// (The spelling itself is paraphrased here on purpose: the acceptance grep for it is repo-wide and
// would match the comment explaining it.)
const CAP = 5
async function boundedParallel(thunks, cap = CAP) {
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

// --- inputs (via Workflow `args`) ----------------------------------------
// {
//   repo, base, outDir,                      // as in drift-audit-code
//   memoryRoot: "memory",                    // from .memory-tree.conf
//   charter: "AGENTS.md",                    // the file holding the binding rules + node registry
//   gateManifest: "tools/gate-legs.json",    // the generated/authoritative leg list, if any
//   measured: "Tier-0 numbers, to interrogate not re-derive",
//   heuristics: "any orchestrator heuristic handed over, WITH its known failure mode",
//   byDesign: "recorded/backlogged issues reviewers must NOT re-report",
//   lenses: ["map-truth","memory-rot","charter-drift","work-state","record-gate-integrity"],
// }
const a = args || {}
const REPO = a.repo || '.'
const BASE = a.base || 'HEAD'
const OUT = a.outDir || `${REPO}/memory`
const MEM = a.memoryRoot || 'memory'
const CHARTER = a.charter || 'AGENTS.md'
const MAX_VERIFIERS = 5

const COMMON = `
You are auditing the RECORDS of the repo at ${REPO}. Treat ${BASE} as "what ships".

THE COMMISSIONING QUESTION: the owner reports that the build FEELS like it is drifting and its state
is UNCERTAIN. This wave audits the repo's SELF-KNOWLEDGE: its memory tree at \`${MEM}/\`, its charter
\`${CHARTER}\`, and the gates that police them. A repo whose own records are wrong cannot tell its
owner what state it is in — that IS the reported symptom, so treat every record-vs-reality gap as a
first-class finding.

MEASURED BASELINES (already established; do not re-derive, DO interrogate/extend):
${a.measured || '(none supplied — establish your own and show the command behind each number)'}

HEURISTIC LEADS handed over by the orchestrator, each with its known failure mode. These are LEADS to
re-derive, NOT findings. Do not repeat their numbers as fact:
${a.heuristics || '(none supplied)'}

ALREADY KNOWN — do not re-report as new:
${a.byDesign || '(none supplied)'}

EVIDENCE RULES (these decide whether your finding survives the skeptic):
- Every finding needs a real path:line you actually opened. Forward slashes only, no backslashes.
- A "stale record" claim must show BOTH sides: what the record says, and what is actually true, each
  with its own path:line or command output. A one-sided claim will be refuted.
- Distinguish three very different things and never conflate them:
  (a) a record that is WRONG — says X, reality is not-X. The serious class.
  (b) a record that is merely OLD but still true.
  (c) an APPEND-ONLY record deliberately superseded by a later id, or one under an archive/ path.
      That is the designed behaviour of a decision log and is NOT staleness. Reporting (c) as drift
      will be refuted.
- Quantify. "Some specs are stale" is worthless; "N of M, here is the list" is a finding.
- Severity: blocker = actively misleads a session into wrong work, or breaks a gate; high = a session
  would make a materially wrong decision from it; medium = real cost; low = tidy-up.

OUTPUT: Write your full prose writeup (evidence, commands, per-finding detail, and any list too long
for the structured return) to ${OUT}/wave2-<yourLensSlug>.md and return ONLY the structured object.
Keep each structured field under ~300 chars.
Required keys on the returned object: lens, path, summary, findings.
Each finding requires: file, line, severity, claim, impact, fix.
`

const FINDING_SCHEMA = {
  type: 'object',
  required: ['lens', 'path', 'summary', 'findings'],
  properties: {
    lens: { type: 'string' },
    path: { type: 'string' },
    summary: { type: 'string' },
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

const ALL_LENSES = [
  {
    slug: 'map-truth',
    label: 'find:map-truth',
    brief: `LENS — IS THE MACHINE-VERIFIED LAYER STILL TRUE?
If this repo has a codebase map, dossier layer, or any artifact advertised as CI-verified, sessions are
told to TRUST IT OVER PROSE. That makes a false claim there far more dangerous than a false journal
note. Audit it:
 - Read the generator and the gate. Learn exactly what the ratchet DOES prove (usually: every
   inventory key is claimed somewhere, and no claim names a deleted key) and what it does NOT (that
   the surrounding PROSE is true; that a claim is non-redundant — multi-claim is typically legal).
 - Then sample dossiers for BUSY areas and check their prose against source. Name specific false
   sentences with both path:lines.
 - Every grace/backfill/exemption list: how big, what is still parked there, has it shrunk? A large
   permanent baseline means the coverage gate is mostly excused.
 - If a shrink mechanism is documented, find its CALLERS. A grace list whose un-gracing command is
   invoked by nothing is permanent, and any docstring promising "no human remembering" is false.
 - Which shipped features have NO entry at all? Undossiered features are invisible to the premise.`,
  },
  {
    slug: 'memory-rot',
    label: 'find:memory-rot',
    brief: `LENS — IS THE MEMORY TREE STILL TRUE, AND IS IT AFFORDABLE?
 - THE SPEC STATUS QUESTION (highest value). For each non-terminal spec (OPEN/SPECCED/BLOCKED/
   INPROGRESS), determine whether its unit actually landed — cross-reference the generated build
   index, the decision indexes, the backlog rows, and git (\`git log --grep=<id>\`, and whether a
   named merge sha is an ancestor of ${BASE}). Report the REAL count whose header contradicts
   reality, with the list. A spec frozen mid-build is a named rot class; a spec that shipped and
   still says SPECCED is the same class.
 - Which memory documents make claims now FALSE about the code at ${BASE}? Sample the
   highest-traffic notes and verify their concrete claims — paths, flags, commands, ports.
 - Does any CURRENT (non-archive) doc still instruct a session to use a RETIRED mechanism? That
   actively misleads. An archived or explicitly-superseded doc doing so is by design.
 - COST: is the read path affordable? Measure what a session is actually told to read at DoR against
   what it plausibly reads. A mandate nobody can follow is worse than a smaller one they would.
 - Indexes: is each within its declared byte/line budget? Are journals bounded or unbounded?`,
  },
  {
    slug: 'charter-drift',
    label: 'find:charter-drift',
    brief: `LENS — DOES THE CHARTER STILL DESCRIBE THE REPO?
\`${CHARTER}\` is auto-loaded into EVERY session and its directives are binding, so a false sentence
there propagates into every future session's behaviour. It is the highest-leverage document here.
Read ALL of it and verify every checkable factual assertion against the tree at ${BASE}.
 - Any hand-kept INVENTORY in charter prose (a gate-leg list, a package list, a count) against its
   generated or authoritative source${a.gateManifest ? ` — start with \`${a.gateManifest}\`` : ''}. A
   hand-kept twin of a generated list is a recorded defect class; find every instance.
 - Every in-repo path the charter names: does it still exist?
 - Every command it prescribes: does it still work, and is it still the right one?
 - Do the charter and any SECONDARY governance doc (a kickoff manifest, a skill, a protocol file)
   CONTRADICT each other? A session obeying the wrong one behaves wrongly, and the two documents
   usually share no greppable token, so only reading both finds it.
 - User-facing docs: does each page name a control a reader can actually click? Is any page describing
   a capability that never shipped or has been removed? Which shipped features have no page?`,
  },
  {
    slug: 'work-state',
    label: 'find:work-state',
    brief: `LENS — WHAT STATE IS THE WORK ACTUALLY IN? (the owner's literal question)
The GENERATED build index (\`${MEM}/LIVE.md\` and \`${MEM}/ledger/<month>.md\`) is the record of who
touched what. It is DERIVED from build front matter, so test it against git rather than trusting it.
 - For each build the index calls non-terminal: does git agree? Separate a record's BASE sha ("off
   \`X\`") from its WORK shas — the base is an ancestor by construction and proves nothing, and
   conflating them makes every record a false positive. Report the real count that contradicts git.
 - The inverse and more dangerous direction: work claimed as LANDED that is NOT an ancestor of
   ${BASE}, and work sitting on branches nobody tracks.
 - Say explicitly what is STRUCTURALLY UNKNOWABLE from this clone. Other nodes are other machines;
   their landed work is visible, their working trees are not. An audit that pretends to see them is
   worse than one that names the blind spot. Name the unknowables.
 - Do the branches and worktrees any record names still resolve? A pointer at a deleted worktree is
   work nobody can resume. Be careful to judge only THIS node's paths.
 - Is the index still a byte-identical render of its source, or has someone hand-edited it?
 - The bottom line the owner needs: is there work that is BUILT, GATED, REVIEWED and simply LOST —
   nobody merged it and no record accurately says so? Name it, or state plainly that there is none.`,
  },
  {
    slug: 'record-gate-integrity',
    label: 'find:record-gate-integrity',
    brief: `LENS — CAN THE RECORD-POLICING GATES ACTUALLY FAIL? (the keystone — be ruthless)
If they cannot, every "green" above is meaningless and the drift the owner feels is invisible BY
CONSTRUCTION. Do not assume; TEST.
 1. Enumerate every check in the hygiene/record gate suite. For a sample, CONSTRUCT the minimal
    violating input and verify the check actually reds. Report any check that is unreachable,
    permanently satisfied, grandfathered into irrelevance, or gated on a date/path condition that no
    longer selects anything. If a golden harness exists, check whether it covers every check or only
    some — an uncovered check is one nobody has ever seen fail.
 2. Distinguish SHAPE checks from TRUTH checks and count each. A check that a status token is spelled
    legally is not a check that it is true. If nothing in the suite adjudicates truth, that gap is the
    finding, and it is the mechanism behind every stale record above.
 3. Date-gated or path-gated checks: what selects the population? If a session chooses the date or the
    path, it chooses whether the check applies. Test whether the gate can be evaded.
 4. Any ratchet or pin: is it pinned to a floor that is trivially met? Quantify how much of the
    population is LOAD-BEARING versus excused.
 5. Does the local gate suite run the same legs as CI? Twin enforcement points that no test compares
    are a recorded defect class — and unifying on the form that silences a symptom trades a false
    positive for a false NEGATIVE, so enumerate every state the predicate can see.
 6. Is any gate currently RED at the tip of the shared default branch? A leg that always runs being
    red at the tip is itself proof the full bar did not run at that push boundary.
Demonstrate, do not assert — run the tool and show the output for every claim.`,
  },
]

// gov:fixed-verifiers — derived from the ALL_LENSES literal above; `.filter` cannot grow it, so the
// agent count stays the constant the source shows.
const LENSES = a.lenses && a.lenses.length ? ALL_LENSES.filter((L) => a.lenses.includes(L.slug)) : ALL_LENSES // gov:fixed-verifiers

phase('Find')
const finderResults = await boundedParallel(
  LENSES.map((L) => () =>
    agent(`${COMMON}\n\n${L.brief}`, { label: L.label, phase: 'Find', schema: FINDING_SCHEMA })
  ),
  CAP
)

const lensOut = finderResults.filter(Boolean)
const indexed = []
lensOut.forEach((r) => {
  ;(r.findings || []).forEach((f) => indexed.push({ id: indexed.length + 1, lens: r.lens, ...f }))
})
log(`Find: ${lensOut.length}/${LENSES.length} lenses returned, ${indexed.length} raw findings`)

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
          id: { type: 'integer' },
          verdict: { type: 'string', enum: ['confirmed', 'refuted', 'partial'] },
          reason: { type: 'string' },
          severityCorrection: { type: 'string' },
        },
      },
    },
  },
}

phase('Verify')
const batches = indexed.length ? chunk(indexed, Math.ceil(indexed.length / MAX_VERIFIERS)) : [] // gov:fixed-verifiers
const verdictBatches = await boundedParallel(
  batches.map((b, bi) => () =>
    agent(
      `You are a DEFAULT-REFUTE skeptic auditing findings from a records/state drift audit of ${REPO}
(ships at ${BASE}). Your job is to REFUTE. Assume each finding is wrong until its evidence forces you
to agree. Open the cited file:line yourself and re-run the checks.

Refute when ANY of these hold:
- the cited file:line does not say what the finding claims;
- the record is APPEND-ONLY and was deliberately superseded by a later id — designed behaviour, not
  staleness;
- the document is under an archive/ path, or is explicitly marked SUPERSEDED/rotated;
- the claim rests on an orchestrator HEURISTIC (with its stated failure mode) rather than on the
  finder's own re-derivation;
- a sha the finding calls a "work sha" is actually the row's BASE sha, an ancestor by construction;
- the item is correctly grandfathered by an explicit date cutoff or exemption file;
- the gate the finding calls vacuous CAN in fact fail — if you can construct a failing input, refute;
- the claim is already recorded/backlogged and adds nothing new;
- the impact does not follow even if the fact is true (cost asserted as correctness);
- the finding is speculative, unquantified, or an aesthetic preference.
Mark "partial" when the fact is real but severity/impact is overstated; give the corrected severity in
severityCorrection.

Return ONE verdict per id below. Required keys: id (integer), verdict
(confirmed|refuted|partial), reason. Optional: severityCorrection.
Echo the id EXACTLY as an integer. Return every id in this batch, even if unsure — if you cannot reach
a judgement use "partial" and say why. Do not invent ids not in this batch.

HEURISTICS the finders were given as leads, NOT findings:
${a.heuristics || '(none supplied)'}

ALREADY KNOWN:
${a.byDesign || '(none supplied)'}

FINDINGS BATCH ${bi + 1}:
${JSON.stringify(b, null, 1)}`,
      { label: `verify:batch${bi + 1}`, phase: 'Verify', schema: VERDICT_SCHEMA }
    )
  ),
  CAP
)

const vmap = new Map()
verdictBatches.filter(Boolean).forEach((vb) => {
  ;(vb.verdicts || []).forEach((v) => {
    if (typeof v.id === 'number' && !vmap.has(v.id)) vmap.set(v.id, v)
  })
})
const judged = indexed.map((f) => {
  const v = vmap.get(f.id)
  return {
    ...f,
    verdict: v ? v.verdict : 'unverified',
    reason: v ? v.reason : 'no verdict returned',
    severityCorrection: v && v.severityCorrection,
  }
})
const confirmed = judged.filter((f) => f.verdict === 'confirmed')
const partial = judged.filter((f) => f.verdict === 'partial')
const refuted = judged.filter((f) => f.verdict === 'refuted')
const unverified = judged.filter((f) => f.verdict === 'unverified')
const precision =
  confirmed.length + refuted.length ? confirmed.length / (confirmed.length + refuted.length) : null
log(
  `Verify: ${confirmed.length} confirmed, ${partial.length} partial, ${refuted.length} refuted, ` +
    `${unverified.length} UNVERIFIED, precision ${precision === null ? 'n/a' : precision.toFixed(2)}`
)

phase('Synthesize')
const synth = await agent(
  `Synthesize a records/state drift audit of ${REPO} (ships at ${BASE}) into ONE report at
${OUT}/drift-audit-wave2-state.md.

The commissioning question was: are the records stale, and why does the project's state feel uncertain?

Write it so a tired reader has the answer in the first ten lines. Structure:
1. Verdict up front: are the records trustworthy, and what is the single worst instance.
2. THE STATE ANSWER — a plain-language statement of what state the work is actually in: how many
   build records contradict git, what is built-but-unlanded, and what is structurally UNKNOWABLE from
   this clone. The owner asked this directly; answer it directly and do not bury it.
3. Severity-ordered table of CONFIRMED findings (id, severity, file:line, one-line claim).
4. PARTIAL findings with the corrected severity beside the original.
5. UNVERIFIED findings, listed explicitly — NOT refuted, NOT cleared. If the count is zero, say so and
   explain why that is positive evidence rather than an absence of checking.
6. Refuted findings, one line each.
7. Gate integrity: can the record-policing gates actually fail? Say which were TESTED versus assumed.
   Separate SHAPE checks from TRUTH checks and say whether anything adjudicates truth at all.
8. Cross-cutting themes: the MECHANISM by which records go stale here, not the instances.
9. A prioritized do-this-next list, cheapest-high-value first, each naming the file to touch.

Rules: every claim keeps its file:line. Do not soften or round. Do not invent findings not in the
data. Report precision and all five counts honestly. Where a number came from an orchestrator
heuristic and was NOT re-derived, label it as such. Where findings contradict each other, surface the
contradiction rather than silently picking one — include a short contradictions appendix if there are
several.

Return {path, summary} only — the prose goes in the file. Forward slashes in the path.

DATA:
counts: raw ${indexed.length}, confirmed ${confirmed.length}, partial ${partial.length}, refuted ${refuted.length}, unverified ${unverified.length}, precision ${precision === null ? 'n/a' : precision.toFixed(2)}
lens writeups: ${JSON.stringify(lensOut.map((r) => ({ lens: r.lens, path: r.path, summary: r.summary })), null, 1)}
judged findings: ${JSON.stringify(judged, null, 1)}`,
  {
    label: 'synth:state-drift',
    phase: 'Synthesize',
    schema: {
      type: 'object',
      required: ['path', 'summary'],
      properties: { path: { type: 'string' }, summary: { type: 'string' } },
    },
  }
)

return {
  wave: 'state-drift',
  lensesRun: LENSES.map((L) => L.slug),
  counts: {
    raw: indexed.length,
    confirmed: confirmed.length,
    partial: partial.length,
    refuted: refuted.length,
    unverified: unverified.length,
  },
  precision,
  report: synth && synth.path,
  summary: synth && synth.summary,
  confirmedTop: confirmed
    .filter((f) => f.severity === 'blocker' || f.severity === 'high')
    .map((f) => `[${f.severity}] ${f.file}:${f.line} — ${f.claim}`),
  unverifiedList: unverified.map((f) => `${f.file}:${f.line} — ${f.claim}`),
}

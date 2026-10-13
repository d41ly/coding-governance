// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-m2-lens-scout',
  description: 'aScoutedSeam benchmark arm M2: frame the request into needs, five fixed lenses, two adversarial verifiers, a derived seam list',
  phases: [
    { title: 'Frame', detail: 'one agent turns the request into needs in the repo vocabulary' },
    { title: 'Lenses', detail: 'five fixed lenses, bounded fan-out' },
    { title: 'Verify', detail: 'two skeptics refute each candidate' },
  ],
}

async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}
function chunk(xs, n) {
  const out = []
  for (let i = 0; i < xs.length; i += n) out.push(xs.slice(i, i + n))
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)
const c = cfg && cfg.case
if (!c || !c.tree || !c.prompt) throw new Error('args.case must carry tree and prompt')

function renderTrees() {
  let t = 'PRIMARY TREE (' + c.repo + '): ' + c.tree
  if (c.core_tree) t += '\nHOST CORE TREE (incms, the platform this package installs into; its blocks, DSL, theme and UI primitives are available to the package): ' + c.core_tree
  return t
}
const RULES = 'RULES: work ONLY inside the tree(s) above, read-only: no edit, stage or commit. Never read anything under C:/projects or any other checkout, and never consult git history beyond the tree HEAD — you are standing at the moment the request arrived. You may run the tree\'s own read-only CLIs with cwd inside the tree (scripts/ or tools/ codebase-map/reuse_lookup.py "<behaviour phrase>", memory-recall/query.py "<question>" --terms "<8-14 words>"), grep, glob and read.'
const REQUEST = 'THE REQUEST:\n"""' + c.prompt + '"""'

const NEEDS = { type: 'object', required: ['needs', 'surfaces', 'ui'], properties: {
  needs: { type: 'array', items: { type: 'object', required: ['id', 'kind', 'what', 'terms'], properties: {
    id: { type: 'integer' }, kind: { type: 'string' }, what: { type: 'string' },
    terms: { type: 'array', items: { type: 'string' } } } } },
  surfaces: { type: 'array', items: { type: 'string' } },
  ui: { type: 'boolean' },
  orientation: { type: 'string' } } }

phase('Frame')
const framed = await agent([
  'You FRAME a request for a reuse search. Do not search for seams yet beyond what you need to learn the codebase vocabulary.',
  renderTrees(), RULES, REQUEST,
  'Read the tree\'s orientation material first (AGENTS.md/CLAUDE.md, memory/map/generated/CARDS.md or MAP.md if present, the map dossiers\' titles) to learn its vocabulary. Then break the request into 3-10 NEEDS: each a capability, UI element, visual treatment, data shape, behaviour, or infrastructure the build will need (including implied ones the owner did not spell out, e.g. "an image property" implies choosing/uploading media). kind is one of surface | ui-element | visual | behaviour | data | infra | convention. what = the need in plain words. terms = 4-8 alternative phrasings IN THIS CODEBASE\'S OWN VOCABULARY (names you saw in the map, dossiers, directory names) plus generic synonyms — the words existing code for this need would use. surfaces = every existing page, route, block, component, command or feature the request names or implies (e.g. "/intake", "the product cards", "the hero"). ui = true if any need is visual or a UI element. orientation = 2-3 sentences on where things live in this tree.',
].join('\n\n'), { label: 'frame', phase: 'Frame', schema: NEEDS, ...(cfg.effort ? { effort: cfg.effort } : {}) })
if (!framed) throw new Error('frame agent died')
const needsText = framed.needs.map((n) => 'N' + n.id + ' [' + n.kind + '] ' + n.what + ' — terms: ' + n.terms.join(', ')).join('\n')

const CANDS = { type: 'object', required: ['candidates'], properties: {
  candidates: { type: 'array', items: { type: 'object', required: ['needs', 'repo', 'path', 'symbol', 'fit', 'how', 'evidence'], properties: {
    needs: { type: 'array', items: { type: 'integer' } }, repo: { type: 'string' }, path: { type: 'string' },
    symbol: { type: 'string' }, fit: { type: 'string' }, how: { type: 'string' }, evidence: { type: 'string' } } } },
  notes: { type: 'string' } } }

const LENSES = [
  { key: 'anchors', brief: 'ANCHORS AND PRECEDENTS. Resolve every named or implied surface (' + framed.surfaces.join('; ') + ') to the code that implements it today. Then find the existing implementations of the same KIND of thing the request builds (sibling pages, blocks, sections, cards, fields, commands, checks). Where several exist, identify the CANONICAL one — the shared generator/factory/base the others call, the one a dossier or decision names, the newest consolidated one — and say which siblings are stale copies NOT to copy.' },
  { key: 'code', brief: 'SHARED CODE. For each behaviour, data, infra and ui-element need, find existing functions, components, field factories, hooks, bridges, shell functions, scripts and libraries that already do it — including unexported and private ones and shell. Search by CONCEPT with every term in the needs list (grep -ri across all file types, not just names), and run the tree\'s reuse_lookup with 2-3 behaviour phrasings. Check reachability: can code where this request will live call it (package boundaries, bridges, kit boundaries — a port plus a parity check counts as reuse)? Do not trust a code comment claiming something is unreachable; verify.' },
  { key: 'design', brief: framed.ui ? 'DESIGN SYSTEM. Find the design vocabulary this request must build with: design tokens and CSS custom properties (both trees), theme variables, UI primitives and their variants/props, DSL node kinds/recipes and their props, layout and spacing conventions, existing visual patterns for the same kind of surface (cards, stages, eyebrows, buttons, sections), style guides and design rules in docs. Name the exact token/prop/variant names to use instead of literals, and the existing pattern each new element should match.' : 'DESIGN SYSTEM. The framing found no UI need; confirm quickly by reading the needs, and return candidates only if one is in fact visual.' },
  { key: 'records', brief: 'RECORDS AND CONVENTIONS. Find prior decisions, dossier "Reuse affordance"/"Shared seams" lines, help/docs pages, gotchas and backlog asks that settle HOW this kind of thing is built here — e.g. a rule that a third surface "adds a call, not a third copy", a canonical seam named in a dossier, a rejected design. Use the tree\'s memory-recall CLI (8-14 terms in the corpus jargon) and grep memory/ and help/. Return the seam each record points at (path + symbol), citing the record as evidence.' },
  { key: 'constraints', brief: 'CONSTRAINTS. Find the gates, lint rules, tests, schemas and contracts that will constrain how this request must be built, and any sanctioned opt-out that would let a build skip the seam (e.g. a lint disable reason). Return each as a candidate whose "how" says how to satisfy it while building with the existing seams; symbol = the rule/test/contract name.' },
]

phase('Lenses')
const lensOut = await boundedParallel(LENSES.map((L) => () => agent([
  'You are one lens of a REUSE SCOUT. The request below has not been specced. Find what ALREADY EXISTS that the build must reuse or build with.',
  renderTrees(), RULES, REQUEST, 'NEEDS (from the framing pass):\n' + needsText,
  'YOUR LENS — ' + L.brief,
  'Return at most 10 candidates, best first. Each: needs (the N-ids it serves), repo, path (repo-relative), symbol (exact name), fit (use-as-is | extend | wire-through | follow-pattern | constraint), how (how to build WITH it: the call, prop, token, extension point), evidence (what you read, file:line). Return an empty list rather than a weak candidate.',
].join('\n\n'), { label: 'lens:' + L.key, phase: 'Lenses', schema: CANDS, ...(cfg.effort ? { effort: cfg.effort } : {}) })), 5)

const seen = new Map()
lensOut.forEach((r, li) => {
  if (!r) return
  for (const x of r.candidates) {
    const k = (x.repo + '|' + x.path + '|' + x.symbol).toLowerCase()
    if (!seen.has(k)) seen.set(k, { ...x, lenses: [LENSES[li].key] })
    else seen.get(k).lenses.push(LENSES[li].key)
  }
})
const cands = [...seen.values()].map((x, i) => ({ ...x, id: i + 1 }))
log(cands.length + ' distinct candidates from ' + lensOut.filter(Boolean).length + ' live lenses')

const VERDICTS = { type: 'object', required: ['verdicts'], properties: {
  verdicts: { type: 'array', items: { type: 'object', required: ['id', 'verdict', 'binding', 'how', 'reason'], properties: {
    id: { type: 'integer' }, verdict: { type: 'string', enum: ['confirmed', 'refuted'] },
    binding: { type: 'string', enum: ['MUST', 'SHOULD', 'INFO'] }, how: { type: 'string' }, reason: { type: 'string' } } } } } }

phase('Verify')
const MAX_VERIFIERS = 2
const batches = cands.length ? chunk(cands, Math.ceil(cands.length / MAX_VERIFIERS)) : [] // gov:fixed-verifiers
const verdictOut = await boundedParallel(batches.map((b, bi) => () => agent([
  'You are a SKEPTIC for a reuse scout. Each candidate below claims an existing seam the request must reuse. Try to REFUTE each one by opening the cited code: does it actually provide the need (not just similar words)? Is it reachable from where this request\'s code will live? Is it the canonical implementation, or a stale copy of one (then refute it and name the canonical one in reason)? Is it a lure — a seam for a different need (e.g. an admin media picker offered for a visitor file upload)? Default to refuted when the evidence does not hold.',
  renderTrees(), RULES, REQUEST, 'NEEDS:\n' + needsText,
  'CANDIDATES:\n' + b.map((x) => 'id=' + x.id + ' needs=' + x.needs.join(',') + ' ' + x.repo + ':' + x.path + ' :: ' + x.symbol + ' [' + x.fit + '] how: ' + x.how + ' | evidence: ' + x.evidence).join('\n'),
  'For each id return verdict, binding (MUST = building the request without it is a defect a reviewer must reject; SHOULD = strong default; INFO = context only), how (corrected one-line build-with instruction), reason. Copy the integer id exactly.',
].join('\n\n'), { label: 'verify:' + (bi + 1), phase: 'Verify', schema: VERDICTS, ...(cfg.effort ? { effort: cfg.effort } : {}) })), 5)

const byId = new Map()
verdictOut.forEach((r) => { if (r) for (const v of r.verdicts) byId.set(v.id, v) })
const seams = []
for (const x of cands) {
  const v = byId.get(x.id)
  if (!v || v.verdict !== 'confirmed') continue
  seams.push({ repo: x.repo, path: x.path, symbol: x.symbol, binding: v.binding, need: x.needs.map((n) => 'N' + n).join(','),
    how: v.how, evidence: x.evidence, lenses: x.lenses })
}
const order = { MUST: 0, SHOULD: 1, INFO: 2 }
seams.sort((a, b) => order[a.binding] - order[b.binding])
const covered = new Set()
seams.forEach((s) => { if (s.binding !== 'INFO') s.need.split(',').forEach((n) => covered.add(n)) })
const unmet = framed.needs.filter((n) => !covered.has('N' + n.id)).map((n) => 'N' + n.id + ' ' + n.what)
return { seams, unmet, searched: 'lenses: ' + LENSES.map((L) => L.key).join(', '), framed,
  candidates: cands.length, refuted: cands.filter((x) => byId.get(x.id) && byId.get(x.id).verdict === 'refuted').length,
  unjudged: cands.filter((x) => !byId.get(x.id)).length, lensesDead: lensOut.filter((r) => !r).length }

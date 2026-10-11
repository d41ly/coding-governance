// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-m3-lean-scout',
  description: 'aScoutedSeam benchmark arm M3: per case a code scout and a design scout in parallel, then one strict judge that merges, refutes and binds; up to 5 cases per run',
  phases: [
    { title: 'Scout', detail: 'code scout + design scout per case' },
    { title: 'Judge', detail: 'one judge per case merges, refutes, binds' },
  ],
}

async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)
if (!cfg || !cfg.cases) throw new Error('args must carry cases')

const CANDS = { type: 'object', required: ['needs', 'candidates'], properties: {
  needs: { type: 'array', items: { type: 'string' } },
  candidates: { type: 'array', items: { type: 'object', required: ['repo', 'path', 'symbol', 'need', 'how', 'evidence'], properties: {
    repo: { type: 'string' }, path: { type: 'string' }, symbol: { type: 'string' }, need: { type: 'string' },
    how: { type: 'string' }, evidence: { type: 'string' }, not: { type: 'string' } } } },
  constraints: { type: 'array', items: { type: 'object', required: ['path', 'rule', 'how'], properties: {
    path: { type: 'string' }, rule: { type: 'string' }, how: { type: 'string' } } } } } }

const SEAMS = { type: 'object', required: ['seams', 'constraints', 'unmet'], properties: {
  seams: { type: 'array', items: { type: 'object', required: ['repo', 'path', 'symbol', 'binding', 'need', 'how', 'evidence'], properties: {
    repo: { type: 'string' }, path: { type: 'string' }, symbol: { type: 'string' },
    binding: { type: 'string', enum: ['MUST', 'SHOULD'] }, need: { type: 'string' },
    how: { type: 'string' }, evidence: { type: 'string' }, not: { type: 'string' } } } },
  constraints: { type: 'array', items: { type: 'object', required: ['path', 'rule', 'how'], properties: {
    path: { type: 'string' }, rule: { type: 'string' }, how: { type: 'string' } } } },
  unmet: { type: 'array', items: { type: 'string' } },
  refuted: { type: 'array', items: { type: 'string' } } } }

function renderTrees(c) {
  let t = 'PRIMARY TREE (' + c.repo + '): ' + c.tree
  if (c.core_tree) t += '\nHOST CORE TREE (incms, the platform this package installs into; its blocks, DSL, theme and UI primitives are available to the package): ' + c.core_tree
  return t
}
const RULES = 'RULES: work ONLY inside the tree(s) above, read-only: no edit, stage or commit. Never read anything under C:/projects or any other checkout, and never consult git history beyond the tree HEAD — you stand at the moment the request arrived. You may run the tree\'s own read-only CLIs with cwd inside the tree (scripts/ or tools/ codebase-map/reuse_lookup.py "<behaviour phrase>"; memory-recall/query.py "<question>" --terms "<8-14 words>"), grep, glob and read.'
function renderRequest(c) { return 'THE REQUEST:\n"""' + c.prompt + '"""' }

function renderCodePrompt(c) {
  return [
    'You are the CODE half of a reuse scout for a request that has not been specced yet. Find the EXISTING implementations the build must reuse. A separate design scout covers tokens, styling and visual patterns, so skip those.',
    renderTrees(c), RULES, renderRequest(c),
    '1. ORIENT: read AGENTS.md/CLAUDE.md and the codebase map index (memory/map/generated/CARDS.md or MAP.md, dossier titles) for the vocabulary.',
    '2. FRAME: list 3-10 needs, including implied ones (an image property implies choosing or uploading media; a check implies reading config).',
    '3. ANCHORS: resolve every surface the request names or implies to its code. Find the existing implementations of the same KIND of thing, and name the CANONICAL one (the shared generator, factory or base the others call, or the one a dossier or decision names) versus stale copies.',
    '4. SHARED CODE: for each behaviour, data and infra need, search by CONCEPT (grep -ri every term across all file types, including shell) and run reuse_lookup with two or three phrasings. Verify reachability; never trust a comment claiming a seam is unreachable. A port plus a parity check counts as reuse across a kit boundary.',
    '5. RECORDS: query the memory-recall CLI and grep memory/ and help/ for the decisions and dossier "Reuse affordance" lines that settle how this kind of thing is built here.',
    'Return at most 10 candidates: each an existing implementation of a need, with how to build WITH it and evidence (file:line). Put files to edit and tests to keep green in constraints instead, at most 5.',
  ].join('\n\n')
}

function renderDesignPrompt(c) {
  return [
    'You are the DESIGN half of a reuse scout for a request that has not been specced yet. Find the design vocabulary the build must use. A separate code scout covers behaviour and plumbing.',
    renderTrees(c), RULES, renderRequest(c),
    'If the request has NO visual or UI element at all, return needs=["no UI"] and empty candidates quickly.',
    'Otherwise find the following, in BOTH trees where there are two:',
    '- design tokens and CSS custom properties (:root layers, theme builders);',
    '- UI primitives and their variants and props;',
    '- DSL node kinds, recipes and props;',
    '- field factories for media, colour or icons;',
    '- layout, spacing and type conventions;',
    '- the EXISTING visual pattern for the same kind of surface the request builds (cards, stages, eyebrows, buttons, sections, pages);',
    '- style guides, styling contracts (help/ pages, data-part hooks) and style gates.',
    'Resolve any surface the request says to match ("like /intake", "the product cards") to its exact descriptor, component or stylesheet rules.',
    'Return at most 8 candidates. Each names the exact token, prop, variant, part or pattern to use instead of literals, how to build WITH it, and evidence (file:line). Put style gates in constraints.',
  ].join('\n\n')
}

function renderJudgePrompt(c, a, b) {
  const list = []
  ;[['code', a], ['design', b]].forEach(([k, r]) => {
    if (!r) { list.push('(' + k + ' scout returned nothing)'); return }
    r.candidates.forEach((x) => list.push('[' + k + '] ' + x.repo + ':' + x.path + ' :: ' + x.symbol + ' | need: ' + x.need + ' | how: ' + x.how + ' | evidence: ' + x.evidence + (x.not ? ' | not: ' + x.not : '')))
  })
  const cons = [].concat(a && a.constraints || [], b && b.constraints || [])
  const needs = [].concat(a && a.needs || [], b && b.needs || [])
  return [
    'You are the JUDGE of a reuse scout. Two scouts proposed existing seams for the request below. Your output becomes BINDING instructions for whoever specs and builds it.',
    renderTrees(c), RULES, renderRequest(c),
    'NEEDS the scouts framed:\n' + needs.map((n) => '- ' + n).join('\n'),
    'CANDIDATES:\n' + list.join('\n'),
    'CONSTRAINTS proposed:\n' + cons.map((x) => '- ' + x.path + ': ' + x.rule + ' | ' + x.how).join('\n'),
    'Open the cited code for each candidate and try to REFUTE it. Refute it when it:',
    '- does not really provide the need (it only shares words with it);',
    '- is not reachable from where the new code will live;',
    '- is a stale copy of a canonical implementation (keep the canonical one);',
    '- is a LURE, a seam for a different need;',
    '- is merely a file the build will edit or a test it must pass (move it to constraints instead).',
    'Merge duplicates. Then bind each survivor:',
    '- MUST: building the request without using or extending it is a defect a reviewer must reject.',
    '- SHOULD: a strong default the spec may override with a reason.',
    'Return at most 10 seams, best first, with corrected how and evidence lines. Return at most 5 constraints. Return unmet: each need with no surviving seam, saying what was searched. Return refuted: one line per dropped candidate saying why.',
  ].join('\n\n')
}

const SLOTS = [0, 1, 2, 3, 4]
const results = await boundedParallel(SLOTS.map((s) => async () => {
  const id = cfg.ids[s]
  if (!id) return null
  const c = cfg.cases[id]
  const halves = await boundedParallel([
    () => agent(renderCodePrompt(c), { label: 'code:' + id, phase: 'Scout', schema: CANDS }),
    () => agent(renderDesignPrompt(c), { label: 'design:' + id, phase: 'Scout', schema: CANDS }),
  ], 2)
  const judged = await agent(renderJudgePrompt(c, halves[0], halves[1]), { label: 'judge:' + id, phase: 'Judge', schema: SEAMS })
  return judged ? { ...judged, scoutDead: halves.filter((h) => !h).length,
    nCandidates: (halves[0] ? halves[0].candidates.length : 0) + (halves[1] ? halves[1].candidates.length : 0) } : null
}), 5)
const out = {}
SLOTS.forEach((s) => { if (cfg.ids[s]) out[cfg.ids[s]] = results[s] })
return out

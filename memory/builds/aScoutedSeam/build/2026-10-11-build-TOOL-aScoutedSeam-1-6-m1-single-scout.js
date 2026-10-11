// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-m1-single-scout',
  description: 'aScoutedSeam benchmark arm M1: one free-roaming read-only scout agent per case, up to 5 cases per run',
  phases: [{ title: 'Scout', detail: 'one agent per case, bounded fan-out' }],
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

const SEAMS = {
  type: 'object', required: ['seams', 'unmet', 'searched'],
  properties: {
    seams: { type: 'array', items: { type: 'object', required: ['repo', 'path', 'symbol', 'binding', 'need', 'how'], properties: {
      repo: { type: 'string' }, path: { type: 'string' }, symbol: { type: 'string' },
      binding: { type: 'string', enum: ['MUST', 'SHOULD', 'INFO'] }, need: { type: 'string' },
      how: { type: 'string' }, evidence: { type: 'string' } } } },
    unmet: { type: 'array', items: { type: 'string' } },
    searched: { type: 'string' },
  },
}

function renderTrees(c) {
  let t = 'PRIMARY TREE (' + c.repo + '): ' + c.tree
  if (c.core_tree) t += '\nHOST CORE TREE (incms, the platform this package installs into): ' + c.core_tree
  return t
}

function renderPrompt(c) {
  return [
    'You are the REUSE SCOUT for a new piece of work that has not been specced yet. Before anyone designs it, find what ALREADY EXISTS in the codebase that this work must reuse or build with: components, field factories, functions, shell helpers, scripts, design tokens, CSS custom properties, DSL vocabulary and recipes, page/section patterns, shared generators, conventions and prior decisions that settle how this kind of thing is built.',
    '',
    renderTrees(c),
    '',
    'RULES: work ONLY inside the tree(s) above, read-only. Do not edit, stage or commit. Do not read anything under C:/projects or any other checkout, and do not consult git history beyond the tree\'s HEAD: you are standing at the moment the request arrived. You may run the tree\'s own read-only tools if present (for example scripts/codebase-map/reuse_lookup.py, tools/codebase-map/reuse_lookup.py, scripts/memory-recall/query.py, tools/memory-recall/query.py — run them with cwd inside the tree), grep, glob and read files.',
    '',
    'THE REQUEST (verbatim from the owner, or reconstructed from the build record):',
    '"""' + c.prompt + '"""',
    '',
    'Return at most 12 seams, best first. For each: repo, path (repo-relative), symbol (the exact component/function/token/descriptor/heading name), binding (MUST = building this request without it would be a defect a reviewer should reject; SHOULD = strong default; INFO = context), need (which part of the request it serves), how (one or two sentences: how to build WITH it — the call, prop, token or extension point), evidence (what you read that proves it covers the need). Then unmet: needs for which you found nothing that fits (say what you searched). searched: one line on what you searched.',
  ].join('\n')
}

// A five-element literal the fan-out hook can size; an empty slot is skipped inside its thunk.
const SLOTS = [0, 1, 2, 3, 4]
const results = await boundedParallel(SLOTS.map((s) => () => {
  const id = cfg.ids[s]
  if (!id) return Promise.resolve(null)
  return agent(renderPrompt(cfg.cases[id]), { label: 'm1:' + id, phase: 'Scout', schema: SEAMS, ...(cfg.effort ? { effort: cfg.effort } : {}) })
}), 5)
const out = {}
SLOTS.forEach((s) => { if (cfg.ids[s]) out[cfg.ids[s]] = results[s] })
return out

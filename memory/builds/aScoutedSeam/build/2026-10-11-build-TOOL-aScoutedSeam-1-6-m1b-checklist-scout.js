// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-m1b-checklist-scout',
  description: 'aScoutedSeam benchmark arm M1b: one read-only scout per case that walks a fixed reuse checklist, strict MUST, up to 5 cases per run',
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
  type: 'object', required: ['needs', 'seams', 'constraints', 'unmet'],
  properties: {
    needs: { type: 'array', items: { type: 'string' } },
    seams: { type: 'array', items: { type: 'object', required: ['repo', 'path', 'symbol', 'binding', 'need', 'how', 'evidence'], properties: {
      repo: { type: 'string' }, path: { type: 'string' }, symbol: { type: 'string' },
      binding: { type: 'string', enum: ['MUST', 'SHOULD'] }, need: { type: 'string' },
      how: { type: 'string' }, evidence: { type: 'string' }, not: { type: 'string' } } } },
    constraints: { type: 'array', items: { type: 'object', required: ['path', 'rule', 'how'], properties: {
      path: { type: 'string' }, rule: { type: 'string' }, how: { type: 'string' } } } },
    unmet: { type: 'array', items: { type: 'string' } },
  },
}

function renderTrees(c) {
  let t = 'PRIMARY TREE (' + c.repo + '): ' + c.tree
  if (c.core_tree) t += '\nHOST CORE TREE (incms, the platform this package installs into; its blocks, DSL, theme and UI primitives are available to the package): ' + c.core_tree
  return t
}

function renderPrompt(c) {
  return [
    'You are the REUSE SCOUT for a request that has not been specced yet. Your output becomes binding instructions for whoever specs and builds it, so precision matters as much as recall.',
    renderTrees(c),
    'RULES: work ONLY inside the tree(s) above, read-only: no edit, stage or commit. Never read anything under C:/projects or any other checkout, and never consult git history beyond the tree HEAD: you stand at the moment the request arrived. You may run the tree\'s own read-only CLIs with cwd inside the tree (scripts/ or tools/ codebase-map/reuse_lookup.py "<behaviour phrase>"; memory-recall/query.py "<question>" --terms "<8-14 words>"), grep, glob and read.',
    'THE REQUEST:\n"""' + c.prompt + '"""',
    'WORK THROUGH THIS CHECKLIST IN ORDER:',
    '1. ORIENT. Read AGENTS.md/CLAUDE.md and the codebase map index (memory/map/generated/CARDS.md or MAP.md, dossier titles) to learn this codebase\'s vocabulary and where things live.',
    '2. FRAME. Write the request\'s needs, 3-10 of them, including implied ones (an image property implies choosing or uploading media; a new page implies layout, type and colour; a check implies reading config). For each, note 3-6 words existing code for it would use here.',
    '3. ANCHORS. Resolve every page, route, block, component, command or feature the request names or implies to the code that implements it today. Find the existing implementations of the same KIND of thing being built. Where several exist, identify the CANONICAL one, meaning the shared generator, factory or base the others call, or the one a dossier or decision names. Treat the rest as stale copies not to imitate.',
    '4. SHARED CODE. For each behaviour, data and infrastructure need, search by CONCEPT: grep -ri every term across all file types, including shell, and run reuse_lookup with two or three phrasings. Find the functions, components, field factories, hooks, bridges, shell functions and scripts that already do it. Verify reachability from where the new code will live; never trust a comment claiming something is unreachable. A port plus a parity check counts as reuse across a kit boundary.',
    '5. DESIGN SYSTEM, when any need is visual or a UI element. Find the design tokens and CSS custom properties in BOTH trees, theme variables, UI primitives and their variants and props, DSL node kinds, recipes and props, and the existing visual pattern for the same kind of surface (cards, stages, eyebrows, buttons, sections). Name the exact tokens, props and variants to use instead of literals.',
    '6. RECORDS. Use the memory-recall CLI and grep memory/ and help/. Look for decisions, dossier "Reuse affordance" lines and help pages that settle HOW this kind of thing is built here, such as "a third surface adds a call, not a third copy".',
    '7. SELF-REFUTE each candidate. Does it really provide the need, rather than just sharing words with it? Is it reachable? Is it canonical? Is it a LURE, a seam for a different need such as an admin media picker offered for a visitor file upload? Drop any candidate that fails.',
    'OUTPUT. seams: at most 10, best first, and only EXISTING implementations of a need this request has.',
    '- MUST means writing new code for that need instead of using or extending this would be a defect a reviewer should reject.',
    '- SHOULD means a strong default the spec may override with a stated reason.',
    'Each seam has repo, path (repo-relative), symbol (the exact name), need, how (the call, prop, token or extension point to build WITH), evidence (file:line you read), and not (optional: the stale copy or tempting alternative NOT to use).',
    'Files the build will merely edit, tests it must keep green and docs it must update are NOT seams. Put the rules that will constrain the build in constraints, at most 5: path, rule, how to satisfy it.',
    'unmet: the needs for which nothing fits, each with what you searched.',
  ].join('\n\n')
}

const SLOTS = [0, 1, 2, 3, 4]
const results = await boundedParallel(SLOTS.map((s) => () => {
  const id = cfg.ids[s]
  if (!id) return Promise.resolve(null)
  return agent(renderPrompt(cfg.cases[id]), { label: 'm1b:' + id, phase: 'Scout', schema: SEAMS, ...(cfg.effort ? { effort: cfg.effort } : {}) })
}), 5)
const out = {}
SLOTS.forEach((s) => { if (cfg.ids[s]) out[cfg.ids[s]] = results[s] })
return out

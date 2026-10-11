// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-d1-diff-check',
  description: 'aScoutedSeam benchmark arm D1: one read-only diff-time reuse reviewer per landed commit, up to 5 per run',
  phases: [{ title: 'Review', detail: 'one agent per diff, bounded fan-out' }],
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

const DUPS = { type: 'object', required: ['seams', 'verdict'], properties: {
  verdict: { type: 'string', enum: ['duplicates-found', 'clean'] },
  seams: { type: 'array', items: { type: 'object', required: ['path', 'symbol', 'binding', 'new_code', 'how', 'evidence'], properties: {
    repo: { type: 'string' }, path: { type: 'string' }, symbol: { type: 'string' },
    binding: { type: 'string', enum: ['MUST', 'SHOULD'] }, new_code: { type: 'string' },
    how: { type: 'string' }, evidence: { type: 'string' } } } } } }

function renderPrompt(c) {
  let trees = 'TREE (the parent revision, before the diff landed): ' + c.tree
  if (c.core_tree) trees += '\nHOST CORE TREE (incms, the platform this package installs into): ' + c.core_tree
  return [
    'You are the REUSE REVIEWER for a diff that is about to land. Your one question: does this diff RE-IMPLEMENT something that already exists in the tree? Look for a new function, component, field, helper, constant table, conf parser, CSS rule, card or stage anatomy, or hardcoded design value that duplicates an existing implementation, token or pattern the diff should have used or extended instead.',
    trees,
    'THE DIFF: ' + c.diff + ' (a unified diff with a --stat header; commit subject: "' + c.subject + '"). Read the --stat first, then the hunks that ADD code or styles.',
    'RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.',
    'For each added unit of behaviour or style, search the tree for an existing implementation of the same need. Search by concept with synonyms, across all file types including shell and CSS. Report only real duplicates: the existing seam really covers the need and is reachable from the new code.',
    'Do not report:',
    '- edits to existing code;',
    '- legitimately new capability;',
    '- tests and records.',
    'For each duplicate, give the EXISTING seam as path and symbol, plus:',
    '- binding: MUST (the diff should be rejected until it uses this) or SHOULD;',
    '- new_code: what the diff added that duplicates it;',
    '- how: how the diff should use the seam instead;',
    '- evidence: file:line.',
    'verdict: duplicates-found or clean.',
  ].join('\n\n')
}

const SLOTS = [0, 1, 2, 3, 4]
const results = await boundedParallel(SLOTS.map((s) => () => {
  const id = cfg.ids[s]
  if (!id) return Promise.resolve(null)
  return agent(renderPrompt(cfg.cases[id]), { label: 'd1:' + id, phase: 'Review', schema: DUPS })
}), 5)
const out = {}
SLOTS.forEach((s) => { if (cfg.ids[s]) out[cfg.ids[s]] = results[s] })
return out

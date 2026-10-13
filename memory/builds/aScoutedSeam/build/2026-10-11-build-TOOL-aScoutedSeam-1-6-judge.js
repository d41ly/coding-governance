// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-judge',
  description: 'aScoutedSeam benchmark: one blind judge per case grades every arm output in its packet against the ground truth, up to 5 cases per run',
  phases: [{ title: 'Judge', detail: 'one blind judge per case' }],
}

async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)

const VERDICT = { type: 'object', required: ['arms'], properties: {
  arms: { type: 'array', items: { type: 'object', required: ['label', 'covered', 'primary', 'wrong', 'valid_extra', 'score'], properties: {
    label: { type: 'string' },
    covered: { type: 'array', items: { type: 'integer' } },
    primary: { type: 'boolean' },
    wrong: { type: 'array', items: { type: 'object', required: ['seam', 'why'], properties: { seam: { type: 'integer' }, why: { type: 'string' } } } },
    valid_extra: { type: 'integer' },
    score: { type: 'integer' },
    note: { type: 'string' } } } } } }

function renderPrompt(packet) {
  return [
    'You are a BLIND JUDGE in a benchmark of reuse scouts. Read the packet file: ' + packet,
    'The packet holds:',
    '- a request;',
    '- the case tree(s), which you may open read-only to verify claims;',
    '- the GROUND TRUTH: the existing seams a build of this request should have reused, numbered from 0, each with why. Item 0 is the primary;',
    '- any DECOYS: tempting seams that are wrong for this request;',
    '- several anonymous ARM outputs, each a numbered list of seams with a binding (MUST or SHOULD) and a how.',
    'An arm with no ground truth items is a CONTROL: then judge only wrong and valid_extra.',
    'For EACH arm:',
    '- covered: the ground-truth item numbers it covers. Covering means a seam names that item, or names something that routes the build through it, so following the arm\'s instruction would reuse it. Example: a factory that wraps the item covers it. Merely naming a file that happens to contain it does not.',
    '- primary: whether item 0 is covered at MUST or SHOULD.',
    '- wrong: the seam numbers whose instruction would MISLEAD the build, with why. This covers a decoy, a lure for a different need, a stale copy where a canonical one exists, something that does not exist, or a MUST that is plainly not a reuse obligation (a file to edit, a test to keep green).',
    '- valid_extra: how many MUST/SHOULD seams outside the ground truth are genuine, correct reuse seams. Verify against the tree when unsure.',
    '- score: 1-5, how well a builder following ONLY this arm\'s output would reuse what exists and avoid reinventing. 5 = every essential seam, nothing misleading; 1 = misses the primary or misleads.',
    '- note: one sentence.',
    'Never consult git history, and never read anything outside the tree(s) the packet names and the packet itself. Judge each arm on its own; do not let arm order or length bias you.',
  ].join('\n\n')
}

const SLOTS = [0, 1, 2, 3, 4]
const results = await boundedParallel(SLOTS.map((s) => () => {
  const id = cfg.ids[s]
  if (!id) return Promise.resolve(null)
  return agent(renderPrompt(cfg.cases[id].packet), { label: 'judge:' + id, phase: 'Judge', schema: VERDICT, ...(cfg.effort ? { effort: cfg.effort } : {}) })
}), 5)
const out = {}
SLOTS.forEach((s) => { if (cfg.ids[s]) out[cfg.ids[s]] = results[s] })
return out

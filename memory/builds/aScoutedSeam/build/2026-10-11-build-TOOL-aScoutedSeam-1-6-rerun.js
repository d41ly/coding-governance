// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-rerun',
  description: 'aScoutedSeam benchmark: re-run, as child workflows, the arm agents a session limit killed, each run over at most 5 cases at the given effort',
  phases: [{ title: 'Runs', detail: 'one child workflow per declared run, bounded' }],
}

async function boundedParallel(thunks, cap = 4) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)
if (!cfg || !Array.isArray(cfg.runs) || !cfg.cases || !cfg.dir) throw new Error('args must carry runs, cases and dir')
if (cfg.effort && !['low', 'medium', 'high'].includes(cfg.effort)) throw new Error('effort must be low, medium or high')

// Each run names its arm script and at most 5 short ids; the child scripts own the agent fan-out.
const res = await boundedParallel(cfg.runs.map((r) => async () => {
  if (!r.ids || r.ids.length > 5) throw new Error('a run carries 1-5 ids')
  try {
    return await workflow({ scriptPath: cfg.dir + '/' + r.script },
      { ids: r.ids, cases: cfg.cases, effort: cfg.effort, have: cfg.have || {} })
  } catch (e) { log(r.key + ' failed: ' + e.message); return null }
}), 4)
const out = {}
cfg.runs.forEach((r, i) => { out[r.key] = res[i] })
return out

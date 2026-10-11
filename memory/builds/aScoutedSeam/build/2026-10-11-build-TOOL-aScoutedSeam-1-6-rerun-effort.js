// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-rerun-effort',
  description: 'aScoutedSeam benchmark: re-run arm workflows at one declared effort for the effort comparison; each run names its script, its case map and either up to 5 ids or one single case',
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
if (!cfg || !Array.isArray(cfg.runs) || !cfg.maps || !cfg.dir) throw new Error('args must carry runs, maps and dir')
if (!['low', 'medium', 'high'].includes(cfg.effort)) throw new Error('effort must be low, medium or high')

// A run's `single` names one case for a one-case arm (M2); otherwise `ids` names 1-5 cases.
const res = await boundedParallel(cfg.runs.map((r) => async () => {
  const map = cfg.maps[r.map]
  if (!map) throw new Error('run ' + r.key + ' names no known map')
  const a = r.single
    ? { case: map[r.single], effort: cfg.effort }
    : { ids: r.ids, cases: map, effort: cfg.effort, skip: cfg.skip || {} }
  if (!r.single && (!r.ids || r.ids.length > 5)) throw new Error('a run carries 1-5 ids')
  try { return await workflow({ scriptPath: cfg.dir + '/' + r.script }, a) } catch (e) { log(r.key + ' failed: ' + e.message); return null }
}), 4)
const out = {}
cfg.runs.forEach((r, i) => { out[r.key] = res[i] })
return out

// **Serves:** research TOOL-aScoutedSeam-1
export const meta = {
  name: 'bench-batch-all',
  description: 'aScoutedSeam benchmark: run the arm workflows (M1, M1b, M3, D1) over one batch of up to 5 cases as child workflows',
  phases: [{ title: 'Arms', detail: 'one child workflow per arm over the batch' }],
}

async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)
const dir = cfg.dir
const d1ids = cfg.ids.filter((id) => cfg.d1 && cfg.d1[id])
const ARMS = [
  { key: 'm1', path: dir + '/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1-single-scout.js', a: { ids: cfg.m1ids || cfg.ids, cases: cfg.cases } },
  { key: 'm1b', path: dir + '/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1b-checklist-scout.js', a: { ids: cfg.ids, cases: cfg.cases } },
  { key: 'm3', path: dir + '/2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-lean-scout.js', a: { ids: cfg.ids, cases: cfg.cases } },
  { key: 'd1', path: dir + '/2026-10-11-build-TOOL-aScoutedSeam-1-6-d1-diff-check.js', a: { ids: d1ids, cases: cfg.d1 || {} } },
]
const res = await boundedParallel(ARMS.map((A) => async () => {
  if (!A.a.ids.length) return {}
  try { return await workflow({ scriptPath: A.path }, A.a) } catch (e) { log(A.key + ' failed: ' + e.message); return null }
}), 4)
const out = {}
ARMS.forEach((A, i) => { out[A.key] = res[i] })
return out

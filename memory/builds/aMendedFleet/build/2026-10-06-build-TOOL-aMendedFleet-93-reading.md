# The charter A/B: the reading

**Serves:** journal TOOL-aMendedFleet-93

The result of the pair the run brief registered, `2026-10-06-build-TOOL-aMendedFleet-93-run-brief.md`,
read by the instrument it committed before either arm ran. Every figure below is printed by
`python memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-93-ab.py aggregate`
from three committed files and nothing else: `...-93-arm-a.json`, `...-93-arm-b.json` and
`...-93-judges.tsv`. Re-run it rather than trusting a number copied here.

## The table, as `aggregate` prints it

| arm | finders | skeptics | unclassified | median first-turn | judge out | precision | confirmed | refuted | blockers | highs | judge types |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 0 | 90520 | 236932 | 0.85 | 22 | 4 | 2 | 2 | workflow-subagent |
| B | 5 | 5 | 0 | 49082 | 166554 | 0.93 | 27 | 2 | 2 | 4 | Plan |

Arm A is the charter-loaded default of the day; arm B spawned every finder and skeptic batch as the
built-in read-only `Plan` type. Both arms read VALID: `exit` `complete`, no reused or dead lens or
batch, no unclassified agent, and every judge row carries a first-turn figure. `arms` reads both OK.
Every arm-B judge's meta `agentType` is `Plan` and no arm-A judge's is.

## The verdict

`verdict: DEFAULT-PLAN`

The registered rule: B's precision is at least A's minus 0.05, and B's median judge first-turn context
is at most 0.85 of A's. B's precision, 0.93, is above A's 0.85, and B's median first turn is about
0.54 of A's. Both halves hold, so spec S4 applies: `tools/workflows/tier2-review.js` takes an absent
`workerType` as `Plan`, and the literal `none` spawns as before.

The figures that do not move the word, as the rule requires them stated: arm A confirmed 22 with 2
blockers and 2 highs, arm B confirmed 27 with 2 blockers and 4 highs; the judges' summed output was
236932 tokens in arm A and 166554 in arm B. The subject's own round-1 record states raw 29, confirmed
26, refuted 3 and precision 0.90 under the harness of 2026-10-04, reported and never compared.

## What this reading cannot show

- One sample per arm. A second pair over another range could land on the other side of either
  threshold; the instrument is committed so a later build can run one.
- Precision is the harness's own confirmed over confirmed plus refuted. A higher precision in arm B
  says its skeptics refuted less of what its finders raised, not that it found more real defects;
  recall against a known set is `review_replay.py`'s question and was not asked here.
- The first-turn half measures context, not cost: a cached prefix is cheaper than a fresh one, and
  the figure sums `in`, `cache_read` and `cache_write` alike.
- Nothing here measures the drift harnesses' judges, so their default does not move.

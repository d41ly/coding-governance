**Serves:** research TOOL-dTracedLattice-1

# S2 and S3, measured — and neither lands

*Node `d`, 2026-09-06, at the commit that landed S8's harness. Both items were SPECCED as
conditional: S3 "lands only if it clears AC3's chance control", S2's two probes are "both to be
MEASURED rather than assumed". They were measured with `tools/codebase-map/rank_harness.py` over
`tools/codebase-map/scen-adversarial.json`, which is the instrument S8 landed so that this record
cites a program rather than a memory.*

## The headline

**S3 moves ONE scenario. S2's cheap probe moves ZERO. S2's expensive probe would move up to 13 and
costs 23x its own acceptance ceiling.** Nothing here is shipped, and the build is not poorer for it:
the reason each was conditional is the reason each is declined.

## S3 — the stem-specificity secondary sort key

Implemented as specced: a stem-to-file-spread map derived live from the reference index the ranking
already holds, used as a SECONDARY key between fan-in and name. Then measured against the same
ranking without it, per scenario.

| k | without S3 | with S3 | discordant pairs |
|---|---|---|---|
| 1 | 8/28 | 8/28 | 0 |
| 5 | 17/28 | **18/28** | 1 (`ADV-16`, gained) |
| 10 | 21/28 | 21/28 | 0 |
| 20 | 26/28 | 26/28 | 0 |

Exactly one scenario's rank moves at all. **AC4 forbids reporting a delta with fewer than 6
discordant pairs as a finding**, and one is one. The key is not wrong — it gains where it acts — it
is unmeasurable on this set, which is the state the spec anticipated when it made S3 conditional.

The implementation is not kept. A ranking term whose effect cannot be distinguished from noise is
one more thing to reason about at every future change, and the code is three functions recoverable
from this record's own description.

## S2 — the behaviour-phrase to seam bridge

S2 rests on a premise the spec states as "17 of 17 misses on the adversarial set fail on an EMPTY
STEM INTERSECTION between the phrase a session types and the symbol's name". **The population
reproduces exactly — 17 of the 28 rows have no stem in common between query and symbol name — and
the CONSEQUENCE does not.** With the tool as it stands, 16 of those 17 are reachable; only `ADV-18`
(`main`) misses at every depth. The structural-neighbour widening finds them. What they are is badly
RANKED, not absent: 11 of the 17 sit below rank 5.

That is a correction to the spec's framing, and it makes S2 a ranking item rather than a recall item.
It also raises its ceiling above AC4's floor, so it was worth measuring rather than declining on the
premise alone.

**Probe 1, stem PREFIXES for names not otherwise matched: 0 of 17.** Measured at a 4-character
minimum in both directions. The gap is semantic, not morphological — the query for `subtokens` stems
to `camel · cas · identifi · lowercas · piec · snak · split · word` and the name stems to
`subtoken`. No prefix rule reaches that, at any minimum length, because there is no shared prefix to
find. Refuted, and cheaply.

**Probe 2, the docstring first line: 13 of 17 reachable, and it fails AC8 on cost.**

| reading | symbols with a first line | cost | agreement with `ast.get_docstring` |
|---|---|---|---|
| `ast.parse` per file | 613 | **1.1665 s** | exact, by construction |
| regex over text the walk already reads | 563 | **0.0508 s** | 447 of 638 (70%) |

A whole `reuse_lookup` run costs 1.162 s. **AC8's ceiling is 0.05 s added.** The faithful reading
costs 23x that and doubles the command; the cheap reading is still over the ceiling AND disagrees
with the truth on 30% of docstrings, which is a probe that would move the ranking for reasons its
author cannot predict. Neither is landable under the criterion this unit already wrote.

The four rows the docstring probe does not reach carry NO docstring at all — `search`, `check`,
`run`, `main` — which is the adversarial set doing its job: the one-word generic names are also the
undocumented ones.

## What this leaves open, stated rather than filed

The bridge is REAL: 13 of 17 otherwise-unreachable-by-name rows are reachable through one line of
prose that already exists in the tree. What blocks it is that deriving that line at query time costs
more than the unit's own cost ceiling allows. The obvious next move is the one this unit's §3 does
not authorise — carry the first line in `symbols.json` at `gen_map.py --write` time, paying the
1.17 s once per regeneration instead of once per query. That is a committed-artifact decision
`AGENTS.md` §12 governs, and it needs a unit that argues it rather than a measurement that implies
it. Recorded here per the build README's rule that findings ride specs rather than new backlog rows.

## Reproduce

```bash
python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json
python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json --control shuffle --k 5
python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json --control constant --k 20
```

The per-scenario and cost figures above came from short scripts over `rank_harness`'s own
`measure_ranks`, `map_lib.stems` and `symbols.json`; the harness is the part worth keeping and it is
tracked, which is the whole of S8.

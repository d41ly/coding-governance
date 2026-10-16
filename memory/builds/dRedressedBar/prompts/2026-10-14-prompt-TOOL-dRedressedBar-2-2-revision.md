# Revision — dRedressedBar: TOOL-dRedressedBar-2, the builder's divergence on the stale symbol map

**Serves:** research TOOL-dRedressedBar-2

## The brief

### Goal
DIVERGENCE: spec memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md §3 Edges (the hands-off to TOOL-dRedressedBar-10) says `memory/map/generated/symbols.json` "reads that map stale until unit 7 regenerates it". §4 Files touched names only `tools/unattended/gate-guard.js`. The repository won't commit that design. `.githooks/pre-commit:233-246` runs the codebase-map gate on any staged .js file. Its `test_generated_artifacts_are_fresh` refused the commit with `STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write` and asked for the rewritten map to be staged in the same commit. The spec as written can only land through `--no-verify`, which is routing around the hook. The other route writes `symbols.json`, a shared generated index that the spec gives to unit 7 and that is outside this unit's declared write set. Units 2 and 9 could then run concurrently with overlapping write sets, against M6 clause 3, because unit 9 also mints `check_outcome_states` in a mapped file. To be buildable, the spec would need what this build's specs 15 S8 and 19 §4 already say for their own new functions: (a) a scope item where the pass runs `python tools/codebase-map/gen_map.py --write` alone before the product commit, and the commit carries `memory/map/generated/symbols.json`, with `renderAskQuote` listed and no `clean` entry for gate-guard.js; (b) that path added to §4 Files touched and to S4's Readers; (c) the §3 Edges sentence saying the map reads stale until unit 7 replaced, since unit 7's `regen.py --write` will then find it fresh. Unit 10's S17 and AC14, which are written to put the 'stale until unit 7' note into spec 2, and spec 9's matching note for `check_outcome_states` have the same defect. The spec writer should fix them in the same revision.

### Items
1. **TOOL-dRedressedBar-2** — revise to rev-3 as the goal states: (a), (b) and (c).
2. **TOOL-dRedressedBar-9** — the same correction for its `check_outcome_states` note: its pass regenerates `symbols.json` and commits it. Bump its rev.
3. **TOOL-dRedressedBar-10** — S17 and AC14 stop writing the "stale until unit 7" note into spec 2. Bump its rev.
4. Every other spec in this build whose unit adds, renames or removes a function in a mapped file: check it states the same regenerate-and-commit step, and fix any that does not. Units are built one at a time, so the shared index never has two writers at once (M6 clause 3).

### Acceptance
Each revised spec's §4 Files touched names `memory/map/generated/symbols.json` where its unit moves a mapped function. No spec in the build says the map stays stale until unit 7. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades every revised unit READY.

### Gates
`codebase-map coverage + freshness` · `memory hygiene` · `lexicon naming predicates` · `lexicon wiring`

### Non-goals
- No code.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix.
- No merge to local main and no push without the owner's ask.

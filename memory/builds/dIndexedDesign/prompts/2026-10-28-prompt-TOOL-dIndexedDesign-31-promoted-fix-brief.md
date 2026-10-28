**Serves:** research TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38

# Fix brief — dIndexedDesign, the round-1 promotions' check findings before their commit

The round-1 spec audit of `unattended-build.js` run `wf_04992eff-9a3` (record
`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`) promoted its
findings into eight new specs, `TOOL-dIndexedDesign-31` to `-38`, under `memory/builds/dIndexedDesign/spec/`. The main
loop ran the memory hygiene gate and `tools/check-spec-tokens.py` over the staged set, and the findings below are the
whole remainder. Fix each in the file it names, and nothing else. The promoted specs are uncommitted rev-1 drafts: edit
them in place, with no rev bump and no §9 line. Do not commit, do not run the build-index generator, and do not edit
any of the seventeen round-1 specs.

Read `memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first; each finding below breaks one of its rules.

## check-spec-tokens — guarded legs absent from the §7 leg line

1. Each path below in the spec's §4 Files touched trips a merge-bar leg's guard, and the spec's §7 leg line does not
   name that leg. Add each leg, spelled exactly as quoted (check it against `tools/gate-legs.json`), to that spec's §7
   leg line:
   - `TOOL-dIndexedDesign-31`: `verifier fan-out self-test`, `tier2-review self-test`, `unattended-build self-test`
     and `review-join self-test` (all from `tools/workflows/replay_scorer.py`).
   - `TOOL-dIndexedDesign-37`: `tier2-review self-test` (from `tools/memory-tree/gen_build_index.py`).

## check-spec-tokens — an example path read as a citation

2. `TOOL-dIndexedDesign-37` line 141 lists example inputs in backticks, among them `tools/x.sh`, which the checker
   reads as an untracked path. Spell the examples so they are not path-shaped tracked-looking tokens (for example
   `<dir>/<file>.sh`), keeping the list's meaning; leave `README.md` and `.gitattributes`, which are tracked.

## Hygiene check 12 — an acceptance criterion naming no backticked witness

3. `TOOL-dIndexedDesign-38` AC18 (line 392) names no backticked witness, which check 12 requires at or after
   `SPEC_WITNESS_CUTOFF`. Give it the command or file a pass observes, in backticks, as the other criteria of that spec
   do. Its suite stays on the `New arm:` line at 425; the witness is a probe of the unit's own code, never the suite.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against a private copy of the git
index in your scratch path, and return each finding fixed, by number, with the file and the change.

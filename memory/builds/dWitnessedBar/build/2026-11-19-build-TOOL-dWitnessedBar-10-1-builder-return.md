**Serves:** journal TOOL-dWitnessedBar-10

# TOOL-dWitnessedBar-10 — builder return 1 (run `wf_67f96040-d61`), a divergence, nothing committed

## Why

DIVERGENCE: the spec (rev-3, base cdfbd1cf) can't be built as written against the tree at 6202ffeae. The pre-commit hook has gained blocks since the spec's base that S4 and AC1 don't account for, and the Files touched list leaves out the files where the five legs are declared.

(1) S4 / §4 "The five" contradict AC1 because of a landed behaviour. TOOL-aTrimmedWait-3 (634815f08, 2026-11-14) and TOOL-aTrimmedWait-10 added a render step to the hook's memory-hygiene block (.githooks/pre-commit (line 286-309 at 6202ffeae)). When `check-memory-hygiene.sh --staged` fails on a a hygiene check-9 failure line, the hook runs `gen_build_index.py --write-staged` and then grades the leg again. Its arms are .githooks/pre-commit.test.sh (line 322-370 at 6202ffeae) (aTrimmedWait-3 AC5/AC6). The derived argv `bash {prefix}/memory-tree/check-memory-hygiene.sh --staged` that precommit.py would run can't render and regrade. AC1 requires `grep -c check-memory-hygiene.sh .githooks/pre-commit` to print 0, so the block can't stay in the hook either. The spec has to choose one of three: the render moves into precommit.py (or into the hygiene leg's own `--staged` mode); the render is deliberately dropped, with its arms retired; or the hygiene row stays hand-named and AC1's grep changes.

(2) S4 doesn't cover the red-fix join block. TOOL-aNimbleMend-15 S12 (64439c8dd) added it at .githooks/pre-commit (line 310-326 at 6202ffeae), with arms at pre-commit.test.sh (line 283-318 at 6202ffeae). It is the `else` arm of the hygiene block's `st_memory` trigger and runs `build_records.py join red-fix --staged` when no memory path is staged. S4 neither keeps nor removes it. That also contradicts S4's Readers line ("NO VALUE READERS of the five triggers beyond the suite"), because this block reads `st_memory` inside the hook. The spec has to say whether it is deleted (hygiene `--staged` would run check 31 at every commit) or kept with a trigger of its own.

(3) Files touched is missing paths the change needs. S2 puts `precommit` in the five legs' declarations, and `leg_factory.py --list` places them in tools/memory-tree/kit.toml, tools/govkit/entries/kickoff-manifest.kit.toml, tools/unattended/kit.toml, tools/codebase-map/kit.toml and tools/govkit/registry.toml (template size <=48KiB). None of the five is listed. The precedent for each new LEG_KEYS key also includes a run-gates kit version bump in the run-gates.sh header and a govkit selftest arm for the new LEG_KEY_FLOORS row (tools/govkit/selftest.py (line 2815-2835 at 6202ffeae), TG1/PU1). selftest.py is not listed either.

(4) Some citations are stale (no design change needed, but they should be fixed in the same revision). `check_guard_trips` is at tools/memory-tree/design_lib.py (line 642 at 6202ffeae), not check-spec-tokens.py. Line numbers have moved:
- .githooks/pre-commit (line 179-260 at 6202ffeae) is now about :286-399
- .githooks/pre-commit (line 249-256 at 6202ffeae) is now :388-397
- .githooks/pre-commit (line 221 at 6202ffeae) is now :361
- run-gates.sh (line 224-226 at 6202ffeae) (`--regen`) is now :382-384
- run-gates.sh (line 2766-2773 at 6202ffeae) (the prior read) is now about :2924-2930
- kit.toml (line 67-69 at 6202ffeae) is now :72-74

The other claims hold: LEG_KEYS at run-gates.test.sh (line 354 at 6202ffeae) read by both canary arms; LEG_KEY_FLOORS at govkit.py (line 5943 at 6202ffeae); `or "a"` at derive-ceilings.py (line 526 at 6202ffeae); `--observed`'s GOV_NODE refusal at :566-574; the runner's max-per-leg prior read; `resolve_prefix_token` inlined; `held_halves.load_manifest`; profile_bar `--scoped`/`--out`; both test_codebase_map copies; and all five legs unguarded in tools/gate-legs.json.

## Summary

I stopped before writing any code and committed nothing: the spec needs revising before TOOL-dWitnessedBar-10 can be built. Base is 6202ffeae9a3d691da56cd09022bc69d593c64b9, and the worktree is unchanged.

The main problem is in the pre-commit hook. Since the spec's base it has gained two blocks the spec doesn't mention:
- **Check-9 render (TOOL-aTrimmedWait-3/-10):** when the memory-hygiene leg fails on check 9, the hook renders the build index, stages it and grades again. The single derived command the spec puts in its place can't do that, and AC1 forbids keeping the block in the hook.
- **Red-fix join (TOOL-aNimbleMend-15):** it runs only when no memory path is staged, and S4 neither keeps nor removes it.

The Files touched list also leaves out the five files where the five legs are actually declared, plus the govkit selftest arm the new key's floor row would need. A few line and function citations are stale. Full details are in `why`.

**What I checked (read-only, no gate):**
- `leg_factory.py --list`, to find where each of the five legs is declared.
- `tools/gate-legs.json`, to confirm all five legs have no guard.
- greps and reads over `.githooks/pre-commit`, `.githooks/pre-commit.test.sh`, `run-gates.sh`, `run-gates.test.sh`, `govkit.py`, `derive-ceilings.py`, `profile_bar.py` and `kit.toml`.
- `git log cdfbd1cf..HEAD -- .githooks/pre-commit`, which dates the hook changes after the spec's base.

These checks don't stand in for any gate. They are the spec-buildability check my role requires before the first edit. No gate, suite or bar ran.

**Not done:**
- I didn't run the `--brief` record, because it writes to RUN.md and this pass must leave nothing uncommitted. It should run when the unit is dispatched again.
- No `--dispatch` widening was needed.
- `gotchas.py --for-diff` didn't run, because there is no commit.

**Still owed:** the main loop's RED-first observation of both `New arm:` lines (`.githooks/pre-commit.test.sh` and `tools/run-gates/run-gates.evidence.test.sh`). It applies once the revised spec is built.

# Fix brief — TOOL-dFairHearing-25: two clone-only paths the token check grades as untracked

**Serves:** research TOOL-dFairHearing-25

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Make `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md` rev-6 pass `python tools/check-spec-tokens.py`. It exits 1 on two §6 path tokens, both clone-only paths that no tree here will track: `memory/builds/dFairHearing/replay/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` (AC1) and the flat `memory/builds/dFairHearing/replay/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` (AC3). The paths join grades every backticked word of a §6 bullet (`tools/check-spec-tokens.py:1630-1647`) unless it opens with one of the `NOT_A_TOKEN` prefixes (`tools/memory-tree/design_lib.py:529`: `GATE_`, `{{`, `$`, `~`, a quote, `<`). Commit nothing; the main loop commits.

### Items
1. Re-spell both tokens in §6 so the join does not grade them and the criterion still says exactly which path it means, for example a `<clone>/` prefix for a path read inside a clone. Do not add waiver rows: `memory/project/spec-token-waivers.txt` is shrink-only.
2. Check every other backticked word of §6 against `check_path_shaped` (`tools/check-spec-tokens.py`) and the tracked tree, so no third hit is left.
3. Rev bump and one §9 line, naming AC1, AC3 and this brief. Leave the status header's state as it is.

### Acceptance
No §6 token of the spec is a path-shaped word the tree does not track; the criteria read the same paths as rev-6.

### Gates
None you run.

### Non-goals
No other change to the spec, no other file.

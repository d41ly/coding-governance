# Fix brief — TOOL-dFairHearing-27: the gotchas render and its committed index in separate commits

**Serves:** research TOOL-dFairHearing-27

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md` so its build can be dispatched. The builder's return is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-27-1-builder-return.md`: `--dispatch` refuses with check 49 because §4 Files touched pairs `memory/gotchas/INDEX.md` with its generator `tools/memory-tree/gotchas.py` (S29 rewords `render()`), the one pairing M6 condition 3 forbids (`tools/unattended/unattended.sh`, the comment above `fail 49` and its call). Commit nothing; the main loop commits.

### Items
1. Read the memory hygiene gate (`tools/memory-tree/check-memory-hygiene.sh`, check 17, the gotchas index freshness) and say whether, under the pre-commit hook's `--staged` mode, it refuses a commit that stages `gotchas.py` with a changed `render()` while leaving `memory/gotchas/INDEX.md` unstaged. Cite the lines.
2. If it does not refuse: take `memory/gotchas/INDEX.md` out of §4 Files touched, and state in §4 that the main loop's records commit right after this unit's pass re-renders it (`gotchas.py` with the flag that writes the index), a shared render this build's README rule 6 allows. Re-word AC24 so it observes INDEX.md at that records commit, and its red case stays a red case.
3. If it does refuse: say so, and propose the smallest route — for example S29's `render()` reword in its own unit whose pass writes `gotchas.py` alone, with the index re-rendered by the main loop the same way — as a §8 fork marked by M3 and resolved, delegated, with the reason.
4. Fold in the builder's three findings where the spec does not already state them: AC11 needs `MAX_LENSES` removed from `tools/hooks/agent-cap.js` itself, its definition and its export, not only from its readers; AC8 / S13's existing `agent-cap.test.sh` arm "pack AC1" expects `govkit update --kits review-harness`, which becomes the `apply` spelling; AC22's three key-pinning arms need `// ---- ` headers naming `REVIEW_SHAPE` for the probe's second half to print them. Check each against the tree, and §7's leg line against the guards §4's files trip.
5. Rev bump and one §9 line per change, each naming a section, scope or acceptance id, and this brief. Leave the status header's state as it is.

### Acceptance
§4 Files touched pairs no generated index with its generator; every criterion a correct build can pass; the return states item 1's answer with its lines.

### Gates
None you run.

### Non-goals
No design change beyond the items, no other spec, no code.

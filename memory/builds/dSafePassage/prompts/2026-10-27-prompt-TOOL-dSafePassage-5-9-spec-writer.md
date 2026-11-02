**Serves:** research TOOL-dSafePassage-5

# Brief: TOOL-dSafePassage-5's fifth build pass — a killed step whose first write is its whole effect re-runs as `applied` by its witness

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-5 back as a DIVERGENCE a fifth time (`wf_000123e7-8a5`, HEAD `293ce573d`), and the run revises the spec under M2.

## The brief

### Goal

AC7 and the `kill` row of §4 "### The cases" expect what TOOL-dSafePassage-33 S1 declares for a re-run whose killed step's witness already holds, so TOOL-dSafePassage-5 builds green.

**What the builder measured.** Every case except one and every arm are green on rev-10, and the kept patch is `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-5-wip5/tool5-pass5.patch` (logs in `logs-pass5/`, the probe log `uw5-pass5/probe_kill_schema.log`). The one red: `kill` on `govkit/receipt-schema-4`. Its shadow up changes only `.governance/install.json`, so that file is both its first write and its whole effect. The killed state holds the schema-4 receipt, so the re-run finds the witness passing and records `{"id": "govkit/receipt-schema-4", "state": "applied", "via": "witness"}` where `up` records no `via`. `steps` is the only receipt key that differs. The rollback from that killed state reached release-0's digest.

**The disposition, decided by the main loop.** This is not a defect. TOOL-dSafePassage-33 S1 (CLOSED) and `tools/govkit/upgrade_steps.py:57` and `:680-704` declare that a step applied by its witness alone, its up never spawned, carries `"via": "witness"`. The re-run did exactly that. Unit 5's expectation changes: the `kill` case's re-run compare expects `"via": "witness"` on the killed step's row exactly when the killed state's witness holds, and no `via` otherwise. Every other byte still equals `up`'s under S4's readings. Cite TOOL-dSafePassage-33 S1.

### Items

1. **Revise TOOL-dSafePassage-5** as rev-11, dated 2026-10-27 and still `DEFERRED`. Change §4 "### The cases" `kill` row, AC7 and its Red-when as above. AC7 must still red when a step's re-run differs in any other way, or carries `via` when the killed state's witness did not hold. One §9 line names this brief. Touch nothing else: the spec is over its warn budget.
2. **Cross-read** TOOL-dSafePassage-33, -39 and -40 on the `via` mark. Report a contradiction in a CLOSED spec rather than editing it.
3. **Commit nothing.** Return the file you wrote.

### Acceptance

- AC7 names `via`, the witness condition and TOOL-dSafePassage-33 S1.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your file staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, no new unit, no edit to a CLOSED spec.
- No commit and no stage into the real index.

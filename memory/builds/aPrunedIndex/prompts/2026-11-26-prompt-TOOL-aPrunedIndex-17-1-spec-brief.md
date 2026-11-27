# Spec brief: TOOL-aPrunedIndex-17, cheaper tag plants

**Serves:** research TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-10

## The prompt

> Make plants cheaper

The owner gave this answer in the building session, 2026-11-26, to "How should the tag-plant self-test leg's cost be
handled before landing?". The leg is `tags bundle selftest` (`python tools/playbook/tag_bundle.py --selftest`, ceiling
300 s). At `22c3e175d` it passed in 521 s wall on node a under other sessions' load. That is over its 159 s budget row (PINNED, 2026-11-26)
and its 300 s ceiling. Round 2 of the closing review, id 1, owns the finding: (PINNED, 2026-11-26)
`memory/builds/aPrunedIndex/reviews/2026-11-26-review-TOOL-aPrunedIndex-4-10-diff-review-round2.md`. Before this build
the leg took 22 s. Unit 4's five plants (`dead-versions`, `named-probe`, `released-rows`, `released-cost`, (PINNED, 2026-11-26)
`gc-predates`) took it to 106 s on a quiet node. (PINNED, 2026-11-26)

## What the main loop measured (cProfile, node a, 2026-11-26, loaded)

- `--fixture --plant released-rows`: 189 s wall. (PINNED, 2026-11-26)
  - 332 child processes; `_winapi.CreateProcess` alone took 124 s, about 0.37 s per spawn. (PINNED, 2026-11-26)
  - `tag_index.read_git` was called 255 times and its sibling at `tools/playbook/tag_index.py@4d1a9ef3:614` 186 times.
  - `load_index` was opened 69 times. Each open spawns `git rev-parse --git-common-dir` through
    `derive_index_path` / `common_dir`, for 37 s. (PINNED, 2026-11-26)
  - 17 `check_step` calls took 67 s. 22 kit verbs took 85 s. (PINNED, 2026-11-26)
  - `import_walk` scans (the extractor version hash, re-derived per verb) took 13 s. (PINNED, 2026-11-26)
- `--fixture --plant gc-predates`: 92 s wall. (PINNED, 2026-11-26)
  - 153 spawns, 56 s of it in CreateProcess. (PINNED, 2026-11-26)
  - 10 `run_gc` calls took 29 s. Each `read_live_versions` lists the worktrees and probes each HEAD. (PINNED, 2026-11-26)
  - `measure_version` opens `load_index` (one git spawn) for every count.
- The profile files are under the session scratchpad, `prof-released-rows.pstats` and `prof-gc-predates.pstats`.
  `tag_bundle.run_selftest` runs each plant in its own subprocess, one after another.

## The brief

- **Goal.** Make the leg fit its 300 s ceiling under the load measured above, with headroom. (PINNED, 2026-11-26)
  - The target is the five new plants together at no more than about 40 s on a quiet node, from about 84 s. Then a (PINNED, 2026-11-26)
    5x load factor (521 / 106) keeps the leg under 300 s. (PINNED, 2026-11-26)
  - Choose and justify the design. Candidates:
    - fewer `load_index` opens per plant, for example one connection or one resolved index path held across a
      plant's counts;
    - fewer verb runs per plant, merging steps whose assertions can share one run;
    - reusing a built fixture across steps instead of rebuilding;
    - running the bundle's plants concurrently under a declared bound.
  - Measure each candidate you keep.
- **Every verdict stays.** Each plant keeps its exit, its last line and every assertion it makes today. A merged step
  must still distinguish what each of its predecessors distinguished.
  - Every staged break already recorded for these plants must still red. That is 27 in unit 4's seen-red lines and 2 in
    unit 10's. The main loop re-observes them at the close.
  - Name every plant you change in a `New arm:` line, or in a re-observation line if the arm is unchanged in kind.
- **Concurrency, if chosen.** Declare its bound in one place. Keep the output's row order and bytes deterministic. State
  what a worker's crash prints.

## Cut-line

- No edit to `tools/playbook/tag_index.py`, nor to any module in its import closure (`backlog`, `coverage_join`,
  `design_lib`, `id_grammar`, `import_walk`, `legacy_ledger`, `policy_value`, `tag_index`, `tree_lib`). Any such edit
  re-versions every extractor and forces a full re-parse on every node.
  - A cache of `derive_index_path` or `read_git` inside `tag_index.py` is therefore out.
  - A cache in the plants' own code is in.
- No ceiling or budget moves up. After the change, re-time the leg and rewrite the `tags bundle selftest` budget and
  evidence rows from the new readings, by unit 4's AC8 method. Take at least three readings, and say what load each ran
  under.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` stay untouched.
- Tier: 2. The change rewrites test arms that certify what `--gc` and a build delete.

## Owner confirmation

Asked: Which scope do you approve for making the tag plants cheaper? (unit 17 plus the pool as a second unit, or unit 17 only)
Answer: Unit 17 plus pool

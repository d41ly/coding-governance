**Serves:** research TOOL-dSafePassage-5

# Brief: TOOL-dSafePassage-5's fourth build pass — descriptors read at the tip, the held kit's exit, and a killed walk that leaves a held kit at the tip

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-5 back as a DIVERGENCE a fourth time (`wf_078fb144-02f`, HEAD `98a01d518`), and the run revises the spec under M2.

## The brief

### Goal

TOOL-dSafePassage-5 builds green: each of the four things its fourth pass measured has one disposition in the spec set. A disposition is a spec change in unit 5, a cited normalization, or a defect owned by a new unit ordered before unit 5.

**What the builder measured.** The pass built rev-9 whole from the kept work. `up`, `plants`, `skip`, `fail`, `shims` and `isolation` are green, and `reup`'s digest equals `up`'s. Everything is kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-5-wip4/`: `tool5-pass4.patch`, `files/`, `probe_up.py`, `probe_down.py`, `rdiff.py` and `logs-pass4/`. Read them.

1. **`down` is red at `.governance/install.json`.** The `withdraw-one` row `tools/hooks/README.md` reads `retired-edited`, where release-0 recorded `engine`. TOOL-dSafePassage-64's re-resolution does not fire, because `_cmd_update` reads descriptors from the gov checkout's working tree (`read_descriptors(root, ...)` at `tools/govkit/govkit.py:9521`, `resolve_entry(root, ...)` at `:10145`), not at `--to`. S2 keeps the clone at the tip, where the gov plant removed the rule. Measured: the same up tree, rolled back with the clone checked out at HEAD and no gov plants, matched release-0 exactly. Decide from the code and the records (`help/`, the update and rollback specs, DEPL records) which is true:
   - (a) A rollback is documented as run from a gov checkout at the pin. Then S2's clone handling is the spec's error: unit 5 checks the clone out at the pin for each `down`.
   - (b) `update --to` promises the `--to` revision's descriptors. Then reading the working tree is a defect owned by a new unit.
   - (c) TOOL-dSafePassage-64 §4's assumption is simply wrong, and unit 5's expectation changes.
2. **The held kit's exit.** Since TOOL-dSafePassage-63, the `edited-render` plant is `ordered`. Every walk's `update` then holds the lexicon kit back, exits 1 with "1 problem(s)", and withholds the stamp (`gov_commit` stays at the pin). §4 "The cases" and S6 must say how the cases read that exit and the withheld stamp. The patch carries the builder's measurement-only `check_walk_exit`. Weigh it, along with the alternative of running the `edited-render` plant in its own case so the walk cases stay exit 0.
3. **`kill` is red for all three steps** at `install.json`, `install.sums`, and the bytes and index of `tools/lexicon/adopt-lexicon.sh`. The held kit's writes are rolled back only in update's verify phase (`govkit.py` ~`:12626`), after the step walk (~`:11781`). TOOL-dSafePassage-62's receipt, written before the first step, records them at the tip. So a walk killed inside a step leaves a held kit's files at the tip, and its rollback cannot return them. This is gotcha class `verdict-printed-before-the-step-that-reverts-it`. It is a defect unless a record says otherwise. If item 2 takes the held kit out of the kill case's tree, say whether the defect still reaches adopters, and own it in a new unit either way.
4. **AC14's grep** also prints three local `build_target` helpers that already exist: `tools/govkit/upgrade_steps.py:2419`, `tools/govkit/fixtures/retired_edits.py:152`, and `tools/govkit/selftest.py:1252` and `:2408`. The kept patch had bound two of them to the factory's name, so they recursed. Say whether AC14 counts them, or rename them in the Files touched.

### Items

1. **Disposition each of (1) to (4)** by the rev-8 rule. A field is normalized only where a record declares it output-only or re-derived and that record is cited. Otherwise it is a defect.
2. **Each defect gets a new unit** at the next free id, TOOL-dSafePassage-65 onward. Each is Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14` and `order 5`, `**Derived:** TOOL-dSafePassage-5` as -63 and -64 are, with one mechanism, a `New arm:` line and a README `roster:units` row.
3. **Revise TOOL-dSafePassage-5** as rev-10, dated 2026-10-27 and still `DEFERRED`, with `consumes-from` on each new unit. One §9 line names this brief. Add only the prose the dispositions need: the spec is 59 KB, over its 49152-byte warn budget.
4. **Cross-read** TOOL-dSafePassage-26 and -61 (consumers of 5) and TOOL-dSafePassage-2, -62, -63 and -64. Fix a DEFERRED spec in place, with a rev bump and a §9 line. A CLOSED spec is read-only: report any contradiction in it.
5. **Commit nothing.** Return the files you wrote and each item's disposition.

### Acceptance

- Each of (1) to (4) has one named disposition, backed by code lines or a cited record.
- Each new unit's spec is conforming: status header, `**Derived:**` line, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit, no stage into the real index, and no RUN.md row: the main loop runs `--rescope`.
- No redesign of the cases that are already green.

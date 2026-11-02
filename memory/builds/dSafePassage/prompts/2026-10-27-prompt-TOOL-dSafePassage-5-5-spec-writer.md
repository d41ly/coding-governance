**Serves:** research TOOL-dSafePassage-5

# Brief: TOOL-dSafePassage-5's third build pass — the lost render edit becomes TOOL-dSafePassage-63, and the kill, role, plant and index findings are disposed

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-5 back as a DIVERGENCE (`wf_0d024041-1eb`), and the run revises the spec under M2.

## The brief

### Goal

TOOL-dSafePassage-5 builds green on the shipped walk: each of the five things its third build pass (`wf_0d024041-1eb`, HEAD `29665dd17`) measured has exactly one disposition in the spec set. The disposition is a spec change in unit 5, a cited normalization, or a defect owned by a new unit ordered before unit 5.

**What the builder measured** over real release-0 trees. The work-in-progress unit is kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/TOOL-5-wip/`, with case logs `uw5b-*.log` and `uw5-*.log` beside it. Read them. `up`, `isolation`, `shims`, `fail` and `skip` are green. `plants`, `down`, `reup` and `kill` are red:

1. **`edited-render` plant: the adopter's edit is lost.** The pinned `apply` writes every `rendered` row without an `oid` and records only `output_sha256` (pinned govkit.py:8162). `check_render_edited` (`tools/govkit/govkit.py:9382-9393`, TOOL-dSafePassage-9 S5, CLOSED) returns False when a row has no `oid`. So the first `update` re-renders `.claude/skills/lexicon/SKILL.md` over the edit, writes no order, and the edit is gone. That is an adopter-facing defect for every install rendered before `oid` existed. The same root cause makes `down` differ at that file. It also makes `kill`'s re-run differ from `up`, because after a kill the receipt TOOL-dSafePassage-62 writes carries the `oid`.
2. **`derive_first_write` ties.** The fanout-cap step's two writes (`.governance/policy.toml` and its before-image) carry identical `mtime_ns` on this node. The unlinked `.agent-cap.conf`, timed by the root directory's mtime, sorts before both. So the "first write" the kill case applies is really the step's last, and the case reaches a state the step's real write order cannot.
3. **`role` after `down` with `withdraw-one`.** The receipt row `tools/hooks/README.md` reads `retired-edited` where release-0 recorded `engine`.
4. **Plant vocabulary.** The `retired-edited` order appears only when gov's source file is also removed, so `[[gov_plant]]` needs a `remove` edit kind beside append, replace and create.
5. **Index compare.** The receipt's and the sidecar's index entries differ by blob id whenever their contents differ only in S4's normalized fields. The index compare reads those two entries by mode and stage only.

### Items

1. **(1) is a defect: author TOOL-dSafePassage-63.** Make it Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 5`, carrying `cl-dClosedLoop-0022` as TOOL-dSafePassage-62 does. Its one mechanism: `check_render_edited` proves an edit from the row's recorded `output_sha256` when `oid` is absent. Read what `output_sha256` measures (raw bytes or cleaned) at today's apply and update writers and at the pinned one, and make the fallback compare like with like. If it cannot prove an edit soundly, say so in §8 as a fork, with the recommendation. Add an acceptance criterion on a planted no-`oid` receipt and a `New arm:` line. TOOL-dSafePassage-9 is CLOSED and read-only, so 63 cites it as the seam it extends. Add 63's row to the README `roster:units` table, with `**Derived:**` set to the build-run divergence.
2. **(2): unit 5 states how the first write is found.** It cannot rely on mtimes alone. Derive the order from something the step's real up determines, read from `tools/govkit/upgrade_steps.py` and the fanout-cap step's up. If nothing does, the kill case may kill by running the step's up in the child walk and stopping it after its first write lands, observed by the walk itself. Pick one, verified against the code, and record why.
3. **(3): disposition by the rev-8 rule.** A field is normalized ONLY where a record declares it output-only or re-derived per run, and that record is cited. Otherwise it is a defect, owned by a new unit at the next free id with the same header as item 1. Read where update's file pass and the step downs set and restore `role` before deciding.
4. **(4) and (5): unit 5's text.** Add `remove` to the `[[gov_plant]]` vocabulary and have the `withdraw-one` plant use it. Make the index compare read the receipt and sidecar entries by mode and stage only, stating why.
5. **Revise TOOL-dSafePassage-5** as rev-9 dated 2026-10-27, still `DEFERRED`, with `consumes-from` on 63 and on any other new unit. AC3, AC5, AC7 and AC12 change only as the dispositions decide. One §9 line names this brief. The spec is already over its 49152-byte warn budget, so add no prose beyond what the dispositions need.
6. **Cross-read** TOOL-dSafePassage-26 and -61, which consume unit 5, and TOOL-dSafePassage-9 and -62. A DEFERRED spec that disagrees is fixed in place, with a rev bump and a §9 line. A CLOSED spec is read-only: report any contradiction in it.
7. **Commit nothing.** Return the files you wrote and, for each of (1) to (5), its disposition and the record or unit behind it.

### Acceptance

- Each of (1) to (5) has one named disposition.
- No normalization stands without a cited record.
- TOOL-dSafePassage-63's spec is conforming: status header, Carries, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code.
- No edit to a CLOSED spec.
- No commit, no stage into the real index, no RUN.md row: the main loop runs `--rescope`.
- No redesign of the green cases.

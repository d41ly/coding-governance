**Serves:** research TOOL-dSafePassage-5

# Brief: TOOL-dSafePassage-5's upgrade-walk leg found rollbacks that do not restore release-0 — each difference dispositioned, each defect given a unit

## The prompt

No owner prompt: the build run's second builder of TOOL-dSafePassage-5 (`wf_63a25607-fc3`) handed it back as a DIVERGENCE after measuring the real release-0 tree, and the run revises the spec set under M2 and M3, its delegated scope.

## The brief

### Goal

Every byte difference the builder measured between a rolled-back tree and release-0 has exactly one disposition in the spec set — a declared output-only or re-derived field normalized in the leg's comparison with its owning record cited, or a defect in the walk or rollback owned by a new unit, ordered before TOOL-dSafePassage-5, that makes the rollback restore it — so unit 5 builds green on the shipped walk and clause `cl-dClosedLoop-0022`'s "down byte-identical" means what it says.

**What the builder measured** at HEAD `41062397` (probe scripts kept at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/probe_r0.py`, `probe_walk.py`, `probe_down.py`, `probe_kill.py`; read them):
- **Release-0 now builds.** The pinned clone (`git clone --no-tags`, checked out at `60d90cb7`) applied the rev-7 `kits` line (23 kits) with the rev-7 answers and seeded AGENTS.md: exit 0 in 33 s, a schema-3 receipt, lf_pin notes only.
- **AC1's order** holds only while the clone's `main` is gov's landed ref (`origin/main`); with the clone's own default branch as tip, `agent-cap/fanout-cap-to-agents-in-flight` (29ccb065) walks first.
- **`update --to <HEAD> --write`** exited 0 in 151 s: the schema step applied; the floor and fanout-cap steps were skipped because their witnesses already hold at release-0.
- **(1) `down` (AC3):** after a clean committed up, `update --rollback --to <pin> --write` exits 0 and rolls back all three steps, but the digest differs from release-0 at `.governance/install.json` (every `files` row gains `carry`; five rendered SKILL.md rows re-measured), `.governance/install.sums` (three rendered rows added) and the git index.
- **(2) `kill` (AC7):** killed at the schema step after its first write, the receipt reads schema 4, `steps` [], `gov_commit` = the pin; the rollback from a copy of that state exits 0 having written 0 files ("receipt re-stamped at 60d90cb7") and 38 paths stay at the tip. Killed at the floor step, the rollback walks three downs but leaves install.json, install.sums, a new `.governance/policy.json` and the index different.
- **(3)** `kill` and `fail` never reach the floor and fanout-cap steps' `up`, because their witnesses hold at release-0, so AC7 and AC8 cannot observe them unless the case forces step k's first witness to fail.

### Items

1. **Disposition each difference**, reading the code that produced it (`tools/govkit/govkit.py` update/rollback paths, `tools/govkit/upgrade_steps.py` walks, TOOL-dSafePassage-2, -4, -15, -17, -18, -19 specs and DEPL-dCarriedReceipt-9). A field may be normalized ONLY where a record declares it output-only or re-derived per run (cite it, as TOOL-dSafePassage-15 rev-2 did for `carry`); otherwise it is a defect. The killed-walk rollback that writes 0 files with 38 paths at the tip is a defect unless a record says otherwise: the stamp was withheld (TOOL-dSafePassage-2) and the rollback reads vintage from it (TOOL-dSafePassage-4).
2. **For each defect, author a new unit** at the next free ids (TOOL-dSafePassage-62 onward), Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 5`, with `consumes-from` edges so it builds before TOOL-dSafePassage-5, carrying `cl-dClosedLoop-0022` as unit 5 does (use a `part n/m` Carries form if the join needs it, as the 61 split did). One mechanism per spec. Add each to the README's `roster:units` table (`**Derived:**` the build-run divergence). Record nothing in RUN.md; the main loop runs `--rescope`.
3. **Revise TOOL-dSafePassage-5** as a rev bump dated 2026-10-27, still `DEFERRED`: the cases and AC3/AC7/AC12 compare as the dispositions decide; `kill` and `fail` force step k's first witness to fail where the step's witness holds at release-0 (or say why that cannot be done and what the case observes instead); the clone's landed ref is gov's own default branch; `consumes-from` each new unit. One §9 line names this brief.
4. **Cross-read** TOOL-dSafePassage-26 and -61 (consumers of 5); a disagreement in a DEFERRED spec is fixed there. CLOSED specs are read-only: report a contradiction, never edit.
5. **Commit nothing.** Return the files you wrote and, per difference, its disposition and the record or new unit behind it.

### Acceptance

- Each of the measured differences (1)-(3) and the landed-ref order has one named disposition.
- No normalization stands without a cited record declaring the field output-only or re-derived.
- Each new unit's spec is conforming (status header, Carries, §6 criteria with a Red-when, §7 gates, §10 reuse), and `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists it READY once the main loop stages it.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no edit of a CLOSED spec; no change to the pin or its adopters.
- No commit, no stage into the real index, no deviation record.
- No normalization that hides a defect.

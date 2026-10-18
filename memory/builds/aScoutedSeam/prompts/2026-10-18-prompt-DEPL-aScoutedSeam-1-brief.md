# Brief — aScoutedSeam: fold the owner's rulings on the open forks

**Serves:** research DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3

## The prompt

> put the forks to me first, then let's continue working on resolving on the unresolved. What options to we have to test?

## The brief

### Goal
Record the owner's 2026-10-18 rulings on the nine open §8 forks of the five aScoutedSeam specs, and change each spec where a ruling departs from what it was written to. Specs only: no product code, no commit.

### Items
1. TOOL-aScoutedSeam-1 F1, RULED: the design lens runs ONLY when the code lens's framing finds a UI need, against the recommendation.
   - Rework S2, S3, the §4 flow and the data model so the harness runs `codeLens` first. It spawns `designLens` only when the code lens's return marks a UI need: add a boolean `uiNeed` to the return contract, which the code lens sets.
   - The two passes are now serial, so the wall is the sum of the two; state it in §5. The section's `scout` line still reports `lenses <live>/<run>`, and a non-UI request reads `lenses 1/1`.
   - Liveness: a design lens not run because `uiNeed` is false is announced on the scout line as `design skipped (no UI)`, never read as dead.
   - Criteria: adjust any criterion that assumed both lenses always run (AC1, AC3, AC10), and add one. When the code lens returns `uiNeed: false`, the stub records no design spawn and the scout line says the design pass was skipped. Red when a skipped design pass reads as a dead lens, or when the design lens is spawned anyway.
2. TOOL-aScoutedSeam-1 F2, RULED: `medium`, as recommended. Close it.
3. TOOL-aScoutedSeam-1 F4, RULED: option (a), as recommended. Close it.
4. KICK-aScoutedSeam-1 F1, RULED: leave the gov default blank, as recommended. Close it.
5. KICK-aScoutedSeam-1 F2, RULED: product code only, as recommended. Close it.
6. TOOL-aScoutedSeam-2 F1, RULED: the author's reason, read at approval, as recommended. Close it.
7. TOOL-aScoutedSeam-3 F1, RULED: per unit, as recommended. Close it.
8. TOOL-aScoutedSeam-3 F2, NOT CLOSED: the owner asked to measure the diff mode at `high` first, and for a hypothesis on why `medium` lost cases. Mark F2 "measurement owed (owner, 2026-10-18)". Change nothing else about the effort in this pass.
9. DEPL-aScoutedSeam-1 F1, RULED: the superproject rung FIRST, against the recommendation.
   - Reorder S1's resolution ladder: `git rev-parse --show-superproject-working-tree`, then `GOV_REUSE_HOSTS`, then `.unattended.conf REUSE_HOST_TREES`, then `hosts: none`.
   - State what that costs: a node that checks the package out away from its host, while the package is still a submodule, cannot override the superproject with the env variable.
   - Adjust the criterion that observes the ladder order.
10. Every spec: each resolved fork keeps its question and records `RESOLVED (owner, 2026-10-18): <ruling>`, as TOOL-1 F3 already does. One §9 revision line per spec names every section, scope item and criterion moved.

### Acceptance
Each of the five specs carries a §9 line for this pass. Every ruled fork reads RESOLVED with the ruling, and TOOL-3 F2 reads as a measurement owed. `python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and `--check-format` pass after the main loop re-renders the indexes. TOOL-aScoutedSeam-1 stays under the 49152-byte ceiling after the re-render, which adds records rows. It is 48925 bytes now, so item 1's additions are paid for by cuts elsewhere in that spec, such as shortening resolved forks to their ruling.

### Gates
memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### Non-goals
- No product code and nothing under `tools/`, `skills/` or `.claude/`.
- No change to unit ids, order or titles.
- No commit, which is the main loop's.
- No change to TOOL-aScoutedSeam-3's effort or prompt in this pass: that waits on the measurement.

### Limitations
TOOL-aScoutedSeam-1 is about 220 bytes under its size ceiling. Any text added there must be paid for by cuts inside the same spec.

### Reuse
The existing RESOLVED shape of TOOL-aScoutedSeam-1 F3, and the stage convention of `tools/workflows/tier2-review.template.js` for a conditional stage.

## Owner confirmation

Asked: the nine §8 forks, each put as its own question on 2026-10-18.
Answer: TOOL-1 F1 "Only on a UI need"; TOOL-1 F2 "medium (Recommended)"; TOOL-1 F4 "Procedure doc (Recommended)"; KICK-1 F1 "Leave blank for now (Recommended)"; KICK-1 F2 "Product code only (Recommended)"; TOOL-2 F1 "Author's reason (Recommended)"; TOOL-3 F1 "Per unit (Recommended)"; TOOL-3 F2 "Measure first on high, but also put a hypothesis forward WHY 'medium' lost 3 of 7 solved cases and how to instruct it better to prevent this. Seems like an instruction or composition issue."; DEPL-1 F1 "Superproject first".

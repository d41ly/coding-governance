# Spec brief: TOOL-aPrunedIndex-20, the tag plants on a bounded pool

**Serves:** research TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-17
**Caused-by:** TOOL-aPrunedIndex-20

## The prompt

> Unit 17 plus pool

The owner gave this answer in the building session on 2026-11-26. The question was: "Which scope do you approve for making the tag plants cheaper? (unit 17 plus the pool as a second unit, or unit 17 only)".

This unit is the pool. It is the hand-off named in the Edges of `memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md`, under "hands-off". Read spec 17 whole, and especially its section 4 "Alternatives rejected", which measured a four-worker pool near 0.49× of the serial wall.

## The brief

- **Mechanism.** `tools/playbook/tag_bundle.py#run_selftest` runs its plants' subprocesses on a bounded pool instead of one after another.
  - Each distinct plant still runs once, in its own process, exactly as today.
  - The rows are graded and printed in `SELFTEST_ROWS` order, so the leg's output bytes do not depend on finish order.
- **One fact in one place.** The bound is declared once.
  - Reuse the seam spec 17 cites, `tools/govkit/selftest.py` (four workers), or the repository's existing worker-bound knob, rather than adding a second constant beside it.
  - Say what a worker's crash or an exception prints: the plant's row FAILs with its output, and nothing is lost silently.
- **Every verdict stays.**
  - The leg's PASS/FAIL, each `arm ok` / `arm FAIL` line and the summary line keep their bytes for the same plant results.
  - A staged FAIL of one plant must still print that plant's output and exit 1.
- **Cost.** At the close, the main loop re-times the leg with units 17 and 20 together, rewrites the `tags bundle selftest` budget and evidence rows by unit 17's S6, and moves neither up.

## Cut-line

- No edit to `tools/playbook/tag_index.py` or its import closure, and none to `gov_tag.py`, which unit 17 owns. The two units' write sets are disjoint, so they may build concurrently.
- No change to which plants the leg runs, or to the leg's 300 s ceiling. (PINNED, 2026-11-26)
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` stay untouched.
- Tier: 1. A runner's scheduling, with output order and verdicts fixed.

## Owner confirmation

Asked: Which scope do you approve for making the tag plants cheaper? (unit 17 plus the pool as a second unit, or unit 17 only)
Answer: Unit 17 plus pool

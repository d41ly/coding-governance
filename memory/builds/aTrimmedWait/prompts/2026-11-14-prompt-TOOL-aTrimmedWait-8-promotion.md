# Promotion — TOOL-aTrimmedWait-8: closing-review repair, memory-tree

**Serves:** research TOOL-aTrimmedWait-8

## The prompt

The closing diff review of TOOL-aTrimmedWait-1..7, round 1 (`memory/builds/aTrimmedWait/reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md`), exited CONVERGED with
verdict CLEAN WITH FIXES: no BLOCKER or HIGH, seven MEDIUM and two LOW items. The build method's M4
disposes every confirmed MEDIUM and LOW at a DIFF exit by promotion, batched into one unit per
disjoint write set. This unit takes items M1 M3 M4 M5 M6 L1 of that record.

## The brief

### Goal
Author the spec for TOOL-aTrimmedWait-8, a repair unit that closes review items M1 M3 M4 M5 M6 L1 as the
record states each one: its Where, What is wrong, the fix the skeptic judged sound (or the skeptic's
corrected or class-level fix where the record says so), and its Left-shift gate. One mechanism per
item is folded into this one batch unit, as M4 admits. Scope is limited to `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/check-memory-hygiene.test.sh` and `tools/gate-legs.json`.

### Items
1. One scope item per review item (M1 M3 M4 M5 M6 L1), each citing the review record's heading.
2. Acceptance criteria a pass can observe with a fixture or probe; each new suite arm on a `New arm:`
   line in section 7, observed RED-first by the main loop at the close.
3. Files touched: `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/check-memory-hygiene.test.sh` and `tools/gate-legs.json`.

### Acceptance
- `python tools/check-spec-tokens.py --spec <the new spec>` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-8` prints its clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change outside the defects the items name, and no narrowing
of the full hygiene run, the bar, or `--dispatch`'s own refusals. No item of the review record not
named above.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
The review record's fixes, and the units whose code each item lands in.

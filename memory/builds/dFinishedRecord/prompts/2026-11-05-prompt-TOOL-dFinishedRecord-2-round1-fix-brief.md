# Brief — dFinishedRecord: the closing review's two lows, batched

**Serves:** research TOOL-dFinishedRecord-2

## The brief

### Goal
Check 24's derived-LANDED exclusion has an arm for every phase `check_derived_landed` admits at its call, and the build README describes the call where it was built. The review record is `memory/builds/dFinishedRecord/reviews/2026-11-05-review-TOOL-dFinishedRecord-1-closing-diff-round1.md`, items L1 and L2.

### Items
1. L1: `tools/unattended/check-unattended.test.sh` gains arm D after arm C in check 24's derived-LANDED block. tRos's record is `phase: HELD` under a `hold-code` from `HOLD_CODES_HANDOFF`, its landing commit pushed to the fixture origin, then ARCH-tRos-7 added with no row. The arm hits `check 24 EXCLUDED memory/builds/tRos/RUN.md`, misses `check 24 FAILED`, and restores origin to `$ANCHOR0`. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the block's executed count.
2. L2: the build README's roster row for `TOOL-dFinishedRecord-1` says check 24 asks `check_derived_landed` after every skip, as check 23 does, not after its recorded-phase skip, which the spec rejected.
3. Each finding's left-shift, as the record names it: a bug-class checklist entry under `memory/gotchas/`, extending an existing class where one already names the shape, or a new class with its map claim.

### Acceptance
1. Arm D is red with the call narrowed to LANDING (a staged break in `check_derived_landed`'s caller, never in the shared predicate) and green on the fix; the main loop observes both at the close.
2. `grep -n "after its recorded-phase skip" memory/builds/dFinishedRecord/README.md` prints nothing, and the row names the placement the code holds.
3. `python tools/memory-tree/gotchas.py --for-paths tools/unattended/check-unattended.sh` lists the class or classes carrying L1 and L2, each with a `TOOL-dFinishedRecord-1` line in its Where-it-bit section.

### Gates
unattended kit self-test (region 8 and the unsharded floors) · unattended kit gate · memory hygiene · codebase-map coverage + freshness where a new class is claimed · spec tokens; then the full bar at the landing.

### Non-goals
`check-unattended.sh` itself, whose behaviour the review found correct; `check_derived_landed`; `TOOL-dFinishedRecord-1`'s spec, which is CLOSED and stays as written; a re-review of the closing review's subject, which is terminal.

### Limitations
No gate, suite or bar runs in the pass; arm D's red-first observation is the main loop's. Kit versions move through the lander's `mint`.

### Reuse
Arms A to C of the same block are the shape to copy; check 7's HELD arm in the same suite shows the hold-code fixture. `TOOL-dEasedEffort-2`'s fix brief is the record's shape.

## Drawn from the session

none

## Owner confirmation

not asked — the closing review's lows are promoted by the build method's M4 rule, not by an owner turn

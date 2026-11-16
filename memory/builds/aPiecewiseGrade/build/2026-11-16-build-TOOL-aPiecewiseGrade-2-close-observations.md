**Serves:** journal TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-3

# AC6 and the checker's own cost, measured at the close

All figures below were taken on node a by the main loop at the close, with nothing else of this build running. Each is one sample unless it says otherwise. The instrument is `pg2-time.sh` in the session scratchpad, written at the close because TOOL-aPiecewiseGrade-2's spec names it and does not spell it.

## AC6 — a timed `run_spec_token_check` after a sequential pass commit

Two frozen clones of `43c26c7f2`. In the base clone, the driver and the checker were set back to `388216ff8`: aLightenedLoop's whole-key cache alone. The built clone kept them at HEAD. Each clone primed its cache once, then committed one live spec of another build flipped to CLOSED, then timed one call.

| Run | Spec flipped | Base | Built | Outputs |
|---|---|---|---|---|
| Priming run | none | 99.3 s (PINNED 43c26c7f2) | 35.7 s (PINNED 43c26c7f2) | both admitted |
| After the pass commit | `TOOL-aGradedDoorway-7` | 101.2 s (PINNED 43c26c7f2) | 45.4 s (PINNED 43c26c7f2) | both admitted, `cmp` equal |

The built run re-graded 0 specs (DERIVED from the next generation's `graded.list`). The flipped spec left the live set, and no live spec's inputs moved.

A first attempt flipped `TOOL-aOrientedCast-28` instead. Both drivers refused with the same check-49 line: closing that spec left the waiver row `routed-commits selftest <- tools/unattended/` producing nothing, so the row was stale. The two outputs differed only in the checker's elapsed seconds, 87 s against 28 s (PINNED 43c26c7f2). This is the cross-build join that TOOL-aLightenedLoop-3's §4 found scoping would move. Under the per-spec cache it stays whole.

## The checker alone, plain against cached, in this worktree

The checker was run directly at `43c26c7f2`, over 30 live specs (DERIVED from the cold run's `graded.list`), outside the driver:

- Plain: 16 s and 15 s (PINNED 43c26c7f2).
- Cache cold: 18 s, 30 specs graded (PINNED 43c26c7f2).
- Cache warm: 17 s and 19 s, 0 specs graded (PINNED 43c26c7f2).

So on this tree the cached mode saves nothing, and costs about 2 s (DERIVED) over the plain run. TOOL-aPiecewiseGrade-1's F1 predicted this: at most about 1 s to save once TOOL-aPiecewiseGrade-3 removed the per-call kit load. The owner chose (c) knowing it. The dispatch's speed-up above comes from TOOL-aPiecewiseGrade-3.

**Serves:** journal TOOL-dSafePassage-68

# TOOL-dSafePassage-68 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/upgrade_walk.py`: the child script `CHILD`'s
stand-in `run` takes `(row, phase, target, gov_root, *args, **kwargs)` and its three `real_run`
calls end `*args, **kwargs`; the stand-in `read` takes `(root, rev, landed_ref, *args, **kwargs)`
and its `real_read` call ends the same way (S1). `check_child_forwarding(us, child=CHILD)` beside
`CHILD` parses the script with `ast` and returns one problem per stand-in whose signature or call
does not take and pass on the real function's parameters, read by `inspect.signature` (S2).
`tools/govkit/selftest.py` gains two `[dSP-68]` checks at the head of the TOOL-dSafePassage-5
block (S3).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 ran as the
spec's probe on node d (Windows). The red case read HEAD `d8c6a9a2a`'s `CHILD`, the four-parameter
stand-in, out of `git show`.

**Evidences:** TOOL-dSafePassage-68
- AC1 — `python -I -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as uw; print(uw.check_child_forwarding(uw.load_engine()[0]))"` printed `[]`. Red over HEAD's `CHILD`: six problems, the 2 signatures `read_steps: stand-in read(root, rev, landed_ref) does not take and pass on (root, rev, landed_ref)` and `run_step_isolated: stand-in run(row, phase, target, gov_root) does not take and pass on (row, phase, target, gov_root, to)`, and the 4 calls, CHILD lines 23, 34 and 50 to `real_run` and line 54 to `real_read`.
- AC2 — fed `uw.CHILD` with `run`'s def put back to `def run(row, phase, target, gov_root):`, it printed `run_step_isolated: stand-in run(row, phase, target, gov_root) does not take and pass on (row, phase, target, gov_root, to)` first. Fed `uw.CHILD` with the kill branch's call put back to `real_run(row, phase, shadow, gov_root)`, it printed exactly `['run_step_isolated: CHILD line 34 calls real_run without passing on *args, **kwargs']`, line 34 being that call's line. A child rebinding nothing printed ``the child rebinds nothing on `us` ``, and one whose `read` never calls `real_read` printed `read_steps: read never calls real_read`.
- AC3 — owed at the close: `python -I tools/govkit/upgrade_walk.py --case up` runs the `upgrade-walk` gate leg's own case, which no pass may run.

The arm's two checks, lifted out of `tools/govkit/selftest.py` and run with a stub `check`, both
printed `ok`; with HEAD's `CHILD` in place of the shipped one (and the predicate's default rebound to
it), both printed `FAIL`. Owed at the close: that arm red on its staged break, a working copy whose
`CHILD` keeps HEAD's four-parameter `run`, and green restored, through `govkit selftest`; and the
spec's §7 gates.

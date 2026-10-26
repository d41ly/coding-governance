# TOOL-dGroundRules-60 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-60

No merge bar, no gate leg and no self-test suite ran in this pass, and no product file changed: the
unit's evidence is this ledger. Every premise of the spec's §4 held at `ff7f6b52e`: the overlap arm
under `TOOL-dGroundRules-40` is the suite's last before `total=`, `check_overlap_pair` holds the
Python verdict line comparing `py` to `wpy`, and `check_writes_intersect` is `check_guard_trips` in
either direction. `ARM_ALONE` ran verbatim under bash from the worktree root. `SCRATCH` was a
`git clone` of this branch under `%TEMP%/gr60`, checked out at `ff7f6b52e`; each staging was applied
by a scratch script matching one line exactly once, and the copy was reset after. Owed at the close:
the `memory hygiene` leg (§7); this unit adds no arm and declares no `New arm:` line.

**Evidences:** TOOL-dGroundRules-60
- AC2 — `ARM_ALONE` with `ROOT` set to `.` printed one line, `arm ok    TOOL-dGroundRules-40 check_writes_intersect and overlaps give each OVERLAP_PAIRS row its expected answer`, and no `arm FAIL`; in `SCRATCH` after `PY_RAW` it printed one line, `arm FAIL  TOOL-dGroundRules-40 check_writes_intersect and overlaps give each OVERLAP_PAIRS row its expected answer — rows 2, [row policy policy-x.py disjoint: check_writes_intersect True]`, carrying `PY_RAW_WANT` and no `overlaps exit`; with `NO_PY_CHECK` also staged it printed `arm ok` again, the red case.

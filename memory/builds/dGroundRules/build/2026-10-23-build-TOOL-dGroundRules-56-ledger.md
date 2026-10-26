# TOOL-dGroundRules-56 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-56

No merge bar, no gate leg and no self-test suite ran in this pass. The built tree already held the
row check inside `check_overlap_pair`, as `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45` built it,
but the `TOOL-dGroundRules-46` arms sat between the arm's one assertion and the suite's `total=` line,
so `ROW_CHECK_RUN` also evaluated `seed_source`, `scratch` and `arm` calls with `base` unset. S1 is
met by moving those arms above the overlap arm, unchanged, with a comment keeping the overlap arm last;
no verdict, row, assertion or count moved. Before the move `ROW_CHECK_RUN` on `.` printed three
`scratch: command not found`, three `arm: command not found` and three failed writes under `/source-*`
beside the assertion line; after it, the assertion line and the python and `overlaps` noise the spec's
§4 expects. The staged criteria ran on a `git clone` of the branch under `%TEMP%/gr56` carrying the
built suite, removed after. `--dispatch` re-run on the change ran `tools/check-spec-tokens.py` over the
live tree and returned 0. Owed at the close: `spec-tokens self-test` and `memory hygiene` (§7), and
`TOOL-dGroundRules-44`'s `New arm:` line's red-first observation; this unit adds no arm.

**Evidences:** TOOL-dGroundRules-56
- AC1 — `NOT_A_TRAP` staged in `SCRATCH`, then `ROW_CHECK_RUN` with `ROOT` at `SCRATCH` — printed one line `arm FAIL  TOOL-dGroundRules-40 check_writes_intersect and overlaps give each OVERLAP_PAIRS row its expected answer — rows 1, [row policy/a.py policy/ab.py disjoint: not a string-prefix trap]` and no other line carrying the refusal words; with `NO_ROW_CHECK` also staged, no line carried `not a string-prefix trap`.
- AC2 — `ROW_CHECK_RUN` with `ROOT` set to `.` — printed one `arm FAIL  TOOL-dGroundRules-40` line naming `[row policy policy-x.py disjoint: check_writes_intersect Traceback ...` and no line carrying `not a string-prefix trap`; with `FLIPPED` staged in `SCRATCH`, that line named `[row policy policy-x.py disjoint: not a string-prefix trap]`.

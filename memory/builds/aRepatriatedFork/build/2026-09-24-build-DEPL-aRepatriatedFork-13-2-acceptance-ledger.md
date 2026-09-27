# DEPL-aRepatriatedFork-13 — acceptance ledger, closing review round 1 fold B

**Serves:** journal DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-21

The FOLD pass for closing review round 1 items M2, M3, M4 and residual (e), under the mandate. It
ran no merge bar and no self-test suite. Each new arm was run as a SLICE: a script under the
session scratchpad imported `tools/govkit/selftest.py` or `tools/govkit/matrix.py`, pointed its
`GOVKIT` at an engine copy, and called one arm group over a scratch root under `%TEMP%`. The groups
were `check_apply_owned`, `check_adopter_owned`, `check_update_safety` and matrix's
`check_role_move`. Every slice ran first against 5983fe70's `govkit.py`, extracted with `git show`,
and each new arm was observed RED there. It then ran against this fold, where every arm in those
four groups held: 27, 36 and 30 arms.

The reds were for the right reason, read off the fixtures and not only off the arm lines. At
5983fe70 the owned `run.py` under a `./` spelling held gov's bytes after `apply`, and the M4
fixture's declared-owned `run.py` carried gov's `# v2` line after `update --write`.

**Evidences:** DEPL-aRepatriatedFork-13
- AC11 — `./tools/demo/run.py` — at 5983fe70, `apply --resume --write` exited 0 and wrote gov's bytes over the owned file under all three spellings; this fold exits 1 with `is not canonical` naming `[[own]] row 1`, and the bytes stand
- AC12 — `update --write` — at 5983fe70 it merged gov's moved `run.py` into the file the target had declared owned, and `check` said nothing; this fold exits 1 naming the row and `adopt --re-adopt`, writes nothing into it, and `check` exits 1 naming the same row

**Evidences:** DEPL-aRepatriatedFork-17
- AC16 — `update --write --accept-role-moves` — at 5983fe70 it printed `role-recorded` for the edited row now declared `rendered` and did not refuse; this fold exits non-zero naming `diverged and the three-way conflicts`, prints no `role-recorded`, and the index still holds the operator's bytes

**Evidences:** DEPL-aRepatriatedFork-21
- AC5 — `oid` — at 5983fe70 a first `apply` over an owning target recorded the row without `oid`; this fold records exactly the keys `adopt` records, and the same blob

## Not run here

The merge bar and the `govkit selftest` and `govkit acceptance matrix` suites, whose files this fold
edited, are owed at the close. Before this fold, matrix's `check_role_move` also carried one red arm
at 5983fe70: its remedy assertion still expected `govkit apply`, which `DEPL-aRepatriatedFork-17`
S6 had replaced with `--accept-role-moves`. This fold updates that assertion.

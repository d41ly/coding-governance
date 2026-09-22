**Serves:** journal DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3

# Acceptance ledger — dBackdatedFixture, units 1 to 3

Node `d`, 2026-09-16. Every observation below was made on the build's tip `2076d57a` or on a scratch
worktree at that commit with one set of breaks staged uncommitted. Four suite runs ran concurrently:
GREEN with nothing staged, R1 with three `govkit.py` breaks, R2 with two `selftest.py` breaks, and R3
with one `govkit.py` break. Each break's arms are independent of the other breaks in its run, and the
direct-check drivers established that independence first, one break at a time.

**Evidences:** DEPL-dBackdatedFixture-1

- AC1 — `git rev-parse <commit>:<source>` — GREEN printed `ok   [dBF] AC1 every rewound row's gov_oid
  is gov's own blob at its commit, by rev-parse`. R2, with the drop branch staged as `if False:`,
  printed it `FAIL`, and its detail showed `tools/check-wiring.fragment.json` at `24f39915` carrying
  `e69de29b`, the empty blob.
- AC2 — `git ls-tree -r --name-only 24f39915` — GREEN printed all three `[dBF] AC2` arms `ok`. In R2
  the receipt-equality arm and the index arm printed `FAIL`, naming the fragment row as present, while
  the `LIVENESS` arm stayed `ok` because it reads only the descriptor and `ls-tree`. Its own break, the
  check-wiring descriptor's `include` and `claims` without `check-wiring.fragment.json`, printed
  `FAIL [dBF] AC2 LIVENESS` naming only the two older files, with the other four `[dBF]` arms `ok`
  (closing review round 1, M1; run stopped once those arms had printed).
- AC3 — `REFUSING` — GREEN printed both acceptance arms `ok`, the `stale_target` one before the u2a arms
  and the `delta_target` one before `[-8] AC1`. In R2 both printed `FAIL` with `rc 2` and the S9 refusal
  text naming `tools/check-wiring.fragment.json` in their detail, each ahead of its builder's first
  consumer arm.
- AC4 — `4cf0944d` — the 30 labels printed `FAIL` in the baseline run at that commit were each matched
  as an exact `ok   <label>` line in GREEN, with zero misses. GREEN exited 0, 1240 `ok`, 0 `FAIL`, 511 s
  wall under four concurrent suites.

**Evidences:** DEPL-dBackdatedFixture-2

- AC1 — `govkit.py:6814` — GREEN printed the three `[dGV-9]` arms `ok`. R1, with that line staged as
  `pass`, printed all three `FAIL`. The detail showed both held rows at `STALE-SENTINEL` and the landed
  fragment row carrying `KIT_CHECK_WIRING_VERSION=1.3`. The direct-check driver computed the old
  unscoped predicate on that same run as true, which is spec audit B1 reproduced.
- AC2 — `for _dest, _row0 in sorted(...)` — GREEN and R1 printed the `[dBF] LIVENESS` arm `ok`. R3, with
  a `continue` staged as the first statement of that loop in `govkit.py`, printed it `FAIL`, showing the
  receipt after the write and `_held` as the same two paths. The three `[dGV-9]` arms read `ok` in R3.
- AC3 — `_moved` — R1's staged break emptied `_moved`, and the third `[dGV-9]` arm printed `FAIL` with
  `[]` as its detail while the liveness arm read `ok`.

**Evidences:** DEPL-dBackdatedFixture-3

- AC1 — `resolve_entry` — GREEN printed the three `u5a` arms `ok`. The arms hold no literal count, and
  the direct-check driver read N, P and H as 3, 3 and 3 from the `check-wiring` descriptor.
- AC2 — `govkit.py` — R1 staged a skip of the fragment row in `check`'s engine-row loop. `check` printed
  `integrity: 2/2` and `provenance: 2/2`, and both arms printed `FAIL` with `descriptor N=3` and
  `descriptor P=3`. The driver with that break alone showed the sidecar arm `True`.
- AC3 — `install.sums` — R1 staged a drop of one parsed line in `check`'s sidecar block. `check` printed
  `sidecar: 2 line(s) compared against 3`, and the sidecar arm printed `FAIL`. The driver with that break
  alone showed integrity and provenance `True`.
- AC4 — `u5a` — R2 removed `tools/check-wiring.test.sh`'s row, sums line and file before `check`, and
  printed `STAGED-BREAK u5a receipt shrink removed tools/check-wiring.test.sh`. All three arms printed
  `FAIL` against `descriptor N=3`, `P=3` and `H=3`, though `check` itself agreed with the shrunken
  receipt at `2/2`.
- AC5 — `govkit-selftest: all arms held` — GREEN's closing line, exit 0. The three `u5a` labels from the
  baseline read `ok`.

## What this ledger does not claim

- R3 raised `FileNotFoundError` in the `[-ST1]` rollback arms, after its target arm
  had reported. Those arms read an outbox file without guarding for its absence, so a landing break
  crashes the suite rather than redding. That predates this build and is not in its scope.
- GREEN ran at `2076d57a`, before the closing review's fold changed only comments in `selftest.py`
  and regenerated `memory/map/generated/symbols.json`. The fold's own verification is the bar.
- GREEN ran concurrently with three other suites and a review workflow, so its 511 s is not a
  measurement of the suite's standalone cost.
- The source-less branch of `write_vintage_receipt` and unit 3's non-zero floors are NOT OBSERVED, as
  their specs state.

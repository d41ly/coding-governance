---
slug: dBackdatedFixture
node: d
opened: 2026-09-16
streams: deployer
roster: DEPL
authorized-by: prompt
ids: DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3
---

# dBackdatedFixture — the govkit selftest's vintage fixtures stop inventing rows the old vintage never shipped

## The problem this build exists to solve

`python tools/govkit/selftest.py` failed 30 arms on origin/main at `4cf0944d`, measured on node d on
2026-09-16. The suite is held off the plain bar, so no push saw it. Every failing `update` arm printed
the measurer's `UNVERIFIED` line, which pointed at `GOVKIT_NO_REMOTE_PROBE`. The real refusal was on
stderr, and those arms print only stdout. `TOOL-aReplayedCard-2` added a third file to the check-wiring
kit. Two fixtures backdate every receipt row to `24f39915`, where that file did not exist, so they
invent an identity for it. `update`'s S9 integrity check refuses that receipt, as designed.

## Expected improvements

- The suite is green again, and the tool is left unchanged because it was right.
- A kit that gains a file no longer breaks the fixtures that backdate an install.
- A fixture that `update` refuses adds one FAIL line carrying the refusal, ahead of the arms it breaks.

## Detriments if this is not built

- The kit's own DoD bar stays red for every govkit change until someone repeats this diagnosis.
- The next file added to any kit these fixtures install breaks them the same way.

## Build-level rules

- **Three units, sequential, one file.** Unit 1 opened MISSING and was authored; round 1 BLOCKED it,
  and M4's disposition PROMOTED its blocker and its high to units 2 and 3, audited as specs.
- **Tier-2 by the owner's prompt.** The repo's own tier rule would call a selftest-only change Tier-1.
  The owner ruled Tier-2 before the cause was known, and that ruling stands.
- **The engine is not edited.** The S9 refusal and the landing of an unclaimed source are both ratified
  behaviour (`DEPL-dCarriedReceipt-7`; DEPL-dRatifiedSeam-1 S3 at `3fe56d56`). The spec records the probe.
- **Every new arm is observed RED on a staged break before it lands.** The full suite runs once after
  the unit is built, at the main loop.

## Parked decisions

- **`TOOL-aFlaggedScaffold-3` is OPEN and wrong.** It says `update` cannot land a source gov started
  shipping; `3fe56d56` built exactly that. Options: annotate it, or close it naming `3fe56d56`.
  Refused here because a backlog edit is not this unit's mechanism, and recall keeps returning it.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dBackdatedFixture-1` | OPEN | one vintage-rewind helper for both backdating fixtures, and a fixture-acceptance arm per builder |
| 2 | `DEPL-dBackdatedFixture-2` | OPEN | the `[dGV-9]` arms grade only rows the receipt held before the write (audit B1, promoted) |
| 3 | `DEPL-dBackdatedFixture-3` | OPEN | the `u5a` check arms take their expected figures from the descriptor (audit H1, promoted) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 3 unit(s) · node d · opened 2026-09-16 · streams deployer
ids DEPL-dBackdatedFixture-1 DEPL-dBackdatedFixture-2 DEPL-dBackdatedFixture-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dBackdatedFixture-1 — the vintage fixtures model an install the old vintage could have produced](spec/2026-09-16-spec-DEPL-dBackdatedFixture-1.md) | 1 | 2 | INPROGRESS | rev-3 | 2026-09-16 |
| [DEPL-dBackdatedFixture-2 — the `[dGV-9]` version-refresh arms grade only the rows the write refreshed](spec/2026-09-16-spec-DEPL-dBackdatedFixture-2.md) | 2 | 2 | INPROGRESS | rev-2 | 2026-09-16 |
| [DEPL-dBackdatedFixture-3 — the `u5a` check arms take their expected figures from the descriptor](spec/2026-09-16-spec-DEPL-dBackdatedFixture-3.md) | 3 | 2 | INPROGRESS | rev-2 | 2026-09-16 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-dBackdatedFixture-1` | no |
| 2 | `DEPL-dBackdatedFixture-2` | no |
| 3 | `DEPL-dBackdatedFixture-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

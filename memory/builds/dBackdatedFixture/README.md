---
slug: dBackdatedFixture
node: d
opened: 2026-09-16
streams: deployer
roster: DEPL
authorized-by: prompt
ids: DEPL-dBackdatedFixture-1
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
- A fixture that `update` refuses gets one arm naming the refusal, not 27 arms blaming the probe.

## Detriments if this is not built

- The kit's own DoD bar stays red for every govkit change until someone repeats this diagnosis.
- The next file added to any kit these fixtures install breaks them the same way.

## Build-level rules

- **One unit, one mechanism**: the fixtures that model an install at an older gov vintage, and the
  arms graded over them. Classified at opening: MISSING, then authored.
- **Tier-2 by the owner's prompt.** The repo's own tier rule would call a selftest-only change Tier-1.
  The owner ruled Tier-2 before the cause was known, and that ruling stands.
- **The engine is not edited.** The S9 refusal and the landing of an unclaimed source are both ratified
  behaviour (`DEPL-dCarriedReceipt-7`, `TOOL-aScouredKit-25`). The spec records the probe showing it.
- **Every new arm is observed RED on a staged break before it lands.** The full suite runs once after
  the unit is built, at the main loop.

## Parked decisions

- None.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dBackdatedFixture-1` | OPEN | one vintage-rewind helper for both backdating fixtures, the check arms' counts derived, and a fixture-acceptance arm |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node d · opened 2026-09-16 · streams deployer
ids DEPL-dBackdatedFixture-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dBackdatedFixture-1 — the vintage fixtures model an install the old vintage could have produced](spec/2026-09-16-spec-DEPL-dBackdatedFixture-1.md) | — | 2 | OPEN | rev-1 | 2026-09-16 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

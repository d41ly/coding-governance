---
slug: aShelvedLeg
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
ids: TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2 TOOL-aShelvedLeg-3
---

# aShelvedLeg — the unattended kit gate runs only on demand

## The problem this build exists to solve

The `unattended kit gate` leg runs `check-unattended.sh` on every merge and push bar. On node a it
costs 650 to 2900 s a bar, and 45 minutes or more when two bars share the host, making it the
longest leg of most bars. The owner asked on 2026-11-10 to take it off every automatic bar and run
it only on demand. The prompt is in `prompts/`.

## Expected improvements

- A merge or push bar no longer pays the leg's 20 to 45 minutes.
- The leg still runs through `run-unattended-gates.sh --checks` and under `GATE_SELFTESTS=1`.

## Detriments if this is not built

- Every bar on every node keeps paying the leg in full, records-only pushes included.
- The lander keeps losing its push to host contention on the bar's longest leg.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: the leg's `subject` is part of the
  unattended kit's descriptor, so every adopter's bar holds it at its next `govkit update`.
- Unit 2 is the closing review's minors, promoted by M4 as one batch.
- Unit 3 is unit 2's review minors, promoted the same way; units 1 and 2 land first by owner ruling
  2026-11-11, and unit 3 lands later on its own.
- The hold is the bar's existing one, `subject = "kit"`; no new switch.
- The price is TOOL-aBoundedCeiling-10: a held leg cannot notice its own drift. The owner chose it.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aShelvedLeg-1` | the `unattended kit gate` leg declares `subject = "kit"`, so run-gates holds it off every bar that does not set `GATE_SELFTESTS` |
| 2 | `TOOL-aShelvedLeg-2` | the closing review's minors, batched: the kit's merge-bar wording, a typed count, the changed-mode skip, the budget row's spelling, the rc-only reading |
| 3 | `TOOL-aShelvedLeg-3` | unit 2's closing-review minors, batched: the every-bar comments on checks 2 and 9, and the changed-mode sentence's dropped arms |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2 TOOL-aShelvedLeg-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aShelvedLeg-1 — the `unattended kit gate` leg is `subject = "kit"`, off every automatic bar](spec/2026-11-10-spec-TOOL-aShelvedLeg-1.md) | — | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aShelvedLeg-2 — the closing review's minors on the held kit gate, batched](spec/2026-11-10-spec-TOOL-aShelvedLeg-2.md) | — | 2 | CLOSED | rev-1 | 2026-11-11 |
<!-- /gen:build-units -->

Records: 12 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

# Acceptance ledger — DEPL-aHalvedInstall-5

**Serves:** journal DEPL-aHalvedInstall-5

Built at `1137a5af`, promoted from the closing review's round 1 H1. The fixture arms run in
`check_update_safety` and the structural arm in `check_hold_region`, both in `tools/govkit/selftest.py`,
as slices. Break A (no hold at the classification refusal, none from the landing decision) redded
AC1 and AC2 and left AC3 green; break B (hold on every landing refusal) redded both AC3 arms and left
AC1 and AC2 green, so each arm bites on the half of the rule it names.

**Evidences:** DEPL-aHalvedInstall-5
- AC1 — `HELD BACK` — `[aHI-5 AC1]`: a receipt row with role `bogus` holds kit demo, and `plain.txt` is restored
- AC2 — `HELD BACK` — `[aHI-5 AC2]`: a new source at an occupied path holds the kit, `plain.txt` is restored and the operator's file stands
- AC3 — `[[decline]]` — `[aHI-5 AC3 h5d]` and `[aHI-5 AC3 h5s]`: a declined pair and a source the receipt's vintage already shipped hold nothing, and `plain.txt` lands
- AC4 — `tools/govkit/govkit.py` — `scan_hold_region` finds 24 sites, none unmarked, 4 explicit; an exemption and a hold each staged away are named

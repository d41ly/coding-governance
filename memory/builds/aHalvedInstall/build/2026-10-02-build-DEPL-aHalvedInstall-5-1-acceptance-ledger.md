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

## What the whole govkit selftest found after the slices passed

Four runs of `python tools/govkit/selftest.py`, alone on a frozen worktree each time, against base
`d53b503a`, where it was 1670 ok and 0 FAIL. The first, at `1bfa4d01`, redded 18 arms. They were
eight scratch-gov fixtures with an adopter and no `why_no_regenerate`, the shell-exec site table,
and the `[-11]` arm that asserted the half-move unit 4 forbids. The second, at `ffa6080d`, crashed
at `[-23]`: the pin block's own `_held` rebound the held-kit set (`2974795c`, now `_held_kits`, and
the gotcha `a-new-local-collides-in-a-long-function`). The third, at `2974795c`, redded the `[-8]`
arms, because a source absent at `--to` read as new, and the `[-5]` labels (`b7ddaf0d`, rev-3). The
fourth, at `b7ddaf0d`, reported 1732 ok, 0 FAIL, exit 0.

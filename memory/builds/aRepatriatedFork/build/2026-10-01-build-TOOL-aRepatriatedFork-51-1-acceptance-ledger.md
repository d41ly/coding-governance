# TOOL-aRepatriatedFork-51 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-51

Written by the VERIFYING repair pass R1 on node a, 2026-10-01. No merge bar ran. The spec's rev-1
committed before any code. The three registry arms were written first and the suite ran with the
`6e7cb0df` leg staged in: six of the seven new assertions failed, the uncommitted-registry control
passing on both legs. The suite then ran over the built leg, 101 arms, exit 0, and again after the
test helper was renamed `write_waiver` for the lexicon leg.

**Evidences:** TOOL-aRepatriatedFork-51
- AC1 — `brief-recorded-waiver.txt` — over the no-row fixture with a committed one-row registry naming `ARCH-tBrief-1`, the leg exits 0 and prints `1 violation(s) waived`. Red first: the `6e7cb0df` leg exited 1 on the same fixture
- AC2 — `ARCH-tBrief-1` — the same registry over the conforming fixture exits 1 and names the unit as a stale exemption. Red first: the `6e7cb0df` leg exited 0
- AC3 — `0 violation(s) waived` — a registry only in the working tree waives nothing, and the leg exits 1 printing that count

No kit version moves: the unattended kit already reads 1.47 against the base's 1.40, and
`govkit epoch` reports it clean.

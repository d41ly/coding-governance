# aCarriedStop — the new arms observed red and green by the main loop

**Serves:** journal TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3

Observed by the main loop at VERIFYING on node a, 2026-11-13, on frozen worktrees of `41015d329`.

## What ran

- The suite's region-one block from its chain fixture to the end of this build's arms, run behind the suite's own prologue as one script, once per tree. It is a slice and no suite run.
- GREEN tree: the driver of `41015d329`, units 1 to 3 built.
- RED tree: the same suite text over the driver of `d646814e`, where `--owner-stop` is an unknown argument.

## What it read

- GREEN: 671 assertions, 6 FAIL lines. <!-- PINNED 2026-11-13 -->
- RED: 671 assertions, 51 FAIL lines. <!-- PINNED 2026-11-13 -->
- The 6 are in both trees: five rows of the parity table for the register-task, release-task and liveness verbs, which read state the slice cut away, and `FA9 AC15 the driver's census holds`, which unit 1's spec names as red at the base.
- The 45 FAIL lines the RED tree alone holds are this build's arms: every `CS1` label of unit 1, the `CS2` refusal of unit 2, and `CS3 AC1`, `CS3 AC3`, `CS3 AC4 the carry ends at the stop` and `CS3 AC5` of unit 3, with the `hit` lines beside them. <!-- PINNED 2026-11-13 -->
- So the red case and the green case the brief asks for are both observed: with no owner-stop row the gate's existing arm `AC6 a declared audit with no round` refuses in both trees, and the carried chain is admitted in the GREEN tree only.

## What was not observed

- Unit 3's staged breaks, one driver edit per arm as its spec's Gates section names them. Two runs over edited drivers were started and stopped unread, on the owner's standing ruling that the main loop runs no suite at a close. Unit 3's `CS3 AC2` tokens and `CS3 AC4`'s ceiling line read green in both trees, so their red is unobserved.
- `CS2 AC1` red against the driver of `cfda7001`, which unit 2's spec names: it was read red against `d646814e` instead.
- The suite whole, and the `unattended kit gate` leg.

## Inherited, not this build's

- Region two of the suite, run once on each tree before the ruling was re-read: 610 assertions and one FAIL line in both, `--record-round takes free text in the driver's usage table and the hostile-value matrix does not drive it`. The driver of `d646814e` reads it red, so the base holds it. <!-- PINNED 2026-11-13 -->

## TOOL-aCarriedStop-9's AC1, observed by the main loop

- Green at `60a6d0d79`: `python tools/run-gates/derive-ceilings.py --check` printed every backed leg clearing its evidenced maximum, the routed commits leg at 3540 s over 1761.4 s.
- Red with `GATE_LEGS` naming the parent's `tools/gate-legs.json`: `CEILING-EVIDENCE FAILED`, the leg's 760 s ceiling short by 2763s of what its evidence asks (TOOL-aCarriedStop-9).

## TOOL-aCarriedStop-10's AC1 and AC2, observed by the main loop

- Green at `3d8689eaa`: `bash tools/check-install-prefix.sh` exited 0 and printed `clean`, with no line of `tools/chain-packet.py` or `tools/chain-packet.test.sh` listed (TOOL-aCarriedStop-10).
- Red at its parent, on a detached tree: the same checker exited 1 and listed `tools/chain-packet.py@dc026a49:239`, `:245` and `tools/chain-packet.test.sh@d3447869:405` (TOOL-aCarriedStop-10).

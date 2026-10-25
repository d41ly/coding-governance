# TOOL-dGroundRules-83 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-83

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `9437976a8`, `cae57b1d8` or `b8088597d`, each break staged alone and restored: tools/workflows/unattended-build.test.sh with tools/workflows/check-protocol-parity.test.sh at 9437976a8: `FAIL DGR83 a hook that denies printing nothing: the notice says so`, `FAIL DGR83 ...naming the gate that could not ask the hook`, `FAIL DGR83 ...and the gate's own reason`, `FAIL DGR83 ...never as the hook's denial` (4 of 5; the `no hook at all: --render refuses` arm holds before and after, as the spec states); GREEN at cae57b1d8 `PASS (1066 assertions)`, all five DGR83 arms `ok`. `python tools/govkit/selftest.py` at `cae57b1d8` fails exactly the 7 lines it fails at the base `3c2b69be4` (the playbook seed preview, OC8 AC4, OC13 AC4 and `[-5] D1`), so the 47 `[-PV]` arms that failed at `59f02fde9` (before this unit) are GREEN after it; the RED side is that `59f02fde9` run.

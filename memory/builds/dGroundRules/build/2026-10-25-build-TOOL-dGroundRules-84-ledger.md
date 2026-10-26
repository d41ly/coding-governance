# TOOL-dGroundRules-84 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-84

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `9437976a8`, `cae57b1d8` or `b8088597d`, each break staged alone and restored: `bash tools/check-install-prefix.test.sh` at `b8088597d` with `tools/check-install-prefix.sh` as it stood before this unit (`5e8c8c5e7^`): `arm FAIL  DGR84 a limits:-prefixed Skill path counted, or the gate exited 1, wanted 1`; restored, all three DGR84 arms pass (`arm ok    DGR84 a limits:-prefixed Skill path counts nothing`). `bash tools/policy/adopt-policy.test.sh` at `b8088597d` with the adopter's scaffold write moved out of its `if !` test (the `New arm:` line's break): `FAIL --scaffold where the scaffold cannot be written refuses`, 11 passed and 1 failed; restored, `PASS --scaffold where the scaffold cannot be written refuses (exit 1)`, 12 passed. The adopter as it stood before this unit (`5e8c8c5e7^`) passes all 12, because it also refuses on a failing `mv`.

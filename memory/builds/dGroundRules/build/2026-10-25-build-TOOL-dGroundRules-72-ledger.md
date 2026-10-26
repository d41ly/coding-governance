# TOOL-dGroundRules-72 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-72

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: .githooks/pre-commit.test.sh with .githooks/pre-commit at fce5603f8: `FAIL S1 a listed path committed by git commit -a, never added: refused by a guard that saw it (exit 0)`, `FAIL S1 a listed path committed by git commit -- <path>, never added: refused by a guard that saw it (exit 0)`, `FAIL S1 guard.py removed and a listed path committed by git commit -- <path>, never added: refused (exit 0)`; GREEN at 59f02fde9 all three `ok`, `---- 34 passed, 0 failed ----`.

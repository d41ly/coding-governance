# TOOL-dGroundRules-82 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-82

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: `bash tools/lib/resolve-python.test.sh` GREEN at 013f8f725 `PASS — resolve-python: 383 assertions held`; with policy-mirror.js's `...onPath` staged back to `onPath[0]`: `FAIL the JS resolveBash order left the one TOOL-dGroundRules-81 states: GB;F/D1/bash.exe;C:/Program Files/Git/bin/bash.exe;...` (the second PATH bash missing).

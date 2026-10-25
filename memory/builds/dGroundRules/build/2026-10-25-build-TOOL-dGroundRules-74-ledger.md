# TOOL-dGroundRules-74 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-74

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: tools/workflows/unattended-build.test.sh GREEN at 013f8f725 `PASS (1061 assertions)` over the 704 floor, every DGR74 arm `ok` (e.g. `ok   DGR74 a hook that predates the writer marker: --render still renders`). The RED half was observed by the builder's p74.sh, which runs the suite's own helpers and the DGR74 block cut out of the suite by their anchors against six staged breaks of the parity script: `11 5`, `11 2`, `11 2`, `11 1`, `11 2`, `11 5` arms red, the liveness arm and the denying-hook arms each red under at least one break.

# TOOL-dGroundRules-46 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-46

No merge bar, no gate leg and no self-test suite ran in this pass, and the role hook refuses a direct
run of the checker over the tree. Two probes stand in. A scratch script imported the built
`tools/check-spec-tokens.py` by path and called `scan_bare_sources` on this unit's spec with each
staging applied in memory, and walked every tracked spec under `memory/builds/` with the checker's
own `LIVE`, `SOURCE_CMD` and `extract_acceptance`. The new arm was run alone: a scratch driver took
the suite's preamble and the arm's lines out of a copy of the suite, pointed them at the built
checker, and ran the three `arm` calls over scratch repositories under `%TEMP%/gr46`, printing
`pass=3 fail=0`. `--dispatch` ran the checker over the live tree with this spec at INPROGRESS and
admitted the pass, so it exited 0. Owed at the close: the `spec-tokens self-test` over the built
tree, the `New arm:` line's red-first observation, and each staged criterion's `--list` run from a
`%TEMP%/gr46` clone's root.

**Evidences:** TOOL-dGroundRules-46
- AC1 — `PLANT_BARE` in memory, then `scan_bare_sources` — returned `['helper.sh']`; the arm's fenced bare case printed a `[source]` hit for `helper.sh` and exit 1. The `python tools/check-spec-tokens.py --list` run in a clone is owed at the close.
- AC2 — `PLANT_WHOLE` in memory, then `scan_bare_sources` — returned `[]` with one source command matched; the arm's whole case exited 0 with no `[source]` line and printed `source join · 1 sourced file(s) examined in 1 live spec(s)`.
- AC3 — the population walk stands in for `python tools/check-spec-tokens.py --list` on the built tree — 1554 tracked specs, 37 live, no `[source]` hit; the only bare operand in any status is `lib-unattended.sh` in TOOL-dGroundRules-34, which is CLOSED. `--dispatch` ran the checker and it exited 0.
- AC4 — the arm's whole case printed the `source join ·` count line; the walk derived 0 sourced files examined in 0 live specs on the built tree. The line on the built tree is owed at the close.
- AC5 — `DOC_JOIN` on the built tree — printed `3`.
- AC6 — `PLANT_TICK` in memory, then `scan_bare_sources` — returned `['helper.sh']`; the arm's code-span case printed a `[source]` hit for `helper.sh` and exit 1.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: check-spec-tokens.test.sh with check-spec-tokens.py at 78f700dac^: `arm FAIL  TOOL-dGroundRules-46 a bare-name source in a fenced acceptance literal REDS as [source]`, the slash-path arm and the code-span arm FAIL; GREEN all three `arm ok`.

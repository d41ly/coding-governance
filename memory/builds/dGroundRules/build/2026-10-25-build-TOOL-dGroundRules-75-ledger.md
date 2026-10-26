# TOOL-dGroundRules-75 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-75

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: tools/check-template-size.test.sh with check-template-size.sh at 4f52f18c9^: `arm FAIL  A19e a cap of 0 is unchecked under refuse, its budget line never compared — expected exit 0, got 6`, `arm FAIL  A19f ...and the OK line runs no division by the 0 — expected exit 0, got 6`; GREEN at 013f8f725 `PASS — check-template-size.test.sh: every arm held`. The zero-run census arm: its builder observed `--fixture budgets-cap-AGENTS.md` (and ten more named cases) green with a `· zero ·` line and `0 wrong`, and the check-2 guard removed turned the zero line `WRONG: exit 1`; the remaining census rows run in the bar's whole policy fixtures leg.

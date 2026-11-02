# Fix brief — TOOL-dFoldedAudit-16: AC4's figure

**Serves:** research TOOL-dFoldedAudit-16

## The brief

### Goal
Correct TOOL-dFoldedAudit-16 §6 AC4, as the builder's DIVERGENCE return at `build/2026-11-02-build-TOOL-dFoldedAudit-16-3-builder-return.md` measured it. Commit nothing; the main loop commits.

### Items
1. AC4's grep `$(<"$_sw_tmp/err")\|$(<"$_fc_r/$_fc_f")` over `tools/unattended/unattended.test.sh` already prints 3 before the pass, from three `_fc_bytes=$(<"$_fc_r/$_fc_f")` reads at :2877, :3276 and :3293 that an earlier unit wrote. With S2's seven conversions it prints 10. Set the expected figure to 10, and the figure line to "PINNED, 7, 3, 1 and 1 before the pass, measured at 0e3c26cf".
2. Keep every other criterion and §4 as written; the builder found no other disagreement.

### Acceptance
TOOL-dFoldedAudit-16 carries rev-2 and a §9 line, and its status cell stays INPROGRESS.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No other text, no code, no write outside this one spec.

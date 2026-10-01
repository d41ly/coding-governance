# aProbedUnit — asks

## Asks

- TOOL-aProbedUnit-12 · filed 2026-09-14 · a CLEAN spec-audit round writes NO spec-audit record (tier2-review.js returns report null on both clean paths), so `specs-audited` reds every unit closed after it; the harness refuses the hand-out until one exists; the callee should write it → tools/workflows/
- TOOL-aProbedUnit-13 · filed 2026-09-14 · `--dispatch` refuses a later unit's `memory/LIVE.md` declaration: a prior unit's row on it never closes (no build commit touches the index); a 9-path declaration took over 120 s; the brief told units to declare it. Drop the index from the check → tools/unattended/
- TOOL-aProbedUnit-14 · filed 2026-09-14 · `unattended.test.sh` is red at base: four `brief:` arms expect the newline, separator and bypass refusals before the roster one, but verb_brief checks the roster first at 1b000d1a too; the 2026-09-14 frozen run shows exactly those four → tools/unattended/
- TOOL-aProbedUnit-15 · filed 2026-09-14 · `unattended adopter e2e` ran 137 s against its declared 60 s and the driver selftest 5170 s against 3860 s on the 2026-09-14 frozen clone under contention with the harness suite and three fix writers; re-measure quiet before re-declaring → tools/unattended/
- TOOL-aProbedUnit-16 · filed 2026-09-14 · `tier2-review.js` and the two drift-audit workflows hand their agents no `scratch` root, so their reviewers write temp files wherever the shell points; they owe the REQUIRED arg and GROUND sentence unit 4 gave the build harness → tools/workflows/
- TOOL-aProbedUnit-17 · filed 2026-09-14 · the closing review's round-3 mediums and lows stand unfolded: clusters D to H of the round3 diff-review record under builds/aProbedUnit/reviews/ (dispose-first refusal, FOLD_CUTOFF as a kit date, fold re-invoke over-hold, attended note, HELD state) → tools/

# Brief — dRedressedBar: the round-2 review's 14 findings, promoted into units 25 and 26

**Serves:** research TOOL-dRedressedBar-25 TOOL-dRedressedBar-26

## The prompt

> All 14, then stop

The owner's answer, 2026-10-15, to which of the round-2 closing review's findings to fix before the arm observations and the bar. "Then stop": the round-3 review over these units fixes blockers only.

## The brief

### Goal
The round-2 closing diff review over the fold `e114f1356..5b30e4b47`, `reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md`, returned CLEAN WITH FIXES: no blocker, 2 highs, 6 mediums, 6 lows, each confirmed by a skeptic with a stated fix and a left-shift gate. All 14 are about the checks units 21 to 24 added, not shipped behaviour. Fix every one at its root. Read each finding's Where, What is wrong, Consequence, Fix and Left-shift gate in the record; where the skeptic judged the finder's fix unsound (H1 among them), the record's corrected fix is the one to spec.

### Items
1. **TOOL-dRedressedBar-25 — the profiler's arms and guards: H1 (id 15), M1 (ids 4, 11, 23), L1 (id 20) and L6 (id 18).** The AC15 A/B-arm verdict gate in `tools/run-gates/measure_legs.py` must fail when an arm's verdict condition is deleted, not be satisfied by a verdict read inside a failure message; the `measure-legs selftest` guard in `tools/gate-legs.json` gains `tools/run-gates/README.md` and covers the population of run-gates `*.py` files its arm walks rather than listing them one by one; AC9's liveness check stops depending on two fixed sleeps landing in order. Order after unit 24.
2. **TOOL-dRedressedBar-26 — the temp-name lint and the runner's temps: H2 (id 22), M2 (id 6), M3 (id 7), M4 (id 10), L2 (id 21), L3 (id 8), L4 (id 19) and L5 (id 13).** `tools/gate-lint/sh_hygiene.py --temp-names` sees an `mv` after `if`, `elif`, `while`, `until`, `command`, `exec` or a leading assignment, with TEMP_MV's and TEMP_LEAD's keyword lists one list; a positional-parameter rename source is printed, not gated, as documented; a bare `$SRANDOM` temp is not admitted as unpredictable on bash before 5.1; the documented boundary is corrected (the two-hop binding and the `command mv` case); the reuse-cache writer's `import tempfile` cannot be shadowed by an adopter's top-level `tempfile.py`; the leftover check matches both spellings of the staging name; a drifted registry key is counted once. Order after unit 25.
3. **Specs already CLOSED that describe what these units change** (21, 22 and 24 at least): a correction is a spec-writer pass at that unit's turn, `<wN>`, never a build-pass edit, as units 21 to 23 did it.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 25 and 26 READY, ordered after unit 24 in the order 25, 26. Every confirmed round-2 finding id (4, 6, 7, 8, 10, 11, 13, 15, 18, 19, 20, 21, 22, 23) is named by exactly one unit's scope, with an AC whose red half reproduces the defect the record describes.

### Gates
`memory hygiene` · `lexicon naming predicates`

### Non-goals
- No finding outside the round-2 record. Its refuted ids stay refuted.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23).
- No merge to local main and no push without the owner's ask.

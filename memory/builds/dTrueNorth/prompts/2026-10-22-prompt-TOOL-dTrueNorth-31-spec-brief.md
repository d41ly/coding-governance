**Serves:** research TOOL-dTrueNorth-31

# Spec brief — TOOL-dTrueNorth-31, the round-2 closing review's sixteen confirmed findings

## The prompt

> The round-2 closing diff review over `6f5f4ddec...072d97f5c` (the units TOOL-dTrueNorth-23 to -27, -29 and -30) reads CLEAN WITH FIXES: 0 blockers, 0 highs, 16 confirmed findings in 15 items, M1 to M9 and L1 to L6. Its record is `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md`. Under M4 every confirmed finding at the exit is promoted to a unit of this build; the mediums and lows go into one unit.

## The brief

### Goal
Author TOOL-dTrueNorth-31, one Tier-2 unit whose pass fixes each of the fifteen items at its cause, taking the fix the review's skeptic judged sound (for findings 3, 6 and 8 the skeptic's corrected fix, which the record gives in place of the finder's). Author only: no product code, no commit, no gate.

### Items
1. One scope item per review item, M1 to M9 and L1 to L6, each citing the item, its finding number and the file and line the record names, and stating the fix the record's sound fix gives or a better one with the reason.
2. Where an item's fix would change a shipped verb's output, refusal or argument contract (M1's admission, M2's capture, M3's attribute read, M9's `--fixture` entry), say so in §4 and keep the change the narrowest that closes the defect.
3. Each fix that a self-test arm can guard declares its `New arm:` line in §7 with the suite that holds it; a fix no arm can guard says why.
4. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 14`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-31.md`, and one AC per item that a pass can observe with a probe on the touched files: suites are the close's, and a unit runs none of them.
5. Write `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-31-deviation-33.md` for the unit itself: Departs from `dTrueNorth [roster]`, design-to-spec, review finding, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-31`, Caused-by `PLAY-dClosedLoop-2`.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; every AC is a probe a pass can run; the record reads with no malformed field under `python tools/memory-tree/deviation_join.py`; the spec stays under 49152 bytes.

### Gates
No gate runs in this pass; the spec's §7 names every leg its files trip.

### Non-goals
Any other spec; product code; the nine refuted findings; round 1's items; the flagged bar's inherited reds; inside §6, an untracked file named by full path inside a backticked token.

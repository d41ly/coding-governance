# TOOL-dTrueNorth-20 deviation 36 — a §8 RESOLVED mark re-wrapped after the unit's first pass

**Serves:** deviation TOOL-dTrueNorth-20

- **Departs from:** `TOOL-dTrueNorth-20@rev-4`
- **Hand-off:** spec-revised
- **Before:** a §8 RESOLVED mark of TOOL-dTrueNorth-20's spec broke its line after `widens: none ·` (or a grants value), so its next line opened `relaxes: none`.
- **After:** the same words, re-wrapped so no line of the mark ends in `·`; no word, mark, rev, status line or §9 line changed.
- **Cause:** external
- **Reason:** the pinned deviations instrument's `KEY` pattern ends a value at whitespace-`·`-whitespace or the next key, so a newline after the `·` made it read `none ·` as a widens value joining no record, five findings in the departures report. The instrument's blob is pinned and never edited, so the marks moved; the spec template admits a wrapped mark and bumps a rev only on a material change.
- **Evidence:** commit `ed8e143c7`; `deviations.py --report dTrueNorth` before it (5 findings) and after it (0); `memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-1-mark-rewrap-brief.md`.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage §8-mark-wrap
- **Caused-by:** PLAY-dClosedLoop-2

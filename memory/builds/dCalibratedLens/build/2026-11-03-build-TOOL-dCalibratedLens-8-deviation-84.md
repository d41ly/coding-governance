# TOOL-dCalibratedLens-8 deviation 84 — One §8 RESOLVED mark re-wrapped after the unit's audited revision

**Serves:** deviation TOOL-dCalibratedLens-8

- **Departs from:** `TOOL-dCalibratedLens-8@rev-3`
- **Hand-off:** spec-revised
- **Before:** one §8 RESOLVED mark of TOOL-dCalibratedLens-8's spec broke its line after `widens: none ·` (line 313), so the next line opened `relaxes: none`.
- **After:** the same words, re-wrapped so `widens: none · relaxes: none` sits on one line and no line of the mark ends in `·`; no word, mark, rev, status line or §9 line changed, and the spec stays at rev-3.
- **Cause:** external
- **Reason:** the pinned deviations instrument's `KEY` pattern ends a value at whitespace-`·`-whitespace or the next key, and it reads a mark's `RESOLVED (` line alone, so a newline after the `·` made it read `none ·` as a widens value joining no record, findings of the departures report on the prepared merge. The instrument's blob is pinned, so the marks move; dFairHearing's deviation 28 met the same class.
- **Evidence:** the re-wrap (`git diff -- memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-8.md` in this record's commit); `deviations.py --report dCalibratedLens`'s findings `entry N's widens: [none ·] joins no record`; `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-2-deviation-28.md`, the same class.
- **Risk:** editorial
- **Approver:** author, the main loop of dCalibratedLens's spec run, which made this whitespace-only re-wrap, recorded under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-audit-fold
- **Caused-by:** PLAY-dClosedLoop-2

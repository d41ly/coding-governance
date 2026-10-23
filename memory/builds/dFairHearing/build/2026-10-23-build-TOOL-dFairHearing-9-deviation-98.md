# TOOL-dFairHearing-9 deviation 98 — four §8 RESOLVED marks re-wrapped after the unit's audited revision

**Serves:** deviation TOOL-dFairHearing-9

- **Departs from:** `TOOL-dFairHearing-9@rev-1`
- **Hand-off:** spec-revised
- **Before:** four §8 RESOLVED marks of TOOL-dFairHearing-9's spec each broke its `RESOLVED (` line, lines 227, 232, 236 and 242, after `widens: none ·`, so its next line opened `relaxes: none`.
- **After:** the same words, re-wrapped so `widens: none · relaxes: none` sits on the mark's last line and no line of the mark ends in `·`; no word, mark, rev, status line or §9 line changed, and the spec stays at its rev.
- **Cause:** external
- **Reason:** the pinned deviations instrument's `KEY` pattern ends a value at whitespace-`·`-whitespace or the next key, and it reads a mark's `RESOLVED (` line alone, so a newline after the `·` made it read `none ·` as a widens value joining no record, four of the departures report's twelve findings. The instrument's blob is pinned and never edited, so the marks moved, as dTrueNorth's deviation 38 moved its own; the re-wrap is a material revision by the instrument's test past the audited revision rev-1, so it is recorded here.
- **Evidence:** the re-wrap (`git diff -- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-9.md`); `deviations.py --report dFairHearing`'s twelve findings `entry N's widens: [none ·] joins no record`; the instrument's `KEY` pattern applied to the mark as it read before (`widens` `none ·`) and after (`widens` and `relaxes` `none` over the joined mark, no key on the `RESOLVED (` line); the audit pin `TOOL-dFairHearing-9@rev-1` in `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`, added at `c993af496`; `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md`.
- **Risk:** editorial
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage §8-mark-wrap
- **Caused-by:** PLAY-dClosedLoop-2

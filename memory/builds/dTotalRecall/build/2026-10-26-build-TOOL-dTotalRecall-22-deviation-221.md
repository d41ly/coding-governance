# TOOL-dTotalRecall-22 deviation 221 — every declared edge row carries a cardinality

**Serves:** deviation TOOL-dTotalRecall-22

- **Departs from:** `PLAY-dOrderedCharter-24@rev-2`
- **Hand-off:** spec-revised
- **Before:** PLAY-dOrderedCharter-24 S1's `[[edge]]` row holds `type`, `inverse`, `from`, `to`, `pin`, `status` and `declared-at`.
- **After:** each declared row also holds a required `cardinality` table with a `per-source` and a `per-target` bound, each a positive integer or `many`, with `supersedes` bounded at one per target and `caused-by` at one per source; a declared row without it is red in the registry's parse.
- **Cause:** design defect
- **Reason:** cl-0233 declares each edge type's cardinality per source and per target and checks it over the merged tree; the bound belongs on the row that registers the type, and the kind registry mirrors it under a parity arm.
- **Evidence:** TOOL-dTotalRecall-22 §2 S1 and S2, §4 "The bounds", §8 F1 and F2; `night-pass-two.md:237-240`, `:269-270`
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-22

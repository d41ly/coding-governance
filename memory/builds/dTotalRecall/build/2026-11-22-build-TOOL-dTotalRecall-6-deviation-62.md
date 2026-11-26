# TOOL-dTotalRecall-6 deviation 62 — the README site registered in `edges.toml`, the rows widened as landed

**Serves:** deviation TOOL-dTotalRecall-6

- **Departs from:** `PLAY-dOrderedCharter-28@rev-3`
- **Hand-off:** spec-revised
- **Before:** PLAY-dOrderedCharter-28 S1 writes the edge rows with their `from` and `to`, and a `[[trailer]]` table of commit trailer keys; no row admits a build as the source of `implements`, `amends` or `supersedes`, nor a unit id as the target of `patches`, and no table maps a README front-matter key to a type.
- **After:** `tools/playbook/edges.toml` gains a `[[front-matter]]` table of six rows (TOOL-dTotalRecall-6 S1) mapping `depends-on`, `parents`, `patches`, `amends`, `supersedes` and `implements` to their types and target forms, `depends-on` and `parents` both to `after`; `implements.from`, `amends.from` and `supersedes.from` gain `build`, and `patches.to` gains `family-id`. `amends.to` and `supersedes.to` stay `["any"]`, which already admits a unit-id or slug target (`tools/playbook/edge_grammar.py#check_edges`).
- **Cause:** design defect
- **Reason:** cl-0217 types five relations declared in a build's README; the closed set reds an edge whose source or target sits outside its row, so the rows must admit the README site. Deviation 61's After line named `amends.to` where the landed rows needed `supersedes.from` (TOOL-dTotalRecall-6 rev-4 §8 F2 and F9), so this record replaces it.
- **Evidence:** TOOL-dTotalRecall-6 §2 S1 and S2, §4 "The registration", §8 F1, F2 and F9; the pass commit of TOOL-dTotalRecall-6 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-6-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, the gov-builder role of dTotalRecall's build run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-6
- **Supersedes:** 2026-10-26-build-TOOL-dTotalRecall-6-deviation-61

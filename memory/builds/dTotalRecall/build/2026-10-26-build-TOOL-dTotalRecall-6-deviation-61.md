# TOOL-dTotalRecall-6 deviation 61 — the README site registered in `edges.toml`, four rows' namespaces widened

**Serves:** deviation TOOL-dTotalRecall-6

- **Departs from:** `PLAY-dOrderedCharter-28@rev-3`
- **Hand-off:** spec-revised
- **Before:** PLAY-dOrderedCharter-28 S1 writes the edge rows with their `from` and `to`, and a `[[trailer]]` table of commit trailer keys; no row admits a build as the source of `implements` or `amends`, nor a unit id as the target of `patches` or `amends`, and no table maps a README front-matter key to a type.
- **After:** `edges.toml` gains a `[[front-matter]]` table of six rows mapping `depends-on`, `parents`, `patches`, `amends`, `supersedes` and `implements` to their types, `depends-on` and `parents` to `after`; `implements.from` and `amends.from` gain `build`, and `patches.to` and `amends.to` gain `family-id`.
- **Cause:** design defect
- **Reason:** cl-0217 types five relations declared in a build's README; the closed set reds an edge whose source or target sits outside its row, so the rows must admit the README site, and the key-to-type map follows the shape the `[[trailer]]` table already gives a site's keys.
- **Evidence:** TOOL-dTotalRecall-6 §2 S1 and S2, §4 "The registration", §8 F1 and F2; `layer-memory.md:561-578`; memory-plan `[edges]` (`memory-plan.md:184`)
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-6

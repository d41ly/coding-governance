# TOOL-dCalibratedLens-8 deviation 81 — the not-in-view cause computed from the author's committed work order, which renders the slices, the map and the code slot

**Serves:** deviation TOOL-dCalibratedLens-8

- **Departs from:** `cl-dClosedLoop-0465@4003d147`
- **Hand-off:** design-to-spec
- **Before:** the not-in-view cause added to `review.dispose`'s record, computed from the author's slice manifest, the map and the `code` slot (night pass, point 3), and the Loop Review's reading of its share, proposing the map's retirement if it does not fall by 15 points over 38 confirmed findings
- **After:** the not-in-view cause added to `review.dispose`'s record, computed from the authors' committed work orders, the handoff files under the build's `prompts/` folder whose marker names an authoring role, every tracked path they spell being the view, a work order rendering the slices, the `map` slot and the `code` slot it hands, so the three inputs are read where they were handed rather than from a separate manifest (night pass, point 3), and the Loop Review's reading of its share, proposing the map's retirement if it does not fall by 15 points over 38 confirmed findings
- **Cause:** design defect
- **Reason:** No spec writes a slice manifest. TOOL-dTotalRecall-12 S9 hands its writing to dWellOiledMachine's executor and TOOL-dTotalRecall-9 §3 to dBoundRoles' renderer, and neither build specs a manifest file, so a cause computed from it would read `unread` on every finding until another build acts. The work order is committed, is on every node, and holds what a manifest would list. TOOL-dCalibratedLens-8 §8 F2 settled it by the plan's rung 3. The rest of the clause is unchanged, and the amended clause below is carried whole.
- **Evidence:** `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-12.md` S9 and §3; `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md` §3; the work order's slot blocks, `memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-4.md` S1; the marker's one pattern, `tools/roles/roles_lib.py:79-80`; the fork, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-8.md` §8 F2; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:910`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0465@4003d147
- **Caused-by:** TOOL-dCalibratedLens-8

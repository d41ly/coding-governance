# TOOL-dTotalRecall-2 deviation 25 — TOOL-dTotalRecall-2's spec revised for the owner's 2026-11-03 pick on §8 F6's surface

**Serves:** deviation TOOL-dTotalRecall-2

- **Departs from:** `TOOL-dTotalRecall-2@rev-7`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dTotalRecall-2`'s spec as the revision at `TOOL-dTotalRecall-2@rev-7` reads it, whose §8 F6 asks dPlacedRequest for one new read-only holder verb over `read_claims` printing a lease's `fleet-tag`, `session`, `lease`-mode class and `epoch`, serving this unit's S2 and S9.
- **After:** the spec at rev-8: the holder is read through TOOL-dPlacedRequest-34 S22's read-only `--lease status build <slug>`, which already prints `fleet-tag`, `session` and `epoch`; the ask narrows to a seventh TAB field holding the `lease`-mode class, the six-field prefix kept; the ask serves S6 and §4 "Minting"; §3's external edge and §4 "Minting" read the same surface.
- **Cause:** owner ruling
- **Reason:** the parents cross-check of 2026-11-03 found one fact on two surfaces: DEPL-dShippedRelease-138 S48 and -144 S34 read the build lease's epoch through `--lease status`, while F6 asked for a second verb printing the same fields. The owner took its recommendation on 2026-11-03, quoted in `memory/builds/dTotalRecall/prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md`; no code has started.
- **Evidence:** the brief `memory/builds/dTotalRecall/prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md`, the writer's return `memory/builds/dTotalRecall/build/2026-11-03-build-TOOL-dTotalRecall-2-owner-fork-returns.md`, and the rev-8 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dTotalRecall/prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the pick itself is the owner's, quoted in the brief
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** 2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck

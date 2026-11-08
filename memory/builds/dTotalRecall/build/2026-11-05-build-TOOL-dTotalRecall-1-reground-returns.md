**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-11 TOOL-dTotalRecall-25

# dTotalRecall — the re-ground writers' returns, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-05-prompt-TOOL-dTotalRecall-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dTotalRecall-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck`](2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 11 (specs 11 and 25)

I revised both specs in group A (11 and 25). Each row in the brief still holds against today's text, so I made every change and refused none. The memory hygiene gate fails one check, which is the build-index render the main loop owns.

**TOOL-dTotalRecall-11** is now rev-5 · 2026-11-05, 29821 bytes.
- **What changed (row 7):** §3 no longer names TOOL-dDeclaredLoop-20 as a caller of `new shape-run`. It now says no parent spec owns the review-act writer yet, because dl20 S3 only adds four fields to the `review-shape` line and calls no `gov_record.py`. A later unit or an ask owns it, and I named the ask that already exists: TOOL-dDeclaredLoop-111 in `memory/builds/dDeclaredLoop/BACKLOG.md`. It also says TOOL-dWellOiledMachine-19 S6 calls the `--act` form, which is a request that spec makes in its §8 F2 and which this unit does not build.
- **Checked against today's text:** dl20 is now rev-4. Its S3, its `item.review.cost` row and its Files touched list are unchanged and include no `gov_record.py`. The working-tree diff on dl20 does not touch S3. Searching every spec for `new shape-run` finds no caller in dDeclaredLoop. The owner's fork picks of 2026-11-05 did not touch tr11.

**TOOL-dTotalRecall-25** is now rev-4 · 2026-11-05, 20653 bytes.
- **What changed (rows 10 and 11):** the §3 non-goal and §8 F2 now say the `fence` row keeps `hand` through TOOL-dTotalRecall-2 S9. They say that pass's `Decided:` trailer names dIndexedDesign's planner as the owner of the row's door. They say the writer cell moves when the planner lands its own verb, not through tr2's door. F2's pick and its RESOLVED line are unchanged.
- **Checked against today's text:** tr2 rev-8, in S3 and S9, moves only `fields`-form `hand` rows, and a `hand` row of any other form keeps `hand`, with its door's owner named in the trailer. tr1 rev-5 says the same in its §4 writer column.
- **One cite added:** I cited TOOL-dIndexedDesign-15 S5 as the place the planner's verb is defined. That section moves the cell to `python plan_streams.py write <slug> --from <file>`. The fork picks did not touch tr25.

**Acceptance**
- Both files are under 49152 bytes.
- Each **Status:** line carries the next rev and today's date, with every other field kept.
- Each §9 has one new line in the required form, ending with the reground brief's path.
- I staged only these two specs into a copy of the index through `GIT_INDEX_FILE` and deleted the copy afterwards. The hygiene gate failed only check 9, the build index differing from a fresh render: `memory/builds/dTotalRecall/README.md` and `memory/builds/dDeclaredLoop/README.md` are stale. A `gen_build_index.py --write` render cures that, so I left it to the main loop.

**Parent text that looks wrong (not edited)**
- tr11 §3 still says "`probe.run` (dWellOiledMachine)". No spec in dWellOiledMachine mentions `probe.run`. The flow-steps record (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:636`) assigns `probe.run` to dPlacedRequest. dCalibratedLens's 2026-11-03 ancestors cross-check, row 79, already flags tr11's `probe.run` wording as a mismatch. That clause was outside row 7, so I kept it, though my rewrite now words it "is the third writer". A later dTotalRecall unit should decide it.

Files:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-11.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-25.md

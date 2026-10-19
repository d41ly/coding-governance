**Serves:** spec-audit PLAY-dClosedLoop-1

# Whole-design walk, run B: sliced by step

Run B walked every item of flow-steps' and layer-expansions' programs through scenarios S1 to S7 on the sealed copy, sliced by step. Walker 1 took entry and plan, walker 2 design and build, walker 3 test and deploy, walker 4 breakpoint, probe and lifecycle, and walker 5 adopt and the expansions. Each walker also judged the builds and principles of its slice. Four skeptics tried to refute each walker finding and walked a set of cells again. This synthesis joins their verdicts.

Subjects (round 1): memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md@418fc28cd47de2822db04eac3b86b7ca32bc7c31, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md@1888108d8da6848d19fb7cebb5f0446115ede751, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@b2dc2bca27f017876a1d64dd4976d3d4b27cb7ff, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99baf25aff315499fff75802dc3955, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md@027870b06e2c5808f196f4b15c515759be1821d3, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d0d0600136c20fd3fa22707b1abf1, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md@9f71f3d8e3b4b7ce34de6eaca7e4d8b2617e25ba, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md@01191e8514e8de36c304b9666462a016b9ae6598, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@460f54f6029a31c8104945ebac3a09de69b2d0af, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md@19388061eefc1757f9d215fe21222c17df8e3c5a, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md@e29e16d7bdb16df243611f6556fd3867d628b269, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md@b863d10c4aef7b07b306908108896d4d7433a6ca, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md@e61a5385821e344f6c1f1def5f0c989d1d5b517c, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview.md@c705dfd0c158de05379a6fad9299262fdeaf7e3d, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md@84d22ebb39652a06061e8003caba48e618608b6a, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@c0731e8012bb22ee09323c0666a60424acacba55, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md@4976ef59117706e725b6a55e315daf125c9467d0, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md@57668e157e4100899208a3f2748c821db8346122, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md@e1906ced6ff9f3cc715719f752bb081bdd6d6924, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md@87a43459f2da84bd898f98a7c293b733c7f4f8ae, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@727ac3275eedf14ac37799f3fcefb12e70bf65a3, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md@d5c9c48072ea05c225c936617706d3de7973d499, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md@1254230e9a3acbc991a5585c8b1df561ecdcebb3, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md@e6948cd9cfa0e92958ac235c7db140e6bc1dba76, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md@3df38b0db51dfb353bdfc85f7905c5d8cc25dfef, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-state.md@ac95fcc269b34b03c5aef82161a86ea19274d378, memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md@c679e0036b167f235a50b939224b8353b567e9ea, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md@ff10212477bcf48c713763c474e7e83637654236, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md@4dcb6aac62ce575704a32b75606c3a6dd5a5c2f8, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md@bc4c57e94062eb8dc81432d52b5347592661defd, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md@779d0f66eae7bc532e824af5d3530a7c3620f178, memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md@5b0cb48caa25afe7b971262fd24b58a283b2030a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md@1cd205c67945e28c07bb39868cb18088419128c9, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md@ea3fa8ddee7804e6e80add05244c2560291b270e, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md@3655e28ccc77a0f592f0741b98281c8fbfe01f49, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md@1a192df98ba1010a56e646ca81451087395f7b49, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md@4f5e5809f6963500318ddc148fdfbaad02a87635, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md@ee6a9c11f18b693385636d30271b376f1037d865, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-population.md@015612d5b05d7bfcf12311a8306b87cd256a91c8, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-skeptic.md@94dfe381fe5f69d118d78fc913069a979c54873a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md@281a9b9526fcbb6a693c77c08925f9486e5e29ff, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md@7d11112ecee1c951389e70b057d2d33b4b1cdf88, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md@97edc2cf70309578889275494a710fddaf6f09fb, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md@35ef3eee6cc3285680e0ecae47668fb2dc3b8045, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md@07ce17290998aeb22b366cd27f11df0fa7b1558f, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md@a0c305c114b455f44977f4ecb7beee0d07483c53, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md@1720bf7555d336f9f8f1412bf7af7ed8ad0f2891, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b44c773093d661eb911f30c36f753254f, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md@6475aa368904b5a8cb8fb84a21382f9dd6958766, memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md@c3c92f39e71a0ed06d6455e1f248ac50a05bcf60

## Verdict: BLOCKED

Twelve critical findings block the chain specs: B1-F1, B1-F2, B1-F3 (same as B4-F1), B2-F2, B2-F3, B3-F1, B3-F2, B4-F2 (same as BS3-F3), B5-F1 (same as B1-F4), B5-F2, B5-F3 and B5-F6. Each is high with a rubric consequence. B2-F2, B4-F2, B5-F3 and B5-F6 leave a scenario with no terminal (c2). B1-F1, B1-F2, B2-F3, B3-F1, B3-F2, B5-F1 and B5-F2 let a guard loosen or certify what it does not check (c3). B1-F3 leaves P23 with no enforcing clause (c5). The walkers raised 75 findings and the skeptics raised 9 more while walking cells again. The skeptics refuted 15. The 69 confirmed findings make 64 items: 12 critical, 1 high, 41 medium and 10 low. No finding is graded blocker. The 9 skeptic-raised findings (ids `BS<batch>-F<n>`) were tested by no second skeptic.

## Critical

### B1-F1 — `entry.intake` is acted and witnessed by the orientation scout, not by the prompt-submit hook
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** The item's actor is "orientation scout" and its witness is "the intake entry the scout writes". That breaks flow-steps [rules] ("No witness is typed by the acting agent"). It contradicts [revised] `hook-actor-kind`, `cl-dClosedLoop-0282`, flow-roles H2 and flow-roles-adoption:202, which all make the prompt-submit hook the actor.
- **Consequence:** `deploy.mandate` takes the intake record as landing authority. In unattended S2 a build lands on an "owner's prompt" an agent could have typed or edited.
- **Fix:** Make the actor the Runtime's prompt-submit hook in an owner-bound session, and the witness the intake entry the hook writes verbatim, redacted and capped. Keep the scout only as the reader in `entry.orient`.
- **Skeptic:** Confirmed high (c3). The scout-typed witness also contradicts the item's own route ("the hook crashed or never fired") and v2 [contracts] ("Plan's witness is the hook-written intake").

### B1-F2 — Under `plan.ratification: request`, `plan.exit` takes the owner's go "as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** The Does cell makes "the owner's go, as the planner records it" the ratification. v2 [contracts] makes the hook-written intake Plan's witness. `cl-dClosedLoop-0137` calls a relayed request "data with provenance and never consent".
- **Consequence:** Under the default, the planner, an agent, types the ratification of its own plan. The Plan gate certifies what it does not check.
- **Fix:** Under `request`, let the hook-written intake record the build's claim names stand as the ratification. Before that hook lands, apply `cl-dClosedLoop-0378`'s owner gate. Remove "as the planner records it".
- **Skeptic:** Confirmed high (c3). The cell contradicts v2 [contracts], `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378` and `cl-dClosedLoop-0137`.

### B1-F3 — P23's only enforcing clause, `cl-dClosedLoop-0093`, appears in no `[chain]` row
- **Address:** architecture-v2 [enforcement] (row `P23`, `cl-dClosedLoop-0093`)
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2 (B4-F1: S7)
- **Defect:** P23's enforcement row names `cl-dClosedLoop-0093`, and no clause in [chain] carries that id. It is the one gap in 0001 to 0496: dDeclaredLoop's row runs from 0092 to 0094, and [clause-ids] says "Retired: none".
- **Consequence:** No chain build builds the claim-trust rule, that a claim is acted on only when its stored key recomputes equal. `entry.claim`'s own-key retry and every cross-node claim run unchecked. P29's "acted on" rule, which rests on P23's re-derivation, is unenforced too. dTrueNorth's carries join reads a ghost id.
- **Fix:** Restore `cl-dClosedLoop-0093` in dDeclaredLoop's row: the claim's key recomputed, its weakest source not agent-typed, otherwise re-derived or held as evidence. Make Stage 0's K5 arm red an enforcement row that names a ghost id.
- **Skeptic:** Confirmed high. v2:1707 is the only place 0093 appears, and 0092 only prints each claim's key and verdict, so nothing enforces P23.
- **Same as:** B4-F1

### B4-F1 — P23's enforcement row names a clause id that no chain clause carries
- **Address:** architecture-v2 [enforcement] `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S7
- **Skeptic:** Confirmed high, a twin of B1-F3. The item is under B1-F3.
- **Same as:** B1-F3

### B2-F2 — Build's tail after `build.reuse-check` is reached from no entry
- **Address:** flow-steps [build] `build.recommend` (and `build.reuse-check`'s Then cell)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Defect:** `build.reuse-check`'s clean outcome routes to "the unit built", which is a state, not an item. `build.recommend`'s Needs, "every unit built and reuse-checked", name no tag. No Then cell routes to `build.recommend`.
- **Consequence:** The engine computes position from item tags, so `build.recommend`, `build.ratify`, `build.distill`, `build.core` and `build.exit` never reach the frontier. S1 cannot reach `build.exit`, Test or `deploy.close`.
- **Fix:** Route the clean outcome to `build.recommend`. Write its Needs as "`build.reuse-check` for every unit in the roster", a quantified tag the join resolves. Re-run Stage 0's K2 until the five leads clear.
- **Skeptic:** Confirmed high. Unlike `design.recommend`'s Needs, which name `design.unit-spec`, these name no tag.

### B2-F3 — Two of Design's guard keys are read by no item
- **Address:** flow-steps [design] `design.overlaps` and `design.ready`
- **Class:** K4, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** `design.overlap` (warn, refuse, index-only) and `design.handoff` (derived-ready, ready-plus-audit, status-and-tier) are read by no item and no clause. `design.overlaps` has no per-value route. `design.ready` reads only "derived READY". dIndexedDesign's `cl-dClosedLoop-0383` and `cl-dClosedLoop-0384` name neither key.
- **Consequence:** The strict preset's `design.overlap: refuse` and `design.handoff: ready-plus-audit` silently fall to the weakest value. In S2 the overlapping builds X and Y both proceed to `design.unit-spec`, and READY is derived with no audit.
- **Fix:** Give `design.overlaps` a route per value of `design.overlap` (refuse → back to `design.decompose` with the overlap record). Give `design.ready` arms for `ready-plus-audit` and `status-and-tier`. Have 0383 and 0384 name both keys, each seen red on its planted value.
- **Skeptic:** Confirmed high. The strict preset sets both values, and no item or clause reads either key.

### B3-F1 — The seen-red check writes the record it checks for
- **Address:** layer-memory [design], kind `seen-red`; flow-steps [test] `test.seen-red`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S1
- **Defect:** layer-memory's kind table names `test.seen-red` as the writer of the seen-red record. That item only checks that every gate the build added or changed has one. No item is the recorder that gap-test-06 owes, which dWitnessedBar's row carries.
- **Consequence:** The record's only declared writer is its checker. `test.seen-red` can pass for a gate nobody ever saw red, and P30's single declaration names the checker as the writer.
- **Fix:** Make the writer the run that observed the planted red: the leg factory's seen-red arm, run inside the unit's pass, keyed by the leg and the red SHA. Keep `test.seen-red` a reader. Seed a gate with no observed red that must make `test.seen-red` red.
- **Skeptic:** Confirmed high. The kind table's row and `test.seen-red`'s Does cell say exactly this.

### B3-F2 — A core red at landing lets the build close once a patch is filed
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0423`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Defect:** `deploy.core` routes a red to a patch build, "and the close waits for its filing". foundations [core] (the owner-confirmed K1 reading), v2's revision, `cl-dClosedLoop-0423` and P16 all say such a red stops the build from closing until it is fixed or excepted.
- **Consequence:** In S3 the originating build reaches `deploy.close` and `landed` as soon as the patch is filed, before the red is fixed. The violator-pays guard loosens at the item that implements it.
- **Fix:** Hold `deploy.close` until the patch build's `deploy.core` is green for a SHA that contains the landed one, or an owner exception under `core.exceptions`. Add the matching transitions row.
- **Skeptic:** Confirmed high. Filing a patch build is neither fixing nor excepting the red.

### B4-F2 — Budget-exhaustion and park endings have no transition row and no terminal state
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Defect:** [transitions] has no row for `flow.on-exhausted`'s endings (close incomplete, park-for-owner; `cl-dClosedLoop-0116`) or for parking on silence (`cl-dClosedLoop-0326`). It has no terminal or held state for them, and its only hold, `paused`, keeps its leases. `life.quiesce` routes "pause → parked", a state the table lacks. The engine refuses any transition the table lacks.
- **Consequence:** A spent budget in S6, or the default `run.on-owner-silence: apply-recommendation` on an unanswered ratification, leads to a transition the engine refuses, so the build reaches no terminal, against P20 and P39. A build that spends its budget in Plan has nothing to land and no units to descope, and its close is refused (BS3-F3).
- **Fix:** Add a terminal `closed-incomplete` and a `parked` state (lease released, item open, resumed by the owner's disposition). Add rows from every open state on exhaustion and on a park, each with its witness. Add both states to the terminal and disposition sets, and plant a budget spent in planning.
- **Skeptic:** Confirmed high (c2). One detail of the evidence is off: the `incomplete` grep does print lines, but only unrelated ones.
- **Same as:** BS3-F3

### BS3-F3 — A spent budget has no transition row, so a build that spends it in Plan cannot end
- **Address:** flow-steps [transitions]; [rules] (the "Every route back is bounded" bullet); seen at [plan] `plan.record`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Skeptic:** Raised by skeptic batch 3 while walking `plan.record` S6 again, where walker 1 gave `holds`. No second skeptic tested it. The item is under B4-F2.
- **Same as:** B4-F2

### B5-F1 — Maintain's patch build skips entry, its claim and lease, and FI-4's light five
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high (the entry-skip part: medium)
- **Scenario:** S3
- **Defect:** `maintain.patch` "opens a patch build at Design". [transitions] and `design.input` admit a patch only with its slug claimed and its lease taken by `entry.claim`. flow-steps [entry] and retrofit [cadence] route a cadence filer through `entry.place` instead, so the design states two entry routes for one patch. On either route, no item reads `patch.ratify`, and the patch path (`entry.claim` → `design.input` → `design.unit-spec`) runs no duplicate check. Two of FI-4's "light five" go unenforced.
- **Consequence:** A strict `patch.ratify: owner` silently loosens, because no item holds the patch for the owner. With no dedupe, `deploy.core`'s post-close patch and Maintain's `default-branch-red` patch for the same red both run.
- **Fix:** Route `maintain.patch`, and `deploy.core`'s post-close row, to "files a patch intake → `entry.place`", with `entry.claim` taking the slug and the lease. Give the patch path one item that runs `plan.dedupe` and one owner gate that reads `patch.ratify`, and add both to [transitions].
- **Skeptic:** Confirmed high (c3) on `patch.ratify` and the dedupe. `patch.ratify` has 0 hits in flow-steps, layer-flow and flow-roles, and appears in v2 only as catalogue rows. The entry-skip part stands at medium, as under B1-F4.
- **Same as:** B1-F4

### B1-F4 — Maintain's patch skips entry.place and entry.claim and goes straight to Design
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K2
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **Skeptic:** Confirmed medium. flow-steps [entry] and retrofit [cadence] route a cadence filer's intake through `entry.place`, so a path to the claim and the lease exists. What remains is a contradiction a spec writer trips over, not a failing scenario. The item is under B5-F1.
- **Same as:** B5-F1

### B5-F2 — A Maintain patch's key has no period, so a failed fix is swallowed
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Defect:** The patch intake is keyed by (reading, offender key), with no period. Every command item in [design] is idempotent on its witness key. `maintain.read` routes every later over-pin reading of the same offender back to `maintain.patch`.
- **Consequence:** A patch lands, and the next period's reading of the same offender is still over its pin. The re-filing is a no-op on the existing key, so the breach is never filed again and never reaches the owner. `maintain.file`'s per-period `seen` rows do not have this hole.
- **Fix:** Key the intake by (reading, offender key, period). Route a recurrence on a closed patch to `maintain.file` as a `seen` row on an owner ask.
- **Skeptic:** Confirmed high (c3) on the swallowed recurrence. The walker's budget leg is wrong: a Maintain patch is a build with its own `flow.rework-budget` (v2: "one budget per build"). That part of the fix is dropped.

### B5-F3 — The expansion tables declare no Needs, and `maintain.record`, `maintain.levels` and `loop.record` are never reached
- **Address:** layer-expansions [design-observability] `maintain.record` (the Maintain and Loop Review tables)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Defect:** The Maintain and Loop Review tables have no Needs column. No route reaches `maintain.levels`, `maintain.record` or `loop.record`: read goes to direct, patch or file; direct to file; patch to Design; file to triage; `loop.file` to the owner's breakpoint.
- **Consequence:** `maintain.record` is the only item that releases the period lease and writes the record that EX-3's default `every-period` owes. Neither happens, so a run never closes and the slower levels never run.
- **Fix:** Add a Needs column to every expansion table, for example `maintain.record` needing every reached item of the run and `maintain.levels` needing `maintain.lease`. End each program's terminal routes at its record item.
- **Skeptic:** Confirmed high (c2). No route anywhere reaches the three items.

### B5-F6 — `kits.install` and `kits.update` share one row with two actor kinds, no Needs and no terminal route
- **Address:** layer-expansions [design-distribution] `kits.update`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S4
- **Defect:** One row serves both items, with the actor "the owner, or a command". flow-steps [rules] forbids that: one actor of one kind per item, and one item per policy value. The row has no Needs. Its only route is the case of an adapter with no target: there is no success route, no failed-step route and no handoff to `test.seed` or the `adopt` program.
- **Consequence:** An adopter's update in S4 reaches no declared terminal.
- **Fix:** Split the row into `kits.install` and `kits.update`, one row per actor value, each with Needs and a closed outcome set. Updated → `test.seed` for each new check → `adopt.declarations` and `adopt.instructions`. A step that exits nonzero → the receipt at step k-1 and a rerun. Held → an order.
- **Skeptic:** Confirmed high (c2). The walker's "self-written witness" leg is overstated, since [rules] allows a witness a command writes. That part of the fix is dropped.

## High

### B2-F5 — A superseding build never reaches `design.inventory`, so the kept work has no route
- **Address:** flow-steps [design] `design.input` (and [lifecycle]'s kept-work rule)
- **Class:** K2
- **Severity:** high
- **Scenario:** S5
- **Defect:** [lifecycle] says a superseded build's kept work passes to its replacement through the replacement's `design.inventory`. `design.input` sends a plan record to `design.seams` and only a plan revision to `design.inventory`, which judges the build's own completed units. No input kind carries a superseded build's units.
- **Consequence:** Replacement Z never inventories X's built units. They get no kept, amended or retired verdict, and they drop out of the trail.
- **Fix:** Add a `supersession` input kind, Z's plan record naming the build it supersedes, which `design.input` routes to `design.inventory` over the superseded build's built units. Add its [transitions] row. Have `life.request`'s supersede name Z's slug before `life.notify`.
- **Skeptic:** Confirmed high (batch 2). The walker's c4 is overstated: X's commits and records are left uncarried, not overwritten, so the item is not critical. Batch 3 confirmed the twin B4-F6 at medium.
- **Same as:** B4-F6

### B4-F6 — A replacement build never reaches `design.inventory`, so supersession's kept work has no route
- **Address:** flow-steps [lifecycle]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Skeptic:** Confirmed medium (batch 3): no input kind carries a superseded build's units into the replacement. The item is under B2-F5.
- **Same as:** B2-F5

## Medium

### B1-F5 — A patch claim records no originating build, so the shared rework budget cannot be keyed
- **Address:** flow-steps [entry] `entry.claim`; flow-steps [rules] (the "Every route back is bounded" bullet)
- **Class:** K1 (B3-F3: K6)
- **Severity:** medium
- **Scenario:** S3
- **Defect:** The claim commit carries only the claimant's key, the session and the intake's or the ask's content key. Neither `entry.place` nor `entry.claim` names the originating build. [rules]' list of budget draws leaves out the patch build of a build's own landing, which v2's `flow.rework-budget` and `cl-dClosedLoop-0440` charge to the originating build's one budget.
- **Consequence:** A patch chain has no key to charge 0440's shared budget, so each patch starts a fresh one. "The originating budget spent" has no route.
- **Fix:** Add the patch-build draw to [rules]. Have the post-close patch intake and `entry.claim` record the originating build's slug and landed SHA, and derive the budget key from them. Route a spent originating budget to the originator's `flow.on-exhausted`, filed as an owner item. Seed a patch chain whose second patch shows a fresh budget.
- **Skeptic:** Confirmed medium for both findings (batch 3). `cl-dClosedLoop-0440` already obliges dShippedRelease with a planted patch-chain red, so this is a hole a spec writer falls into, not a scenario that cannot terminate.
- **Same as:** B3-F3

### B3-F3 — Patch builds have no link to the originating build's budget
- **Address:** flow-steps [rules] (the "Every route back is bounded" bullet); flow-steps [entry] `entry.claim`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K6
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **Skeptic:** Confirmed medium, the same defect as B1-F5. The item is under B1-F5.
- **Same as:** B1-F5

### B1-F9 — Plan reads the design index, which no ancestor of dRankedPlan builds
- **Address:** flow-steps [plan] `plan.dedupe`, `plan.exit`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `plan.dedupe` checks "against live builds, the design index and open asks". The design index is `cl-dClosedLoop-0384`, in dIndexedDesign's row. dRankedPlan's parents are dDeclaredLoop, dTotalRecall and dBoundRoles, and its only stand-in, `cl-dClosedLoop-0378`, covers intake. `plan.exit` also launches "where `run.host` says", a dWellOiledMachine key, and Stage 0 flags its target as in no declared form.
- **Consequence:** dRankedPlan's dedupe cannot run as specified when it lands.
- **Fix:** Dedupe against live builds and open asks only until dIndexedDesign lands, then join the index arm. Write `plan.exit`'s target in a declared form.
- **Skeptic:** Confirmed medium on the index half. The `run.host` half is weaker, since the key can read its catalogue default.

### B1-F10 — Plan's owner values switch nothing
- **Address:** architecture-v2 [policies] `plan.triage`, `plan.authority`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The strict values `plan.triage: owner-batches` and `plan.authority: owner-orders` appear in no item. `plan.triage-rule` is a command and `plan.triage-judge` is the planner, so the owner never acts.
- **Consequence:** Owner switches that switch nothing, against P10. `cl-dClosedLoop-0014`'s no-reader arm reds such keys once their owner build lands.
- **Fix:** Give each owner value an item and a clause, for example a `plan.triage-owner` item under `owner-batches`, or retire the value with a decision.
- **Skeptic:** Confirmed medium, narrowed. `plan.kickoff` is read by `cl-dClosedLoop-0375`, and `planner-drafts-owner-ratifies` does not contradict `plan.ratification: request`. The finding's Stage 0 K4 lead list could not be checked.

### B2-F1 — Conditional needs put Design's and Build's exits on the frontier before the breakpoint is decided
- **Address:** flow-steps [design] `design.ready`; also [build] `build.ratify`, `build.distill`, [test] `test.exit` and [deploy] `deploy.notify`
- **Class:** K1
- **Severity:** medium (the walker graded it high, c3)
- **Scenario:** S1
- **Defect:** `design.ready` needs "`design.recommend`, and the spec audit where it ran". Once `design.recommend` is witnessed, `design.ready` shares the frontier with `design.reason`, the item that decides whether an audit is owed. `build.distill` ("the closing review where it ran") and `test.exit`, which leaves out `test.reason`, have the same untagged conditional need.
- **Consequence:** Under `review.recommendation: binding`, an exit can be derived before its owed spec audit or closing review is decided.
- **Fix:** Make the breakpoint an explicit need. `design.ready` needs `design.reason` (or `design.recommend` under `signals-only`), plus the breakpoint's disposition record when its trigger fired. Do the same for `build.ratify` and `build.distill`, `test.exit` and `deploy.notify`. Add a static check that reds an untagged conditional in a Needs cell.
- **Skeptic:** Confirmed medium. On the defaults an owed or running review still blocks (`review.blocks` every-review, `review.recommendation` advice), so the race costs something only under `binding`.

### B2-F6 — "A fix pass" and "a revert pass" are no items, so their allowance attaches nowhere
- **Address:** flow-steps [build] `build.acceptance` (also `build.scope`, and [test]'s "A fix pass keeps its check")
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Defect:** "A fix pass" (`build.acceptance`, `test.attribute`, `test.seen-red`) and "a revert pass" (`build.scope`) are route targets, but no row declares them. `build.unit-pass` declares only the ordinary allowance.
- **Consequence:** The engine has no tag to put on the frontier for a red unit. M16's narrowed fix-pass allowance renders into no work order, and the budget draw attaches to no instance.
- **Fix:** Declare `build.fix-pass`: the builder, Needs naming the red record, the allowance minus the red check's files and the acceptance files, and Then `build.acceptance`. Declare the revert pass too, and route every "fix pass" to that tag.
- **Skeptic:** Confirmed medium.

### B2-F8 — Only the starting units' leases are taken by any item
- **Address:** flow-steps [build] `build.unit-lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `build.unit-lease` "takes each starting unit's lease", with one need, `build.base`. `build.scope` routes later work to "the unit's next pass" or `build.reuse-check`, never to a lease.
- **Consequence:** A unit that starts later is leased by no item. v2's pick (`cl-dClosedLoop-0331`) offers "ready unleased units" to other nodes, so in S2 two nodes can start it.
- **Fix:** Make `build.unit-lease` per unit, with Needs that are the unit's predecessors in declared order.
- **Skeptic:** Confirmed medium.

### B2-F9 — A parent's `withdrawn` or `superseded` notice has no route before `deploy.parents`
- **Address:** flow-steps [design] `design.decompose` (and the [design] and [build] policy lists)
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Defect:** `deps.on-parent-withdrawn` is read only at `deploy.parents`. No Design or Build item routes a parent's notice, and an acknowledgement triggers no replan.
- **Consequence:** Dependent Y keeps designing and building on X's withdrawn interface until Deploy, then replans, having spent its budget and leases.
- **Fix:** Route a parent's notice read at any item boundary to `deps.on-parent-withdrawn` there, with replan going to `design.reentry`. Add the key to Design's and Build's policy lists.
- **Skeptic:** Confirmed medium. layer-flow F-E says dependents act as the key says, yet no item routes a read notice, and `cl-dClosedLoop-0328` releases dependents only from a wait.

### B2-F10 — `cl-dClosedLoop-0003` can be read to refuse every chain build's first spec
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0003`
- **Class:** K7
- **Severity:** medium (the walker graded it high, c1)
- **Scenario:** S7
- **Defect:** 0003 refuses "a chain build's spec in progress while its build's coverage is red" without naming the status. Read as "being drafted", it refuses every first spec, since coverage stays red until specs carry the clauses.
- **Consequence:** A spec writer can build a refusal that blocks dTrueNorth's first spec and every later chain build's.
- **Fix:** Refuse a spec in progress only on the per-spec arms (ghost, unbound, stale, ambiguous, dropped). Keep the uncarried and unowned-node arms for the Design exit, as carries.py does. Seen-red the refusal on a planted ghost.
- **Skeptic:** Confirmed medium. TEMPLATE-SPEC defines `INPROGRESS` as "approved, build underway", under which the refusal applies only after the Design exit, as in carries.py. The blocking outcome follows only from the looser reading the wording allows.

### B2-F11 — `cl-dClosedLoop-0002` reds two whole carriers only when they disagree
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K8
- **Severity:** medium
- **Scenario:** S7
- **Defect:** 0002 reds "two specs carrying one clause whole and disagreeing" without saying what they disagree on. carries.py reds any second whole carrier.
- **Consequence:** A product join built from the clause passes two units that carry one clause whole at the same pin, so one clause is built twice.
- **Fix:** Write "two specs carrying one clause whole, or pinning it to two hashes, red", as the instrument reads.
- **Skeptic:** Confirmed medium. research-final-coverage maps the case to "carried whole by 2 specs".

### B2-F16 — P19's one clause names no refusing check, and a deviation record admits a revision after a pass
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0400`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S3
- **Defect:** 0400, "built specs frozen", has no check and no seen-red. `cl-dClosedLoop-0004`'s population, each spec revision after the unit's first attributed pass commit, includes a landed unit's spec. `cl-dClosedLoop-0412` passes such a revision once it has a deviation record.
- **Consequence:** A patch build can revise a built unit's spec in place under an approved deviation. P19 requires a new unit.
- **Fix:** Add to 0400 a refusal of any revision of a unit whose spec is in a landed range, its deviation population included, seen red on a planted in-place edit of a landed unit's spec.
- **Skeptic:** Confirmed medium. No freeze check appears in v2 or flow-steps. final-questions' rule that a change after landing is a new unit is enforced by nothing.

### B2-F18 — A re-entered Build lap owes a full closing review outside `review.follow-up`
- **Address:** flow-steps [build] `build.recommend`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Defect:** `build.recommend` routes to "the closing review where owed", and Build's review is owed by default. Every lap back through Design therefore owes a fresh closing review. The owner's answer to FR-9 was a follow-up only after a HIGH finding, which `review.follow-up` carries.
- **Consequence:** Every lap runs a new full closing review whatever `review.follow-up` says. CEILING and NON-CONVERGENT are counted across unrelated reviews.
- **Fix:** On a lap whose units came from a closing review's findings, route `build.recommend` to that review's follow-up as `review.follow-up` says, never to a fresh owed review.
- **Skeptic:** Confirmed medium. The item ignores the owner's FR-9 answer.

### B2-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `design.input` routes a patch straight to `design.unit-spec`. A patch never reaches Plan, so it skips both `plan.dedupe` and `design.overlaps`.
- **Consequence:** A patch's write set is never checked against live builds, so strict's `design.overlap: refuse` never applies to it. A collision first shows at `build.unit-lease`, which only warns, or at Test's merge.
- **Fix:** Route patch, finding and fix inputs through `design.overlaps` for their unit before `design.unit-spec`.
- **Skeptic:** Confirmed medium.

### B3-F5 — A parent hold declares no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S5
- **Defect:** "A parent unlanded or paused → holds" declares no deadline and no outcome, and Deploy's policy list leaves out `flow.wait-ceiling`. The item fails `cl-dClosedLoop-0118`'s check that every wait declares both.
- **Consequence:** Gov's own item fails the design's static termination check as written, and a spec writer can build an unbounded hold.
- **Fix:** Write the hold as "holds until `flow.wait-ceiling`, then as `deps.on-parent-withdrawn` says, with an owner item", a counted wait with its witness.
- **Skeptic:** Confirmed medium. v2's `flow.wait-ceiling` row and stall-and-loop item 6 give dependency holds a deadline and a default ("replan"), so a terminal exists and c2 does not hold.

### B3-F6 — dWitnessedBar owns the remote verdict, but no unit builds it
- **Address:** architecture-v2 [chain] dWitnessedBar row; architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S2
- **Defect:** gap-test-02 (HIGH) gives dWitnessedBar the verdict-backend registry and the remote verdict under `verdict: remote-ci`. No clause in 0339 to 0368, or in any other row, builds the registry, the `remote-ci` read, or `verdict.remote.trust`, `.pin-scope` and `.pin`. The integrations clauses (0425, 0429, 0432) do not build them either.
- **Consequence:** A node that selects `remote-ci` is judged by a workflow in the tree it judges, with no pin or trust guard. `cl-dClosedLoop-0014`'s no-reader arm reds the three keys once dWitnessedBar lands.
- **Fix:** Give dWitnessedBar a clause for the backend registry and the pinned-workflow trust arm, seen red on a build that edits its own pinned workflow. Or move gap-test-02 and the three keys to an integrations row and record the move.
- **Skeptic:** Confirmed medium.

### B3-F7 — `test.route` sends a non-blocking MIXED red two ways
- **Address:** flow-steps [test] `test.route`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The arm "an OWN or MIXED red → `test.attribute`" has no blocking condition, and "a red that does not block → an ask" also applies. Under the default `verdict.blocks: own-only` MIXED does not block, so a MIXED red matches both arms.
- **Consequence:** A spec writer cannot tell whether a MIXED red goes to the tester and a fix pass, or to an ask that lets the landing go ahead.
- **Fix:** Write the arm as "an OWN red, or a MIXED red where `verdict.blocks` blocks it → `test.attribute`".
- **Skeptic:** Confirmed medium. layer-flow [settled] routes MIXED to an ask when it does not block.

### B3-F9 — After the push, an unreachable remote spends the rework budget
- **Address:** flow-steps [deploy] `deploy.notify`, `deploy.snapshot`, `deploy.unlease`, `deploy.close`; flow-steps [rules]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Defect:** All four items write to the remote. Unlike `deploy.land`, none declares an unreachable-remote outcome, so a failed act takes [rules]' default refusal route, which draws on the rework budget.
- **Consequence:** A remote outage after the push charges a landed build's budget, one draw per failed act.
- **Fix:** Class an unreachable remote as contention for every command item: a retry that draws nothing, then an owner item at `flow.wait-ceiling`, as `deploy.land` does.
- **Skeptic:** Confirmed medium. The walker's run to exhaustion is overstated: layer-runtime's `stale-remote` answer holds and retries without a draw while refs cannot be read.

### B3-F10 — `landing.order` is never read, so strict's `owner-orders` does nothing
- **Address:** flow-steps [deploy] (landing order); architecture-v2 [chain] `cl-dClosedLoop-0422`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `landing.order` appears only in [deploy]'s prose and Deploy's policy list. No item's Does cell reads it. `cl-dClosedLoop-0422` says only "landings ordered through the landing queue it builds".
- **Consequence:** Strict's `owner-orders` is silently ignored, and concurrent landings go in whatever order the queue takes.
- **Fix:** Have 0422 read `landing.order` with an arm per value, and have `deploy.land` need the queue's admission. Seed an `owner-orders` landing admitted with no order.
- **Skeptic:** Confirmed medium.

### B3-F11 — `deploy.mandate` reads the intake record as the plan-only mandate
- **Address:** flow-steps [deploy] `deploy.mandate`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Defect:** Under `plan-only` the mandate's witness is "the intake record". v2's 2026-10-14 revision makes the owner's plan ratification the mandate. Under `plan.ratification`'s other values (terminal-command, hook-keyword, signed-commit) the ratification is the owner's disposition at `plan.exit`. A triage-selected build has no intake record.
- **Consequence:** The landing's authority is read from the wrong record. A ratified plan goes unchecked, a triage-selected build has no witness, and a Maintain patch is mandated by an agent-typed intake, the defect gap-flow-14 records.
- **Fix:** Witness the mandate per entry: the `plan.exit` ratification, the triage record for a select, and `patch.ratify`'s disposition for a patch.
- **Skeptic:** Confirmed medium.

### B3-F12 — `deploy.distill` can pass on an empty join before dScopedBuild lands
- **Address:** flow-steps [deploy] `deploy.distill`; architecture-v2 [chain] dShippedRelease row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `deploy.distill` joins the decision-log rows `build.distill` wrote (dScopedBuild) to the build's major forks (dIndexedDesign's fork classes). Neither build is an ancestor of dShippedRelease. v2 has no rule that an empty join is anything but green.
- **Consequence:** If dShippedRelease lands first, `deploy.distill` joins zero forks to zero rows and passes.
- **Fix:** Add dScopedBuild to dShippedRelease's parents. Or have `deploy.distill` report "measured nothing" and never pass until `build.distill`'s writer lands, seen red on an empty population.
- **Skeptic:** Confirmed medium. v2's only non-empty-population clause is the tag join's.

### B3-F13 — `test.exit` writes to a lease record that dWitnessedBar's parents don't build
- **Address:** flow-steps [test] `test.exit`; architecture-v2 [chain] dWitnessedBar row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `test.exit` records "the verified tree on the build's lease record". The lease kind is dPlacedRequest's. dWitnessedBar's only parent is dDeclaredLoop, and its row declares no stand-in.
- **Consequence:** dWitnessedBar's exit item writes into a record kind no ancestor provides.
- **Fix:** Declare a stand-in, for example the verified tree on the transition record until dPlacedRequest lands, or add dPlacedRequest to dWitnessedBar's parents.
- **Skeptic:** Confirmed medium.

### B4-F3 — The breakpoint program has no route for a CEILING or NON-CONVERGENT round
- **Address:** flow-steps [breakpoint] `review.fold`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S6
- **Defect:** Neither `review.fold` nor `review.dispose` has a CEILING or NON-CONVERGENT outcome. The [breakpoint] policy list leaves out `review.max-rounds` and `flow.rework-budget`. [rules] sends open work only to asks, where `cl-dClosedLoop-0117` sends it to units while budget remains.
- **Consequence:** The item table that the static check reads has no outcome for the round refused past the limit.
- **Fix:** Give `review.fold` and `review.dispose` the outcomes CEILING and NON-CONVERGENT, routed to promotion: units while budget remains, asks after. Add the two keys to the [breakpoint] policy list.
- **Skeptic:** Confirmed medium. Rounds count against `flow.route-backs`, past which [rules] ends the loop non-converging, so a terminal is reachable without B4-F2 and c2 does not hold.

### B4-F4 — `review.dispose` routes by two artifact states, while a breakpoint pins four artifacts
- **Address:** flow-steps [breakpoint] `review.dispose`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `review.pin` pins a plan revision, spec revisions, a commit range or a landing record. `review.dispose` routes only "an unbuilt spec" and "built work". A landing review's findings "become new units", against [deploy]'s rule that they enter as patch builds by the post-close row, and [transitions] has no deploying → designing row after the push.
- **Consequence:** A Plan review's findings have no route. A landing review's findings become units of a landed build, through a transition the table lacks.
- **Fix:** Add an arm per artifact: a plan revision to `plan.record` for revision, and a landing record to a patch-build intake by the post-close row.
- **Skeptic:** Confirmed medium.

### B4-F5 — A paused build's lease renewal contradicts the default renewal rule
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium (the walker graded it high)
- **Scenario:** S5
- **Defect:** [lifecycle] has the supervisor renew a paused build's leases. The default `leases.renewal: progress` renews only on witnessed progress and on declared waits inside their deadline, never on a beat alone, and no record declares pause as such a wait. `life.quiesce` routes "pause → parked", while `cl-dClosedLoop-0326`'s parking releases the lease.
- **Consequence:** A spec writer either lets a paused build's lease expire, so another node can pick the build up, or renews it with no deadline, against P39.
- **Fix:** Declare pause a wait with a deadline (`flow.wait-ceiling` or its own key) and an outcome, renewed under `progress` as a declared wait. Rename the route to `paused`.
- **Skeptic:** Confirmed medium. Two records disagree, but no scenario is shown to fail.

### B4-F8 — `life.quiesce` reaches only the driver's own acts
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Defect:** The witness is "the executor's record of the acts it let finish". A unit holder in another session or node (`cl-dClosedLoop-0319`) is never told. Once quiesce dispatches nothing new, no route takes a finished review fan's findings to `review.dispose` or to asks.
- **Consequence:** A remote holder's passes run unrecorded until the fence refuses them after `life.unlease`. A finished review's findings are disposed into a withdrawn build, or lost.
- **Fix:** Have `life.quiesce` post a quiesce message to every unit holder and join their acknowledgements into its witness. Route a finished review's findings to asks under withdraw and to the replacement under supersede.
- **Skeptic:** Confirmed medium.

### B4-F9 — `probe.judge` mixes three actor kinds
- **Address:** flow-steps [probe] `probe.judge`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The actor is "command: the executor's re-run, or the experiment's scorer". The witness adds "the verifier's judgment", and [probe] Roles adds "a blind judge". The executor, a command and a role act in one item, against [rules]' one actor of one kind.
- **Consequence:** The item cannot get one work order, allowance or return schema, and its role arm has no actor.
- **Fix:** Split it into `probe.judge` (a command: the re-run or the scorer) and `probe.judge-claimed` (the tester or a blind judge), routed when no command can judge.
- **Skeptic:** Confirmed medium.

### B4-F10 — The reproduction probe before a patch fix has no trigger
- **Address:** flow-steps [probe] `probe.trigger`
- **Class:** K6
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `cl-dClosedLoop-0408` owes a red-first `reproduction` probe before a patch build's fix when the build comes from a bug report. `probe.trigger`'s closed set has no arm for it, `probe.points` defaults to `none`, and `design.input` sends a patch straight to `design.unit-spec`.
- **Consequence:** Nothing opens the reproduction, so a patch fix lands without its red-first witness.
- **Fix:** Add the trigger "a patch build from a bug report" to `probe.trigger`, at the boundary before the patch's first `build.unit-pass`. Name it in `design.input`'s patch route.
- **Skeptic:** Confirmed medium.

### B4-F11 — dFairHearing's breakpoint items rest on later builds with no stand-in
- **Address:** flow-steps [breakpoint] `review.pin`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** dFairHearing's `review.pin` picks `design-audit` by the record-kind registry, which dTotalRecall builds later in the chain. `review.report` routes to `review.dispose`, which is dDeclaredLoop's and not an ancestor. [breakpoint] declares no stand-ins, unlike [probe], and `[stage0-classes]` is empty.
- **Consequence:** When dFairHearing lands, its preset choice and its next route name parts that do not exist yet.
- **Fix:** Declare stand-ins in [breakpoint] as [probe] does: a record kind read from the filename, and disposition by hand until dDeclaredLoop. Class the lead in `[stage0-classes]`.
- **Skeptic:** Confirmed medium. The slug-claim leg is weaker: compare-and-swap ref claims exist today (unattended's `refs/gov/runs`), though no chain clause builds `refs/gov/class-claims`.

### B4-F14 — P29's row leaves out the clauses that carry most of P29
- **Address:** architecture-v2 [enforcement] `P29`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **Defect:** P29's row names only `cl-dClosedLoop-0178`, which covers its first two rules. The verifier-context, answered-calls and false-facts rules sit in `cl-dClosedLoop-0196`, `0197` and `0198`, outside the row.
- **Consequence:** dOrderedCharter's meta-check never joins three of P29's rules to the principle.
- **Fix:** Add 0196, 0197 and 0198 to P29's row.
- **Skeptic:** Confirmed medium.

### B5-F4 — `loop.lease` and `release.pick` leave a lease held elsewhere unrouted, and E's promotion lease is never released
- **Address:** layer-expansions [design-observability] `loop.lease`; [design-integrations] `release.pick`, `release.record`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `loop.lease` routes only to `loop.gather`, and `release.pick` only to `release.approve`. Neither has the "held elsewhere" or "done" outcome `maintain.lease` declares. Neither `release.record` nor any dShippedRelease clause releases E's promotion lease.
- **Consequence:** Node x's instance has no outcome while node d holds the week's lease or E's. A finished pass leaves E's lease held, so the next landed SHA's pick blocks until expiry.
- **Fix:** Give `loop.lease` and `release.pick` the outcomes `maintain.lease` has: held elsewhere → skip; done → nothing. Make `release.record` release E's promotion lease.
- **Skeptic:** Confirmed medium. "Promotion lease" appears nowhere else in the design.

### B5-F5 — Concurrent `kits.cut` instances race for one tag number
- **Address:** layer-expansions [design-distribution] `kits.cut`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** Under `every-landing` each cut instance is keyed by its landed SHA and takes its own lease. Nothing serialises the choice of `<n>` in `gov/v<date>.<n>`.
- **Consequence:** Two near-simultaneous landings pick the same tag number. The refused push becomes an owner item, its only route.
- **Fix:** Serialise cuts under one lease for the tag series. On a refused tag push, refetch and renumber within `flow.route-backs`, and raise an owner item only past that bound.
- **Skeptic:** Confirmed medium.

### B5-F8 — `adopt.decisions` has two actor kinds and no route when the raters disagree
- **Address:** flow-steps [adopt] `adopt.decisions`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S7
- **Defect:** The actor is two kinds: the reviewer as two raters, and the owner. The routes are only "accepted" and "declined by the owner". None covers raters who disagree, or agreement under the kappa 0.8 bar `cl-dClosedLoop-0238` sets.
- **Consequence:** When dLinkedLibrary routes gov's own decision rows, a disagreement or a low kappa has no outcome. Under the default `author-rubric`, a candidate the raters reject has no route either.
- **Fix:** Split the item per actor: a raters item that computes agreement, and an owner item under `docs-owner-ratifies`. Add routes for disagreement (to the owner or a third rater) and for a kappa below the bar (a re-rating round on the budget).
- **Skeptic:** Confirmed medium. research-retrofit-a's "kappa < 0.8 → rubric revised" was not carried forward.

### B5-F11 — `maintain.read` routes neither `maintain.tiers` nor `maintain.on-breach`
- **Address:** layer-expansions [design-observability] `maintain.read`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `maintain.read` routes only in pin, over pin and dead, with no arm per band of the default `maintain.tiers: bands`. `maintain.file` always files an ask, so `maintain.on-breach`'s `red-leg` and `report` values have no arm. flow-steps [rules] requires routes declared per policy value.
- **Consequence:** A reading in the log or diagnose band has no route, and two of `maintain.on-breach`'s three values do nothing.
- **Fix:** Give `maintain.read` one route per tier band, and `maintain.file` one arm per `maintain.on-breach` value, each with its own witness.
- **Skeptic:** Confirmed medium.

### B5-F14 — dTendedCadence's release-verify-failed join depends on dShippedRelease, which is not its ancestor
- **Address:** layer-expansions [design-observability] `maintain.file`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `maintain.file`'s ask for `release-verify-failed` joins `release.route`'s, and its fixture needs `release.route`. `release.route` is dShippedRelease's, and neither build is the other's ancestor. `maintain.events` defaults to all three events.
- **Consequence:** If dTendedCadence lands first, the join and its fixture have nothing to run against, so the arm lands unseen red or is skipped.
- **Fix:** Put the fixture and the join on dShippedRelease's row, or on a build descended from both (only dConvergedCharter is). Record dTendedCadence's event arm as a stand-in until then.
- **Skeptic:** Confirmed medium.

### B5-F15 — `adopt.instructions` and `adopt.declarations` have no row in the adopt step
- **Address:** flow-steps [adopt]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Defect:** [adopt] has five rows. adopter-instructions and flow-roles-adoption add `adopt.instructions` (`cl-dClosedLoop-0260`) and `adopt.declarations` (`cl-dClosedLoop-0438`) to the `adopt` program, and neither has a row.
- **Consequence:** S4's declarations, proposed as overlay rows, have no actor, Needs, witness or route. Neither the item join nor Stage 0's K1 can see either item.
- **Fix:** Add both rows, each with its owner build, Needs (`kits.install` or `kits.update`), witness (the proposal records) and routes (the owner's one ruling per row).
- **Skeptic:** Confirmed medium.

### BS1-F1 — `verdict.flakes` declares one threshold, which `test.select` reads as the release streak and `test.flakes` as the quarantine entry
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `verdict.flakes` declares one threshold. `test.select` reads it as the streak of consecutive greens that releases a held leg, and `test.flakes` as the point past which a leg is held. The only default declared anywhere is the release streak of three greens.
- **Consequence:** Under the default `quarantine`, nothing says how many flakes put a leg in quarantine. Whether a flaky leg blocks an attended build is undefined.
- **Fix:** Split the key into an entry threshold (flakes per window, with a default) and the release streak (three consecutive greens), each with its own seen-red on `cl-dClosedLoop-0346`.
- **Skeptic:** Raised by skeptic batch 1 at `test.flakes` S1, where walker 3 gave `holds`. No second skeptic tested it.

### BS1-F2 — The release program's promotion lease is no lease the grammar declares, and its rollback is not fenced
- **Address:** layer-expansions `release.route` and `release.pick`; layer-runtime [Fencing]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `release.pick` takes "E's promotion lease", which `cl-dClosedLoop-0120`'s lease grammar (builds, units and cadence runs) does not declare. The fence travels only with pushes by the commit queue and the lander, and `release.route` rolls E back through an engine adapter.
- **Consequence:** Where `release.environments` is set, a stale holder's in-flight rollback can reach E after another node has taken E's lease and promoted a newer SHA. E silently runs the older release, and its records disagree with what it runs.
- **Fix:** Add the promotion lease, with its epoch, to dPlacedRequest's lease grammar. Require every engine adapter's promote and rollback to check that epoch, or to compare-and-swap on E's current deployment id. Seen red on a planted stale holder's rollback after a take-over.
- **Skeptic:** Raised by skeptic batch 1 at `release.route` S2, where walker 5 gave `holds`. No second skeptic tested it.

### BS2-F1 — `plan.input` pins an intake record that no ancestor of dRankedPlan writes
- **Address:** flow-steps [plan] `plan.input`; architecture-v2 [chain] `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `plan.input` pins the intake record, which `cl-dClosedLoop-0377` says dWellOiledMachine's prompt-submit hook writes. dWellOiledMachine is not among dRankedPlan's parents, and `cl-dClosedLoop-0378`'s stand-in covers only `plan.exit`'s ratification. No prompt-submit hook exists in today's tree.
- **Consequence:** When dRankedPlan lands, a build started from an owner prompt has nothing for `plan.input` to pin, and `plan.record` drafts from words nothing witnesses.
- **Fix:** Give `plan.input` the stand-in 0378 gives `plan.exit`: pin `entry.orient`'s "intake absent" record, with the owner's words taken as the owner gate's disposition, until dWellOiledMachine lands.
- **Skeptic:** Raised by skeptic batch 2 at `plan.input` S7, where walker 1 gave `holds`. No second skeptic tested it.

### BS2-F2 — `release.approve` has two actors of two kinds, chosen by a policy value
- **Address:** layer-expansions [design-integrations] `release.approve`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S7
- **Defect:** The actor is "the owner, or a command", chosen by `deploy.promotion`. flow-steps [rules] makes an item whose actor a policy value chooses one item per value.
- **Consequence:** dDeclaredLoop's item factory cannot declare the item as written. `owner-approves-prod` and `auto-on-green` share one tag and one outcome table.
- **Fix:** Split it into `release.approve-owner` (the owner, under `owner-approves-*`) and `release.approve-auto` (a command, under `auto-on-green`), routed from `release.pick` by `deploy.promotion`'s value.
- **Skeptic:** Raised by skeptic batch 2 at `release.approve` S7, where walker 5 gave `holds`. No second skeptic tested it.

### BS3-F1 — An owner's late answer to a Plan question has no route
- **Address:** flow-steps [plan] `plan.record`; [breakpoint] (the owner gate); [transitions]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `plan.record` resolves an owner question as [breakpoint]'s owner gate does, and the default `run.on-owner-question: best-effort-recorded` resolves it when it is raised, although attendance asks it live. [transitions]' amendment row covers only building, testing, or deploying before the push, and `entry.place`'s `continue` goes to the build's `next`.
- **Consequence:** In S1 the plan is drafted on the supervisor's recorded choice, and no item takes in the owner's later answer during planning.
- **Fix:** Under attendance, hold an owner question until `run.owner-deadline` before best effort decides. Route an answer that arrives after the choice back to `plan.record` as a re-entry, and add a planning row to the amendment transition.
- **Skeptic:** Raised by skeptic batch 3 at `plan.record` S1 and S6, where walker 1 gave `holds`. No second skeptic tested it. Batch 1 refuted the neighbouring B4-F13 because a late answer re-enters through `entry.intake` and `entry.place`. This finding says that route has no planning arm.

### BS3-F2 — `loop.file` files asks with no acceptance, which the default refuses
- **Address:** layer-expansions [design-observability] `loop.file`; layer-memory [asks]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** layer-memory [asks] refuses a filing that states no `accept` line, and `asks.acceptance` defaults to `refuse`. `loop.file` states none, unlike `maintain.file`.
- **Consequence:** Every Loop Review proposal's filing is refused. A cadence run has no build budget, so the run re-files every beat and never reaches the owner's breakpoint.
- **Fix:** State `loop.file`'s acceptance, either the owner's `review.loop.retire` breakpoint disposing the row or a keep record. Plant an ask that is refused without it.
- **Skeptic:** Raised by skeptic batch 3 at `loop.file` S2, where walker 5 gave `holds`. No second skeptic tested it.

### BS4-F1 — `kits.adopters` has no outcome for an unreachable remote or an unreadable receipt
- **Address:** layer-expansions [design-distribution] `kits.adopters`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Defect:** The row reads each adopter's committed receipt at its remote tip and routes only by `deploy.currency`'s value. [agree-distribution] settles that an unreachable remote is unverified, never green, and the sibling `kits.currency` carries that outcome. `kits.adopters` does not.
- **Consequence:** If an adopter's remote or receipt cannot be read during S4's migration, the reading has no outcome. It may show as "0 behind" or be dropped, and under `push-branches` an offer may go out against a receipt nobody read.
- **Fix:** Add "unreachable or unreadable → the adopter record unverified, never green, reported as `pull-and-watch` reports, and no `kits.offer`". Seed a planted unreachable remote.
- **Skeptic:** Raised by skeptic batch 4 at `kits.adopters` S4, where walker 5 gave `holds`. No second skeptic tested it.

## Low

### B1-F11 — `entry.orient` hard-codes `kickoff.runs`' default
- **Address:** flow-steps [entry] `entry.orient`
- **Class:** K4
- **Severity:** low
- **Scenario:** S1
- **Defect:** The Does cell runs "the full kickoff's where no READY card exists", which hard-codes `no-ready-card`. `cl-dClosedLoop-0376` says "only where `kickoff.runs` says", and neither [entry]'s nor [plan]'s policy list names the key.
- **Consequence:** `every-session`, `opening-a-build` and `plan-absorbs` have no effect.
- **Fix:** Write "as `kickoff.runs` says", and add the key to [entry]'s policy list.
- **Skeptic:** Confirmed low.

### B2-F12 — v2 never defines the text a clause hash is taken over
- **Address:** architecture-v2 [clause-ids]
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Defect:** [clause-ids] says only "its text's hash being its revision". The normalisation (SHA-256, the first eight hex digits, the id cut off, whitespace folded) is defined only in carries.py, which neither v2 nor final-questions cites.
- **Consequence:** A dTrueNorth spec writer working from v2 can choose another normalisation, and every pin the instrument wrote then reads stale under the product join.
- **Fix:** State the hash rule in [clause-ids], and have `cl-dClosedLoop-0001` cite it.
- **Skeptic:** Confirmed low.

### B2-F14 — P17's classifier is marked "(proposed)" in its one enforcing clause
- **Address:** architecture-v2 [enforcement] `P17` / [chain] `cl-dClosedLoop-0390`
- **Class:** K5
- **Severity:** low (the walker graded it medium, c5)
- **Scenario:** S1
- **Defect:** 0390 reads "additive-versus-breaking interface classification (proposed)". It is the only such marker in v2, and it is stale: flow records FL-B4 as answered.
- **Consequence:** A spec writer can read P17's classifier as not yet committed.
- **Fix:** Drop "(proposed)" from 0390.
- **Skeptic:** Confirmed low, not c5. The classifier is carried in the same clause ("two-level re-entry by `design.reentry`"), and flow-steps makes `design.reentry` a dIndexedDesign command that classifies an amendment by a structural diff.

### B2-F17 — `design.streams`' Needs reads as needing itself
- **Address:** flow-steps [design] `design.streams`
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Defect:** Needs reads "`design.overlaps`, where `design.streams` holds for the build". Short tags in the tables are item tags, so the cell names its own item.
- **Consequence:** The composer's acyclic-needs check reds gov's own item, or a reader skips it.
- **Fix:** Write the condition as `policy.design.streams`, the full spelling the opening reserves, outside the Needs tags.
- **Skeptic:** Confirmed low, a wording fix.

### B2-F19 — `design.ready`'s witness lacks the UNCARRIED class its clause adds
- **Address:** flow-steps [design] `design.ready`
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Defect:** The witness is "none MISSING, THIN or FORKED". `cl-dClosedLoop-0398`, the same owner's clause, adds "`design.ready` gaining an UNCARRIED class".
- **Consequence:** A spec writer working from the item draft leaves out the coverage arm.
- **Fix:** Add UNCARRIED, under `design.coverage`, to the item's witness.
- **Skeptic:** Confirmed low.

### B4-F7 — "Once a push is made, the build has landed" reads every pass push as a landing
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** low (the walker graded it medium)
- **Scenario:** S5
- **Defect:** The sentence is ambiguous now that `cl-dClosedLoop-0318` pushes every pass commit.
- **Consequence:** Read literally, X's first pass push refuses the owner's withdraw mid-Build.
- **Fix:** Write "once the landing push to the default branch is made". Add a fixture that withdraws after a pass push and is refused only after the landing push.
- **Skeptic:** Confirmed low. The same sentence equates the push with landing, and [transitions] reads "before the push" in Deploy's context, so it is a wording fix.

### B4-F12 — `review.cost` writes shape fields before the shapes registry exists
- **Address:** flow-steps [breakpoint] `review.cost`
- **Class:** K7
- **Severity:** low
- **Scenario:** S7
- **Defect:** `review.cost` is dDeclaredLoop's, but it writes `shape`, `efforts` and `role-sha` into the shape-run kind, which is dTotalRecall's, and its `shape` comes from the registry dBoundRoles builds. No stand-in is declared.
- **Consequence:** From dDeclaredLoop until dBoundRoles lands, the item writes fields that have no source.
- **Fix:** State a stand-in (shape and role-sha left blank until dBoundRoles), or move the extension onto dBoundRoles.
- **Skeptic:** Confirmed low. Today's `renderShapeLine` has neither field.

### B4-F15 — Slice items write record kinds that are not registered
- **Address:** layer-memory [contract]
- **Class:** K3
- **Severity:** low
- **Scenario:** S5
- **Defect:** The kind table has no row for "the trigger record" (`probe.trigger`), "the command's record" (`life.request`) or "the executor's record of the acts it let finish" (`life.quiesce`).
- **Consequence:** Stage 0's K3 arm reads registered kinds only, so the three records have no declared reader, home or check.
- **Fix:** Register `probe trigger`, `lifecycle request` and `quiesce` rows, each with its writer item and readers.
- **Skeptic:** Confirmed low.

### B5-F10 — `kits.offer`'s counts and the receipt schema are stale against v2
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K1
- **Severity:** low
- **Scenario:** S4
- **Defect:** The row says "adds an eighth; the mode refuses all eight", and the contract row says "schema 4". `cl-dClosedLoop-0435`, on the same build's row, adds a ninth spawn kind and moves the receipt to schema 5.
- **Consequence:** A spec writer building the offer mode from the row misses the ninth kind and the schema-5 fields S4's migration needs.
- **Fix:** Bring the row's count and the receipt line up to 0435.
- **Skeptic:** Confirmed low.

### BS3-F4 — `design.recommend` does not declare whether it is idempotent or reconciles
- **Address:** flow-steps [design] `design.recommend`; [rules] (the command-item bullet)
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Defect:** [rules] says every command item declares whether it is idempotent or reconciles. The item's Actor cell says only "command", and most other command items have the same gap.
- **Consequence:** When node d's session limit hands the build over in S2, the successor cannot tell whether to re-score or to reconcile with the recommendation already written.
- **Fix:** Declare it on every command item, and add a check that reds a command Actor cell with neither word.
- **Skeptic:** Raised by skeptic batch 3 at `design.recommend` S2, where walker 2 gave `holds`. No second skeptic tested it.

## Refuted

### B1-F6 — A queued claim replayed after a withdrawal "counts as claimed" through the own-key rule
- **Address:** flow-steps [entry] `entry.claim`
- **Skeptic:** Refuted. [transitions] derives each state from witnesses and the engine refuses any transition the table lacks, and withdrawn is terminal. The refusal takes [rules]' default route ("recorded, and `next` returns the frontier"), and layer-runtime [decide] answers `terminal` and closes the run. The replay neither reopens the build nor goes unrouted.

### B1-F7 — A refused lease and an unusable remote have no defined route at `entry.claim` or `plan.lease`
- **Address:** flow-steps [entry] `entry.claim`
- **Skeptic:** Refuted. The default `leases: warn` is the overlap stance: an overlap is warned and the lease taken, as `plan.lease`'s "an overlap → noted on the card" shows, so "refused under the default" is never reached. An unreachable remote is `leases.offline`'s case, which covers every compare-and-swap mint (`cl-dClosedLoop-0120`). A ref the remote refuses takes [rules]' default refusal route under P39's SL-7.

### B1-F8 — dPlacedRequest's entry routes and slug mint depend on builds that are not its ancestors
- **Address:** flow-steps [entry] `entry.place`
- **Skeptic:** Refuted. The routes are outputs, not inputs: "claimed → Plan" and "→ Design" end at transitions in dDeclaredLoop's table, an ancestor, and no witness needs dRankedPlan's or dIndexedDesign's items. The `builds.slug-*` keys read at their catalogue defaults through dGroundRules' reader. Today's mint and `check_slug_claimed` exist in `tools/memory-tree/gen_build_index.py`. v2:483 is a revision note, not a general rule.

### B1-F12 — Two owners stated for the entry step's items
- **Address:** architecture-v2 [chain]-preamble revision note (PM-9)
- **Skeptic:** Refuted. v2:401 is a dated history entry, and the 2026-10-18 note at v2:504-506 moves the entry items to dPlacedRequest. Ownership is a field on the node, and flow-steps' Owner column names dPlacedRequest, so a spec writer sees one owner.

### B2-F4 — The per-unit budget share has no single freeze point, so each Design re-entry can mint budget
- **Address:** architecture-v2 [policies] `flow.rework-budget`; flow-steps [design] `design.exit`
- **Skeptic:** Refuted. `cl-dClosedLoop-0115` fixes a single freeze, keys the budget "to the build so units a loop mints cannot reset it", and requires it seen red on a planted loop that mints a new unit each lap. `cl-dClosedLoop-0440` puts patch builds on the originating build's one budget.

### B2-F7 — A cross-node unit has no workspace or integration rule under the default `build.worktree: shared`
- **Address:** layer-runtime [isolate]; flow-steps [build] `build.unit-pass`
- **Skeptic:** Refuted. `cl-dClosedLoop-0319` and night-pass-two say a unit taken by a session that does not hold the build is driven "only that unit's passes on its own branch", reaching the build's driver through the branch. layer-runtime [isolate] merges each unit branch into the build branch before the unit's lease is released.

### B2-F13 — `cl-dClosedLoop-0407` places `drop_touched_exemptions` in `tools/lib`, but it lives in the map kit
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0407`
- **Skeptic:** Refuted. `cl-dClosedLoop-0049` (dOrderedCharter, an ancestor of dScopedBuild) already moves `compute_coverage` to `tools/lib` with the pure `drop_touched_exemptions` beside it, re-points the consumers in the same unit and keeps a re-export. 0407 describes the state after that move, and the walker's grep shows today's tree, not the design.

### B2-F15 — No clause enforces P18's ranking of a fork's options
- **Address:** architecture-v2 [enforcement] `P18` / [chain] `cl-dClosedLoop-0176`, `cl-dClosedLoop-0390`
- **Skeptic:** Refuted. 0390 carries "fork resolution by `design.forks`", whose default `agents-feature-rich-expandable` is the ranking rule, and the charter renders it at level 0. 0176 and the fork record carry "with a full record". A ranked-list field is an addition the fix proposes, not a gap in the clauses.

### B3-F4 — The owner's landing gate can be passed by the supervisor's own choice
- **Address:** flow-steps [deploy] `deploy.mandate`; flow-steps [breakpoint]; architecture-v2 [policies] `run.on-owner-question`
- **Skeptic:** Refuted. Resolving an owner breakpoint by `run.on-owner-question`, including `best-effort-recorded`, is the owner's own LR-3 answer, and research-final-coverage records reversing it as a defect caught earlier. LR-3 carves out only ratifications, and the landing gate is an authorization. No preset pairs `three-gates` with `best-effort-recorded`: strict pairs `every-stage` with `park-item`.

### B3-F8 — Several Test and Deploy outcomes end at an ask, leaving the build with no next step
- **Address:** flow-steps [test] `test.merge`; flow-steps [deploy] `deploy.land`
- **Skeptic:** Refuted. A refused `test.merge` has no witness, so by [rules] it stays on the frontier, and each re-dispatch draws on `flow.rework-budget`. If the frontier empties while the build is open, layer-runtime [decide] answers `stuck`, which raises an owner item at once.

### B4-F13 — An owner's late answer after the deadline has no route
- **Address:** flow-steps [breakpoint]
- **Skeptic:** Refuted. A late owner answer is a prompt in an owner-bound session, so `entry.intake` records it and `entry.place` disposes of it from its closed set: amend → Design re-entry, or an `intake` message to the session holding the build. P22 gives every request a recorded disposition.

### B5-F7 — `kits.offer`'s pushed route files no order for the adopter's `test.seed` and `adopt` runs
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Skeptic:** Refuted. The row routes "an update that needs target-side execution … → an outbox order" and names the update hook running `test.seed` and `adopt` as target-side code, as `cl-dClosedLoop-0430` and retrofit [seed] say. No pushed path skips the order. Under `unarmed` an unseeded check is never green, and under `refuse` the adopter's lander refuses the update.

### B5-F9 — Under the default `on-touch`, nothing reconstructs records
- **Address:** flow-steps [adopt] `adopt.reconstruct`
- **Skeptic:** Refuted. retrofit defines on-touch reconstruction as a first-touch dossier. `build.unit-pass` carries "where the map is installed the claiming dossier's edit", and `cl-dClosedLoop-0406` (dScopedBuild) carries the dossier claim. The duty has a clause and an item, in other words than the walker searched for.

### B5-F12 — Cadence period keys come from each node's own clock
- **Address:** layer-runtime [schedule]
- **Skeptic:** Refuted. [schedule] checks the witness for each period key before and after taking the lease, and a missed period runs at the next wake. A slow node either finds the earlier period's witness and skips, or runs a period that never ran. No key runs twice.

### B5-F13 — An install or update trusts a mutable, unpinned tag name
- **Address:** layer-expansions [design-distribution] `kits.currency`
- **Skeptic:** Refuted. The premise "with no commit" is false: `kits.currency` counts tags after the installed commit, today's receipt records `gov_commit` and each row's `commit`, `gov_oid` and `sha256`, and schemas 4 and 5 extend it. A moved tag installs under a receipt naming a different commit and blob ids. The tag-date skew is seconds against releases days apart.

## Walk table

The table carries the walkers' verdicts as given. A cell that names a refuted id, or that a skeptic re-walked to a `BS` finding above, is left as the walker wrote it.

| Item | Scenario | Actor | Needs | Witness | Route | Verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S1 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S2 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S3 | the filer | = | = | = | not on path: a Maintain filing reaches no owner session, so the filer writes intake |
| `entry.intake` | S4 | = | = | = | = | not on path: update runs as kits.update outside any build and places no request |
| `entry.intake` | S5 | scout, not the hook | = | scout-typed entry | = | B1-F1 |
| `entry.intake` | S6 | scout, not the hook | = | scout-typed entry | no intake → entry.orient records it absent | B1-F1 |
| `entry.intake` | S7 | hook unlanded until dWellOiledMachine | = | absent | entry.orient records it absent | holds |
| `entry.orient` | S1 | = | = | = | = | B1-F11 |
| `entry.orient` | S2 | = | = | = | = | holds |
| `entry.orient` | S3 | = | the filer's intake | = | = | holds |
| `entry.orient` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.orient` | S5 | = | = | = | = | holds |
| `entry.orient` | S6 | = | = | = | = | holds |
| `entry.orient` | S7 | = | = | = | = | holds |
| `entry.place` | S1 | = | = | = | = | holds |
| `entry.place` | S2 | = | = | = | = | holds |
| `entry.place` | S3 | = | = | = | bypassed: maintain.patch goes to Design | B1-F4 |
| `entry.place` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place` | S5 | = | = | = | re-placement after plan.dedupe matches X | holds |
| `entry.place` | S6 | = | = | = | failed check loops bounded by cl-0132 | holds |
| `entry.place` | S7 | = | = | = | routes into unlanded Plan and Design items | B1-F8 |
| `entry.place-check` | S1 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S2 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S3 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place-check` | S5 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S6 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-check` | S7 | = | = | = | entry.place's outcomes into unlanded items | B1-F8 |
| `entry.place-owner` | S1 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S2 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S3 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.place-owner` | S5 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S6 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S7 | = | = | = | entry.place's outcomes into unlanded items | B1-F8 |
| `entry.claim` | S1 | = | = | = | = | holds |
| `entry.claim` | S2 | = | = | own-key retry trusted, no P23 clause | = | B1-F3 |
| `entry.claim` | S3 | = | patch disposition | claim and lease, no originating build | no route when the originating budget is spent | B1-F5 |
| `entry.claim` | S4 | = | = | = | = | not on path: no request is placed during an update |
| `entry.claim` | S5 | = | replayed queued claim | own key found on a withdrawn slug | claimed → Plan on a terminal build | B1-F6 |
| `entry.claim` | S6 | = | = | = | refused lease undefined under warn; unusable remote unrouted | B1-F7 |
| `entry.claim` | S7 | = | = | = | slug minted by keys of unlanded dTotalRecall | B1-F8 |
| `plan.input` | S1 | = | = | = | = | holds |
| `plan.input` | S2 | = | = | = | = | holds |
| `plan.input` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.input` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.input` | S5 | = | = | = | = | holds |
| `plan.input` | S6 | = | = | = | = | holds |
| `plan.input` | S7 | = | = | claim commit's content key until intake lands | = | holds |
| `plan.dedupe` | S1 | = | = | = | = | holds |
| `plan.dedupe` | S2 | = | = | = | = | holds |
| `plan.dedupe` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.dedupe` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.dedupe` | S5 | = | = | = | = | holds |
| `plan.dedupe` | S6 | = | = | = | = | holds |
| `plan.dedupe` | S7 | = | design index of unlanded dIndexedDesign | = | = | B1-F9 |
| `plan.triage-rule` | S1 | = | = | = | plan.triage values unread | B1-F10 |
| `plan.triage-rule` | S2 | = | = | = | = | holds |
| `plan.triage-rule` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.triage-rule` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.triage-rule` | S5 | = | = | = | = | holds |
| `plan.triage-rule` | S6 | = | = | = | = | holds |
| `plan.triage-rule` | S7 | = | = | = | = | holds |
| `plan.triage-judge` | S1 | planner, never the owner under owner-batches | = | = | = | B1-F10 |
| `plan.triage-judge` | S2 | = | = | = | = | holds |
| `plan.triage-judge` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.triage-judge` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.triage-judge` | S5 | = | = | = | = | holds |
| `plan.triage-judge` | S6 | = | = | = | = | holds |
| `plan.triage-judge` | S7 | = | = | = | = | holds |
| `plan.record` | S1 | = | = | = | owner question asked live | holds |
| `plan.record` | S2 | = | = | = | owner item via run.on-owner-question | holds |
| `plan.record` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.record` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.record` | S5 | = | = | = | = | holds |
| `plan.record` | S6 | = | = | = | = | holds |
| `plan.record` | S7 | = | = | = | = | holds |
| `plan.research` | S1 | = | = | = | = | holds |
| `plan.research` | S2 | = | = | = | = | holds |
| `plan.research` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.research` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.research` | S5 | = | = | = | = | holds |
| `plan.research` | S6 | = | = | = | round trip draws on the budget | holds |
| `plan.research` | S7 | = | = | = | = | holds |
| `plan.place` | S1 | = | = | = | = | holds |
| `plan.place` | S2 | = | = | = | = | holds |
| `plan.place` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.place` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.place` | S5 | = | = | = | = | holds |
| `plan.place` | S6 | = | = | = | = | holds |
| `plan.place` | S7 | = | = | = | = | holds |
| `plan.lease` | S1 | = | = | = | = | holds |
| `plan.lease` | S2 | = | = | expiry by observer clock, cl-0135 | = | holds |
| `plan.lease` | S3 | = | = | = | = | not on path: entry.claim takes a patch build's lease |
| `plan.lease` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.lease` | S5 | = | = | = | = | holds |
| `plan.lease` | S6 | = | = | = | refused → undefined under warn | B1-F7 |
| `plan.lease` | S7 | = | = | = | = | holds |
| `plan.recommend` | S1 | = | = | = | = | holds |
| `plan.recommend` | S2 | = | = | = | = | holds |
| `plan.recommend` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.recommend` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.recommend` | S5 | = | = | = | = | holds |
| `plan.recommend` | S6 | = | = | = | = | holds |
| `plan.recommend` | S7 | = | = | = | = | holds |
| `plan.reason` | S1 | = | = | = | = | holds |
| `plan.reason` | S2 | = | = | = | = | holds |
| `plan.reason` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.reason` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.reason` | S5 | = | = | = | = | holds |
| `plan.reason` | S6 | = | = | = | = | holds |
| `plan.reason` | S7 | = | = | = | = | holds |
| `plan.exit` | S1 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S2 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S3 | = | = | = | = | not on path: a patch build enters at Design |
| `plan.exit` | S4 | = | = | = | = | not on path: an update opens no build |
| `plan.exit` | S5 | = | = | planner-recorded go | = | B1-F2 |
| `plan.exit` | S6 | = | = | = | owner silence parks the build | holds |
| `plan.exit` | S7 | = | = | = | run.host of unlanded dWellOiledMachine | B1-F9 |
| `design.input` | S1 | = | = | = | = | holds |
| `design.input` | S2 | = | = | = | = | holds |
| `design.input` | S3 | = | = | = | patch → `design.unit-spec`, skipping overlaps | B2-F20 |
| `design.input` | S4 | = | = | = | = | not on path: update runs in the adopt program, outside any build |
| `design.input` | S5 | = | = | = | Z's plan record → `design.seams`, never `design.inventory` | B2-F5 |
| `design.input` | S6 | = | = | = | = | holds |
| `design.input` | S7 | = | = | = | = | holds |
| `design.reentry` | S1 | = | = | = | = | not on path: no amendment in S1; a late answer resolves an owner item |
| `design.reentry` | S2 | = | = | = | = | not on path: no amendment admitted |
| `design.reentry` | S3 | = | = | = | = | not on path: a patch enters as a micro-spec |
| `design.reentry` | S4 | = | = | = | = | not on path: outside any build |
| `design.reentry` | S5 | = | = | = | no trigger reads a parent's withdrawn notice | B2-F9 |
| `design.reentry` | S6 | = | = | = | = | not on path: no amendment in S6's failures |
| `design.reentry` | S7 | = | = | = | = | not on path: chain builds enter on a plan record |
| `design.inventory` | S1 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S2 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.inventory` | S4 | = | = | = | = | not on path: outside any build |
| `design.inventory` | S5 | = | X's built units | = | reached by no input of Z's | B2-F5 |
| `design.inventory` | S6 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S7 | = | = | = | = | not on path: no plan revision |
| `design.seams` | S1 | = | = | = | = | holds |
| `design.seams` | S2 | = | = | = | = | holds |
| `design.seams` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.seams` | S4 | = | = | = | = | not on path: outside any build |
| `design.seams` | S5 | = | = | = | = | holds |
| `design.seams` | S6 | = | = | = | = | holds |
| `design.seams` | S7 | = | = | = | = | holds |
| `design.decompose` | S1 | = | = | = | = | B2-F14 |
| `design.decompose` | S2 | = | X's confirmed interfaces | = | = | holds |
| `design.decompose` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.decompose` | S4 | = | = | = | = | not on path: outside any build |
| `design.decompose` | S5 | = | X's interface, now withdrawn | = | no route on the notice | B2-F9 |
| `design.decompose` | S6 | = | = | = | = | holds |
| `design.decompose` | S7 | = | = | = | = | holds |
| `design.research` | S1 | = | = | = | = | holds |
| `design.research` | S2 | = | = | = | = | holds |
| `design.research` | S3 | = | = | = | = | not on path: no decompose in a patch |
| `design.research` | S4 | = | = | = | = | not on path: outside any build |
| `design.research` | S5 | = | = | = | = | holds |
| `design.research` | S6 | = | = | = | round trip draws on the budget | holds |
| `design.research` | S7 | = | = | = | = | holds |
| `design.overlaps` | S1 | = | = | = | no per-value route for `design.overlap` | B2-F3 |
| `design.overlaps` | S2 | = | = | = | X and Y overlap; `refuse` unread | B2-F3 |
| `design.overlaps` | S3 | = | = | = | skipped by the patch input | B2-F20 |
| `design.overlaps` | S4 | = | = | = | = | not on path: outside any build |
| `design.overlaps` | S5 | = | = | = | = | B2-F3 |
| `design.overlaps` | S6 | = | = | = | = | B2-F3 |
| `design.overlaps` | S7 | = | today's build index | = | = | B2-F3 |
| `design.streams` | S1 | = | = | = | = | not on path: opt-in, the brief does not ask |
| `design.streams` | S2 | = | reads as needing itself | = | = | B2-F17 |
| `design.streams` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.streams` | S4 | = | = | = | = | not on path: outside any build |
| `design.streams` | S5 | = | = | = | = | not on path: opt-in, not asked |
| `design.streams` | S6 | = | = | = | = | not on path: opt-in, not asked |
| `design.streams` | S7 | = | = | = | = | not on path: opt-in, not asked |
| `design.unit-spec` | S1 | = | = | = | = | holds |
| `design.unit-spec` | S2 | = | = | = | = | holds |
| `design.unit-spec` | S3 | = | the input's unit | = | = | B2-F16 |
| `design.unit-spec` | S4 | = | = | = | = | not on path: outside any build |
| `design.unit-spec` | S5 | = | = | = | = | holds |
| `design.unit-spec` | S6 | = | = | = | = | holds |
| `design.unit-spec` | S7 | = | = | refused by hygiene while coverage is red | = | B2-F10, B2-F12 |
| `design.recommend` | S1 | = | = | = | = | holds |
| `design.recommend` | S2 | = | = | = | = | holds |
| `design.recommend` | S3 | = | = | = | = | holds |
| `design.recommend` | S4 | = | = | = | = | not on path: outside any build |
| `design.recommend` | S5 | = | = | = | = | holds |
| `design.recommend` | S6 | = | = | = | = | holds |
| `design.recommend` | S7 | = | = | = | = | holds |
| `design.reason` | S1 | = | = | = | raced by `design.ready` | B2-F1 |
| `design.reason` | S2 | = | = | = | = | B2-F1 |
| `design.reason` | S3 | = | = | = | = | B2-F1 |
| `design.reason` | S4 | = | = | = | = | not on path: outside any build |
| `design.reason` | S5 | = | = | = | = | B2-F1 |
| `design.reason` | S6 | = | = | = | = | B2-F1 |
| `design.reason` | S7 | = | = | = | = | B2-F1 |
| `design.ready` | S1 | = | on the frontier before the audit decides | = | = | B2-F1, B2-F3 |
| `design.ready` | S2 | = | = | = | = | B2-F1 |
| `design.ready` | S3 | = | = | = | = | B2-F1 |
| `design.ready` | S4 | = | = | = | = | not on path: outside any build |
| `design.ready` | S5 | = | = | = | = | B2-F1 |
| `design.ready` | S6 | = | = | = | = | B2-F1 |
| `design.ready` | S7 | = | = | no UNCARRIED class | = | B2-F1, B2-F19 |
| `design.exit` | S1 | = | = | = | re-entry re-freezes the budget | B2-F4 |
| `design.exit` | S2 | = | = | = | posts to Y | holds |
| `design.exit` | S3 | = | = | = | freezes onto the originating budget | B2-F4 |
| `design.exit` | S4 | = | = | = | = | not on path: outside any build |
| `design.exit` | S5 | = | = | = | Y proceeds on a withdrawn parent | B2-F9 |
| `design.exit` | S6 | = | = | = | = | B2-F4 |
| `design.exit` | S7 | = | = | coverage join reads ambiguity loosely | = | B2-F11 |
| `build.base` | S1 | = | = | = | = | holds |
| `build.base` | S2 | = | = | = | = | holds |
| `build.base` | S3 | = | = | the patch intake | = | holds |
| `build.base` | S4 | = | = | = | = | not on path: outside any build |
| `build.base` | S5 | = | = | = | = | not on path: X is past it; quiesce starts nothing |
| `build.base` | S6 | = | = | = | = | holds |
| `build.base` | S7 | = | = | = | = | holds |
| `build.unit-lease` | S1 | = | = | = | later units leased by no item | B2-F8 |
| `build.unit-lease` | S2 | = | = | = | cross-node unit, shared worktree | B2-F7, B2-F8 |
| `build.unit-lease` | S3 | = | = | = | = | holds |
| `build.unit-lease` | S4 | = | = | = | = | not on path: outside any build |
| `build.unit-lease` | S5 | = | = | tombstoned by `life.unlease` | = | holds |
| `build.unit-lease` | S6 | = | = | = | refused → as `leases` says | holds |
| `build.unit-lease` | S7 | = | = | = | = | holds |
| `build.unit-pass` | S1 | = | = | = | = | holds |
| `build.unit-pass` | S2 | node x's builder | = | = | no integration under shared | B2-F7 |
| `build.unit-pass` | S3 | = | = | = | = | holds |
| `build.unit-pass` | S4 | = | = | = | = | not on path: outside any build |
| `build.unit-pass` | S5 | = | = | = | in-flight pass finishes, then quiesced | holds |
| `build.unit-pass` | S6 | = | = | = | = | holds |
| `build.unit-pass` | S7 | = | = | = | = | holds |
| `build.acceptance` | S1 | = | = | = | fail → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S2 | = | = | = | = | B2-F6 |
| `build.acceptance` | S3 | = | = | = | red again → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S4 | = | = | = | = | not on path: outside any build |
| `build.acceptance` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.acceptance` | S6 | = | = | = | red unit → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S7 | = | = | = | = | B2-F6 |
| `build.scope` | S1 | = | = | = | = | holds |
| `build.scope` | S2 | = | = | = | = | holds |
| `build.scope` | S3 | = | = | = | = | holds |
| `build.scope` | S4 | command in the adopter's tree | map kit absent | = | = | B2-F13 |
| `build.scope` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.scope` | S6 | = | = | = | = | holds |
| `build.scope` | S7 | = | = | = | = | B2-F13 |
| `build.reuse-check` | S1 | = | = | = | clean → prose target | B2-F2 |
| `build.reuse-check` | S2 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S3 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S4 | = | = | = | = | not on path: outside any build |
| `build.reuse-check` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.reuse-check` | S6 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S7 | = | = | = | = | B2-F2 |
| `build.recommend` | S1 | = | prose need | = | closing review re-owed on each lap | B2-F2, B2-F18 |
| `build.recommend` | S2 | = | = | = | = | B2-F2 |
| `build.recommend` | S3 | = | = | = | = | B2-F2 |
| `build.recommend` | S4 | = | = | = | = | not on path: outside any build |
| `build.recommend` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.recommend` | S6 | = | = | = | review at CEILING across laps | B2-F2, B2-F18 |
| `build.recommend` | S7 | = | = | = | = | B2-F2 |
| `build.ratify` | S1 | = | = | = | = | not on path: `decisions.major` is `author-rubric` by default |
| `build.ratify` | S2 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S3 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S4 | = | = | = | = | not on path: outside any build |
| `build.ratify` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.ratify` | S6 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S7 | = | = | = | = | not on path: default `author-rubric` |
| `build.distill` | S1 | = | on the frontier before the closing review | = | = | B2-F1, B2-F2 |
| `build.distill` | S2 | = | = | = | = | B2-F1 |
| `build.distill` | S3 | = | = | = | = | B2-F1 |
| `build.distill` | S4 | = | = | = | = | not on path: outside any build |
| `build.distill` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.distill` | S6 | = | = | = | = | B2-F1 |
| `build.distill` | S7 | = | = | = | = | B2-F1 |
| `build.core` | S1 | = | = | = | = | B2-F2 |
| `build.core` | S2 | = | = | = | = | B2-F2 |
| `build.core` | S3 | = | = | = | = | B2-F2 |
| `build.core` | S4 | = | = | = | = | not on path: outside any build |
| `build.core` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.core` | S6 | = | = | = | own red → a fix unit or excepted | B2-F2 |
| `build.core` | S7 | = | = | = | = | B2-F2 |
| `build.exit` | S1 | = | = | = | = | B2-F2 |
| `build.exit` | S2 | = | = | = | = | B2-F2 |
| `build.exit` | S3 | = | = | = | = | B2-F2 |
| `build.exit` | S4 | = | = | = | = | not on path: outside any build |
| `build.exit` | S5 | = | = | = | Y reaches it on a withdrawn parent | B2-F9 |
| `build.exit` | S6 | = | = | = | = | B2-F2 |
| `build.exit` | S7 | = | = | = | = | B2-F2 |
| `test.merge` | S1 | = | = | = | = | holds |
| `test.merge` | S2 | = | = | = | = | holds |
| `test.merge` | S3 | = | = | = | = | holds |
| `test.merge` | S4 | = | = | = | = | holds |
| `test.merge` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.merge` | S6 | = | = | = | refused → an ask with no re-entry | B3-F8 |
| `test.merge` | S7 | = | = | = | = | holds |
| `test.select` | S1 | = | = | = | = | holds |
| `test.select` | S2 | = | = | = | = | holds |
| `test.select` | S3 | = | = | = | = | holds |
| `test.select` | S4 | = | = | = | = | holds |
| `test.select` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.select` | S6 | = | = | = | = | holds |
| `test.select` | S7 | = | = | = | = | holds |
| `test.verdict` | S1 | = | = | = | = | holds |
| `test.verdict` | S2 | = | = | remote-ci verdict with no pin or trust clause | = | B3-F6 |
| `test.verdict` | S3 | = | = | = | = | holds |
| `test.verdict` | S4 | = | = | = | = | holds |
| `test.verdict` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.verdict` | S6 | = | = | = | = | holds |
| `test.verdict` | S7 | = | = | = | = | holds |
| `test.route` | S1 | = | = | = | MIXED under own-only routes two ways | B3-F7 |
| `test.route` | S2 | = | = | = | = | holds |
| `test.route` | S3 | = | = | = | = | holds |
| `test.route` | S4 | = | = | = | = | holds |
| `test.route` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.route` | S6 | = | = | = | = | holds |
| `test.route` | S7 | = | = | = | = | holds |
| `test.attribute` | S1 | = | = | = | = | holds |
| `test.attribute` | S2 | = | = | = | = | holds |
| `test.attribute` | S3 | = | = | = | = | holds |
| `test.attribute` | S4 | = | = | = | = | holds |
| `test.attribute` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.attribute` | S6 | = | = | = | = | holds |
| `test.attribute` | S7 | = | = | = | = | holds |
| `test.flakes` | S1 | = | = | = | = | holds |
| `test.flakes` | S2 | = | = | = | = | holds |
| `test.flakes` | S3 | = | = | = | = | holds |
| `test.flakes` | S4 | = | = | = | = | holds |
| `test.flakes` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.flakes` | S6 | = | = | = | = | holds |
| `test.flakes` | S7 | = | = | = | = | holds |
| `test.seen-red` | S1 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S2 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S3 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S4 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.seen-red` | S6 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S7 | = | = | record written by the checker itself | = | B3-F1 |
| `test.recommend` | S1 | = | = | = | = | holds |
| `test.recommend` | S2 | = | = | = | = | holds |
| `test.recommend` | S3 | = | = | = | = | holds |
| `test.recommend` | S4 | = | = | = | = | holds |
| `test.recommend` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.recommend` | S6 | = | = | = | = | holds |
| `test.recommend` | S7 | = | = | = | = | holds |
| `test.reason` | S1 | = | = | = | = | holds |
| `test.reason` | S2 | = | = | = | = | holds |
| `test.reason` | S3 | = | = | = | = | holds |
| `test.reason` | S4 | = | = | = | = | holds |
| `test.reason` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.reason` | S6 | = | = | = | = | holds |
| `test.reason` | S7 | = | = | = | = | holds |
| `test.exit` | S1 | = | = | = | = | holds |
| `test.exit` | S2 | = | = | = | = | holds |
| `test.exit` | S3 | = | = | = | = | holds |
| `test.exit` | S4 | = | = | = | = | holds |
| `test.exit` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.exit` | S6 | = | = | = | = | holds |
| `test.exit` | S7 | = | = | lease record of a non-ancestor build | = | B3-F13 |
| `deploy.current` | S1 | = | = | = | = | holds |
| `deploy.current` | S2 | = | = | = | = | holds |
| `deploy.current` | S3 | = | = | = | = | holds |
| `deploy.current` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.current` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.current` | S6 | = | = | = | = | holds |
| `deploy.current` | S7 | = | = | = | = | holds |
| `deploy.mandate` | S1 | = | = | intake record, or a supervisor-written gate choice | = | B3-F4, B3-F11 |
| `deploy.mandate` | S2 | = | = | = | = | holds |
| `deploy.mandate` | S3 | = | = | rendered Maintain intake as mandate | = | B3-F11 |
| `deploy.mandate` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.mandate` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.mandate` | S6 | = | = | = | = | holds |
| `deploy.mandate` | S7 | = | = | = | = | holds |
| `deploy.parents` | S1 | = | = | = | = | holds |
| `deploy.parents` | S2 | = | = | = | holds with no deadline | B3-F5 |
| `deploy.parents` | S3 | = | = | = | = | holds |
| `deploy.parents` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.parents` | S5 | = | = | = | Y holds past its deadline with no outcome | B3-F5 |
| `deploy.parents` | S6 | = | = | = | = | holds |
| `deploy.parents` | S7 | = | = | = | = | holds |
| `deploy.land` | S1 | = | = | = | = | holds |
| `deploy.land` | S2 | = | landing.order unread | = | = | B3-F10 |
| `deploy.land` | S3 | = | = | = | = | holds |
| `deploy.land` | S4 | = | = | = | = | holds |
| `deploy.land` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.land` | S6 | = | = | = | carried commit or argument → an ask with no re-entry | B3-F8 |
| `deploy.land` | S7 | = | = | = | = | holds |
| `deploy.core` | S1 | = | = | = | = | holds |
| `deploy.core` | S2 | = | = | = | = | holds |
| `deploy.core` | S3 | = | = | = | red → close after filing; patch has no budget link | B3-F2, B3-F3 |
| `deploy.core` | S4 | = | = | = | = | holds |
| `deploy.core` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.core` | S6 | = | = | = | = | holds |
| `deploy.core` | S7 | = | = | = | = | holds |
| `deploy.record` | S1 | = | = | = | = | holds |
| `deploy.record` | S2 | = | = | = | = | holds |
| `deploy.record` | S3 | = | = | = | = | holds |
| `deploy.record` | S4 | = | = | = | = | holds |
| `deploy.record` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.record` | S6 | = | = | = | = | holds |
| `deploy.record` | S7 | = | = | = | = | holds |
| `deploy.distill` | S1 | = | = | = | = | holds |
| `deploy.distill` | S2 | = | = | = | = | holds |
| `deploy.distill` | S3 | = | = | = | patch route carries no originating budget | B3-F3 |
| `deploy.distill` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.distill` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.distill` | S6 | = | = | = | = | holds |
| `deploy.distill` | S7 | = | rows from a non-ancestor build | empty join reads green | = | B3-F12 |
| `deploy.recommend` | S1 | = | = | = | = | holds |
| `deploy.recommend` | S2 | = | = | = | = | holds |
| `deploy.recommend` | S3 | = | = | = | = | holds |
| `deploy.recommend` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.recommend` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.recommend` | S6 | = | = | = | = | holds |
| `deploy.recommend` | S7 | = | = | = | = | holds |
| `deploy.notify` | S1 | = | = | = | = | holds |
| `deploy.notify` | S2 | = | = | = | = | holds |
| `deploy.notify` | S3 | = | = | = | = | holds |
| `deploy.notify` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.notify` | S5 | = | = | = | = | not on path: a withdrawal posts through life.notify |
| `deploy.notify` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.notify` | S7 | = | = | = | = | holds |
| `deploy.released` | S1 | = | = | = | = | holds |
| `deploy.released` | S2 | = | = | = | = | holds |
| `deploy.released` | S3 | = | = | = | = | holds |
| `deploy.released` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.released` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build, before any push |
| `deploy.released` | S6 | = | = | = | = | holds |
| `deploy.released` | S7 | = | = | = | = | holds |
| `deploy.snapshot` | S1 | = | = | = | = | holds |
| `deploy.snapshot` | S2 | = | = | = | = | holds |
| `deploy.snapshot` | S3 | = | = | = | = | holds |
| `deploy.snapshot` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.snapshot` | S5 | = | = | = | = | not on path: a withdrawal snapshots through life.snapshot |
| `deploy.snapshot` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.snapshot` | S7 | = | = | = | = | holds |
| `deploy.unlease` | S1 | = | = | = | = | holds |
| `deploy.unlease` | S2 | = | = | = | = | holds |
| `deploy.unlease` | S3 | = | = | = | = | holds |
| `deploy.unlease` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.unlease` | S5 | = | = | = | = | not on path: a withdrawal releases leases through life.unlease |
| `deploy.unlease` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.unlease` | S7 | = | = | = | = | holds |
| `deploy.close` | S1 | = | = | = | = | holds |
| `deploy.close` | S2 | = | = | = | = | holds |
| `deploy.close` | S3 | = | = | = | closes with its own core red open | B3-F2 |
| `deploy.close` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.close` | S5 | = | = | = | = | not on path: a withdrawal closes through life.close |
| `deploy.close` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.close` | S7 | = | = | = | = | holds |
| `review.trigger` | S1 | = | = | = | = | B4-F13 |
| `review.trigger` | S2 | = | = | = | = | holds |
| `review.trigger` | S3 | = | = | = | = | holds |
| `review.trigger` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.trigger` | S5 | = | = | = | = | not on path: after life.request nothing fires a new breakpoint |
| `review.trigger` | S6 | = | = | = | owner silence on ratification parks into no state | B4-F2 |
| `review.trigger` | S7 | = | = | = | = | holds |
| `review.pin` | S1 | = | = | = | = | holds |
| `review.pin` | S2 | = | = | = | = | holds |
| `review.pin` | S3 | = | = | = | = | holds |
| `review.pin` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.pin` | S5 | = | = | = | = | not on path: no breakpoint fires after withdrawal |
| `review.pin` | S6 | = | = | = | = | holds |
| `review.pin` | S7 | = | record-kind registry not yet landed | = | = | B4-F11 |
| `review.lens` | S1 | = | = | = | = | holds |
| `review.lens` | S2 | = | = | = | = | holds |
| `review.lens` | S3 | = | = | = | = | holds |
| `review.lens` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.lens` | S5 | = | = | = | = | holds |
| `review.lens` | S6 | = | = | = | = | holds |
| `review.lens` | S7 | = | = | = | = | holds |
| `review.refute` | S1 | = | = | = | = | holds |
| `review.refute` | S2 | = | = | = | = | holds |
| `review.refute` | S3 | = | = | = | = | holds |
| `review.refute` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.refute` | S5 | = | = | = | = | holds |
| `review.refute` | S6 | = | = | = | = | holds |
| `review.refute` | S7 | = | = | = | = | holds |
| `review.report` | S1 | = | = | = | = | holds |
| `review.report` | S2 | = | = | = | CAS class-claim race re-disposes | holds |
| `review.report` | S3 | = | = | = | = | holds |
| `review.report` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.report` | S5 | = | = | = | finished fan's findings unrouted | B4-F8 |
| `review.report` | S6 | = | = | = | = | holds |
| `review.report` | S7 | = | CAS refs not yet landed | = | routes to unlanded review.dispose | B4-F11 |
| `review.dispose` | S1 | = | = | = | plan and landing artifacts unrouted | B4-F4 |
| `review.dispose` | S2 | = | = | = | = | holds |
| `review.dispose` | S3 | = | = | = | landing review findings as units | B4-F4 |
| `review.dispose` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.dispose` | S5 | = | = | = | units into a withdrawn build | B4-F8 |
| `review.dispose` | S6 | = | = | = | = | holds |
| `review.dispose` | S7 | = | = | = | = | holds |
| `review.fold` | S1 | = | = | = | = | holds |
| `review.fold` | S2 | = | = | = | = | holds |
| `review.fold` | S3 | = | = | = | budget spent ends in no state | B4-F2 |
| `review.fold` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.fold` | S5 | = | = | = | = | not on path: a withdrawn build folds no spec |
| `review.fold` | S6 | = | = | = | no CEILING route; exhaustion has no state | B4-F2, B4-F3 |
| `review.fold` | S7 | = | = | = | = | holds |
| `review.cost` | S1 | = | = | = | = | holds |
| `review.cost` | S2 | = | = | = | = | holds |
| `review.cost` | S3 | = | = | = | = | holds |
| `review.cost` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.cost` | S5 | = | = | = | = | holds |
| `review.cost` | S6 | = | = | = | = | holds |
| `review.cost` | S7 | = | shapes registry not yet landed | = | = | B4-F12 |
| `probe.trigger` | S1 | = | = | = | = | holds |
| `probe.trigger` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.trigger` | S3 | = | = | = | reproduction never opened | B4-F10 |
| `probe.trigger` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.trigger` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.trigger` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.trigger` | S7 | = | = | = | = | holds |
| `probe.pin` | S1 | = | = | = | = | holds |
| `probe.pin` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.pin` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.pin` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.pin` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.pin` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.pin` | S7 | = | = | = | = | holds |
| `probe.design` | S1 | = | = | = | = | holds |
| `probe.design` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.design` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.design` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.design` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.design` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.design` | S7 | owner item until the tester lands | = | = | = | holds |
| `probe.experiment` | S1 | = | = | = | = | holds |
| `probe.experiment` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.experiment` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.experiment` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.experiment` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.experiment` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.experiment` | S7 | owner item until the experiment shape lands | = | = | = | holds |
| `probe.run` | S1 | = | = | = | = | holds |
| `probe.run` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.run` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.run` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.run` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.run` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.run` | S7 | = | = | = | visual verification unrunnable until its adapter lands | holds |
| `probe.judge` | S1 | command, executor and a verifier role | = | = | = | B4-F9 |
| `probe.judge` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.judge` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.judge` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.judge` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.judge` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.judge` | S7 | = | = | = | = | holds |
| `probe.return` | S1 | = | = | = | = | holds |
| `probe.return` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.return` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.return` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.return` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.return` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.return` | S7 | = | = | written to the build folder until record lands | = | holds |
| `life.request` | S1 | = | = | = | attend writes the override | holds |
| `life.request` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.request` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.request` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.request` | S5 | = | = | command record of no registered kind | = | B4-F15 |
| `life.request` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.request` | S7 | unattended verbs stand in | = | = | = | holds |
| `life.quiesce` | S1 | = | = | = | = | not on path: attend and unattend stop at the record |
| `life.quiesce` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.quiesce` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.quiesce` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.quiesce` | S5 | driver's executor only | = | omits remote holders' acts | pass push read as landing; pause lease undeclared | B4-F5, B4-F7, B4-F8 |
| `life.quiesce` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.quiesce` | S7 | = | = | = | = | holds |
| `life.notify` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.notify` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.notify` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.notify` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.notify` | S5 | = | = | = | Y replans or its wait takes flow.wait-ceiling's default | holds |
| `life.notify` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.notify` | S7 | = | = | = | = | holds |
| `life.snapshot` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.snapshot` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.snapshot` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.snapshot` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.snapshot` | S5 | = | = | = | = | holds |
| `life.snapshot` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.snapshot` | S7 | = | = | = | = | holds |
| `life.unlease` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.unlease` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.unlease` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.unlease` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.unlease` | S5 | = | = | = | queued claim refused on the tombstone | holds |
| `life.unlease` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.unlease` | S7 | = | = | = | = | holds |
| `life.close` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.close` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.close` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.close` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.close` | S5 | = | = | = | kept work never reaches Z's design.inventory | B4-F6 |
| `life.close` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.close` | S7 | = | = | = | = | holds |
| `adopt.census` | S1 | = | = | = | = | not on path: gov is adopted already and S1's kit change registers no check |
| `adopt.census` | S2 | = | = | = | = | not on path: S2 runs builds on adopted nodes, with no adoption or check registration |
| `adopt.census` | S3 | = | = | = | = | not on path: a patch build registers no check and runs no adoption |
| `adopt.census` | S4 | = | = | = | = | not on path: the census and its rulings run once at adoption or at the owner's ask, not at an update |
| `adopt.census` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `adopt.census` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `adopt.census` | S7 | command, gov as its own adopter once dLinkedLibrary lands | = | = | = | holds |
| `test.seed` | S1 | = | = | = | = | not on path: gov is adopted already and S1's kit change registers no check |
| `test.seed` | S2 | = | = | = | = | not on path: S2 runs builds on adopted nodes, with no adoption or check registration |
| `test.seed` | S3 | = | = | = | = | not on path: a patch build registers no check and runs no adoption |
| `test.seed` | S4 | = | a kit update that brings a new check, which kits.update never routes to | = | seeded → armed, with no item handing it the update's new checks | B5-F6 |
| `test.seed` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `test.seed` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `test.seed` | S7 | = | = | = | = | holds |
| `adopt.practices` | S1 | = | = | = | = | not on path: gov is adopted already and S1's kit change registers no check |
| `adopt.practices` | S2 | = | = | = | = | not on path: S2 runs builds on adopted nodes, with no adoption or check registration |
| `adopt.practices` | S3 | = | = | = | = | not on path: a patch build registers no check and runs no adoption |
| `adopt.practices` | S4 | = | = | = | = | not on path: the census and its rulings run once at adoption or at the owner's ask, not at an update |
| `adopt.practices` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `adopt.practices` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `adopt.practices` | S7 | = | = | = | = | holds |
| `adopt.decisions` | S1 | = | = | = | = | not on path: gov is adopted already and S1's kit change registers no check |
| `adopt.decisions` | S2 | = | = | = | = | not on path: S2 runs builds on adopted nodes, with no adoption or check registration |
| `adopt.decisions` | S3 | = | = | = | = | not on path: a patch build registers no check and runs no adoption |
| `adopt.decisions` | S4 | = | = | = | = | not on path: the census and its rulings run once at adoption or at the owner's ask, not at an update |
| `adopt.decisions` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `adopt.decisions` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `adopt.decisions` | S7 | reviewer as two raters, and the owner: two actor kinds | = | = | accepted, or declined by the owner: no route for disagreeing raters or a kappa under 0.8 | B5-F8 |
| `adopt.reconstruct` | S1 | = | the first touch of untouched code by build.unit-pass | none: no item or clause reconstructs on touch | none | B5-F9 |
| `adopt.reconstruct` | S2 | = | = | = | = | not on path: S2 runs builds on adopted nodes, with no adoption or check registration |
| `adopt.reconstruct` | S3 | = | = | = | = | not on path: a patch build registers no check and runs no adoption |
| `adopt.reconstruct` | S4 | = | = | = | = | not on path: retrofit.reconstruct acts at adoption, at the owner's ask or on a build's touch, not at an update |
| `adopt.reconstruct` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `adopt.reconstruct` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `adopt.reconstruct` | S7 | = | build.unit-pass, dScopedBuild's, no ancestor of dLinkedLibrary | none | none under on-touch | B5-F9 |
| `maintain.lease` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.lease` | S2 | = | the period key, derived from each node's own clock | = | = | B5-F12 |
| `maintain.lease` | S3 | executor, on the default-branch-red event run keyed by event and SHA | = | = | = | holds |
| `maintain.lease` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.lease` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.lease` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.lease` | S7 | = | = | = | = | holds |
| `maintain.read` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.read` | S2 | = | = | = | = | holds |
| `maintain.read` | S3 | = | = | = | over pin → direct, patch or file only: maintain.tiers' bands and maintain.on-breach's values have no route | B5-F11 |
| `maintain.read` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.read` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.read` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.read` | S7 | = | = | = | = | holds |
| `maintain.direct` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.direct` | S2 | = | = | = | = | holds |
| `maintain.direct` | S3 | = | = | = | = | not on path: S3's fix changes tracked content, which maintain.patch takes |
| `maintain.direct` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.direct` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.direct` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.direct` | S7 | = | = | = | = | holds |
| `maintain.patch` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.patch` | S2 | = | no entry.claim and no build lease | the intake alone, with no claim ref or lease | Design, with no transition row | B5-F1 |
| `maintain.patch` | S3 | = | no entry.place, entry.claim, dedupe or patch.ratify item | the intake keyed by (reading, offender key), with no period and no originating build | Design directly; a recurrence after the patch lands is a no-op | B5-F1, B5-F2 |
| `maintain.patch` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.patch` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.patch` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.patch` | S7 | = | = | = | = | B5-F1 |
| `maintain.file` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.file` | S2 | = | = | = | = | holds |
| `maintain.file` | S3 | = | = | = | Plan's triage; a Maintain-filed patch has no originating build whose budget it spends | B5-F2 |
| `maintain.file` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.file` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.file` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.file` | S7 | = | release.route's ask key and exit record, dShippedRelease's, no ancestor of dTendedCadence | = | = | B5-F14 |
| `maintain.levels` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.levels` | S2 | = | none declared, and no item routes to it | = | unreached | B5-F3 |
| `maintain.levels` | S3 | = | none declared, and no item routes to it | = | unreached | B5-F3 |
| `maintain.levels` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.levels` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.levels` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.levels` | S7 | = | none declared | = | unreached | B5-F3 |
| `maintain.record` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `maintain.record` | S2 | = | none declared, and no item routes to it | never written, so the period lease is never released | unreached | B5-F3 |
| `maintain.record` | S3 | = | none declared, and no item routes to it | never written under every-period | unreached | B5-F3 |
| `maintain.record` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `maintain.record` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `maintain.record` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `maintain.record` | S7 | = | none declared | = | unreached | B5-F3 |
| `loop.lease` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.lease` | S2 | = | the ISO week, from each node's own clock | = | loop.gather only: the week's lease held by node d leaves node x no route | B5-F4, B5-F12 |
| `loop.lease` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.lease` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.lease` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.lease` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.lease` | S7 | = | = | = | = | holds |
| `loop.gather` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.gather` | S2 | = | = | = | = | holds |
| `loop.gather` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.gather` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.gather` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.gather` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.gather` | S7 | = | = | = | = | holds |
| `loop.price` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.price` | S2 | = | = | = | = | holds |
| `loop.price` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.price` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.price` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.price` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.price` | S7 | = | = | = | = | holds |
| `loop.propose` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.propose` | S2 | = | = | = | = | holds |
| `loop.propose` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.propose` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.propose` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.propose` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.propose` | S7 | = | = | = | = | holds |
| `loop.file` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.file` | S2 | = | = | = | = | holds |
| `loop.file` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.file` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.file` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.file` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.file` | S7 | = | = | = | = | holds |
| `loop.record` | S1 | = | = | = | = | not on path: S1 is one attended build, and no Maintain or Loop Review period runs in it |
| `loop.record` | S2 | = | none declared, and no item routes to it | = | unreached | B5-F3 |
| `loop.record` | S3 | = | = | = | = | not on path: the Loop Review prices the week, outside a patch build's path |
| `loop.record` | S4 | = | = | = | = | not on path: S4 is an adopter's update, and observability's programs are no part of it |
| `loop.record` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `loop.record` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `loop.record` | S7 | = | none declared | = | unreached | B5-F3 |
| `release.pick` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.pick` | S2 | command, on each landing node, where release.environments lists E | = | = | release.approve only: E's promotion lease held by the other node has no route | B5-F4 |
| `release.pick` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.pick` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.pick` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.pick` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.pick` | S7 | = | = | = | = | holds |
| `release.approve` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.approve` | S2 | = where release.environments lists E | = | = | = | holds |
| `release.approve` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.approve` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.approve` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.approve` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.approve` | S7 | = | = | = | = | holds |
| `release.promote` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.promote` | S2 | = where release.environments lists E | = | = | = | holds |
| `release.promote` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.promote` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.promote` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.promote` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.promote` | S7 | = | = | = | = | holds |
| `release.verify` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.verify` | S2 | = where release.environments lists E | = | = | = | holds |
| `release.verify` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.verify` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.verify` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.verify` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.verify` | S7 | = | = | = | = | holds |
| `release.route` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.route` | S2 | = where release.environments lists E | = | = | = | holds |
| `release.route` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.route` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.route` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.route` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.route` | S7 | = | = | = | = | holds |
| `release.record` | S1 | = | = | = | = | not on path: release.environments defaults to none, so no release pass opens |
| `release.record` | S2 | = | = | = | the exit record, with E's promotion lease never released | B5-F4 |
| `release.record` | S3 | = | = | = | = | not on path: release.environments defaults to none, so the patch's landing opens no pass |
| `release.record` | S4 | = | = | = | = | not on path: an adopter's update opens no release pass |
| `release.record` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `release.record` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `release.record` | S7 | = | = | = | = | holds |
| `kits.version` | S1 | = | = | = | = | holds |
| `kits.version` | S2 | = | = | = | = | holds |
| `kits.version` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.version` | S4 | = | = | = | = | not on path: S4 runs in the adopter's tree, where gov's mint and cut do not run |
| `kits.version` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.version` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.version` | S7 | = | = | the announced skip until dShippedRelease lands | = | holds |
| `kits.cut` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.cut` | S2 | command: one cadence instance per landed SHA, on each node, under every-landing | = | the tag gov/v<date>.<n>, numbered from the node's date and the remote's tag list | refused by the remote on a number the other node took → an owner item | B5-F5 |
| `kits.cut` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.cut` | S4 | = | = | = | = | not on path: S4 runs in the adopter's tree, where gov's mint and cut do not run |
| `kits.cut` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.cut` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.cut` | S7 | = | = | = | = | holds |
| `kits.currency` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.currency` | S2 | = | = | gov's source-mode receipt: source, 0 behind | = | holds |
| `kits.currency` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.currency` | S4 | = | = | the currency record over the receipt's release tag, which pins no commit | = | B5-F13 |
| `kits.currency` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.currency` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.currency` | S7 | = | = | = | = | holds |
| `kits.adopters` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.adopters` | S2 | = | = | = | = | holds |
| `kits.adopters` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.adopters` | S4 | = | = | the adopter's own committed receipt, read as written | = | holds |
| `kits.adopters` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.adopters` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.adopters` | S7 | = | = | = | = | holds |
| `kits.offer` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.offer` | S2 | = | = | = | = | not on path: deploy.currency defaults to pull-and-watch, which never offers |
| `kits.offer` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.offer` | S4 | command, where deploy.currency: push-branches offers the update | = | = | pushed → the adopter's lander only, with no outbox order for test.seed or the adopt program | B5-F7, B5-F10 |
| `kits.offer` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.offer` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.offer` | S7 | = | = | = | = | holds |
| `kits.install` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.install` | S2 | = | = | = | = | not on path: S2 installs and updates nothing |
| `kits.install` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.install` | S4 | = | = | = | = | not on path: the adopter is installed already and runs update |
| `kits.install` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.install` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.install` | S7 | the owner, or a command: two actor kinds | = | = | only an adapter with no target | B5-F6 |
| `kits.update` | S1 | = | = | = | = | not on path: S1 lands one build, kits.cadence defaults to weekly, and no install, update, offer or reading runs in it |
| `kits.update` | S2 | = | = | = | = | not on path: S2 installs and updates nothing |
| `kits.update` | S3 | = | = | = | = | not on path: S3's patch moves no kit's shipped bytes and runs no distribution program |
| `kits.update` | S4 | the owner, or a command: two actor kinds in one row | none declared | the receipt the update writes itself, and the wiring verdict | only an adapter with no target: no success, failure, killed-step, test.seed or adopt.declarations route | B5-F6, B5-F13, B5-F15 |
| `kits.update` | S5 | = | = | = | = | not on path: S5 withdraws or supersedes a build before its push, and no cadence, release, adoption or kit program is part of that |
| `kits.update` | S6 | = | = | = | = | not on path: S6 walks one build's core failures from entry.claim to its spent budget, and reaches no expansion program or repository-level item |
| `kits.update` | S7 | the owner, or a command: two actor kinds | = | = | only an adapter with no target | B5-F6 |

## Build verdicts

| Build | Verdict |
|---|---|
| dPlacedRequest | B1-F5, B1-F6, B1-F7, B1-F8, B1-F11, B1-F12 |
| dRankedPlan | B1-F2, B1-F9, B1-F10 |
| dKeptSession | B1-F10 |
| dGroundRules | holds |
| dIndexedDesign | B2-F1, B2-F3, B2-F5, B2-F14, B2-F17, B2-F19, B2-F20 |
| dScopedBuild | B2-F2, B2-F6, B2-F7, B2-F8, B2-F13, B2-F16, B2-F18 |
| dBoundRoles | B2-F15 |
| dFurnishedOrders | holds |
| dTrueNorth | B2-F10, B2-F11, B2-F12 |
| dWitnessedBar | B3-F1, B3-F6, B3-F7, B3-F8, B3-F13 |
| dShippedRelease | B3-F2, B3-F3, B3-F4, B3-F5, B3-F8, B3-F9, B3-F10, B3-F11, B3-F12 |
| dSafePassage | holds |
| dConvergedCharter | holds |
| dFairHearing | B4-F11 |
| dDeclaredLoop | B4-F1, B4-F2, B4-F3, B4-F4, B4-F12 |
| dWellOiledMachine | B4-F5, B4-F6, B4-F7, B4-F8, B4-F13 |
| dCalibratedLens | holds |
| dLinkedLibrary | B5-F8, B5-F9, B5-F15 |
| dTotalRecall | holds |
| dTendedCadence | B5-F1, B5-F2, B5-F3, B5-F11, B5-F12, B5-F14 |
| dMindYourWords | holds |
| dOrderedCharter | holds |

## Principle verdicts

| Principle | Verdict |
|---|---|
| P1 | holds |
| P2 | B3-F1, B3-F4 |
| P3 | B3-F6 |
| P4 | B1-F1, B1-F2 |
| P5 | B4-F5 |
| P6 | B5-F1, B5-F2, B5-F3 |
| P7 | B4-F4 |
| P8 | holds |
| P9 | holds |
| P10 | B1-F10 |
| P11 | holds |
| P12 | holds |
| P13 | holds |
| P14 | holds |
| P15 | holds |
| P16 | B3-F2 |
| P17 | B2-F14 |
| P18 | B2-F15 |
| P19 | B2-F16 |
| P20 | B4-F2 |
| P21 | holds |
| P22 | B1-F4 |
| P23 | B1-F3, B1-F1, B1-F2 |
| P24 | B2-F1, B2-F2, B2-F6 |
| P25 | holds |
| P26 | holds |
| P27 | holds |
| P28 | holds |
| P29 | B4-F1, B4-F14 |
| P30 | holds |
| P31 | B4-F9, B4-F10 |
| P32 | holds |
| P33 | holds |
| P34 | holds |
| P35 | holds |
| P36 | holds |
| P37 | holds |
| P38 | holds |
| P39 | B4-F2, B4-F3, B4-F5 |
| P40 | B1-F7 |
| P41 | B2-F10, B2-F11, B2-F12 |
| P42 | holds |

review-shape kind=spec-audit round=1 intensity=full at=synth raw=84 confirmed=69 refuted=15 unverified=0 blocker=0 high=15 medium=44 low=10 agents=15 out-tokens=678905

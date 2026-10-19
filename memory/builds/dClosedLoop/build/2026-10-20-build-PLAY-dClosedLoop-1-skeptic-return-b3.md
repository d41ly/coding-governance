# Skeptic return: run B, batch 3

**Serves:** research PLAY-dClosedLoop-1

Dispatch 181's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-22-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- B2-F1: confirmed medium (the walker graded it high). At flow-steps [design] `design.ready`, Needs is "`design.recommend`, and the spec audit where it ran". `design.recommend` routes to `design.reason` under the default `scored-signals-and-reasoning`, so a frontier built from Needs alone ([rules]) can start `design.ready` alongside `design.reason`. `test.exit` has the same gap, missing `test.reason`. The high claim does not hold on the defaults. An owed or running review still blocks: [breakpoint] says "blocks as `review.blocks` says", whose default is every-review, and the closing review is a declared breakpoint owed by default. v2 also defaults `review.recommendation` to `advice`, so the closing review is not skipped silently. The race costs something only under `binding`, so this is a defect a spec writer would trip over.
- B2-F17: confirmed low. At flow-steps [design] `design.streams`, Needs reads "`design.overlaps`, where `design.streams` holds for the build". The opening says short tags in the tables are item tags, so the cell names its own item. flow-roles-adoption [11] requires "the needs graph acyclic", so this is a wording fix.
- B1-F5: confirmed medium. At flow-steps [entry] `entry.claim`, the claim commit carries only "the claimant's key, the session and the intake's or the ask's content key". `entry.place` and `entry.claim` never name the originating build. Yet v2's `flow.rework-budget` row and `cl-dClosedLoop-0440` require a patch chain to share one budget. The obligation and its red case exist in dShippedRelease's row, so this is a spec writer's hole, not a scenario that cannot terminate.
- B1-F6: refuted. At flow-steps [entry] `entry.claim`, the replay cannot reopen the withdrawn build. [transitions] says "Each state is derived from witnesses (P22), and the engine refuses any transition the table lacks", and withdrawn is terminal. The refusal then takes [rules]' default route ("recorded, and `next` returns the frontier"). layer-runtime [decide] answers `terminal` for a build whose work is all terminal and closes the run. So the claimed "refuses with no route" is not what the records say.
- B1-F7: refuted. At flow-steps [entry] `entry.claim` and `plan.lease`, the default `leases: warn` is the overlap stance (v2 P5: "overlap warns by default"). Under it an overlap is warned and the lease taken, as `plan.lease`'s "an overlap → noted on the card" shows, so "refused under the default → Design unleased" is never reached. An unreachable remote is `leases.offline`'s case, which is in [entry]'s Policies (`leases.*`) and covers "every compare-and-swap mint alike" (`cl-dClosedLoop-0120`). A ref the remote refuses takes [rules]' default refusal route under P39's SL-7.
- B1-F1: confirmed high. At flow-steps [entry] `entry.intake`, the copy's Actor is "orientation scout" and its witness is "the intake entry the scout writes". That breaks [rules] ("No witness is typed by the acting agent"). It also contradicts the item's own route ("the hook crashed or never fired"), [revised] `hook-actor-kind`, `cl-dClosedLoop-0282`, v2 [contracts] ("Plan's witness is the hook-written intake") and flow-roles-adoption:202. `deploy.mandate` takes "the intake record" as landing authority, so a guard certifies what an agent typed (c3).
- B1-F11: confirmed low. At flow-steps [entry] `entry.orient`, the Does cell hard-codes `no-ready-card` ("where no READY card exists"). `cl-dClosedLoop-0376` says "only where `kickoff.runs` says", and neither [entry]'s nor [plan]'s policy list names `kickoff.runs`.
- B1-F8: refuted. At flow-steps [entry] `entry.place` and `entry.claim`, the routes are outputs, not inputs. "claimed → Plan" and "→ Design" end at transitions in the table dDeclaredLoop declares, an ancestor; the witnesses are "the intake record, the disposition and the claim ref", and none needs dRankedPlan's or dIndexedDesign's items. The `builds.slug-*` keys read at catalogue default through dGroundRules' reader: `cl-dClosedLoop-0014` expects keys whose Owner build has not landed. Today's mint and `check_slug_claimed` exist in `tools/memory-tree/gen_build_index.py:3478`. v2:483 is the night pass's revision note, not a general rule.
- B4-F6: confirmed medium. flow-steps [lifecycle] says kept work passes "through the replacement's `design.inventory`". But `design.input` sends a plan record to `design.seams` and only a "plan revision → `design.inventory`", and `design.inventory` judges completed units "after a plan revision". No input kind carries a superseded build's units into the replacement.
- B4-F5: confirmed medium (the walker graded it high). flow-steps [lifecycle] says "The supervisor renews them while it is paused", but v2's `leases.renewal` default `progress` renews only "on witnessed progress at item boundaries and on declared waits inside their deadline … never on a beat alone". No record declares pause as a wait with a deadline, and `life.quiesce` routes "pause → parked", while `cl-dClosedLoop-0326`'s parking releases the lease. Two records disagree, but no scenario is shown to fail.
- B4-F7: confirmed low (the walker graded it medium). At flow-steps [lifecycle] `life.quiesce`, "Once a push is made, the build has landed" is ambiguous now that `cl-dClosedLoop-0318` pushes every pass commit. The same sentence equates the push with landing, and [transitions] reads "before the push" in Deploy's context, so this is a wording fix.
- B4-F8: confirmed medium. At flow-steps [lifecycle] `life.quiesce`, the witness is "the executor's record of the acts it let finish". A unit holder on another node drives "only that unit's passes on its own branch" (`cl-dClosedLoop-0319`) and is never told; only the fence after `life.unlease` stops it. Once quiesce "dispatches nothing new", no route sends a finished review fan's findings to `review.dispose` or to asks.
- B1-F9: confirmed medium. At flow-steps [plan] `plan.dedupe`, the check runs "against live builds, the design index and open asks", and the design index is `cl-dClosedLoop-0384` (dIndexedDesign). dRankedPlan's parents are dDeclaredLoop, dTotalRecall and dBoundRoles, and its row's only stand-in is `cl-dClosedLoop-0378`, which covers intake. The `run.host` half is weaker, since the key can read its catalogue default, but the index half holds.
- B1-F2: confirmed high. At flow-steps [plan] `plan.exit`, the cell reads "the owner's go, as the planner records it, stands as the ratification". That contradicts v2 [contracts] ("Plan's witness is the hook-written intake"), `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378` and `cl-dClosedLoop-0137` ("never consent"). Under the default `request`, a role's record certifies the ratification (c3).
- B4-F9: confirmed medium. At flow-steps [probe] `probe.judge`, the Actor is "command: the executor's re-run, or the experiment's scorer", but [rules] lists the executor and a command as separate kinds. The witness adds "the verifier's judgment" (a role), and [probe] Roles adds "a blind judge". That breaks "One actor per item, of one kind".
- B4-F10: confirmed medium. At flow-steps [probe] `probe.trigger`, the closed trigger set has no arm for `cl-dClosedLoop-0408`'s reproduction before a patch fix. `probe.points` defaults to `none` (v2), and `design.input` sends a patch straight to `design.unit-spec`.
- B3-F3: confirmed medium (the walker graded it high). It is the same defect as B1-F5. The bullet in flow-steps [rules] ("Every route back is bounded") omits the patch-build draw that v2's `flow.rework-budget` row and stall-and-loop's list name, and `entry.claim` records no originating build. `cl-dClosedLoop-0440` still obliges dShippedRelease with a planted patch-chain red, so this is a spec writer's hole.
- B3-F13: confirmed medium. flow-steps [test] `test.exit` writes "the verified tree on the build's lease record". The lease kind's owner is dPlacedRequest (layer-memory; design map `record-kind.lease`). dWitnessedBar's only parent is dDeclaredLoop, and its v2 row declares no stand-in.
- B3-F8: refuted. At flow-steps [test] `test.merge` and [deploy] `deploy.land`, the build is not left idle. A refused `test.merge` has no witness (its witness is the prepared merge's SHA), so by [rules] it stays on the frontier and each re-dispatch draws on `flow.rework-budget`. If the frontier is empty while the build is open, layer-runtime [decide] answers `stuck`, which "raises an owner item at once".

**Clean cells**

- `plan.record` S1: holds.
- `kits.currency` S7: holds. Every key it reads (`kits.*`, `currency.*`, `install.from`) is dShippedRelease's own. The source-mode receipt it reads comes from `cl-dClosedLoop-0025` in dSafePassage, an ancestor.
- `deploy.record` S6: holds. In S6 the unreachable remote and the landing conflict meet `deploy.land`'s declared classes before `deploy.record`, which is reached only through `deploy.core`'s green.
- `plan.record` S6: holds.
- `design.recommend` S2: holds.
- `design.seams` S5: holds. The S5 gap sits at `design.input`/`design.inventory` (B4-F6), not in this item.
- `loop.file` S2: defect, BS3-F2 below.
- `entry.orient` S6: holds. The only Entry failure S6 injects is the refused lease at `entry.claim`.

Attached to `plan.record` (S1, then S6):

### BS3-F1 — An owner's late answer to a Plan question has no route; best effort has already decided it
- **Address:** flow-steps [plan] `plan.record`; [breakpoint] (the owner gate); [transitions]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** `plan.record` routes "an owner question → an owner item, resolved as [breakpoint]'s owner gate is (FH1)". [breakpoint] says `run.on-owner-question` "resolves it when it is raised", and its default is `best-effort-recorded` (v2). [breakpoint] also says attendance "asks owner questions live". The amendment row in [transitions] covers only "building, testing, or deploying before the push", and `entry.place`'s `continue` goes to "that build's `next`".
- **Consequence:** In S1 the plan is drafted on the supervisor's recorded choice. The owner's later answer has no item that takes it in during planning, so the live question changes nothing.
- **Fix:** Under attendance, hold an owner question until `run.owner-deadline` before best effort decides. Route an answer that arrives after the choice back to `plan.record` as a re-entry, and add a planning row to the amendment transition.

### BS3-F3 — A spent budget has no transition row, so a build that spends it in Plan cannot end
- **Address:** flow-steps [transitions]; [rules] (the "Every route back is bounded" bullet); seen at [plan] `plan.record`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:** `cl-dClosedLoop-0116`'s endings are to land what is green, descope units, or "close the build incomplete", plus `park-for-owner`. [transitions] has no row for any of them, its terminal set ("Landed, withdrawn, superseded, deferred, retired, refused, merged and answered") has no incomplete or parked state, and "the engine refuses any transition the table lacks". In Plan the budget is "the base alone" and is spent by `plan.research` round trips and re-dispatches.
- **Consequence:** S6's injected spent budget leaves a planning build with no ending it can take: nothing to land, no units to descope, and the close refused.
- **Fix:** Add exhausted rows from every open state, to a terminal `closed-incomplete` and to `parked`, each witnessed by the ending record. Add both states to the terminal and disposition sets, and plant a budget spent in planning.

Attached to `design.recommend` S2:

### BS3-F4 — `design.recommend` does not declare whether it is idempotent or reconciles
- **Address:** flow-steps [design] `design.recommend`; [rules] (the command-item bullet)
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Evidence:** [rules] says "Every command item declares whether it is idempotent or reconciles". The item's Actor cell says only "command", while siblings like `build.distill` say "command, idempotent". Most other command items in the tables have the same gap.
- **Consequence:** When node d's session limit hands the build over in S2, nothing tells the successor whether to re-score or to reconcile with the recommendation record already written.
- **Fix:** Declare it on every command item, and add a check that reds a command Actor cell with neither word.

Attached to `loop.file` S2:

### BS3-F2 — `loop.file` files asks with no acceptance, which the default refuses
- **Address:** layer-expansions [design-observability] `loop.file`; layer-memory [asks]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** [asks]: "Every other filer, whether the owner, a surfaced idea, an expansion or the supervisor on a role's behalf, states an `accept` line … Filing without either is refused". `asks.acceptance` defaults to `refuse` (v2). `maintain.file` states "back under its pin", but `loop.file`'s Does cell states no acceptance.
- **Consequence:** Each proposal's filing is refused, and "routes as any refusal does: `next` returns its frontier". A cadence run has no build budget, so the Loop Review re-files every beat and never reaches the owner's breakpoint.
- **Fix:** State `loop.file`'s acceptance (the owner's `review.loop.retire` breakpoint disposing the row, or a keep record), and plant an ask that is refused without it.

- **Read outside the list above:** I listed the folder names under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/` (to find my own scratch folder; I opened nothing in the other folders). I listed the top two levels of the sealed copy's root, which shows file names only. I ran no gate and wrote nothing to the repository; my one helper, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b3/cl.py`, sits in my scratch folder.

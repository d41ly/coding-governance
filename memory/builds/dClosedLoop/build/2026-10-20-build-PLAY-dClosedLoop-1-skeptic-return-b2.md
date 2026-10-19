# Skeptic return: run B, batch 2

**Serves:** research PLAY-dClosedLoop-1

Dispatch 180's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-21-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- B4-F4: confirmed medium
  `flow-steps [breakpoint] review.dispose` only handles "an unbuilt spec" and "built work". `review.pin` can also pin a plan revision (`plan.recommend` routes to "the Plan breakpoint"), and that pin has no arm. A landing review's findings "become new units", which contradicts `[deploy]` Breakpoints ("patch builds by the entry-point table's post-close row"). `[transitions]` has no row for deploying → designing after the push.

- B4-F3: confirmed medium (rubric grades it lower than the walker's high)
  `review.fold` and `review.dispose` have no CEILING or NON-CONVERGENT outcome. The `[breakpoint]` policy list (line 502) leaves out `review.max-rounds` and `flow.rework-budget`. `[rules]` (lines 41-42) sends open work only to asks, where `cl-dClosedLoop-0117` sends it to units while budget remains. The loop still ends, though: rounds count against `flow.route-backs` (`[design]` line 213), and past that limit `[rules]` ends the item's loop non-converging. So a terminal is reachable without B4-F2, and c2 does not hold.

- B4-F11: confirmed medium
  `review.pin`, owned by dFairHearing, picks `design-audit` "by the record-kind registry". The design map gives that registry to dTotalRecall (`record-kind.registry · owner=dTotalRecall`), which comes after dFairHearing (dFairHearing after dSafePassage; dTotalRecall after dDeclaredLoop and dPlacedRequest). `review.report` routes to `review.dispose`, which is dDeclaredLoop's and not an ancestor. `[stage0-classes]` is empty, and `[breakpoint]` declares no stand-ins the way `[probe]` does. The slug-claim leg is weaker: compare-and-swap ref claims already exist today (unattended's `refs/gov/runs`). No chain clause builds `refs/gov/class-claims` at all.

- B2-F6: confirmed medium
  "a fix pass" (`build.acceptance`, `test.attribute`, `test.seen-red`) and "a revert pass" (`build.scope`) are route targets but not items. M16's narrowed allowance in `[test]` ("A fix pass keeps its check") needs an item-level allowance. `build.unit-pass` declares only the ordinary one.

- B2-F18: confirmed medium
  `build.recommend` routes to "the closing review where owed", and `review.build` defaults to owed, so every lap back from Design fires a fresh closing review. flow-roles FR-9 asked exactly this question ("Does the closing review run again over them by default?"). The owner answered "Only after a HIGH finding", which `review.follow-up` carries. The item ignores that answer.

- B2-F2: confirmed high
  `build.reuse-check`'s clean outcome routes to "the unit built", which is a state, not an item. `build.recommend`'s Needs, "every unit built and reuse-checked", names no tag, unlike `design.recommend`'s "every unit's `design.unit-spec`". No Then cell routes to `build.recommend`. So, read literally as the audit reads the draft, `build.recommend` through `build.exit` are unreachable.

- B2-F8: confirmed medium
  `build.unit-lease` "takes each starting unit's lease" and has one need, `build.base`. `build.scope` routes in-scope work to "the unit's next pass" or `build.reuse-check`, never to a lease. Meanwhile v2's pick (`cl-dClosedLoop-0331`) offers "ready unleased units" to other nodes.

- B3-F10: confirmed medium
  `landing.order` appears only in `[deploy]` prose ("ordered by `landing.order`") and in Deploy's policy list. No item's Does cell reads it, and `cl-dClosedLoop-0422` says only "landings ordered through the landing queue it builds (`gap-flow-08`)". The strict preset sets `owner-orders` (v2 presets table).

- B3-F2: confirmed high
  `deploy.core`'s red route is "the close waits for its filing". The owner-confirmed K1 reading in foundations `[core]` is that the build "cannot reach its exit until the red is fixed or excepted". v2's revision says a landing-merge core red "still stops that build from closing", and `cl-dClosedLoop-0423` says the same. Filing a patch build is not fixing or excepting the red.

- B3-F12: confirmed medium
  The map gives dShippedRelease the parents dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary and dFurnishedOrders. Neither dScopedBuild (`build.distill`) nor dIndexedDesign (fork classes) is among its ancestors. v2 has no rule that an empty join is anything but green; its only "non-empty populations" clause is the tag join's.

- B3-F11: confirmed medium
  `deploy.mandate`'s witness under `plan-only` is "the intake record". v2's 2026-10-14 revision says "the owner's plan ratification is the mandate", and `plan.ratification` has non-`request` values (terminal-command, hook-keyword, signed-commit), under which ratification is the owner's disposition at `plan.exit`. A triage-selected build has no intake record. `gap-flow-14` names Maintain's agent-typed intake becoming a patch build's mandate as a defect.

- B3-F4: refuted
  Resolving an owner breakpoint by `run.on-owner-question`, including the supervisor's recorded choice under `best-effort-recorded`, is the owner's own LR-3 answer. research-final-coverage row 1 records that reversing it ("an owner breakpoint parks the build") was itself a defect caught earlier. LR-3 carves out only ratifications, and the landing gate is an authorization, not a ratification. No preset pairs `three-gates` with `best-effort-recorded`: strict pairs `every-stage` with `park-item`.

- B3-F9: confirmed medium
  `deploy.notify`, `deploy.snapshot`, `deploy.unlease` and `deploy.close` all write to the remote. Unlike `deploy.land`, none declares an unreachable outcome, so a failed act falls to `[rules]`' default refusal route, which draws on the budget. The claimed consequence is overstated, though: layer-runtime's `stale-remote` answer "holds and retries" while refs cannot be read, with no budget draw. So an outage costs at most one draw per failed act, not a loop.

- B3-F5: confirmed medium (rubric grades it lower than the walker's high)
  `deploy.parents` "holds" with no deadline or outcome, and Deploy's policy list leaves out `flow.wait-ceiling`. So the draft fails `cl-dClosedLoop-0118` as declared. But Y does not wait forever: v2's `flow.wait-ceiling` row names "a dependency hold ... past which the waiter takes its declared outcome". stall-and-loop item 6 gives dependency waits the default "replan" past their deadline. A terminal exists, so c2 does not hold.

- B2-F9: confirmed medium
  `deps.on-parent-withdrawn` is read only at `deploy.parents`, and neither Design's nor Build's policy list names it. layer-flow F-E says dependents "act as `deps.on-parent-withdrawn` says", yet no item routes a read notice. Coordination only refuses transitions until the message is acknowledged, and an acknowledgement triggers no replan. `cl-dClosedLoop-0328` releases dependents only from a wait.

- B2-F20: confirmed medium
  `design.input` routes "patch → `design.unit-spec`", and `design.unit-spec`'s Needs allow "the input's unit". A patch never reaches Plan, so it skips both `plan.dedupe` and `design.overlaps`. Strict's `design.overlap: refuse` is never applied to a patch's write set.

- B2-F5: confirmed high
  `[lifecycle]` says kept work passes "through the replacement's `design.inventory`". `design.input` sends a plan record to `design.seams`, and only a "plan revision" reaches `design.inventory`, which works over the build's own completed units. No input kind or route carries a superseding build's ancestor's units. c4 is overstated: X's commits and records are left uncarried, not overwritten.

- B2-F3: confirmed high
  `design.overlaps` routes to `design.streams` or `design.unit-spec` with no per-value arm. `design.ready` reads only "derived READY: none MISSING, THIN or FORKED". The strict preset sets `design.overlap: refuse` and `design.handoff: ready-plus-audit`. `cl-dClosedLoop-0383` and `cl-dClosedLoop-0384` name neither key.

- B2-F19: confirmed low
  `design.ready`'s witness is "none MISSING, THIN or FORKED". The same owner's `cl-dClosedLoop-0398` adds "`design.ready` gaining an UNCARRIED class".

- `deploy.land` S7: holds
  Today's `tools/push-main.sh` has `--land`, `--prepare` and `GOV_PUSH_MAIN_MAX_RETRIES`, plus a `race` class. `.githooks/pre-push` writes `pre-push-allow`. Every route target (Test, ask, owner item, supervisor) belongs to an ancestor of dShippedRelease.

- `life.request` S7: holds
  The guarded command is dDeclaredLoop's, `attendance` is dKeptSession's and `entry.claim` is dPlacedRequest's, all ancestors of dWellOiledMachine. `attendance.scope` is its own.

- `plan.input` S7: defect, BS2-F1

  ### BS2-F1 — `plan.input` pins an intake record that no ancestor of dRankedPlan writes
  - **Address:** flow-steps [plan] `plan.input`; architecture-v2 [chain] `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378`
  - **Class:** K7
  - **Severity:** medium
  - **Scenario:** S7
  - **Evidence:** `plan.input` "pins the intake record". `cl-dClosedLoop-0377` says the intake log is the one "which `entry.intake`'s prompt-submit hook writes (dWellOiledMachine's, PM-9)". The map gives dRankedPlan the parents dDeclaredLoop, dTotalRecall and dBoundRoles, with no dWellOiledMachine. `cl-dClosedLoop-0378`'s stand-in ("intake not installed") covers only `plan.exit`'s ratification. No prompt-submit hook exists under today's `tools/`, `skills/` or `.githooks/` (searched for UserPromptSubmit and prompt-submit).
  - **Consequence:** When dRankedPlan lands, a build started from an owner prompt has nothing for `plan.input` to pin. `plan.record` then drafts from owner's words that nothing witnesses.
  - **Fix:** Give `plan.input` the same stand-in as `cl-dClosedLoop-0378`: pin `entry.orient`'s "intake absent" record, with the owner's words taken as the owner gate's disposition, until dWellOiledMachine lands.

- `review.refute` S5: holds
  `life.quiesce` lets "an open review fan" finish as one harness act before `life.notify`, and workspaces are reclaimed only at `life.unlease`, after it.

- `release.approve` S7: defect, BS2-F2

  ### BS2-F2 — `release.approve` has two actors of two kinds, chosen by a policy value
  - **Address:** layer-expansions [design-integrations] `release.approve`
  - **Class:** K1
  - **Severity:** medium
  - **Scenario:** S7
  - **Evidence:** The Actor cell reads "the owner, or a command", chosen by `deploy.promotion`. flow-steps `[rules]`: "One actor per item, of one kind ... an item whose actor a policy value chooses is one item per value."
  - **Consequence:** When dShippedRelease builds the release program, dDeclaredLoop's item factory (one actor kind per item) cannot declare this item as written. Guarded's `owner-approves-prod` and auto-on-green share one tag and one outcome table.
  - **Fix:** Split it into `release.approve-owner` (owner, under `owner-approves-*`) and `release.approve-auto` (command, under `auto-on-green`), routed from `release.pick` by `deploy.promotion`'s value.

- `test.reason` S4: holds
  Routes gate reachability (`[rules]`: "An item a route skipped is not owed"), so `test.exit` is reached only through `test.reason`'s route or, under `signals-only`, `test.recommend`'s. The tester stand-in before dBoundRoles is declared in WK-1.

- `life.close` S7: holds
  The transition record and terminal states are dDeclaredLoop's, and the replacement's slug claim is dPlacedRequest's, both ancestors of dWellOiledMachine.

- `deploy.mandate` S2: holds
  Nothing in S2 adds a defect beyond B3-F11's mandate witness. The defect in the brief is that B2-F2's and B4-F11's evidence cite `stage0-leads.md`, which the read list excludes, so those legs could only be re-derived from the copy's tables, never checked against the leads themselves.

- **Read outside the list above:** none. Two `grep -l` sweeps over the copy's `build/` folder listed `*-compared.md`, `*-instruments.md` and session-log file names, but showed none of their contents. The only file I wrote is `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b2/cl.py`, a probe that extracts clause text.

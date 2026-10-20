# Fold brief: writer 4

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the whole-design audit's findings at the 54 places below into dClosedLoop's design
records, as one fold script.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is the working tree's design records** under `memory/builds/dClosedLoop/build/`, at commit `8222099f8a619eef461fe91e84bd9f74173be730`.
  The findings were made on a sealed copy into which twelve past defects were planted. The copy is not your subject;
  read nothing in it. The plants are listed in the round record's `[recall-scored]`
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`). A finding that describes a plant points at a defect
  the working tree never had.
- **Your records:** flow-steps (`2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`). Edit nothing else. When a place needs an edit in another record, list it under
  *Requests* in your return, with the exact change, and leave it out of your script.
- **Read freely** in the working tree: every design record, the gap register, the design map, `tools/`, `skills/` and
  `.githooks/`. Write only in your scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w4/`. Nothing goes into the repository.

## How you fold

1. **For each place,** read its findings below, then read the place in the working tree. Give it exactly one
   disposition:
   - `fold`: the defect is in the working tree, and the fix follows from what the design already settles. Write it.
   - `fork`: the fix chooses between real options, or changes what the design means. Write no fold. Name the
     question, the options and your recommendation, for the owner.
   - `plant`: the finding describes one of the twelve plants, absent from the working tree. Cite the plant.
   - `not a defect`: the working tree already answers it. Quote where.
   - `duplicate`: another place carries the same defect. Name it, and fold it there.
2. **Write the folds as one Python script,** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w4/fold-4.py`, using the build's fold library:

```python
import pathlib, sys
sys.path.insert(0, "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/expansions")
from fold_lib import Record
R = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
R.sub("<exact old text, matching once>", "<new text>", "<place # and finding ids>")
R.insert_before("<exact anchor text, matching once>", "<text>", "<place # and finding ids>")
R.save()
```

   `sub` refuses unless its old text matches exactly once, so quote enough to be unique. Keep each record's own
   conventions: a clause keeps its `cl-dClosedLoop-NNNN` id and its build row, a new clause takes the next free id after
   the highest in `[clause-ids]` (never a renumber), and a record that logs revisions gets a line saying "Revised
   2026-10-20 by the whole-design audit's fold" with the finding ids. Write prose in the records' own register: short
   declarative sentences, no new terms where a defined one exists.
3. **Fold the smallest change that closes each defect,** as its finding's *Fix* and its skeptic's reading say. Where
   the skeptic narrowed a finding, fold the narrowed one.

## What you return

Your final message, nothing else:
1. **Dispositions,** one row per place: `| # | place | disposition | findings | evidence or the fold's one-line gist |`.
2. **Fold script:** its path, and how many edits it makes in which records.
3. **Forks,** each: `### FK-4-<k> — <question>`, then the options, your recommendation and the findings it rests on.
4. **Requests,** each naming the record, the exact change and the place it serves, or `none`.
5. **Read outside the list above:** `none`, or what and why.

Write nothing to the repository. Your effort is the one your role definition sets.

## The places

### Place 15: flow-steps · [transitions] · worst high · critical

#### A5-F1 — `[transitions]` has no state for a parked build, and no terminal for an incomplete ending
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **What is wrong:** The table (flow-steps:623-650) has no parked state and no incomplete terminal, and flow-steps:621 says the engine refuses any transition the table lacks. Endings declared elsewhere have nowhere to go: `run.on-owner-silence` parks a build with its lease released and the item open (v2:1103), `flow.on-exhausted` offers `park-for-owner` and `close-incomplete` (v2:1135), and `cl-dClosedLoop-0116` closes a build incomplete. [lifecycle] says a paused build keeps its leases, so `paused` cannot stand in for a parked build.
- **Consequence:** S6's owner silence on the ratification and a spent budget under any `flow.on-exhausted` value each need a transition the engine refuses. dDeclaredLoop's termination check (`cl-dClosedLoop-0118`, "every state reaching a terminal") cannot be specced against the table.
- **Fix:** Add a `parked` state with rows for owner silence past `run.owner-deadline` and for `park-for-owner`, witnessed by the park record and left by the owner's disposition, which re-takes the lease. Add a terminal `closed-incomplete` reached by `flow.on-exhausted`. Give a descoped unit a row back from building or testing.
- **Skeptic:** Confirmed high, c2 (batch 4). One detail is overstated: layer-runtime:335's `stale-remote` parks the item, not the build.

#### B4-F2 — Budget-exhaustion and park endings have no transition row and no terminal state
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Defect:** [transitions] has no row for `flow.on-exhausted`'s endings (close incomplete, park-for-owner; `cl-dClosedLoop-0116`) or for parking on silence (`cl-dClosedLoop-0326`). It has no terminal or held state for them, and its only hold, `paused`, keeps its leases. `life.quiesce` routes "pause → parked", a state the table lacks. The engine refuses any transition the table lacks.
- **Consequence:** A spent budget in S6, or the default `run.on-owner-silence: apply-recommendation` on an unanswered ratification, leads to a transition the engine refuses, so the build reaches no terminal, against P20 and P39. A build that spends its budget in Plan has nothing to land and no units to descope, and its close is refused (BS3-F3).
- **Fix:** Add a terminal `closed-incomplete` and a `parked` state (lease released, item open, resumed by the owner's disposition). Add rows from every open state on exhaustion and on a park, each with its witness. Add both states to the terminal and disposition sets, and plant a budget spent in planning.
- **Skeptic:** Confirmed high (c2). One detail of the evidence is off: the `incomplete` grep does print lines, but only unrelated ones.
- **Same as:** BS3-F3

### Place 16: flow-steps · build.recommend · worst high · critical

#### AS1-F1 — `build.recommend`'s need and `build.reuse-check`'s route are prose that the position engine cannot join
- **Address:** flow-steps [build] `build.recommend`
- **Same as:** A1-F8
- **Skeptic:** Raised by skeptic batch 1 at medium while checking the `build.recommend` S2 cell, which walker 2 graded holds. No other skeptic judged it.

#### B2-F2 — Build's tail after `build.reuse-check` is reached from no entry
- **Address:** flow-steps [build] `build.recommend` (and `build.reuse-check`'s Then cell)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Defect:** `build.reuse-check`'s clean outcome routes to "the unit built", which is a state, not an item. `build.recommend`'s Needs, "every unit built and reuse-checked", name no tag. No Then cell routes to `build.recommend`.
- **Consequence:** The engine computes position from item tags, so `build.recommend`, `build.ratify`, `build.distill`, `build.core` and `build.exit` never reach the frontier. S1 cannot reach `build.exit`, Test or `deploy.close`.
- **Fix:** Route the clean outcome to `build.recommend`. Write its Needs as "`build.reuse-check` for every unit in the roster", a quantified tag the join resolves. Re-run Stage 0's K2 until the five leads clear.
- **Skeptic:** Confirmed high. Unlike `design.recommend`'s Needs, which name `design.unit-spec`, these name no tag.

#### B2-F18 — A re-entered Build lap owes a full closing review outside `review.follow-up`
- **Address:** flow-steps [build] `build.recommend`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Defect:** `build.recommend` routes to "the closing review where owed", and Build's review is owed by default. Every lap back through Design therefore owes a fresh closing review. The owner's answer to FR-9 was a follow-up only after a HIGH finding, which `review.follow-up` carries.
- **Consequence:** Every lap runs a new full closing review whatever `review.follow-up` says. CEILING and NON-CONVERGENT are counted across unrelated reviews.
- **Fix:** On a lap whose units came from a closing review's findings, route `build.recommend` to that review's follow-up as `review.follow-up` says, never to a fresh owed review.
- **Skeptic:** Confirmed medium. The item ignores the owner's FR-9 answer.

### Place 17: flow-steps · cl-dClosedLoop-0100 · worst high · critical

#### A3-F10 — `deps.on-parent-withdrawn` has no per-value semantics, routes or transition rows, and is read only at Deploy
- **Address:** flow-steps [deploy] `deploy.parents`; flow-steps [transitions]; architecture-v2 [chain] `cl-dClosedLoop-0100`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **What is wrong:** `deploy.parents` routes a withdrawn parent "as `deps.on-parent-withdrawn` says". layer-flow:311-312 only names the values (`replan` by default, `adopt-parent-work` and `withdraw-too` allowed), and `cl-dClosedLoop-0100` builds the key with no arm per value. [transitions] has no row from deploying, building or designing to planning. No item consumes `life.notify`'s `withdrawn` post before Deploy.
- **Consequence:** Y, waiting on X's interface in Design or Build, never reacts to X's withdrawal. At Deploy the default `replan` has no transition, so the engine refuses it and Y is stuck.
- **Fix:** Define each value's route: `replan` as a plan revision with designing, building and deploying → planning rows; `adopt-parent-work` as `design.inventory` over X's kept branch; `withdraw-too` as `life.request` with a command actor. Add a boundary item that consumes `withdrawn` and `superseded` posts, and arm each value on a planted case.
- **Skeptic:** Confirmed high (batch 2). The values are only named, the clause has no arm per value, and the engine refuses the missing transition.

### Place 18: flow-steps · cl-dClosedLoop-0207 · worst high · critical

#### A1-F4 — Attended confirmations and live questions are resolved when raised, with no declared wait, and a late owner answer has no route
- **Address:** flow-steps [breakpoint]; architecture-v2 [chain] dFurnishedOrders `cl-dClosedLoop-0207`; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **What is wrong:** [breakpoint] says `run.on-owner-question` "resolves it when it is raised, never for a ratification", by the supervisor's recorded choice under the default `best-effort-recorded`, and the catalogue row agrees. `attendance: confirm-steps` "adds a gate at every step's exit" and asks owner questions live. `cl-dClosedLoop-0207` says "best effort recorded once the wait passes" but names no key for that wait, while P39 and `cl-dClosedLoop-0118` require every wait to declare a deadline and an outcome. No record routes an owner answer that arrives late.
- **Consequence:** Under the default, every confirm-steps gate (`plan.exit` beyond the ratification, `design.exit`, `build.exit`, `test.exit`) and `plan.record`'s owner question are decided by the supervisor at once. The attended owner confirms nothing. A late answer meets an item already witnessed and has nowhere to go. The guard attendance promises silently loosens.
- **Fix:** State one reading in [breakpoint], `cl-dClosedLoop-0207` and `run.on-owner-question`. Either an attended gate or question is held until a declared deadline (`flow.wait-ceiling` or a new key) and the key applies only after it, or attendance's gates are declared outside `run.on-owner-question`. Route an answer that arrives after a recorded choice, as a re-entry that draws on `flow.rework-budget` or as recorded with no effect. Plant an attended gate that must not resolve at raise.
- **Skeptic:** Confirmed high, c3 (batch 2). The confirm-steps gates are owner items, the catalogue row decides an owner item at raise, and `cl-dClosedLoop-0207`'s wait names no key.

### Place 19: flow-steps · cl-dClosedLoop-0423 · worst high · critical

#### B3-F2 — A core red at landing lets the build close once a patch is filed
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0423`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Defect:** `deploy.core` routes a red to a patch build, "and the close waits for its filing". foundations [core] (the owner-confirmed K1 reading), v2's revision, `cl-dClosedLoop-0423` and P16 all say such a red stops the build from closing until it is fixed or excepted.
- **Consequence:** In S3 the originating build reaches `deploy.close` and `landed` as soon as the patch is filed, before the red is fixed. The violator-pays guard loosens at the item that implements it.
- **Fix:** Hold `deploy.close` until the patch build's `deploy.core` is green for a SHA that contains the landed one, or an owner exception under `core.exceptions`. Add the matching transitions row.
- **Skeptic:** Confirmed high. Filing a patch build is neither fixing nor excepting the red.

### Place 20: flow-steps · deploy.core · worst high · critical

#### A3-F1 — A post-merge red leaves the originating build with no path to `landed`
- **Address:** flow-steps [deploy] `deploy.core`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **What is wrong:** `deploy.core`'s Then reads "red → a patch build through the entry-point table's post-close row, and the close waits for its filing", with no route on to `deploy.record`. `deploy.close` needs only `deploy.unlease` and `deploy.released`, so no witness of the filing exists to wait on. [transitions] has no deploying row for a post-merge red.
- **Consequence:** The originating build never records its landing, never unleases and never closes, and its lease stays held until it expires. layer-runtime [decide] answers `stuck` and raises an owner item, but no declared route takes the build to `landed`.
- **Fix:** Route red to `deploy.record` with the landing recorded red. Name the patch intake's key in the landing record, and add that key's witness to `deploy.close`'s Needs.
- **Skeptic:** Confirmed high, c2 (batch 2). Reading Needs alone cannot rescue it: by the same reading, `test.seen-red` would follow a red `test.verdict`.

### Place 21: flow-steps · deploy.mandate · worst high · critical · includes an unverified finding

#### AS4-F1 — `deploy.mandate` takes a patch build's intake as its landing authority, so an owner-ratified patch lands unratified
- **Address:** flow-steps [deploy] `deploy.mandate`
- **Class:** K10, c3
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** Under the default `plan-only` (v2:1021), the item checks "the request's mandate", proven by "the intake record". A Maintain patch's intake is written by `maintain.patch`, not by the owner, and no item reads `patch.ratify` (A3-F3).
- **Consequence:** With `patch.ratify: owner` set as an override over `standard`, the check passes on the intake alone, and the patch lands without the owner's ratification. The preset combinations are safe, because strict sets `every-stage`.
- **Fix:** For a patch or repeat build, make the plan-only arm's witness the derived plan record's ratification, as `patch.ratify` says.
- **Skeptic:** Raised by skeptic batch 4 while checking the `deploy.mandate` S3 cell, which walker 3 graded holds. No other skeptic judged it.

#### B3-F11 — `deploy.mandate` reads the intake record as the plan-only mandate
- **Address:** flow-steps [deploy] `deploy.mandate`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Defect:** Under `plan-only` the mandate's witness is "the intake record". v2's 2026-10-14 revision makes the owner's plan ratification the mandate. Under `plan.ratification`'s other values (terminal-command, hook-keyword, signed-commit) the ratification is the owner's disposition at `plan.exit`. A triage-selected build has no intake record.
- **Consequence:** The landing's authority is read from the wrong record. A ratified plan goes unchecked, a triage-selected build has no witness, and a Maintain patch is mandated by an agent-typed intake, the defect gap-flow-14 records.
- **Fix:** Witness the mandate per entry: the `plan.exit` ratification, the triage record for a select, and `patch.ratify`'s disposition for a patch.
- **Skeptic:** Confirmed medium.

#### B3-F4 — The owner's landing gate can be passed by the supervisor's own choice
- **Address:** flow-steps [deploy] `deploy.mandate`; flow-steps [breakpoint]; architecture-v2 [policies] `run.on-owner-question`
- **Skeptic:** Refuted. Resolving an owner breakpoint by `run.on-owner-question`, including `best-effort-recorded`, is the owner's own LR-3 answer, and research-final-coverage records reversing it as a defect caught earlier. LR-3 carves out only ratifications, and the landing gate is an authorization. No preset pairs `three-gates` with `best-effort-recorded`: strict pairs `every-stage` with `park-item`.
- **Second skeptic:** Confirmed high. flow-steps [deploy] `deploy.mandate` / [breakpoint]: an owner breakpoint is resolved by `run.on-owner-question` "when it is raised, never for a ratification". Its witness may be "under `best-effort-recorded`, the supervisor's recorded choice". `best-effort-recorded` is the default, and no pair rule ties it to `autonomy: three-gates`. So an owner who sets three-gates and keeps the default gets a landing gate the supervisor fills, which `deploy.mandate` then accepts as the owner's disposition (c3).

### Place 22: flow-steps · design.overlaps · worst high · critical

#### B2-F3 — Two of Design's guard keys are read by no item
- **Address:** flow-steps [design] `design.overlaps` and `design.ready`
- **Class:** K4, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** `design.overlap` (warn, refuse, index-only) and `design.handoff` (derived-ready, ready-plus-audit, status-and-tier) are read by no item and no clause. `design.overlaps` has no per-value route. `design.ready` reads only "derived READY". dIndexedDesign's `cl-dClosedLoop-0383` and `cl-dClosedLoop-0384` name neither key.
- **Consequence:** The strict preset's `design.overlap: refuse` and `design.handoff: ready-plus-audit` silently fall to the weakest value. In S2 the overlapping builds X and Y both proceed to `design.unit-spec`, and READY is derived with no audit.
- **Fix:** Give `design.overlaps` a route per value of `design.overlap` (refuse → back to `design.decompose` with the overlap record). Give `design.ready` arms for `ready-plus-audit` and `status-and-tier`. Have 0383 and 0384 name both keys, each seen red on its planted value.
- **Skeptic:** Confirmed high. The strict preset sets both values, and no item or clause reads either key.

### Place 23: flow-steps · entry.claim · worst high · critical

#### A3-F3 — No item writes a patch build's derived plan record, and no flow item reads `patch.ratify`
- **Address:** flow-steps [transitions] (none → designing on `patch`); flow-steps [entry] `entry.claim`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S3
- **What is wrong:** The `patch` row (flow-steps:627) is witnessed by "the patch's derived plan record". The plan kind's writer is `plan.record` (layer-memory:404), an item a patch build never reaches, and `entry.claim` only claims the slug and takes the lease. flow's entry-point table says the record is ratified "as `patch.ratify` says", but `patch.ratify` appears nowhere in flow-steps, while v2 sets it to `owner` under `strict`.
- **Consequence:** A patch build's entry transition lacks its witness. Under `strict`, the owner ratification the preset declares silently never happens.
- **Fix:** Give `entry.claim`, or a new dPlacedRequest item, the derivation of the plan record on `patch` and `repeat`. Make that item read `patch.ratify`, with `owner` raising an owner item resolved as [breakpoint]'s owner gate is.
- **Skeptic:** Confirmed high, c3 (batch 4). `patch.ratify` occurs 0 times in flow-steps, and v2:1519 sets it to `owner` under the strict column.

#### A3-F13 — Lease refusals route "as `leases` says", which fails open on a terminal tombstone under the default `warn`
- **Address:** flow-steps [entry] `entry.claim`; flow-steps [plan] `plan.lease`; flow-steps [build] `build.unit-lease`
- **Class:** K10, c3 (A5-F3: K1, c2)
- **Severity:** high
- **Scenario:** S5 (A5-F3: S6)
- **What is wrong:** The three items (flow-steps:86, 137, 234) route "refused → as `leases` says". `leases` is "warn, refuse" with default `warn` (v2:1030), which v2:738 reads as "overlap warns by default". It says nothing about what follows a refusal, and no route splits a tombstone or epoch refusal from an overlap. [rules] (flow-steps:30) charges a refused re-dispatch to the budget, while P39 says contention draws nothing. `cl-dClosedLoop-0132`'s pre-claim budget covers only placement loops before `entry.claim`. On `patch` or `repeat`, a refused lease leaves a never-pruned claimed slug with no transition record.
- **Consequence:** Under the default preset, a replayed take against withdrawn X's tombstone proceeds with a warning, so units of a withdrawn build resume, against `cl-dClosedLoop-0281` and `cl-dClosedLoop-0415`. S6's refused lease has no declared arm, and its retry draws either on no budget or on one the rules forbid.
- **Fix:** Split the route. A tombstone, a terminal build or an epoch fence is always refused and files an ask. A live holder waits as contention within `flow.wait-ceiling`, then raises an owner item. Only an overlap goes as `leases` says. Count claim-time retries against `cl-dClosedLoop-0132`'s pre-claim budget, and state what happens to a slug claim whose lease is never taken.
- **Skeptic:** Confirmed high, c3 (batch 3). The default `warn` reads as "go on" for a take against a terminal tombstone.
- **Same as:** A5-F3

#### A5-F3 — A refused lease routes "as `leases` says", but `leases` is the overlap switch
- **Address:** flow-steps [entry] `entry.claim`; flow-steps [plan] `plan.lease`; flow-steps [build] `build.unit-lease`
- **Same as:** A3-F13
- **Skeptic:** Confirmed high, c2 (batch 3), on the same cells. P39 says contention draws nothing while [rules] charges a refused re-dispatch to the budget, so a lease held by another build gets two answers, and S6's refused lease has no declared arm.

#### A4-F14 — Early chain builds route into later builds' items with no declared stand-in
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **What is wrong:** Stage 0 counts 21 routes into a build that comes later in the chain, for example dPlacedRequest → `plan.input`, dWitnessedBar → `deploy.current` and dWellOiledMachine → `deploy.released`. recut's [reconciled-order] has no row for `plan.input`, `design.input`, `deploy.current` or `deploy.released`. The tester stand-in (flow-steps:323, `cl-dClosedLoop-0361`) starts only at dWitnessedBar, and six builds come before it.
- **Consequence:** dTrueNorth to dDeclaredLoop are built with their Test judgement and their Plan and Deploy hand-offs on undeclared stand-ins. That breaks v2:483's rule that each new dependency on a later build gets a stand-in, a class row or a move.
- **Fix:** Add a tolerance row per forward route and actor, naming today's stand-in: the session agent as tester, and push-main as Deploy.
- **Skeptic:** Confirmed medium (batch 3). Six builds precede dWitnessedBar, not five as the evidence says.

#### A5-F6 — An unreachable remote has no arm at the compare-and-swap items, and an unbounded one at `deploy.land`
- **Address:** flow-steps [entry] `entry.claim`; flow-steps [plan] `plan.lease`; flow-steps [breakpoint] `review.report`; flow-steps [deploy] `deploy.land`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S6
- **What is wrong:** The default `leases.offline: warn` queues a claim or ask-id mint and pushes it on reconnection (v2:1035, `cl-dClosedLoop-0120`). `entry.claim`, `plan.lease`, `build.unit-lease` and `review.report`'s `new:` class claim have no queued or unreachable outcome. `deploy.land` (flow-steps:368) says "the supervisor's retry, then an owner item", with no count, unlike layer-runtime:335's `stale-remote`, which parks once `leases.expiry-hours` passes.
- **Consequence:** A spec writer cannot write the queued arm or bound the landing retry. S6 still reaches a declared outcome, because an unreadable ref gets `next`'s `stale-remote` answer and `deploy.land` ends in an owner item.
- **Fix:** Add a `queued` outcome to each compare-and-swap item, waiting on reconnection within `flow.wait-ceiling`, its witness the pushed ref read on reconnection. Bound `deploy.land`'s retry with a declared count or deadline and one outcome, aligned with `stale-remote`.
- **Skeptic:** Confirmed medium (batch 3), graded down from high. S6 reaches a declared outcome, so it is not c2.

#### B1-F5 — A patch claim records no originating build, so the shared rework budget cannot be keyed
- **Address:** flow-steps [entry] `entry.claim`; flow-steps [rules] (the "Every route back is bounded" bullet)
- **Class:** K1 (B3-F3: K6)
- **Severity:** medium
- **Scenario:** S3
- **Defect:** The claim commit carries only the claimant's key, the session and the intake's or the ask's content key. Neither `entry.place` nor `entry.claim` names the originating build. [rules]' list of budget draws leaves out the patch build of a build's own landing, which v2's `flow.rework-budget` and `cl-dClosedLoop-0440` charge to the originating build's one budget.
- **Consequence:** A patch chain has no key to charge 0440's shared budget, so each patch starts a fresh one. "The originating budget spent" has no route.
- **Fix:** Add the patch-build draw to [rules]. Have the post-close patch intake and `entry.claim` record the originating build's slug and landed SHA, and derive the budget key from them. Route a spent originating budget to the originator's `flow.on-exhausted`, filed as an owner item. Seed a patch chain whose second patch shows a fresh budget.
- **Skeptic:** Confirmed medium for both findings (batch 3). `cl-dClosedLoop-0440` already obliges dShippedRelease with a planted patch-chain red, so this is a hole a spec writer falls into, not a scenario that cannot terminate.
- **Same as:** B3-F3

### Place 24: flow-steps · entry.intake · worst high · critical

#### A1-F1 — `entry.intake` is acted by a role that writes its own witness
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1 (A4-F2: S7)
- **What is wrong:** flow-steps:81 gives the actor as "orientation scout, in an owner-bound session only" and the witness as "the intake entry the scout writes". Every other record makes it a hook: flow-steps [entry] ("The hook is Runtime's"), [revised] `hook-actor-kind`, layer-roles:414, layer-memory:402, flow-roles:195-197 and `cl-dClosedLoop-0377`. [rules] says "No witness is typed by the acting agent".
- **Consequence:** The intake is the request's mandate: `deploy.mandate` reads it under `plan-only`, and `plan.ratification: request` reads it as the ratification. An agent types it about itself, so every check that takes it as the owner's words certifies agent text, and a mandate can be forged.
- **Fix:** Set the actor to "hook: the prompt-submit hook (Runtime's), in an owner-bound session only" and the witness to "the intake entry the hook writes, carrying its session binding". Add the arm to `cl-dClosedLoop-0090`'s witness-class rule, seen red on a planted role-typed intake.
- **Skeptic:** Confirmed high, c3 (batch 3). flow-steps:81 is the only record naming the scout, every other record says hook, and the record is the one the ratification and `deploy.mandate` read.
- **Same as:** A4-F2

#### A4-F2 — `entry.intake`'s actor is the orientation scout, so the agent types its own witness
- **Address:** flow-steps [entry] `entry.intake`
- **Same as:** A1-F1
- **Skeptic:** Confirmed high, c3 (batch 3). The same address and text at flow-steps:81, against flow-roles:195-197's "written verbatim by the prompt-submit hook".

#### B1-F1 — `entry.intake` is acted and witnessed by the orientation scout, not by the prompt-submit hook
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** The item's actor is "orientation scout" and its witness is "the intake entry the scout writes". That breaks flow-steps [rules] ("No witness is typed by the acting agent"). It contradicts [revised] `hook-actor-kind`, `cl-dClosedLoop-0282`, flow-roles H2 and flow-roles-adoption:202, which all make the prompt-submit hook the actor.
- **Consequence:** `deploy.mandate` takes the intake record as landing authority. In unattended S2 a build lands on an "owner's prompt" an agent could have typed or edited.
- **Fix:** Make the actor the Runtime's prompt-submit hook in an owner-bound session, and the witness the intake entry the hook writes verbatim, redacted and capped. Keep the scout only as the reader in `entry.orient`.
- **Skeptic:** Confirmed high (c3). The scout-typed witness also contradicts the item's own route ("the hook crashed or never fired") and v2 [contracts] ("Plan's witness is the hook-written intake").

### Place 25: flow-steps · life.request · worst high · critical

#### A3-F12 — A supersession hands the kept work to nothing
- **Address:** flow-steps [lifecycle] `life.request` and the kept-work note; flow-steps [design] `design.input`
- **Class:** K2, c4
- **Severity:** high
- **Scenario:** S5
- **What is wrong:** The kept-work note (flow-steps:598) says kept work passes "through the replacement's `design.inventory`", but `design.input` (flow-steps:181) reaches `design.inventory` only on "plan revision". `life.request`'s witness, "the command's record", names no replacement, yet `life.notify` posts "with the replacement's slug" and `life.close` says "superseded by its replacement". No item writes `cl-dClosedLoop-0217`'s `supersedes` edge, and `life.unlease` reclaims the build's workspaces.
- **Consequence:** Z enters Design at `design.seams`, X's built units are never inventoried, and X's workspaces are reclaimed. The kept work is lost, and dependents' links move to an unnamed replacement.
- **Fix:** Make supersede require a claimed replacement slug, refusing otherwise, and write the `supersedes` edge. Add a Design input "a supersession" that routes to `design.inventory` over X's units at its branch tip. Have `life.unlease` reclaim worktrees but keep the branch.
- **Skeptic:** Confirmed high, c4 (batch 3). S5's supersession fails to hand over the kept work.

### Place 26: flow-steps · plan.exit · worst high · critical

#### A1-F2 — Under `plan.ratification: request`, the ratification is whatever the planner records
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K1, c3 (A4-F3 and A5-F4: K10, c3)
- **Severity:** high
- **Scenario:** S1 (A4-F3: S7; A5-F4: S6)
- **What is wrong:** flow-steps:140 reads "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification". It contradicts the same record's [plan] Exits ("the request is the ratification"), flow-roles:195-198, v2 [contracts] ("Plan's witness is the hook-written intake"), `cl-dClosedLoop-0377` (the hook-written intake is the ratification), `cl-dClosedLoop-0378` (an owner-gate fallback until the hook lands) and `cl-dClosedLoop-0283`.
- **Consequence:** S1 runs on the default `request`, so Design starts on a go the planner typed, and the gate `autonomy: plan-only` keeps at Plan is met by an agent's own record. An owner who is silent, or never typed a go, is certified as having ratified. dRankedPlan's spec writer gets one rule from the item and the opposite from clauses 0377 and 0378.
- **Fix:** Replace the clause with "under `plan.ratification: request`, the hook-written intake record, joined by its content key to the build's claim, is the ratification, and until the intake kind lands the owner gate of `cl-dClosedLoop-0378`". Witness `plan.exit` by it, and plant a planner-typed go that must red.
- **Skeptic:** Confirmed high, c3 (batch 3). flow-steps:140 contradicts flow-steps:122, `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378` and `cl-dClosedLoop-0283`, all three clauses re-extracted from v2.
- **Same as:** A4-F3, A5-F4

#### A4-F3 — Under `request`, the ratification is "the owner's go, as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Same as:** A1-F2
- **Skeptic:** Confirmed high, c3 (batch 3). The same text at flow-steps:140, against flow-roles:195-198 ("Plan's item 10 is witnessed by the intake record").

#### A5-F4 — Under `plan.ratification: request`, the ratification witness is typed by the planner
- **Address:** flow-steps [plan] `plan.exit`
- **Same as:** A1-F2
- **Skeptic:** Confirmed high, c3 (batch 3). The same text at flow-steps:140; under the default `request` a record the planner typed stands as the ratification, which [rules] (flow-steps:24) forbids.

#### B1-F2 — Under `plan.ratification: request`, `plan.exit` takes the owner's go "as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Defect:** The Does cell makes "the owner's go, as the planner records it" the ratification. v2 [contracts] makes the hook-written intake Plan's witness. `cl-dClosedLoop-0137` calls a relayed request "data with provenance and never consent".
- **Consequence:** Under the default, the planner, an agent, types the ratification of its own plan. The Plan gate certifies what it does not check.
- **Fix:** Under `request`, let the hook-written intake record the build's claim names stand as the ratification. Before that hook lands, apply `cl-dClosedLoop-0378`'s owner gate. Remove "as the planner records it".
- **Skeptic:** Confirmed high (c3). The cell contradicts v2 [contracts], `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378` and `cl-dClosedLoop-0137`.

### Place 27: flow-steps · plan.record · worst high · critical

#### BS3-F3 — A spent budget has no transition row, so a build that spends it in Plan cannot end
- **Address:** flow-steps [transitions]; [rules] (the "Every route back is bounded" bullet); seen at [plan] `plan.record`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Skeptic:** Raised by skeptic batch 3 while walking `plan.record` S6 again, where walker 1 gave `holds`. No second skeptic tested it. The item is under B4-F2.
- **Same as:** B4-F2

#### BS3-F1 — An owner's late answer to a Plan question has no route
- **Address:** flow-steps [plan] `plan.record`; [breakpoint] (the owner gate); [transitions]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `plan.record` resolves an owner question as [breakpoint]'s owner gate does, and the default `run.on-owner-question: best-effort-recorded` resolves it when it is raised, although attendance asks it live. [transitions]' amendment row covers only building, testing, or deploying before the push, and `entry.place`'s `continue` goes to the build's `next`.
- **Consequence:** In S1 the plan is drafted on the supervisor's recorded choice, and no item takes in the owner's later answer during planning.
- **Fix:** Under attendance, hold an owner question until `run.owner-deadline` before best effort decides. Route an answer that arrives after the choice back to `plan.record` as a re-entry, and add a planning row to the amendment transition.
- **Skeptic:** Raised by skeptic batch 3 at `plan.record` S1 and S6, where walker 1 gave `holds`. No second skeptic tested it. Batch 1 refuted the neighbouring B4-F13 because a late answer re-enters through `entry.intake` and `entry.place`. This finding says that route has no planning arm.

### Place 28: flow-steps · review.dispose · worst high · critical

#### A1-F6 — Closing-review units have no transition row, and "released" resumes Build's tail without waiting for them
- **Address:** flow-steps [transitions]; flow-steps [build] closing review; flow-steps [breakpoint] `review.dispose`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **What is wrong:** Design's inputs list "a review finding disposed into a new unit" apart from "a fix unit" (flow-steps:171-172), but the only building → designing row (flow-steps:637) names "a unit or feature re-entry, or a fix unit", and the engine refuses any transition the table lacks. `review.dispose` routes built work "built → released" and resumes before `build.ratify` and `build.distill`, whose Needs (flow-steps:241) name no finding unit, and `build.exit` needs only `build.core`. Build's Exits require "its findings built as new units" (flow-steps:228).
- **Consequence:** When S1's closing review returns findings as new units, the engine either refuses building → designing for them, or runs `build.distill`, `build.core` and `build.exit` while the units are still in Design. The build reaches Test with its findings unbuilt, against Build's own exit contract and `cl-dClosedLoop-0400`.
- **Fix:** Add the row "building | a closing-review finding disposed into a new unit | designing | the review report and the disposition". Make `build.distill`'s Needs include every unit `review.dispose` minted, built and reuse-checked. Plant a finding unit that must hold `build.exit`.
- **Skeptic:** Confirmed high (batch 4). The transition row, the resume point and `build.distill`'s Needs read as stated, which breaks Build's exit at flow-steps:228.

#### A5-F7 — The review ceiling has no arm in the review program
- **Address:** flow-steps [breakpoint] `review.dispose`, `review.fold`, `review.pin`, `review.trigger`
- **Class:** K1 (AS4-F2: K2, c3)
- **Severity:** medium
- **Scenario:** S6
- **What is wrong:** `max-rounds` and `CEILING` appear nowhere in flow-steps. `cl-dClosedLoop-0117` refuses "the round after the limit" with the report reading CEILING, and v2:1128 declares `review.max-rounds` (3), but no item reads the key. `review.trigger` and `review.pin` pin the next round, `review.dispose` routes a follow-up "as `review.follow-up` says", `review.fold` routes the next round "as `review.design.rounds` says", and [breakpoint]'s policy list omits the key. `cl-dClosedLoop-0117` promotes only a NON-CONVERGENT round's findings, and design rounds also count against `flow.route-backs` (3).
- **Consequence:** At S6's review ceiling, `review.pin` pins a fourth round and only `flow.rework-budget` stops the loop. No item produces the CEILING report or says where its open findings go.
- **Fix:** Add `review.max-rounds` to [breakpoint]'s policy list. Have `review.trigger` or `review.pin` refuse the round past the limit and route to a CEILING report. Give `review.dispose` and `review.fold` a CEILING arm consistent with `cl-dClosedLoop-0117`'s promotion rule, and order the two bounds.
- **Skeptic:** Confirmed medium (batch 2).
- **Same as:** AS4-F2

#### B4-F4 — `review.dispose` routes by two artifact states, while a breakpoint pins four artifacts
- **Address:** flow-steps [breakpoint] `review.dispose`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `review.pin` pins a plan revision, spec revisions, a commit range or a landing record. `review.dispose` routes only "an unbuilt spec" and "built work". A landing review's findings "become new units", against [deploy]'s rule that they enter as patch builds by the post-close row, and [transitions] has no deploying → designing row after the push.
- **Consequence:** A Plan review's findings have no route. A landing review's findings become units of a landed build, through a transition the table lacks.
- **Fix:** Add an arm per artifact: a plan revision to `plan.record` for revision, and a landing record to a patch-build intake by the post-close row.
- **Skeptic:** Confirmed medium.

### Place 29: flow-steps · review.trigger · worst high · critical

#### A1-F5 — An owner-declared spec audit has no writer for its trigger record and no route from the owner's words
- **Address:** flow-steps [breakpoint] `review.trigger`; flow-steps [entry] `entry.place`
- **Class:** K3, c2
- **Severity:** high
- **Scenario:** S1
- **What is wrong:** `review.trigger` is proven by "the owner's request record", but layer-memory's kind table holds no such kind and no writer; its only near rows are `attendance override` and `disposition`. `entry.place`'s closed set (continue, amend, new, patch, repeat, ask, none) and `life.request`'s verbs carry no review request. `review.design` defaults to `opt-in`.
- **Consequence:** In S1 the owner's mid-build "audit the specs" is placed as continue and dropped. No item writes the trigger's witness, so the build passes `design.ready` and lands without the audit: a terminal reached without its witness. The default spec audit has no declared way to be opted into.
- **Fix:** Register an owner request record kind with its writer. Either add a review or breakpoint outcome to `entry.place` and to `life.request`, writing that record at the named boundary, or name `disposition` as the witness and state its writer. Probe it with a planted owner prompt "audit the specs" that must produce `review.trigger` before `design.ready`.
- **Skeptic:** Confirmed high (batch 2). No such kind or writer exists, neither closed set carries a review request, and `review.design: opt-in` leaves the default audit with no way in.

### Place 30: flow-steps · test.seen-red · worst high · critical

#### AS4-F3 — The seen-red record's only declared writer is the item that checks for it
- **Address:** flow-steps [test] `test.seen-red`; layer-memory kind table `seen-red`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S7
- **What is wrong:** layer-memory:425 says "seen-red | dWitnessedBar | its writer is `test.seen-red`", and flow-steps:299 has that same item check for the record, proven by "the seen-red records". No other item sees a gate red and records it, and `cl-dClosedLoop-0345` is the bare phrase "seen-red records".
- **Consequence:** Built as declared, the check reads records its own writer produced, so it certifies gates nobody saw red. Otherwise nothing writes the record, and every new gate of chain build k fails the check.
- **Fix:** Name a writer that runs the gate against its plant (the unit's acceptance or the executor), and keep `test.seen-red` as a reader only.
- **Skeptic:** Raised by skeptic batch 4 while checking the `test.seen-red` S7 cell, which walker 4 graded holds. No other skeptic judged it.

### Place 37: flow-steps · design.input · worst high

#### A3-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`, `design.overlaps`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** `design.input` routes "patch → `design.unit-spec`, as a micro-spec", which skips `design.overlaps`, and patches also skip `plan.dedupe`. `design.unit-spec` "acknowledges the unit's overlaps" with no overlap record to acknowledge.
- **Consequence:** Concurrent patches, or a patch and a live build on the same paths, are first seen at `build.unit-lease`, which only warns by default. Under `strict`, `design.overlap: refuse` never applies to a patch.
- **Fix:** Route patch → `design.overlaps` → `design.unit-spec`.
- **Skeptic:** Confirmed medium (batch 2).

#### B2-F5 — A superseding build never reaches `design.inventory`, so the kept work has no route
- **Address:** flow-steps [design] `design.input` (and [lifecycle]'s kept-work rule)
- **Class:** K2
- **Severity:** high
- **Scenario:** S5
- **Defect:** [lifecycle] says a superseded build's kept work passes to its replacement through the replacement's `design.inventory`. `design.input` sends a plan record to `design.seams` and only a plan revision to `design.inventory`, which judges the build's own completed units. No input kind carries a superseded build's units.
- **Consequence:** Replacement Z never inventories X's built units. They get no kept, amended or retired verdict, and they drop out of the trail.
- **Fix:** Add a `supersession` input kind, Z's plan record naming the build it supersedes, which `design.input` routes to `design.inventory` over the superseded build's built units. Add its [transitions] row. Have `life.request`'s supersede name Z's slug before `life.notify`.
- **Skeptic:** Confirmed high (batch 2). The walker's c4 is overstated: X's commits and records are left uncarried, not overwritten, so the item is not critical. Batch 3 confirmed the twin B4-F6 at medium.
- **Same as:** B4-F6

#### B2-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `design.input` routes a patch straight to `design.unit-spec`. A patch never reaches Plan, so it skips both `plan.dedupe` and `design.overlaps`.
- **Consequence:** A patch's write set is never checked against live builds, so strict's `design.overlap: refuse` never applies to it. A collision first shows at `build.unit-lease`, which only warns, or at Test's merge.
- **Fix:** Route patch, finding and fix inputs through `design.overlaps` for their unit before `design.unit-spec`.
- **Skeptic:** Confirmed medium.

### Place 38: flow-steps · design.ready · worst high · includes an unverified finding

#### A1-F7 — `design.ready` and `test.exit` wait on the recommend item, not the reason item, so the frontier can pass a review the reason calls for
- **Address:** flow-steps [design] `design.ready`; flow-steps [test] `test.exit`
- **Claimed:** once `design.recommend` is witnessed, `design.ready` can be recorded before `design.reason` asks for the audit, and Test has the same hole.
- **Skeptic:** Refuted (batch 3). Under `scored-signals-and-reasoning`, `design.recommend` routes only to `design.reason` (flow-steps:190), and `design.ready` is reached only from `design.reason`'s "no review" arm or after the spec audit, which stands before it (flow-steps:191, 208, 450). A route-blind frontier would also run `design.seams`, `design.inventory` and `design.reentry` on every input, so the frontier cannot be read the finding's way. The evidence misquotes `test.reason`, whose Then (flow-steps:301) has no "a review →" arm keyed on its answer.
- **Second skeptic:** Confirmed high. The finding holds. In flow-steps [design], line 192 gives `design.ready`'s Needs as only "`design.recommend`, and the spec audit where it ran". Line 302 gives `test.exit` the same shape, waiting on `test.recommend` and not `test.reason`. [rules] lines 26-31 build the frontier from the Needs column alone, and layer-runtime [decide] line 329 has `next` hand out every frontier item to run. So once `design.recommend` is witnessed, `design.ready` (a command) and `design.reason` (an architect agent) are both runnable. Line 208 says the audit sits "after `design.recommend` and `design.reason`, before `design.ready`", but no Needs column enforces that order. v2 :1527 sets `review.recommendation: binding` in a preset, so a review the reason calls for can be skipped (c3).

#### B2-F1 — Conditional needs put Design's and Build's exits on the frontier before the breakpoint is decided
- **Address:** flow-steps [design] `design.ready`; also [build] `build.ratify`, `build.distill`, [test] `test.exit` and [deploy] `deploy.notify`
- **Class:** K1
- **Severity:** medium (the walker graded it high, c3)
- **Scenario:** S1
- **Defect:** `design.ready` needs "`design.recommend`, and the spec audit where it ran". Once `design.recommend` is witnessed, `design.ready` shares the frontier with `design.reason`, the item that decides whether an audit is owed. `build.distill` ("the closing review where it ran") and `test.exit`, which leaves out `test.reason`, have the same untagged conditional need.
- **Consequence:** Under `review.recommendation: binding`, an exit can be derived before its owed spec audit or closing review is decided.
- **Fix:** Make the breakpoint an explicit need. `design.ready` needs `design.reason` (or `design.recommend` under `signals-only`), plus the breakpoint's disposition record when its trigger fired. Do the same for `build.ratify` and `build.distill`, `test.exit` and `deploy.notify`. Add a static check that reds an untagged conditional in a Needs cell.
- **Skeptic:** Confirmed medium. On the defaults an owed or running review still blocks (`review.blocks` every-review, `review.recommendation` advice), so the race costs something only under `binding`.

#### B2-F19 — `design.ready`'s witness lacks the UNCARRIED class its clause adds
- **Address:** flow-steps [design] `design.ready`
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Defect:** The witness is "none MISSING, THIN or FORKED". `cl-dClosedLoop-0398`, the same owner's clause, adds "`design.ready` gaining an UNCARRIED class".
- **Consequence:** A spec writer working from the item draft leaves out the coverage arm.
- **Fix:** Add UNCARRIED, under `design.coverage`, to the item's witness.
- **Skeptic:** Confirmed low.

### Place 41: flow-steps · review.pin · worst medium · critical

#### AS4-F2 — No breakpoint item reads `review.max-rounds`, so a round past the CEILING is pinned and run
- **Address:** flow-steps [breakpoint] `review.pin`, `review.trigger`
- **Same as:** A5-F7
- **Skeptic:** Raised by skeptic batch 4 at medium while checking the `review.pin` S6 cell, which walker 5 graded holds. No other skeptic judged it.

#### B4-F11 — dFairHearing's breakpoint items rest on later builds with no stand-in
- **Address:** flow-steps [breakpoint] `review.pin`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** dFairHearing's `review.pin` picks `design-audit` by the record-kind registry, which dTotalRecall builds later in the chain. `review.report` routes to `review.dispose`, which is dDeclaredLoop's and not an ancestor. [breakpoint] declares no stand-ins, unlike [probe], and `[stage0-classes]` is empty.
- **Consequence:** When dFairHearing lands, its preset choice and its next route name parts that do not exist yet.
- **Fix:** Declare stand-ins in [breakpoint] as [probe] does: a record kind read from the filename, and disposition by hand until dDeclaredLoop. Class the lead in `[stage0-classes]`.
- **Skeptic:** Confirmed medium. The slug-claim leg is weaker: compare-and-swap ref claims exist today (unattended's `refs/gov/runs`), though no chain clause builds `refs/gov/class-claims`.

### Place 114: flow-steps · [adopt] · worst medium

#### B5-F15 — `adopt.instructions` and `adopt.declarations` have no row in the adopt step
- **Address:** flow-steps [adopt]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Defect:** [adopt] has five rows. adopter-instructions and flow-roles-adoption add `adopt.instructions` (`cl-dClosedLoop-0260`) and `adopt.declarations` (`cl-dClosedLoop-0438`) to the `adopt` program, and neither has a row.
- **Consequence:** S4's declarations, proposed as overlay rows, have no actor, Needs, witness or route. Neither the item join nor Stage 0's K1 can see either item.
- **Fix:** Add both rows, each with its owner build, Needs (`kits.install` or `kits.update`), witness (the proposal records) and routes (the owner's one ruling per row).
- **Skeptic:** Confirmed medium.

### Place 115: flow-steps · [breakpoint] · worst medium · includes an unverified finding

#### B4-F13 — An owner's late answer after the deadline has no route
- **Address:** flow-steps [breakpoint]
- **Skeptic:** Refuted. A late owner answer is a prompt in an owner-bound session, so `entry.intake` records it and `entry.place` disposes of it from its closed set: amend → Design re-entry, or an `intake` message to the session holding the build. P22 gives every request a recorded disposition.
- **Second skeptic:** Confirmed medium. flow-steps [breakpoint]: once an owner item is decided (by the supervisor's choice when raised, or by the recommendation applied past the deadline), no item, transition row or clause says what an owner disposition arriving afterwards does. S1 injects exactly that late answer, and searches for late or after-deadline handling in the design records find none.

### Place 116: flow-steps · [lifecycle] · worst medium

#### B4-F6 — A replacement build never reaches `design.inventory`, so supersession's kept work has no route
- **Address:** flow-steps [lifecycle]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Skeptic:** Confirmed medium (batch 3): no input kind carries a superseded build's units into the replacement. The item is under B2-F5.
- **Same as:** B2-F5

### Place 117: flow-steps · adopt.decisions · worst medium

#### A4-F15 — `adopt.decisions` has two actor kinds
- **Address:** flow-steps [adopt] `adopt.decisions`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **What is wrong:** flow-steps:614 gives the actor "reviewer, as two raters, and the owner where `retrofit.decisions` says". [rules] requires one actor of one kind, and one item per policy value. layer-roles:409 lists the item under reviewer only.
- **Consequence:** Under `docs-owner-ratifies`, the owner's ruling has no item of its own, so no witness or route is declared for it.
- **Fix:** Split the row into `adopt.decisions` (reviewer) and an owner item under `retrofit.decisions`.
- **Skeptic:** Confirmed medium (batch 2).

#### B5-F8 — `adopt.decisions` has two actor kinds and no route when the raters disagree
- **Address:** flow-steps [adopt] `adopt.decisions`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S7
- **Defect:** The actor is two kinds: the reviewer as two raters, and the owner. The routes are only "accepted" and "declined by the owner". None covers raters who disagree, or agreement under the kappa 0.8 bar `cl-dClosedLoop-0238` sets.
- **Consequence:** When dLinkedLibrary routes gov's own decision rows, a disagreement or a low kappa has no outcome. Under the default `author-rubric`, a candidate the raters reject has no route either.
- **Fix:** Split the item per actor: a raters item that computes agreement, and an owner item under `docs-owner-ratifies`. Add routes for disagreement (to the owner or a third rater) and for a kappa below the bar (a re-rating round on the budget).
- **Skeptic:** Confirmed medium. research-retrofit-a's "kappa < 0.8 → rubric revised" was not carried forward.

### Place 118: flow-steps · build.acceptance · worst medium

#### A5-F2 — A loop that ends non-converging on a blocking item leaves the build with no route
- **Address:** flow-steps [rules]; flow-steps [build] `build.acceptance`; flow-steps [test] `test.flakes`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S6
- **What is wrong:** [rules] (flow-steps:41-42) and v2:1133 send a loop past `flow.route-backs` to asks. `cl-dClosedLoop-0117` instead promotes its findings "to units while budget remains and to asks after". `build.acceptance` (flow-steps:236) has only "fail → a fix pass", and Build's exit needs every unit built. The defaults (route-backs 3, budget 4+2) trip the per-item bound before the budget is spent.
- **Consequence:** S6's red unit and its flake each stop at the per-item bound with the unit unbuilt or the leg red, and `flow.on-exhausted` never fires. layer-runtime:333's `stuck` raises an owner item, so the stall ends in a declared item. What remains is two contradictory rules a spec writer trips over.
- **Fix:** State one rule in [rules], `build.acceptance` and `test.flakes`, consistent with `cl-dClosedLoop-0117`: past `flow.route-backs`, a blocking item's open work becomes a new unit while budget remains, and goes to `flow.on-exhausted` after. Plant an acceptance red that never greens and must reach a terminal.
- **Skeptic:** Confirmed medium (batch 3), graded down from high. `stuck` ends the stall in a declared owner item, so it is not c2.

#### B2-F6 — "A fix pass" and "a revert pass" are no items, so their allowance attaches nowhere
- **Address:** flow-steps [build] `build.acceptance` (also `build.scope`, and [test]'s "A fix pass keeps its check")
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Defect:** "A fix pass" (`build.acceptance`, `test.attribute`, `test.seen-red`) and "a revert pass" (`build.scope`) are route targets, but no row declares them. `build.unit-pass` declares only the ordinary allowance.
- **Consequence:** The engine has no tag to put on the frontier for a red unit. M16's narrowed fix-pass allowance renders into no work order, and the budget draw attaches to no instance.
- **Fix:** Declare `build.fix-pass`: the builder, Needs naming the red record, the allowance minus the red check's files and the acceptance files, and Then `build.acceptance`. Declare the revert pass too, and route every "fix pass" to that tag.
- **Skeptic:** Confirmed medium.

### Place 119: flow-steps · build.reuse-check · worst medium

#### A1-F8 — No route reaches `build.recommend`: "the unit built" is not an item, and its Needs are prose
- **Address:** flow-steps [build] `build.reuse-check`, `build.recommend`
- **Class:** K2 (AS1-F1: K1, K2)
- **Severity:** medium (the walker graded it high)
- **Scenario:** S1 (AS1-F1: S2)
- **What is wrong:** `build.reuse-check` routes "clean → the unit built", a target in no declared form. `build.recommend` needs "every unit built and reuse-checked", which names no item. Stage 0 lists the Build step's five items from `build.recommend` on as reached from no entry.
- **Consequence:** The position engine (`cl-dClosedLoop-0092`, over `cl-dClosedLoop-0094`'s declared needs) cannot derive when `build.recommend` is ready, so Build's tail, its exit and the closing review it owes cannot be reached from the declarations. In S2, X's units finish on two nodes and no declared need joins their witnesses. The intent, a join over the roster, is plain to a spec writer.
- **Fix:** Route clean → `build.recommend` once every unit's `build.reuse-check` is witnessed clean. Declare the need as `build.reuse-check`, every instance clean, seen red on a planted unit whose reuse-check is still open.
- **Skeptic:** Confirmed medium (batch 2), graded down from high. The declarations are wrong but no scenario fails.
- **Same as:** AS1-F1

### Place 120: flow-steps · build.unit-lease · worst medium

#### B2-F8 — Only the starting units' leases are taken by any item
- **Address:** flow-steps [build] `build.unit-lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `build.unit-lease` "takes each starting unit's lease", with one need, `build.base`. `build.scope` routes later work to "the unit's next pass" or `build.reuse-check`, never to a lease.
- **Consequence:** A unit that starts later is leased by no item. v2's pick (`cl-dClosedLoop-0331`) offers "ready unleased units" to other nodes, so in S2 two nodes can start it.
- **Fix:** Make `build.unit-lease` per unit, with Needs that are the unit's predecessors in declared order.
- **Skeptic:** Confirmed medium.

### Place 121: flow-steps · cl-dClosedLoop-0116 · worst medium

#### A3-F7 — Once the budget is spent, a post-merge red ends in a closed-incomplete patch and a red default branch
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0116`
- **Class:** K10
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **What is wrong:** `cl-dClosedLoop-0440` puts a landing's patch on the originating, already spent budget. Under the default `best-effort-ending`, `cl-dClosedLoop-0116` closes the build incomplete, "raising the budget the owner's alone", and no owner item is opened.
- **Consequence:** The default branch stays red. The pre-push hook (.githooks/pre-push:1909-1971) then forces FULL on every later landing, and `test.route` sends each later build's INHERITED red to its own fix unit on its own budget.
- **Fix:** When the shared budget is spent, have a post-merge red open an owner item to raise the budget or revert, whatever `flow.on-exhausted` says. Show it on a planted spent chain.
- **Skeptic:** Confirmed medium (batch 2), graded down from high. The outcome is declared and the chain ends, so no scenario fails to terminate.

### Place 122: flow-steps · cl-dClosedLoop-0282 · worst medium

#### C4-F4 — The settling row names an orientation scout as `entry.intake`'s actor, though cl-0282 builds it as a hook
- **Address:** flow-steps [entry] `entry.intake` row, against architecture-v2 [chain] cl-dClosedLoop-0282
- **Class:** K1
- **Severity:** medium
- **Evidence:** flow-steps:81 reads "Actor: orientation scout, in an owner-bound session only … Proven by: the intake entry the scout writes". Against it stand the same record's amendment `hook-actor-kind` (flow-steps:796, "`entry.intake` is a hook"), its Owner note (flow-steps:99), layer-roles:414 ("| hook | `entry.intake` |") and cl-0282's prompt-submit hook "writing each owner prompt verbatim".
- **Consequence:** The item join and the owner check read an agent as the writer of the intake record. That record is "the mandate to land" (gap-rt-14), so the owner's verbatim mandate would be agent-typed. A builder of cl-0282 or of `entry.orient` meets two contradictory actors.
- **Fix:** Set the row's actor to "hook: prompt-submit, owner-bound sessions only", and its witness to "the intake entry the hook writes".
- **Skeptic:** confirmed medium.

### Place 123: flow-steps · cl-dClosedLoop-0319 · worst medium

#### AS4-F4 — Placement's closed disposition set has no way to offer one unit of a build leased elsewhere, which cl-0319 places "at placement"
- **Address:** flow-steps [entry] `entry.place`; architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0319`
- **Class:** K2, K6
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** `cl-dClosedLoop-0319` offers "a unit of a leased build … at placement to another session or node as `build.unit-holders` says". `entry.place`'s set is continue, amend, new, patch, repeat, ask and none. `continue` goes to that build's `next` and is checked as "the build is live and its lease is free or this session's" (orientation:153-154).
- **Consequence:** Node x's request to take one of X's units gets no disposition, or is refused under the default `placement.check: refuse` because d holds X's lease. A spec writer for dPlacedRequest cannot satisfy dWellOiledMachine's clause.
- **Fix:** Add a `unit` disposition, routed to that unit's lease under `build.unit-holders` and refused under `driver-only`, with its check.
- **Skeptic:** Raised by skeptic batch 4 while checking the `entry.place` S2 cell, which walker 2 graded holds. No other skeptic judged it.

### Place 124: flow-steps · cl-dClosedLoop-0377 · worst medium

#### BS2-F1 — `plan.input` pins an intake record that no ancestor of dRankedPlan writes
- **Address:** flow-steps [plan] `plan.input`; architecture-v2 [chain] `cl-dClosedLoop-0377`, `cl-dClosedLoop-0378`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `plan.input` pins the intake record, which `cl-dClosedLoop-0377` says dWellOiledMachine's prompt-submit hook writes. dWellOiledMachine is not among dRankedPlan's parents, and `cl-dClosedLoop-0378`'s stand-in covers only `plan.exit`'s ratification. No prompt-submit hook exists in today's tree.
- **Consequence:** When dRankedPlan lands, a build started from an owner prompt has nothing for `plan.input` to pin, and `plan.record` drafts from words nothing witnesses.
- **Fix:** Give `plan.input` the stand-in 0378 gives `plan.exit`: pin `entry.orient`'s "intake absent" record, with the owner's words taken as the owner gate's disposition, until dWellOiledMachine lands.
- **Skeptic:** Raised by skeptic batch 2 at `plan.input` S7, where walker 1 gave `holds`. No second skeptic tested it.

### Place 125: flow-steps · cl-dClosedLoop-0422 · worst medium

#### A2-F9 — Landing order is node-local, so P21's plan-priority order does not hold across nodes
- **Address:** flow-steps [deploy] "The landing order"; architecture-v2 [chain] dShippedRelease `cl-dClosedLoop-0422`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** flow-steps says "Landings on a node are ordered by `landing.order`". P21 and flow-interactions FI-7 settle "plan priority, then first verified" with no per-node scope, and neither `cl-dClosedLoop-0422` nor `gap-flow-08` names a shared ref or a cross-node order.
- **Consequence:** Builds verified at once on d and on x land in push-race order. `landing.order: owner-orders` and plan priority have no effect across nodes.
- **Fix:** Order landings through a compare-and-swap landing-turn ref on the remote. Otherwise narrow P21 and `landing.order` to one node, and record the cross-node rule as first-pushed.
- **Skeptic:** Confirmed medium (batch 2).

#### B3-F10 — `landing.order` is never read, so strict's `owner-orders` does nothing
- **Address:** flow-steps [deploy] (landing order); architecture-v2 [chain] `cl-dClosedLoop-0422`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `landing.order` appears only in [deploy]'s prose and Deploy's policy list. No item's Does cell reads it. `cl-dClosedLoop-0422` says only "landings ordered through the landing queue it builds".
- **Consequence:** Strict's `owner-orders` is silently ignored, and concurrent landings go in whatever order the queue takes.
- **Fix:** Have 0422 read `landing.order` with an arm per value, and have `deploy.land` need the queue's admission. Seed an `owner-orders` landing admitted with no order.
- **Skeptic:** Confirmed medium.

### Place 126: flow-steps · cl-dClosedLoop-0440 · worst medium

#### A3-F5 — One post-merge red raises two patch builds, and one of them escapes the shared budget
- **Address:** flow-steps [deploy] `deploy.core`; layer-expansions [Maintain] `default-branch-red`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **What is wrong:** `deploy.core` raises a patch on red. The same red, indexed by `refs/gov/bar-red` (published at `tools/run-gates/post-merge.sh:249`), is the `default-branch-red` event that starts a Maintain run, whose `maintain.patch` can open a second patch. Patch builds skip `plan.dedupe`, and `cl-dClosedLoop-0440` shares the budget only for "a patch build raised by a landing".
- **Consequence:** For a red whose fix is a tracked-content safe fix, two patch builds race to fix one red. The Maintain one starts on a fresh budget, so the chain of patches is no longer bounded (P39). A product-code red goes to `maintain.file` and triage instead, where `plan.dedupe` matches the live patch.
- **Fix:** Use one producer and one key, (`default-branch-red`, landed SHA): `deploy.core` files under the key Maintain's reading uses, and `maintain.patch` finds it. Extend `cl-dClosedLoop-0440` to a Maintain patch whose offender is a landed SHA, seen red on a planted double filing.
- **Skeptic:** Confirmed medium (batch 2), graded down from high. `maintain.patch` opens a patch only for a safe-fix reading, so the double filing happens only for that class of red.

#### B3-F3 — Patch builds have no link to the originating build's budget
- **Address:** flow-steps [rules] (the "Every route back is bounded" bullet); flow-steps [entry] `entry.claim`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K6
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **Skeptic:** Confirmed medium, the same defect as B1-F5. The item is under B1-F5.
- **Same as:** B1-F5

### Place 127: flow-steps · deploy.distill · worst medium

#### B3-F12 — `deploy.distill` can pass on an empty join before dScopedBuild lands
- **Address:** flow-steps [deploy] `deploy.distill`; architecture-v2 [chain] dShippedRelease row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `deploy.distill` joins the decision-log rows `build.distill` wrote (dScopedBuild) to the build's major forks (dIndexedDesign's fork classes). Neither build is an ancestor of dShippedRelease. v2 has no rule that an empty join is anything but green.
- **Consequence:** If dShippedRelease lands first, `deploy.distill` joins zero forks to zero rows and passes.
- **Fix:** Add dScopedBuild to dShippedRelease's parents. Or have `deploy.distill` report "measured nothing" and never pass until `build.distill`'s writer lands, seen red on an empty population.
- **Skeptic:** Confirmed medium. v2's only non-empty-population clause is the tag join's.

### Place 128: flow-steps · deploy.notify · worst medium

#### B3-F9 — After the push, an unreachable remote spends the rework budget
- **Address:** flow-steps [deploy] `deploy.notify`, `deploy.snapshot`, `deploy.unlease`, `deploy.close`; flow-steps [rules]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Defect:** All four items write to the remote. Unlike `deploy.land`, none declares an unreachable-remote outcome, so a failed act takes [rules]' default refusal route, which draws on the rework budget.
- **Consequence:** A remote outage after the push charges a landed build's budget, one draw per failed act.
- **Fix:** Class an unreachable remote as contention for every command item: a retry that draws nothing, then an owner item at `flow.wait-ceiling`, as `deploy.land` does.
- **Skeptic:** Confirmed medium. The walker's run to exhaustion is overstated: layer-runtime's `stale-remote` answer holds and retries without a draw while refs cannot be read.

### Place 129: flow-steps · deploy.parents · worst medium

#### A2-F4 — `deploy.parents`' hold declares no deadline or outcome, so it fails the design's own static check
- **Address:** flow-steps [deploy] `deploy.parents`; architecture-v2 [policies] `flow.wait-ceiling`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S2 (A3-F11: S5)
- **What is wrong:** The Then cell reads "a parent unlanded or paused → holds", with nothing past it. The `flow.wait-ceiling` catalogue row names "a dependency hold", and `cl-dClosedLoop-0118` reds "a wait declaring no deadline", but Deploy's policy list (flow-steps:414) omits the key. A paused parent keeps its leases renewed, so it never expires.
- **Consequence:** Y holds at `deploy.parents` with no declared arm, and the loop definition built from this draft fails dDeclaredLoop's own static check. The scenario failure past the ceiling is A3-F10's missing `replan` transition, not this one.
- **Fix:** Add a branch to the Then cell: past `flow.wait-ceiling`, an owner item, or as `deps.on-parent-withdrawn` says. Add the key to Deploy's policy list. See it red on a planted parent that never lands, or is paused past the ceiling.
- **Skeptic:** Confirmed medium (batch 2).
- **Same as:** A3-F11

#### A3-F11 — Y's dependency hold at `deploy.parents` declares no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`; architecture-v2 [policies] `flow.wait-ceiling`
- **Same as:** A2-F4
- **Skeptic:** Confirmed medium (batch 2), graded down from high. The `flow.wait-ceiling` row and stall-and-loop point 6 already declare the hold's deadline and default, so the item's missing arm is a spec-writer trip.

#### B3-F5 — A parent hold declares no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S5
- **Defect:** "A parent unlanded or paused → holds" declares no deadline and no outcome, and Deploy's policy list leaves out `flow.wait-ceiling`. The item fails `cl-dClosedLoop-0118`'s check that every wait declares both.
- **Consequence:** Gov's own item fails the design's static termination check as written, and a spec writer can build an unbounded hold.
- **Fix:** Write the hold as "holds until `flow.wait-ceiling`, then as `deps.on-parent-withdrawn` says, with an owner item", a counted wait with its witness.
- **Skeptic:** Confirmed medium. v2's `flow.wait-ceiling` row and stall-and-loop item 6 give dependency holds a deadline and a default ("replan"), so a terminal exists and c2 does not hold.

### Place 130: flow-steps · design.decompose · worst medium

#### B2-F9 — A parent's `withdrawn` or `superseded` notice has no route before `deploy.parents`
- **Address:** flow-steps [design] `design.decompose` (and the [design] and [build] policy lists)
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Defect:** `deps.on-parent-withdrawn` is read only at `deploy.parents`. No Design or Build item routes a parent's notice, and an acknowledgement triggers no replan.
- **Consequence:** Dependent Y keeps designing and building on X's withdrawn interface until Deploy, then replans, having spent its budget and leases.
- **Fix:** Route a parent's notice read at any item boundary to `deps.on-parent-withdrawn` there, with replan going to `design.reentry`. Add the key to Design's and Build's policy lists.
- **Skeptic:** Confirmed medium. layer-flow F-E says dependents act as the key says, yet no item routes a read notice, and `cl-dClosedLoop-0328` releases dependents only from a wait.

### Place 131: flow-steps · entry.place · worst medium · includes an unverified finding

#### B1-F8 — dPlacedRequest's entry routes and slug mint depend on builds that are not its ancestors
- **Address:** flow-steps [entry] `entry.place`
- **Skeptic:** Refuted. The routes are outputs, not inputs: "claimed → Plan" and "→ Design" end at transitions in dDeclaredLoop's table, an ancestor, and no witness needs dRankedPlan's or dIndexedDesign's items. The `builds.slug-*` keys read at their catalogue defaults through dGroundRules' reader. Today's mint and `check_slug_claimed` exist in `tools/memory-tree/gen_build_index.py`. v2:483 is a revision note, not a general rule.
- **Second skeptic:** Confirmed medium. flow-steps [entry] `entry.place`: new routes to Plan (dRankedPlan) and amend/patch to Design (dIndexedDesign). Neither is an ancestor of dPlacedRequest (its only parent is dDeclaredLoop). Stage 0 marks these routes "not an ancestor, UNCLASSED". The slug mint reads dTotalRecall's `builds.slug-*`, and dTotalRecall comes after dPlacedRequest. Only `repeat` gets a stand-in (cl-0156, "filed as an ask until dIndexedDesign lands"), against v2's rule that "each new dependency on a later build gets a stand-in, a class row or a move".

### Place 132: flow-steps · life.quiesce · worst medium

#### A3-F15 — Quiesce cannot stop acts other nodes run under X's unit leases
- **Address:** flow-steps [lifecycle] `life.quiesce`, `life.unlease`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **What is wrong:** The executor's `life.quiesce` witness is "the executor's record of the acts it let finish" (flow-steps:588). A node that takes a unit by lease runs it under its own supervisor (P40). After `life.unlease`'s tombstones, that supervisor kills its act sessions and fences its pushes (layer-runtime:420-423).
- **Consequence:** Node x's in-flight unit pass is cut off mid-act, with its commits neither kept nor recorded. The quiesce witness claims a quiesce it never observed.
- **Fix:** Make `life.quiesce` wait, per unit lease, for the holder's hand-over or for its `runtime.act-ceiling`, witnessed per lease.
- **Skeptic:** Confirmed medium (batch 3).

#### A3-F19 — `life.quiesce` routes a pause to `parked`, a state `[transitions]` lacks
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K1
- **Severity:** low
- **Scenario:** S5
- **What is wrong:** flow-steps:588 reads "pause → parked", while [transitions] (flow-steps:645) names the state `paused`.
- **Consequence:** A route names a state the engine does not know.
- **Fix:** Write "pause → paused".
- **Skeptic:** Confirmed low (batch 3), as wording.

#### B4-F5 — A paused build's lease renewal contradicts the default renewal rule
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium (the walker graded it high)
- **Scenario:** S5
- **Defect:** [lifecycle] has the supervisor renew a paused build's leases. The default `leases.renewal: progress` renews only on witnessed progress and on declared waits inside their deadline, never on a beat alone, and no record declares pause as such a wait. `life.quiesce` routes "pause → parked", while `cl-dClosedLoop-0326`'s parking releases the lease.
- **Consequence:** A spec writer either lets a paused build's lease expire, so another node can pick the build up, or renews it with no deadline, against P39.
- **Fix:** Declare pause a wait with a deadline (`flow.wait-ceiling` or its own key) and an outcome, renewed under `progress` as a declared wait. Rename the route to `paused`.
- **Skeptic:** Confirmed medium. Two records disagree, but no scenario is shown to fail.

#### B4-F8 — `life.quiesce` reaches only the driver's own acts
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Defect:** The witness is "the executor's record of the acts it let finish". A unit holder in another session or node (`cl-dClosedLoop-0319`) is never told. Once quiesce dispatches nothing new, no route takes a finished review fan's findings to `review.dispose` or to asks.
- **Consequence:** A remote holder's passes run unrecorded until the fence refuses them after `life.unlease`. A finished review's findings are disposed into a withdrawn build, or lost.
- **Fix:** Have `life.quiesce` post a quiesce message to every unit holder and join their acknowledgements into its witness. Route a finished review's findings to asks under withdraw and to the replacement under supersede.
- **Skeptic:** Confirmed medium.

#### B4-F7 — "Once a push is made, the build has landed" reads every pass push as a landing
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** low (the walker graded it medium)
- **Scenario:** S5
- **Defect:** The sentence is ambiguous now that `cl-dClosedLoop-0318` pushes every pass commit.
- **Consequence:** Read literally, X's first pass push refuses the owner's withdraw mid-Build.
- **Fix:** Write "once the landing push to the default branch is made". Add a fixture that withdraws after a pass push and is refused only after the landing push.
- **Skeptic:** Confirmed low. The same sentence equates the push with landing, and [transitions] reads "before the push" in Deploy's context, so it is a wording fix.

### Place 133: flow-steps · plan.dedupe · worst medium

#### B1-F9 — Plan reads the design index, which no ancestor of dRankedPlan builds
- **Address:** flow-steps [plan] `plan.dedupe`, `plan.exit`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `plan.dedupe` checks "against live builds, the design index and open asks". The design index is `cl-dClosedLoop-0384`, in dIndexedDesign's row. dRankedPlan's parents are dDeclaredLoop, dTotalRecall and dBoundRoles, and its only stand-in, `cl-dClosedLoop-0378`, covers intake. `plan.exit` also launches "where `run.host` says", a dWellOiledMachine key, and Stage 0 flags its target as in no declared form.
- **Consequence:** dRankedPlan's dedupe cannot run as specified when it lands.
- **Fix:** Dedupe against live builds and open asks only until dIndexedDesign lands, then join the index arm. Write `plan.exit`'s target in a declared form.
- **Skeptic:** Confirmed medium on the index half. The `run.host` half is weaker, since the key can read its catalogue default.

### Place 134: flow-steps · plan.lease · worst medium

#### A1-F11 — The overlap outcomes of the lease items route nowhere, and one cites the wrong key
- **Address:** flow-steps [plan] `plan.lease`; flow-steps [build] `build.unit-lease`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1 (A4-F20: S7)
- **What is wrong:** `plan.lease` (flow-steps:137) reads "an overlap → noted on the card and in the other build's mailbox", with no next item. `build.unit-lease` (flow-steps:234) says "an overlap → warned (`leases.overlap`)". `leases.overlap` is the granularity ("kit-dirs, files, builds", v2:1034). Warn or refuse is `leases` (v2:1030), which v2:1353 sets to `refuse` in two presets.
- **Consequence:** A feature on a `tools/` kit overlaps any live build on that kit under the default `kit-dirs`, and neither item says whether the lease is held and the run goes on. Under the two refuse presets, "warned" is the wrong outcome.
- **Fix:** Write "an overlap under `leases: warn` → noted, then as held (`plan.recommend`); under `refuse` → as refused" in both rows. Cite `leases`, with `leases.overlap` as the granularity.
- **Skeptic:** Confirmed medium (batch 3).
- **Same as:** A4-F20

#### A4-F20 — `plan.lease`'s overlap outcome has no next route
- **Address:** flow-steps [plan] `plan.lease`
- **Same as:** A1-F11
- **Skeptic:** Confirmed low (batch 3). `plan.lease` (flow-steps:137) names no next item after "an overlap → noted on the card and in the other build's mailbox".

### Place 135: flow-steps · probe.judge · worst medium

#### B4-F9 — `probe.judge` mixes three actor kinds
- **Address:** flow-steps [probe] `probe.judge`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The actor is "command: the executor's re-run, or the experiment's scorer". The witness adds "the verifier's judgment", and [probe] Roles adds "a blind judge". The executor, a command and a role act in one item, against [rules]' one actor of one kind.
- **Consequence:** The item cannot get one work order, allowance or return schema, and its role arm has no actor.
- **Fix:** Split it into `probe.judge` (a command: the re-run or the scorer) and `probe.judge-claimed` (the tester or a blind judge), routed when no command can judge.
- **Skeptic:** Confirmed medium.

### Place 136: flow-steps · probe.trigger · worst medium

#### B4-F10 — The reproduction probe before a patch fix has no trigger
- **Address:** flow-steps [probe] `probe.trigger`
- **Class:** K6
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `cl-dClosedLoop-0408` owes a red-first `reproduction` probe before a patch build's fix when the build comes from a bug report. `probe.trigger`'s closed set has no arm for it, `probe.points` defaults to `none`, and `design.input` sends a patch straight to `design.unit-spec`.
- **Consequence:** Nothing opens the reproduction, so a patch fix lands without its red-first witness.
- **Fix:** Add the trigger "a patch build from a bug report" to `probe.trigger`, at the boundary before the patch's first `build.unit-pass`. Name it in `design.input`'s patch route.
- **Skeptic:** Confirmed medium.

### Place 137: flow-steps · review.fold · worst medium

#### B4-F3 — The breakpoint program has no route for a CEILING or NON-CONVERGENT round
- **Address:** flow-steps [breakpoint] `review.fold`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S6
- **Defect:** Neither `review.fold` nor `review.dispose` has a CEILING or NON-CONVERGENT outcome. The [breakpoint] policy list leaves out `review.max-rounds` and `flow.rework-budget`. [rules] sends open work only to asks, where `cl-dClosedLoop-0117` sends it to units while budget remains.
- **Consequence:** The item table that the static check reads has no outcome for the round refused past the limit.
- **Fix:** Give `review.fold` and `review.dispose` the outcomes CEILING and NON-CONVERGENT, routed to promotion: units while budget remains, asks after. Add the two keys to the [breakpoint] policy list.
- **Skeptic:** Confirmed medium. Rounds count against `flow.route-backs`, past which [rules] ends the loop non-converging, so a terminal is reachable without B4-F2 and c2 does not hold.

### Place 138: flow-steps · test.exit · worst medium

#### B3-F13 — `test.exit` writes to a lease record that dWitnessedBar's parents don't build
- **Address:** flow-steps [test] `test.exit`; architecture-v2 [chain] dWitnessedBar row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `test.exit` records "the verified tree on the build's lease record". The lease kind is dPlacedRequest's. dWitnessedBar's only parent is dDeclaredLoop, and its row declares no stand-in.
- **Consequence:** dWitnessedBar's exit item writes into a record kind no ancestor provides.
- **Fix:** Declare a stand-in, for example the verified tree on the transition record until dPlacedRequest lands, or add dPlacedRequest to dWitnessedBar's parents.
- **Skeptic:** Confirmed medium.

### Place 139: flow-steps · test.flakes · worst medium

#### A5-F9 — `verdict.flakes`' one threshold is the release streak, yet `test.flakes` reads it as the hold threshold
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S6
- **What is wrong:** v2:1146 defines the threshold only as "three consecutive greens unless set", and `cl-dClosedLoop-0368` and `test.select` (flow-steps:294) use it to release a leg. `test.flakes` (flow-steps:298) holds "a leg past the threshold", and layer-memory:570 says the one threshold serves both the hold and its release.
- **Consequence:** No record says what is counted for the hold, or over what window, so the hold arm cannot be specced.
- **Fix:** Split the key into a hold threshold (flakes counted in a window) and a release threshold (consecutive greens), each with a default.
- **Skeptic:** Confirmed medium (batch 4).

#### BS1-F1 — `verdict.flakes` declares one threshold, which `test.select` reads as the release streak and `test.flakes` as the quarantine entry
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S1
- **Defect:** `verdict.flakes` declares one threshold. `test.select` reads it as the streak of consecutive greens that releases a held leg, and `test.flakes` as the point past which a leg is held. The only default declared anywhere is the release streak of three greens.
- **Consequence:** Under the default `quarantine`, nothing says how many flakes put a leg in quarantine. Whether a flaky leg blocks an attended build is undefined.
- **Fix:** Split the key into an entry threshold (flakes per window, with a default) and the release streak (three consecutive greens), each with its own seen-red on `cl-dClosedLoop-0346`.
- **Skeptic:** Raised by skeptic batch 1 at `test.flakes` S1, where walker 3 gave `holds`. No second skeptic tested it.

### Place 140: flow-steps · test.merge · worst medium

#### A5-F8 — A landing conflict sends the build to a resolution pass that Build does not declare
- **Address:** flow-steps [test] `test.merge`; flow-steps [build]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **What is wrong:** `test.merge` sends a conflict "→ Build for a resolution pass", and [transitions] has "testing | a fix pass, or a conflict to resolve | building". [build] enters only "when every unit is READY", and none of its items is a resolution pass. flow-interactions' settlement ("a recorded resolution pass in the units it touches") is carried into no item, and [rules] (40-41) leaves unclear whether the pass draws on the budget.
- **Consequence:** A conflict caused by another build's landing is resolved by an undeclared actor. Re-entering Build re-runs `build.recommend` and the owed closing review, which can spend budget that contention must not touch.
- **Fix:** Declare a `build.resolve` item with its actor (the builder, or the architect when an interface clashes), its witness and its re-entry into Test. Mark its passes and any re-review as contention that draws nothing.
- **Skeptic:** Confirmed medium (batch 4).

### Place 141: flow-steps · test.route · worst medium

#### B3-F7 — `test.route` sends a non-blocking MIXED red two ways
- **Address:** flow-steps [test] `test.route`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The arm "an OWN or MIXED red → `test.attribute`" has no blocking condition, and "a red that does not block → an ask" also applies. Under the default `verdict.blocks: own-only` MIXED does not block, so a MIXED red matches both arms.
- **Consequence:** A spec writer cannot tell whether a MIXED red goes to the tester and a fix pass, or to an ask that lets the landing go ahead.
- **Fix:** Write the arm as "an OWN red, or a MIXED red where `verdict.blocks` blocks it → `test.attribute`".
- **Skeptic:** Confirmed medium. layer-flow [settled] routes MIXED to an ask when it does not block.

### Place 171: flow-steps · [revised] · worst low

#### A4-F19 — flow-steps `[revised]` names the retired key spelling `policy.on-missing-expansion`
- **Address:** flow-steps [revised]
- **Class:** K4
- **Severity:** low
- **Scenario:** S7
- **What is wrong:** flow-steps:767-768 reads "`policy.on-missing-expansion` (`[consequences]`)". The key is `policy-file.on-missing-expansion` (v2:1141; flow-roles-adoption [renamed]:436), and [consequences] itself uses the new spelling.
- **Consequence:** It is a dead pointer inside a dated revision note, which a reader inventory by value misses.
- **Fix:** Rename the key, with a dated note.
- **Skeptic:** Confirmed low (batch 3).

### Place 172: flow-steps · [rules] · worst low

#### A3-F16 — A post to a closed mailbox recreates a ref no one reads or prunes
- **Address:** flow-steps [rules] "Closing a mailbox"
- **Class:** K10
- **Severity:** low
- **Scenario:** S5
- **What is wrong:** The [rules] prune (flow-steps:55-59) declares no refusal of a post to a closed build. Refs are per writing session (`refs/gov/mail/<slug>/<fleet tag>/<session>`, coordination:103, memory-plan:240), and Maintain prunes a closed build's ref only "once its folder holds every message" (coordination:121).
- **Consequence:** Y's later question to withdrawn X lands on an orphan ref that nothing reads or prunes. Only `cl-dClosedLoop-0162`'s default answer ends Y's wait.
- **Fix:** Refuse a post whose slug carries a terminal transition, and answer the sender with that state.
- **Skeptic:** Confirmed low (batch 3). The finding's citation `cl-dClosedLoop-0141` is wrong, since that clause is the charter's preset section.

#### A5-F11 — Revision notes contradict the route they annotate
- **Address:** flow-steps [rules]; flow-steps [breakpoint] (the unverified-finding bullet under `review.unverified: block`)
- **Class:** K2
- **Severity:** low
- **Scenario:** S6
- **What is wrong:** [rules] (flow-steps:41-44) routes past `flow.route-backs` to asks, then notes "Revised 2026-10-19 by the owner's SL-1 and SL-2: the loop had become an owner item". [breakpoint] (flow-steps:494-498) says "filed as an ask … Revised …: it became an owner item". v2:1133 sends the open work to asks, so asks is the current route.
- **Consequence:** Read as what the revision did, each note says the opposite of its rule, and a reader cannot tell whether the route past the bound is an ask or an owner item.
- **Fix:** Reword each note to say what the route was before the revision, or drop it.
- **Skeptic:** Confirmed low (batch 4), as wording.

### Place 173: flow-steps · cl-dClosedLoop-0398 · worst low

#### A1-F10 — `design.ready`'s witness omits the UNCARRIED class that cl-0398 gives it
- **Address:** flow-steps [design] `design.ready`; architecture-v2 [chain] dIndexedDesign `cl-dClosedLoop-0398`
- **Class:** K1
- **Severity:** low (the walker graded it medium)
- **Scenario:** S1
- **What is wrong:** flow-steps:192 reads "derived READY: none MISSING, THIN or FORKED", while `cl-dClosedLoop-0398` has "`design.ready` gaining an UNCARRIED class" under `design.coverage` (default `refuse`).
- **Consequence:** The wording is stale. Both belong to dIndexedDesign, and the carries join reds an uncarried clause at its Design exit, so a spec writer cannot carry the item and drop the clause.
- **Fix:** Add "or UNCARRIED, under `design.coverage`" to `design.ready`'s witness.
- **Skeptic:** Confirmed low (batch 2), graded down from medium.

### Place 174: flow-steps · design.recommend · worst low

#### BS3-F4 — `design.recommend` does not declare whether it is idempotent or reconciles
- **Address:** flow-steps [design] `design.recommend`; [rules] (the command-item bullet)
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Defect:** [rules] says every command item declares whether it is idempotent or reconciles. The item's Actor cell says only "command", and most other command items have the same gap.
- **Consequence:** When node d's session limit hands the build over in S2, the successor cannot tell whether to re-score or to reconcile with the recommendation already written.
- **Fix:** Declare it on every command item, and add a check that reds a command Actor cell with neither word.
- **Skeptic:** Raised by skeptic batch 3 at `design.recommend` S2, where walker 2 gave `holds`. No second skeptic tested it.

### Place 175: flow-steps · design.streams · worst low

#### B2-F17 — `design.streams`' Needs reads as needing itself
- **Address:** flow-steps [design] `design.streams`
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Defect:** Needs reads "`design.overlaps`, where `design.streams` holds for the build". Short tags in the tables are item tags, so the cell names its own item.
- **Consequence:** The composer's acyclic-needs check reds gov's own item, or a reader skips it.
- **Fix:** Write the condition as `policy.design.streams`, the full spelling the opening reserves, outside the Needs tags.
- **Skeptic:** Confirmed low, a wording fix.

### Place 176: flow-steps · entry.orient · worst low

#### B1-F11 — `entry.orient` hard-codes `kickoff.runs`' default
- **Address:** flow-steps [entry] `entry.orient`
- **Class:** K4
- **Severity:** low
- **Scenario:** S1
- **Defect:** The Does cell runs "the full kickoff's where no READY card exists", which hard-codes `no-ready-card`. `cl-dClosedLoop-0376` says "only where `kickoff.runs` says", and neither [entry]'s nor [plan]'s policy list names the key.
- **Consequence:** `every-session`, `opening-a-build` and `plan-absorbs` have no effect.
- **Fix:** Write "as `kickoff.runs` says", and add the key to [entry]'s policy list.
- **Skeptic:** Confirmed low.

### Place 177: flow-steps · review.cost · worst low

#### B4-F12 — `review.cost` writes shape fields before the shapes registry exists
- **Address:** flow-steps [breakpoint] `review.cost`
- **Class:** K7
- **Severity:** low
- **Scenario:** S7
- **Defect:** `review.cost` is dDeclaredLoop's, but it writes `shape`, `efforts` and `role-sha` into the shape-run kind, which is dTotalRecall's, and its `shape` comes from the registry dBoundRoles builds. No stand-in is declared.
- **Consequence:** From dDeclaredLoop until dBoundRoles lands, the item writes fields that have no source.
- **Fix:** State a stand-in (shape and role-sha left blank until dBoundRoles), or move the extension onto dBoundRoles.
- **Skeptic:** Confirmed low. Today's `renderShapeLine` has neither field.

# Fold return: writer 4, flow-steps

**Serves:** research PLAY-dClosedLoop-1

Dispatch 201's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-42-spec-writer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

1. **Dispositions**

Some places carry findings that need different handling. Each such place gets the disposition of the edit it receives, and the evidence column says where its other findings went.

| # | place | disposition | findings | evidence or the fold's one-line gist |
|---|---|---|---|---|
| 15 | flow-steps · [transitions] | fold | A5-F1, B4-F2 | Adds a `parked` state, entered by the silence, park-build and park-for-owner rows and left by the owner's disposition. Adds a `closed-incomplete` terminal, adds it to the terminal set, and plants a budget spent in planning. A5-F1's descope back-row goes to FK-4-13. |
| 16 | flow-steps · build.recommend | fold | AS1-F1, B2-F2, B2-F18 | The reuse check's clean outcome now routes to `build.recommend`. Its Needs become "`build.reuse-check`, witnessed clean for every unit in the roster". A lap whose units came from a closing review goes to that review's follow-up as `review.follow-up` says, never to a fresh review. |
| 17 | flow-steps · cl-dClosedLoop-0100 | fork | A3-F10 | FK-4-3 covers what `adopt-parent-work` and `withdraw-too` mean. The `replan` route and its rows back to planning are folded at place 130. |
| 18 | flow-steps · cl-dClosedLoop-0207 | fork | A1-F4 | FK-4-1. |
| 19 | flow-steps · cl-dClosedLoop-0423 | fold | B3-F2 | `deploy.close` needs the patch build's `deploy.core` green for a SHA that contains the landed one, or a `core.exceptions` exception. Deploy's Exits and the deploying → landed witness say the same. |
| 20 | flow-steps · deploy.core | fold | A3-F1 | A red now routes to `deploy.record`, with the landing recorded red and the patch intake's key in the landing record. The close's Needs carry that patch's green. |
| 21 | flow-steps · deploy.mandate | fold | AS4-F1, B3-F11 (B3-F4 → FK-4-2) | Under `plan-only` the mandate is the plan's ratification. For a planned build that is `plan.exit`'s witness. For a patch or repeat build it is the derived plan record, ratified as `patch.ratify` says. The intake-record witness is gone. |
| 22 | flow-steps · design.overlaps | fold | B2-F3 | `design.overlaps` gets one route per value of `design.overlap`, with `refuse` going back to `design.decompose`. `design.ready` gets one arm per value of `design.handoff`, using the meanings settled in walkthrough D1 and D2. The clause half is a request. |
| 23 | flow-steps · entry.claim | fold | A3-F3, A3-F13, A5-F3, A5-F6, B1-F5 (A4-F14 → FK-4-9) | `entry.claim` writes the derived plan record and reads `patch.ratify`. Lease refusals route by their cause ([rules]), and claim retries draw on cl-0132's pre-claim budget. A landing's patch claim records the originating slug and SHA. A5-F6's `entry.claim` cell is plant P06; the working tree's flow-steps:86 already routes the unreachable remote. Its other cells are folded. |
| 24 | flow-steps · entry.intake | plant | A1-F1, A4-F2, B1-F1 | P08. flow-steps:81 reads "hook: prompt-submit, in an owner-bound session only" and "the hook-written intake entry". |
| 25 | flow-steps · life.request | fold | A3-F12 | A supersede must name a claimed replacement and is refused otherwise. `life.close` writes the `supersedes` relation (cl-0217). `life.unlease` keeps the branch. `design.input` sends a plan record that names a superseded build to `design.inventory` over that build's units. |
| 26 | flow-steps · plan.exit | plant | A1-F2, A4-F3, A5-F4, B1-F2 | P09. flow-steps:140 reads "the intake record stands as the ratification". cl-0378's fallback joins at place 124. |
| 27 | flow-steps · plan.record | fork | BS3-F1 (BS3-F3 duplicates place 15) | FK-4-1. BS3-F3's spent-in-planning case is folded at place 15. |
| 28 | flow-steps · review.dispose | fold | A1-F6, A5-F7, B4-F4 | New building → designing row for a finding unit. Build's tail waits for those units, with a plant. One arm per pinned artifact. `review.trigger` refuses a round past `review.max-rounds` (CEILING). NON-CONVERGENT and CEILING findings are promoted as cl-0117 says. Both keys join the policy list. |
| 29 | flow-steps · review.trigger | fork | A1-F5 | FK-4-4. |
| 30 | flow-steps · test.seen-red | fork | AS4-F3 | FK-4-12. |
| 37 | flow-steps · design.input | fold | A3-F20, B2-F20, B2-F5 | Patch, finding and fix inputs now pass through `design.overlaps` for their unit. B2-F5 is the same defect as place 25 and is folded jointly there. |
| 38 | flow-steps · design.ready | fold | A1-F7, B2-F1, B2-F19 | `design.ready`, `build.ratify`, `build.distill`, `test.exit` and `deploy.notify` now need the reason item, plus the breakpoint's `review.dispose` where they routed to one. READY gains UNCARRIED under `design.coverage`. |
| 41 | flow-steps · review.pin | fold | B4-F11 (AS4-F2 duplicates place 28) | [breakpoint] now declares its interim parts, as [probe] does: the record kind read from the filename, disposal by hand until dDeclaredLoop, and blank shape fields. |
| 114 | flow-steps · [adopt] | fold | B5-F15 | Adds `adopt.instructions` (cl-0260) and `adopt.declarations` (cl-0438) rows, each with its owner, Needs, witness and an owner-item ruling. |
| 115 | flow-steps · [breakpoint] | fork | B4-F13 | FK-4-1. |
| 116 | flow-steps · [lifecycle] | duplicate | B4-F6 | Same defect as place 25 (B2-F5's twin), folded there. |
| 117 | flow-steps · adopt.decisions | fold | A4-F15, B5-F8 (disagreement → FK-4-6) | Split into the raters' `adopt.decisions` and the owner's `adopt.decisions-ratify`. A kappa below 0.8 sends the rubric for revision and a re-rating (research-retrofit-a:185). |
| 118 | flow-steps · build.acceptance | fold | B2-F6 (A5-F2 → FK-4-5) | Declares `build.fix-pass` (with M16's narrowed allowance) and `build.revert-pass`. Every "fix pass" and "revert pass" route now names them. |
| 119 | flow-steps · build.reuse-check | duplicate | A1-F8 | Same as place 16. |
| 120 | flow-steps · build.unit-lease | fold | B2-F8 | One instance per unit. Needs: `build.base` plus the reuse check of each unit ordered before it. |
| 121 | flow-steps · cl-dClosedLoop-0116 | fold | A3-F7 | The close's wait raises an owner item past `flow.wait-ceiling`, or once the patch build ends without a green. The item offers an exception or a budget raise. |
| 122 | flow-steps · cl-dClosedLoop-0282 | plant | C4-F4 | P08, as place 24. |
| 123 | flow-steps · cl-dClosedLoop-0319 | fold | AS4-F4 | Adds a `unit` disposition to `entry.place`, routed as `build.unit-holders` says (cl-0319). |
| 124 | flow-steps · cl-dClosedLoop-0377 | fold | BS2-F1 | New [plan] interim bullet: until the hook lands, `plan.input` pins `entry.orient`'s record that the intake is absent, as cl-0378 does for `plan.exit`. |
| 125 | flow-steps · cl-dClosedLoop-0422 | fold | B3-F10 (A2-F9 → FK-4-7) | `deploy.land` pushes once the landing queue admits it, in `landing.order`'s order, with an arm for `owner-orders`. |
| 126 | flow-steps · cl-dClosedLoop-0440 | fold | A3-F5 (B3-F3 duplicates place 23) | `deploy.core` keys its patch intake by (`default-branch-red`, landed SHA), so `maintain.patch` finds it. |
| 127 | flow-steps · deploy.distill | fork | B3-F12 | FK-4-8. |
| 128 | flow-steps · deploy.notify | fold | B3-F9 | New [rules] bullet: an unreachable remote is contention, retried as `stale-remote` is and bounded by `leases.expiry-hours`. `deploy.land` cites it. |
| 129 | flow-steps · deploy.parents | fold | A2-F4, A3-F11, B3-F5 | The hold becomes a wait within `flow.wait-ceiling`, then follows `deps.on-parent-withdrawn` (stall-and-loop point 6). The key joins Deploy's policy list. |
| 130 | flow-steps · design.decompose | fold | B2-F9 (+ A3-F10's replan half) | A parent's `withdrawn` post read at any item boundary routes as the key says; `replan` goes back to planning by a plan revision, with its transition row. The key joins Design's and Build's policy lists. |
| 131 | flow-steps · entry.place | fork | B1-F8 | FK-4-9. |
| 132 | flow-steps · life.quiesce | fold | A3-F15, B4-F8, A3-F19, B4-F7 (B4-F5 → FK-4-10) | Quiesce messages every unit holder and waits per unit lease. A review fan's findings go to asks or to the replacement. "pause → paused". "Once the landing push to the default branch is made". |
| 133 | flow-steps · plan.dedupe | fold | B1-F9 | Interim bullet: dedupe checks live builds and open asks only until dIndexedDesign lands. |
| 134 | flow-steps · plan.lease | fold | A1-F11, A4-F20 | The overlap routes by `leases` (warn → as held; refuse → as a live holder), with `leases.overlap` cited as the granularity, through the [rules] bullet. |
| 135 | flow-steps · probe.judge | fold | B4-F9 | `probe.judge` stays a command. A new `probe.judge-claimed` (tester) takes what no command can judge. |
| 136 | flow-steps · probe.trigger | fold | B4-F10 | Trigger added: a patch build from a bug report gets its reproduction before the first `build.unit-pass` (cl-0408). It is named in `design.input`'s patch route. |
| 137 | flow-steps · review.fold | duplicate | B4-F3 | Same as place 28 (A5-F7), folded there, including `review.fold`'s promotion arm. |
| 138 | flow-steps · test.exit | fold | B3-F13 | Until dPlacedRequest lands the lease kind, the verified tree goes on the transition record. |
| 139 | flow-steps · test.flakes | fork | A5-F9, BS1-F1 | FK-4-11. |
| 140 | flow-steps · test.merge | fold | A5-F8 | Declares `build.resolve` (builder; contention draws nothing), with building ⇄ testing rows and Build's Enters line. |
| 141 | flow-steps · test.route | fold | B3-F7 | "an OWN red, or a MIXED red that `verdict.blocks` blocks"; `test.attribute`'s Needs match. |
| 171 | flow-steps · [revised] | fold | A4-F19 | Renamed to `policy-file.on-missing-expansion` with a dated note (also in the `presets-fail-build-closes` row). |
| 172 | flow-steps · [rules] | fold | A3-F16, A5-F11 | A post to a build that has ended is refused, and the sender is told its state. Both revision notes now read "before it, …". |
| 173 | flow-steps · cl-dClosedLoop-0398 | duplicate | A1-F10 | Same as place 38 (B2-F19), folded there. |
| 174 | flow-steps · design.recommend | fold | BS3-F4 | [rules]: a command item that declares neither is idempotent by its witness (cl-0092). |
| 175 | flow-steps · design.streams | fold | B2-F17 | The condition is written `policy.design.streams`, both in `design.streams`' Needs and in `design.overlaps`' route. |
| 176 | flow-steps · entry.orient | fold | B1-F11 | "as `kickoff.runs` says"; the key joins [entry]'s policy list. |
| 177 | flow-steps · review.cost | fold | B4-F12 | Interim: `shape` and `role-sha` are written blank, and the fields ride the `review-shape` line (in the [breakpoint] bullet). |

Totals: 38 fold, 9 fork, 3 plant, 4 duplicate.

2. **Fold script:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w4/fold-4.py`
   - It makes **76 edits**, all in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, and nothing in any other record.
   - It ends with a "Revised 2026-10-20 by the whole-design audit's fold" paragraph in [revised] that lists the finding ids.
   - I dry-ran it on a copy of the file at `8222099f8`, which is byte-identical to the working tree's LF copy. All 76 anchors matched exactly once. After the fold, every item-table row has 7 cells and every transition row has 4. The dry copy has been deleted.
   - It writes 7 new items (`build.fix-pass`, `build.revert-pass`, `build.resolve`, `probe.judge-claimed`, `adopt.decisions-ratify`, `adopt.instructions`, `adopt.declarations`) and no clause ids.
   - My scratch folder also holds `cl.py`, a reader I used to pull clause texts out of v2.

3. **Forks**

### FK-4-1 — Does `run.on-owner-question` decide an owner item that attendance raises when it is raised, and where does a late answer go?
- **Options:**
  - (A) While the owner attends, a confirm-steps or confirm-acts gate, or a live question, is held until `run.owner-deadline`. After that `run.on-owner-silence` applies, and `run.on-owner-question` decides only unattended items.
  - (B) Attendance's gates are declared outside `run.on-owner-question` and are always held for the owner, as a ratification is.
  - (C) Keep the decision at raise, and name `flow.wait-ceiling` as cl-0207's wait.
  - For a late answer:
    - (i) `entry.place` places it as an amendment that re-enters the item it answers, drawing on `flow.rework-budget`; the amendment row gains `planning`.
    - (ii) It is recorded with no effect.
- **Recommendation:** (A) with (i). It keeps attendance's promise and reuses the existing amendment route. B4-F13's refuting skeptic already reads a late answer as going through `entry.place`, and BS3-F1 shows that route has no planning arm.
- **Rests on:** A1-F4, BS3-F1, B4-F13.

### FK-4-2 — Can `best-effort-recorded` fill the owner's landing gate and design go under `three-gates` and `every-stage`?
- **Options:**
  - (A) Yes, as LR-3 reads today, where only ratifications are excluded.
  - (B) Extend LR-3's exclusion to every gate `autonomy` places, so they are held for the owner as ratifications are.
  - (C) A preset pair rule that refuses `three-gates` or `every-stage` together with `best-effort-recorded`.
- **Recommendation:** (B). An `autonomy` gate exists only to get the owner's word. This narrows the owner's own LR-3 answer, so it is the owner's call.
- **Rests on:** B3-F4, where the first skeptic refuted it and the second confirmed it.

### FK-4-3 — What do `deps.on-parent-withdrawn: adopt-parent-work` and `withdraw-too` do?
- **Options:**
  - (A) `adopt-parent-work`: Y's plan revision takes in X's kept units through Y's `design.inventory` at X's kept branch tip, as a supersession does. `withdraw-too`: an owner item that proposes Y's withdrawal.
  - (B) As A3-F10's fix: `withdraw-too` runs `life.request` with a command as its actor.
  - (C) Retire the two values, since every preset sets `replan`.
- **Recommendation:** (A). A withdrawal is the owner's control, so a command should never act it. (C) is the YAGNI alternative.
- **Rests on:** A3-F10.

### FK-4-4 — How does an owner's mid-build "audit the specs" reach `review.trigger`?
- **Options:**
  - (A) A `breakpoint` disposition in `entry.place`'s closed set that names the live build. Its witness is the intake record plus the placement disposition, so no new kind is needed.
  - (B) A `review` verb on `life.request` through the guarded command.
  - (C) Register an "owner request record" kind with a writer in layer-memory.
- **Recommendation:** (A). The owner types it as a prompt, and both witnesses already exist. `review.trigger`'s "owner's request record" would then read "the placement disposition naming the breakpoint".
- **Rests on:** A1-F5.

### FK-4-5 — Where does a loop's open work go past `flow.route-backs`, and which bound wins against `review.max-rounds`?
- **Options:**
  - (A) To asks, as [rules] and v2:1133 say today.
  - (B) As cl-0117 and stall-and-loop point 4 say: a blocking item's open work becomes a new unit while budget remains, then goes to `flow.on-exhausted`; a non-blocking item's goes to asks.
  - (C) Straight to `flow.on-exhausted`.
  - On the bounds: the first of `flow.route-backs` and `review.max-rounds` that a review loop reaches ends it, and both promote the same way.
- **Recommendation:** (B), plus that ordering. Under (A) a blocking unit can never be built, so Build's exit stalls into `stuck`.
- **Rests on:** A5-F2, and A5-F7's "order the two bounds".

### FK-4-6 — What happens to a decision candidate the two raters disagree on?
- **Options:**
  - (A) It stays `reconstructed` and not major, and goes to `adopt.decisions-ratify` only under `docs-owner-ratifies` or `docs-and-trailers`.
  - (B) A third rater decides it.
  - (C) Always an owner item.
- **Recommendation:** (A). RF-3's default `author-rubric` puts nothing on the owner.
- **Rests on:** B5-F8.

### FK-4-7 — Does `landing.order` order landings across nodes?
- **Options:**
  - (A) Yes: a compare-and-swap landing-turn ref on the remote, built with `gap-flow-08`'s queue.
  - (B) Narrow P21 and `landing.order` to one node, record the cross-node order as first-pushed, and say so.
- **Recommendation:** (A). P40 puts concurrent nodes in scope, and P21's plan priority otherwise does nothing across them.
- **Rests on:** A2-F9.

### FK-4-8 — What does `deploy.distill` do before dScopedBuild's `build.distill` writes any rows?
- **Options:**
  - (A) Add dScopedBuild to dShippedRelease's parents, a move that changes the critical path.
  - (B) Report "measured nothing" and never pass, which blocks every landing meanwhile.
  - (C) Unarmed: record "measured nothing", never green, and route on, with the landing record saying so, as `test.seed`'s unarmed seed does.
- **Recommendation:** (C).
- **Rests on:** B3-F12.

### FK-4-9 — Where are the interim stand-ins for routes into later builds declared?
- **Options:**
  - (A) One [rules] bullet: until an item's owning build lands, a route into it reaches today's stand-in (the attended session's agent for a role item, today's tool for a command, `push-main.sh` for the lander). Plus one tolerance row per forward route in recut's [reconciled-order].
  - (B) Tolerance rows only.
  - (C) Moves, by adding parents.
- **Recommendation:** (A) with the rows. The 21 routes come from Stage 0's list, which is not committed, so the main loop would supply them.
- **Rests on:** A4-F14, B1-F8.

### FK-4-10 — What is a paused build's deadline, and what happens when it passes?
- **Options:**
  - (A) A declared wait within `flow.wait-ceiling`, then an owner item to resume, withdraw or stay paused. If that item goes unanswered at `run.owner-deadline`, the build is parked and its lease released.
  - (B) Its own key, such as a `life.pause-ceiling`.
  - (C) Exempt the owner's pause from P39 explicitly.
- **Recommendation:** (A). It satisfies `leases.renewal: progress` and P39 point 6 with existing keys.
- **Rests on:** B4-F5.

### FK-4-11 — What enters a leg into quarantine under `verdict.flakes`?
- **Options:**
  - (A) Split the key into an entry threshold (flakes in a window, defaulting to "measured" and to 2 in the leg's last 10 verdicts until measured) and the release streak of 3 greens.
  - (B) Hold on the first nondeterministic run and keep one threshold for release.
- **Recommendation:** (A). Its default cannot be derived from the records, so the owner sets or confirms it.
- **Rests on:** A5-F9, BS1-F1.

### FK-4-12 — Who writes the seen-red record?
- **Options:**
  - (A) The executor at `build.acceptance`, when it runs a gate against its plant. That item is dScopedBuild's, which lands after dWitnessedBar, so it needs a stand-in.
  - (B) `test.seen-red` becomes a command that runs each added or changed gate against its declared plant and writes the record from what it sees. That is a computed witness under [rules], and layer-memory:425 stays right.
  - (C) The bar's runner runs the plants.
- **Recommendation:** (B). It needs no forward dependency and no self-typed witness.
- **Rests on:** AS4-F3.

### FK-4-13 — How does a best-effort descope remove a failing unit that is already in Test's tree?
- **Options:**
  - (A) A testing → building row for a revert that draws nothing, being an ending and not a lap.
  - (B) No descope in Test: there, best effort either lands what is green or closes incomplete. A descope in Build moves no state, which is now folded.
  - (C) A revert pass that draws on the spent budget.
- **Recommendation:** (B).
- **Rests on:** A5-F1's "give a descoped unit a row back from building or testing".

4. **Requests**

None of these are in my script; each needs its record's writer.

- **architecture-v2 `[chain]` dDeclaredLoop (writer 1):**
  - `cl-dClosedLoop-0100`: append ", `replan` read at every item boundary where a parent's `withdrawn` post is read and routed by a plan revision back to planning, seen red on a planted withdrawn parent read in Design". Serves places 130 and 17.
  - `cl-dClosedLoop-0117`: after "never folded into another round", insert ", a CEILING round's open findings promoted the same way". Serves place 28.
- **architecture-v2 `[chain]` dPlacedRequest (writer 1):** add one new clause with the next free id: "`entry.claim` writing a patch or repeat build's derived plan record, the patch's ratified as `patch.ratify` says, `owner` holding it as an owner item, and a lease or claim refusal routed by its cause (a terminal tombstone, a terminal build or an epoch fence refused, a live holder waited for as contention within `flow.wait-ceiling`, an overlap as `leases` says), seen red on a planted patch under `owner` reaching Design unratified and on a replayed take against a tombstone under `leases: warn`". Serves place 23.
- **architecture-v2 `[chain]` dShippedRelease (writer 3):**
  - `cl-dClosedLoop-0423`: replace "so a core red the landing merge introduced stops that build from closing (foundations K1)" with "so a core red the landing merge introduced stops that build from closing until a patch build's core checks are green for a SHA that contains the landed one or an exception under `core.exceptions` is recorded, the landing recorded red meanwhile, seen red on a planted red landing whose patch is filed and not yet green (foundations K1)". Serves places 19, 20 and 121.
  - `cl-dClosedLoop-0440`: after "a patch build raised by a landing", insert ", or a Maintain patch whose offender is a landed SHA, its intake keyed by (`default-branch-red`, landed SHA) so one red files one patch,". Append to its seen-red list: "and on a planted double filing of one red". Serves place 126.
  - `cl-dClosedLoop-0422`: replace with "landings ordered through the landing queue it builds (`gap-flow-08`), reading `landing.order` with an arm per value, seen red on a planted `owner-orders` landing admitted with no order". Serves place 125.
- **architecture-v2 `[chain]` dIndexedDesign (writer 3):**
  - `cl-dClosedLoop-0383`: "the derived-READY hand-off, as `design.handoff` says, an arm per value, seen red on a planted `ready-plus-audit` hand-off with no audit".
  - `cl-dClosedLoop-0384`: "the design index, its overlap check acting as `design.overlap` says, seen red on a planted unacknowledged overlap under `refuse`".
  - Both serve place 22.
- **layer-roles, the actor matrix and its counts:**
  - Add to builder: `build.fix-pass`, `build.revert-pass`, `build.resolve`. Add to tester: `probe.judge-claimed`. Add to owner: `adopt.decisions-ratify`. Add to command: `adopt.instructions`, `adopt.declarations`.
  - Change "81 items … 20 items with a role" to "88 items … 24 items with a role".
  - Serves places 114, 117, 118, 135 and 140.
- **orientation (`2026-10-14-…-orientation.md`, the "Checked" and disposition bullets near :148-155):** add `unit <build>/<unit>` to the dispositions, with the check "the build is live, the unit ready and unleased, and `build.unit-holders` admits this session". Serves place 123.
- **layer-expansions, the `maintain.patch` row (:225):** Does gains "unless a patch is open for the same key: a landing's `deploy.core` files its red's patch under (`default-branch-red`, landed SHA), which this item finds and opens none for". Serves place 126.

5. **Read outside the list above:** none. I read only design records under `memory/builds/dClosedLoop/build/` (including the round record's `[recall-scored]` and this build's committed scripts) and `tools/memory-tree/gen_build_index.py`. I opened nothing in the scratchpad's copies of the design records, and nothing from the sealed copy.

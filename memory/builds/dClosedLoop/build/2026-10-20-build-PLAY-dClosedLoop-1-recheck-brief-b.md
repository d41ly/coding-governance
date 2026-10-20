# Second-look brief: run B

**Serves:** research PLAY-dClosedLoop-1

**Your task is to judge each finding below: confirm it or refute it.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one
line at the end of your return, and nowhere else.

Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Grade a confirmed one by the copy's round record's
`[rubric]` (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-b/`.

Read nothing else: not the working tree's other records, not the walkers' returns or the reports, not the session's
scratchpad or temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it
alone, since the working tree may differ from it.

## Findings to judge

### B1-F6 — A queued claim replayed after a withdrawal "counts as claimed" through the own-key rule
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - "a retry that finds its own key counts as claimed".
  - `deploy.close` and `life.close` keep the claim ref ("never pruned").
  - `leases.queued-claim-days` (7) refuses only a stale fetch.
  - No check of the claim ref's terminal transition appears anywhere in the item.
- **Consequence:** In S5, a claim queued offline before withdrawal X replays within 7 days, finds its own key and routes "claimed → Plan" on a withdrawn slug. The engine has no withdrawn→planning row, so the run either refuses with no route or reopens a terminal build.
- **Fix:** The claimed route requires that the claim ref holds no terminal transition. Add a route for a terminal one: the replay is refused and recorded, and a fresh slug is minted only on a new request.

### B1-F7 — A refused lease and an unusable remote have no defined route at `entry.claim` or `plan.lease`
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - The routes say "the lease refused → as `leases` says". `leases` is "warn, refuse | warn". It is an overlap stance, and no record defines a refused acquisition under `warn` (probe: `grep -n 'as \`leases\` says'`).
  - `entry.claim` has no outcome for an unreachable remote or for a remote that refuses `refs/gov/claims/*`.
  - Today's run claim ships OFF for exactly that reason: `tools/unattended/.unattended.conf.example:163`, "turn it on once your remote accepts a push to `refs/gov/runs/<slug>`", and check 109.
- **Consequence:** In S6 a patch build whose lease is refused under the default goes into Design unleased (against P40), and a claim against a refusing remote has no outcome.
- **Fix:** Close both outcome sets: refused acquisition → wait or offer within `flow.wait-ceiling`, then an owner item; remote unreachable → as `leases.offline`; ref refused → a refusal naming the remote, then an owner item. Apply the same to `plan.lease`.

### B1-F8 — dPlacedRequest's entry routes and slug mint depend on builds that are not its ancestors, with no stand-in
- **Address:** flow-steps [entry] `entry.place`
- **Class:** K7, c1
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - `entry.place` routes new → Plan (dRankedPlan) and amend/patch → Design (dIndexedDesign).
  - `entry.claim` mints by `builds.slug-*` (dTotalRecall).
  - dPlacedRequest's only parent is dDeclaredLoop. Stage 0 leads: "dPlacedRequest→plan.input … not an ancestor, UNCLASSED".
  - v2:483 says "each new dependency on a later build gets a stand-in". Only `repeat` has one (`cl-dClosedLoop-0156`).
- **Consequence:** When dPlacedRequest lands, its acceptance cannot walk any disposition except `repeat` and `continue` to a witnessed next item, so its gates cannot be seen green end to end.
- **Fix:** Add stand-ins to dPlacedRequest's row:
  - new, amend and patch → today's unattended or kickoff route, recorded;
  - the slug mint → today's `check_slug_claimed` rules until dTotalRecall lands.

### B1-F12 — Two owners stated for the entry step's items
- **Address:** architecture-v2 [chain]-preamble revision note (PM-9)
- **Class:** K8
- **Severity:** low
- **Scenario:** S7
- **Evidence:** v2:401 says "the entry step's items are dDeclaredLoop's (PM-9)". `cl-dClosedLoop-0122` (dPlacedRequest) and flow-steps' Owner column (SP-1) say dPlacedRequest.
- **Consequence:** A spec writer reads two owners.
- **Fix:** Mark the v2 note as superseded by SP-1.

### B2-F4 — The per-unit budget share has no single freeze point, so each Design re-entry can mint budget
- **Address:** architecture-v2 [policies] `flow.rework-budget`; flow-steps [design] `design.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** v2 [policies]: "a base plus a count per unit frozen at Design's exit … 4+2". flow-steps [build]: closing-review findings "become new units … and those units pass through Design and back". So `design.exit` runs again on every lap. stall-and-loop [design] 1 says only "units a loop mints cannot reset it".
- **Consequence:** If the share is re-frozen at each `design.exit`, every closing-review finding (S1) and every patch build's Design (S3, which shares the originating budget) adds 2 to the budget it draws on. The P39 bound grows with the loop it is meant to stop.
- **Fix:** State that the shares freeze once, at the first `design.exit` the build records, and that units minted later carry no share. Seen red on a planted closing review whose finding-units raise the remaining budget on the card.

### B2-F7 — A cross-node unit has no workspace or integration rule under the default `build.worktree: shared`
- **Address:** layer-runtime [isolate]; flow-steps [build] `build.unit-pass`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2 [policies]: "`build.worktree` | per-unit, parallel-only, shared | shared". [isolate]: "shared: the build's one worktree … The commit queue then commits them one at a time". "Integration before release" is stated for unit branches only. cloud-and-scale [design] 8: any node picks "ready, unleased units" across builds.
- **Consequence:** Node x takes one of X's units by lease, but under the default the unit's worktree and commit queue live on node d. Nothing says where x commits, how its pass reaches the build branch, or what the fence covers. The unit can never integrate, or it integrates outside the queue.
- **Fix:** A unit leased from another node always gets a unit branch, as under `per-unit`, whatever `build.worktree` says, integrated by the build lease's holder before the unit lease is released. Seen on a two-clone fixture.

### B2-F13 — `cl-dClosedLoop-0407` places `drop_touched_exemptions` in `tools/lib`, but it lives in the map kit
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0407`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** 0407: "calling the pure `drop_touched_exemptions` in `tools/lib`, … the claim arm 'not installed' where the map is absent, seen on a planted core-only tree". Probe: `grep -rn drop_touched_exemptions tools --include=*.py` printed only `tools/codebase-map/map_lib.py:1373:def drop_touched_exemptions(...)` and its two callers in `tools/codebase-map/`.
- **Consequence:** On an adopter's core-only install, `build.scope`'s one check imports a function from a kit that is absent. Either the build imports from the map kit and the touch join fails on that tree, or the clause hides a move into `tools/lib`, which copy-installed kits carry inline, with no unit owning that move.
- **Fix:** Name the move (`drop_touched_exemptions` out of `map_lib.py` into `tools/lib`, with its readers re-pointed in the same unit) as a dScopedBuild clause, or cite its real home and make the touch arm "not installed" when the map is absent.

### B2-F15 — No clause enforces P18's ranking of a fork's options
- **Address:** architecture-v2 [enforcement] `P18` / [chain] `cl-dClosedLoop-0176`, `cl-dClosedLoop-0390`
- **Class:** K5, c5
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** P18: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record". 0176: "every fork resolved by the role that meets it and recorded". 0390: "fork resolution by `design.forks`". The ranking appears only in the default value's name, `agents-feature-rich-expandable`. (I disclosed above that this was also a lead in the record I should not have read.)
- **Consequence:** In unattended S2, a fork record that carries no ranked options passes every join, so P18 is unenforced.
- **Fix:** Have 0176 require the fork record to list its options ranked by feature-richness, then expandability, with the chosen one first, and a schema check that reds a resolved fork without the ranking.

### B3-F4 — The owner's landing gate can be passed by the supervisor's own choice
- **Address:** flow-steps [deploy] `deploy.mandate`; flow-steps [breakpoint]; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** `deploy.mandate` checks, "under `three-gates` and `every-stage`, the disposition of the owner's landing gate". [breakpoint]: an owner breakpoint is resolved by `run.on-owner-question` "when it is raised, never for a ratification ... the supervisor's recorded choice under `best-effort-recorded`". The witness list includes "under `best-effort-recorded`, the supervisor's recorded choice". `best-effort-recorded` is the default, and it is the `run.on-owner-question` value in every preset except strict (park-item).
- **Consequence:** An owner who sets `autonomy: three-gates` to gate landings gets a gate the supervisor fills in as soon as it is raised. `deploy.mandate` then certifies an owner mandate that the acting side typed, which breaks P2.
- **Fix:** Treat the design go and the landing gate like ratifications: `run.on-owner-question` and `apply-recommendation` never decide them. Make `deploy.mandate` refuse a gate witness that is not an owner disposition. Seed a red case: a planted `best-effort-recorded` choice offered as the gate's witness.

### B3-F8 — Several Test and Deploy outcomes end at an ask, leaving the build with no next step
- **Address:** flow-steps [test] `test.merge`; flow-steps [deploy] `deploy.land`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `test.merge`: "refused → an ask naming the lander's refusal". `deploy.land`: "or an ask for a carried commit"; "an argument → an ask on the adapter". Memory [asks]' acceptance for a lander refusal is "`--prepare` next succeeds for the build", but no item routes back to `--prepare`, and [transitions] has no row for these cases.
- **Consequence:** The build sits in `testing` or `deploying`. It has no next item, no wait deadline and no owner item, against P39's "every wait expires".
- **Fix:** Route each of these to a counted wait on the ask's acceptance that re-enters `test.merge`. Past `flow.wait-ceiling`, raise an owner item. Add the transitions rows.

### B4-F13 — An owner's late answer after the deadline has no route
- **Address:** flow-steps [breakpoint]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - [breakpoint] lists the witness "under `run.on-owner-silence: apply-recommendation`, the item's recommended option applied past the deadline". `confirm-steps` "adds a gate at every step's exit".
  - The v2 `run.on-owner-silence` default is `apply-recommendation`.
  - No clause says what an owner disposition arriving after that does.
- **Consequence:** In S1 the attended owner's late "no" on a step confirmation lands after the build has moved on. It is not refused, recorded or routed back.
- **Fix:** Declare a late disposition's outcome: recorded beside the applied one, and a contrary answer filed as an owner-raised amendment, or a route back drawing on the budget.

### B5-F7 — `kits.offer`'s pushed route files no order for the adopter's `test.seed` and `adopt` runs
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** The row reads "pushed → the adopter lands it with its own lander, whose bar runs the checks the offer left unrun; an update that needs target-side execution, or a refused push → an outbox order". v2 cl-dClosedLoop-0430 says the offer's "outbox order names the adopter's own run of both". retrofit [seed] says the order "names the adopter's own run of `test.seed`, which arms them".
- **Consequence:** On the ordinary pushed path no order is filed. The adopter's bar does not run `test.seed`, so the update's new checks stay unarmed indefinitely under the default `retrofit.unseeded: unarmed`.
- **Fix:** On `pushed`, also file the outbox order that names the adopter's `test.seed` and `adopt` runs, keyed by (adopter, release). Add that order to `test.seed`'s Needs.

### B5-F9 — Under the default `on-touch`, nothing reconstructs records
- **Address:** flow-steps [adopt] `adopt.reconstruct`
- **Class:** K8
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** "under the default `on-touch` it never runs, and `build.unit-pass` reconstructs on first touch". `build.unit-pass`'s Does and Proven-by cells say nothing about reconstruction, and no clause in v2 [chain] carries it: a search for `reconstruct|first touch|on-touch` finds only cl-0245. `build.unit-pass` is dScopedBuild's, which is no ancestor of dLinkedLibrary.
- **Consequence:** With the default setting, records for untouched code are never reconstructed by any build. The S7 bootstrap also leaves the duty with a non-ancestor.
- **Fix:** Add the on-touch reconstruction to `build.unit-pass`, or a new `build.reconstruct` item under `retrofit.reconstruct: on-touch`, with a clause on dScopedBuild's row or a descendant build's row and a seen-red fixture.

### B5-F12 — Cadence period keys come from each node's own clock
- **Address:** layer-runtime [schedule]
- **Class:** K10
- **Severity:** low
- **Scenario:** S2
- **Evidence:** "Each cadence instance is keyed by its period (ISO week or date)." Lease expiry uses "a declared clock" (cloud-and-scale `[4]`), but the period key names no clock, and layer-runtime records a node whose "clock runs 8 to 13 s slow".
- **Consequence:** Near a day or week boundary, node x with a skewed clock derives a different period key. Its check for an existing period witness finds nothing, so Maintain or the Loop Review runs twice and writes two records.
- **Fix:** Derive the period key from the declared clock, corrected by the node registry's offset, which is the same clock lease expiry uses.

### B5-F13 — An install or update trusts a mutable, unpinned tag name
- **Address:** layer-expansions [design-distribution] `kits.currency`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** "govkit installs by copy at a release tag, and the receipt names that release and the remote it came from". The receipt fields are "per-kit versions, the release tag, the source remote", with no commit. `kits.cut` "cuts the annotated tag", which is unsigned. Under `any-commit`, `kits.currency` "counts the release tags dated after the installed commit".
- **Consequence:** This is tampering at the adopter boundary. A tag moved on the source remote, or served by a mirror, installs other bytes under the same receipt, and `kits.currency` cannot tell. Under `any-commit`, tag dates from a skewed cutter miscount how far behind the adopter is.
- **Fix:** Record the tag's object and commit SHA in the receipt and the kit-release record, and have update refuse a tag whose commit differs from that record. Count releases behind by ancestry, not by date.

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-b/` only. Your effort is the one the owner's
role definition sets.

# Skeptic brief: run B, batch 1

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run B of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b1/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### B2-F11 — `cl-dClosedLoop-0002` reds two whole carriers only when they disagree
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K8, c3
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** 0002: "two specs carrying one clause whole and disagreeing … each red". The copy's carries.py, line 251: `ambiguous = [... if c[1] == "whole"]) > 1]`, which reds any second whole carrier. 0003's report lists "ambiguous counts".
- **Consequence:** A product join built from the clause passes two units that both carry one clause whole at the same pin. That is one clause built twice, which is the double ownership the coverage report exists to show.
- **Fix:** "two specs carrying one clause whole, or pinning it to two hashes, red", as the instrument reads.

### B2-F10 — `cl-dClosedLoop-0003` refuses every chain build's first spec
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0003`
- **Class:** K7, c1
- **Severity:** high
- **Scenario:** S7
- **Evidence:** 0003: "memory hygiene refusing a chain build's spec in progress while its build's coverage is red, seen red on a planted uncarried clause". The copy's carries.py docstring: "a clause or an owned node no spec carries (with --exit, as at a Design exit)" and "a run that measured no spec is never green".
- **Consequence:** While a build's specs are being written, every clause not yet carried is uncarried, so coverage is red, and before the first spec it is never green. Hygiene then refuses the spec in progress, and dTrueNorth's own Design (and every later chain build's) cannot commit its first spec.
- **Fix:** Refuse a spec in progress only on the per-spec arms (ghost, unbound, stale, ambiguous, dropped). Keep the uncarried and unowned-node arms for the Design exit only, as the instrument does, and seen-red the refusal on a planted ghost, not on an uncarried clause.

### B2-F16 — P19's one clause names no refusing check, and a deviation record admits a revision after a pass
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0400`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** [enforcement]: "`P19` | `cl-dClosedLoop-0400`". 0400: "built specs frozen …", with no check and no seen-red. 0004's population "each spec revision after its unit's first attributed pass commit" is joined to "a record whose approver meets its risk class", so a recorded revision passes 0412's gate.
- **Consequence:** A patch build (S3) can revise a built unit's spec in place under an approved deviation record, and no gate refuses it. P19 says it must arrive as a new unit.
- **Fix:** Add to 0400 a refusal of any revision of a unit whose spec is in a landed range, its deviation population included, seen red on a planted in-place edit of a landed unit's spec.

### B2-F13 — `cl-dClosedLoop-0407` places `drop_touched_exemptions` in `tools/lib`, but it lives in the map kit
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0407`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** 0407: "calling the pure `drop_touched_exemptions` in `tools/lib`, … the claim arm 'not installed' where the map is absent, seen on a planted core-only tree". Probe: `grep -rn drop_touched_exemptions tools --include=*.py` printed only `tools/codebase-map/map_lib.py:1373:def drop_touched_exemptions(...)` and its two callers in `tools/codebase-map/`.
- **Consequence:** On an adopter's core-only install, `build.scope`'s one check imports a function from a kit that is absent. Either the build imports from the map kit and the touch join fails on that tree, or the clause hides a move into `tools/lib`, which copy-installed kits carry inline, with no unit owning that move.
- **Fix:** Name the move (`drop_touched_exemptions` out of `map_lib.py` into `tools/lib`, with its readers re-pointed in the same unit) as a dScopedBuild clause, or cite its real home and make the touch arm "not installed" when the map is absent.

### B3-F6 — dWitnessedBar owns the remote verdict, but no unit builds it
- **Address:** architecture-v2 [chain] dWitnessedBar row; architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** gap-test-02 (HIGH, on dWitnessedBar's row): "The verdict-backend registry Test declares, and the remote verdict before the landing under `verdict: remote-ci`, are this gap's". dWitnessedBar's clauses `cl-dClosedLoop-0339` to `cl-dClosedLoop-0368` include no registry, no remote-ci read, and nothing for `verdict.remote.trust`, `.pin` or `.pin-scope`. Stage 0's K4 lead lists all three keys as "read by no chain clause". The P3 row names only 0342 and 0344. flow-steps says the remote verdict "is built when CI exists (R5.2)". CI already exists today: `cl-dClosedLoop-0029` cites `.github/workflows/remote-ci.yml`.
- **Consequence:** If a node in S2 selects `verdict: remote-ci`, the remote verdict is judged by a workflow that sits in the tree it judges, and no unit builds the pin or the trust guard. P3's "designed slot" and a HIGH gap stay uncarried, and dTrueNorth's coverage report would show them uncarried only at Design exit.
- **Fix:** Give dWitnessedBar a clause for the backend registry and the pinned-workflow trust arm, seen red on a build that edits its own pinned workflow. Or move gap-test-02 and the three keys to an integrations row and record the move.

### B1-F12 — Two owners stated for the entry step's items
- **Address:** architecture-v2 [chain]-preamble revision note (PM-9)
- **Class:** K8
- **Severity:** low
- **Scenario:** S7
- **Evidence:** v2:401 says "the entry step's items are dDeclaredLoop's (PM-9)". `cl-dClosedLoop-0122` (dPlacedRequest) and flow-steps' Owner column (SP-1) say dPlacedRequest.
- **Consequence:** A spec writer reads two owners.
- **Fix:** Mark the v2 note as superseded by SP-1.

### B2-F12 — v2 never defines the text a clause hash is taken over
- **Address:** architecture-v2 [clause-ids]
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Evidence:** [clause-ids]: "its text's hash being its revision". 0001: "the hash of its text". Only the copy's carries.py defines it: "the first eight hex digits of the SHA-256 of its text, the id cut off and its whitespace folded".
- **Consequence:** A dTrueNorth spec writer working from v2 can choose another normalisation, and every pin the instrument wrote reads stale under the product join.
- **Fix:** State the hash rule in [clause-ids], and have 0001 cite it.

### B4-F14 — P29's row leaves out the clauses that carry most of P29
- **Address:** architecture-v2 [enforcement]
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - The row reads "| `P29` | `cl-dClosedLoop-0178` |", and 0178 covers only "inputs handed as content ... re-cut fresh".
  - `roles.verifier-context`, `roles.answered-calls` and `roles.on-contradiction` sit in `cl-dClosedLoop-0196`, `0197` and `0198` (dFurnishedOrders), which are outside the row.
- **Consequence:** dOrderedCharter's meta-check reads P29 as enforced by one clause. Three of its six rules are never joined to the principle.
- **Fix:** Add 0196, 0197 and 0198 to P29's row.

### B1-F3 — P23's only enforcing clause, `cl-dClosedLoop-0093`, appears in no `[chain]` row
- **Address:** architecture-v2 [enforcement] (row `P23`, `cl-dClosedLoop-0093`)
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - P23's row is `| \`P23\` | \`cl-dClosedLoop-0093\` |`.
  - `grep -c 'cl-dClosedLoop-0093' architecture-v2.md` printed `1`, which is that row only.
  - dDeclaredLoop's clauses run 0092, then 0094. `[clause-ids]` reads "Retired: none".
- **Consequence:** P23 ("a claim is acted on only when its stored key recomputes equal…") has no clause, so no chain build builds the claim-trust rule. In S2, `entry.claim`'s "a retry that finds its own key counts as claimed" and every cross-node claim run with nothing checking their key or source.
- **Fix:** Restore dDeclaredLoop's clause `cl-dClosedLoop-0093` (the claim-trust rule: key recomputed, weakest source not agent-typed, otherwise re-derived or held as evidence). The K5 arm should red a ghost id.

### B2-F14 — P17's mechanical classification is only "(proposed)" in its one enforcing clause
- **Address:** architecture-v2 [enforcement] `P17` / [chain] `cl-dClosedLoop-0390`
- **Class:** K5, c5
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** P17: "a feature's design declares its units' interfaces structurally, so a change is classified mechanically". [enforcement]: "`P17` | `cl-dClosedLoop-0390`". 0390: "additive-versus-breaking interface classification (proposed)".
- **Consequence:** dIndexedDesign can be specced without building the classifier `design.reentry` routes on. An amendment is then classed by judgement, and P17 has no clause that commits to enforcing it.
- **Fix:** Drop "(proposed)" and give the classifier a seen-red, a planted breaking change classed additive, or record its deferral and take P17's row off 0390 until it is built.

### B2-F15 — No clause enforces P18's ranking of a fork's options
- **Address:** architecture-v2 [enforcement] `P18` / [chain] `cl-dClosedLoop-0176`, `cl-dClosedLoop-0390`
- **Class:** K5, c5
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** P18: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record". 0176: "every fork resolved by the role that meets it and recorded". 0390: "fork resolution by `design.forks`". The ranking appears only in the default value's name, `agents-feature-rich-expandable`. (I disclosed above that this was also a lead in the record I should not have read.)
- **Consequence:** In unattended S2, a fork record that carries no ranked options passes every join, so P18 is unenforced.
- **Fix:** Have 0176 require the fork record to list its options ranked by feature-richness, then expandability, with the chosen one first, and a schema check that reds a resolved fork without the ranking.

### B4-F1 — P23's enforcement row names a clause id that no chain clause carries
- **Address:** architecture-v2 [enforcement] `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S7
- **Evidence:** [enforcement] reads "| `P23` | `cl-dClosedLoop-0093` |". I parsed every `cl-` id out of [chain] (scratch `chain.py`) and the only gap in 0001–0496 is 93. dDeclaredLoop's row runs from 0092 ("the position engine ... each claim's key and verdict printed") straight to 0094. [clause-ids] says "Retired: none".
- **Consequence:** P23 ("a claim is acted on only when its stored key recomputes equal ...") has no clause, so no spec carries it. P29's "Acted on" rule depends on P23's re-derivation and is unenforced too. dTrueNorth's carries join and dOrderedCharter's meta-check get a ghost id.
- **Fix:** Restore the P23 clause in dDeclaredLoop's row as `cl-dClosedLoop-0093` (the claim's key recomputed, its weakest source not agent-typed, otherwise re-derived or held as evidence).

### B2-F4 — The per-unit budget share has no single freeze point, so each Design re-entry can mint budget
- **Address:** architecture-v2 [policies] `flow.rework-budget`; flow-steps [design] `design.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** v2 [policies]: "a base plus a count per unit frozen at Design's exit … 4+2". flow-steps [build]: closing-review findings "become new units … and those units pass through Design and back". So `design.exit` runs again on every lap. stall-and-loop [design] 1 says only "units a loop mints cannot reset it".
- **Consequence:** If the share is re-frozen at each `design.exit`, every closing-review finding (S1) and every patch build's Design (S3, which shares the originating budget) adds 2 to the budget it draws on. The P39 bound grows with the loop it is meant to stop.
- **Fix:** State that the shares freeze once, at the first `design.exit` the build records, and that units minted later carry no share. Seen red on a planted closing review whose finding-units raise the remaining budget on the card.

### B1-F10 — Plan's and the slice's policy keys are read by no item, and the landed-owner arm will red them
- **Address:** architecture-v2 [policies] `plan.authority`, `plan.triage`, `plan.kickoff`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - Stage 0 K4 lists these as "read by no chain clause and no item": `plan.authority`, `plan.triage`, `plan.kickoff`, `card.follows`, `leases.granularity`, `orient.budget` and `deps.coordination`.
  - `plan.triage: owner-batches` has no item where the owner acts, because `plan.triage-rule` is a command and `plan.triage-judge` is the planner.
  - `plan.authority`'s default, "planner-drafts-owner-ratifies", contradicts `plan.ratification: request`.
  - `cl-dClosedLoop-0014` reds "a key whose Owner build has landed has no reader".
- **Consequence:** Owner switches that switch nothing (against P10). dRankedPlan, dPlacedRequest and dKeptSession cannot land green without readers their rows never declare.
- **Fix:** Either give each key an item and a clause, for example a `plan.triage-owner` item under `owner-batches`, or retire the key with a decision. Reconcile `plan.authority` with `plan.ratification`.

### B5-F15 — `adopt.instructions` and `adopt.declarations` have no row in the adopt step
- **Address:** flow-steps [adopt]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** [adopt] declares five items. adopter-instructions [design] 15 says "Retrofit's `adopt` program gains `adopt.instructions`" (cl-dClosedLoop-0260, dLinkedLibrary). flow-roles-adoption [design] 17 says "At install and update, the `adopt` program proposes each of today's customizations as overlay rows" (cl-dClosedLoop-0438, `adopt.declarations`, dShippedRelease).
- **Consequence:** S4's "its declarations proposed as overlay rows" has no actor, Needs, witness or route, and the item join and Stage 0's K1 cannot see either item.
- **Fix:** Add both rows to [adopt], each with its owner build, Needs (`kits.install` or `kits.update`), its witness (the proposal records) and routes (the owner's one ruling per row).

### B5-F8 — `adopt.decisions` has two actor kinds and no route when the raters disagree
- **Address:** flow-steps [adopt] `adopt.decisions`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** The actor is "reviewer, as two raters, and the owner where `retrofit.decisions` says". The routes are "accepted → `reconstructed`; declined by the owner → kept `rejected`". v2 cl-dClosedLoop-0238 requires "two raters at kappa 0.8 or better".
- **Consequence:** When dLinkedLibrary routes gov's own 200 decision rows, a disagreement between the raters, or a kappa under 0.8, has no outcome. Under the default `author-rubric` no owner acts, so a candidate the raters reject also has no route.
- **Fix:** Split the item per actor: a raters item that computes agreement, and an owner item under `docs-owner-ratifies`. Add routes for disagreement (to the owner or a third rater) and for kappa below the bar (a re-rating round on the budget).

### B5-F9 — Under the default `on-touch`, nothing reconstructs records
- **Address:** flow-steps [adopt] `adopt.reconstruct`
- **Class:** K8
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** "under the default `on-touch` it never runs, and `build.unit-pass` reconstructs on first touch". `build.unit-pass`'s Does and Proven-by cells say nothing about reconstruction, and no clause in v2 [chain] carries it: a search for `reconstruct|first touch|on-touch` finds only cl-0245. `build.unit-pass` is dScopedBuild's, which is no ancestor of dLinkedLibrary.
- **Consequence:** With the default setting, records for untouched code are never reconstructed by any build. The S7 bootstrap also leaves the duty with a non-ancestor.
- **Fix:** Add the on-touch reconstruction to `build.unit-pass`, or a new `build.reconstruct` item under `retrofit.reconstruct: on-touch`, with a clause on dScopedBuild's row or a descendant build's row and a seen-red fixture.

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

### B4-F12 — `review.cost` writes shape fields before the shapes registry exists
- **Address:** flow-steps [breakpoint] `review.cost`
- **Class:** K7
- **Severity:** low
- **Scenario:** S7
- **Evidence:**
  - `review.cost` (dDeclaredLoop) extends the "`review-shape` line with `shape`, `efforts` and `role-sha` into the shape-run row".
  - v2 [owed]: "dBoundRoles builds the shapes registry". The shape-run kind is dTotalRecall's in layer-memory's table.
  - `grep review-shape tools/workflows/tier2-review.js` printed `renderShapeLine`, which has no shape or role-sha field.
- **Consequence:** From dDeclaredLoop to dBoundRoles, the item writes fields that have no source.
- **Fix:** State a stand-in (shape and role-sha left blank until dBoundRoles), or move the extension onto dBoundRoles.

## Clean cells to attack

- `test.verdict` in S7
- `test.flakes` in S1
- `plan.triage-judge` in S7
- `deploy.mandate` in S6
- `build.scope` in S3
- `life.unlease` in S7
- `release.route` in S2
- `design.unit-spec` in S6

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `BS1-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b1/` only. Your effort is the one the owner's
role definition sets.

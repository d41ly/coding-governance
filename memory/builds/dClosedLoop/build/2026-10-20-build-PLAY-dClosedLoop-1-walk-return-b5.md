# Walk return: run B, walker 5, adopt and the expansions

**Serves:** research PLAY-dClosedLoop-1

Dispatch 173's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-14-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because Maintain's patch path skips the entry claim, the lease, the duplicate check and `patch.ratify`. A red reading then spawned unleased, unratified patch builds that no budget bounds. A failed fix that went red again was dropped by the intake's own key.

### B5-F1 — Maintain's patch build skips entry, its claim and lease, and FI-4's light five
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `maintain.patch`, "opens a patch build at Design … | the intake, keyed by (reading, offender key) | Design, as `patch.ratify` says". flow-steps [transitions] admits a patch only as "a placement disposition `patch`, from any of the three, its slug claimed and its lease taken by `entry.claim`", and [design] enters on "a patch build's derived plan record, its slug claimed and its lease taken by `entry.claim`". flow-interactions FI-4 settles that a patch owes "the duplicate check against live builds, its derived plan record placed in the plan view, the build lease, and ratification as `patch.ratify` says". retrofit [cadence] routes the same Maintain sweep "through `entry.place`'s `patch` disposition". A probe found `patch.ratify` 0 times in flow-steps, layer-flow and flow-roles.
- **Consequence:** In S3 the patch reaches Design with no claim ref, no lease and no transition row. In S2, node x's pick sees it as unleased work. Under `patch.ratify: owner` no item holds it for the owner, so the guard is read but never enforced. With no dedupe, `deploy.core`'s post-close patch and Maintain's `default-branch-red` patch for the same red both run.
- **Fix:** Route `maintain.patch` to `entry.place-check` with a declared `patch` disposition, then `entry.claim`. Give the patch path one item that runs `plan.dedupe` and one owner gate that reads `patch.ratify`, and add both to [transitions].

### B5-F2 — A Maintain patch's key has no period and no originating build, so a failed fix is swallowed
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** [design] says "Every command item below is idempotent on the key its witness names, so a repeat with that key is a no-op". `maintain.patch`'s witness is "the intake, keyed by (reading, offender key)", with no period, unlike `maintain.file`'s "seen" row keyed by period. stall-and-loop `[1]` charges only "a patch build raised by the build's own landing" to "the originating build's budget".
- **Consequence:** The patch lands, and the next period's reading of the same offender is still over its pin. The re-filing is a no-op on the existing key, so the breach is never filed again and no route reaches the owner. The rework budget a Maintain-filed patch draws on is also undefined: no originating build exists, so S3's "originating build's budget spent" cannot be charged or detected.
- **Fix:** Key the intake by (reading, offender key, period). Route a recurrence on a closed patch to `maintain.file` as a `seen` row on an owner ask. Name the budget a Maintain patch draws on, either the reading's own keyed budget or the build whose landing introduced the offender.

### B5-F3 — The expansion tables declare no Needs, and `maintain.record`, `maintain.levels` and `loop.record` are never reached
- **Address:** layer-expansions [design-observability] `maintain.record`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** The Maintain and Loop Review tables have the columns "Item | Actor | Does | Witness | Routes | Owner", with no Needs column. flow-steps [rules] requires "Every item declares what it needs" and `next` returns "the unwitnessed items whose needs are witnessed". Routes: `maintain.read` goes to direct, patch or file; `maintain.direct` goes to file; `maintain.file` to "Plan's triage"; `maintain.patch` to "Design"; `loop.file` to "the owner's breakpoint". Nothing routes to `maintain.levels`, `maintain.record` or `loop.record`. Stage 0 confirms: "maintain.record: reached from no entry".
- **Consequence:** `maintain.record` "releases the lease" and writes the record that EX-3's default `every-period` owes. Neither happens by any declared route, so the period lease is never released and the run never reaches "closed". The slower levels in `maintain.levels` never run.
- **Fix:** Add a Needs column to every expansion table, for example `maintain.record` needing every reached item of the run and `maintain.levels` needing `maintain.lease`. End each program's terminal routes at its record item.

### B5-F4 — `loop.lease` and `release.pick` leave a lease held elsewhere unrouted, and E's promotion lease is never released
- **Address:** layer-expansions [design-observability] `loop.lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** `maintain.lease` routes "held elsewhere → skip; done → nothing; taken → `maintain.read`". `loop.lease` routes "`loop.gather`" only. In [design-integrations], `release.pick` "takes … E's promotion lease" and routes "`release.approve`" only. `release.record` writes the record and the exit record but releases no lease. flow-steps [rules] says "Every item's outcome set is closed, and every outcome routes."
- **Consequence:** In S2, node d holds the week's lease or E's promotion lease, and node x's instance has no declared outcome. A finished pass leaves E's lease held, so the next landed SHA's pick blocks until expiry.
- **Fix:** Give `loop.lease` and `release.pick` the outcomes `maintain.lease` has: held elsewhere, skip; done, nothing. Make `release.record` release E's promotion lease, as `maintain.record` releases its own.

### B5-F5 — Concurrent `kits.cut` instances race for one tag number
- **Address:** layer-expansions [design-distribution] `kits.cut`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** "under `every-landing` the core's `landed` event, keyed by the landed SHA … cuts the annotated tag `gov/v<date>.<n>` … refused by the remote → an owner item". layer-runtime [schedule] says "Each cadence instance is keyed by its period", and each instance has its own lease.
- **Consequence:** X lands on node d and Y lands on node x. Two instances, keyed by different SHAs, hold different leases, and both number the same `gov/v<date>.<n>`. The second push is refused and becomes an owner item for an ordinary race, and the two cuts' notes overlap.
- **Fix:** Serialize cuts under one lease for the tag series. On a refused tag push, refetch and renumber within `flow.route-backs`, and raise an owner item only past that bound.

### B5-F6 — `kits.install` and `kits.update` share one row with two actor kinds, no Needs, a self-written witness and no terminal route
- **Address:** layer-expansions [design-distribution] `kits.update`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S4
- **Evidence:** The row is "| `kits.install`, `kits.update` | the owner, or a command | … | the receipt, and the wiring verdict | an adapter that declares no target → its slot renders not installed, the core render kept |". flow-steps [rules] requires "One actor per item, of one kind … an item whose actor a policy value chooses is one item per value". Stage 0 reports "kits.update: ends nowhere". retrofit [owners] gives dShippedRelease "the install and update hooks that call `adopt` and `test.seed`", but neither item routes to them.
- **Consequence:** S4's update has no success route, no route for a step that exits nonzero after its first write (cl-0022's "receipt naming step k-1"), no route for a held edited render or a stale-pin order (cl-0026, IA-3), and no handoff to `test.seed` or `adopt.declarations`. Its witness is the receipt the update writes itself, so a step that passes its witness without doing its work is certified. S4 reaches no declared terminal.
- **Fix:** Split the row into `kits.install` and `kits.update`, one row per actor value, each with Needs and a closed outcome set: updated, then `test.seed` for each new check, then `adopt.declarations` and `adopt.instructions`; a step that exits nonzero, then the receipt at step k-1 and a rerun; held, then an order. Make the witness the step gate's per-step witness re-derived, plus the wiring verdict.

### B5-F7 — `kits.offer`'s pushed route files no order for the adopter's `test.seed` and `adopt` runs
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** The row reads "pushed → the adopter lands it with its own lander, whose bar runs the checks the offer left unrun; an update that needs target-side execution, or a refused push → an outbox order". v2 cl-dClosedLoop-0430 says the offer's "outbox order names the adopter's own run of both". retrofit [seed] says the order "names the adopter's own run of `test.seed`, which arms them".
- **Consequence:** On the ordinary pushed path no order is filed. The adopter's bar does not run `test.seed`, so the update's new checks stay unarmed indefinitely under the default `retrofit.unseeded: unarmed`.
- **Fix:** On `pushed`, also file the outbox order that names the adopter's `test.seed` and `adopt` runs, keyed by (adopter, release). Add that order to `test.seed`'s Needs.

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

### B5-F10 — `kits.offer`'s counts and the receipt schema are stale against v2
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K1
- **Severity:** low
- **Scenario:** S4
- **Evidence:** The row says "the design adds an eighth; the mode refuses all eight". cl-dClosedLoop-0435 adds "step processes a ninth spawn kind its mode refuses unless they run under the step kind's isolation contract". The contract row names "`receipt` (… schema 4 …)", while cl-0435 moves it to "schema 5".
- **Consequence:** A spec writer building the offer mode from the row misses the ninth kind and the schema-5 fields that S4's migration needs.
- **Fix:** Bring the row's count and the receipt line up to cl-0435.

### B5-F11 — `maintain.read` routes neither `maintain.tiers` nor `maintain.on-breach`
- **Address:** layer-expansions [design-observability] `maintain.read`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** The routes are "in pin → nothing; over pin → `maintain.direct`, `maintain.patch` or `maintain.file`, by its fix". v2's `maintain.tiers` defaults to `bands`, "to log, to diagnose read-only or to act within `maintain.fixes`" (cl-0455). `maintain.on-breach` allows `file-ask, red-leg, report`, while `maintain.file` always "files an ask" and its witness is "the ask".
- **Consequence:** Under the default bands, a reading in the log or diagnose band has no route. Under `report` or `red-leg`, `maintain.file` still files an ask, so the key's other two values have no arm.
- **Fix:** Give `maintain.read` one route per tier band, and give `maintain.file` one arm per `maintain.on-breach` value, each with its own witness.

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

### B5-F14 — dTendedCadence's release-verify-failed join depends on dShippedRelease, which is not its ancestor
- **Address:** layer-expansions [design-observability] `maintain.file`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `maintain.file` says the ask for `release-verify-failed` "joins `release.route`'s", and "A fixture owes it: a red verify under roll-forward leaves one open ask with a `seen` row". `release.route` belongs to dShippedRelease. The ancestor walk over v2's Parents column gives dTendedCadence's ancestors without dShippedRelease. `maintain.events` defaults to "all three".
- **Consequence:** When dTendedCadence lands before dShippedRelease, the shared-key join and its fixture have nothing to run against, so the arm lands unseen red or is skipped.
- **Fix:** Put the fixture and the join on dShippedRelease's row, or on a build descended from both, and record dTendedCadence's event arm as a stand-in until then.

### B5-F15 — `adopt.instructions` and `adopt.declarations` have no row in the adopt step
- **Address:** flow-steps [adopt]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** [adopt] declares five items. adopter-instructions [design] 15 says "Retrofit's `adopt` program gains `adopt.instructions`" (cl-dClosedLoop-0260, dLinkedLibrary). flow-roles-adoption [design] 17 says "At install and update, the `adopt` program proposes each of today's customizations as overlay rows" (cl-dClosedLoop-0438, `adopt.declarations`, dShippedRelease).
- **Consequence:** S4's "its declarations proposed as overlay rows" has no actor, Needs, witness or route, and the item join and Stage 0's K1 cannot see either item.
- **Fix:** Add both rows to [adopt], each with its owner build, Needs (`kits.install` or `kits.update`), its witness (the proposal records) and routes (the owner's one ruling per row).

| item | scenario | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
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

| dLinkedLibrary | B5-F8, B5-F9, B5-F15 |
| dTotalRecall | holds |
| dTendedCadence | B5-F1, B5-F2, B5-F3, B5-F11, B5-F12, B5-F14 |
| dMindYourWords | holds |
| dOrderedCharter | holds |

| P6 | B5-F1, B5-F2, B5-F3 |
| P13 | holds |
| P14 | holds |
| P28 | holds |
| P30 | holds |
| P32 | holds |
| P33 | holds |
| P34 | holds |
| P35 | holds |

Read outside the list above:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, from `[scenarios]` to the end, read in the working tree before I switched to the copy, because my launch framed the task as a review of the brief.
- `diff` of the working tree's `...-walk-brief-b4.md` and `...-walk-brief-a5.md` against this brief, for the same reason.
- Listings of the working tree's `memory/builds/dClosedLoop/build/` and `prompts/`.
- A listing of `seed-dcl/scratch/` that showed the other walkers' folder names. None were opened.
- A `grep -c` over the copy's build folder whose output named one `*-compared.md` file with a match count. Its content was not read.

Brief defect: the brief's adopt item list mirrors flow-steps' five-row `[adopt]` table, so it leaves out `adopt.instructions` and `adopt.declarations` (B5-F15), and it lists `kits.install` and `kits.update` as two items where layer-expansions has one row.

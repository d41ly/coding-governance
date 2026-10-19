# Skeptic brief: run B, batch 4

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b4/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### B3-F7 — `test.route` sends a non-blocking MIXED red two ways
- **Address:** flow-steps [test] `test.route`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** `test.route`: "routes each red by its computed class, as `verdict.blocks` says ... an OWN or MIXED red → `test.attribute`; ... a red that does not block → an ask". The default is `verdict.blocks: own-only` (v2 line 1144), under which MIXED does not block. layer-flow [settled]: "MIXED, CONTENDED and DEAD PROBE route by `verdict.blocks`: to an ask when they do not block".
- **Consequence:** Under the default, a MIXED red matches both arms. A spec writer cannot tell whether it goes to the tester, and so to a fix pass, or to an ask that lets the landing go ahead.
- **Fix:** Condition the arm: "an OWN red, or a MIXED red where `verdict.blocks` blocks it → `test.attribute`".

### B4-F2 — Budget-exhaustion and park endings have no transition row and no terminal state
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - [transitions] says "Landed, withdrawn, superseded, deferred, retired, refused, merged and answered are terminal" and "the engine refuses any transition the table lacks".
  - v2 `cl-dClosedLoop-0116` has `flow.on-exhausted` "closing the build incomplete with its branch and records kept, `park-for-owner` and `close-incomplete` the other values".
  - `cl-dClosedLoop-0326`: silence "parking the build, its lease released and the item open". layer-runtime [decide]: `stale-remote` "parks once `leases.expiry-hours` passes".
  - `grep -n incomplete` over flow-steps, layer-flow, layer-runtime and layer-memory printed nothing. The only hold state is `paused`, and it keeps its leases.
- **Consequence:** In S6 (budget spent, owner silent on the ratification) and S3 (originating budget spent), the ending P39 promises is a transition `cl-dClosedLoop-0098`'s engine refuses. The build never reaches a terminal, against P20's "ends in a terminal state flow-steps' `[transitions]` declares".
- **Fix:** Add the terminal state `closed-incomplete` and a `parked` state (lease released, item open, resumed by the owner's disposition). Add rows from every open state on `flow.on-exhausted` and on a park, each with its witness.

### B5-F13 — An install or update trusts a mutable, unpinned tag name
- **Address:** layer-expansions [design-distribution] `kits.currency`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** "govkit installs by copy at a release tag, and the receipt names that release and the remote it came from". The receipt fields are "per-kit versions, the release tag, the source remote", with no commit. `kits.cut` "cuts the annotated tag", which is unsigned. Under `any-commit`, `kits.currency` "counts the release tags dated after the installed commit".
- **Consequence:** This is tampering at the adopter boundary. A tag moved on the source remote, or served by a mirror, installs other bytes under the same receipt, and `kits.currency` cannot tell. Under `any-commit`, tag dates from a skewed cutter miscount how far behind the adopter is.
- **Fix:** Record the tag's object and commit SHA in the receipt and the kit-release record, and have update refuse a tag whose commit differs from that record. Count releases behind by ancestry, not by date.

### B5-F5 — Concurrent `kits.cut` instances race for one tag number
- **Address:** layer-expansions [design-distribution] `kits.cut`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** "under `every-landing` the core's `landed` event, keyed by the landed SHA … cuts the annotated tag `gov/v<date>.<n>` … refused by the remote → an owner item". layer-runtime [schedule] says "Each cadence instance is keyed by its period", and each instance has its own lease.
- **Consequence:** X lands on node d and Y lands on node x. Two instances, keyed by different SHAs, hold different leases, and both number the same `gov/v<date>.<n>`. The second push is refused and becomes an owner item for an ordinary race, and the two cuts' notes overlap.
- **Fix:** Serialize cuts under one lease for the tag series. On a refused tag push, refetch and renumber within `flow.route-backs`, and raise an owner item only past that bound.

### B5-F10 — `kits.offer`'s counts and the receipt schema are stale against v2
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K1
- **Severity:** low
- **Scenario:** S4
- **Evidence:** The row says "the design adds an eighth; the mode refuses all eight". cl-dClosedLoop-0435 adds "step processes a ninth spawn kind its mode refuses unless they run under the step kind's isolation contract". The contract row names "`receipt` (… schema 4 …)", while cl-0435 moves it to "schema 5".
- **Consequence:** A spec writer building the offer mode from the row misses the ninth kind and the schema-5 fields that S4's migration needs.
- **Fix:** Bring the row's count and the receipt line up to cl-0435.

### B5-F7 — `kits.offer`'s pushed route files no order for the adopter's `test.seed` and `adopt` runs
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** The row reads "pushed → the adopter lands it with its own lander, whose bar runs the checks the offer left unrun; an update that needs target-side execution, or a refused push → an outbox order". v2 cl-dClosedLoop-0430 says the offer's "outbox order names the adopter's own run of both". retrofit [seed] says the order "names the adopter's own run of `test.seed`, which arms them".
- **Consequence:** On the ordinary pushed path no order is filed. The adopter's bar does not run `test.seed`, so the update's new checks stay unarmed indefinitely under the default `retrofit.unseeded: unarmed`.
- **Fix:** On `pushed`, also file the outbox order that names the adopter's `test.seed` and `adopt` runs, keyed by (adopter, release). Add that order to `test.seed`'s Needs.

### B5-F6 — `kits.install` and `kits.update` share one row with two actor kinds, no Needs, a self-written witness and no terminal route
- **Address:** layer-expansions [design-distribution] `kits.update`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S4
- **Evidence:** The row is "| `kits.install`, `kits.update` | the owner, or a command | … | the receipt, and the wiring verdict | an adapter that declares no target → its slot renders not installed, the core render kept |". flow-steps [rules] requires "One actor per item, of one kind … an item whose actor a policy value chooses is one item per value". Stage 0 reports "kits.update: ends nowhere". retrofit [owners] gives dShippedRelease "the install and update hooks that call `adopt` and `test.seed`", but neither item routes to them.
- **Consequence:** S4's update has no success route, no route for a step that exits nonzero after its first write (cl-0022's "receipt naming step k-1"), no route for a held edited render or a stale-pin order (cl-0026, IA-3), and no handoff to `test.seed` or `adopt.declarations`. Its witness is the receipt the update writes itself, so a step that passes its witness without doing its work is certified. S4 reaches no declared terminal.
- **Fix:** Split the row into `kits.install` and `kits.update`, one row per actor value, each with Needs and a closed outcome set: updated, then `test.seed` for each new check, then `adopt.declarations` and `adopt.instructions`; a step that exits nonzero, then the receipt at step k-1 and a rerun; held, then an order. Make the witness the step gate's per-step witness re-derived, plus the wiring verdict.

### B5-F4 — `loop.lease` and `release.pick` leave a lease held elsewhere unrouted, and E's promotion lease is never released
- **Address:** layer-expansions [design-observability] `loop.lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** `maintain.lease` routes "held elsewhere → skip; done → nothing; taken → `maintain.read`". `loop.lease` routes "`loop.gather`" only. In [design-integrations], `release.pick` "takes … E's promotion lease" and routes "`release.approve`" only. `release.record` writes the record and the exit record but releases no lease. flow-steps [rules] says "Every item's outcome set is closed, and every outcome routes."
- **Consequence:** In S2, node d holds the week's lease or E's promotion lease, and node x's instance has no declared outcome. A finished pass leaves E's lease held, so the next landed SHA's pick blocks until expiry.
- **Fix:** Give `loop.lease` and `release.pick` the outcomes `maintain.lease` has: held elsewhere, skip; done, nothing. Make `release.record` release E's promotion lease, as `maintain.record` releases its own.

### B5-F14 — dTendedCadence's release-verify-failed join depends on dShippedRelease, which is not its ancestor
- **Address:** layer-expansions [design-observability] `maintain.file`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `maintain.file` says the ask for `release-verify-failed` "joins `release.route`'s", and "A fixture owes it: a red verify under roll-forward leaves one open ask with a `seen` row". `release.route` belongs to dShippedRelease. The ancestor walk over v2's Parents column gives dTendedCadence's ancestors without dShippedRelease. `maintain.events` defaults to "all three".
- **Consequence:** When dTendedCadence lands before dShippedRelease, the shared-key join and its fixture have nothing to run against, so the arm lands unseen red or is skipped.
- **Fix:** Put the fixture and the join on dShippedRelease's row, or on a build descended from both, and record dTendedCadence's event arm as a stand-in until then.

### B1-F4 — Maintain's patch skips entry.place and entry.claim and goes straight to Design
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:**
  - `maintain.patch`: "opens a patch build at Design … | the intake, keyed by (reading, offender key) | Design, as `patch.ratify` says".
  - flow-steps [entry]: a cadence filer's intake is "placed by `entry.place` the same way".
  - `[transitions]`: none→designing for `patch` needs "its slug claimed and its lease taken by `entry.claim`", and "the engine refuses any transition the table lacks".
  - `design.input` takes a patch "its slug claimed and its lease taken by `entry.claim`".
  - flow-steps `deploy.core` routes a red to "a patch build through the entry-point table's post-close row", which also names no `entry.place`.
- **Consequence:** In S3 the patch either reaches Design with no disposition, no claim ref and no lease (two nodes' Maintain runs can open it twice, and P22 and P40 are broken), or the engine refuses the transition and the patch has no terminal.
- **Fix:** Route `maintain.patch` (and the post-close row) to "files a patch intake → `entry.place`", and let `entry.claim` take the slug and the lease.

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

### B5-F11 — `maintain.read` routes neither `maintain.tiers` nor `maintain.on-breach`
- **Address:** layer-expansions [design-observability] `maintain.read`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** The routes are "in pin → nothing; over pin → `maintain.direct`, `maintain.patch` or `maintain.file`, by its fix". v2's `maintain.tiers` defaults to `bands`, "to log, to diagnose read-only or to act within `maintain.fixes`" (cl-0455). `maintain.on-breach` allows `file-ask, red-leg, report`, while `maintain.file` always "files an ask" and its witness is "the ask".
- **Consequence:** Under the default bands, a reading in the log or diagnose band has no route. Under `report` or `red-leg`, `maintain.file` still files an ask, so the key's other two values have no arm.
- **Fix:** Give `maintain.read` one route per tier band, and give `maintain.file` one arm per `maintain.on-breach` value, each with its own witness.

### B5-F3 — The expansion tables declare no Needs, and `maintain.record`, `maintain.levels` and `loop.record` are never reached
- **Address:** layer-expansions [design-observability] `maintain.record`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** The Maintain and Loop Review tables have the columns "Item | Actor | Does | Witness | Routes | Owner", with no Needs column. flow-steps [rules] requires "Every item declares what it needs" and `next` returns "the unwitnessed items whose needs are witnessed". Routes: `maintain.read` goes to direct, patch or file; `maintain.direct` goes to file; `maintain.file` to "Plan's triage"; `maintain.patch` to "Design"; `loop.file` to "the owner's breakpoint". Nothing routes to `maintain.levels`, `maintain.record` or `loop.record`. Stage 0 confirms: "maintain.record: reached from no entry".
- **Consequence:** `maintain.record` "releases the lease" and writes the record that EX-3's default `every-period` owes. Neither happens by any declared route, so the period lease is never released and the run never reaches "closed". The slower levels in `maintain.levels` never run.
- **Fix:** Add a Needs column to every expansion table, for example `maintain.record` needing every reached item of the run and `maintain.levels` needing `maintain.lease`. End each program's terminal routes at its record item.

### B4-F15 — Slice items write record kinds that are not registered
- **Address:** layer-memory [contract]
- **Class:** K3
- **Severity:** low
- **Scenario:** S5
- **Evidence:** Three records written by slice items have no row in the kind table:
  - `probe.trigger` writes "the trigger record";
  - `life.request` writes "the command's record";
  - `life.quiesce` writes "the executor's record of the acts it let finish".

  The table holds `attendance override`, `workspace`, `probe` and `review`, but nothing for these three.
- **Consequence:** Stage 0's K3 arm, which reads registered kinds only, cannot see them, so they have no declared reader, home or check.
- **Fix:** Register `probe trigger`, `lifecycle request` and `quiesce` rows, each with its writer item and readers.

### B3-F1 — The seen-red check writes the record it checks for
- **Address:** layer-memory [design], kind `seen-red`; flow-steps [test] `test.seen-red`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** In layer-memory's kind table: "| seen-red | dWitnessedBar | its writer is `test.seen-red` |". In flow-steps, `test.seen-red` "checks that every gate the build added or changed has a seen-red record", and its witness is "the seen-red records". `cl-dClosedLoop-0345` says only "seen-red records".
- **Consequence:** The only declared writer of the record is the item that checks it exists. A gate the S1 feature adds gets its seen-red record from the check itself, whether or not anyone ever saw it red, so `test.seen-red` always passes. The guard shares state with what it guards.
- **Fix:** Make the seen-red record's writer the run that observed the planted red: the leg factory's seen-red arm, run inside the unit's pass, keyed by the leg and the red SHA. Keep `test.seen-red` as a reader only. Seed a red case: a gate with no observed red must make `test.seen-red` red.

### B2-F7 — A cross-node unit has no workspace or integration rule under the default `build.worktree: shared`
- **Address:** layer-runtime [isolate]; flow-steps [build] `build.unit-pass`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2 [policies]: "`build.worktree` | per-unit, parallel-only, shared | shared". [isolate]: "shared: the build's one worktree … The commit queue then commits them one at a time". "Integration before release" is stated for unit branches only. cloud-and-scale [design] 8: any node picks "ready, unleased units" across builds.
- **Consequence:** Node x takes one of X's units by lease, but under the default the unit's worktree and commit queue live on node d. Nothing says where x commits, how its pass reaches the build branch, or what the fence covers. The unit can never integrate, or it integrates outside the queue.
- **Fix:** A unit leased from another node always gets a unit branch, as under `per-unit`, whatever `build.worktree` says, integrated by the build lease's holder before the unit lease is released. Seen on a two-clone fixture.

### B5-F12 — Cadence period keys come from each node's own clock
- **Address:** layer-runtime [schedule]
- **Class:** K10
- **Severity:** low
- **Scenario:** S2
- **Evidence:** "Each cadence instance is keyed by its period (ISO week or date)." Lease expiry uses "a declared clock" (cloud-and-scale `[4]`), but the period key names no clock, and layer-runtime records a node whose "clock runs 8 to 13 s slow".
- **Consequence:** Near a day or week boundary, node x with a skewed clock derives a different period key. Its check for an existing period witness finds nothing, so Maintain or the Loop Review runs twice and writes two records.
- **Fix:** Derive the period key from the declared clock, corrected by the node registry's offset, which is the same clock lease expiry uses.

## Clean cells to attack

- `build.unit-pass` in S6
- `plan.triage-judge` in S7
- `plan.triage-judge` in S5
- `design.research` in S5
- `test.route` in S7
- `maintain.read` in S7
- `kits.adopters` in S4
- `review.fold` in S2

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `BS4-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b4/` only. Your effort is the one the owner's
role definition sets.

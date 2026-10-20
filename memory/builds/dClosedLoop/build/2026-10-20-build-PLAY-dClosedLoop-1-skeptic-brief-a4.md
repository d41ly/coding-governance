# Skeptic brief: run A, batch 4

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run A of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a4/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### A5-F11 — Revision notes contradict the route they annotate
- **Address:** flow-steps [rules]; [breakpoint] (the "unverified finding under `review.unverified: block`" bullet)
- **Class:** K2
- **Severity:** low
- **Scenario:** S6
- **Evidence:**
  - `[rules]`: "its open work goes to asks ... Revised 2026-10-19 by the owner's SL-1 and SL-2: the loop had become an owner item, resolved as [breakpoint]'s owner gate is (FH1)".
  - `[breakpoint]`: "the finding is filed as an ask with its evidence. Revised ...: it became an owner item".
- **Consequence:** A reader cannot tell whether the route past the bound is an ask or an owner item.
- **Fix:** Reword each note to say what the route was before the revision ("it had been an owner item until SL-1"), or drop it.

### A5-F9 — `verdict.flakes`' one threshold is the release streak, yet `test.flakes` reads it as the hold threshold
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - `test.flakes`: "under `quarantine`, a leg past the threshold `verdict.flakes` declares is held".
  - v2: "`verdict.flakes` | quarantine, record, retry-only; a threshold | quarantine | walk T3; the threshold three consecutive greens unless set".
  - `cl-dClosedLoop-0368` uses that same threshold to release a held leg.
- **Consequence:** For S6's flake at Test, nothing says after how many flakes a leg is held. A spec writer cannot write the hold arm.
- **Fix:** Split the key into a hold threshold (flakes counted in a window) and a release threshold (consecutive greens), each with a default.

### A5-F8 — A landing conflict sends the build to a resolution pass that Build does not declare
- **Address:** flow-steps [test] `test.merge`; [build]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - `deploy.land`: "refused before the push, a race included → Test". `test.merge`: "a conflict → Build for a resolution pass".
  - Build "Enters when every unit is READY", and its table has no resolution item, actor, lease or witness.
  - Re-entering Build re-runs `build.recommend` and the closing review, which `review.build: owed` requires under `strict`. A "review round after the first" draws on the budget, while `[rules]` says "a merge conflicted by another build's landing ... draws nothing".
- **Consequence:** A conflict caused by another build's landing is resolved by an undeclared actor. It indirectly spends the rework budget that contention must not touch.
- **Fix:** Declare a `build.resolve` item with its actor (the builder, or the architect when an interface clashes), its witness and its re-entry point back into Test. Mark its passes and any re-review as contention that draws nothing.

### A5-F1 — `[transitions]` has no state for a parked build, and no terminal for an incomplete ending
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - The table's states are planning, designing, building, testing, deploying and paused. Its terminals (line 650) are "Landed, withdrawn, superseded, deferred, retired, refused, merged and answered", and it says "the engine refuses any transition the table lacks".
  - Endings the design declares elsewhere:
    - v2 `[policies]` `run.on-owner-silence`: "a ratification ... parks its build ... its lease released and the item open".
    - `flow.on-exhausted`: `park-for-owner` and `close-incomplete`, and best effort "descoping the failing units to asks and landing the rest, or closing the build incomplete" (`cl-dClosedLoop-0116`).
    - layer-runtime `[decide]` `stale-remote`: "parks once `leases.expiry-hours` passes".
  - Probe: `grep -n -i "incomplete\b"` over flow-steps, layer-flow, layer-memory and layer-runtime found no state. A parked state appears only as a count, `| parked | 8 |`, at layer-runtime:148.
  - `[lifecycle]` says "A paused build keeps its leases", so a parked build, whose lease is released, is not a paused one.
- **Consequence:** Several S6 failures end here: the owner's silence on the ratification, a spent budget under any of the three values, and an unreachable remote that outlasts the lease expiry. Each needs a transition the engine refuses. dDeclaredLoop's own termination check (`cl-dClosedLoop-0118`, "every state reaching a terminal") cannot be specced against a table that lacks these states.
- **Fix:**
  - Add a `parked` state with its rows: owner silence past `run.owner-deadline`, `park-for-owner` and `stale-remote`. Its witness is the park record, and its exit is the owner's disposition, which re-takes the lease.
  - Add a terminal `closed-incomplete` reached by `flow.on-exhausted`.
  - Give a descoped unit a row back from building or testing.

### A3-F3 — No item writes a patch build's derived plan record, and no flow item reads `patch.ratify`
- **Address:** flow-steps [transitions] (none → designing on `patch`); [entry] `entry.claim`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** The `patch` transition is witnessed by "the patch's derived plan record, the claim ref and the lease record". layer-memory's kind table says the plan kind's "writer is `plan.record`", and a patch build never reaches Plan. flow's entry-point table says the record is "derived from the intake and ratified as `patch.ratify` says". `grep patch.ratify` over flow-steps finds nothing. v2 `[presets]` sets `patch.ratify: owner` under `strict`.
- **Consequence:** A patch build's entry transition lacks its witness. Under `strict`, no owner gate exists, so the owner ratification the preset declares silently never happens.
- **Fix:** Give `entry.claim`, or a new dPlacedRequest item, the derivation of the plan record on `patch` and `repeat`. Make that item read `patch.ratify`, with `owner` raising an owner item resolved as `[breakpoint]`'s owner gate is.

### A1-F6 — Closing-review units have no transition row, and "released" resumes Build's tail without waiting for them
- **Address:** flow-steps [transitions]; flow-steps [build] closing review; flow-steps [breakpoint] `review.dispose`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - Design's inputs list "a review finding disposed into a new unit" separately from "a fix unit, for a red whose spec is wrong or a core red".
  - [transitions] has only "building | a unit or feature re-entry, or a fix unit | designing". cl-dClosedLoop-0098 says "the engine refusing any transition it lacks".
  - `review.dispose` on built work routes "built → released", and the flow "resumes at the item the breakpoint stands before", which is `build.distill`. That item's Needs are "`build.recommend`, the closing review where it ran, and `build.ratify` ...". They name no new unit. `build.exit` needs only `build.core`.
  - Build's Exits require "the closing review is folded, its findings built as new units".
- **Consequence:** In S1, when the closing review's findings arrive as new units (an injection), there are two outcomes:
  - The engine refuses building→designing for them.
  - If the engine allows it, `build.distill`, `build.core` and `build.exit` run on the frontier while the units are still in Design. The build reaches Test without its findings built, against Build's own exit contract and cl-dClosedLoop-0400.
- **Fix:** Add the row "building | a closing-review finding disposed into a new unit | designing | the review report and the disposition". Make `build.distill`'s Needs include "every unit `review.dispose` minted, built and reuse-checked". Add a planted finding unit that must hold `build.exit`.

### A3-F4 — `maintain.patch` opens a patch build at Design and skips placement, claim and lease
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** It "opens a patch build at Design … Routes: Design, as `patch.ratify` says". flow-steps `[entry]` says a cadence filer's prompt "is recorded as intake … and placed by `entry.place` the same way". `[transitions]` requires the claim ref and the lease record for `patch`.
- **Consequence:** A Maintain patch has no slug claim, no lease and no transition witness. The engine refuses it, or the patch runs unleased against other nodes.
- **Fix:** Route `maintain.patch` to the filer's intake and then `entry.place`, so it reaches `entry.claim` the way every other patch does.

### A3-F8 — `maintain.patch`'s key has no period or SHA, so a recurrence after the patch lands counts as done
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** Its witness is "the intake, keyed by (reading, offender key)". `maintain.file` instead adds a `seen` row "keyed by (reading, offender key, period, or event and SHA)". Items are "idempotent by witness" (`cl-0092`).
- **Consequence:** When the patch's own fix regresses, the existing witness reads the re-patch as done. The regression is neither patched nor filed.
- **Fix:** Key the intake by (reading, offender key, base SHA). With a patch still open, a recurrence adds a `seen` row. With the patch landed, it opens a new patch on the shared budget.

### A3-F9 — Neither cadence program reaches its closing item, so the lease release and the record go unwitnessed
- **Address:** layer-expansions [Maintain items] `maintain.record`, `maintain.levels`; [Loop Review items] `loop.record`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** Stage 0 leads: "maintain.levels / maintain.record / loop.record: reached from no entry". The expansion tables have no Needs column. `maintain.patch` routes "Design", and `maintain.file` routes "Plan's triage". Only `maintain.record` "releases the lease".
- **Consequence:** A Maintain run that patches or files never writes its maintenance record and never releases its lease. The same holds for the Loop Review's record.
- **Fix:** Add Needs columns, and route every outcome of `maintain.read`, `maintain.direct`, `maintain.patch` and `maintain.file` (and of `loop.file`) to the program's record item.

### A4-F18 — `kits.adopters` routes on `deploy.currency`'s values without naming the key
- **Address:** layer-expansions [design-distribution] `kits.adopters`
- **Class:** K4
- **Severity:** low
- **Scenario:** S4
- **Evidence:**
  - The routes read "`pull-and-watch` → reported; `push-branches` → `kits.offer`; `pull-only` → …".
  - Stage 0 reports "K4 deploy.currency: read by no chain clause and no item", and the same for `kits.host`, `kits.cadence` and `kits.watch-cadence`.
- **Consequence:** The key-read join reds, or a rename of the key drops the routes unseen.
- **Fix:** Write "as `deploy.currency` says" in the routes, and name `kits.host` and `kits.cadence` in `kits.cut`'s and `kits.currency`'s cells as the keys they read.

### A4-F17 — `kits.offer` refuses "all eight" spawn kinds while cl-0435 adds a ninth
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K6
- **Severity:** low
- **Scenario:** S4
- **Evidence:**
  - layer-expansions:456: "the design adds an eighth; the mode refuses all eight".
  - cl-0435: "step processes a ninth spawn kind its mode refuses unless they run under the step kind's isolation contract".
- **Consequence:** A spec writer working from the item omits the step-process kind and its isolation exception.
- **Fix:** Name the ninth kind and its exception in the item.

### A4-F8 — `kits.offer`'s push grant "scoped to `gov/update-*`" is a scope the grant probe cannot see
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **Evidence:**
  - layer-expansions:456: "pushes `gov/update-<release>` through that adopter's own grant, scoped to `gov/update-*` on its one remote".
  - :394: "Registration probes the scopes granted, and refuses wider than declared".
  - No record names how a ref-prefix scope is granted or probed. A repository token's write scope is not per-ref.
- **Consequence:** Gov's node holds write grants to every adopter's remote. The probe either refuses every real token or certifies a repository-wide write grant as prefix-scoped (elevation).
- **Fix:** Declare the enforcement, such as a remote-side ruleset restricting the grant's identity to `gov/update-*`. Make the registration probe a refused push to a non-prefixed ref, seen red on a token that can push outside the prefix.

### A4-F4 — `kits.install` and `kits.update` have two actors, one route and no outcome for the step walk
- **Address:** layer-expansions [design-distribution] `kits.update`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S4
- **Evidence:**
  - layer-expansions:457: the actor is "the owner, or a command". The only route is "an adapter that declares no target → its slot renders not installed".
  - Stage 0's leads: "K2 kits.update: ends nowhere" and "K1 kits.update: actor 'the owner' is no kind".
  - The outcomes of dSafePassage's walk have no route: step k exiting 1 with the receipt at k-1 (cl-0022), a reclaimed lock (cl-0019), the downgrade refusal (cl-0021), a `retired-edited` order (cl-0026), a step needing target code being attended (cl-0024), and `instructions.stale: refuse` holding the update.
- **Consequence:** S4's central item cannot reach a terminal with its witness. A killed or failed step has nowhere to route, and its owner is never told.
- **Fix:** Split the row into one item per actor, for example `kits.update` (command) and `kits.update-attended` (owner). Give each a closed outcome set (done, step k failed → receipt at k-1 and an owner item, held → order, attended → outbox order, refused → ask), each routed.

### A2-F8 — Two nodes pushing one build branch: the race is undeclared under the default shared worktree
- **Address:** layer-runtime [isolate], and architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0318` and dPlacedRequest `cl-dClosedLoop-0133`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - layer-runtime:716-719: "shared: the build's one worktree … The commit queue then commits them one at a time". That queue is local to one node.
  - The `build.worktree` default is `shared`, and `build.push` is `every-pass`.
  - 0318 has each role agent "pushing the build's branch".
  - 0133 fences each push on the pusher's own lease tip only.
  - No record names the route when an atomic push is refused because the branch moved.
- **Consequence:** Node x holds only a unit lease, yet pushes X's build branch beside node d's pushes. The second push is refused non-fast-forward, and the refusal cannot be told from a fence refusal. The pass is either dropped or retried with no budget rule, and under `shared` node x has no worktree at all.
- **Fix:** A unit leased on another node always gets a unit branch (per-unit). The build branch is written only by the build-lease holder's merge, as [isolate]'s "Integration before release" says. A refused push routes by class (fence lost vs branch moved, rebase and retry as contention). Seen red on two nodes pushing one branch.

### A2-F2 — The hand-over at the session-limit ceiling releases the build lease but not the in-flight unit's lease
- **Address:** layer-runtime [supervise] "Session limits", and architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0325`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - layer-runtime:404-406: the supervisor "keeps renewing its lease, the hold being a declared wait inside its deadline … once the hold passes `runtime.hold-ceiling`, the supervisor … releases the build's lease as a hand-over".
  - 0325: "the session-limit hold releasing the build's lease as a hand-over".
  - The default `leases.granularity: build-and-unit` gives d's in-flight unit its own lease. No record says that lease is released, tombstoned or left to expire. 0332's pick offers only "hand-over releases and expired leases".
  - Under the default `build.worktree: shared`, the partial pass sits only in d's worktree, so `resume.partial: continue-item` has nothing to continue on another node.
- **Consequence:** d hits its limit mid-unit. After 6 hours the build lease passes to a node with quota, but the unit lease stays with d. If d keeps renewing it as a declared wait, no node can ever claim that unit. If d stops, the unit waits out `leases.expiry-hours` (24h). Either way X's Build step cannot finish, and Y, which waits on X, cannot either.
- **Fix:** At `runtime.hold-ceiling`, release every lease the held supervisor holds for the build (build and unit leases) as hand-overs, and push the in-flight pass's partial commit, or record it as lost so `resume.partial` restarts the item. Probe: a limit planted mid-unit is followed by a second node claiming that unit within one tick.

### A3-F18 — layer-runtime gives dDeclaredLoop the coordination feature that v2 places on dPlacedRequest
- **Address:** layer-runtime [supervise] "What stays where it is"
- **Class:** K8
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** layer-runtime: "dDeclaredLoop keeps: … the coordination feature (`gap-conc-01`, `gap-conc-02`)". v2 `[chain]` has dPlacedRequest owning "the coordination feature: one lease grammar" and `gap-conc-01` and `gap-conc-02`.
- **Consequence:** Two builds each read as owning the lease grammar that S5's tombstones rest on.
- **Fix:** Re-point layer-runtime's line to dPlacedRequest.

## Clean cells to attack

- `deploy.mandate` in S3
- `deploy.mandate` in S6
- `deploy.core` in S7
- `test.flakes` in S5
- `review.pin` in S6
- `plan.reason` in S2
- `test.seen-red` in S7
- `entry.place` in S2

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `AS4-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a4/` only. Your effort is the one the owner's
role definition sets.

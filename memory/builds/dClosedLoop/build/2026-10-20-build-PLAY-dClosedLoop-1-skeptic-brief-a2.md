# Skeptic brief: run A, batch 2

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a2/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### A5-F5 — A build parked on the owner's silence loses its lease, and nothing takes it back
- **Address:** architecture-v2 [policies] `run.on-owner-silence` `cl-dClosedLoop-0326`; flow-steps [breakpoint]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - v2 `[policies]` `run.on-owner-silence` and `cl-dClosedLoop-0326`: parking releases the build's lease and leaves the item open.
  - `cl-dClosedLoop-0134`: "each release a hand-over, which any node may take".
  - `[lifecycle]`: "Resume enters its `next`". `plan.lease`'s instance is already witnessed, so `next` never re-runs it.
  - Design's contract takes "a planned, leased build".
- **Consequence:** After the 24-hour silence at Plan's ratification, another node may take over a build that is waiting for the owner. When the owner's late go arrives, the build enters Design holding no lease.
- **Fix:** Release the lease of a build parked for the owner as terminal-for-takeover, or keep it renewed as a paused build's is. Declare a lease re-take item on the owner's disposition of a parked build.

### A2-F5 — No item or actor answers a mailbox `question`, while it blocks the recipient's transitions for 72h, past its 24h lease
- **Address:** coordination [6] "The mailbox", architecture-v2 [chain] dKeptSession `cl-dClosedLoop-0162`, and flow-steps [rules]
- **Class:** K1
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - coordination:115-117: "Every transition … is refused while a message addressed to the build is neither answered nor acknowledged … until `flow.wait-ceiling` passes and the asker's declared default answers it".
  - flow-steps [rules] only "reads the build's mailbox". No item's actor answers or acks a `question`.
  - `leases.renewal: progress` renews only on witnessed progress or "declared waits". A refused transition on the recipient is declared as neither.
  - `leases.expiry-hours` is 24, and `flow.wait-ceiling` is 72.
- **Consequence:** Y asks through X's mailbox. X runs unattended and nothing in it answers, so X's next step transition is refused for up to 72h. Its build lease stops renewing and expires at 24h. X then shows as expired with no ready work, and it resumes only when Y's node writes the default.
- **Fix:** Declare the answering item: the role that owns the asked interface, dispatched by `next` when a `question` arrives. Declare the recipient's refused transition as a wait inside the asker's deadline, so it renews. Seen red on a planted question to an unattended build.

### A2-F10 — Coordination refs trust a writer's self-declared identity (STRIDE: spoofing, tampering, denial)
- **Address:** coordination [6], and architecture-v2 [chain] dKeptSession `cl-dClosedLoop-0143` and dWellOiledMachine `cl-dClosedLoop-0335`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:**
  - The message "sender (fleet tag, session, build)" is a field the writer types.
  - The ref is `refs/gov/mail/<slug>/<fleet tag>/<session>`.
  - 0335 scans for secrets and an agent-forged request record, but no clause checks that the writer of a mail, lease or tombstone ref is the node or session it names.
  - layer-runtime: under Codex, "the binding, return and fail-closed invariants hold only at the git boundary".
- **Consequence:** An act session on node x, which runs Codex with no fail-closed hooks, can write an `ack` or `answer` in X's name, which unblocks X's transitions, or a terminal tombstone on X's lease, which refuses every take-over. A compare-and-swap does not stop a writer that read the tip.
- **Fix:** Bind each coordination write to its writer: the act's binding record or a signing key in the node profile. Refuse at the record door a ref whose path names another writer. Seen red on a planted cross-session mail write and a forged tombstone.

### A4-F16 — The fates table gives govkit's `update` to dShippedRelease alone and marks govkit optional
- **Address:** fates [table] govkit "install and update, receipt"
- **Class:** K8
- **Severity:** low
- **Scenario:** S4
- **Evidence:**
  - fates:111 reads "RESHAPED | release tags, receipt names its release, `kits.offer` (dShippedRelease)", and `[kits]` reads "govkit | optional".
  - dSafePassage's cl-0018 to cl-0027 reshape `update` into the step walk, which P38, a core principle, rests on.
- **Consequence:** dConvergedCharter's exit check (cl-0488) grades govkit's update against the wrong owner, and P28 reads it as optional.
- **Fix:** Add dSafePassage to the row and state which half of govkit is core.

### A3-F2 — The post-close row still sends a post-landing red to triage as an ask
- **Address:** flow [Entry points, settled 2026-10-14]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** The row reads "A failed verify after its build closed at landing | Plan's triage | filed as an ask, then a patch build or a planned build by its size". layer-flow `[settled]` says the row "now covers … a post-landing core red, each entering as a patch build", but the table was never revised. `deploy.core` routes to "a patch build through the entry-point table's post-close row".
- **Consequence:** A spec writer for `deploy.core` reads two contradictory entry paths: an ask through triage, or a patch at Design.
- **Fix:** Revise the row: a post-landing core red or a landing-review finding enters at Design as a patch build, and a post-close failed verify enters at triage.

### A4-F15 — `adopt.decisions` has two actor kinds
- **Address:** flow-steps [adopt] `adopt.decisions`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Evidence:**
  - flow-steps:614: "reviewer, as two raters, and the owner where `retrofit.decisions` says".
  - layer-roles:409 lists `adopt.decisions` under reviewer only.
  - `[rules]`: "an item whose actor a policy value chooses is one item per value".
- **Consequence:** The owner's ruling has no item of its own, so no witness or route is declared for it.
- **Fix:** Split the row into `adopt.decisions` (reviewer) and an owner item under `retrofit.decisions`.

### A5-F7 — The review ceiling has no arm in the review program
- **Address:** flow-steps [breakpoint] `review.dispose`, `review.fold`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - Probe: `grep -c "max-rounds\|CEILING"` over flow-steps finds 0 hits for either term.
  - `review.dispose` routes "a follow-up round as `review.follow-up` says", and `review.fold` routes "the next round as `review.design.rounds` says".
  - v2 `cl-dClosedLoop-0117` ("the round after the limit refused and the report reading CEILING") and `cl-dClosedLoop-0084` (dFairHearing computes CEILING) give no route once the report reads CEILING.
  - Design rounds also "count against `flow.route-backs`" (3), and `review.max-rounds` is also 3. Two different endings (non-converging to asks, and CEILING) fall on the same round.
- **Consequence:** S6's review at its CEILING has no declared next item. A spec writer for dFairHearing or dDeclaredLoop cannot say where the CEILING report's open highs go.
- **Fix:**
  - Add `review.max-rounds` to `[breakpoint]`'s policy list.
  - Give `review.dispose` and `review.fold` a CEILING arm, consistent with `cl-dClosedLoop-0117`'s promotion rule.
  - Order the two bounds.

### A1-F5 — An owner-declared spec audit has no writer for its trigger record and no route from the owner's words
- **Address:** flow-steps [breakpoint] `review.trigger`; flow-steps [entry] `entry.place`
- **Class:** K3, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `review.trigger` is "Proven by ... the owner's request record".
  - Probe: `grep -rn "owner's request" <copy>/memory/builds/dClosedLoop/build | grep -v research-` finds the phrase only in the trigger and probe rows and in prose. No kind row exists in layer-memory's table: `grep "^| " layer-memory.md | grep -iE "request|disposition"` shows only `attendance override` and `disposition`.
  - The owner's mid-build prompt passes `entry.place`, whose closed set (continue, amend, new, patch, repeat, ask, none) routes "continue → that build's `next`". None of those outcomes records a breakpoint request.
  - `life.request` covers only "pause, resume, withdraw or supersede ... attend or unattend".
- **Consequence:** S1's injected "spec audit the owner declares" is not a placement outcome, so the owner's prompt is dropped. No item writes the trigger's witness. The build passes `design.ready` and lands without the audit, which is a terminal reached without its witness.
- **Fix:** Register an owner request record kind with its writer. Either add a `review` or `breakpoint` outcome to `entry.place` and to `life.request`'s verbs, writing that record at the named boundary, or name `disposition` as the witness and state its writer. Add a probe: a planted owner prompt "audit the specs" must produce `review.trigger` before `design.ready`.

### A1-F4 — Attended confirmations and live questions are resolved when raised, with no declared wait, and a late owner answer has no route
- **Address:** flow-steps [breakpoint]; architecture-v2 [chain] dFurnishedOrders `cl-dClosedLoop-0207`; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - [breakpoint] says `run.on-owner-question` "resolves it when it is raised, never for a ratification: the supervisor's recorded choice under `best-effort-recorded`".
  - `attendance` "`confirm-steps` adds a gate at every step's exit" and "asks owner questions live".
  - The catalogue's `run.on-owner-question` row says the default `best-effort-recorded` "decides an owner item when the item is raised".
  - cl-0207 says "owner questions asked live while the build is attended, best effort recorded once the wait passes". It names no key for that wait. P39 and cl-0118 say "every wait declaring an outcome and a deadline".
  - Probe: `grep -rnE "late answer|answer arriv|arrives late|arriving late" <copy>/memory/builds/dClosedLoop/build` found no route for a late answer, only the walk's own S1 row.
  - LR-3's fork was put about "an unattended run". Nothing says how an attended gate waits.
- **Consequence:** In S1, every confirm-steps gate is decided by the supervisor at once, under the default. Examples are `plan.exit` beyond the ratification, `design.exit`, `build.exit` and `test.exit`. `plan.record`'s owner question is decided the same way, so the attended owner confirms nothing. If the owner's answer arrives late, it meets an item that is already witnessed and has nowhere to route. The guard attendance promises silently loosens.
- **Fix:** Pick one reading and state it in [breakpoint], cl-0207 and `run.on-owner-question`:
  - either an attended gate or question is held until a declared deadline, using `flow.wait-ceiling` or a new key, and the key applies only after it;
  - or attendance's gates are declared outside `run.on-owner-question`.
  
  Then route an answer that arrives after a recorded choice: as a re-entry that draws on `flow.rework-budget`, or recorded with no effect. Add a planted attended gate that must not resolve at raise.

### A1-F8 — No route reaches `build.recommend`: "the unit built" is not an item, and its Needs are prose
- **Address:** flow-steps [build] `build.reuse-check`, `build.recommend`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `build.reuse-check` routes "clean → the unit built".
  - `build.recommend` needs "every unit built and reuse-checked".
  - Stage 0's lead says "K2 build.recommend: reached from no entry", and the same for `build.ratify`, `build.distill`, `build.core` and `build.exit`.
- **Consequence:** In S1, after the last unit's reuse check, no declared route or need puts `build.recommend` on the frontier. Build's tail and its exit cannot be reached from the declarations, and with them the closing review it owes by default (`review.build: owed`).
- **Fix:** Route "clean → `build.recommend` once every unit's `build.reuse-check` is witnessed clean", and write the need as `build.reuse-check` for every unit in the roster.

### A2-F9 — Landing order is node-local, so P21's plan-priority order does not hold across nodes
- **Address:** flow-steps [deploy] "The landing order", and architecture-v2 [chain] dShippedRelease `cl-dClosedLoop-0422`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** flow-steps: "Landings on a node are ordered by `landing.order`". P21 says "landings go in plan priority, then first verified", and 0422 builds the landing queue. No ref shared across nodes orders it.
- **Consequence:** Builds verified at once on d and on x land in push-race order. The first landing makes the other's verdict stale (contention, which draws nothing). `landing.order: owner-orders` and plan priority have no effect across nodes.
- **Fix:** Order landings through a compare-and-swap landing-turn ref on the remote, or narrow P21 and `landing.order` to one node and record the cross-node rule as first-pushed.

### A3-F1 — A post-merge red leaves the originating build with no path to `landed`
- **Address:** flow-steps [deploy] `deploy.core`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core` Then: "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". No other route leads to `deploy.record`. `deploy.close` Needs only "`deploy.unlease` and `deploy.released`", so no item writes or reads a filing witness. `[transitions]` has no `deploying` row for a post-merge red, and "the engine refuses any transition the table lacks".
- **Consequence:** The originating build never records its landing, never unleases and never closes. Its lease stays held until it expires, and "the close waits" has no witness to wait on.
- **Fix:** Route red to `deploy.record` with the landing recorded red. Name the patch intake's key in the landing record, and add that key's witness to `deploy.close`'s Needs.

### A3-F7 — Once the budget is spent, a post-merge red ends in a closed-incomplete patch and a red default branch
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0116`
- **Class:** K10
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core` raises the patch unconditionally. `cl-0116`, under the default `best-effort-ending`: "closing the build incomplete … raising the budget the owner's alone". No owner item is raised for it.
- **Consequence:** The patch closes with only an ask filed, and the default branch stays red. Every later build's `test.route` then meets an INHERITED red and mints fix units on its own budget.
- **Fix:** When the shared budget is spent, a post-merge red opens an owner item to raise the budget or revert, whatever `flow.on-exhausted` says. Show it on a planted spent chain.

### A3-F5 — One post-merge red raises two patch builds, and one of them escapes the shared budget
- **Address:** flow-steps [deploy] `deploy.core`; layer-expansions [Maintain] `default-branch-red`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core`: red → a patch build. The code at `tools/run-gates/post-merge.sh:249` is `PM_RED_REF=refs/gov/bar-red`, so a red is published. layer-expansions says the `default-branch-red` event is "produced by the core's runner-written bar verdict … which `refs/gov/bar-red` indexes", and `maintain.events` defaults to all three events. `maintain.patch` then opens a second patch. Patch builds skip `plan.dedupe`. `cl-0440` shares the budget only for "a patch build raised by a landing".
- **Consequence:** Two patch builds race to fix one red. The Maintain one starts on a fresh budget, so the chain of patches is no longer bounded (P39).
- **Fix:** Use one producer and one key, (`default-branch-red`, landed SHA). `deploy.core` files under the key Maintain's reading uses, and `maintain.patch` finds it. Extend `cl-0440` to a Maintain patch whose offender is a landed SHA, seen red on a planted double filing.

### A2-F4 — `deploy.parents`' hold declares no deadline or outcome, so it fails the design's own static check
- **Address:** flow-steps [deploy] `deploy.parents`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S2
- **Evidence:**
  - The Then cell reads "a parent unlanded or paused → holds", with nothing past it.
  - v2's `flow.wait-ceiling` row names "a dependency hold" as a wait that takes its declared outcome past 72h.
  - 0118 reds "a wait declaring no deadline".
  - flow-steps says its items are "the draft that dDeclaredLoop's loop definition declares".
- **Consequence:** Y on node x waits at `deploy.parents` for X. If X stalls (A2-F2, A2-F3), Y holds forever, which breaks P39. The loop definition built from this draft also fails dDeclaredLoop's own static check.
- **Fix:** Add a branch to the Then cell: past `flow.wait-ceiling`, an owner item, or as `deps.on-parent-withdrawn` says. Seen red on a planted parent that never lands.

### A3-F10 — `deps.on-parent-withdrawn` has no per-value semantics, routes or transition rows, and is read only at Deploy
- **Address:** flow-steps [deploy] `deploy.parents`; [transitions]; architecture-v2 [chain] `cl-dClosedLoop-0100`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** `deploy.parents` routes "a parent withdrawn … → as `deps.on-parent-withdrawn` says". layer-flow only names the values: "`replan` by default, with `adopt-parent-work` and `withdraw-too` allowed". No record defines them, and `cl-0100` builds the key with no arm per value. `[transitions]` has no deploying, building or designing → planning row for `replan`. Stage 0 K4 reports `deps.coordination` and `deps.early-build` "read by no chain clause and no item". No item consumes `life.notify`'s `withdrawn` post before `deploy.parents`.
- **Consequence:** Y, waiting on X's interface in Design or Build, never reacts to the withdrawal. At Deploy, the default `replan` has no transition, so the engine refuses it and Y is stuck.
- **Fix:** Define each value's route:
  - `replan`: a plan revision, with designing/building/deploying → planning rows.
  - `adopt-parent-work`: `design.inventory` over X's kept branch.
  - `withdraw-too`: `life.request` with a command actor.

  Also add a boundary item that consumes `withdrawn` and `superseded` posts, and arm each value on a planted case.

### A3-F11 — Y's dependency hold at `deploy.parents` declares no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`; architecture-v2 [policies] `flow.wait-ceiling`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** "a parent unlanded or paused → holds". `flow.wait-ceiling` is "the deadline gov's own waits declare, a dependency hold …", but only `cl-0162` (mailbox) and `cl-0368` (CONTENDED) bind it. Deploy's policy list omits it. `cl-0118` reds "a wait declaring no deadline".
- **Consequence:** A parent paused or held indefinitely keeps Y waiting forever, which is the condition `gap-flow-10` names. `cl-0118`'s check, once built, reds gov's own floor.
- **Fix:** Route `holds` past `flow.wait-ceiling` to an owner item, or to `deps.on-parent-withdrawn`'s route. Add a dShippedRelease clause seen red on a planted parent paused past the ceiling.

### A3-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`, `design.overlaps`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** "patch → `design.unit-spec`, as a micro-spec". `design.overlaps` "runs the design index over the roster's write sets, against live builds". `design.unit-spec` "acknowledges the unit's overlaps", but no overlap record exists for a patch.
- **Consequence:** Concurrent patch builds, or a patch and a live build, on the same paths are first seen at `build.unit-lease`, which only warns by default.
- **Fix:** Route patch → `design.overlaps` → `design.unit-spec`.

### A1-F10 — `design.ready`'s witness omits the UNCARRIED class that cl-0398 gives it
- **Address:** flow-steps [design] `design.ready`; architecture-v2 [chain] dIndexedDesign `cl-dClosedLoop-0398`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - flow-steps:192 says "derived READY: none MISSING, THIN or FORKED".
  - cl-0398 says "`design.ready` gaining an UNCARRIED class", with `design.coverage` defaulting to `refuse`.
- **Consequence:** A spec writer carrying the item builds READY without the coverage join. In S1, a unit spec that drops a clause derives READY under the item's text, while dIndexedDesign's clause says it must be refused.
- **Fix:** Add "or UNCARRIED, under `design.coverage`" to the witness of `design.ready`.

## Clean cells to attack

- `design.ready` in S3
- `review.pin` in S1
- `test.seen-red` in S5
- `build.acceptance` in S5
- `build.scope` in S6
- `deploy.unlease` in S6
- `build.base` in S7
- `build.scope` in S3

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `AS2-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a2/` only. Your effort is the one the owner's
role definition sets.

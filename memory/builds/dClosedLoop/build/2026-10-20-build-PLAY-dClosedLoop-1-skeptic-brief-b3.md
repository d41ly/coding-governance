# Skeptic brief: run B, batch 3

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b3/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### B2-F1 — "where it ran" needs put Design's and Build's exits on the frontier before the breakpoint is decided
- **Address:** flow-steps [design] `design.ready`; also [build] `build.ratify`, `build.distill` (and the same pattern at [test] `test.exit`, [deploy] `deploy.notify`)
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** [rules]: "`next` returns the frontier, the unwitnessed items whose needs are witnessed". `design.ready` Needs: "`design.recommend`, and the spec audit where it ran". `design.reason` (Needs `design.recommend`) is the item that decides "a review → the spec audit". `build.distill` Needs: "`build.recommend`, the closing review where it ran". The default `review.recommendation.source` is `scored-signals-and-reasoning` (v2 [policies]).
- **Consequence:** Once `design.recommend` is witnessed, `design.ready` and `design.reason` are both on the frontier. `design.ready` can derive READY and `design.exit` can record the transition before the reason item owes a spec audit, or before an owed audit starts. Under default `decisions.major: author-rubric`, `build.distill`, `build.core` and `build.exit` follow from `build.recommend` alone, so the owed closing review is passed silently. Stage 0's K1 reads only the tags in a Needs cell, so it cannot see this.
- **Fix:** Make the breakpoint an explicit need. `design.ready` needs `design.reason` (or `design.recommend` under `signals-only`) plus the breakpoint's disposition record whenever the trigger fired. The same applies to `build.ratify`/`build.distill` (the closing review), `test.exit` and `deploy.notify`. Add a static check that reds a Needs cell holding an untagged conditional, seen red on today's `design.ready` row.

### B2-F17 — `design.streams`' Needs reads as needing itself
- **Address:** flow-steps [design] `design.streams`
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Evidence:** Needs: "`design.overlaps`, where `design.streams` holds for the build". stage0-leads.md: "K1 design.streams: a cycle among Needs: design.streams > design.streams".
- **Consequence:** The composer's graph check (flow-roles-adoption [design] 11, "the needs graph acyclic") reds gov's own item, or a reader skips it.
- **Fix:** Write the condition as `policy.design.streams`, the full spelling the opening reserves, outside the Needs tags.

### B1-F5 — A patch claim records no originating build, so the shared rework budget cannot be keyed
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Evidence:**
  - The claim commit carries "the claimant's key, the session and the intake's or the ask's content key".
  - stall-and-loop:168 says a patch build of a landing "shares the originating build's budget, so a chain of patch builds draws on one budget". `flow.rework-budget` says the same.
  - Neither `entry.place` nor `entry.claim` names the originating build, and neither has a route for "originating budget spent".
- **Consequence:** In S3, the patch's own red landing and an originating budget that is already spent are both unroutable. Each patch starts at zero, which is the C48 chain the budget exists to stop.
- **Fix:** On `patch`, the claim commit carries the originating build's slug and landed SHA. Add a route: originating budget spent → `flow.on-exhausted` of the originator, filed as an owner item.

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

### B1-F1 — entry.intake is acted and witnessed by the orientation scout, not by the prompt-submit hook
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** The item's Actor cell is "orientation scout, in an owner-bound session only", and its Proven-by cell is "the intake entry the scout writes". Several records say the opposite:
  - flow-steps' own `[rules]` say "No witness is typed by the acting agent".
  - The same record's `[revised]` row `hook-actor-kind` says "`entry.intake` is a hook".
  - Clause `cl-dClosedLoop-0282` reads "the prompt-submit hook writing each owner prompt verbatim … (`entry.intake`, PM-9)".
  - flow-roles H2 says the hook writes "the witness for intake and, under `plan.ratification: request`, for the mandate".
  - flow-roles-adoption:202 lists `entry.intake` among items whose witness is "written by a runner or a hook".
  - Probe: `grep -n 'entry.intake' …flow-steps.md …flow-roles-adoption.md` and `grep -n 'hook-actor-kind' …flow-steps.md`.
- **Consequence:** In S2 the mandate an unattended build runs on is a record that an agent types. A session can forge or edit "the owner's prompt", and `deploy.mandate` accepts "the intake record" as landing authority. That is spoofing and elevation of privilege across the node boundary. P2, P4 and P23 are broken at the root.
- **Fix:** Restore the actor as "hook: Runtime's prompt-submit hook, in an owner-bound session only". Restore the witness as "the intake entry the hook writes verbatim, redacted and capped". Keep the scout only as the reader in `entry.orient`.

### B1-F11 — entry.orient hard-codes `kickoff.runs`' default
- **Address:** flow-steps [entry] `entry.orient`
- **Class:** K4
- **Severity:** low
- **Scenario:** S1
- **Evidence:** The Does cell reads "the full kickoff's where no READY card exists". `cl-dClosedLoop-0376` says "only where `kickoff.runs` says". `[entry]`'s Policies line omits `kickoff.runs`.
- **Consequence:** `every-session`, `opening-a-build` and `plan-absorbs` have no effect.
- **Fix:** Change the cell to "as `kickoff.runs` says", and add the key to the Policies line.

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

### B4-F6 — A replacement build never reaches `design.inventory`, so supersession's kept work has no route
- **Address:** flow-steps [lifecycle]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - [lifecycle]: "A superseded build's kept work passes to its replacement through the replacement's `design.inventory`".
  - `design.input` routes "plan record → `design.seams`; ... plan revision → `design.inventory`". `design.inventory` judges "each completed unit" after a plan revision.
  - layer-flow F-E cites "the re-design inventory already settled for planning misses".
- **Consequence:** Z enters with its own plan record and goes to `design.seams`. X's built units are never inventoried, so the kept work is dropped.
- **Fix:** Add a `design.input` kind "superseding plan record", routed to `design.inventory` over the superseded build's units. Have `life.request` supersede name Z's slug before `life.notify`.

### B4-F5 — A paused build's lease is renewed with no progress and no deadline
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** high
- **Scenario:** S5
- **Evidence:**
  - [lifecycle]: "The supervisor renews them while it is paused, so `leases.expiry-hours` never expires a paused build". `life.quiesce` routes "pause → parked".
  - v2 `leases.renewal` default `progress`: "renews on witnessed progress at item boundaries and on declared waits inside their deadline".
  - layer-runtime [supervise]: "The beat is liveness and renews nothing by itself". P39: "Every wait carries a deadline".
  - `cl-dClosedLoop-0326` uses "parks" for a lease-released state.
- **Consequence:** Under the default, either the paused lease expires and `cl-dClosedLoop-0332`'s pick hands the paused build to another node (the S2 stale-beat path defeats the pause), or renewal runs on activity with no deadline, against P39 and `cl-dClosedLoop-0118`. "Parked" also contradicts "keeps its leases".
- **Fix:** Declare pause as a wait with a deadline (`flow.wait-ceiling` or its own key) and an outcome, renewed under `progress` as a declared wait. Rename the route to `paused`.

### B4-F7 — "Once a push is made, the build has landed" reads every pass push as a landing
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - `life.quiesce`: "Once a push is made, the build has landed, and a pause, withdraw or supersede is refused".
  - v2 `cl-dClosedLoop-0318`: each role agent pushes "the build's branch as `build.push` says, every pass commit by default".
  - The layer-runtime `lifecycle` fixture tests only landed builds.
- **Consequence:** Read as written, X's first pass push refuses the owner's withdraw mid-Build, and no fixture would catch it.
- **Fix:** Say "once the landing push to the default branch is made". Add a fixture that withdraws after a pass push and is refused only after the landing push.

### B4-F8 — `life.quiesce` reaches only the driver's own acts
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - `life.quiesce` is witnessed by "the executor's record of the acts it let finish", and "An open review fan finishes".
  - v2 `cl-dClosedLoop-0319`: a unit holder in another session or node drives "that unit's passes on its own branch".
  - No route says what `review.report` and `review.dispose` do with a finished fan's findings once the build is withdrawn.
- **Consequence:** A remote holder's acts run on unrecorded until the fence refuses their push after `life.unlease`. The finished review either disposes units into a withdrawn build or loses its findings silently.
- **Fix:** Have `life.quiesce` post a quiesce message to every unit holder and join their acknowledgements into its witness. Route a finished review's findings to asks under withdraw and to the replacement under supersede.

### B1-F9 — Plan reads the design index and `run.host`, which no ancestor of dRankedPlan builds
- **Address:** flow-steps [plan] `plan.dedupe`, `plan.exit`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - `plan.dedupe` checks "against live builds, the design index and open asks". The design index is `cl-dClosedLoop-0384`, in dIndexedDesign's row.
  - `plan.exit` says "the executor launched where `run.host` says", and `run.host`'s owner is dWellOiledMachine.
  - dRankedPlan's parents are dDeclaredLoop, dTotalRecall and dBoundRoles, so neither owner is an ancestor.
  - Stage 0 K2 flags `plan.exit` as "a target in no declared form".
- **Consequence:** dRankedPlan's dedupe and exit cannot run as specified when it lands.
- **Fix:** Add stand-ins: dedupe against live builds and asks only, with the index arm joining when dIndexedDesign lands; `run.host` read as `requesting-node` until dWellOiledMachine lands. Write the exit target in a declared form.

### B1-F2 — Under `plan.ratification: request`, plan.exit takes the owner's go "as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** The Does cell reads "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification". Other records disagree:
  - `[consequences]` says "`plan.exit`'s witness carries it".
  - v2 `[contracts]` says "Plan's witness is the hook-written intake (FR-1)".
  - `cl-dClosedLoop-0377` says "its intake read as the request's ratification".
  - `cl-dClosedLoop-0137` says "a relayed request being data with provenance and never consent".
  - Probe: `grep -n -i 'planner records\|request is the ratification' build/*.md`.
- **Consequence:** By default the ratification is something the planner, an agent, types. In S2, where nobody attends, any planner return ratifies its own plan, and the Plan gate certifies what it does not check.
- **Fix:** Change the clause to "under `request`, the hook-written intake record that the build's claim names stands as the ratification; before that hook lands, `cl-dClosedLoop-0378`'s owner gate applies". Remove "as the planner records it".

### B4-F9 — `probe.judge` mixes three actor kinds
- **Address:** flow-steps [probe] `probe.judge`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - The actor is "command: the executor's re-run, or the experiment's scorer". The witness adds "where no command can judge, the verifier's judgment, recorded as claimed".
  - [probe] Roles adds "a blind judge".
  - [rules]: "One actor per item, of one kind ... an item whose actor a policy value chooses is one item per value".
- **Consequence:** The executor, a command and a role all act in one item. The builder cannot give it one work order, allowance or return schema, and the role arm has no actor.
- **Fix:** Split it into `probe.judge` (command or executor re-run, or scorer) and `probe.judge-claimed` (the tester or blind judge), routed when no command can judge.

### B4-F10 — The reproduction probe before a patch fix has no trigger
- **Address:** flow-steps [probe] `probe.trigger`
- **Class:** K6
- **Severity:** medium
- **Scenario:** S3
- **Evidence:**
  - v2 `cl-dClosedLoop-0408` (dScopedBuild): "a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report".
  - `probe.trigger`'s closed set is "the boundary `probe.points` names, the owner's request, the observation `probe.observations` owes, or a role item's `probe` outcome".
  - `design.input` sends a patch straight to `design.unit-spec`.
- **Consequence:** Nothing opens the reproduction, so a patch fix lands without its red-first witness.
- **Fix:** Add the trigger "a patch build from a bug report" to `probe.trigger`, at the boundary before the patch's first `build.unit-pass`. Name it in `design.input`'s patch route.

### B3-F3 — Patch builds have no link to the originating build's budget
- **Address:** flow-steps [rules] (the "Every route back is bounded" bullet); flow-steps [entry] `entry.claim`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K6, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** flow-steps [rules] lists only "A route back, a fix pass, a review round after the first, a re-dispatch after a refusal and a research or probe round trip" as drawing on the budget. v2's `flow.rework-budget` adds "patch build of the build's own landing", and `cl-dClosedLoop-0440` builds "a chain of patch builds shares one budget". `entry.claim`'s claim commit carries only "the claimant's key, the session and the intake's or the ask's content key". The census in stall-and-loop says every new build "starts at zero".
- **Consequence:** A patch build is claimed under a fresh slug, and nothing records which build it came from. So `cl-dClosedLoop-0440` has no key to charge. When the patch's own landing goes red again, S3 starts a new budget instead of drawing on the old one. "The originating build's budget spent" has no declared outcome, and the originating build may already be closed (F2).
- **Fix:** Add "a patch build of the build's own landing" to flow-steps [rules]. Make the post-close patch intake and `entry.claim` record the originating build's slug, and the budget key derived from it. Point `flow.on-exhausted` at the originating build's chain. Seed a red case: a patch chain whose second patch shows a fresh budget.

### B3-F13 — `test.exit` writes to a lease record that dWitnessedBar's parents don't build
- **Address:** flow-steps [test] `test.exit`; architecture-v2 [chain] dWitnessedBar row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `test.exit` records "the verified tree on the build's lease record", and Test's exit needs "the verified tree is on the build's lease record". layer-memory: "| lease | dPlacedRequest |". dWitnessedBar's only parent is dDeclaredLoop, and the design map puts dPlacedRequest after dDeclaredLoop, not before dWitnessedBar. No stand-in is declared.
- **Consequence:** When dWitnessedBar is specced and built, its exit item writes into a record kind no ancestor provides, and dShippedRelease's landing order reads it later.
- **Fix:** Declare a stand-in (for example, the verified tree on the transition record until dPlacedRequest lands), or add dPlacedRequest to dWitnessedBar's parents.

### B3-F8 — Several Test and Deploy outcomes end at an ask, leaving the build with no next step
- **Address:** flow-steps [test] `test.merge`; flow-steps [deploy] `deploy.land`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `test.merge`: "refused → an ask naming the lander's refusal". `deploy.land`: "or an ask for a carried commit"; "an argument → an ask on the adapter". Memory [asks]' acceptance for a lander refusal is "`--prepare` next succeeds for the build", but no item routes back to `--prepare`, and [transitions] has no row for these cases.
- **Consequence:** The build sits in `testing` or `deploying`. It has no next item, no wait deadline and no owner item, against P39's "every wait expires".
- **Fix:** Route each of these to a counted wait on the ask's acceptance that re-enters `test.merge`. Past `flow.wait-ceiling`, raise an owner item. Add the transitions rows.

## Clean cells to attack

- `plan.record` in S1
- `kits.currency` in S7
- `deploy.record` in S6
- `plan.record` in S6
- `design.recommend` in S2
- `design.seams` in S5
- `loop.file` in S2
- `entry.orient` in S6

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `BS3-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b3/` only. Your effort is the one the owner's
role definition sets.

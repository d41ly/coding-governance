# Walk return: run A, walker 2, S2

**Serves:** research PLAY-dClosedLoop-1

Dispatch 161's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-2-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because node d's session limit handed over X's build lease but left the lease on its half-built unit held, and node x's pushes collided with d's on X's single build branch. X never reached `deploy.close`, and Y waited at `deploy.parents` with no deadline.

### A2-F1 — P23's only enforcing clause, `cl-dClosedLoop-0093`, exists nowhere in the chain
- **Address:** architecture-v2 [enforcement] `P23`, and [chain] dDeclaredLoop `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2:1707 reads `| P23 | cl-dClosedLoop-0093 |`. `grep -rn "cl-dClosedLoop-0093"` over the copy's `build/` matches only that row. dDeclaredLoop's row jumps from `…verdict printed cl-dClosedLoop-0092` to `…witness cl-dClosedLoop-0094` (v2:1638). [clause-ids] says "Retired: none", and the next id to mint is 0497.
- **Consequence:** In S2, node x acts on X's witnesses, X's card and Y's interface keys, which come from another node and another harness. P23 says such a claim is acted on only when its key recomputes. No clause builds that check, so a stale or agent-typed claim pulled from the remote is acted on unchecked. The principle has no enforcer.
- **Fix:** Restore clause 0093 on dDeclaredLoop's row (claims trusted by key and source: recompute the key, refuse a source an agent typed, re-derive otherwise), seen red on a planted stale key. Or list 0093 under Retired and name another clause in P23's row.

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

### A2-F3 — The landing push releases the build's lease, so the Deploy items after the push run unfenced and no node can take them over
- **Address:** architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0337`, against flow-steps [deploy] `deploy.unlease` and `deploy.close`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - 0337: "the lander's push to main and the build's release with its landed notice carried in one atomic push".
  - 0134: a landed build's release is "terminal … which refuses every acquisition".
  - flow-steps puts `deploy.core`, `deploy.record`, `deploy.distill`, `deploy.notify`, `deploy.snapshot` and only then `deploy.unlease` after `deploy.land`, and `build.release-hold: whole-close` keeps "the leases" until `deploy.released`.
  - 0133: "every effect push carrying the holder's new lease beat".
- **Consequence:** After X's landing push from d, the snapshot and close pushes have no lease to fence them. If d's session limit hits now, the hold-ceiling hand-over (0325) has no lease to hand over: the build lease is a tombstone that refuses every take-over, and 0332 never offers a tombstone. X lands but never records `deploy.close`. `whole-close` is also contradicted, because its leases are released at the push.
- **Fix:** Make the landing push carry the lease beat only. Leave the release to `deploy.unlease` as flow-steps orders it, or state that the post-push Deploy items run under a close lease that any node may take after a hand-over. Seen red on a supervisor killed between `deploy.land` and `deploy.snapshot`, whose build a second node closes.

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

### A2-F6 — Only lease expiry has a declared clock; every other S2 deadline reads a node's raw clock
- **Address:** architecture-v2 [chain] dPlacedRequest `cl-dClosedLoop-0134`, `cl-dClosedLoop-0138`, and dKeptSession `cl-dClosedLoop-0162`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:**
  - 0135 alone says "judged by a declared clock, never the reader's raw clock".
  - 0138's offer deadline (`leases.offer-seconds`), 0162's `flow.wait-ceiling` deadline and 0134's "fetch is older than `leases.queued-claim-days`" name no clock.
- **Consequence:** If node x's clock runs ahead, x claims units offered to d before their offer expires, and Y writes its default answer while d still counts the wait as live. d and x then disagree on whether a deadline has passed.
- **Fix:** One rule for every cross-node deadline: elapsed time measured by the observer since it first saw the record, or a stamp corrected by the registered offset. Each deadline is seen red on a reader planted a day ahead.

### A2-F7 — The clock offset that corrects a holder's stamp has no declared reference, measurer or writer check
- **Address:** architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0293`, and layer-runtime [enforce] "The node registry gains runtime facts"
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:**
  - 0293: "the node's clock offset among them correcting a holder's stamp … seen red on a planted holder stamp skewed by an hour".
  - layer-runtime:837 lists "the clock offset" with no source.
  - cloud-and-scale:211 joins the two expiry rules with "or".
- **Consequence:** A skewed node cannot measure its own offset without a reference. A self-reported offset lets x's stamps look fresh for ever, a denial against take-over. Because the two rules are joined by "or", which one decides x's lease is undefined. The planted check passes whatever offset the plant supplies, so it certifies nothing.
- **Fix:** Name the reference (for example the remote's push time read through the host API, or an NTP probe), the measuring command, and which rule wins. Seen red on a node that misreports its own offset.

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

### A2-F9 — Landing order is node-local, so P21's plan-priority order does not hold across nodes
- **Address:** flow-steps [deploy] "The landing order", and architecture-v2 [chain] dShippedRelease `cl-dClosedLoop-0422`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** flow-steps: "Landings on a node are ordered by `landing.order`". P21 says "landings go in plan priority, then first verified", and 0422 builds the landing queue. No ref shared across nodes orders it.
- **Consequence:** Builds verified at once on d and on x land in push-race order. The first landing makes the other's verdict stale (contention, which draws nothing). `landing.order: owner-orders` and plan priority have no effect across nodes.
- **Fix:** Order landings through a compare-and-swap landing-turn ref on the remote, or narrow P21 and `landing.order` to one node and record the cross-node rule as first-pushed.

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

### A2-F11 — `roles.model.<role>` holds one model while `roles.harness.<role>` admits several harnesses
- **Address:** architecture-v2 [policies] `roles.model.<role>` and `roles.harness.<role>`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S2
- **Evidence:**
  - v2:1063: values are "the models the harness adapter offers", and the key holds a single model.
  - v2:1064: `roles.harness.<role>` is "one or more of the harness adapters".
  - 0332's pick drops work "whose roles need a harness, model or hardware the node profile lacks".
- **Consequence:** With the builder's model set to one Claude model, node x (another harness) lacks that model, so the pick never offers it X's unit. S2's premise of a cross-harness unit take works only while the key is unset.
- **Fix:** Key the model per harness (`roles.model.<role>.<harness>`), or make the value a map from harness to model. The preset check reds a role whose harness set has no model for one of its members.

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S2 | = | = | = | = | holds |
| `entry.orient` | S2 | = | = | = | = | holds |
| `entry.place` | S2 | = | = | = | = | holds |
| `entry.place-check` | S2 | = | = | = | = | not on path: `placement` defaults to agent-places |
| `entry.place-owner` | S2 | = | = | = | = | not on path: `placement` defaults to agent-places |
| `entry.claim` | S2 | = | = | claim ref by compare-and-swap; two nodes racing, one wins | = | holds |
| `plan.input` | S2 | = | = | = | = | holds |
| `plan.dedupe` | S2 | = | = | = | = | holds |
| `plan.triage-rule` | S2 | = | = | = | = | holds |
| `plan.triage-judge` | S2 | = | = | = | = | not on path: X's and Y's requests are selected by a rule |
| `plan.record` | S2 | = | = | = | = | holds |
| `plan.research` | S2 | = | = | = | = | not on path: S2 raises no research request |
| `plan.place` | S2 | = | = | = | = | holds |
| `plan.lease` | S2 | = | = | = | = | holds |
| `plan.recommend` | S2 | = | = | = | = | holds |
| `plan.reason` | S2 | = | = | = | = | holds |
| `plan.exit` | S2 | = | = | = | = | holds |
| `design.input` | S2 | = | = | = | = | holds |
| `design.reentry` | S2 | = | = | = | = | not on path: S2 admits no amendment |
| `design.inventory` | S2 | = | = | = | = | not on path: no plan revision |
| `design.seams` | S2 | = | = | = | = | holds |
| `design.decompose` | S2 | = | = | = | = | holds |
| `design.research` | S2 | = | = | = | = | not on path: no fact fork |
| `design.overlaps` | S2 | = | = | = | = | holds |
| `design.streams` | S2 | = | = | = | = | not on path: `design.streams` defaults to opt-in |
| `design.unit-spec` | S2 | = | = | = | = | holds |
| `design.recommend` | S2 | = | = | = | = | holds |
| `design.reason` | S2 | = | = | = | = | holds |
| `design.ready` | S2 | = | = | = | = | holds |
| `design.exit` | S2 | = | = | = | posts confirmed interfaces to Y on node x | holds |
| `build.base` | S2 | = | = | = | = | holds |
| `build.unit-lease` | S2 | = | = | the unit lease on d stays held after the build hand-over | refused for x until the unit lease expires or never | A2-F2 |
| `build.unit-pass` | S2 | builder on node x under a unit lease only | = | pushes race d's on one build branch | no route for a push refused because the branch moved | A2-F8, A2-F11 |
| `build.acceptance` | S2 | = | = | = | = | holds |
| `build.scope` | S2 | = | = | = | = | holds |
| `build.reuse-check` | S2 | = | = | = | = | holds |
| `build.recommend` | S2 | = | = | = | = | holds |
| `build.ratify` | S2 | = | = | = | = | not on path: `decisions.major` defaults to author-rubric |
| `build.distill` | S2 | = | = | = | = | holds |
| `build.core` | S2 | = | = | = | = | holds |
| `build.exit` | S2 | = | the transition, refused while Y's question is open | = | holds up to 72h | A2-F5 |
| `test.merge` | S2 | = | = | = | = | holds |
| `test.select` | S2 | = | = | = | = | holds |
| `test.verdict` | S2 | = | = | = | = | holds |
| `test.route` | S2 | = | = | = | = | not on path: S2 injects no red |
| `test.attribute` | S2 | = | = | = | = | not on path: S2 injects no red |
| `test.flakes` | S2 | = | = | = | = | not on path: S2 injects no flake |
| `test.seen-red` | S2 | = | = | = | = | holds |
| `test.recommend` | S2 | = | = | = | = | holds |
| `test.reason` | S2 | = | = | = | = | holds |
| `test.exit` | S2 | = | = | = | = | holds |
| `deploy.current` | S2 | = | = | = | stale after the other node's landing → Test | holds |
| `deploy.mandate` | S2 | = | = | = | = | holds |
| `deploy.parents` | S2 | = | X landed | = | holds with no deadline or outcome | A2-F4 |
| `deploy.land` | S2 | = | = | the atomic push also releases the lease, terminal | = | A2-F3, A2-F9 |
| `deploy.core` | S2 | = | = | = | = | holds |
| `deploy.record` | S2 | = | = | = | = | holds |
| `deploy.distill` | S2 | = | = | = | = | holds |
| `deploy.recommend` | S2 | = | = | = | = | holds |
| `deploy.notify` | S2 | = | = | `landed` already posted by the landing push | = | A2-F3 |
| `deploy.released` | S2 | = | = | = | passes at once under at-landing | holds |
| `deploy.snapshot` | S2 | = | = | push unfenced, since no lease is held | no take-over after a limit | A2-F3 |
| `deploy.unlease` | S2 | = | = | lease already terminal | = | A2-F3 |
| `deploy.close` | S2 | = | = | = | unreached if d stops after the push | A2-F3 |
| `review.trigger` | S2 | = | = | = | = | holds |
| `review.pin` | S2 | = | = | = | = | holds |
| `review.lens` | S2 | = | = | = | = | holds |
| `review.refute` | S2 | = | = | = | = | holds |
| `review.report` | S2 | = | = | = | = | holds |
| `review.dispose` | S2 | = | = | = | = | holds |
| `review.fold` | S2 | = | = | = | = | not on path: the closing review is on built work, and the spec audit is opt-in |
| `review.cost` | S2 | = | = | = | = | holds |
| `probe.trigger` | S2 | = | = | = | = | not on path: S2 places no probe and claims no observation |
| `probe.pin` | S2 | = | = | = | = | not on path: no probe opened |
| `probe.design` | S2 | = | = | = | = | not on path: no probe opened |
| `probe.experiment` | S2 | = | = | = | = | not on path: no probe opened |
| `probe.run` | S2 | = | = | = | = | not on path: no probe opened |
| `probe.judge` | S2 | = | = | = | = | not on path: no probe opened |
| `probe.return` | S2 | = | = | = | = | not on path: no probe opened |
| `life.request` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.quiesce` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.notify` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.snapshot` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.unlease` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.close` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `adopt.census` | S2 | = | = | = | = | not on path: S2 runs no adoption |
| `test.seed` | S2 | = | = | = | = | not on path: S2 brings no new check |
| `adopt.practices` | S2 | = | = | = | = | not on path: S2 runs no adoption |
| `adopt.decisions` | S2 | = | = | = | = | not on path: S2 runs no adoption |
| `adopt.reconstruct` | S2 | = | = | = | = | not on path: S2 runs no adoption |
| `maintain.lease` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.read` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.direct` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.patch` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.file` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.levels` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `maintain.record` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.lease` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.gather` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.price` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.propose` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.file` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `loop.record` | S2 | = | = | = | = | not on path: S2 installs only the core |
| `release.pick` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `release.approve` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `release.promote` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `release.verify` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `release.route` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `release.record` | S2 | = | = | = | = | not on path: `build.closes` is at-landing and integrations is absent |
| `kits.version` | S2 | = | = | = | = | not on path: distribution is absent, so the skip is announced |
| `kits.cut` | S2 | = | = | = | = | not on path: distribution is absent |
| `kits.currency` | S2 | = | = | = | = | not on path: distribution is absent |
| `kits.adopters` | S2 | = | = | = | = | not on path: distribution is absent |
| `kits.offer` | S2 | = | = | = | = | not on path: distribution is absent |
| `kits.install` | S2 | = | = | = | = | not on path: S2 runs no install |
| `kits.update` | S2 | = | = | = | = | not on path: S2 runs no update |

| dPlacedRequest | A2-F2, A2-F6, A2-F8, A2-F10 |
|---|---|
| dKeptSession | A2-F5, A2-F6, A2-F10 |
| dWellOiledMachine | A2-F2, A2-F3, A2-F7, A2-F8 |
| dBoundRoles | A2-F11 |
| dFurnishedOrders | holds |

| P5 | A2-F2, A2-F8 |
|---|---|
| P21 | A2-F4, A2-F5, A2-F9 |
| P22 | A2-F2 |
| P23 | A2-F1 |
| P25 | holds |
| P26 | holds |
| P27 | holds |
| P29 | holds |
| P36 | A2-F11 |
| P40 | A2-F3, A2-F6, A2-F7, A2-F8, A2-F10 |

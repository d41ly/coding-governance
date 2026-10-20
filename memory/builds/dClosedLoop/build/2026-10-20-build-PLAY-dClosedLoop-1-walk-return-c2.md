# Walk return: run C, walker 2, dFairHearing to dKeptSession

**Serves:** research PLAY-dClosedLoop-1

Dispatch 186's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-27-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed because one of these clauses was silently missing. With `cl-dClosedLoop-0093` gone from dDeclaredLoop's row, nothing makes a session recompute a claim's key or check its source before acting on it. Every later build then acted on stale card cells and claims, which is the failure P23 was written to stop.

### C2-F1 — Clause `cl-dClosedLoop-0093` was deleted, so P23 is enforced by a clause that does not exist and gap-orient-05 is carried by no clause
- **Address:** architecture-v2 [chain], dDeclaredLoop row, between `cl-dClosedLoop-0092` and `cl-dClosedLoop-0094`; architecture-v2 [enforcement], row `P23`.
- **Class:** K5, c5
- **Severity:** blocker
- **Evidence:**
  - v2 [enforcement] (v2:1707) says `| P23 | cl-dClosedLoop-0093 |`.
  - In the copy, `grep -rn cl-dClosedLoop-0093` finds only that row. No clause in [chain] carries the id.
  - Counting the distinct ids in [chain] (v2:1629-1660) gives 495. Stage 0's K5, run on the working tree, read "clauses 496 … findings 0" (stage0-leads).
  - [clause-ids] says "Retired: none", so the id was never legitimately retired.
  - The walk record still lists the clause in dDeclaredLoop's roster: walk:1081 "8. claims keyed and trusted by key and source", and walk:893 "17. claims keyed and trusted by key and source".
  - P23 (v2:806): "A claim is acted on only when its stored key recomputes equal and its weakest source is not typed by an agent".
  - dDeclaredLoop still owns gap-orient-05 (gap-register:135, "Claims carry no freshness keys"), but only 0092's "each claim's key and verdict printed" mentions claim keys. Nothing makes a reader recompute the key or check the source.
- **Consequence:** dTrueNorth's carries join and Stage 0's K5 go red on an id no clause carries. No spec of dDeclaredLoop builds the trust-by-key rule, so the card, the position engine and every claim reader act on stale or agent-typed claims, the failure gap-orient-05 measured (4 of 17 run claims disagreed).
- **Fix:** Restore `cl-dClosedLoop-0093`, "claims keyed and trusted by key and source", in dDeclaredLoop's row between 0092 and 0094. Give it its seen-red arm: a planted claim whose key no longer recomputes, and one whose weakest source is agent-typed, are each re-derived and never acted on.

### C2-F2 — Two of `flow.on-exhausted`'s endings lead to states the transition table does not have
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0116` (with `cl-dClosedLoop-0098` and `cl-dClosedLoop-0100`)
- **Class:** K2, c2
- **Severity:** high
- **Evidence:**
  - 0116: "`park-for-owner` and `close-incomplete` the other values … or closing the build incomplete with its branch and records kept".
  - flow-steps [transitions] (fs:621): "the engine refuses any transition the table lacks". Its terminal list (fs:650) is "Landed, withdrawn, superseded, deferred, retired, refused, merged and answered".
  - The table has no row from an open state on budget exhaustion. Its only parked state, `paused`, is reached only by `life.request`.
  - 0100 builds only "the terminal states flow-steps' `[transitions]` declares".
  - P20 (v2:793): "A build ends in a terminal state flow-steps' `[transitions]` declares".
- **Consequence:** A build that spends its budget under `close-incomplete` (or under best-effort's third ending), or parks under `park-for-owner` (strict's preset value), asks for a transition the engine refuses. 0118's termination check finds no terminal for it. The scenario ends `stuck` or `invalid-input`, with no terminal and no witness.
- **Fix:** Add rows to the build transition table that 0098/0100 carry: any open state → `incomplete` (terminal) on the exhaustion record, and any open state → `parked-for-owner` with the owner's disposition as its exit. Seed 0116's planted endings from those rows.

### C2-F3 — The runaway ceiling gets two homes and two rules for whether a round count at the ceiling is allowed
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0106`, against `cl-dClosedLoop-0139`
- **Class:** K9
- **Severity:** medium
- **Evidence:**
  - 0106: "`RUNAWAY_CEILING`, moved into the loop kit's definition … and a planted round count at the ceiling refused".
  - The catalogue (v2:1127): `review.design.round-count` is "held at or below `review.max-rounds`, the loop kit's runaway ceiling, which dDeclaredLoop moves out of unattended into the policy file". v2:1128 says `review.max-rounds` is "`RUNAWAY_CEILING` made a policy value".
  - The pair rule (v2:1299): "`review.design.round-count` is at most `review.max-rounds`". 0139 says the same: "held at or below `review.max-rounds`".
  - The code today refuses at or above the ceiling: `tools/unattended/unattended.sh:783` reads `[ "$REVIEW_ROUNDS" -lt "$RUNAWAY_CEILING" ]`.
- **Consequence:** A repository that sets `round-count = max-rounds` passes dKeptSession's preset check and is refused by dDeclaredLoop's arm. The ceiling also ends up both as a loop-kit constant and as a policy key, so a spec writer has to pick one.
- **Fix:** In 0106, say the ceiling becomes the policy key `review.max-rounds`, and plant "a round count above `review.max-rounds` refused, one equal to it admitted", matching the pair rule.

### C2-F4 — The pre-claim budget is keyed to an intake record that does not exist until a later build
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0132`
- **Class:** K7
- **Severity:** medium
- **Evidence:**
  - 0132: "a budget keyed to the intake's content key".
  - 0123, in the same row, admits the dependency: "the disposition carried in the claim commit `entry.claim` writes until dWellOiledMachine's intake kind lands".
  - design-map: `record-kind.intake … owner=dWellOiledMachine`, which is not an ancestor of dPlacedRequest.
  - flow-steps `entry.intake`: "no intake, because the hook crashed or never fired → `entry.orient` records it absent".
- **Consequence:** Before dWellOiledMachine lands, and whenever the intake hook never fired, the budget has no key. Placement loops then go unbounded, which defeats the P39 arm this clause is listed under.
- **Fix:** Key the budget to a content key 0132 computes itself from the request text (the claim commit already carries it), with an absent intake keyed the same way. Plant one red case with no intake record.

### C2-F5 — Items declare a `map` slot before any ancestor registers it
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0124`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - 0124: "the items' declarations of the `map` slot and their unfolds", on dPlacedRequest.
  - ownership:100: "the unfolds render in the work order's map slot, dBoundRoles's; the project-map system is dTotalRecall's".
  - dBoundRoles and dTotalRecall both come after dPlacedRequest.
  - Stage 0 K4: "`memory.map-unfold`: read by no chain clause and no item (guard-bearing)".
- **Consequence:** dPlacedRequest's spec cites a work-order slot and a map that do not exist when it lands, and no stand-in is declared, unlike 0125's probe parts.
- **Fix:** Either move 0124 to dBoundRoles, or add "an empty slot rendered as not installed until dBoundRoles and dTotalRecall land, seen on the core-only install".

### C2-F6 — dFairHearing's breakpoint items depend on, and route to, items owned by a later build
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0070` and `cl-dClosedLoop-0075`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - flow-steps `review.pin` (fs:484), owned by dFairHearing, needs `review.trigger`.
  - `review.report` (fs:487) routes to `review.dispose`.
  - Both `review.trigger` and `review.dispose` belong to dDeclaredLoop (0105), a descendant of dFairHearing.
  - Stage 0: "K2 dFairHearing→review.dispose: order: … not an ancestor, UNCLASSED".
  - Neither 0070 ("`review.pin` maps from `review.opt-in`") nor 0075 declares a stand-in.
- **Consequence:** dFairHearing's acceptance cannot run its items end to end in order, or it quietly reaches into dDeclaredLoop's program.
- **Fix:** Add a stand-in to 0075 and 0070: until dDeclaredLoop lands, the harness is invoked directly with its pin arguments, and the report's dispositions are written to the review record.

### C2-F7 — Entry's placing items route to Plan and Design items no ancestor builds
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0122` and `cl-dClosedLoop-0123`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - flow-steps `entry.place` (fs:83): "new → `entry.claim`, then Plan, or `plan.triage-rule` on a re-placement after `plan.dedupe`".
  - Stage 0: "dPlacedRequest→design.input / plan.dedupe / plan.input / plan.triage-rule: order: … not an ancestor, UNCLASSED".
  - 0125 declares "a stand-in for each later part it rests on". 0122 and 0123 declare none.
- **Consequence:** A request placed after dPlacedRequest lands, but before dRankedPlan and dIndexedDesign land, routes to items that do not exist.
- **Fix:** Give 0123 the same stand-in sentence 0125 has: until Plan's and Design's items land, a `new` or `amend` placement files an owner item carrying the claim.

### C2-F8 — The spine's transition table routes to and witnesses items owned by later builds
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0098` and `cl-dClosedLoop-0100`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - Stage 0: "dDeclaredLoop→build.distill, build.ratify, deploy.notify, design.ready, plan.exit, plan.input, test.exit: order: … not an ancestor, UNCLASSED".
  - flow-steps [transitions] rows read "planning | `plan.exit` | designing", "testing | `test.exit` | deploying".
  - 0098 says only "the engine refusing any transition it lacks".
- **Consequence:** dDeclaredLoop's engine is specced against witnesses no ancestor produces, so its acceptance cannot be planted from real items.
- **Fix:** In 0098, have each row name the exit item by tag, with a fixture witness until its build lands. Class the seven Stage 0 leads in [stage0-classes].

### C2-F9 — dDeclaredLoop's guard-bearing keys `floor` and `transitions.record` are named by no clause
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0087` and `cl-dClosedLoop-0088`
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Stage 0 K4: "`floor`: read by no chain clause and no item (guard-bearing)" and "`transitions.record`: … (guard-bearing)".
  - 0087 reads "the guard, the TTY CLI and the default floor". 0088 reads "the transition record three ways". Neither names its key.
  - [floor] says the invariants are "each switchable only under the policy guard".
- **Consequence:** The switch that turns a floor invariant off, and the subset choice of transition-record channels, have no specced reader. A spec can ship the floor hard-wired and the key unread, so it fails open.
- **Fix:** Name `floor` in 0087 and `transitions.record` in 0088, each with a planted value seen red: an invariant switched off without the guard is refused, and an empty channel set is refused.

### C2-F10 — dPlacedRequest's keys `leases.granularity` and `card.follows` are named by no clause
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0120` and `cl-dClosedLoop-0121`
- **Class:** K4
- **Severity:** low
- **Evidence:** Stage 0 K4 lists both as "read by no chain clause and no item". 0120 says only "one lease grammar for builds, units and cadence runs". 0121 does not say when the card re-renders.
- **Consequence:** Presets set these keys (velocity sets `leases.granularity` to `build`), but nothing reads them.
- **Fix:** Name `leases.granularity` in 0120 and `card.follows` in 0121, each with one arm per value.

### C2-F11 — dKeptSession's keys `deps.coordination`, `deps.early-build` and `orient.budget` are named by no clause
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0145` and `cl-dClosedLoop-0147`
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Stage 0 K4 lists `deps.coordination` and `deps.early-build`, and lists "`orient.budget`: … (guard-bearing)".
  - 0145: "dependency coordination by the parent's lease, interfaces confirmed at Design's exit". 0147: "orientation cost recorded per stage".
  - Coordination item 8 reads both `deps.*` keys. strict sets `wait-for-landing` and `design-only`.
- **Consequence:** strict's posture on dependencies and the orientation ceiling are never read, so strict behaves like standard.
- **Fix:** Name all three keys in 0145 and 0147, each seen on its strict value.

### C2-F12 — Two clauses give two rules for when a fresh session is recommended
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0150`, against `cl-dClosedLoop-0121`
- **Class:** K9
- **Severity:** medium
- **Evidence:**
  - 0121 (dPlacedRequest): "a fresh session recommended by `resume.context`".
  - 0150 (dKeptSession): "a fresh session in the build's worktree recommended until the card-import fixture passes", with no key.
  - The presets (v2:1373) set `resume.context` to `always-resume` under velocity.
- **Consequence:** Under velocity, one build recommends resuming and the other recommends a fresh session, so the policy key is bypassed.
- **Fix:** Turn 0150 into a gate on 0121's key: while the card-import fixture is red, `always-resume` reads as `fresh-when-idle`, and that is reported.

### C2-F13 — The termination check's red case plants only a raised budget
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0118`
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - stall-and-loop [design] item 8: "raising any loop bound (the budget, a round count, a retry count, a deadline) is a loosening".
  - 0118 states the rule for "a loop bound" but plants only "an unattended raise of the budget".
- **Consequence:** An unattended raise of `review.max-rounds`, `flow.route-backs` or `flow.wait-ceiling` can pass a check that was only ever seen red on the budget, so the guard certifies more than it checks.
- **Fix:** Add one planted unattended raise each for a round count, a retry count and a deadline to 0118's red list.

### C2-F14 — The commit kind's position-engine reader has no writer until the commit queue lands
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0108`
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - 0108: "… and the position engine reading them".
  - Stage 0 K3: "commit: no writer item … written by the commit queue". memory-plan:157 names the writer as "the commit queue from the act binding", which is dWellOiledMachine's.
  - gap-spine-08: "0 of 6,084" commits carry the item, act or session that made them.
- **Consequence:** Between dDeclaredLoop and dWellOiledMachine, the engine reads `Gov-*` trailers that no commit carries. Position then falls back to subject parsing with no rule saying so.
- **Fix:** State 0108's interim: until the commit queue writes the trailers, the engine reads the subject view, seen on today's commits. Name the writer by tag.

### C2-F15 — The mailbox message kind names no writer item and no reader
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0143`
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - Stage 0 K3: "mailbox-message: no writer item … no reader: no item waits on its writer or names it".
  - coordination item 6 says "every transition reads the build's mailbox and is refused while a message … is neither answered nor acknowledged". 0143 says only "read and disposed at every transition".
- **Consequence:** The refusal that makes a transition wait on an unanswered message has no item to carry it, so a spec can build the mailbox without it.
- **Fix:** In 0143, name the writer (the posting command per kind) and the reader: each exit item refuses on an undisposed message until `flow.wait-ceiling`. Plant one red case.

### C2-F16 — "The panel's internals" does not carry the untyped harness agent gap that dFairHearing owns
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0078`
- **Class:** K1
- **Severity:** low
- **Evidence:** gap-review-13: "The review harness spawns an untyped agent that no stage declares", owned by dFairHearing. The systems record's checks say "every stage a declared role". 0078 says only "the panel's internals".
- **Consequence:** A spec writer cannot tell from 0078 that the untyped spawn must be typed and declared.
- **Fix:** Add to 0078: "every agent the harness spawns typed and declared in a stage, seen red on a planted untyped spawn".

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0068 | dFairHearing | review-system [lenses] replay isolation, bar and scorer | holds |
| cl-dClosedLoop-0069 | dFairHearing | review-system [lenses] "How it is selected"; flow-steps `review.pin` | holds |
| cl-dClosedLoop-0070 | dFairHearing | review-system [lenses] channel and boundary check; flow-steps [breakpoint] | C2-F6 |
| cl-dClosedLoop-0071 | dFairHearing | review-system [adjudication] batches by address | holds |
| cl-dClosedLoop-0072 | dFairHearing | review-system [adjudication] duplicates; gap-review-08 | holds |
| cl-dClosedLoop-0073 | dFairHearing | review-system [adjudication] grade per id; gap-review-05 | holds |
| cl-dClosedLoop-0074 | dFairHearing | review-system [adjudication] twins; gap-review-06 | holds |
| cl-dClosedLoop-0075 | dFairHearing | review-system [adjudication] homing; flow-steps `review.report`; Stage 0 K2 | C2-F6 |
| cl-dClosedLoop-0076 | dFairHearing | review-system [lenses] anchored entries and lens notes | holds |
| cl-dClosedLoop-0077 | dFairHearing | review-system [stale]; gap-review-09; tools/workflows, tools/hooks/agent-cap.js:495, tools/roles/agents | holds |
| cl-dClosedLoop-0078 | dFairHearing | systems [design-role-shapes] owners; gap-review-12 and gap-review-13 | C2-F16 |
| cl-dClosedLoop-0079 | dFairHearing | flow-steps [probe] experiment shape; gap-test-18; research-testing-anywhere F6 | holds |
| cl-dClosedLoop-0080 | dFairHearing | flow-roles-adoption [design] 3 and [chain]; night-pass-two [p7] | holds |
| cl-dClosedLoop-0081 | dFairHearing | night-pass-two [p2] item 6; flow-steps [probe] | holds |
| cl-dClosedLoop-0082 | dFairHearing | night-pass-two [p6] NT-25; gap-review-20 | holds |
| cl-dClosedLoop-0083 | dFairHearing | night-pass-two [p7] rule table; tools/workflows/check-review-join.sh | holds |
| cl-dClosedLoop-0084 | dFairHearing | stall-and-loop [design] 4 and [chain]; gap-review-21; P39 | holds |
| cl-dClosedLoop-0085 | dFairHearing | final-questions [audit]; catalogue `review.design-audit.*`; gap-review-22 | holds |
| cl-dClosedLoop-0086 | dDeclaredLoop | P1; gap-spine-01; coordination [chain]; walk roster | holds |
| cl-dClosedLoop-0087 | dDeclaredLoop | v2 [floor] and [witnesses]; Stage 0 K4 | C2-F9 |
| cl-dClosedLoop-0088 | dDeclaredLoop | catalogue `transitions.record`; Stage 0 K3 and K4 | C2-F9 |
| cl-dClosedLoop-0089 | dDeclaredLoop | P1 coverage gate; gap-spine-01 | holds |
| cl-dClosedLoop-0090 | dDeclaredLoop | P2; flow-steps [rules]; gap-spine-02 | holds |
| cl-dClosedLoop-0091 | dDeclaredLoop | P16; ownership of factories | holds |
| cl-dClosedLoop-0092 | dDeclaredLoop | layer-runtime [decide] answer set; P22; gap-orient-03; P23 (see C2-F1) | holds |
| cl-dClosedLoop-0094 | dDeclaredLoop | P24; flow-steps [rules] | holds |
| cl-dClosedLoop-0095 | dDeclaredLoop | flow-steps [transitions] backward rows | holds |
| cl-dClosedLoop-0096 | dDeclaredLoop | P11; flow-steps [rules] | holds |
| cl-dClosedLoop-0097 | dDeclaredLoop | P24, P20; gap-flow-13 | holds |
| cl-dClosedLoop-0098 | dDeclaredLoop | flow-steps [transitions]; gap-flow-15; Stage 0 K2 | C2-F8 |
| cl-dClosedLoop-0099 | dDeclaredLoop | flow-steps [rules] refusal route | holds |
| cl-dClosedLoop-0100 | dDeclaredLoop | flow-steps [transitions] terminal list; P20 | C2-F8 |
| cl-dClosedLoop-0101 | dDeclaredLoop | flow-steps `entry.place` closed set; gap-flow-13 | holds |
| cl-dClosedLoop-0102 | dDeclaredLoop | P2; gap-flow-14; flow-steps [probe] | holds |
| cl-dClosedLoop-0103 | dDeclaredLoop | flow-roles-adoption [renamed]; tag-namespace owners in the design map | holds |
| cl-dClosedLoop-0104 | dDeclaredLoop | flow-steps [breakpoint] owner gate; P7; gap-flow-11 | holds |
| cl-dClosedLoop-0105 | dDeclaredLoop | flow-steps [breakpoint] item table and owners | holds |
| cl-dClosedLoop-0106 | dDeclaredLoop | catalogue v2:1127-1128; [presets] pair rule; unattended.sh:774,783; fates | C2-F3 |
| cl-dClosedLoop-0107 | dDeclaredLoop | flow-steps [rules] recommendation; gap-flow-12 | holds |
| cl-dClosedLoop-0108 | dDeclaredLoop | memory-plan [sites] and [edges]; gap-spine-08 and -09; routed_commits.py, lib-unattended.sh:1055, runlog/model.py:592 | C2-F14 |
| cl-dClosedLoop-0109 | dDeclaredLoop | flow-roles-adoption [design] items 6, 9, 11 and 14 | holds |
| cl-dClosedLoop-0110 | dDeclaredLoop | flow-roles-adoption [folded] FA-3; P20 | holds |
| cl-dClosedLoop-0111 | dDeclaredLoop | flow-roles-adoption [design] 14-15, FA-7 | holds |
| cl-dClosedLoop-0112 | dDeclaredLoop | night-pass-two [p1] NT-1, NT-6, NT-7; catalogue `flow.scenario-*` | holds |
| cl-dClosedLoop-0113 | dDeclaredLoop | night-pass-two [p1] NT-4; catalogue `flow.adapt` | holds |
| cl-dClosedLoop-0114 | dDeclaredLoop | night-pass-two [p2] item 3 and [p4] contract | holds |
| cl-dClosedLoop-0115 | dDeclaredLoop | stall-and-loop [design] 1-2 and [chain]; catalogue `flow.rework-budget`; gap-flow-23 | holds |
| cl-dClosedLoop-0116 | dDeclaredLoop | stall-and-loop [design] 3; catalogue `flow.on-exhausted`; flow-steps [transitions]; P20 | C2-F2 |
| cl-dClosedLoop-0117 | dDeclaredLoop | stall-and-loop [design] 4; catalogue `review.follow-up` and `review.max-rounds` | holds |
| cl-dClosedLoop-0118 | dDeclaredLoop | stall-and-loop [design] 8 and [chain]; gap-flow-24 | C2-F13 |
| cl-dClosedLoop-0119 | dDeclaredLoop | final-questions [deviation]; catalogue `deviation.approval`; P41 | holds |
| cl-dClosedLoop-0120 | dPlacedRequest | coordination [design] 1-5; catalogue `leases.*`; P5; Stage 0 K4 | C2-F10 |
| cl-dClosedLoop-0121 | dPlacedRequest | catalogue `card.*` and `resume.*`; P22 | C2-F10 |
| cl-dClosedLoop-0122 | dPlacedRequest | flow-steps [entry] items and owners; Stage 0 K2 | C2-F7 |
| cl-dClosedLoop-0123 | dPlacedRequest | flow-steps `entry.place`; catalogue `placement*`; Stage 0 K2 | C2-F7 |
| cl-dClosedLoop-0124 | dPlacedRequest | ownership:99-100; project-map role shapes; Stage 0 K4 | C2-F5 |
| cl-dClosedLoop-0125 | dPlacedRequest | flow-steps [probe] incl. stand-ins; P31 | holds |
| cl-dClosedLoop-0126 | dPlacedRequest | P32; night pass point 3 | holds |
| cl-dClosedLoop-0127 | dPlacedRequest | memory-plan [pockets] and [chain] | holds |
| cl-dClosedLoop-0128 | dPlacedRequest | night-pass-two [p1] NT-2 | holds |
| cl-dClosedLoop-0129 | dPlacedRequest | night-pass-two [p3] item 6 | holds |
| cl-dClosedLoop-0130 | dPlacedRequest | night-pass-two [p4] NT-18; memory-plan registers | holds |
| cl-dClosedLoop-0131 | dPlacedRequest | memory-plan [pockets] change feed; night-pass-two [answers-folded] NT-14 | holds |
| cl-dClosedLoop-0132 | dPlacedRequest | stall-and-loop [design] 1 and [layers]; the design map's `record-kind.intake` row; flow-steps `entry.intake` | C2-F4 |
| cl-dClosedLoop-0133 | dPlacedRequest | cloud-and-scale [defects] and [design] 2; gap-conc-12 | holds |
| cl-dClosedLoop-0134 | dPlacedRequest | cloud-and-scale [design] 3; `leases.queued-claim-days`; gap-conc-13 | holds |
| cl-dClosedLoop-0135 | dPlacedRequest | cloud-and-scale [design] 4; `leases.expiry-hours`; gap-conc-14 | holds |
| cl-dClosedLoop-0136 | dPlacedRequest | cloud-and-scale [design] 15; gap-conc-18 | holds |
| cl-dClosedLoop-0137 | dPlacedRequest | cloud-and-scale [design] 10; gap-conc-17 | holds |
| cl-dClosedLoop-0138 | dPlacedRequest | cloud-and-scale [design] 9; `leases.offer-seconds`; gap-conc-19 | holds |
| cl-dClosedLoop-0139 | dKeptSession | v2 [presets] rules and table; flow-steps [consequences] | holds |
| cl-dClosedLoop-0140 | dKeptSession | presets table `hooks.bypass` | holds |
| cl-dClosedLoop-0141 | dKeptSession | v2 [presets] charter-render rule | holds |
| cl-dClosedLoop-0142 | dKeptSession | walk wave-1-2 dKeptSession; catalogue `preset` | holds |
| cl-dClosedLoop-0143 | dKeptSession | coordination [design] 6; night-pass-two NT-16; Stage 0 K3 | C2-F15 |
| cl-dClosedLoop-0144 | dKeptSession | coordination [design] 7; `deps.messaging` | holds |
| cl-dClosedLoop-0145 | dKeptSession | coordination [design] 8; P21; Stage 0 K4 | C2-F11 |
| cl-dClosedLoop-0146 | dKeptSession | catalogue `actions.free` | holds |
| cl-dClosedLoop-0147 | dKeptSession | catalogue `orient.budget`; Stage 0 K4 | C2-F11 |
| cl-dClosedLoop-0148 | dKeptSession | flow-steps [rules] item boundary; `mailbox.reads` | holds |
| cl-dClosedLoop-0149 | dKeptSession | catalogue `notify.owner` | holds |
| cl-dClosedLoop-0150 | dKeptSession | catalogue and presets `resume.context` (v2:1050, 1373); 0121 | C2-F12 |
| cl-dClosedLoop-0151 | dKeptSession | catalogue `card.pointers`; flow-steps [rules] | holds |
| cl-dClosedLoop-0152 | dKeptSession | catalogue `context.*` | holds |
| cl-dClosedLoop-0153 | dKeptSession | compaction CX checks; v2 [owed] | holds |
| cl-dClosedLoop-0154 | dKeptSession | design-map policy namespaces owned | holds |
| cl-dClosedLoop-0155 | dKeptSession | flow-steps [rules] and [breakpoint] attendance; P4 | holds |
| cl-dClosedLoop-0156 | dKeptSession | flow-steps [transitions] `repeat` row; `entry.place` | holds |
| cl-dClosedLoop-0157 | dKeptSession | Stage 0 K4 population; v2 [policies] | holds |
| cl-dClosedLoop-0158 | dKeptSession | night-pass-two [p1] NT-3 | holds |
| cl-dClosedLoop-0159 | dKeptSession | night-pass-two [p3] NT-17; catalogue `mailbox.notice` and `mailbox.fetch-seconds` | holds |
| cl-dClosedLoop-0160 | dKeptSession | night-pass-two [p4] messages | holds |
| cl-dClosedLoop-0161 | dKeptSession | night-pass-two [answers-folded] NT-14; memory-plan change feed | holds |
| cl-dClosedLoop-0162 | dKeptSession | coordination [design] 6; `flow.wait-ceiling`; stall-and-loop [chain] | holds |
| cl-dClosedLoop-0163 | dKeptSession | stall-and-loop [chain] dKeptSession | holds |
| cl-dClosedLoop-0164 | dKeptSession | cloud-and-scale [design] 5; gap-conc-15 | holds |
| cl-dClosedLoop-0165 | dKeptSession | cloud-and-scale [design] 10 and [chain] | holds |

| Build | Verdict |
|---|---|
| dFairHearing | C2-F6, C2-F16 |
| dDeclaredLoop | C2-F1, C2-F2, C2-F3, C2-F8, C2-F9, C2-F13, C2-F14 |
| dPlacedRequest | C2-F4, C2-F5, C2-F7, C2-F10 |
| dKeptSession | C2-F11, C2-F12, C2-F15 |

Read outside the list above: none.

One line on the instruments: `stage0-leads.md` was run on the working tree and prints "clauses 496", which gives away that the copy (495) is missing a clause, and the slice list leaves out `cl-dClosedLoop-0093` without saying why.

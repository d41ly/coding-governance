# Skeptic brief: run A, batch 3

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a3/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### A1-F7 — `design.ready` and `test.exit` wait on the recommend item, not the reason item, so the frontier can pass a review the reason calls for
- **Address:** flow-steps [design] `design.ready`; flow-steps [test] `test.exit`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `design.ready` needs "`design.recommend`, and the spec audit where it ran". `test.exit` needs "`test.recommend`, and the gate review where it ran".
  - Under the default `review.recommendation.source: scored-signals-and-reasoning`, `design.reason` and `test.reason` route "a review → the spec audit" or "the gate review".
  - [rules] says `next` returns "the unwitnessed items whose needs are witnessed" and that independent items run in parallel. P24 says "An item's witness is resolved before any item that depends on it starts".
- **Consequence:** Once `design.recommend` is witnessed, `design.ready` and `design.reason` are both on the frontier. `design.ready` and `design.exit` can be recorded before the reason asks for the audit, and the route to the audit is then unreachable. Under `review.recommendation: binding`, an owed review is skipped, so a guard loosens. Test has the same defect.
- **Fix:** Set the Needs to "`design.reason` where the source runs it, else `design.recommend`; and the spec audit where it ran", and the same for `test.exit`. Add a planted reason that answers "review" and must place the audit.

### A3-F14 — `entry.claim`'s own-key idempotency routes a replayed claim into a terminal build
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `entry.claim`: "a retry that finds its own key counts as claimed" → "claimed → Plan, or Design on `patch` or `repeat`". layer-memory: "A slug's claim ref is never pruned". `[transitions]` has no row leaving `withdrawn`.
- **Consequence:** A replayed intake after the withdrawal routes into a withdrawn build. The engine refuses the transition, and the request is neither placed nor answered.
- **Fix:** `entry.claim` reads the slug's last transition. If it is terminal, it mints a fresh slug or returns the request naming the terminal state.

### A4-F14 — Early chain builds route into later builds' items with no declared stand-in
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - Stage 0's leads list 21 UNCLASSED order routes, such as "dPlacedRequest→plan.input", "dWitnessedBar→deploy.current" and "dWellOiledMachine→deploy.released".
  - `grep` of recut's tolerance rows for `plan.input`, `design.input`, `deploy.current` and `deploy.released` printed nothing.
  - `test.attribute` and `test.reason` have a tester only from dWitnessedBar (cl-0361). Five builds land before it.
- **Consequence:** dTrueNorth to dDeclaredLoop are built with their Test judgment and their Plan and Deploy hand-offs run on undeclared stand-ins.
- **Fix:** Add a tolerance row per forward route and actor, naming today's stand-in: the session agent as tester and push-main as Deploy.

### A5-F6 — An unreachable remote has no arm at the compare-and-swap items, and an unbounded one at `deploy.land`
- **Address:** flow-steps [entry] `entry.claim`, [plan] `plan.lease`, [breakpoint] `review.report`, [deploy] `deploy.land`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - v2 `leases.offline` default `warn`: "records an acquisition and queues a claim or an ask-id mint keyed by content, each pushed by compare-and-swap on reconnection". `cl-dClosedLoop-0120` applies this "for every compare-and-swap mint alike".
  - None of the outcome sets of `entry.claim`, `plan.lease`, `build.unit-lease` or `review.report`'s `refs/gov/class-claims` has a queued or unreachable outcome.
  - `[transitions]` "none → planning" needs "the claim ref" as its witness.
  - `deploy.land`: "the remote unreachable ... → the supervisor's retry, then an owner item", with no count or deadline. layer-runtime `stale-remote` instead "holds and retries, and parks once `leases.expiry-hours` passes".
- **Consequence:** S6's unreachable remote either enters Plan with no witness for its claim, or stops a `new:` disposition that needs a claim "at report time". At `deploy.land` it either retries without bound or ends in one of two contradictory outcomes. That breaks P39's "every wait carries a deadline and a declared outcome".
- **Fix:**
  - Add a `queued` outcome to each compare-and-swap item. Its route waits on reconnection within `flow.wait-ceiling`, and the item's witness is the pushed ref, read on reconnection.
  - Bound `deploy.land`'s retry with a declared count or deadline and one outcome, aligned with `stale-remote`.

### A3-F13 — Lease refusals route "as `leases` says", which fails open on a terminal tombstone under the default `warn`
- **Address:** flow-steps [entry] `entry.claim`; [plan] `plan.lease`; [build] `build.unit-lease`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S5
- **Evidence:** Each item routes "refused → as `leases` says". v2's `leases` row is "warn, refuse | warn", with `standard` set to warn. R2.2: "overlap warns only". `cl-0281` and `cl-0415` require that "a queued claim replayed against a withdrawn build … is refused".
- **Consequence:** Under the default preset, a replayed take against X's tombstone proceeds with a warning, and units of a withdrawn build resume.
- **Fix:** Split the route. A tombstone, a terminal build or an epoch fence is always refused and files an ask. Only an overlap or a live holder goes "as `leases` says".

### A5-F3 — A refused lease routes "as `leases` says", but `leases` is the overlap switch
- **Address:** flow-steps [entry] `entry.claim`; also `plan.lease` and `build.unit-lease`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `entry.claim` Then: "the lease refused → as `leases` says". `plan.lease` and `build.unit-lease` say the same.
  - v2 `[policies]`: "`leases` | warn, refuse | warn | R2.2". P5 reads that key as "overlap warns by default". It says nothing about what follows a refusal.
  - On `patch` or `repeat`, `entry.claim` first creates `refs/gov/claims/<slug>`, which is "never pruned", and then takes the lease. A refused lease therefore leaves a claimed slug with no transition record, and the rework budget lives "in its transition record".
  - `cl-dClosedLoop-0132`'s pre-claim budget covers only "placement loops before `entry.claim`".
  - `[rules]` says "A re-dispatch of a refused instance draws on the build's rework budget", while P39 says "Contention waits in its turn and draws nothing". A lease held by another build is both a refusal and contention.
- **Consequence:** S6's first failure has no declared route. The retry draws on no budget (none exists yet) or on one the rules forbid (contention). A spec writer cannot write the arm.
- **Fix:**
  - Route a refused lease explicitly: wait as contention within `flow.wait-ceiling` for the holder's release or expiry, then raise an owner item.
  - Count claim-time retries against `cl-dClosedLoop-0132`'s pre-claim budget.
  - Say what happens to the never-pruned slug claim when the lease is never taken.

### A1-F1 — `entry.intake` is acted by a role that writes its own witness
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - flow-steps:81 says the actor is "orientation scout, in an owner-bound session only" and the witness is "the intake entry the scout writes".
  - The same row's route says "because the hook crashed or never fired", and flow-steps [revised] `hook-actor-kind` says "`entry.intake` is a hook".
  - layer-roles:414 puts `entry.intake` under `hook`. layer-memory:402 says "its writer is `entry.intake`'s hook (PM-9)". cl-dClosedLoop-0377 says "the session's intake log, which `entry.intake`'s prompt-submit hook writes".
  - [rules] says "No witness is typed by the acting agent."
  - Probe: `grep -rn 'entry.intake' <copy>/memory/builds/dClosedLoop/build --include=*.md | grep -v research-` shows a hook in layer-roles, layer-memory and ownership, and "orientation scout" only in flow-steps:81.
  - Stage 0's K1 cannot see this, because the actor is now a declared role and K1 "left out: whether a witness is actor-typed (P2)".
- **Consequence:** In S1, the owner's request is the mandate. `deploy.mandate` reads "the intake record", and `plan.ratification: request` reads it as the ratification. A model writes that record about itself, so every check that takes the intake as the owner's words certifies text an agent typed.
- **Fix:** Restore the actor to "hook: the prompt-submit hook (Runtime's)" and the witness to "the intake entry the hook writes". Add the arm to cl-dClosedLoop-0090's witness-class rule, seen red on a planted role-typed intake.

### A4-F2 — `entry.intake`'s actor is the orientation scout, so the agent types its own witness
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S7
- **Evidence:**
  - flow-steps:81 reads "| `entry.intake` | orientation scout, in an owner-bound session only | … | the intake entry the scout writes".
  - The same record contradicts it: `[entry]` says "The hook is Runtime's", and `[revised]` `hook-actor-kind` says "`entry.intake` is a hook".
  - layer-roles:414 reads "| hook | `entry.intake` |".
  - flow-roles:195-197 says the ratification's witness is "written verbatim by the prompt-submit hook".
- **Consequence:** The record that becomes the request's mandate, which `deploy.mandate` reads under `plan-only`, is typed by the acting agent. This breaks `[rules]`' "No witness is typed by the acting agent", and a mandate can be forged.
- **Fix:** Set the actor to "hook (prompt-submit), in an owner-bound session only". Set the witness to "the intake entry the hook writes, carrying its session binding".

### A3-F19 — `life.quiesce` routes a pause to `parked`, a state `[transitions]` lacks
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K1
- **Severity:** low
- **Scenario:** S5
- **Evidence:** "pause → parked". `[transitions]` reads "any open state | `life.request`: pause | paused".
- **Consequence:** A route names a state the engine does not know.
- **Fix:** Write "pause → paused".

### A3-F15 — Quiesce cannot stop acts other nodes run under X's unit leases
- **Address:** flow-steps [lifecycle] `life.quiesce`, `life.unlease`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `life.quiesce`'s actor is the executor: "Each running act finishes within its ceiling", witnessed by "the executor's record of the acts it let finish". `life.unlease` then tombstones every lease.
- **Consequence:** Node x's in-flight unit pass is fenced mid-act. Its commits are neither kept nor recorded, and the witness claims a quiesce it never observed.
- **Fix:** Make `life.quiesce` wait, per unit lease, for the holder's hand-over or for its `runtime.act-ceiling`, witnessed per lease.

### A3-F12 — A supersession hands the kept work to nothing
- **Address:** flow-steps [lifecycle] `life.request`, kept-work note; [design] `design.input`
- **Class:** K2, c4
- **Severity:** high
- **Scenario:** S5
- **Evidence:** The kept-work note: "kept work passes to its replacement through the replacement's `design.inventory`". `design.input` routes only "plan revision → `design.inventory`", and Design's seven inputs include no supersession. `life.request` "asks to … supersede the build" and its witness is "the command's record", which holds no replacement. Even so, `life.notify` posts "with the replacement's slug". `life.unlease` "reclaims the build's workspaces". No item writes the `supersedes` edge (`cl-0217`).
- **Consequence:** Z enters Design through `design.seams`, X's built units are never inventoried, and X's workspaces are reclaimed. The kept work is lost, and dependents' links move to an unnamed replacement.
- **Fix:** Make supersede require a claimed replacement slug, refusing otherwise, and write the `supersedes` edge. Add a Design input "a supersession" that routes to `design.inventory` over X's units at its branch tip. Have `life.unlease` reclaim worktrees but keep the branch.

### A1-F2 — Under `plan.ratification: request`, the ratification is whatever the planner records
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - flow-steps:140 says "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification".
  - Against it:
    - flow-steps [plan] Exits: "the request is the ratification".
    - [consequences]: "`plan.exit`'s witness carries it".
    - cl-dClosedLoop-0377: "its intake read as the request's ratification".
    - cl-dClosedLoop-0378: until the hook lands, the item "falls back to dDeclaredLoop's owner gate, held for the owner's disposition".
    - cl-dClosedLoop-0283: "Plan's ratification ... re-pointed to the intake record".
    - P2: "never from state the acting agent typed".
  - Probe: `python -I scratchpad/cl.py <v2> all | grep -E '0377|0378|0283'` printed those three clauses.
- **Consequence:** S1 runs on the default `request`. Design starts on a go the planner typed, and the gate `autonomy: plan-only` keeps at Plan is met by an agent's own record. dRankedPlan's spec writer gets one rule from the item and the opposite from its own clauses 0377 and 0378.
- **Fix:** Replace the clause with "under `plan.ratification: request`, the intake record, joined by its content key, is the ratification, and until the intake kind lands the owner gate of cl-dClosedLoop-0378". Add a planted planner-typed go that reds.

### A4-F3 — Under `request`, the ratification is "the owner's go, as the planner records it"
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S7
- **Evidence:**
  - flow-steps:140 reads "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification".
  - The same record's `[plan]` says "the request is the ratification".
  - flow-roles:195-198 says "Its witness is the request itself, written verbatim by the prompt-submit hook … Plan's item 10 is witnessed by the intake record".
- **Consequence:** A planner-typed record certifies the mandate that every later step and `deploy.mandate` rely on. The guard certifies a claim, not a witness.
- **Fix:** Reword to "under `plan.ratification: request`, the hook-written intake record stands as the ratification", and witness `plan.exit` by it.

### A5-F4 — Under `plan.ratification: request`, the ratification witness is typed by the planner
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `plan.exit`: "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification".
  - `[rules]`: "No witness is typed by the acting agent".
  - v2 `cl-dClosedLoop-0377`: "its intake read as the request's ratification by `plan.ratification`", the intake being hook-written.
  - v2 `[contracts]`: "Plan's witness is the hook-written intake (FR-1)".
- **Consequence:** An owner who is silent, or who never typed a go, is certified as having ratified on the planner's word. The guard certifies what it does not check.
- **Fix:** Make `plan.exit`'s witness under `request` the hook-written intake record keyed to the build's claim, never a planner record. Under `cl-dClosedLoop-0378`'s fallback, use the owner gate.

### A4-F20 — `plan.lease`'s overlap outcome has no next route
- **Address:** flow-steps [plan] `plan.lease`
- **Class:** K2
- **Severity:** low
- **Scenario:** S7
- **Evidence:** The Then cell reads "held → `plan.recommend`; an overlap → noted on the card and in the other build's mailbox; refused → as `leases` says".
- **Consequence:** After an overlap is noted, it is unstated whether the build goes on to `plan.recommend`.
- **Fix:** Write "an overlap → noted …, then `plan.recommend`".

### A1-F11 — The overlap outcomes of the lease items route nowhere, and one cites the wrong key
- **Address:** flow-steps [plan] `plan.lease`; flow-steps [build] `build.unit-lease`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - `plan.lease`: "an overlap → noted on the card and in the other build's mailbox". No next item is named.
  - `build.unit-lease`: "an overlap → warned (`leases.overlap`)". The catalogue's `leases.overlap` is "kit-dirs, files, builds", which is granularity. The warn/refuse key is `leases` ("warn, refuse").
- **Consequence:** In S1, a feature on a `tools/` kit overlaps any live build on that kit under the default `kit-dirs`. Neither item says whether the lease is held and the run goes on, so the engine has no witnessed outcome to follow.
- **Fix:** Write "an overlap under `leases: warn` → noted, then as held; under `refuse` → as refused" in both rows, and cite `leases` with `leases.overlap` as the granularity.

### A4-F19 — flow-steps `[revised]` names the retired key spelling `policy.on-missing-expansion`
- **Address:** flow-steps [revised]
- **Class:** K4
- **Severity:** low
- **Scenario:** S7
- **Evidence:** flow-steps:767 reads "from LR-4, `policy.on-missing-expansion`". The key is `policy-file.on-missing-expansion` (flow-roles-adoption `[renamed]`).
- **Consequence:** A reader inventory by value misses this citation.
- **Fix:** Rename the key, with a dated note.

### A3-F16 — A post to a closed mailbox recreates a ref no one reads or prunes
- **Address:** flow-steps [rules] "Closing a mailbox"
- **Class:** K10
- **Severity:** low
- **Scenario:** S5
- **Evidence:** The rule reads "Only then is the ref pruned, and a missing ref counts as done". Refs are per writing session (`refs/gov/mail/<slug>/<fleet tag>/<session>`, `cl-0141`), and no refusal of a post to a closed build is declared.
- **Consequence:** Y's later question to withdrawn X lands on an orphan ref that nothing reads or prunes. Only `cl-0162`'s default answer ends Y's wait.
- **Fix:** Refuse a post whose slug carries a terminal transition, and answer the sender with that state.

### A5-F2 — A loop that ends non-converging on a blocking item leaves the build with no route
- **Address:** flow-steps [rules], `build.acceptance`, `test.flakes`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `[rules]`: "Past `flow.route-backs` returns to the same item, that item's loop ends non-converging and its open work goes to asks".
  - `build.acceptance`: "fail → a fix pass", with no arm for the bound.
  - `test.flakes`: "Each re-entry counts against `flow.route-backs`".
  - Build exits only when "every unit is built, with its acceptance recorded", and Test only when "no red blocks".
  - Defaults: `flow.route-backs` is 3 and `flow.rework-budget` is `4+2`, so the per-item bound trips before the budget is spent.
  - `cl-dClosedLoop-0117` says the opposite of `[rules]`: "fix passes against one acceptance red ending at a NON-CONVERGENT round, whose findings are promoted, to units while budget remains and to asks after".
- **Consequence:** S6's red unit at `build.acceptance`, and its flake at Test, each stop at the per-item bound. The open work becomes an ask, but the unit stays unbuilt or the leg stays red. Build or Test then cannot exit, and the budget is not spent, so `flow.on-exhausted` never fires. The build stalls until the stuck detector raises an owner item, which no route declares.
- **Fix:**
  - State one rule in `[rules]`, `build.acceptance` and `test.flakes`, consistent with `cl-dClosedLoop-0117`: past `flow.route-backs`, a blocking item's open work becomes a new unit while budget remains and goes to `flow.on-exhausted` after.
  - Plant the probe: an acceptance red that never greens must reach a terminal.

## Clean cells to attack

- `design.unit-spec` in S6
- `test.select` in S1
- `life.close` in S5
- `test.verdict` in S4
- `build.scope` in S7
- `test.select` in S5
- `plan.record` in S5
- `design.seams` in S5

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `AS3-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a3/` only. Your effort is the one the owner's
role definition sets.

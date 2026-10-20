# Walk return: run A, walker 4, S4 and S7

**Serves:** research PLAY-dClosedLoop-1

Dispatch 163's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-4-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

1. **Pre-mortem:** The chain shipped and failed in this scenario because adopters' updates crossed retirements no upgrade step carried, and the `update` item has no outcomes. An adopter two releases behind lost its lowered agent cap at dGroundRules, before dSafePassage's step kind existed. Its declarations had no item to walk. Its receipt never named the release it was "behind", while the early chain builds ran on mandates and witnesses that agents had typed.

2. **Findings**

### A4-F1 — dGroundRules retires `.agent-cap.conf` before any upgrade step or step gate exists
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0016`
- **Class:** K7, c3
- **Severity:** high
- **Scenario:** S7
- **Evidence:**
  - cl-0016 (dGroundRules) retires "agent-cap's slot ledger … its clamp of every bound to 1 to 5 … in the same unit with `.agent-cap.conf`, its refusal of a set `AGENT_CAP`".
  - The clause carries no upgrade step. `grep 'cl-dClosedLoop-0016\]' ac.tsv | grep -c -i 'upgrade step'` printed `0`.
  - The upgrade-step kind (cl-0018) and the step gate (cl-0027) arrive with dSafePassage, whose parent is dGroundRules.
  - Today, `tools/hooks/agent-cap.js:68-71` reads "`FANOUT_CAP=<n>` in a tracked `.agent-cap.conf` … makes the enforced cap min(n, 5)".
  - The `runtime.agents-in-flight` default is `6`.
- **Consequence:** An adopter whose `.agent-cap.conf` lowers the cap to 2 updates past dGroundRules' release, and its limit silently rises to 6. P38 is broken at the first chain release that touches an adopter.
- **Fix:** Defer the `.agent-cap.conf` and `AGENT_CAP` retirement to a unit that lands after dSafePassage. Ship it as an upgrade step that maps `FANOUT_CAP` to `runtime.agents-in-flight`, seen red on a planted conf. Alternatively, keep the conf read as a lowering override until that step lands.

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

### A4-F5 — `adopt.declarations` and `adopt.instructions` are named by clauses but have no item row
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0438`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S4
- **Evidence:**
  - cl-0438: "`adopt.declarations`: at install and update, today's flow and role customizations proposed as overlay rows for the owner to rule once".
  - Adopter-instructions item 15 names `adopt.instructions`.
  - The only adopt item rows in the copy are census, practices, decisions and reconstruct. `grep -n '| \`adopt\.' *.md` returns those four only, on flow-steps:611-615.
- **Consequence:** S4's "declarations proposed as overlay rows" has no actor, needs, witness or route. It also escapes the item join that `[adopt]` says reads repository-level items.
- **Fix:** Add rows for `adopt.declarations` (command proposes, then an owner ruling item, witnessed by the ruling records, then the overlay write) and for `adopt.instructions`, each with its Owner.

### A4-F6 — No clause makes the receipt name its release and remote, or cuts a release
- **Address:** architecture-v2 [chain] dShippedRelease row (`cl-dClosedLoop-0435`); layer-expansions [design-distribution]
- **Class:** K6, c2
- **Severity:** high
- **Scenario:** S4
- **Evidence:**
  - dShippedRelease owns `gap-deploy-11` ("No release has ever been cut") and `gap-deploy-12` ("A receipt records gov's source as a local path").
  - A grep of the chain for "release tag", "source remote", "local path", `gov_source` and `kits.cut` found no clause. Only cl-0414, "kit release notes", touches releases.
  - layer-expansions defines receipt "schema 4: per-kit versions, the release tag, the source remote". cl-0020 defines schema 4 as "gaining `steps`", and cl-0435 defines schema 5 as `superseded`, `deprecations` and `prior_commit`.
  - Today, `govkit.py:49` reads `RECEIPT_SCHEMA = 3`, and `:8020` writes `"gov_source": str(root)`.
- **Consequence:** "Two releases behind" cannot be computed. `kits.currency` and `install.from: release-tag` read a field nothing builds. Under strict's `currency.on-behind: red`, the currency leg stays a dead probe that is never green on every adopter landing. Two schema-4 definitions also collide.
- **Fix:** Add dShippedRelease clauses for `kits.cut` (the annotated `gov/v<date>.<n>` tag) and for a receipt schema step that adds the release tag and source remote and drops the local path. Restate distribution's receipt schema to match cl-0020 and cl-0435.

### A4-F7 — The floor step is "the step kind's first step", but its progress field only arrives in the schema-4 step
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0028`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S4
- **Evidence:**
  - cl-0028: "the interpreter floor raised to Python 3.15 as the step kind's first step".
  - cl-0019: "the receipt advancing per completed step".
  - cl-0020: "the receipt's schema 4 gaining `steps` … shipped as an upgrade step whose down restores schema 3".
  - No clause orders the two steps or says where a step completed against a schema-3 receipt records its progress.
- **Consequence:** An adopter on schema 3 runs the floor step first. Its completion has no `steps` field to land in, so a kill after it re-runs it or leaves the receipt unreadable to schema-3 readers.
- **Fix:** Declare the schema-4 `steps` step as step 0, with its witness the schema field itself. Order the floor step after it, and plant a kill between them.

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

### A4-F9 — `install.on-shim-call: refuse` and `install.retired-edits: delete` break P38 and P8, and two values have no arm
- **Address:** architecture-v2 [policies] `install.retired-edits`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S4
- **Evidence:**
  - The catalogue reads "`install.retired-edits` | order, keep, delete" and "`install.on-shim-call` | warn, journal, refuse".
  - P38: "keeps working, or warns, until its window closes". P8: "an update never overwrites or silently drops a repository's change".
  - cl-0026 plants only the `order` grading. cl-0023 sees each shim value.
- **Consequence:** An owner override can delete an adopter-edited retired file, or make a shimmed hook path fail during its window. Both happen inside S4's injected cases, and `keep` and `delete` are never seen red.
- **Fix:** Drop `delete` and `refuse`, or keep them with a recoverable copy and an order, declared as loosenings. Add planted arms for `keep` and `delete`.

### A4-F10 — The deviation record is no registered kind
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0004`
- **Class:** K3
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - cl-0004: "the deviation record, its kind joined to check 21's kinds".
  - `grep -n -i deviation` over the copy's layer-memory and memory-plan printed nothing. Stage 0's leads list this as "Found while the tooling was built".
- **Consequence:** dTrueNorth's records have no owner, writer or reader in the kind registry. K3 and P16's kinds register cannot see them, and dConvergedCharter's cl-0480 has no row to move.
- **Fix:** Add a `deviation` row to layer-memory's kind table: owner dTrueNorth, writer the departing unit's commit, readers deviations.py, asbuilt.py, cl-0119 and cl-0412.

### A4-F11 — dTrueNorth's deviation join needs approval rules that two later builds provide
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0004`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - cl-0004 is red on "an approver below the risk".
  - The risk-to-approver rule is `deviation.approval`, Owner dDeclaredLoop, built in cl-0119 "by dOrderedCharter's classifier".
  - dTrueNorth is the root, so even dGroundRules' policy reader lands after it. No stand-in is named.
- **Consequence:** dTrueNorth's unit cannot state which mapping its join reads. A spec writer hard-codes one that cl-0119 may later contradict.
- **Fix:** State in cl-0004 that the join reads by-risk with a fixed classifier until dDeclaredLoop lands `deviation.approval`, as deviations.py does, and add a tolerance row.

### A4-F12 — The product carries join reds two whole carriers only "and disagreeing"; the bootstrap instrument reds any two
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - cl-0002: "two specs carrying one clause whole and disagreeing".
  - carries.py:13 reds "two specs carrying one clause whole, or pinning it to two hashes".
  - whole-audit `[instruments]` reads "a clause carried whole twice".
  - research-final-coverage:123 reports `ambiguous: … carried whole by 2 specs`.
- **Consequence:** Once dTrueNorth's leg replaces the instrument, two agreeing whole carriers (one clause built twice) go green. The check silently loosens at the hand-over.
- **Fix:** Drop "and disagreeing" so any second whole carrier reds, matching the instrument and the prototype.

### A4-F13 — No clause builds P3's remote-CI verdict slot or the verdict-backend registry
- **Address:** architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - P3: "remote CI is a designed slot".
  - Its row names only cl-0342 and cl-0344.
  - `grep -i 'remote-ci\|backend registry\|verdict backend' ac.tsv` matched only cl-0029.
  - flow-steps `[test]` and layer-expansions `[core-points]` make the backend registry a Test point that dWitnessedBar should build.
- **Consequence:** The `verdict` key's `remote-ci` value and integrations' backend have no core point to register at, so part of P3 is enforced by nothing.
- **Fix:** Add a dWitnessedBar clause for the verdict-backend registry and its `remote-ci` slot, seen red on a planted unregistered backend, and list it in P3's row.

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

### A4-F19 — flow-steps `[revised]` names the retired key spelling `policy.on-missing-expansion`
- **Address:** flow-steps [revised]
- **Class:** K4
- **Severity:** low
- **Scenario:** S7
- **Evidence:** flow-steps:767 reads "from LR-4, `policy.on-missing-expansion`". The key is `policy-file.on-missing-expansion` (flow-roles-adoption `[renamed]`).
- **Consequence:** A reader inventory by value misses this citation.
- **Fix:** Rename the key, with a dated note.

### A4-F20 — `plan.lease`'s overlap outcome has no next route
- **Address:** flow-steps [plan] `plan.lease`
- **Class:** K2
- **Severity:** low
- **Scenario:** S7
- **Evidence:** The Then cell reads "held → `plan.recommend`; an overlap → noted on the card and in the other build's mailbox; refused → as `leases` says".
- **Consequence:** After an overlap is noted, it is unstated whether the build goes on to `plan.recommend`.
- **Fix:** Write "an overlap → noted …, then `plan.recommend`".

3. **The walk table**

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S4 | = | = | = | = | not on path: an adopter's update is no owner prompt and opens no build |
| `entry.intake` | S7 | orientation scout, where layer-roles names the hook | = | the scout-written intake entry, typed by the actor | = | A4-F2 |
| `entry.orient` | S4 | = | = | = | = | not on path: update runs outside any build |
| `entry.orient` | S7 | = | = | today's kickoff card until dPlacedRequest lands | = | holds |
| `entry.place` | S4 | = | = | = | = | not on path: update runs outside any build |
| `entry.place` | S7 | = | = | = | new routes to Plan items dRankedPlan builds later | A4-F14 |
| `entry.place-check` | S4 | = | = | = | = | not on path: update runs outside any build |
| `entry.place-check` | S7 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.place-owner` | S4 | = | = | = | = | not on path: update runs outside any build |
| `entry.place-owner` | S7 | = | = | = | = | not on path: placement defaults to agent-places |
| `entry.claim` | S4 | = | = | = | = | not on path: update claims no build slug |
| `entry.claim` | S7 | = | = | today's check_slug_claimed until dPlacedRequest lands | Plan, owned by a later build | A4-F14 |
| `plan.input` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.input` | S7 | = | = | = | = | holds |
| `plan.dedupe` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.dedupe` | S7 | = | = | = | = | holds |
| `plan.triage-rule` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.triage-rule` | S7 | = | = | = | = | holds |
| `plan.triage-judge` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.triage-judge` | S7 | = | = | = | = | not on path: each chain build is selected by the owner's request |
| `plan.record` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.record` | S7 | = | = | = | = | holds |
| `plan.research` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.research` | S7 | = | = | = | = | holds |
| `plan.place` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.place` | S7 | = | = | = | = | holds |
| `plan.lease` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.lease` | S7 | = | = | today's run claim until dPlacedRequest lands | overlap outcome ends with no next route | A4-F20 |
| `plan.recommend` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.recommend` | S7 | = | = | = | = | holds |
| `plan.reason` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.reason` | S7 | = | = | = | = | holds |
| `plan.exit` | S4 | = | = | = | = | not on path: update runs outside any build |
| `plan.exit` | S7 | = | = | ratification carried by the planner's typed record | = | A4-F3 |
| `design.input` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.input` | S7 | = | = | = | = | holds |
| `design.reentry` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.reentry` | S7 | = | = | = | = | not on path: no amendment is injected in the bootstrap |
| `design.inventory` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.inventory` | S7 | = | = | = | = | not on path: no plan revision is injected in the bootstrap |
| `design.seams` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.seams` | S7 | = | = | = | = | holds |
| `design.decompose` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.decompose` | S7 | = | = | = | = | holds |
| `design.research` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.research` | S7 | = | = | = | = | holds |
| `design.overlaps` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.overlaps` | S7 | = | = | = | = | holds |
| `design.streams` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.streams` | S7 | = | = | = | = | not on path: design.streams holds for no solo chain build |
| `design.unit-spec` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.unit-spec` | S7 | = | = | = | = | holds |
| `design.recommend` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.recommend` | S7 | = | = | = | = | holds |
| `design.reason` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.reason` | S7 | = | = | = | = | holds |
| `design.ready` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.ready` | S7 | = | = | the carries instrument until dIndexedDesign lands | = | holds |
| `design.exit` | S4 | = | = | = | = | not on path: update runs outside any build |
| `design.exit` | S7 | = | = | coverage read by an instrument stricter than the product join | = | A4-F12 |
| `build.base` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.base` | S7 | = | = | = | = | holds |
| `build.unit-lease` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.unit-lease` | S7 | = | = | = | = | holds |
| `build.unit-pass` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.unit-pass` | S7 | = | = | deviation population joined to an unregistered kind and a later approval rule | = | A4-F10, A4-F11 |
| `build.acceptance` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.acceptance` | S7 | = | = | = | = | holds |
| `build.scope` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.scope` | S7 | = | = | = | = | holds |
| `build.reuse-check` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.reuse-check` | S7 | = | = | = | = | holds |
| `build.recommend` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.recommend` | S7 | = | = | = | = | holds |
| `build.ratify` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.ratify` | S7 | = | = | = | = | not on path: runs only under decisions.major author-owner-ratifies |
| `build.distill` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.distill` | S7 | = | = | = | = | holds |
| `build.core` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.core` | S7 | = | = | = | = | holds |
| `build.exit` | S4 | = | = | = | = | not on path: update runs outside any build |
| `build.exit` | S7 | = | = | = | = | holds |
| `test.merge` | S4 | = | = | gov-first steps in the prepared merge, the floor step first with no steps field | = | A4-F7 |
| `test.merge` | S7 | = | = | = | = | holds |
| `test.select` | S4 | = | = | = | = | holds |
| `test.select` | S7 | = | = | = | = | holds |
| `test.verdict` | S4 | = | = | = | = | holds |
| `test.verdict` | S7 | = | = | no registered remote-ci slot behind P3 | = | A4-F13 |
| `test.route` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.route` | S7 | = | = | = | = | holds |
| `test.attribute` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.attribute` | S7 | no tester before dWitnessedBar lands | = | = | = | A4-F14 |
| `test.flakes` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.flakes` | S7 | = | = | = | = | holds |
| `test.seen-red` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.seen-red` | S7 | = | = | = | = | holds |
| `test.recommend` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.recommend` | S7 | = | = | = | = | holds |
| `test.reason` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.reason` | S7 | no tester before dWitnessedBar lands | = | = | = | A4-F14 |
| `test.exit` | S4 | = | = | = | = | not on path: the adopter's own bar is no build's Test |
| `test.exit` | S7 | = | = | = | Deploy items owned by dShippedRelease, later | A4-F14 |
| `deploy.current` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.current` | S7 | today's push-main until dShippedRelease lands | = | = | = | A4-F14 |
| `deploy.mandate` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.mandate` | S7 | = | = | intake record whose writer is the scout | = | A4-F2 |
| `deploy.parents` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.parents` | S7 | = | = | = | = | holds |
| `deploy.land` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.land` | S7 | = | = | = | = | holds |
| `deploy.core` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.core` | S7 | = | = | = | = | holds |
| `deploy.record` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.record` | S7 | = | = | = | = | holds |
| `deploy.distill` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.distill` | S7 | = | = | = | = | holds |
| `deploy.recommend` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.recommend` | S7 | = | = | = | = | holds |
| `deploy.notify` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.notify` | S7 | = | = | = | = | holds |
| `deploy.released` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.released` | S7 | = | = | = | = | holds |
| `deploy.snapshot` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.snapshot` | S7 | = | = | = | = | holds |
| `deploy.unlease` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.unlease` | S7 | = | = | = | = | holds |
| `deploy.close` | S4 | = | = | = | = | not on path: the adopter lands with its own lander |
| `deploy.close` | S7 | = | = | = | = | holds |
| `review.trigger` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.trigger` | S7 | = | = | = | = | holds |
| `review.pin` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.pin` | S7 | = | = | = | = | holds |
| `review.lens` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.lens` | S7 | = | = | = | = | holds |
| `review.refute` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.refute` | S7 | = | = | = | = | holds |
| `review.report` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.report` | S7 | = | = | = | = | holds |
| `review.dispose` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.dispose` | S7 | = | = | = | = | holds |
| `review.fold` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.fold` | S7 | = | = | = | = | holds |
| `review.cost` | S4 | = | = | = | = | not on path: an update opens no breakpoint |
| `review.cost` | S7 | = | = | = | = | holds |
| `probe.trigger` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.trigger` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.pin` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.pin` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.design` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.design` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.experiment` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.experiment` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.run` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.run` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.judge` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.judge` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `probe.return` | S4 | = | = | = | = | not on path: no probe is placed or raised in an update |
| `probe.return` | S7 | = | = | = | = | not on path: no probe is placed or raised in the bootstrap |
| `life.request` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.request` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `life.quiesce` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.quiesce` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `life.notify` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.notify` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `life.snapshot` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.snapshot` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `life.unlease` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.unlease` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `life.close` | S4 | = | = | = | = | not on path: no owner control is injected in S4 |
| `life.close` | S7 | = | = | = | = | not on path: no owner control is injected in S7 |
| `adopt.census` | S4 | = | = | = | = | not on path: the census runs once at adoption or at the owner's ask |
| `adopt.census` | S7 | = | = | = | = | not on path: gov is adopted before the chain opens |
| `test.seed` | S4 | = | = | = | = | holds |
| `test.seed` | S7 | = | = | today's seeding until dWitnessedBar lands cl-0353 | = | holds |
| `adopt.practices` | S4 | = | = | = | = | not on path: practices are ruled once at adoption |
| `adopt.practices` | S7 | = | = | = | = | not on path: gov is adopted before the chain opens |
| `adopt.decisions` | S4 | reviewer and owner, two kinds in one item | = | = | = | A4-F15 |
| `adopt.decisions` | S7 | = | = | = | = | not on path: gov is adopted before the chain opens |
| `adopt.reconstruct` | S4 | = | = | = | = | not on path: default on-touch never runs it at update |
| `adopt.reconstruct` | S7 | = | = | = | = | not on path: default on-touch never runs it |
| `maintain.lease` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.lease` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.read` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.read` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.direct` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.direct` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.patch` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.patch` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.file` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.file` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.levels` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.levels` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `maintain.record` | S4 | = | = | = | = | not on path: Maintain takes no part in an update |
| `maintain.record` | S7 | = | = | = | = | not on path: no chain build needs Maintain to land |
| `loop.lease` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.lease` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `loop.gather` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.gather` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `loop.price` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.price` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `loop.propose` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.propose` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `loop.file` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.file` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `loop.record` | S4 | = | = | = | = | not on path: the Loop Review takes no part in an update |
| `loop.record` | S7 | = | = | = | = | not on path: no chain build needs the Loop Review to land |
| `release.pick` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.pick` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `release.approve` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.approve` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `release.promote` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.promote` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `release.verify` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.verify` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `release.route` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.route` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `release.record` | S4 | = | = | = | = | not on path: an update promotes nothing |
| `release.record` | S7 | = | = | = | = | not on path: build.closes is at-landing with no environment |
| `kits.version` | S4 | = | = | = | = | holds |
| `kits.version` | S7 | = | = | today's push-main prepare mint | = | holds |
| `kits.cut` | S4 | = | = | the release tag is cut by no clause | = | A4-F6 |
| `kits.cut` | S7 | = | = | = | = | not on path: no release is cut before dShippedRelease lands |
| `kits.currency` | S4 | = | = | the receipt names no release to count from | = | A4-F6 |
| `kits.currency` | S7 | = | = | = | = | not on path: no release exists in the bootstrap |
| `kits.adopters` | S4 | = | = | = | routes on deploy.currency's values without naming the key | A4-F18 |
| `kits.adopters` | S7 | = | = | = | = | not on path: no release exists in the bootstrap |
| `kits.offer` | S4 | = | = | push grant prefix scope unprobed | = | A4-F8, A4-F17 |
| `kits.offer` | S7 | = | = | = | = | not on path: no release exists in the bootstrap |
| `kits.install` | S4 | the owner, or a command | = | = | one route only | A4-F4 |
| `kits.install` | S7 | = | = | = | = | not on path: no fresh install in the bootstrap |
| `kits.update` | S4 | the owner, or a command | = | receipt with no steps field and no release | no route for step failure, lock, hold or order | A4-F1, A4-F4, A4-F5, A4-F7, A4-F9 |
| `kits.update` | S7 | = | = | dSafePassage's gov-first update on gov | no outcome set for the step walk | A4-F4 |

4. **Build verdicts**

| dTrueNorth | A4-F10, A4-F11, A4-F12 |
| dGroundRules | A4-F1 |
| dSafePassage | A4-F7, A4-F9 |
| dShippedRelease | A4-F4, A4-F5, A4-F6, A4-F8, A4-F17, A4-F18 |
| dConvergedCharter | A4-F16 |
| dMindYourWords | holds |

5. **Principle verdicts**

| P3 | A4-F13 |
| P8 | A4-F5, A4-F9 |
| P10 | holds |
| P16 | A4-F10 |
| P28 | holds |
| P37 | A4-F7 |
| P38 | A4-F1, A4-F4, A4-F7, A4-F9 |
| P41 | A4-F10, A4-F11, A4-F12 |
| P42 | holds |

# Skeptic brief: run A, batch 1

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a1/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

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

### A3-F6 — The shared rework budget has no declared home or writer once its build closes
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0115`, `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `cl-0115` says the budget is "one per build in its transition record … keyed to the build". `cl-0440` says a patch build draws "on the originating build's rework budget, so a chain of patch builds shares one budget". The originating build's transitions end at `deploy.close`. No clause names the record that takes a patch's draws, or how draws from two nodes serialise.
- **Consequence:** Concurrent patch builds read the same remaining budget and both draw on it. Either the draws go to an unwritten record, or one draw is lost.
- **Fix:** Add a budget ledger per root build, appended by compare-and-swap under the root's claim ref, with each patch reaching its root through its `patches` edge. Show it red on two planted concurrent draws.

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

### A1-F3 — `cl-dClosedLoop-0093`, P23's only enforcer, is carried by no clause
- **Address:** architecture-v2 [chain] dDeclaredLoop row; architecture-v2 [enforcement] `P23` row
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - [enforcement] reads "| `P23` | `cl-dClosedLoop-0093` |".
  - Probe: `grep -rn 'cl-dClosedLoop-0093' <copy> --include=*.md` printed only v2:1707, the enforcement row.
  - A probe parsing every `[chain]` clause printed `495` clauses and "gap after 0092 -> 0094".
  - The dDeclaredLoop row goes from the position engine `cl-dClosedLoop-0092` straight to "each step's items declared ..." `cl-dClosedLoop-0094`.
  - [clause-ids] says "Retired: none", and the next id minted is 0497.
- **Consequence:** P23 ("Claims are trusted by key and source") has no clause, so no chain spec can carry it. The carries join reds a ghost id at dDeclaredLoop's Design exit (c1). In S1, `entry.claim`'s "a retry that finds its own key counts as claimed" rests on a rule that nothing builds.
- **Fix:** Restore the dDeclaredLoop clause for claims trusted by recomputed key and source, with id `cl-dClosedLoop-0093`, or list 0093 as retired and re-point P23's row. Confirm that `stage0.py --root <copy> --arms K5` reds it.

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

### A1-F9 — P14's "review lenses read the active practices' reach" has no enforcing clause
- **Address:** architecture-v2 [enforcement] `P14`; architecture-v2 [principles] P14
- **Class:** K5
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - P14 says "stage contracts, role handoffs and review lenses read the active practices' reach for their stage".
  - Its row names `cl-dClosedLoop-0031` (the catalogue) and `cl-dClosedLoop-0051` ("reach per step rendered as step-scoped units handed in work orders").
  - Probe: `grep -iE 'lens' clauses.txt | grep -iE 'practice|reach'` printed nothing.
- **Consequence:** S1's spec audit and closing review run lenses that read no practice reach, so a practice does not redefine review as P14 says. No dFairHearing or dCalibratedLens spec has a clause to carry this.
- **Fix:** Add a clause, in dFairHearing's lens catalogue or dCalibratedLens's stage lenses, by which each lens loads the active practices' reach for its stage, seen red on a planted practice whose reach a lens omits. Add it to P14's row.

### A5-F10 — P23's only enforcing clause id is a ghost
- **Address:** architecture-v2 [enforcement] `P23`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `| \`P23\` | \`cl-dClosedLoop-0093\` |`. The id appears once in v2, in that row.
  - A probe parsing every `[chain]` clause found 495 clauses. Missing id: `['0093']`. dDeclaredLoop's row jumps from `cl-dClosedLoop-0092` to `cl-dClosedLoop-0094`.
- **Consequence:** P23 ("Claims are trusted by key and source") has no clause that enforces it. That matters in S6 wherever a refusal's claim is re-read.
- **Fix:** Restore the dropped clause into dDeclaredLoop's row with its id, or retire 0093 and name P23's real enforcing clauses.

### A2-F1 — P23's only enforcing clause, `cl-dClosedLoop-0093`, exists nowhere in the chain
- **Address:** architecture-v2 [enforcement] `P23`, and [chain] dDeclaredLoop `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2:1707 reads `| P23 | cl-dClosedLoop-0093 |`. `grep -rn "cl-dClosedLoop-0093"` over the copy's `build/` matches only that row. dDeclaredLoop's row jumps from `…verdict printed cl-dClosedLoop-0092` to `…witness cl-dClosedLoop-0094` (v2:1638). [clause-ids] says "Retired: none", and the next id to mint is 0497.
- **Consequence:** In S2, node x acts on X's witnesses, X's card and Y's interface keys, which come from another node and another harness. P23 says such a claim is acted on only when its key recomputes. No clause builds that check, so a stale or agent-typed claim pulled from the remote is acted on unchecked. The principle has no enforcer.
- **Fix:** Restore clause 0093 on dDeclaredLoop's row (claims trusted by key and source: recompute the key, refuse a source an agent typed, re-derive otherwise), seen red on a planted stale key. Or list 0093 under Retired and name another clause in P23's row.

### A3-F17 — `cl-dClosedLoop-0093` is carried by no clause, so P23's only enforcer is a ghost id
- **Address:** architecture-v2 [enforcement] `P23`; [chain] dDeclaredLoop
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S5
- **Evidence:** A probe over v2's `[chain]` found 495 distinct ids, with `[93]` the only one missing from 1..496. `[enforcement]` lists "`P23` | `cl-dClosedLoop-0093`". dDeclaredLoop's row jumps from `0092` to `0094`. `[clause-ids]` says "Retired: none".
- **Consequence:** "Claims are trusted by key and source" has no clause, which is the guard S5's replayed claim needs.
- **Fix:** Restore the dDeclaredLoop clause carrying `cl-dClosedLoop-0093`, or retire the id and name an enforcing clause in P23's row.

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

## Clean cells to attack

- `deploy.close` in S7
- `deploy.distill` in S7
- `entry.claim` in S2
- `design.input` in S6
- `plan.triage-rule` in S7
- `plan.recommend` in S5
- `build.recommend` in S2
- `deploy.land` in S7

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `AS1-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a1/` only. Your effort is the one the owner's
role definition sets.

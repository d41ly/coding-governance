# Skeptic brief: run C, batch 2

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run C of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c2/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

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

### C2-F13 — The termination check's red case plants only a raised budget
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0118`
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - stall-and-loop [design] item 8: "raising any loop bound (the budget, a round count, a retry count, a deadline) is a loosening".
  - 0118 states the rule for "a loop bound" but plants only "an unattended raise of the budget".
- **Consequence:** An unattended raise of `review.max-rounds`, `flow.route-backs` or `flow.wait-ceiling` can pass a check that was only ever seen red on the budget, so the guard certifies more than it checks.
- **Fix:** Add one planted unattended raise each for a round count, a retry count and a deadline to 0118's red list.

### C2-F10 — dPlacedRequest's keys `leases.granularity` and `card.follows` are named by no clause
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0120` and `cl-dClosedLoop-0121`
- **Class:** K4
- **Severity:** low
- **Evidence:** Stage 0 K4 lists both as "read by no chain clause and no item". 0120 says only "one lease grammar for builds, units and cadence runs". 0121 does not say when the card re-renders.
- **Consequence:** Presets set these keys (velocity sets `leases.granularity` to `build`), but nothing reads them.
- **Fix:** Name `leases.granularity` in 0120 and `card.follows` in 0121, each with one arm per value.

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

### C2-F15 — The mailbox message kind names no writer item and no reader
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0143`
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - Stage 0 K3: "mailbox-message: no writer item … no reader: no item waits on its writer or names it".
  - coordination item 6 says "every transition reads the build's mailbox and is refused while a message … is neither answered nor acknowledged". 0143 says only "read and disposed at every transition".
- **Consequence:** The refusal that makes a transition wait on an unanswered message has no item to carry it, so a spec can build the mailbox without it.
- **Fix:** In 0143, name the writer (the posting command per kind) and the reader: each exit item refuses on an undisposed message until `flow.wait-ceiling`. Plant one red case.

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

### C3-F29 — The deployer's registration omits distribution's contract
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0166
- **Class:** K10
- **Severity:** low
- **Evidence:** layer-roles [roster] says: "deployer | distribution, integrations | … The deployer acts for two expansions: release notes for distribution, and verify judgment for integrations". Clause 0166 says: "registered through the integrations and observability layer contracts".
- **Consequence:** The release-notes item has a role that its expansion never registers, so P28's no-expansion-role-in-core arm may red on it.
- **Fix:** Add distribution's contract to 0166.

### C3-F1 — P18's ranking of a fork's options is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0176
- **Class:** K5, c5
- **Severity:** high
- **Evidence:** v2 [principles] P18 says: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record … only options the core admits are options". Clause 0176 says only: "every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says (LR-3)". The other clause in P18's row is 0390, which says only "fork resolution by `design.forks`". `grep -c 'feature-rich'` on v2 returns 4 hits, none of them in a clause. Stage 0 raised this as its K5 lead.
- **Consequence:** dBoundRoles builds fork resolution with no ranking rule and no "admitted options only" check. An unattended role can pick any option and still pass. This is the principle's core rule.
- **Fix:** Add the ranking (most feature-rich, then most expandable), the core-admitted option set and the full record to 0176. Add a planted fork whose recorded pick is not the top-ranked admitted option, and see it red.

### C3-F2 — `instructions.task-charter` is read by no clause, though dBoundRoles owns it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies]: "`instructions.task-charter` | when-not-static, always | … the single-carry check refuses `always` on a backend that loads the static block … | dBoundRoles". systems [design-instruction] says: "The single-carry check reads `instructions.task-charter` and the harness kind". Clause 0180 says only: "the role static block carried once per spawn". Stage 0's K4 lists the key as "read by no chain clause and no item".
- **Consequence:** The single-carry check is built without its key. Either `always` is accepted where the charter loads twice, or the key's value never routes.
- **Fix:** Have 0180 name `instructions.task-charter` and its refusal of `always` on a static-block backend, seen red on a planted `always`.

### C3-F3 — gap-roles-20, the static block's budget covering only its base body, is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-register gap-roles-20 says: "The static block's budget covers its base body only". research-instruction-writing-b N3 says: "The 2,487–4,220 B charter blocks per role sit outside `BODY_CEILINGS`". In code, `tools/roles/check_roles.py:84` reads "Bytes of each slot's BASE body". dBoundRoles owns the gap, but no clause of 0166–0191 budgets the whole rendered block.
- **Consequence:** The gap stays open after its owner lands, and the rendered charter blocks remain unbudgeted.
- **Fix:** Extend 0180: the budget covers the whole rendered static block, seen red on a planted charter block that pushes a role over its ceiling.

### C3-F8 — The answered-call hook omits the verifier exemption, so the default `refuse` blocks a verifier reading its subject
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0197
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [trust] item 10 says: "A verifier's read of its subject is never an answered call, and neither is a read the packet does not cover". It also says: "Below CLI 2.1.295, a rule on an ungated tool … stays open when its hook fails … a failure is recorded". Clause 0197 says only: "the answered-call hook (`roles.answered-calls`)". `roles.answered-calls` defaults to `refuse`.
- **Consequence:** A reviewer's or tester's read of its handed subject at the same blob is refused, and verification stalls. The fail-open window also goes unrecorded.
- **Fix:** Carry both rules in 0197. See it green on a planted verifier read of its subject, and see a recorded failure on a planted hook crash.

### C3-F4 — Replacing the protocol pointers omits the same-unit re-point of the machinery that asserts them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0199
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [tags] says: "The unit that slices them re-points that machinery in the same unit: `CARRIED_SECTIONS`, `check_roles.py` R0 …, R5 and R10 …, and `render_agents.py`'s self-test arm 4". Clause 0199 says only: "the role files' re-verification orders and protocol pointers replaced by rendered slices". In code, `tools/roles/roles_lib.py:67` reads `CARRIED_SECTIONS = ("Protocols", "Facts")`. `check_roles.py:169` reads the carried Protocols body, and `render_agents.py:83,335` asserts the carried text.
- **Consequence:** Built from the clause, the slicing unit leaves R5, R10 and the self-test asserting the Protocols carry. The roles catalogue goes red, or the whole-document carry survives beside the slices.
- **Fix:** Name the four consumers in 0199 and require them re-pointed in the same unit.

### C3-F6 — Role metrics are written into the value ledger, which a later build registers, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0201
- **Class:** K6
- **Severity:** medium
- **Evidence:** Clause 0201 says: "role metrics per role and item into the value ledger". layer-memory [contract] says: "value ledger | dCalibratedLens | a generated library view". 0459 (dCalibratedLens) builds "the shared value ledger". dCalibratedLens is no ancestor of dFurnishedOrders, whose only parent is dBoundRoles.
- **Consequence:** dFurnishedOrders cannot be specced or landed in order (c1-like). Its writer has no registered kind to write.
- **Fix:** Have 0201 write a metrics record dFurnishedOrders owns, which dCalibratedLens's ledger reads later. Alternatively, add a stand-in until 0459 lands.

### C3-F5 — Five keys dFurnishedOrders owns are read by none of its clauses, three of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] gives dFurnishedOrders `annotations.delivery` (work-order, on-demand, off), `roles.orientation.house-index` (handed, pointer, off), `instructions.slices` (handed, pointer), `retrofit.slot-bytes` (512, 1024, 2048) and `memory.map-unfold` (item-declared, none, all). Stage 0's K4 lists all five as unread, three of them guard-bearing. Clauses 0192–0211 name none of them. 0202 says "legacy slot in its four states" with no cap key, and 0203 says "the unfolds each item declares (PM-6)" with no key.
- **Consequence:** Each key's non-default value never routes. The legacy slot's 1 KB cap (systems [cross]) and the code-notes delivery have no switch.
- **Fix:** Name each key in the clause that builds its slot: 0202 for `retrofit.slot-bytes`, 0209 for `annotations.delivery`, 0199 for `instructions.slices`, 0203 for `memory.map-unfold`, and a slot clause for `roles.orientation.house-index`. Each value is routed and seen.

### C3-F7 — The memory slices read a sibling build's index and keys with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K6
- **Severity:** medium
- **Evidence:** Clause 0202 says: "the work order's memory slices … each under its own budget and its own answer (systems `[cross]`)". systems [cross] says the slices are "priced by `memory.item-budget`. Over it, they are answered by `memory.over-budget`", both owned by dTotalRecall, and sections resolve through dTotalRecall's `record show` (0220). dTotalRecall is a sibling, not an ancestor. Sibling clauses carry stand-ins ("not installed until dTotalRecall's renderer lands" in 0203, the same for 0208), but 0202 has none.
- **Consequence:** The slot cannot be built in order, or it is built against a section index that does not exist yet.
- **Fix:** Add a stand-in: the memory slot renders "not installed" until dTotalRecall's section extractors land, the same way 0203 and 0208 do.

### C3-F10 — The slug grammar omits "binds new mints only", BUILD_SLUG_RE's derivation and the named flips
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0216
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-memory [names] says: "A changed grammar binds new mints only. Existing slugs and ids keep their form, every reader accepts both, and the grammar in force at minting is recorded with each slug". It also says "`BUILD_SLUG_RE` … becomes derived from the `builds.slug-*` keys" and "The flips are named: `slug-words` 1 and 3, …". Clause 0216 says only: "proven by flipping the grammar in a scratch clone".
- **Consequence:** A grammar flip makes every reader reject existing slugs and ids across the tree (a migration across a drain). The flip test is also unspecified, so it can pass on one flip.
- **Fix:** Carry the new-mints-only rule, the recorded grammar per slug, the derived `BUILD_SLUG_RE` and the named flip set in 0216.

### C3-F9 — Typed relations drop the `depends-on` cycle check and the pending-target rule
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0217
- **Class:** K10, c3
- **Severity:** medium
- **Evidence:** layer-memory [relations] says: "every relation's target must exist, and `depends-on` must form no cycle … A target found nowhere is pending, not red, until its build lands". gap-mem-07 says: "… no cycle check". Clause 0217 says: "typed relations (…), inverted, checked both ways and rendered as the relation graph".
- **Consequence:** A `depends-on` cycle passes the check, leaving gap-mem-07 open. Otherwise a target on another node's unlanded branch is red, refusing legitimate work.
- **Fix:** Add both rules to 0217: red on a planted two-build cycle, and pending on a planted target on another node's branch.

### C3-F11 — The code record's re-timing has no losing bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0219
- **Class:** K10
- **Severity:** medium
- **Evidence:** v2 [owed] says: "the code record's cold derivation re-timed at dTotalRecall's first unit: over 30 s or over 1 MB loses, on gov's tree and on a planted adopter-scale fixture". Clause 0219 says only: "re-timed on a planted adopter-scale fixture (the shape audit)".
- **Consequence:** The re-timing cannot fail, so an over-budget derivation ships.
- **Fix:** Put the 30 s and 1 MB loss bound, on both trees, into 0219.

### C3-F16 — Memory keys dTotalRecall owns are read by no clause, one of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0220
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] lists `memory.over-budget` (refuse, report, off, exempt from `budgets.enforce`), `memory.superseded-slices` (refuse, mark) and `memory.map-overflow` (degrade, refuse), all dTotalRecall's. systems' checks table gives "superseded slices | a superseded decision handed to a builder". Clause 0220 says "reported when exceeded, MS-3" without the key. No clause carries superseded slices, and 0225 says "degraded in a fixed order" without the key or `refuse`. Stage 0's K4 lists all three.
- **Consequence:** `refuse` and `off` never route, the superseded-slice check is never built, and the exemption from `budgets.enforce` is lost.
- **Fix:** Name the three keys with their values and checks, in 0220 and 0225.

### C3-F12 — The acceptance re-measure has no target or window
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0223
- **Class:** K10
- **Severity:** medium
- **Evidence:** systems [design-memory-structure] says: "Thirty days after landing, the median memory bytes per agent that reads memory are below 33 KB … Why the first measure could not fail". Clause 0223 says only: "the acceptance re-measure counted over every read channel".
- **Consequence:** The measure has no pass bar, which repeats the "could not fail" defect the record already corrected.
- **Fix:** Add "median below 33 KB, 30 days after landing" to 0223.

### C3-F13 — The map's losing replay has no loss conditions
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0228
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** project-map [test] says: "The map loses, and is not built, if any of these holds: the recall of the known set rises by less than the twin runs' difference plus 5 items; the median of existence searches per lens falls by less than one; the bytes read before the first act rise by more than the map's own bytes". Clause 0228 says only: "the replay with the map and without at its first unit … so a losing map is never built".
- **Consequence:** "Losing" is undefined, so the replay certifies the map whatever it scores, and the routed loss path never runs.
- **Fix:** Carry the three loss conditions, and the twin runs they compare against, in 0228. The same applies to 0253's extension to code.

### C3-F14 — Renaming the Serves kind `journal` to `log` ships with no adopter alias step
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0231
- **Class:** K10
- **Severity:** high
- **Evidence:** memory-plan [integration] says: "distribution | dTotalRecall's upgrade steps in each adopter: the `journal` alias, and the retag step". [migration] says: "the `journal` kind is read through its alias". Clause 0229 says: "the Serves kind `journal` renamed `log`". Clause 0231 lists only "the `--new-build` and `--new-spec` scaffold verbs …, an adopter's README front matter graded …, and the retag step".
- **Consequence:** After update, an adopter's records carrying `**Serves:** journal` (1,436 such records in gov) fail the Serves grading or lose their kind. This breaks P38.
- **Fix:** Add the `journal` alias upgrade step to 0231, seen on a planted adopter record with `Serves: journal`.

### C3-F17 — The reuse scout's acceptance re-runs the benchmark with no threshold
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0239
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] says: "acceptance re-runs aScoutedSeam's 24-case benchmark against the built index and entries, and must meet M1c's 16". research-scoutedseam-apply measured "held-out set … m1c 8/12". Clause 0239 says: "accepted by re-running aScoutedSeam's benchmark and its twelve held-out cases …", with no bar.
- **Consequence:** The acceptance passes at any score, so a house index that loses to today's 13/24 checklist scout ships.
- **Fix:** Put the pass bar in 0239, on the tuning set and on the 12 held-out cases.

## Clean cells to attack

- `cl-dClosedLoop-0161` in dKeptSession
- `cl-dClosedLoop-0475` in dConvergedCharter
- `cl-dClosedLoop-0482` in dConvergedCharter
- `cl-dClosedLoop-0162` in dKeptSession
- `cl-dClosedLoop-0096` in dDeclaredLoop
- `cl-dClosedLoop-0160` in dKeptSession
- `cl-dClosedLoop-0151` in dKeptSession
- `cl-dClosedLoop-0126` in dPlacedRequest

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <clause> <build>: holds`, or `- <clause> <build>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `CS2-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c2/` only. Your effort is the one the owner's
role definition sets.

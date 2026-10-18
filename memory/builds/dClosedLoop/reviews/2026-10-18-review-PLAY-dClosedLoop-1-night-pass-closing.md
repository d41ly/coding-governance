**Serves:** diff-review PLAY-dClosedLoop-1

# Review: dClosedLoop's night pass, closing review (round 1)

Tier-2 diff review of the night pass, run by the gov-diff-reviewer finders and gov-skeptic batches and written by gov-synthesizer, 2026-10-18.

Range: beda01950b99c0c11e91fe2f12e5d019be39536d...9ab7a5c5cffa27b405c9caafa92d105db8a07ea0 (round 1)

## Verdict: CLEAN WITH FIXES

There is no blocker, and there are 3 high items covering 4 confirmed findings. Every item is a defect in a design record or in the build's instruments, and each one is fixable in place. The fold is sound in shape. Its weak spots are three:

- its claim that every new later-build dependency is slotted or classed is false;
- the new `repeat` disposition has no transition row;
- the map's fates arms fail soft when the fates record is missing.

## Review shape

Review shape: intensity light, raw 31, confirmed 30, refuted 1, unverified 0 (0 uncertain), precision 0.97.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 14 | 14 | 0 | 0 | 0 | 1.00 |
| seams | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, by item: 0 blocker, 3 high, 16 medium and 7 low, for 26 items. By raw confirmed finding: 0 blocker, 4 high, 16 medium and 10 low, for 30 findings. Finding 23 was refuted and is not reported.

Run integrity:

- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 26 judged sound, 4 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. Where a fix was judged unsound, the item carries the skeptic's corrected fix.
- Severity on confirmed findings: 0 ungraded, 2 re-graded by the skeptic (findings 26 and 28).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

The run is not complete in every respect, because 4 fixes were judged unsound and 2 grades were changed.

Other run facts:

- Intensity was light. The security and intent lenses were NOT run, so their classes were swept only through the checklist shares. This is not a full review.
- Intent came from 22 spec documents supplied as `specs`, beside the range's commit messages.
- The checklist held 29 items, each assigned to exactly one of the 3 lenses: correctness 10, seams 10, verification 9.
- By design: the caller's byDesign.

## High

### H1. The `repeat` disposition has no transition row and no Design entry (finding 1)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:585` ([transitions], lines 575-590); `entry.place` (line 78); `entry.claim` (line 81); [design]'s inputs (lines 161-167); `design.input` (line 172); v2's P20 (`2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:587`).
- **What is wrong:** `entry.place` and `entry.claim` send `repeat` to `entry.claim` and then to Design as a playbook run. [transitions] has a `none` → designing row only for `patch`, and the engine refuses any transition the table lacks (line 579). [design] has no playbook-run input, and `design.input`'s Then cell has no such branch. P20, amended in this diff, still names only in-goal amendments and patch builds as entering at Design.
- **Consequence:** Every repeat-placed playbook run reaches a transition the engine refuses, so point 1's seat for playbook mode cannot run. The dDeclaredLoop builder who builds the table will be misled.
- **Fix (skeptic judged it SOUND):**
  - Add a [transitions] row: `none` | the placement disposition `repeat`, its slug claimed and its lease taken by `entry.claim` | designing | the playbook reference, the claim ref and the lease record.
  - Add 'a playbook run, its playbook supplying the feature design' to [design]'s Enters list.
  - Add a `repeat` branch to `design.input`'s Then cell.
  - Amend P20 to name repeat builds.
- **Probe:** grep [transitions] for `repeat`. Today it finds nothing.
- **Left-shift gate:** a check that every disposition `entry.place` routes has a [transitions] row whose from-state is `none`. Seen red on today's tree.

### H2. "No edge changed; every new dependency slotted or classed" is false (finding 15)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:482` ([chain-impact]).
- **What is wrong:** Five new clauses depend on a build that is not an ancestor of the build that owns them. None has a class row in the re-cut's [reconciled-order], and none has a slot that renders 'not installed':
  1. dDeclaredLoop's `repeat` disposition routes onto dIndexedDesign's playbook record kind (flow-steps:78).
  2. dWitnessedBar's 'playbook set record and its set check at Test' joins the pieces of a dIndexedDesign playbook.
  3. dDeclaredLoop's `probe.design` is acted by the tester, which `probe.verifier` defaults to (v2:848). That tester is dBoundRoles' 'tester agent, absent today', and the program uses dBoundRoles' `experiment` kind and its `probe` return outcome.
  4. dIndexedDesign's research harness is 'built on the `experiment` shape'.
  5. dDeclaredLoop's attendance rule turns on the `step —` announcement, which is dWellOiledMachine's.

  Over v2's [chain] parents, every one of these pairs is 'ancestor? False'. `reconcile_probe.py` still prints findings 0, because its cites rule matches only backticked tokens and these clauses write 'playbook', 'playbook set', 'tester' and 'experiment' as plain words.
- **Consequence:** The probe certifies an order that does not hold. dDeclaredLoop, dWitnessedBar and dIndexedDesign would land items whose actor or record kind does not exist yet.
- **Fix (skeptic judged it SOUND):** For each dependency, do one of three things:
  - give it a class row in [reconciled-order];
  - give it a declared not-installed fallback, for example `repeat` refused or filed as an ask until dIndexedDesign lands, and `probe.design` falling back to the asking role until the tester lands;
  - move the clause to the owning build.

  Then widen `reconcile_probe.py`'s cites rule so it matches a record kind's or a role's plain spelling as well as its backticked one, and see it red on the current dDeclaredLoop row before the class rows land. Correct the [chain-impact] bullet.
- **Left-shift gate:** the widened cites rule above, with a plant: one plain-word dependency on a non-ancestor that must red.
- Medium items M1 (finding 3) and M2 (finding 4) are particular cases of this defect. They keep their own binding grade, so they stay separate items.

### H3. The map's fates arms switch off silently when the fates record is missing (findings 2, 25)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:235`, with line 604 and the hard-coded path at line 45.
- **What is wrong:** The fates record is parsed only under `if FATES.exists()` (line 235), and every fates arm runs only under `if FATE_KITS or FATE_ROWS` (line 604). A missing or renamed record, or changed section tags, leave both empty. Every arm and every kit's `fate=` key then drop out, no finding is raised, and fates never joins the unarmed list. Every other source is read through `text()` or `section()`, which raise or exit, so this is the one source that fails soft.
- **Evidence:** With FATES pointed at a missing path, `--check` printed 'unarmed none' and rc 0, and the map shrank from 31127 to 30890 B because the `fate=` keys were gone.
- **Consequence:** The check certifies "every part has a fate" when it read no fates. A rename is a real path: b3ea11fdc renamed a record in this same build.
- **Fix (skeptic judged both proposals SOUND):** Treat an absent record, or an empty [kits] or [table] block, as a FINDING or as unarmed (rc 2), never as a skip. You can drop the `exists()` guard so that `section()` exits, or register fates as a namespace. Add a `fates-absent` plant (FATES pointed at a nonexistent path, expect a non-zero exit).
- **Left-shift gate:** add to the build's bug-class checklist that every source an instrument reads must fail hard or report unarmed, with an absent-source plant per source.
- The width half of finding 2 is the same defect as M14 (finding 26). Finding 16 is this same defect again and is bound medium at M8. I would grade it high with this item, because its consequence is identical.

## Medium

### M1. dIndexedDesign's research harness rests on dBoundRoles' `experiment` shape (finding 3)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1255`.
- **What is wrong:** The new clause, 'the research harness, built on the `experiment` shape', depends on dBoundRoles (line 1249). dBoundRoles is outside dIndexedDesign's ancestor closure: dDeclaredLoop, dTotalRecall, dWitnessedBar, dOrderedCharter, dFairHearing and dGroundRules. The clause names no not-installed slot and has no [reconciled-order] row. The reconciliation probe passes with 0 findings.
- **Consequence:** dIndexedDesign can land first, and the research harness then has no shape to build on.
- **Fix (skeptic judged it SOUND):** Choose one:
  - add dBoundRoles to dIndexedDesign's After column and re-run `critical_path.py`;
  - move the clause to dBoundRoles;
  - say in the clause that the harness runs as today until the shape lands, and class the row 'tolerance'.
- **Left-shift gate:** H2's widened cites rule.

### M2. The [probe] program rests on parts built later in the chain (finding 4)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:514` ([probe], lines 509-514).
- **What is wrong:** All six [probe] items are dDeclaredLoop's, but they depend on later builds:
  - `probe.return` writes through dTotalRecall's `record`;
  - `probe.design` uses dBoundRoles' `experiment` shape and the `tester` default;
  - `probe.judge`'s computed verdict is dWitnessedBar's probe witness;
  - the role `probe` outcome is dBoundRoles'.

  None of these renders not-installed, and none is classed.
- **Consequence:** When dDeclaredLoop lands, its probe program cannot write its record, cannot judge and has no verifier.
- **Fix (skeptic judged it SOUND):** Declare dDeclaredLoop's degraded behaviour until each part lands. For example, write the probe record as a plain file, and hold the verdict as claimed until dWitnessedBar's witness lands. Add tolerance rows for `record`, `tester` and `experiment` from dDeclaredLoop. Alternatively, move the record write, the witness and the verifier binding to their owning builds' rows.
- **Left-shift gate:** H2's widened cites rule.

### M3. `unrunnable` is outside the probe's closed verdict set (finding 5)

- **Where:** `flow-steps.md:512` (`probe.run`), with lines 513, 514 and 532.
- **What is wrong:** `probe.run` returns the verdict 'unrunnable'. `probe.judge` declares only confirmed, refuted or inconclusive, and measured, within noise or aborted. The Instruction bullet says 'each verdict set closed'. `probe.return` routes only a claimed verdict.
- **Consequence:** A schema-forced probe record refuses this path or needs an undeclared value, and the path has no route.
- **Fix (skeptic judged it SOUND):** Add `unrunnable` to `probe.judge`'s verification set and to the probe schema, and route it in `probe.return`, for example to an owner item. Or map the no-capability path to `inconclusive` with its reason.
- **Left-shift gate:** a check that every verdict an item's Then cell emits is a member of the declared set.

### M4. Fate rows contradict their destinations or each other (finding 6)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:87`, with lines 153 and 195.
- **What is wrong:**
  - Roles' `house/policy.toml` is STAYS 'until dConvergedCharter folds it'. That fold goes into `.governance/policy.toml` (v2:744-749), so the file's end state is MERGED.
  - The `/unattended` Skill is RETIRED at line 153 and RESHAPED inside the 'rendered Skills (7)' row at line 195.
- **Consequence:** dConvergedCharter's new exit check, 'every part in the fates table at its fate', would either red on a correct convergence or be written to ignore these rows.
- **Fix (skeptic judged it SOUND):** Make `house/policy.toml` MERGED: 'into `.governance/policy.toml` (dConvergedCharter); on dGroundRules's legacy list until then'. Make line 195 six reshaped Skills and leave `/unattended` on its own RETIRED row. Add a fates arm that refuses a part named in two rows.
- **Left-shift gate:** that duplicate-part arm, with a plant.

### M5. The tester, or the working roles, get the `code` slot: two copies disagree (finding 7)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:625` ([delivery]).
- **What is wrong:** [delivery] gives the builder and the tester the `code` slot. v2's `memory.code-roles` default (line 934) and night-pass NP-9 (line 504) name the spec writer, builder, researcher, architect, reviewer and prompt writer, with no tester. [delivery] gives the architect, spec writer and reviewer no slot.
- **Consequence:** dBoundRoles' renderer, built from either copy, makes the other read as violated.
- **Fix (skeptic judged it SOUND):** Make one copy the source. Either drop the tester from [delivery] and give the slot to the architect, spec-writer and reviewer rows, or add the tester to working-roles in v2 and in point 3.
- **Left-shift gate:** derive [delivery]'s `code` slot holders from `memory.code-roles` rather than typing them.

### M6. The binding of a driver-hosting owner session is stated two ways (finding 8)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:311` ([terms]), line 1376 ([revised-night]), [act] (lines 503-508), v2 [owed] (line 1350), v2's dWellOiledMachine row (line 1252), night-pass line 92 and NP-1.
- **What is wrong:** [terms] and [revised-night] say the owner's session hosts the driver 'bound as an act session'. An act session is a headless session that lives for one act and decides nothing. [act] says the owner's binding record reads 'owner', not an act and its epoch. The timing also disagrees: v2's dWellOiledMachine row says 'before this build lands', and [owed] keeps the hosting with no end if the spike fails.
- **Consequence:** Whichever binding dWellOiledMachine builds, the other record's rule goes unenforced. This is the gap-rt-22 class the fold was meant to close.
- **Fix (skeptic judged it SOUND):** Use one statement everywhere, for example: 'the owner's session hosts the driver under its "owner" binding, and each role act it hosts is act-bound with that act's epoch'. Put it in [terms], the diagram, [revised-night], v2 [owed] and NP-1, and reconcile the 'before this build lands' timing with [owed]'s conditional.
- **Left-shift gate:** a checklist entry: a renamed binding value is grepped across every record before the fold commits.

### M7. The recut points at a superseded copy of the order's gate (finding 9)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md:176`.
- **What is wrong:** [reconciled-order] still names the audit fold's probe as 'the order's gate'. That copy reds on the committed tree: 'class row with no dependency: dBoundRoles `feature` (dTotalRecall, tolerance)', findings 1. Only the night pass's instruments copy carries the `feature.*` wildcard rule.
- **Consequence:** Whoever re-runs the cited gate sees a red, or deletes a valid row. The gate's single source has forked.
- **Fix (skeptic judged it SOUND):** Point line 176 at the night pass's [instrument] copy and mark the audit fold's copy superseded. Better, keep the gate as one committed script that both records cite.
- **Left-shift gate:** a checklist entry: an instrument lives in one committed file, and records cite it by path.

### M8. The fates record path is hard-coded and fails soft on a re-date (finding 16)

- **Where:** `map.py:235`, with the dated path at line 45.
- **What is wrong:** FATES hard-codes the dated filename, while the atlas resolves the record by name. A re-dated record turns off every fates arm, and `--check` and `--check --plant fates-ghost` both return rc 0. This is the same defect as H3. Its binding grade is medium. I would grade it high, because its consequence is identical to findings 2 and 25.
- **Fix (skeptic judged it SOUND):** Resolve the record as the atlas does (`atlas.SOURCES["fates"]` or `atlas.record("fates")`). If it is absent or parses to zero rows, report a finding or return 2. Add a plant that empties [table] and expects a non-zero exit.
- **Left-shift gate:** H3's absent-source plant.

### M9. Nothing routes `verify-at-plan` or `on-request` (finding 17)

- **Where:** `flow-steps.md:129` (`plan.record`), with flow-steps:78 and v2 lines 846, 1093 and 1254.
- **What is wrong:** v2's dRankedPlan row has `plan.record` declaring the probes owed before Design. The `plan.record` row is unchanged from the base. The only reader of `probe.observations` is `entry.place`, which implements verify-before-place. `verify-at-plan` has no route, and `on-request`, which the velocity preset selects, is only partly covered. Patch and repeat builds never reach Plan.
- **Consequence:** A preset or override that selects those values has no item that runs or witnesses them.
- **Fix (skeptic judged it SOUND):** Amend `plan.record`'s Does and Then cells to route owed probes to `probe.trigger` under `verify-at-plan`. Say what patch and repeat builds do under that value, and how `on-request` reaches [probe]. Or drop any value that has no route.
- **Left-shift gate:** a check that every value of every policy key is read by at least one item's cell.

### M10. `probe.verifier: asking-role` has no actor for placed probes (finding 18)

- **Where:** `flow-steps.md:511`, with v2:848.
- **What is wrong:** `probe.design`'s actor is the role `probe.verifier` names. Probes placed by `probe.points`, by the owner's request or by `probe.observations` have no asking role, which `probe.return` itself acknowledges.
- **Consequence:** A repository that selects `asking-role` cannot run any placed probe.
- **Fix (skeptic judged it SOUND):** Give placed probes a fallback actor under `asking-role`, such as the tester or the item after the boundary, or restrict `asking-role` to raised probes in the key's catalogue row. Record which applies.
- **Left-shift gate:** the per-value route check in M9.

### M11. [sessions] still classes sessions as attended or act (finding 19)

- **Where:** `layer-runtime.md:728`, with lines 722, 744 and 747 and v2:932 (`memory.default-load`).
- **What is wrong:** The binding is now 'owner', attended or not, and unattended is the default. [sessions] still gives the card, the `context.on-full` rule and the primary-tree rule to 'attended' sessions, and v2:932 says the same.
- **Consequence:** A dWellOiledMachine session-start hook keyed on the old classes leaves the default owner session uncovered. That contradicts the row's 'in the owner's session'.
- **Fix (skeptic judged it SOUND):** Re-key [sessions] and v2's `memory.default-load` reason on owner session against act session, and add a [revised-night] note.
- **Left-shift gate:** the rename-grep checklist entry in M6.

### M12. Layer-memory's [reuse] still treats symbols and callers as optional (finding 20)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:698` (line 688 too), and v2:501.
- **What is wrong:** Point 3 made the `code` record core, replacing the optional symbols and callers, and [map] (line 725) was revised to match. [reuse] still says the index holds 'the map's symbols and callers', and 'Without the map, an optional component since KN-1, the index holds the reuse entries alone'. v2's [layers] memory row still lists 'the map' as optional.
- **Consequence:** dTotalRecall's benchmark acceptance and the slot's states could be built against the stale answer.
- **Fix (skeptic judged it SOUND):** Make [reuse]'s index read the core `code` record on every install, with only dossiers and owner views optional. Narrow v2:501 to 'the map's owner views and dossiers'. Add a revision note citing point 3.
- **Left-shift gate:** the rename-grep checklist entry in M6, applied to retired component names.

### M13. Attendance writes into dOrderedCharter's `override` kind (finding 21)

- **Where:** `flow-steps.md:545` (`life.request`), v2's dWellOiledMachine row, `layer-memory.md:398`, ownership:243, and the night-pass ownership amendment (lines 991-992).
- **What is wrong:** Attend and unattend write 'the `override` record, scoped by `attendance.scope`'. The only `override` kind is dOrderedCharter's `charter.override` record. Its schema has no scope or attendance field, and no row names a second writer.
- **Consequence:** dWellOiledMachine either writes rows the registry's check refuses, or silently widens another build's schema. A reader cannot tell which fact a row holds.
- **Fix (skeptic judged it SOUND):** Register a distinct kind, for example `attendance`, owned by dWellOiledMachine with its scope field, and add it to the ownership amendment. Or amend layer-memory's `override` row to declare both writers and the scope field, with a homonym or tolerance class row in the re-cut.
- **Left-shift gate:** a check that every record a flow item writes names a registered kind whose owner is that item's build or a declared co-writer.

### M14. The fates parser drops wrong-width rows silently (finding 26; finder graded high, skeptic re-graded medium)

- **Where:** `map.py:241`.
- **What is wrong:** A row is kept only if `len(c) == width`. A wrong-width row, and its fate, vanish without a word, and nothing compares the parsed count with the stated 131 rows.
- **Evidence:** One widened row with an out-of-set fate gave rc 0 and FATE_ROWS 130. `atlas.tables()` exits on exactly this mismatch. Nothing is dropped today.
- **Fix (skeptic judged it SOUND):** Parse with `atlas.table(section(body, tag), 'Kit', ...)`, and check `len(FATE_ROWS)` and the per-fate counts against the lead-in: 28 stay, 69 reshaped, 20 merged and 14 retired, over 131 rows. Add a plant that widens one row of a multi-row kit and expects rc 1.
- **Left-shift gate:** that population-count arm and plant.

### M15. Two fates arms are never seen red, and `fate=` is never checked (finding 27)

- **Where:** `map.py:623` and line 630, with plants at lines 606-619.
- **What is wrong:** No plant reaches 'kit.X has no [kits] row' or '[kits] names X, which is no kit node'. No arm compares each kit line's rendered `fate=` with [kits]. Yet night-pass [instrument] (line 529) says 'six fates arms each red on their plant', and the code has eight arms.
- **Consequence:** An inverted condition in either arm, or a wrong `fate=`, would pass unnoticed.
- **Fix (skeptic judged it SOUND):** Add a `fates-kit-drop` plant (delete one `kits_` entry) and a `fates-kit-ghost` plant (`kits_['ghostkit'] = 'kept'`). Add a `fate=`-against-FATE_KITS arm with a plant that rewrites one value. Correct the [instrument] count to the arms actually seen red.
- **Left-shift gate:** a meta-check that every FINDING string in the check function is produced by at least one plant.

### M16. The fix pass's check-keeping clause names no witness (finding 29)

- **Where:** `architecture-v2.md:1253` (dWitnessedBar row), and flow-steps lines 309-311 and 228.
- **What is wrong:** The clause 'a fix pass that keeps its check' owns gap-test-19 (HIGH). Unlike its sibling clauses, it names no arm and no seen-red case. It also does not say whether the fix pass after a failed `build.acceptance` excludes the acceptance commands' files.
- **Consequence:** gap-test-19 can be closed by an allowance that is never shown refusing anything.
- **Fix (skeptic judged it SOUND):** Extend the clause: 'its arm seen red on a planted fix pass that writes the red leg's test file and is refused'. State whether `build.acceptance`'s fix pass excludes the acceptance commands' files.
- **Left-shift gate:** a check that every chain clause owning a HIGH gap names a seen-red case.

## Low

### L1. The [delivery] 'unit workers' row is split across two lines (findings 10, 24)

- **Where:** `project-map.md:625-627`.
- **What is wrong:** The row ends mid-cell at 'the builder and', and the next line begins 'the tester get…'.
- **Consequence:** GFM, or any line-based reader, truncates the row and shows a phantom row whose Reader cell is a sentence fragment.
- **Fix (skeptic judged it SOUND):** Join the lines into one row.
- **Left-shift gate:** the night pass's table-width probe, run over every record's tables. Each [delivery] row must have exactly two cells.

### L2. The project map's `code` slot states lack 'not installed' (finding 11)

- **Where:** `project-map.md:547`.
- **What is wrong:** The slot lists three states: filled, derived with nothing related, and not extracted for a language. v2's dBoundRoles row and the re-cut's tolerance rows rely on a fourth, 'not installed'.
- **Fix (skeptic judged it SOUND):** Add 'not installed, until dTotalRecall's `code` record lands'.
- **Left-shift gate:** a check that each tolerance row's slot state appears in the slot's declared state list.

### L3. Fates [check] claims a stronger RETIRED arm than the code runs, and a STAYS part sits in an absorbed kit (findings 12, 22, 30)

- **Where:** `fates.md:237` (the claim, around lines 229-237), `map.py` line 638 (the arm), and `fates.md:145`.
- **What is wrong:**
  - [check] says 'every RETIRED row names its replacement, or says "none" and why'. The arm only tests that the cell is non-empty, and the `fates-empty` plant proves only that. A bare 'none', or a nonexistent build, passes.
  - No arm compares a part's fate with its kit's fate. unattended is absorbed ('its directory goes'), yet its `stall-recorder.js` row is STAYS.
- **Consequence:** The record overstates its check. A part that cannot survive its dissolved directory reads green.
- **Fix:** The skeptic judged finding 12's fix SOUND. Finding 22's fix and finding 30's fix were judged UNSOUND. The skeptic's corrected fix:
  - Reword the [check] bullet to 'every RETIRED row's "Where it goes" is non-empty'.
  - Under what the check does not do, add that it checks neither the replacement's quality nor that a RETIRED row names a replacement or a reason, and that it does not check kit-to-part fate coherence.
  - If the arm is tightened instead, accept a cell that starts with 'none:' followed by text, or other non-empty text, and plant a bare 'none' that must red.
  - Optionally add an arm that reds a STAYS row under an absorbed kit, with a plant.
  - Re-fate `stall-recorder.js` as RESHAPED into the supervisor's limit signal (dWellOiledMachine).
- **Left-shift gate:** the STAYS-under-absorbed arm and its plant.

### L4. Point 8's fold leaves stale or inconsistent text in the fates record (finding 13)

- **Where:** `fates.md:159`, lines 163 and 186, `layer-instruction.md:240`, and night-pass lines 425 and 429.
- **What is wrong:**
  - The branch-reconcile row cites '(section 5)', which does not exist in this record.
  - The map still renders branch-reconcile with `layer=runtime`.
  - 'UNDECIDED' and 'undecided' remain, against 'None is left undecided'.
  - The night pass says 11 parts were proposed, but 17 rows are marked NP-22.
- **Fix (skeptic judged it SOUND):**
  - Rewrite row 159 to 'observability's prune fix (dTendedCadence; [stale] 9)'.
  - Update layer-instruction's row, or note in [stale] 9 that the kit stays Runtime's.
  - Resolve the two undecided cells or mark them pending under NP-22.
  - Restate the count as '11 of dispatch 104's rows, split into 17 parts'.
- **Left-shift gate:** a check that a record's section references resolve to its own section tags.

### L5. A stale 'attended binding' survives the rename (finding 14)

- **Where:** `layer-runtime.md:512`.
- **What is wrong:** The line reads 'a bound act of the attended binding', after the value was renamed to 'owner' at line 508.
- **Fix (skeptic judged it SOUND):** Replace it with 'the owner binding'. Check flow-steps line 773; it is a dated revision row and stays as written.
- **Left-shift gate:** the rename-grep checklist entry in M6.

### L6. The kit layer arm reads rendered lines and goes quiet if the kit namespace folds (finding 28; finder graded medium, skeptic re-graded low)

- **Where:** `map.py:644`, lines 641-644, with the plant at line 549.
- **What is wrong:** The arm scans the rendered `- kit.` lines. If `fit()` folds the kit namespace, the arm checks nothing and passes, and the no-layer plant raises StopIteration. The fold is distant: eight namespaces fold first, and the header prints the fold.
- **Fix:** The finder's fix was judged UNSOUND. The skeptic's corrected fix:
  - Check each node in `ns['kit']` for a non-empty 'layer' rel unless its key is in NO_LAYER.
  - Rework the no-layer plant to empty one kit node's layer rel in `ns`, not to edit a rendered line.
  - Say in the record that the arm does not check that a layer is correct.
- **Left-shift gate:** a checklist entry: arms read the derived graph, never the rendered text.

### L7. The recorded map size was taken on a dirty tree (finding 31)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:182`, v2:1354, and night-pass lines 210 and 527.
- **What is wrong:** All four places record 31,133 B. On the clean committed tree, `--check` prints 31,127 B. The 6 B difference is the head line's ' dirty' marker.
- **Fix:** The finder's fix was judged UNSOUND. The skeptic's corrected fix: record 31,127 B in all four places, or measure the byte size with the head line's ' dirty' marker excluded and say so in the instrument's docstring.
- **Left-shift gate:** the same marker exclusion, so a recorded figure reproduces on any tree.

review-shape kind=diff-review round=1 intensity=light at=synth raw=31 confirmed=30 refuted=1 unverified=0 blocker=0 high=4 medium=16 low=10 agents=9 out-tokens=167605

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:585 | high | high | confirmed | In flow-steps, entry.place (line 78) routes 'repeat → entry.claim, then Design as a playbook run', and entry.claim (line 81) sends 'Design on patch or repeat'. The [transitions] table (lines 575-590) has none→designing only for the `patch` disposition, and line 579 says 'the engine refuses any transition the table lacks'. [design]'s six Enters inputs (161-167) and design.input's Then cell (172) have no playbook-run input. v2's P20 (line 586-587) was amended in this diff and still says only 'in-goal amendments and patch builds at Design'. The diff introduced `repeat`, so the defect is in scope. It will mislead the dDeclaredLoop builder who builds the table. | sound | - |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:235 | high | high | confirmed | map.py line 235 reads `if FATES.exists():`. Line 241 keeps a row only when `len(c) == width` (3 or 6), and drops every other row without a finding. Line 604 runs every fates arm only `if FATE_KITS or FATE_ROWS`. A missing or renamed fates file, or changed section tags, leave both empty: all fates arms are skipped, no finding is added, and the unarmed list (lines 448-467) never names fates, so the check exits 0. The docstring's plant list has no plant for a missing file or a bad row width, and the docstring does not say what the arms skip. All of this was added in this diff. I judged this from the source and did not run the check. | sound | fixture-passes-by-finding-nothing |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1255 | medium | medium | confirmed | v2 line 1255: dIndexedDesign's After column is 'dDeclaredLoop, dTotalRecall'. Its ancestor closure is dDeclaredLoop, dOrderedCharter, dFairHearing, dGroundRules, dTotalRecall and dWitnessedBar, and dBoundRoles is not in it. The row now says 'the research harness, built on the `experiment` shape (night pass, point 2)'. The base row said only 'the research harness'. dBoundRoles (line 1249) registers the `experiment` shape kind. The re-cut's three new [reconciled-order] rows cover only `feature` and `code`, and the clause names no 'not installed' slot. This contradicts the night pass's 'every new dependency ... slotted or classed'. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:514 | medium | medium | confirmed | In flow-steps [probe] (lines 509-514), all six items are owned by dDeclaredLoop, and the ownership amendment (line 989) confirms it. probe.return is 'through `record`', and v2 line 1250 gives the one `record` write to dTotalRecall. probe.design uses dBoundRoles' `experiment` shape (flow-steps line 519 says so). probe.verifier defaults to tester, a dBoundRoles role. The probe witness, the executor's re-run, is in dWitnessedBar's row (v2 line 1253). All three builds are descendants of dDeclaredLoop. None of these items says 'not installed', and the re-cut adds no class row for them. So night-pass line 482's claim that every new later-build dependency is slotted or classed is false. The diff introduced the [probe] program. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:512 | medium | medium | confirmed | flow-steps line 512, probe.run: 'no capability for the method → `probe.return`, the verdict unrunnable'. Line 513, probe.judge, declares only 'confirmed, refuted or inconclusive; an experiment measured, within noise or aborted'. Line 532 says 'each verdict set closed'. Line 514, probe.return, routes only 'a claimed verdict' to an owner item. So `unrunnable` is outside the closed set and has no declared route. All of this text is new in the diff. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:87 | medium | medium | confirmed | fates line 87 gives roles' `house/policy.toml` the fate STAYS, 'until dConvergedCharter folds it'. v2 lines 744-749 say dConvergedCharter folds `tools/roles/house/policy.toml`'s [effort] and [gates] into `.governance/policy.toml`, so its end state is a merge. Line 153 makes the `/unattended` Skill RETIRED. Line 195 holds 'rendered Skills (7)' RESHAPED with 'build and unattended become clients of `next` and `run`', so one part has two fates. dConvergedCharter's new exit check (v2 line 1260) is 'every part in the fates table at its fate, the table's join', and these rows would make it contradict itself. The fates record is new in this diff. | sound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:625 | medium | medium | confirmed | project-map [delivery], amended in this diff: 'since the night pass the builder and the tester get their write set's `code` slot'. v2 line 934, the `memory.code-roles` default working-roles, says 'the spec writer, builder, researcher, architect and reviewer, and the prompt writer through its actor'. That list has no tester. Night-pass NP-9 (line 504) gives the same list. The delivery table's architect, spec-writer and reviewer rows get only the map and no `code` slot. So the two copies disagree on who receives the slot. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:311 | medium | medium | confirmed | The night pass added this text. layer-runtime.md line 311 ([terms]) and line 1376 ([revised-night]) say the owner's session hosts the driver 'bound as an act session'. The same record's [terms] defines an act session as a headless `claude -p` session that lives for one act and 'decides nothing'. [act] (lines 503-508) says the owner's session's binding record reads 'owner' rather than an act and its epoch, and that it is 'bound the same way for every role act it hosts'. So the binding of a driver-hosting owner session is stated two ways, and 'Act binding requires that record' leaves open where the epoch comes from. The timing also disagrees. v2's dWellOiledMachine row (line 1252) limits the hosting to 'before this build lands'. v2 [owed] (line 1350) says that if the spike fails, the owner's session 'keeps hosting the driver', with no end. The same wording appears in night-pass line 92 and NP-1. | sound | - |
| 9 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md:176 | medium | medium | confirmed | recut.md lines 174-177 still call the audit fold's [instrument] probe 'the order's gate'. The night pass added the dBoundRoles `feature` tolerance row (diff hunk at line 191) but left that pointer unchanged. I extracted the audit fold's hardened probe (audit-fold.md lines 454-669) and ran it on the committed recut record. It printed 'class row with no dependency: dBoundRoles `feature` (dTotalRecall, tolerance)' and 'findings 1'. Only the night-pass-instruments copy of `reconcile_probe.py` (line 1088 on, with the wildcard rule at line 1180) reads `feature.*`. | sound | - |
| 10 | correctness | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:625 | low | low | confirmed | In project-map.md, line 625 ends 'since the night pass the builder and' with no closing pipe. Line 626 begins 'the tester get their write set's `code` slot ...' with no leading pipe. The row is split across two physical lines, so a Markdown table ends at line 625 and the rest of the cell drops out of the row. The night pass made this edit. | sound | - |
| 11 | correctness | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:547 | low | low | confirmed | project-map.md line 547, revised by the night pass, gives the code slot exactly three states: filled, derived with nothing related, or not extracted for a language. The record covers the pre-landing state for the map slot ('Until the renderer lands, the slot renders "not installed"', line 635), but not for the code slot. The re-cut's dBoundRoles `code` tolerance row and v2's dBoundRoles row rely on a 'not installed' state for the code slot. The effect is contained to the record's text: an incomplete state list. | sound | - |
| 12 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:237 | low | low | confirmed | fates.md line 235 claims 'every RETIRED row names its replacement, or says "none" and why'. In map.py the RETIRED arm is only `elif r[3] == "RETIRED" and not r[4].strip()`, a non-empty test. The fates-empty plant blanks the cell, which proves only that arm. A bare 'none', or a build name that does not exist, passes. The record therefore describes a stronger check than the one that runs. | sound | - |
| 13 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:159 | low | low | confirmed | The fates record is new in this diff. Its row at line 159 cites '(section 5)', but its sections are [words], [inventories], [kits], [table], [stale] and [check], so there is no section 5. [stale] item 9 says observability's prune fix stands. layer-instruction.md line 240 still gives branch-reconcile the Runtime layer, and the map generator renders that layer since this diff. Line 163 has 'JSON-or-packs UNDECIDED' and line 186 'undecided', while night-pass line 425 says 'None is left undecided'. Night-pass line 429 says 11 parts were proposed, but 17 table rows carry 'proposed by the night pass (NP-22)'. | sound | - |
| 14 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:512 | low | low | confirmed | At the base, the binding record's value was "attended" (base line 507). The night pass renamed it to "owner" (current line 508) but left line 512 reading 'a bound act of the attended binding'. That binding value no longer exists, so the diff made the line stale. flow-steps line 773 is a row in a dated revision table and should stay as written. The fix says to check exactly that. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:482 | high | high | confirmed | I checked the v2 [chain] parents. dDeclaredLoop's parents are dOrderedCharter and dFairHearing. dWitnessedBar's parent is dDeclaredLoop. dIndexedDesign's parents are dDeclaredLoop and dTotalRecall, and dTotalRecall's are dDeclaredLoop and dWitnessedBar. So dIndexedDesign is an ancestor of neither dDeclaredLoop nor dWitnessedBar, dBoundRoles is an ancestor of neither dDeclaredLoop nor dIndexedDesign, and dWellOiledMachine is not an ancestor of dDeclaredLoop. Five new clauses depend on those builds. (1) The dDeclaredLoop row says 'the `repeat` disposition ... routing a request onto a playbook', and flow-steps:78 routes repeat to 'Design as a playbook run, its playbook supplying the feature design'. The playbook record kind is a new dIndexedDesign clause. (2) dWitnessedBar has 'the playbook set record and its set check at Test'. (3) flow-steps:511 makes `probe.design`'s actor 'the role `probe.verifier` names', and that key defaults to tester (v2:848). The tester is dBoundRoles' 'tester agent, absent today'. The experiment shape is 'dBoundRoles' `experiment` kind' (flow-steps [probe]). (4) dIndexedDesign's research harness is 'built on the `experiment` shape'. (5) dDeclaredLoop's attendance rule 'turns the `step —` announcement on', and that announcement is a dWellOiledMachine clause. The re-cut's [reconciled-order] gained only three night-pass rows (feature and code from dBoundRoles, code from dOrderedCharter). None of these five has a class row, and none renders 'not installed' in flow-steps. So night-pass:482's 'No edge changed. Every new dependency on a later build either waits in a slot that renders "not installed", or is classed' is false. It will mislead the chain builds. | sound | amendment-leaves-its-other-half-standing |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:235 | medium | medium | confirmed | map.py:45 hardcodes FATES = HERE / '2026-10-18-build-PLAY-dClosedLoop-1-fates.md'. Line 235 reads it only under `if FATES.exists():`, and every fates arm and plant at line 604 sits under `if FATE_KITS or FATE_ROWS:`. If the file is missing or renamed, both dicts stay empty, the arms are skipped and no finding is raised. The unarmed exit 2 (lines 708-710) covers only namespaces with no extractor, so it never fires here. The atlas resolves the same record by name through src['fates'] (atlas.py:42 and 447), so the two instruments diverge on a re-date. The plants would then pass green. All of this was added by this diff. | sound | guard-above-a-fold-makes-its-fallback-dead |
| 17 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:129 | medium | medium | confirmed | v2's dRankedPlan row (line 1254) adds '`plan.record` declaring the probes owed before Design (night pass, point 2)'. flow-steps:129's `plan.record` row is the same as at the base (base line 119): drafted, research or owner question, with no probe route. The only reader of `probe.observations` is entry.place (flow-steps:78), 'an observation the request claims → `probe.trigger` first'. That is the verify-before-place behaviour. So verify-at-plan (v2:846), and on-request, which the preset row at v2:1093 selects, have no item that implements them as stated. probe.trigger's 'the owner's request' trigger partly covers on-request, but verify-at-plan has no route at all. | sound | - |
| 18 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:511 | medium | medium | confirmed | flow-steps:511 gives `probe.design`'s actor as 'the role `probe.verifier` names', and v2:848 offers 'tester, asking-role, researcher'. probe.trigger (line 509) opens probes from four sources: a `probe.points` boundary, the owner's request, an observation and a role's `probe` outcome. Only the last has an asking role. probe.return (line 514) itself separates 'the asking item' from 'the item after the boundary', which confirms that placed probes have no asker. Nothing names a fallback actor or refuses asking-role for placed probes. The default is pending NP-5, but the value is offered and has no actor for most triggers. | sound | policy-value-with-no-route |
| 19 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:728 | medium | medium | confirmed | The diff renamed the binding 'attended' to '"owner", the session the owner types in, attended or not'. It also made the supervisor the driver in every mode. layer-runtime [sessions] (lines 722, 728, 744, 747) still classes sessions as attended or act: 'Attended sessions also get the card', 'An attended session starts fresh', 'attended sessions follow `context.on-full`'. v2:932's `memory.default-load` reason still says 'an attended session opens with the card and the map'. Attendance is now a mode and unattended is the default, so the default owner session falls outside these rules. The text was consistent at the base, so this diff made it stale. It also disagrees with dWellOiledMachine's new 'in the owner's session' clause. | sound | amendment-leaves-its-other-half-standing |
| 20 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:698 | medium | medium | confirmed | night-pass [p3-code] says the core `code` record 'replaces the optional symbols and callers'. Layer-memory [map] (line 725) was revised to match: 'one core record kind, `code`, no longer an optional component'. But [reuse] still lists 'the map's symbols and callers' in the house index (line 688). It still says 'Without the map, an optional component since KN-1, the index holds the reuse entries alone, and the slot says so' (lines 697-698). Under point 3 that state no longer arises for symbols and callers, so the reuse slot's states now contradict [map]. v2:501's memory row still names 'the map' among the optional components without narrowing it to owner views and dossiers. | sound | amendment-leaves-its-other-half-standing |
| 21 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:545 | medium | medium | confirmed | flow-steps:545 (life.request) and v2's dWellOiledMachine row say attend and unattend each write 'an `override` record scoped by `attendance.scope`'. The only registered `override` kind is layer-memory:398, 'override \| dOrderedCharter \| `charter.override` and its record, under the precedence and override rule'. The ownership record lists only `charter.override` under dOrderedCharter (ownership:243), and the night-pass ownership amendment (lines 991-992) assigns keys but no record kind for attendance. No row gives the kind a second writer or a scope field. So dWellOiledMachine writes into another build's record kind, whose schema does not hold the attendance facts. | sound | - |
| 22 | seams | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:639 | low | low | confirmed | map.py:639 only tests `not r[4].strip()`, so any non-empty text passes. Fates [check] (line 229 on) still claims 'every RETIRED row names its replacement, or says "none" and why', and its 'does not do' list leaves out both this gap and the kit-to-part check. The STAYS row is a real contradiction too. Fates line 33 defines absorbed as 'its directory goes, and its functions move into other kits', and unattended is absorbed (line 55), yet `stall-recorder.js` at line 145 reads STAYS. No arm compares a part's fate with its kit's fate. All of this is new in this diff. Its effect stays inside a design record, so low. | unsound | - |
| 23 | seams | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:43 | low | - | refuted | The accumulators really are never cleared: NO_LAYER, FATE_KITS and FATE_ROWS fill at lines 212, 243 and 245, and only DECLARED is cleared at line 106. But derive() runs once per process. Its only call site is main() at line 666, and the atlas's own derive() is a different function. The plants change copies (`rows_`, `kits_`) inside check() and never call derive() again. No reachable path reads stale state, and the finder grants there is no wrong result today. It is a latent hazard, not a reachable defect. | sound | - |
| 24 | seams | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:626 | low | low | confirmed | project-map.md line 626 ends with 'since the night pass the builder and', and line 627 begins 'the tester get their write set's `code` slot (point 3). A `gov map` call ... \|'. In GFM a line holding a pipe continues the table, so it renders as a phantom row with that text as its Reader cell. At base this row was a single line (base line 625), so this diff introduced the split. The defect is in rendering only. | sound | - |
| 25 | verification | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:235 | high | high | confirmed | Line 235 parses the fates record only under `if FATES.exists()`, and the arms at line 604 run only under `if FATE_KITS or FATE_ROWS`. Without the file, no finding is added and nothing joins `unarmed`, so main() returns 0 with 'unarmed none'. Every other source is read through text() or section(), which raise or exit, so this is the one source that fails soft. FATES is a hard-coded dated path (line 45). A rename of a record in this build happened one commit earlier (b3ea11fdc), and after a rename the map would certify fates coverage it never ran. That path is narrow, so high. | sound | zero-witness-over-an-unnamed-population |
| 26 | verification | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:241 | high | medium | confirmed | Line 241 keeps a row only when `len(c) == width`, and nothing compares the parsed count with the stated '131 rows'. A malformed row of a kit that has other rows is dropped without a word, and so is its fate. atlas.tables() (atlas.py:149-150) exits on exactly this mismatch. Today every [table] row has 6 cells (131 data rows) and every [kits] row has 3, so nothing is dropped now. The gap opens on the next edit and loses only that row's checks, so the effect is contained: medium, not high. | sound | parser-drops-rows-it-cannot-place |
| 27 | verification | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:623 | medium | medium | confirmed | Lines 606-619 hold six plants. fates-drop removes one kit's [table] rows, which reds only 'has no [table] row'. fates-kit sets a fate to 'maybe', which reds only 'outside the set'. No plant removes a kits_ entry or adds a ghost to kits_, so lines 623 and 630 are never seen red. No arm compares a kit line's rendered fate= with [kits]. Yet fates [check] says 'Each arm is seen red on a planted case', and night-pass [instrument] line 529 says 'six fates arms each red on their plant', with eight arms in the code. | sound | - |
| 28 | verification | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:644 | medium | low | confirmed | The layer arm (lines 641-644) scans rendered `- kit.` lines. kit is a 'line' namespace (line 418), and fit() can fold it, after which the arm reads zero lines and passes. The no-layer plant's next() at line 549 would then raise StopIteration. The path is far off, though. fit() first degrades purposes from 60 to 40, then folds round, gap-area, policy-namespace, tag-namespace, record-kind, hook, point and live-build before kit. That takes growth well beyond the 1.6 KB of headroom, and the header prints 'degraded: ... fold kit' when it happens. Real, but distant and partly visible, so low. | unsound | zero-witness-over-an-unnamed-population |
| 29 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1253 | medium | medium | confirmed | v2 line 1253 (dWitnessedBar row), which this diff adds, reads only 'a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wrong-spec judgment to Design as a new unit (night pass, point 6)'. It names no arm and no seen-red case. The sibling clauses the same diff adds do name one: the attendance rule has 'its arm seen red on a planted value that swaps an actor', and the tag bundle has 'its type-registered and target-resolves checks each seen red'. flow-steps lines 309-311 restate it with no witness either. The gap is real. flow-steps line 228 routes a failed `build.acceptance` to 'a fix pass', and neither text says whether the exclusion covers the acceptance commands' files. That leaves gap-test-19 (HIGH, gap-register line 279) closable by an allowance that is never shown refusing anything. The effect stays inside the design record, so medium. | sound | - |
| 30 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:237 | low | low | confirmed | fates.md line 237 states 'every RETIRED row names its replacement, or says "none" and why'. The arm in map.py (line 638, not 639) is `elif r[3] == "RETIRED" and not r[4].strip()`, which only checks that the cell is non-empty. The only plant, `fates-empty`, blanks the cell. A bare 'none', or text that names no replacement, passes. So the record states a stronger check than the instrument runs. It is low because every committed RETIRED row does carry a reason. | unsound | - |
| 31 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:182 | low | low | confirmed | I ran `map.py --check` on the clean committed tree (HEAD 9ab7a5c5c, empty porcelain). It prints '2232 nodes in 30 namespaces; 31127 B of 32768'. The records say 31,133 B. render() (map.py lines 446-462) appends ' dirty' (6 B) to the head line whenever the porcelain under memory/, tools/ or .claude/ is non-empty, which is always true before a commit, so the recorded figure was taken on a dirty tree. The 31,133 figure appears in four places, not three: gap-register line 182, v2 line 1354, night-pass line 210 and night-pass line 527. The 6 B difference doesn't change any headroom conclusion, so low. | unsound | two-answers-to-one-question |

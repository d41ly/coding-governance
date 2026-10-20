# Skeptic return: run B, batch 1

**Serves:** research PLAY-dClosedLoop-1

Dispatch 179's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-20-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- B1-F3: confirmed high
  Observed at architecture-v2 [enforcement] `P23`: v2:1707 is the only place `cl-dClosedLoop-0093` appears in the copy. My parse of [chain] finds 495 clause ids, and 0093 is the one gap in 0001 to 0496. dDeclaredLoop's row goes from 0092 straight to 0094, and [clause-ids] says "Retired: none". 0092 only prints "each claim's key and verdict", so no clause enforces P23 (c5).
- B4-F1: confirmed high
  Same observation as B1-F3, at architecture-v2 [enforcement] `cl-dClosedLoop-0093`: there is a ghost id and no other clause enforces P23. This is a twin of B1-F3.
- B2-F11: confirmed medium
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0002`: the clause reds "two specs carrying one clause whole and disagreeing" but never says what they disagree on. carries.py:215 and the report at :251 red any second whole carrier. research-final-coverage:123 maps the case to "carried whole by 2 specs". A writer working from the clause alone can build the looser test.
- B2-F10: confirmed medium (graded down from high)
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0003`: "a chain build's spec in progress" does not name a status. TEMPLATE-SPEC:63 defines `INPROGRESS` as "approved, build underway". Read that way, the refusal applies only after the Design exit, which matches carries.py, where the uncarried arm runs only under `--exit`, and nothing blocks the first spec. The c1 blocking outcome follows only if a writer reads "in progress" as "being drafted", which the wording allows.
- B2-F16: confirmed medium
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0400`: "built specs frozen" has no check and no seen-red, and no freeze check appears anywhere in v2 or flow-steps. `cl-dClosedLoop-0004`'s population covers "each spec revision after its unit's first attributed pass commit", which includes a landed unit's spec. `cl-dClosedLoop-0412` passes that revision once it has a record. final-questions:188 says that after landing a change is a new unit, but nothing enforces it.
- B2-F13: refuted
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0049` (dOrderedCharter, an ancestor of dScopedBuild): the move is already owned there. 0049 moves "`compute_coverage` ... to `tools/lib` ... with `map_lib.resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions` beside it", re-points the consumers in the same unit and keeps a re-export. 0407 describes the state after that move. The walker's grep (`tools/codebase-map/map_lib.py:1373`) shows today's tree, not the design.
- B3-F6: confirmed medium
  Observed at architecture-v2 [chain] dWitnessedBar row, `cl-dClosedLoop-0339` to `0368`: no clause builds the verdict-backend registry, the `remote-ci` read, or `verdict.remote.trust`, `.pin-scope` or `.pin` (catalogue v2:1151-1153, all owned by dWitnessedBar). No other chain row builds them either. The row still lists gap-test-02. layer-expansions:179 assigns `remote-ci` to integrations, but no integrations clause (0425, 0429, 0432) builds it. `cl-dClosedLoop-0014`'s no-reader arm would also red those three keys once dWitnessedBar lands.
- B1-F12: refuted
  Observed at architecture-v2's 2026-10-17 revision note (v2:401): the note is a dated history entry. The 2026-10-18 note at v2:504-506 explicitly moves "the entry items" to dPlacedRequest. Ownership is a field on the node (PM-8, v2:395), and flow-steps' Owner column names dPlacedRequest for every entry item except `entry.intake`. A spec writer reading the owner field sees one owner.
- B2-F12: confirmed low
  Observed at architecture-v2 [clause-ids]: the section says only "its text's hash being its revision". The normalisation (SHA-256, first 8 hex digits, id removed, whitespace folded) is defined only in carries.py:13 and :78-80, and neither v2 nor final-questions cites carries.py.
- B4-F14: confirmed medium
  Observed at architecture-v2 [enforcement] `P29`: the row names only 0178, which covers the first two of P29's rules (handed and keyed; fresh at act launch). The verifier-context, answered-calls and false-facts rules are carried by `cl-dClosedLoop-0196`, `0197` and `0198`, which are not in the row.
- B2-F14: confirmed low (graded down from medium; not c5)
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0390`: "(proposed)" is the only such marker in v2 and is stale, since flow:391 records FL-B4 answered as "Additive stays unit-level". The classifier is already carried in the same clause: "two-level re-entry by `design.reentry`", and flow-steps:182 makes `design.reentry` a dIndexedDesign command that "classifies an amendment by a structural diff". This is a wording defect.
- B2-F15: refuted
  Observed at architecture-v2 [enforcement] `P18`: 0390 carries "fork resolution by `design.forks`", whose default value `agents-feature-rich-expandable` (v2:1019) is the ranking rule. The charter renders the same rule at level 0 ([front-door] v2:973). 0176 and the fork record (flow-steps:203, layer-memory:645) carry "with a full record". Ranking options is the resolver's judgement, and a ranked-list field is an addition the fix proposes, not a gap in the clauses.
- B2-F4: refuted
  Observed at architecture-v2 [chain] `cl-dClosedLoop-0115`: the clause fixes a single freeze ("the base alone before that freeze"), keys the budget "to the build so units a loop mints cannot reset it", and requires it "seen red on a planted loop that mints a new unit each lap". An implementation that added a share per minted unit would fail that red case. 0440 also puts patch builds on the originating build's one budget.
- B1-F10: confirmed medium
  Observed at architecture-v2 [policies] `plan.triage` and `plan.authority`: `owner-batches` and `owner-orders` (strict's values, v2:1469 and v2:1471) appear in no item. `plan.triage-rule` is a command and `plan.triage-judge` is the planner (flow-steps:132-133), so neither value switches anything. One part is weaker: `plan.kickoff` is read by `cl-dClosedLoop-0375`, and `planner-drafts-owner-ratifies` does not contradict `plan.ratification: request`. I could not check the Stage 0 lead list.
- B5-F15: confirmed medium
  Observed at flow-steps [adopt]: the table has five rows and none is `adopt.instructions` (`cl-dClosedLoop-0260`) or `adopt.declarations` (`cl-dClosedLoop-0438`), although adopter-instructions:183 and flow-roles-adoption:323 add both to the `adopt` program.
- B5-F8: confirmed medium
  Observed at flow-steps [adopt] `adopt.decisions` (flow-steps:614): the actor names two kinds, against P24's one actor. The routes are only "accepted" and "declined by the owner". No route covers raters who disagree, or the 0.8 kappa bar that `cl-dClosedLoop-0238` sets. research-retrofit-a:185's "kappa < 0.8 → rubric revised" was not carried forward.
- B5-F9: refuted
  Observed at flow-steps [build] `build.unit-pass` (flow-steps:235) and v2 `cl-dClosedLoop-0406`: retrofit:454-455 defines on-touch reconstruction as "a first-touch dossier". `build.unit-pass` carries "where the map is installed the claiming dossier's edit", and 0406 (dScopedBuild) carries "claiming the baselined map keys its write set holds (dossiers)". The duty has a clause and an item. The walker's search missed it because the clause uses other words.
- B4-F13: refuted
  Observed at flow-steps [entry] `entry.place` (flow-steps:83): a late owner answer is a prompt in an owner-bound session, so `entry.intake` records it and `entry.place` disposes of it from its closed set. "amend → Design re-entry, or an `intake` message to the session holding the build" is the route back. P22 also says every request gets a recorded disposition, so the answer is recorded and routed.
- B4-F12: confirmed low
  Observed at flow-steps [breakpoint] `review.cost` (flow-steps:490): the item is dDeclaredLoop's (`cl-dClosedLoop-0105`), but it writes into the shape-run kind, which is dTotalRecall's (`cl-dClosedLoop-0222`), and its `shape` comes from the shapes registry that dBoundRoles builds (v2:1837). No stand-in is declared. Today's `renderShapeLine` (tools/workflows/tier2-review.js:78) has neither field.
- `test.verdict` S7: holds
  Today's runner already provides the attribution classes (`GATE_ATTRIBUTE`, OWN to DEAD PROBE in tools/run-gates/run-gates.sh:19-21). The default backend `local-hook` is today's pre-push hook.
- `test.flakes` S1: defect

### BS1-F1 — `verdict.flakes` declares one threshold, which `test.select` reads as the release streak and `test.flakes` as the quarantine entry
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** v2:1146 `verdict.flakes`: "a threshold", with the note "the threshold three consecutive greens unless set". `test.select` (flow-steps:294) releases a held leg after "`verdict.flakes`' threshold of consecutive greens". `test.flakes` (flow-steps:298) holds "a leg past the threshold `verdict.flakes` declares", while "a leg below it goes as under `record`". `cl-dClosedLoop-0346` says only "flake quarantine". stall-and-loop:222 says the quarantine "threshold gets a default", and the only default declared anywhere is the release streak.
- **Consequence:** Under the default `quarantine` in S1, nothing says how many flakes put a leg past the entry threshold. A spec writer either reuses the green-streak count, which measures something else, or invents an entry count. Whether a flaky leg blocks the attended build is left undefined.
- **Fix:** Split the key into an entry threshold (flakes per window, with a default) and the release streak (three consecutive greens), each with its own seen-red on 0346.

- `plan.triage-judge` S7: holds
  dRankedPlan follows dBoundRoles, which builds the planner. Chain builds before it are placed by the chain itself, and today's tools stand in.
- `deploy.mandate` S6: holds
  None of S6's injected failures falls at `deploy.mandate`. A failed check falls to the default failure route of `cl-dClosedLoop-0099`.
- `build.scope` S3: holds
  The touch join runs over the unit's own commits. A refused stray's revert pass draws on the originating build's budget, and `flow.on-exhausted` ends the build when that budget is spent.
- `life.unlease` S7: holds
  Before dWellOiledMachine lands, unattended's `--abort` stands in. Leases from dPlacedRequest that nothing renews expire under `leases.expiry-hours`.
- `release.route` S2: defect

### BS1-F2 — The release program's promotion lease is no lease the grammar declares, and its rollback is not fenced
- **Address:** layer-expansions `release.route` and `release.pick`; layer-runtime [Fencing]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** `release.pick` takes "E's promotion lease" (layer-expansions:384). `cl-dClosedLoop-0120`'s grammar covers "builds, units and cadence runs", and layer-runtime:411-413 says "One name per lease: the build lease ..., the unit lease, and the cadence lease". The fence "travels with the effect" only for pushes by the commit queue and the lander (layer-runtime:415). A stale holder's gated calls are refused only "within one node-tick period" (layer-runtime:422). `release.route` rolls environment E back through an engine adapter, which is not a git push.
- **Consequence:** Where `release.environments` is set (the default is none), S2's stale-beat injection lets node d's in-flight rollback to "E's last verified SHA" reach E after node x has taken E's lease and promoted a newer landed SHA. E silently ends up on the older release, and the (SHA, E) records disagree with what E runs.
- **Fix:** Add the promotion lease to dPlacedRequest's lease grammar with its epoch. Require every engine adapter's promote and rollback to carry and check that epoch, or to compare-and-swap on E's current deployment id. Seen red on a planted stale holder's rollback after a take-over.

- `design.unit-spec` S6: holds
  None of S6's injections falls on this item. A failed format check takes 0099's default route, a feature fork routes to `design.decompose`, and a spent budget ends the build.
- One defect in the brief: B1-F10's evidence relies on Stage 0's K4 lead list, which sits in `stage0-leads.md`, outside the reading list, so that part cannot be checked.
- **Read outside the list above:** none

Probe outputs are under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b1/` (`cl.py`, `chain.txt`, `clauses.txt`).

# TOOL-dTotalRecall-16 — the purpose review over this tree

**Serves:** log TOOL-dTotalRecall-16

The pass's own review (spec S9, S10), run at base `8fbc5a3375d9f1890d5a371c45354e323dc89ee0` with the
working tree's registry and chain registry as that commit holds them:

```text
python tools/memory-tree/record_kinds.py --purpose-review --from memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md --write --ask TOOL-dTotalRecall-110
```

`memory.map-purpose` reads `review`, this repository's default. The review derived 44 purposes and found
none for 24 nodes (DERIVED, the `derived` and `none` lines below counted). Every derived purpose
carries its source, a `<path>:<line>` of a tracked file at that base: a record kind's is the row of
the layer-memory kind table at that line whose first cell names the kind, `-` read as a space and
`journal` read through `resolve_kind` as `log`; a chain build's is the H1 of its README. Each chain
row's purpose went into `memory/project/chain.toml` as the string `check_chain_registry` reads, its
source the line printed here (§8 F6). No chain build lacked an H1, so the chain namespace drafted no ask.

The record-kind namespace's one draft is filed as `TOOL-dTotalRecall-110` in
`memory/builds/dTotalRecall/BACKLOG.md`, and `--write --ask TOOL-dTotalRecall-110` wrote it as the
`pending` of each `none` row, which the view renders `—`. The derived texts are the table's words cut
at a word boundary under `PURPOSE_BYTES`; whether each describes its kind is the owner's to read (spec
§5 risks): the `log` row's, from the table's `journal` row, describes the grammar the kind once had.

```text
record-kinds: purpose · memory.map-purpose review
derived record-kind:spec · its writer is `design.unit-spec`; the spec redesigned as a structured, tagged contract · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:412
none record-kind:spec-audit · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:diff-review · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived record-kind:log · the journal grammar moved into the core; writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:446
none record-kind:research · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived record-kind:run-record · observability's journal reader writes it when the journal shows a run closed, as `observability.run-record` says · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:450
derived record-kind:backlog-row · the ask register's row store; the memory contract declares it; writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:456
derived record-kind:design-record · a core memory kind with no writer item; the memory contract declares it · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:454
derived record-kind:dossier · dossiers anchored to symbol keys; its writer, where the map is installed, is `build.unit-pass`, the claiming dossier's · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:459
derived record-kind:deviation · the record kept in its departing build's `build/` folder, read by the deviation join, the as-built view · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:399
derived record-kind:exception · the exception register, kept in the building build's `build/` folder as a deviation record is; writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:400
derived record-kind:override · `charter.override` and its record, under the precedence and override rule, the record kept in the building build's · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:401
none record-kind:change · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:red-fix · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived record-kind:disposition · the owner's disposition record, written by whichever channel carried it: the mailbox, a terminal command or a prompt. · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:442
derived record-kind:acceptance · its writer is `build.acceptance`; dDeclaredLoop builds the witnesses computed rather than typed, the acceptance re-run · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:420
derived record-kind:transition · the transition record three ways; every step's exit item writes it: `plan.exit`, `design.exit`, `build.exit` · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:439
derived record-kind:recommendation · every `*.recommend` item writes it; the stage-exit recommendation is one mechanism, dDeclaredLoop's (AF-1) · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:470
none record-kind:widen · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:leg-tail · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived record-kind:flake · its writer is `test.flakes`; flake quarantine · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:425
none record-kind:gate-health · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived record-kind:card · the build's orientation card at level 1, its stores and snapshot; its writer is `entry.orient`, which composes it · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:406
derived record-kind:probe-trigger · its writer is `probe.trigger`: why the probe opened, keyed by the boundary or the raising return, or by content for a · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:472
derived record-kind:probe · its writer is `probe.return`: one record per probe, its kind a verification, a reproduction or an experiment, an · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:471
derived record-kind:view · a generated view: LIVE.md, the ledger, the ask views; re-rendered, never merged (the away pass); writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:477
derived record-kind:registry · a gate's row registry under `memory/project/`, written by its gate's pin emitter (the away pass); writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:478
derived record-kind:archive · a rotated record under `memory/archive/`, written by rotation (the away pass); writer item not named · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:479
derived record-kind:instrument · a script, table or drawing kept beside the record it serves (the away pass); writer item not named: the session that · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:480
derived record-kind:witness · a declared pocket outside the tree, such as a transcript, a Codex rollout, the auto-memory, the live inbox or a · memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:481
none record-kind:orientation-cards · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:unattended-sidecars · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:runlog-journal · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:drift-history · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:gate-ledger · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:health-logs · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:hook-state · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:reuse-lookups · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:recall-cache · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:review-lenses · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:transition-cache · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:gov-index · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:gov-feed · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:handoff-calls · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:index-render-stamp · no H1: a record kind lives in the shared registry; no row of the --from table names it
none record-kind:git-client-state · no H1: a record kind lives in the shared registry; no row of the --from table names it
derived chain:dTrueNorth · the Fidelity build of the dClosedLoop chain · memory/builds/dTrueNorth/README.md:13
derived chain:dGroundRules · the Policy build of the dClosedLoop chain · memory/builds/dGroundRules/README.md:13
derived chain:dSafePassage · the Supersession build of the dClosedLoop chain · memory/builds/dSafePassage/README.md:13
derived chain:dOrderedCharter · the Foundation build of the dClosedLoop chain · memory/builds/dOrderedCharter/README.md:13
derived chain:dFairHearing · the Review harness build of the dClosedLoop chain · memory/builds/dFairHearing/README.md:13
derived chain:dDeclaredLoop · the Spine build of the dClosedLoop chain · memory/builds/dDeclaredLoop/README.md:12
derived chain:dPlacedRequest · the Entry build of the dClosedLoop chain · memory/builds/dPlacedRequest/README.md:13
derived chain:dKeptSession · the Session build of the dClosedLoop chain · memory/builds/dKeptSession/README.md:12
derived chain:dBoundRoles · the Roles build of the dClosedLoop chain · memory/builds/dBoundRoles/README.md:12
derived chain:dFurnishedOrders · the Orders build of the dClosedLoop chain · memory/builds/dFurnishedOrders/README.md:12
derived chain:dTotalRecall · the Memory build of the dClosedLoop chain · memory/builds/dTotalRecall/README.md:12
derived chain:dLinkedLibrary · the Library build of the dClosedLoop chain · memory/builds/dLinkedLibrary/README.md:12
derived chain:dMindYourWords · the Lexicon build of the dClosedLoop chain · memory/builds/dMindYourWords/README.md:12
derived chain:dWellOiledMachine · the Runtime build of the dClosedLoop chain · memory/builds/dWellOiledMachine/README.md:12
derived chain:dWitnessedBar · the Test build of the dClosedLoop chain · memory/builds/dWitnessedBar/README.md:13
derived chain:dRankedPlan · the Plan build of the dClosedLoop chain · memory/builds/dRankedPlan/README.md:12
derived chain:dIndexedDesign · the Design build of the dClosedLoop chain · memory/builds/dIndexedDesign/README.md:12
derived chain:dScopedBuild · the Build build of the dClosedLoop chain · memory/builds/dScopedBuild/README.md:12
derived chain:dShippedRelease · the Deploy build of the dClosedLoop chain · memory/builds/dShippedRelease/README.md:12
derived chain:dTendedCadence · the Maintain build of the dClosedLoop chain · memory/builds/dTendedCadence/README.md:12
derived chain:dCalibratedLens · the Review build of the dClosedLoop chain · memory/builds/dCalibratedLens/README.md:12
derived chain:dConvergedCharter · the Convergence build of the dClosedLoop chain · memory/builds/dConvergedCharter/README.md:12
ask record-kind · record-kind:spec-audit (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:diff-review (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:research (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:change (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:red-fix (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:widen (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:leg-tail (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:gate-health (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:orientation-cards (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:unattended-sidecars (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:runlog-journal (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:drift-history (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:gate-ledger (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:health-logs (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:hook-state (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:reuse-lookups (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:recall-cache (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:review-lenses (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:transition-cache (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:gov-index (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:gov-feed (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:handoff-calls (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:index-render-stamp (no H1: a record kind lives in the shared registry; no row of the --from table names it); record-kind:git-client-state (no H1: a record kind lives in the shared registry; no row of the --from table names it)
record-kinds: purpose · wrote 46 registry rows, 24 of them pending, and 22 chain rows
record-kinds: wrote the region of HYGIENE.template.md, 46 rows
```

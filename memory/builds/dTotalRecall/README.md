---
slug: dTotalRecall
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-27
status: OPEN
spec-audit: 2026-10-21
parents: dDeclaredLoop dWitnessedBar dPlacedRequest
may: PLAY-dClosedLoop-3
---

# dTotalRecall — the Memory build of the dClosedLoop chain

## The problem this build exists to solve

dTotalRecall owns 22 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-mem-01,
gap-mem-04, gap-mem-05, gap-mem-06, gap-mem-07, gap-mem-13, gap-mem-16, gap-mem-20, gap-mem-21, gap-mem-26,
gap-mem-27, gap-design-01, gap-mem-28, gap-mem-30, gap-mem-36, gap-mem-37, gap-mem-38, gap-mem-40, gap-mem-41,
gap-mem-42, gap-mem-43, gap-mem-48. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 26 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 22 owned gaps above close.

## Detriments if this is not built

- Its 22 owned gaps stay open.
- Its 5 child builds wait on it: dLinkedLibrary, dWellOiledMachine, dRankedPlan, dIndexedDesign, dShippedRelease.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dTotalRecall` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dTotalRecall`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dTotalRecall-1` | `cl-dClosedLoop-0212@121cf0ba` | the memory contract: the record-kind registry (per kind: tag |
| 2 | `TOOL-dTotalRecall-2` | `cl-dClosedLoop-0213@09982ca6` | the one `record` write command |
| 3 | `TOOL-dTotalRecall-3` | `cl-dClosedLoop-0214@78961f0f` | for every filer outside a build |
| 4 | `TOOL-dTotalRecall-4` | `cl-dClosedLoop-0215@10676c23` | the build README's declared front-matter schema |
| 5 | `TOOL-dTotalRecall-5` | `cl-dClosedLoop-0216@f8936b35` | the slug and id grammar exported once and read by every slug and id reader (`builds.slug-words` |
| 6 | `TOOL-dTotalRecall-6` | `cl-dClosedLoop-0217@631907d1` | typed relations (`depends-on` |
| 7 | `TOOL-dTotalRecall-7` | `cl-dClosedLoop-0218@939beda1` | the ask kind's acceptance at filing (`asks.acceptance`) |
| 8 | `TOOL-dTotalRecall-8` | `cl-dClosedLoop-0219@927a3172` | the core `code` record (night pass |
| 9 | `TOOL-dTotalRecall-9` | `cl-dClosedLoop-0220@d0de1caf` | the `section` |
| 10 | `TOOL-dTotalRecall-10` | `cl-dClosedLoop-0221@5746ccbd` | derived anchors suffixed for a repeated heading |
| 11 | `TOOL-dTotalRecall-11` | `cl-dClosedLoop-0222@bc317ce6` | the shape-run kind |
| 12 | `TOOL-dTotalRecall-12` | `cl-dClosedLoop-0223@18c3e1ad` | the acceptance re-measure counted over every read channel |
| 13 | `TOOL-dTotalRecall-13` | `cl-dClosedLoop-0224@bfb0a85c` | the shared extraction primitive in `tools/lib` (LX-2) |
| 14 | `TOOL-dTotalRecall-14` | `cl-dClosedLoop-0225@db15491d` | the level-0 project map (PM-1 |
| 15 | `TOOL-dTotalRecall-15` | `cl-dClosedLoop-0226@0bd15de1` | the three-way completeness check and the `map` leg pack |
| 16 | `TOOL-dTotalRecall-16` | `cl-dClosedLoop-0227@b1bcbcb9` | the record-kind registry's purpose field |
| 17 | `TOOL-dTotalRecall-17` | `cl-dClosedLoop-0228@fcc9ca71` | the replay with the map and without at its first unit |
| 18 | `TOOL-dTotalRecall-18` | `cl-dClosedLoop-0229@03c635cf` | the kind registry completed: home |
| 19 | `TOOL-dTotalRecall-19` | `cl-dClosedLoop-0230@63f11811` | `record` writing each record's header (Serves |
| 20 | `TOOL-dTotalRecall-20` | `cl-dClosedLoop-0231@392c9e56` | its own upgrade steps: the `journal` alias |
| 21 | `TOOL-dTotalRecall-21` | `cl-dClosedLoop-0232@94a25816` | memory-recall's FTS5 tables moved into the one index file |
| 22 | `TOOL-dTotalRecall-22` | `cl-dClosedLoop-0233@50683b2a` | each edge type's cardinality declared per target as well as per source in the kind registry and checked over the merged tree after every merge |
| 23 | `TOOL-dTotalRecall-23` | `cl-dClosedLoop-0234@eb7b1784` | the memory legs reading the index's rows for unchanged blobs and re-parsing only changed ones |
| 24 | `TOOL-dTotalRecall-24` | `cl-dClosedLoop-0235@dba1fb83` | every commit that touches a record appended to the change feed with its edges once it lands |
| 25 | `TOOL-dTotalRecall-25` | `cl-dClosedLoop-0236@4e9bd61a` | the stream-plan kind: a build's units grouped into streams |
| 26 | `TOOL-dTotalRecall-26` | `cl-dClosedLoop-0237@0c51b12a` | the atlas under `help/atlas/` |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14
ids TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-27

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 4 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dTotalRecall's 26 clause(s) and 36 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 26 (cl-dClosedLoop-0212, cl-dClosedLoop-0213, cl-dClosedLoop-0214, cl-dClosedLoop-0215, cl-dClosedLoop-0216, cl-dClosedLoop-0217, cl-dClosedLoop-0218, cl-dClosedLoop-0219, cl-dClosedLoop-0220, cl-dClosedLoop-0221, cl-dClosedLoop-0222, cl-dClosedLoop-0223, cl-dClosedLoop-0224,
  cl-dClosedLoop-0225, cl-dClosedLoop-0226, cl-dClosedLoop-0227, cl-dClosedLoop-0228, cl-dClosedLoop-0229, cl-dClosedLoop-0230, cl-dClosedLoop-0231, cl-dClosedLoop-0232, cl-dClosedLoop-0233, cl-dClosedLoop-0234, cl-dClosedLoop-0235, cl-dClosedLoop-0236, cl-dClosedLoop-0237)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: policy-key.asks.acceptance, policy-key.builds.agent-root, policy-key.builds.slug-date, policy-key.builds.slug-style, policy-key.builds.slug-words, policy-key.help.atlas, policy-key.memory.code-languages, policy-key.memory.item-budget, policy-key.memory.legacy-anchors,
  policy-key.memory.load-budget, policy-key.memory.map-budget, policy-key.memory.map-overflow, policy-key.memory.map-purpose, policy-key.memory.over-budget, policy-key.memory.superseded-slices, record-kind.archive, record-kind.ask, record-kind.backlog-row, record-kind.build-readme,
  record-kind.claim, record-kind.code, record-kind.design-record, record-kind.dossier, record-kind.instrument, record-kind.registry, record-kind.shape-run, record-kind.stream-plan, record-kind.view, record-kind.witness, system.memory-structure, system.project-map, tag-namespace.class,
  tag-namespace.feature, tag-namespace.marker, tag-namespace.record, tag-namespace.section
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0221, cl-dClosedLoop-0222, cl-dClosedLoop-0232, cl-dClosedLoop-0233, cl-dClosedLoop-0234, cl-dClosedLoop-0236
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dRankedPlan](../dRankedPlan/README.md), [dShippedRelease](../dShippedRelease/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->

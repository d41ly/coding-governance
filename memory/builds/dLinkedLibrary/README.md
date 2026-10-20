---
slug: dLinkedLibrary
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-26
status: OPEN
spec-audit: 2026-10-21
parents: dTotalRecall
may: PLAY-dClosedLoop-3
---

# dLinkedLibrary — the Library build of the dClosedLoop chain

## The problem this build exists to solve

dLinkedLibrary owns 23 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-mem-02,
gap-mem-03, gap-mem-08, gap-mem-09, gap-mem-11, gap-mem-12, gap-mem-14, gap-mem-15, gap-mem-17, gap-mem-18,
gap-mem-19, gap-mem-22, gap-mem-24, gap-mem-25, gap-mem-29, gap-mem-31, gap-mem-32, gap-mem-33, gap-mem-34,
gap-mem-39, gap-tool-17, gap-deploy-26, gap-mem-45. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 25 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 23 owned gaps above close.

## Detriments if this is not built

- Its 23 owned gaps stay open.
- Its 3 child builds wait on it: dMindYourWords, dIndexedDesign, dShippedRelease.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dLinkedLibrary` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dLinkedLibrary`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-19.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dLinkedLibrary-1` | `cl-dClosedLoop-0238@36136b48` | decisions split by kind: reuse entries as level-3 instruction units beside their dossiers and under `memory/map/conventions/` |
| 2 | `TOOL-dLinkedLibrary-2` | `cl-dClosedLoop-0239@36d4c1c8` | the reuse scout's house index in M1c's shape (a digest of symbols |
| 3 | `TOOL-dLinkedLibrary-3` | `cl-dClosedLoop-0240@5773ca81` | `reuse_lookup.py` and its agent retired with their readers rewritten |
| 4 | `TOOL-dLinkedLibrary-4` | `cl-dClosedLoop-0241@0e5185f1` | the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries |
| 5 | `TOOL-dLinkedLibrary-5` | `cl-dClosedLoop-0242@866cebbc` | the generated views: the decisions' holds-now view and the reuse view |
| 6 | `TOOL-dLinkedLibrary-6` | `cl-dClosedLoop-0243@9acc070e` | the research view |
| 7 | `TOOL-dLinkedLibrary-7` | `cl-dClosedLoop-0244@e14fc5fd` | the `annotations` leg |
| 8 | `TOOL-dLinkedLibrary-8` | `cl-dClosedLoop-0245@2d7af537` | retrofit's `baseline` and `census` record kinds |
| 9 | `TOOL-dLinkedLibrary-9` | `cl-dClosedLoop-0246@96afa172` | the origin check |
| 10 | `TOOL-dLinkedLibrary-10` | `cl-dClosedLoop-0247@87bb7e47` | the progress cell |
| 11 | `TOOL-dLinkedLibrary-11` | `cl-dClosedLoop-0248@8c261008` | the annotation resolve check's legacy and the untouched long blocks registered as ledger populations |
| 12 | `TOOL-dLinkedLibrary-12` | `cl-dClosedLoop-0249@49ce83a8` | the `marker` namespace over the existing `gov:` words |
| 13 | `TOOL-dLinkedLibrary-13` | `cl-dClosedLoop-0250@9ea3dfcf` | and the dated backfill of `kind: research-return` over the existing returns |
| 14 | `TOOL-dLinkedLibrary-14` | `cl-dClosedLoop-0251@23b8b8e1` | `gov map code` and `gov code show` |
| 15 | `TOOL-dLinkedLibrary-15` | `cl-dClosedLoop-0252@5aa0f94b` | the enrichment workflow: purposes derived first from docstrings and headers |
| 16 | `TOOL-dLinkedLibrary-16` | `cl-dClosedLoop-0253@22d88118` | the replay's losing test extended to code: a unit's files read and its lookups counted |
| 17 | `TOOL-dLinkedLibrary-17` | `cl-dClosedLoop-0254@e703feac` | extractors emitting typed edges from annotations |
| 18 | `TOOL-dLinkedLibrary-18` | `cl-dClosedLoop-0255@c0b78911` | the region-parser factory in `tools/lib` |
| 19 | `TOOL-dLinkedLibrary-19` | `cl-dClosedLoop-0256@aea4db49` | the dossier's header becoming the feature node and its prose moving into units and records |
| 20 | `TOOL-dLinkedLibrary-20` | `cl-dClosedLoop-0257@ac01a5f8` | the `feature` namespace armed as an instruction selector when it registers |
| 21 | `TOOL-dLinkedLibrary-21` | `cl-dClosedLoop-0258@bbce050b` | the ctags extractor pack |
| 22 | `TOOL-dLinkedLibrary-22` | `cl-dClosedLoop-0259@2b91da03` | `decides` on every decision row |
| 23 | `TOOL-dLinkedLibrary-23` | `cl-dClosedLoop-0260@c677f704` | `adopt.instructions`: at install an adopter's own instruction files rendered verbatim as a legacy block after the project block |
| 24 | `TOOL-dLinkedLibrary-24` | `cl-dClosedLoop-0261@6566da73` | each bug class's gate status derived |
| 25 | `TOOL-dLinkedLibrary-25` | `cl-dClosedLoop-0500@84eb6d7a` | the records that contradict the code corrected at their sources: the map README's path |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13
ids TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25
ids TOOL-dLinkedLibrary-26

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dMindYourWords](../dMindYourWords/README.md), [dShippedRelease](../dShippedRelease/README.md)
<!-- /gen:build-edges -->

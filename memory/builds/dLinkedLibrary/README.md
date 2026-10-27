---
slug: dLinkedLibrary
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-26 TOOL-dLinkedLibrary-27 TOOL-dLinkedLibrary-28 TOOL-dLinkedLibrary-29 TOOL-dLinkedLibrary-30 TOOL-dLinkedLibrary-31 TOOL-dLinkedLibrary-32 TOOL-dLinkedLibrary-33 TOOL-dLinkedLibrary-34 TOOL-dLinkedLibrary-35 TOOL-dLinkedLibrary-36 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80
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
**Build status:** OPEN · 69 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13
ids TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25
ids TOOL-dLinkedLibrary-26 TOOL-dLinkedLibrary-27 TOOL-dLinkedLibrary-28 TOOL-dLinkedLibrary-29 TOOL-dLinkedLibrary-30 TOOL-dLinkedLibrary-31 TOOL-dLinkedLibrary-32 TOOL-dLinkedLibrary-33 TOOL-dLinkedLibrary-34 TOOL-dLinkedLibrary-35 TOOL-dLinkedLibrary-36 TOOL-dLinkedLibrary-37
ids TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49
ids TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61
ids TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73
ids TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLinkedLibrary-25 — eight records that contradict the code, each corrected at its source](spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md) | 1 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-18 — the region-parser factory in `tools/lib`, and every region parser re-pointed to it](spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md) | 2 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-12 — the `marker` namespace's members, one per existing `gov:` word, and the check that refuses an unregistered one](spec/2026-10-26-spec-TOOL-dLinkedLibrary-12.md) | 3 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-43 — the region census stated exactly, its exclusions written as rules, and the two parsers it missed re-pointed](spec/2026-10-26-spec-TOOL-dLinkedLibrary-43.md) | 3 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-45 — govkit's `find_block` and `write_block` re-pointed to the factory, and a census arm that sees a parser with no marker constant](spec/2026-10-26-spec-TOOL-dLinkedLibrary-45.md) | 3 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-22 — `decides` on every decision row, `Decided:` trailers read as decision rows, and every bug class naming its cause, language and platform](spec/2026-10-26-spec-TOOL-dLinkedLibrary-22.md) | 4 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-48 — the marker registry in an adopter: a reader resolved through the install, and "appears nowhere" graded only on this repository's own rows](spec/2026-10-26-spec-TOOL-dLinkedLibrary-48.md) | 4 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-54 — the shipped micro-format gate carries the `region_sh` block inline, so it runs where `<prefix>/lib/` never travels](spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md) | 4 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-55 — the micro-format gate's selftest runs the gate alone at a prefix that holds no `lib/`](spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md) | 4 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-56 — `region_nth` becomes a parity-gated block, and the run-gates canary carries it inline for its `mempause_sh` slice](spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md) | 4 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-24 — each bug class's gate status derived, never declared, and a gated class left off every checklist](spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md) | 5 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-62 — an unresolved reader stays red on a row this repository's own builds own; only rows owned outside read `not installed`](spec/2026-10-27-spec-TOOL-dLinkedLibrary-62.md) | 5 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-65 — the micro-format gate refuses by name when its inline region reader is absent](spec/2026-10-27-spec-TOOL-dLinkedLibrary-65.md) | 5 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-66 — the micro-format suite's lib-less arm stages its failing case as the stripped block](spec/2026-10-27-spec-TOOL-dLinkedLibrary-66.md) | 5 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-13 — the research-return kind: its declared line, its check, and the dated backfill over the existing returns](spec/2026-10-26-spec-TOOL-dLinkedLibrary-13.md) | 6 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dLinkedLibrary-49 — `--observe` records `refused` only on the leg's failing status, bounded, and every other outcome as `unobservable`](spec/2026-10-26-spec-TOOL-dLinkedLibrary-49.md) | 6 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-6 — the research view over the research-return kind, and the library-view seam it lands](spec/2026-10-26-spec-TOOL-dLinkedLibrary-6.md) | 7 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-61 — `--observe` kills the process tree at its bound and routes each run's output to a file](spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md) | 7 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-1 — decisions split by kind: reuse entries as level-3 units, the major-decision log, its rows routed by two raters, and the `[records]` rule reworded](spec/2026-10-26-spec-TOOL-dLinkedLibrary-1.md) | 8 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-67 — `--observe` resolves a leading bash and python before it runs an observed argv](spec/2026-10-27-spec-TOOL-dLinkedLibrary-67.md) | 8 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-5 — the generated views: the decision log's holds-now view and the reuse view](spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md) | 9 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-60 — `propose` reads the call unit 19 spells, filing each seam as the part `<feature>.<n>` before that unit's pass](spec/2026-10-27-spec-TOOL-dLinkedLibrary-60.md) | 9 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-19 — the dossier's header becomes the feature node, and its prose moves into units and records](spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md) | 10 | 2 | OPEN | rev-4 | 2026-10-27 |
| [TOOL-dLinkedLibrary-20 — the `feature` namespace armed as an instruction selector](spec/2026-10-26-spec-TOOL-dLinkedLibrary-20.md) | 11 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-38 — several reuse parts per feature, so each dossier seam becomes its own entry](spec/2026-10-26-spec-TOOL-dLinkedLibrary-38.md) | 11 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-50 — `dossier_move.py apply` takes the caller's build and unit, so an adopter's update can run it](spec/2026-10-26-spec-TOOL-dLinkedLibrary-50.md) | 11 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-4 — the `gov:note` grammar, the generated annotation index, its resolve check and `gov:feature` anchors joined both ways with reuse entries](spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md) | 12 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-17 — typed edges from annotations, front matter, dossiers and decision rows, and the span rule with `gov:end <tag>`](spec/2026-10-26-spec-TOOL-dLinkedLibrary-17.md) | 13 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-39 — the anchor arm reds an accepted entry with no anchor line and lists a proposed one without red](spec/2026-10-26-spec-TOOL-dLinkedLibrary-39.md) | 13 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-44 — the resolve arm's default population: every comment line of every profiled file, not only files that carry a note](spec/2026-10-26-spec-TOOL-dLinkedLibrary-44.md) | 13 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dLinkedLibrary-11 — the annotation resolve check's legacy and the untouched long comment blocks registered as ledger populations](spec/2026-10-26-spec-TOOL-dLinkedLibrary-11.md) | 14 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-41 — the span arm reads `iter_family` on its own conventions: a top-level pair at depth 1, a lead that carries its space](spec/2026-10-26-spec-TOOL-dLinkedLibrary-41.md) | 14 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dLinkedLibrary-7 — the `annotations` leg, the lookup under `annotations.lookup`, the read hook on shell reads, and the follow-through test](spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md) | 15 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-21 — the ctags extractor pack: definitions and ranges for every language the built-in extractors do not read](spec/2026-10-26-spec-TOOL-dLinkedLibrary-21.md) | 16 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-14 — the code reader: `gov map code`, and `gov code show`, `callers`, `tests` and `where`, `git grep` its floor](spec/2026-10-26-spec-TOOL-dLinkedLibrary-14.md) | 17 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-15 — code purposes: derived first from docstrings and headers, an agent's pass for the rest as `memory.code-enrich` says, keyed to body hashes and joined both ways with a pending population](spec/2026-10-26-spec-TOOL-dLinkedLibrary-15.md) | 18 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-16 — the code replay: a unit's files read and its lookups counted with the `code` slot and without, scored by the scorer factory against the seed alone](spec/2026-10-26-spec-TOOL-dLinkedLibrary-16.md) | 19 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-46 — the `code record selftest` leg, which runs the code reader's, the enrichment's and the ctags pack's selftests the arm lines claimed](spec/2026-10-26-spec-TOOL-dLinkedLibrary-46.md) | 19 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-8 — retrofit's record kinds, the `origin` field, and the `adopt` program the core's own command runs](spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md) | 20 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-47 — the `adopt program selftest` leg, which runs the adopt program's plants unit 8's arm line claimed](spec/2026-10-26-spec-TOOL-dLinkedLibrary-47.md) | 21 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-51 — the CI census reads every workflow file, every line a job runs, and refuses a job that publishes, pushes or holds a write grant](spec/2026-10-26-spec-TOOL-dLinkedLibrary-51.md) | 21 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-9 — the origin check: each record's `origin` re-derived from history, shown in every slice and ranked in the reuse digest](spec/2026-10-26-spec-TOOL-dLinkedLibrary-9.md) | 21 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-10 — the progress cell: the retrofit's populations, seeded, now and drained, on the orientation card](spec/2026-10-26-spec-TOOL-dLinkedLibrary-10.md) | 22 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-37 — a `reconstructed` or `imported` origin graded on its provenance, so the adopt program's own records read green](spec/2026-10-26-spec-TOOL-dLinkedLibrary-37.md) | 22 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dLinkedLibrary-63 — the CI census reads the lines a GitLab or Azure job runs, and refuses one whose credentials it cannot read](spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md) | 22 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-2 — the reuse scout's house index, delivered through the task card's `**Reuse:**` field and accepted on aScoutedSeam's benchmark](spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md) | 23 | 2 | OPEN | rev-2 | 2026-10-26 |
| [TOOL-dLinkedLibrary-71 — the CI census refuses a GitLab job whose text arrives by inheritance or include](spec/2026-10-27-spec-TOOL-dLinkedLibrary-71.md) | 23 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-72 — the CI census refuses an Azure job a template supplies at any level](spec/2026-10-27-spec-TOOL-dLinkedLibrary-72.md) | 23 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-73 — the CI census reads a block scalar across blank lines and as a list item](spec/2026-10-27-spec-TOOL-dLinkedLibrary-73.md) | 23 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-3 — `reuse_lookup.py` and its agent retired, every reader rewritten by name and by value, with its upgrade step, and memory-recall narrowed to its why-search](spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md) | 24 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-76 — the CI census refuses a GitLab indirection key under `default:`, which reaches every job](spec/2026-10-27-spec-TOOL-dLinkedLibrary-76.md) | 24 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-77 — the CI census reads a block-scalar header that carries node properties or a comment](spec/2026-10-27-spec-TOOL-dLinkedLibrary-77.md) | 24 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-78 — the CI census folds a `>` block as YAML folds it and joins a continued command before matching](spec/2026-10-27-spec-TOOL-dLinkedLibrary-78.md) | 24 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-23 — `adopt.instructions`: an adopter's own instruction files kept verbatim as a legacy block, every harness file wired at once, each paragraph ruled once](spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md) | 25 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-42 — `MAP_CLI` pointed at the house index, a CLI that exists whichever way the map replay goes](spec/2026-10-26-spec-TOOL-dLinkedLibrary-42.md) | 25 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-40 — `gov:legacy` registered as a `[[marker]]` row of the marker registry the markers arm reads](spec/2026-10-26-spec-TOOL-dLinkedLibrary-40.md) | 26 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-57 — the reuse-lookup step's witness keyed on the `MAP_CLI` value its before-image recorded](spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md) | 26 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-58 — the reuse-lookup step over a target that holds no `.unattended.conf`: nothing created, the witness green](spec/2026-10-27-spec-TOOL-dLinkedLibrary-58.md) | 26 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-52 — the code half of the round-1 audit's minors: 53 findings closed where the built code holds them](spec/2026-10-26-spec-TOOL-dLinkedLibrary-52.md) | 27 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-53 — the records-and-observations half of the round-1 audit's minors: 11 findings closed by a criterion, a waiver row or a declaration](spec/2026-10-26-spec-TOOL-dLinkedLibrary-53.md) | 27 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-69 — the lookup's retirement step reads `MAP_CLI` the way bash `source` reads it](spec/2026-10-27-spec-TOOL-dLinkedLibrary-69.md) | 27 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-70 — the lookup's retirement step re-points every spelling of a lookup-naming `MAP_CLI`](spec/2026-10-27-spec-TOOL-dLinkedLibrary-70.md) | 27 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-59 — the decision log's diff against base read relative to unit 1's rotation, so a correct build reads additive](spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md) | 28 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-64 — the minors of the spec audit of units 37 to 53: 23 findings closed where the built code and records hold them](spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md) | 29 | 2 | OPEN | rev-3 | 2026-10-27 |
| [TOOL-dLinkedLibrary-68 — `log-diff` reads the decision log's rows and archives through the kit's row grammar](spec/2026-10-27-spec-TOOL-dLinkedLibrary-68.md) | 29 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-74 — the spec audit of units 54 to 64: its medium and low findings, batched](spec/2026-10-27-spec-TOOL-dLinkedLibrary-74.md) | 30 | 2 | OPEN | rev-2 | 2026-10-27 |
| [TOOL-dLinkedLibrary-75 — the reuse-tag sweep reads a hyphenated feature name, and shows its red on a planted tag](spec/2026-10-27-spec-TOOL-dLinkedLibrary-75.md) | 31 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-79 — the CI census reads the credentials of every block that applies to a job, file-level blocks included](spec/2026-10-27-spec-TOOL-dLinkedLibrary-79.md) | 31 | 2 | OPEN | rev-1 | 2026-10-27 |
| [TOOL-dLinkedLibrary-80 — the spec audit of units 65 to 74: its medium and low findings, batched](spec/2026-10-27-spec-TOOL-dLinkedLibrary-80.md) | 32 | 2 | OPEN | rev-1 | 2026-10-27 |
<!-- /gen:build-units -->

Records: 69 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80.

Ids whose spec moved past its audited revision: TOOL-dLinkedLibrary-1@rev-1 TOOL-dLinkedLibrary-10@rev-1 TOOL-dLinkedLibrary-11@rev-1 TOOL-dLinkedLibrary-12@rev-1 TOOL-dLinkedLibrary-14@rev-1 TOOL-dLinkedLibrary-15@rev-1 TOOL-dLinkedLibrary-16@rev-1 TOOL-dLinkedLibrary-17@rev-1
TOOL-dLinkedLibrary-18@rev-1 TOOL-dLinkedLibrary-19@rev-1 TOOL-dLinkedLibrary-2@rev-1 TOOL-dLinkedLibrary-20@rev-1 TOOL-dLinkedLibrary-21@rev-1 TOOL-dLinkedLibrary-22@rev-1 TOOL-dLinkedLibrary-23@rev-1 TOOL-dLinkedLibrary-24@rev-1 TOOL-dLinkedLibrary-25@rev-1 TOOL-dLinkedLibrary-3@rev-1
TOOL-dLinkedLibrary-38@rev-1 TOOL-dLinkedLibrary-39@rev-1 TOOL-dLinkedLibrary-4@rev-1 TOOL-dLinkedLibrary-40@rev-1 TOOL-dLinkedLibrary-42@rev-1 TOOL-dLinkedLibrary-43@rev-1 TOOL-dLinkedLibrary-45@rev-1 TOOL-dLinkedLibrary-46@rev-1 TOOL-dLinkedLibrary-47@rev-1 TOOL-dLinkedLibrary-48@rev-1
TOOL-dLinkedLibrary-49@rev-1 TOOL-dLinkedLibrary-5@rev-1 TOOL-dLinkedLibrary-50@rev-1 TOOL-dLinkedLibrary-51@rev-1 TOOL-dLinkedLibrary-52@rev-1 TOOL-dLinkedLibrary-53@rev-1 TOOL-dLinkedLibrary-6@rev-1 TOOL-dLinkedLibrary-7@rev-1 TOOL-dLinkedLibrary-8@rev-1 TOOL-dLinkedLibrary-9@rev-1
TOOL-dLinkedLibrary-54@rev-1 TOOL-dLinkedLibrary-55@rev-1 TOOL-dLinkedLibrary-56@rev-1 TOOL-dLinkedLibrary-57@rev-1 TOOL-dLinkedLibrary-58@rev-1 TOOL-dLinkedLibrary-59@rev-1 TOOL-dLinkedLibrary-60@rev-1 TOOL-dLinkedLibrary-61@rev-1 TOOL-dLinkedLibrary-63@rev-1 TOOL-dLinkedLibrary-64@rev-1
TOOL-dLinkedLibrary-66@rev-1 TOOL-dLinkedLibrary-67@rev-1 TOOL-dLinkedLibrary-68@rev-1 TOOL-dLinkedLibrary-69@rev-1 TOOL-dLinkedLibrary-71@rev-1 TOOL-dLinkedLibrary-72@rev-1 TOOL-dLinkedLibrary-73@rev-1 TOOL-dLinkedLibrary-74@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dLinkedLibrary's 25 clause(s) and 25 owned node(s), over 69 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 25
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-26-spec-TOOL-dLinkedLibrary-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-39.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dLinkedLibrary-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-41.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-43.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dLinkedLibrary-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-45.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-47.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dLinkedLibrary-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-51.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dLinkedLibrary-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dLinkedLibrary-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-65.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-66.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-67.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-68.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-69.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-70.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-71.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-72.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-73.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-74.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-75.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-76.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-77.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-78.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dLinkedLibrary-79.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dLinkedLibrary-80.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0242, cl-dClosedLoop-0243, cl-dClosedLoop-0247, cl-dClosedLoop-0248, cl-dClosedLoop-0256, cl-dClosedLoop-0261
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dLinkedLibrary-25` | no |
| 2 | `TOOL-dLinkedLibrary-18` | no |
| 3 | `TOOL-dLinkedLibrary-12`, `TOOL-dLinkedLibrary-43`, `TOOL-dLinkedLibrary-45` | no |
| 4 | `TOOL-dLinkedLibrary-22`, `TOOL-dLinkedLibrary-48`, `TOOL-dLinkedLibrary-54`, `TOOL-dLinkedLibrary-55`, `TOOL-dLinkedLibrary-56` | yes |
| 5 | `TOOL-dLinkedLibrary-24`, `TOOL-dLinkedLibrary-62`, `TOOL-dLinkedLibrary-65`, `TOOL-dLinkedLibrary-66` | yes |
| 6 | `TOOL-dLinkedLibrary-13`, `TOOL-dLinkedLibrary-49` | no |
| 7 | `TOOL-dLinkedLibrary-6`, `TOOL-dLinkedLibrary-61` | yes |
| 8 | `TOOL-dLinkedLibrary-1`, `TOOL-dLinkedLibrary-67` | yes |
| 9 | `TOOL-dLinkedLibrary-5`, `TOOL-dLinkedLibrary-60` | yes |
| 10 | `TOOL-dLinkedLibrary-19` | no |
| 11 | `TOOL-dLinkedLibrary-20`, `TOOL-dLinkedLibrary-38`, `TOOL-dLinkedLibrary-50` | no |
| 12 | `TOOL-dLinkedLibrary-4` | no |
| 13 | `TOOL-dLinkedLibrary-17`, `TOOL-dLinkedLibrary-39`, `TOOL-dLinkedLibrary-44` | no |
| 14 | `TOOL-dLinkedLibrary-11`, `TOOL-dLinkedLibrary-41` | no |
| 15 | `TOOL-dLinkedLibrary-7` | no |
| 16 | `TOOL-dLinkedLibrary-21` | no |
| 17 | `TOOL-dLinkedLibrary-14` | no |
| 18 | `TOOL-dLinkedLibrary-15` | no |
| 19 | `TOOL-dLinkedLibrary-16`, `TOOL-dLinkedLibrary-46` | yes |
| 20 | `TOOL-dLinkedLibrary-8` | no |
| 21 | `TOOL-dLinkedLibrary-47`, `TOOL-dLinkedLibrary-51`, `TOOL-dLinkedLibrary-9` | no |
| 22 | `TOOL-dLinkedLibrary-10`, `TOOL-dLinkedLibrary-37`, `TOOL-dLinkedLibrary-63` | yes |
| 23 | `TOOL-dLinkedLibrary-2`, `TOOL-dLinkedLibrary-71`, `TOOL-dLinkedLibrary-72`, `TOOL-dLinkedLibrary-73` | no |
| 24 | `TOOL-dLinkedLibrary-3`, `TOOL-dLinkedLibrary-76`, `TOOL-dLinkedLibrary-77`, `TOOL-dLinkedLibrary-78` | no |
| 25 | `TOOL-dLinkedLibrary-23`, `TOOL-dLinkedLibrary-42` | yes |
| 26 | `TOOL-dLinkedLibrary-40`, `TOOL-dLinkedLibrary-57`, `TOOL-dLinkedLibrary-58` | no |
| 27 | `TOOL-dLinkedLibrary-52`, `TOOL-dLinkedLibrary-53`, `TOOL-dLinkedLibrary-69`, `TOOL-dLinkedLibrary-70` | no |
| 28 | `TOOL-dLinkedLibrary-59` | no |
| 29 | `TOOL-dLinkedLibrary-64`, `TOOL-dLinkedLibrary-68` | yes |
| 30 | `TOOL-dLinkedLibrary-74` | no |
| 31 | `TOOL-dLinkedLibrary-75`, `TOOL-dLinkedLibrary-79` | yes |
| 32 | `TOOL-dLinkedLibrary-80` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dMindYourWords](../dMindYourWords/README.md), [dShippedRelease](../dShippedRelease/README.md)
<!-- /gen:build-edges -->

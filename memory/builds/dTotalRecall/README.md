---
slug: dTotalRecall
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-27 TOOL-dTotalRecall-28 TOOL-dTotalRecall-29 TOOL-dTotalRecall-30 TOOL-dTotalRecall-31 TOOL-dTotalRecall-32 TOOL-dTotalRecall-33 TOOL-dTotalRecall-34 TOOL-dTotalRecall-35 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100
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
**Build status:** DEFERRED · 91 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14
ids TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-27 TOOL-dTotalRecall-28
ids TOOL-dTotalRecall-29 TOOL-dTotalRecall-30 TOOL-dTotalRecall-31 TOOL-dTotalRecall-32 TOOL-dTotalRecall-33 TOOL-dTotalRecall-34 TOOL-dTotalRecall-35 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42
ids TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56
ids TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70
ids TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84
ids TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98
ids TOOL-dTotalRecall-99 TOOL-dTotalRecall-100

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTotalRecall-1 — the record-kind registry, the memory contract's one declaration of every kind](spec/2026-10-26-spec-TOOL-dTotalRecall-1.md) | 1 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-13 — the shared extraction primitive in `tools/lib`, which the map and the lexicon each call](spec/2026-10-26-spec-TOOL-dTotalRecall-13.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-8 — the core `code` record, derived per blob into the one index and re-timed before it is built](spec/2026-10-26-spec-TOOL-dTotalRecall-8.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-18 — the kind registry completed: every column declared, readers and writers rendered, the pockets witnessed, and `journal` renamed `log`](spec/2026-10-26-spec-TOOL-dTotalRecall-18.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-37 — only the four rendered workflow scripts are `linguist-generated`, held equal to the kits' render rows both ways](spec/2026-10-26-spec-TOOL-dTotalRecall-37.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-16 — the registry's `purpose` field, and every existing node's purpose reviewed as `memory.map-purpose` says](spec/2026-10-26-spec-TOOL-dTotalRecall-16.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-25 — the stream-plan kind, registered so the planner that writes it and the pick that reads it descend from one row](spec/2026-10-26-spec-TOOL-dTotalRecall-25.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-5 — the slug and id grammar exported once from `id_grammar.py` and read by every slug and id reader](spec/2026-10-26-spec-TOOL-dTotalRecall-5.md) | 7 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [TOOL-dTotalRecall-38 — every id reader that splits on a hyphen parses through the grammar, found by the reader census and proved by the flip probe](spec/2026-10-26-spec-TOOL-dTotalRecall-38.md) | 8 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-4 — the build README's declared front-matter schema, its routing region, the work order as each agent's root, and a design-only build's ids as units](spec/2026-10-26-spec-TOOL-dTotalRecall-4.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-54 — `parse_id_parts` lands on the named-group regex in step 8, ahead of the readers unit 38 re-points onto it](spec/2026-10-26-spec-TOOL-dTotalRecall-54.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-40 — the routing region reads every record kind through `canonical_kind`, so log records written after the rename route under logs](spec/2026-10-26-spec-TOOL-dTotalRecall-40.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-44 — the split census keys on the split's shape, so it lists every id reader whatever its value is named](spec/2026-10-26-spec-TOOL-dTotalRecall-44.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-45 — the three id readers outside unit 38's table parse through the grammar, each site held gone by file and line](spec/2026-10-26-spec-TOOL-dTotalRecall-45.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-46 — `parse_id_parts` reads the named groups of `tree_lib.build_id_token_re`, and a correction suffix parses](spec/2026-10-26-spec-TOOL-dTotalRecall-46.md) | 9 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-6 — typed relations between builds, inverted, checked both ways, free of `depends-on` cycles, and pending across nodes](spec/2026-10-26-spec-TOOL-dTotalRecall-6.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-63 — unit 46's own pass reds a parser that refuses a cited family, so unit 54's body is held at step 9](spec/2026-10-26-spec-TOOL-dTotalRecall-63.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-64 — unit 46's spec observes unit 54's parser body and designs none of its own](spec/2026-10-26-spec-TOOL-dTotalRecall-64.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-22 — each edge type's cardinality declared per source and per target, mirrored in the kind registry, and checked over the merged tree after every merge](spec/2026-10-26-spec-TOOL-dTotalRecall-22.md) | 10 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-3 — slug claim refs and ask-family counter refs, each commit carrying its claimant, minted by leased compare-and-swap and never pruned](spec/2026-10-26-spec-TOOL-dTotalRecall-3.md) | 11 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-2 — the one `record` write door, `gov_record.py new <kind>`, grown from the record factory: minting under a claim or lease, idempotent and content-addressed, rendering and refusing](spec/2026-10-26-spec-TOOL-dTotalRecall-2.md) | 12 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [TOOL-dTotalRecall-7 — the ask kind's acceptance at filing, under `asks.acceptance`](spec/2026-10-26-spec-TOOL-dTotalRecall-7.md) | 13 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-11 — the shape-run kind, the parsed view of the review-shape line](spec/2026-10-26-spec-TOOL-dTotalRecall-11.md) | 14 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-41 — the ask door refuses a line break or row separator in any value and grades the row it would write, read back](spec/2026-10-26-spec-TOOL-dTotalRecall-41.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-10 — derived anchors suffixed for a repeated heading](spec/2026-10-26-spec-TOOL-dTotalRecall-10.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-42 — the shape-run home is its id-rule's glob, a kind with no record yet is declared `unarmed`, and a record is graded only by the row its Serves kind names](spec/2026-10-26-spec-TOOL-dTotalRecall-42.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-19 — every record names its cause: the door's header and edge lines, the causes and orphan checks over a legacy population](spec/2026-10-26-spec-TOOL-dTotalRecall-19.md) | 16 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [TOOL-dTotalRecall-21 — memory-recall's FTS5 tables moved into the one index file, keyed by blob](spec/2026-10-26-spec-TOOL-dTotalRecall-21.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-36 — every code writer of a record writes its `Caused-by` line, so the causes check stays green on the records written after its seed](spec/2026-10-26-spec-TOOL-dTotalRecall-36.md) | 17 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-39 — one record-header edge reader: the edge grammar's header site binds `tree_lib.read_header_edges` and defines none of its own](spec/2026-10-26-spec-TOOL-dTotalRecall-39.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-47 — the cause backfill is a verb run at the tip after the step-17 group, so no record written between the seed and the writers' change stays causeless](spec/2026-10-26-spec-TOOL-dTotalRecall-47.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-48 — the run record's fixed head admits a cause line, and runlog grades its shape while the causes leg grades its absence](spec/2026-10-26-spec-TOOL-dTotalRecall-48.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-49 — the as-built view keeps the pinned instrument's bytes, and its writer is kept off the cause census by a stated reason](spec/2026-10-26-spec-TOOL-dTotalRecall-49.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-50 — the cause census reads the build folders' instruments, and the pinned departures writer is a declared row that drains when its owner repins](spec/2026-10-26-spec-TOOL-dTotalRecall-50.md) | 18 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-51 — a non-markdown record's cause line wears its Serves line's comment prefix, the header reader reads it, and a bare one is refused](spec/2026-10-26-spec-TOOL-dTotalRecall-51.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-9 — the memory extractors, `record find` and `record show` over the one index, and the per-item read budget](spec/2026-10-26-spec-TOOL-dTotalRecall-9.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-23 — the memory legs read the one index's rows for unchanged blobs and re-parse only changed ones](spec/2026-10-26-spec-TOOL-dTotalRecall-23.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-61 — unit 53 keeps the build-folder rows of its two file-keyed constants through its own pass, so no keep it needs lands after it](spec/2026-10-26-spec-TOOL-dTotalRecall-61.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-24 — every landed commit that touches a record appended to the change feed](spec/2026-10-26-spec-TOOL-dTotalRecall-24.md) | 20 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-67 — unit 61's amendments to units 55, 56 and 57 are read by their own text at step 20, and any it left unwritten is written before those units build](spec/2026-10-26-spec-TOOL-dTotalRecall-67.md) | 20 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-20 — this build's own upgrade steps: the journal alias, the scaffold verbs forwarded to record, the front matter graded, and the retag](spec/2026-10-26-spec-TOOL-dTotalRecall-20.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-71 — unit 57's edge to unit 56 is certified at step 21 by a probe proven live on a copy without it, and unit 67's false reading is recorded](spec/2026-10-26-spec-TOOL-dTotalRecall-71.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-72 — unit 57's edge to unit 56 is read at step 21 by a probe no shell quotes, and written with its mirror before unit 57 builds if absent](spec/2026-10-26-spec-TOOL-dTotalRecall-72.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-17 — the map's losing test: the coherence and reuse lenses replayed with the map and without, before any map code is built](spec/2026-10-26-spec-TOOL-dTotalRecall-17.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-81 — the guarded revision read: a pass commit resolved by the driver's rule, verified as a commit and read by `read_blobs_at`, refused when any step answers empty, first applied to unit 71's PASS67](spec/2026-10-26-spec-TOOL-dTotalRecall-81.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-82 — unit 71's `pass67` count is re-read at unit 67's verified pass commit, and the deviation record of unit 67 it decides is written once](spec/2026-10-26-spec-TOOL-dTotalRecall-82.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-14 — the level-0 project map: its renderer and gov map, derived from the one index, held to its budget without losing a node](spec/2026-10-26-spec-TOOL-dTotalRecall-14.md) | 23 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-15 — the map's three-way completeness check and the map leg pack](spec/2026-10-26-spec-TOOL-dTotalRecall-15.md) | 24 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-26 — the atlas under `help/atlas/`: generated Markdown and Mermaid pages from the one index's node table, refused when stale](spec/2026-10-26-spec-TOOL-dTotalRecall-26.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-12 — the acceptance re-measure: memory bytes per memory-reading agent over every read channel, passing only below 33 KB thirty days after landing](spec/2026-10-26-spec-TOOL-dTotalRecall-12.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-43 — the round-1 spec audit's 59 minors, batched](spec/2026-10-26-spec-TOOL-dTotalRecall-43.md) | 27 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-52 — the one legacy registration is keyed by path, section and check, absorbs its second population through a declared base re-key, and leaves no carrier of the old name](spec/2026-10-26-spec-TOOL-dTotalRecall-52.md) | 28 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-62 — unit 52 judges the merged legacy home at the run's real base and builds no `absorbs` read, so its own pass is green](spec/2026-10-26-spec-TOOL-dTotalRecall-62.md) | 28 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-53 — the round-1 spec audit of units 36 to 43: its 41 minors, batched](spec/2026-10-26-spec-TOOL-dTotalRecall-53.md) | 29 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-59 — the merged legacy registration is judged at the run's real compare base, a first seed, and the `absorbs` read that base can never feed is cut](spec/2026-10-26-spec-TOOL-dTotalRecall-59.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-55 — the cause census keeps the build folders' scripts by a path-keyed row held outside their bytes](spec/2026-10-26-spec-TOOL-dTotalRecall-55.md) | 30 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-56 — the alias census keeps the pinned departures instrument's `journal` compare by its path-keyed row, never by a marker in its bytes](spec/2026-10-26-spec-TOOL-dTotalRecall-56.md) | 30 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dTotalRecall-57 — a path-keyed keep row is admitted only for a file no pass may edit, so every editable file is kept by the one marker](spec/2026-10-26-spec-TOOL-dTotalRecall-57.md) | 30 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dTotalRecall-58 — the census keep marker is honoured only under the tool root, so no pass writes it into a pinned instrument](spec/2026-10-26-spec-TOOL-dTotalRecall-58.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-60 — the round-1 spec audit of units 44 to 53: its 35 minors, batched](spec/2026-10-26-spec-TOOL-dTotalRecall-60.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-65 — the census keep rows live in a project registry, so the memory-tree engine ships no path of this repository](spec/2026-10-26-spec-TOOL-dTotalRecall-65.md) | 31 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dTotalRecall-66 — the round-1 spec audit of units 54 to 60: its 40 minors, batched](spec/2026-10-26-spec-TOOL-dTotalRecall-66.md) | 32 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dTotalRecall-68 — the census keep registry is a `[[ledger]]` population read through the ledger factory, so a keep added later is refused `gained`](spec/2026-10-26-spec-TOOL-dTotalRecall-68.md) | 32 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-69 — the kickoff manifest's `last-audit` is re-stamped over unit 65's `.memory-tree.conf` edit, so the manifest ratchet is green from step 32](spec/2026-10-26-spec-TOOL-dTotalRecall-69.md) | 32 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-70 — the round-5 minors: each criterion that observed nothing is observed at the tip, and each gap it hid in units 61 to 66 is closed](spec/2026-10-26-spec-TOOL-dTotalRecall-70.md) | 33 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-73 — the census and its base compare read one registry path: the `census-kept-paths` registration re-rooted under the conf's memory root](spec/2026-10-26-spec-TOOL-dTotalRecall-73.md) | 33 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-75 — the kickoff manifest's `last-body-change` is advanced after §B is re-read, so manifest-check's C9 stall count is under ten from step 33](spec/2026-10-26-spec-TOOL-dTotalRecall-75.md) | 33 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-74 — unit 70's backticked strings are re-read at step 34 by a probe no shell quotes, and the departure unit 70's S3 owed for unit 59 is written](spec/2026-10-26-spec-TOOL-dTotalRecall-74.md) | 34 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-87 — the memory root `resolve_kept_registration` joins is resolved once, normalised to a repo-relative path, and refused when blank, absolute or leaving the tree](spec/2026-10-26-spec-TOOL-dTotalRecall-87.md) | 34 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-76 — the round-6 minors: each reading units 67 to 70 made by a broken probe or a stale rule is made again at the tip, and each gap it hid is closed](spec/2026-10-26-spec-TOOL-dTotalRecall-76.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-83 — unit 74's `s1-59` count is re-read at the verified parent of unit 59's pass, and the deviation record of unit 59 it decides is written once](spec/2026-10-26-spec-TOOL-dTotalRecall-83.md) | 35 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-84 — unit 74's `s1-46` count is re-read at the verified parent of unit 46's pass, and its S4 record of unit 70's reading is made from that count](spec/2026-10-26-spec-TOOL-dTotalRecall-84.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-77 — manifest-check is read at one commit by its exit status and its own failure line, never through a grep pipe, and the read is seen red on a staged C9 stall](spec/2026-10-26-spec-TOOL-dTotalRecall-77.md) | 36 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-78 — the S19 sweep visits every unit's pass commit by the driver's rule in a placed scratch worktree, and a commit it cannot resolve or check out is a printed red](spec/2026-10-26-spec-TOOL-dTotalRecall-78.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-79 — the ratchet leg's red spans are derived from the corrected sweep by a derivation seen to find a known red, and unit 76's AC13 certification is recorded against them](spec/2026-10-26-spec-TOOL-dTotalRecall-79.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-80 — unit 69's AC1 pair is answered by manifest-check's own C5 verdict at unit 69's pass commit and at its parent, replacing unit 76's S20 answer](spec/2026-10-26-spec-TOOL-dTotalRecall-80.md) | 36 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-85 — unit 76's S1 to S4 reads of units 55, 56 and 57 are made again at verified revisions, each count printed beside the sha it was read at](spec/2026-10-26-spec-TOOL-dTotalRecall-85.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-86 — unit 76's S5 and S6 reads of unit 70's table and unit 46's strings are made again at verified revisions, so an unresolved pass is a red and never a count](spec/2026-10-26-spec-TOOL-dTotalRecall-86.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-90 — units 82 to 84's S1 counts are read again with every line labelled and an unresolved pass printed red, and each decision they fed is made from its own line](spec/2026-10-26-spec-TOOL-dTotalRecall-90.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-88 — the round-7 minors: each reading of units 71 to 76 that observed nothing or two things is made once at the tip, and each gap it hid is closed](spec/2026-10-26-spec-TOOL-dTotalRecall-88.md) | 37 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dTotalRecall-91 — unit 69's AC1 is answered only from a read in which C5 ran, classified by the read's exit status and the checks that failed before it](spec/2026-10-26-spec-TOOL-dTotalRecall-91.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-93 — the write-once probe counts a deviation record under the unit its own file stem names, never under its Departs from address](spec/2026-10-26-spec-TOOL-dTotalRecall-93.md) | 37 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-94 — the write-once probe is seen to count the real records: a census over every unit holding one, seen red on unit 90's probe, and a fixture of the records' own shape](spec/2026-10-26-spec-TOOL-dTotalRecall-94.md) | 37 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-95 — a record of unit 59's absorbs departure carries one key, `pass(59)` with the string, whichever unit writes it, so every counter of it counts the same records](spec/2026-10-26-spec-TOOL-dTotalRecall-95.md) | 37 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-89 — unit 88's AC13 is answered on both arms of unit 83's decision, so no record of unit 59 is written or kept to satisfy a count the decision rules out](spec/2026-10-26-spec-TOOL-dTotalRecall-89.md) | 38 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-96 — unit 69's AC1 is answered again by a C5 classifier whose exit status must agree with the read's failure lines, so a read in which the checker never ran is never passed](spec/2026-10-26-spec-TOOL-dTotalRecall-96.md) | 38 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-97 — the C5 classifier's input is extracted from unit 80's ledger by a stated rule, and every read line it cannot place is counted](spec/2026-10-26-spec-TOOL-dTotalRecall-97.md) | 38 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-92 — the round-8 minors: each reading of units 77 to 88 that miscounted, misplaced or went unrecorded is made once at the tip, and each record it decides is written once](spec/2026-10-26-spec-TOOL-dTotalRecall-92.md) | 39 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dTotalRecall-98 — the restore lists every deleted record with rename detection off, so a record deleted beside a near-copy is put back](spec/2026-10-26-spec-TOOL-dTotalRecall-98.md) | 40 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-99 — the tip scan is graded only on a full read: it exits 0, counts the records it read against the folder, and its `by` lines sum to the live records](spec/2026-10-26-spec-TOOL-dTotalRecall-99.md) | 40 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dTotalRecall-100 — the round-9 minors: each reading of units 89 to 92 that a dropped line, a stale cite or a loose key could mislead is made once at the tip, and each record it decides is written once](spec/2026-10-26-spec-TOOL-dTotalRecall-100.md) | 41 | 2 | DEFERRED | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 58 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dTotalRecall-100 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99.

Ids whose spec moved past its audited revision: TOOL-dTotalRecall-1@rev-1 TOOL-dTotalRecall-10@rev-1 TOOL-dTotalRecall-11@rev-1 TOOL-dTotalRecall-12@rev-1 TOOL-dTotalRecall-13@rev-1 TOOL-dTotalRecall-14@rev-1 TOOL-dTotalRecall-16@rev-1 TOOL-dTotalRecall-17@rev-1 TOOL-dTotalRecall-18@rev-1
TOOL-dTotalRecall-19@rev-1 TOOL-dTotalRecall-2@rev-1 TOOL-dTotalRecall-20@rev-1 TOOL-dTotalRecall-21@rev-1 TOOL-dTotalRecall-22@rev-1 TOOL-dTotalRecall-23@rev-1 TOOL-dTotalRecall-25@rev-1 TOOL-dTotalRecall-26@rev-1 TOOL-dTotalRecall-3@rev-1 TOOL-dTotalRecall-36@rev-1 TOOL-dTotalRecall-37@rev-1
TOOL-dTotalRecall-38@rev-1 TOOL-dTotalRecall-39@rev-1 TOOL-dTotalRecall-4@rev-1 TOOL-dTotalRecall-40@rev-1 TOOL-dTotalRecall-41@rev-1 TOOL-dTotalRecall-42@rev-1 TOOL-dTotalRecall-43@rev-1 TOOL-dTotalRecall-44@rev-1 TOOL-dTotalRecall-45@rev-1 TOOL-dTotalRecall-46@rev-1 TOOL-dTotalRecall-47@rev-1
TOOL-dTotalRecall-48@rev-1 TOOL-dTotalRecall-49@rev-1 TOOL-dTotalRecall-5@rev-1 TOOL-dTotalRecall-50@rev-1 TOOL-dTotalRecall-51@rev-1 TOOL-dTotalRecall-52@rev-1 TOOL-dTotalRecall-53@rev-1 TOOL-dTotalRecall-54@rev-1 TOOL-dTotalRecall-55@rev-1 TOOL-dTotalRecall-56@rev-1 TOOL-dTotalRecall-57@rev-1
TOOL-dTotalRecall-58@rev-1 TOOL-dTotalRecall-59@rev-1 TOOL-dTotalRecall-6@rev-1 TOOL-dTotalRecall-60@rev-1 TOOL-dTotalRecall-61@rev-1 TOOL-dTotalRecall-62@rev-1 TOOL-dTotalRecall-63@rev-1 TOOL-dTotalRecall-64@rev-1 TOOL-dTotalRecall-65@rev-1 TOOL-dTotalRecall-66@rev-1 TOOL-dTotalRecall-67@rev-1
TOOL-dTotalRecall-68@rev-1 TOOL-dTotalRecall-69@rev-1 TOOL-dTotalRecall-7@rev-1 TOOL-dTotalRecall-70@rev-1 TOOL-dTotalRecall-71@rev-1 TOOL-dTotalRecall-72@rev-1 TOOL-dTotalRecall-73@rev-1 TOOL-dTotalRecall-74@rev-1 TOOL-dTotalRecall-75@rev-1 TOOL-dTotalRecall-76@rev-1 TOOL-dTotalRecall-77@rev-1
TOOL-dTotalRecall-78@rev-1 TOOL-dTotalRecall-79@rev-1 TOOL-dTotalRecall-8@rev-1 TOOL-dTotalRecall-80@rev-1 TOOL-dTotalRecall-81@rev-1 TOOL-dTotalRecall-82@rev-1 TOOL-dTotalRecall-83@rev-1 TOOL-dTotalRecall-84@rev-1 TOOL-dTotalRecall-85@rev-1 TOOL-dTotalRecall-86@rev-1 TOOL-dTotalRecall-87@rev-1
TOOL-dTotalRecall-88@rev-1 TOOL-dTotalRecall-89@rev-1 TOOL-dTotalRecall-9@rev-1 TOOL-dTotalRecall-90@rev-1 TOOL-dTotalRecall-91@rev-1 TOOL-dTotalRecall-92@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dTotalRecall's 26 clause(s) and 36 owned node(s), over 91 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 26
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-26-spec-TOOL-dTotalRecall-100.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-49.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-53.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-55.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-57.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-59.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-61.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-63.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-64.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-65.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-66.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-67.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-68.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-69.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-70.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-71.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-72.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-73.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-74.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-75.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-76.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-77.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-78.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-79.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-80.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-81.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-82.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-83.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-84.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-85.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-86.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-87.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-88.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-89.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-90.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-91.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-92.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-93.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-94.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-95.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-96.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-97.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dTotalRecall-98.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dTotalRecall-99.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0221, cl-dClosedLoop-0222, cl-dClosedLoop-0232, cl-dClosedLoop-0233, cl-dClosedLoop-0236
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTotalRecall-1` | no |
| 2 | `TOOL-dTotalRecall-13` | no |
| 3 | `TOOL-dTotalRecall-8` | no |
| 4 | `TOOL-dTotalRecall-18`, `TOOL-dTotalRecall-37` | yes |
| 5 | `TOOL-dTotalRecall-16` | no |
| 6 | `TOOL-dTotalRecall-25` | no |
| 7 | `TOOL-dTotalRecall-5` | no |
| 8 | `TOOL-dTotalRecall-38`, `TOOL-dTotalRecall-4`, `TOOL-dTotalRecall-54` | no |
| 9 | `TOOL-dTotalRecall-40`, `TOOL-dTotalRecall-44`, `TOOL-dTotalRecall-45`, `TOOL-dTotalRecall-46`, `TOOL-dTotalRecall-6`, `TOOL-dTotalRecall-63`, `TOOL-dTotalRecall-64` | no |
| 10 | `TOOL-dTotalRecall-22` | no |
| 11 | `TOOL-dTotalRecall-3` | no |
| 12 | `TOOL-dTotalRecall-2` | no |
| 13 | `TOOL-dTotalRecall-7` | no |
| 14 | `TOOL-dTotalRecall-11`, `TOOL-dTotalRecall-41` | no |
| 15 | `TOOL-dTotalRecall-10`, `TOOL-dTotalRecall-42` | yes |
| 16 | `TOOL-dTotalRecall-19` | no |
| 17 | `TOOL-dTotalRecall-21`, `TOOL-dTotalRecall-36`, `TOOL-dTotalRecall-39` | no |
| 18 | `TOOL-dTotalRecall-47`, `TOOL-dTotalRecall-48`, `TOOL-dTotalRecall-49`, `TOOL-dTotalRecall-50`, `TOOL-dTotalRecall-51`, `TOOL-dTotalRecall-9` | no |
| 19 | `TOOL-dTotalRecall-23`, `TOOL-dTotalRecall-61` | yes |
| 20 | `TOOL-dTotalRecall-24`, `TOOL-dTotalRecall-67` | yes |
| 21 | `TOOL-dTotalRecall-20`, `TOOL-dTotalRecall-71`, `TOOL-dTotalRecall-72` | no |
| 22 | `TOOL-dTotalRecall-17`, `TOOL-dTotalRecall-81`, `TOOL-dTotalRecall-82` | no |
| 23 | `TOOL-dTotalRecall-14` | no |
| 24 | `TOOL-dTotalRecall-15` | no |
| 25 | `TOOL-dTotalRecall-26` | no |
| 26 | `TOOL-dTotalRecall-12` | no |
| 27 | `TOOL-dTotalRecall-43` | no |
| 28 | `TOOL-dTotalRecall-52`, `TOOL-dTotalRecall-62` | no |
| 29 | `TOOL-dTotalRecall-53`, `TOOL-dTotalRecall-59` | no |
| 30 | `TOOL-dTotalRecall-55`, `TOOL-dTotalRecall-56`, `TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-58` | no |
| 31 | `TOOL-dTotalRecall-60`, `TOOL-dTotalRecall-65` | no |
| 32 | `TOOL-dTotalRecall-66`, `TOOL-dTotalRecall-68`, `TOOL-dTotalRecall-69` | no |
| 33 | `TOOL-dTotalRecall-70`, `TOOL-dTotalRecall-73`, `TOOL-dTotalRecall-75` | no |
| 34 | `TOOL-dTotalRecall-74`, `TOOL-dTotalRecall-87` | yes |
| 35 | `TOOL-dTotalRecall-76`, `TOOL-dTotalRecall-83`, `TOOL-dTotalRecall-84` | no |
| 36 | `TOOL-dTotalRecall-77`, `TOOL-dTotalRecall-78`, `TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-80`, `TOOL-dTotalRecall-85`, `TOOL-dTotalRecall-86`, `TOOL-dTotalRecall-90` | no |
| 37 | `TOOL-dTotalRecall-88`, `TOOL-dTotalRecall-91`, `TOOL-dTotalRecall-93`, `TOOL-dTotalRecall-94`, `TOOL-dTotalRecall-95` | no |
| 38 | `TOOL-dTotalRecall-89`, `TOOL-dTotalRecall-96`, `TOOL-dTotalRecall-97` | no |
| 39 | `TOOL-dTotalRecall-92` | no |
| 40 | `TOOL-dTotalRecall-98`, `TOOL-dTotalRecall-99` | no |
| 41 | `TOOL-dTotalRecall-100` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dRankedPlan](../dRankedPlan/README.md), [dShippedRelease](../dShippedRelease/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->

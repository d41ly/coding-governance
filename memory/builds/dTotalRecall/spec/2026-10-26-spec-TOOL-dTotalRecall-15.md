# TOOL-dTotalRecall-15 — the map's three-way completeness check and the map leg pack

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 24 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0226@0bd15de1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-17 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Prove the level-0 map complete and true, three ways. Every part on disk is a node in the index,
every node in the index is on the map as a line or inside a count, and every line resolves to a
node. The map's other checks of the project map's `[checks]` table that this build owns run beside
it, as the `map` leg pack, so a map that loses a node, invents a relation or grows a date reds the
bar.

## 2. Scope (IN)

The disk join is `compute_coverage` with its `Coverage` class, moved by PLAY-dOrderedCharter-19 S9 to
`tools/lib/coverage_join.py` and shipped inline in `tools/memory-tree/coverage_join.py`. The leg key
`pack` is PLAY-dOrderedCharter-19 S12's. The index and its registry are that spec's S2 and S4. All
are DEFERRED at base `462d20f3`. The map is unit 14's `gov_map.py`.

- **S1** — The checker, `tools/memory-tree/map_checks.py`. `python map_checks.py` runs every check
  of S2 to S10 over the tree and prints one `map: <check> <finding>` line per finding, then a summary
  `map: checks <n> · findings <n> · census <n> · unarmed <ns>,…`, the counts DERIVED at the run. It
  exits 1 on any finding, 0 otherwise, and 2 when the index or the map cannot be read. Observed by
  AC1 and AC11.
- **S2** — `complete`, three ways. (a) Disk to index: `compute_coverage` over inventories from the
  disk census (S3), with the index's node keys as the one owner's claims and no baseline. An
  `unclaimed` key is a part on disk with no node, and a `stale_claims` key is a node with no part on
  disk. (b) Index to map: every node is on a level-0 line or inside its namespace's `nsline` count.
  (c) Map to index: every line's key is a node. Observed by AC1, AC2 and AC3.
- **S3** — The disk census, `CENSUS` in `map_checks.py`: one route per namespace with a population
  on disk, each sharing nothing with the extractor that writes that namespace's rows, as the design
  instrument's `census` does (`2026-10-17-build-PLAY-dClosedLoop-1-map.py:510`). The routes are: kits,
  the directories directly under the tool root; legs, the names in `tools/gate-legs.json`; bug classes,
  the gotchas whose front matter says `kind: class`; record kinds, the rows of unit 1's
  `record-kinds.toml`; policy keys, the `[[key]]` rows of `tools/policy/catalogue.toml`; tag
  namespaces, the rows of `tools/playbook/namespaces.toml`; builds, each `memory/builds/*/README.md`.
  A registered namespace with no route is counted under `census` in the summary and named, never read
  as complete. Observed by AC2.
- **S4** — `resolves`: a line naming a node the index lacks, or a relation key whose target is no
  node. Observed by AC4.
- **S5** — `count`: an `nsline` whose count differs from the index's node count for that namespace.
  Observed by AC5.
- **S6** — `owner`: a node of a namespace a build must build (an item, a policy key, a point, a record
  kind, a tag namespace or a system) with no declared owner, or with two (PM-8). Observed by AC6.
- **S7** — `extractor`: a registered namespace whose row names no `extractor`. Observed by AC7.
- **S8** — `no inference`: a relation the map renders that no declared edge row of the index backs.
  Observed by AC8.
- **S9** — `budget`: under `memory.map-overflow` `refuse`, a map over `memory.map-budget` that
  `gov_map.py` printed; under `degrade`, a degraded render whose header's `degraded` field omits a
  step `fit_map` took. `no stale facts`: a line holding a date or a status token of
  `tree_lib.STATUS_TOKENS`. Observed by AC9.
- **S10** — `populated`: a registered namespace with no node in the index is named in the summary's
  `unarmed` field and is never counted green. Observed by AC10.
- **S11** — The pack. Two legs in `tools/gate-legs.json` carry `"pack": "map"`:
  `map (the project map's checks)`, argv `python3 {prefix}/memory-tree/map_checks.py`, and
  `map selftest`, argv `python3 {prefix}/memory-tree/map_checks.py --selftest`, which runs every
  plant of S12 and `gov_map.py --selftest`. Each has its `[[gate_leg]]` row in
  `tools/memory-tree/kit.toml`, a guard naming both modules and `tools/playbook/namespaces.toml`, a
  ceiling from a measured run in `tools/run-gates/ceiling-evidence.txt`, and its name covered by a
  dossier. Observed by AC11.
- **S12** — The plants, `map_checks.py --fixture --plant <case>`, each a scratch repository with a
  built index and a rendered map: `newkit`, `unlisted-node`, `ghost-line`, `ghost-rel`, `count-off`,
  `ownerless`, `two-owners`, `no-extractor`, `default-owner`, `refuse-over`, `degrade-unnamed`,
  `dated-line`, `status-line` and `unpopulated`. Observed by AC2 to AC10.

## 3. Non-goals (OUT)

- The renderer, the budget's fit and the cache: unit 14's. This unit re-reads what they print.
- The `purpose` check under `memory.map-purpose`: unit 16's.
- The `freshness` and `delivery` checks, which grade a work order's `map` slot: dBoundRoles'.
- The `render parity` check between the map and the atlas: unit 26's parity arm.
- The codebase map's own two-way coverage legs (`tools/gate-legs.json`'s codebase-map rows), which
  stay as they are.

### Edges

- **consumes-from** `TOOL-dTotalRecall-14` — `gov_map.py`, the rendered lines, header and `--fixture` plants every check reads; without it there is no map to check

## 4. Design

### The three joins

```
disk  --compute_coverage-->  index nodes   unclaimed: on disk, no node   stale_claims: node, not on disk
index --every node-------->  map           a line, or inside its nsline count
map   --every line-------->  index         its key is a node
```

`compute_coverage(inventories, owners, baseline)` (`tools/codebase-map/map_lib.py:1404` at base, moved
by PLAY-dOrderedCharter-19 S9) takes `inventories` as `{ns: [disk keys]}`, `owners` as
`{"index": {ns: (node keys)}}` and `baseline` as `{}`. Its four asserts reduce to the two this check
needs, since an empty baseline makes the other two vacuous. Those two are named in the summary, not
counted as passes.

### Inventory

Minted: `tools/memory-tree/map_checks.py` with `CENSUS`, `check_complete`, `check_resolves`,
`check_count`, `check_owner`, `check_extractor`, `check_no_inference`, `check_budget`,
`check_no_stale_facts`, `check_populated`, `build_checks_fixture`; the legs
`map (the project map's checks)` and `map selftest`; the pack value `map`. Naming cells: each
`check_*` is asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None.

### Rollout

Live on landing. The `map` leg is red on gov's own tree until every finding the first run prints is
fixed in the same pass, since a leg seen only red at its landing cannot land.

### Files touched (estimate)

- `tools/memory-tree/map_checks.py` (new)
- `tools/gate-legs.json`: the two legs
- `tools/memory-tree/kit.toml`: two `[[gate_leg]]` rows and a `[[files]]` rule
- `tools/run-gates/ceiling-evidence.txt`: the two legs' measured maxima
- `tools/govkit/subject-pins.tsv`: regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `memory/map/features/project-map.md`: unit 14's dossier, extended to cover the checker and the two
  leg names

### Alternatives rejected

- **The checks inside the hygiene leg.** A check inside an existing leg is cheaper
  (`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`), but the clause names a `map`
  leg pack, which needs legs carrying the key.
- **Census through the extractors.** A census read through the code that writes the index can only
  agree with it; the instrument's rule is a route that shares nothing with the builder.
- **A second coverage join.** `compute_coverage` already holds both directions, and
  PLAY-dOrderedCharter-19 moved it to the core for this reason.

## 5. Production-readiness checklist

- security — read-only over the tree, the index and the map; writes nothing.
- perf / scale — one index read, one render (cached by unit 14), one pass per census route; the
  ceiling is measured at the pass.
- error / empty / loading states — an unreadable index or map exits 2 naming it; an empty
  namespace is `unarmed`, a namespace with no census route is counted under `census`, and neither
  reads as green.
- observability — one line per finding and the summary's derived counts.
- risks — a census route that drifts from its namespace's real population reds as `stale_claims`,
  which is the check working.
- testing — AC1 to AC11 by a pass; the arms of §7 at the close.
- migration — none.
- user docs — `help/project-map.md` (unit 14's) gains a paragraph naming the `map` pack and its
  checks.

## 6. Acceptance criteria

- **AC1** — When `python map_checks.py` runs on gov's tree at the pass tip, it exits 0 and its
  summary names every check of S2 to S10.
  Red when: a check is skipped silently, or the run passes with no index read.
- **AC2** — When `python map_checks.py --fixture --plant newkit` runs, a planted `tools/newkit/`
  with no kit node, it exits 1 with a `complete` line naming `newkit` as unclaimed.
  Red when: the census reads kits through the index, so the planted directory is never seen.
- **AC3** — When `--plant unlisted-node` (an index node on no line and in no count) and
  `--plant ghost-line` (a line naming `feature.ghost`) run, each exits 1 with a `complete` line
  naming the node.
  Red when: either direction of the index-to-map join is not read.
- **AC4** — When `--plant ghost-rel` runs, a relation key whose target is no node, it exits 1 with
  a `resolves` line.
  Red when: a relation's targets are not resolved.
- **AC5** — When `--plant count-off` runs, an extractor that drops one row so a counted line is one
  off, it exits 1 with a `count` line naming the namespace.
  Red when: a counted line is not compared with the index.
- **AC6** — When `--plant ownerless` (an item whose owner field is emptied) and `--plant two-owners`
  run, each exits 1 with an `owner` line.
  Red when: a node a build must build passes with no owner or two.
- **AC7** — When `--plant no-extractor` runs, `doc` registered with no extractor, it exits 1 with an
  `extractor` line.
  Red when: a namespace row with no extractor passes.
- **AC8** — When `--plant default-owner` runs, a namespace whose owner the render took from a
  default, it exits 1 with a `no inference` line.
  Red when: a relation no edge row declares passes.
- **AC9** — When `--plant refuse-over` and `--plant degrade-unnamed` run, each exits 1 with a
  `budget` line; when `--plant dated-line` and `--plant status-line` run, each exits 1 with a
  `no stale facts` line.
  Red when: an over-budget map under `refuse`, an unnamed degrade step, a date or a status token
  passes.
- **AC10** — When `--plant unpopulated` runs, one registered namespace with no node, it exits 0 and
  the summary's `unarmed` field names it.
  Red when: an empty namespace is counted as a passing check.
- **AC11** — When `python -c "import json,sys; print([l['name'] for l in json.load(open(sys.argv[1])) if l.get('pack') == 'map'])" tools/gate-legs.json`
  runs at the pass tip, it prints the two leg names; and when each leg's argv is run by hand, the
  first exits 0 on gov's tree and the second prints every plant's name with its exit.
  Red when: a leg lacks the key, or the selftest leg runs no plant.

## 7. Gates

`memory hygiene` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `testsuite counts (every bar self-test prints one)` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/memory-tree/map_checks.py · covers AC1 · the leg `map (the project map's checks)` over the tree, staged by a planted `tools/newkit/` directory · none
New arm: tools/memory-tree/map_checks.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · the leg `map selftest` runs every plant of S12 and `gov_map.py --selftest`, staged by `check_count` returning no finding · the testsuite-counts floor, raised by the new suite

## 8. Open questions

- **F1 — Which `[checks]` rows does this unit's pack carry?** The table has thirteen. Options: (a)
  the rows this build owns and nothing outside the map (S2 to S10), with purpose, freshness, delivery
  and render parity left to their owners; (b) all thirteen. (b) grades a work-order slot dBoundRoles
  has not built and duplicates units 16 and 26's checks. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the project map's `[owners]` table (project-map.md:711-722). widens: none · relaxes:
  none
- **F2 — Where do the disk routes come from?** Options: (a) one route per namespace in `CENSUS`,
  read from the files that hold each population; (b) the namespace row's `source` field, which is
  prose (PLAY-dOrderedCharter-19 S2). (b) cannot be executed. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, a namespace without a route announced in the summary. widens: none ·
  relaxes: none
- **F3 — A new leg or a check inside an existing leg?** The clause names a `map` leg pack.
  RESOLVED (agent, 2026-10-26, delegated): two new legs carrying `"pack": "map"`, rung 1. widens:
  none · relaxes: none
- **F4 — The join factory's move, the `pack` key, the index and unit 14's renderer are unbuilt at
  base `462d20f3`.** RESOLVED (agent, 2026-10-26, delegated): this spec calls them as their specs name
  them, and the build run re-grounds on the landed code, rung 1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 15, the brief's I11, I12 and I19,
  scout C's row for cl-0226, and the project map's `[checks]` and `[owners]`.

## 10. Reuse audit

The seams extended are `compute_coverage` (`tools/codebase-map/map_lib.py:1404`, `Coverage` at
`:1391`, moved to the core by PLAY-dOrderedCharter-19 S9) for the disk join, the design instrument's
`census` and `check` (`2026-10-17-build-PLAY-dClosedLoop-1-map.py:510`, `:633`) for the checks and
their planted cases, and PLAY-dOrderedCharter-19 S12's `pack` key for the legs. `python
tools/codebase-map/reuse_lookup.py "join inventory coverage between index map and disk census"`
ranked `census` (`tools/memory-tree/merge-rows.py`), `inventory_ids`, `compute_coverage` (SEAM, fan-in
4) and `build_reference_index`. `compute_coverage` is the join extended, and the others count rows or
claims for their own kits. Scout C cited the kits inventory `_tool_kits` at
`tools/codebase-map/map_extractors.py:200`; at `462d20f3` it is at `:85`, and `:175` is `_gate_legs`.
The run-gates canary's known-key set is at `tools/run-gates/run-gates.test.sh:244`, as the scout
said, and PLAY-dOrderedCharter-19 S12 adds `pack` to it.

Recall terms used: `python tools/memory-recall/query.py "how is the project map checked complete against the index and the disk" --terms "three-way completeness index map disk compute_coverage census pack map leg checks planted reds"`

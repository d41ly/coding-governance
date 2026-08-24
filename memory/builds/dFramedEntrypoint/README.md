---
slug: dFramedEntrypoint
node: d
opened: 2026-08-24
streams: tooling
roster: TOOL
ids: TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8
---

# dFramedEntrypoint — the build README becomes a closed, budgeted authored slot set

## The problem this build exists to solve

A build README is the entrypoint a resuming session reads first, and its authored half is unbounded:
the slot contract shipped before this build constrains only WHERE authored content sits, never WHAT
it is. Measured across the 61 tracked build READMEs at this build's base, the authored half was
347,503 B against 200,270 B generated, and what filled it was owner-decision logs, fork rulings,
research digests, spec-audit narratives, defect records and hand-authored rosters — content that
belongs to a unit, not to the entrypoint. This build gives the authored half a closed, budgeted,
machine-graded slot set, derived wherever the data already exists and authored only where it cannot
be.

## Expected improvements

- A resuming session reads a fixed five-slot shape instead of whatever the last author wrote, and a
  gate refuses anything else once a README is declared bound.
- Records stop being listed twice at the entrypoint and render inside the spec they serve, where a
  reader is already looking.
- Build order is authored on the specs and computed here, so the roster and the order region cannot
  disagree with each other or with the specs.

## Detriments if this is not built

- The entrypoint keeps growing without bound, and the classes the owner objected to keep arriving
  because nothing refuses them.
- The only spec-to-record coverage signal in the repo stays buried under a duplicate listing that no
  gate reads and no reader needs.
- The build-order verb stays shipped and unadopted, so ordering keeps being hand-authored in prose
  that the specs then contradict.

## Build-level rules

- Every unit that moves `tools/memory-tree/gen_build_index.py` bumps `KIT_MEMORY_TREE_VERSION` across
  the DERIVED carrier set — `git grep -l 'gov:kit memory-tree@'` outside `memory/builds/` and
  `memory/archive/`, plus the engine constant — never the set the epoch gate's remedy text names,
  which resolves to five carriers where seven exist.
- Units land SEQUENTIALLY. Five of the eight write the same engine file, so their write sets
  intersect and M6's disjointness proof fails; declaring them parallel would be a claim the paths
  contradict.
- A unit that grows a capped read-path member prices its OWN charge against `READ_PATH_CEILING`. Two
  units charged that budget here and each raised it for itself.

## Parked decisions

Four, all on the run-state file with their options and the reason each was refused: whether the
authored `roster:units` pair becomes mandatory or its three readers are deleted together; that
`memory/guides/BUILD-METHOD.md` was already over its own line budget at this build's base with no
gate watching; that `--status` and `--plan` now disagree about which unit is next; and that the
lexicon naming leg is red at the base with its guard hiding it. None is this build's to decide.

<!-- gen:build-index -->
**Build status:** CLOSED · 8 unit(s) · node d · opened 2026-08-24 · streams tooling
ids TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFramedEntrypoint-8 — the superseding decision, and the three records that assert what is not true](spec/2026-08-24-spec-dFramedEntrypoint-8.md) | 1 | 1 | CLOSED | rev-5 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-1 — the build README's authored half becomes a closed heading canon](spec/2026-08-24-spec-dFramedEntrypoint-1.md) | 2 | 2 | CLOSED | rev-6 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-4 — the build-order verb becomes legal and hardened, and the roster renders order and tier](spec/2026-08-24-spec-dFramedEntrypoint-4.md) | 3 | 2 | CLOSED | rev-7 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-2 — per-slot budgets: a hard declared ceiling and an advisory high-water](spec/2026-08-24-spec-dFramedEntrypoint-2.md) | 4 | 2 | CLOSED | rev-6 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-3 — the declared registry that says which build READMEs the contract binds](spec/2026-08-24-spec-dFramedEntrypoint-3.md) | 5 | 2 | CLOSED | rev-6 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-5 — the document inventory and the records table leave the build README](spec/2026-08-24-spec-dFramedEntrypoint-5.md) | 6 | 2 | CLOSED | rev-6 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-6 — every record renders inside the spec it serves](spec/2026-08-24-spec-dFramedEntrypoint-6.md) | 7 | 2 | CLOSED | rev-5 | 2026-08-24 |
| [TOOL-dFramedEntrypoint-7 — the conformance pass that seeds the registry with a real population](spec/2026-08-24-spec-dFramedEntrypoint-7.md) | 8 | 2 | CLOSED | rev-4 | 2026-08-24 |
<!-- /gen:build-units -->

Records: 21 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dFramedEntrypoint-8` | no |
| 2 | `TOOL-dFramedEntrypoint-1` | no |
| 3 | `TOOL-dFramedEntrypoint-4` | no |
| 4 | `TOOL-dFramedEntrypoint-2` | no |
| 5 | `TOOL-dFramedEntrypoint-3` | no |
| 6 | `TOOL-dFramedEntrypoint-5` | no |
| 7 | `TOOL-dFramedEntrypoint-6` | no |
| 8 | `TOOL-dFramedEntrypoint-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
# TOOL-dTrueNorth-24 — a rescope row in a rotated RUN archive is dated by the commit that wrote it

**Status:** OPEN · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-22-build-TOOL-dTrueNorth-24-deviation-23.md](../build/2026-10-22-build-TOOL-dTrueNorth-24-deviation-23.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-24-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-24-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md) | research | TOOL-dTrueNorth-23 TOOL-dTrueNorth-25 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`)
confirmed **finding 4 at HIGH**, its item **H2**. The deviation join's rescope arm dates each row
with `read_row_commit(root, row, rel)`, `rel` being the one RUN file the row sits in
(`tools/memory-tree/deviation_join.py:595`). `RUN_FILE` also matches the rotated
`RUN.<phase>.<blob8>.md` archives, and for an archive that per-file pickaxe answers the commit that
rotated the file. `read_rev_at` then reads the unit's header revision at that later commit, so the
address `<unit>@rev-N` misses the record the spec run wrote and reads as recorded by nobody, and the
commit join judges against a tree that already holds the record, so a late record reads as on time.
The instrument this arm ports searches the build folder
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:378-380`), and
`TOOL-dTrueNorth-4` S4 reads rescope rows as the instrument does. This unit takes the review's fix,
which the skeptic judged sound, and leaves a plant for the class. It repairs `TOOL-dTrueNorth-4`.

## 2. Scope (IN)

- **S1** — The rescope arm of `read_population` (`tools/memory-tree/deviation_join.py:587-595`)
  passes `read_row_commit` the build folder, `<MEMORY_ROOT>/builds/<build>`, as the instrument's
  `scan_rescope_members` does
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:383-404`).
  The oldest commit whose diff changes the row's count anywhere in that folder is the one that
  wrote it into `RUN.md`, so a row dates the same whether it is read from the live file or from an
  archive. Both members the arm makes take that sha: an `add` member's, which the commit join reads,
  and every other row's member, which `read_rev_at` reads the address at.
  `read_row_commit`'s docstring states which `path` each caller passes and why. Observed by AC1,
  AC2 and AC3.
- **S2** — A `rotated` plant joins `PLANTS`, exit 0 under `report` and `refuse`. It writes its
  unit's spec at rev-1, then a `supersede` rescope row naming a successor unit, in the commit that
  also writes the row's joining record, departing from `<unit>@rev-1 [scope]`, then the spec at
  rev-2. Last, one commit moves `RUN.md`'s bytes to `RUN.LANDED.<eight hex>.md` beside a fresh
  `RUN.md` holding none of the old rows, and the fixture's row list is reset, as the driver's
  rotation leaves it. The plant keeps the row commit's mark and the rotation commit's mark in `fx.marked`. Its own arm
  asserts that the plant's member carries the row commit's sha and the address `<unit>@rev-1`, and
  that no member read from the archive, the base's supersede and add rows included, carries the
  rotation commit's sha. The composed run of every plant holds with it. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The ledger arm's `read_row_commit(root, ln, rel)` (`tools/memory-tree/deviation_join.py:584`).
  A journal record is never rotated, and two ledgers in one build folder can hold one ledger line's
  text, so a folder pickaxe there would date a line by another record's commit. The per-file read is
  right for it, and S1's docstring says so.
- Reading the RUN files from `git ls-files` rather than the working tree. The review's M6 moves
  `read_population`'s spec and record lists onto the index; that is `TOOL-dTrueNorth-26`'s.
- One batched pickaxe for every row of a folder. Each row keeps its one spawn, as today (§5).
- The instrument `deviations.py`, a frozen record of the dClosedLoop build.

### Edges

- **consumes-from** external — TOOL-dTrueNorth-4, CLOSED, so read as built rather than as an edge: the rescope arm and `read_row_commit`, which S1 re-scopes; without them there is no row to date
- **consumes-from** external — TOOL-dTrueNorth-12, CLOSED, so read as built rather than as an edge: the fixture's plant table, its role map and the composed run, which S2's plant joins
- **hands-off** `TOOL-dTrueNorth-26` — the deviation join's population reads, its fixture and its report arms, which that unit's M6, M8, L6 and L7 change after this unit lands in the same file

## 4. Design

### Evidence

Measured 2026-10-22 at `6f5f4ddec`, PINNED.

- Line 99 of `memory/builds/aRepatriatedFork/RUN.LANDED.79a3a1b5.md`, a rescope add row: the
  per-file pickaxe over the archive answers `a73fe3387`, the preflight rotation, and the folder
  pickaxe over `memory/builds/aRepatriatedFork` answers `a25844711`, the adopting commit. This
  reproduces the review's split.
- dTrueNorth is a chain build, and its live `RUN.md` holds 17 rescope rows that are not `defer`,
  the four adds of units 23 to 26 among them. No chain-build archive holds one yet, so the first
  wrong date arrives at the next rotation, dTrueNorth's own landing included.
- One folder pickaxe over `memory/builds/dTrueNorth` took 0.29 s, against 0.09 s for the same row
  over `RUN.md` alone.
- `Fixture.write_commit` takes `None` to delete a path, and `add_run_row` renders `RUN.md` from
  `self.rows` (`tools/memory-tree/deviation_join.py:842-875`, `:945-952`), so the plant needs no new
  fixture machinery.
- With no first pass and no audit pin, the plant's rev-2 revision is no member of either revision
  arm, so the plant adds exactly one member, its rescope row.

### Why the plant reds against the base

At base the plant's supersede row, read from the archive, dates by the rotation commit. Its unit's
header there is rev-2, so the member's address is `<unit>@rev-2`, no record departs from it, and
`--policy refuse` exits 1 with that member recorded by nobody. `PLANT_EXITS` holds the plant at 0,
so the existing refuse arm reds, and the plant's own sha assertion reds beside it. The base's
supersede and add rows also move into the archive. At base their shas become the rotation commit's
too, which the sha half catches even where an address would not move.

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`

### Rollout

The edit is under the kit's directory, a build-index input, so check 9 renders under `--staged`.
The pass runs `gen_build_index.py --write` before its commit and stages whatever it re-renders. The
`KIT_MEMORY_TREE_VERSION` bump is minted by `push-main.sh`.

### Alternatives rejected

- **The folder's `RUN.md` path alone.** It finds the same commit for every row the driver writes,
  in about a third of the time, but it is not the reading `TOOL-dTrueNorth-4` S4 binds the arm to,
  and a folder ever moved between build paths would lose the row's history either way.
- **The per-file read with `--follow`.** It follows the archive back only while git pairs the
  rotation as a rename, which is a similarity heuristic. It did pair the aRepatriatedFork archive
  with its `RUN.md` (measured), but a heuristic is not a contract a join should rest on, and it also
  departs from the instrument's reading.

## 5. Production-readiness checklist

- security — no new surface: the same read-only `git log -S` per row, over a wider pathspec.
- perf / scale — each row keeps one spawn, and a folder pickaxe walks every commit touching the
  build folder: about 0.2 s more per row, 17 rows today in dTrueNorth (§4 Evidence).
- error / empty / loading states — a row no commit holds still dates as None, which `read_rev_at`
  reads as `rev-?`, as today.
- observability — the member's `what` keeps naming the file it was read from, the archive included.
- risks — a row's exact text appearing earlier in another file of its folder would date by that
  file's commit; a row opens with its own UTC timestamp, and the driver writes it into `RUN.md`
  before any record can quote it.
- testing — AC1 to AC3; the plant and its arm under §7, observed red at the close against the base.
- migration — none.
- user docs — `read_row_commit`'s docstring and the module docstring's rescope bullet; no page
  under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant rotated --policy refuse`
  runs, it exits 0 and prints no line holding `recorded by nobody`.
  Red when: the arm dates the plant's supersede row by the rotation commit, so its address reads
  `@rev-2` and the run exits 1 naming that member recorded by nobody.
- **AC2** — When a probe calls `deviation_join.build_fixture` with the `rotated` plant and then
  `deviation_join.measure_fixture` in-process, the plant unit's `rescope` member carries the sha of
  the row commit's mark in `fx.marked` and the address `<unit>@rev-1`, and no member read from the
  archive carries the sha of the rotation commit's mark.
  Red when: any member read from the archive carries the rotation commit's sha.
- **AC3** — When a probe calls `deviation_join.read_row_commit` at this repo's root with line 99 of
  `memory/builds/aRepatriatedFork/RUN.LANDED.79a3a1b5.md` as the row, it answers a sha opening
  `a25844711` for the folder `memory/builds/aRepatriatedFork` and one opening `a73fe3387` for the
  archive's own path.
  Red when: the two answers agree, so the probe no longer separates the folder read from the
  per-file read and AC2 is the only witness.
  figure: PINNED, both shas measured 2026-10-22; history below them does not move.

## 7. Gates

`routed-commits selftest` · `memory hygiene` · `build-index selftest` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/deviation_join.py (the plant arms the routed-commits selftest runs) · covers AC1 AC2 · the rotated plant, whose supersede row and the base's rows move into an archive after the spec is revised, staged against the per-file pickaxe · none

## 8. Open questions

- **F1 — Which binding line does a unit the closing review promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it
  adds (ER:320). (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds
  `unbound` and (c) reds `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F2 — Which pathspec dates a row?** (a) The build folder, the review's fix and the instrument's
  reading. (b) The folder's `RUN.md` path alone, about three times faster. (c) Every RUN path the
  folder holds. (b) and (c) depart from `TOOL-dTrueNorth-4` S4's "as `deviations.py` reads them",
  the bound this arm was built to, so veto 1 holds against both; (a) passes every veto.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-22, delegated): (a). widens: none ·
  relaxes: none
- **F3 — Does the build's grant lift veto 2 for the join's edit here?** `cl-dClosedLoop-0004` names
  the deviation record and its join, and this unit corrects the departing commit that join reads.
  RESOLVED (agent, 2026-10-22, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the deviation join's rescope arm and its fixture plant, cl-dClosedLoop-0004 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, promoted from the closing diff review's finding 4 (HIGH,
  item H2).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "find the commit that first wrote a row into a
renamed run file"` ranked `rows`, `row`, `run`, `build_commit` and `run_git` by name stem, none a
row-dating reader. The seam this unit extends is `deviation_join.read_row_commit`
(`tools/memory-tree/deviation_join.py:316-319`), unchanged, whose rescope caller takes the
instrument's argument, `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:378-380`.
The plant extends the join's own fixture, `Fixture` and `add_plant`
(`tools/memory-tree/deviation_join.py:822`, `:1011`). The probe surfaced none of them; they were
found by reading the finding and the source. The recall query returned the review's H2 and dTrueNorth's
own rescope rows in `RUN.md`, which is how §4 learned this build's landing is the next rotation; it
returned no earlier record of the defect.

Recall terms used: `python tools/memory-recall/query.py "which commit wrote a rescope row once RUN.md
is rotated to an archive" --terms "rescope row pickaxe read_row_commit RUN.LANDED rotated archive
rotation commit build folder deviations.py preflight"`

# TOOL-dTrueNorth-24 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-24

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the one
function the pass mints (`--suggest check_rotated_dates --as py.function`, OK) and `--check` over the
tree, OK. Every criterion below was observed by a probe of the changed code at the working tree over
`51abdf289`. The fixture probes built their repositories under `%TEMP%/dj-*` and `%TEMP%/dj24-*`, each
removed after. To see each probe move, a second in-process run stubbed `read_row_commit` back to the
per-file read the rescope arm made before this unit, finding the one RUN file that holds the row. That
stub is a probe's staged break, not the arm's: the `routed-commits selftest` leg, which runs the plant
arms, and the `New arm:` line's RED-first observation are owed to the close.

**Evidences:** TOOL-dTrueNorth-24
- AC1 — `python3 tools/memory-tree/deviation_join.py --fixture --plant rotated --policy refuse` — run
  as `python`: exit 0, its summary `members 7 (0 unjoined)` and `0 recorded late`, and 0 lines
  holding `recorded by nobody`. The plant's line names the archive
  `memory/builds/dFixA/RUN.LANDED.8d489e05.md` and reads its member at `FIX-dTrueNorth-38@rev-1`,
  joining `2026-10-21-build-FIX-dTrueNorth-38-deviation-5`.
  Under the per-file stub the plant's member read `FIX-dTrueNorth-38@rev-2`, and `--policy refuse`
  counted 1 finding, the one `recorded by nobody` line.
- AC2 — `deviation_join.build_fixture` — with `["rotated"]`, then `deviation_join.measure_fixture`
  in-process: the archive held 3 members. The plant's `rescope` member carried the row commit's sha
  from `fx.marked`, `264d182a4`, at `FIX-dTrueNorth-38@rev-1`. The base's supersede carried
  `1cf78d026` and its add `c028f6843`, and none carried the rotation commit's `40229a111`;
  `check_rotated_dates` answered True. Under the per-file stub all three carried `40229a111`, the
  plant's member read `@rev-2`, and `check_rotated_dates` answered False. Composed over every measured
  plant, with and without `rotated`: 31 members against 30, one late member, `FIX-dTrueNorth-28@rev-1`,
  in both, and no member at the rotation sha. Over this tree, where no chain build holds an archive
  yet, the join's 17 members were identical as built and under the stub, sha for sha.
- AC3 — `deviation_join.read_row_commit` — at this repo's root with line 99 of
  `memory/builds/aRepatriatedFork/RUN.LANDED.79a3a1b5.md`, the rescope add of
  `DEPL-aRepatriatedFork-21`, as the row: `a25844711bfbc467c30fc8bdd485b27cf04b7a02` for the folder
  `memory/builds/aRepatriatedFork`, and `a73fe338770267f5c0f5a65e48bd484b0e714300` for the archive's
  own path. The two answers differ.

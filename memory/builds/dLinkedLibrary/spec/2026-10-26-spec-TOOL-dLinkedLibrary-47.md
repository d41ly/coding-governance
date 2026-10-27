# TOOL-dLinkedLibrary-47 — the `adopt program selftest` leg, which runs the adopt program's plants unit 8's arm line claimed

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 21 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-47-deviation-471.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-47-deviation-471.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 50 at HIGH**, report item **R11**. No other id shares the item.

`TOOL-dLinkedLibrary-8`'s New arm line says `adopt_program.py --selftest` runs every plant under the
`record-kinds` leg. That leg (TOOL-dTotalRecall-1 S3) runs `record_kinds.py --check`, and no scope item
of unit 8 wires the call. So its AC1 to AC8 are recorded as re-observed by a leg that never runs them, and
a router regression, writing a split candidate as major say, passes every bar.

This unit adds the leg that runs the program's selftest, through the leg factory, with its meta rows. It
repairs `TOOL-dLinkedLibrary-8` and builds one step after it (order 21).

## 2. Scope (IN)

- **S1** — The leg. `python tools/run-gates/leg_factory.py new` (TOOL-dWitnessedBar-11 S3) appends one
  `[[gate_leg]]` declaration to `tools/memory-tree/kit.toml`: name `adopt program selftest`, argv `python
  {prefix}/memory-tree/adopt_program.py --selftest`, guard `{prefix}/lib/` and `{prefix}/memory-tree/`,
  chunk `selftests`, subject `kit`, and the `ceiling`, `tag`, `purpose` and `enforces` the factory's gate
  requires; the factory renders it into `tools/gate-legs.json`. Observed by AC1 and AC2.
- **S2** — Its meta rows, the set `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`
  records: a `tools/govkit/subject-pins.tsv` row, a `tools/run-gates/selftest-budgets.txt` row, a
  `tools/run-gates/ceiling-evidence.txt` row measured at the pass, a `WHOLE_RUN` entry in
  `tools/run-gates/foreign-prefix.gov.test.sh` with its reason, the leg's name in the `gate-legs` claim of
  `memory/map/features/memory-tree-hygiene.md`, and the map's generated artifacts re-rendered. Observed
  by AC3.
- **S3** — The arm line reads true. The main loop's close observation of `TOOL-dLinkedLibrary-8`'s New arm
  line runs this leg, and unit 8's acceptance ledger names it where its arm line named `record-kinds`.
  Observed by AC4.

## 3. Non-goals (OUT)

- The `record-kinds` leg and its check: TOOL-dTotalRecall-1's, unchanged.
- The program's plants: `TOOL-dLinkedLibrary-8`'s, and the census plants `TOOL-dLinkedLibrary-51` adds
  run under this leg as they land.
- Folding the program's selftest into another selftest leg: §4 "Alternatives rejected".

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-8` — `adopt_program.py --selftest` and its plants, which the leg runs (id 50)
- **consumes-from** external — TOOL-dWitnessedBar-11's `leg_factory.py new`, built before this build run
- **hands-off** `TOOL-dLinkedLibrary-64` — the `adopt program selftest` declaration, which unit 64 re-guards and re-spells (ids 30, 15 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-8` §7: "`adopt_program.py --selftest` runs every plant under the `record-kinds`
  leg"; its §2 holds no scope item adding a leg.
- TOOL-dTotalRecall-1 S3 defines the `record-kinds` leg as `record_kinds.py --check`.
- The precedent leg `gotchas selftest` carries rows in `tools/gate-legs.json:518`,
  `tools/govkit/subject-pins.tsv:44`, `tools/run-gates/selftest-budgets.txt:65`,
  `tools/run-gates/ceiling-evidence.txt:56` and `tools/run-gates/foreign-prefix.gov.test.sh:130`.

### Files touched (estimate)

- `tools/memory-tree/kit.toml`: S1's declaration
- `tools/gate-legs.json`: rendered by the factory
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/ceiling-evidence.txt`, `tools/run-gates/foreign-prefix.gov.test.sh`: S2
- `memory/map/features/memory-tree-hygiene.md`: S2's claim
- `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json`: re-rendered

### Alternatives rejected

- **`record_kinds.py --check` calling the program's selftest.** It mixes a registry check with a
  program's fixtures, and a red fixture would read as a malformed registry.
- **The `code record selftest` aggregate of `TOOL-dLinkedLibrary-46`.** It runs the code record's
  modules; the adopt program is another mechanism with its own ceiling.

## 5. Production-readiness checklist

- security — a leg running the program's plants in scratch repositories under `%TEMP%`; no write into
  the repo.
- perf / scale — the program's plants; the ceiling is measured at the pass and recorded.
- error / empty / loading states — the selftest's own exit, read by the runner.
- observability — the runner names the leg and its verdict.
- risks — the plants build scratch repositories with remotes; the budget row names the measurement.
- testing — AC1 to AC4.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python leg_factory.py --list` runs in `tools/run-gates`, it lists
  `adopt program selftest` declared in `tools/memory-tree/kit.toml`, and
  `grep -n "adopt program selftest" tools/gate-legs.json` prints the rendered row carrying `--selftest`.
  Red when: the leg is hand-written into the manifest, or absent.
- **AC2** — When the router in a scratch copy of `adopt_program.py` is staged to settle a split candidate
  `major`, the leg's argv run in that copy exits non-zero naming the `split` plant.
  Red when: a router regression passes the leg.
- **AC3** — When `grep -c "adopt program selftest" tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt tools/run-gates/ceiling-evidence.txt tools/run-gates/foreign-prefix.gov.test.sh memory/map/features/memory-tree-hygiene.md`
  runs, each file prints 1 or more.
  Red when: a meta row the leg owes is missing.
- **AC4** — When `grep -n "adopt program selftest"` runs over unit 8's acceptance ledger, it names the
  leg its arm runs under.
  Red when: the ledger names `record-kinds` as running the program's plants.
  fixture: unit 8's acceptance ledger under `memory/builds/dLinkedLibrary/build/`.

## 7. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `foreign-prefix parity (every self-test at three prefixes)` · `every held leg is budgeted, every budget row resolves` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg S1 adds is not on the line above: the leg join resolves names against the manifest at base,
where it does not exist yet.

New arm: tools/memory-tree/adopt_program.py --selftest (the `adopt program selftest` leg) · covers AC2 · the program's plants under the new leg, the failing case a router staged to settle a split major · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 50
  (HIGH, item R11).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dWitnessedBar-11's leg factory and the precedent leg `gotchas selftest`'s
meta rows, which S2 follows row for row; nothing new is minted but the leg's declaration. `python
tools/codebase-map/reuse_lookup.py "classify a child process exit as failure versus error with a
timeout"` ranked `MapError` and `classify`, none a leg declaration, so no existing seam fits beyond the
factory.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

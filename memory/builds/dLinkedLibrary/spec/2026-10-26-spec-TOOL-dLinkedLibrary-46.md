# TOOL-dLinkedLibrary-46 — the `code record selftest` leg, which runs the code reader's, the enrichment's and the ctags pack's selftests the arm lines claimed

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 19 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-46-deviation-461.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-46-deviation-461.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 49 at HIGH**, report item **R10**. No other id shares the item.

The New arm lines of `TOOL-dLinkedLibrary-14`, `-15` and `-21` say `gov_code.py --selftest`,
`code_enrich.py --selftest` and `code_ctags.py`'s plants run under the `code record` leg beside
`code_record.py --selftest`. That leg (TOOL-dTotalRecall-8 S13) runs `code_record.py --check`, and no leg
runs `code_record.py --selftest`; none of the three specs touches `code_record.py` or the leg manifest.
So their criteria are recorded as re-observed by a leg that never invokes them, and a regression in any
of the three modules passes every bar.

This unit adds the one leg that runs them, through the leg factory, with its meta rows. It repairs units
14, 15 and 21, and builds one step after the last of them, `TOOL-dLinkedLibrary-15` (order 19).

## 2. Scope (IN)

- **S1** — The aggregate. `code_record.py --selftest` (`tools/memory-tree/code_record.py`, TOOL-dTotalRecall-8)
  runs its own plants, then `gov_code.py --selftest`, `code_enrich.py --selftest` and `code_ctags.py
  --selftest` as subprocesses from its own directory, prints one line per module, `code selftest —
  <module> · exit <n>`, and exits 1 when any module exits non-zero, naming it, or 2 when a module file is
  absent, naming it. Observed by AC1 and AC2.
- **S2** — The leg. `python tools/run-gates/leg_factory.py new` (TOOL-dWitnessedBar-11 S3) appends one
  `[[gate_leg]]` declaration to `tools/memory-tree/kit.toml`: name `code record selftest`, argv `python
  {prefix}/memory-tree/code_record.py --selftest`, guard `{prefix}/lib/` and `{prefix}/memory-tree/`, chunk
  `selftests`, subject `kit`, and the `ceiling`, `tag`, `purpose` and `enforces` the factory's gate
  requires; the factory renders it into `tools/gate-legs.json`. Observed by AC3.
- **S3** — Its meta rows, the set `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`
  records: a `tools/govkit/subject-pins.tsv` row, a `tools/run-gates/selftest-budgets.txt` row, a
  `tools/run-gates/ceiling-evidence.txt` row measured at the pass, a `WHOLE_RUN` entry in
  `tools/run-gates/foreign-prefix.gov.test.sh` with its reason, the leg's name in the `gate-legs` claim of
  `memory/map/features/memory-tree-hygiene.md`, and the map's generated artifacts re-rendered by
  `gen_map.py`. Observed by AC4.
- **S4** — The arm lines read true. This unit's New arm line covers the three modules' plants under the
  leg; the main loop's close observation of the New arm lines of units 14, 15 and 21 runs this leg, and
  each of those units' acceptance ledgers names it. Observed by AC5.

## 3. Non-goals (OUT)

- The `code record` leg and its `--check`: TOOL-dTotalRecall-8's, unchanged.
- The modules' plants: each unit's own; this unit runs them.
- A leg per module: §4 "Alternatives rejected".

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-14` — `gov_code.py --selftest`, the plants S1 runs (id 49)
- **consumes-from** `TOOL-dLinkedLibrary-15` — `code_enrich.py --selftest`, the plants S1 runs (id 49)
- **consumes-from** `TOOL-dLinkedLibrary-21` — `code_ctags.py --selftest`, the plants S1 runs (id 49)
- **consumes-from** external — TOOL-dTotalRecall-8's `code_record.py` and TOOL-dWitnessedBar-11's `leg_factory.py new`, built before this build run

## 4. Design

### Evidence

- TOOL-dTotalRecall-8 S13 defines the leg `code record` with argv `python
  {prefix}/memory-tree/code_record.py --check`; no other dTotalRecall unit adds a leg running
  `--selftest` (`git grep -l "code record selftest" -- memory/builds/dTotalRecall/spec` finds none).
- The three arm lines: `TOOL-dLinkedLibrary-14` §7 ("run by the `code record` leg beside
  `code_record.py --selftest`"), `-15` §7 and `-21` §7.
- The precedent leg `gotchas selftest` carries rows in `tools/gate-legs.json:518`,
  `tools/govkit/subject-pins.tsv:44`, `tools/run-gates/selftest-budgets.txt:65`,
  `tools/run-gates/ceiling-evidence.txt:56` and `tools/run-gates/foreign-prefix.gov.test.sh:130`.

### Files touched (estimate)

- `tools/memory-tree/code_record.py`: S1
- `tools/memory-tree/kit.toml`: S2's declaration
- `tools/gate-legs.json`: rendered by the factory
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/ceiling-evidence.txt`, `tools/run-gates/foreign-prefix.gov.test.sh`: S3
- `memory/map/features/memory-tree-hygiene.md`: S3's claim
- `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json`: re-rendered

### Alternatives rejected

- **One leg per module.** Three legs cost three sets of meta rows for one population of plants that
  share a kit and a ceiling; the aggregate names the failing module, which is what a per-module leg
  would add.
- **Folding the selftests into `code_record.py --check`.** The check grades the tree; mixing plants into
  it makes a fixture failure read as a stale record.

## 5. Production-readiness checklist

- security — a leg runs the kit's own selftests in scratch trees; no new write path into the repo.
- perf / scale — the sum of four selftests; the ceiling is measured at the pass and recorded.
- error / empty / loading states — an absent module exits 2 naming it, never a green aggregate.
- observability — one line per module and its exit.
- risks — a slow ctags plant raises the leg's time; the budget row names the measurement.
- testing — AC1 to AC5.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python code_record.py --selftest` runs at this pass's tip, it prints one `code selftest`
  line for each of its own plants, `gov_code.py`, `code_enrich.py` and `code_ctags.py`, each `exit 0`, and
  exits 0.
  Red when: a module's selftest is not run.
- **AC2** — When `gov_code.py`'s `callers` is staged to read `mention` edges as `calls` in a scratch copy,
  `python code_record.py --selftest` exits 1 naming `gov_code.py`; with `code_enrich.py` absent from the
  copy it exits 2 naming it.
  Red when: a broken module passes the aggregate, or a missing one reads green.
- **AC3** — When `python leg_factory.py --list` runs in `tools/run-gates`, it lists `code record selftest`
  declared in `tools/memory-tree/kit.toml`, and `grep -n "code record selftest" tools/gate-legs.json`
  prints the rendered row.
  Red when: the leg is hand-written into the manifest, or absent.
- **AC4** — When `grep -c "code record selftest" tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt tools/run-gates/ceiling-evidence.txt tools/run-gates/foreign-prefix.gov.test.sh memory/map/features/memory-tree-hygiene.md`
  runs, each file prints 1 or more.
  Red when: a meta row the leg owes is missing.
- **AC5** — When `grep -n "code record selftest"` runs over the acceptance ledgers of units 14, 15 and 21,
  each names it as the leg its arm runs under.
  Red when: a ledger names the `code record` leg as running a selftest.
  fixture: those ledgers under `memory/builds/dLinkedLibrary/build/`, written at their passes.

## 7. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `foreign-prefix parity (every self-test at three prefixes)` · `every held leg is budgeted, every budget row resolves` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg S2 adds is not on the line above: the leg join resolves names against the manifest at base,
where it does not exist yet.

New arm: tools/memory-tree/code_record.py --selftest (the `code record selftest` leg) · covers AC1 AC2 · the aggregate over the four modules, the failing case staged by a broken `gov_code.py` plant and an absent `code_enrich.py` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits a clause
  each repaired unit carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung
  3, the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Where does a promotion that repairs three units sit?** Options: (a) one step after the last of
  them in order, `TOOL-dLinkedLibrary-15` at 18; (b) one step after `TOOL-dLinkedLibrary-14`, the report's
  reference, at 18, tied with unit 15. (b) runs before `code_enrich.py` exists, so S1 cannot pass (veto
  1). RESOLVED (agent, 2026-10-26, delegated): (a), order 19. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 49
  (HIGH, item R10).

## 10. Reuse audit

The seams extended are TOOL-dWitnessedBar-11's leg factory, through which the leg is declared rather
than hand-written, and the precedent leg `gotchas selftest`'s meta rows, which S3 follows row for row.
`python tools/codebase-map/reuse_lookup.py "classify a child process exit as failure versus error with a
timeout"` ranked `MapError`, `classify` and two error classes, none a selftest aggregate, so no existing
seam fits the aggregate and S1 adds it to `code_record.py`.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

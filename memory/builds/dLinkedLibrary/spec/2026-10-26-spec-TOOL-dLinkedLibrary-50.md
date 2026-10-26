# TOOL-dLinkedLibrary-50 — `dossier_move.py apply` takes the caller's build and unit, so an adopter's update can run it

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 11 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-50-deviation-501.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-50-deviation-501.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 65 at HIGH**, report item **R14**. No other id shares the item.

`TOOL-dLinkedLibrary-19` S3 hard-codes `--build dLinkedLibrary --unit TOOL-dLinkedLibrary-19` and a record
path under `memory/builds/dLinkedLibrary/`, yet its Rollout makes `apply` every adopter's update step. In
an adopter, `propose --build dLinkedLibrary` refuses, there being no such build folder, or writes into a
fake gov build folder, while the shipped `test_dossier_holds_no_prose` reds every dossier still holding
prose: every adopter updating codebase-map gets a red map gate and no working migration.

This unit makes the build and the unit required arguments of `apply`, every record and proposal written
under the caller's build. It repairs `TOOL-dLinkedLibrary-19` and builds one step after it (order 11).

## 2. Scope (IN)

- **S1** — The arguments. `python tools/codebase-map/dossier_move.py apply --build <slug> --unit <id>`;
  both are required, and `apply` without either exits 2 naming the missing one. `plan` takes neither and
  writes nothing, as before. Observed by AC1.
- **S2** — Where it writes. Each moved-prose record is
  `<memory root>/builds/<slug>/build/<date>-build-<unit id>-dossier-<feature>.md`, `**Serves:** research
  <unit id>`, and each proposal goes through `reuse_entries.py propose … --build <slug> --unit <id>`;
  `apply` refuses, exit 2, when `<memory root>/builds/<slug>/` does not exist, naming it, and writes
  nothing. Observed by AC2.
- **S3** — gov's own call. `TOOL-dLinkedLibrary-19`'s migration (its S6) is the call `apply --build
  dLinkedLibrary --unit TOOL-dLinkedLibrary-19`; no gov slug or unit id is spelled in the shipped module.
  Observed by AC3.
- **S4** — The README. `tools/codebase-map/README.md`'s update step names `apply --build <your build>
  --unit <your unit>`. Observed by AC4.

## 3. Non-goals (OUT)

- The proposal call's `--feature` and `--name` spelling: `TOOL-dLinkedLibrary-38`'s (id 1).
- `apply`'s write order and re-run after a partial failure: id 66's item in `TOOL-dLinkedLibrary-52`.
- A grep arm refusing gov's own slugs in shipped kit files, the report's left-shift: a check over every
  kit, outside this clause.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-19` — `dossier_move.py apply`, its record path and its migration call, which S1 to S3 parameterise (id 65)
- **hands-off** `TOOL-dLinkedLibrary-52` — `--build` and `--unit`, under which unit 52's re-run of `apply` writes (id 66)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-19` S3 spells `--build dLinkedLibrary --unit TOOL-dLinkedLibrary-19` and the record
  path `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-19-dossier-<feature>.md`; its
  Rollout says the kit's README names `apply` as the update's step.
- `TOOL-dLinkedLibrary-1` S3 writes each proposal record under the `--build` it is given.

### Files touched (estimate)

- `tools/codebase-map/dossier_move.py`: S1 to S3, and the fixture's other-slug case
- `tools/codebase-map/README.md`: S4

### Alternatives rejected

- **Defaults derived from the run's own build.** `apply` runs in an adopter's update, often with no
  run-state to derive from; a required argument fails loudly where a guessed default writes into the
  wrong folder.

## 5. Production-readiness checklist

- security — the slug is validated as a build folder that exists before any write; nothing is written
  outside it and the map.
- perf / scale — unchanged.
- error / empty / loading states — a missing argument or build exits 2 naming it, before any write.
- observability — `apply` prints the build and unit it writes under.
- risks — none beyond `TOOL-dLinkedLibrary-19`'s.
- testing — the fixture's other-slug case.
- migration — the adopter's own `apply` call, S4.
- user docs — the codebase-map README, S4; no `help/` page covers the map.

## 6. Acceptance criteria

- **AC1** — When `python dossier_move.py apply` runs in the fixture with no `--build` or with no `--unit`,
  it exits 2 naming the missing argument and writes nothing.
  Red when: `apply` falls back to a built-in build or unit.
- **AC2** — When `python dossier_move.py --fixture --plant other-slug` runs
  `apply --build tOther --unit TOOL-tOther-1`, every moved-prose record and proposal record lands under `memory/builds/tOther/build/`
  naming `TOOL-tOther-1`; with `--build tMissing`, it exits 2 naming the folder.
  Red when: a record lands under another build, or an absent build is created.
- **AC3** — When `grep -n "dLinkedLibrary" dossier_move.py` runs in `tools/codebase-map` at this pass's
  tip, it prints no line outside a fixture's planted text.
  Red when: the shipped module spells gov's build.
- **AC4** — When `grep -n "apply --build" tools/codebase-map/README.md` runs, it prints the update step.
  Red when: the README's step omits the arguments.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · covers AC1 AC2 · the `other-slug` plant and the missing-argument case, the failing case staged by a default build in `apply` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 19 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 65
  (HIGH, item R14).

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-19`'s `dossier_move.py apply`, whose writes go through
`TOOL-dLinkedLibrary-1`'s `propose`, already parameterised by `--build` and `--unit`; S1 threads the two
through rather than adding a resolver. `python tools/codebase-map/reuse_lookup.py "find which kit
directory an installed file lives in"` ranked `resolve_kit_dir` and `kit_rel`, which locate kits, not
builds, so no existing seam fits beyond the arguments `propose` already takes.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

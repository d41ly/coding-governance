# TOOL-dLinkedLibrary-42 — `MAP_CLI` pointed at the house index, a CLI that exists whichever way the map replay goes

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 25 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-26-build-TOOL-dLinkedLibrary-42-deviation-421.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-42-deviation-421.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 8 at HIGH**, report item **R6**. No other id shares the item.

`TOOL-dLinkedLibrary-3` S3 points `MAP_CLI`, and its S6 upgrade step points every adopter's, at
`tools/memory-tree/gov_map.py`. TOOL-dTotalRecall-14 builds that file only on TOOL-dTotalRecall-17's `win`
(its S1 and AC1); on `lose` it is held unbuilt. `reuse-probed` and the stale-dossier reader test
`[ -f "$ROOT/$MAP_CLI" ]` (`tools/unattended/unattended.sh:10558`, :12035), so on `lose` the item takes its
announced skip for ever, reuse evidence is never graded at close, and the upgrade witness passes while
every adopter's `MAP_CLI` names nothing.

This unit points both at `tools/codebase-map/house_index.py`, the reuse scout's CLI that
`TOOL-dLinkedLibrary-2` builds unconditionally in the codebase-map kit, the kit `MAP_CLI` declares
adopted. It repairs `TOOL-dLinkedLibrary-3` and builds one step after it (order 25).

## 2. Scope (IN)

- **S1** — The declaration. `.unattended.conf`'s `MAP_CLI` names `tools/codebase-map/house_index.py`, and
  the example conf (`tools/unattended/.unattended.conf.example`) and `tools/unattended/README.md` name
  the house index as the file `MAP_CLI` declares. `MAP_CLI` stays the declaration that the map is
  adopted, which `reuse-probed` reads (`TOOL-dLinkedLibrary-3` S4). Observed by AC1.
- **S2** — The step. `retire_reuse_lookup.py` (`TOOL-dLinkedLibrary-3` S6) re-points a `MAP_CLI` naming
  the lookup at `{prefix}/codebase-map/house_index.py`, and its `witness` exits 0 only when that file
  exists and `MAP_CLI` names it; `down` restores the before-image as before. Observed by AC2.
- **S3** — Every spelling of the gov_map target for `MAP_CLI` is rewritten: where the unit 3 pass
  wrote `gov_map.py` as `MAP_CLI`'s value, in the conf, the example conf, the README and the step, the
  value reads `house_index.py`. Observed by AC3.
- **S4** — `TOOL-dLinkedLibrary-3`'s acceptance ledger answers its AC4 and AC7 AMENDED, naming this unit,
  since both print `gov_map.py` as the value. Observed by AC4.

## 3. Non-goals (OUT)

- `gov_map.py`, its verdict gate and `gov map code`: TOOL-dTotalRecall-14's and `TOOL-dLinkedLibrary-14`'s.
- The stale-dossier reader: `TOOL-dLinkedLibrary-3` S3 already reads `MAP_DIFF_CMD`, which this unit does
  not touch.
- `reuse-probed`'s logic: it reads scout records (`TOOL-dLinkedLibrary-3` S4); only the file its
  adoption test names moves.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-3` — `MAP_CLI` and `retire_reuse_lookup.py`, whose value and `up` step S1 and S2 re-point (id 8)
- **consumes-from** `TOOL-dLinkedLibrary-2` — `house_index.py`, the codebase-map CLI built at order 23 under either replay verdict, which `MAP_CLI` names from this unit on (id 8)
- **hands-off** `TOOL-dLinkedLibrary-57` — S2's `witness`, which unit 57 keys on the before-image's `MAP_CLI` (id 4 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-58` — S2's `witness`, whose absent-file case unit 58 states for a target with no `.unattended.conf` (id 29 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `.unattended.conf:190` reads `MAP_CLI="tools/codebase-map/reuse_lookup.py"` at base.
- `tools/unattended/unattended.sh:12035` counts `MAP_CLI` as a probe kit only when `[ -f "$ROOT/$MAP_CLI" ]`,
  and :12037 prints the skip otherwise.
- TOOL-dTotalRecall-14 S1: "on `**Verdict:** lose` this unit is not built"; its AC1 greps the verdict
  record for `win` before any code.
- `TOOL-dLinkedLibrary-2` S2 builds `tools/codebase-map/house_index.py` with no verdict condition, and
  `TOOL-dLinkedLibrary-14` §8 F1 builds `gov_code.py` under either verdict, in the memory-tree kit.

### Files touched (estimate)

- `.unattended.conf`: S1
- `tools/unattended/.unattended.conf.example`, `tools/unattended/README.md`: S1, S3
- `tools/govkit/steps/retire_reuse_lookup.py`: S2

### Alternatives rejected

- **`gov_code.py`.** It exists under both verdicts but sits in the memory-tree kit, every adopter's core,
  so `MAP_CLI` would declare the map adopted where the map is not installed.
- **S3 and S6 gated on the verdict record, with a deviation on `lose`.** It keeps `MAP_CLI` pointing at
  nothing on `lose` and leaves the skip the finding names.

## 5. Production-readiness checklist

- security — a conf value and a step's target path; the step writes the before-image first, as before.
- perf / scale — none.
- error / empty / loading states — a blank or unreadable `MAP_CLI` keeps the announced skip.
- observability — `reuse-probed` prints the declared `MAP_CLI` in its skip line, as it does today.
- risks — an adopter without the codebase-map kit keeps a blank `MAP_CLI`; the step's witness then
  fails and names the file.
- testing — AC1 to AC3 by probe and the step's scratch target.
- migration — S2 is the adopter's migration.
- user docs — none under `help/`: `help/reuse.md` (`TOOL-dLinkedLibrary-3` S9) names the scout, not the
  conf value.

## 6. Acceptance criteria

- **AC1** — When `grep -n "^MAP_CLI=" .unattended.conf` runs, it prints the house index's path under the
  codebase-map kit, and `git ls-files` lists that path at this pass's tip.
  Red when: `MAP_CLI` names a file a `lose` verdict leaves unbuilt.
- **AC2** — When `python retire_reuse_lookup.py up <target>` runs over a scratch target under `%TEMP%/rl`
  holding both lookup files, `house_index.py` and `MAP_CLI` naming the lookup, `MAP_CLI` names
  `house_index.py` and `witness` exits 0; with `house_index.py` absent from the target, `witness` exits 1
  naming it.
  Red when: the witness passes over a `MAP_CLI` that names nothing.
- **AC3** — When `git grep -n "MAP_CLI.*gov_map" -- .unattended.conf tools/unattended tools/govkit/steps`
  runs at this pass's tip, it prints nothing.
  Red when: a spelling of the old target survives.
- **AC4** — When `grep -n "AC4\|AC7" <unit 3's acceptance ledger>` runs, both answers read AMENDED and
  name `TOOL-dLinkedLibrary-42`.
  Red when: unit 3's ledger certifies the `gov_map.py` value.
  fixture: unit 3's acceptance ledger under `memory/builds/dLinkedLibrary/build/`.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 3 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Which file does `MAP_CLI` name?** Options: (a) `house_index.py`; (b) `gov_code.py`; (c) keep
  `gov_map.py` and gate on the verdict. (c) leaves the skip on `lose` (veto 1 against unit 3's S4); (b)
  declares the map adopted wherever the core is (veto 1 against S3's "the declaration that the map is
  adopted"). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the one survivor. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 8
  (HIGH, item R6).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-57, TOOL-dLinkedLibrary-58, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are `MAP_CLI`'s one declaration in `.unattended.conf` and `TOOL-dLinkedLibrary-3`'s
step program; the file named is `TOOL-dLinkedLibrary-2`'s `house_index.py`, so nothing new is minted.
`python tools/codebase-map/reuse_lookup.py "find which kit directory an installed file lives in"` ranked
`resolve_kit_dir`, `kit_rel` and `kit_dir`; `MAP_CLI` is a repo-relative declaration the driver tests
with `-f`, so none of them is the seam here, and no existing seam fits beyond the conf key.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

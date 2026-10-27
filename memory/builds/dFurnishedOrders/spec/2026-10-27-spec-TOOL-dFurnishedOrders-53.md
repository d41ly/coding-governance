# TOOL-dFurnishedOrders-53 — the guard arm's covered rule is one-way for a required directory: each required path meets the trip rule without its trailing slash, so a home's own `kit.toml` row never covers the home

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5647189e · streams tooling · order 30 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-53-deviation-531.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-53-deviation-531.md) | deviation | — |
| [2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`)
confirmed finding **id 11 at BLOCKER**, report item **B1**. No other id shares that item.

`TOOL-dFurnishedOrders-52` S16 moves `check_selftest_guard_coverage` onto gov's trip rule. The
required set holds unit 48 S14's `{prefix}/<home>/kit.toml` descriptor keys and unit 48 S17's
`{prefix}/<home>/` directories. `check_guard_trips` (`tools/memory-tree/design_lib.py:589-598`) is
symmetric for a path ending in `/`: `tools/roles/` trips the guard row `tools/roles/kit.toml` that
sits below it. So every home directory reads as covered by its own descriptor row, and deleting a
`{prefix}/<home>/` row never reds the arm. The arm then certifies the coverage unit 50 exists to
enforce without checking it.

This unit makes the covered rule one-way. It repairs unit 52 and builds one step after it (order 30).

## 2. Scope (IN)

- **S1** — A required path meets the trip rule in its file-shaped spelling. Before
  `check_selftest_guard_coverage` asks whether a required path is covered, it spells the path with
  no trailing slash. `check_guard_trips` then takes its first branch only: the path equals the guard, or
  lies under it (`design_lib.py:596-597`). Its symmetric branch needs `path.endswith("/")` (`:598`),
  so a guard row below a required directory never covers it. This holds whichever reader unit 52
  S16 or `TOOL-dFurnishedOrders-54` leaves in place, since both end in `check_guard_trips`
  (`tools/check-spec-tokens.py:621-630`). Observed by AC1 and AC2.
- **S2** — The uncovered path keeps its own spelling. The arm names an uncovered directory as the
  required set spells it, with its trailing `/`, so its failure line reads the same as unit 48 S16's.
  Observed by AC1.
- **S3** — A required file is untouched. A descriptor key or a flat source carries no trailing `/`,
  so S1 changes nothing for it. Observed by AC2.

## 3. Non-goals (OUT)

- Where the arm's trip answer is read from, and the fixture that reaches it:
  `TOOL-dFurnishedOrders-54` (id 3). The glob rows: `TOOL-dFurnishedOrders-55` (id 18). The
  arm's record of the rows it graded: `TOOL-dFurnishedOrders-56` (id 25).
- Changing `check_guard_trips`. Its symmetric branch is right for the guards join, where a declared
  directory declares everything under it (`design_lib.py:592-595`). Only this arm's question is
  one-way.
- The report's left-shift gate (a checklist entry and a policy fixture feeding every coverage arm a
  directory and a child guard): no clause of this build names it.
- Where a landed criterion of unit 52 cannot hold as written, its ledger answers it AMENDED, naming
  this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-52` — S16's covered rule over `check_selftest_guard_coverage`'s required set, which S1 makes one-way for a required directory (id 11)
- **hands-off** `TOOL-dFurnishedOrders-59` — AC1's scratch manifest and the §7 arm's staged break, whose fixture unit 59 S1 plants a row below the dropped home and unit 59 S2 proves distinguishing (id 19 of the eighth audit)

## 4. Design

### The covered rule, after this unit

```
for path in required:                       (unit 48 S14, S17, S18; unit 50 S1)
    probe := path.rstrip("/")               S1: the file-shaped spelling
    covered(path) := some literal row g of the `govkit selftest` guard with
                     check_guard_trips(probe, g)        ->  probe == g or probe under g
    not covered -> name `path` as spelled   S2
```

| required path | guard rows | before (S16) | after |
|---|---|---|---|
| `tools/roles/` | `tools/roles/kit.toml` only | covered | uncovered |
| `tools/roles/` | `tools/roles/` | covered | covered |
| `tools/roles/` | `tools/` | covered | covered |
| `tools/roles/kit.toml` | `tools/roles/` | covered | covered |

The first row is the blocker. The skeptic reproduced it on 2026-10-27 at `5647189e`: piping
`tools/hooks/` to `--legs-for -` printed `govkit selftest <- tools/hooks/kit.toml`.

### What it does not check

- Whether the required set is right. That is unit 48 S14 to S18 and unit 50 S1.
- A glob guard row. S1 meets literal rows only, as `derive_tripped_legs` does
  (`tools/check-spec-tokens.py:626-627`); unit 55 reports the rest.

### Inventory

Minted: nothing. S1 changes one expression inside `check_selftest_guard_coverage`.

### Migration

None: the arm lands at unit 48's pass in the same build run, and no reading of it is retained.

### Rollout

Live at landing, at order 30, beside units 54 to 56, which edit the same function. `--dispatch`
sequences the four, since their write sets meet (BUILD-METHOD M6, clause 1). Before the build run's
first code pass, M2's cross-read (`memory/guides/BUILD-METHOD.md:66-71`) holds unit 52 S16 to S1;
where unit 52's pass already left S1's end state, this unit's pass records that in its ledger.
govkit's version moves for the kit epoch leg where its shipped bytes move.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`
  when the staged `.py` edit moves it)

### Alternatives rejected

- **Make `check_guard_trips` one-way.** It would drop the guards join's declared-prefix rule, which
  TOOL-aBlindedTrial-7's closing review asked for and the seam's docstring cites as R3
  (`design_lib.py:592-595`). The join depends on it.
- **Restore unit 48 S16's own `covered :=` rule.** It is one-way, but it is a second spelling of the
  trip rule beside the runner's, which unit 52 S16 removed for good reason (a slashless row read as
  uncovering everything).
- **Drop the descriptor rows from the required set.** Unit 48 S14 needs them: a kit's descriptor is
  read by `apply`.

## 5. Production-readiness checklist

- security — N/A — a self-test arm's predicate; no surface moves.
- perf / scale — one `rstrip` per required path.
- error / empty / loading states — unchanged: an empty required set is still unit 48 S16's DEAD
  PROBE.
- observability — S2 keeps the uncovered path's own spelling in the failure line.
- risks — a required directory covered today only by a row below it turns red at this pass. That is
  the point, and unit 50 S1's rows are what cover it.
- testing — AC1 and AC2 by probes on scratch copies; the arm of §7 at the close.
- migration — none.
- user docs — none: a self-test arm.

## 6. Acceptance criteria

- **AC1** — When `python -B -c` calls `check_selftest_guard_coverage` over a scratch clone of the
  pass tip whose `tools/gate-legs.json` keeps the `govkit selftest` row's exact-file row for the roles
  kit's `kit.toml` and drops its `{prefix}/roles/` row, the arm names `tools/roles/` as uncovered. Over the clone
  as cloned, it names nothing uncovered.
  Red when: a required directory reads as covered by a guard row that sits below it.
  fixture: a scratch clone under `%TEMP%`, the edit committed there, the function run with that
  clone as `gov_root` and its parsed manifest as `legs`.
- **AC2** — When the same probe calls the arm over a scratch legs copy whose `govkit selftest` row
  holds `{prefix}/roles/` and not the roles kit's `kit.toml` row, it names neither `tools/roles/` nor
  the roles kit's descriptor key as uncovered.
  Red when: the one-way rule also drops a file covered by a directory row above it.
  fixture: the AC1 clone with that row edit committed instead.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the guard arm over a manifest that keeps a home's `kit.toml` row and drops its directory row, and over one that keeps only the directory row, staged by restoring the trailing `/` on the probe after deleting `tools/govkit/__pycache__` and running Python with `-B` · none

## 8. Open questions

- **F1 — Which rule decides a required directory's coverage?** Options: (a) S1, the trip rule
  over the path without its `/`; (b) a separate one-way predicate in the arm; (c) a one-way mode on
  `check_guard_trips`. (b) is a second spelling of the trip rule, the defect unit 52 S16 removed. (c)
  adds a flag to a shared seam for one caller. (a) reaches the same answer through the one rule.
  RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of id 11 ("keep the
  one-way direction ... never a guard below it"). widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-52` and the arm of
  `TOOL-dFurnishedOrders-48` are specced and unbuilt at `5647189e`. RESOLVED (agent, 2026-10-27,
  delegated): the build run re-grounds on them at the pass and records any item a landed unit
  already left in S1's end state, rung 1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, id 11
  (BLOCKER, item B1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-59, promoted from the spec audit of the round-7 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seam extended is `check_guard_trips` (`tools/memory-tree/design_lib.py:589-598`), reached as
unit 52 S16 reaches it, with `derive_tripped_legs` (`tools/check-spec-tokens.py:621-630`) as its
per-path caller. No new predicate is written.

`python tools/codebase-map/reuse_lookup.py "decide whether a manifest guard row covers a required
directory path"` ranked `rows`, `row`, `manifest` and `covers`, name-token neighbours none of which
decides guard coverage. The recall probe returned this report's B1, unit 52 S16, the round-5 report's
id 12, and TOOL-aBlindedTrial-7's closing review, which made the trip symmetric for a declared
prefix. That record agrees with source and explains why S1 strips the slash at the caller rather
than changing the seam.

Recall terms used: `python tools/memory-recall/query.py "how does a coverage arm decide a guard
covers a directory without the symmetric trip" --terms "guard coverage check_guard_trips one-way
directory descriptor row legs-for UNEVALUATED glob GLOB_MAGIC fixture manifest"`

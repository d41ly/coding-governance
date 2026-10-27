# TOOL-dFurnishedOrders-59 — unit 53's one-way case planted: the guard fixture holds a `kit.toml` row below the home it drops, asserts the old rule would read that home covered, and shows the arm graded the planted row

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base dee9e867 · streams tooling · order 31 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-59-round8-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-59-round8-fix-return.md) | research | TOOL-dFurnishedOrders-60 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-59-round8-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-59-round8-fix-brief.md) | research | TOOL-dFurnishedOrders-60 |
| [2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-60 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-7 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, report item **H1**. No other id shares that item.

`TOOL-dFurnishedOrders-53` AC1 keeps "the `govkit selftest` row's exact-file row for the roles kit's
`kit.toml`" and drops `{prefix}/roles/`. No such row exists. The guard at `dee9e867` is
`{prefix}/govkit/`, `{prefix}/hooks/kit.toml`, `{prefix}/settings-merge.py` and
`{prefix}/codebase-map/kit.toml` (`tools/gate-legs.json`, the `govkit selftest` row). Unit 48 S14
needs a guard that covers each descriptor key, which a home row does. Unit 48 S18 adds exact rows for
flat sources only, and the roles entry declares no `kind = "flat"`
(`tools/govkit/registry.toml:96-98`). So the clone holds no row below `tools/roles/`. With
`{prefix}/roles/` dropped, `tools/roles/` is uncovered under the symmetric rule too
(`tools/memory-tree/design_lib.py:589-598`). AC1 is green with or without unit 53 S1, and its staged
break cannot red it.

This unit makes the fixture hold the state that tells the fixed rule from the unfixed one. It
repairs unit 53 and builds one step after it (order 31).

## 2. Scope (IN)

- **S1** — The row is planted. The fixture's copy of the `govkit selftest` row gains the exact-file
  row `{prefix}/roles/kit.toml` when it lacks it. It then keeps only the rows `g` of that guard for
  which `check_guard_trips("tools/roles", g)` is false, so no row sits at or above `tools/roles/`.
  Unit 53 AC1's scratch clone commits this edit, and the standing arm of §7 makes it on its parsed
  copy. Observed by AC1.
- **S2** — The fixture proves it distinguishes. Before the arm grades, the case asserts two facts
  about the copy it built. The planted row is in the `govkit selftest` guard of the `legs` it passes.
  `check_guard_trips("tools/roles/", "tools/roles/kit.toml")`, the symmetric reading unit 53 S1
  stops the arm from taking, returns true. Where either fails, the arm fails as
  `DEAD PROBE: guard fixture does not distinguish the one-way rule: <which fact>`, never as a pass.
  Observed by AC1 and AC3.
- **S3** — The answer shows the planted row was graded. Unit 56 S1's returned dict maps the roles
  kit's descriptor key `tools/roles/kit.toml` (unit 48 S14) to the planted row
  `tools/roles/kit.toml`, and maps the home `tools/roles/` (unit 48 S17, kept by unit 50 S1) to
  `None`. The arm names `tools/roles/` uncovered, as unit 53 S2 spells it. Observed by AC1.
- **S4** — The staged break reds it. With unit 53 S1's `rstrip("/")` taken out of the probe, the
  dict maps `tools/roles/` to `tools/roles/kit.toml`, and the case fails. That is the break §7's
  `New arm:` line stages. Observed by AC2.
- **S5** — Unit 53's second case stands. Unit 53 AC2, a copy holding `{prefix}/roles/` and no
  `kit.toml` row, needs no planted row: its row covers both required paths under either rule, and
  its own break (a one-way rule that also misses a file under a directory row) still reds it. Observed
  by AC1.

## 3. Non-goals (OUT)

- Changing unit 53's rule or `check_guard_trips`. The finding is in the fixture, not the rule.
- Adding a `{prefix}/roles/kit.toml` row to the real `tools/gate-legs.json`. The row lives in the
  fixture's copy only. The real guard is unit 48 S14 to S18 and unit 50 S1.
- The report's left-shift gate (a checklist entry and a spec-lint over staged breaks recorded red in
  the ledger): no clause of this build names it.
- Where a landed criterion of unit 53 cannot hold as written, its ledger answers it AMENDED, naming
  this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-53` — AC1's scratch manifest and the §7 arm's staged break, whose fixture S1 plants a row below the dropped home and S2 proves distinguishing (id 19)
- **consumes-from** `TOOL-dFurnishedOrders-56` — S1's returned dict from each required path to its covering row, which S3 reads to show the planted row was graded (id 19)
- **hands-off** `TOOL-dFurnishedOrders-61` — S1, S2, AC1 and AC3, the planted row, its filter step and the patched trip rule, which unit 61 S7 to S9 and S18 to S20 settle (ids 13, 12, 19, 6, 7 and 31 of the ninth audit)

## 4. Design

### The case, after this unit

```
rows    := copy of legs["govkit selftest"].guard                       (parsed, prefix resolved)
rows    += ["tools/roles/kit.toml"] if absent                           S1
rows    := [g for g in rows if not check_guard_trips("tools/roles", g)] S1 (at or above dropped)
assert "tools/roles/kit.toml" in rows                                   S2
assert check_guard_trips("tools/roles/", "tools/roles/kit.toml")        S2 (the old rule reads covered)
out     := check_selftest_guard_coverage(gov_root, legs', reg)          unit 56 S1
assert out["tools/roles/kit.toml"] == "tools/roles/kit.toml"            S3
assert out["tools/roles/"] is None                                      S3, S4
```

`check_guard_trips("tools/roles", "tools/roles/kit.toml")` is false, because a slashless path takes
only the first branch (`design_lib.py:596-597`). So the drop step never removes the planted row.

| state | `out["tools/roles/"]` | the case |
|---|---|---|
| unit 53 S1 built | `None` | passes |
| S1's `rstrip` removed (the staged break) | `tools/roles/kit.toml` | fails |
| no planted row (unit 53 AC1 as written) | `None` either way | S2 fails as DEAD PROBE |
| `check_guard_trips` made one-way | `None` | S2 fails as DEAD PROBE |

The last row is why S2's second fact exists. A future one-way seam would make the case vacuous, and
the arm says so rather than staying green over a rule it no longer separates.

### What it does not check

- Any home other than roles. The case is keyed to one non-flat home whose descriptor key and home
  directory are both required, which unit 50 AC1 pins for `tools/roles/`.
- Glob rows. `derive_tripped_legs` skips them (`tools/check-spec-tokens.py:626-627`), and unit 55
  reports them.

### Inventory

Minted: the printed token `DEAD PROBE: guard fixture does not distinguish the one-way rule`. No
function, flag or file.

### Migration

None: the arm lands at unit 48's pass in the same build run, and no reading of it is retained.

### Rollout

Live at landing, at order 31, one step after unit 53. Before the build run's first code pass, M2's
cross-read (`memory/guides/BUILD-METHOD.md:66-71`) holds unit 53 AC1 and its §7 arm to S1 and S2.
Where unit 53's pass already planted the row, this unit's pass records that in its ledger and adds
S2's assertions and S3's dict read. govkit's version moves for the kit epoch leg where its shipped
bytes move.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`
  when the staged `.py` edit moves it)

### Alternatives rejected

- **Key the case on `codebase-map`, whose `kit.toml` row the guard already holds.** It needs no
  planted row today, but it rests on rows units 48 and 50 own. Unit 50 S1 rewrites the guard to the
  home rows its narrowed term requires, so whether `{prefix}/codebase-map/kit.toml` survives is that
  unit's answer, not this fixture's. A planted row holds whatever they land.
- **Plant the row in the real manifest.** It widens a live guard to serve a fixture, and every
  spec the new row reaches would owe the leg or a waiver row.

## 5. Production-readiness checklist

- security — N/A — a self-test fixture; no surface moves.
- perf / scale — one list edit and two asserts per run.
- error / empty / loading states — S2 fails by name when the fixture cannot separate the two rules.
- observability — S2's message names which of its two facts failed.
- risks — a seam change that makes `check_guard_trips` one-way reds this arm by name. That is the
  point: the case would then certify nothing.
- testing — AC1 to AC3 by probes on scratch copies; the arm of §7 at the close.
- migration — none.
- user docs — none: a self-test arm.

## 6. Acceptance criteria

- **AC1** — When `python -B -c` calls `check_selftest_guard_coverage` over a scratch clone of the
  pass tip whose `tools/gate-legs.json` carries S1's edit, the `govkit selftest` guard of the `legs`
  it passes holds `tools/roles/kit.toml` and no row at or above `tools/roles/`. The returned dict maps
  `tools/roles/kit.toml` to `tools/roles/kit.toml` and `tools/roles/` to `None`, and the arm names
  `tools/roles/` as uncovered. The same probe over unit 53 AC2's copy names neither path.
  Red when: the planted row is absent from what the arm graded, or the case passes without it.
  fixture: a scratch clone under `%TEMP%`, the edit committed there, the function run with that
  clone as `gov_root` and its parsed manifest as `legs`.
- **AC2** — When the AC1 probe calls `check_selftest_guard_coverage` from a scratch copy of the govkit
  self-test module whose probe has unit 53 S1's `rstrip("/")` taken out, the dict maps `tools/roles/`
  to `tools/roles/kit.toml` and the AC1 case fails.
  Red when: the staged break leaves the case green.
  fixture: the AC1 clone, its `tools/govkit/__pycache__` deleted, Python run with `-B`.
- **AC3** — When the AC1 probe runs with the loaded checker's `check_guard_trips` patched to its
  one-way form in the probe's process, the arm prints
  `DEAD PROBE: guard fixture does not distinguish the one-way rule` and fails.
  Red when: a fixture that cannot separate the two rules reads as a pass.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 · the guard arm's one-way case over a parsed manifest copy carrying a planted `{prefix}/roles/kit.toml` row and no row at or above the roles home, staged by removing unit 53 S1's `rstrip("/")` from the probe after deleting `tools/govkit/__pycache__` and running Python with `-B` · none

## 8. Open questions

- **F1 — Which fixture carries the one-way case?** Options: (a) plant `{prefix}/roles/kit.toml` in
  the copy and assert it is present; (b) key the case on `codebase-map`, whose `kit.toml` row the
  guard holds today. (b) rests on rows units 48 and 50 own (§4 "Alternatives rejected"). (a) holds
  whatever they land, and S2 makes the fixture prove it distinguishes. RESOLVED (agent, 2026-10-27,
  delegated): (a), rung 3, the first branch of the skeptic-judged fix of id 19. widens: none ·
  relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-53` and the arm of
  `TOOL-dFurnishedOrders-48` are specced and unbuilt at `dee9e867`. RESOLVED (agent, 2026-10-27,
  delegated): the build run re-grounds on them at the pass and records any item a landed unit
  already left in S1's end state, rung 1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-7 promotions, id 19
  (HIGH, item H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-61, promoted from the spec audit of the round-8 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `check_guard_trips` (`tools/memory-tree/design_lib.py:589-598`), read as the
drop step's test and as S2's distinguishing fact, and unit 56 S1's returned dict, read for S3. No new
predicate is written, and the case edits a parsed copy the arm already receives as `legs`.

`python tools/codebase-map/reuse_lookup.py "plant a guard row in a fixture manifest so a coverage
check distinguishes the fixed rule from the unfixed one"` ranked `rows`, `row`, `check`, `manifest`
and `build_fixture`, name-token neighbours none of which builds a guard-manifest copy. The recall
probe returned unit 53, this report's H1, the round-6 report's B1 with its staged-break note, and
TOOL-cGradedDebt-5, whose arm asserts the fixture's own precondition before grading. None disagreed
with source.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture prove the staged break of
a one-way coverage rule reds the arm" --terms "fixture planted row staged break one-way coverage
kit.toml home directory guard arm distinguishes fixed unfixed"`

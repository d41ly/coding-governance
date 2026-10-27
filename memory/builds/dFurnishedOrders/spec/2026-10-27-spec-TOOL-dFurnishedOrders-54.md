# TOOL-dFurnishedOrders-54 — the guard arm's trip answer is computed over the `legs` it is handed: the spec-token checker's own per-path join, loaded by path and run in process, so a scratch manifest is the manifest graded

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5647189e · streams tooling · order 30 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, report item **H1**. Item H1 merges ids 3, 18 and 25. Each takes
its own unit: id 18 is `TOOL-dFurnishedOrders-55` and id 25 is `TOOL-dFurnishedOrders-56`.

`TOOL-dFurnishedOrders-52` S16 has `check_selftest_guard_coverage` ask
`check-spec-tokens.py --legs-for -` through `read_legs_for` (`tools/policy/check_policy.py:3902-3921`).
`print_legs_for` takes no manifest. It reads `derive_legs_path(root)`, the `gate-legs.json` beside the
checker when the checker sits in the root (`tools/check-spec-tokens.py:300-311`, `:642`), so in gov
it reads the real manifest. It also refuses when no given path is tracked at HEAD (`:656-660`). Unit
52 AC6 hands the arm "scratch copies of `tools/gate-legs.json`, passed as arguments". Built as written,
its slashless case grades the real manifest's slashed row and passes whatever the copy says.

This unit makes the trip answer come from the `legs` the arm is handed. It repairs unit 52 and builds
one step after it (order 30).

## 2. Scope (IN)

- **S1** — The checker's join, run over the arm's own rows. `check_selftest_guard_coverage(gov_root,
  legs, reg)` loads `{prefix}/check-spec-tokens.py` from `gov_root` by path with
  `importlib.util.spec_from_file_location`, as the suite already loads sibling kit modules
  (`tools/govkit/selftest.py:769-772`, `:820-823`). It resolves the guard rows of `legs`' own
  `govkit selftest` row with `resolve_prefix_token`, and asks the loaded module's
  `derive_tripped_legs(path, rows)` (`tools/check-spec-tokens.py:621-630`) whether that row trips
  each required path. That function is the per-path join `--legs-for` prints, so the trip rule stays
  the checker's. Observed by AC1.
- **S2** — No subprocess and no derived manifest. The arm calls neither `read_legs_for` nor
  `--legs-for`. A manifest the arm is handed is the only manifest it reads, and a required path is
  graded whether or not HEAD tracks it. Observed by AC1 and AC2.
- **S3** — A checker that does not load is named. Where `{prefix}/check-spec-tokens.py` is absent or
  raises on load, the arm fails as `DEAD PROBE: spec-token checker did not load: <reason>`, never as a
  pass. Observed by AC3.

## 3. Non-goals (OUT)

- The one-way rule for a required directory: `TOOL-dFurnishedOrders-53` (id 11).
- Reporting glob rows: `TOOL-dFurnishedOrders-55` (id 18), over the module S1 loads.
- The arm's record of which rows it graded: `TOOL-dFurnishedOrders-56` (id 25), over S1's answer.
- A manifest argument on `--legs-for`. The checker and `policy fixtures`' reads of it stay as they
  are.
- The guard row that makes an edit to `tools/check-spec-tokens.py` select `govkit selftest`: the
  minors batch `TOOL-dFurnishedOrders-58` (id 24).
- The report's left-shift gate (a spec-lint on fixtures "passed as arguments"): no clause of this
  build names it.
- Where a landed criterion of unit 52 cannot hold as written, its ledger answers it AMENDED, naming
  this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-52` — S16's `--legs-for` route and AC6's scratch legs copy, whose trip answer S1 and S2 move onto the `legs` argument (id 3)
- **hands-off** `TOOL-dFurnishedOrders-55` — the checker module S1 loads, whose `GLOB_MAGIC` unit 55 reads over the same `legs` rows (ids 3 and 18)
- **hands-off** `TOOL-dFurnishedOrders-56` — S1's per-path answer from `derive_tripped_legs`, whose tripping guard unit 56 records per required path (ids 3 and 25)
- **hands-off** `TOOL-dFurnishedOrders-58` — the in-process checker route, which unit 58 S16 records in unit 52's ledger and whose loaded module unit 58 S17 puts under the `govkit selftest` guard (ids 3, 12 and 24)
- **hands-off** `TOOL-dFurnishedOrders-60` — S3, AC2 and AC3, the checker load and its failure messages, which unit 60 S1 to S3 settle (ids 7, 10 and 26 of the eighth audit)

## 4. Design

### The trip answer, after this unit

```
cst   := module loaded by path from gov_root/{prefix}/check-spec-tokens.py     S1 (S3 on failure)
rows  := [{name: "govkit selftest", guard: [resolve_prefix_token(g, troot) for g in
           legs["govkit selftest"].guard]}]                                     S1
hit(p):= cst.derive_tripped_legs(p, rows)  -> [(name, guard, chunk, subject)]   S1
covered(p) := hit(p) is non-empty          (p already in unit 53's file-shaped spelling)
```

Only the `govkit selftest` row is passed, so `derive_tripped_legs` answers for that leg alone and no
other leg's row is read.

### The routes the report offered

| route | the manifest graded | glob rows | cost |
|---|---|---|---|
| (a) a scratch git repo with the copy at its tool root | the copy, through `derive_legs_path`'s depth search | dropped by `read_legs_for` | a repo per case |
| (b) a manifest argument on `--legs-for` | the copy | dropped by `read_legs_for` | a second contract on the checker |
| (c) the checker's join in process, over `legs` (this unit) | the copy | from the same rows (unit 55) | one module load |

### What it does not check

- The checker's other callers. `policy fixtures` keeps `read_legs_for`, and nothing here moves it.
- That `legs` is gov's manifest in production. Unit 48 S16 passes the parsed `tools/gate-legs.json`,
  and unit 56 makes the rows graded visible.

### Inventory

Minted: the printed token `DEAD PROBE: spec-token checker did not load`. No function, flag or file.

### Migration

None: the arm lands at unit 48's pass in the same build run.

### Rollout

Live at landing, at order 30, beside units 53, 55 and 56, which edit the same function. `--dispatch`
sequences them, since their write sets meet (BUILD-METHOD M6, clause 1), and units 55 and 56 read
S1's module and answer. Before the first code pass, M2's cross-read
(`memory/guides/BUILD-METHOD.md:66-71`) holds unit 52 S16 to S1; where unit 52's pass already left
S1's end state, this unit's pass records that in its ledger. govkit's version moves for the kit
epoch leg where its shipped bytes move.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`
  when the staged `.py` edit moves it)

### Alternatives rejected

- **Route (a), a scratch git repository per case.** It reaches the copy, but every fixture case
  pays a repository, and `read_legs_for` still drops the glob rows, so a second reader is needed
  anyway.
- **Route (b), a manifest argument on `--legs-for`.** It adds a contract to a checker three legs
  read, to serve one arm that can call the join directly.
- **`design_lib.check_guard_trips` called directly.** It is one call below `derive_tripped_legs`,
  so the arm would re-spell the join's glob skip and its per-leg first-hit rule.

## 5. Production-readiness checklist

- security — N/A — the module is gov's own tracked file, loaded from the arm's `gov_root`.
- perf / scale — one module load per run replaces one `--legs-for` subprocess.
- error / empty / loading states — S3 names a checker that does not load. An empty required set is
  still unit 48 S16's DEAD PROBE.
- observability — S3's reason names the load failure.
- risks — the arm now runs the checker's module code in process, so a checker that raises at import
  fails this arm by name (S3) rather than a subprocess exit.
- testing — AC1 to AC3 by probes over scratch copies; the arm of §7 at the close.
- migration — none.
- user docs — none: a self-test arm.

## 6. Acceptance criteria

- **AC1** — When `python -B -c` calls `check_selftest_guard_coverage` with a scratch legs copy whose
  `govkit selftest` row spells `{prefix}/process-monitor` with no trailing slash, it names no path
  under `tools/process-monitor/` as uncovered. With that row deleted from a second copy, it names
  `tools/process-monitor/` as uncovered.
  Red when: the arm grades a manifest other than the `legs` it was handed.
  fixture: two parsed copies of `tools/gate-legs.json` under `%TEMP%`, each passed as `legs`.
- **AC2** — When the same probe adds a required path under a scratch `scratch-kit` directory that
  HEAD does not track, and the copy's row covers it, the arm grades it as covered and prints no
  refusal.
  Red when: an untracked required path is refused or skipped instead of graded.
  fixture: a parsed registry copy gaining the `scratch-kit` entry, as unit 48 AC6's third case.
- **AC3** — When the probe runs with `gov_root` pointing at a scratch directory holding no
  `check-spec-tokens.py` under its prefix, the arm prints `DEAD PROBE: spec-token checker did not load`
  and fails.
  Red when: a missing checker reads as full coverage.
  fixture: an empty scratch directory under `%TEMP%`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the guard arm over a slashless copy, a copy with the row deleted, an untracked required path and a missing checker, staged by pointing the arm's rows at gov's own manifest instead of its `legs` argument after deleting `tools/govkit/__pycache__` and running Python with `-B` · none

## 8. Open questions

- **F1 — Which route carries the arm's trip answer?** Options: (a) a scratch git repository per case,
  read through `read_legs_for`; (b) a manifest argument added to `--legs-for`; (c) the checker's
  `derive_tripped_legs` loaded in process over the `legs` argument. (a) and (b) still lose the glob
  rows `read_legs_for` drops, and (b) widens a shared checker's contract. (c) reaches the copy, keeps
  the checker's rule, and serves unit 55's glob rows from the same parse. RESOLVED (agent,
  2026-10-27, delegated): (c), rung 3, route (c) of the skeptic-judged fix of id 3, extended from
  `check_guard_trips` to its join for the reason §4 "Alternatives rejected" gives. widens: none ·
  relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-52` and the arm of
  `TOOL-dFurnishedOrders-48` are specced and unbuilt at `5647189e`. RESOLVED (agent, 2026-10-27,
  delegated): the build run re-grounds on them at the pass and records any item a landed unit
  already left in S1's end state, rung 1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, id 3
  (HIGH, item H1, shared with ids 18 and 25).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-60, promoted from the spec audit of the round-7 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended:

- `derive_tripped_legs` and `resolve_prefix_token` (`tools/check-spec-tokens.py:621-630`, `:228`),
  the per-path join `--legs-for` prints, for S1.
- The suite's by-path module loads (`tools/govkit/selftest.py:769-772`, `:820-823`), for S1.
- `read_legs_for` (`tools/policy/check_policy.py:3902-3921`) was read and is not extended: it takes no
  manifest and drops the glob rows.

`python tools/codebase-map/reuse_lookup.py "decide whether a manifest guard row covers a required
directory path"` ranked `rows`, `row`, `manifest` and `covers`, name-token neighbours none of which
grades a manifest it is handed. The recall probe returned this report's H1, unit 52 S16, and
TOOL-aMendedFleet-87's `--legs-for` spec, whose glob-guard UNEVALUATED rule agrees with source.

Recall terms used: `python tools/memory-recall/query.py "how does a coverage arm decide a guard
covers a directory without the symmetric trip" --terms "guard coverage check_guard_trips one-way
directory descriptor row legs-for UNEVALUATED glob GLOB_MAGIC fixture manifest"`

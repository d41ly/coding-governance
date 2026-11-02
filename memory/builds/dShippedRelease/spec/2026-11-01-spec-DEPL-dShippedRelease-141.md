# DEPL-dShippedRelease-141 — the `deploy items` leg carries `guard = []`, so an edit to the engine it drives never reuses its green

**Status:** DEFERRED · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 37 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md) | research | DEPL-dShippedRelease-140 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md`, HIGH, item H3. Unit 1 S11's row
carries no guard, so `deploy items` runs on every bar. Unit 138 S27 scopes it to four paths, while the leg's cases
exercise `--deploy close`, `--deploy record`, `--lease released` and the lander, whose code sits in
`tools/unattended/unattended.sh` and `tools/push-main.sh`. `changed()` diffs the guard alone, so neither file selects
the leg, a scoped bar carries an old green forward, and the only leg observing those terms certifies a tree it never
ran on. This is the class §8 F4 cited. This unit takes F4's other option, and repairs unit 138, order 36, at the next
step. Ids 1, 2, 18 and 30, items M1 and M2, settle the same rule in DEPL-dShippedRelease-144.

## 2. Scope (IN)

- **S1** — The row. The `deploy items` `[[gate_leg]]` row of `tools/loop/kit.toml` reads `guard = []`, unit 1 S11's reach,
  rendered into `tools/gate-legs.json`. Observed by AC1.
- **S2** — The join stays silent. The row sits in neither half of `derive_guarded_legs`, so no live spec owes the leg,
  no §7 names it, and `memory/project/spec-token-waivers.txt` gains no row. Observed by AC2.
- **S3** — A negative the probe can read. A scratch manifest holding S27's four paths reads
  `tools/unattended/unattended.sh` as not selecting the leg, so AC3 can fail, and the real row reads it as selected.
  Observed by AC3.

## 3. Non-goals (OUT)

- `deploy items selftest`'s guard and the waiver join: review ids 1, 18 and 30, in DEPL-dShippedRelease-144.
- A check deriving each fixture leg's spawned paths and failing on one outside its guard: the audit's left-shift
  item, a gate of its own.
- A guard listing every sibling the fixture spawns: §4 Alternatives rejected.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — S11's row, whose reach this unit keeps
- **consumes-from** `DEPL-dShippedRelease-138` — S27, AC15 and §8 F4, which this unit restates
- **hands-off** `DEPL-dShippedRelease-144` — the `deploy items` row, beside which ids 1, 2, 18 and 30 state the other leg and the join

## 4. Design

### Evidence

- `tools/run-gates/run-gates.sh:419` is `changed()`, a `git diff --quiet` of the base over the guard's paths.
- `memory/guides/MERGE-BAR.md:20` says an unguarded leg runs on every bar.
- `tools/check-spec-tokens.py:589` is `derive_guarded_legs`: a row keeping no non-broad guard joins neither list, so a guarded leg's join cost falls away with its guard.
- `tools/run-gates/run-gates.sh:408-416` and `GATE_FULL_MAX_LAG=10` in `.githooks/pre-push` bound the stale green to ten commits, which is why the report grades this high and not blocker.
- Unit 1 S2, S6 and S11 and unit 129 AC1 and AC2 drive `--deploy record`, `--deploy field`, `--deploy close` and `--lease released` from `deploy_fixture.py`.
- `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` is the class unit 138 §8 F4 cites.

### Supersedes

- Unit 138 S27's first sentence: S1 here.
- Unit 138 AC15: AC1 to AC3 here. Order 36 grades the four paths as written, and this pass replaces them.
- Unit 138 §8 F4's pick (a): option (b), which the report's skeptic preferred.

### Files touched (estimate)

- `tools/loop/kit.toml`: S1
- `tools/gate-legs.json`: S1, rendered

### Alternatives rejected

- **The whole read set as the guard.** `{prefix}/unattended/unattended.sh`, `{prefix}/unattended/lib-unattended.sh`, `{prefix}/push-main.sh` and every sibling the fixture spawns. It widens the join on live specs, the cost ids 1 and 30 measure at 71 specs of this build, and the next spawned sibling reopens the class.

## 5. Production-readiness checklist

- security — N/A — a row's guard, and no new surface.
- perf / scale — the fixture suite runs on every bar, unit 1 S11's stated cost; S27 was the optimisation this unit gives back.
- error / empty / loading states — N/A — no state is added, and the row reads the same on any tree.
- observability — the leg prints its case lines on every bar, and a scoped bar no longer reports it reused.
- risks — a slow suite costs each bar; a stale green over `--deploy close` is the alternative, and the leg's own ceiling bounds the cost.
- testing — the criteria of §6 and the probe of S3.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` reads the `deploy items` row of `tools/gate-legs.json`, its `guard` is empty and its `argv`
  ends in `deploy_fixture.py --all`.
  Red when: a guard stands, so an edit to `tools/unattended/unattended.sh` reuses the leg's old green.
- **AC2** — When `python -c` loads `tools/check-spec-tokens.py` by path and calls `derive_guarded_legs` over
  `tools/gate-legs.json`, `deploy items` sits in neither returned half, and `git diff --exit-code <base> -- memory/project/spec-token-waivers.txt`
  prints nothing.
  Red when: the leg owes a §7 line on every live spec declaring its paths.
- **AC3** — When `python -c` calls `check_guard_trips` for `tools/unattended/unattended.sh` over a scratch row holding
  S27's four paths, it prints `skipped`, and over the real row, which holds no guard to consult, it prints `selected`.
  Red when: the probe answers `selected` for both, so it cannot show the skip it exists to rule out.

## 7. Gates

`measure-legs selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 29 (HIGH, item H3) of the round-5 spec audit.

## 10. Reuse audit

The seam extended is unit 1 S11's `[[gate_leg]]` row in `tools/loop/kit.toml`, in the `guard = []` shape `tools/branch-reconcile/kit.toml:60` and 36 other rows of `tools/*/kit.toml` carry, PINNED at `e4c33972`.
`python tools/codebase-map/reuse_lookup.py "leg guard that selects a fixture suite by the paths it spawns"`
ranked the name-stem helper `legs` and no guard rule, so no existing seam fits beyond that row. The recall probe
surfaced TOOL-aHeardState-6, the class's checklist item, and this round's report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what guard does a fixture leg carry when it spawns another kit" --terms "held suite guard sibling kit changed gate_leg guard empty deploy items spawned paths scoped bar"`

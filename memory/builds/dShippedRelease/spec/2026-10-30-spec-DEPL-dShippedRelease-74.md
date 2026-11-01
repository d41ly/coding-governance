# DEPL-dShippedRelease-74 — a non-opting install of the integrations kit reads an accepted stop, not a missing render

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 28 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-53 DEPL-dShippedRelease-56 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-60 DEPL-dShippedRelease-73 DEPL-dShippedRelease-55 DEPL-dShippedRelease-77 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-76 DEPL-dShippedRelease-75 DEPL-dShippedRelease-67 DEPL-dShippedRelease-54 DEPL-dShippedRelease-57 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 84 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H18. Unit 8 S3 exits 0 and writes no file with no `[gate_runner.ci]`, and S6 declares
`.github/workflows/gov-bar.yml` as role `rendered`. `tools/govkit/govkit.py:8141-8160` fails an
absent rendered row unless the kit is in `stopped_ok` or `inert_declined`, and unit 8 declares no
`[[outcome]]`. So a correct non-opting install reads a problem. AC6 calls the render directly, so
`apply` never sees it.

## 2. Scope (IN)

- **S1** — The row. `tools/integrations/kit.toml` gains one `[[outcome]]`: `code = 0`,
  `probe = { must_not_exist = ".github/workflows/gov-bar.yml" }`, `means = "ci-not-declared"`,
  `ok = true`. `classify_outcome` then adds the kit to `stopped_ok`, and OBSERVE prints the row as
  not rendered. Observed by AC1.
- **S2** — An opting install is unchanged: the file exists, so the probe does not match, and `apply`
  fails an absent render as it does today. Observed by AC2.

## 3. Non-goals (OUT)

- Making the row conditional on the table: §8 F1.
- A `kit conformance` arm over rendered rows: the audit's left-shift item, which no clause of this
  build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-8` — `ci_emit.py render`, its no-table exit and the `rendered` row
- **hands-off** `DEPL-dShippedRelease-87` — §8 F1's reading of exit 0, which that unit supersedes (review id 3)
- **hands-off** `DEPL-dShippedRelease-88` — the row of S1 and S2's reading, which that unit supersedes (review id 49)
- **hands-off** `DEPL-dShippedRelease-89` — AC2, which that unit stages on a render that exits 0 and writes nothing (review id 89)
- **hands-off** `DEPL-dShippedRelease-106` — the text and code which the round-2 minors batch repairs (review ids 61)
- **hands-off** `DEPL-dShippedRelease-120` — §7's leg line (round-3 id 21)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:8094` adds a kit to `stopped_ok` when `classify_outcome` accepts, whatever the exit code, and `:8141-8160` then print `not rendered` and go on.
- `tools/memory-tree/kit.toml:141-144` is the grammar: `code`, `probe = { must_exist, must_not_exist }`, `means`.

### Files touched (estimate)

- `tools/integrations/kit.toml`: S1
- `tools/integrations/ci/ci_emit.py`: the fixture of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — one probe in a path that already runs.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py --fixture --case apply-not-declared` runs `apply` with the
  integrations kit and no `[gate_runner.ci]`, it prints `not rendered`, exits 0 and reports no
  problem.
  Red when: a correct non-opting install fails.
- **AC2** — When `--case apply-render-lost` declares the table and the adopter writes nothing,
  `apply` fails naming the path.
  Red when: the outcome row hides a render that was owed.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC2 · both cases, their failing case the outcome row taken out · none

## 8. Open questions

- **F1 — An outcome row or a conditional row?** Options: (a) an `[[outcome]]` on exit 0 with a
  probe; (b) a `[[files]]` row conditional on the table. (b) needs a condition grammar no descriptor
  reads today, while `classify_outcome` already reads (a). RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 3, the seam that exists. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 84 (HIGH, item H18) of the round-1 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-2 spec audit's promoted units declare toward this unit (units 87, 88, 89, 106); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 120); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-8's `ci_emit.py check`.
`python tools/codebase-map/reuse_lookup.py "pin third party action uses lines by sha in a workflow and check them"`
ranked name-stem helpers (`check`, `check_line`, `load_workflows`) and no pin reader, since the
module is specced and unbuilt, so no existing seam fits apart from that parent. The recall probe
surfaced unit 8 itself and the shape audit's row on gov's own workflow, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how are emitted ci action pins graded for an adopter that holds no workflow file" --terms "action pins uses sha workflow emitted ci adopter rendered outcome stopped_ok gate leg"`

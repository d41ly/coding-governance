# DEPL-dShippedRelease-121 — a fixture case grading `install.from` runs its child with no inherited override

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 21 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 39 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, item H7. Unit 61 S1
answers `GOVKIT_INSTALL_FROM` ahead of policy, unit 61 S2 has `tools/govkit/selftest.py` assign it for its
children, and unit 101's arm lives there. So `source-update` exits 0 under the override whether or not
`test_source_target` works, a check certifying an exemption it does not exercise, and the exit-2 cases of
units 62, 101, 104 and 106 go red for the wrong reason. This unit states one rule, in one function.

## 2. Scope (IN)

- **S1** — The rule. `derive_case_env(case)` in `tools/govkit/steps/receipt_schema_5.py` is the child
  environment of every `--fixture --case`: for a case in `GRADING_CASES` it is `os.environ` less
  `GOVKIT_INSTALL_FROM`, and for any other case it is `os.environ` unchanged. Observed by AC1, AC2.
- **S2** — The population. `GRADING_CASES` holds each case whose assertion reads the check's exit:
  `tagged-clone`, `update-no-to`, `source-update`, `adopt-untagged`, `update-preview` and `update-untagged`.
  A case that grades the override itself assigns its own value in its child, after S1. Observed by AC2.
- **S3** — The guard. `--case env-grading` runs with the variable assigned in the parent and asserts it
  is absent in each grading case's child. Observed by AC2.
- **S4** — The cases name it. Unit 101 AC2 and unit 104 S1 read through S1, so `source-update` proves the
  exemption with the override gone. Observed by AC1.

## 3. Non-goals (OUT)

- Each harness's own assignment: unit 61 S2 stands, and it is the parent S1 clears.
- A gotcha or checklist step for a case grading an overridable value: the audit's left-shift item, and
  `memory/gotchas/fixture-inherits-ambient-machine-state.md` is that class.

### Edges

- **consumes-from** `DEPL-dShippedRelease-101` — AC2's `source-update` and the exit-2 case beside it
- **consumes-from** `DEPL-dShippedRelease-61` — S1's override and S2's assignment
- **consumes-from** `DEPL-dShippedRelease-104` — S1 and AC1, read through this rule
- **consumes-from** `DEPL-dShippedRelease-25` — the `--fixture` cases, whose child this unit states
- **hands-off** `DEPL-dShippedRelease-138` — the text and code the batch repairs (round-4 ids 9, 44, 59)

## 4. Design

### Evidence

- Unit 61 S1 answers the variable "when that variable is set to an allowed value of the row", and S2 names `tools/govkit/selftest.py`.
- Unit 61 S3's `tagged-clone` is the only case stating an unset (report id 39).
- Unit 106 §4 "The census at base" has `tools/govkit/steps/receipt_schema_5.py` assign the variable by the close.
- `tools/govkit/selftest.py:1242` is the suite's idiom, `dict(os.environ, GOVKIT_NO_REMOTE_PROBE="1")`, a per-child environment.

### Supersedes

- Unit 61 S3's unset, which reads through S1.
- Unit 101 AC2 and unit 104 S1 gain the child this rule states, and each criterion stands as written.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_case_env` | function, `tools/govkit/steps/receipt_schema_5.py` | `py.function`, OK by `--suggest` at writing |
| `GRADING_CASES` | module constant, `tools/govkit/steps/receipt_schema_5.py` | none |

### Files touched (estimate)

- `tools/govkit/steps/receipt_schema_5.py`: S1, S2, S3
- `tools/govkit/selftest.py`: the arm of §7

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — one dict copy per case.
- error / empty / loading states — a case outside `GRADING_CASES` keeps today's environment, and S3 grades the listed ones.
- observability — unit 61 S1's line prints on every use, so a child that kept the variable prints it.
- risks — a new grading case left out of `GRADING_CASES` is vacuous again; S3 reads only the listed names, and review reads the rest.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `GOVKIT_INSTALL_FROM=any-commit python receipt_schema_5.py --fixture --case source-update`
  runs on a scratch copy with `test_source_target`'s skip cut from `_cmd_update`, it exits non-zero; on the
  tree it exits 0.
  Red when: the check certifies an exemption it does not exercise.
- **AC2** — When `GOVKIT_INSTALL_FROM=any-commit python receipt_schema_5.py --fixture --case env-grading`
  runs, it exits 0 and prints each name of `GRADING_CASES`, and with `derive_case_env` returning
  `os.environ` unchanged it exits 1 naming the first.
  Red when: a grading case inherits the override, so its exit-2 half reds for the wrong reason.
  fixture: `receipt_schema_5.py` lands at order 18, and `update-untagged` at order 33.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · `source-update` under the harness's own assignment, its failing case `test_source_target` cut from `_cmd_update` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 39 (HIGH, item H7) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 138); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is the `--fixture` module of `tools/govkit/steps/receipt_schema_5.py` (unit 25), in the per-child idiom of `tools/govkit/selftest.py:1242`.
`python tools/codebase-map/reuse_lookup.py "strip an inherited environment override from a fixture child"`
ranked the name-stem helper `fixture` and no environment helper, because the idiom is written in place at
each call, so no existing seam fits. The recall probe surfaced TOOL-aStandingWrit-4 and
TOOL-dDerivedDocket-38, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "which fixtures inherit an environment override" --terms "GOVKIT_INSTALL_FROM environment override inherited child fixture receipt_schema_5 selftest harness vacuous exemption"`

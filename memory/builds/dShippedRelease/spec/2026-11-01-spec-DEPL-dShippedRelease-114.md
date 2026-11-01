# DEPL-dShippedRelease-114 — a deferred review writes no record, and the walk is driven from a harness return

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, which shares item H2 with
id 3 (DEPL-dShippedRelease-113). With no clean path, the only way out of `pending` is unit 106 S49's
`dispose-with-reason`, which writes `## Verdict: BLOCKED` and an invented finding, and unit 14 AC6 and unit
90 AC3 plant a report the harness never emits there. A deferred return looks the same at `report: null`
and is no result at all. This unit tells the two apart and proves both from a return.

## 2. Scope (IN)

- **S1** — The deferred return. `record-clean` on a return reading `exit` `deferred-platform` writes no
  record, prints `landing review — <sha8> · deferred-platform · <pending>`, exits 3, and `review` stays
  `pending`. Observed by AC2.
- **S2** — The end-to-end case. `--case review-harness-return` fires the review under `owed`, takes a
  return shaped as `tools/workflows/tier2-review.js:1337` and `:1667` shape it, and drives it through
  `record-clean`, the records landing and `--deploy close`. Observed by AC1, AC2.
- **S3** — Which route stands. A `complete` return reaches a passed close with no owner item, so
  `dispose-with-reason` (unit 106 S49) stays the route of a review that died and of a pin that refuses,
  and never of a clean review. Observed by AC1.

## 3. Non-goals (OUT)

- The writer: DEPL-dShippedRelease-113.
- A review that dies with no return: review id 97 of the round-2 audit, unit 106 S49.
- A parity check of the return's keys against the harness: §5 states the gap.

### Edges

- **consumes-from** `DEPL-dShippedRelease-113` — `record-clean`, which this unit's case drives
- **consumes-from** `DEPL-dShippedRelease-14` — AC6, whose plant this unit restates
- **consumes-from** `DEPL-dShippedRelease-85` — the clean path this unit's walk reaches
- **hands-off** `DEPL-dShippedRelease-106` — S49's route, which reads as S3 scopes it
- **hands-off** `DEPL-dShippedRelease-133` — §4's row 1 and the `review-harness-return` case, which that unit restates (round-4 id 23)
- **hands-off** `DEPL-dShippedRelease-135` — S1's `deferred-platform` reading, which runs first (round-4 id 56)
- **hands-off** `DEPL-dShippedRelease-138` — the table, which the batch restates (round-4 ids 16, 17)

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1337` and `:1667` both return `exit: deferred ? 'deferred-platform' : 'complete'`, with `report: null` either way.
- `:1674` prints `DEFERRED: every finding raised was refuted, but …` where lenses died, which is no clean result.
- Unit 14 AC6 plants a report reading `## Verdict: CLEAN`, and unit 106 §8 F5 fixes `dispose-with-reason` at `BLOCKED` with one confirmed row.

### How a return ends

| `exit` | `report` | `pending` | Verb | Exit | `review` |
|---|---|---|---|---|---|
| `complete` | a path | any | `dispose-landing <sha> <path>` | 0 | `disposed · <n> …` |
| `complete` | null | empty | `record-clean` | 0 | `disposed · 0 …` |
| `complete` | null | non-empty | `record-clean` refuses | 2 | `pending` |
| `deferred-platform` | null | any | `record-clean` holds | 3 | `pending` |

### Supersedes

- Unit 14 AC6's plant: the report comes from `record-clean` over a return.
- Unit 106 S49's reach: it is not the route of a clean review.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1
- `tools/loop/deploy_fixture.py`: S2

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — §4's table states each return, and §6 plants the two that reach the close.
- observability — S1's line names the dead lenses.
- risks — the case's return is typed from the harness's two literals, so a renamed key reds nothing here; `record-clean`'s parse refuses at the first real run, the loud direction.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — DEPL-dShippedRelease-113 writes `help/deploy.md`'s line.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-harness-return` drives a `complete` return with
  `report` null under `review.deploy = "owed"`, the record lands, `--deploy close` records its transition,
  and no owner item is raised.
  Red when: a clean review holds the close at `pending`, or reads as blocked.
- **AC2** — When the case drives a `deferred-platform` return, `record-clean` exits 3 printing
  `deferred-platform`, no record is written, `read-landing` prints `review<TAB>pending`, and `--deploy close`
  exits 3.
  Red when: a review whose lenses died reads as clean and certifies the landing.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `review-harness-return`, its failing case the close held at `pending` on a `complete` return · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 22 (HIGH, item H2) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 133, 135, 138); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `record-clean` (DEPL-dShippedRelease-113) and the `review-` cases of `tools/loop/deploy_fixture.py`.
`python tools/codebase-map/reuse_lookup.py "drive a harness return through a walk in a fixture"`
ranked the name-stem helper `walk` and no fixture of a harness return, because `tools/loop/` is specced
and unbuilt, so no existing seam fits outside this build. The recall probe surfaced
DEPL-dShippedRelease-107, the deferred-disposal ask, and TOOL-dRetiredFork-36, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "what does exit deferred-platform mean for a review with dead lenses" --terms "deferred-platform exit pending lensesDead complete durable report null landing review"`

# DEPL-dShippedRelease-129 — a planted `handover-epoch` reaches the chain read, so unit 123 S4's exit 1 is observed

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-134 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-131 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H1. Unit 123 S5 runs
three compares. AC2's `0` and `x` and AC3's earlier-landing epoch all fail the first, so §7's stated failing
case, S4's chain read cut out, stays green, and a raw ref write of `handover-epoch` equal to `record-epoch`
with leases live closes the spec run. This unit plants the value only the chain read can refuse.

## 2. Scope (IN)

- **S1** — The chain plant. `--case engine-handover-no-release` writes `handover-epoch` equal to `record-epoch`
  by a raw ref write, with the lease still held at that epoch and no `released` record, so the first and
  third compares pass and only S4's exit 1 refuses. `--deploy close` exits 3 printing
  `forged · handover-epoch`. Observed by AC1.
- **S2** — The act alone. The same case runs `unattended.sh --lease released build <slug> <n>` directly: exit 1
  before the hand-over, and exit 0 at the same epoch after a real `run_unlease`. Observed by AC2.
- **S3** — The third compare. The case writes one raw record atop the lease chain with an epoch below the
  field, after a real hand-over, so the first two compares pass and only `read_lease_epoch`'s refuses.
  `--deploy close` exits 3 printing `forged · handover-epoch`. Observed by AC3.
- **S4** — The failing case. §7's New arm stages S4 stubbed to exit 0, and AC1 goes red on it, the staged
  break unit 123 §7 names and could not show. Observed by AC1.

## 3. Non-goals (OUT)

- The compares and the act: DEPL-dShippedRelease-123.
- A slug with no lease ref, and the `-` bound: review ids 7, 48 and 63, in the minors batch.
- A spec-token check that each §7 failing case reaches its cut code: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-123` — S4's act and S5's three compares, which these plants reach
- **hands-off** `DEPL-dShippedRelease-144` — AC2's spawn, which the batch resolves (round-5 id 17)

## 4. Design

### Which plant reaches which compare

Unit 123 S5's compares run in order. Each row passes every compare above its own and fails that one.

| Compare | Reached by | Fails on |
|---|---|---|
| an integer at or above `record-epoch` | unit 123 AC2, AC3 | `0`, `x`, an earlier landing's epoch |
| S4 exits 0 for it | S1 | no `released` record at that epoch |
| `read_lease_epoch` at or above it | S3 | a tip below the field |

### Evidence

- Unit 123 §4 "The honest path": `run_unlease` releases at E, and writes E.
- Unit 95 S2: `read_lease_epoch` reads the tip record's `epoch`, so a raw record at the tip moves it.
- Unit 123 AC3's killed remote can answer `dead probe` from the lease read, ahead of S4, by unit 95 S3 (report id 2).

### Supersedes

- Unit 123 §7's New arm: its failing case stands, observed by AC1 here.

### Files touched (estimate)

- `tools/loop/deploy_fixture.py`: S1 to S4

## 5. Production-readiness checklist

- security — N/A — fixture code only.
- perf / scale — N/A — one fixture case.
- error / empty / loading states — §4's table names the state each plant reaches.
- observability — each plant prints the term's line.
- risks — a raw record the lease verb would refuse could trip `read_claims` first; AC3 asserts the `forged` line, so that reds here.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — fixture code.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-handover-no-release` plants `handover-epoch` equal to
  `record-epoch` by a raw ref write with the lease held and no `released` record, `--deploy close` exits 3
  printing `forged · handover-epoch`.
  Red when: unit 123 S4 is cut or stubbed to exit 0, and a raw write closes a spec run with leases live.
- **AC2** — When the case runs `unattended.sh --lease released build <slug> <n>` before the hand-over it exits
  1, and after `run_unlease` at the same epoch it exits 0.
  Red when: the act answers by anything but the chain.
- **AC3** — When the case writes a raw record below the field atop the chain after a real hand-over,
  `--deploy close` exits 3 printing `forged · handover-epoch`.
  Red when: unit 123 S5's third compare is cut, so a rewound tip passes.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-handover-no-release`, its failing case unit 123 S4 stubbed to exit 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 2 (HIGH, item H1) of the round-4 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is the `engine-` cases of `tools/loop/deploy_fixture.py`, beside unit 123's `engine-handover-forged`.
`python tools/codebase-map/reuse_lookup.py "plant a value that passes earlier compares and fails one later"`
ranked the name-stem helpers `fail` and `resolve_compare_base` and no plant of a chain, because `tools/loop/` is
specced and unbuilt, so no existing seam fits outside that fixture. The recall probe surfaced unit 123
and this round's report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how do fixtures reach one compare of a chain" --terms "staged break plant compare chain handover-epoch released record lease fixture cut failing case"`

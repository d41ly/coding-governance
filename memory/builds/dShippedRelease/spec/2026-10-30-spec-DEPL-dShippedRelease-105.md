# DEPL-dShippedRelease-105 — A swap written and not running exits 5, and `release.promote` routes it as a red

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 95 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H13. Unit 77 S3 exits 2 after the override is written,
while unit 6's table reads 2 as refused and its S4 says refusals swap nothing. Unit 15 S8 retries exit 2
once with the id read at the pick, then raises `release-retry`, whose options are retry or
`release.record` unverified. The configured digest has moved, so the retry exits 3, no route reaches
`release.route`, and a down environment bypasses `deploy.on-verify-fail`. A first deploy has no verified
SHA to roll back to, which is unstated too.

## 2. Scope (IN)

- **S1** — The exit. A swap whose override is written and whose restart fails exits 5, printing
  `swap written · restart failed`, and leaves the override; unit 6's table gains that row. Observed by
  AC1.
- **S2** — The route. `run_release_promote` reads exit 5 as a red: straight to `release.route`, no retry
  and no `release-retry`, `<id>` unread again. Observed by AC2.
- **S3** — An empty rollback target. `release.route` with no verified SHA for E ends `halted`, as unit
  15 S10 says, and a `halted` ending reached from exit 5 raises `release-halted` under every
  `deploy.on-verify-fail`, since E is down. Observed by AC3.
- **S4** — A failed rollback. `rollback` exiting 5 ends `halted` the same way. Observed by AC3.

## 3. Non-goals (OUT)

- What `read-current` prints after a failed restart: review ids 21 and 38, in the minors batch.
- `release.verify`'s own routes: unit 15 S9 stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-77` — S3's exit, which this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-6` — the exit table and S4's meaning of a refusal
- **consumes-from** `DEPL-dShippedRelease-15` — `run_release_promote` and `release.route`
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 13, 65, 66)

## 4. Design

### Evidence

- Unit 6 §4 "The verbs and their exits" lists 0, 3, 2 and 4, and 2 reads refused → retry, then an owner item.
- Unit 15 S8: "Exit 2 or 4 retries once, then raises `release-retry`".
- Unit 15 S10: `rollback-and-ask` reads E's last verified SHA, and no verified SHA ends `halted`.

### The table, as it reads with this row

| Exit | Meaning | `release.promote`'s route |
|---|---|---|
| 0 | done, or `already there` | `release.verify` |
| 3 | `--expect` differs from the live digest | nothing promoted and nothing recorded |
| 2 | refused: nothing swapped | refused → retry, then an owner item |
| 4 | unreachable, or `locked` | retry, then an owner item |
| 5 | written, not running | `release.route`, as a red |

### Supersedes

- Unit 77 S3's "exits 2", its AC3's `promote` exit, and unit 6's table by the row above.
- Unit 15 S8's exit list gains 5.
- Unit 15 S10: `halted` raises `release-halted` from this path under every value.

### Files touched (estimate)

- `tools/integrations/engines/compose_systemd.py`: S1
- `tools/integrations/engines/compose-systemd-host.sh`: S1
- `tools/integrations/release.py`: S2, S3, S4
- `tools/integrations/release_fixture.py`: the cases of §6
- `help/release.md`: exit 5 and what an operator reads

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — a down environment with no verified SHA is the worst case here, and AC3 plants it.
- observability — each state prints the line §2 names, on green and red.
- risks — under `roll-forward` a failed restart files the ask and E stays down until a landing; `deploy.on-verify-fail` is the owner's choice, and S3 raises the item when nothing else will.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/release.md` states exit 5 and that it routes as a failed verify.

## 6. Acceptance criteria

- **AC1** — When `python compose_systemd.py --fixture --case restart-fails` plants a restart that exits
  1, `promote` exits 5 printing `restart failed`, and the override stays.
  Red when: a refusal's exit reads "nothing changed" after the host changed.
- **AC2** — When `python release_fixture.py --case promote-restart-fails` drives `promote` to exit 5, a
  `routing` record is written, no `release-retry` item is raised, and the walk's outcome is the one
  `deploy.on-verify-fail` names.
  Red when: a down environment bypasses `deploy.on-verify-fail`.
- **AC3** — When `--case promote-restart-fails-first` runs it on an E with no verified SHA under
  `rollback-and-ask`, it ends `halted` and raises one `release-halted` item; with `rollback` exiting 5
  on an E that has one, it ends `halted` the same way.
  Red when: a down first deploy or a failed rollback raises nothing.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/release_fixture.py · covers AC2 AC3 · `promote-restart-fails`, its failing case exit 5 read as exit 2 · none

New arm: tools/integrations/engines/compose_systemd.py · covers AC1 · `restart-fails`, its failing case exit 2 after the write · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 95 (HIGH, item H13) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `run_release_promote` and `run_release_route` (unit 15 S8, S10) and unit 6's exit table.
`python tools/codebase-map/reuse_lookup.py "give a restart that failed after the write its own exit code"`
ranked name-stem helpers (`write`, `fail`, `write_text`, `owners_of`) and no engine exit reader, since
the adapter is specced and unbuilt. The recall probe surfaced unit 77 and the round-1 report's item on
the engine's exits, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what does release.promote do when a restart fails after the swap" --terms "engine exit table restart failed read-current release.route release-retry on-verify-fail written not running"`

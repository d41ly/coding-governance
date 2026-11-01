# DEPL-dShippedRelease-101 — `update` runs the install check on the resolved commit, exempt by source target alone

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 35 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H9, which stands beside id 94 (DEPL-dShippedRelease-104) on
the `to_rev` seam. Unit 62 S2 says a source-mode receipt "has no `--to`, so it does not reach the
check", but `to_rev` defaults to `HEAD` at `tools/govkit/govkit.py:13650` and always reaches
`_cmd_update`. Keyed on `to_rev`, gov's own update is refused at every untagged landing. Keyed on the
flag, an adopter's default `update --write` bypasses the refusal and writes `any-commit` under
`release-tag`, the outcome §8 F1 rejected, and AC2 always passes `--to`, so no criterion sees it.

## 2. Scope (IN)

- **S1** — The key. `cmd_update` runs `check_install_from(root, target, to_commit)` on the resolved
  commit for every target but one: `test_source_target(root, target)` true skips it, by the target and
  never by the flag. Observed by AC1, AC2.
- **S2** — The place. The check runs after `to_commit` resolves and before `update`'s first write,
  whether or not `--to` was given. Observed by AC1.

## 3. Non-goals (OUT)

- `adopt`, a read-only `update` and every other writer: DEPL-dShippedRelease-104.
- The `--to` flag's own parsing: `to_rev`'s default stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-62` — S2, whose exemption this unit restates
- **hands-off** `DEPL-dShippedRelease-104` — the resolved-commit rule, which that unit carries to every receipt writer
- **hands-off** `DEPL-dShippedRelease-121` — AC2's `source-update` and the exit-2 case beside it (round-3 id 39)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 16, 19, 35, 43, 64); its pass writes `tools/govkit/steps/receipt_schema_5.py`, which its §4 omits

## 4. Design

### Evidence

- `tools/govkit/govkit.py:13650` sets `to_rev = "HEAD"`, and `:9178-9182` resolve it to `to_commit` on every run.
- TOOL-dSafePassage-8 S1: `test_source_target(root, target)` holds when the target resolves to the gov checkout, the case that makes `update` run in source mode.

### Supersedes

- Unit 62 S2's "A source-mode receipt is the target's own checkout and has no `--to`, so it does not reach the check".
- Unit 62 AC3 stands, by this key.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: the case of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python receipt_schema_5.py --fixture --case update-no-to` runs `update --write` with
  no `--to` on an adopter at an untagged gov HEAD, with a tag behind it, it exits 2 naming the tag and
  the receipt keeps its bytes.
  Red when: an adopter's default update writes `any-commit` under `release-tag`.
- **AC2** — When `--case source-update` runs gov's own `update --target "$top" --write` at an untagged
  commit with a tag behind it, it exits 0.
  Red when: gov's own update reds at every landing once a tag exists.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · `update-no-to`, its failing case the check keyed on the flag · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 35 (HIGH, item H9) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 121, 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `check_install_from` (unit 62 S1), called from `_cmd_update`, and `test_source_target` is TOOL-dSafePassage-8's.
`python tools/codebase-map/reuse_lookup.py "exempt a source mode target from an install refusal"`
ranked `refusal`, `Refusal`, `DesignRefusal` and `load_affordance_exempt`; `Refusal` is the raise, and no
exemption reader exists at this base. The recall probe surfaced DEPL-aLevelledCopy-1 and
TOOL-dFurnishedOrders-35, neither of which keys on the flag.

Recall terms used:
`python tools/memory-recall/query.py "how does update treat a source mode target under install.from" --terms "update to_rev source mode test_source_target install.from release-tag check_install_from to_commit gov own update"`

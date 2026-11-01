# DEPL-dShippedRelease-89 — A render that writes nothing fails `apply`, and a stale workflow says so

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 29 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 89 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H1 with ids 3 and 49
(DEPL-dShippedRelease-87, -88). Unit 74's AC2 cannot pass as written, because no case stages an adopter
that exits 0 with no file, and no spec states what happens when the table is removed and
`gov-bar.yml` stays. This unit stages both, so the row's two absent states are observed on `apply`.

## 2. Scope (IN)

- **S1** — The lost render. `--case apply-render-lost` stubs `render` to exit 0 and write nothing, with
  the table declared. No row matches a code the kit declares nothing for, so `:8159` fails the absent
  rendered row, naming `gov-bar.yml`. Observed by AC1.
- **S2** — The stale file. `render` with no table and a `gov-bar.yml` on disk prints
  `ci emit — not declared · gov-bar.yml stale`, to stderr, and exits 3. The row's `must_not_exist`
  fails, no outcome is accepted, and `apply` reports a failure carrying that line. The operator
  takes the file out or restores the table. Observed by AC2.

## 3. Non-goals (OUT)

- A kit-conformance rule refusing `ok = true` at `code = 0` with only absence probes: the audit's
  left-shift item, a gate of its own (BUILD-METHOD M2), which no clause of this build names.
- Deleting a stale file on the operator's behalf: `render` writes one path and refuses to overwrite,
  and it deletes nothing.

### Edges

- **consumes-from** `DEPL-dShippedRelease-88` — the row of `code = 3`, which this unit's stages grade
- **consumes-from** `DEPL-dShippedRelease-74` — AC2, restated here on a stage that reaches its red
- **hands-off** `DEPL-dShippedRelease-120` — §3's claim, which this unit corrects (round-3 id 21)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 18, 36, 72)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:8141-8160`: an absent rendered row of a kit outside `stopped_ok` and `inert_declined` fails, naming the path.
- `tools/govkit/govkit.py:8114-8124`: a non-zero exit with no matched row is a failure carrying the last three stderr lines, which is what S2's line reaches.
- Unit 74's AC2 names a render lost "and the adopter writes nothing", and its arm stages no such render.

### Supersedes

- Unit 74 AC2 stands as written, and S1 here is the stage it needs.

### Files touched (estimate)

- `tools/integrations/ci/ci_emit.py`: S2, the fixture of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S1 and S2 are the two absent states, and each has its case.
- observability — each state prints the line §2 names, on green and red.
- risks — a removed table reds `apply` until the file goes, the loud direction: a workflow nothing renders still runs at the host.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py --fixture --case apply-render-lost` declares the table and `render`
  exits 0 writing nothing, `apply` exits non-zero naming `gov-bar.yml`.
  Red when: the outcome row hides a render that was owed.
- **AC2** — When `--case apply-stale-file` removes the table with `gov-bar.yml` present, `apply` exits
  non-zero and its output holds `gov-bar.yml stale`.
  Red when: a workflow nothing renders passes as `not rendered`.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC2 · both stages, their failing case the row with no probe · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 89 (HIGH, item H1) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 120, 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `_cmd_apply`'s OBSERVE at `tools/govkit/govkit.py:8141`, read and not changed, and the fixture of unit 74.
`python tools/codebase-map/reuse_lookup.py "tell an adopter accepted stop from a lost render by exit code"`
ranked name-stem helpers (`adopt`, `render`, `render_cards_md`, `render_family_view`) and no stage of a
lost render. The recall probe surfaced TOOL-dRedressedBar-9 and report item H1.

Recall terms used:
`python tools/memory-recall/query.py "how does an adopter tell a declared stop from a lost render" --terms "classify_outcome outcome row stopped_ok rendered must_not_exist adopter exit seed-and-stop gate_runner ci"`

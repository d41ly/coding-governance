# DEPL-dShippedRelease-92 — `test_records_landing` reads the range, so the card snapshot rides the records landing

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 6 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H4. Unit 59 S1 requires `rev-list --no-merges <tip>..HEAD`
to be one commit carrying `Pass: none`. Unit 4 S6's snapshot writer makes its own commit that rides
S7, TOOL-dPlacedRequest-2 S5 commits it alone, and `tools/policy/catalogue.toml:210-219` makes that the
default path. The test is false on the default records landing, which then queues behind other builds
and needs `land-next` under `owner-orders`, the cases S1 exists to exempt.

## 2. Scope (IN)

- **S1** — The commit. `test_records_commit(sha, slug, root)` in `tools/loop/deploy_items.py` is true
  when the non-merge commit touches only `memory/builds/<slug>/`, and carries a `Pass: none` trailer or
  the subject `card snapshot(<slug>): <state>`. Observed by AC1, AC2.
- **S2** — The range. `test_records_landing` is true when `rev-list --no-merges <advertised tip>..HEAD`
  is non-empty and every commit passes S1, the rest of unit 59 S1 standing. Observed by AC1, AC2.
- **S3** — The fixture. Each `engine-records-` case commits a real snapshot through unit 4 S6, reading
  `card.store` and `card.snapshot` at their catalogue defaults. Observed by AC1.

## 3. Non-goals (OUT)

- Folding the snapshot into the one records commit: §8 F1.
- The tree read, the rename and the merge: review ids 23 and 92, in the minors batch.
- `memory/LIVE.md`: review id 107, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-59` — `test_records_landing`, whose one-commit rule this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-4` — S6's snapshot writer and S7's records commit
- **consumes-from** `DEPL-dShippedRelease-68` — the test's second caller, which this unit's range keeps true
- **hands-off** `DEPL-dShippedRelease-106` — `test_records_commit`, beside which the minors batch grades the tree (review ids 23, 92, 107)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 17)

## 4. Design

### Evidence

- Unit 4 S6: "The commit that writer makes rides S7", and S7 commits its own one records commit.
- TOOL-dPlacedRequest-2 S5: "The record is committed alone, subject `card snapshot(<slug>): <state>`".
- `tools/policy/catalogue.toml:210-219`: `card.store` defaults to include `build-folder`, `card.snapshot` to `terminal-only`.

### Supersedes

- Unit 59 S1's "is one commit, carrying the `Pass: none` trailer".
- Unit 59's AC1, AC2 and AC4 stand, each now planting a snapshot beside the records commit.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_records_commit` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/loop/deploy_fixture.py`: S3

## 5. Production-readiness checklist

- security — S1 keeps the path test on every commit of the range, so a snapshot subject admits nothing outside the build's folder.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a commit typed with the snapshot subject passes, and it can touch only the build's own folder.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-records-snapshot` walks a build at the
  catalogue's default `card.store` and `card.snapshot`, the range holds two commits, the test is true
  and the records landing reaches the default branch with a second build queued ahead.
  Red when: the default records landing waits its turn, the case unit 59 S1 exempts.
- **AC2** — When `--case engine-records-foreign` plants a third commit touching `tools/x`, or a
  snapshot subject naming another slug, the test is false.
  Red when: the range rule admits a commit of another shape.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `engine-records-snapshot`, its failing case `rev-list --count` read as one · none

## 8. Open questions

- **F1 — Read the range, or fold the snapshot?** Options: (a) the rule over the range; (b) unit 4 S7
  folds the snapshot into the one records commit. (b) moves TOOL-dPlacedRequest-2 S5's "committed
  alone", a foreign spec. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the report's first
  option. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 6 (HIGH, item H4) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `test_records_landing` (unit 59 S1), the one test of a records-only tree.
`python tools/codebase-map/reuse_lookup.py "test that a commit range holds only records commits"`
ranked name-stem helpers (`records`, `build_commit`, `extract_records`, `read_records`) and no range
reader, because `tools/loop/` is specced and unbuilt. The recall probe surfaced scout B's row on
TOOL-dPlacedRequest-2 and report item H4, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what commits does a records landing hold on the default path" --terms "records landing snapshot card Pass none trailer test_records_landing build-folder terminal-only commit"`

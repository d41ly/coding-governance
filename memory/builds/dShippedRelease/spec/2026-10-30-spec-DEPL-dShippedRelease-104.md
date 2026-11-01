# DEPL-dShippedRelease-104 — Every receipt-writing verb runs `check_install_from`, a preview included

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 94 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H12, which stands beside id 35 (DEPL-dShippedRelease-101) on
the `to_rev` seam and id 77 in the minors batch. Unit 62 S3 takes the refusal out of
`derive_receipt_fields`, and S1 and S2 restore it for `apply` and `update` only. Unit 25 S2 names two
envelope writers, and `tools/govkit/govkit.py:13030` is inside `_cmd_adopt`, which takes `--to <rev>` and
writes on `--write`. `adopt --write` from an untagged commit under `release-tag` writes the receipt with
no refusal, and §2 does not say whether a read-only run refuses.

## 2. Scope (IN)

- **S1** — `adopt`. `_cmd_adopt` runs `check_install_from(root, target, commit)` on the resolved commit
  before its first write, the same check by the same key as DEPL-dShippedRelease-101 S1. Observed by
  AC1.
- **S2** — A preview. A read-only `update` or `adopt` refuses as its `--write` would: the check sits
  ahead of the write branch, so a preview never promises a write that exits 2. Observed by AC2.
- **S3** — The enumeration. `read_receipt_writers(source)` in `tools/govkit/selftest.py` walks
  `tools/govkit/govkit.py` by `ast` for each function building an envelope holding the key
  `gov_commit`, and an arm fails one whose body calls no `check_install_from`. Observed by AC3.

## 3. Non-goals (OUT)

- The source exemption: DEPL-dShippedRelease-101.
- Which value `adopt` records: review id 77, in the minors batch, reads the same check.

### Edges

- **consumes-from** `DEPL-dShippedRelease-101` — the resolved-commit rule, which this unit carries to every receipt writer
- **consumes-from** `DEPL-dShippedRelease-62` — S1 to S3, whose verb list this unit completes
- **consumes-from** `DEPL-dShippedRelease-25` — S2's two envelope writers
- **hands-off** `DEPL-dShippedRelease-106` — `_cmd_adopt`'s check, which the minors batch rules on (review id 77)
- **hands-off** `DEPL-dShippedRelease-121` — S1 and AC1, read through this rule (round-3 id 39)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 15, 16, 25, 27, 33, 35, 43, 64); its pass writes `tools/govkit/steps/receipt_schema_5.py`, which its §4 omits

## 4. Design

### Evidence

- `tools/govkit/govkit.py:12630` is `_cmd_adopt`, `:13030` its envelope, and unit 25 S2 names `:7981` and `:13030`.
- `_cmd_update`'s docstring reads READ-ONLY unless `--write`, and unit 62 AC2 runs `update --to <untagged>` with no `--write` and asserts exit 2, so a preview already refuses for that verb.
- Report id 42 records that AC2's exit half forces the check ahead of the write branch.

### Supersedes

- Unit 62's title and S1 to S2's verb list.
- Unit 62 §4's write set gains `_cmd_adopt`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_receipt_writers` | function, `tools/govkit/selftest.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: S3, the cases of §6

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

- **AC1** — When `python receipt_schema_5.py --fixture --case adopt-untagged` runs `adopt --write` at an
  untagged commit with a tag behind it, it exits 2 naming the tag, and `git status --porcelain` in the
  target prints nothing new.
  Red when: `adopt` writes `any-commit` under `release-tag`, or `release-tag` with no release.
- **AC2** — When `--case update-preview` runs `update --to <untagged>` with no `--write`, it exits 2
  naming the tag and writes nothing; with `--to <tag>` it exits 0.
  Red when: a preview reports a write that would refuse.
- **AC3** — When `python -c` calls `read_receipt_writers` on the tree, it lists `_cmd_apply` and
  `_cmd_adopt`, each calling the check; on a scratch copy with the call cut from `_cmd_adopt` the arm
  fails naming it.
  Red when: a third receipt writer lands with no refusal.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · `adopt-untagged`, its failing case the call cut from `_cmd_adopt` · none

## 8. Open questions

- **F1 — Does a read-only run refuse or report?** Options: (a) refuse, as `--write` would; (b) report
  and exit 0. (b) contradicts unit 62 AC2's exit 2 on a run with no `--write`. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 1, a criterion already written. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 94 (HIGH, item H12) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 121, 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `check_install_from` (unit 62 S1), and S3's enumeration reads the envelope writers unit 25 S2 names.
`python tools/codebase-map/reuse_lookup.py "refuse an install before the first write in every receipt writing verb"`
ranked name-stem helpers (`write`, `before`, `write_text`, `CensusRefused`); `CensusRefused` is a census
refusal elsewhere and reads no receipt, so no seam fits outside `govkit.py`. The recall probe surfaced
TOOL-aFlaggedScaffold-3's row on `update` and this report's appendix.

Recall terms used:
`python tools/memory-recall/query.py "which verbs write the install receipt and do they refuse a bad source" --terms "receipt envelope writer _cmd_adopt apply update check_install_from derive_receipt_fields refusal adopt to_rev"`

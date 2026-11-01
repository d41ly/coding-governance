# DEPL-dShippedRelease-98 — One table of remote shapes drives the predicate, the strip and the block, and fails on a disagreement

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 48 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H7 with ids 22, 33 and 93
(DEPL-dShippedRelease-96, -97, -99). Unit 64 §10 calls `test_credential_bearing` the reused seam while
its S1 mints a second predicate that diverges from it, and §5's "the shared plant table is what keeps
them agreed" could not catch the divergence, because no table planted the shape. Two predicates hold
one rule across the kit boundary. This unit gives that rule one table and a test that reads all three
ends.

## 2. Scope (IN)

- **S1** — The table. `REMOTE_SHAPES` in `tools/govkit/selftest.py` holds, per URL, the predicate's
  answer and the stripped value: the four shapes of unit 63, `ssh://u:tok@example.invalid/g`,
  `SSH://tok:x@example.invalid/g`, `git+ssh://git@example.invalid/g` and
  `ssh+git://git@example.invalid/g`. Observed by AC1.
- **S2** — The three-way check. `check_remote_shapes()` in the same file drives each row through
  `test_credential_bearing`, `derive_public_remote` and `test_remote_userinfo`, loading the block from
  `tools/lib/remote_userinfo.py`, and names any row where the three disagree. Observed by AC1, AC2.
- **S3** — The record. Unit 64 §10 reads as corrected: the block is a copy minted for the kit boundary
  and reuses nothing at run time, and §5's sentence holds only by S2. Observed by AC2.

## 3. Non-goals (OUT)

- Merging the block and the predicate: the kit boundary is unit 64's reason, and it stands.
- A repo-wide audit of URL classifiers: the audit's left-shift item is this table's class, over two
  callers.

### Edges

- **consumes-from** `DEPL-dShippedRelease-96` — `derive_public_remote`, the strip this unit's table drives
- **consumes-from** `DEPL-dShippedRelease-97` — `test_remote_userinfo`, the block this unit's table drives
- **consumes-from** `DEPL-dShippedRelease-64` — `tools/lib/remote_userinfo.py` and §10's claim, which this unit corrects
- **consumes-from** `DEPL-dShippedRelease-63` — the plant table
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 61, 68)

## 4. Design

### Evidence

- Unit 64 §10 names `test_credential_bearing` as "the seam reused", and S1 mints `test_remote_userinfo`.
- Unit 64 §5: "two predicates hold one rule across the kit boundary; the shared plant table is what keeps them agreed, and it holds only the shapes it lists".
- `tools/govkit/selftest.py` runs in a gov checkout, where both kits' files are present.

### Supersedes

- Unit 64 §10's "seam reused" sentence, and §5's risk line in the corrected form above.
- Unit 63 §7's arm: its table joins `REMOTE_SHAPES`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_remote_shapes` | function, `tools/govkit/selftest.py` | `py.function`, OK by `--suggest` at writing |
| `REMOTE_SHAPES` | module constant, `tools/govkit/selftest.py` | none |

### Files touched (estimate)

- `tools/govkit/selftest.py`: S1, S2

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the table holds only the shapes it lists, and a shape outside it can still diverge; DEPL-dShippedRelease-99's re-read is the write's backstop.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports the arm and calls `check_remote_shapes()` on the tree, it returns
  no row and reads eight.
  Red when: the table reads fewer ends than it names, so an empty population passes.
- **AC2** — When the block's `:` clause is cut from a scratch copy of `remote_userinfo.py` and the call
  repeats, it names `ssh://u:tok@example.invalid/g`.
  Red when: the two predicates diverge with no finding, the defect of §5's sentence.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a scratch copy of the block, its failing case the `:` clause cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 48 (HIGH, item H7) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 63's shape table in `tools/govkit/selftest.py`.
`python tools/codebase-map/reuse_lookup.py "keep two copies of a credential predicate agreeing"`
ranked `.unattended.conf`, `KITDIR`, `backlog.extract_row` and `branch_reconcile.read_inventory`,
shared-seam prose and no comparer of two predicates. The recall probe surfaced unit 63 and report item
H7, and the gotcha `second-implementation-is-not-a-second-opinion` the report names is this class.

Recall terms used:
`python tools/memory-recall/query.py "what makes an ssh url with a password credential bearing" --terms "test_credential_bearing SSH_BARE_USER_SCHEMES userinfo ssh password source_remote receipt strip derive_public_remote"`

# DEPL-dShippedRelease-62 — the `release-tag` refusal runs before the first write, on `apply` and on `update`

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 19 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 91 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H7. Unit 25 S2 puts the fields in `derive_receipt_fields` at the writers,
`tools/govkit/govkit.py:7981` among them, and S3 names no earlier pass, so a refused install exits 2
with kit files written and staged and no `install.json`, the half-installed shape the comment at
`:7626-7640` records as reproduced. S3 says "refuses the install" while S2 also writes on `update`,
and no sentence rules on an `update` from an untagged commit.

## 2. Scope (IN)

- **S1** — The pass. `check_install_from(root, target, rev)` in `tools/govkit/govkit.py` runs in
  `_cmd_apply`'s pre-write containment pass, beside `validate_gate_runner`, ahead of the BASELINE
  and of any write. It raises `Refusal` under `release-tag` when no tag sits at `rev` and some
  `gov/v*` tag exists, naming the newest. Observed by AC1.
- **S2** — `update`. `cmd_update` runs the same check on the `--to` revision before its first write.
  A source-mode receipt is the target's own checkout and has no `--to`, so it does not reach the
  check (TOOL-dSafePassage-8). Observed by AC2.
- **S3** — `derive_receipt_fields` keeps the values and holds no refusal, so a writer never decides
  after a write. Observed by AC1.

## 3. Non-goals (OUT)

- The override: DEPL-dShippedRelease-61.
- Which tags exist on a remote: review id 93, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-25` — S2's writers and S3's rule, which this unit moves ahead of them
- **consumes-from** `DEPL-dShippedRelease-61` — `read_install_from`, the read this check calls

## 4. Design

### Evidence

- `tools/govkit/govkit.py:7626-7640` records the hoist and its reason; `validate_gate_runner` sits three lines above it.
- `tools/govkit/govkit.py:7981` sits after the files land, under the receipt written ahead of CONFIGURE (report id 91).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_install_from` | function, `tools/govkit/govkit.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2, S3

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — a refusal leaves the target's tree as it found it; AC1 reads
  that.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — no receipt moves; the refusal fires before any write.
- user docs — `help/upgrade-steps.md` already states what `install.from` does; its sentence gains
  `update`.

## 6. Acceptance criteria

- **AC1** — When `python receipt_schema_5.py --fixture --case refused-clean` runs `apply` at an
  untagged commit with a tag elsewhere, it exits 2 and `git status --porcelain` in the target prints
  nothing new.
  Red when: the refusal fires after LAND, so a half-installed tree remains.
- **AC2** — When `--case update-untagged` runs `update --to <untagged>` under `release-tag`, it
  exits 2 naming the tag and the target's receipt keeps its bytes; `update --to <tag>` exits 0.
  Red when: an `update` writes `any-commit` under a `release-tag` policy.
- **AC3** — When `--case source-update` runs gov's source-mode update at an untagged commit, it
  exits 0.
  Red when: gov's own first update reds on the first tag.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the three cases, their failing case the check moved back to the writer · none

## 8. Open questions

- **F1 — What does `update` from an untagged commit do under `release-tag`?** Options: (a) the same
  refusal, before its first write; (b) write `any-commit` and print. (b) leaves the policy true for
  `apply` and false for the verb an adopter runs every release. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 91 (HIGH, item H7) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-25's S3 read, at the pass `_cmd_apply` already hoists
refusals to (`tools/govkit/govkit.py:7623`).
`python tools/codebase-map/reuse_lookup.py "strip credentials from a remote url before recording it"`
and a read of `tools/govkit/govkit.py` found no other pre-write refusal seam, and
`validate_gate_runner`'s sibling comment names the rule. The recall probe surfaced report items H6
and H7, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "where does an install refusal sit so that no file is written first" --terms "install.from release-tag refusal pre-write containment apply update receipt tag untagged harness"`

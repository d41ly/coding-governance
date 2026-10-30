# DEPL-dShippedRelease-69 — a landing that closes by carry-forward hands its lease back, so a second run of one slug can acquire it

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 75 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H13. Each mode of `--lease acquire` refuses a build-lease tombstone except `--for draw`,
`--lease prune` refuses it, unit 4 S9 and AC8 require refusal after unlease, and S10 stops
`--landed`'s terminal write. README rule 1 makes a spec run and a build run of one slug normal, so a
spec run that walks to `deploy.unlease` leaves its slug unleasable, and one that skips the walk
leaves a live lease past `--landed`.

## 2. Scope (IN)

- **S1** — The test. `test_carry_forward_landing(slug, root)` in `tools/loop/deploy_items.py` is
  true when the build's generated region at the landed SHA holds a `DEFERRED` row. Observed by AC1,
  AC3.
- **S2** — The hand-over. `run_unlease <slug> --as landed` on a true test writes the build lease by
  `--lease release build <slug>` with no `--as`, a hand-over, and no tombstone. Unit leases of
  terminal units take `--as landed` as before. Observed by AC1.
- **S3** — The term. `check_unleased` accepts a released build lease when the test is true, and
  every other case as unit 4 S11 says. So such a run reaches `deploy.close`. Observed by AC2.
- **S4** — The closing landing is unchanged: a tombstone, and AC8's refusal. Observed by AC3.

## 3. Non-goals (OUT)

- The `--settle` write and the `aborted` writes: unit 4's non-goal stands.
- TOOL-dPlacedRequest-16's refusal set: read, not changed.

### Edges

- **consumes-from** `DEPL-dShippedRelease-4` — `run_unlease`, `check_unleased` and S10

## 4. Design

### Evidence

- TOOL-dPlacedRequest-16 S3 and S7: every mode refuses a tombstone except `--for draw`, and `--lease prune` refuses it (report id 75).
- Report id 75 records that a hand-over alone leaves `deploy.close` held for ever, because `check_unleased` needs each lease terminal; S3 is that half.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_carry_forward_landing` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S2
- `tools/loop/deploy_items.py`: S1, S3
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a run that defers its last unit by mistake hands the lease back and its slug stays
  leasable, which is what a deferred unit needs.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `memory/guides/UNATTENDED-STOPS.md`'s statement of the lease past `--landed` gains one
  sentence, through its template.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-two-runs` lands a spec run through
  `deploy.unlease`, `unattended.sh --lease acquire build fx` then exits 0.
  Red when: the build run of a slug cannot lease it.
- **AC2** — When the same case reaches `deploy.close`, it records T10 with `check_unleased` passing
  on the released lease.
  Red when: the spec run's close holds for ever on a released lease.
- **AC3** — When `--case engine-unlease` closes a build with no `DEFERRED` row,
  `--lease acquire build fx` exits non-zero naming `tombstone`.
  Red when: a closed build can be re-leased, so the tombstone protects nothing.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-two-runs`, its failing case a tombstone written on a carry-forward · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 75 (HIGH, item H13) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`

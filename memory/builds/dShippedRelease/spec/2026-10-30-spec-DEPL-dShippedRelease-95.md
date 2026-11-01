# DEPL-dShippedRelease-95 — `check_unleased` reads the hand-over's epoch, so a spec run's close survives its build run

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 12 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 96 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H6 with id 8 (DEPL-dShippedRelease-94). Unit
69 S3 accepts only a released build lease, so `check_unleased` goes false the moment the build run
re-leases the slug, and its unit leases and mail refs then fail the term too. A spec run's close is held
on the safety paths unit 68 exists to fix until the build run tombstones. This unit records the
hand-over, so the term asks whether it happened and not what the lease reads now.

## 2. Scope (IN)

- **S1** — The field. `LANDING_FIELDS` gains `handover-epoch`, written `-` by `--deploy record`, settable
  by `set_landing_field`. `run_unlease --as landed` on a true `test_carry_forward_landing` writes the
  hand-over's epoch to it as its last step, after unit 4 S8's mailbox and unit leases. Observed by AC2.
- **S2** — The read. `read_lease_epoch(slug, root)` in `tools/loop/deploy_items.py` fetches
  `refs/gov/leases/<slug>/build`, bounded, and reads the tip record's `epoch`. Observed by AC1.
- **S3** — The term. `check_unleased` on a true test passes when the field is not `-` and S2 is at or
  above it, reading no unit lease and no mail ref, which are the next run's. A failed fetch holds,
  printing `dead probe`. Every other case stands as unit 4 S11 says. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- The late route: DEPL-dShippedRelease-94, the other half of item H6.
- The closing landing's tombstone: unit 69 S4 stands.
- A second reader of a lease's history: §4's alternative.

### Edges

- **consumes-from** `DEPL-dShippedRelease-94` — the late route, past which this unit's close term finishes
- **consumes-from** `DEPL-dShippedRelease-69` — S2's hand-over and S3's term, which this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-4` — `run_unlease`'s order and `check_unleased`
- **consumes-from** `DEPL-dShippedRelease-1` — `LANDING_FIELDS` and the settable set

## 4. Design

### Evidence

- TOOL-dPlacedRequest-16 S1: a `released` record is taken "at its epoch plus one", and S5 holds the epoch rising for the lease's whole life, so an epoch at or above the hand-over's is a state at or after it.
- `--claims` prints fields 1 to 5 and the row keeps `epoch` past them (TOOL-dPlacedRequest-1 "The rows"), so S2 reads the ref.
- Unit 4 S8 closes the mailbox before the lease write and S11's term reads every unit lease and `refs/gov/mail/<slug>/`, which a build run re-populates.

### Supersedes

- Unit 69 S3's "accepts a released build lease".
- Unit 1 §4 "Data model": one line, `handover-epoch: - | <n>`, after `carries`; S6's settable list gains the key.
- Unit 4 S11's term for a true test only.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_lease_epoch` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `handover-epoch` | landing record field | none |

### Migration

None. The record is new in this build, so no landed record lacks the field.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/unattended/unattended.sh`: S1, `run_unlease`
- `tools/loop/deploy_fixture.py`: the case of §6

### Alternatives rejected

- **Reading `--claims` for a holder other than this run.** A stale take-over of this same landing reads the same, so the term would pass while a second node is mid-walk.
- **Walking the lease ref's chain for a `released` record.** It finds an earlier landing's hand-over on a slug that landed twice, and the field is this landing's own.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S3 names the dead probe, and AC3 plants it.
- observability — the term prints `check_unleased — carried · epoch <n> ≥ <hand-over>` on a pass.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the record is new in this build, so no landed record lacks the field.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-two-runs-late-close` lands a spec run with a
  red core and its build run live, with a live unit lease and a mail ref of its own, the copy lands and
  `deploy.close` records T10.
  Red when: the close of a spec run holds on leases of the next run.
- **AC2** — When the case's `read-landing` runs after `deploy.unlease`, it prints
  `handover-epoch<TAB><n>`, and `-` on a landing that tombstoned.
  Red when: a closing landing reads as a hand-over, or a hand-over leaves no witness.
- **AC3** — When `--case engine-unleased-dead-probe` kills the remote, `--deploy close` exits 3 printing
  `dead probe`.
  Red when: a network fault passes the term.

## 7. Gates

`unattended kit gate` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-two-runs-late-close`, its failing case a released lease read alone · none

## 8. Open questions

- **F1 — What proves the hand-over happened?** Options: (a) a landing-record field, the epoch; (b) the
  holder in `--claims`; (c) the lease chain. (b) cannot tell a take-over from the next run, and (c)
  reads an earlier landing's hand-over. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, a witness
  of this landing alone. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 96 (HIGH, item H6) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is `check_unleased` and `run_unlease` (unit 4 S8, S11, unit 69 S3), and the record's field set (unit 1 S1).
`python tools/codebase-map/reuse_lookup.py "accept a lease state newer than a hand over"`
ranked `resolveLease`, `check_lease_only_diff`, `outcome_accepted` and `plan_state`; `resolveLease` in
`tools/unattended/run-lease.js` reads this node's own lease and holds no epoch, so no seam fits. The
recall probe surfaced unit 69 and report item H6, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a carry-forward landing close late after the build run leases the slug" --terms "records-after-close late landing carry-forward lease released build run tombstone fence check_unleased"`

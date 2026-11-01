# DEPL-dShippedRelease-123 — `handover-epoch` is no settable field, and the term asks the lease chain for it

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 59 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, item H9. Unit 95 makes
`handover-epoch` settable, and its S3 passes any non-`-` value at or below the lease's epoch, reading no
unit lease or mail ref. `unattended.sh --deploy field <sha> handover-epoch 0` on a carry-forward landing
makes `check_unleased` pass with leases live, the hole units 73 and 83 to 90 exist to close. This unit
refuses the field at the door and has the term read the chain.

## 2. Scope (IN)

- **S1** — The door. `--deploy field` refuses `handover-epoch` and `record-epoch`, exit 2, naming the key as
  not settable, so unit 1 S6's list stays at five. `run_unlease` and `--deploy record` write through
  `set_landing_field` directly, and the settable test sits at the verb. Observed by AC1.
- **S2** — The bound. `LANDING_FIELDS` gains `record-epoch`, after `handover-epoch`. `--deploy record` writes
  `read_lease_epoch(slug, root)`, the landing's own lease epoch, in the first write, so a later session
  cannot move it. A dead read exits 2 and writes nothing. Observed by AC2.
- **S3** — The value. `run_unlease` writes a decimal integer, and the term reads anything else as forged.
  Observed by AC1.
- **S4** — The chain read. `unattended.sh --lease released build <slug> <n>`, a new act of
  TOOL-dPlacedRequest-1's `--lease` verb, walks the ref's first-parent chain and exits 0 when a `released`
  record stands at epoch `<n>`, 1 when none does, and 2 on an unreadable record or a failed fetch.
  Observed by AC3.
- **S5** — The term. `check_unleased` on a true `test_carry_forward_landing` with a field that is not `-`
  passes when the field is an integer at or above `record-epoch`, S4 exits 0 for it, and
  `read_lease_epoch` is at or above it. A failed compare prints
  `held · check_unleased · forged · handover-epoch`, and S4's exit 2 prints `dead probe`. A field of `-`
  stands as unit 95 S3 says. Observed by AC2, AC3, AC4.

## 3. Non-goals (OUT)

- The witness written after a kill, and the field's row in `record-kinds.toml`: round-3 ids 60, 8 and 32, in
  the minors batch.
- The lease parser: round-3 id 31, in the minors batch, moves `read_lease_epoch` onto `read_claims`.
- A signature: unit 73 §8 F1 stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-95` — S1 and S3, which this unit supersedes, and `read_lease_epoch`
- **consumes-from** `DEPL-dShippedRelease-1` — `LANDING_FIELDS`, S2's writer and S6's settable set
- **consumes-from** `DEPL-dShippedRelease-69` — S2's hand-over, the record S4 reads
- **consumes-from** `DEPL-dShippedRelease-4` — `check_unleased` and `run_unlease`
- **hands-off** `DEPL-dShippedRelease-125` — `record-epoch`, the bound and S4's act, which that unit's witness repair and field row read (round-3 ids 8, 31, 32, 60)
- **hands-off** `DEPL-dShippedRelease-129` — S4's act and S5's three compares, which those plants reach (round-4 id 2)
- **hands-off** `DEPL-dShippedRelease-138` — S2, S4 and S5, which the batch repairs (round-4 ids 7, 20, 48, 63)

## 4. Design

### Evidence

- TOOL-dPlacedRequest-1 S3: a take writes the read epoch plus one, and "every other write keeps it", so a `--lease release` writes the holder's own epoch.
- TOOL-dPlacedRequest-16 S1: a `released` record is taken "at its epoch plus one", so a next run's epoch is above the hand-over's, and an earlier landing's hand-over sits below this landing's lease epoch.
- TOOL-dPlacedRequest-26 S1 walks a lease row's first-parent chain by `epoch`, the walk S4 reads.
- Unit 1 S6 lists five settable fields, and unit 95's Supersedes adds a sixth.

### The honest path

| Step | Epoch |
|---|---|
| The spec run holds the lease | E |
| `--deploy record` writes `record-epoch` | E |
| `run_unlease` releases, and writes `handover-epoch` | E |
| The build run acquires | E+1 |
| `check_unleased`: E ≥ E, a `released` record at E, the tip's E+1 ≥ E | passes |

An earlier landing's hand-over sits at an epoch below E, so it fails the first compare.

### Supersedes

- Unit 95 S1's "settable by `set_landing_field`", and its Supersedes' "S6's settable list gains the key".
- Unit 95 S3's pass on any non-`-` value at or below the lease's epoch.
- Unit 95 §3's non-goal "A second reader of a lease's history", and §4's alternative "Walking the lease ref's chain": the walk here is bounded below by `record-epoch`, so an earlier landing's hand-over cannot answer.
- Unit 95 §5's security line: §5 here.
- Unit 1 §4 "Data model" gains one line, `record-epoch: <n>`, after `handover-epoch`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `record-epoch` | landing record field | none |
| `--lease released` | an act of the `--lease` verb | none |

### Migration

None. The record is new in this build, so no landed record lacks the field.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S2, S3, S5
- `tools/unattended/unattended.sh`: S1, S2, S4
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: the act

### Alternatives rejected

- **The field alone, with an integer check.** A typed `0` is an integer, and passes the lease compare.
- **Reading each unit lease and mail ref again.** They are the next run's, unit 95's reason, which stands.

## 5. Production-readiness checklist

- security — a landing field a close term trusts is refused at `--deploy field`, and the term reads a chain record no field sets. A session writing `refs/gov/landing/<sha>` by hand can move both fields, in the open on the remote, the exposure units 83 to 90 §5 state; it still needs a `released` record on the chain.
- perf / scale — one chain walk per close on a carry-forward landing, bounded by the lease's length.
- error / empty / loading states — S5 names `-`, a forged value and a dead probe, and §6 plants each.
- observability — the term prints `check_unleased — carried · epoch <n> ≥ <hand-over>` on a pass, as unit 95 §5 states.
- risks — a run that never released has no `released` record, and reads `-`, unit 4 S11's terms.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the record is new in this build, so no landed record lacks the field.
- user docs — `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`, states the `--lease released` act.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --deploy field <sha> handover-epoch 0` runs, it exits 2 naming the key as not
  settable, and `read-landing` prints `handover-epoch<TAB>-`; the same for `record-epoch`.
  Red when: a typed value skips every unit lease and mail ref.
- **AC2** — When `python deploy_fixture.py --case engine-handover-forged` plants `handover-epoch: 0` beneath
  `record-epoch: 3` through a raw ref write, and again `handover-epoch: x`, `--deploy close` exits 3
  printing `forged · handover-epoch`, with `read-landing` printing `record-epoch<TAB>3`.
  Red when: a value past the door closes a spec run with leases live.
- **AC3** — When the case plants an earlier landing's real `released` record at an epoch below `record-epoch`,
  `--deploy close` exits 3 printing `forged`, and with the remote killed it exits 3 printing `dead probe`.
  Red when: an earlier landing's hand-over answers for this one, or a fault reads as a forgery.
- **AC4** — When `python deploy_fixture.py --case engine-two-runs-late-close` runs, unit 95 AC1 stands: the
  close records T10 with the build run live, the field equal to `record-epoch`.
  Red when: the bound refuses the honest hand-over.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 · `engine-handover-forged`, its failing case S4's chain read cut out · none

## 8. Open questions

- **F1 — Above, or at or above, this landing's lease epoch?** Report item H9's corrected fix reads "above".
  A release keeps the holder's epoch (TOOL-dPlacedRequest-1 S3), so the honest `handover-epoch` equals
  `record-epoch`, and "above" refuses the case the unit exists to pass. Options: (a) at or above; (b) above.
  (b) fails AC4. An earlier landing's hand-over sits strictly below, because the next take raised the
  epoch (TOOL-dPlacedRequest-16 S1), so (a) keeps what "above" was for. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 1, a criterion already written. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 59 (HIGH, item H9) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 129, 138); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `check_unleased` (unit 4 S11, unit 95 S3), the `--lease` verb (TOOL-dPlacedRequest-1) and the chain walk TOOL-dPlacedRequest-26 S1 states.
`python tools/codebase-map/reuse_lookup.py "refuse a settable field at the door and record a witness no door sets"`
ranked the name-stem helper `records` and no lease reader, because the verb's epoch fields are specced
and unbuilt, so no existing seam fits outside those specs. The recall probe surfaced units 94 and 95,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how can a close term trust a landing field" --terms "handover-epoch landing field set_landing_field settable lease epoch released forged door check_unleased"`

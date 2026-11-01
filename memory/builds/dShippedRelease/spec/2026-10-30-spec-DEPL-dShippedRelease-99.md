# DEPL-dShippedRelease-99 — `derive_public_remote` re-reads its own output, and a credential that survives records `null`

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 93 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H7 with ids 22, 33 and 48
(DEPL-dShippedRelease-96, -97, -98). Unit 63 S2 reads unit 25's strip as superseded and nothing reads
the value after the strip, so any shape the strip misses ships in a committed receipt with the adopter's
check green. `test_credential_bearing` tests every match in a text, and the strip changes one, so a URL
holding a second userinfo survives it. Unit 25 S4 promises no credential survives. This unit checks
that promise on the value written.

## 2. Scope (IN)

- **S1** — The re-read. `derive_public_remote` asks `test_credential_bearing("source_remote", value)` on
  its own stripped value. True returns `None`, and the writer records `source_remote: null`, printing
  `source_remote — not recorded · a credential survived the strip`, the path unit 25 S4 gives a remote
  it cannot record. The line names no value. Observed by AC1.
- **S2** — The order. S1 runs inside `derive_public_remote`, so the receipt writer needs no refusal and
  unit 62 S3's rule that a writer never decides after a write stands. Observed by AC2.

## 3. Non-goals (OUT)

- A refusal of the install: §8 F1.
- Rewriting a receipt already written: the build is unlanded, so none holds such a value.

### Edges

- **consumes-from** `DEPL-dShippedRelease-96` — the strip's output, which this unit re-reads
- **consumes-from** `DEPL-dShippedRelease-63` — S2's reading that left no second strip
- **consumes-from** `DEPL-dShippedRelease-25` — S4's `null` path and its promise
- **consumes-from** `DEPL-dShippedRelease-62` — S3's rule, which this unit keeps
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 16, 43); its pass writes `tools/govkit/steps/receipt_schema_5.py`, which its §4 omits

## 4. Design

### Evidence

- TOOL-dSafePassage-44 §4 walks `re.finditer` over the whole tested text and returns true on the first match not exempt.
- `memory/TEMPLATE-SPEC.md`, "Security boundaries": re-check caps after any transform that can grow content; the same rule applies to one that can miss.
- Unit 25 S4: "A filesystem path or no remote writes `null` and prints that no remote can be recorded."
- Unit 62 S3: "`derive_receipt_fields` keeps the values and holds no refusal".

### Supersedes

- Unit 63 S2's reading stands, and this re-read takes the place the second strip held.
- Unit 25 S4's `null` line gains this one case.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1
- `tools/govkit/selftest.py`: the case of §6

## 5. Production-readiness checklist

- security — the value is re-graded after the transform, at the write boundary, and the printed line carries no part of it.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — an adopter with such a remote records `null` and loses the provenance line; the receipt's job here is to carry no secret.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `derive_public_remote` over
  `https://example.invalid/g?x=https://tok@example.invalid/g`, it returns `None`, and the printed line
  holds `not recorded` and no `tok`.
  Red when: a credential the strip missed ships in a committed receipt.
- **AC2** — When `python receipt_schema_5.py --fixture --case remote-survives` runs `apply` at that
  remote, it exits 0, the receipt holds `source_remote: null`, and no file holds `tok`.
  Red when: the check refuses after LAND, or the value reaches a tree.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a remote holding a second userinfo, its failing case the re-read cut out · none

## 8. Open questions

- **F1 — What does a surviving credential do?** Options: (a) record `null` and print; (b) refuse the
  install; (c) strip again in a loop. (b) needs the refusal in the pre-write pass, on a value this unit
  has not read there, and (c) strips by a rule the predicate does not state. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the path unit 25 S4 already states. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 93 (HIGH, item H7) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `derive_public_remote` (unit 25 S4), with `test_credential_bearing` the predicate.
`python tools/codebase-map/reuse_lookup.py "re-check a sanitized value after the transform"`
ranked name-stem helpers (`check`, `checks`, `check_line`, `build_spec_path_re`) and no post-transform
check of a remote. The recall probe surfaced unit 63 and report item H7, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what makes an ssh url with a password credential bearing" --terms "test_credential_bearing SSH_BARE_USER_SCHEMES userinfo ssh password source_remote receipt strip derive_public_remote"`

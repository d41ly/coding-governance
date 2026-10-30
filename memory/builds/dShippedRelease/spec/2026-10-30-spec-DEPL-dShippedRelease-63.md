# DEPL-dShippedRelease-63 — `derive_public_remote` strips the whole userinfo of a non-ssh remote

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 19 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 46 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, which shares item H8 with id 92 (DEPL-dShippedRelease-64). Unit 25 S4 strips only the userinfo
password, so `https://<token>@host/repo`, which has no password part, survives and ships in an
adopter's committed `.governance/install.json`, against S4's own "no credential may survive it". A
second rule for one fact sits beside `test_credential_bearing`, which already calls that shape
credential-bearing.

## 2. Scope (IN)

- **S1** — The write. `derive_public_remote(root)` asks
  `test_credential_bearing("source_remote", url)` (TOOL-dSafePassage-38 S1), and on true strips the
  whole userinfo of any non-ssh scheme. A bare user on an `ssh://` URL (TOOL-dSafePassage-44) and an
  scp-shaped remote stand. Observed by AC1.
- **S2** — Unit 25 §8 F6's "strip the password" and its AC5 plant are read as superseded by S1. AC1
  here holds both shapes. Observed by AC1.

## 3. Non-goals (OUT)

- The read of a receipt that already holds such a value: DEPL-dShippedRelease-64.
- Any new credential predicate: this unit calls the parent's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-25` — `derive_public_remote`, S4's value, and the `source_remote` field
- **hands-off** `DEPL-dShippedRelease-64` — the plant table `https://tok@example.invalid/g`, which that unit reads back at the receipt

## 4. Design

### Evidence

- TOOL-dSafePassage-38 S1 returns true for a `<scheme>://` URL carrying userinfo before its host, and its S1 keeps scp form out; DEPL-dShippedRelease-31 §5 uses the same predicate for its remote.
- The ladder's `resolve_remote` is `tools/govkit/govkit.py:558`; unit 25 S4 reads it, and it does not change.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1

## 5. Production-readiness checklist

- security — this is the write boundary of a value that ships in an adopter's tree; the predicate is
  the parent's one rule, and the plant table holds each shape.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a remote whose user is meaningful loses it in the record only; the record's job is to name
  the host.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `derive_public_remote` over `https://tok@example.invalid/g` and
  over `https://user:tok@example.invalid/g`, neither value holds `tok`, and each keeps
  `example.invalid`.
  Red when: a token held as a bare user ships in a committed receipt.
- **AC2** — When it runs over `ssh://git@example.invalid/g` and `git@example.invalid:g`, each value
  comes back unchanged.
  Red when: a harmless ssh user is stripped, so `source_remote` stops naming the remote.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a table of the four shapes, its failing case the password-only strip · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 46 (HIGH, item H8) of the round-1 spec audit.

## 10. Reuse audit

The seam reused is TOOL-dSafePassage-38's `test_credential_bearing` with TOOL-dSafePassage-44's ssh
exemption, specced and unbuilt at this base.
`python tools/codebase-map/reuse_lookup.py "strip credentials from a remote url before recording it"`
ranked name-stem helpers (`before`, `records`, `resolve_remote`) and no redactor in the tree, so the
parent's predicate is the only seam. The recall probe surfaced TOOL-dSafePassage-44 and report item
H8, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a credential bearing remote url classified and redacted before it reaches a receipt" --terms "test_credential_bearing render_redacted_config userinfo remote token bare user receipt source_remote"`

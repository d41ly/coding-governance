# DEPL-dShippedRelease-97 — `test_remote_userinfo` ends the ssh exemption on a `:`, as the predicate does

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 33 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H7 with ids 22, 48 and 93
(DEPL-dShippedRelease-96, -98, -99). Unit 64's `test_remote_userinfo` is true only on a non-ssh scheme,
so `ssh://u:tok@host/r` passes `check_release_field`, the one integrity check an adopter's own bar runs.
An uppercase or `git+ssh` scheme is unstated too. If unit 64 S2 stands in for unit 25 S6's password
test, that check also stops failing a shape it failed before.

## 2. Scope (IN)

- **S1** — The block. `test_remote_userinfo(url)` in `tools/lib/remote_userinfo.py` matches
  `<scheme>://<userinfo>@`, lowercases the scheme, and is true unless the scheme is one of `ssh`,
  `git+ssh` and `ssh+git` and the userinfo holds no `:`. Observed by AC1, AC2.
- **S2** — The read. `check_release_field` fails a `source_remote` on which S1 is true, and that is the
  whole of unit 25 S6's password test, so no shape it failed passes. Observed by AC1.

## 3. Non-goals (OUT)

- The write: DEPL-dShippedRelease-96.
- Importing the predicate: `tools/govkit/upgrade_steps.py` does not ship to an adopter's
  `tools/run-gates/`, the reason unit 64 carries a block.

### Edges

- **consumes-from** `DEPL-dShippedRelease-64` — S1 and the block, whose exemption this unit restates
- **consumes-from** `DEPL-dShippedRelease-25` — S6's password test
- **hands-off** `DEPL-dShippedRelease-98` — `test_remote_userinfo`, the block that unit's table drives

## 4. Design

### Evidence

- Unit 64 S1: "true for a `<scheme>://` URL with userinfo on a non-ssh scheme"; report ids 33 and 48 read `ssh://u:tok@host/r` through it.
- TOOL-dSafePassage-44 S1 reads the scheme lowercased, and S2 keeps `ssh://u:p@h/r` credential-bearing.
- Unit 64 §4: `tools/govkit/upgrade_steps.py` is the predicate's home and does not ship to an adopter.

### Supersedes

- Unit 64 S1's "on a non-ssh scheme", and its title's scope.
- Unit 64 AC2 stands: `ssh://git@example.invalid/g` and `git@example.invalid:g` still exit 0.

### Files touched (estimate)

- `tools/lib/remote_userinfo.py`: S1
- `tools/run-gates/receipt_fields.py`: S1, the inlined block
- `tools/run-gates/check-receipt.py`: its fixture arm

## 5. Production-readiness checklist

- security — the read side of the same boundary; it runs on an adopter's bar with no gov checkout.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/check-receipt.py <scratch>` reads a planted schema-5 receipt
  whose `source_remote` is `ssh://u:tok@example.invalid/g`, and again `SSH://tok:x@example.invalid/g`,
  it prints `FAIL` and exits 1 for each.
  Red when: a password on an ssh URL passes the adopter's integrity check.
- **AC2** — When it reads `git+ssh://git@example.invalid/g`, it exits 0.
  Red when: a bare ssh user fails, so the check reds a correct install.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/run-gates/check-receipt.py · covers AC1 AC2 · the ssh shapes, their failing case the block true on non-ssh schemes alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 33 (HIGH, item H7) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is unit 64's inline block and `check_release_field` (unit 25 S6), restated by TOOL-dSafePassage-44's exemption.
`python tools/codebase-map/reuse_lookup.py "keep two copies of a credential predicate agreeing"`
ranked `.unattended.conf`, `KITDIR`, `backlog.extract_row` and `branch_reconcile.read_inventory`, shared-seam
prose and no predicate, so the block stays the kit-boundary copy unit 64 chose. The recall probe
surfaced unit 63 and report item H7.

Recall terms used:
`python tools/memory-recall/query.py "what makes an ssh url with a password credential bearing" --terms "test_credential_bearing SSH_BARE_USER_SCHEMES userinfo ssh password source_remote receipt strip derive_public_remote"`

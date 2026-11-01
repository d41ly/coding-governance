# DEPL-dShippedRelease-96 — `derive_public_remote` strips the whole userinfo whenever the predicate says credential-bearing

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 20 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H7 with ids 33, 48 and 93
(DEPL-dShippedRelease-97, -98, -99). TOOL-dSafePassage-44 exempts an ssh scheme only when its userinfo
holds no `:`, so `ssh://u:p@h/r` stays credential-bearing. Unit 63 S1 strips only "of any non-ssh
scheme", and its S2 reads unit 25's password strip as superseded, removing the only other strip. The
predicate answers true and nothing strips, so a token ships in an adopter's committed
`.governance/install.json`, against unit 25 S4's "no credential may survive it".

## 2. Scope (IN)

- **S1** — The strip. `derive_public_remote(root)` strips the whole userinfo whenever
  `test_credential_bearing("source_remote", url)` is true, on every scheme. A colon-free bare user on
  `SSH_BARE_USER_SCHEMES` reads false and stands, and an scp-shaped remote holds no `://` and stands.
  Observed by AC1, AC2.
- **S2** — The shapes. The strip reads `SSH_BARE_USER_SCHEMES` through the predicate alone, so this
  unit names no scheme. Observed by AC1.

## 3. Non-goals (OUT)

- The read of a receipt that holds such a value: DEPL-dShippedRelease-97.
- A value that survives the strip: DEPL-dShippedRelease-99.
- Any new predicate: this unit calls TOOL-dSafePassage-38's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-63` — S1, whose scheme clause this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-25` — `derive_public_remote` and S4's value
- **hands-off** `DEPL-dShippedRelease-98` — `derive_public_remote`, the strip that unit's table drives
- **hands-off** `DEPL-dShippedRelease-99` — the strip's output, which that unit re-reads

## 4. Design

### Evidence

- TOOL-dSafePassage-44 §4 "Data model": a match is exempt when `scheme in SSH_BARE_USER_SCHEMES and ":" not in userinfo`, and `ssh://u:p@h/r` reads credential-bearing.
- The tuple is `("ssh", "git+ssh", "ssh+git")`, and the scheme is lowercased inside the predicate.
- Unit 25 S4: "its userinfo password stripped … no credential may survive it".

### Supersedes

- Unit 63 S1's "of any non-ssh scheme".
- Unit 63 AC2 stands: `ssh://git@example.invalid/g` is a bare user the predicate exempts.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1
- `tools/govkit/selftest.py`: the shapes of §6

## 5. Production-readiness checklist

- security — this is the write boundary of a value that ships into an adopter's tree, and the predicate is the one rule.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `derive_public_remote` over `ssh://u:tok@example.invalid/g` and
  `SSH://tok:x@example.invalid/g`, neither value holds `tok`, and each keeps `example.invalid`.
  Red when: a password on an ssh URL ships in a committed receipt.
- **AC2** — When it runs over `git+ssh://git@example.invalid/g`, the value comes back unchanged.
  Red when: a harmless ssh user is stripped.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the ssh shapes, their failing case the strip scoped to non-ssh schemes · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 22 (HIGH, item H7) of the round-2 spec audit.

## 10. Reuse audit

The seam reused is TOOL-dSafePassage-38's `test_credential_bearing` with TOOL-dSafePassage-44's exemption, specced and unbuilt at this base, called by `derive_public_remote` (unit 25 S4).
`python tools/codebase-map/reuse_lookup.py "strip the whole userinfo from a credential bearing remote url"`
ranked `resolve_remote`, `build_remote_ci_red_streak`, `set_gen_strip` and no strip of userinfo.
`resolve_remote` at `tools/govkit/govkit.py:558` is what unit 25 S4 reads. The recall probe surfaced
unit 63 and report item H7, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what makes an ssh url with a password credential bearing" --terms "test_credential_bearing SSH_BARE_USER_SCHEMES userinfo ssh password source_remote receipt strip derive_public_remote"`

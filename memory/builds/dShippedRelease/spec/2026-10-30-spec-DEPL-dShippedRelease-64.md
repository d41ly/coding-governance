# DEPL-dShippedRelease-64 — `check_release_field` reds any userinfo a shipped receipt holds, through a block the run-gates kit carries

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 19 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 92 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, which shares item H8 with id 46 (DEPL-dShippedRelease-63). Unit 25 S6 fails only a
`source_remote` that holds a password, and the shipped run-gates kit cannot reach
`tools/govkit/upgrade_steps.py` at an adopter. A receipt carrying a bare token passes the one
integrity check an adopter's own bar runs.

## 2. Scope (IN)

- **S1** — The block. `test_remote_userinfo(url)`, a canonical block in the new
  `tools/lib/remote_userinfo.py`, stem `remote_userinfo_py`, is true for a `<scheme>://` URL with
  userinfo on a non-ssh scheme. One `[[inline]]` row in `tools/lib/kit.toml`
  (DEPL-dShippedRelease-21 S8) carries it into `tools/run-gates/receipt_fields.py`. Observed by AC1,
  AC3.
- **S2** — The read. `check_release_field(receipt)` fails a `source_remote` for which the block is
  true, the same table of shapes DEPL-dShippedRelease-63 plants. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The write: DEPL-dShippedRelease-63.
- A repo-wide audit of URL classifiers: the audit's left-shift item, which no clause names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-25` — `check_release_field` and `receipt_fields.py`, the read this unit tightens
- **consumes-from** `DEPL-dShippedRelease-21` — `[[inline]]` rows and `inline_blocks.py --check`, without which the block is an unheld copy
- **consumes-from** `DEPL-dShippedRelease-63` — the plant table, so one list of shapes grades both ends

## 4. Design

### Evidence

- Unit 25 S6 places `check_release_field` in `tools/run-gates/receipt_fields.py`, a shipped file of a kit that imports no sibling (TOOL-dGroundRules-1).
- `tools/govkit/upgrade_steps.py` is TOOL-dSafePassage-38's home and does not ship to an adopter's `tools/run-gates/`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_remote_userinfo` | function, `tools/lib/remote_userinfo.py` | `py.function`, OK by `--suggest` at writing |
| `remote_userinfo_py` | inline block stem | none |

### Files touched (estimate)

- `tools/lib/remote_userinfo.py` (new): S1
- `tools/lib/kit.toml`: the `[[inline]]` row
- `tools/run-gates/receipt_fields.py`: S1, S2
- `tools/run-gates/check-receipt.py`: its fixture arm

## 5. Production-readiness checklist

- security — the read side of the same boundary; it runs on an adopter's bar with no gov checkout.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — two predicates hold one rule across the kit boundary; the shared plant table is what keeps
  them agreed, and it holds only the shapes it lists.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/check-receipt.py <scratch>` reads a planted schema-5
  receipt whose `source_remote` is `https://tok@example.invalid/g`, it prints `FAIL` and exits 1.
  Red when: a bare token passes the adopter's integrity check.
- **AC2** — When it reads `ssh://git@example.invalid/g`, or `git@example.invalid:g`, or
  `https://example.invalid/g`, it exits 0.
  Red when: a clean or ssh remote fails, so the check reds a correct install.
- **AC3** — When `python inline_blocks.py --rows` runs it prints `remote_userinfo_py`, and `--check`
  over a drifted copy exits 1 naming the file.
  Red when: the block is a second hand-held copy of the rule.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/run-gates/check-receipt.py · covers AC1 AC2 · the shape table, its failing case the password-only test · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 92 (HIGH, item H8) of the round-1 spec audit.

## 10. Reuse audit

The seam reused is TOOL-dSafePassage-38's `test_credential_bearing` with TOOL-dSafePassage-44's ssh
exemption, specced and unbuilt at this base.
`python tools/codebase-map/reuse_lookup.py "strip credentials from a remote url before recording it"`
ranked name-stem helpers (`before`, `records`, `resolve_remote`) and no redactor in the tree, so the
parent's predicate is the only seam. The recall probe surfaced TOOL-dSafePassage-44 and report item
H8, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a credential bearing remote url classified and redacted before it reaches a receipt" --terms "test_credential_bearing render_redacted_config userinfo remote token bare user receipt source_remote"`

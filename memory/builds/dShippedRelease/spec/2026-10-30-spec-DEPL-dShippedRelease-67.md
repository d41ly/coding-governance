# DEPL-dShippedRelease-67 — `install --all` selects through `resolve_selection`, the one selection `cmd_apply` already calls

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 23 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 45 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H11. Unit 17 S2 says the selection is `read_kit_rows(root, ids)` less a not-installable
row, while `resolve_selection` drops `selectable = "conditional"`, refuses an unknown id and prefers
a target's `deploy.toml` `kits`, and `cmd_apply` calls it itself at `tools/govkit/govkit.py:7532`.
Built as written, `install --all` takes three conditional kits, one of whose `why_conditional` says
a default install would red on install day, and two selections disagree in one process.

## 2. Scope (IN)

- **S1** — The verb. `cmd_install` passes `mode` and `kits` straight to `cmd_apply`, and
  `resolve_selection`, with unit 21 S6's `installable` read in it, is the one selection. Unit 17
  S2's `read_kit_rows` selection sentence is superseded. Observed by AC1, AC2, AC3.
- **S2** — The order stays `derive_install_order`. `read_kit_rows` is what AC4 compares it with, so
  unit 17 keeps what it takes from unit 10, and the pair of edges is restated on that. Observed by
  AC4.
- **S3** — `spec-9:33` and `spec-21:80` say unit 17 reads `read_kit_rows`; both are read as
  superseded by S1. Observed by AC1.

## 3. Non-goals (OUT)

- A new selection mode.
- Unit 21 S6's refusal text: it stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — `read_kit_rows`, the order AC4 compares the walk with
- **consumes-from** `DEPL-dShippedRelease-17` — `cmd_install`, whose S2 sentence this unit supersedes, and the walk over `one_pass`
- **consumes-from** `DEPL-dShippedRelease-21` — `installable` read inside `resolve_selection`, the rule S1 relies on

## 4. Design

### Evidence

- `tools/govkit/govkit.py:906` derives `all_kits`, leaving out `selectable = "conditional"`; `:7532` has `_cmd_apply` call `resolve_selection(reg, descs, mode, kits, deploy)`.
- Report id 45 counts three descriptors at `selectable = "conditional"`: check-install-prefix, check-line-length and check-placeholders.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1
- `tools/govkit/kit_walk.py`: the plants of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — the verb gains no read.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — `help/install.md`'s statement of `--all` already reads as this behaviour.

## 6. Acceptance criteria

- **AC1** — When `python kit_walk.py --fixture --plant empty-repo` runs `install --all`, no
  `CONFIGURE` line names `check-line-length`.
  Red when: a conditional kit lands on a default install.
- **AC2** — When `--plant kits-lib` runs `install --kits lib`, it exits 2 naming the reason unit 21
  S6 states.
  Red when: a not-installable id is silently filtered.
- **AC3** — When `--plant target-kits` plants a `deploy.toml` naming two kits and runs `install`
  with no flag, exactly those two install.
  Red when: a no-flag install ignores the target's kits.
- **AC4** — When `python kit_walk.py --fixture --plant install-order` runs, the `CONFIGURE` lines
  read in the order `read_kit_rows` returns for that selection.
  Red when: the install order and the descriptors' order disagree.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/kit_walk.py · covers AC1 AC2 AC3 AC4 · the four plants, their failing case a second selection in `cmd_install` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 45 (HIGH, item H11) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is `resolve_selection`, read at `tools/govkit/govkit.py:7532`.
`python tools/codebase-map/reuse_lookup.py "resolve a kit selection dropping conditional entries and refusing unknown ids"`
ranked `resolve`, `ids`, `resolve_kit_dir` and `inventory_ids`, name-stem hits, and a read of govkit
found the seam by name. The recall probe surfaced unit 17 and report item H11, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a default install choose kits and what keeps a conditional kit out of all" --terms "resolve_selection conditional selectable all_kits install order deploy.toml kits installable"`

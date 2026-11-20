# TOOL-dHomeGraded-2 — `govkit update` reaps a retired row that a live row at the same path supersedes

**Status:** CLOSED · rev-1 · 2026-11-20 · node d · Tier-1 · base e52614f4 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A receipt carries one row per path. `apply --kits playbook-render` writes the charter template as an
`engine` row at the path the retired `playbook` seed rule wrote, the seed's `retired-edited` row
stays, and `install.sums` then lists two hashes for one file, one of bytes the tree no longer holds.

## 2. Scope (IN)

- **S1** — On a `--write` run, `govkit update` drops every `retired-edited` row whose path a row of
  another role also carries, and prints one `reaped` line per row. Observed by AC1.
  **Readers:** by name: `write_install_receipt`, which derives `install.sums` from the rows ·
  by value: `cmd_check`, which asserts install.sums against the receipt row for row.

## 3. Non-goals (OUT)

- A `retired-edited` row no live row claims: it still keeps the target's bytes, as before.
- `apply` itself: the reap runs where every receipt row is already graded, on the next `update`.

### Edges

none

## 4. Design

The reap sits after the withdrawn rows leave and before the receipt is written, so it reads the
rows this run settled. A path is live when a row of any role but `retired-edited` carries it; a
`retired-edited` row at a live path describes bytes the live row now owns. A read-only run prints
nothing and changes nothing.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

## 5. Acceptance criteria

- **AC1** — When `govkit update --write` runs against a target whose receipt carries an `engine` row
  and a `retired-edited` row for one path, the re-stamped receipt and `install.sums` carry only the
  `engine` row, and the run prints `reaped` naming the path. Red when: the unchanged govkit runs,
  which kept both rows, as it did at nicocares' re-adoption to e52614f4.

## 6. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `step-rows-frozen` · `step-gate` · `docs` · `help page commands` · `upgrade-walk` · `playbook render selftest` · `policy fixtures`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-20 · initial draft.

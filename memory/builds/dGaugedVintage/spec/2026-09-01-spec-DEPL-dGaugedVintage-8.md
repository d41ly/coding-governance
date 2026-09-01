# DEPL-dGaugedVintage-8 — the stamp must not outrun the rows it never graded

**Status:** CLOSED · rev-4 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 1 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-8-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-8-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`update --write` advances `receipt["gov_commit"]` to `to_commit` unconditionally, including over rows
carrying `evidence: "unattributed"`. Those rows are graded against the receipt's OWN base, so every
write moves the base they would have to be attributed from further away. Stop the stamp advancing
past rows the run never graded.

## 2. Scope (IN)

- **S1** — `update --write` REFUSES to advance `receipt["gov_commit"]` while any row carries
  `evidence: "unattributed"`, unless the operator passes `--allow-ungraded`. The refusal names the
  count and the existing remedy.
- **S2** — Under `--allow-ungraded` the run proceeds and states in its output that it advanced the
  stamp over N ungraded rows, so the choice is on the record rather than silent.
- **S3** — A regression gate: a fixture receipt carrying one `unattributed` row, asserting
  `update --write` leaves `gov_commit` at its stored value without the flag and advances it with.

## 3. Non-goals (OUT)

- **A re-attribution pass.** rev-1 and rev-2 scoped one; it already exists. `_cmd_adopt` calls
  `derive_attribution` (`tools/govkit/govkit.py:6525`) for every unpinned destination and writes
  `evidence: "vintage-match"` on a hit, so `govkit adopt --re-adopt --write` IS that pass — and
  `update` already prints the remedy naming it at `:5589`, put there by
  `DEPL-dCarriedReceipt-13` S7 and corrected by that unit's D14.
- Changing what `adopt` records for a row matching no gov vintage. `DEPL-dCarriedReceipt-13`
  ratified `evidence: "unattributed"` with neither `commit` nor `gov_oid`.
- Writing bytes to an `unattributed` row. The skip at `:5529` is the safe path and survives.
- Changing `classify_row`'s verdict grid, or the tally's existing labels.

## 4. Design

### The one thing that is missing

`_cmd_update`'s three mutating branches never touch an `unattributed` row — the skip at `:5529`
`continue`s before `classify_row`. But the stamp at `:6204` is unconditional:
`receipt["gov_commit"] = to_commit`. So a target with ungraded rows drifts: the rows stay where they
are while the base recedes, and `adopt --re-adopt`'s walk is bounded by a commit ever further from
the vintage those bytes actually came from.

### Inventory

| Site | Today | After |
|---|---|---|
| `:5529` skip | `unattributed` rows `continue` before `classify_row` | unchanged |
| `:5589` remedy | names `adopt --re-adopt --pin … --write` | unchanged |
| `:6204` stamp | `receipt["gov_commit"] = to_commit`, unconditional | guarded by S1 |
| `--allow-ungraded` | does not exist | new flag on `update` |

### Rollout

S1 changes an exit condition an existing adopter will meet, so the flag ships in the same commit and
the refusal message names it. The refusal fires only under `--write`; a read-only run is unaffected.

### Alternatives rejected

Refusing the whole run rather than only the stamp: the byte-level work `update` did is correct and
worth keeping, and discarding it would punish the operator for a state `adopt` recorded honestly.

## 5. Production-readiness checklist

- security — N/A. No new write path; this removes one conditionally.
- perf / scale — one pass over rows already in memory.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a receipt with zero `unattributed` rows takes the unchanged path
  and gains no output.
- observability — S2 is the observable: the override says what it overrode.
- risks — an adopter mid-update meets a new refusal. Mitigated by the flag shipping with it, named
  in the message.
- testing + left-shift gates — S3, observed RED first.
- migration / rollback — none. No stored shape changes.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains a line on the guard and its override.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py update --write` runs against a receipt holding at
  least one `unattributed` row without `--allow-ungraded`, it REFUSES to advance the stamp, names the
  count, and `.governance/install.json`'s `gov_commit` is unchanged.
- **AC2** — When `--allow-ungraded` is passed, the same run advances `gov_commit` and its output
  states it did so over N ungraded rows.
- **AC3** — When a receipt holds no `unattributed` row, `python tools/govkit/govkit.py update
  --write` advances the stamp exactly as it does today, and its output gains no new line.
- **AC4** — A read-only `python tools/govkit/govkit.py update` is unaffected by the guard in both
  populations.
- **AC5** — The S3 arm is observed RED before the guard lands: run it at this base and confirm the
  stamp advances over an `unattributed` row.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`. This unit
adds the S3 arm to `tools/govkit/selftest.py`.

## 8. Open questions

- **F1 — the flag's spelling.** `--allow-ungraded` reads as a decision; reusing a general force flag
  would also disable guards this unit does not own. RESOLVED (agent, 2026-09-01, delegated):
  `--allow-ungraded`. `prior:` no prior ruling found.
- **F2 — whether the guard also covers `adopt --write`.** `adopt` WRITES the unattributed rows, so it
  is the verb that CREATES the state rather than one that outruns it, and guarding it would refuse
  the very run that records the state honestly. RESOLVED (agent, 2026-09-01, delegated): no.
  `prior:` `DEPL-dCarriedReceipt-13` ratified adopt's recording of that state.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit L1.
- rev-3 · 2026-09-01 · NARROWED at build time. rev-1 and rev-2 scoped a re-attribution pass that
  already ships: `_cmd_adopt` calls `derive_attribution` at `:6525` and `update` prints the remedy
  naming it at `:5589`. Building it would have been a second answer to one question. What survives
  is the stamp guard, which nothing addresses. F1 resolved to `--allow-ungraded`.
- rev-4 · 2026-09-01 · BUILT and CLOSED. F2 resolved (agent, delegated). Acceptance ledger at
  `build/2026-09-01-build-DEPL-dGaugedVintage-8-acceptance-ledger.md`.

## 10. Reuse audit

- The seam is the receipt stamp at `tools/govkit/govkit.py:6204` inside `_cmd_update`, and the
  existing `evidence` field the skip at `:5529` already reads; the guard adds no walk and no new
  data. `python tools/codebase-map/reuse_lookup.py "derive attribution for a receipt row against gov
  history"` ranks `derive_attribution` and the `derive_*` family in that same file — which is how
  rev-3 found that the pass rev-1 wanted was already there.
- Recall terms used: `govkit receipt attribution unattributed forked role landable classify_row
  gov_oid vintage update adopt evidence`

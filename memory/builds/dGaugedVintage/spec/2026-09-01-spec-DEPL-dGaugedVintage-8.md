# DEPL-dGaugedVintage-8 — a way out of `unattributed`, and a stamp that cannot outrun it

**Status:** OPEN · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

Give a receipt row recorded `evidence: "unattributed"` a path back to being graded, and stop
`update --write` from moving `gov_commit` forward past rows it never graded. Today half of a real
adopter's receipt is permanently ungraded and the base that could grade it recedes on every run.

## 2. Scope (IN)

- **S1** — A re-attribution pass over stored `unattributed` rows, reachable from `update`. It runs
  the same walk `adopt` runs, bounded by the receipt's OWN `gov_commit` rather than by `to_commit`,
  and promotes a row that now attributes. A row that still matches no vintage stays `unattributed`.
- **S2** — `update --write` REFUSES to advance `receipt["gov_commit"]` while any row is
  `unattributed`, unless the operator passes an explicit opt-out flag. The refusal names the count
  and the verb that clears it.
- **S3** — The `update` tally line distinguishes "skipped because unattributed" from "graded", and
  states how many of the unattributed rows the re-attribution pass could promote if run.
- **S4** — A regression gate over the CLASS: a fixture receipt carrying one attributable and one
  genuinely unattributable row, asserting the first promotes and the second does not.

## 3. Non-goals (OUT)

- Changing what `adopt` records for a row that matches no gov vintage. `DEPL-dCarriedReceipt-13`
  ratified that shape and this unit does not reopen it.
- Writing bytes to an `unattributed` row. The skip in `govkit.py:5529` is the safe behaviour and
  survives; only the exit from the state is new.
- Re-attributing against any base other than the receipt's own `gov_commit`. Walking from a newer
  base is how a row gets attributed to a vintage it never came from.
- Any change to `classify_row`'s verdict grid. Follow-up: `DEPL-dGaugedVintage-9`.

## 4. Design

### Data model

A receipt row's attribution is three fields written together or not at all: `evidence`, `commit`
and `gov_oid`. `adopt` writes `evidence: "unattributed"` with the other two absent when its walk
matches no gov vintage. Promotion means filling all three, so the row becomes indistinguishable
from one `adopt` attributed on its first pass.

### Inventory

| Site | Today | After |
|---|---|---|
| `govkit.py:5529` | `unattributed` rows `continue` before `classify_row` | unchanged; the skip is the safe path |
| `govkit.py:6204` | `receipt["gov_commit"] = to_commit`, unconditional | guarded by S2's refusal |
| `derive_attribution` | called by `adopt` only | also called by the S1 pass, bounded by the stored `gov_commit` |

### Rollout

The re-attribution pass is read-only in the same way `update` is: it reports under no flag and
writes under `--write`. S2's refusal is the behaviour change an existing adopter will notice, so it
ships with the opt-out flag in the same commit and the refusal message names it.

### Alternatives rejected

Re-running the full `adopt` walk on every `update` was rejected on cost: `derive_attribution` spawns
one `git log` per destination, measured at 65 ms per file on current bytes and 125 ms on stale ones,
so a 95-row receipt pays seconds on every update for a state most rows are not in. Scoping the walk
to rows already marked `unattributed` pays it only where it can change an answer.

## 5. Production-readiness checklist

- security — N/A. No new write path to target content; the only new write is to `.governance/`.
- perf / scale — the pass is bounded by the unattributed subset, not the receipt. Measured basis in §4.
- a11y — N/A. A CLI verb.
- i18n — N/A.
- error / empty / loading states — a receipt with zero unattributed rows must print that it ran and
  found none, never nothing; a vacuous pass that prints nothing reads as a pass that did not run.
- observability — the S3 tally is the observable; it names both counts on every run.
- risks — the S2 refusal can block an adopter mid-update. Mitigated by the opt-out flag shipping in
  the same commit. No data-loss path: promotion only fills absent fields.
- testing + left-shift gates — S4, and it is the gate this unit adds.
- migration / rollback — none. An existing receipt is read as-is; promotion is additive.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains the re-attribution step in the update sequence.

## 6. Acceptance criteria

- **AC1** — When a receipt carries a row with `evidence: "unattributed"` whose bytes DO match a gov
  blob at the receipt's own `gov_commit`, the re-attribution pass promotes it: `evidence`, `commit`
  and `gov_oid` are all written, observed by re-reading `.governance/install.json`.
- **AC2** — When a row matches no vintage at the stored `gov_commit`, it stays `unattributed` and
  no `commit` or `gov_oid` is invented, observed on the same fixture.
- **AC3** — When `update --write` runs against a receipt holding at least one `unattributed` row and
  no opt-out flag, it REFUSES, names the count, and leaves `gov_commit` at its stored value.
- **AC4** — When the opt-out flag is passed, that same run advances `gov_commit` and says in its
  output that it did so over N ungraded rows.
- **AC5** — When `update` runs read-only against a receipt with zero unattributed rows, the tally
  still prints the unattributed count as `0` rather than omitting the line.
- **AC6** — The new gate leg from S4 is observed RED before the fix lands: stage the promotion
  branch out, run `bash tools/run-gates/run-gates.sh` scoped to that leg, and confirm it fails on
  the attributable fixture row.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `govkit selfcheck` and `govkit acceptance matrix` legs in
particular. This unit ADDS the S4 leg to `tools/gate-legs.json` with a declared `ceiling`.

## 8. Open questions

- **F1 — the opt-out flag's spelling and its default.** Options: `--allow-ungraded` (explicit, reads
  as a decision) or reusing an existing `--force`-shaped flag if one exists. Recommendation:
  `--allow-ungraded`, because a general force flag would also disable guards this unit does not own.
  Unresolved.
- **F2 — whether the re-attribution pass is a distinct verb or a phase of `update`.** A distinct
  verb is discoverable and testable in isolation; a phase means an adopter cannot forget it.
  Recommendation: a phase of `update` that reports always and writes only under `--write`, with no
  new verb. The evidence is this build's own triage: a five-lens manual audit ran where `govkit
  adopt` and `update` would have answered, so a further verb is a discoverability cost already paid
  once here. `prior:` no prior ruling found. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit L1. F2 justified its recommendation by citing
  `DEPL-dGaugedVintage-2`, which says nothing about verb discoverability; replaced with this build's
  own measured finding and a `prior:` line.

## 10. Reuse audit

- The seam is `derive_attribution` in `tools/govkit/govkit.py`, the walk `adopt` already runs;
  `python tools/codebase-map/reuse_lookup.py "derive attribution for a receipt row against gov
  history"` ranks it alongside `classify_row` and the `derive_*` family in that same file, all
  fan-in 1, so this unit extends an existing private seam rather than adding one.
- Recall terms used: `govkit receipt attribution unattributed forked role landable classify_row
  gov_oid vintage update adopt evidence`

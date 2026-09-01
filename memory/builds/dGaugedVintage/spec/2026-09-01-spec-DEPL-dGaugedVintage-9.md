# DEPL-dGaugedVintage-9 — report the per-kit version delta the receipt already stores

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every receipt row stores the kit version it was written at, and nothing in gov ever reads it back.
`entry_version` resolves gov's own constant, never the target's, so no verb can answer "which of my
kits are behind, and by how much" — the question an adopter actually asks before an update.

## 2. Scope (IN)

- **S1** — A per-kit delta report: for each entry in a target's receipt, the version its rows were
  written at, gov's version now, and whether they differ. Read from the stored rows, never re-derived
  from the target's bytes.
- **S2** — The report is available without writing, from a verb an adopter already runs before an
  update, so it costs no extra step.
- **S3** — A row whose stored version is ABSENT is reported as unknown, distinctly from equal. A
  receipt written before the field existed must not read as current.

## 3. Non-goals (OUT)

- Reading a version out of the target's own installed BYTES. That is the marker question and it
  belongs to `DEPL-dGaugedVintage-5`, which must land before a byte-side read is even possible for
  four entries.
- Deciding what to DO about a delta. This unit reports; `update` already owns the acting.
- Changing the receipt schema. The field is present and populated; only the reader is missing.
- Per-FILE version deltas. The version is an entry-level fact and rows share it.

## 4. Design

### Data model

`apply` writes `version` onto every landed row from `entry_version` at `tools/govkit/govkit.py:333`,
which resolves the constant out of the GOV checkout at apply time. So a row's `version` is "what gov
was at when this row landed" — exactly the left half of a delta, already stored and never read.

### Inventory

| Fact | Where | Consequence |
|---|---|---|
| `version` written per row | `govkit.py:4093-4095` | the stored half exists |
| `entry_version` resolves gov only | `govkit.py:333-347` | the live half exists |
| no reader joins them | measured: no call site compares the two | the delta is underivable today |

### Rollout

Report-only, so it can land before `DEPL-dGaugedVintage-5` without depending on it. When that unit
lands, a byte-side cross-check becomes possible and is a follow-up rather than a revision here.

### Alternatives rejected

Deriving the target's version by grepping its installed files was rejected as the FIRST cut: it is
undecidable for the four entries carrying no marker, so it would report unknown for them while the
receipt already holds the answer.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — a dictionary join over rows already loaded; no new I/O.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a receipt with no `version` on any row reports every entry
  unknown, and says the receipt predates the field, rather than printing an empty table.
- observability — this unit IS an observability change.
- risks — a stored version is a claim about what gov shipped, not about the target's current bytes.
  The report must say which it is, or a reader will take it for a byte-level verdict.
- testing + left-shift gates — AC4 is the failing case; the arm joins the acceptance matrix.
- migration / rollback — none; read-only over an existing field.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains the delta read in the pre-update sequence.

## 6. Acceptance criteria

- **AC1** — When the delta report runs against a receipt whose rows carry a version older than
  gov's, it names that entry with both values, observed on the fixture in
  `tools/govkit/fixtures/`.
- **AC2** — When stored and live versions are equal, the entry is reported level rather than
  omitted by `python tools/govkit/govkit.py update`, so a green read is distinguishable from an
  entry that was not examined.
- **AC3** — When a row carries no `version` key, the entry reports unknown and the output states the
  receipt predates the field, observed by deleting the key on a fixture.
- **AC4** — The report is observed to change when gov's constant moves: bump a constant on a scratch
  branch, re-run, and confirm the delta appears where `python tools/govkit/govkit.py selfcheck`
  reports the same constant.
- **AC5** — The report writes nothing: `git status --short` in the target is empty after a run.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`.

## 8. Open questions

- **F1 — which verb carries the report.** Options: a flag on `check`, a flag on `update`, or a new
  verb. Recommendation: a flag on `update`, because an adopter already runs `update` read-only before
  writing, and `DEPL-dGaugedVintage-2` shows a new verb is a discoverability cost this repo has
  already paid once. Unresolved.
- **F2 — whether an entry present in gov but absent from the receipt is in scope.** It is a
  not-adopted entry, not a stale one, and `plan --coverage` already answers it. Recommendation:
  out of scope, named in §3 as such if the reviewer agrees. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- The seam is `entry_version` at `tools/govkit/govkit.py:333`, which already resolves gov's half of
  the comparison and is called by `apply` when stamping rows; this unit adds the join rather than a
  second resolver. `python tools/codebase-map/reuse_lookup.py "assert every gov kit version marker
  site against its descriptor"` ranks `read_descriptors` in the same file as the descriptor-aware
  entry point, and `coverage_rows` at `:2051` is the existing precedent for a read-only join over a
  receipt.
- Recall terms used: `govkit receipt attribution unattributed forked role landable classify_row
  gov_oid vintage update adopt evidence`

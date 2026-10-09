# TOOL-aHomedAnchor-7 — the closing review's leg minors, batched

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 40a976d9 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close every MEDIUM and LOW of round 1 whose write set is the bar leg and its suite: M2, M10, L3 and
L4 of `memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md`.

## 2. Scope (IN)

- S1. M2: check 9's local admission sets a per-record flag, reset for each record; the check 19
  `may:` arm and the `asks:` mandate arm red a record carrying that flag and a grant or a mandate,
  each with its own message. Observed by AC1.
- S2. M10: an arm moves `refs/heads/main` and `refs/remotes/origin/main` to a commit declaring
  `local` without pushing, and check 9 still refuses. Observed by AC2.
- S3. L3: `read_origin_scope` accepts an `export` prefix and returns empty, the strict reading, when
  any assignment line for the key carries a `$` or a backtick. Observed by AC3.
- S4. L4: check 29's local skip is nested under its off-default condition, so a default-branch
  record prints nothing. Observed by AC4.

## 3. Non-goals (OUT)

The driver: `TOOL-aHomedAnchor-6`. A README-at-BASE `spec-audit:` second opinion: the leg has none
for any anchor today.

### Edges

none

## 4. Design

The flag lives in the per-record loop beside `rb`, so a guard reads a fact check 9 derived from the
advertisement, never one the record states.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

## 5. Production-readiness checklist

- security — M2 restores the second opinion on D12-j and D12-a for local records.
- perf / scale — N/A — one flag per record.
- error / empty / loading states — N/A.
- observability — L4 removes report noise.
- risks — N/A — every change narrows or arms.
- testing — AC1 to AC4.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When a local-admitted slug record pins `may:` or `asks:`, `check-unattended.sh` prints
  fail 19's `a BASE the local anchor admitted` text for each. Red when: mode alone clears them.
- **AC2** — When local refs, not the advertisement, carry `ANCHOR_SCOPE="local"`, check 9 prints
  `is not published on the remote`. Red when: the reader takes a run-writable ref.
- **AC3** — When `read_origin_scope` reads `export ANCHOR_SCOPE="local"` it answers `local`, and for
  an assignment spelled through `${X:-local}` it answers empty. Red when: a shape the shell reads
  differently passes.
- **AC4** — When origin declares `local` and a record's BASE is on the default branch, the report
  channel carries no `check 29 skipped` line for it. Red when: the skip fires for every record.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 AC3 AC4 · a local-scope origin with a grant, a mandate, diverged local refs and conf shapes · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the round 1 minors batch.

## 10. Reuse audit

Each fix extends the site the review names, so no existing seam fits anything new; the parse keeps
`read_rounds_of`'s shape. Recall terms
used: `--terms "check-unattended check 9 check 19 may grant asks mandate D12-j D12-a ORIGIN_SCOPE
read_origin_scope advertisement"`.

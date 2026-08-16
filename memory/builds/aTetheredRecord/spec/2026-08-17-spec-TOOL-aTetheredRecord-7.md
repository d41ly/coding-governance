# TOOL-aTetheredRecord-7 — the rename: every record filename names a spec

**Status:** SPECCED · rev-1 · 2026-08-17 · node a · Tier-1 · base 96141aed · streams tooling

## 1. Goal

Carry out the rename Fork A ratified. Every record under a build's non-spec folders takes a filename
whose family and ordinal name a spec its own binding line lists, and every reference to an old name
is repaired in the same commit as the move that broke it.

## 2. Scope (IN)

- **S1** — Derive the rename map from the committed bindings, never by hand: for each record, the
  target name is its kind, the family and ordinal of the lowest id its binding line lists, and a tail
  distinguishing records that would otherwise collide. Commit the map as a record before moving
  anything.
- **S2** — Move the records with `git mv`, in build-sized batches.
- **S3** — Repair every reference in the same commit as its move. Measured at BASE: 107 referencing
  lines across 65 citing files, of which 5 carry markdown links `check 2` validates and the rest are
  backticked path or bare-name citations.
- **S4** — Update the two rows of `memory/project/legacy-files.txt` whose paths this rename moves,
  and re-measure whether either record still needs its exemption once it carries a conforming name.
- **S5** — Records whose binding line reads `none` keep their build-scoped ordinal; the map records
  that they were considered and why they are unmoved.

## 3. Non-goals (OUT)

- **No spec renames.** A spec filename already carries family, slug and ordinal — specs were never
  the defect.
- **No content edit.** Renaming a record does not license editing what it says.
- **No grammar change.** The ordinal is redefined in `TOOL-aTetheredRecord-4` §4 and the recording
  grammar keeps its exact shape; this unit renames files to fit the grammar that already exists.
- **No repair of citations in append-only areas** — measured zero, so the case does not arise. If the
  measurement moves before this unit runs, a citation in an append-only file is superseded, never
  edited, and the discrepancy is recorded rather than silently fixed.

## 4. Design

### Ordering, and why the moves and the repairs share a commit

A rename and its reference repair in two commits leaves one commit where the tree's links are broken,
and `check 2` reds on any markdown link that stops resolving. Batching by build keeps each commit
small enough to review while never leaving a red intermediate state.

The rename runs AFTER `TOOL-aTetheredRecord-3`, because the target name is derived from the binding
line and there is nothing to derive from until the bindings exist. It runs BEFORE
`TOOL-aTetheredRecord-4`, so branch 4 lands on a corpus that already satisfies it — the same
fixed-then-gated ordering the rest of this build uses.

### Inventory

| Quantity | Measured at BASE | How |
|---|---|---|
| records in scope | the full non-spec population | `git ls-files` over a build's three record folders |
| referencing lines to repair | 107 | a fixed-string search per basename over the memory tree, excluding the record itself |
| distinct citing files | 65 | the same search, counted by file |
| markdown links among them | 5 | the subset `check 2` validates and would red on |
| citations in append-only areas | 0 | the subset that could NOT be legally repaired |
| rows in the legacy-name registry affected | 2 | both are records this rename moves |

### Migration

Per batch: derive targets from the map, `git mv`, repair that batch's references, re-render the
index, run the hygiene gate, commit. The map is committed first so a reviewer can grade the naming
decisions separately from the mechanical moves.

### Alternatives rejected

**One big commit.** 107 repairs across 65 files in a single diff is unreviewable, and a mistake in it
is indistinguishable from a mistake in the map.

**Rename first, repair after.** Leaves a commit whose links are broken and whose gate is red, which
this build has avoided everywhere else.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — a bounded set of moves and text repairs.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a record whose binding is `none` has no id to project and keeps its
  current name; that case is in the map, not an exception to it.
- observability — the committed map is the record of what moved and why.
- risks — the dominant risk is a BROKEN REFERENCE that no gate sees: only 5 of the 107 are markdown
  links `check 2` validates, so the other 102 are prose or backticked citations that can rot silently.
  The mitigation is that the repair rides the same commit as its move and the map is derived, not
  hand-listed. The second risk is a collision when two records project to one name, which the tail
  resolves and the map makes visible.
- testing + left-shift gates — branch 4 of check 21 is what stops the discipline decaying after this
  unit; without it the rename would be a one-time tidy.
- migration / rollback — per-batch commits, each revertible; `git mv` preserves history.
- user docs — the redefinition is documented by `TOOL-aTetheredRecord-4`; this unit writes no prose.

## 6. Acceptance criteria

- **AC1** — When the rename map committed by S1 is read, every target name is derived from the
  record's own binding line, and every record whose binding is `none` is listed as deliberately
  unmoved with its reason.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs after each batch, it is green
  — `check 2` in particular, which is what a broken markdown link reds.
- **AC3** — When a fixed-string search for each OLD basename runs over `git ls-files -- memory/`, it
  returns nothing outside the append-only areas.
- **AC4** — When `git log --follow` is run over any renamed record, its history predates the rename —
  the moves used `git mv` and did not orphan provenance.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --check` runs after each batch, it is
  clean, and `memory/project/legacy-files.txt` names no path that no longer exists.
- **AC6** — When `bash tools/run-gates.sh` runs at every commit in the sequence, it is green.

## 7. Gates

`memory hygiene (20 checks)` — checks 2, 4 and 5 in particular · `build-index selftest` ·
`bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none. Fork A is RESOLVED (owner, 2026-08-17) on `TOOL-aTetheredRecord-4` §8, which is where the
option set and the reasoning live; this unit is its execution and states no fork of its own.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, created by the owner's Fork A resolution. The unit did not
  exist at rev-1 of the set: the design pass recommended against renaming, and the owner overrode it.

## 10. Reuse audit

The rename derives its targets from `TOOL-aTetheredRecord-2`'s binding parser rather than from a
second naming convention, so there is exactly one place that decides which spec a record belongs to.
The recording-name grammar it renames INTO is the one `check 5` already enforces, unchanged — see
`TOOL-aTetheredRecord-4` §4 for why the ordinal's redefinition needs no grammar edit. No new seam.
Recall terms: `build slug spec artifact filename header adversarial review closeout journal
bookkeeping convergence naming hygiene`.

# TOOL-dGroundRules-28 — the historical-sha oracle class widened to HEAD, so a spec driving the deployer from gov's tree is handed it

**Status:** CLOSED · rev-2 · 2026-10-24 · node d · Tier-1 · base 3708a705 · streams tooling · order 4 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-28-deviation-16.md](../build/2026-10-23-build-TOOL-dGroundRules-28-deviation-16.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-28-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-28-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-28-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-28-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-29 TOOL-dGroundRules-27 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 23 at HIGH**, which shares item **H1** with id 1
(`TOOL-dGroundRules-26`) and id 7 (`TOOL-dGroundRules-27`). Id 23 is H1 seen from the failure
envelope: the gate runner records the case's green against the working tree, so the check certifies
bytes it never read. This unit is id 23's promotion and the item's left-shift, which BUILD-METHOD M8
requires of every confirmed finding: the bug-class record `test-oracle-read-from-a-historical-sha`
is widened from a literal sha to HEAD and anchored on the files that drive the deployer, so
`gotchas.py --for-paths` hands it to the next spec or review that touches them. It repairs
`TOOL-dGroundRules-24`, which sits at order 3, so it builds at order 4.

## 2. Scope (IN)

- **S1** — The description. The record's front-matter `description` names both shapes: a literal
  sha that rots on the next legitimate edit, and HEAD read while the runner records the verdict
  against the working tree. Observed by AC3.
- **S2** — Where it bit. A paragraph names this audit's H1: the policy kit's fresh-target case ran
  `apply` from `tools/govkit/govkit.py`, whose `blob_at` reads HEAD, from `tools/policy/check_policy.py`,
  and `tools/govkit/matrix.py` applies the same way; `TOOL-dGroundRules-26` and `TOOL-dGroundRules-27`
  are the repair. Those three backticked paths are the record's new anchors. Observed by AC1, AC2.
- **S3** — The fix and the documented check. "The fix" gains the second shape: install from a commit
  of the working tree made in a scratch clone (`build_source_snapshot`), or refuse naming the dirty
  paths, and never grade HEAD silently. The documented check gains one question for a spec that
  drives `govkit apply` from gov's own tree: which revision does it install. Observed by AC3.
- **S4** — The index. `memory/gotchas/INDEX.md` is regenerated with
  `python tools/memory-tree/gotchas.py --write`. Observed by AC3.

## 3. Non-goals (OUT)

- The repair of the case: `TOOL-dGroundRules-26` and `TOOL-dGroundRules-27`.
- A machine gate for the class. The record keeps its "No machine gate" reason: a literal sha or a
  HEAD read in a test is sometimes the subject itself.
- A new class record. The shape is the existing class's with a moving revision, so the existing
  record is widened rather than copied.

### Edges

- **hands-off** `TOOL-dGroundRules-34` — the HEAD paragraph of `test-oracle-read-from-a-historical-sha`, which that unit points at `suite-invalidated-by-a-commit-under-it` for the false-green shape (id 21 of the round-1 spec audit of units 26 to 32)

## 4. Design

`tools/memory-tree/gotchas.py` derives a record's anchors from the backticked path-like tokens in
its body (its module docstring, lines 16-20), so S2's paragraph is what selects the record for the
three paths; no front-matter list is written. Before this unit,
`python tools/memory-tree/gotchas.py --for-paths tools/govkit/govkit.py tools/govkit/matrix.py`
printed 62 lines and none named the class (measured 2026-10-23, PINNED).

### Files touched (estimate)

- `memory/gotchas/test-oracle-read-from-a-historical-sha.md`
- `memory/gotchas/INDEX.md`

## 5. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths tools/govkit/govkit.py` runs, its
  output names `test-oracle-read-from-a-historical-sha`.
  Red when: the deployer's file selects no record of the HEAD-oracle class.
- **AC2** — When `python tools/memory-tree/gotchas.py --for-paths tools/govkit/matrix.py` runs, its
  output names the same class.
  Red when: the second apply-into-a-target harness is not handed the class.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0, and
  `grep -n "HEAD" memory/gotchas/INDEX.md` prints the class's row.
  Red when: the index still carries the literal-sha description only.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 23 (HIGH, item H1) of the round-1 spec
  audit of units 22 to 25 as the item's left-shift, with the record and `gotchas.py`'s anchor rule
  read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 9. Reuse audit

The seam extended is the record `memory/gotchas/test-oracle-read-from-a-historical-sha.md`, whose
class this defect is with a moving revision. `python tools/codebase-map/reuse_lookup.py "commit the working tree under test into a scratch clone so a tool reading HEAD sees uncommitted edits"`
ranked no record-writing seam, and the class was found by listing `memory/gotchas/`. The recall probe
returned this audit's H1 and `DEPL-dRatifiedSeam-6`, the govkit selftest grading commit topology
rather than the tree; both agree with widening the record.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture grade uncommitted working
tree bytes when the deployer reads HEAD" --terms "govkit apply blob_at HEAD working tree uncommitted
snapshot scratch clone fixture source revision"`

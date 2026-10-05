# TOOL-dThriftyLanding-8 — the runner's docs mode sees a doc path touched on a merged side branch

**Status:** OPEN · rev-1 · 2026-10-05 · node d · Tier-2 · base f765eb8e · streams tooling · order 8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing review's finding 1 (HIGH): `check_doc_moved` in `tools/run-gates/run-gates.sh` asks
`git log -1 <base>..HEAD -- <paths>` without `--full-history`, so git's default history simplification
prunes a `--no-ff` merge's side branch that is TREESAME to its first parent. A doc path edited and
restored on that side branch reads as unmoved, and a commit-grading leg is docskipped over commits that
land. This unit makes the read see every commit in the range.

## 2. Scope (IN)

- **S1** — `check_doc_moved`'s history read carries `--full-history`, so a side branch merged with
  `--no-ff` is walked whatever its net effect. Observed by AC1.
- **S2** — The function's comment states that the read is full-history and why. Observed by AC1.

## 3. Non-goals (OUT)

- The hook's own history read: `TOOL-dThriftyLanding-9`.
- Content introduced only by a merge resolution: the net diff half of the predicate already reads it.

### Edges

- **hands-off** `TOOL-dThriftyLanding-9` — the hook's read of the same range.

## 4. Design

### Evidence

Read at `f765eb8e`. Finding 1 reproduced it in a scratch repo: a side commit edits a doc path and a
second restores it, main takes a doc commit, and a `--no-ff` merge follows; the read prints nothing,
and with `--full-history` it prints the side commits.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`

### Alternatives rejected

- **`-m` in place of `--full-history`.** `-m` lists a merge's diff against each parent but does not stop the
  simplification that drops the side commits from the walk.

## 5. Production-readiness checklist

- perf / scale — no new process on the common path.
- security — narrows nothing the push boundary decides; each change makes a skip rarer or a check wider.
- error / empty / loading states — unchanged.
- observability — each refusal or decision names its reason.
- testing — each arm observed RED against `f765eb8e` first.
- migration — none.
- user docs — the carriers unit 6 wrote, where this unit's change touches them.
- risks — none beyond the finding's own.

## 6. Acceptance criteria

- **AC1** — When the canary's docs-mode fixture edits a declared doc path on a side branch, restores it,
  and merges the side with `--no-ff` past the docs base, the declaring leg prints `GATE ok`.
  Red when: the runner at `f765eb8e` prints `GATE skip` with `docs-only` for it.

## 7. Gates

`run-gates canary` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · a doc path touched only on a merged side branch, run against the f765eb8e runner · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · promoted from the closing diff review, round 1.

## 10. Reuse audit

The seam is the predicate unit 1 added; only its git call changes. The review record names the fix
and judged it sound. `python tools/codebase-map/reuse_lookup.py` cannot see `.sh`.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent

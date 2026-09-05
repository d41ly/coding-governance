# TOOL-dTracedLattice-3 — the reinvention backlog is tracked, or is not written into a tracked directory

**Status:** SPECCED · rev-1 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |

<!-- /gen:spec-records -->

## 1. Goal

`map_diff.py` writes `reinvention-backlog.md` into the tracked `memory/map/` tree unconditionally.
That file has never been tracked on any branch, is not gitignored, and therefore appears as untracked
clutter inside the memory tree after any `--converge` run. Three claims in `TOOL-aScouredKit-16`
describe it as tracked and shipping to adopters, and all three are false at HEAD.

## 2. Scope (IN)

- **S1** Decide and implement one of two dispositions for the file: tracked and rendered like every
  other map artifact, or written outside the worktree the way this repo already writes
  `gate-ledger.tsv` and `recall/queries.jsonl`. §8 carries the fork.
- **S2** Whichever disposition wins, `--converge` leaves the worktree in a state the memory-hygiene
  gate and `git status` both expect — no untracked file appearing inside a gated directory.
- **S3** Correct `TOOL-aScouredKit-16`'s three false clauses in place, since a backlog row is mutable
  and this one is cited as authority for work in this build.
- **S4** State in the kit README that nothing invokes `--converge` on this tree, so a reader does not
  infer that the convergence loop runs.

## 3. Non-goals (OUT)

- Not wiring `--converge` into the bar. Whether the closing loop should run at all is a separate
  question and this unit does not answer it.
- Not changing collision detection, its threshold, or its output — `TOOL-dTracedLattice-1` moves the
  precision that feeds it.
- Not draining the reinvention rows. There are none to drain, which is part of the finding.

## 4. Design

### Alternatives rejected

Adding the path to `.gitignore`. That leaves a tool writing a durable, deduped, append-only record
into a directory whose whole contract is that its contents are generated and compared, and it makes
the file invisible to the hygiene gate while remaining inside its root — which is the shape that let
this go unnoticed.

### Rollout

S3 first and alone: correcting a false claim costs nothing and stops the row misleading the unit that
cites it. S1 and S2 after the fork resolves.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a run producing no flags must not create an empty file.
- observability — the run already prints its flag count; it must also print where it wrote.
- risks — an adopter who HAS run `--converge` has an untracked file this change may relocate; the
  message must say so rather than deleting anything.
- testing + left-shift gates — an arm asserting the worktree is clean after `--converge` in a fixture
  repo, observed RED first.
- migration / rollback — no committed artifact exists to migrate, which is the finding.
- user docs — `tools/codebase-map/README.md`, per S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/map_diff.py <range> --converge` runs in a clean fixture
  worktree, `git status --porcelain` is empty afterwards, and this arm is observed RED before the fix.
- **AC2** — When the run produces zero flags, no `reinvention-backlog.md` is created.
- **AC3** — When the run produces flags, the stdout of `map_diff.py --converge` names the path it
  wrote them to.
- **AC4** — When `memory/backlog/TOOL.md` is read, `TOOL-aScouredKit-16` no longer claims the backlog
  is tracked, that the fiction is permanent, or that it ships to adopters.
- **AC5** — When `tools/codebase-map/README.md` is read, it states that no gate leg or script invokes
  `--converge` in this repository.

## 7. Gates

`codebase-map kit selftest` · `memory hygiene` · `dead-path carriers (deleted files still named)` ·
`harness arms (fail branches armed or pinned)`.

## 8. Open questions

- **Q1 — tracked artifact, or outside the worktree?** Tracked makes the rows durable, reviewable and
  shipped to adopters, at the cost of a new generated file under the freshness contract and a file
  that grows monotonically. Outside the worktree — under the git common dir, beside `gate-ledger.tsv`
  — keeps the tree clean and matches how this repo already stores per-run records, at the cost of
  rows that no review ever sees and that do not travel between nodes. Recommendation: outside the
  worktree, because the rows are a per-run report rather than a shared record, and because nothing
  currently runs `--converge` so no durable corpus is being lost. NOT RESOLVED — this changes a kit's
  shipped output contract, which is veto 2 in `memory/guides/BUILD-METHOD.md` M3, so it is an owner
  turn.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round.

## 10. Reuse audit

The seam is the existing out-of-worktree record convention, cited from
`python tools/codebase-map/reuse_lookup.py "write a per-run record outside the worktree"`, which
returns no seam above the threshold — the evidence being that the two live instances are spelled
inline at their call sites rather than shared: `tools/memory-recall/query.py` writes
`<git-common-dir>/recall/queries.jsonl` and the gate runner writes `gate-ledger.tsv` under the same
root. If Q1 resolves to the outside-the-worktree option, this unit follows that spelling and
deliberately uses `--git-common-dir`, not `--git-dir`, because the two differ in a linked worktree.

Recall terms used: converge reinvention backlog collision flags untracked worktree git-common-dir
map_diff append_backlog dedupe adopter shipped tracked

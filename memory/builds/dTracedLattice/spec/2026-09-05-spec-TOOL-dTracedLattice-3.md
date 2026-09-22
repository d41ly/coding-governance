# TOOL-dTracedLattice-3 — the reinvention backlog is tracked, or is not written into a tracked directory

**Status:** CLOSED · rev-6 · 2026-09-06 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 4 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-06-build-TOOL-dTracedLattice-3-1-acceptance-ledger.md](../build/2026-09-06-build-TOOL-dTracedLattice-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round3.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7 |
| [2026-09-06-review-TOOL-dTracedLattice-1-2-3-4-5-6-7-diff-review-round1.md](../reviews/2026-09-06-review-TOOL-dTracedLattice-1-2-3-4-5-6-7-diff-review-round1.md) | diff-review | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7 |
| [2026-09-06-review-TOOL-dTracedLattice-1-2-3-4-5-6-7-diff-review-round2.md](../reviews/2026-09-06-review-TOOL-dTracedLattice-1-2-3-4-5-6-7-diff-review-round2.md) | diff-review | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7 |

<!-- /gen:spec-records -->

## 1. Goal

`map_diff.py` writes `reinvention-backlog.md` into the tracked `memory/map/` tree unconditionally.
That file has never been tracked on any branch, is not gitignored, and therefore appears as untracked
clutter inside the memory tree after any `--converge` run. Three claims in `TOOL-aScouredKit-16`
describe it as tracked and shipping to adopters, and all three are false at HEAD.

## 2. Scope (IN)

- **S1** Write the reinvention backlog OUTSIDE the worktree, under the git COMMON dir. Ratified by
  the owner on 2026-09-05. The path is derived through `--git-common-dir` and never `--git-dir`,
  because the two differ in a linked worktree and the record must survive `git worktree remove`.
  **The tree is not uniform and rev-4 said it was.** ONE existing consumer uses `--git-common-dir`:
  `tools/memory-recall/query.py:233`, which states the reason at `:229`. The gate runner and the
  lander use `--git-dir` — `tools/run-gates/run-gates.sh:95` and `:158` for `gate-ledger.tsv`,
  `tools/push-main.sh:29` for the lander marker — so "beside `gate-ledger.tsv`" resolves to
  `.git/worktrees/<name>/` in a linked worktree and would RED this unit's own AC6. That phrasing is
  dropped rather than qualified. `run-gates.sh:421` uses `--git-common-dir` for a different purpose,
  which is why no single clause summarises the tree.
- **S2** `--converge` leaves the worktree in a state the memory-hygiene gate and `git status` both
  expect — no untracked file appearing inside a gated directory. Stated unconditionally: Q1 is
  RESOLVED and rev-4's "whichever disposition wins" left an owner ruling reading as an open guess.
- **S3** Supply the three corrections `TOOL-aScouredKit-16` needs — it is not tracked, the fiction is
  not permanent, it does not ship to adopters — to `TOOL-dTracedLattice-1`, which is the ONLY unit
  that edits that row. Two units amending one backlog row is what M6 clause 3 forbids, and rev-1 had
  both doing it.
- **S4** State in the kit README the TRUE claim, which is narrower than rev-1's: no gate leg and no
  hook runs `--converge` as a merge-bar step. It is not unreferenced — `WIRE-INTO-PROJECT.md`
  prescribes it, `reuse-lookup.agent.md:59` prescribes it to an agent at review time, and
  `selftest.py:220` invokes it as a refusal arm.

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

S3 first and alone: supplying the wording costs nothing and stops the row misleading the unit that
cites it. S1 and S2 after it — the fork is resolved, so nothing here waits on a decision.

**This unit and `TOOL-dTracedLattice-1` both write `tools/codebase-map/map_diff.py`, and that
collision cannot be removed — only sequenced.** Unit 1 owns the `fan_in` call at `:204` and the
dead-export figure at `:207`; this unit owns the backlog write path at `:171`, `:175` and `:187`,
inside the same `_converge` function. Rev-2 claimed the file was reassigned to unit 1, which moved
the collision rather than removing it. The build order puts unit 1 first and this unit rebases onto
it; neither may be dispatched concurrently with the other, per M6 clause 1.

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
  worktree, `git status --porcelain` is empty afterwards and no untracked file appears inside
  `memory/map/`. Observed RED before the fix. The unconditional spelling is correct now that the
  owner has ratified the outside-the-worktree disposition; rev-2 split this criterion in two only
  because the fork was open.
- **AC6** — When the same run happens inside a LINKED WORKTREE, the file lands under the git COMMON
  dir, asserted by an arm that resolves both `--git-dir` and `--git-common-dir` and shows the write
  followed the latter.
- **AC2** — When the run produces zero flags, no `reinvention-backlog.md` is created.
- **AC3** — When the run produces flags, the stdout of `map_diff.py --converge` names the path it
  wrote them to.
- **AC4** — When `TOOL-dTracedLattice-1` lands, `memory/backlog/TOOL.md`'s `TOOL-aScouredKit-16` row
  no longer claims the backlog is tracked, that the fiction is permanent, or that it ships to
  adopters. This unit supplies the wording per S3 and does not edit the file.
- **AC7** — When `--converge` runs in a fixture worktree that ALREADY carries an untracked
  `reinvention-backlog.md` inside `memory/map/` from a previous release, the run names that legacy
  path, states
  it is no longer written, leaves the file in place, and `git status` still shows it. Observed before
  the fix so the silent case is seen once. This is the migration §5's risks row obliges and rev-4's
  ratification created; AC1 is scoped to a CLEAN fixture and reaches none of it.
- **AC5** — When `tools/codebase-map/README.md` is read, it states that no gate leg and no hook runs
  `--converge` as a merge-bar step, and names `WIRE-INTO-PROJECT.md` and `reuse-lookup.agent.md` as
  the places that DO prescribe it at review time.

## 7. Gates

`codebase-map kit selftest` · `memory hygiene` · `dead-path carriers (deleted files still named)` ·
`harness arms (fail branches armed or pinned)`.

`codebase-map kit selftest` is a `subject: kit` leg and is HELD on a plain bar, so a builder verifying this unit needs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` to reach it; the runner names every held leg, so it is announced rather than silent. This unit's bar names no other held leg — rev-3 carried a sentence about `codebase-map coverage + freshness`, which is neither held (`tools/gate-legs.json` gives it `subject: repo`, `chunk: declarations`, no guard) nor in this unit's leg list above.

## 8. Open questions

- **Q1 — tracked artifact, or outside the worktree?** Tracked makes the rows durable, reviewable and
  shipped to adopters, at the cost of a new generated file under the freshness contract and a file
  that grows monotonically. Outside the worktree — under the git COMMON dir, which is where
  `tools/memory-recall/query.py:233` writes and NOT where `gate-ledger.tsv` goes; the option was
  posed citing the ledger and S1 records why that citation is wrong — keeps the tree clean and matches how this repo already stores per-run records, at the cost of
  rows that no review ever sees and that do not travel between nodes. A third option the first
  decision saw: keep the durable destination and TRACK it, which is what F7 chose.

  **This is a REVERSAL of a landed decision, not an open choice.** `bConvergentLodestar` F7 posed this
  question, decided for the durable deduped destination, and BUILT it as `append_backlog`. Neither
  rev-1 of this spec nor the dossier named that, which made a decided fork look open. The honest case
  for reversing is an observation about practice rather than a defect in F7's reasoning: the rows have
  never been reviewed by anyone, because the file has never existed. RESOLVED (owner, 2026-09-05):
  outside the worktree. This REVERSES `bConvergentLodestar` F7, and the reversal is recorded as such
  rather than as a fresh decision — F7's reasoning about durability was sound for a file somebody
  reads, and the ground for reversing is three years of nobody reading one that never existed.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round.
- rev-6 · 2026-09-06 · built. `derive_backlog_path` writes under the git COMMON dir; the migration
  note became its own function so AC7 could be ARMED rather than asserted about, since a clean
  fixture never reaches the case. Status CLOSED.
- rev-5 · 2026-09-06 · folded the round-3 spec audit: H10 (S1's "every existing consumer uses
  `--git-common-dir`" is false — one does, the gate runner and the lander use `--git-dir` — and
  "beside `gate-ledger.tsv`" resolves under `--git-dir` and would red this unit's own AC6, so the
  phrase is dropped and §10's reuse evidence corrected to one instance), H6 (the held-legs sentence
  named a leg that is neither held nor in this unit's §7 list), M2 (AC7 grades the migration case
  rev-4's ratification created, which AC1's clean fixture cannot reach), L1 (S2, §4's Rollout and §10
  still spoke of Q1 as open after the owner resolved it).
- rev-4 · 2026-09-05 · the owner ratified Q1 for the outside-the-worktree disposition, so S1 states
  it, AC1a and AC1b collapse to an unconditional AC1, AC6 pins the linked-worktree case, and the unit
  moves to order 4.
- rev-3 · 2026-09-05 · folded the round-2 spec audit: H2 (rev-2's reassignment of `map_diff.py` to
  unit 1 moved the collision rather than removing it — both units write that file, in the same
  function, and the rollout now says so and sequences them), M1 (§7 discloses the held kit legs).
- rev-2 · 2026-09-05 · folded the round-1 spec audit: B1 (S3 hands the backlog amendment to unit 1
  rather than editing the same row), H3 (AC1 split into a branch-neutral AC1a and a branch-specific
  AC1b so no criterion pre-commits Q1), H4 (S4 and AC5 narrowed to the true claim, three tracked files
  having falsified the rev-1 wording), H5 (Q1 names `bConvergentLodestar` F7 and restates itself as a
  reversal, with the third option restored).

## 10. Reuse audit

The seam is the existing out-of-worktree record convention, cited from
`python tools/codebase-map/reuse_lookup.py "write a per-run record outside the worktree"`, which
returns no seam above the threshold — the evidence being that the two live instances are spelled
inline at their call sites rather than shared: `tools/memory-recall/query.py` writes
`<git-common-dir>/recall/queries.jsonl` and the gate runner writes `gate-ledger.tsv` under the same
root — but `gate-ledger.tsv` is written under `--git-dir` (`run-gates.sh:95`, `:158`) and only
`queries.jsonl` under `--git-common-dir` (`query.py:233`), so the two live instances differ and the
reuse evidence is one instance, not two. Q1 is RESOLVED for outside the worktree, and this unit
follows `query.py`'s `--git-common-dir` spelling, not the ledger's, because the record must survive
`git worktree remove`.

Recall terms used: converge reinvention backlog collision flags untracked worktree git-common-dir
map_diff append_backlog dedupe adopter shipped tracked

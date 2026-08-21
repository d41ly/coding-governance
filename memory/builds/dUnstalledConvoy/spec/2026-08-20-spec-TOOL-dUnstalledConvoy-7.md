# TOOL-dUnstalledConvoy-7 — E3 and E4 are measured, and the verdict is recorded with the test that would have lost

**Status:** CLOSED · rev-3 · 2026-08-21 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

## 1. Goal

The recorded verdict `parallelism route: none` rests on two criteria its own evidence marks as NEVER
RUN. This unit runs them against the real tree, records what would have made each lose before running
anything, and produces the verdict `TOOL-dUnstalledConvoy-8` branches on. It ships no rule.

## 2. Scope (IN)

- **S1** — the losing conditions are written into the record BEFORE either test runs. A test whose
  result cannot change the pick is a rehearsal, and writing the loss condition first is the only
  thing that stops one being reinterpreted afterwards.
- **S2** — **E3 is measured**: can M6's three conditions hold for a dispatched pair, condition 3
  included. The orchestrator owns every phase move and every shared-record write; two sidechain
  passes are dispatched with declared, disjoint write sets. The observation is the actual path set
  each pass wrote, taken from git rather than from what the pass reports.
- **S3** — **E4 is measured**: can two passes commit at their own ends without racing one index. Two
  linked worktrees on two throwaway branches off the run's branch, each pass committing in its own,
  then the orchestrator merging both. The observation is whether both commits survive the merge with
  no conflict markers and no dropped rows.
- **S4** — E4's merge half specifically exercises the row-keyed merge driver, because two open rows in
  this tree record it failing under a real `git merge` and failing again inside a linked worktree.
  If parallel passes can reach a row-merged file at all, that is E4's losing condition and it must be
  hit deliberately rather than discovered later.
- **S5** — the record carries a single verdict token on its own line, in the shape the prior
  parallelism record used, so the inversion unit reads a token rather than parsing prose. The token
  set is CLOSED and declared here: `parallelism route: cleared`, `parallelism route: failed`, or
  `parallelism route: not-observed`. Review fold: M1. The first draft promised a token whose legal
  values were enumerated in neither spec, which left the consuming unit branching on an undefined
  input domain.
- **S6** — every rejected candidate carries the test that rejected it. A rejected candidate with no
  recorded test is indistinguishable from one nobody tried, and the next build pays to re-run it.
- **S7** — the record states which criteria were CLEARED by the prior hunt and are not re-run here.
  E1 and E2 were measured and hold; re-running them would spend budget re-deriving the known.

## 3. Non-goals (OUT)

- Shipping the inversion. That is `TOOL-dUnstalledConvoy-8`, and it is conditional on this verdict.
- Re-measuring E1 and E2. Both were cleared by the prior hunt against this same harness, and S7
  records that rather than repeating it.
- Re-opening R1, R3 or R4. R1 fails E2 on a budget key an unattended run cannot mint, R3 died on a
  `command -v` lookup, and R4's schedule is not one the run controls. All three are adverse evidence
  rather than absent evidence, which is the distinction this unit exists to respect.
- Building any dispatch machinery. This unit measures; if the verdict is favourable, units 8, 10 and
  11 are what ship.

## 4. Design

### The losing conditions, written first

| Criterion | LOSES if |
|---|---|
| E3 | any dispatched pass writes a path outside its declared set, or touches the run-state file, `memory/DECISIONS.md`, a backlog shard, or a generated index together with its generator |
| E3 | the orchestrator cannot move a phase without a dispatched pass having already moved it |
| E4 | two commits from two worktrees cannot both reach the run's branch without a conflict a human must resolve |
| E4 | the row-keyed merge driver leaves conflict markers when the orchestrator merges the two branches |
| both | the harness refuses the dispatch at all, or the sidechain cannot perform a pass kind M6 names |

### E3's test

Two sidechain passes, dispatched through `Workflow` because M4 already mandates that route and the
prior hunt cleared E1 and E2 for it. Each is primed with the directive set and given ONE declared
write path under a scratch prefix. The orchestrator performs every phase move itself and makes every
shared-record write itself.

The observation is `git status --porcelain` and the per-pass diff, not the passes' own reports. A
pass that says it wrote one file and wrote two is exactly the failure E3 is about, and asking it is
the one method that cannot detect that.

### E4's test

Two linked worktrees, each on a throwaway branch off the run's branch, each carrying one pass that
commits at its end. Then the orchestrator merges both branches into the run's branch in sequence.

The prior hunt observed that this repo's worktrees each hold their own index, so the RACE half is
already answered as a checkout property. What is unmeasured is the MERGE half, and S4 aims the test
straight at the recorded defect: the row-merged files fail closed under a real `git merge` in a
linked worktree, recovering only by running the driver directly on the three stages.

If the two passes' write sets exclude every row-merged file — which M6 condition 3 already requires,
since backlogs and decision logs are exactly the shared mutable records it names — then E4 passes and
the recorded defect never fires. That is the outcome this test is designed to discriminate, and it is
not knowable by argument.

### Inventory of what the prior hunt already settled

| Criterion | Route R2 | Source |
|---|---|---|
| E1 the layer reaches the pass | CLEARED, against the document that said otherwise | probe observation |
| E2 the budget resets or is not spent | CLEARED, a sidechain agent is not counted | probe observation |
| E3 | NOT OBSERVED | the record says so in those words |
| E4 | NOT OBSERVED | the same |
| R5 as a checkout shape | viable, six worktrees each with their own index | observation |

### Files touched (estimate)

| File | Change |
|---|---|
| `memory/builds/dUnstalledConvoy/build/` | one record carrying the verdict token, the losing conditions and both observations |

No product file moves in this unit. That is the point of it.

### Alternatives rejected

- **Reasoning E3 and E4 to a conclusion.** The prior record explicitly refuses this: "an argument is
  not an observation". Repeating the refusal it recorded would be the same error with better prose.
- **Measuring on a scratch repo rather than this tree.** Rejected: the recorded merge-driver defects
  are conditional on a linked worktree and on this repo's own conf layout, and a scratch fixture
  would clear E4 by not having the thing that breaks it.

## 5. Production-readiness checklist

- security — the dispatched passes write only under a scratch prefix, and the orchestrator makes
  every shared-record write. No credential and no remote operation is involved.
- perf / scale — two sidechain dispatches, within the fan-out and concurrency caps the review
  protocol declares.
- a11y — N/A — a measurement producing a record.
- i18n — N/A — the same.
- error / empty / loading states — a test that cannot run is recorded as NOT OBSERVED, in exactly the
  words the prior hunt used, and never as a pass.
- observability — the record IS the deliverable.
- risks (concurrency, data-loss, rollback hazards) — the throwaway branches and worktrees are removed
  after the measurement. The worktree inventory is `git worktree list` diffed against the directory
  listing, because an open memory records six orphaned empty directories surviving the former.
- testing + left-shift gates — this unit IS a test. Its left-shift is the verdict token unit 8 reads.
- migration / rollback — none.
- user docs — none. The record is internal evidence.

## 6. Acceptance criteria

- **AC1** — The record's first content line carries a verdict token in the prior record's shape, and
  `grep` for that token returns exactly one line.
- **AC2** — The losing conditions appear in the record ABOVE both observations, and the commit that
  adds them is EARLIER than the commit carrying either result, observed by `git log --oneline` on the
  record's path.
- **AC3** — E3's observation cites `git status --porcelain` or a per-pass diff, never a pass's own
  self-report.
- **AC4** — E4's observation states whether `tools/memory-tree/merge-rows.py` was reached at all, and
  if it was, whether the merge produced conflict markers.
- **AC5** — Every criterion is recorded as CLEARED, FAILED or NOT OBSERVED, and no criterion is
  recorded as passing on an argument, observed in `memory/builds/dUnstalledConvoy/build/`.
- **AC6** — The record carries a `**Serves:**` line naming this unit and unit 8, satisfying hygiene
  check 21's record-binding grammar, with the filename projecting the lowest id it serves.

## 7. Gates

`memory-tree hygiene` (checks 5 and 21, the record filename and its binding line) · the full bar at
the push boundary. This unit adds no gate.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): if E3 clears and E4 fails, the build ships NO inversion. The rule is the same one the consuming unit now carries — anything other than `cleared` on either criterion is a non-shipping outcome — so the two units cannot disagree about a three-valued vocabulary. This resolves the DISPOSITION now, which is what M3 asks for, while leaving the measurement itself genuinely unmade: S1 still requires the losing conditions written before either test runs, and no result is presumed here.**

  The question this settles: OPEN, and deliberately so: if E3 clears and E4 fails, does the build ship a narrowed inversion? It is honestly unresolvable until the measurement is taken, and writing the answer
  before the test is exactly what S1 exists to prevent. What the 2026-08-20 reorder fixed is not the
  fork but the CLAIM attached to it. The first draft said a run could resolve this under the new scope
  authority, which was false when written: the authority and the recording verb both landed after this
  unit, so at this position M3 still said a scope fork was not the run's to take and the verb did not
  exist. Under the reordered plan the authority is position 2 and the verb position 3 against this
  unit's 5, so the sentence is now true. Review fold: M11. A pass-level
  parallelism that cannot commit independently is still useful if the orchestrator commits for both,
  which changes M6's condition set rather than abandoning it. Options: record the failure and let
  unit 8 not ship; or record it and let unit 8 ship an inversion scoped to orchestrator-committed
  passes. **Recommendation: decide from the measurement, not now.** Writing the answer before the
  test is what S1 exists to prevent, and this fork is honestly unresolvable until AC4 is observed.
  It is a scope fork under `TOOL-dUnstalledConvoy-4`'s new authority, so a run may resolve it — and
  it must record the resolution as an amendment.

## 9. Revision log

- rev-3 · 2026-08-21 · MEASURED. Both criteria CLEARED and the verdict token reads `cleared`, so the
  inversion unit ships. The losing conditions were committed one commit ahead of the results and git
  carries both, so S1's ordering is checkable rather than asserted. E4 carries a CONTROL the spec did
  not require and which the clearance is worth nothing without: the same two-worktree merge run again
  with both passes editing a row-merged file reproduces the recorded driver defect on demand — a
  conflict, two markers, failing closed. E4 therefore clears because M6 condition 3 excludes the files
  that would break it, not because the driver is sound, and the record says so in those words.
- rev-2 · 2026-08-20 · folded the spec audit: M1 (the verdict-token set is CLOSED and declared), M11 (F1 was
  resolvable only under an authority that used to land later; the reorder makes its own text true).
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "dispatch a build pass concurrently and observe what it
wrote"` returns the `unattended` and `agent-cap` dossiers, and `agent-cap.topLevelArgs` as the
affordance seam bounding any fan-out. No code seam is extended: this unit writes a record.

`python tools/memory-recall/query.py "why does an unattended build run strictly sequentially instead
of dispatching independent units to Agent or Workflow concurrently" --terms "parallelism route direct
spawn sidechain hook agent-cap budget per-prompt concurrency dispatch build pass unattended
directive"` returns the prior verdict, its evidence record and the live backlog row saying the routes
are re-openable on E3 and E4 being RUN. The prior record's own closing paragraph is the warrant for
this unit: it states the gap is unmeasured evidence rather than adverse evidence, and asks whoever
re-opens it to know the difference.

Verified at source before writing: the prior record's per-route section marks E3 and E4 as NOT
OBSERVED in those words, and marks R5 viable. Two open backlog rows record the merge-driver failures
S4 aims at.

Recall terms used: parallelism route direct spawn sidechain hook agent-cap budget per-prompt
concurrency dispatch build pass unattended directive.

# E3 and E4 — the two criteria the parallelism verdict never ran

**Serves:** journal TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8  <!-- the measurement, and the unit whose branch it decides -->

parallelism route: pending

**This half of the record is committed BEFORE either test runs, and that ordering is the point.** A
test whose result cannot change the pick is a rehearsal, and a losing condition written after the
result is a rationalisation. The verdict token above reads `pending` until the results half replaces
it, so a reader who finds this file mid-run cannot mistake it for an answer.

## What is NOT re-run, and why

The prior hunt measured four criteria against route R2, the `Workflow` sidechain. Two of them CLEARED
and are not re-measured here — re-deriving the known is the spend this whole method exists to avoid.

| Criterion | Prior result | Here |
|---|---|---|
| E1 — the directive layer reaches the dispatched pass | CLEARED, against the document that denied it | not re-run |
| E2 — the budget resets, or is not spent | CLEARED — a sidechain agent is not counted against the per-prompt direct-spawn budget | not re-run |
| E3 — M6's three conditions can hold for the pair, condition 3 included | **NOT OBSERVED** | **measured below** |
| E4 — each pass can commit at its own end without the two commits racing one index | **NOT OBSERVED** | **measured below** |

Routes R1, R3 and R4 are adverse evidence rather than absent evidence and stay closed: R1 fails E2 on
a budget key an unattended run cannot mint, R3 died on a `command -v` lookup, and R4's schedule is not
one the run controls. R5, one worktree per pass, was measured a viable checkout shape and is what E4
uses.

## The losing conditions, written first

Each is a condition under which the criterion FAILS. If none fires, the criterion clears.

**E3 loses if:**

1. A dispatched pass writes any path outside the set it declared before dispatch.
2. A dispatched pass touches a shared mutable record — the run-state file, the decision log, a
   backlog shard, or a generated index together with its generator.
3. The orchestrator cannot move a phase without a dispatched pass having already moved it.
4. The harness refuses the dispatch, or a sidechain cannot perform a pass kind M6 names.

**E4 loses if:**

5. Two commits made in two linked worktrees cannot both reach one branch without a conflict a human
   must resolve.
6. The row-keyed merge driver leaves conflict markers when the orchestrator merges the two branches.
7. Either worktree's commit is lost, reordered, or silently absorbed by the other.

**Both lose if** the observation has to come from a pass's own report rather than from git. A pass
that says it wrote one file and wrote two is exactly the failure E3 is about, and asking it is the
one method that cannot detect that.

## How each is observed

**E3.** Two agents dispatched through one `Workflow` — the route M4 already mandates for spec audits,
so it is in daily use here rather than novel. Each is primed with one declared write path inside a
throwaway git repository, and the orchestrator performs every phase move and every shared-record
write itself. The observation is `git status --porcelain` in that repository plus the per-path diff,
never what an agent reports.

The throwaway repository is deliberate and is NOT the fixture shortcut this build rejected elsewhere:
E3 asks whether a dispatched pass stays inside its lane, which is a property of the dispatch and not
of this repo's conf layout. E4 is the opposite case and runs here, for the reason below.

**E4.** Two linked worktrees on two throwaway branches off this run's own branch, each carrying one
commit, then both merged into a THROWAWAY branch — never into the run's branch. It runs in THIS
repository on purpose: two open rows record the row-keyed merge driver failing under a real `git
merge` and failing again inside a linked worktree, and both defects are conditional on this repo's
own conf layout. A scratch fixture would clear E4 by not having the thing that breaks it.

Condition 6 is aimed straight at that recorded defect. If M6's condition 3 already excludes every
row-merged file — and backlogs and decision logs are exactly the shared mutable records it names —
then E4 clears and the defect never fires. That is the discriminating question and it is not
knowable by argument.

## What the verdict decides

`TOOL-dUnstalledConvoy-8` ships the M6 inversion only on `cleared`. Anything else — `failed` or
`not-observed` — is a non-shipping outcome, and that rule is already written into that unit's own
scope so the two cannot disagree about a three-valued vocabulary.

The losses are recorded either way. A rejected candidate with no recorded test is indistinguishable
from one nobody tried, and the next build pays to re-run it.

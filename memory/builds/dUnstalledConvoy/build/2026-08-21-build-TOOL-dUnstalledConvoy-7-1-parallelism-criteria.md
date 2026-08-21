# E3 and E4 — the two criteria the parallelism verdict never ran

**Serves:** journal TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8  <!-- the measurement, and the unit whose branch it decides -->

parallelism route: cleared

**The first half of this record was committed BEFORE either test ran, and that ordering is the point.** A
test whose result cannot change the pick is a rehearsal, and a losing condition written after the
result is a rationalisation. The verdict token above read `pending` until the results
below replaced it, and git carries both commits, so the ordering is checkable rather than asserted.

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


---

# The results

Both criteria CLEARED. Every observation below comes from git or from a merge's own exit status,
never from a dispatched pass's report — which is the rule both criteria share, and the one that makes
the rest of it worth reading.

## E3 — CLEARED

Two agents dispatched through one `Workflow`, each primed with the directive text and one declared
write path, into a throwaway repository seeded with all four shared mutable records.

| Losing condition | Fired? | Observation |
|---|---|---|
| 1 — a pass writes outside its declared set | no | `git status --porcelain` showed exactly two modified paths, each the declaring pass's own |
| 2 — a pass touches a shared mutable record | no | `git status --porcelain` over the decision log, the backlog shard, the generated index and the run-state file returned zero rows |
| 3 — the orchestrator cannot move a phase first | no | the run-state file is byte-unchanged, so no pass moved a phase |
| 4 — the harness refuses the dispatch | no | both agents ran and returned; 2 agents, 6 tool calls, 17.4 s wall |

Zero untracked files were created anywhere. Both passes appended exactly the line they were given and
left the sibling lane alone.

**Both agents also SELF-REPORTED holding the line, and that is recorded as worthless.** The losing
conditions say the observation comes from git precisely because a pass that writes two files and
reports one is the failure E3 exists to detect. The reports happened to agree with git here; had they
disagreed, git would have won and the criterion would have failed.

## E4 — CLEARED, and the control is what makes that mean something

Two linked worktrees on two throwaway branches off this run's own branch, each carrying one commit
touching a DISJOINT non-shared path, both merged `--no-ff` into a third throwaway branch checked out
in a third LINKED worktree — which is the condition two open rows record the merge driver failing
under.

| Losing condition | Fired? | Observation |
|---|---|---|
| 5 — a conflict a human must resolve | no | both merges returned 0 |
| 6 — the row driver leaves conflict markers | no | it was never REACHED: no row-merged file was in either write set |
| 7 — a commit lost, reordered or absorbed | no | both pass commits present in the log, both markers present in the merged tree, working tree clean |

**THE CONTROL.** A clearance that comes from never touching the breaking thing is worth nothing
unless the breaking thing is shown to break. So the same shape was run again with both passes editing
`memory/backlog/TOOL.md` — a row-merged file, and exactly what M6 condition 3 forbids. The second
merge returned 1 with `CONFLICT (content)`, two conflict markers in the file, and the driver's own
message about writing a conflict rather than a silent take-ours.

That is the recorded defect reproducing on demand. It is also the argument that condition 3 is
LOAD-BEARING rather than decorative: E4 clears because condition 3 excludes the files that would
break it, not because the driver is sound.

## The verdict, and what it costs

`parallelism route: cleared`. R2 with R5 — a `Workflow` sidechain, one worktree per pass — holds all
four criteria. E1 and E2 were cleared by the prior hunt; E3 and E4 are cleared here.

**What this does NOT establish**, stated so the next reader does not over-read it:

- Two passes were dispatched, not five. Nothing here measures what a wider fan does to the rate
  limiter, and the review protocol's caps are unchanged and still bind.
- The passes were trivial — one append each. A pass that runs a gate, renders an index or resolves a
  conf has a wider real write set than its declared one, and E3 measures the DISCIPLINE, not the
  difficulty of declaring correctly.
- E4 merged two commits, not two mid-flight passes racing. The index-per-worktree property was
  already measured by the prior hunt and is not re-derived here.
- Nothing was measured about WALL CLOCK. The owner's report is that unattended runs are slow, and
  this record does not claim concurrency is faster — only that it is admissible.

## Losses, recorded

No candidate lost here, which is itself the finding: the two criteria the prior verdict recorded as
NOT OBSERVED both clear when they are actually run. The prior verdict's own closing paragraph asked
whoever re-opened it to know the difference between unmeasured and adverse evidence. It was
unmeasured, and this is the measurement.

R1, R3 and R4 remain rejected on the prior hunt's own tests — a budget key an unattended run cannot
mint, a `command -v` that finds nothing, and a schedule the run does not control. None was re-run,
and none is re-opened.

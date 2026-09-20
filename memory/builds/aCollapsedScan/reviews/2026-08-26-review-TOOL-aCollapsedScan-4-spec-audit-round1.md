## Verdict: CLEAN WITH FIXES

**Serves:** spec-audit TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-6 TOOL-aCollapsedScan-7

Round 1, 2026-08-26, node `a`. Four primed lenses over the three rev-1 specs, batched skeptics
defaulting to REFUTE, cap 5 verifiers. **45 findings raised, 15 confirmed, 30 refuted** — precision
0.33, which is below the ~0.5 the charter names as the point to tighten priming rather than add
agents. Recorded here because the corpus of these numbers is what retunes the defaults; the yield
was still high because three findings went and MEASURED rather than argued.

Severity of the confirmed set: 8 high, 6 medium, 1 low. Zero blockers, so all three subjects
CONVERGED at round 1 and the loop is closed for them.

## The three that changed a design

**`govkit.py` already fixed this defect and documents it (id=38, high).** `tools/govkit/govkit.py:83`
takes the walk-up, and its docstring says why: *"a `git -C <dir> rev-parse --show-toplevel` returns
`<dir>` itself when an absolute GIT_DIR is inherited — which is what git exports to a merge driver in
a linked worktree, and it is exactly how the row-keyed merge driver was found to be inert here."*
Verified at source. The rev-1 spec rejected the walk-up as though its only precedent were a sibling
kit's private helper. It is instead this repo's established, documented answer to this exact defect,
which re-decides F1.

**The defect needs a LINKED WORKTREE, and the merge-bar leg cannot reach one (id=27, high).** The
lens wired a `merge.<driver>.driver` that dumps its environment and ran a real two-branch merge twice
on git 2.54.0.windows.1. Ordinary clone: `GIT_DIR` unset, and `git -C sub rev-parse --show-toplevel`
returns the repo root — the defect is ABSENT. Linked worktree: `GIT_DIR` set to
`<abs>/.git/worktrees/wt`, and the same command returns `sub` — PRESENT. `merge-rows.test.sh` case 9,
the end-to-end arm, builds its fixture with `git init` in an ordinary scratch dir, so it cannot set
the precondition, cannot fail before the fix and cannot pass differently after it. Fixing the
function without that arm leaves the leg exactly as blind to the class as it was.

**There is no shared function every caller routes through (id=41, high; id=39, id=7, id=24, id=30).**
Four independent `repo_root()` implementations, verified at source:

| Where | Mechanism | State |
|---|---|---|
| `tools/memory-recall/recall_conf.py:50` | `-C` + `rev-parse` | the defect, and S1's subject |
| `tools/memory-recall/query.py:199` | bare `rev-parse`, no `-C` | worse — cwd-dependent too |
| `tools/drift-audit/drift_report.py:65` | near-verbatim copy of the first | identical defect |
| `tools/govkit/govkit.py:83` | walk-up | already correct, and documents why |

rev-1's §4 called the scrub "the guard in the shared function every caller routes through". Two of
those four are not callers of it, so the sentence was false about its own repo.

## The rest of the confirmed set

- **id=17, high, `-4`** — S1 and S2 contradict: S1 writes a node-`a` figure into the `BUDGET_*`
  block while S2 asserts in that same block that every figure in it is a node-`d` reading. The
  file's own line 42 carries the same claim and would go stale on landing.
- **id=21, high, `-6`** — `WONTDO` is terminal, yet the spec carries live deliverables (S2, S3) that
  no M6 pass will ever build, so the stale backlog row it exists to retire survives it.
- **id=29, high, `-4`** — the file this unit edits declares its own Definition of Done in its header
  (a GREEN `--selftests` for any work under `tools/unattended/`) and the spec names neither.
- **id=40, high, `-4`** — F1 reverses the build README's recorded parked decision without amending
  it, leaving two documents disagreeing about whether the scoping is deferred or refused.
- **id=8, medium, `-7`** — "eleven callers" is a misread of `reuse_lookup.py`'s fan-in, which is a
  name-stem metric across the tree. `recall_conf.repo_root` has four call sites outside its module,
  in two files. The blast-radius argument rested on a number that did not count what it claimed.
- **id=42, medium, `-7`** — the scrub list was re-derived incompletely. `.githooks/pre-push:25`
  already pins eight names and documents the deliberate `GIT_EXEC_PATH` exclusion, under
  `TOOL-dScrubbedConduit-1`.
- **id=34, medium, `-6`** — the `^-[^-]` predicate that missed the deletions has no `memory/gotchas/`
  class, so the left-shift the charter asks for is absent.
- **id=37, low, `-7`** — a kit-version bump feeds `recall_conf.Conf.digest()` and invalidates every
  warm recall cache; the perf line said "unchanged".

## What was refuted, and the one pattern in it

30 of 45. The dominant refuted shape was a lens objecting to a §3 non-goal as though it were an
omission — the spec had already named the thing and declined it, which is what a non-goal is. That
is a priming failure rather than a reviewer failure, and it is most of the gap between 0.33 and 0.5.

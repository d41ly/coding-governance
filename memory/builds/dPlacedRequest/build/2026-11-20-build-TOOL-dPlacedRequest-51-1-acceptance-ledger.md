# TOOL-dPlacedRequest-51 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-51

The unit was built from its spec at rev-3 on base `b4db035dd`. Its Files touched names no product
file: the class record's section "A merge onto the default tip" gains the split rows and the fixture
line under its table, and no new line backticks a path, so `memory/gotchas/INDEX.md` does not move.
No gate, suite or bar ran in this pass. Every reading is a `grep` of the record or `git log` over a
fixture repository built under the node's short temp path.

THE RECORD AS UNIT 45 LEFT IT, probed before the edit: its blob at HEAD was `b8c40292`, the blob the
spec's citations pin, so its first-parent row read "no — the default branch's line only" unchanged.

THE FIXTURE, the shape the spec's S2 states, git 2.54.0 on node a: a base commit holding
`KIT_UNATTENDED_VERSION=1.110` in `tools/unattended/unattended.sh`, a run branch of the commits
`bump` (that line to 1.111) and `b2` (adds `b2`), the commit `m1` on main past the branch point, and
a detached `--no-ff` merge of the branch onto main with the subject
`merge: dPlacedRequest — land onto origin/main at x`, its first parent main's tip.

**Evidences:** TOOL-dPlacedRequest-51
- AC1 — `--first-parent --no-merges <base>..HEAD` — `grep -cF -e` over the record printed 1, and before the edit it printed 0, the red the criterion names. (DERIVED)
- AC1 — `--first-parent -p <base>..HEAD` — `grep -cF -e` over the record printed 1, and its row reads `yes, the whole branch diff, attributed to the merge`. (DERIVED)
- AC1 — `--no-merges HEAD^1..HEAD^2` — `grep -cF -e` over the record printed 1. (DERIVED)
- AC2 — `grep -c '^Measured 2026-11-20'` over the record printed 1. (DERIVED)
- AC2 — `KIT_UNATTENDED_VERSION` — `git log --first-parent -p <base>..HEAD` on the fixture's merge printed `-KIT_UNATTENDED_VERSION=1.110` and `+KIT_UNATTENDED_VERSION=1.111` under the merge, and `--name-status` printed `A b2` and `M tools/unattended/unattended.sh` there. (PINNED)
- AC2 — `git log --first-parent --no-merges --format=%s <base>..HEAD` on the fixture's merge listed `m1` alone, the default-branch commit. (PINNED)
- AC2 — `git log --no-merges --format=%s HEAD^1..HEAD^2` listed `b2` and `bump`, the 2 branch commits. (PINNED)

## Readings beside the criteria

- Bare `git log --first-parent --format=%s <base>..HEAD` listed the merge subject and `m1`, the walk the old row called the default branch's line only. (PINNED)
- A plain `python tools/playbook/writing_practice.py check pinned-facts` read green after the edit. (DERIVED)

## Items diverged

- None: the record stood as the spec's evidence states it, and every fixture reading matched the spec's section-4 evidence.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec names no `New arm:`,
  so no RED-first observation is owed.

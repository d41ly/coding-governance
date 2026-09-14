# Build brief — TOOL-aRatifiedRulings-2

**Serves:** journal TOOL-aRatifiedRulings-2

The pass this brief was handed to builds unit 2 of `aRatifiedRulings` at rev-3. The spec is
`memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-2.md` and it is
authoritative; the ruling it implements is `TOOL-aLeakedHandle-7` in `memory/DECISIONS.md`.

## What the pass builds

Check 23 of `tools/unattended/check-unattended.sh` drops a committed path that a
`brief · item <unit>` row names for that unit from its undeclared-write population. The rows are
read from the run-state file at the PASS COMMIT'S TREE, so a row appended after the commit hides
nothing, and the comparison is normalised path EQUALITY, never directory containment. One report
line per exclusion.

## What two audit rounds settled

- **The boundary is the row's path at the pass commit's tree.** Not the prompts/ directory. A
  directory exclusion would let a pass hide any write under prompts/, and fixture D exists to prove
  the checker refuses that.
- **AC7's population is DERIVED, not typed.** The spec spells the loop: 29 brief-naming lines at
  base, 28 whose pass commit carries the row, 1 that does not (`TOOL-dRetiredFork-6`, whose row
  landed in a later commit). No grandfathering; the mechanism is unchanged and the criterion asserts
  exactly what it produces. Re-run the loop rather than trusting the numbers.
- **`check-unattended.test.sh` is RED at base** (`TOOL-aHoistedPass-38`), so the suite prints no
  PASS line. AC6 is keyed to the FAIL-line DELTA and an over-pinned floor, as the spec states. Do not
  try to fix -38; it is out of this mandate.
- **Every fixture has a staged break.** A, B, E red against the base checker; C and D are controls
  that print nothing at base and after, each with ONE named break at the landed tip that reds only
  its own fixture. Observe all of them.
- **The kit version bump is NOT this unit's.** §8 F1 assigns it to the closing pass. Leave
  `KIT_UNATTENDED_VERSION` at 1.19.

## The rules this pass is bound by

- Every arm's failing case OBSERVED RED first, with a positive artifact that it ran.
- The passes are SEQUENTIAL; unit 1 is CLOSED and nothing else is open.
- Commit with the unit id in the subject; then `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD` and act on it. Flip the spec status header in the same commit as the code.
- Re-declare WIDER with `--dispatch` before the commit if the set grows.

## What the pass must not do

- No sibling unit's files. `unattended.sh` is unit 1's and is CLOSED. `run-gates.sh` is unit 4's.
- Never `git stash` on this worktree.

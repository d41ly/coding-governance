# TOOL-dDerivedDocket-52 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-52

One resolver in the unattended gate leg that answers which commit introduced a line in a run-state
record, across the rotation rename, floored at the record's own tenancy and announcing four named
empties instead of a plausible wrong sha. No merge bar, no gate leg and no `*.test.sh` suite was run
in this pass. What was run instead: the resolver itself, extracted from the leg the way the arms
extract it, over eight scratch git repositories; and the arm block itself, sliced out of the suite by
its own markers and executed standalone in a replica of that suite's prologue — thirty assertions,
green, and RED under each of six staged breaks (the floor removed, `--full-history` dropped, the cap
spelled to keep the newest commits, the floor's parent-test exception deleted, the header sentence
deleted, and the path set narrowed to the queried path alone).

**Evidences:** TOOL-dDerivedDocket-52
- AC1 — `tools/unattended/check-unattended.sh` — over a fixture whose record was rotated by a later
  run's preflight (a staged `git mv` inside the folder plus a fresh live record in one commit), the
  extracted resolver returns the run's own preflight commit, prints no reason line, and the arm
  separately asserts the answer is not the rotation commit. Staged RED: with the path set narrowed
  to the queried path alone the same fixture answers the rotation. The check-19 verdict half is
  this criterion's `permission:` line and belongs to unit 18's commit, where the first caller lands.
- AC2 — `tools/unattended/check-unattended.sh` — the rotation and the preflight both carry the line
  and the preflight is returned; and in a second fixture, where the tenancy boundary is an archived
  sibling filed in a commit of its own, the oldest candidate's first parent already carries the line,
  that candidate is passed over, and the walk ends in S4's no-candidate empty rather than a sha. A
  control in the same fixture shows a genuine introduction IS answered. rev-2 added the `fixture:`
  clause recording why the pass-over is only observable in that shape.
- AC3 — `tools/unattended/check-unattended.sh` — in a `--depth 1` clone the resolver returns empty
  and prints the unresolved-range reason naming the grafted oldest end; the arm asserts the printed
  line and not only the empty return. Measured on the way in: an add search in that same clone
  answers the graft commit for a record created three commits earlier, which is the wrong sha this
  refusal replaces. The caller's reading is the criterion's `permission:` line, at unit 18.
- AC4 — amended rev-2 — `tools/unattended/check-unattended.sh` — rev-1 asked one fixture to carry
  two measurements and only one held. Measured in a scratch repo: where the rotation lands inside a
  MERGE, the resolver still answers the preflight while an add search over the archived path answers
  NOTHING under the plain spelling and under `--full-history` alike, because git computes no diff for
  a merge — so neither end of the window is resolved by an add. The `--full-history` contrast lives
  in the `-s ours` shape instead, where a simplified walk loses the introducing commit entirely. Both
  are now fixtures and both are asserted; §9's rev-2 entry logs the correction. Staged RED: with
  `--full-history` dropped, fixture (b) answers nothing.
- AC5 — amended rev-2 — `FLOOR_ASSERTIONS` — the floor rev-1 named cannot move. `ARMS_FLOORS` is not
  an executed-assertion floor: `tools/memory-tree/check-arms.py` discovers its population from
  `fail <n> "` call sites, and this unit adds no `fail` branch, which §4's Fail codes row already
  said. The floor that moves is the suite's own: `FLOOR_ASSERTIONS` 419 → 449 and `FLOOR_SHARD_2`
  328 → 358, both readable with `git show` at this commit and its parent, `FLOOR_SHARD_1` untouched
  at 91 because every new assertion sits in region two. The raise is the block's thirty
  assertion-helper call sites, counted and then confirmed by executing the block standalone. That the
  suite still passes AT the raised floor is the criterion's `permission:` line and belongs to the
  build's one post-build bar.
- AC6 — `tools/unattended/check-unattended.sh` — a fixture nine commits deep, graded at cap 4,
  returns empty and names truncation; the same fixture at cap 400 answers the introducing commit with
  no reason line. A second fixture carries the introduce-remove-re-introduce shape inside a window
  deeper than the cap: it announces truncation and does not return the re-introduction, and uncapped
  it answers the FIRST introduction. Staged RED: spelled `--max-count=$_cap` with the truncation test
  removed, the first fixture reports no-candidate and the second returns the RE-introduction.
- AC7 — `git grep -c` — the header sentence naming both limits occurs exactly once in
  `tools/unattended/check-unattended.sh` at this commit and zero times at its parent, where the
  function does not exist; the arm asserts the count is 1 and that the same sentence carries the
  moved-record limit two lines on. Staged RED: with that line deleted the arm reads 0.
- AC8 — `tools/unattended/check-unattended.sh` — over a fixture whose live record shares
  `anchor-kind: default-branch` byte for byte with the record a previous run left at that path, the
  resolver answers the SECOND tenancy's preflight, and the arm asserts the unfloored walk over the
  same fixture answers the FIRST run's commit instead. A second fixture, a record with no committed
  history, returns the tenancy-floor empty, textually distinct from the other three. Staged RED both
  ways: unfloored, the live query answers the first run's commit; with the floor's parent-test
  exception deleted, it answers nothing at all.

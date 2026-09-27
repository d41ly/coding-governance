# Gate repair brief R5 — the unattended kit's suites at VERIFYING

**Serves:** journal TOOL-aRepatriatedFork-6

A repair pass under the aRepatriatedFork mandate, at VERIFYING. The unattended kit's suites are not on
the merge bar; `bash tools/unattended/run-unattended-gates.sh --pooled` ran all twenty at HEAD
`84c3733c`, and three rows failed an arm. Each suite's full output is under
`C:/projects/coding-governance/.git/worktrees/arepatriated-fork-build-e42158/gate-logs/selftests/`,
one `.out` file per row named after it.

## The failures

- **unattended driver selftest** (`tools/unattended/unattended.test.sh`): `FAIL and so does the
  checker: expected [1], got [2]`. Read `unattended_driver_selftest.out` for the arm and its block.
- **unattended gate selftest shard 8/8** (`tools/unattended/check-unattended.test.sh --shard 8/8`):
  `FAIL unexpected: build-brief.md`.
- **unattended resume-tick selftest** (`tools/unattended/resume-tick.test.sh`): `FAIL AC2 the tick
  did not wait for the CLI's 60 s orphan: expected [yes], got [no: 26s]` and `FAIL AC1 the tick
  returned well inside the 60 s launch, so it is detached: expected [yes], got [no: 34s]`. The
  closing-review fold E changed resume-tick's lease read to keep only `## Run facts`; decide whether
  that change, or the width-8 pool's clock, produced these two. Timing arms under a contended pool
  can move; a lease read that no longer finds its facts would move them the same way.

Two rows were KILLED at their evidence bound under the pool and did not fail: `unattended adopter
e2e` (606 s bound; it passed in 158 s serially at the same HEAD) and `unattended runlog-writer
selftest` (330 s bound). Report whether either is a hang by running its failing-free question the
smallest way you can; do not change a bound.

## Diagnosed by the first attempt, which --dispatch refused before any write

A first pass reproduced all of the above by slicing, then stopped at a stale dispatch the main loop
has since closed. Its findings, to re-verify rather than re-derive:

- driver `and so does the checker`: a TEST defect. The arm greps `baseline_units ` in
  `check-unattended.sh`, and fold E's header comment (about `:2914`) names it, so the comment counts
  as a second call. Strip comment lines before counting, on both sides; the expectation of 1 stays.
- shard 8/8 `unexpected: build-brief.md`: a PRODUCT defect in check 34. Its key pattern `/^[^ :]+:/`
  reads a timestamped row (`2026-08-21T00:00:00Z dispatch · ...`) inside `## Run facts` as the key
  `2026-08-21T00`. Match `/^[^ :]+: /` and take the key as `substr($0, 1, RLENGTH - 2)`, so check 34
  grades exactly what `fact`/`fact_of` read. That moves shipped bytes: unattended 1.36 -> 1.37 in
  every carrier.
- resume-tick AC1/AC2 and the two killed rows: pool contention. Sliced alone at HEAD and before fold
  E, AC2 took 3-4 s and AC1 5-7 s; runlog-writer's arms took 13 s and adopter e2e's arm 1 took 6 s. No
  change owed.

## How to repair

- Reproduce each failure at HEAD by SLICING its suite (the prologue plus the failing block) or by
  running the one arm; a unit pass may not run a suite whole. Compare against the pre-fold code of the
  commit that touched the arm's subject (`git log -S`), in a `git clone --local --shared` under a
  short `%TEMP%` path.
- Fix the CAUSE. An arm pinning text this build legitimately changed is updated to the new text; an
  arm that caught a regression keeps its expectation and the code is fixed. Say which, per arm, and
  name the FILE each fix changed and whether it is product code or a test.
- Fold each fix into its OWNING unit's spec as a rev-N bump whose §9 line names "gate repair at
  VERIFYING" and the suite; status headers stay CLOSED.
- Before committing, all exit 0: `python tools/lexicon/lexicon.py`, `bash tools/check-install-prefix.sh`,
  `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`,
  `python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`. After committing:
  `python tools/govkit/govkit.py epoch --base f8fdd873`, `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py selfcheck`, `python3 tools/memory-tree/check-arms.py --check`; a kit
  whose shipped bytes moved owes its version bump in every carrier.

## What to return

Per failure: reproduced or not, the cause, the fix with its file, and the slice's result after it.
For the two killed rows: hang or slow box, with the evidence.

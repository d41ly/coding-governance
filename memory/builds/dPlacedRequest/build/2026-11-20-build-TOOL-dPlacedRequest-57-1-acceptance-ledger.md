# TOOL-dPlacedRequest-57 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-57

The unit was observed from its spec at rev-5 on base `786ebb028`. The spec touches no product file:
the read is criterion text and the oracle is the block of `TOOL-dPlacedRequest-56`'s design section,
so this pass is the ledger alone. No gate, suite or bar ran in this pass. The block under that
spec's "The oracle the close runs" heading was cut by `awk` into the run's scratch directory and run
by `bash`, with the base read by S1's command over this worktree's `memory/builds/dPlacedRequest/RUN.md`
through `tools/unattended/lib-unattended.sh#extract_run_facts`. The red of AC1 was staged on a
shared clone under `%TEMP%`, removed after; the red of AC2 on a scratch copy of spec 54 under the
run's scratch directory, never in the tree.

**Evidences:** TOOL-dPlacedRequest-57
- AC1 — `git rev-parse --verify "$b^{commit}"`: S1's command over this worktree's run-state file read `b` as the run's `## Run facts` base, and the verify resolved it to itself, exit 0. (DERIVED)
- AC1 — `9e21ac76`: the base `b` read, the newest first-parent merge on HEAD, subject `merge: dDeclaredLoop — land onto origin/main at c1f80c00`. (PINNED)
- AC1 — `version oracle: no prepared merge on HEAD`: the block run with `"$b"` in this worktree before `--prepare` printed that line and exited 2. (DERIVED)
- AC1 — `version oracle: base does not resolve`: over a scratch copy of the run-state file with its `base:` line dropped, S1's command read `b` empty and the block printed that line and exited 2. (DERIVED)
- AC1 — `version oracle`: the red, on a shared clone whose HEAD is the spec run's landing `60d90cb71` (`merge: dPlacedRequest — land onto origin/main at 191ba7ab`), the block run with `c63aabbb`, the base an earlier run pinned, walked that landing as this build's merge and exited 0. (DERIVED)
- AC1 — `version oracle`: that red walk's header read `60d90cb7^1..60d90cb7^2 · 1 commits`. (PINNED)
- AC1 — `version oracle: no prepared merge on HEAD`: on the same clone the block run with `9e21ac76`, or with the landing's own sha, printed that line and exited 2, so the base alone moved the reading. (DERIVED)
- AC2 — `TOOL-dPlacedRequest-57`: the criterion's bounded `awk` over spec 54 printed its AC1 bullet alone, closing at the next bullet, and the output named the unit once. (DERIVED)
- AC2 — `c63aabbb`: the same output held it zero times. (DERIVED)
- AC2 — `awk '/^- \*\*AC1\*\*/{f=1} f'`: the red, over a scratch copy of spec 54 whose AC1 says "the base the run reads" while its non-goals section and revision log still name the unit, this unbounded read printed the name through the revision log, and the criterion's bounded read printed it zero times. (DERIVED)

## Items diverged

None: each criterion held as written. One reading was taken: spec 54's AC1 bullet carries a figure
line pinning `9e21ac76` as the merge fact 1 found on its observation date; that is an observed
figure, not the base the criterion runs with, which the bullet names as this unit's read, so it is
not the `Red when:` of AC2.

## Owed at the close

- No new arm: the spec's Gates section declares none.
- The legs the spec's Gates section names, run once by the main loop.
- The close's run of `TOOL-dPlacedRequest-56`'s block with S1's read, after the last `push-main.sh --prepare`, which this pass cannot stage.

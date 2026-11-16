# TOOL-aMeasuredDrag-1 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-1

No merge bar and no self-test suite ran in this pass. Every criterion was observed with the unit's
own CLI, `--check-commit`, run in this worktree over this run's record, with this unit's dispatch
row already in `RUN.md`. The "before" captures ran the script at 1c3d2821. The "after" captures
ran the script this commit records. `RUN.md` had the same hash and the index the same staged set
across both captures, so no dispatch row voided the pair. The `--check-commit` arms of
`tools/unattended/unattended.test.sh` are owed to the close through the merge bar. No arm is added,
so no RED-first observation is owed.

**Evidences:** TOOL-aMeasuredDrag-1
- AC1 — `--check-commit` with `cmp` — four messages, each run before and after the edit: one ending
  `Pass: none`; a subject naming no unit with no trailer; a subject naming `TOOL-aMeasuredDrag-1`
  with no trailer; and one ending `Pass: TOOL-aMeasuredDrag-11`. `cmp` found stdout, stderr and
  exit status byte-identical for all twelve pairs. The first two exited 0 and printed nothing. The
  third failed check 49 because the subject names an open dispatched pass with no `Pass:` trailer.
  The fourth failed check 49 because TOOL-aMeasuredDrag-11 has no open dispatched pass.
- AC2 — `grep -cE '^\++ pass_commit '` over a `bash -x` trace — before the edit (1c3d2821):
  `Pass: none` 1, no-unit subject 1, unit subject 1. After the edit: `Pass: none` 0, no-unit
  subject 0, unit subject 1. All counts were derived from the trace at observation time.
- AC3 — `time` of the `Pass: none` message — eight alternating before/after samples, each round
  with the ten-`/usr/bin/true` baseline from the same shell. The machine was loaded by parallel
  builders, so the medians are recorded. Baseline median 368 ms PINNED. Before median 2874 ms
  PINNED (script at 1c3d2821). After median 2546 ms PINNED (script in this commit). The sorted
  after samples sit under the sorted before samples at every rank. The run has one current key,
  so the saving is one `pass_commit` walk. It grows with every key a run has dispatched.

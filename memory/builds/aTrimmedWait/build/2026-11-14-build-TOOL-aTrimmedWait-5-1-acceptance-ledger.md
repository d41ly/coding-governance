# TOOL-aTrimmedWait-5 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-5

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-3. The probe
is the spec's §4 block, saved as `r5.sh` in the run's scratch directory and run once from the
worktree root with `SCRATCH` set to that directory. It built the fixture repository at
`%TEMP%/tw5f` and ran the base driver from `846d51d3` and this unit's driver against it. The changed
reader is the brief-staleness block in `tools/unattended/unattended.sh#verb_status`. The suite arm in
region four of `tools/unattended/unattended.test.sh` and its RED-first observation are owed to the
main loop at the close.

**Evidences:** TOOL-aTrimmedWait-5
- AC1 — the probe printed `status identical`, `resume identical` and `STALE briefs 1 · briefs gone 1`.
  The new status line read `noted 72 · STALE briefs 1 · briefs gone 1 · worktree holds the run`. <!-- DERIVED from the fixture's 72 rows -->
- AC2 — the probe printed `calls base 71 new 1 stdin 1`. <!-- DERIVED from the fixture: 72 rows, one gone -->
- AC3 — the probe printed `fallback identical` and `fallback calls 72`, the failed batch and then <!-- DERIVED from the fixture: 1 batch plus 71 present rows -->
  the per-path call for each present brief.
- Verdict parity on the fixture — the base and the built driver printed the same `--status` and
  `--resume` stdout, and the failed-batch run printed the base's `--status` stdout, so the same stale
  and gone counts and the same lines hold before and after.
- AC4 — `bash "$SCRATCH/base5/unattended.sh" --resume tB --keepalive-id kTB` in `%TEMP%/tw5f`, with
  `CLAUDE_CODE_SESSION_ID=tw-sess` and `CLAUDE_PID=4242` exported, then the built driver's same call:
  8.3 s base, exit 0, and 2.9 s built, exit 0. <!-- PINNED 2026-11-14 -->
  A second pair read 8.7 s base and 2.5 s built. <!-- PINNED 2026-11-14 -->
  The built reading is the lower in both pairs. The host was less loaded than when the spec's base
  figure was taken, so these readings stand in for that figure rather than compare with it.
- Fix pass, an empty batch over one brief (brief `2026-11-14-prompt-TOOL-aTrimmedWait-5-fix`) — the
  batch result in `tools/unattended/unattended.sh#verb_status` now splits to zero lines when the
  capture is empty, so S2's count check falls back. `r5.sh` printed the same six lines before and
  after the fix, `cmp` identical: `status identical`, `resume identical`,
  `STALE briefs 1 · briefs gone 1`, `calls base 71 new 1 stdin 1`, `fallback identical` and
  `fallback calls 72`. It took 52.8 s before and 52.2 s after, one at a time on node a. <!-- PINNED 2026-11-14 -->
  A one-brief copy of the fixture (`r5e.sh`, at `%TEMP%/tw5e`) ran `--status` under a shim whose
  `--stdin-paths` exits 0 with no output. At 69ed1688d it printed `STALE briefs 1` where the
  real-git run printed none, and made 0 per-path `hash-object` calls. After the fix the two status
  lines are identical and it made 1 per-path call after the batch. <!-- DERIVED from the one-brief fixture -->
  The suite arm's three new region-four assertions and their RED-first observation are owed to the
  main loop at the close.

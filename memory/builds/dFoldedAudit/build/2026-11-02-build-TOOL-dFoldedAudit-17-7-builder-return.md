# dFoldedAudit — unit 17's builder return, third dispatch

**Serves:** journal TOOL-dFoldedAudit-17

Run direct/af40d13e2a7598114, summarized from its task notification.

- Built at rev-5 in the run worktree. M is `ccfa23ffe`, with parents `fc1bfde6` and `84acebdc`. F is `1a804910b`. Both commits passed every hook under Python 3.15.2 and carry `Pass: none` and the charter's trailer.
- Observed:
  - AC1: exactly eight conflicts.
  - AC2: 46 markers before resolution and 0 after, with `diff --check` clean against each parent.
  - AC3: the orderings hold.
  - AC4: `py_compile` passes.
  - AC5: `FLOOR_ASSERTIONS=215`.
  - AC6: probe P prints its 13 lines.
  - AC7: probe D prints `37 39 True`.
  - AC8 and AC9: the join count is 2, and the pin row reads `38 39 ok (pin 39, drain it)`.
  - AC10: both generators' `--check` exit 0.
  - AC11: the mirror check exits 1 on M and 0 on F.
  - AC12: the stamps are right.
  - AC13: `merge-tree` is clean.
- AC12's `manifest-check.sh` was refused to the builder. The main loop ran it after F, and it exited 0.
- Both commits record `manifest-audit: delta none · watch-commits-since-stamp: 15`.
- The four build-index renders are named in M's body.
- The probes are kept in the temp root under `dFoldedAudit-17-probes`.

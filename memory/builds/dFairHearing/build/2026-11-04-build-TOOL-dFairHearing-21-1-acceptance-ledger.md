# Acceptance ledger — TOOL-dFairHearing-21

**Serves:** journal TOOL-dFairHearing-21

Built against spec rev-2 and committed as the pass commit `0e647030c`, whose parent is `3b9561918`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-21-1-builder-return.md`, and every observation below is that return's. No suite, gate or bar ran in the pass: the checks were a scratch fixture probe standing in for the `review-replay selftest` leg, over a fixture repository at `%TEMP%/fhh` and a shallow clone at `%TEMP%/fhs`, both deleted afterwards. The `New arm:` line's red-first observation and the spec's legs are owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-21
- AC1 — `frozen at <sha>` — the clean file printed `frozen at <sha>` first, and with one byte appended the run exited 2 naming `held.json` and both ids. Before the change the edited file still printed `frozen at`
- AC2 — `--experiment` — over the shallow clone the `--experiment` run exited 2 naming the shallow history, with no figure line. Before the change the shallow clone still printed `frozen at`
- AC3 — `frozen at b6c828a92` — the real held-out file in this checkout printed `frozen at b6c828a92…` and the run continued
- AC4 — `grep -n "hash-object\|shallow" tools/workflows/README.md` — it printed lines 824 and 826

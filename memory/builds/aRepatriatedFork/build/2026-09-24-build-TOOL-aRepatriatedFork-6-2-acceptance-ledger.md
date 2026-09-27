# TOOL-aRepatriatedFork-6 — acceptance ledger, closing review folds

**Serves:** journal TOOL-aRepatriatedFork-6

The folds of closing review round 1 L1 and L2 (commits `e5dc0cda`, `ad15b56e`) and round 2 M1 and L1
(`995a5185`), written at the main loop from those passes' returns. Each arm ran as a slice of its
suite and was observed red at the pre-fold commit named; the close's bar runs the suites whole.

**Evidences:** TOOL-aRepatriatedFork-6
- AC9 — `phase: LANDED` — a slice of `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`: at 6ddeb7d5 `--status` read the forged phase and the halt code under Parked, and the leg reported the forged ABORTED record; after the fold both read the in-section facts only
- AC10 — `phase: LANDED` — a `tools/unattended/gate-guard.test.sh` slice: at 00c092d4 the hook allowed both the above-heading phase and the `run-branch:` park row; after the fold both deny and the in-section control rebinds; check 36 named twelve unscoped reads over 00c092d4's readers and none now
- AC11 — `base:` — an `unattended.test.sh` slice: at 00c092d4 `--preflight` left the section with no base when `base:` sat above the heading; after the fold the section carries it

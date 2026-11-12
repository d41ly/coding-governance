# PLAY-dOrderedCharter-84 deviation 841 — each guard-run scenario commits its own run-state record

**Serves:** deviation PLAY-dOrderedCharter-84

- **Departs from:** `PLAY-dOrderedCharter-84@rev-2` [Design]
- **Hand-off:** spec-to-code
- **Before:** each case commits the driver and the run-state record on `run/t` before its scenarios, holding the case's `phase:` and `run-branch:` lines, and each scenario resets to the case's commit.
- **After:** each case commits the driver on `run/t` before its scenarios; each scenario then commits its own record, with the phase and run-branch its row of the fixture table gives, and resets to the driver's commit.
- **Cause:** builder discovery
- **Reason:** the table's scenarios inside one case read different facts: `guard-run-live` holds two `run-branch` spellings and `guard-run-terminal` holds `LANDED`, `ABORTED` and `BUILDING`, so no one record per case can serve them. The record per scenario is the table as written, and every scenario still stages the same two guarded edits over a committed record and driver.
- **Evidence:** the fixture table in the spec's Design section, rows for `guard-run-live` and `guard-run-terminal`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-84

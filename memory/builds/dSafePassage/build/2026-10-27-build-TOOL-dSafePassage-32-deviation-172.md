# TOOL-dSafePassage-32 deviation 172 — the reclaim guard records its boot-clock start too

**Serves:** deviation TOOL-dSafePassage-32

- **Departs from:** TOOL-dSafePassage-32@rev-3 [§2 S2]
- **Hand-off:** spec-to-code
- **Before:** S2 has `take_write_lock` write `started_boot` beside `started`; the reclaim guard `write_reclaimed_lock` writes keeps its `{"pid", "started", "host"}` record.
- **After:** both records pass through `add_boot_start` in `tools/govkit/upgrade_steps.py`, so the guard carries `started_boot` wherever `read_boot_clock` returns a float, and neither carries the key where it returns None.
- **Cause:** builder discovery
- **Reason:** `check_holder_dead` judges a guard's holder as it judges a lock's, and S5 makes a `posix-ps` row of a record with no `started_boot` read `unknown` where the wall estimate says reused. A guard left on the wall alone would then never be cleared on POSIX once its dead holder's pid is reused, and every later take would read `busy` against it with no remedy but deleting the guard by hand, where before this unit it read `dead` and was cleared.
- **Evidence:** this unit's acceptance ledger, its "Unbroken neighbours" line: `fixture lock --plant guard-dead` exits 0 with the guard cleared; under WSL `add_boot_start({"pid": 1, "started": 0.0})` returns the keys `pid`, `started`, `started_boot`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-32, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-2

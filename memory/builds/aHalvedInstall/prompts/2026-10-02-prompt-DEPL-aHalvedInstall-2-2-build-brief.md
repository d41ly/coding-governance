# Build brief — DEPL-aHalvedInstall-2

**Serves:** journal DEPL-aHalvedInstall-2

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: units 1, 2 and 4
all write `tools/govkit/govkit.py`, a 12k-line file whose seams the main loop has already read, so the
passes are sequenced by hand in roster order and each is one commit.

Build exactly what the unit's spec states, in `memory/builds/aHalvedInstall/spec/`. Fast checks
only inside the pass: `python tools/govkit/govkit.py selfcheck`, the unit's own selftest arms run as a
slice, and `python tools/govkit/govkit.py epoch`. Nothing held: no merge bar, no full self-test
suite — those run once, at VERIFYING. Observe every new arm RED on a staged break before it lands.
Temporary files go to the session scratchpad.

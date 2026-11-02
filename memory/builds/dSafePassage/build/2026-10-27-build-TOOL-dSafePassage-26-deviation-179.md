# TOOL-dSafePassage-26 deviation 179 — the js forwarder reads a missing target file as a target that never started

**Serves:** deviation TOOL-dSafePassage-26

- **Departs from:** TOOL-dSafePassage-26@rev-11 [§2 S34]
- **Hand-off:** spec-to-code
- **Before:** S34 maps the js forwarder's exit from `spawnSync`'s fields alone: 127 printing the error when it sets `error`, 128 plus the signal's number when it sets `signal`, `status` otherwise.
- **After:** the forwarder spawns only where its target file exists; a missing target is handed to the same `error` branch as an `ENOENT` error, so it prints the error and exits 127. The signal and status branches are S34's.
- **Cause:** builder discovery
- **Reason:** `spawnSync(process.execPath, [<missing file>])` starts node, which cannot load the module and exits 1 with `error` unset, so S34's mapping alone exits 1 over AC33's `missing-target` plant, where AC33 asks for 127. The existence test is what makes a target that never started reach the branch S34 names for it.
- **Evidence:** `python tools/govkit/shims.py --fixture --plant missing-target --lang js` printed `exit: 127 · expects 127 · ok` and `the error printed: True` and exited 0 (this unit's acceptance ledger, AC33).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-26, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-26

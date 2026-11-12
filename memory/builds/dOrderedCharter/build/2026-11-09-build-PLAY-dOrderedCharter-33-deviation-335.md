# PLAY-dOrderedCharter-33 deviation 335 — the update criterion's fixture is a file of the deployer's fixtures folder

**Serves:** deviation PLAY-dOrderedCharter-33

- **Departs from:** `PLAY-dOrderedCharter-33@rev-6` [Design]
- **Hand-off:** spec-to-code
- **Before:** the files-touched estimate lists the deployer's self-test for the update criterion's arm and no fixture file beside it.
- **After:** `tools/govkit/fixtures/stale_edges.py` builds the scratch gov and target the update criterion runs over, with an `order` and a `refuse` plant and a `no-handler` stub that removes the handler call; the self-test's arm runs it, as it runs the retired-edits fixture it borrows its loader and commit helpers from.
- **Cause:** builder discovery
- **Reason:** the update criterion needs a scratch gov carrying the deployer, the policy, playbook and memory-tree kits and a kit shipping one unit, and a target installed from it; the deployer's fixtures folder is where each such scratch build lives, and a fixture file can be run as a probe where the self-test cannot.
- **Evidence:** `stale_edges.py --plant order` matched 5 of 5 observations and `--plant refuse` 3 of 3; each under `--stub no-handler` missed, 2 of 5 and 0 of 3 matched.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-33

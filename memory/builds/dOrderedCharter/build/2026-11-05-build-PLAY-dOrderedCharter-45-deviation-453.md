# PLAY-dOrderedCharter-45 deviation 453 — the driver suite's group floor moved with the new arm's group, as built

**Serves:** deviation PLAY-dOrderedCharter-45

- **Departs from:** `PLAY-dOrderedCharter-45@rev-3` [Gates]
- **Hand-off:** spec-to-code
- **Before:** the spec's `New arm:` line closes with `none` in its floor field, so the arm moves no floor.
- **After:** `tools/memory-tree/merge-rows.test.sh` carries the arm as its own group, and its banner floor rose from 55 to 56 beside it.
- **Cause:** builder discovery
- **Reason:** the suite's floor sat exactly at its banner count and its comment names it a ratchet raised with the groups, never left behind, or a deleted group passes as a green run; left at 55, this arm's group could be deleted with nothing refusing it. The run-case floor did not move, since the arm drives no `run` case.
- **Evidence:** `git show HEAD:tools/memory-tree/merge-rows.test.sh` carries 55 banners under a floor of 55; the suite itself runs at the close, the main loop's.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-45

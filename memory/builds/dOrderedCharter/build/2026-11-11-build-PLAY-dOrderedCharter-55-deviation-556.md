# PLAY-dOrderedCharter-55 deviation 556 — the merge attribute is written where the renderer writes the lock, behind the adopter's exec

**Serves:** deviation PLAY-dOrderedCharter-55

- **Departs from:** `PLAY-dOrderedCharter-55@rev-7` [Design]
- **Hand-off:** spec-to-code
- **Before:** S20 says the playbook adopter, `tools/playbook/adopt-playbook.sh` with `--target`, writes the lock's `merge=ours` line into the target's `.gitattributes` and wires `merge.ours.driver true`, and Files touched lists the adopter and not the renderer.
- **After:** the adopter execs the renderer for every verb but `--selftest`, so the write lives in `tools/playbook/render_playbook.py#write_charter_lock`, the one place a write-mode render writes the lock: after the lock row it appends the line where the target's `.gitattributes` lacks it and sets the driver where the target's config holds none, a value already set left alone as `tools/check-wiring.sh#check_merge_ours` leaves it.
- **Cause:** builder discovery
- **Reason:** a line in the shell after the exec never runs, and one before it runs ahead of the render that writes the lock; the renderer's lock writer is reached by the adopter's `--target` render and by every other write-mode render, so every target that holds a lock gets the line.
- **Evidence:** `tools/playbook/adopt-playbook.sh` execs `render_playbook.py` for every argv without `--selftest`; the scratch adopter merge recorded under the ledger's AC20 line.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-49

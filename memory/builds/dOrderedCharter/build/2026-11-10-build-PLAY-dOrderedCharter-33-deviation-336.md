# PLAY-dOrderedCharter-33 deviation 336 — the unit plant matches its row in a CRLF checkout

**Serves:** deviation PLAY-dOrderedCharter-33

- **Departs from:** `PLAY-dOrderedCharter-33@rev-6` [Design]
- **Hand-off:** spec-to-code
- **Before:** the later commit lands the `unit` class row and its `usage.toml` row and nothing else of the unit; `write_unit_plant` removes the first gov unit row by replacing its body in the manifest's bytes.
- **After:** the later commit also corrects `write_unit_plant` in `tools/playbook/pins.py`: it matches the row's body in the manifest's own line endings, and raises naming the tag where the body is not found, so the plant can no longer stage nothing and report a member.
- **Cause:** builder discovery
- **Reason:** `read_units` reads with universal newlines, so a row's body holds LF; the step gate's fixture clones HEAD, and on a checkout with `core.autocrlf` the manifest holds CRLF, so the replace matched nothing and the plant named `unit:unit.policy-schema` while removing no row. S5 says the plant takes one out; without the fix AC7 cannot be observed and the class's arm cannot go red.
- **Evidence:** in a scratch clone carrying the rows, `step_gate.py --fixture --plant unit` exited 0 with nothing vanished before the fix and 1 naming `unit:unit.policy-schema` after it; `pins.py --fixture --plant unit-class` stayed green over its LF fixture.
- **Risk:** stricter
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-33

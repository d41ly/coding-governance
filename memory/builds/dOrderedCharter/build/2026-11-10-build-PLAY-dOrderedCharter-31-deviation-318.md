# PLAY-dOrderedCharter-31 deviation 318 — with the agent-instructions row taken out, the step gate refuses rather than naming the entry

**Serves:** deviation PLAY-dOrderedCharter-31

- **Departs from:** `PLAY-dOrderedCharter-31@rev-15` [Acceptance criteria]
- **Hand-off:** spec-to-code
- **Before:** AC1 expects `step_gate.py --base ce13efbe`, over the tip with the `agent-instructions` `[[retired]]` row taken out, to exit 1 naming `entry:agent-instructions`.
- **After:** over this tree it exits 2: the `file` class's reader refuses on the tip side, naming `agent-instructions` as no registry entry in gov's `deploy.toml` `kits`. With the row in, it exits 0 and witnesses all nine vanished members.
- **Cause:** builder discovery
- **Reason:** S10 reads a retired id in gov's own selection through the same row, so taking the row out takes away the succession `tools/govkit/govkit.py#read_plan_destinations` reads gov's `kits` through, and the gate refuses before it compares populations. The criterion's red, a kit leaving with no succession row while the gate stays green, still holds: the gate does not exit 0. A red naming the members is observed too: the first run, before the row's `surfaces` named the kit's files, exited 1 naming its three `file:` and three `installable:` members.
- **Evidence:** the probe that cut the row printed `step_gate --base 2` with `class file's reader raised on the tip side: Refusal: the target's deploy.toml names agent-instructions in kits`; restored, `9 vanished · 9 witnessed` and exit 0.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-31

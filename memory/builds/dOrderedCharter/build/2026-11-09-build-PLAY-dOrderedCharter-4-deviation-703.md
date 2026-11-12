# PLAY-dOrderedCharter-4 deviation 703 — the charter's help page and the playbook README name the preset line and the replay

**Serves:** deviation PLAY-dOrderedCharter-4

- **Departs from:** `PLAY-dOrderedCharter-4@rev-5` [Production-readiness checklist]
- **Hand-off:** spec-to-code
- **Before:** the checklist's user-docs row reads N/A, agent-facing hook output with no command an owner runs, and the files touched are the playbook module, the checker and its suite.
- **After:** `help/charter.md`'s map paragraph gains three lines naming the `preset —` line and the replay printing the map first, and `tools/playbook/README.md`'s `{{INSTRUCTION_MAP}}` sentence names the preset line after the `held —` line.
- **Cause:** builder discovery
- **Reason:** the preset line lands in the shared map function, so the rendered charter gains it, and both pages already describe that map line by line; left alone, each would describe a map one line shorter than the one rendered.
- **Evidence:** the re-rendered `AGENTS.md` carries `- preset — none: presets join the policy reader at dKeptSession; a key's source: policy.py get <key> --explain` after its `held —` line, and the two pages listed every other line of the map before this pass.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-4

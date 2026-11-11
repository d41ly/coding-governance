# PLAY-dOrderedCharter-39 deviation 392 — the kept wiring leg stays on gov's bar, and an adopter that held the kit stops carrying it

**Serves:** deviation PLAY-dOrderedCharter-39

- **Departs from:** dOrderedCharter [fork F3 of PLAY-dOrderedCharter-39]
- **Hand-off:** spec-to-code
- **Before:** an adopter that held the agent-instructions kit carried its `agent-instructions wiring` leg on its own bar, through the kit's descriptor row
- **After:** the leg runs the renderer's entry-files check on gov's own bar alone, named by an exempt-leg row of the registry, and an adopter that held the kit stops carrying it at its next `update`; the upgrade-steps help page says so and names the command it can run itself
- **Cause:** design defect
- **Reason:** a descriptor row on the `playbook-render` entry would hand the leg to every target selecting that entry, the registry default among them, where it reds while the target's aliases are unwired, and no path of `apply` wires one, so each new adopter's bar would red on install day; the other option adds a renderer mode to a public surface, and both are vetoed, which leaves this relax
- **Evidence:** the resolution mark of F3 in `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-39.md`, the exempt-leg row naming the leg in `tools/govkit/registry.toml`, and the help page sentence in `help/upgrade-steps.md`
- **Risk:** loosening
- **Approver:** author, the unit's builder, recording the spec writer's F3 mark under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-39
- **Bound:** the entry-file wiring leg of an adopter that held the agent-instructions kit, from its next `update`; gov's own bar keeps the leg
- **Tier:** weaker, the adopter can still run the renderer's entry-files check by hand

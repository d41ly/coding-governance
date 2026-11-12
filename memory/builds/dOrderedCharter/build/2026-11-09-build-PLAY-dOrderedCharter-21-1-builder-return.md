# dOrderedCharter — unit 21's builder return

**Serves:** journal PLAY-dOrderedCharter-21

Run wf_1722f4d3-15c, summarized from its return.

- Built at rev-4 as pass commit `e542b6367`.
- What the unit landed:
  - A `step` on every row of `tools/roles/workflows.toml`, refused by the roles check outside its declared step names.
  - Reach units: each active practice that reaches a role's step joins its load set, and a step of `none` adds none.
  - The handoff's `### Practices at <step>` block, filled into a new slot of the work-order template.
  - `instruction_units.py practices --check-charter` with the `practices-reach` plant.
  - The `charter.practices` read moved into `instruction_units.read_active_practices`, shared by the charter render and the reach units.
- Deviation 211: the AC1 arm sits in the roles adopter's suite, since the roles check has no selftest a leg runs.
- Observed by probe: AC1 to AC4, the charter render check and three load-set plants. After the pass the main loop read the agent
  render check green and the arms check with no new site.
- The packet's instrument pins were not checked in the pass: its probe timed out inside the carries check.
- Owed at the close: RED then GREEN for the two step lines in the roles adopter's suite and the `practices-reach` plant; the roles
  catalogue leg; the work-order plant's pinned bytes; the tags leg. No leg runs `--check-charter` over gov's own charter.

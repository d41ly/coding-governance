# TOOL-dWitnessedBar-29 deviation 292 — where a gathered warning's marker rides, and what `grown by -` says

**Serves:** deviation TOOL-dWitnessedBar-29

- **Departs from:** `TOOL-dWitnessedBar-29@rev-5`
- **Hand-off:** spec-to-code
- **Before:** S2: a site that gathers its lines into a list prints the marker where that list is printed, so no list reader takes it for a line of its own; Python sites build it through S9's factory. S6: `GATE warn  <leg name>  (<subject>: <detail>; grown by <unit>)`; §5 and AC6: an absent kit or a failed attribution writes `-` and names why on that line. S5: the third argument limits the log walk to that path.
- **After:** a gathered site whose list is printed in the same function holds the marker beside its line, `gen_build_index.py#scan_slot_budget` as `(line, marker)` pairs that `cmd_check_format` prints, `gotchas.py#cmd_check` in a map its notes loop reads; a site whose list travels to printers elsewhere, `load_sets.py#check_budget`, `render_playbook.py#check_one_line_regions`, `check_roles.py#check_roles` and `handoff.py#print_roster`, carries the marker inside the warning's own item after a newline, so every printer of the list prints it on the line after the warning and no list reader counts it as an item; `render_playbook.py#check_charter_budget` puts its key and largest-contributor tail on the warning line, before the marker. A Python site reads the policy kit's module the cap answer already loaded, so one with no policy kit loaded prints its warning and no marker; `load_sets.py` appends the kit it resolves to the path for that. The `GATE warn` line names why before the unit, `(<subject>: <detail>; <why>; grown by -)`, and shows a TAB in the detail as a space. The path is handed to git as `:(literal)<path>`. (DERIVED from the builder's probe)
- **Cause:** builder discovery
- **Reason:** a marker appended as an item of its own is prefixed by `render_playbook`'s `budget` note and indented by its printer, so it no longer opens its line and the runner cannot read it; the line still ends `grown by -` as AC6 reads it; a literal pathspec keeps a subject that holds glob or magic characters naming that file alone.
- **Evidence:** `tools/memory-tree/gen_build_index.py#scan_slot_budget`, `tools/memory-tree/gen_build_index.py#cmd_check_format`, `tools/memory-tree/gotchas.py#cmd_check`, `tools/playbook/load_sets.py#check_budget`, `tools/playbook/load_sets.py#read_cap_answers`, `tools/playbook/render_playbook.py#check_one_line_regions`, `tools/playbook/render_playbook.py#check_charter_budget`, `tools/roles/check_roles.py#check_roles`, `tools/roles/handoff.py#print_roster`, `tools/run-gates/run-gates.sh#scan_leg_warnings`, `tools/memory-tree/routed_commits.py#read_newest_unit`.
- **Risk:** neutral
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dWitnessedBar-29

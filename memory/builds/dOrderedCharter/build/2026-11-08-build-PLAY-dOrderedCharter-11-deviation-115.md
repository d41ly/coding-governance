# PLAY-dOrderedCharter-11 deviation 115 — the agent-type render checks every role in one run, before its loop

**Serves:** deviation PLAY-dOrderedCharter-11

- **Departs from:** `PLAY-dOrderedCharter-11@rev-9` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S4 has `render_agent_file` derive the role's load set and run the missing-unit and budget checks before writing, one role per call.
- **After:** `run_mode` in `tools/roles/render_agents.py` runs the load-set check once for every agent type before the render loop, through `tools/roles/roles_lib.py#check_load_set`, and hands each role's `Missing required unit:` lines to `render_agent_file`, which places them in the body; a refusal refuses the whole render, writing nothing. `render_handoff` runs the same helper for its one role, before any input is read.
- **Cause:** builder discovery
- **Reason:** the check is a subprocess of the playbook kit, which itself starts the policy reader and the budgets script; one run per agent type would start each of them nine times per render in gov and per render in every roles self-test fixture, where one run answers every role. The helper sits in the roles kit's library because both renderers call it and the kit already keeps its one reach into a sibling kit there.
- **Evidence:** `python tools/roles/render_agents.py --check` in this tree printed one budget note per agent type and `9 agent type(s) and 1 index graded`, exit 0, in about a second; the `required-away` plant under `refuse` printed the handoff's refusal and `handoff: no prompt file written`.
- **Risk:** none
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-11

# aProfiledEffort — asks

## Asks
- TOOL-aProfiledEffort-5 · filed 2026-11-10 · the build harness's `committer` stage and the review harness's `probe` stage take no level from the effort policy, so on a model a profile matches they run at the session's own effort while every other stage runs at the profile's; found by the closing diff review, round 1, item 4, which `TOOL-aProfiledEffort-4` answered by narrowing the texts · seen `tools/roles/workflows.toml` matching `stages = {` · accept each harness stage that spawns an agent is a key of its workflow's `stages` table, so `handoff.py stage-efforts` prints a level for it
- TOOL-aProfiledEffort-6 · filed 2026-11-10 · nothing refuses a role spawn at a level its model's profile does not give: the dispatch carriers tell a session to pass `--model` and the resolved level, and the `agent` line prints effort and model after the fact · seen `tools/roles/README.md` matching `The spawn guard reads no` · accept the spawn guard refuses a role spawn or a harness call whose effort differs from what `handoff.py role-efforts --model` or `stage-efforts --model` prints for the session's model

## Dispositions
- SEV · TOOL-aProfiledEffort-5 · LOW · two short stages run at the session's effort on a profiled model; no level is misreported
- KEEP · TOOL-aProfiledEffort-5 · a stage key and a harness argument are a new mechanism, outside this build's roster
- SEV · TOOL-aProfiledEffort-6 · MED · a session that omits the model runs every role at the default tables' level, and only the agent line shows it
- KEEP · TOOL-aProfiledEffort-6 · the brief's Non-goals put the hook out of this build and promised the ask

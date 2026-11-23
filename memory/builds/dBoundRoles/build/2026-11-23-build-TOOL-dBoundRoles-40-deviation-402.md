# TOOL-dBoundRoles-40 deviation 402 — the builder's choices the spec did not state

**Serves:** deviation TOOL-dBoundRoles-40

- **Departs from:** `TOOL-dBoundRoles-40@rev-4` [S1, S3, §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** S3 says each `SubagentStop` command runs bounded by a timeout and leaves the shell that runs a command string, the bound's figure and the environment beyond `CLAUDE_PROJECT_DIR` open; S2 names the default apply of `tools/govkit/selftest.py#check_roles_install` and is silent on the case's runner apply; S1 places the session directory under the scratch target without naming it; §4 Inventory mints no function and admits one if the pass lifts the replay.
- **After:** (1) the replay is lifted into `tools/govkit/selftest.py#check_stop_replay`, which `lexicon.py --suggest check_stop_replay --as py.function` answered OK, beside the minted constants `STOP_RUN_ID`, `STOP_AGENT_ID` and `STOP_REPLAY_TIMEOUT`. (2) Each command runs through `govkit_module().resolve_bash()` with `-c`, as the case already runs `check-wiring.sh`, under a 30-second bound, the figure `TOOL-dBoundRoles-50` S18 states; a timeout is red, its label naming the command and the payload. (3) The hook's environment is the case's own with every `GIT_*` variable dropped, so a `GIT_DIR` inherited from a commit hook cannot point the hook's `git rev-parse` at gov. (4) The replay runs once, on the default apply with a governing doc, and not on `runner=True`'s apply, which S2 does not name. (5) The session directory is `fixture-sessions/fixture-session/` under the target, its parent transcript `fixture-sessions/fixture-session.jsonl` beside it, as the runtime lays out a session. (6) A red's label carries the exit, the stdout and the new record paths, since `FAILURES` holds labels alone and AC3 reads the command, the payload and the `decision` line from it.
- **Cause:** builder discovery
- **Reason:** a command string needs a shell to run it, and the bash resolver is the one this case already trusts on Windows, where the bare `bash` can resolve to the WSL launcher; S3's bound needs a figure, and taking unit 50's keeps the two units from stating two bounds. A label is the only thing `FAILURES` holds, so a red that names its output only in the detail line would leave AC3 unobservable from `FAILURES`.
- **Evidence:** the build brief `memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-40-build-brief.md` and `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-40-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-40

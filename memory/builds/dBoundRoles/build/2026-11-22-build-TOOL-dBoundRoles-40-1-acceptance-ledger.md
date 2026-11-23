**Serves:** journal TOOL-dBoundRoles-40

# TOOL-dBoundRoles-40 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `21c2a4e8d`: a `python` probe in the session scratchpad that built a scratch
target under `%TEMP%` with `selftest.build_target` over `DEPLOY_REGISTRY_DEFAULT`, wrote the governing doc as
`tools/govkit/selftest.py#check_roles_install` does, ran govkit's `apply` into it, and then called
`tools/govkit/selftest.py#check_stop_replay` on the target three times: as applied, with the target's return-check
launcher replaced, and with the `SubagentStop` group deleted from its `.claude/settings.json`. The apply wired one
`SubagentStop` command, `bash "${CLAUDE_PROJECT_DIR}/tools/roles/return-check.sh"`, matcher `*`. The probe did not call
`check_roles_install` itself, which is a case of the govkit self-test. No gate, suite or bar ran in the pass: the slice
section 6 names, the `New arm:` arm section 7 declares with its RED-first observation, and the legs section 7 lists are
owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-40
- AC1 — `FAILURES` — over the applied target both payloads, `stop_hook_active` false and true, ran the return-check command to exit 0 with empty stdout and no path under the target's `.git/return-check/`, and `FAILURES` read `[]`. OWED: the slice over `check_roles_install` at the close, and the `govkit selftest` leg.
- AC2 — `empty population` — with the `SubagentStop` group deleted after the apply, `FAILURES` held the one label `[dBR-40 S2] the default install registers at least one SubagentStop command, never an empty population`. OWED: the RED-first observation on a scratch copy of the module whose case deletes the group, at the close.
- AC3 — `decision` — with the launcher replaced by one calling `check-return` from a copy of the target's `handoff.py` that drops the route test of `tools/roles/handoff.py#run_return_check`, `FAILURES` held one label per payload naming the command, the payload and the printed `{"decision": "block", ...}` line, send-back 1 of 3 and then 2 of 3, the first also naming the new `afixture000001.json` record. OWED: the RED-first observation on a scratch copy of the module whose case replaces the launcher, at the close.

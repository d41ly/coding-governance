# TOOL-dWitnessedBar-44 deviation 443 — a `GATE_POLICY_FILE` naming the policy file refuses

**Serves:** deviation TOOL-dWitnessedBar-44

- **Departs from:** `TOOL-dWitnessedBar-44@rev-4`
- **Hand-off:** spec-to-code
- **Before:** S1 reads the file `GATE_POLICY_FILE` names wherever it is a contained repo-relative path, and states no case where that file is the policy file the step writes.
- **After:** a `GATE_POLICY_FILE` that normalises to `.governance/policy.toml` exits 1 naming the conf, writing nothing (`tools/govkit/steps/inherited_red.py#derive_reads`).
- **Cause:** builder discovery
- **Reason:** the up's after-state is one map keyed by path, so a gate file that is also the policy file would have its key-stripped bytes overwritten by the policy bytes, or the reverse, and the before-image would record one path for two edits. Refusing is the only answer that never loosens, and no reader of the kit before the step could have read a TOML file as a gate file in a way an adopter relied on.
- **Evidence:** a scratch probe over a target whose conf names `.governance/policy.toml` beside a `land` key in `.githooks/gate-env.sh`: the up exited 1 and wrote nothing.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-44

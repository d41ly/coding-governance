# TOOL-dWitnessedBar-29 deviation 291 — no kit version moved in the pass, the lander mints them

**Serves:** deviation TOOL-dWitnessedBar-29

- **Departs from:** `TOOL-dWitnessedBar-29@rev-5`
- **Hand-off:** spec-to-code
- **Before:** §4 Rollout: every kit whose shipped bytes move carries a version above its landing base's, the set DERIVED by the `kit epoch` leg at the pass, and the pass moves each version it names at the kit's own version home; Files touched lists the version lines of `tools/policy/policy.py`, `tools/roles/roles_lib.py` and `tools/memory-recall/recall_conf.py`.
- **After:** the pass moves no version. The builder role runs no gate leg, so `kit epoch` was not run here; read from its source, `govkit.py epoch` off the push boundary prints a moved kit `owed at the lander` and does not fail, and `govkit.py mint` is what writes the bump, into the prepared merge or the attended landing's mint commit, so a branch owes none (TOOL-aMendedFleet-65 S6). The kits whose shipped bytes this pass moves are policy, roles, memory-recall, memory-tree, playbook, run-gates and the session-kickoff skill, with the root gates `check-template-size.sh`, `check-line-length.sh` and `check-spec-tokens.py`; the lander mints each one `epoch` names. Unit 30, landed before this one in the same run, moved run-gates' shipped bytes and no version either. (DERIVED from the builder's probe)
- **Cause:** builder discovery
- **Reason:** a version bumped on the branch is a second writer of the value the lander mints from the landing base, and the pass cannot derive the set without the leg the role may not run.
- **Evidence:** `tools/govkit/govkit.py#cmd_epoch`, `tools/govkit/govkit.py#cmd_mint`.
- **Risk:** neutral
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dWitnessedBar-29

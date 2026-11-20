# TOOL-dWitnessedBar-5 deviation 52 — the `held guard` arm's "never both" reads a guard in every form

**Serves:** deviation TOOL-dWitnessedBar-5

- **Departs from:** `TOOL-dWitnessedBar-5@rev-8`
- **Hand-off:** spec-to-code
- **Before:** S8 (a) has every held declaration carry a non-empty `guard` or a non-empty `unguarded_why`, never both, and §4 "Held legs guarded (S8)" lists the 36 rows of gov's manifest that gain one; `tools/playbook/kit.toml` is not in Files touched.
- **After:** the arm refuses a reason only where the declaration is guarded in EVERY form, its own row and the row `[gate_leg.gov]` renders (`tools/run-gates/leg_factory.py#check_declarations`); a split guard beside a reason passes. `playbook render selftest`, guarded under `[gate_leg.gov]` alone, gains an `unguarded_why` naming why it runs whole in an adopter.
- **Cause:** builder discovery
- **Reason:** the arm also runs in an adopter's form, `run_conform_adopter`, over each declaration's own row. A declaration whose guard is split runs unguarded in one form and guarded in the other: `agent-cap restatement self-test` and `testsuite counts self-test` guard their row and gov clears it, and `playbook render selftest` the reverse. Read literally, "never both" leaves the playbook leg red in every adopter or red in gov. A reason is false only where no form runs the leg unguarded, so the arm refuses exactly that, and every case S8 and AC7 name still refuses.
- **Evidence:** before the change, the adopter form over this tree printed `held guard` on `playbook render selftest` for carrying neither. After it, gov's `--conform` and the adopter form print no `held guard` finding. `check_declarations` probes refuse neither, an empty reason, and a guard in every form beside a reason, and pass a split guard beside a reason.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-5

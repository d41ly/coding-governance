# TOOL-dWitnessedBar-51 deviation 515 — an undeclared INHERITED_RED keeps v2's own-only default, said where the step runs

**Serves:** deviation TOOL-dWitnessedBar-51

- **Departs from:** `TOOL-dWitnessedBar-51@rev-7` [§8 F2]
- **Hand-off:** spec-to-code
- **Before:** at base an adopter with no `INHERITED_RED` declared read the kit default `land` (`.githooks/pre-push@1ecf9aa6:1341`, `tools/unattended/unattended.sh@f499fbac:9590`), so MIXED and CONTENDED reds blocked its landing; `inherited_red.py up` over such a target wrote nothing and said nothing of the change.
- **After:** the undeclared path keeps v2's catalogue default `own-only`, and `inherited_red.py up` over a target where no file read declares `INHERITED_RED` writes nothing and prints `inherited-red: undeclared — the kit default land read MIXED and CONTENDED reds as blocking; own-only now passes them`.
- **Cause:** review finding
- **Reason:** v2's walk T1 default, the owner's; the round-1 spec audit's id 19 asked that the loosening it makes be said where it happens, never land silent.
- **Bound:** the undeclared `INHERITED_RED` path only; a declared `park` or `land` is moved by the step as before
- **Tier:** middle, a policy key's bound
- **Evidence:** `tools/govkit/steps/inherited_red.py#cmd_up`, `tools/govkit/steps/inherited_red.py#UNDECLARED`; S16 and §8 F2 of `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md`.
- **Risk:** loosening
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; the fork pick is the run's under its mandate, §8 F2
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-51

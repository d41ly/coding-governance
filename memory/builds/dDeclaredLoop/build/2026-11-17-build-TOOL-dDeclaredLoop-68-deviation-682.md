# TOOL-dDeclaredLoop-68 deviation 682 — the normaliser's refusal names `bash:` where no step of the three failed

**Serves:** deviation TOOL-dDeclaredLoop-68

- **Departs from:** `TOOL-dDeclaredLoop-68@rev-4` [§4]
- **Hand-off:** spec-to-code
- **Before:** the route's sketch spells every refusal of the normaliser's bash as `witness: normaliser unavailable — <source|write_normaliser|sed>: <exit or why>`, for an exit of the three steps, any other non-zero exit, an `OSError` and a run past the bound alike.
- **After:** `tools/loop/loop_witness.py#run_normaliser` names the step for the three exits it maps, `source:`, `write_normaliser:` and `sed:` followed by the exit and the last line of `normalise.err`; a bash that does not start reads `bash: did not start: <why>`, a run past the bound `bash: past the <bound> s bound`, and any other exit `bash: exit <n>`. Each still opens `witness: normaliser unavailable — `, and a failing apply step's reason still opens `sed:` as S3 asks. The step labels carry their colon in the code, so the source spells no `"sed"` literal AC2 greps for.
- **Cause:** builder discovery
- **Reason:** a bash that never started, or one killed on the bound, ran no step the three names could truthfully name; naming the bash is the reason those cases have.
- **Evidence:** `python loop_witness.py --fixture --plant normaliser-missing` printed the kit's own refusal after the prefix; `git grep -n '"sed"' -- tools/loop/` printed nothing.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the route's sketch reads as the three named steps plus `bash:` for the cases no step owns; no spec edit is owed
- **Caused-by:** PLAY-dClosedLoop-2

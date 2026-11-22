# TOOL-dWitnessedBar-62 deviation 622 — the absent-conf line goes to stderr, and the when-form arm's unit-54 checks fold into its new trees

**Serves:** deviation TOOL-dWitnessedBar-62

- **Departs from:** `TOOL-dWitnessedBar-62@rev-5`
- **Hand-off:** spec-to-code
- **Before:** S23 has `read_root_confs` print a listed conf absent from the work tree as `not in the work tree <path>` without naming the stream; §6 AC1 and AC2 describe the admissible tree and the refused trees and say nothing of unit 54's AC2 check, which emptied the leg factory's own row's `when` in the same selfcheck run; S22 names `regen.py#check_when`, selfcheck and lib-unattended, and no README row for the `exists:` containment. (DERIVED from the spec)
- **After:** the line is printed on stderr, since `keys-not-scalar --measure` is a seed whose stdout the factory parses as rows, and `check_plant_case` reads both streams. `check_when_forms_agree` no longer edits the factory row: unit 54's AC2 assertion, selfcheck naming both forms on an empty `exists:` when, is made on the empty-path refused tree's planted row. The run-gates README's `when` table row names the containment refusal beside regen's change.
- **Cause:** builder discovery
- **Reason:** a stdout line would make every `--measure` seed run print a row `read_rows` refuses, so the seed would read unarmed instead of naming the conf. Each refused form now sits alone beside one conf-true row, so the empty `exists:` when is already planted there, and emptying the factory row too would put a second refused row in that tree. The README row is the reader's documented contract, and a changed refusal it does not name is a user-facing change left undocumented.
- **Evidence:** `python ratchet.py --fixture --plant deleted-conf` in `tools/memory-tree/` printed two PASS lines, the measure exiting 0 naming `not in the work tree .x.conf` and `.fix.conf BAR_PIN 1`; a probe of `regen.check_when` and `resolve_generated_indexes` over a scratch tree under `%TEMP%/w62b` refused and skipped the unknown-token, empty-path, no-colon, absolute, `..` and drive forms alike and kept the conf-true and present-path rows only.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-62

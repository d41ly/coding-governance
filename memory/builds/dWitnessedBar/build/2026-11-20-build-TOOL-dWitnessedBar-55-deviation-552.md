# TOOL-dWitnessedBar-55 deviation 552 — the witness's "spells the key" is read as the key before an `=`, and the arm lands inside the unit-44 arm

**Serves:** deviation TOOL-dWitnessedBar-55

- **Departs from:** `TOOL-dWitnessedBar-55@rev-4`
- **Hand-off:** spec-to-code
- **Before:** §4 "The change, in the step" has the witness print one `not an assignment <file>:<line>` row per line that "spells the key" and fails `check_policy_assignment`, leaving what spells the key to `TOOL-dWitnessedBar-62`; §10 places S4's arm "beside" `tools/govkit/selftest.py#check_inherited_red_step`, and §4's Inventory mints nothing in `selftest.py`. (DERIVED from the spec)
- **After:** a line spells the key where `INHERITED_RED` follows no word character and is followed by optional whitespace and an `=` (`(?<!\w)INHERITED_RED\s*=`), so `export`, indented, commented, spaced and BOM-led spellings are named and `INHERITED_RED_MAX_AGE=` is not. The AC1 to AC4 checks are appended to `check_inherited_red_step` itself, reusing its `run_step` and `read_blocks`, rather than a second function; the AC4 check's one
  local helper, `read_hook_value`, nested in that arm, runs the cut hook function over one fixture
  body and is not module-level.
- **Cause:** builder discovery
- **Reason:** the witness needs some predicate to print the row the spec mints, and the plain substring `INHERITED_RED` would name every `INHERITED_RED_MAX_AGE` line and its comments in gov's own `.githooks/gate-env.sh` as stray assignments. A separate arm function would copy the unit-44 arm's two verb helpers, the second instance the charter's reuse rule forbids, and would mint a name the Inventory does not list.
- **Evidence:** the probe over `%TEMP%/ir55p` named `.githooks/gate-env.sh@6834ee4b:1` for an `export` line and nothing for a file holding only assignments; `grep -n INHERITED_RED .githooks/gate-env.sh` at base prints only `INHERITED_RED_MAX_AGE` lines.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-55

# TOOL-dSafePassage-1 deviation 149 — TOOL-dSafePassage-1's spec re-grounded against dGroundRules' landed specs

**Serves:** deviation TOOL-dSafePassage-1

- **Departs from:** `TOOL-dSafePassage-1@rev-6`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dSafePassage-1`'s spec as the revision at `TOOL-dSafePassage-1@rev-6` reads it, written before dGroundRules' spec run landed and naming its interfaces from the design alone.
- **After:** the spec at rev-7, revised for the cross-check record's rows 3, 4, 6, 8, 9 and 11 and U1 to U4: every policy and cap read re-pointed from `read_policy_key` to dGroundRules' `policy.py get` and `budgets.py resolve`, the pre-commit reads and the witness parsing the step's own text with `tomllib`, the conf parsed in `read_legacy_fanout`'s grammar, S5's window population taken from the steps' declared surfaces instead of the legacy-homes list, S8 retiring `budgets.py`'s `limits:` branch, the `caps.toml` homes and `arm_limits_readers`' row and landing the regenerated mirror in a second commit, a resumed up working from its before-image alone, and the open fork F12 on what S8 leaves of the limits-file machinery.
- **Cause:** external
- **Reason:** dGroundRules' spec run landed after this build's, and its specs spell the policy reader, the cap reader, the catalogue, the mirror and the guard differently from what this spec assumed; the owner asked for the specs to be fixed before the build run, and no code has started.
- **Evidence:** `memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, and the rev-7 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck

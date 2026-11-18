# TOOL-dDeclaredLoop-21 deviation 218 — the one policy writer reads a dotted table back

**Serves:** deviation TOOL-dDeclaredLoop-21

- **Departs from:** `TOOL-dDeclaredLoop-21@rev-8` [§2 S8]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-21`'s spec at rev-8 has `tools/govkit/steps/conf_to_policy.py` write its policy text through `tools/govkit/upgrade_steps.py#render_policy_text`, and names no edit to `tools/govkit/upgrade_steps.py`.
- **After:** `tools/govkit/upgrade_steps.py#render_policy_text` reads its written value back through each segment of a dotted table name, so `review.design.rounds` and `review.design.round-count` are written under `[review.design]` through it; an undotted table reads back exactly as before.
- **Cause:** builder discovery
- **Reason:** the writer's read-back looked the table up by its whole name, so every key under a dotted table read back as None and was refused: the step could write no `review.design` key through the one writer the spec names.
- **Evidence:** a `python -c` probe of `render_policy_text('', 'review.design', 'round-count', 2)` at the pass's base refused with `does not read back (tomllib reads None)`, and after the change wrote and read it back; the `[dSP-1 S6 F9]` inputs read the same answers; `tools/govkit/selftest.py#check_review_rounds_step` adds the dotted-table case.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage `tools/govkit/upgrade_steps.py#render_policy_text`
- **Caused-by:** TOOL-dDeclaredLoop-21

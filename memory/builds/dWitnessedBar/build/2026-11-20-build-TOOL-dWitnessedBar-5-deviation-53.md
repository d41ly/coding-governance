# TOOL-dWitnessedBar-5 deviation 53 — the `push-selected` export rule is spelled in the hook and in `verdict_flow.py`

**Serves:** deviation TOOL-dWitnessedBar-5

- **Departs from:** `TOOL-dWitnessedBar-5@rev-8`
- **Hand-off:** spec-to-code
- **Before:** S6 has `push-selected` make the pre-push hook export `GATE_SELFTESTS=changed` for its bar when the pusher set nothing. AC6 observes it by `verdict_flow.py --fixture held-policy`. The spec states no second place the rule lives.
- **After:** the rule is stated in `tools/run-gates/verdict_flow.py#derive_held_export`, which `select` prints and the `held-policy` fixture observes, and spelled once more in `.githooks/pre-push` after `read_policy_at` reads `verdict.held` at R. The pre-push suite's SEL arm observes the hook's copy.
- **Cause:** builder discovery
- **Reason:** the hook exports before its own bar, and §8 F2 keeps `select` out of the hook: the Test step runs it, and the hook only checks its record. So no python call answers the hook's export, and the rule has to be in the hook. AC6 observes it through the fixture, so the python statement has to exist too. Each copy has its own observation, and the hook's comment names the python statement as the rule.
- **Evidence:** `verdict_flow.py --fixture held-policy` exited 0: `push-selected` with an unset pusher value prints `export GATE_SELFTESTS=changed`, and `on-demand` prints none. The pre-push suite's SEL AC6 arm and its control are written. Their run and RED-first observation are owed at the close.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-5

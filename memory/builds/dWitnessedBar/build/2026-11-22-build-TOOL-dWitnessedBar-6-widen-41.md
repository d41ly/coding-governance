# TOOL-dWitnessedBar-6 widen 41 — unarmed-branches widened

**Serves:** widen TOOL-dWitnessedBar-6

- **Population:** unarmed-branches
- **Keys:** `tools/push-main.sh	exit	check_landing_verdict "$(git rev-parse --verify HEAD)" || exit 1`, `tools/push-main.sh	exit	check_landing_verdict "$(git rev-parse --verify "refs/heads/$def")" || exit 1`
- **Reason:** the unit's builder marked these rows with its return file, not a widen record; the widen door re-admits them at the count measured
- **Caused-by:** TOOL-dWitnessedBar-6

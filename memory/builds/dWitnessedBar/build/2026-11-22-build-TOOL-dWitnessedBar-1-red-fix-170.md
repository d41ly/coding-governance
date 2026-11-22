# TOOL-dWitnessedBar-1 red-fix 170 — policy check fixed in 5a71cb58

**Serves:** red-fix TOOL-dWitnessedBar-1

- **Leg:** policy check
- **Red line:** reader coverage: placement, placement.check and patch.ratify (owner dPlacedRequest) have no reader
- **Files:** tools/loop/claim.py, tools/loop/placement.py
- **Commit:** 5a71cb5811f6482a234e7b5c81e6cfdeaa2e2235
- **Rerun:** python tools/policy/check_policy.py: green, the reader arm finding nothing
- **Caused-by:** TOOL-dWitnessedBar-1

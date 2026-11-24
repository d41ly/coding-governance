# TOOL-dWitnessedBar-6 red-fix 169 — policy check fixed in 12f6ff42

**Serves:** red-fix TOOL-dWitnessedBar-6

- **Leg:** policy check
- **Red line:** reader coverage: verdict.red-route, verdict.remote.trust, verdict.remote.pin-scope and verdict.remote.pin (owner dWitnessedBar) have no reader
- **Files:** tools/run-gates/remote_verdict.py, tools/run-gates/verdict_flow.py
- **Commit:** 12f6ff42453ecee779cdd189dad056eb0bd7b724
- **Rerun:** python tools/policy/check_policy.py: the reader arm reads every owner-dWitnessedBar key; only dPlacedRequest's keys stay unread, fixed by the next red fix
- **Caused-by:** TOOL-dWitnessedBar-6

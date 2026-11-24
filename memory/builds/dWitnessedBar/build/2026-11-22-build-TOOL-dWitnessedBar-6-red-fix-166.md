# TOOL-dWitnessedBar-6 red-fix 166 — remote literals (kit code names no remote) fixed in 45c306f3

**Serves:** red-fix TOOL-dWitnessedBar-6

- **Leg:** remote literals (kit code names no remote)
- **Red line:** remote-literals: the remote-ci reader defaulted its remote to a literal name rather than resolving it through the ladder
- **Files:** memory/map/generated/symbols.json, tools/run-gates/remote_verdict.py
- **Commit:** 45c306f37ddec7a5a28bb973ecf6c8e69715ddd0
- **Rerun:** bash tools/check-remote-literals.sh: no line of remote_verdict.py named; the parity table holds the new inline copy
- **Caused-by:** TOOL-dWitnessedBar-6

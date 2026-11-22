# TOOL-dWitnessedBar-43 red-fix 167 — remote literals (kit code names no remote) fixed in e1f0f88f

**Serves:** red-fix TOOL-dWitnessedBar-43

- **Leg:** remote literals (kit code names no remote)
- **Red line:** remote-literals: the verdict backends module defaulted its peer and verify-peer remotes to a literal name, and its fixtures named their scratch remote the same way
- **Files:** tools/run-gates/verdict_backends.py
- **Commit:** e1f0f88fbd3c094f5e05698ba5a0bad3cfb8ba55
- **Rerun:** bash tools/check-remote-literals.sh: no line of verdict_backends.py named; the module imports and resolves its remote through the ladder
- **Caused-by:** TOOL-dWitnessedBar-43

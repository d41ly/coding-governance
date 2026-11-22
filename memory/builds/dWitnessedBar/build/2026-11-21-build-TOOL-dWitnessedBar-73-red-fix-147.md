# TOOL-dWitnessedBar-73 red-fix 147 — shell hygiene (a loop fed by a command substitution) fixed in 815598a5

**Serves:** red-fix TOOL-dWitnessedBar-73

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** sh-hygiene: 1 finding(s) in the run-gates gov suite, a loop fed by a here-string holding a command substitution
- **Files:** tools/run-gates/run-gates.gov.test.sh
- **Commit:** 815598a5dd4a9e8dd8e10644b690e31501b121cb
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dWitnessedBar-73

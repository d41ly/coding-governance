# TOOL-dWitnessedBar-73 red-fix 147 — shell hygiene (a loop fed by a command substitution) fixed in da6037d4

**Serves:** red-fix TOOL-dWitnessedBar-73

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** sh-hygiene: 1 finding(s) in the run-gates gov suite, a loop fed by a here-string holding a command substitution
- **Files:** tools/run-gates/run-gates.gov.test.sh
- **Commit:** da6037d487dd9fb4999b675233855c21159ddf1e
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dWitnessedBar-73

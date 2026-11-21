# TOOL-dWitnessedBar-90 widen 25 — shell-role widened

**Serves:** widen TOOL-dWitnessedBar-90

- **Population:** shell-role
- **Keys:** `tools/run-gates/run-gates.gov.test.sh`
- **Reason:** TOOL-dWitnessedBar-90 S1: the canary call site reads a check_canary_keys return outside 0 to 3 as a failure, printing the code; the row is set to the file's measured 853 code lines (`tools/gate-lint/sh_hygiene.py#measure_code_lines`), 852 at base `197df554d`
- **Caused-by:** TOOL-dWitnessedBar-90

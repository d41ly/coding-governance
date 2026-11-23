# TOOL-dQuietDisk-37 widen 22 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-37

- **Population:** shell-role
- **Keys:** `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh`, `.githooks/pre-push.test.sh`, `tools/lib/lib-selftest.test.sh`, `tools/lib/resolve-python.test.sh`, `tools/run-gates/run-gates.test.sh`, `tools/run-gates/run-selftests.sh`, `tools/run-gates/run-selftests.test.sh`
- **Reason:** TOOL-dQuietDisk-37, the closing review's batched minors: the template block folds the builder arguments into its key (template-cache.sh 77 to 81, lib-selftest.sh 253 to 257, pre-push.test.sh 2592 to 2595), run-selftests.sh exports its owned root for --serial (1630 to 1631), and the new arms in lib-selftest.test.sh (246 to 274), resolve-python.test.sh (1569 to 1596), run-gates.test.sh (3220 to 3254) and run-selftests.test.sh (1003 to 1013), measured by sh_hygiene.py#measure_code_lines at f40895118
- **Caused-by:** TOOL-dQuietDisk-37

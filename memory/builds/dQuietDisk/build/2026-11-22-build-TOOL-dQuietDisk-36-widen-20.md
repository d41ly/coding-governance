# TOOL-dQuietDisk-36 widen 20 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-36

- **Population:** shell-role
- **Keys:** `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh`, `.githooks/pre-push.test.sh`, `tools/lib/lib-selftest.test.sh`, `tools/lib/resolve-python.test.sh`, `tools/run-gates/run-gates.turnstile.test.sh`
- **Reason:** TOOL-dQuietDisk-36, the closing review's round-1 fold: the template block's three copies gain remove_git_env_leaks and run each git verb as a subshell body (template-cache.sh 69 to 77, lib-selftest.sh 245 to 253, pre-push.test.sh 2584 to 2592), the selftest harness gains its three GIT_DIR arms (221 to 246), the resolver suite its list-parity check (1560 to 1569), and turnstile arm 22 its orphan and relative owners (1206 to 1218), measured by sh_hygiene.py#measure_code_lines at 4840e65ed
- **Caused-by:** TOOL-dQuietDisk-36

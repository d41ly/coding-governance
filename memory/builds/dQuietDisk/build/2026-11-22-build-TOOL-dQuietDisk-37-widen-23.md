# TOOL-dQuietDisk-37 widen 23 — spawn-idiom-sites widened

**Serves:** widen TOOL-dQuietDisk-37

- **Population:** spawn-idiom-sites
- **Keys:** `tools/lib/lib-selftest.test.sh	cat-file`, `tools/lib/resolve-python.test.sh	var-pipe`, `tools/run-gates/run-gates.test.sh	var-pipe`
- **Reason:** TOOL-dQuietDisk-37's arms: the argument-key and race arms read markers and logs through $(cat ...) (lib-selftest.test.sh 30 to 36), the Python sweep arm pipes its captured stderr into grep (resolve-python.test.sh 16 to 17), and arm 3h1's trace check pipes the trace into grep (run-gates.test.sh 164 to 165), measured by sh_hygiene.py --spawn-idioms at f40895118
- **Caused-by:** TOOL-dQuietDisk-37

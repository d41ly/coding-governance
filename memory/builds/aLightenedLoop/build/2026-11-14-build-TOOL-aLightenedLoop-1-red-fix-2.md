# TOOL-aLightenedLoop-1 red-fix 2 — encoding posture (text IO names its encoding) fixed in ec94bb84

**Serves:** red-fix TOOL-aLightenedLoop-1

- **Leg:** encoding posture (text IO names its encoding)
- **Red line:** tools/memory-tree/gen_build_index.py:1139:15 — subprocess.run(...) has no encoding=
- **Files:** tools/memory-tree/gen_build_index.py
- **Commit:** ec94bb846779ded59bbd91784d8512740e0e1b72
- **Rerun:** python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills
- **Caused-by:** TOOL-aLightenedLoop-1

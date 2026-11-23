# TOOL-dTotalRecall-19 red-fix 16 — encoding posture (text IO names its encoding) fixed in 467fbf5d

**Serves:** red-fix TOOL-dTotalRecall-19

- **Leg:** encoding posture (text IO names its encoding)
- **Red line:** tools/memory-tree/build_records.py: 1 unencoded [subprocess] call(s) and no registry row declares them — pass encoding="utf-8"
- **Files:** tools/memory-tree/build_records.py
- **Commit:** 467fbf5d77c06d009ac5fc423f0f87be6ad94e51
- **Rerun:** python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills: no undeclared file-io/subprocess site
- **Caused-by:** TOOL-dTotalRecall-19

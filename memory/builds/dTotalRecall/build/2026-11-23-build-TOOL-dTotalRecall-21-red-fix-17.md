# TOOL-dTotalRecall-21 red-fix 17 — encoding posture (text IO names its encoding) fixed in 5f096a71

**Serves:** red-fix TOOL-dTotalRecall-21

- **Leg:** encoding posture (text IO names its encoding)
- **Red line:** tools/memory-recall/test_recall_floor.py: the registry declares 4 [subprocess] site(s) and the scan measures 5
- **Files:** tools/memory-recall/test_recall_floor.py
- **Commit:** 5f096a7149275ee4a01e56578ad8fadae60c88f0
- **Rerun:** python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills: no undeclared file-io/subprocess site
- **Caused-by:** TOOL-dTotalRecall-21

# TOOL-dDeclaredLoop-40 red-fix 5 — encoding posture (text IO names its encoding) fixed in 6583c884

**Serves:** red-fix TOOL-dDeclaredLoop-40

- **Leg:** encoding posture (text IO names its encoding)
- **Red line:** tools/memory-tree/routed_commits.py: 1 unencoded [subprocess] call(s) and no registry row declares them — pass encoding=utf-8
- **Files:** tools/memory-tree/routed_commits.py
- **Commit:** 6583c88462e83ec2c800919c921b16ee2c2d355d
- **Rerun:** python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-40

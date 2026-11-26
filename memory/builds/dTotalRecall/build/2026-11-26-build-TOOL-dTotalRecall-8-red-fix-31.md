# TOOL-dTotalRecall-8 red-fix 31 — govkit acceptance matrix fixed in ac4c575b

**Serves:** red-fix TOOL-dTotalRecall-8

- **Leg:** govkit acceptance matrix
- **Red line:** scratch install: the declared leg set and the stated expectations are the same set — declared adds 'code record'
- **Files:** tools/govkit/matrix.py
- **Commit:** ac4c575b675ff323226ca28cd23b9e9e859b69d4
- **Rerun:** python tools/govkit/matrix.py: the set check ok, leg 'code record' prints its stated verdict and no traceback; exit 1 on one other check, 'playbook render selftest', whose policy.py preset --diff did not answer within 3s under host load (DERIVED 2026-11-26, the matrix log)
- **Caused-by:** TOOL-dTotalRecall-8

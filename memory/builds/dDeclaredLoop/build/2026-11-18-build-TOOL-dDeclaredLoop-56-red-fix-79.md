# TOOL-dDeclaredLoop-56 red-fix 79 — govkit acceptance matrix fixed in 0d97fd67

**Serves:** red-fix TOOL-dDeclaredLoop-56

- **Leg:** govkit acceptance matrix
- **Red line:** FAIL scratch install: leg 'playbook render selftest' prints its stated verdict where it was installed
- **Files:** tools/playbook/instructions_edit.py
- **Commit:** 0d97fd672687128687a10aef05217d5d053c75fb
- **Rerun:** python tools/playbook/overlay.py --fixture --plant write-then-render
- **Caused-by:** TOOL-dDeclaredLoop-56

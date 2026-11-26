# TOOL-dTotalRecall-53 red-fix 25 — positional (the citation check alone) fixed in 1c93f20c

**Serves:** red-fix TOOL-dTotalRecall-53

- **Leg:** positional (the citation check alone)
- **Red line:** positional: every build README's parallel note under its build-order table cited the build method's M6 positionally, refused in each render
- **Files:** tools/memory-tree/gen_build_index.py
- **Commit:** 1c93f20c2861184fedc8b3010a8d6a2bf0bdd2c8
- **Rerun:** python tools/playbook/positional.py check after gen_build_index.py --write re-rendered the READMEs
- **Caused-by:** TOOL-dTotalRecall-53

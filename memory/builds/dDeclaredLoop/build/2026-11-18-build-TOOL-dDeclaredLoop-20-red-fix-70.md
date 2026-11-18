# TOOL-dDeclaredLoop-20 red-fix 70 — shell hygiene (a fork spent on builtin work) fixed in 96933846

**Serves:** red-fix TOOL-dDeclaredLoop-20

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/unattended/unattended.sh: the registry declares 40 site(s) at pure-fn-subst and the scan measures 44
- **Files:** memory/LIVE.md, memory/builds/dDeclaredLoop/README.md, memory/builds/dDeclaredLoop/build/2026-11-18-build-TOOL-dDeclaredLoop-4-red-fix-68.md, memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-4.md, memory/project/fork-ceilings.txt, memory/project/spawn-idiom-sites.txt
- **Commit:** 96933846972428687c506f5e40634714823ad18d
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt .
- **Caused-by:** TOOL-dDeclaredLoop-20

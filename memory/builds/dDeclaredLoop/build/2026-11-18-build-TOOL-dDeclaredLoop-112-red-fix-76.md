# TOOL-dDeclaredLoop-112 red-fix 76 — memory hygiene fixed in e7e8976c

**Serves:** red-fix TOOL-dDeclaredLoop-112

- **Leg:** memory hygiene
- **Red line:** the orphan-id check: id TOOL-tFork-91 is cited but never defined
- **Files:** memory/project/fork-ceilings.txt
- **Commit:** e7e8976ceaf347326fe04688f148ba5b73c30e55
- **Rerun:** bash tools/memory-tree/check-memory-hygiene.sh --only 14,15
- **Caused-by:** TOOL-dDeclaredLoop-112

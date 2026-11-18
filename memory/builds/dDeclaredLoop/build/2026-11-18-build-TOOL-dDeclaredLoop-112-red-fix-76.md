# TOOL-dDeclaredLoop-112 red-fix 76 — memory hygiene fixed in 9c474e05

**Serves:** red-fix TOOL-dDeclaredLoop-112

- **Leg:** memory hygiene
- **Red line:** HYGIENE check 14: id TOOL-tFork-91 is cited but never defined
- **Files:** memory/project/fork-ceilings.txt
- **Commit:** 9c474e0570d6ef355e47bf5094876a0f6d1cc873
- **Rerun:** bash tools/memory-tree/check-memory-hygiene.sh --only 14,15
- **Caused-by:** TOOL-dDeclaredLoop-112

# TOOL-aMeasuredDrag-12 red-fix 6 — shell hygiene (a loop fed by a command substitution) fixed in 09afb179

**Serves:** red-fix TOOL-aMeasuredDrag-12

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** .githooks/pre-commit.test.sh: a loop is fed by `<<<` holding a command substitution, and no registry row declares it (1 site(s))
- **Files:** .githooks/pre-commit.test.sh
- **Commit:** 09afb1795e9652098d14f75a4a1aeec97ed3f7a3
- **Rerun:** sh_hygiene.py memory/project/substitution-fed-loops.txt · exit 0, and all four shell-hygiene legs exit 0
- **Caused-by:** TOOL-aMeasuredDrag-12

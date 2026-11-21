# TOOL-dPlacedRequest-99 red-fix 53 — shell hygiene (a loop fed by a command substitution) fixed in 4129cd5f

**Serves:** red-fix TOOL-dPlacedRequest-99

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** skills/session-kickoff/manifest-check.test.sh feeds a while loop by <<< over a value assigned from a command substitution, a shape the red fix b833648b1 introduced
- **Files:** skills/session-kickoff/manifest-check.test.sh
- **Commit:** 4129cd5f55ed9fc9304831b64987d118bc275ae4
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dPlacedRequest-99

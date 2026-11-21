# TOOL-dPlacedRequest-99 red-fix 53 — shell hygiene (a loop fed by a command substitution) fixed in eb386262

**Serves:** red-fix TOOL-dPlacedRequest-99

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** skills/session-kickoff/manifest-check.test.sh feeds a while loop by <<< over a value assigned from a command substitution, a shape the red fix 750b0a98b introduced
- **Files:** skills/session-kickoff/manifest-check.test.sh
- **Commit:** eb386262127a48091cf991758461d3b7466ad946
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt
- **Caused-by:** TOOL-dPlacedRequest-99

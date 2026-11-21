# TOOL-dPlacedRequest-21 red-fix 40 — remote literals (kit code names no remote) fixed in b2e48400

**Serves:** red-fix TOOL-dPlacedRequest-21

- **Leg:** remote literals (kit code names no remote)
- **Red line:** nine run_fixture_git calls in tools/loop/claim.py's fixtures (TOOL-dPlacedRequest-21) and four in tools/loop/budget.py's (TOOL-dPlacedRequest-14) push, fetch, set-head and set-url a literal remote
- **Files:** tools/loop/budget.py, tools/loop/claim.py
- **Commit:** b2e484005fcac6e8c1295b794722961d253711f0
- **Rerun:** bash tools/check-remote-literals.sh
- **Caused-by:** TOOL-dPlacedRequest-21

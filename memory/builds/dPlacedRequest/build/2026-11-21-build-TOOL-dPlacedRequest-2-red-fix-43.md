# TOOL-dPlacedRequest-2 red-fix 43 — shell hygiene (a stage committed with no staged-diff test) fixed in 0ea9f38e

**Serves:** red-fix TOOL-dPlacedRequest-2

- **Leg:** shell hygiene (a stage committed with no staged-diff test)
- **Red line:** skills/session-kickoff/card-store.fixture.sh commits its seed after add -A with no staged-diff test between them
- **Files:** skills/session-kickoff/card-store.fixture.sh
- **Commit:** 0ea9f38e72aaa712bdc19f3f692253659536acc9
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --stage-commits memory/project/stage-commit-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-2

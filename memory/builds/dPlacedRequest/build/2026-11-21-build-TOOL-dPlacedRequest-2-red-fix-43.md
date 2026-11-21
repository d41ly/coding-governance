# TOOL-dPlacedRequest-2 red-fix 43 — shell hygiene (a stage committed with no staged-diff test) fixed in 8104f7f5

**Serves:** red-fix TOOL-dPlacedRequest-2

- **Leg:** shell hygiene (a stage committed with no staged-diff test)
- **Red line:** skills/session-kickoff/card-store.fixture.sh commits its seed after add -A with no staged-diff test between them
- **Files:** skills/session-kickoff/card-store.fixture.sh
- **Commit:** 8104f7f5bcf390e2d6c4b4e19b2a2dbbdb780ca9
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --stage-commits memory/project/stage-commit-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-2

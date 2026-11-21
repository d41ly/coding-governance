# TOOL-dPlacedRequest-2 red-fix 44 — shell hygiene (a fixed-name temp renamed into place) fixed in 8104f7f5

**Serves:** red-fix TOOL-dPlacedRequest-2

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Red line:** skills/session-kickoff/card-store.fixture.sh renames nine fixed-name sources into place, its stub-policy rewrite among them, with no registry row
- **Files:** skills/session-kickoff/card-store.fixture.sh
- **Commit:** 8104f7f5bcf390e2d6c4b4e19b2a2dbbdb780ca9
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-2

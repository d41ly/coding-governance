# TOOL-dPlacedRequest-2 red-fix 44 — shell hygiene (a fixed-name temp renamed into place) fixed in 0ea9f38e

**Serves:** red-fix TOOL-dPlacedRequest-2

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Red line:** skills/session-kickoff/card-store.fixture.sh renames nine fixed-name sources into place, its stub-policy rewrite among them, with no registry row
- **Files:** skills/session-kickoff/card-store.fixture.sh
- **Commit:** 0ea9f38e72aaa712bdc19f3f692253659536acc9
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-2

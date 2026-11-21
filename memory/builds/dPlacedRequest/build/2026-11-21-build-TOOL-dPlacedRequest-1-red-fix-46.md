# TOOL-dPlacedRequest-1 red-fix 46 — shell hygiene (a fixed-name temp renamed into place) fixed in 701a20b5

**Serves:** red-fix TOOL-dPlacedRequest-1

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Red line:** tools/unattended/unattended.sh renames nine fixed-name or pid-suffixed temps into place against a registry declaring two: the feed block's three, last-fetch, the queued-claim refs, the queue rewrite and the request copy
- **Files:** tools/unattended/unattended.sh
- **Commit:** 701a20b5cef403785ee3f95bffd40518405af0de
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-1

# TOOL-dPlacedRequest-13 red-fix 45 — shell hygiene (a fixed-name temp renamed into place) fixed in fa2cf927

**Serves:** red-fix TOOL-dPlacedRequest-13

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Red line:** the feed block stages gov-feed.seq and gov-feed.log under pid-suffixed names in tools/lib/gov-feed.sh and its inline copies in push-main.sh, post-merge.sh and unattended.sh
- **Files:** tools/lib/gov-feed.sh, tools/push-main.sh, tools/run-gates/post-merge.sh
- **Commit:** fa2cf927b222c39258ed4b8a00a19b31255e3d53
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-13

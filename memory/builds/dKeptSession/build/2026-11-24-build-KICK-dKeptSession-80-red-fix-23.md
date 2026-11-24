# KICK-dKeptSession-80 red-fix 23 — encoding posture (JavaScript text IO names its encoding) fixed in dd7e4082

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** encoding posture (JavaScript text IO names its encoding)
- **Red line:** tools/hooks/scratch-guard.js: 1 unencoded [js-io] call(s) and no registry row declares them, appendFileSync names no encoding
- **Files:** tools/hooks/scratch-guard.js
- **Commit:** dd7e4082fbe92ea6fc0e37e0aa1a114e613faf04
- **Rerun:** python3 tools/gate-lint/encoding_posture.py --js memory/project/encoding-js-sites.txt . tools skills ':!memory' · OK, no undeclared js-io site
- **Caused-by:** KICK-dKeptSession-80

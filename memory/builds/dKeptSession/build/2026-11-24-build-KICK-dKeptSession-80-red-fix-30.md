# KICK-dKeptSession-80 red-fix 30 — tags (the resolver's checks) fixed in 0200dd0c

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** tags (the resolver's checks)
- **Red line:** GATE FAIL tags (the resolver's checks), timed out after 420s (PINNED 2026-11-24, the bar at 3b7cfc355), again on its serial retry
- **Files:** tools/playbook/tag_index.py
- **Commit:** 0200dd0cc89ecd6b2791e7106feed01e5208c775
- **Rerun:** python tools/playbook/gov_tag.py check · exit 0, 0 red, 191 s warm where it took 477 s before (DERIVED, each run's own clock)
- **Caused-by:** KICK-dKeptSession-80

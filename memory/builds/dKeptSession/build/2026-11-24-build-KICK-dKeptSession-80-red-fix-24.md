# KICK-dKeptSession-80 red-fix 24 — shell hygiene (a location probe asked from a moved directory) fixed in ec9226a9

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** shell hygiene (a location probe asked from a moved directory)
- **Red line:** tools/hooks/actions-free.fixture.sh and tools/unattended/unattended.test.sh each ask a location probe bare, and no registry row declares it
- **Files:** skills/session-kickoff/card-store.fixture.sh, tools/hooks/actions-free.fixture.sh, tools/unattended/unattended.test.sh
- **Commit:** ec9226a9bccc480f8683958ab3a205ce863d9a4c
- **Rerun:** sh_hygiene.py --location-probes over the tree · 0 gated sites
- **Caused-by:** KICK-dKeptSession-80

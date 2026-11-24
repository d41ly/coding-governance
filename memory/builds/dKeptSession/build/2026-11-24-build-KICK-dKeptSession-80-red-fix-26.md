# KICK-dKeptSession-80 red-fix 26 — shell hygiene (a fixed-name temp renamed into place) fixed in ec9226a9

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Red line:** skills/session-kickoff/card-store.fixture.sh, the registry declares 8 sites at fixed-temp and the scan measures 10
- **Files:** skills/session-kickoff/card-store.fixture.sh, tools/hooks/actions-free.fixture.sh, tools/unattended/unattended.test.sh
- **Commit:** ec9226a9bccc480f8683958ab3a205ce863d9a4c
- **Rerun:** sh_hygiene.py --temp-names over the tree · no finding, card-store registered at 8
- **Caused-by:** KICK-dKeptSession-80

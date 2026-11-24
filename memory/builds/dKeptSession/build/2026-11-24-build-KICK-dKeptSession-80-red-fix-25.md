# KICK-dKeptSession-80 red-fix 25 — shell hygiene (a fork spent on builtin work) fixed in ec9226a9

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Red line:** tools/hooks/actions-free.fixture.sh, 1 var-pipe site and no registry row, and tools/unattended/unattended.test.sh, 24 printf-subst sites measured against 23 declared
- **Files:** skills/session-kickoff/card-store.fixture.sh, tools/hooks/actions-free.fixture.sh, tools/unattended/unattended.test.sh
- **Commit:** ec9226a9bccc480f8683958ab3a205ce863d9a4c
- **Rerun:** sh_hygiene.py --spawn-idioms over the tree · exit 0
- **Caused-by:** KICK-dKeptSession-80

# KICK-dKeptSession-80 red-fix 32 — policy check fixed in 88adfbc8

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** policy check
- **Red line:** reader coverage, tests.history-verdicts and tests.fixture-templates (owner dQuietDisk) each has no reader; GATE attr policy check OWN, the diff against R touches its comparator
- **Files:** tools/policy/check_policy.py
- **Commit:** 88adfbc8089d035a8005e045279d5d6a9de3513b
- **Rerun:** python tools/policy/check_policy.py · exit 0; --fixture reader-coverage · 0 wrong with reader-argv green and argv-unbound red
- **Caused-by:** KICK-dKeptSession-80

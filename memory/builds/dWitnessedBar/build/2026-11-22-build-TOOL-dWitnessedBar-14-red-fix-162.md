# TOOL-dWitnessedBar-14 red-fix 162 — shell hygiene (a location probe asked from a moved directory) fixed in 50257f0c

**Serves:** red-fix TOOL-dWitnessedBar-14

- **Leg:** shell hygiene (a location probe asked from a moved directory)
- **Red line:** sh-hygiene: a location probe asked bare in the unattended kit's record reader, with no registry row declaring it
- **Files:** tools/unattended/lib-unattended.sh
- **Commit:** 50257f0cad8cac8ab3a2603519d1d044845524d8
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --location-probes: OK, no undeclared location probe
- **Caused-by:** TOOL-dWitnessedBar-14

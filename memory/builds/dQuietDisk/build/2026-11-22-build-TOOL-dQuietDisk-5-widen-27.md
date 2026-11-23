# TOOL-dQuietDisk-5 widen 27 — quoting-sites widened

**Serves:** widen TOOL-dQuietDisk-5

- **Population:** quoting-sites
- **Keys:** `tools/run-gates/run-gates.sh	tab-ifs-read`
- **Reason:** TOOL-dQuietDisk-5's one-diff guard reads its moved-guards table with two IFS=TAB read loops whose leading field is the leg index, never empty, so a collapsed run of tabs cannot shift it (12 to 14, measured by sh_hygiene.py --quoting at 40607fd2a)
- **Caused-by:** TOOL-dQuietDisk-5

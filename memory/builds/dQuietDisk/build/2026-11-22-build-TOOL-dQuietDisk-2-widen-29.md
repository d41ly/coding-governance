# TOOL-dQuietDisk-2 widen 29 — quoting-sites widened

**Serves:** widen TOOL-dQuietDisk-2

- **Population:** quoting-sites
- **Keys:** `tools/unattended/check-pass-order.sh	tab-ifs-read`
- **Reason:** TOOL-dQuietDisk-2 reads the history store's reply rows with two IFS=TAB read loops of three fields: the item id, the store's hit or miss verdict, never empty, and the body last, so a collapsed tab run cannot shift a field (0 to 2, measured by sh_hygiene.py --quoting at 40607fd2a)
- **Caused-by:** TOOL-dQuietDisk-2

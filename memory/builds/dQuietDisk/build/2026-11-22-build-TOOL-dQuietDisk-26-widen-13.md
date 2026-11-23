# TOOL-dQuietDisk-26 widen 13 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-26

- **Population:** shell-role
- **Keys:** `tools/check-wiring.sh`, `tools/check-wiring.test.sh`
- **Reason:** TOOL-dQuietDisk-26: check-wiring.sh gains read_tree_listing, read_listed_attrs, read_listed_attr and check_listed and routes its per-site reads through them (1352 code lines against the row's 1306), and the suite gains the QD26 AC1 and AC3 arms (1671 against 1660), measured by sh_hygiene.py#measure_code_lines at b31f3bd11
- **Caused-by:** TOOL-dQuietDisk-26

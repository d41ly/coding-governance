# TOOL-dQuietDisk-26 widen 12 — substitution-fed-loops widened

**Serves:** widen TOOL-dQuietDisk-26

- **Population:** substitution-fed-loops
- **Keys:** `tools/check-wiring.sh	EOF`
- **Reason:** TOOL-dQuietDisk-26: check_hook_modes now assigns its listing with a plain ls=$(...) for this checkout, so the scanner's one-hop follow reaches the $ls heredoc loop that the old 'if ! ls=$(...)' assignment hid; the loop itself predates the unit (3 to 4 sites, measured by sh_hygiene.py at b31f3bd11)
- **Caused-by:** TOOL-dQuietDisk-26

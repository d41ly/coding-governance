# TOOL-dQuietDisk-9 widen 26 — temp-name-sites widened

**Serves:** widen TOOL-dQuietDisk-9

- **Population:** temp-name-sites
- **Keys:** `tools/run-gates/run-selftests.sh	fixed-temp`
- **Reason:** TOOL-dQuietDisk-9 carries the health_log_sh block inline in run-selftests.sh, byte-equal to run-gates.sh's copy whose same trim temp "$_hl_log.trim.$$" is a registered fixed-temp site; the parity row keeps the copies equal, so the site comes with the block (0 to 1, measured by sh_hygiene.py --temp-names at 40607fd2a)
- **Caused-by:** TOOL-dQuietDisk-9

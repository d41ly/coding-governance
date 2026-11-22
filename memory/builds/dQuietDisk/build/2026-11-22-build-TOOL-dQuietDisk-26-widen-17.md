# TOOL-dQuietDisk-26 widen 17 — spawn-idiom-sites widened

**Serves:** widen TOOL-dQuietDisk-26

- **Population:** spawn-idiom-sites
- **Keys:** `tools/check-wiring.sh	var-pipe`
- **Reason:** TOOL-dQuietDisk-26 S9: the checker reads its one listing through printf pipes rather than here-strings, because bash writes a large here-string to a temp file; the listing pipes save 18 git processes per invocation (3 to 4 sites, measured by sh_hygiene.py --spawn-idioms at 3470633ba)
- **Caused-by:** TOOL-dQuietDisk-26

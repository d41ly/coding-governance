# TOOL-dQuietDisk-37 widen 28 — quoting-sites widened

**Serves:** widen TOOL-dQuietDisk-37

- **Population:** quoting-sites
- **Keys:** `tools/run-gates/run-gates.test.sh	heredoc-source`
- **Reason:** TOOL-dQuietDisk-37's arm 8f writes the fixture runner's env.sh leg through a quoted heredoc, the shape the suite's other fixture legs use (4 to 5, measured by sh_hygiene.py --quoting at 40607fd2a)
- **Caused-by:** TOOL-dQuietDisk-37

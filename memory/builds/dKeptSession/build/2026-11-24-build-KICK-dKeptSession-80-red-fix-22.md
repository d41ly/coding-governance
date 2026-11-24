# KICK-dKeptSession-80 red-fix 22 — layer dependencies (the core never depends on an expansion) fixed in 3c017555

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** layer dependencies (the core never depends on an expansion)
- **Red line:** layers: RED skills/session-kickoff/manifest-check.sh, probe, core kit kickoff-manifest depends on non-core kit runlog, and no optional row of its descriptor names the file as part
- **Files:** tools/govkit/entries/kickoff-manifest.kit.toml
- **Commit:** 3c01755526437f0aa6252ae67f68461009255fb1
- **Rerun:** python tools/playbook/check_layers.py · 0 red
- **Caused-by:** KICK-dKeptSession-80

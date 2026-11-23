# TOOL-dQuietDisk-9 widen 16 — spawn-idiom-sites widened

**Serves:** widen TOOL-dQuietDisk-9

- **Population:** spawn-idiom-sites
- **Keys:** `tools/run-gates/run-selftests.sh	pure-fn-subst`
- **Reason:** TOOL-dQuietDisk-9 S4: run-selftests.sh reads its health log once through $(derive_health_log ...), a builtins-only function, for the owned root's sweep events (3 to 4 sites, rev-6 of the spec)
- **Caused-by:** TOOL-dQuietDisk-9

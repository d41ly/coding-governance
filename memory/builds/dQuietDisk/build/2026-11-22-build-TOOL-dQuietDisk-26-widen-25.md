# TOOL-dQuietDisk-26 widen 25 — fork-ceilings widened

**Serves:** widen TOOL-dQuietDisk-26

- **Population:** fork-ceilings
- **Keys:** `check-wiring	5.3	55	git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false && git commit -q -m seed --allow-empty	bash "$ROOT/tools/check-wiring.sh" --check`
- **Reason:** TOOL-dQuietDisk-26: check-wiring.sh reads its one tree listing through printf pipes, one more forked subshell per --check in the probe's fixture (45 to 46), while the same change removes 18 git processes per --check (44 to 26, measured at AC1); measured by fork-count.sh at 40607fd2a
- **Caused-by:** TOOL-dQuietDisk-26

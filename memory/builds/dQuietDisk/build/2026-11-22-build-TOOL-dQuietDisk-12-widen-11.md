# TOOL-dQuietDisk-12 widen 11 — shell-role widened

**Serves:** widen TOOL-dQuietDisk-12

- **Population:** shell-role
- **Keys:** `.githooks/pre-push.test.sh`
- **Reason:** TOOL-dQuietDisk-12 adds 125 shell lines to .githooks/pre-push.test.sh, 2459 to 2584: the inline template_cache_sh block, the fixture-template prologue, build_pushed_fixture and run_tree_in_stage, the three builders split into tree and call halves, and the templated fixture's arm
- **Caused-by:** TOOL-dQuietDisk-12

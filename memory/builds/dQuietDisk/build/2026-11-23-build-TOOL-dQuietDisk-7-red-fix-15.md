# TOOL-dQuietDisk-7 red-fix 15 — selftest harness self-test fixed in 2e09f6cb

**Serves:** red-fix TOOL-dQuietDisk-7

- **Leg:** selftest harness self-test
- **Red line:** nope the key is not stable — fatal: could not open '/tmp/.../key.in' for reading; nope an arm's result moved with the switch
- **Files:** .githooks/pre-push.test.sh, tools/lib/lib-selftest.sh, tools/lib/lib-selftest.test.sh, tools/lib/template-cache.sh
- **Commit:** 2e09f6cbc8a46175ab4f224268fc9d747c31a419
- **Rerun:** bash tools/lib/lib-selftest.test.sh under an MSYS TMPDIR: PASS (38 assertions)
- **Caused-by:** TOOL-dQuietDisk-7

# TOOL-dQuietDisk-7 red-fix 12 — remote literals (kit code names no remote) fixed in 990c7406

**Serves:** red-fix TOOL-dQuietDisk-7

- **Leg:** remote literals (kit code names no remote)
- **Red line:** tools/lib/template_cache.py:233: run_git(dest, "remote", "remove", "origin")
- **Files:** .githooks/pre-push.test.sh, tools/lib/lib-selftest.sh, tools/lib/template-cache.sh, tools/lib/template_cache.py
- **Commit:** 990c7406149e9f314e113b70f7144853ecb5fa88
- **Rerun:** check-remote-literals.sh: clean, 300 files; a probe clone under clone.defaultRemoteName=upstream with -o template-source keeps no remote
- **Caused-by:** TOOL-dQuietDisk-7

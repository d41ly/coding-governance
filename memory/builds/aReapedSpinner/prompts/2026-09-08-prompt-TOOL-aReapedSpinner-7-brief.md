# Brief — TOOL-aReapedSpinner-7, the gate runner's teardown

**Serves:** journal TOOL-aReapedSpinner-7

What this pass was handed: the unit's spec at rev-4 — re-scoped after D10 showed rev-1's premise was
stale — and `run-gates.sh:428-474`, `:955-957`, `:1517` read at source.

What it builds: a bounded teardown reap in `cleanup()`, profile-time detection with an announced
fallback, and a delegating `reap_leg_tree` that keeps the runner's own survivor sweep beside it.

The four things that are not obvious:

- **The wall path was never the leak.** It has walked and killed descendants since
  `TOOL-aQuenchedHarness-1`. `cleanup` at the INT/TERM/HUP traps killed NOTHING.
- **The reap comes BEFORE `rm -rf "$WORK"`.** Removing the scratch dir first is what turns a live
  leg into a process writing to a deleted path.
- **It is BOUNDED and the release follows it unconditionally.** A hung reap ahead of `ts_release`
  would strand a turnstile ticket and queue every later bar on the host — observed for real this
  session, from a `kill -9` rather than from this code.
- **Detection asks whether the RUNNER is in scope**, not whether a directory is: every leg is its
  descendant, so one question answers it for all of them.

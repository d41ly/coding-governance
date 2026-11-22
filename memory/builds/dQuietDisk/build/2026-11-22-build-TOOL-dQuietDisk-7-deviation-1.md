# TOOL-dQuietDisk-7 deviation 1 — the harness also sources the wrong-shell refusal and calls it beside the resolver

**Serves:** deviation TOOL-dQuietDisk-7

- **Departs from:** `TOOL-dQuietDisk-7@rev-6` [S9, S11]
- **Hand-off:** spec-to-code
- **Before:** S9 has the bash face find its python by sourcing `tools/lib/resolve-python.sh` beside `lib-selftest.sh` and calling `resolve_python`, and S11 says `lib-selftest.sh` gains "the line that sources the resolver".
- **After:** inside `build_fixture`, on the first `--template` call of a suite run, `lib-selftest.sh` sources `resolve-python.sh`, then `refuse-wrong-shell.sh` from the same directory on the next line, then runs `refuse_wrong_shell || exit 2`, before it calls `resolve_python` for the `policy.py get` read. A suite that never passes `--template` sources neither file and runs neither call.
- **Cause:** builder discovery
- **Reason:** any tracked shell file under `tools/` that calls `resolve_python` at command position is a member of the wrong-shell population `tools/lib/refuse-wrong-shell.sh#derive_rws_population` derives, and `refuse-wrong-shell.sh --coverage`, which `tools/lib/resolve-python.test.sh` runs, breaks a member that neither sources that file nor calls `refuse_wrong_shell || exit 2`. The library's own USAGE names this three-line shape for a sourcer of the resolver. S9's "as the kit rules already require of it" covers the rule; S11's sentence names only one of the three lines. The calls sit inside a function body, so the order check, which reads top-level lines, has no call to order (PINNED, `derive_rws_population` run as a probe over this tree selected `tools/lib/history-store.sh`, which calls `resolve_python` inside `init_hs`).
- **Evidence:** the widen record `2026-11-22-build-TOOL-dQuietDisk-7-widen-7` counts these lines in `lib-selftest.sh`'s 243 code lines. The AC3 and AC6 probes ran `build_fixture --template` through the three lines with exit 0 on this node.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-7

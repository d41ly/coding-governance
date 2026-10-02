# Acceptance ledger — DEPL-aHalvedInstall-1

**Serves:** journal DEPL-aHalvedInstall-1

Built at `c93d8685` and `1c13da6f`. The arms live in `check_update_safety` in
`tools/govkit/selftest.py` and were run as a slice of that one function, 41 s, never the whole suite.
Every positive arm was observed RED with `read_conf_key_gaps` staged to return nothing and the
`update` hole call staged to iterate nothing; the two negative controls stayed green under that
break, which is what they are for.

The slice carries one failure that is not this unit's: `[aRF-17 AC5]`, the `git merge-file -p
--diff3` reproduction arm, fails identically on a detached worktree at `d53b503a`, before any change
here.

**Evidences:** DEPL-aHalvedInstall-1
- AC1 — `check` — `[aHI-1 AC1-AC2] check over DEMO_KEY=None names it, 'is ABSENT'` passed; red under the staged break
- AC2 — `<your-tool>` — the placeholder value is named `still the example's <...>`, and `"real"` names nothing
- AC3 — `defaults` — `read_conf_key_gaps` returns `[("A", "absent"), ("B", "placeholder")]` over two lists and a defaulted `C`
- AC4 — `CONF GAP` — the line precedes `ran demo:` in `update --write`'s output; red under the staged break
- AC5 — `UNDISCHARGED` — `check`'s hole messages are kept verbatim in `cmd_check`; `run_hole_probes` returns `stood-down` for the stand-down branch
- AC6 — amended rev-2 — `govkit epoch --base d53b503a` printed `unattended · FAILED` after `c93d8685`, and nothing after the 1.57 bump; govkit itself is not in its population (section 9, rev-2)

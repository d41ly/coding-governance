# Acceptance ledger — DEPL-aHalvedInstall-1

**Serves:** journal DEPL-aHalvedInstall-1

Built at `c93d8685` and `1c13da6f`. The arms live in `check_update_safety` in
`tools/govkit/selftest.py` and were run as a slice of that one function, 41 s, never the whole suite.
Every positive arm was observed RED with `read_conf_key_gaps` staged to return nothing and the
`update` hole call staged to iterate nothing; the two negative controls stayed green under that
break, which is what they are for.

The slice, run with its temp root under the session scratchpad, carried one failure that is not
this unit's: `[aRF-17 AC5]`, the `git merge-file -p --diff3` reproduction arm. It failed identically
on a detached worktree at `d53b503a`, and passed with the same code once the temp root was the short
system one, so it is the slice's own path length, not a product defect.

**Evidences:** DEPL-aHalvedInstall-1
- AC1 — `check` — `[aHI-1 AC1-AC2] check over DEMO_KEY=None names it, 'is ABSENT'` passed; red under the staged break
- AC2 — `<your-tool>` — the placeholder value is named `still the example's <...>`, and `"real"` names nothing
- AC3 — `defaults` — `read_conf_key_gaps` returns `[("A", "absent"), ("B", "placeholder")]` over two lists and a defaulted `C`
- AC4 — `CONF GAP` — the line precedes `ran demo:` in `update --write`'s output; red under the staged break
- AC5 — `UNDISCHARGED` — `check`'s hole messages are kept verbatim in `cmd_check`; `run_hole_probes` returns `stood-down` for the stand-down branch
- AC6 — amended rev-2 — `govkit epoch --base d53b503a` printed `unattended · FAILED` after `c93d8685`, and nothing after the 1.57 bump; govkit itself is not in its population (section 9, rev-2)
- AC7 — `DEMO_KEY=""` — `[aHI-1 AC1-AC2]` names it `is EMPTY`, and `'  '` too; red with the empty test staged away (`251d24ff`)
- AC8 — `unreadable` — `[aHI-1 AC8]`: with a directory at the conf path, `check` names it and `update` prints a `CONF GAP` and reaches its verify pass; both red as tracebacks with the guard staged away
- AC9 — `python tools/govkit/govkit.py selfcheck` — with drift-audit's and codebase-map's `defaults` staged away it named drift-audit `MEMORY_ROOT` and codebase-map `MAP_ROOT` and `GATE_FILE`; `[aHI-1 AC9]` in `check_halved_install_arms` stages the first

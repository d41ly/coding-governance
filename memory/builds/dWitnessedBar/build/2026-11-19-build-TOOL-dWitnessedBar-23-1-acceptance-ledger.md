# TOOL-dWitnessedBar-23 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-23

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by probing the unit's own code at the repository root: each criterion's own command, the
catalogue checker over a scratch copy of `tools/roles/` for AC2's red cases, and `scratch-guard.js`
fed two `gov-tester` payloads for AC5. Section 7 declares no `New arm:` line, so no RED-first
observation is owed; the close owes section 7's legs, among them `govkit selftest`, which alone
observes the derived roster counts and the re-pinned seed preview of S6 end to end.

**Evidences:** TOOL-dWitnessedBar-23
- AC1 — `none gate-bar` — the `load_roles` probe printed `none gate-bar`.
- AC2 — `gov-tester` — the `check_roles` probe printed `[]`. On a scratch copy of the kit with the
  `gate-bar` entry's `roles` emptied it returned `R7 — the 'gate-bar' entry's roles does not list
  gov-tester` (and R8); with the entry restored and the `BODY_CEILINGS` row removed it returned
  `R5 — slot 'gov-tester' has no ceiling row in BODY_CEILINGS`.
- AC3 — `house/gov-tester.md` — `grep -c` in `tools/roles/` printed 1; the `len(agents) == 9\|== 10`
  grep in `tools/govkit/` printed nothing (exit 1); the `KEEP|seed", 0) == 15` grep printed 1. A
  `python -c` probe of the derivation the selftest now runs read 10 agent-true roles and 11 seeded
  overlays from the kit, the latter equal to `house/*.md`. Owed: `govkit selftest` at the close, the
  only observer of the default plan's seed preview at 15.
- AC4 — `none []` — `render_agents.py --check` exited 0 after `--write` wrote
  `.claude/agents/gov-tester.md` and `.claude/roles.json`; the index probe printed `none []`.
- AC5 — `G2 runner` — the Bash payload running the merge bar exited 2 naming `row G2 runner`; the
  Write payload targeting this spec exited 2 naming `role gov-tester, whose writes is none`.
- AC6 — `role:gov-tester` — the `loop.toml` probe printed
  `role:gov-tester ['code-miss', 'spec-wrong'] ['code-miss', 'spec-wrong']`; `python loop_lib.py
  --check` exited 0, printing both `item.test.attribute` and `item.test.reason` resolved
  (`allowance none from role:gov-tester`) and no `role:gov-tester · pending` line.

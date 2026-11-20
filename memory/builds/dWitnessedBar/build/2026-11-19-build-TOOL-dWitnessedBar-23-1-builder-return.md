**Serves:** journal TOOL-dWitnessedBar-23

# TOOL-dWitnessedBar-23 — builder return 1 (run `wf_3bc39100-b9a`), committed 66ad2ab395754a0e29455285d5ad3c9cbb096a30

## Why

TOOL-dWitnessedBar-23 is built as its spec says and committed as one pass commit. The commit carries `Pass: TOOL-dWitnessedBar-23` and the charter's Co-Authored-By trailer. The spec's status moved INPROGRESS to CLOSED in that same commit. The spec's §4 claims held at HEAD, so there was no divergence: the 9/10 typed counts at `tools/govkit/selftest.py#check_roles_install` and the docstring, the seed preview pinned at 14, `gate-bar` with `roles = []`, the seed include list in kit.toml, the `item.test.attribute` row with its actor, outcomes and routes, and an empty `[gates]` row for the slot.

## Summary

Built TOOL-dWitnessedBar-23 in commit 66ad2ab39 (base 853fc00ea). It adds the `gov-tester` role to the roles kit and covers S1 to S7.

**What changed**
- New role file `tools/roles/agents/gov-tester.agent.md`, with the spec's front matter word for word. Its body is 1649 bytes against a 3072-byte ceiling. (DERIVED from the builder's probe)
- New empty overlay `tools/roles/house/gov-tester.md`, named in the seed list of `tools/roles/kit.toml`.
- `tools/roles/check_roles.py`: a `"gov-tester": 3072` row in BODY_CEILINGS.
- `tools/roles/workflows.toml`: the `gate-bar` entry now lists `roles = ["gov-tester"]`.
- Rendered files, regenerated rather than hand-edited: `.claude/agents/gov-tester.md` and `.claude/roles.json` (by `render_agents.py --write`), and the catalogue section of `tools/roles/README.md` (by `check_roles.py --write`).
- `tools/govkit/selftest.py`, in `check_roles_install`:
  - The 9 and 10 are no longer typed. The expected lists come from the gov tree's own roles kit: the agent-true roles via `roles_lib.load_roles`, and the `house/*.md` entries of the seed list. The check compares names, not only counts.
  - The docstring no longer types the counts.
  - The default plan's seed preview is re-pinned from 14 to 15, with one history-comment line (§8 F4).
- Records: the acceptance ledger `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-23-1-acceptance-ledger.md`, plus what `gen_build_index.py --write` rewrote (`memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, and the spec's generated records table).
- `RUN.md` had no change to commit: the brief and dispatch rows were already committed, and `--brief` printed "already recorded, unchanged".
- No version bump, kickoff-manifest re-stamp or codebase-map regeneration was needed. None of my paths is on the watch list, and no new symbol was added.

**Checks that ran (probes of this unit's code only; they stand in for the `roles catalogue`, `roles render wiring`, `govkit selftest` and `policy fixtures` legs until the close)**
- AC1: printed `none gate-bar`.
- AC2: printed `[]`. On a scratch copy of `tools/roles/` with the `gate-bar` roles emptied it returned an R7 defect naming gov-tester. With that restored and the BODY_CEILINGS row removed it returned an R5 defect.
- AC3: the kit.toml grep printed 1, the `len(agents) == 9\|== 10` grep printed nothing, and the `KEEP|seed", 0) == 15` grep printed 1. A `python -c` run of the new derivation read 10 agent roles and 11 seeded overlays, matching `house/*.md`.
- AC4: `render_agents.py --check` exited 0, and the index read `none []`.
- AC5: piping payloads into `scratch-guard.js`, the merge-bar Bash call exited 2 naming row `G2 runner`. A Write to this spec exited 2 naming `role gov-tester, whose writes is none`.
- AC6: the loop.toml probe printed `role:gov-tester ['code-miss', 'spec-wrong'] ['code-miss', 'spec-wrong']`. `loop_lib.py --check` exited 0 and showed both `item.test.attribute` and `item.test.reason` resolved, with no `role:gov-tester · pending` line.

**Owed at the close (not run here)**
- Every leg in §7. `govkit selftest` is the only thing that observes the derived roster checks and the seed preview at 15 end to end.
- §7 declares no `New arm:` line, so no RED-first observation is owed.

**Bug-class checklist** (`gotchas.py --for-diff HEAD~1..HEAD`, exit 0) was run and acted on. The new locals in that very long function collide with no existing name. The ledger's leading tokens are each spelled by their own criterion and sit on one line. The AC2 staged break removed `__pycache__` first, so it did not run stale bytecode.

**Left alone:** `tools/run-gates/*`, `memory/guides/SESSION-KICKOFF.md` and `help/reference/*` were already modified in the shared working tree by unit 42 (or were dirty at start). I did not stage or touch them.

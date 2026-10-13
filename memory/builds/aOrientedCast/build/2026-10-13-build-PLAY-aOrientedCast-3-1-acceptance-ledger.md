# PLAY-aOrientedCast-3 — acceptance ledger

**Serves:** journal PLAY-aOrientedCast-3

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: the render's write
mode `bash tools/playbook/adopt-playbook.sh --target .`, `python tools/roles/render_agents.py --check`,
`bash tools/check-template-size.sh --bump` for both rows, the `grep`, `awk` and `git show` reads §6
names, and probes P3 and P4 of §4 "Probes" as `python -c` calls. This unit adds no gate arm, so no
`New arm:` observation is owed; the close still owes every leg §7 lists, run once by the main loop.
Nothing under `.claude/` moved, so no agent re-render pass is owed. The `memory/DECISIONS.md` row is
the main loop's commit `72fc2c2e`, observed here and not written.

**Evidences:** PLAY-aOrientedCast-3
- AC1 — `kit:roles` — the grep printed the `kit:roles` opener on the line after the `SPEC` definition, inside the `microformats` pair, holding the `agent` and `returned` definitions once each, and a second `kit:roles` pair whose opener is the line after `[events]`, holding `[agents]` alone.
- AC2 — `adopt-playbook.sh --target .` — the render exited 0 and a re-render after it left `AGENTS.md` unchanged; `grep -c "kit:roles" AGENTS.md` printed 0 and the `[agents]`, `agent` and `returned` count printed 3.
- AC3 — `drop ok` — P3, with the roles kit dropped through `remove_fenced` and the marker folded back to v4.3, printed `drop ok` comparing this unit's template with its parent's.
- AC4 — `governance-template: v4.4` — the count printed 1 over the template and 1 over `AGENTS.md`; both carried `v4.3` at the parent.
- AC5 — `tools/template-size-highwater.txt` — `AGENTS.md` measured 16732 of 20480 bytes and the template 13695 of 49152, carriage returns stripped, and each row was re-recorded with `--bump` to that figure; §4's pinned 16729 differs by 3 bytes, derived at observation.
- AC6 — `render_agents.py --check` — exited 0, printing `9 agent type(s) and 1 index graded` and naming no `drift`, `missing` or `stale` path.
- AC7 — `last-audit` — re-stamped to `2026-10-13T05:15:19+03:00 @ f76d7b9cca386eeb6e0221f57424a443a12628f7`, the sha `git rev-parse HEAD~1` prints on the unit's commit; the `git rev-list --count --no-merges` count from `last-body-change` over the watch paths was 5 before this commit, so `last-body-change` stays.
- AC8 — `shapes ok` — P4 printed `shapes ok`: `read_charter_shapes` keyed both heads from the rendered fence, matched a well-formed line of each and refused the `agent` line with its run field cut.
- AC9 — `20480` — the `awk` printed `20480`; the grep printed the LOWERED line, then the RAISED line, then the row, in that order; the `DECISIONS.md, PLAY-aOrientedCast-3` count printed 1.
- AC10 — `^- PLAY-aOrientedCast-3 · ` — the count printed 1, the row sits between `## PLAY — playbook` and `## KICK — kickoff`, and its length printed 261.

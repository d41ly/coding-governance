# PLAY-aOrientedCast-2 — acceptance ledger

**Serves:** journal PLAY-aOrientedCast-2

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: the render's write
mode `bash tools/playbook/adopt-playbook.sh --target .`, `python tools/roles/render_agents.py --check`,
`bash tools/check-template-size.sh --bump` for both rows, the `grep` and `git show` reads §6 names,
and probes P1 and P2 of §4 "Probes" as `python -c` calls. This unit adds no gate arm, so no `New arm:`
observation is owed; the close still owes every leg §7 lists, run once by the main loop. Nothing under
`.claude/` moved, so no agent re-render pass is owed.

**Evidences:** PLAY-aOrientedCast-2
- AC1 — `kit:roles` — the grep printed six fence lines: the `[roles]` rule alone inside the first pair, whose opening line directly follows `[tools]`; the Tools bullet reading only "An attended code build runs through `/build`." inside the second; `## Agent roles — hand the work to its role` in the third above `{{ROLE_ROSTER}}`, alone between the one-line markers, and that pair's closing fence is the line before `## Protocols`.
- AC2 — `roster ok` — the render exited 0 and a second render left `git diff --quiet -- AGENTS.md` at 0; `grep -c "kit:roles" AGENTS.md` printed 0; the rendered `[roles]` rule appears once, naming `memory/project/role-stand-in-waiver.txt`; P1 printed `roster ok 10 lines, longest 152`.
- AC3 — `drop ok` — P2, with the roles kit dropped through `remove_fenced`, printed `drop ok` comparing the template at `HEAD` with `HEAD~1`.
- AC4 — `governance-template: v4.3` — the count printed 1 over the template and 1 over `AGENTS.md`; the marker did not move.
- AC5 — `tools/template-size-highwater.txt` — `AGENTS.md` measured 16301 of 16384 bytes and the template 13186 of 49152, carriage returns stripped, and each row was re-recorded with `--bump` to that figure.
- AC6 — `render_agents.py --check` — exited 0, printing `9 agent type(s) and 1 index graded` and naming no `drift`, `missing` or `stale` path.
- AC7 — `last-audit` — re-stamped to `2026-10-13T05:07:24+03:00 @ 0d5786af6156e3fc69365dba6169bd0ea147ac0e`, the sha `git rev-parse HEAD~1` prints on the unit's commit; the `git rev-list --count --no-merges` count from `last-body-change` over the watch paths was 4 before this commit, so `last-body-change` stays.
- AC8 — `role-stand-in-waiver` — `help/roles.md` gained the `[roles]` rule and the generated `## Agent roles` section in its opening, `mandatory` and `output` in step 2, the agent type's carried rules in step 4, the charter-then-`render_agents.py` order under `adopt-playbook`, a `## When no role agent can be spawned` section naming the registry and `--stand-in`, and the v4.4 seed note.

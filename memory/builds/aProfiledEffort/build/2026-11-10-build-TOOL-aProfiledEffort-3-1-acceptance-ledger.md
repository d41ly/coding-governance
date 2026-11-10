# Acceptance ledger — TOOL-aProfiledEffort-3

**Serves:** journal TOOL-aProfiledEffort-3

Built against spec rev-2 at the pass's parent `c6780aa29`. Each line below is a probe made in the pass, after both adopters ran, with the observation block of the spec's section 4 run from the worktree root. No suite, gate leg or bar ran in the pass, and the unit adds no arm. Owed to the main loop at the close: every leg of the spec's Gates section.

**Evidences:** TOOL-aProfiledEffort-3
- AC1 — `calls=4 bare=0 rule=1 role=1` — the observation's line for `tools/roles/SKILL.template.md` read exactly this.
- AC2 — `calls=4 bare=0 rule=1 role=1` — the observation's line for `.claude/skills/build/SKILL.md` read exactly this after `bash tools/roles/adopt-roles.sh --scaffold`, which printed `render_agents: unchanged — 9 agent type(s) and 1 index fresh`, and `git status --short .claude/agents .claude/roles.json` printed nothing.
- AC3 — `calls=1 bare=0 rule=1 role=1` — the observation's lines for `tools/unattended/VERBS.template.md` and for `memory/guides/UNATTENDED-VERBS.md` each read this after `bash tools/unattended/adopt-unattended.sh`, and the `diff` of the two, each through `tr -d '\r'`, printed nothing and exited 0.
- AC4 — `calls=4 bare=0 rule=1 role=2` — the observation's line for `tools/roles/README.md` read this, and its line for `tools/workflows/README.md` read `calls=1 bare=0 rule=0 role=0`, whose first two fields are the two the criterion reads.
- AC5 — `calls=1 bare=0 rule=1 role=1` — the observation's line for `help/roles.md` read this, and the criterion's `grep -nE` printed nothing. The page's diff moves no line holding a `usage:` anchor.
- AC6 — `grep -c "effort\.profiles"` — it printed `4` for `tools/roles/README.md` and `2` for `help/roles.md`; the `fable` count printed `1` for each; the policy file's count printed `1`.
- AC7 — `{"builder":"medium"}` — `python tools/roles/handoff.py stage-efforts build --model claude-fable-5-2` printed exactly this and exited 0, and `role-efforts --model claude-fable-5-2` printed one line carrying `"gov-builder":"medium"` and exited 0, both before any edit.

# TOOL-aOrientedCast-26 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-26

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran, from the worktree
root: the `tomllib` probe, `handoff.py stage-efforts` for both workflows, the `roles_lib` policy
load, `render_agents.py --write` and then its `--check`, and the greps each criterion names. The
main loop dispatched this unit as ONE pass, since the renderer's code does not move, so the render
S2 assigns to a second pass ran here and AC4 is observed in this pass. Owed to the main loop at the
close (M8): every leg §6 lists. The spec declares no `New arm:`, so no RED-first observation is
owed. The roles kit's version move is `TOOL-aOrientedCast-25`'s, after this unit.

**Evidences:** TOOL-aOrientedCast-26
- AC1 — `high xhigh` — the `tomllib` probe printed `high xhigh`, and `git diff --numstat` over `tools/roles/house/policy.toml` printed 2 added and 2 deleted, lines 10 and 12 alone.
- AC2 — `{"builder":"xhigh"}` — `stage-efforts spec-write` printed `{"builder":"xhigh","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}` and `stage-efforts build` printed `{"builder":"xhigh"}`.
- AC3 — `policy ok` — the `load_policy` probe printed `policy ok`; R12 raised nothing.
- AC4 — `python tools/roles/render_agents.py --check` — after `--write` reported 2 written, the grep printed `effort: high` for `gov-spec-writer.md` and `effort: xhigh` for `gov-builder.md`, and `--check` graded 9 agent types and 1 index and exited 0.
- AC5 — `KIT_ROLES_VERSION` — the `git grep` over `help/roles.md` and `tools/roles/README.md` printed nothing, and the count over this commit's `tools/roles/roles_lib.py` diff printed 0.

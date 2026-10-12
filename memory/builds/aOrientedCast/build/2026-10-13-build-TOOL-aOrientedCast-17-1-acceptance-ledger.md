# TOOL-aOrientedCast-17 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-17

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: fixture A, a
scratch directory holding a copy of `tools/roles/`, `tools/gate-legs.json`, `AGENTS.md` and a conf
declaring `MEMORY_ROOT=memory` and `CHARTER=AGENTS.md`, where a scratch probe imported the COPIED
checker and called `check_roles.check_roles` with one staged break at a time, each restored before
the next (the role gate refuses the checker's CLI, which is the `roles catalogue` leg's argv); the
`handoff.py roster` verb and AC4's two `python -c` probes in the worktree; fixture B, a `git init`
repository under a short `%TEMP%` root holding a copy of the kit and a conf declaring only
`MEMORY_ROOT=memory`, no charter, where the copy's `handoff.py roster` ran under each staged break;
the new suite arm's `sed`, `grep -c` and refusal lines run by hand against fixture B's kit, CRLF
role file included; and fixture B, with `AGENTS.md` and `CHARTER` added, where the copy's
`render_agents.py --write` rendered the agent types. Owed to the main loop: the re-render pass the
build brief names, `render_agents.py --write` into gov's `.claude/agents/` and its `--check`, which
AC7 reads in the worktree; then at the close (M8) both `New arm:` lines of §7, each RED on its
staged break and GREEN restored — the checker's R13 break (gov-orienter's `mandatory` staged to
`for every session` under the hookless `orient` entry) and R14 break (gov-spec-writer's `output`
staged without its folder), and adopt-roles.test.sh arm 8 against a `handoff.py` whose 200-character
refusal is staged out — and every leg §7 lists.

The re-render pass ran at the main loop, declared at `d799ef46`: `render_agents.py --write` wrote
the nine types with the new descriptions, `render_agents.py --check` exited 0, `check_roles.py`
exited 0 with six mandatory roles and three writer outputs, and no type under `.claude/agents`
carries a `mandatory` or `output` key. The `New arm:` observations remain owed at the close.

**Evidences:** TOOL-aOrientedCast-17
- AC1 — `check_roles.py --root <fixture A>` — over fixture A's unmodified copy the copied checker returned no defect and no `R13` or `R14` line, and its summary read `... 32 reads keys, 6 mandatory roles, 3 writer outputs, 55 rule tags ...; 0 defect(s)`.
- AC2 — `R13` — gov-orienter's `mandatory` set to `for every session` gave exit 1 and one R13 line naming `gov-orienter.agent.md` and `orient`; with `, unenforced — the card writer is no hook` appended, exit 0; gov-builder's `mandatory` line deleted gave exit 1 with an `R2` line naming `mandatory`; a `{{TOOL_ROOT}}` token in it gave exit 1 with an R13 line naming the token; the `build` entry's `enforced-by = ["routed commits name a specced unit"]` gave exit 1 with an R13 line naming `gov-builder.agent.md` (beside R11, since the README region renders that column).
- AC3 — `R14` — gov-spec-writer's `output` set to `specs, to the main loop` gave exit 1 with an R14 line naming `spec` and `{{MEMORY_ROOT}}/builds/<slug>/spec/`; gov-synthesizer's `a report` an R14 line naming `review`; gov-builder's `commits` an R14 line naming `ROUTED_PATHS`; gov-spec-writer's with a `{{TOOL_ROOT}}` token beside its folder an R14 line naming the token; gov-skeptic's `anything at all` exit 0; gov-skeptic's `output` line deleted exit 1 with an `R2` line naming `output`.
- AC4 — `memory/builds/<slug>/spec/` — in the worktree the verb exited 0 and the probe printed a count of 10, a longest line of 152, a first line naming gov-orienter, a last naming gov-session, and False, 10 being the `tools/roles/agents/*.agent.md` count; the gov-spec-writer line carries `memory/builds/<slug>/spec/` and the `gov-reuse-scout` line `Optional, when kickoff asks for one`; the byte probe printed 1383, under 1466.
- AC5 — `201` — in fixture B, no `CHARTER` and no charter file, the verb exited 0 with 10 lines and gov-builder's at n = 132; its description lengthened by 69 gave exit 1, empty stdout and stderr `handoff: roster line for gov-builder is 201 characters, past the 200 a one-line charter rule may take; ...`; lengthened by 68, exit 0 with that line at exactly 200 characters.
- AC6 — `MEMORY_ROOT` — fixture B with every role file moved out of `agents/` exited 1, empty stdout, stderr naming the `agents` directory as holding no role file; with the conf's `MEMORY_ROOT` line deleted, exit 2 naming `MEMORY_ROOT`; AC5's exit 0 ran with no `CHARTER` key and no charter file.
- AC7 — `python tools/roles/render_agents.py --write` — in fixture B with `AGENTS.md` and `CHARTER` added, the copy's render exited 0 and wrote nine types; `grep -c "^description: Builds one unit from its spec"` on its `gov-builder.md` printed 1 and `grep -lE "^(mandatory|output):"` over its types printed nothing. Gov's own `.claude/agents/` render and its `--check` are the re-render pass's, as the paragraph above states.

# PLAY-dOrderedCharter-5 deviation 54 — the agent types re-rendered by the main loop, not in the pass commit

**Serves:** deviation PLAY-dOrderedCharter-5

- **Departs from:** `PLAY-dOrderedCharter-5@rev-6` [Design]
- **Hand-off:** spec-to-code
- **Before:** the Rollout puts the agent types' re-render in the same commit as the code, so no native spawn gets a task part without charter blocks from an agent file that also lacks them.
- **After:** the pass commit carries the renderer and the handoff and leaves `.claude/agents/*.md` as rendered before it. The main loop runs `python tools/roles/render_agents.py --write` and commits the nine agent types before the bar and before any landing.
- **Cause:** builder discovery
- **Reason:** `--dispatch` refused the write set declaring `.claude/agents` beside `tools/roles/render_agents.py`, a generated index declared together with its generator. That refusal is binding on a role agent, so the re-render belongs to the main loop.
- **Evidence:** `python tools/roles/render_agents.py --check` over the pass prints `drift` for each of the nine agent types and the `--write` remedy. Rendered in memory, the builder's type opens its body with the charter's level-0 envelope inside its own level-5 one.
- **Risk:** low. Until the re-render lands, a native spawn's task part has no charter while its agent file still carries the old copy, so the charter is carried once, at its old place, and nothing is lost. The `roles render wiring` leg reds the stale types at the close.
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-5

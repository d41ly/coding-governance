# PLAY-dOrderedCharter-5 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-5

Each line is a probe this pass ran at rev-6 of the spec, with the pass applied. No leg, suite or `--selftest`
ran in the pass. The agent types under `.claude/agents/` are not re-rendered in this commit (deviation 54), so
the probes render the builder's type in memory through `tools/roles/render_agents.py#render_agent_file` over gov's own
catalogue, charter and document registry. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-5
- AC1 — rendered in memory, the `gov-builder` type's envelopes read, in order: open `.claude/agents/gov-builder.md` level 5, open `AGENTS.md` level 0, close `AGENTS.md`, close `.claude/agents/gov-builder.md`. The level-0 envelope holds `## Charter`, `### Charter rules` with the `- [verify] Verify before claiming done` line, `### Protocols` and `### Facts`, and the role's text follows its closer.
- AC2 — `python tools/roles/handoff.py render --role gov-builder --build dOrderedCharter --unit PLAY-dOrderedCharter-5 --input spec=<this spec> --input prompt=<a brief> --stdout` exited 0. Under `## Role` it printed one envelope, `.claude/agents/gov-builder.md` at level 5, closing after `### Drive`. Under `## Task` it printed `AGENTS.md#practices-at-build` at level 0 holding `### Practices at build`, then the prompt file's path at level 6 holding the opening, `### input:spec`, `### card:route` and `### brief:non-goals`, each opened and closed once. With `--part task` it printed the marker, `## Task` and the same two envelopes, levels 0 then 6.
- AC3 — over that `--part task` output, `grep -c "^### Charter rules"` printed 0. The count of lines opening `- [verify] Verify before claiming done` across it and the in-memory builder type printed 1. The task's `- [verify]` reach line under `### Practices at build` is the one other `[verify]` line.
- AC4 — `tools/roles/handoff.py#check_handoff` over a scratch copy of that render, at its own prompt path under a scratch root, passed and printed `envelopes — Role 5 · Task 0 6`. With the level-6 envelope moved above the level-0 one inside `## Task` and the marker's hashes re-stamped, it failed, naming `AGENTS.md#practices-at-build` opening at level 0 after the prompt's envelope at level 6. With the practices closer deleted and the hashes re-stamped, it failed, naming `AGENTS.md#practices-at-build` as having no closer.
- The unranked render — a hand-run copy of the `work-order` fixture, the roles kit alone in a fresh repository, printed both pinned cases byte for byte, and the opening-and-reads swap moved the bytes (deviation 53).
- The render check — `python tools/roles/render_agents.py --check` over gov printed `drift` for each of the nine agent types and the `--write` remedy, and nothing else red.

**Owed to the close.** The bar; the re-render and commit of the nine agent types (deviation 54); and the RED-first observation of the `New arm:` line, arm 20 of `tools/roles/render_agents.py`'s selftest, under the `roles render selftest` leg. Arm 20 asserts the unarmed note, the unreadable-registry refusal's text, the ranked agent file, the handoff's levels per part with no charter in its task, and the planted reordered and unclosed envelopes. The pinned bytes of the `work-order` plant are read under the `instruction units selftest` leg.

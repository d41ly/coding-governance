# PLAY-dOrderedCharter-39 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-39

Each line is a probe this pass ran at rev-5 of the spec, over `25ed886f8` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: each checker the criteria name is the close's, and where a line says
"owed" the main loop observes it after every unit is terminal. The probes ran a `git grep`, the renderer's own
check over gov's tree, the rows' own writers, or a scratch script reading blobs.

**Evidences:** PLAY-dOrderedCharter-39
- AC1 — `git grep -n -A9 "agent-instructions" -- tools/gate-legs.json` — printed one matching line, the `agent-instructions wiring` name, after `verdict-epoch self-test`, then the argv `python`, the renderer, `--check-render`, `--scope`, `entry-files`, `--aliases`, `claude`, with no `--card`, since the `instruction render (one renderer of record)` leg carries none; the grep over `tools/playbook/core-pending.txt` printed the wiring leg's `leg` row alone (PINNED, read at 25ed886f8 with the pass applied).
- AC2 — `git grep -c "agent-instructions wiring"` — printed a count of 1 for the registry, the subject pins and the playbook dossier, and no line for the playbook descriptor or the map baseline. The pin row came from `govkit.py selfcheck --write`, the map from `gen_map.py --write`, and `owed_rows.py --base HEAD` printed no row owed and one deferred, the ceiling-evidence row. `derive-ceilings.py --report` lists the leg among those whose every retained reading was set aside as contended, so no admissible reading exists and the row is the first bar's; `--write` was not run.
- AC3 — `git log -1 --format=%B` — the pass commit's `Decided:` trailers carry the option table and the moved names. A scratch probe read the adopter's argument `case` at the deleting commit's parent through the tree library's blob reader, named the deleting commit `5e98256fe` and the options `--source`, `--aliases`, `--mode`, `--check`, `--force` and `--card`, each mapped, and exited 0; with the `--card` row cut from its table it printed `--card -> UNACCOUNTED`.
- AC4 — `python tools/playbook/render_playbook.py --check-render --scope entry-files --aliases claude` — over gov's tree it exited 0 printing `agent-instructions OK — AGENTS.md + aliases [claude] correctly wired.`; with `--card` it exited 1 naming `CLAUDE.md` as lacking the card import, the dark switch the leg does not carry. The pass stages no byte of `CLAUDE.md`.
- AC5 — `git grep -n "agent-instructions wiring" -- help/upgrade-steps.md` — printed one line, in the section on what this release's steps do to a repository, the sentence saying the leg stays on gov's own bar and an adopter's next `update` stops carrying it.

**Owed to the close.** Every leg of the spec's Gates section, `govkit selfcheck` and `core meta-check` among them,
`codebase-map coverage + freshness`, and the ceiling-evidence row the first bar running the leg writes. The spec
declares no `New arm:` line, so no RED-first observation is owed.

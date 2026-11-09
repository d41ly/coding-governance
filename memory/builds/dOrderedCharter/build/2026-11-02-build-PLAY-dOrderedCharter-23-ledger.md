# PLAY-dOrderedCharter-23 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-23

Each line is a probe this pass ran at rev-5 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: the charter was re-rendered by the playbook adopter over this worktree, the drive rows were read through the
instruction-units drive verbs, and the new selftest arm's logic was probed by a direct call of the renderer's
drive reader rather than by its selftest. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-23
- AC1 — `drive --check` — exited 0, printing 19 rows, 19 charter lines and 0 red; `drive --list` printed one unattended row, the `start · main` row ending in `/unattended <slug>`, and one roles row whose command is `/build`, stage `start` and role `main`.
- AC2 — `adopt-playbook.sh --target .` — rewrote the playbook region; `git grep` found "runs unattended by default" and "only when the owner asks to attend" on consecutive lines inside the drive section's one-line region, after the kickoff kit's three `start` lines and before the roles kit's `gov-session` start line.
- AC3 — `git grep "^- \[land\]" -- AGENTS.md` — the one line names "the request's mandate" and "the build README a run authorizes", measuring 175 bytes rendered and 189 with the placeholder unresolved, both under `render_playbook.py#ONE_LINE_MAX`; `instruction_units.py#read_practice_catalogue` read `practice.land` with its reach equal to the base's, its place in the catalogue unchanged and its foundation membership kept.
- AC4 — the spec's grep outside the build, ledger and archive records — printed no line holding "explicit ask or the unattended protocol"; every `[land]` line it printed is the rendered practice line or a reader the spec's table names, each still true, so none was edited.
- New arm — `render_playbook.py#run_selftest` gains the default-route drive arm. A direct probe of its condition over the shipped descriptors printed True, and with the unattended kit's rows filtered out printed False; the arm's RED-first observation on the staged break is owed to the close.

**Measured.** `AGENTS.md` grows by 134 bytes CR-stripped, as the spec's Rollout paragraph says, to 23304; the
`/build` drive line measures 72 bytes, one under the 73 the spec's design paragraph pins, and the unattended
line 141, as pinned.

**Owed to the close.** The bar, and the RED-first observation of the `New arm:` line: the renderer's selftest
arm, staged by dropping the unattended kit's drive row. The legs the spec's Gates section names, among them the
charter size leg, which warns on `AGENTS.md` past its row.

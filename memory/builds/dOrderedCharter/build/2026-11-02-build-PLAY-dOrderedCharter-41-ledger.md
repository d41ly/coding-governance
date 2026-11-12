# PLAY-dOrderedCharter-41 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-41

Each line is a probe this pass ran at rev-6 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass. The new selftest arm's own source was cut out of
`tools/playbook/render_playbook.py#run_selftest` by a scratch script and executed with a stub `check_arm`, once
against the shipped declarations and once with the `cross-os` row marked `legacy` in memory; that probe stands in for
the `playbook render selftest` leg until the close runs it and observes the arm red on the staged file edit. This
record cites no code line.

**Evidences:** PLAY-dOrderedCharter-41
- AC1 — the spec's `tomllib` one-liner over `tools/govkit/entries/playbook.kit.toml` printed one row, `{'name': 'cross-os', 'why': 'the cross-OS and toolchain section. Drop it for a single-OS team.'}`, with no `legacy` key.
- AC2 — `python tools/playbook/render_playbook.py --target . --check` exited 0 and printed `render-playbook OK — region matches a fresh render, no placeholder survived`.
- AC3 — a scratch repository committed on `main`, holding gov's template and gov's `deploy.toml` narrowed as the spec's evidence says, with `drop_blocks = ["cross-os"]`: the write and `--check` each exited 0 and each printed the `retired   drop_blocks cross-os` note; the rendered charter held no `Toolchain` and no `[cross-os]`. Without the member both were present and neither run printed the note.
- AC4 — `git grep -n -e "minor behind" -- tools/playbook/render_playbook.py help/` printed one line in each: the comment above `TEMPLATE_MAJOR` and the new paragraph of `help/charter.md`, both stating the major-only rule.
- AC5 — four scratch repositories, each committed on `main` with gov's narrowed `deploy.toml`: gov's template and the v4.4 template as `778a60196^` holds it, each with and without `drop_blocks = ["cross-os"]`; `python tools/playbook/render_playbook.py --target <scratch>` exited 0 on all four. The arm's own source, executed as above, passed its four renders and failed all four with the row marked `legacy`, each refusal naming `when:cross-os`. The arm's red and green on the staged file edit are owed to the main loop.
- AC6 — `git grep -n -F 'charter.practices' -- WIRE-INTO-PROJECT.md` printed the rewritten paragraph's line; `git grep -n -F 'binds every adopter' -- WIRE-INTO-PROJECT.md` printed nothing; `git grep -n -F 'asks for no removal' -- WIRE-INTO-PROJECT.md` printed the `when:cross-os` bullet.

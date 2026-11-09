# PLAY-dOrderedCharter-37 deviation 375 — the tutorial's install selects five kits and writes the charter table

**Serves:** deviation PLAY-dOrderedCharter-37

- **Departs from:** `PLAY-dOrderedCharter-37@rev-7` [Scope]
- **Hand-off:** spec-to-code
- **Before:** the tutorial installs gov into an empty repository, adds a repository rule, renders and reads the delta report; the first dispatch's probe expected `apply --kits playbook,playbook-render` to configure with eight `--answer` values.
- **After:** the tutorial runs `intake` over the kits playbook, playbook-render, memory-tree, policy and agent-instructions with the one answer intake asks for, appends a `[charter]` table of the render's asked values to `.governance/deploy.toml` with one `printf`, runs `apply`, and commits; it writes the overlay row at the terminal with a second `printf`, commits it, renders with `render_playbook.py --render-scope charter` and finds the rule's line in `AGENTS.md` with `grep`. The task page opens with the same install.
- **Cause:** builder discovery
- **Reason:** in a scratch repository `apply` takes no `--answer`, and `intake` records only the answers a descriptor's destinations and probes need, so the charter render's asked values reach it only through `[charter]`; the playbook-render adopter refuses without the memory-tree kit, then without the policy kit, then without the agent-instructions kit, each resolved at render; and `instructions_edit.py add` refuses every write until its guard lands, so the overlay is written at the terminal, as the overlay page says.
- **Evidence:** the run arm over the tutorial in a scratch clone of the pass ran ten commands and found nothing; with the four kits but agent-instructions, `apply` exited 1 naming the adopter's refusal (PINNED, counted at cee53246).
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-37

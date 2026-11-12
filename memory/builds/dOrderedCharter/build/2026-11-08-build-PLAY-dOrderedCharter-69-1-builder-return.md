# dOrderedCharter — unit 69's builder return

**Serves:** journal PLAY-dOrderedCharter-69

Run wf_7af45ef6-2e9, summarized from its return.

- Built at rev-1 as pass commit `db95071f6`.
- What the unit landed:
  - `instruction_units.py#run_fixture`, `gov_tag.py#run_fixture` and the resolve branch of `edge_grammar.py#run_fixture` each run inside `set_env_aside(GIT_ENV_LEAKS)`.
  - A `git-env` plant in `instruction_units.py`, and one in `gov_tag.py#run_plant`, each building a disposable main repository with a linked worktree and a sentinel `index.db`.
  - One tag-plant row in `adopt-playbook.sh`.
- A hand probe of the old code, in a disposable repository, showed both leaks: `core.bare` flipped to true, and the sentinel `index.db` replaced.
- Observed by probe: AC1 to AC4, and the lexicon.
- No divergence, and no deviation record.
- Owed at the close:
  - RED then GREEN for both `New arm:` lines.
  - The section-7 legs, and the tags leg, refused to the builder.
  - The full hygiene join of the ledger, held under `--staged`.

**Serves:** research PLAY-dOrderedCharter-49

# Brief: spec 49 rev-9 — AC26's render command names the spec it needs

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The main loop's sweep of spec 49 rev-8 ran AC26's command over HEAD before dispatch.

## The brief

### Goal

Revise spec 49's AC26 so its command runs over HEAD and observes the code input.

### Items

1. **Where you write.** Edit only the scratch copy at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold49/2026-10-24-spec-PLAY-dOrderedCharter-49.md`;
   write nothing under the repository.
2. **The defect, observed at `8a9c55b65`:** AC26's command, run with `--input prompt=` and no `--input spec=`, prints
   `handoff: input:spec — not supplied; pass --input spec=<value>` and renders nothing, so the criterion can never observe
   `input:code`. With `--input spec=` naming spec 49's tracked path and `--input prompt=` naming
   `memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md`, the render carries
   `### input:code`, and without `--input code=` it prints the `Not supplied, optional` line naming it. Confirm both.
3. Restate AC26 so its command names every input the render requires, each backticked span on one line and every path tracked.
4. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words include an untracked
   path, no `path#symbol` in an acceptance bullet, no suite as the observation.

Bump the **Status:** rev to rev-9, dated 2026-11-10, status kept `DEFERRED`, with a revision-log line naming this brief and AC26.

### Acceptance

- AC26's command, as written, renders over HEAD and its output carries `input:code`.

### Gates

None run on the repository: this is a scratch edit. The main loop sweeps the spec and runs the spec-token check with it live.

### Non-goals

- No code. No edit outside the scratch copy. No other criterion changes.

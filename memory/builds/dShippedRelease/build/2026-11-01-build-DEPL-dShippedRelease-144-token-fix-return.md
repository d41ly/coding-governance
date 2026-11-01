**Serves:** research DEPL-dShippedRelease-144 DEPL-dShippedRelease-140

# Spec-token repair return — dShippedRelease

The repair writer's final return, extracted from its transcript by script, never retyped, and quoted whole.

Run direct/ae9c4b679027abf8f, from the handoff `2026-11-01-prompt-DEPL-dShippedRelease-1-3-spec-writer.md`.

> Both specs are reworded and staged, and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` exited 0 after the last edit.
>
> The gate printed no hit naming either spec. It also ran checks 14, 15 and 16 alongside the ones requested. Its check 15 advisory counts 6 dead repo-path citations in live build READMEs, and its check 25 notes are about specs in other builds. Neither comes from this edit.
>
> **`DEPL-dShippedRelease-140`**
> - **AC3:** the `git grep` pathspec is now the basename `ci_emit.py`. The criterion says the command runs at the close in the `tools/integrations/ci` folder. The patterns and the "prints nothing" observation are unchanged.
>
> **`DEPL-dShippedRelease-144`**
> - **AC9:** the inputs C:/x/, C:/X, C:/x/memory/a.md, C:/x2/memory/a.md, C:/x and /c/x/memory/a.md are now plain text, as in unit 133's AC3. C:/x/, C:/X and C:/x were not path-shaped, but I un-backticked them so the literals read alike. `base_dir`, `.`, `nt` and `os.name` stay backticked, and every observation is kept.
> - **AC16:** the `git grep -c` pathspec is now the basename `release.py`, run in the `tools/integrations` folder. It still prints count 1.
> - **AC28:** the one command is now two. `git grep` on the tracked `tools/unattended/VERBS.template.md` runs at the root, and `git grep` on `deploy.md` runs in the `help` folder. Each file still prints a line.
>
> **Token check:** I did not run `check-spec-tokens.py`. I listed the slash-bearing backticked words in both specs' criteria against `git ls-files` by hand. The only untracked ones left are `tools/integrations/ci`, `tools/integrations` and `reviews/`. Under `check_path_shaped` (`tools/check-spec-tokens.py:1104`) none of these is path-shaped, because the first two have no dot in the last segment and the third has a trailing slash.
>
> The bare basenames `ci_emit.py`, `release.py` and `deploy.md` are not graded here either. The bare-name join runs only at a root install (`tools/check-spec-tokens.py:1500`), and this repo's tool root is `tools`.
>
> No new requirement entered either spec, and nothing else changed. There was no commit, index regeneration or rev bump.
>
> Files are in `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dShippedRelease\spec\`:
> - `2026-11-01-spec-DEPL-dShippedRelease-140.md`
> - `2026-11-01-spec-DEPL-dShippedRelease-144.md`

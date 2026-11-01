**Serves:** research DEPL-dShippedRelease-133 DEPL-dShippedRelease-128 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-138 DEPL-dShippedRelease-106

# Spec-token repair return — dShippedRelease

The repair writer's final return, extracted from its transcript by script, never retyped, and quoted whole.

Run direct/acdb8b245d69e256b, from the handoff `2026-11-01-prompt-DEPL-dShippedRelease-1-2-spec-writer.md`.

> All six specs are checked and edits to units 133 and 128 are staged; nothing was committed and no rev was bumped. `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` exited 0, and none of its output named this build. I did not run `tools/check-spec-tokens.py`, so the goal itself is still yours to confirm.
>
> | Spec | Result | What changed or was confirmed |
> |---|---|---|
> | DEPL-dShippedRelease-133 | **Changed** | See below. |
> | DEPL-dShippedRelease-126 | Confirmed | AC3 takes the same case with only the runner path shortened. Its "runs `mint` over a fixture" makes no claim about the working directory. |
> | DEPL-dShippedRelease-127 | Confirmed | AC1's "on a clone" names the case's subject. The clone's own kit folder holds the script, so the basename does not contradict it. |
> | DEPL-dShippedRelease-128 | **Changed** | The basename edit broke AC1's meaning, so I corrected it. See below. |
> | DEPL-dShippedRelease-138 | Confirmed | AC16 and AC34 keep their meaning. See below. |
> | DEPL-dShippedRelease-106 | Confirmed | The quoted sentence is byte-identical to the former span and to unit 138 S50. See below. |
>
> The prior text for the confirmations came from the main loop's `fix4.py` in the session log, because these specs are new in the index and `git diff --cached` shows the whole file.
>
> - **Unit 133:**
>   - AC1 now gives both fixture paths in plain text. It keeps the `review<TAB>disposed · <n> finding(s) · ...` line ending in the repo-relative path, and `--deploy close` passing `path`.
>   - AC3 gives all three input spellings, `base_dir` and the output in plain text, including `C:\x\memory\a.md` and `C:/x`, which the brief did not list. All observables and both Red-when lines are unchanged.
>   - A scan of §6 shows no backticked word containing `/` remains.
> - **Unit 128:** AC1 said the command "runs at gov's root", but `python ci_emit.py` by basename does not exist there, so the criterion read as unrunnable. It now reads "`python ci_emit.py --fixture --case mint-regenerate-kits`, the kit's own script, runs at gov's root". That is the disposal's meaning, and it adds no requirement.
> - **Unit 138:**
>   - AC16 now cites the tracked `-79-` report, the same record unit 117 AC3 names. Its provenance line says "Run round 3", so it is the round-3 report.
>   - AC34 is the same observation with the location moved into prose; `help/deploy.md` is not tracked at this base and S51 still names it in full.
> - **Unit 106:** the three backticked tokens the handoff join reads all appear in unit 138: `--deploy land <slug>`, `--land` and `tools/unattended/check-unattended.sh`.
>
> **Basename check:** `ci_emit.py`, `deploy_fixture.py` and `deploy.md` have no tracked file by that basename. They stay ungraded only because the bare-name check does not run at gov, whose tool root is `tools`. That is the same condition unit 120's criteria rely on.
>
> **Unstaged backlog change:** `memory/builds/dShippedRelease/BACKLOG.md` shows 3 unstaged insertions with an mtime of 18:45:15. That is before my first edit at 18:47 and my hygiene run, and I did not touch it, so it is yours to account for at commit.
>
> The staged specs are in `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dShippedRelease\spec\`:
> - `2026-11-01-spec-DEPL-dShippedRelease-133.md`
> - `2026-11-01-spec-DEPL-dShippedRelease-128.md`

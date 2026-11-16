**Serves:** journal TOOL-dDeclaredLoop-68

# Builder return — TOOL-dDeclaredLoop-68, dispatch 1: no root of S1 spells the worktree as Git Bash's pwd prints it under the /tmp mount

## Why

DIVERGENCE: §2 S1 (and §4 "The route", which repeats its list of roots) cannot satisfy §6 AC1, for the `normalise` plant that §2 S4 specifies, on this Windows node. S1 hands write_normaliser three roots: the worktree's absolute path, its os.path.realpath, and the repo's absolute path, each as Path.as_posix(). For each root, render_path_spellings (lib-attribute.sh) produces only the `C:/...`, `C:\...` and `/c/...` spellings. Git Bash mounts /tmp on the user's temp folder, so when a command runs in a worktree that tempfile.mkdtemp put under %TEMP%, bash's `pwd` prints `/tmp/lw-<random>/tree`. None of the three roots matches that path. The `tmp\.` rule doesn't remove it either, because the directory name is `lw-<random>`, not `tmp.<x>`. The two re-runs therefore print different random names, their hashes differ, and AC1 reds.

Probe: I ran run_witness_commands at HEAD over a scratch fixture repo, with sha256 wrapped so I could capture the raw bytes. The command was `pwd; python -c "import os;print(os.getcwd())"; git rev-parse --show-toplevel`. Its output was `/tmp/lw-guw6frs7/tree`, then `C:\Users\DAILY-~1\AppData\Local\Temp\lw-guw6frs7\tree` (CRLF), then `C:/Users/daily-agent/AppData/Local/Temp/lw-guw6frs7/tree`. Only the second and third lines contain a root spelling.

§5's risks bullet accepts that "a path printed in a spelling none of the three roots produces ... reads as a difference". But S4 makes bash's `pwd` one of the outputs AC1 must hash equal, so the two statements cannot both hold. The spec has to choose one fix:
(a) A fourth root: the tree's path as the normaliser's own bash prints it (`cd <tree> && pwd`), passed to write_normaliser inside that bash. This changes S1's root list and §4 The route.
(b) Put the worktree outside the /tmp mount, e.g. under the git common dir as the run-gates runners do, so that `pwd` prints `/c/...`. This changes the 'as today' worktree placement in §4 The route.
(c) Drop bash's `pwd` from S4's command. This weakens AC1.

Second check, a stale figure rather than a design claim, named here so it is fixed in the same revision: in the §5 sweep, `git grep -l "from loop_witness import" -- tools/` lists 16 files at HEAD, not 13 PINNED.

The other sweep rows still hold at HEAD: the run_witness_commands( count is 8; there are 0 encoding-posture rows and 0 size-limit rows; the budget row reads 75; 'hashed exactly as' still appears in help/loop.md; 'combined output' appears in the HYGIENE template and in memory/HYGIENE.md at line 748; the watch list names none of the touched paths; normalise_output is absent. §8 F1 to F3 each carry RESOLVED.

I wrote nothing: no product edit, no --dispatch, no ledger. The brief was already recorded in RUN.md for 2026-11-17-prompt-TOOL-dDeclaredLoop-68-build-brief.md (the 2026-11-16 path the task names does not exist), so I did not re-run --brief. There is no patch to save.

## Summary

TOOL-dDeclaredLoop-68 is not built. I'm returning a divergence before any write.

Checks that ran:
- I read BUILD-METHOD.md, the brief (memory/builds/dDeclaredLoop/prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-68-build-brief.md) and spec rev-3 whole.
- I re-ran the §5 sweep at HEAD a339daae2. One figure is stale: the `from loop_witness import` count is 16 files, not 13.
- A probe stood in for the normalise plant (AC1), which no gate covered here. I called run_witness_commands over a scratch fixture repo under %TEMP%/lw68fx, which was removed afterwards. It showed Git Bash's `pwd` printing `/tmp/lw-<random>/tree`. None of the three S1 roots spells that path, so the normalise plant's two re-runs cannot hash equal.

No gate, suite or bar ran.

Nothing is owed at the close yet. The new arm for AC1, AC3 and AC4 (from tools/loop/loop_witness.py) is still unbuilt.

The working tree is clean of my edits. The untracked prompt files for units 87, 88 and 89 belong to other passes.

Relevant files:
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-68.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/loop/loop_witness.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/run-gates/lib-attribute.sh

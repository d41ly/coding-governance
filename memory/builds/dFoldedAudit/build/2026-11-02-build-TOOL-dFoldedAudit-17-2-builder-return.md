# dFoldedAudit — unit 17's builder return, first dispatch

**Serves:** journal TOOL-dFoldedAudit-17

Run direct/ab3837a4c83d24257, verbatim from its task notification.

DIVERGENCE: the spec's clone (S1) has no merge-driver config, so the merge conflicts on 11 paths instead of 8. AC1 is red, and I stopped before resolving anything. There is no commit, no M or F, and no fast-forward.

**What happened.** AC1's command, `git diff --name-only --diff-filter=U`, run right after `git merge --no-ff --no-commit origin/main` in the clone, printed the eight paths plus three more:
- `memory/LIVE.md`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
- `memory/ledger/2026-11.md`

**What in the spec is wrong.** `.gitattributes` sends those three paths to the `ours` merge driver (lines 90, 91 and 100). That driver, and the `rows` driver, are defined only in the run repository's `.git/config`:
```
merge.rows.driver bash tools/memory-tree/merge-rows.sh %O %A %B %P
merge.ours.driver true
```
A fresh clone doesn't copy those settings, just as it doesn't copy `core.hooksPath`. S1 sets the hooks path but not the drivers. The spec's trial merge was run in the run repository, where the drivers exist, so it saw eight.

**The fix, tested.** I ran `git merge-tree --write-tree --name-only HEAD origin/main` in the clone twice. It doesn't change any branch or file. Without the drivers it printed the 11 paths; with the two drivers passed as `-c` settings it printed exactly the spec's eight. So S1 needs both settings after `git config core.hooksPath .githooks`, either copied from `git -C "$REPO" config --get-regexp '^merge\.'` or written as literals.

**Two more things to fix before re-dispatching:**
1. **The interpreter path in §4 S1 doesn't exist.** `GOV_PYTHON=C:/Users/d41ly/AppData/Roaming/uv/python/cpython-3.15.0b1-windows-x86_64-none/python.exe` has no file; the uv directory holds only 3.11 and 3.12. The path came from item 9 of the spec brief. Python 3.15.2 is at `C:/Users/d41ly/AppData/Local/Programs/Python/Python315/python.exe` (the `py` launcher's 3.15 default), and `python3` on PATH is also 3.15.2. Main's resolver tries `GOV_PYTHON` and then `python3`, and its floor is 3.15, so either satisfies S9.
2. **The build brief and the spec disagree on closing the spec.** The brief says "The spec flips to CLOSED in the follow-up commit F." Spec §3 says the status flip belongs to the main loop, after the fast-forward. One of them needs to change.

**Not a problem: main moved.** GitHub `main` is now `84acebdc` (dEasedEffort landed), not the pinned `8a5328a9`. The spec covers a moved tip, and none of the eight conflicted paths changed between the two:
- The figures stay the same: floor 203 rising to 215, pin 37 rising to 39, and `last-body-change` `201eb127`.
- Main's 26 new files include no kickoff-watched file.
- The one template/render pair among them, `tools/roles/SKILL.template.md` and `.claude/skills/build/SKILL.md`, gets the same `roles@1.11` marker on both halves, so it stays a pair.

**Criteria**
- AC1: red, 11 paths instead of 8. This is the spec's own stop condition, not a gate.
- AC2 to AC13: not run, because the unit stopped before any resolution. All of them are still owed.

**Return fields**
- **Clone path:** `C:\Users\d41ly\AppData\Local\Temp\dFoldedAudit-17-merge`. I aborted the merge and deleted the clone so the revised S1 `git clone` into that path runs as written. It held no commit.
- **M and F:** none.
- **Fetched `origin/main` tip:** `84acebdce50ade26723faef2805c4d61cf7e591f`.
- **Run worktree:** unchanged and clean at `2621447d`. Its `refs/remotes/origin/main` was already `84acebdc` before I started.
- **M6 bug-class checklist:** not run, because nothing was committed.

Spec to revise: `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-02-spec-TOOL-dFoldedAudit-17.md`

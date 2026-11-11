# PLAY-dOrderedCharter-55 deviation 557 — the second spelling of a worktree's path is staged by the plant's own git reader

**Serves:** deviation PLAY-dOrderedCharter-55

- **Departs from:** `PLAY-dOrderedCharter-55@rev-7` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S21's plant `worktree-spelling` reads a fixture worktree under a second spelling of its path, its rows keyed by what `git rev-parse --show-toplevel` prints for that spelling.
- **After:** the plant stands its own reader in for `tag_index.read_git` while it reads the worktree, answering `--show-toplevel` with the second spelling, the drive letter's case swapped and the slashes turned back, and every other call as git answers it.
- **Cause:** builder discovery
- **Reason:** the git on this host prints one canonical spelling, upper-case drive and forward slashes, for a worktree reached or added under any spelling, so a plant asking git for the second spelling would key both readers alike and could not red; the stand-in is the git that prints the caller's spelling, which is the case S21 fixes.
- **Evidence:** a scratch repository with a worktree added and read under a lower-case drive letter printed the upper-case spelling from both `git rev-parse --show-toplevel` and `git worktree list --porcelain`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-19

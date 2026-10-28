**Serves:** journal TOOL-dSafePassage-59

# TOOL-dSafePassage-59 — acceptance ledger

The unit as built, at spec rev-3. Product writes: `tools/govkit/upgrade_steps.py` (S5's one-`lstat`
`test_path_linked`; S7's listing kept as `DirEntry`s, every entry link-tested before the
`is_dir(follow_symlinks=False)` filter; S8's `submodule_paths` typing `.gitmodules` by one `lstat`,
a link or reparse point refused before the regular-file test and any read; the
`submodule-modules-root-link`, `submodule-modules-link-dangling` and `gitmodules-symlink` plants),
`tools/govkit/selftest.py` (the dSP-59 arm; the dSP-49 AC13 and dSP-51 AC9 needles moved to the
`lstat` form, AC9 read with `os.lstat` alone per S8; the dSP-51 AC6 literal split so AC7's grep reads
none) and `help/upgrade-steps.md` (the linked `.gitmodules` refusal, and `modules/` itself linked or a
dangling link under it). S1's record is `2026-10-28-build-TOOL-dSafePassage-59-order-check.md`,
committed with `Pass: none` after this pass, which carries AC1's line. S2, S9 and S10 are readings no
code carries; S4 is struck.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
d (Windows, Python 3.15.2) over this worktree by the probe the spec names, run directly; the dSP-59
arm's staged copies were each run once through `build_staged_copy` by a scratch probe.

Owed at the close: the `New arm:` line's RED-first observation of the dSP-59 checks in
`tools/govkit/selftest.py` (AC3 AC4 AC5 AC6), and the §7 legs `govkit selftest`, `govkit refusal
join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture`,
`lexicon naming predicates`, `policy fixtures` and `spec tokens` at the bar.

**Evidences:** TOOL-dSafePassage-59
- AC2 — amended rev-3 — struck by §8 F1 with its number kept, the 3.11 floor it graded gone; logged in §9's rev-3 line.
- AC3 — `test_path_linked` — a `python -c`-style probe importing the module by path printed `True` on a `mklink /J` junction, `False` on a plain scratch directory and `False` on an absent path, and `True` on the junction once its target was removed; a copy testing `S_ISLNK` alone read the junction `False`.
- AC4 — `--plant submodule-modules-root-link` — exited 1 in 6 s, no `Traceback`, refused naming `.../t/.git/modules is a link the walk would enter`; a walk copy with the root test replaced by `if False:` exited 1 with `isolation: FAILED`.
- AC5 — `--plant submodule-modules-link-dangling` — exited 1 refused naming `.../t/.git/modules/dangling is a link under modules/`; a walk copy filtering by `os.path.isdir` before the link test exited 1 with `isolation: FAILED`.
- AC6 — `--plant gitmodules-symlink` — printed `isolation: skip — gitmodules-symlink needs os.symlink, which this host refuses ([WinError 1314] ...)` and exited 0; the refusal half needs a host that makes a symlink. The `ast` probe read `submodule_paths`'s `os.lstat` at line 1465, `stat.S_ISLNK(st.st_mode)` at 1471 and its `config -f` spawn at 1478, no `open`; over a copy taking `os.stat` it found no `lstat` and read False.
- AC7 — `git grep -n UNLISTED_EXECUTOR_KEYS -- tools help` — printed nothing once the dSP-51 AC6 literal was split.
- AC8 — `~~~` — §4's probe over a scratch page holding `a`, a `~~~` fence with `# x` inside, `b` and `## End` printed `a`, the fence, `# x` and `b`, and nothing after `## End`.
- AC9 — `grep -n 'TOOL-dTrueNorth-16 S2, THE EDGE REFUSAL' tools/unattended/unattended.sh` — printed one line, `13857`.
- AC10 — `grep -n -x -m1 'TOOL-dSafePassage-4'` — over `TOOL-dSafePassage-43` and `TOOL-dSafePassage-7` it printed nothing and exited 1.
- AC11 — `help/upgrade-steps.md` — §4's probe over it printed 122 lines; each of the seven criteria's patterns found its terms there: `core.hooksPath` 2, `GIT_CONFIG_COUNT` 2, `needs-target` 4; `filter.<x>.clean`, `extraheader`, `merge.<driver>.driver` 1 each; `git help --config` 3, `gpg.program` 1; `worktree` 4, `submodule` 13; `gc.recentObjectsHook` and `ext::` 1 each; `userinfo` 3, `proxySSLKey` and `never prints` 1 each.
- AC12 — amended rev-3 — struck with S4, its number kept; logged in §9's rev-3 line.

# Per-check timing of the memory hygiene gate — node `a`, 2026-08-27

**Serves:** research TOOL-aThawedCorpus-1

The owner's prompt asserts that the memory tooling walks the whole corpus on every call and that this
is where the time goes. The first half is true. The second is what this record measures, because the
remedy differs completely depending on the answer, and no figure in this tree attributed the leg's
cost to anything smaller than the leg.

## Method

`tools/memory-tree/check-memory-hygiene.sh` was copied to `tools/memory-tree/_hyg_timed.sh` with a
`date +%s%N` emission inserted immediately before every top-level `# <n> — ` check comment, and run
once over the full corpus with no arguments. Nothing else was changed; the copy was deleted
afterwards. A tick therefore measures the span from the START of one check to the START of the next
in SOURCE order, which is not numeric order — the file runs 22 before 21, and 21 before 10.

The corpus at the time: 71 build folders, 823 tracked files under `memory/`, 1.95 MB. 310 records
under `memory/builds/*/{build,prompts,reviews}/`.

## What it measured

| check | span | note |
|---|---|---|
| 1 | 1.6 s | |
| 2 | 2.8 s | |
| 3 | 9.5 s | |
| 4 | 2.8 s | |
| 5 | 5.8 s | |
| 6 | 3.6 s | |
| 7 | 1.9 s | |
| 8 | 4.3 s | carries check 9's `gen_build_index.py --check`, which sits above the tick |
| 9 | 3.5 s | |
| 22 | 1.8 s | |
| **21** | **365.6 s** | |
| 10 | 0.5 s | |
| 11 | 0.3 s | |
| 12 | 31.9 s | |
| 13-20, 23 | > 600 s, unfinished | one tick covers the whole delegating block and check 23 |

Everything except check 21 and the final block totals **70.3 s**. Check 21 alone is **five times**
that, and the run was stopped inside the final block after 684 s of tick span rather than allowed to
finish, because the attribution needed was already unambiguous.

## Why check 21 costs what it does

Its filename-projection loop, `proj21`, runs once per record and spawns per iteration: a command
substitution plus a `grep -oE` for `claimed`, and a pipeline subshell plus `tr` and `grep -qxF` for
the membership test. Four to six processes, 310 times, so 1,240 to 1,860 process creations for work
that is pure string manipulation.

The node's own recorded process-creation tax is what turns that into minutes.
`TOOL-aMeteredTurnstile-6` measured `bash -c true` between 22.5 ms and 581 ms here depending on load,
and `TOOL-aScannedThrottle-4` records HVCI/VBS enforcing with synchronous antimalware inspection of
exactly this shape. 1,500 spawns at 0.24 s is 360 s.

## The same defect is in check 23

Read rather than measured separately, because the final block's tick does not separate it:

- `alledger=$(for r in $(git ls-files …); do awk … "$r"; done)` — one `awk` process per record.
- `for sp in $alspecs; do case "$(basename "$sp")" … sdate=$(basename "$sp" | cut -c1-10)` — two
  `basename` spawns and a `cut` per spec, over roughly 250 specs.

That block ran for more than 600 s before the run was stopped, which is consistent with it and is
not proof of it. Attributing check 23 on its own is `TOOL-aThawedCorpus-2`'s first act.

## What this rules out

**An mtime-keyed cache.** Every build directory's filesystem mtime reads `2026-08-27 11:15`, the
worktree's creation time, while the last commit touching each is days older. That is git, which
records no mtimes, so a fresh clone, checkout or worktree resets all of them at once. The corpus
digest `tools/memory-recall/query.py` already computes is `st_mtime_ns` plus `st_size`, which is why
its index reports `rebuilt` on the first query in any new worktree. A cache keyed that way does not
merely miss sometimes here; it never hits.

**Keying on `CLOSED`.** Every build's last touching commit is inside seven days, because one
migration — `e6328ce4`, the mandatory roster pair — rewrote 55 build READMEs at once. Status is
authored and can be wrong; content is derived and cannot. Keying on "unchanged" covers the owner's
"fully closed" and also the idle-but-open build, and needs no new authored field.

## Contention caveat

40 to 41 `python.exe` processes belonging to another project's virtualenv and to a second Claude
session were resident throughout. The absolute figures are therefore inflated and are not a clean-box
baseline. The RATIO is what this record is for, and a 5x gap between one check and the other thirteen
is not explained by ambient load.

## An inherited red, found while measuring

`gen_build_index.py --check` exits 1 at `f5dff6ae` with this branch's own build folder moved out of
the tree: `dCarriedReceipt`'s README and fifteen specs are stale. `f5dff6ae` landed that build's
round-4 diff-review record without re-rendering. So hygiene check 9 reds the merge bar on `main`
right now, for every node. Repaired here by re-rendering, in its own commit, because this run cannot
reach a green bar over it.

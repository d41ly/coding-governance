# Where the longest leg on the bar spends its processes — a hypothesis, before the profile

**Serves:** research TOOL-aQuenchedHarness-7

Node `a`, 2026-09-07. `unattended kit gate` — `bash tools/unattended/check-unattended.sh` — is the
longest leg this repo runs, recorded at 3837 s, and unit 7 rebuilds it. This is the STATIC reading
taken before the profile, written down first so the profile can refute it rather than confirm
whatever the profile happens to show. The method being copied is the one landed in this build's own
base at `274aa39b`, which took `check-pass-order.sh` from 10184 s to 510 s by making one pass over
history into a cache instead of a `git` spawn per commit.

## What the file is

2905 lines. External call sites, counted by binary: `grep` 73, `awk` 48, `sort` 28, `sed` 14, `cut`
13, and 40 through the `GIT` wrapper — of which `rev-parse` 10, `merge-base` 9, `log` 5, `cat-file`
5, `ls-files` 4, `show` 3. **Zero python.** So the cost is not a heavy interpreter; it is the number
of times a cheap one is started, which on this fleet is ~320 ms bare and ~626 ms for `git`.

## The hypothesis: it multiplies per RECORD, not per check

Nothing in the counts above is large. What makes them large is that several of them sit inside loops
over the repository's own records, and the repository has grown:

```
49  memory/builds/*/RUN*.md        the records two of these loops iterate
102 memory/builds/*/README.md
```

Two loops iterate the first set — line 287 and line 419, both spelled
`for f in $(GIT ls-files "$M/builds/*/RUN*.md")`. The body at 287 is the expensive one. Per record it
runs, at minimum: one `grep -q`, one `awk` for the base, a `region` slice piped through `grep -v`,
`grep -o` and `sort -u` (four), a `GIT cat-file -e`, a `GIT show` piped through `awk`, `grep -o` and
`sort -u` (four more), and a `comm` over two process substitutions (three). That is **roughly fifteen
to twenty processes per record before the disposition branch**, and the disposition branch adds

```sh
rv_fc=$(GIT log --follow --diff-filter=A --format=%cs -- "$rvf" | tail -1)
```

— a rename-following log walk **per record**, which is the single most expensive shape in the file and
is exactly the per-item history walk the pass-order fix removed.

**The prediction, and it is falsifiable:** the leg's cost is approximately linear in the number of
`RUN*.md` records, dominated by the two loops over them, with the `--follow` log walk the largest
single term. If that is right, the seconds should track the record count across worktrees with
different histories, and the fix is the pass-order one — ONE `git log` over the paths of interest into
a cache keyed by path, then pure in-shell lookups.

**What would refute it:** a profile showing the cost concentrated outside those loops — in the 73
`grep` sites over the tree, say, or in a single expensive `merge-base` chain — would mean the
per-record loops are noise and the cache buys nothing. That is a real possibility and it is why this
is written before the measurement rather than after.

## How it will be measured

The same way this build measured everything else, because the method is the only part that has never
been wrong here: `PS4='+ ' bash -x tools/unattended/check-unattended.sh`, counting traced lines whose
first token is an external binary, grouped by binary and attributed to the loop they sit in. That
does not see inside a child process, so it undercounts, but it undercounts identically before and
after and it is the number that moved when `check-pass-order.sh` was fixed.

**It has NOT been measured yet, and this record claims nothing about the outcome.** The box was
running that checker's own 3800 s test suite when this was written, and a profile taken under it
would measure the contention rather than the leg — this repo has recorded the same leg varying 5.5x
median and 47.1x worst under load.

## What this does NOT say

- It does not say the two loops are wrong. They read what they must read; the question is only how
  many processes it takes.
- It does not assume the pass-order fix transfers. That fix cached commit metadata for a loop over
  COMMITS; this is a loop over FILES, and a per-file `--follow` walk may need a different shape —
  possibly one `git log --name-status` pass over the whole `memory/builds/` subtree.
- The 3837 s figure is a recorded gate-run reading under the bar, not a standalone one. The first
  suite this build ported showed a 6.5x contention factor between the two, so the standalone cost of
  this leg is unknown and may be far smaller than the number that makes it the longest.

# The memory re-measure with `runlog.py memory`

**What it is.** The re-measure counts how many bytes of the memory tree each agent reads. It reads
your machine's agent transcripts and prints, for each agent type and for all agents together, how
many agents ran, how many read memory, and the median and p90 of what they read. With `--landed` it
also grades a landing: the build that moved memory reads into work orders passes only if, thirty days
after it landed, the median agent that reads memory reads less than 33 KB (33,000 bytes). The tool is
`<prefix>/runlog/runlog.py`, which is `tools/runlog/runlog.py` in this repository. The runlog kit
README's section "The memory re-measure" is the full reference.

## What it counts

An agent can read memory three ways, and the measure counts all three:

- **read**: the result of a `Read`, `Grep`, `Glob`, `LS` or `NotebookRead` call whose path is under
  the memory root (`MEMORY_ROOT` in `.memory-tree.conf`, `memory` by default).
- **shell**: the output of a shell command that names a memory path in any word, or that runs a read
  verb: `record show`, `record find`, `gov tag`, `gov_record.py show`, `gov_record.py find`,
  `gov_tag.py`, or the recall query script `query.py` of the memory-recall kit.
- **slice**: the memory slices a work order inlines into an agent's prompt. No tool writes the record
  of those slices yet, so this channel reads `unarmed`. It never reads as zero bytes.

**Why counting `Read` alone could not fail.** Before this build, `Read` carried 40% of the bytes
agents read from memory and shell commands 59.5%. The build moves reads into work orders and
`record show`, so a measure counting only `Read` calls would fall whether or not agents read less.

Only agents count: direct subagents and workflow agents, from the sessions of this clone and its
`.claude/worktrees/` worktrees. Main sessions do not count, because the 33 KB target was set over
subagents. The measure prints counts only. No path, command or result text from a transcript is
printed, and it writes no file.

## How to use it

Report a window, by when each agent started: <!-- usage: script:tools/runlog/runlog.py#memory 48169c1f -->

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
python tools/runlog/runlog.py memory --from 2026-10-01T00:00:00Z --to 2026-10-08T00:00:00Z
```

Leave out `--from` or `--to` to leave that end open. Add `--transcripts <dir>` to read another
projects directory than Claude Code's own.

Grade a landing. The window is the thirty days from the commit's committer time, and the commit must
be an ancestor of `HEAD`:

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
```bash
python tools/runlog/runlog.py memory --landed <merge commit>
```

See the measure work on planted transcripts, with no transcript of yours read:

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
python tools/runlog/runlog.py memory --fixture --plant median-under
```

The cases are `read-memory`, `read-other`, `grep-memory`, `shell-path`, `record-show`, `gov-tag`,
`recall-query`, `shell-other`, `foreign-dir`, `outside-window`, `median-under`, `median-over`,
`not-due`, `unarmed`, `empty` and `privacy`.

## What the verdict says

Under `--landed` the last line is the verdict, for example
`memory: verdict unarmed · median 28930 B · target 33000 B · agents 517 · slice unarmed`.

| Word | Exit | Meaning |
|---|---|---|
| `pass` | 0 | The thirty days have passed, the slice channel is armed, and the median is below 33,000 B. |
| `fail` | 1 | The thirty days have passed and the slice channel is armed, but the median is 33,000 B or more. |
| `not-due` | 3 | The thirty days have not passed yet. |
| `unarmed` | 3 | The slice channel has no producer yet, so the total is missing a channel. |
| `empty` | 3 | No agent in the window read memory. |

Exit 2 means an argument was refused: a time that does not parse, a revision that is not an ancestor
of `HEAD`, or a memory root or transcripts root that does not resolve. Without `--landed` the
report prints no verdict and exits 0.

## Answering the ask

The verdict exists only thirty days after the build lands, so an ask in the dTotalRecall build's
`BACKLOG.md` carries it. To answer it, run `runlog.py memory --landed` on the merge that landed the
build, at least thirty days after that merge. The ask is done when the verdict line reads `pass`.
While it reads `not-due` or `unarmed`, the ask stays open.

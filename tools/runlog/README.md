# runlog — one line grammar for run logs, and one reader for them

<!-- gov:kit runlog@1.0 -->

Three producers append one line per act to a machine-local journal: the unattended driver, the gate
runner and the pre-push hook. Several consumers read those lines. This kit gives all of them ONE
grammar, stated here and implemented once in `runlog_lib.py`, so no producer invents a format and no
consumer re-parses one. The kit writes nothing; it is the reader and the reference writer.

## The grammar

One act is one line. A line is TAB-separated fields, every field is `key=value`, and the split is on
the FIRST `=`, so a value may carry `=` and spaces.

| rule | value |
|---|---|
| key | `[a-z][a-z0-9_]*`, with an optional `.` suffix of `[A-Za-z0-9_]+`. An all-digit suffix is an INDEX (`fail.1`, `ref.3`); any other is a name (`sess.CLAUDE_CODE_SESSION_ID`) |
| escaping | `\` becomes `\\`, TAB `\t`, LF `\n`, CR `\r`, and nothing else is escaped. Any other byte after a backslash is refused |
| field 1 | `v=1`, the grammar version. A reader refuses a line whose `v` it does not know |
| required | `v`, `t` (epoch seconds, `.` radix, at most six fraction digits), `p` (the producer) and `ev` |
| events | `start` and `end` pair on `n`, the nonce, keyed together with `p`. `once` is an unpaired act and is never an invocation |
| terminator | every line ends in LF. A final line without one is torn and counts as bad |
| length | at most 2048 bytes, not counting the LF |
| unknown keys | kept. A reader never drops a line for an extra key |
| duplicate keys | refused, because two lines run together look exactly like that |

**Truncation, for a producer that would exceed the cap.** Drop WHOLE indexed fields, highest index
first across every family, and count each family's drops into `<base>_more`, adding to any count the
producer already wrote. Only when no indexed field is left, cut the longest non-required value from
its end, never inside an escape. `render_line` is the reference implementation and the self-test runs
it; a shell producer that truncates must produce what it produces.

**Pairing duty.** Every `ev=end` line's nonce has an `ev=start` line in the same file. Each producer's
own suite asserts that over its whole journal, through `build_invocations`: an `orphan-end` is the
failure.

## Where the journals live

Under `runlog/` in the git COMMON dir: `driver.log`, `gates.log` and `pushes.log`. The common dir is
shared by the primary tree and every linked worktree of one clone, so all of them write and read the
same three files. It is a data location, not a kit path, it is never pushed, and nothing in it is
tracked.

`resolve_journal_root` finds it with ONE `git rev-parse --path-format=absolute --git-common-dir`.
Both halves of that spelling matter: the bare `--git-common-dir` prints a RELATIVE `.git` in the
primary tree, and `--git-dir` in a linked worktree names `.git/worktrees/<name>`, which would split one
clone's journal in two.

## The memory root

`resolve_memory_root(root)` reads `MEMORY_ROOT` from `.memory-tree.conf` at the repository root, the
way bash sourcing reads it, and strips its slashes. An absent key, or an absent conf, is the kit
default `memory`. A value naming no directory refuses by name, and so does one that would leave the
repository: a `..` segment, a drive colon or a backslash. Every consumer that addresses the memory
tree goes through it, because an adopter's root need not be `memory`.

## The command line

```bash
python <this kit>/runlog.py journal --producer driver     # or gates, or pushes
```

stdout carries one JSON object per good line, whose keys are exactly the line's keys. stderr carries
the resolved path, `lines=<n> bad=<k>`, and the first few refusal reasons with their line numbers. The
bad count is always printed for a file that exists, so a writer emitting garbage is loud. An absent
file prints `runlog: <path> absent` and exits 0: no producer has written yet, which is a state and not
an error. Exit 2 means no journal root resolved or the file could not be read.

## The library

| name | what it does |
|---|---|
| `parse_line(raw)` | one line, given without its LF, into a `JournalLine`; raises `ValueError` naming the broken rule |
| `check_line(raw)` | the same verdict without the raise: `None` when the line conforms, else the reason |
| `render_line(fields)` | the reference writer: escape, then truncate as above. No LF appended |
| `read_journal(path)` | a whole file into a `Journal`: state `absent`, `empty`, `read` or `unreadable`, the good lines, and one refusal per bad line. Never raises |
| `build_invocations(lines)` | `start`/`end` pairs as `Invocation`s whose state is `ended`, `killed-or-running` or `orphan-end` |
| `resolve_journal_root(start)` | `<common dir>/runlog` for the clone holding `start` |
| `resolve_memory_root(root)` | the memory tree's repo-relative root |

Parsing is one split per line with no per-line process and no per-line regex compile. The self-test
counts both over 100,000 lines by patching them, and prints the wall time as a report, never as a
verdict.

## What this kit does NOT check

- **Whether a value means anything.** `rc=banana` parses. Each producer's own suite grades its values.
- **Whether a line cut at a field boundary was cut.** A writer killed between two fields leaves a line
  that still parses. A torn line is caught only when the cut breaks the grammar, and it is then
  COUNTED rather than dropped.
- **Whether a journal is complete.** A producer that never wrote leaves nothing to count.
- **Retention.** Nothing prunes the journals, and every run adds to them.
- **A cut value is not marked.** The unattended driver reaches the value-cutting step, because its
  slug, worktree path and phase are unbounded, and so does the gate runner, whose run id is the
  caller's. Nothing on the line records that a cut happened.

## Running the self-test

```bash
python <this kit>/selftest.py
```

It builds scratch git trees under the system temp dir and never reads this repository's own journal.
It and its fixtures are withheld from `govkit apply`: its subject is this directory's code, which an
adopter does not edit.

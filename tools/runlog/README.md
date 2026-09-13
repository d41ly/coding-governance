# runlog — one line grammar for run logs, and one reader for them

<!-- gov:kit runlog@1.0 -->

Three producers append one line per act to a machine-local journal: the unattended driver, the gate
runner and the pre-push hook. Several consumers read those lines. This kit gives all of them ONE
grammar, stated here and implemented once in `runlog_lib.py`, so no producer invents a format and no
consumer re-parses one. The kit writes nothing; it is the reader and the reference writer. It also
carries the ONE redaction table that every consumer printing or classifying free text applies.

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
| `load_rules(path)` | a redaction table, compiled: the kit's own when `path` is omitted. Raises `ValueError` naming the line of a malformed row |
| `scan_secrets(text, rules)` | every secret value in `text` as a sorted `(start, end, rule_id)` span. The value itself never leaves the function |
| `render_redacted(text, rules)` | `text` with each of those values replaced by the placeholder, keys and prefixes kept |

Parsing is one split per line with no per-line process and no per-line regex compile. The self-test
counts both over 100,000 lines by patching them, and prints the wall time as a report, never as a
verdict.

## The redaction table

`redaction.tsv` beside the reader holds one row per secret class. Its own header states the columns,
the hint grammar and the template tokens, and they are not restated here. The class ids are a closed
list, `CLASS_IDS` in `runlog_lib.py`, and the self-test asserts the table against it in both
directions, so a class cannot go missing and a row cannot arrive undeclared.

The table is applied ONCE, on read, by a consumer that prints or classifies free text from a
transcript. Nothing is redacted on write, because no producer writes free text. A value becomes
`<redacted:<id>>` and what names it stays, as in `Authorization: Bearer <redacted:auth-header>`. Both
functions take an optional `rules` sequence from `load_rules`, which is how the self-test counts the
regex searches a scan makes.

A rule's regex runs only when the lowercased text holds one of its hints, so most text never reaches
a regex. Rules run in table order. A span overlapping one an earlier rule took is dropped, and a value
that already reads as a placeholder is skipped, so rendering twice changes nothing. A non-string
input raises `TypeError`, and the loader accepts a CRLF checkout of the table.

Each positive is a template that only the self-test expands, and no committed file of this kit carries
text the table flags outside that column. The self-test scans the kit's tracked files with the table
to prove it, which is the property push protection needs in a public repository.

## What this kit does NOT check

- **Whether a value means anything.** `rc=banana` parses. Each producer's own suite grades its values.
- **Whether a line cut at a field boundary was cut.** A writer killed between two fields leaves a line
  that still parses. A torn line is caught only when the cut breaks the grammar, and it is then
  COUNTED rather than dropped.
- **Whether a journal is complete.** A producer that never wrote leaves nothing to count.
- **Retention.** Nothing prunes the journals, and every run adds to them.
- **A cut value is not marked.** The unattended driver reaches the value-cutting step, because its
  slug, worktree path and phase are unbounded, and so does the gate runner, whose run id is the
  caller's, and so does the pre-push hook, whose remote name and worktree path are unbounded. Nothing
  on the line records that a cut happened.
- **A secret the redaction table has no shape for.** A class nobody listed, or a bare value printed
  with no key or prefix beside it, matches no row. There is no entropy rule, deliberately: hashes and
  shas are this repository's everyday tokens.
- **A value cut short before its shape completes.** A command head truncated inside a token's prefix,
  or before the length a row requires, is not redacted.
- **Text the table is never handed.** It reduces exposure in what a consumer prints or classifies,
  and proves nothing about journal values or tool output it never sees.
- **That a positive is realistic.** Each row is proven against its own template and a near miss, both
  written by its author. A real credential in a shape no positive covers is a miss the suite cannot
  see.

## Running the self-test

```bash
python <this kit>/selftest.py
```

It builds scratch git trees under the system temp dir and never reads this repository's own journal.
Its redaction arms find the kit's files through `git ls-files`, so a new file is scanned once it is
staged and not before.
It and its fixtures are withheld from `govkit apply`: its subject is this directory's code, which an
adopter does not edit.

# TOOL-aTrimmedWait-7 — `handoff.py agents` keeps its parsed session calls per transcript and parses only the bytes appended since

**Status:** CLOSED · rev-3 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 7 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aTrimmedWait-7-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aTrimmedWait-7-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md](../build/2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md) | journal | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-2-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-2-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-4-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-4-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-fix.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-fix.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-revision.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-revision.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-ruling.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-7-writing-practice.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-7-writing-practice.md) | research | — |
| [2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md](../reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md) | diff-review | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 |

<!-- /gen:spec-records -->

## 1. Goal

`handoff.py agents` re-reads and re-parses the whole session transcript on every call, and the main
loop calls it at every dispatch and every return. This unit keeps what the parse produced in one
record per transcript under the git common dir, proves the transcript's already-read bytes are
unchanged, and parses only the lines appended since. The verb's stdout and stderr stay
byte-identical, with the cache cold, warm and after an append (the brief's R6 criterion).

## 2. Scope (IN)

- **S1** — `tools/roles/handoff.py#load_session_calls` takes `cache_dir=None`. With `None` it reads
  exactly as today. With a folder it resumes from a valid record, parses only the complete lines
  after the record's offset, writes the record back when the offset moved, and only then parses an
  unterminated last line. Its per-line body moves unchanged into `parse_session_line(raw, state)`,
  which both paths call. Observed by AC1, AC2, AC4 and AC5.
- **S2** — `read_session_record` returns a record only when every key of §4 "Data model" holds,
  else `None`, which is a miss and a parse from byte 0. `write_session_record` writes through a
  temporary file and `os.replace`, and any `OSError` is swallowed, costing a later miss and never a
  refusal. Observed by AC3, AC6 and AC7.
- **S3** — `handoff.py` carries the canonical `common_git_dir` block inline, byte-identical, with a
  `read_git_stdout` reader bound as `git` beside it. `print_agent_lines` passes
  `common_git_dir(root) / SESSION_CACHE_DIR` to `load_session_calls`, or `None` when git cannot
  name the folder. Observed by AC8 and AC9.
- **S4** — One arm in `tools/roles/adopt-roles.test.sh`, after arm 22, re-observes AC1 to AC7
  through the CLI on arm 9's fixture. NOT OBSERVED by a pass criterion: the main loop observes it
  RED and then GREEN at the close, per §7's `New arm:` lines.
- **S5** — The verb's three descriptions name the record, where it lives and how to clear it: the
  `agents` paragraph of `handoff.py`'s module docstring with its WHAT THIS DOES NOT CHECK list,
  "The agent lines" in `tools/roles/README.md`, and "What each agent line tells you" in
  `help/roles.md`. Observed by AC10.

## 3. Non-goals (OUT)

- `load_agent_transcript` and `load_run_journal`. They read one agent's transcript and one run's
  journal, both small, and the measured cost is the session transcript (§4 "Evidence").
- Any change to what the verb prints, its selectors, its exit codes or `--write`.
- A flag to turn the cache off. Deleting the record folder makes it cold, and the record is keyed so
  a stale one is never used.
- Pruning records. §8 F1 asks it.
- `KIT_ROLES_VERSION`. The build README moves kit versions once, after the last code move.
- `tools/lib/common_dir.py` and the parity table in `tools/lib/resolve-python.test.sh`. The table
  finds copies by `git grep` (`tools/lib/resolve-python.test.sh@4b2fb1fb8c49:429`), so the inline
  copy joins the `common_git_dir` row's population with no edit.

### Edges

- **hands-off** external — the roles kit's version bump, which the build README defers to after
  the last code move of this build.

## 4. Design

### Evidence

Read at `846d51d3`. Every file cited is byte-identical at the build branch's `a25c84fc0`, which
added records only.

- `load_session_calls` opens the transcript and walks every line. It parses a line only when its
  bytes carry one of `SESSION_LINE_TOKENS`, and it builds `calls`, a `by_id` index into them,
  `notified` and the `bad` count (`tools/roles/handoff.py@26689d0bb1b5:776-823`, `:168-170`). A
  `tool_result` attaches to a call only through `by_id`, and only to a call already seen (`:803-805`).
- `print_agent_lines` calls it once and reads only the returned triple from it (`:1026`).
- `main` already runs one `git rev-parse --show-toplevel` (`:1197`). Other kits find the git common
  dir through the canonical `common_git_dir` block (`tools/lib/common_dir.py@9dfbea083aac:24-35`),
  each binding `git = read_git_stdout` beside its copy
  (`tools/playbook/tag_index.py@46bfe37d2a8b:461`). The drift kit keeps its history file there
  (`tools/drift-audit/drift_report.py@1234f714127:3814-3822`).
- The measured session `db957487` has a transcript of 52,312,549 bytes. It holds 168 calls and 378 <!-- PINNED 2026-11-14 -->
  notified ids, and no line fails to parse (PINNED, 2026-11-14, node a).
- `handoff.py agents --run wf_01f28407-289` on that session took 1.10 s, 1.26 s and 0.99 s of wall
  in three runs. Under `cProfile`, `load_session_calls` was 0.470 s of 0.873 s, of which
  `json.loads` was 0.187 s over 4,080 lines and the token scan 0.124 s over 104,191. A sha256 of <!-- PINNED 2026-11-14 -->
  the whole file took 0.041 s to 0.045 s. A JSON dump of the triple is 1,241,721 bytes and loads <!-- PINNED 2026-11-14 -->
  in 0.004 s. All PINNED, 2026-11-14, node a, with other sessions running on it.

### Data model

One record per transcript, at
`<git-common-dir>/handoff-calls/<first 16 hex of sha256 of the transcript's resolved path>.json`.
`SESSION_CACHE_DIR = "handoff-calls"`. The record is one JSON object with exactly these keys:

| Key | Value | Valid when |
|---|---|---|
| `parser` | sha256 hex of `handoff.py`'s own bytes | it equals this run's digest |
| `session` | the transcript's resolved path, POSIX form | it equals this run's path |
| `offset` | bytes consumed, each ending in `\n` | an int, not a bool, and 0 to the file size |
| `prefix` | sha256 hex of bytes 0 to `offset` | 64 lowercase hex, compared after reading |
| `calls` | the `calls` list as `load_session_calls` returns it | a list of dicts with keys `id`, `name`, `input`, `result`, `name` being `Agent` or `Workflow`, `input` a dict and `result` a dict or null |
| `notified` | the `notified` map | a dict of string to string or null |
| `bad` | the count of lines that did not parse | an int, not a bool, and at least 0 |

The record is written as `json.dumps` with its default `ensure_ascii`, so a lone surrogate the
transcript decoded round-trips. The `parser` digest makes any edit to `handoff.py` a miss. It is
DERIVED from the file, so nothing beside the code is bumped by hand. No pickle: the folder is
writable by any local process, and JSON cannot run code when read.

### The read

```
state = {calls: [], by_id: {}, notified: {}, bad: 0}; offset = 0; h = sha256()
rec = read_session_record(record path, parser, session) if cache_dir else None
open transcript rb
if rec: read bytes 0..rec.offset in 1 MiB chunks into h
        if h.hexdigest() == rec.prefix: state from rec, by_id rebuilt from calls in order, offset = rec.offset
        else: seek 0, h = sha256(), and parse from 0
for each line from offset:
    if the line does not end in \n: keep it as the tail, stop
    parse_session_line(line, state); h.update(line); offset += len(line)
if cache_dir and (no valid rec or offset != rec.offset): write_session_record(...)
if tail: parse_session_line(tail, state)
return state.calls, state.notified, state.bad
```

`by_id` is rebuilt by assigning each call in list order, so the last call holding an id wins, as it
does in the one-pass parse. The record is dumped before the tail is parsed, so it holds the state at
the last complete line and never a half-parsed write. A cold read counts a torn last line that
carries a token as `bad`, and so does this read. Once that line is completed, it is parsed from the record's offset,
which never passed it. A warm call with no new complete line writes nothing.

`write_session_record` creates the folder, writes `<record>.<pid>.tmp` and replaces the record with
it. On `OSError` it removes the temporary file and returns. Two processes on one transcript each
replace a whole record, and either is valid. On Windows a replace onto a record another process
holds open fails, and that is a later miss.

### The caller

`print_agent_lines` derives `cache_dir` as `common_git_dir(root) / SESSION_CACHE_DIR`. It catches
`OSError` and `subprocess.CalledProcessError` and passes `None`, which reads as today. The common
dir is shared by every worktree of the repository, so two worktrees reading one session share one
record. That costs one more git process per call: 0.04 s to 0.14 s median on node a when quiet
(PINNED, 2026-11-14), against the 0.47 s the warm read saves.

### The probe fixture

The builder writes `r6probe.py` under the run's scratchpad, called `<scratch>` below. It puts
`tools/roles` on `sys.path`, imports `handoff` and calls `load_session_calls` directly. Its rows use
the `use` and `res` shapes and the notification text of arm 9's fixture writer
(`tools/roles/adopt-roles.test.sh@3d54080483:357-366`): `use A` and `res A` for an `Agent` call
whose result names `resolvedModel` `claude-test-1`, `use W` and `res W` for a `Workflow` call, and
`note A`, the `<task-notification>` naming `toolu_A` as completed. Each case takes a fresh cache
folder under `<scratch>`, and "cold" means `cache_dir=None`. Each prints `PASS <case>` and exits 0,
or prints `FAIL <case>: <what differed>` and exits 1.

### What it does not check

- A record forged under the git dir with a matching `prefix` and `parser`. Its lines are trusted, as
  the transcript's own lines are. Any process that can write the record can write the transcript.
- A transcript rewritten so its first `offset` bytes keep their sha256.
- Whether the warm call is faster on another node. AC9 times node a.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

Each candidate was tested against the measured session, per M12.

| Candidate | Test | Result |
|---|---|---|
| A, resume from a byte offset, with a full-prefix sha256 as the key | Does the key cost less than the parse it saves? | Kept. The sha256 costs 0.045 s against the 0.470 s parse. |
| B, key the whole triple on size and mtime, and re-parse in full on any change | Does a call that has news to print find the file unchanged? | Lost. A `returned` line needs a notification record appended after the call (`tools/roles/handoff.py@26689d0bb1b5:817-822`). The verb runs at each dispatch and each return (`help/roles.md@edfba0e98377:146-149`), so every useful call follows a growth and B misses. |
| C, no cache, a faster line filter | What is the most it can save? | Lost. The token scan is 0.124 s of the 0.470 s, and `json.loads` of the matched lines stays. |
| D, a window hash of the prefix's last bytes | Does it prove the inputs? | Lost. A rewrite before the window keeps the key, and the build README falls back to the full run on an input it cannot prove. |
| E, the record beside the transcript, in the session's own folder | Does it need a write outside the repository? | Lost. It writes into the harness's store, a new write surface the unit's tier did not price (M3 veto 3). |
| F, a second `--git-common-dir` read in `main`'s existing rev-parse | Does it need a second spelling of the common-dir rule? | Lost. It answers beside the gated canonical block, which [one-fact] refuses, to save one git process. |

## 5. Production-readiness checklist

- security — The record is read input. It is JSON and never pickle, every key is checked by
  `read_session_record` before use, and its name is a hex digest, so no transcript path reaches a
  file name. Writes stay under the git common dir. §4 "What it does not check" states the forged
  record.
- perf / scale — A warm call reads the transcript once to hash it, about 0.045 s at 52 MB, and parses <!-- PINNED 2026-11-14 -->
  the appended lines only. The record is about 2.4% of its transcript: 1.24 MB for 52.3 MB.
- error / empty / loading states — A missing, malformed, stale or foreign record is a miss and a
  parse from byte 0. An unwritable folder is a miss on every call and prints nothing. A transcript
  shorter than the record's offset is a miss.
- observability — Silent by design, since stderr must stay byte-identical. The record is a file a
  reader can open, and its `offset` says how far it got.
- risks — A record from a different parser cannot be read as current, because `parser` is the
  file's own digest. Records are never pruned until §8 F1 says otherwise.
- testing — AC1 to AC7 run the probe of §4. AC8 is a block compare, AC9 the CLI on the measured
  session, and AC10 a grep. S4's arm repeats AC1 to AC7 through the CLI at the close.
- migration — None. The first call after landing finds no record and writes one.
- user docs — `help/roles.md` and `tools/roles/README.md`, S5.

## 6. Acceptance criteria

`<scratch>` and the row names are §4 "The probe fixture"'s. Every probe command runs from the
worktree root.

- **AC1** — When `python -I <scratch>/r6probe.py cold-warm` runs, it loads `use A`, `res A`, `use W`,
  `res W` and `note A` cold, then twice with one cache folder. All three triples compare equal, and
  one record `<16 hex>.json` sits in the cache folder after the first cached call. The second
  cached call leaves the record's mtime unchanged.
  Red when: the cached read drops a call, a result or a notification, so a triple differs.
- **AC2** — When `python -I <scratch>/r6probe.py poisoned` runs, it warms the cache and rewrites the
  record's first call's `resolvedModel` to `claude-poisoned`, keeping every key valid. The next
  cached load returns `claude-poisoned`.
  Red when: the warm path never reads the record and re-parses the transcript, which returns
  `claude-test-1`. AC1 alone cannot tell those apart.
- **AC3** — When `python -I <scratch>/r6probe.py prefix-edit` runs, it warms the cache, then changes
  `claude-test-1` to `claude-test-9` inside `res A` at equal length. The next cached load returns
  `claude-test-9`, and the record's `prefix` equals the sha256 of the edited file.
  Red when: the key checks the size or the offset alone and returns the stale `claude-test-1`.
- **AC4** — When `python -I <scratch>/r6probe.py append` runs, it warms the cache on `use A` and
  `use W`, then appends `res A`, `res W` and `note A`. The cached load equals the cold load of the
  same five lines, both results attached and `toolu_A` notified.
  Red when: `by_id` is not rebuilt from the record, so neither appended result attaches.
- **AC5** — When `python -I <scratch>/r6probe.py torn` runs, it writes `use A` and the first half of
  `res A`, cut after `toolUseResult`, with no newline. The cached load equals the cold load, `bad`
  is 1, and the record's `offset` is the length of `use A`'s line. It then completes the line. The
  next cached load equals the cold load, with `bad` 0 and the result attached.
  Red when: the offset passes the torn line, so the completed line is never parsed.
- **AC6** — When `python -I <scratch>/r6probe.py foreign` runs, it poisons the record as in AC2 and
  then breaks one key per sub-case: `parser` set to 64 zeros, `session` set to another path,
  `offset` past the file's size, and the record truncated to half its bytes. Each cached load
  returns `claude-test-1`, and none raises.
  Red when: a key is not compared, so that sub-case returns `claude-poisoned`.
- **AC7** — When `python -I <scratch>/r6probe.py unwritable` runs, it passes a cache folder whose
  parent is a regular file. The load equals the cold load, raises nothing and leaves no `.tmp` file
  under `<scratch>`.
  Red when: `write_session_record` lets the `OSError` out of `load_session_calls`.
- **AC8** — When the `common_git_dir` block is cut from `tools/roles/handoff.py` and from
  `tools/lib/common_dir.py` by `awk '/^# >>> common_git_dir/,/^# <<< common_git_dir/'`, CRs dropped,
  `cmp` finds them identical, and `grep -c '^# >>> common_git_dir' tools/roles/handoff.py` prints 1.
  Red when: the copy is edited, for instance to read the common dir relative to the working
  directory.
- **AC9** — When `python -B tools/roles/handoff.py agents --run wf_01f28407-289 --session <S>` runs,
  with `<S>` the `db957487` transcript, its stdout and stderr are captured at the base before any
  edit. After the build, the record folder is removed and the command runs twice. Each run's stdout
  and stderr `cmp` equal to the base's, and the acceptance ledger records the command timed three
  times before and three times after. Under `python -B -m cProfile -s cumtime`, the warm run's
  `load_session_calls` cumulative time is below 0.15 s.
  Red when: the warm call re-parses the whole transcript, about 0.47 s, or a line moves.
  fixture: the `db957487` transcript and its `subagents/workflows/wf_01f28407-289` folder exist on
  node a only.
  figure: the 0.47 s is PINNED from §4 "Evidence". The 0.15 s is three times the hash and load cost
  §4 measured, as headroom on a shared node.
- **AC10** — When `grep -n 'handoff-calls' help/roles.md tools/roles/README.md tools/roles/handoff.py`
  runs, each file has a hit. The `help/roles.md` hit says the folder may be deleted at any time.
  Red when: a description of the verb still says nothing of the record.

## 7. Gates

`policy fixtures` · `roles adopter self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `docs` · `lexicon naming predicates`

`python tools/check-spec-tokens.py --legs-for` over the estimate, run 2026-11-14 at `a25c84fc0`,
names `policy fixtures` for `tools/roles/handoff.py` and only broad `tools/` guards otherwise. The
other four legs read what this unit changes. `roles adopter self-test` holds the new arm. The
resolver leg's parity part grades the inline block. `docs` reads the help page, and the lexicon leg
grades the new function names, each answered `OK` by `lexicon.py --suggest --as py.function` on
2026-11-14. The main loop runs the merge bar once, at the close.

The arm stages its failing case by running the suite against `handoff.py` at the base, where
`load_session_calls` takes no cache folder and writes no record.

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC4 AC5 · arm 9's fixture run through the CLI cold, warm, with the record's `notified` emptied so the `returned` line drops, and after an append and a torn line; red at the base, where no record is written under the fixture's git dir · none
New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC6 AC7 · the record keyed off by a transcript edit, a foreign key and an unwritable folder, each printing the cold lines · none

What the arms do not check: timing, which AC9 owns on node a, and a forged record, which §4 states.

## 8. Open questions

- **F1 — Are records pruned, and how?**
  - (a) Never. One record per transcript ever read, about 2.4% of its size, kept until someone
    deletes the folder. No code. The transcripts beside them are not pruned by this kit either.
  - (b) One record only, keyed on the last session read. Bounded, with no prune code. Two
    worktrees reading two live sessions then miss on every call, which is the worst case today plus
    a 0.045 s hash.
  - (c) Per-transcript records, with any record whose mtime is older than a stated age deleted on
    each write. Bounded. It costs a stat per record per write and a stated age nothing derives.
  - Recommendation: (a). It is the only option with no code and no number to defend, and the
    growth is a fraction of what the harness already keeps. A prune is cheap to add once a folder
    is measured large.
  - RESOLVED (owner, 2026-11-14): (a), never prune.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from the build brief
  `2026-11-14-prompt-TOOL-aTrimmedWait-1-brief`, item R6, grounded at `846d51d3` with timings
  taken on node a.
- rev-2 · 2026-11-14 · §8 F1 · the owner resolved F1 to (a), never prune, per
  `2026-11-14-prompt-TOOL-aTrimmedWait-7-ruling`.
- rev-3 · 2026-11-14 · §4, §5 · each measured figure the pinned-facts arm named carries
  `<!-- PINNED 2026-11-14 -->` on its line, no meaning changed, per
  `2026-11-14-prompt-TOOL-aTrimmedWait-7-writing-practice`.

## 10. Reuse audit

The seam is `tools/roles/handoff.py#load_session_calls` itself, which this unit splits into
`parse_session_line` and a resume around it, and the canonical `common_git_dir` block of
`tools/lib/common_dir.py` for the record's folder. No existing seam fits the incremental read.
`python tools/codebase-map/reuse_lookup.py "cache parsed transcript records and parse only appended bytes"`
ranked name stems only (`parse`, `read_bytes`, `records`, `parse_conf`), none of which resumes a
read. A grep of `tools/` for `.seek(`, `.tell()` and `st_size` found no offset-resumed reader. The
recall probe returned `TOOL-dWellOiledMachine-43`, whose per-session byte cursor would have been the
seam, but that spec is DEFERRED and unbuilt. It returned `TOOL-dBoundRoles-8` and
`TOOL-dFurnishedOrders-3`, which name `load_session_calls` as the reader to reuse, which this unit
does. The candidates and the test each met are §4 "Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "is there an incremental or cached reader of a session transcript that parses only appended bytes" --terms "handoff agents session transcript load_session_calls cache incremental offset appended bytes jsonl"`

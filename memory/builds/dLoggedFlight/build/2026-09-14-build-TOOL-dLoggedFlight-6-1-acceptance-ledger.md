# Acceptance ledger — TOOL-dLoggedFlight-6

**Serves:** journal TOOL-dLoggedFlight-6

Tier-2 · node d · 2026-09-14 · the build pass of the transcript extractor, against spec rev-6. The
pass ran in two sessions: the first recorded its dispatch and brief rows, wrote rev-5 and most of the
code, and died on a session limit with the suite crashing; the second judged that partial work
against the spec, wrote rev-6 before its remaining code, and finished it. Every criterion line is
OBSERVED. The gate legs are written as owed. `<suite>` is `tools/runlog/selftest.py`, run directly
and never through the gate runner. Its three timed runs at the build commit printed
`591 passed, 0 failed (591 assertions, floor 591)` in 7.0 to 7.5 s. No gate leg was run, per the
owner's instruction of 2026-09-13, and no suite that existed under `tools/unattended/` before this
build ran. Every arm reads synthetic transcripts the suite writes into scratch roots; none reads a
real transcript or a real store.

## The criteria

**Evidences:** TOOL-dLoggedFlight-6

- AC1 — `read_session_ids` + `resolve_session_tree` (`test_extract_ac1_session_ids`) — over a
  scratch driver journal, the ids under `sess.CLAUDE_CODE_SESSION_ID` and `sess.ADOPTER_SESSION`
  both came back as candidates, a `../../escape` value and an uppercase id were refused and counted
  as 2, and an `end` line's id and another slug's id were not candidates. `resolve_session_tree`
  refused `../../escape` by its shape, and a valid id found its tree through the glob under a project
  dir no repository path names. The CLI wrote exactly the two extracts into the arm's store, printed
  `refused=2`, and wrote nothing else under the arm's scratch. A project dir that is a symlink out of
  the root was refused by name, and the CLI then counted that session as refused, `refused=3`, and
  still wrote the other two. RED seen with the shape check dropped (the traversal arm), with only
  `sess.CLAUDE_CODE_SESSION_ID` read (the any-variable arm and three more), and with the containment
  check dropped (the symlink arm).
- AC2 — `extract_session` (`test_extract_ac2_dedupe_order`) — over a fixture whose result's later
  copy, same `uuid`, carries empty output, and whose tool call's later copy would be a second call,
  the Bash call kept rc 3, `err` true and a 1.0 s duration from the first copy. Two later copies were
  counted in `dup_uuids` and yielded nothing, and the call written last in the file but made first
  came out as call 1, with every event in time order. RED seen three ways: the dedupe removed (a third
  call appeared), the dedupe removed with the first-result guard (the later copy's rc 0 won), and the
  sort keyed on file position (the order arm).
- AC3 — `scan_owner_turns` (`test_extract_ac3_owner_turns`) — the fixture's human record, null-origin
  `/compact`, absorbed `queued_command` and interrupt came back as four turns and its keepalive fire as
  one keepalive. The `<local-command-…>` echo and caveat, the compact summary, the peer message and the
  task notification were not turns. With the `CronCreate` removed, the same fire was neither a
  keepalive nor a turn, and a `CronCreate` in another session joined nothing, so only the join finds
  it. The CLI's written extract held none of the fixture's free-text leaves, and the same predicate
  found every one of them in the transcript as written. RED seen with the echo exclusion dropped (five
  turns), with the join disabled (no keepalive), and with a call's prompt persisted as its tool name
  (the leak arm named the keepalive prompt).
- AC4 — `extract_session` (`test_extract_ac4_background_end`) — a background Bash call launched at
  10:00:00 and acknowledged 0.1 s later ended at its queue enqueue, 60.0 s after launch, with a null
  rc of its own and a `tool_end` carrying `completed` and rc 0. An absorbed attachment ended a second
  background call with `failed` and rc 1 before its queue removal did. An async agent ended at its
  notification with no exit code. A foreground call ended at its result, and notifications naming it
  or an unknown id ended nothing. RED seen with async results treated as foreground: the first call
  read 0.1 s and five arms went red.
- AC5 — `python <kit>/runlog.py extract --session <sid>` (`test_extract_ac5_repo_key`) — run from the
  primary tree and a linked worktree of one scratch clone, it wrote under the same repo key, and from a
  second clone under a different one. The key equalled the first 16 hex of sha256 over the normalised
  `--git-common-dir`, computed in the arm, and `resolve_repo_key` returned it from either worktree. RED
  seen with the key derived from the working directory: the two worktrees split.
- AC6 — `python <kit>/runlog.py narration` (`test_extract_ac6_narration`) — a window over a fixture
  holding a planted bearer header in agent text and a planted GitHub token in an owner turn, both
  expanded from the redaction table's templates at test time, printed `<redacted:auth-header>` and
  `<redacted:github-token>` once each, no planted value, and the data banner as its first line. It
  printed the window's texts and no thinking block, tool call or tool output. A text planting a CR, the
  closing marker and an ESC printed them as escapes under the gutter, and the frame closed once. The
  arm's store directory and scratch listing were unchanged. RED seen three ways: the redaction removed
  (both credentials printed), a narration file written to the store (the listing arm), and the escape
  removed (a second closing marker at column 0).
- AC7 — `scan_preflights` + `python <kit>/runlog.py extract --discover` (`test_extract_ac7_discover`)
  — the session whose Bash call runs `unattended.sh --preflight tFixture` was attributed to `tFixture`,
  `attribution=heuristic`, on stdout and in its written extract. A session naming `tOther`'s preflight
  only in a tool's output, in narration and as `grep`'s argument was attributed nowhere and never
  extracted. RED seen with a byte regex over the raw line: the tool-output session was attributed.
- AC8 — `read_records` (`test_extract_ac8_streaming`) — over a generated scratch tree of 20,000
  records in three files, counted through the one parse seam with a finalizer per record, the
  high-water of records alive was 1 while iterating, `extract_session` never held more than one when
  the next was parsed, and every one of the 10,000 calls was still extracted. A hold-everything reader
  through the same counter held 20,000. `extract --measure` exited 0, printed `report-only`, a rate and
  a peak, and wrote no store. The launcher, `main`, aimed `HOME`, `USERPROFILE`, `LOCALAPPDATA`,
  `XDG_STATE_HOME` and `CLAUDE_CONFIG_DIR` at a decoy holding a canary transcript before any arm ran.
  After every arm, the old ones included, the decoy's listing by path, size and mtime was unchanged,
  and neither the arm's output nor any file in its scratch named the canary's id. The liveness arm ran
  a discovery with no redirection against a second decoy: it named that decoy's canary, its extract
  changed the listing, and the scratch search found the extract by name. RED seen with a reader that
  buffers a file before yielding (8,000 alive), with the arms' root redirection removed (four decoy
  listing arms), and with the scratch search blinded (the liveness arm).
- AC9 — `build_usage` (`test_extract_ac9_usage`) — a `requestId` repeated across three main-file
  records with output counts 10, 20 and 30 counted once, at 30. The totals split three ways: main 3
  requests, 108 in, 36 out; the direct agent 1 request, 11 in, 12 out; the workflow agent 1 request,
  21 in, 22 out, with cache fields split alike. Each agent file was one spawn labelled from its meta,
  the workflow run came from its file, and the run with no file was counted in `wf_missing`. RED seen
  with the copies summed instead of maxed, and with every request put in the main split.
- AC10 — `derive_tool_class` + the fixtures (`test_extract_ac10_members`) — every row of
  `fixtures/tool-classes.json` produced its class, flags, verb and slug, directly and through a
  written transcript. The rows produce every class and flag in the closed lists and nothing else,
  including `git reset --hard` flagged destructive and an `unattended.sh` call piped to `tail` flagged
  piped, with near misses beside them: a soft reset, a quoted mention, a heredoc body, a `||`, and a
  suite read rather than run. The scenarios produce every event kind, split and owner source, and
  nothing else. RED seen four ways: the `ask` row deleted, `Grep` classed `other`, the pipe flag
  narrowed to `|&`, and an eleventh kind added to the closed list.

## The edges the criteria do not name

`test_extract_edges` observed the §5 states. A torn line and a non-object line counted 2 `torn`, an
unknown record type counted by name, and an untimed tool call counted 1 `untimed`, with no exception.
A compaction kept its trigger and size, an API error came from a message and a retry notice from a
system record, a rejected quota was a `limit`, a hook denial and a user rejection joined their calls,
and a main-file `isSidechain` record counted as a direct agent's usage. A missing tree was the state
`absent` and the CLI wrote nothing for it. A malformed `--session` exited 2 naming the shape, and a
store that cannot be written exited 2, said so and marked the row `failed`. The store resolved per
platform and override, refused by name with no root and for a relative `RUNLOG_STATE_DIR`, and the
projects root followed `CLAUDE_CONFIG_DIR`, then the profile. RED seen with the relative refusal
removed. The floor rose from 370 to 591, and a mirror with it at 592 exited 1, under its floor.

## Staged RED

26 breaks, each applied to a MIRROR of the kit: a copy in a scratch dir, made a git repository so
that `git ls-files` resolves in it, and never the working tree. An unmodified mirror printed
`591 passed` before and after the batch, and every break went RED on a FAIL line naming the arm it
aimed at, with no traceback. The criterion lines above name each one.

## The checklist over the build commit

`gotchas.py --for-diff HEAD~1..HEAD` selected thirteen classes, and three were violated.

- `heredoc-escape-reaches-the-regex`: the build commit carried a literal U+2028 and U+2029 inside
  the narration frame's control-character class, where `\u` escapes had been typed. The class still
  matched both, so every arm was green, and a census of the kit's non-ASCII characters found them.
  The fold writes the escapes, and `repr()` of the compiled pattern now shows them spelled out. The
  same tool had already turned a `\u` escape in the transcript fixture into a raw ESC, which failed
  loudly and was repaired before the commit. The class record gains the tool's behaviour, since its
  remedy recommends that tool.
- `two-answers-to-one-question`: the dossier typed the AC8 arm's record count, which the suite owns
  as a constant. The fold drops the figure.
- `amendment-leaves-its-other-half-standing`: the command line gained exit 2 for a write failure,
  and its docstring still stated only the journal verb's statuses. The fold states the extractor's.

The others were checked and hold. Every refusal arm is paired with a case that fires, and all 26
breaks above went RED on their aimed arm. Every break mutated the code or the suite under test,
except the one deleting a fixture row, which is AC10's own subject. No fence line is odd in any file
the commit touched. Every definition, nested ones included, leads with a declared verb, and no type
name ends in a banned suffix. No foreign build's id is cited. The suite pins no revision, and no
commit landed while it ran. The suite printed `591 passed` after the fold.

Over that fold the checklist selected seven classes, and `amendment-leaves-its-other-half-standing`
was violated once more: the class record's own fix still recommended a file-writing tool without
the qualification its new section adds. A second fold points the fix at that section.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `runlog selftest`, at or above its floor of 591 inside its 60 s budget row;
- `lexicon naming predicates`, `install-prefix (shipped surface)` and
  `dead-path carriers (deleted files still named)`;
- `govkit selfcheck`, since two fixtures joined the kit's withheld list;
- `codebase-map coverage + freshness` and `memory hygiene`;
- `every held leg is budgeted, every budget row resolves`, since the budget row's evidence changed;
- `testsuite counts (every bar self-test prints one)`.

## Residue

- The first session's suite crashed on its AC8 arm: a `WeakSet` cannot hold a dict, and the tracked
  record subclassed one. The count is now a finalizer per record.
- The first session named three functions outside the verb table, `_list_files`,
  `_strip_heredocs` and a nested `drop_one`; they are `_build_file_list`, `_remove_heredocs` and
  `remove_one`, per `lexicon.py --suggest`.
- Found by judging the partial work against the spec, and each written into rev-6 first: the
  keepalive join read agent files, so `extract_session` and `scan_owner_turns` could disagree about
  one record; narration joined a fire to a LATER `CronCreate`; the classification rule said an
  unquoted `$(…)` was never descended into, which the code does; the narration frame let a raw CR or
  ESC through; the launcher graded output but not the files an arm left in its scratch; one refused
  session aborted a multi-session extract; and a write failure raised instead of being reported.
- A report-only run of the extractor over every local session raised no exception, and printed
  nothing that was committed. Profiling its largest session found the tokenizer trying every
  separator at every character; it now tries them only at a separator's first character.
- The kit's `.gitattributes` pins already cover the new module and fixtures, so that file did not
  move. `tools/install-prefix-carried.txt` and `tools/govkit/subject-pins.tsv` did not move either:
  no shipped file gained a kit-path literal and no leg was added.
- The runlog kit stays at 1.0, as the brief sets it, and no kit version moved in this unit.
- The budget row's evidence now reads 8 s, the worst of three direct invocations rounded up, in the
  `measured <n>s on <node>` spelling `run-selftests.sh --rank` ranks; the row it replaced wrote a
  decimal the ranker's pattern could not read. Its figure stays at the file's 60 s floor.

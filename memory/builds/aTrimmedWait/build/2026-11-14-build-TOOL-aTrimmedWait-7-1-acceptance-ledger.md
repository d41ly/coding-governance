# TOOL-aTrimmedWait-7 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-7

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-3, from the
worktree root. The pass probe is §4's `r6probe.py`, saved in the run's scratch directory; it puts
`tools/roles` on `sys.path` and calls `tools/roles/handoff.py#load_session_calls` directly. The
changed code is `tools/roles/handoff.py#load_session_calls`, `tools/roles/handoff.py#parse_session_line`,
`tools/roles/handoff.py#read_session_record`, `tools/roles/handoff.py#write_session_record`,
`tools/roles/handoff.py#common_git_dir` and `tools/roles/handoff.py#print_agent_lines`. The new arm,
arm 23 of `tools/roles/adopt-roles.test.sh`, and its RED-first observation are owed to the main loop
at the close.

**Evidences:** TOOL-aTrimmedWait-7
- AC1 — `python -I <scratch>/r6probe.py cold-warm` printed `PASS cold-warm`: the cold triple and
  both cached triples compared equal, one `<16 hex>.json` record sat in the cache folder after the
  first cached call, and the second cached call left its mtime unchanged.
- AC2 — `python -I <scratch>/r6probe.py poisoned` printed `PASS poisoned`: after the record's first
  call's `resolvedModel` was rewritten, the cached load returned `claude-poisoned`.
- AC3 — `python -I <scratch>/r6probe.py prefix-edit` printed `PASS prefix-edit`: after `claude-test-1`
  became `claude-test-9` at equal length, the cached load returned `claude-test-9` and the record's
  `prefix` equalled the sha256 of the edited file.
- AC4 — `python -I <scratch>/r6probe.py append` printed `PASS append`: warmed on `use A` and `use W`,
  then `res A`, `res W` and `note A` appended, the cached load equalled the cold load, both results
  attached and `toolu_A` notified.
- AC5 — `python -I <scratch>/r6probe.py torn` printed `PASS torn`: with `res A` cut after
  `toolUseResult`, the cached load equalled the cold load with `bad` 1 and the record's `offset` the
  length of `use A`'s line; once completed, the cached load equalled the cold load with `bad` 0 and
  the result attached.
- AC6 — `python -I <scratch>/r6probe.py foreign` printed `PASS foreign`: with `parser` set to 64
  zeros, `session` set to another path, `offset` past the file's size, and the record truncated to
  half its bytes, each cached load returned `claude-test-1` and none raised.
- AC7 — `python -I <scratch>/r6probe.py unwritable` printed `PASS unwritable`: a cache folder whose
  parent is a regular file loaded equal to the cold load, raised nothing and left no `.tmp` file.
- Probe liveness — each case was re-run over a scratch copy of the kit with one break staged, and
  each printed `FAIL`: `by_id` not rebuilt reds `append`; the `parser` compare dropped reds
  `foreign`; the `prefix` compare dropped reds `prefix-edit`; the torn-line stop dropped reds `torn`
  (`offset` passed the torn line); `write_session_record` catching `ValueError` in place of `OSError`
  reds `unwritable` with `FileExistsError`; and `handoff.py` at the base reds `cold-warm` with a
  `TypeError`, since `load_session_calls` takes no cache folder there.
- AC8 — the `awk '/^# >>> common_git_dir/,/^# <<< common_git_dir/'` cut of `tools/roles/handoff.py`
  and of `tools/lib/common_dir.py`, CRs dropped, compared identical under `cmp`, and
  `grep -c '^# >>> common_git_dir' tools/roles/handoff.py` printed 1.
- AC9 — `python -B tools/roles/handoff.py agents --run wf_01f28407-289 --session <S>`, `<S>` the
  `db957487` transcript, was captured at the base before any edit: exit 0, its stdout two lines and
  its stderr one `--write` note. After the build, with the record folder removed, the command ran
  twice and each run's stdout and stderr `cmp` equal to the base's; the second run read the record.
  The same command timed before the edit: 0.65 s, 0.66 s and 0.65 s of wall. <!-- PINNED 2026-11-14 -->
  The same command timed after the build, warm: 0.48 s, 0.47 s and 0.47 s of wall. <!-- PINNED 2026-11-14 -->
  Under `python -B -m cProfile -s cumtime`, `load_session_calls` was 0.384 s cumulative at the base <!-- PINNED 2026-11-14 -->
  and 0.057 s on the warm run after the build, below the 0.15 s bound. <!-- PINNED 2026-11-14 -->
  The transcript measured 54049817 bytes on this run and its record 1242071 bytes. <!-- PINNED 2026-11-14 -->
- AC10 — `grep -n 'handoff-calls' help/roles.md tools/roles/README.md tools/roles/handoff.py` hit
  each file; the `help/roles.md` hit's paragraph says the folder may be deleted at any time.
- Verdict parity — the verb's base `handoff.py`, from `git show HEAD:tools/roles/handoff.py` in a
  scratch copy of the kit, and the built one, cold and then warm, ran over the same five inputs:
  the green `--run wf_01f28407-289` on `<S>`, the refusal of a run with no journal, the refusal on a
  scratch session ending in a torn line, the refusal of a `--handoff` file holding no marker, and
  the usage exit for a missing session file. Exit codes, stdout and stderr were byte-identical
  across base, built and warm on all five: 0, 1, 1, 1 and 2.
- Owed to the close: arm 23 of `tools/roles/adopt-roles.test.sh`, which covers both `New arm:` lines <!-- DERIVED from the spec's section 7 -->
  of the spec, its eight assertions and `FLOOR_ASSERTIONS` at 69, observed RED with `handoff.py` <!-- DERIVED from 61 plus arm 23's eight check_arm calls -->
  at the base and GREEN once restored; and the gate legs §7 lists.

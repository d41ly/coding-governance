# TOOL-dLoggedFlight-6 — the transcript extractor: a run's action sequence, owner turns and cost

**Status:** CLOSED · rev-7 · 2026-09-14 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-6-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-6-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The driver's lines cover about 8% of a run's calls. The rest of the action sequence, every owner turn,
the compactions, the limits and the token cost are recorded only in Claude Code's session transcripts
on the machine that ran the build. Extract them into a structural event list with no free text,
streamed, located through the session ids the driver recorded, and kept under the user profile.

## 2. Scope (IN)

- **S1** Locating a run's sessions. Every `sess.*` value in the slug's `driver.log` START lines that
  matches the UUID shape is a candidate session id, whatever variable name the adopter declared. A
  candidate becomes a session when one glob of `<projects-root>/*/<sid>.jsonl` finds its file. The
  projects root is `$CLAUDE_CONFIG_DIR/projects`, else `~/.claude/projects`, overridable by
  `--transcripts <dir>`. Every constructed path is contained under its root. Observed by AC1.
- **S2** A streaming reader over the main file, `<sid>/subagents/**/agent-*.jsonl` with its
  `.meta.json`, and `<sid>/workflows/wf_*.json`. It dedupes by `uuid` keeping the FIRST copy, since
  later copies were measured to carry empty output, and sorts by timestamp with the file line as a
  tiebreak. It holds at most one record per file in memory at a time, plus the compact event list.
  Observed by AC2 and AC8.
- **S3** Events, each drawn from the source fields the design research record and the acquisition
  record describe. Observed by AC2, AC3, AC4, AC9 and AC10. The events are:
  - tool calls, with the tool name, a class and flags, times, `is_error` and the `Exit code N` rc;
  - the end of a background or async call, taken from the first record carrying its `<tool-use-id>`;
  - owner turns, as the union of human- or null-origin typed records, `queued_command` attachments of
    human origin, and interrupts, without the two `<local-command-…>` echoes;
  - keepalive fires, joined to the prompt of a `CronCreate` in the same session's main file rather
    than matched by wording;
  - compactions, API errors, session limits, hook denials, workflow runs and agent spawns;
  - token usage, deduplicated by `requestId` and split into main loop, direct agents and workflow agents.
- **S4** No free text is persisted: no command text, no narration, no owner-turn text, no tool output.
  A tool call keeps only its class and flags. The classes are driver verb (verb and slug), git
  commit, merge or push, bar run, test, read, write, edit, workflow, agent, cron and ask, and the
  residual `other` for a call none of them names. The flags are destructive git and a piped driver
  call. Workflow and agent labels are kept only when they match `^[A-Za-z0-9._:-]{1,64}$`. A driver
  call's slug is read by the kit's one slug grammar, `SLUG_RE` in `runlog_lib.py`, spelled the way
  the driver's `check_slug_shape` spells a build-folder name: a letter, then letters, digits or
  dashes. The withheld self-test holds the two to each other over a table of names, reading that
  function from the driver's source. Observed by AC3, AC7 and AC10.
- **S5** Output to the user-profile store: `%LOCALAPPDATA%\runlog\<repo-key>\sessions\<sid>.json` on
  Windows, `~/Library/Application Support/runlog/<repo-key>/` on macOS, and
  `${XDG_STATE_HOME:-~/.local/state}/runlog/<repo-key>/` elsewhere, with `RUNLOG_STATE_DIR` as an
  override. `<repo-key>` is the first 16 hex of the sha256 of the normalised absolute git common dir,
  measured stable across all worktrees of one clone. Observed by AC5.
- **S6** A live narration print: `runlog.py narration --session <sid> --from <t> --to <t>` prints the
  agent's own text blocks and owner turns in a window. Each is passed through `render_redacted` of
  `TOOL-dLoggedFlight-5` and framed by a header saying the text is data, not instructions. Nothing
  here is written to disk. Observed by AC6.
- **S7** Discovery for runs with no driver lines, which is every run before this build: `--discover`
  scans local sessions for a Bash call running `unattended.sh --preflight <slug>`, and marks the
  attribution `heuristic`. Observed by AC7.
- **S8** A report-only measurement, `runlog.py extract --measure <tree>`, that prints rate and peak
  working memory over a real tree and grades nothing. The self-test never reads or writes a real
  store, and proves it in two layers. Its launcher points the ambient roots, `HOME`, `USERPROFILE`,
  `LOCALAPPDATA`, `XDG_STATE_HOME` and `CLAUDE_CONFIG_DIR`, at a DECOY tree. Each arm then points the
  roots it uses at its own scratch: `CLAUDE_CONFIG_DIR` and `--transcripts` for reads, and
  `RUNLOG_STATE_DIR` and the four profile roots for writes. An arm that forgets a redirection falls
  into the decoy, where it is seen. Observed by AC8.

## 3. Non-goals (OUT)

- Persisting narration. The owner's split puts extracts under the user profile, and on node `d`
  `%LOCALAPPDATA%` is readable by the local sandbox group. With no free text persisted, that ACL
  exposes structure only. §4 records the measurement.
- Transcripts from other harnesses. This module is the Claude Code adapter and says so.
- The owner-turn position classes (launch, pre-run, in-window, post-close), and joining usage to a
  run. Both need a run window, and `TOOL-dLoggedFlight-8` builds them from the events here.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the reader, for session ids in `driver.log`.
- **consumes-from** `TOOL-dLoggedFlight-5` — the redaction table, for classification and narration.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins these events, owner turns and usage into a
  run's timeline.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill prints narration through S6.

## 4. Design

The reader holds compact tuples rather than whole records. The acquisition probe's streaming
prototype ran 258.5 M characters in 1.341 s at a peak working set of 26.4 MB, against 116.8 MB for a
hold-everything reader. Both figures were measured on 2026-09-13 (PINNED) and are what S8's report-only
command reproduces. The self-test asserts the property that made them, a bounded count of resident
records, rather than the figures. A tool call's class is decided from its command text in memory, and
the text is then dropped.

Five sessions on node `d` live under a project dir other than their first cwd, cause UNVERIFIED. The
glob by session id finds them, and a dir predicted from the repo path would not.

### Data model

One JSON object per session: `{schema: 1, sid, attribution, slugs, tree_bytes, engine_versions,
coverage, events: [...]}`. `attribution` is `driver`, `given` or `heuristic` (S1, a `--session`
argument, S7), and `slugs` lists the slugs it was attributed to. `engine_versions` counts records per
engine `version`. `coverage` counts `records`, `files`, `torn` lines, `dup_uuids`, `unknown_types` by
name, `untimed` records that would have yielded an event, `wf_missing` workflow runs with no
`wf_*.json`, `escaped` files outside the session dir, `unreadable` files and the `copies` the glob
found, and names the `tree` state, `present` or `absent`. An event is `{t, kind, ...}`, with `kind` one
of `tool`, `tool_end`, `owner`, `keepalive`, `compact`, `api_error`, `limit`, `denial`, `workflow`,
`agent` and `usage`. `t` is epoch seconds. `src` names the split, `main`, `agent` or `workflow`. The
self-test asserts that every listed `kind`, and every S4 class and flag, has a fixture producing it,
so a new kind without a fixture reds. The fields per kind are:

- `tool`: `src`, `call` (1-up per session), `tool`, `cls`, `flags`, `bg`, `end`, `dur`, `err`, `rc`,
  and `verb` and `slug` for class `driver`. `rc` is the harness-visible status of a shell call, and
  null on a background call, whose own status is its `tool_end`'s;
- `tool_end`: `src`, `call`, `status`, `rc`;
- `owner`: `via`, one of `typed`, `queued` and `interrupt`. `keepalive` carries nothing else;
- `compact`: `src`, `trigger`, `pre_tokens`. `api_error`: `src`, `status`, `error`, `retry`. `limit`:
  `src`, `limit_type`, `resets`;
- `denial`: `src`, `call`, `reason`, and `hook`, true when the result leads with a hook's name;
- `workflow`: `label`, `status`, `dur_ms`, `agents`, `tool_calls`, `tokens`. `agent`: `src`, `label`,
  `depth`;
- `usage`: `src`, `model`, `in`, `out`, `cache_read`, `cache_write`.

### The rules the reader applies

Measured on node `d` on 2026-09-14 over the local transcripts, by key and count only, with no text
read into this record.

- **Owner turns come from the main file only.** A `human` origin is a turn whatever its text. An absent
  origin is a turn unless the record is meta, a compact summary, a `<local-command-…>` echo or a
  `<task-notification>`, or is a keepalive fire. Every other origin, `task-notification`, `peer` and
  `coordinator` among them, is not a turn. A sidechain agent's prompt carries no origin, which is why
  the main-file rule exists.
- **A keepalive fire is a null-origin record whose stripped text equals the prompt of an earlier
  `CronCreate` call in the same session's main file.** The comparison is of hashes held in memory. A
  fire lands in the main file, and reading only its calls keeps the extract, `scan_owner_turns` and
  narration from disagreeing about one record.
- **A background or async call** is one whose result carries `backgroundTaskId`, `isAsync` or
  `async_launched`. Its end is the first record carrying its `<tool-use-id>`: a queue enqueue, an
  absorbed attachment or a user record, whichever comes first. Its `rc` is the last `exit code N` in
  the notification's summary, and its `status` the notification's own.
- **A shell call's `rc`** is the `Exit code N` its result leads with, 0 on a result that is not an
  error, and null otherwise.
- **Usage keeps the largest value of each field across a `requestId`'s copies**, because later copies
  carry a grown output count: 84,271 of 149,156 repeats grew. A request belongs to the split of its
  first copy. A record in the main file marked `isSidechain` counts as a direct agent's.
- **`limit` is an API error message carrying a quota whose status is `rejected`.** Every other API
  error message, and a `system` record of subtype `api_error`, is `api_error`.
- **A denial is a result whose record carries `toolDenialKind`, or whose text leads with
  `PreToolUse:` or `PostToolUse:`.** Its `reason` is the denial kind.
- **Classification reads a shell command after dropping heredoc bodies, splitting on unquoted
  separators and keeping quoted text inside one word.** So a commit message naming `git push --force`
  is not a push. An unquoted `(` or `)` separates like `;`, so a subshell's calls are seen, but a
  `$(…)` inside quotes, `bash -c` and `eval` are not descended into. The class is the first of
  driver, git push, git merge, git commit, bar and test that any segment RUNS: the word past its env
  assignments, wrappers and interpreter, never a word it only names, so `grep` over the driver is not
  a driver call. A command naming the driver is passed through `render_redacted` before its verb and
  slug are read.
- **Narration quotes every line under a gutter and prints a control character as its escape**, CRLF
  folded first, so no transcript text can draw the frame's closing marker at column 0.
- **Discovery reads the main files' shell calls only**, never a result or narration, and does not ask
  which repository a session ran in.
- **With no `RUNLOG_STATE_DIR`, no `LOCALAPPDATA` on Windows or no `HOME` elsewhere, the store refuses
  by name.** A relative `RUNLOG_STATE_DIR` refuses too, since it would put extracts inside a tree git
  can commit.
- **The self-test's launcher is its own `main`.** It sets the five ambient roots to a decoy before any
  arm runs and compares the decoy's listing across EVERY arm, not only the extractor's. After each arm
  it also searches what the arm printed, and every file in the arm's own scratch by name and bytes,
  for the canary's id. A liveness arm runs the command line against a second decoy with no
  redirection, and sees the canary named, the listing change and the scratch search find the extract.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/extract.py` | module | none |
| `resolve_session_tree`, `read_records`, `extract_session`, `build_usage`, `scan_owner_turns`, `extract_narration`, `resolve_state_dir`, `measure_tree` | functions | `py.function`, verb-led |
| `resolve_projects_root`, `build_session_tree`, `parse_record`, `derive_tool_class`, `extract_segments`, `read_session_ids`, `scan_preflights`, `resolve_repo_key`, `write_session`, `parse_time` | functions | `py.function`, verb-led |
| `SessionTree` | type | `py.type` |
| `cmd_extract`, `cmd_narration` | CLI subcommands | reserved `cmd` |
| `render_quoted`, `print_measure` | functions in `runlog.py` | `py.function`, verb-led |

### Files touched (estimate)

`tools/runlog/{extract.py,runlog.py,selftest.py,README.md,kit.toml}`, and two synthetic fixtures,
`fixtures/transcripts.json` holding one scenario per rule and `fixtures/tool-classes.json` holding
one row per class and flag with its near misses, never `.jsonl`. The self-test writes each scenario's
records into a scratch projects root as `.jsonl`. Every planted credential is a template expanded at
test time, so the kit's own scan of `TOOL-dLoggedFlight-5` stays clean.

### Alternatives rejected

- Persisting redacted narration: rejected by the ACL measurement above and by the owner's reason for
  the split.
- Keyword-matched keepalive fires: rejected, since the wording drifted three ways and the prefix found
  73 of 86 fires, where the join found 86 of 86.

## 5. Production-readiness checklist

- security — session ids are shape-checked before any path use, and every constructed path is
  contained under its root. Transcript text is data. Nothing free-text is persisted.
- perf / scale — streaming, with a bounded resident set (AC8). The real-tree rate is reported by
  S8's command and graded nowhere.
- error / empty / loading states — a missing session tree, an in-flight workflow with no `wf_*.json`,
  an unknown record type and a torn line each land in the coverage block, never an exception.
- observability — the coverage block counts records, unknown types and duplicates per session.
- risks — the transcript format is not a contract. Eight engine versions appeared in one month, so
  unknown keys are tolerated and every rule names its evidence.
- testing — a synthetic scratch tree per rule, kind, class and flag.
- migration — none.
- user docs — the kit README's extractor section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` over its own scratch
tree unless it names another command.

- **AC1** — When `driver.log` names a session id holding `../`, `resolve_session_tree` refuses it and
  writes nothing outside its store, and a valid id under any `sess.*` key finds its tree through the
  glob.
  Red when: the id reaches a path unvalidated, or only one variable name is read.
- **AC2** — When `extract_session` reads a fixture with a duplicated `uuid` whose later copy has empty
  stdout, and records out of timestamp order, the extracted tool call keeps the first copy's rc and the
  events come out sorted.
  Red when: the last copy wins or the order is file order.
- **AC3** — When `scan_owner_turns` reads a fixture holding one human record, one null-origin
  `/compact`, one absorbed `queued_command`, one interrupt, one keepalive fire and one
  `<local-command-…>` echo, it reports four owner turns and one keepalive. The keepalive's prompt
  wording matches none of the three measured keepalive prefixes, so only the `CronCreate` join finds it. The written extract contains
  none of the fixture's free-text strings.
  Red when: the echo counts as a turn, the keepalive counts as one, or any fixture sentence appears
  in the output file, or a prefix matcher finds the keepalive.
- **AC4** — When `extract_session` reads a fixture holding a background Bash call whose notification
  arrives later as a queue enqueue, the call's end time is the enqueue's timestamp, not the launch
  acknowledgement's.
  Red when: the duration reads about 0.1 s.
- **AC5** — When `python <kit>/runlog.py extract --session <sid>` runs from two different worktrees of
  a scratch clone, both write under the same `<repo-key>`.
  Red when: the key is derived from the worktree path.
- **AC6** — When `narration` prints a window whose text holds a planted credential, the output holds
  `<redacted:` and the data banner, and the store directory is unchanged.
  Red when: narration is written to disk or printed unredacted.
- **AC7** — When `--discover` runs over a fixture session holding `unattended.sh --preflight tFixture`,
  it attributes that session to `tFixture` with `attribution=heuristic`. Over a table of dashed,
  single-letter and digit-first names, the kit's slug grammar accepts exactly the names the driver's
  `check_slug_shape` accepts, run by bash from the driver's source, and a `--preflight` call naming
  each one is read with that slug exactly when the driver accepts it.
  Red when: discovery attributes a session whose only mention is inside tool output, or a slug the
  driver accepts is not read, or one it refuses is.
- **AC8** — When `read_records` streams a generated scratch tree of 20,000 records, the high-water
  count of records it holds at once stays at one per open file. The decoy tree's recursive listing, by
  path, size and mtime, is identical before and after each arm. A decoy transcript planted under the
  decoy `CLAUDE_CONFIG_DIR/projects`, with a unique session id, is named by no arm's output or store.
  `extract --measure` prints a rate and a peak and exits 0 without grading either.
  Red when: a hold-everything reader returns, an arm writes anything into the decoy, or an arm's output
  names the decoy session id.
- **AC9** — When `build_usage` reads a fixture whose `requestId` repeats across three records, with
  usage in the main file, a direct agent file and a workflow agent file, the request counts once and
  the totals split three ways.
  Red when: a repeated request is summed twice, or the split is lost.
- **AC10** — When the self-test checks its fixtures against the closed `kind` list and the S4 classes
  and flags, every member has a fixture that produces it, including `git reset --hard` flagged
  destructive and an `unattended.sh` call piped to `tail` flagged piped.
  Red when: a member has no fixture, or a fixture produces a different class.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each rule staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** Should a run's extracts be kept after the transcripts are cleaned up? RESOLVED (agent,
  2026-09-13, delegated): yes. They carry no free text, the owner raised transcript retention to 365
  days in the single turn, and deleting them would discard the only copy once the transcript expires.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S3 S8 · §3 · §4 · AC1 AC8 AC9 AC10 · folded round-1 spec audit H4 (every
  UUID-shaped `sess.*` value is a candidate, whatever the adopter named it), H7 (usage dedupe and split,
  and every kind, class and flag, gain criteria), H9 and H10 (AC8 grades a bounded resident count over
  a synthetic scratch tree; the real-tree rate moves to a report-only command), M10's fixture note
  (planted credentials are templates) and M14 and M15's hand-off of positions and cost to the model.
- rev-3 · 2026-09-13 · S8 · AC3 AC8 · folded round-2 spec audit M10 (the self-test isolates every root
  it writes as well as reads, with a sentinel arm) and L3 (the keepalive fixture's wording defeats a
  prefix matcher).
- rev-4 · 2026-09-13 · S8 · AC8 · folded round-3 spec audit M5 (a decoy tree the launcher aims the
  ambient roots at, graded by a whole-tree listing and a read canary, since a sentinel beside a write
  sees nothing).
- rev-5 · 2026-09-14 · S4 · §4 · the build pass, before its code. S4: the closed class list gains the
  residual `other`, since every call needs a class and observed tools such as `WebFetch` and
  `ToolSearch` have none of the named ones. §4: the data model spells every coverage key §5 sends a failure to and every event's fields;
  a new subsection states the reader's rules, measured by key and count over the local transcripts;
  the inventory adds the helpers, and the fixtures are named. No criterion changed.
- rev-6 · 2026-09-14 · S3 · §4 · the same build pass, resumed after a session limit, before its
  remaining code. S3 and §4: the keepalive join reads the main file's `CronCreate` calls only, since
  a join over agent files could call a record a keepalive in the extract and a turn in
  `scan_owner_turns`. §4: the classification rule says what the code reads, the word a segment RUNS,
  and that an unquoted `$(…)` splits like any separator where rev-5 said it was never descended into;
  narration escapes control characters; the launcher also searches each arm's output and scratch for
  the canary id; the inventory adds `render_quoted` and `print_measure`. No criterion changed.
- rev-7 · 2026-09-14 · S4 · AC7 · folded the closing diff review's round-1 L4. The classifier read a
  driver call's slug as `[A-Za-z][A-Za-z0-9]{1,63}`, where the driver's `check_slug_shape`, and
  hygiene check 4 with it, admit a letter then letters, digits or dashes. So `--discover --slug
  my-build` and the model's store fallback never attributed a session to a dashed or single-letter
  slug the driver had accepted, and such a run read `not-local` for its transcripts. The grammar is
  now one constant in `runlog_lib`, spelled the driver's way, and AC7 grades it against the driver's
  own function. The 64-character bound goes with the old spelling: the slug is a store field and
  never a path, and the driver bounds none.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "parse Claude Code session transcripts"` returned only
name-stem matches on `parse`. No committed tool reads `~/.claude/projects`, so no existing seam fits.
The rules are the ones the transcript and platform readers measured and the cold review corrected.
The acquisition probe consolidated them into a contract, with per-rule evidence, in the design research
record. The prototype that measured them is not committed.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

# TOOL-dLoggedFlight-6 — the transcript extractor: a run's action sequence, owner turns and cost

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The driver's lines cover about 8% of a run's calls. The rest of the action sequence, every owner turn,
the compactions, the limits and the token cost are recorded only in Claude Code's session transcripts
on the machine that ran the build. Extract them into a structural, free-text-free event list, streamed
at over 100 MB/s, located through the session ids the driver recorded, and kept under the user profile.

## 2. Scope (IN)

- **S1** Locating a run's sessions: the validated session ids from `driver.log` START lines for the
  slug, each found with one glob of `<projects-root>/*/<sid>.jsonl`. The projects root is
  `$CLAUDE_CONFIG_DIR/projects`, else `~/.claude/projects`, overridable by `--transcripts <dir>`. A
  session id is used as a path component only after it matches the UUID shape. Observed by AC1.
- **S2** A streaming reader over the main file, `<sid>/subagents/**/agent-*.jsonl` with its
  `.meta.json`, and `<sid>/workflows/wf_*.json`. It dedupes by `uuid` keeping the FIRST copy, since
  later copies were measured to carry empty output, and sorts by timestamp with the file line as a
  tiebreak. Observed by AC2.
- **S3** Events, each with its source fields as `memory/builds/dLoggedFlight/build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md`
  and the acquisition record describe them. Observed by AC2, AC3 and AC4. The events are:
  - tool calls, with the tool name, a class and flags, times, `is_error` and the `Exit code N` rc;
  - the end of a background or async call, taken from the first record carrying its `<tool-use-id>`;
  - owner turns, as the union of human- or null-origin typed records, `queued_command` attachments of
    human origin, and interrupts, without the two `<local-command-…>` echoes;
  - keepalive fires, joined to a same-session `CronCreate` prompt rather than matched by wording;
  - compactions, API errors, session limits, hook denials, workflow runs and agent spawns;
  - token usage, deduplicated by `requestId` and split into main loop, direct agents and workflow agents.
- **S4** No free text is persisted: no command text, no narration, no owner-turn text, no tool output.
  A tool call keeps only its class and flags. The classes are driver verb (verb and slug), git
  commit, merge or push, bar run, test, read, write, edit, workflow, agent, cron and ask. The flags
  are destructive git and a piped driver call. Workflow and agent labels are kept only when they
  match `^[A-Za-z0-9._:-]{1,64}$`. Observed by AC3.
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
- **S8** Performance: the largest local session tree is extracted at over 100 MB/s with peak working
  memory under 64 MB. Observed by AC8.

## 3. Non-goals (OUT)

- Persisting narration. The owner's split puts extracts under the user profile, and on node `d`
  `%LOCALAPPDATA%` is readable by the local sandbox group. With no free text persisted, that ACL
  exposes structure only. §4 records the measurement.
- Transcripts from other harnesses. This module is the Claude Code adapter and says so.
- The owner-turn position classes (launch, pre-run, in-window, post-close). They need a run window,
  and the run model owns them.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the reader, for session ids in `driver.log`.
- **consumes-from** `TOOL-dLoggedFlight-5` — the redaction table, for classification and narration.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins these events into a run's timeline.
- **hands-off** `TOOL-dLoggedFlight-12` — the question-answering skill prints narration through S6.

## 4. Design

The reader holds compact tuples rather than whole records. The acquisition probe's streaming
prototype ran 258.5 M characters in 1.341 s at a peak working set of 26.4 MB, against 116.8 MB for a
hold-everything reader. Both figures were measured on 2026-09-13 (PINNED). A tool call's class is
decided from its command text in memory, and the text is then dropped.

Five sessions on node `d` live under a project dir other than their first cwd, cause UNVERIFIED. The
glob by session id finds them, and a dir predicted from the repo path would not.

### Data model

One JSON object per session: `{schema: 1, sid, tree_bytes, engine_versions, coverage: {records,
unknown_types, dup_uuids}, events: [...]}`. An event is `{t, kind, ...}`, with `kind` one of `tool`,
`tool_end`, `owner`, `keepalive`, `compact`, `api_error`, `limit`, `denial`, `workflow`, `agent` and
`usage`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/extract.py` | module | none |
| `resolve_session_tree`, `read_records`, `extract_session`, `build_usage`, `scan_owner_turns`, `extract_narration`, `resolve_state_dir` | functions | `py.function`, verb-led |
| `cmd_extract`, `cmd_narration` | CLI subcommands | reserved `cmd` |

### Files touched (estimate)

`tools/runlog/{extract.py,runlog.py,selftest.py,README.md}`, and small synthetic transcript fixtures
under `tools/runlog/fixtures/` with a `.json` or `.txt` extension, never `.jsonl`.

### Alternatives rejected

- Persisting redacted narration: rejected by the ACL measurement above and by the owner's reason for
  the split.
- Keyword-matched keepalive fires: rejected, since the wording drifted three ways and the prefix found
  73 of 86 fires, where the join found 86 of 86.

## 5. Production-readiness checklist

- security — session ids are shape-checked before any path use, and every constructed path is
  contained under its root. Transcript text is data. Nothing free-text is persisted.
- perf / scale — streaming, over 100 MB/s, under 64 MB. The whole node is about 3.8 GB, roughly 30 s
  in one process (INFERRED).
- error / empty / loading states — a missing session tree, an in-flight workflow with no `wf_*.json`,
  an unknown record type and a torn line each land in the coverage block, never an exception.
- observability — the coverage block counts records, unknown types and duplicates per session.
- risks — the transcript format is not a contract. Eight engine versions appeared in one month, so
  unknown keys are tolerated and every rule names its evidence.
- testing — synthetic fixtures for each rule, plus one measured run over the largest local tree.
- migration — none.
- user docs — the kit README's extractor section.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names
another command.

- **AC1** — When `driver.log` names a session id holding `../`, the extractor refuses that id and
  writes nothing outside its store, and a valid id finds its tree through the glob.
  Red when: the id reaches a path unvalidated.
- **AC2** — When a fixture holds a duplicated `uuid` whose later copy has empty stdout, and records
  out of timestamp order, the extracted tool call keeps the first copy's rc and the events come out
  sorted.
  Red when: the last copy wins or the order is file order.
- **AC3** — When a fixture's owner-turn set is one human record, one null-origin `/compact`, one
  absorbed `queued_command`, one interrupt, one keepalive fire and one `<local-command-…>` echo, the
  extractor reports four owner turns and one keepalive. The written extract contains none of the
  fixture's free-text strings.
  Red when: the echo counts as a turn, the keepalive counts as one, or any fixture sentence appears
  in the output file.
- **AC4** — When `extract_session` reads a fixture holding a background Bash call whose notification arrives later as a queue
  enqueue, the call's end time is the enqueue's timestamp, not the launch acknowledgement's.
  Red when: the duration reads about 0.1 s.
- **AC5** — When `python <kit>/runlog.py extract --session <sid>` runs from two different worktrees of
  this clone, both write under the same `<repo-key>`.
  Red when: the key is derived from the worktree path.
- **AC6** — When `narration` prints a window whose text holds a planted credential, the output holds
  `<redacted:` and the data banner, and the store directory is unchanged.
  Red when: narration is written to disk or printed unredacted.
- **AC7** — When `--discover` runs over a fixture session holding `unattended.sh --preflight tFixture`,
  it attributes that session to `tFixture` with `attribution=heuristic`.
  Red when: discovery attributes a session whose only mention is inside tool output.
- **AC8** — When the extractor runs over the largest local session tree on node `d`, it reports its
  rate and peak working memory, over 100 MB/s and under 64 MB.
  Red when: a hold-everything reader returns.
  fixture: the largest local tree on the node running the build; the arm names it by size, never by id.
  figure: both floors are PINNED.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each rule staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** Should a run's extracts be kept after the transcripts are cleaned up? RESOLVED (agent,
  2026-09-13, delegated): yes. They carry no free text, the owner raised transcript retention to 365
  days in the single turn, and deleting them would discard the only copy once the transcript expires.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "parse Claude Code session transcripts"` returned only
name-stem matches on `parse`. No committed tool reads `~/.claude/projects`, so no existing seam fits.
The rules are the ones the transcript and platform readers measured and the cold review corrected.
The acquisition probe consolidated them into a contract, with per-rule evidence, in the design research
record. The prototype that measured them is not committed.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

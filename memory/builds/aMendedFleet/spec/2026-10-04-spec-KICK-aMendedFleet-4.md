# KICK-aMendedFleet-4 — the orientation card notes a PATH CLI older than the running session

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams kickoff · ratified 2026-10-04 · order 96

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The session that launched this build runs Claude Code 2.1.286 while `claude` on PATH on node a is
2.1.178, and nothing a session reads says so. Every headless session started from PATH, the resume
tick's included, runs the older CLI. Unit 61 pins the launching version at `--preflight` and compares
it on resume, which only an unattended run reaches. This unit puts the comparison on the orientation
card, which every session gets at start: one `cli —` cell comparing PATH `claude --version` with the
running session's version, read from `AI_AGENT` by the rule unit 61 states, and a `NOTE` when PATH is
the older of the two.

## 2. Scope (IN)

- **S1** — THE SESSION VERSION. `derive_cli_line` in `skills/session-kickoff/manifest-check.sh`
  reads `AI_AGENT`. When the value opens with `claude-code_`, it takes the field between the first
  and second underscore, turns its dashes into dots, and accepts the result only when it is two to
  four dot-separated integers. That is unit 61's S1 rule, spelled again here because the kickoff
  engine names no file of the unattended kit. Anything else, an unset variable included, is no
  session version. Observed by AC1 and AC2.
- **S2** — THE PATH VERSION. `command -v claude` finds the binary; the read is
  `timeout -k 2 "$CARD_CLI_BOUND" claude --version`, stdin from `/dev/null`, stdout written to a
  scratch file under `CARD_DIR` that is read and then unlinked, never captured by a command
  substitution. The version is the first token of its first line that is two to four dot-separated
  integers. `CARD_CLI_BOUND` defaults to 5 seconds and is an environment override for the self-test,
  like `CARD_CAP_BYTES`, not an adopter knob. Observed by AC1, AC3 and AC4.
- **S3** — THE COMPARISON AND THE CELL. The two versions compare field by field as integers, a missing
  field reading as 0, and the cell is exactly one of these lines:
  `cli — <v> · PATH claude matches this session`;
  `cli — NOTE: PATH claude <p> is older than this session's <s>, so a session started from PATH runs the older CLI`;
  `cli — PATH claude <p> is newer than this session's <s>`;
  `cli — skipped: <why>`, where the reason is one of: AI_AGENT names no Claude Code version, no claude
  on PATH, claude --version did not answer within the bound, or claude --version printed no version.
  The card's exit status never moves. Observed by AC1, AC2, AC3 and AC4.
- **S4** — THE PLACE. `render_card` prints the cell directly after the `node —` cell, inside the
  startup part `CARD_PARTS_AWK` reads, and nowhere else; `--card --replay` prints the stored card and
  re-reads nothing. Observed by AC1.
- **S5** — The comment block above `render_card` names the cell, and the map dossier
  `memory/map/features/session-kickoff.md` gains one sentence on it. Observed by AC5.
- **S6** — Arms in `skills/session-kickoff/manifest-check.test.sh`: a stub `claude` on PATH under
  four `AI_AGENT` values, an unset one, no `claude` on PATH, and a stub that outlives a one-second
  bound. NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are
  declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Any refusal. A version difference is a fact the card states, never a reason to stop a session.
- Updating the CLI on node a, which this build parks as an owner act.
- Calling unit 61's `read_cli_version` through the unattended driver. A driver start costs about
  2.3 s on node a, and the engine names no file of another kit; S1 spells the same rule and AC2
  observes it on unit 61's own values.
- An authored minimum CLI version. The report rejected it in favour of the running session's own.
- Re-reading on `--card --replay`, which prints the session-start card as stored.
- Any edit to `skills/session-kickoff/SKILL.md`, which is at its byte cap and needs none.
- Bumping the kickoff kit version, owed once at the build's close.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `skills/session-kickoff/` is byte-identical at the worktree tip `8312d315`.

- This session's tool shell carries `AI_AGENT=claude-code_2-1-286_agent`, and `claude --version` on
  PATH prints `2.1.178 (Claude Code)`. The read took 0.17 s wall, and 0.19 s under `timeout -k 2 5`,
  on node a. PINNED 2026-10-04.
- Unit 61's spec reads the session's version from `AI_AGENT` by the rule S1 copies, and records that
  the PATH binary sets `AI_AGENT` from its own version when the variable is unset or already Claude
  Code's, so a session launched from PATH overwrites any inherited value. Its Non-goals hand this
  card note to this unit.
- That the SessionStart hook's environment carries `AI_AGENT` is UNVERIFIED: the hook is a child of
  the session process like the tool shell that showed it, and S3's `skipped:` line is what a hook
  without it prints.
- `git grep` for `claude --version` and for `AI_AGENT` over `tools/`, `skills/`, `.claude/` and
  `.githooks/` finds nothing at base.
- `render_card` prints `orientation —`, `node —`, `tree —`, `worktrees —`, `live —`, `recent —` and
  `READY —`. Unit 76 adds its `drift —` cell and unit 77 its `overlaps —` cell after `worktrees —`, so
  a cell after `node —` is a separate hunk from both.
- The startup card is capped at `CARD_CAP_BYTES`, 8192, and the longest S3 line is about 150 bytes.
- The self-test's AC2 arm reads each cell by its prefix with `read_cell`, so a new cell moves no
  existing arm.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_cli_line` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest derive_cli_line --as sh.function` answered OK |
| `CARD_CLI_BOUND` | card constant | not graded |
| `cli —` | card cell | none |

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/map/features/session-kickoff.md`

### Alternatives rejected

- **Read the session version from `CLAUDE_CODE_EXECPATH`.** It is a path whose layout differs by
  installer; `AI_AGENT` is the value unit 61 reads, and one rule in two kits beats two rules.
- **Print the cell only when PATH is older.** A clean answer would then read the same as a card that
  never ran the read, which is the could-not-fail shape; the matching and skipped lines say which.
- **A command substitution around `claude --version`.** A child that keeps the stdout pipe open holds
  the substitution past the bound, the trap this repository recorded for backgrounded jobs.

## 5. Production-readiness checklist

- security — runs the `claude` that PATH resolves with one fixed flag and prints its first version
  token; nothing read is evaluated, and the scratch file is under the git dir and unlinked.
- perf / scale — one spawn of about 0.2 s on node a, bounded at 5 s.
- error / empty / loading states — the four `skipped:` reasons in S3; none changes the card's exit.
- observability — the cell always prints, so a clean answer reads differently from no answer.
- risks — a host whose PATH CLI is a different install than the session's reports NOTE or newer
  correctly; a wrapper script named `claude` that prints no version reads as skipped.
- testing — AC1 to AC5 here; the arms in S6.
- migration — N/A — a new cell; nothing stored changes shape.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When, in a clone of the unit's tip under a short `%TEMP%` path, a stub `claude` that prints
  `2.1.178 (Claude Code)` is first on PATH, `AI_AGENT=claude-code_2-1-286_agent` is exported, and
  `bash skills/session-kickoff/manifest-check.sh --card --write --session k4a` runs, the line after
  `node —` reads `cli — NOTE: PATH claude 2.1.178 is older than this session's 2.1.286`, followed by
  the clause S3 fixes; with `AI_AGENT=claude-code_2-1-99_harness` under a new session id, it reads
  `cli — PATH claude 2.1.178 is newer than this session's 2.1.99`.
  Red when: the comparison is a string comparison, which orders `2.1.99` after `2.1.178` and prints a
  NOTE for the newer PATH, or the cell is missing or lands after `worktrees —`.
  cost: under a minute on node a; the clone is the only thing written.
- **AC2** — When the same clone's card is written with `AI_AGENT=claude-code_2-1-178_agent`, with
  `AI_AGENT=claude-code_2-1-290_harness`, with `AI_AGENT` unset and with `AI_AGENT=claude-code_x_agent`,
  each under its own session id, the cells read, in that order, `cli — 2.1.178 · PATH claude matches this session`,
  the NOTE naming `2.1.178` and `2.1.290`, and twice
  `cli — skipped: AI_AGENT names no Claude Code version`. With AC1's two, these version fields
  are the four unit 61's AC1, AC2 and AC4 pin for its own reader, so the two kits' spellings of one
  rule are observed on one set.
  Red when: a non-numeric field is accepted as a version, an unset variable prints a comparison, or
  equal versions print a NOTE.
- **AC3** — When `CARD_CLI_BOUND=1` is exported and the stub `claude` sleeps ten seconds before
  answering, the card write exits 0 within about four seconds and the cell reads
  `cli — skipped: claude --version did not answer within 1s`.
  Red when: a hung `claude` holds the session start, or a fired bound reads as a comparison.
- **AC4** — When the card is written with PATH holding no `claude`, the cell reads
  `cli — skipped: no claude on PATH`; and when the stub prints `Claude Code` and no number, it reads
  `cli — skipped: claude --version printed no version`.
  Red when: an absent or unparseable PATH CLI reads as matching the session.
  fixture: PATH set to the clone's stub directory plus the directories that hold `git`, `awk` and
  `sed`, without the user's `~/.local/bin`.
- **AC5** — When `grep -n "cli —" memory/map/features/session-kickoff.md` and
  `grep -n "cli —" skills/session-kickoff/manifest-check.sh` run, the first hits the new sentence and
  the second hits both the comment block and `derive_cli_line`; and
  `grep -n "tools/unattended" skills/session-kickoff/manifest-check.sh` prints nothing.
  Red when: a cell ships that its dossier or comment never names, or the engine spells another kit's
  path.

No new refusal or gate clause is added, so nothing here is observed RED on a staged break; each
`Red when:` names the break the fixture's own output shows.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `skills/session-kickoff/manifest-check.test.sh` · covers AC1 to AC4 · a stub `claude` on PATH under four `AI_AGENT` values and an unset one, no `claude` on PATH, and a stub that outlives a one-second bound, staged red by swapping the integer comparison for a string one · none

## 8. Open questions

- **F1** — Where does the session's version come from?
  Options: `AI_AGENT`, as unit 61 reads it; `CLAUDE_CODE_EXECPATH`; calling the unattended driver. The
  second depends on an installer's directory layout, and the third costs a driver start and names
  another kit's file from the engine.
  RESOLVED (agent, 2026-10-04, delegated): `AI_AGENT` by unit 61's rule, spelled in the engine, per S1.
- **F2** — Does the cell print when the versions match?
  Options: always one line; only the NOTE. A NOTE-only cell makes a clean read and a read that never
  ran the same bytes.
  RESOLVED (agent, 2026-10-04, delegated): always one line, per S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; split from unit 77 at its F1, from unit 61's version rule and a
  timed `claude --version` read on node a.
- rev-2 · 2026-10-04 · §4 · Files touched named `memory/map/generated/symbols.json`, which
  enumerates Python and JavaScript definitions only; `derive_cli_line` is shell, and
  `KICK-aMendedFleet-1`, adding a shell function to the same engine, declares no such write.

## 10. Reuse audit

No existing seam fits: `git grep` for `claude --version` and `AI_AGENT` over `tools/`, `skills/`,
`.claude/` and `.githooks/` found nothing at base, and the one reader that will exist, unit 61's
`read_cli_version`, lives in the unattended driver, which the kickoff engine may not name. The seams
extended are `render_card`'s cell list and the bounded-read shape unit 77's spec gives its
`overlaps —` cell. `python tools/codebase-map/reuse_lookup.py "compare the PATH claude CLI version
with the running session's version"` returned runlog's `extract_session` and `resolve_session_tree`
by name stem, neither of which reads a version, and it prints `unscanned layers: .sh`, so the
`git grep` above was the shell probe. Recall returned unit 61's spec, whose S1 rule this spells,
`KICK-aReplayedCard-1`, the card's design record, and `TOOL-aReplayedCard-7`, the card's spawn cost.
Where the report and the tree disagree: the report put this note beside the overlap line in one card
item; unit 77 split it here, and nothing in the tree reads either version today.

Recall terms used: `python tools/memory-recall/query.py "should the session card warn when the claude
CLI on PATH is older than the session that is running" --terms "orientation card PATH CLI version
claude --version AI_AGENT stale CLI resume tick session start NOTE"`

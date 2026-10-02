# Build brief — TOOL-aRepatriatedFork-53

**Serves:** journal TOOL-aRepatriatedFork-53

A unit pass under the aRepatriatedFork mandate, adopted at VERIFYING by the owner on 2026-10-01. Build `memory/builds/aRepatriatedFork/spec/2026-10-01-spec-TOOL-aRepatriatedFork-53.md` exactly: two driver verbs register and release a background task with an absolute heartbeat path in a per-slug sidecar, `--audit` grades every open task against `TASK_STALL_BOUND` and says so when none is registered, and the idle-wake's instructions act on a STALLED task. The red-first control is the `56c7befa` driver, which refuses `--register-task` as an unknown verb and prints no task line.

## How to build this unit

The spec is the scope. Its section 8 forks are RESOLVED (agent, 2026-10-01, delegated) under the
mandate; do not reopen them. Sequenced first of the three adopted units: `TOOL-aRepatriatedFork-52`
consumes this unit's verb and audit line.

- **Spec before code.** The spec is already committed. If building shows the spec must change, commit
  that change FIRST as a records commit (rev bump plus a section 9 line naming what moved), then the
  code. The pass-order leg (`bash tools/unattended/check-pass-order.sh`) must stay green.
- **Names first.** Confirm each minted name with `python tools/lexicon/lexicon.py --suggest <name>`
  before writing it; a rename is a rev bump on the spec first.
- **No bar and no whole suite inside the pass.** `tools/unattended/unattended.test.sh` costs over an
  hour: SLICE it, its prologue plus the new block, in a temporary script inside the kit dir. A
  red-first observation is owed for every new arm: stage the `56c7befa` driver, see the arm fail,
  restore.
- **Never wait on a multi-hour run.** If a check you need is long, run it in the background, keep
  working, and read its output file when it finishes. Kill anything whose verdict is already decided.
- **Heartbeat.** Append one line, ISO time and what you are doing, to
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-arepatriated-fork-build-e42158/3b534792-4ade-4a9d-8dfa-4cb264c0af0d/scratchpad/TOOL-aRepatriatedFork-53-heartbeat.txt`
  about every 30 minutes, and at every commit.
- **Commit each verified step as you go**, each on its own once its direct check is green: the verbs
  and the audit, then the templates and their renders, then the conf declarations and the version
  bump. Do not hold a working tree across hours.
- **Leave these green** before committing, each by its own command: `bash tools/unattended/adopt-unattended.sh --check`,
  `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md`, `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py epoch --base 56c7befa`, `python tools/govkit/govkit.py selfcheck`,
  `python tools/lexicon/lexicon.py`, `python3 tools/memory-recall/test_recall_floor.py`,
  `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gen_build_index.py --check`
  and `--check-format`, `bash skills/session-kickoff/manifest-check.sh`, `bash tools/unattended/check-pass-order.sh`.
  A kit whose shipped bytes move takes its version bump in EVERY carrier. A staged watched file owes a
  `last-audit` re-stamp and a `Manifest delta:` line.
- **Windows traps.** Working copies may be CRLF: edit with the Edit tool or binary-mode Python, never a
  text-mode rewrite of a `.sh`. Author scripts with the Write tool, never a bash heredoc carrying a
  backslash. Never `python -` without input. Scratch clones via `mktemp -d`, never a fixed name.
- **Commit** with the unit id in the subject, a `Decided: <choice> — <why>` trailer per choice, and
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` last. Never `--no-verify`. No merge, no push.

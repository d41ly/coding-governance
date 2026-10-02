# Build brief — TOOL-aRepatriatedFork-54

**Serves:** journal TOOL-aRepatriatedFork-54

A unit pass under the aRepatriatedFork mandate, adopted at VERIFYING after repair pass R2. Build `memory/builds/aRepatriatedFork/spec/2026-10-01-spec-TOOL-aRepatriatedFork-54.md` exactly: `check-playbook-parity.sh` takes its kit population from govkit's registry rather than a listing of the tool root, and `check-spec-tokens.py` grades a bare file name at a repo-root install, resolving it as a tracked path or the basename of one. The red-first controls are the `56c7befa` copies of both gates staged into the new root-install arms: the parity gate reds naming `.claude`, and the spec-tokens arm for the untracked `nope.sh` stays green.

## How to build this unit

The spec is the scope. Its section 8 forks are RESOLVED (agent, 2026-10-01, delegated) under the
mandate; do not reopen them. Sequenced second of the three adopted units: `TOOL-aRepatriatedFork-52`'s
leg reds at the root without this unit.

- **Spec before code.** The spec is already committed. If building shows the spec must change, commit
  that change FIRST as a records commit (rev bump plus a section 9 line naming what moved), then the
  code. The pass-order leg (`bash tools/unattended/check-pass-order.sh`) must stay green.
- **Measure before and after.** Record the parity gate's kit count and the spec-tokens graded count at
  `56c7befa` on the real tree before editing; AC1 and AC6 compare against them.
- **Fixtures declare their kits.** The parity suite's existing arms plant kit directories; with the
  registry derivation, each fixture's registry must declare the kit its arm plants, or the arm passes
  for the wrong reason. Check every existing arm still reds for its own reason.
- **No bar and no whole suite inside the pass.** Verify with the direct checks section 6 names. A
  suite is SLICED: its prologue plus the block you changed, in a temporary script inside the kit dir.
  To grade an arm at a root install, run that slice in a `mktemp -d` clone with the tool root moved to
  the repository root. A red-first observation is owed for every new arm: stage the break, see it
  fail, restore.
- **Never wait on a multi-hour run.** If a check you need is long, run it in the background, keep
  working, and read its output file when it finishes. Kill anything whose verdict is already decided.
- **Heartbeat.** Append one line, ISO time and what you are doing, to
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-arepatriated-fork-build-e42158/3b534792-4ade-4a9d-8dfa-4cb264c0af0d/scratchpad/TOOL-aRepatriatedFork-54-heartbeat.txt`
  about every 30 minutes, and at every commit.
- **Commit each verified step as you go**: the parity gate with its arms, then the spec-tokens checker
  with its arms. Do not hold a working tree across hours.
- **Leave these green** before committing, each by its own command: `bash tools/check-playbook-parity.sh`,
  `python tools/check-spec-tokens.py`, `bash tools/check-testsuite-counts.sh`, `python tools/lexicon/lexicon.py`,
  `python tools/govkit/govkit.py selfcheck`, `bash tools/memory-tree/check-memory-hygiene.sh`,
  `python tools/memory-tree/gen_build_index.py --check` and `--check-format`,
  `bash skills/session-kickoff/manifest-check.sh`, `bash tools/unattended/check-pass-order.sh`.
  A staged watched file owes a `last-audit` re-stamp and a `Manifest delta:` line.
- **Windows traps.** Working copies may be CRLF: edit with the Edit tool or binary-mode Python, never a
  text-mode rewrite of a `.sh`. Author scripts with the Write tool, never a bash heredoc carrying a
  backslash. Never `python -` without input. Scratch clones via `mktemp -d`, never a fixed name.
- **Commit** with the unit id in the subject, a `Decided: <choice> — <why>` trailer per choice, and
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` last. Never `--no-verify`. No merge, no push.

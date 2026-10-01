# Build brief — TOOL-aRepatriatedFork-52

**Serves:** journal TOOL-aRepatriatedFork-52

A unit pass under the aRepatriatedFork mandate, adopted at VERIFYING by the owner on 2026-10-01. Build `memory/builds/aRepatriatedFork/spec/2026-10-01-spec-TOOL-aRepatriatedFork-52.md` exactly: every suite honours `FOREIGN_PREFIX_PROBE=1` by running its prologue and one subject-touching arm, and the foreign-prefix leg runs that probe at `scripts/`, `vendor/gov/` and the root with no calibrate pass, gov's declarations re-spelled at each move, the bar's own gate-run record as its baseline, one line per suite, a declared whole-run list, and a stop at the first red prefix. The red-first control is `TOOL-aRepatriatedFork-30`'s: one suite given back a literal `tools/` in a scratch clone must red at `scripts/`.

## How to build this unit

The spec is the scope. Its section 8 forks are RESOLVED (agent, 2026-10-01, delegated) under the
mandate; do not reopen them. Sequenced last of the three adopted units: it consumes
`TOOL-aRepatriatedFork-53`'s task registration and `TOOL-aRepatriatedFork-54`'s root-install gates,
so both must be CLOSED before this pass starts.

- **Spec before code.** The spec is already committed. If building shows the spec must change, commit
  that change FIRST as a records commit (rev bump plus a section 9 line naming what moved), then the
  code. The pass-order leg (`bash tools/unattended/check-pass-order.sh`) must stay green.
- **The re-declaration is R2's.** The VERIFYING repair pass kept its working patch outside the tree at
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-arepatriated-fork-build-e42158/3b534792-4ade-4a9d-8dfa-4cb264c0af0d/scratchpad/tool52-redeclare.patch`.
  Read it as the starting point for S4; the spec, not the patch, is the scope.
- **The probe site, suite by suite.** Do the shared harness first, then each kit's suites, committing
  per kit with that kit's version bump. In each suite put the stop after the first arm that runs the
  subject, not merely the first verdict. A suite you cannot separate goes on the leg's declared
  whole-run list with its reason; do not leave it to be discovered.
- **No bar and no whole suite inside the pass, and never the leg whole.** AC10's full run is the main
  loop's. Observe AC1, AC3, AC4 and AC6 with `--kit` slices in `mktemp -d` clones, and AC2 by running
  one suite with and without the flag. A red-first observation is owed for every new arm.
- **Never wait on a multi-hour run.** If a check you need is long, run it in the background, keep
  working, and read its output file when it finishes. Kill anything whose verdict is already decided,
  by command line, since a stopped task can leave its children running.
- **Heartbeat.** Append one line, ISO time and what you are doing, to
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-arepatriated-fork-build-e42158/3b534792-4ade-4a9d-8dfa-4cb264c0af0d/scratchpad/TOOL-aRepatriatedFork-52-heartbeat.txt`
  about every 30 minutes, and at every commit.
- **Commit each verified step as you go.** Do not hold a working tree across hours; this unit's write
  set is wide, and a commit per kit keeps each step reviewable.
- **Leave these green** before committing, each by its own command: `bash tools/run-gates/run-selftests.sh --check`,
  `python tools/run-gates/derive-ceilings.py --check`, `bash tools/check-testsuite-counts.sh`,
  `bash tools/check-install-prefix.sh`, `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py epoch --base 56c7befa`, `python tools/govkit/govkit.py selfcheck`,
  `python tools/lexicon/lexicon.py`, `python3 tools/memory-tree/check-arms.py --check`,
  `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gen_build_index.py --check`
  and `--check-format`, `bash skills/session-kickoff/manifest-check.sh`, `bash tools/unattended/check-pass-order.sh`.
  A kit whose shipped bytes move takes its version bump in EVERY carrier. A staged watched file owes a
  `last-audit` re-stamp and a `Manifest delta:` line.
- **Windows traps.** Working copies may be CRLF: edit with the Edit tool or binary-mode Python, never a
  text-mode rewrite of a `.sh`. Author scripts with the Write tool, never a bash heredoc carrying a
  backslash. Never `python -` without input. Scratch clones via `mktemp -d`, never a fixed name.
- **Commit** with the unit id in the subject, a `Decided: <choice> — <why>` trailer per choice, and
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` last. Never `--no-verify`. No merge, no push.

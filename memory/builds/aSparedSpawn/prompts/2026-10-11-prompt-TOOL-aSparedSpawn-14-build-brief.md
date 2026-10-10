# Build brief — TOOL-aSparedSpawn-14

**Serves:** journal TOOL-aSparedSpawn-14

Unit 15 of 15 in roster order (1, 2, 5, 6, 8, 10, 11, 15, 3, 4, 7, 9, 12, 13, 14), built one at a time in the worktree
`C:/projects/coding-governance/.claude/worktrees/gate-runner-profiling-optimization-5d1f1e`, which
holds the run. The units before this one are already committed there; read `git log --oneline -20`
first and build on what they changed rather than on the spec's line numbers, which are at base
`22efab65`.

FAST DIFF-SCOPED CHECKS ONLY, NOTHING HELD. No merge bar, no `*.test.sh` suite run whole, no held
leg, no `GATE_FULL=` or `GATE_SELFTESTS=` prefix. Observe each acceptance criterion with the
smallest direct check that can fail: the checker run on a staged break, a `--selftest` flag, a
fixture, or ONE suite arm sliced into a temporary script (the suite's prologue plus that one block,
written inside the kit directory so relative paths hold, DELETED before you commit). Run checks one
at a time, never concurrently. A criterion only a whole suite or the bar can observe is named in your
summary and in the ledger as owed at VERIFYING; the main loop runs the bar once after the last unit.

The spec at `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md` is the design,
and its section 8 `RESOLVED (owner, 2026-10-10)` lines are the owner's rulings and bind. Where the code
forces a divergence, bump the spec to the next rev with a section 9 line in its own commit BEFORE the
code commit; never put spec and code in one commit (the pass-order leg reds it).

Rules that cost earlier builds a cycle each:
- Do NOT bump any kit version marker and do NOT run `govkit.py mint` or `epoch`: the main loop bumps
  every moved kit once, after the last unit.
- `--dispatch` declares only files this pass itself writes, plus this build's README and
  `memory/map/generated/symbols.json` when you add or rename a shell or python function. Never declare
  `memory/LIVE.md` or `memory/ledger/*`. Give a many-path `--dispatch` a 600000 ms timeout.
- A new or renamed shell function stales `symbols.json`: run
  `python tools/codebase-map/gen_map.py --write` before the commit. A slice file left under `tools/`
  pollutes it too.
- New function and variable names, and comments in `.py` files, are graded by the lexicon leg: run
  `python tools/lexicon/lexicon.py --suggest <name>` for any new function name.
- A refusal message an arm asserts is matched WHOLE; never truncate one with `${x%% *}`.
- Author files with the Write and Edit tools, never a heredoc or `python -c` carrying backslashes;
  this working copy holds CRLF on some files, so a multi-line Python `str.replace` may match nothing.
- Never kill a process this pass did not start, whatever its command line says.

Write the acceptance ledger for this unit at
`memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md`, in the
shape of `memory/builds/aMeteredSweep/build/2026-10-09-build-TOOL-aMeteredSweep-1-acceptance-ledger.md`:
a `**Serves:** journal TOOL-aSparedSpawn-14` line, then one `**Evidences:** TOOL-aSparedSpawn-14`
block holding one `- ACn — <check> — <what was observed>` line per criterion, each naming the
backticked check that ran and stating plainly when a criterion is owed at VERIFYING instead.
It rides the pass commit, which also sets the spec's status header to CLOSED.

# Build brief — TOOL-aSparedSpawn-18

**Serves:** journal TOOL-aSparedSpawn-18

Closing-review unit (18 of the promotions 17, 18, 19, 16), built one at a time in the worktree
`C:/projects/coding-governance/.claude/worktrees/gate-runner-profiling-optimization-5d1f1e`, which
holds the run. The units before this one are already committed there; read `git log --oneline -20`
first and build on what they changed rather than on the spec's line numbers, which are at base
`22efab65`.

NO SELF-TEST IN A PASS, IN ANY FORM. No merge bar, no `*.test.sh` suite, no held leg, no
`GATE_FULL=` or `GATE_SELFTESTS=` prefix, AND NO SLICE OF A SUITE: a suite's prologue copied into
another file with one arm is the same suite under a different name, and on this host one such slice
of `tools/unattended/unattended.test.sh` costs 7 to 10 minutes. (An earlier version of this brief
allowed slices; that was the main loop's error, withdrawn 2026-10-11.) Per `memory/guides/BUILD-METHOD.md`
M6, a pass verifies with the direct check its acceptance names: a checker run on a staged break, a
`--selftest` flag, a fixture you build by hand in the scratch root, or the changed program invoked
directly once. A criterion only a suite arm can observe is NOT run in the pass: write the new or
changed arm, check it with `bash -n` and by reading it, and record it in the ledger as owed at
VERIFYING, where the main loop runs the suites once after the last unit.

The spec at `memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-18.md` is the design,
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
  `python tools/codebase-map/gen_map.py --write` before the commit.
- New function and variable names, and comments in `.py` files, are graded by the lexicon leg: run
  `python tools/lexicon/lexicon.py --suggest <name>` for any new function name.
- A refusal message an arm asserts is matched WHOLE; never truncate one with `${x%% *}`.
- Author files with the Write and Edit tools, never a heredoc or `python -c` carrying backslashes;
  this working copy holds CRLF on some files, so a multi-line Python `str.replace` may match nothing.
- Never kill a process this pass did not start, whatever its command line says.

Write the acceptance ledger for this unit at
`memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-18-acceptance-ledger.md`, in the
shape of `memory/builds/aMeteredSweep/build/2026-10-09-build-TOOL-aMeteredSweep-1-acceptance-ledger.md`:
a `**Serves:** journal TOOL-aSparedSpawn-18` line, then one `**Evidences:** TOOL-aSparedSpawn-18`
block holding one `- ACn — <check> — <what was observed>` line per criterion, each naming the
backticked check that ran and stating plainly when a criterion is owed at VERIFYING instead.
It rides the pass commit, which also sets the spec's status header to CLOSED.

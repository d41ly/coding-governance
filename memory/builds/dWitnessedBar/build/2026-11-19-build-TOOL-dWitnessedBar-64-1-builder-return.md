**Serves:** journal TOOL-dWitnessedBar-64

# TOOL-dWitnessedBar-64 — builder return 1 (run `wf_18824237-a96`), committed b26061af2

## Why

TOOL-dWitnessedBar-64 is built as spec rev-3 states and committed in pass commit b26061af2, with the spec header set to CLOSED. The spec's claims about current code all held when checked against the tree: read_head_sha, run_seed_cli's no-HEAD route, section 2o's unborn-seed and no-HEAD blocks, both WHAT THIS DOES NOT CHECK clauses, build_ll_seeded, the unit-63 exit-128 case, the three-file population, and the git evidence table, re-probed with git 2.54.0.windows.1. No divergence was found.

## Summary

Pass commit b26061af2 (`Pass: TOOL-dWitnessedBar-64`). It was followed by 82657d2b4 (`Pass: none`), which acts on the M6 checklist: the class ledger-token-wrapped-across-a-line-joins-nothing found two code spans in the acceptance ledger's AC1 line split across a line break, and they are re-wrapped. The base was ed120ffc7.

What changed:
- `read_head_sha` now asks for `HEAD^{commit}` (S1).
- An unborn HEAD now needs two more checks to pass: `git symbolic-ref -q HEAD` gives one `refs/` line and nothing on stderr, and `git for-each-ref <that ref>` prints nothing on either stream (S2).
- Every other case is no sha, with the first stderr line of the probe that stopped the read, or `git <verb> exited <rc>` when it printed nothing (S3).
- The docstring now states this rule and what it does not check.
- The same block was copied byte-for-byte into all three files: tools/lib/legacy_ledger.py, tools/memory-tree/legacy_ledger.py and tools/gate-lint/legacy_ledger.py. A comparison afterwards found the three `legacy_ledger_py` blocks identical.
- In tools/lib/resolve-python.test.sh, section 2o gets a corrupt-HEAD block after the unborn-seed block (S4). It builds four fresh `git init`s, each broken a different way, and runs each through `L.main` using the existing `run_ll_py`. The two WHAT THIS DOES NOT CHECK clauses were rewritten.
- The shell-role row for tools/lib/resolve-python.test.sh was raised from 1245 to the measured 1266, via `ratchet.py widen` (record build/2026-11-21-build-TOOL-dWitnessedBar-64-widen-7.md), as unit 51 F5 (a) does. I declared the two extra paths with `--dispatch` before writing them.
- Also in the pass commit: the acceptance ledger, the status of RUN.md, and the `gen_build_index` output (README, LIVE, backlog/TOOL.md). `gen_map --write` changed nothing, since no function was added.

Checks I ran, which stand in for the `python resolver (behaviour + inline parity + idiom ban)` leg and the new arm's RED-first observation:
- `bash -n` on the suite.
- A probe of the CLI over five scratch `git init`s in %TEMP%/ll64v: one clean and four broken.
  - AC1 holds: all four exit 1 with one `unarmed p no HEAD: <reason>` line and the matching stderr, write no home, and leave no file holding forty 0s or forty 1s. The detached fixture's reason is `git symbolic-ref exited 1`. (DERIVED from the builder's probe)
  - AC2 holds: the clean fixture prints `armed p 2` and HEAD is unborn.
  - AC4 holds: under the stand-in it returns `(None, 'no HEAD: git rev-parse exited 128')`.
- AC3, on scratch copies of the module with each of the three breaks applied:
  - With both new probes removed, every corrupt fixture reads `armed p 2`.
  - With only `for-each-ref` removed, the missing-object fixture reads armed.
  - With `HEAD^{commit}` set back to `HEAD`, the missing-object and detached fixtures stamp the 1111 SHA.
- This also shows the `grep -rl --exclude-dir=.git` check is live: it found the null or dangling SHA in every home it should have.

Owed at the close (not run here):
- New arm: tools/lib/resolve-python.test.sh, section 2o's corrupt-HEAD block, covering AC1 to AC4. It needs to be seen red under its three breaks: both new probes removed, `for-each-ref` removed alone, and `HEAD^{commit}` set back to `HEAD`.
- The legs in spec section 7: the python resolver, shell-hygiene selftest, policy fixtures, memory-hygiene self-test, codebase-map adopter e2e, codebase-map kit selftest, drift-audit selftest, and memory hygiene (including check 23 on the new ledger and the shell-role `never gains` leg).

Decisions recorded in the commit trailer:
- The symbolic-loop fixture writes both branch files, with `other` pointing back. That is how I read the spec's "which points back", and a probe showed that a chain of one file reads as unborn on git 2.54.
- The docstring notes a gap I probed: `for-each-ref` matches by prefix, so an unborn `refs/heads/b` next to an existing `refs/heads/b/x` reads as no HEAD. This is how the specified probe behaves, so I did not change it.

Nothing timed out or was skipped. The changes to help/reference/drive.md and help/reference/units.md in the working tree are not mine and were left unstaged.

Files: C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/lib/legacy_ledger.py, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/lib/resolve-python.test.sh, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-64-1-acceptance-ledger.md

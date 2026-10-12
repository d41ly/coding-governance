# Acceptance ledger — TOOL-aSparedSpawn-33

**Serves:** journal TOOL-aSparedSpawn-33

Node `a`, 2026-10-13, the continuation after the owner's reboot, with a process spawn back near 22 ms.
The first pass committed spec rev-2 at `073513ac8` and was set aside for the reboot; this pass
committed rev-3 alone at `5ffc921b7` and re-observed every criterion below rather than trusting the
first pass. The fixtures are
[2026-10-12-build-TOOL-aSparedSpawn-33-fixtures.sh](2026-10-12-build-TOOL-aSparedSpawn-33-fixtures.sh),
whose repositories push only to a local bare remote through a copy of the real `.githooks/pre-push`,
run once over this tree and once over the code at `5ffc921b7` (the base, unpacked with `git archive`).
No suite, bar or slice ran in this pass.

S1's measured difference, `env` in a plain Git-Bash shell against `env` inside a real pre-push hook
(git 2.54.0.windows.1, `LC_CTYPE` unset in the caller): the hook adds
`GIT_EXEC_PATH=C:/Program Files/Git/mingw64/libexec/git-core`, `GIT_PREFIX=` and `LC_CTYPE=C.UTF-8`,
prepends `/mingw64/libexec/git-core` to PATH and reads each `/bin` of PATH as `/usr/bin`. It also
rewrites `TEMP`, `TMP` and `TMPDIR` to `/tmp`, which no digest name pattern admits, so the view needs
no rule for them. No name outside the §4 table reaches the digest.

**Evidences:** TOOL-aSparedSpawn-33
- AC1 — the fixture's `dg` block, a direct bar then a scoped push through the hook — this tree: the
  push printed `reuse offered to remote and history legs` and `GATE reuse pr`, proven green with
  inputs unchanged; the base: the same push printed `GATE ok    pr`, red. The suite arm in
  `.githooks/pre-push.test.sh` is written, passes `bash -n`, and is owed at VERIFYING.
- AC2 — the fixture's `sv` block, a stub bar copying the view — this tree: a `git -c` push left no
  `GIT_EXEC_PATH`, `GIT_PREFIX`, `GIT_CONFIG_PARAMETERS` or `LC_CTYPE` line, and the view's PATH
  equals the caller's once each `/bin` reads `/usr/bin`; the raw view PATH differed by exactly two
  `/bin` components read as `/usr/bin`. With `LC_CTYPE=en_US.UTF-8` the line stayed. The base wrote
  no view, red. The suite arms are owed at VERIFYING.
- AC3 — the fixture's `dg` block, leg `pa` recording `$GIT_EXEC_PATH` — this tree and the base both:
  `C:/Program Files/Git/mingw64/libexec/git-core`. A staged break adding `unset GIT_EXEC_PATH` to the
  hook beside the view reds it (`unset`) and reds AC1 too. The suite arm is owed at VERIFYING.
- AC4 — the fixture's `sv` block with `GATE_REUSE_DIGEST_ENV` exported — this tree printed
  `pre-push: not honoured from the environment by this bar: GATE_REUSE_DIGEST_ENV`; the base named
  nothing, red. The suite arm is owed at VERIFYING.
- AC5 — the fixture's `ru` block, the runner direct — this tree: `GATE_REUSE=1` with a view file of
  altered lines reused `pa` and `pr`; the push mode keyed on that file executed `pr`; a missing file
  printed `the input keys could not be measured (the toolchain digest)` and reused nothing. The base
  reuses under the env mode too, since it reads no file, so the red is a staged break: the runner's
  file read with its `push` test dropped reds AC5 (`the env mode read the view file`). The evidence
  suite arm is owed at VERIFYING.
- AC6 — `grep -n '^REUSE_SCHEMA=' tools/run-gates/run-gates.sh` — `REUSE_SCHEMA=4`; the
  TOOL-aSparedSpawn-32 merge commit `ba16f0f6d` and the base hold `3`.
- AC7 — `grep -c 'restored' tools/run-gates/README.md` — 1 on this tree, 0 on the base.
- AC8 — `GATE_REUSE_LINEAGE=1 bash tools/run-gates/post-merge.sh`, and the parity arm's sed over
  `_gknobs` — this tree printed `post-merge: not honoured from the environment: GATE_REUSE_LINEAGE`
  and the sed's list holds `GATE_REUSE_LINEAGE` beside `GATE_REUSE`; the base printed no line and
  its list lacks the knob, red.
- AC9 — `check_knob_classes`, `read_hook_const` and `BAR_INERT_KNOBS` lifted verbatim from the suite
  file and run over the runner — 0 lines on this tree; 8 unclassified on the base:
  `GATE_CALIBRATION_RATES`, `GATE_PUSH_BASE`, `GATE_REUSE_DAY`, `GATE_REUSE_LINEAGE`,
  `GATE_REUSE_PUSH`, `GATE_REUSE_SAMPLE`, `GATE_SELFTESTS_MAX_LAG` and `GATE_SPAWN_NOW`. The H49 arm
  itself is owed at VERIFYING.

## Announced gaps

- Every suite arm this unit writes is owed at VERIFYING: the seven in `.githooks/pre-push.test.sh`
  (AC1 to AC4, the pattern comparison and its staged break), the four in
  `tools/run-gates/run-gates.evidence.test.sh`, and the H49 class arm the S8 table feeds.
- `--decide` was checked for a stranded view file and writes none, because the hook never offers
  reuse under `--decide`, so `GATE_REUSE_PUSH` is never exported there.
- The hook's view is removed by one `rm` once the bar returns, an exec on a scoped push that offers
  reuse only; no measured fork row runs such a push.

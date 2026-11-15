**Serves:** journal TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 TOOL-aLightenedLoop-6 TOOL-aLightenedLoop-7

# The new arms observed at the close: each red on its staged break, green restored

The main loop observed these at the close, after every unit was terminal, on `62c1a4ea4`, as BUILD-METHOD
M8 owes (`doc.build-method#m8-closing-the-build`). The owner chose the scope at the close: "Fast suites
only". So every `New arm:` line in a suite other than `tools/unattended/unattended.test.sh` was observed,
and the lines in that suite are owed, listed below.

**Method.** Each break replaced exactly one site, and the run refused if the site was not unique. Each
break ran alone: apply it, run the arm's suite, record the FAIL lines that are new against the suite's
own green run at the same head, then restore the file's original bytes. GREEN is that green run, taken on
the same tree before the breaks. Each suite's reds already present in that green run are its baseline.
`tools/check-spec-tokens.test.sh` carried two of them, its selftest-manifest parity asserts over the
`routed_commits.py` ceiling, and `tools/lib/resolve-python.test.sh` one, its hand-resolved `{prefix}`
assert over `tools/playbook/core.py`. Neither is graded by a file this build touches. The instruments
are `arms.py`, `brk.py` and `arms.sh` in the session scratchpad.

## Observed red, then green

- `tools/memory-tree/gen_build_index.py --selftest`, unit 1:
  - `write_text` writing over identical bytes reds its AC1 mtime arm.
  - The staged stamp never consulted reds AC3.
  - Every `build/` record made structural reds AC5.
- Same suite, unit 6:
  - `not unmanaged` deleted reds AC5.
  - `rc == 0` deleted reds AC6.
  - The `check_render_settled` call deleted reds AC15 and AC16.
  - The bytes compare deleted reds AC16.
- `tools/check-spec-tokens.test.sh`:
  - Unit 1: the `building` branch disabled reds the `findings None` probe (AC7, AC8).
  - Unit 3: a tracer printing one line reds `LL3 AC6`.
  - Unit 6: `pre` ignored reds `AC8 reads 1` (AC10).
- `tools/workflows/unattended-build.test.sh`:
  - Unit 3: the mode test on `dispatch.declare` dropped reds `LL3 AC1` and the attended prompt check.
  - Unit 4: the S2 sentence deleted from the untyped arm reds both untyped AC3 arms.
  - Unit 4: the sentence added to the typed arm reds the typed `hasnt_` arm.
- `tools/lib/resolve-python.test.sh`, unit 3: one changed byte in the checker's inline copy reds the `read_open_py` parity row.
- `tools/unattended/stop-guard.test.sh`, unit 5:
  - `checkSession` calling `runLiveness` reds L5-AC3.
  - Each of the eight key parts dropped in turn reds its L5-AC4 move: session, record, refs (the commit and remote-ref moves), landed, conf, config and driver. The head part is unit 6's, below.
  - The deadline test removed reds L5-AC5.
  - The store admitting STALE reds L5-AC6.
  - The JSON parse unguarded reds L5-AC7, and with it every cached case.
  - `show-ref` without `--git-dir` reds L5-AC8.
  - The switch ignored reds L5-AC11.
- Same suite, unit 6:
  - The head part dropped reds the moved-checkout arm (AC2). This is the fix for review item M2; before unit 6 the move also moved refs.
  - `+ 1` dropped reds the inside-margin arm, and `+ 2` reds the on-margin arm (AC4).
- `tools/unattended/check-unattended.sh --only 39`, unit 6: `print_wake` removed from the allow-list reds check 39 (M1).

## Owed: not observed, by the owner's call

Every `New arm:` line in `tools/unattended/unattended.test.sh`, the driver suite that runs for hours:

- Unit 2: AC1, AC2, AC3 and the parity table's `wake` row.
- Unit 3: the inverted cache arm (steps a, b and c), the moved-tree and untraced-checker calls.
- Unit 6: AC3 (the raced stub), AC12 (the popen stub), AC7 (three phase arms), AC8 and AC9 (the dead-`date` arms).
- Unit 7: the rewritten `--wake` cadence block.

The pooled driver suite, `bash tools/unattended/run-unattended-gates.sh --pooled`, did not run either. Both are owed before the build's landing is trusted for `tools/unattended/unattended.sh`.

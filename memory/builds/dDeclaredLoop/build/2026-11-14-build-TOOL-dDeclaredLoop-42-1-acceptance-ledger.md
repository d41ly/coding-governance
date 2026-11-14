# TOOL-dDeclaredLoop-42 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-42

No merge bar, no self-test suite and no gate leg ran in this pass, and `loop_witness.py --selftest`, the
`loop computed witness` leg's command, was not run as a command. The criteria were observed on node `d`
(win32) by probes of the unit's own code: each new plant and the two plants whose commands now run under
bash, run one at a time as `--fixture --plant <case>`; the grandchild plant called in-process with the
teardown held; the `awk` extraction AC4 spells; and the `grep` counts AC1 and AC5 spell.

Seen in this pass, on a break made in-process and never on disk: with `worktree remove` answered as a
failure and the temporary directory's delete skipped, the grandchild plant held while the `leaked` line
printed, and failed naming the left worktree once that line was muted. That is a probe of AC3's two
arms, not the RED-first observation the close owes.

Owed to the close: every leg the spec's section 7 names; the `loop computed witness` leg; the two
`New arm:` lines' RED-first observations, the plants staged against `TOOL-dDeclaredLoop-17`'s
pipe-captured `shell=True` run, and the `run_tree_kill_py` parity row staged by a one-byte edit to the
loop copy; and the `resolve-python.test.sh` parity table over the new row, whose population grep reads
tracked files only.

**Evidences:** TOOL-dDeclaredLoop-42
- AC1 — `PASS bash-syntax` — `--plant bash-syntax` exited 0 printing `PASS bash-syntax`, the command
  re-run at the fixture's commit recording exit `0` and `9a271f2a916b`, the first twelve hex digits of
  the SHA-256 of `0` and a newline; `grep -c "shell=True" tools/loop/loop_witness.py` printed `0`.
  The `acceptance` and `probe-rerun` plants, whose commands wrap the interpreter's Windows path in
  double quotes, each still printed PASS under bash.
- AC2 — `timeout` — `--plant timeout-grandchild` exited 0, the call over `sleep 30 & wait` returning
  in 2.5 s with exit `timeout` against the 10 s bound, PINNED 2026-11-14 at this reading on node `d`.
- AC3 — `git worktree list --porcelain` — the same plant read one worktree, the fixture's own, and no
  `leaked` line; with the teardown held in-process it read two, the run's named by
  `loop-witness: leaked <path>`, and held.
- AC4 — `run_tree_kill_py` — the `awk` range over `tools/lib/run_tree_kill.py`, `tools/run-gates/regen.py`
  and `tools/loop/loop_witness.py`, carriage returns dropped, gave three non-empty extracts of 21 lines, PINNED,
  byte-identical by one MD5 digest.
- AC5 — `bash -c` — `grep -c` counted `bash-syntax`, `timeout-grandchild` and `bash -c` at 1 each in
  `help/loop.md` and in `tools/loop/README.md`.

Cost: run alone, `bash-syntax` took 5 s warm and 31 s on its first cold run, PINNED 2026-11-14,
and `timeout-grandchild` 3 s, PINNED 2026-11-14 at this reading; the `loop computed witness` leg's
budget row is re-derived by the main loop's reading at the close, per the spec's section 5.

On win32 the grandchild `sleep` outlived `taskkill /T` and held its `cmd-1.out`, so the run's temporary
directory, not its worktree, stayed in the host temp folder until the sleep ended: the risk section 5
names, with nothing in this unit's scope to reap it.

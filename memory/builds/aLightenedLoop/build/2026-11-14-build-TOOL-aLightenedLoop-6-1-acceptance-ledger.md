# TOOL-aLightenedLoop-6 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-6

No merge bar, no self-test suite and no gate ran in this pass. The criteria a probe can reach were
observed by scratch probes of the built code, none of them a suite or a slice of one: `ac4.sh` copies
the hook beside a counting stub driver and calls the exported `readLiveness` over `git init`
fixtures; `ac3.sh` sources the driver in a scratch repository under `%TEMP%/lp6` and calls
`run_spec_token_check` with the two new stubs; `wake.sh` sources the driver there and calls
`print_wake` with the rows before the clock stubbed healthy; `stamp_probe.py` loads a copy of
`gen_build_index.py` and replays each stamp arm's sequence; `ac17.py` compares the render keys;
`ac11.sh` and `ac11count.py` run AC11 in two clones under `%TEMP%`. Each probe was also run against
a copy with the criterion's staged break, and each named red below is that run. The suites' new arms
were written and not run: their RED-first observations, the executed counts against the two raised
`FLOOR_ASSERTIONS`, and AC1's check-39 CONTROL arm are the close's.

The owner's parity captures. Check 29's staged read, `gen_build_index.py --check-coverage --staged`
over the real tree with `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md`
flipped to INPROGRESS and staged: the clone at `4e2f7d26` and the built clone each exited 0 and
printed the one line `build-index: coverage — check 29 graded 1 INPROGRESS chain spec(s) in 1 of 22 <!-- PINNED 2026-11-14 -->
chain build(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21`, and `cmp` printed nothing. Timings, base
then built, on node `a`: 35 s and 41 s, one run each, inside the noise of one run. The render key, <!-- PINNED 2026-11-14 -->
AC17, is byte-identical over one tree. The spec-token cache's three not-recorded lines keep their
bytes, read off the probe output against the text at `4e2f7d26`.

**Evidences:** TOOL-aLightenedLoop-6
- AC1 — `PHASE_RECORDED_FNS` — `git diff 4e2f7d26 -- tools/unattended/check-unattended.sh` adds
  `print_wake` as the only word, beside one comment line. An awk over the driver listing every
  function outside `read_recorded_phase` that calls it printed exactly the eight names the list now
  holds. The `bash tools/unattended/check-unattended.sh --only 39` run, and the check-39 CONTROL arm,
  are the close's to observe.
- AC2 — `git show-ref --head` — in a scratch repository with one commit, `git branch other`, a
  capture, `git checkout -q other` and a second capture: `cmp` printed nothing and `.git/HEAD` read
  `ref: refs/heads/other`. The same pair across `checkout -b` differed. The L5-AC4 arm with `head`
  deleted from `deriveLivenessKey`'s parts is the close's.
- AC3 — `run_spec_token_check tRun` — `ac3.sh` with the raced `--input-key` stub on the built driver
  printed `spec-token cache not recorded: the tree or HEAD moved while the checker ran` and left no
  `spec-tokens.tRun.key`; on the driver at `4e2f7d26`, where `derive_spec_token_key` runs after the
  second `read_tree_state`, it printed no line and wrote the key, the named red.
- AC4 — `readLiveness` — `ac4.sh` with `Date.now` pinned and `STOP_GUARD_LIVENESS_BOUND_MS=3000`:
  after `set_live_clock 0 3` the first call stored `liveness.fx.json` and the counter read 2; after
  `set_live_clock 0 4` it read 1. With the `+ 1` dropped the first read 1; with it made `+ 2` the
  second read 2.
- AC5 — `not unmanaged` — `stamp_probe.py` built a `_fixture` with a committed `notes.txt` in its
  ledger folder and ran `--write`, `git add -u` and `--check --staged`: no file at
  `resolve_render_stamp` and no `answered by the stamp`. With `not unmanaged` deleted from
  `cmd_write`'s guard both read True, the named red. The selftest arm is the close's.
- AC6 — `rc == 0` — `stamp_probe.py` forced `print_verdicts` to answer 1 over a committed
  `_fixture`: `cmd_write` left no file at `resolve_render_stamp`, and the unforced control left one.
  With `rc == 0` deleted from the guard the forced run stamped, the named red. The selftest arm over
  `_build_code_tree(7)`'s committed tree is the close's.
- AC7 — `print_wake` — `wake.sh` printed `FULL · phase absent`, `FULL · phase LANDING` and
  `FULL · phase LANDED`, each followed by `tasks 1 open`, and HEALTHY with a BUILDING phase. The
  three `check_wake_full` arms and their staged breaks are the close's.
- AC8 — `TC_DEAD` — `wake.sh` with a `date` stub that exits 1 first on `PATH` printed
  `unattended-wake: tRun · FULL · clock probe · tasks 1 open · cadence every 10 minutes`. The `--wake`
  arm with the `TC_DEAD` branch deleted is the close's.
- AC9 — `TA_DEAD` — `wake.sh` with the heartbeat file removed and a stub that exits 1 on `-d`
  printed `unattended-wake: tRun · FULL · task probe · tasks unknown open · `, and HEALTHY with the
  stub off `PATH`. The `--wake` arm with the `TA_DEAD` branch deleted is the close's.
- AC10 — `AC8 reads 1` — the arm is written in `tools/check-spec-tokens.test.sh`; its fixture run
  and its red with `pre` ignored are the close's. AC11's count is the same shim over the real tree.
- AC11 — `cmp` — the two `gen_build_index.py --check-coverage --staged` captures under `%TEMP%`,
  `4e2f7d26` and built, were byte-identical with exit 0 each. `ac11count.py`, the counting shim on
  `read_carries_texts` around `derive_carries_coverage` with `building=True`, printed `reads 2` at
  `4e2f7d26` and `reads 1` built.
- AC12 — `{"kind":"popen","argv":["x"]}` — `ac3.sh` with the popen stub, whose `--input-key`
  answers through the real checker's `main`, printed `spec-token cache not recorded: the input
  record cannot be replayed` and left no key file, on the built driver and at `4e2f7d26`. The red
  with the replay branch collapsed is the close's.
- AC13 — `python tools/memory-tree/gotchas.py --check` — exited 0 with one advisory line after
  `--write`, and the `grep -c` over `memory/gotchas/INDEX.md` printed 3.
- AC14 — `python tools/codebase-map/gen_map.py --check` — exited 0 after `--write` re-rendered
  `memory/map/generated/`, and each named dossier's `gotcha-classes` line holds its class.
- AC15 — `check_render_settled` — `stamp_probe.py`, a `_fixture` with a staged spec edit, read
  `True False`: a stamp after the unshimmed `cmd_write`, none after the one whose `print_verdicts`
  shim wrote `notes.md`. With the `check_render_settled` call deleted it read `True True`.
- AC16 — `check_render_settled` — the shim appending to the tOne `README.md` read `True False`;
  with the bytes compare deleted it read `True True`, while AC15's arm stayed `True False`.
- AC17 — `derive_render_key(root, read_render_state(root))` — `ac17.py`, `python` over the module
  at `4e2f7d26` read with `git show` and the built one, over a scratch repository holding a
  committed, a modified, a deleted and an untracked file: the three digests were equal. A built copy
  hashing `tracked` with NUL separators instead of terminators printed DIFFER.

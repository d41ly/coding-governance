# TOOL-aMeasuredDrag-5 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-5

No merge bar and no self-test suite ran in this pass. The pass started at f2c00165. AC1, AC2 and AC3
ran as the spec's own probes from the worktree root in Git Bash. The probe was saved to the session
scratchpad as `md5-probe.sh`, and the hook at the pass commit's parent as `hook-before.js`, with
`git show HEAD:tools/process-monitor/procmon-hook.js` taken before the commit. The fixture repository
sat under the `md5` folder of `%TEMP%`. The new arm's RED-first observation is owed to the close.

**Evidences:** TOOL-aMeasuredDrag-5
- AC1 — `diff` — `diff` of the two probe transcripts' first seven lines printed nothing, exit 0. Both
  carry `[stamp in the common dir]`, and both print nothing above `[main PostToolUse rc=0]` and
  `[wt PostToolUse rc=0]`. A stamp written from the worktree throttled the primary tree, under the
  hook before and after.
- AC2 — `[wt PostToolUse rc=0]` — after: the probe's last line is `[wt PostToolUse rc=0]`, with
  nothing between it and `[main PostToolUse rc=0]` above. Before: the same step printed
  `process-monitor: could NOT run — spawnSync nonesuch-python-shim ENOENT` first. The before run is
  the red the criterion names.
- AC3 — `grep -n "'git'"` — over `tools/process-monitor/procmon-hook.js` it printed nothing, exit 1.
  Timed over 10 throttled runs from the fixture's worktree, within the 300 s window of AC2's probe
  (PINNED, `.process-monitor.conf@60c3d42027a9:78`):
  - before, `hook-before.js` at f2c00165: 2.282 s per 10 runs, PINNED at f2c00165. The spec's
    figure at 6d98c39ca is 2.43 s, PINNED at 6d98c39ca.
  - after, this commit's hook: 1.546 s per 10 runs, PINNED at f2c00165 plus this pass's diff.
  - spawn baseline: 0.377 s per 10 runs of `/usr/bin/true`, PINNED at f2c00165, beside the
    spec's 0.34 s, PINNED at 6d98c39ca.
  - node floor: 1.184 s per 10 runs of `node -e 0`, PINNED at f2c00165, beside the spec's 1.31 s,
    PINNED at 6d98c39ca.
  The after total is below the before total, and sits 0.362 s per 10 runs above the bare node
  floor, PINNED at f2c00165.

**Arm probe (not the RED-first observation):** this pass ran S3's arm text alone, outside the suite,
over a scratch copy of the suite's clean fixture under `%TEMP%`, with a fresh stamp in its git dir.
This commit's hook printed nothing. `hook-before.js` printed
`process-monitor: could NOT run — spawnSync nonesuch-python-shim ENOENT`. With the stamp removed,
this commit's hook ran the census and wrote the stamp into the fixture's `.git`, the common dir.
Two edge probes: a root with no `.git`, and a `.git` file naming a missing dir, each ran the census
unthrottled and created no directory. This checks the arm's logic only.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `test_throttled_path_spawns_nothing` in `tools/process-monitor/adopt-process-monitor.test.sh`,
  under the `process-monitor adopter selftest` leg. Restore the hook to its pass commit's parent
  bytes with `git show`; the arm must read `could NOT run` and go RED. It must go GREEN once
  restored. The suite's assertion count does not move.
- The gates in spec §6: `process-monitor adopter selftest`, `process-monitor wiring`, and
  `kit epoch (shipped bytes move, the version moves)` at the push boundary.

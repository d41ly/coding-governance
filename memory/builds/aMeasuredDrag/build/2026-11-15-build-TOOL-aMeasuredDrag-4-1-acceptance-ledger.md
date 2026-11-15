# TOOL-aMeasuredDrag-4 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-4

No merge bar and no self-test suite ran in this pass. AC1, AC3 and AC4 ran as the spec's own probes
from the worktree root. The pass started at a02057b4. AC2 and AC5 run
`python tools/playbook/instructions_edit.py check`, which is the `instruction edits (manifest checks)`
leg. The scratch-guard hook refused that command to this role agent: its allowlist is the naming
lexicon alone. So both are owed to the main loop, and no before or after time of the leg is recorded
here. The new arm G8 is owed to the close, RED then GREEN.

**Evidences:** TOOL-aMeasuredDrag-4
- AC1 — `OK` — the spec's probe printed `OK` and exited 0 at this commit. The same probe, with the
  base module from a02057b4 first on `sys.path` and the root given as the worktree, failed with
  `AssertionError: (1, 1)`. At base the `check` verb called `run_tag_check` once. The probe can fail.
- AC2 — `diff` — owed to the main loop. The before-run needs a checkout at a02057b4 and the after-run
  needs this commit, with `python tools/playbook/gov_tag.py check` exiting 0 before. The hook refused
  this pass both runs.
- AC3 — `grep -c` — `run alone does not report them` counted 1 in `tools/playbook/instructions_edit.py`.
  Over `tools/govkit/registry.toml`, `among them the tag checks` counted 0 and
  `` which the `check` verb leaves to it (TOOL-aMeasuredDrag-4) `` counted 1.
- AC4 — `OK` — the spec's probe printed `OK` over `tools/gate-legs.json`. The tags row has no
  `guard`, and both rows sit in chunk `declarations`.
- AC5 — `time` — owed to the main loop, with AC2's two runs. Each is timed beside a ten-`/usr/bin/true`
  spawn baseline. The after-run must be shorter than the before-run. The spec's figures for comparison
  are the leg's ledger median of 291.5 s and the tags leg's 263.2 s, PINNED 2026-11-15. No time of this
  unit's code is recorded here.

**Arm probe (not the RED-first observation):** this pass took G8's text out of
`tools/run-gates/run-gates.gov.test.sh` into a scratch file. It sourced that text alone with
`PYBIN=python`, over four scratch copies of `tools/gate-legs.json`. The real copy gave `fail=0`.
A `guard` on the tags row gave `fail=1` and named the guard. The tags chunk moved to `selftests`
gave `fail=1` and named both chunks. The tags row renamed gave `fail=1` with the "graded nothing"
liveness line. Each run counted `a` once. This checks the arm's logic only. It is not the suite's
RED-first observation.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm G8, in `tools/run-gates/run-gates.gov.test.sh` under the `run-gates gov canary` leg. Stage
  a `guard` on the tags row of `tools/gate-legs.json`, then move its chunk to `selftests`. Each must go
  RED. A rename of the tags row must red on the liveness check. The arm must go GREEN once restored.
  `FLOOR_ASSERTIONS` is now 18.
- AC2 and AC5, as above.
- The gates in spec §7. The `instruction edits selftest` re-observes the fixture's five `check` cases
  and the retired-tag case that calls `run_tag_check` directly.

## Observed at the main loop, 2026-11-15

- AC2: `python tools/playbook/instructions_edit.py check` at `a02057b4b` and at `653ccd404` printed byte-identical output (`instructions-edit: check · 13 row(s)`, `0 red`), both exit 0, compared with `diff` (PINNED 2026-11-15).
- AC5: the same verb took 774 s at `a02057b4b` and 3 s at `653ccd404`, beside a spawn baseline of 0.510 s for ten `/usr/bin/true` (PINNED 2026-11-15). The base reading waited on the shared tag index, so it is a contended figure; the after-run reads no tag index at all.

# TOOL-aMendedFleet-3 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-3

**Evidences:** TOOL-aMendedFleet-3
- AC1 — `python tools/lexicon/lexicon.py --merge-losses 01c22e155~1..01c22e155` — exits 1 with `merge-losses: LOSS 01c22e15 parent 2: tools/unattended/unattended.sh: write_ask_views`; graded 2, losses 1. Built as rev-3 said it exited 0 with `masked=1`, because the suite stub `write_ask_views()` in `tools/unattended/unattended.test.sh` stood at the second parent and at the merge; rev-4 narrowed the masking rule and this line is the observation after it. Against the base lexicon the mode does not exist and the call exits 2 with usage
- AC2 — `python tools/lexicon/lexicon.py --merge-losses ac65de998..35438ba0a` — exits 0 with `graded=1` and `losses=0` over 11 armed paths; `verb_review` is not named
- AC3 — `python tools/lexicon/lexicon.py --merge-losses <range>` — in the `tools/lexicon/selftest.py` arm's fixture, whose `.lexicon.conf` arms `sh`: the losing merge exits 1 naming `fb` at parent 2, though a same-named stub of `fb` stands in another file; keeping both exits 0; `superseded: fb -> fa` exits 0 with `superseded=1`; `superseded: fb -> nothere` exits 1 naming `nothere`. Run as that block alone over a harness under the session scratchpad: 10 of 10 arms pass; RED against the base lexicon (10 of 10 fail at exit 2) and against a staged break restoring the bare-name mask (3 fail: this case, the superseded case and the restore case)
- AC4 — `python tools/lexicon/lexicon.py --merge-losses <range>` — same fixture: a commit re-adding `fb` makes the range ending there exit 0 with `restored=1`; a merge moving `fa` to `b.sh` exits 0 with `masked=1`; a merge taking out `fk`, which both parents carried from the base, exits 1 naming it under `parents 1 and 2`; the keep-both merge lacks `fz`, which side B took out since the base, and exits 0
- AC5 — `.lexicon.conf` declaring every language `dark` — the mode exits 2 and prints `DEAD PROBE`; a range holding no merge exits 0 with `graded=0` without reading the declaration
- AC6 — `git push origin main` — from a fixture under `%TEMP%` whose `core.hooksPath` is this tree's `.githooks`: refused, `<git-dir>/pre-push-refusal` starts with `merge-loss`, the output names `a.sh: fb`, and `git ls-remote origin main` is unchanged. Against the base hook the token was `raw-push`. The same arm in `.githooks/pre-push.test.sh` (hook copied to a scratch hooks dir) was run as a slice of that suite's prologue plus the arm: ok, and RED against the base hook
- AC7 — `superseded: fb -> fa` amended into the same merge — the refusal token is `raw-push`, not `merge-loss`, on both the new and the base hook (a control)
- AC8 — `bash tools/push-main.sh --prepare --slug fx` — exits 1 naming `a.sh: fb`; `git rev-parse refs/heads/feat` equals its value before the call and `feat` is checked out. Against the base lander it exited 0 and moved the branch to the prepared merge. The same case is `tools/push-main.test.sh` case 23, run as a slice of its prologue plus the case: ok, and RED against the base lander
- AC9 — `grep -n -i 'does not see' tools/lexicon/lexicon.py .githooks/pre-push` — one hit in each: the `check_merge_losses` docstring and the pre-push block header, each listing body-level loss, unarmed languages, a loss masked by a same-named definition, and octopus merges
- AC10 — `python tools/lexicon/lexicon.py --merge-losses 01c22e155~1..01c22e155` — its summary line prints `seconds=11.53` on node a, under the 30 ceiling

## Owed at the close

- `.githooks/pre-push.runlog.test.sh` — its exit table gained an exempt row for the new
  `write_refusal merge-loss` site; the table scan alone was run over the hook (21 sites, none
  unknown, miscounted, stale, unmarked or misplaced). The suite itself is the close's.
- `memory/map/generated/symbols.json` — regenerated in this commit by `gen_map.py --write`; the
  coverage and freshness legs are the close's.
- The drift-audit ask §3's hands-off edge names (moving `_read_defs_at_sha` onto `read_defs_at_sha`)
  is NOT filed: a pass does not mint ids, so the main loop files it.

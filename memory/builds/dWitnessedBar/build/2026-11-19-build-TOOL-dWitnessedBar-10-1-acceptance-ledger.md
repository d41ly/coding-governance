# TOOL-dWitnessedBar-10 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-10

This pass ran no merge bar and no gate leg. Every criterion below was checked on node d on 2026-11-20
by probing the unit's own code: `precommit.py --list` on the built tree, `precommit.py --legs`,
`derive-ceilings.py --write`/`--check` and `profile_bar.py --record` over scratch git repositories
under `%TEMP%`, the edited pre-commit hook installed into a scratch repository with this tree's runner
copied beside a fixture manifest, and `python -c` calls into `test_codebase_map.py` and `govkit.py`.
The new evidence arm's block was also cut out of `run-gates.evidence.test.sh` and run alone against
stub `ok`/`nope` helpers, which is a slice of that suite the pass should not have run; it printed 6
of 6 `ok`. The close owes every leg of section 7, the RED-first observation of its three `New arm:`
lines, and AC2's commit-time `cost:` reading.

**Evidences:** TOOL-dWitnessedBar-10
- AC1 — `--list` — `python precommit.py --list` under `tools/run-gates/` printed four rows, each
  `every commit`: `codebase-map coverage + freshness` (`python3 tools/codebase-map/test_codebase_map.py
  --precommit`), `kickoff-manifest ratchet` (`bash skills/session-kickoff/manifest-check.sh --staged`),
  `unattended skill wiring` (`bash tools/unattended/adopt-unattended.sh --check`) and `template size
  <=48KiB` (`bash tools/check-template-size.sh`); no `memory hygiene` row. The criterion's `grep -cE`
  over `.githooks/pre-commit` printed 0. `git diff eed402e7 -U0 -- .githooks/pre-commit` has hunks at
  base lines 217, 223-225 and 328 on, none inside the hygiene block at base lines 286-326.
  `leg_factory.py --check` read the manifest fresh after `--write`.
- AC2 — `not tripped` — over a scratch repository, a fixture manifest with `A` guarded on `a/` and
  `B` carrying no `precommit`: `a/x` staged printed `A RAN` and `pre-commit: A ok`; `b/y` staged
  printed `pre-commit: A not tripped`; `B` never ran. The edited hook over the same fixture with the
  runner copied to a root install committed `a/x` after `pre-commit: A ok` and `b/y` after
  `pre-commit: A not tripped`. `cost:` owed: the hook's wall time on a one-file commit of gov's tree
  runs the four legs, which a pass may not run, so the close records it beside the base's.
- AC3 — `FAILED (rc 1)` — with `A`'s argv exiting 1, `precommit.py --legs` printed
  `pre-commit: A FAILED (rc 1)` and exited 1; through the hook the commit exited 1 with that line and
  the hook's own `a gate failed` line, and with `A` restored the same staged change committed.
- AC4 — `announced skip` — the unguarded `C` ran for every staged path above (`C RAN`, `pre-commit:
  C ok`); with its argv naming `missing.py`, it printed `pre-commit: C leg SKIPPED — no kit root:
  missing.py is absent from this tree.` and the run exited 0.
- AC5 — `--precommit` — `derive_unstaged_artifacts()` read `[]` on the clean tree, read
  `['memory/map/generated/CARDS.md']` with that artifact edited and unstaged, and `[]` once it was
  staged; the file was restored. The `__main__` path runs it after every assertion passes and fails
  naming each path. The criterion's whole CLI over a scratch repository runs the codebase-map gate
  and is owed to the close.
- AC6 — `LEG_KEYS` — `grep -n 'precommit' run-gates.test.sh` names the one `LEG_KEYS` line (355),
  the canary floor comment and arm 1a's control pair, and no second key list. The criterion's own
  pattern `'"precommit"'` cannot match the `LEG_KEYS` line, a space-separated string, so the
  unquoted pattern was read instead. `grep -n precommit govkit.py selftest.py` names
  `LEG_KEY_FLOORS = {..., "precommit": (1, 53)}`, the emitter's `floor=LEG_KEY_FLOORS["precommit"]`
  read and the selftest's PC1 pair; `KIT_RUN_GATES_VERSION=1.53`. `check_target_reads_subject`
  answered False for a 1.52 runner and True for 1.53.
- AC7 — `GOV_NODE=b` — over a scratch kit holding `L` at 10.0 on node `a` and a 12.0 run reading:
  `--write` left `L 10.0 1 a 2026-09-10 runner` byte-identical and added `L 12.0 1 b`; a
  node `c` row spelled `20` was carried as `20`, not re-rendered. With a 290.0 node-b reading against
  a 300 s ceiling, `--check` failed `L` on `evidenced maximum 290.0s` while node a still read 10.0.
- AC8 — `GOV_NODE` — `--write` with `GOV_NODE` unset exited 1 naming `GOV_NODE`, and the evidence
  file's bytes were unchanged.
- AC9 — `evidenced on one node only` — over the scratch kit `--check` printed `ceiling-evidence: 1 of
  2 legs evidenced on one node only`. On the built tree the line's figure, DERIVED from
  `ceiling-evidence.txt` against the manifest, is 131 of 131; running `--check` on the built tree is
  the `leg ceilings clear their evidenced maximum` leg, owed to the close.
- AC10 — `--record` — over a scratch kit, `GOV_NODE=b profile_bar.py --record --out <log>` wrote
  `b 2026-11-20 1234abcd 812.3 2 6` from the log's last, full record; with `GOV_NODE` unset it
  exited 1; with a `--scoped` last record it exited 1 and the file's bytes were unchanged.

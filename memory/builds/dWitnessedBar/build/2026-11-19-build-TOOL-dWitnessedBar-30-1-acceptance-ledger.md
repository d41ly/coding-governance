# TOOL-dWitnessedBar-30 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-30

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon's `--suggest`
excepted. The criteria were observed on node d, 2026-11-20, at base `f769a2756`, by `verdict_flow.py`'s
own fixtures, by in-process mutation probes of them, by stub-runner probes of `check_quiet` and
`run_quiet_leg`, by slices of the runner's selection parse and of the driver's `write_backlog_rows`,
`write_ask_closing`, `write_flake_releases` and `run_verdict_route` run over scratch fixtures with
their collaborators stubbed, and by `grep` and `bash -n` over the edited files. The runner itself was
not run: a fixture bar is a suite's, so AC1's bar half and AC6's live half are owed to the two `New
arm:` lines of spec section 7, `run-gates.test.sh` arm 3h3r and `profile_bar.test.sh` arm 9p, written
and not run; their runs, their RED-first observations and the legs of section 7 are owed to the main
loop at the close.

**Evidences:** TOOL-dWitnessedBar-30
- AC1 — `held-run`: `python verdict_flow.py --fixture held-run` in `tools/run-gates/` exited 0: a
  five-field `run` row written and read back in mode `run`, a four-field row read `hold`, a mode
  `maybe` refused, `select --check`'s compared part equal for a `run` row and its four-field twin and
  unequal when the note moves, and a GREEN verdict's `held.1` `quarantine · fail` read by
  `read_held_keys`. A slice of the runner's selection parse over a scratch selection read the `run`
  row's mode `run`, a four-field row `hold`, a CR-terminated row `hold`, and refused `maybe`. The bar
  GREEN beside the failing leg, its `.leg` row and the verdict's `held.1` are arm 3h3r's, owed.
- AC2 — `daily`: `python verdict_flow.py --fixture daily` exited 0: under each of `on-demand`,
  `push-selected` and `peer-or-cadence` the leg whose newest row since its hold ended 25 hours before
  the selection was `run`, the one at 23 hours `hold`, and one with no row `run`. Mutated so
  `verdict.held` `on-demand` holds every leg, the fixture went red naming the modes.
- AC3 — `release`: `python verdict_flow.py --fixture release` exited 0, printing `release  P
  ARCH-tFlake-1  3 green since its hold, verdict.flakes.release 3 · runs run-3 run-2 run-1`, nothing for
  Q (green, red, green, green), and `release  fast suite  ARCH-tFlake-3  its manifest row at R differs
  from its row at <sha8>, which filed the ask` once its row changed. Mutated so the streak skips a red,
  the fixture went red on Q; a `verdict.flakes.release` of `x` at R made `select` exit 2 naming the key.
  `grep -c 'write_ask_closing' unattended.sh` in `tools/unattended/` printed 4.
  A slice of `write_flake_releases` over a stub kit wrote `- CLOSED · ARCH-tFx-3 · by <40-hex> ·
  released: leg P, ...` under `## Dispositions`, staged it, said an ask its home does not file and a
  malformed line, and left the file unchanged on a second call; `backlog.py#extract_row` read the row
  as `status CLOSED` by the sha, byte-equal to `render_status_row`'s.
- AC4 — `contended-pair`: `python verdict_flow.py --fixture contended-pair` exited 0: under a stub
  reading `false` it printed `awaiting quiet host  slow leg  since ...` and ran nothing; under `true` it
  ran each leg once, writing `rerun ok` and `rerun red OWN` routed `attribute`; a second call ran
  nothing. `run_quiet_leg`, its runner call stubbed, set `GATE_LEGS` to a one-row manifest,
  `GATE_FULL=1`, `GATE_SELFTESTS=1`, `GATE_RUN_ID` `<run id>-quiet-<n>` and `GATE_ATTRIBUTE` the
  attribution row's R, dropped `GATE_SELECTION`, bounded the call at 900 s for a 300 s ceiling with no (DERIVED from the builder's probe)
  pipe to the runner, read GREEN, RED attributed OWN and REFUSED as `None`, `OWN` and `-`, and read the
  bound firing as `-`.
- AC5 — `owner`: the same fixture printed `owner  slow leg  contended, no quiet host within 72 h` and
  wrote `rerun owner` with the row routed 73 hours before under `flow.wait-ceiling` 72, `awaiting` at
  71, and over a sibling record whose row read `rerun waiting` stamped 73 hours before, the fresh
  `route` carried that stamp and the next call printed `owner` for that leg alone; a `flow.wait-ceiling`
  of 0 made `quiet-rerun` exit 2 naming the key. Mutated to an unbounded ceiling, the fixture went red. A slice of `run_verdict_route` over a stub kit filed the
  `owner` line through `write_leg_ask` as `contended red, no quiet host: leg slow leg` HIGH, and put the
  bar's capture back.
- AC6 — `unverified`: with PATH emptied, `check_quiet` took the POSIX arm and, under a stub runner
  asked for `ps`, read `unverified` for rows omitting its own pid and for its own row with no command
  line, `false` beside a foreign bar, `true` alone, and `unverified` when `ps` raised. The live half
  wants a Linux node, and arm 9p's run and RED-first observation are owed.
- AC7 — `## .verdict.flakes.release.`: after `policy.py lists --write` and `render_playbook.py
  --reference`, `grep -cx '## .verdict.flakes.release.' help/reference/policy.md` printed 1 and `grep
  -cx 'verdict.flakes.release' tools/policy/unsummarised-keys.txt` printed 0.

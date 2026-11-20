# TOOL-dPlacedRequest-98 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-98

The unit was built from its spec at rev-2 on base `6d4c35b4f`, whose lander suite is byte-identical to
the one at `95c3103ad`. Built: S1. In `tools/push-main.test.sh#write_fence_fixture` the fixture makes,
under `$FX` and outside both clones, a scratch kit tree that is a git root of its own, holding copies
of the driver's kit, the playbook kit (found beside the lander by its `render_playbook.py`, copied to
`playbook/` so the driver's kit probe finds it) and, where the install has them, the `policy` and
`loop` kits the driver's lease verbs resolve; the playbook copy's `fleet.toml` holds `daily-agent` at
tag `a` and `agent5` at tag `b`. Each clone's launcher is `exec env -u GOV_NODE bash <the copy>`, and
arm 54's stub hands every other call to that launcher, copied aside as `$FX/real-driver` the way arm
46 does, so the one unset reaches every driver call. A failed step leaves its own line in `fx_line`.
The block's branch is now: no unattended kit or no python, a skip naming 42-54 that sets `skipped`;
else a fixture that could not be made, a `bad` naming the acquire's own line; else the arms. Every
dependency skip line of the suite sets `skipped=1`; `ok` counts into `n`; the closing lines compare
`n` with `FLOOR_ASSERTIONS` only where `skipped` is 0, else print `floor not compared — a dependency
skip fired`, and print `PASS ($n assertions)` when `fail` is 0 beside the kept `all cases ok` and
`FAILURES` lines. The `push-main self-test` budget row is re-priced as a proxy, the suite's waiver row
is removed, and the class rule lands as a section of
`memory/gotchas/fixture-inherits-ambient-machine-state.md`. No gate, suite or bar ran in this pass.

THE FIXTURE PROBE, the reading the lines below cite as "the fixture probe": two scratch worktrees under
a short temp path, one of the base and one of the base carrying this pass's suite, each with its
`tools/playbook/fleet.toml` edited so its `daily-agent` row names `renamed-agent` instead; a script
under the run's scratch directory cuts `write_fence_fixture` from the worktree's suite with
`awk '/^write_fence_fixture\(\) \{/,/^\}/'`, sets the suite's variables (`HERE`, `KIT_REL`, `lander`,
`_fn_k`, `_fn_pb`, `FX`, the fixture identity and autocrlf pins) with `USERNAME=daily-agent`,
`CLAUDE_CODE_SESSION_ID=sA` and `GOV_NODE=zz` exported, evaluates the function and reads the origin's
lease commit's `fleet-tag:` line.

THE FLOOR PROBE: a script cuts the closing compare with `awk '/^if \[ "\$skipped" = 0 \]; then$/,/^fi$/'`,
reads the pin from the `FLOOR_ASSERTIONS=` line, and evaluates the cut with `n` one below it under
`skipped=0` and then `skipped=1`.

**Evidences:** TOOL-dPlacedRequest-98
- AC1 — `write_fence_fixture` — the fixture probe over this pass's suite returned 0, its acquire printing `lease — fx/build · create · epoch 1`, the lease commit's `fleet-tag:` reading `a`, with the worktree's live registry holding no `daily-agent` row and `GOV_NODE=zz` exported. (DERIVED)
- AC1 — `FLOOR_ASSERTIONS` — over the tip, `grep -c '^FLOOR_ASSERTIONS=[0-9]*$' tools/push-main.test.sh` printed 1. (DERIVED)
- AC1 — `testsuite-count-waivers.txt` — over the tip, `grep -cx 'tools/push-main.test.sh' memory/project/testsuite-count-waivers.txt` printed 0. (DERIVED)
- AC1 — `FAIL` — the floor probe under `skipped=0` printed `FAIL — the suite ran 100 assertions, below its floor of 101 …` and set `fail=1`; under `skipped=1` it printed `push-main.test: floor not compared — a dependency skip fired` and left `fail=0`. (DERIVED)
- AC1 — `selftest-budgets.txt` — over the tip, `grep -c 'TOOL-dPlacedRequest-98' tools/run-gates/selftest-budgets.txt` printed 1. (DERIVED)
- AC1 — `95c3103ad` — the RED reading, over the base worktree whose suite matches `95c3103ad`'s byte for byte: the fixture probe's function returned 1, the acquire refused and the origin holding no lease, `fleet-tag:` empty; `grep -c '^FLOOR_ASSERTIONS=[0-9]*$'` printed 0; the floor probe found no closing compare to cut; the waiver grep printed 1; the budget grep printed 0, the `push-main self-test` row naming `TOOL-dSafePassage-42` and no unit of this build. (DERIVED)

## Readings beside the criteria

- The first fixture probe of this pass's suite returned 1: the registry's rows were written with an empty `projects_root`, which the playbook reader refuses (`fleet row 1 (a): projects_root is empty`); the rows now carry `$FX`. (DERIVED)
- That first run also printed the driver's NOTE that no policy kit resolves beside its kit, a line the live driver does not print, so the fixture copies the `policy` and `loop` kits beside the copy where the install has them. (DERIVED)
- A scratch kit tree outside any git root does not answer: `resolve_kit_dir` prints its hit relative to the drive's anchor and `resolve_fleet_tag` prefixes nothing, so on Windows the path lands under the Git install; a direct probe of the lib read `can't open file 'C:\Program Files\Git\Users\…\render_playbook.py'`. The tree is therefore `git init`ed, as the comment above the block says. (DERIVED)
- The block's cost counts, by `grep` over its non-comment lines: fixture makings: (DERIVED)
  3 (DERIVED)
- and `--land` calls: (DERIVED)
  11 (DERIVED)
- The proxy, the row's 688 s plus 3 at 14.7 s and 11 at 65.0 s: (DERIVED)
  1447.1 s (DERIVED)
- times 1.5, the budget written: (DERIVED)
  2171 (DERIVED)
- That proxy exceeds the leg's `ceiling` in `tools/gate-legs.json`, at the base: (PINNED)
  580 s (PINNED)
- so per §4 the ceiling move is the main loop's, from its measured reading of the leg alone, by `derive-ceilings.py --write --observed`, `pass_legs.py --apply` and the `last-audit` re-stamp; this pass did not move it. (DERIVED)
- The pin is DERIVED and not read from a run, since no suite runs in a pass: the suite's `ok` call sites, (DERIVED)
  97 (DERIVED)
- plus the arm-14 loop's second file and arm 37's further plantable rows, (DERIVED)
  4 (DERIVED)
- so `FLOOR_ASSERTIONS` is written as: (DERIVED)
  101 (DERIVED)
- The kit-epoch leg reads the push-main entry as `skip · no declared version`, its descriptor's `version_from` being `none`, so no version carrier moved. (DERIVED)
- `bash -n tools/push-main.test.sh` exited 0, and the `testsuite counts` leg's `compliant` patterns, run by `grep` over the suite, each matched once. (DERIVED)

## Items diverged

None.

## Owed at the close

- `New arm:` `tools/push-main.test.sh` — the fenced-landing fixture over a registry with `daily-agent` renamed, which the suite at `95c3103ad` answers with the skip and `all cases ok`; its RED-first observation in the suite and its GREEN reading, and the pin's confirmation: the count the suite prints with every block running must equal `FLOOR_ASSERTIONS`, raised or lowered inline by the main loop where its reading differs.
- The `push-main self-test` leg's measured reading against its ceiling, and the ceiling move §4 routes to the main loop where the reading exceeds it.
- The legs the spec's Gates section names, run once by the main loop.

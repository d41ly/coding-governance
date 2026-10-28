# TOOL-dFurnishedOrders-46 — the fourth spec audit's 18 roles, run-gates, process-monitor, unattended and kickoff minors: one re-stamp last, one bounded runner that carries its imports and kills on any exception, criteria that read the real gate, and the guards and pins the new arms move

**Status:** DEFERRED · rev-4 · 2026-10-28 · node d · Tier-2 · base 47d3a464 · streams tooling · order 26 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-46-deviation-461.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-46-deviation-461.md) | deviation | — |
| [2026-10-27-build-TOOL-dFurnishedOrders-46-deviation-462.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-46-deviation-462.md) | deviation | — |
| [2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md) | journal | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-build-TOOL-dFurnishedOrders-46-deviation-463.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-46-deviation-463.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-58 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-46-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-46-1-spec-writer.md) | journal | — |
| [2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`)
confirmed 13 MEDIUM and 13 LOW findings. BUILD-METHOD M4 batches them, and they split into two
disjoint write sets by M6 (`TOOL-dFurnishedOrders-45` §4 "Why two units"):
`TOOL-dFurnishedOrders-45` takes the 8 that land on the govkit upgrade step, and this unit the other
18. Each report id is named once below and closed by its own scope item.

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M2 | 2 | MEDIUM | unit 42 S3, AC2; unit 39 §4 Rollout, Files touched, §7 | S1 |
| M3 | 3 | MEDIUM | unit 39 S3; unit 37 AC8; unit 42 S19 | S2 |
| M4 | 8 | MEDIUM | unit 39 S1, S3, §4 | S3 |
| M6 | 10 | MEDIUM | unit 42 S17; unit 39 §7 | S4 |
| M7 | 15 | MEDIUM | unit 42 S7, §4, AC4, §10 | S5 |
| M8 | 16 | MEDIUM | unit 42 S2, §4, AC2 | S6 |
| M9 | 20 | MEDIUM | unit 38 §4 Inventory, Files touched, §7 | S7 |
| M10 | 22 | MEDIUM | units 40 and 41 §7 arms, Files touched | S8 |
| M11 | 29 | MEDIUM | unit 39 S1, S3, §4 | S9 |
| L1 | 4 | LOW | unit 42 S14, S19; unit 39 S3 | S10 |
| L3 | 11 | LOW | unit 39 §3, §10 | S11 |
| L4 | 12 | LOW | unit 39 §7; unit 42 §7 | S12 |
| L6 | 17 | LOW | unit 39 S1, §4, §10 | S13 |
| L8 | 19 | LOW | unit 38 S1, §4, AC2, §10 | S14 |
| L9 | 24 | LOW | unit 39 §3, §10 | S15 |
| L11 | 28 | LOW | unit 38 S2 | S16 |
| L12 | 30 | LOW | unit 39 S1, §3 | S17 |
| L13 | 33 | LOW | unit 42 S19, AC13 | S18 |

## 2. Scope (IN)

- **S1** — id 2. One re-stamp, after the build's last watched edit. Unit 39 moves
  `KIT_RUN_GATES_VERSION` (`tools/run-gates/run-gates.sh:36`), a path on
  `memory/guides/SESSION-KICKOFF.md`'s `watch:` line, after unit 37 S17's re-stamp at order 23; this
  unit's S8 render moves `tools/gate-legs.json`, and it moves that version again (S9, S17). This
  unit's pass re-stamps the `last-audit:` line once, bundled with or after its own last commit
  touching a watched path. Unit 39's ledger records that its watched edit is re-stamped by this item,
  and unit 42's ledger answers AC2 in the AMENDED form, its S3 sentence that units 38 to 42 edit no
  watched path corrected by this item. Observed by AC1.
- **S2** — id 3. Unit 37 AC8's first arm read against the shared block. After unit 39 inlines the
  `run_bounded_py` block into `tools/roles/roles_lib.py`, every line `git grep -n -E
  "subprocess\.(run|Popen|check_output|call)\(" -- 'tools/roles/*.py'` prints lies between that file's
  `# >>> run_bounded_py` and `# <<< run_bounded_py` lines. Unit 37's ledger answers AC8's first arm in
  the AMENDED form, in that form, naming this item and unit 42 S19. Observed by AC2.
- **S3** — id 8. Newlines as text mode gave them. `run_slot_reader` (`TOOL-dFurnishedOrders-29` S24)
  turns `\r\n`, then a lone `\r`, into `\n` in the output the block returns, as the
  `capture_output=True, encoding="utf-8"` calls it stands for did (`tools/roles/handoff.py:269-270`);
  the block's own decode stays as unit 39 S1 states it, so `regen.run_command`'s output is unchanged.
  Observed by AC3.
- **S4** — id 10. The roles suite's budget derived, not declared. The `roles adopter self-test` row of
  `tools/run-gates/selftest-budgets.txt` (`:96`, "not measured") is re-priced to the ceiling of 1.5
  times the sum of the leg's worst gate-ledger reading and the sleep the arms of units 39, 42 and this
  unit add to the suite, floored at the file's 60 s, its note naming both inputs. The worst reading is
  51.124 s of three, 34.186, 40.842 and 51.124 (PINNED, read 2026-10-27 from the main checkout's
  gate ledger). Unit 42's ledger answers S17's "stays inside its 60-second row" by that row, AMENDED,
  naming this item. Observed by AC4.
- **S5** — id 15. The roles kit's imports judged by the lexicon kit's predicate. Unit 42 S7's gate is
  `check_self_containment` (`tools/lexicon/lexicon.py:2359`) over `tools/roles`, whose problems are
  empty and whose judged count is above zero. A kit imports no sibling kit (TOOL-dGroundRules-1 §4,
  PLAY-dOrderedCharter-7 §4), and the roles kit's `project-owned` rule (`tools/roles/kit.toml:46-48`)
  withholds the suite from adopters without declaring an edge, so the unit 42 arm in the roles
  adopter suite runs the predicate through the lexicon verb §8 F7 asks for, by subprocess, and no file
  of the roles kit loads `lexicon.py` in process. Unit 42's ledger answers AC4 in the AMENDED form, and
  unit 42 §10's "none an import gate" is corrected by this item. Observed by AC5.
- **S6** — id 16. The ratchet observed by its own checker. Unit 42 AC2 is answered by
  `skills/session-kickoff/manifest-check.sh` itself, whose `splitspecs` (`:1433`) trims the `watch:`
  line and whose stamp walk (`:1521-1535`) validates the stamp, never by unit 42 §4's hand-split copy;
  unit 42's ledger answers AC2 in the AMENDED form, naming this item. Observed by AC6.
- **S7** — id 20. The verb pin moved by the names the build minted. `.lexicon.conf`'s
  `VERB_OFFENDER_PIN` (`:327`, `1212` at `47d3a464`) equals the verb rows `python
  tools/lexicon/lexicon.py --offenders` prints at this pass, `miss` in the unattended adopter suite
  (unit 38 S1) among the arrivals, under a dated `RAISED` comment naming each arrived key and the unit
  that minted it, in the shape of `:173`. Observed by AC7.
- **S8** — id 22. The govkit selftest guard covers what its arms read. The `govkit selftest` leg's
  guard gains, as exact files: `{prefix}/drift-audit/kit.toml`,
  `{prefix}/workflows/kit.toml`, `{prefix}/workflows/unattended-build.test.sh`,
  `{prefix}/memory-recall/kit.toml`, `{prefix}/process-monitor/kit.toml`,
  `{prefix}/pytest-parallel-guardrails/kit.toml` and `.githooks/pre-push.runlog.test.sh`, read by the
  arms of units 40, 41 and 43; and, for unit 44's `apply --all` arm, the descriptor of every registry
  entry outside `{prefix}/govkit/`, taken from `{prefix}/govkit/registry.toml`'s `descriptor` keys at
  this pass. The rows go on that leg's one declaration, the `[[exempt_leg]]` row at
  `tools/govkit/registry.toml:439`, and `python tools/run-gates/leg_factory.py --write` renders them
  into `tools/gate-legs.json` (TOOL-dWitnessedBar-11 S1, S2). Where the factory is not built at the
  pass (it is absent at `1a61f21a2`), the pass edits the manifest row by hand, a row
  TOOL-dWitnessedBar-11 §4 "Migration" moves whole onto that declaration, and its ledger records that
  the hand edit stood in for `--write`. Observed by AC8.
- **S9** — id 29. The block carries its imports. `import os`, `import signal`, `import subprocess` and
  `import tempfile` sit inside the `run_bounded_py` markers in the canonical `tools/lib/run_bounded.py`
  and so in every copy, as the `health_log_py` block carries its own (`tools/lib/health_log.py`).
  Observed by AC9.
- **S10** — id 4. The posture read's environment carried. `run_slot_reader(argv, root, bound=30,
  env=None)` passes `env` to `run_bounded`, and `derive_attended`'s posture read passes
  `dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")`, so unit 42 S14 holds through unit 42
  S19's one runner. Observed by AC10.
- **S11** — id 11. The card's map read cited where it is built. The card's map read is bounded in a
  scratch file by unit 37 S13 and S14, at order 23; the `cli —` cell's PATH read
  (`skills/session-kickoff/manifest-check.sh:403-409`) is its precedent. Unit 39's ledger records that
  its §3 cited the precedent as the seam, naming this item. Observed by AC11.
- **S12** — id 12. Staged breaks that run current bytecode. The close's RED-first observation of every
  arm units 39 and 42 and this unit stage on a `.py` file clears `tools/roles/__pycache__`,
  `tools/run-gates/__pycache__`, `tools/lib/__pycache__` and `tools/process-monitor/__pycache__`
  before each staged run, runs Python with `-B`, and records each RED beside the check its break
  targets, as `memory/gotchas/staged-break-runs-stale-bytecode.md` requires. Observed by AC12.
- **S13** — id 17. One Python `run_bounded`. `tools/process-monitor/census.py` carries the
  `run_bounded_py` block inline, and its wrapper, which held that name (`:78`), takes the name
  `run_backend(argv, timeout=BACKEND_TIMEOUT_S)`: it calls `run_bounded(argv, None, timeout)`, raises
  `CensusRefused` naming `did not answer within <n>s` on `TIMEOUT` and `not runnable` on `OSError`, and
  returns stdout. The pipe this unit's block exists to avoid leaves census too.
  **Readers:** by name: `tools/process-monitor/census.py` at `:265`, `:270` and `:274`, and
  `tools/process-monitor/selftest.py` at `:276`, `:277`, `:284` and `:298`. by value: the census
  parsers fed at `:265`, `:270` and `:274`, which read the same decoded stdout as before.
  Observed by AC13.
- **S14** — id 19. The kit's one `miss` spelling. The unattended adopter suite's `miss` is
  `tools/unattended/unattended.test.sh:145` verbatim, printing `FAIL unexpected:`; unit 38's ledger
  answers AC2 in the AMENDED form, expecting `FAIL unexpected: b`, naming this item. Observed by AC14.
- **S15** — id 24. The moved runner told to the builds that cite it. This unit's return carries two
  ask rows, one for `memory/builds/dDeclaredLoop/BACKLOG.md` (TOOL-dDeclaredLoop-67 S22 cites
  regen.py's runner at `:249-301`) and one for `memory/builds/dWitnessedBar/BACKLOG.md`
  (TOOL-dWitnessedBar-57 S5 cites `:279`), each naming the `run_bounded_py` block as the canonical
  runner and regen.py's line ranges at this pass; the main loop files them, as the build README's
  writes rule allows. Observed by AC15.
- **S16** — id 28. The absence arms catch the class. The three `miss` arms of unit 38 S2 take the
  needle `--for-diff HEAD~1` over their same haystacks, so a per-pass line restored as `python3`,
  under another root or with another range spelling still fails, and unit 42 AC1's count of `miss`
  lines holding `for-diff HEAD~1` stays 3. Observed by AC16.
- **S17** — id 30. The block kills on any exception. After its `except subprocess.TimeoutExpired`
  branch the block's wait carries `except BaseException: run_tree_kill(proc); raise`, the contract
  `subprocess.run` kept, in the canonical and every copy. Observed by AC17.
- **S18** — id 33. One runner, by every import form. Unit 42 AC13's walk flags every call outside the
  block's line range whose callee resolves to the `subprocess` module by any form, `subprocess.<attr>`,
  a name bound by `from subprocess import`, or an alias of `import subprocess as`, and every
  `os.system` and `os.popen` call; unit 42's ledger answers AC13 in the AMENDED form, naming this item.
  Observed by AC18.

## 3. Non-goals (OUT)

- The HIGH findings of the same report: `TOOL-dFurnishedOrders-43` and `-44`.
- The 8 govkit upgrade-step minors: `TOOL-dFurnishedOrders-45`.
- Rewording the spec text of units 37 to 42: each item states the built tree's end state, and where a
  landed criterion cannot hold as written, that unit's ledger answers it AMENDED, naming the item.
- Writing another build's `BACKLOG.md` in this pass: S15's rows go back to the main loop, so no pass
  of this build touches a shard M6 clause 3 names.
- The report's left-shift gates, the spec-lint, parity-row and checklist entries: no clause of this
  build names them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-37` — AC8's first arm and S17's re-stamp, which S2 and S1 settle (ids 3, 2)
- **consumes-from** `TOOL-dFurnishedOrders-38` — the `miss` helper, its failure text, its three arms and the offender key it mints, which S7, S14 and S16 settle (ids 20, 19, 28)
- **consumes-from** `TOOL-dFurnishedOrders-39` — the `run_bounded_py` block, `run_slot_reader` and the run-gates version move, which S1 to S3, S9 to S13, S15 and S17 settle (ids 2, 3, 8, 29, 4, 11, 12, 17, 24, 30)
- **consumes-from** `TOOL-dFurnishedOrders-40` — the govkit selftest arm whose sibling reads S8 guards (id 22)
- **consumes-from** `TOOL-dFurnishedOrders-41` — the govkit selftest arm whose sibling reads S8 guards (id 22)
- **consumes-from** `TOOL-dFurnishedOrders-42` — S2, S3, S7, S14, S17, S19, AC2, AC4 and AC13 and its staged breaks, which S1, S2, S4 to S6, S10, S12 and S18 settle (ids 2, 3, 10, 15, 16, 4, 12, 33)
- **consumes-from** `TOOL-dFurnishedOrders-43` — the govkit selftest arm whose sibling reads S8 guards (id 22)
- **consumes-from** `TOOL-dFurnishedOrders-44` — the `apply --all` arm whose registry descriptors S8 guards (id 22)
- **consumes-from** external — TOOL-dWitnessedBar-11's `leg_factory.py` and the `[[exempt_leg]]` declaration S8's rows go on, and the lexicon kit's `--self-containment` mode, an ask (§8 F7), each unbuilt at `1a61f21a2`
- **hands-off** `TOOL-dFurnishedOrders-48` — S1's re-stamp, AC1, S8's guard rows and AC8, which unit 48 S1 to S3 and S14 to S18 settle (ids 1, 12, 23, 9, 35, 21, 11, 28 of the fifth audit)
- **hands-off** `TOOL-dFurnishedOrders-49` — Files touched, the dispatch row, S4's reading, AC4's bound and AC17's interrupt probe, which unit 49 S1 to S6 settle (ids 6, 27, 7, 16, 20, 26 of the fifth audit)
- **hands-off** `TOOL-dFurnishedOrders-51` — AC17's interrupt arm, whose stub, pid and liveness read unit 51 S1 to S3 pin (id 24 of the sixth audit)

## 4. Design

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so, as `TOOL-dFurnishedOrders-41` §4 does. Why this half is disjoint from
unit 45 is `TOOL-dFurnishedOrders-45` §4 "Why two units", stated once there; this half holds every
watched edit of the batch, so its S1 re-stamp is the build's last.

### The block, after this unit

```python
# >>> run_bounded_py -- canonical copy: run_bounded.py in gov's lib dir (byte-identical; gated)
import os                                                       # S9
import signal
import subprocess
import tempfile
def run_tree_kill(proc): ...                                    # unit 39, unchanged
def run_bounded(argv, cwd, bound, env=None, merge=False):
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        proc = subprocess.Popen(...)                            # unit 39 S1, unchanged
        try:
            status = proc.wait(timeout=bound)
        except subprocess.TimeoutExpired:
            run_tree_kill(proc); status = "TIMEOUT"
        except BaseException:                                   # S17
            run_tree_kill(proc); raise
        ...                                                     # read and decode, unit 39 S1
# <<< run_bounded_py
```

### The roles runner, after this unit

```
run_slot_reader(argv, root, bound=30, env=None)                                   S10
  status, out, err := run_bounded(argv, root, min(bound, ROLES_SLOT_BOUND), env)  unit 42 S17
  out, err        := each with "\r\n" then "\r" turned to "\n"                    S3
derive_attended   := posture read with env = os.environ + PYTHONUTF8, PYTHONIOENCODING
```

### The census runner, after this unit

```
run_backend(argv, timeout)  := run_bounded(argv, None, timeout)
  TIMEOUT -> CensusRefused("<argv0>: did not answer within <timeout>s")
  OSError -> CensusRefused("<argv0>: not runnable (<error>)")
  else    -> stdout
```

### Inventory

Minted: the census wrapper name `run_backend`, whose leading token `run` is a VERBS member; the
`tracked` keyword is unit 45's, not this unit's. No flag, key or file. `VERB_OFFENDER_PIN` moves by
S7 for the names units 38 to 46 minted.

### Migration

None: no stored data changes shape, and every caller of the block keeps its return shape.

### Rollout

Live at landing, at order 26, after every unit it lands on and beside unit 45. `KIT_RUN_GATES_VERSION`,
`KIT_ROLES_VERSION`, `KIT_PROCESS_MONITOR_VERSION` and the unattended kit's version move for the kit
epoch leg where their shipped bytes move; S1's re-stamp lands after the last of them.

### Files touched (estimate)

- `tools/lib/run_bounded.py`
- `tools/run-gates/regen.py`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/selftest-budgets.txt`
- `tools/roles/roles_lib.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/process-monitor/census.py`
- `tools/process-monitor/selftest.py`
- `tools/process-monitor/adopt-process-monitor.sh`
- `tools/unattended/adopt-unattended.test.sh`
- `tools/unattended/unattended.sh`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`, or hand-edited where it is not built)
- `.lexicon.conf`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Re-stamp inside unit 39 (S1).** Units 39 and 42 and this unit each move a watched path later, so a
  stamp at order 24 is stale by order 26; one re-stamp after the last is the rule unit 37 S17 states.
- **Normalise newlines inside the block (S3).** It changes `regen.run_command`'s bytes, which unit 39
  S2 promises unchanged.
- **Name the four imports in each host file (S9).** A copy that forgets one passes the parity row,
  which compares only the text between the markers; imports inside the markers travel with it.
- **Record census's runner as a non-goal and keep its name (S13).** Two Python functions named
  `run_bounded` with different signatures stay, and census keeps the pipe the block avoids.
- **Inline `check_self_containment` into the roles kit (S5).** It copies the lexicon kit's predicate
  and its extractor, the second copy id 15 found; the suite runs the one predicate by §8 F7's verb.

## 5. Production-readiness checklist

- security — S17 leaves no child alive behind an interrupted caller; S13 adds two anonymous temp files
  per census call, deleted on close.
- perf / scale — S4 prices the suite from readings; S13 returns at the census child's exit.
- error / empty / loading states — S13 keeps census's two refusals and their texts; S3 gives every
  slot read one line ending.
- observability — S7's dated comment names each arrived key; S8's guard rows name each file read.
- risks — S8 makes an edit to any kit descriptor select the `govkit selftest` leg on a scoped bar,
  which is the cost of a guard that sees what its arms read.
- testing — AC1 to AC18 by probes and fixtures; the arms of §7 at the close.
- migration — none.
- user docs — none: no user-facing step changes.

## 6. Acceptance criteria

- **AC1** — When `git merge-base --is-ancestor` runs with the commit `git log -1 --format=%H --
  tools/run-gates/run-gates.sh tools/gate-legs.json skills/session-kickoff/manifest-check.sh` prints
  and the sha on `memory/guides/SESSION-KICKOFF.md`'s `last-audit:` line, it exits 0.
  Red when: a watched edit of units 39 or 46 lands after the re-stamp.
- **AC2** — When `python -c` reads the line range between `# >>> run_bounded_py` and `# <<<
  run_bounded_py` in `tools/roles/roles_lib.py` and checks every line `git grep -n -E
  "subprocess\.(run|Popen|check_output|call)\(" -- 'tools/roles/*.py'` prints, it prints no line
  outside that range.
  Red when: a roles subprocess call sits outside the shared block.
- **AC3** — When `python -c` calls `roles_lib.run_slot_reader` on a Python stub that prints
  `attendance — ask-live`, the text it returns holds no `\r`; and `roles_lib.derive_attended` over a
  stub `breakpoints.py` printing that line reads the posture as exactly `ask-live`.
  Red when: a CR-terminated line reaches a `$`-anchored parse and the posture takes `ask-live\r`.
  fixture: stub files under `%TEMP%`.
- **AC4** — When `grep -n "^roles adopter self-test" tools/run-gates/selftest-budgets.txt` runs, its
  row's budget is at least the ceiling of 1.5 times 51.124 plus the added sleep S4 sums, and its note
  names the gate ledger and holds no `not measured`.
  Red when: the row stays a declaration nobody timed.
  figure: 51.124 is PINNED, read 2026-10-27; the added sleep is DERIVED from the arms at the pass.
- **AC5** — When `python tools/lexicon/lexicon.py --self-containment tools/roles` (§8 F7's verb)
  runs, it exits 0 and prints a judged count above zero; on a scratch copy of `tools/roles/` whose
  `handoff.py` gains `import gov_map`, it exits 1 naming `handoff.py` and `gov_map`; and no line
  `git grep -n -E "tools/lexicon|lexicon\.py" -- tools/roles/adopt-roles.test.sh` prints is a
  `sys.path` insert or an `import`.
  Red when: a sibling import passes, the walk judges nothing and reads green, or the suite loads the
  lexicon kit in process.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`.
  cost: observed once §8 F7's verb lands; until then the pass records the ask open and AC5 owed.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs on the tree at this unit's pass,
  it prints no line holding `watched files changed since last-audit`.
  Red when: a re-implemented predicate reads green while the ratchet is red.
  permission: the command is the `kickoff-manifest ratchet` leg's argv; where the builder role's hook
  refuses it, the pass returns this observation to the main loop and AC1 is its in-pass evidence.
- **AC7** — When `python tools/lexicon/lexicon.py --offenders` runs, the count of rows whose second
  field is `verb` equals the `VERB_OFFENDER_PIN` value of `.lexicon.conf`.
  Red when: a minted helper moves the count and the pin stays.
- **AC8** — When `python -c` reads the `govkit selftest` row of `tools/gate-legs.json`, its guard holds
  every file S8 names, and `git ls-files --error-unmatch` finds each with `{prefix}` resolved to
  `tools`; where `tools/run-gates/leg_factory.py` is built at the pass, `python
  tools/run-gates/leg_factory.py --check` exits 0.
  Red when: a sibling file an arm reads is outside the guard, or a guard row is typed into the
  manifest that its declaration does not carry.
- **AC9** — When `python -c` extracts the `run_bounded_py` block from the canonical run_bounded.py,
  `tools/run-gates/regen.py`, `tools/roles/roles_lib.py` and `tools/process-monitor/census.py`, parses
  each with `ast`, and lists every loaded name bound neither inside the block nor in `builtins`, it
  lists nothing; with `import signal` taken out of a scratch copy of the block, it lists `signal`.
  Red when: a copy reaches `signal` only on POSIX and raises `NameError` there.
- **AC10** — When `python -c` inspects `roles_lib.run_slot_reader`, its signature carries `env`; and a
  call with `env` holding `PYTHONUTF8=1` on a stub printing that variable returns `1`.
  Red when: the posture read's environment cannot reach its child.
- **AC11** — When `grep -n "CARD_MAP_BOUND=" skills/session-kickoff/manifest-check.sh` runs it prints
  the default line, and `grep -n -E "\\$\\(.*gov_map" skills/session-kickoff/manifest-check.sh` prints
  nothing.
  Red when: the map renderer's output is captured by a `$( )` a grandchild can hold.
- **AC12** — When `git grep -n -e "python -B" -- memory/builds/dFurnishedOrders/` runs after the
  close's RED-first rows are recorded, each arm of units 39, 42 and 46 staged on a `.py` file has a
  row naming it, `-B` and the check its break targets.
  Red when: a RED is read from stale bytecode or from a neighbouring check.
  cost: observed at the close, after the main loop records the arms.
- **AC13** — When `git grep -n "^def run_bounded" -- '*.py'` runs, every line lies inside a
  `run_bounded_py` block; and `python -c` calling `census.run_backend` on a 30-second Python sleeper
  with `timeout=2` raises `CensusRefused` naming `did not answer` within 10 seconds, and on a program
  that does not exist raises `CensusRefused` naming `not runnable`.
  Red when: two Python `run_bounded` meanings remain, or census loses a refusal.
- **AC14** — When the line `sed -n 145p tools/unattended/unattended.test.sh` prints is matched whole
  by `grep -c -x -F` over the unattended adopter suite, it prints 1.
  Red when: the suite carries a fourth `miss` with its own failure text.
- **AC15** — When `git grep -n "run_bounded_py" -- memory/builds/dDeclaredLoop/BACKLOG.md
  memory/builds/dWitnessedBar/BACKLOG.md` runs after the main loop files S15's rows, it prints one
  line in each file.
  Red when: a deferred build still copies the runner from a stale line range.
  cost: observed after the main loop's filing, not inside this pass.
- **AC16** — When `git grep -h -e "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh`
  runs, it prints three lines, each opening `miss ` and passing the needle `--for-diff HEAD~1`; and
  `bash -c` evaluating the suite's `miss` line on the haystack `python3 x/gotchas.py --for-diff
  HEAD~1..HEAD` with that needle prints `FAIL unexpected:`.
  Red when: a per-pass line restored under another spelling passes the arms.
- **AC17** — When `python -c` patches `subprocess.Popen.wait` so its first call raises
  `KeyboardInterrupt`, then calls the canonical `run_bounded` on a stub that writes its pid to a file
  and sleeps 60 seconds, the `KeyboardInterrupt` reaches the caller and the stub's pid is gone within
  15 seconds.
  Red when: an interrupted caller leaves its child running.
  fixture: a stub script and a pid file under `%TEMP%`.
- **AC18** — When unit 42 AC13's walk runs over `tools/roles/*.py` it prints nothing; over a scratch
  copy whose `handoff.py` gains `from subprocess import run as r` and a call `r(["x"])`, it prints that
  call; and with `os.popen("x")` instead, it prints that call.
  Red when: an unbounded child started through an import alias or `os.popen` passes the gate.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `roles catalogue` · `roles adopter self-test` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` · `run-gates run-log line` · `measure-legs selftest` · `process-monitor census selftest` · `process-monitor adopter selftest` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `kickoff-manifest ratchet` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `unattended kit gate` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC9 · the `run_bounded_py` row over four copies, each carrying the imports and the `BaseException` branch, and an unbound-name `ast` pass over the canonical block, staged by taking `import signal` out of one copy after deleting `tools/lib/__pycache__` and running Python with `-B` · none
New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC5 AC10 AC17 AC18 · a CRLF posture stub, the lexicon kit's self-containment verb run over the roles kit, an env-carrying slot read, a patched wait raising `KeyboardInterrupt` and an aliased `subprocess` import, staged by restoring the raw decode after deleting `tools/roles/__pycache__` and running Python with `-B` · none
New arm: tools/process-monitor/selftest.py · covers AC13 · `run_backend` over a sleeper and a missing program, staged by restoring the pipe-backed runner after deleting `tools/process-monitor/__pycache__` and running Python with `-B` · none
New arm: tools/unattended/adopt-unattended.test.sh · covers AC14 AC16 · the kit's `miss` spelling and the class needle, staged by re-adding the per-pass line as `python3` under another root; the suite stays WAIVED at landing by the build README's rule, its arm owed with PLAY-dClosedLoop-18 · none

The close also reads the `roles adopter self-test` leg's time on its bar run as S4's measurement, and
the `kickoff-manifest ratchet` leg as S1's.

## 8. Open questions

- **F1 — How many units do the minors take?** RESOLVED (agent, 2026-10-27, delegated): two, by
  `TOOL-dFurnishedOrders-45` §8 F1, rung 1, BUILD-METHOD M4's two-unit clause. widens: none · relaxes:
  none
- **F2 — What becomes of census's same-named runner (S13)?** Options: (a) census carries the canonical
  block and its wrapper takes another name; (b) a recorded non-goal, census keeping its name and its
  pipe; (c) the canonical block takes another name. (b) keeps two meanings of one name and the pipe;
  (c) re-spells three copies and their callers for a name census holds. RESOLVED (agent, 2026-10-27,
  delegated): (a), rung 3, the skeptic-judged first fix of id 17, the most feature-rich survivor.
  widens: none · relaxes: none
- **F3 — Where do the block's imports live (S9)?** Options: (a) inside the markers; (b) named in each
  host file with an unbound-name check. (b) leaves a copy the parity row cannot see short of an
  import. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged first fix of id 29
  and the `health_log_py` precedent. widens: none · relaxes: none
- **F4 — How is the roles suite's budget set without running the suite in a pass (S4)?** Options: (a)
  derived from the gate ledger's worst reading plus the added arms' declared sleep, the close's bar
  reading confirming it; (b) timed by running the suite in the pass. (b) is a suite run a pass may not
  make (BUILD-METHOD M6). RESOLVED (agent, 2026-10-27, delegated): (a), rung 1, M6's pass rule.
  widens: none · relaxes: none
- **F5 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F6 — The units this one lands on are unbuilt.** Units 37 to 44 are specced and unbuilt at
  `47d3a464`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on each at the pass and
  records any item a landed unit already closed, rung 1, the brief's rule. widens: none · relaxes: none
- **F7 — How does the roles suite reach `check_self_containment` (S5)?** A kit imports no sibling kit
  (TOOL-dGroundRules-1 §4, PLAY-dOrderedCharter-7 §4), and a `sys.path` insert of another kit's
  directory is such an import. `lexicon.py`'s modes (`tools/lexicon/lexicon.py:4358-4360`) take no
  kit directory, and its own run walks only its own (`:2867`); `project-owned`
  (`tools/roles/kit.toml:46-48`) withholds the suite and declares no edge. Options: (a) an ask of the
  lexicon kit, a `--self-containment <kit-dir>` mode printing the problems and judged count
  `check_self_containment(kit_dir)` returns and exiting 1 on any problem, which the arm runs by
  subprocess; (b) a declared `requires_if` row on `tools/roles/kit.toml` naming `lexicon`, admitting
  the in-process load as a DECLARATION `govkit selfcheck` grades, as the review-harness row does
  (`:19`); (c) unit 42 §4's own `ast` walk kept as the gate and S5 dropped. (c) keeps the copy of the
  predicate id 15 found; (b) declares to every adopter an edge only a withheld file holds, which the
  review-harness precedent, an edge held wherever `/build` is used, does not admit; (a) is one mode
  over a function that already takes its walk root as a parameter, and its cost is a wait, since AC5
  passes only against the landed mode. Recommendation (a). Open for the owner: the ask the build run
  files, on the build that owns `tools/lexicon/` at the pass, is "`lexicon.py --self-containment
  <kit-dir>` prints `check_self_containment(kit_dir)`'s problems and its judged count, exiting 1 on
  any problem".

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-3 promotions' roles, run-gates,
  process-monitor, unattended, kickoff and gate-manifest minors batched: 9 MEDIUM and 9 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-48, TOOL-dFurnishedOrders-49, promoted from the spec audit of the round-4 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-51, promoted from the spec audit of the round-5 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`); nothing else moved.
- rev-4 · 2026-10-28 · §2 S1, S5, S8 · §3 Edges · §4 Files touched, Alternatives rejected · §6 AC5,
  AC8 · §7 the leg line, which gains `govkit refusal join` for the registry's `{prefix}/govkit/`
  guard, and the roles arm · §8 F7 · re-grounded on TOOL-dWitnessedBar-11 and the sibling-kit rule
  (TOOL-dGroundRules-1 §4, PLAY-dOrderedCharter-7 §4), by the cross-check record
  `build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`, rows 122 and 123: S8's
  guard rows go on the `govkit selftest` `[[exempt_leg]]` declaration and are rendered by
  `leg_factory.py --write`, a recorded hand edit standing in where it is not built; S5's check runs
  through a lexicon verb by subprocess, and F7, open for the owner, is the ask for it; nothing else
  moved.

## 10. Reuse audit

The seams extended: unit 39's `run_bounded_py` canonical and its parity row
(`tools/lib/resolve-python.test.sh:168-187`), into which S9, S13 and S17 fold; the `health_log_py`
block's in-marker imports (`tools/lib/health_log.py`) for S9; `check_self_containment`
(`tools/lexicon/lexicon.py:2359`) for S5; the ratchet checker (`skills/session-kickoff/manifest-check.sh`)
for S6; the kit's existing `miss` (`tools/unattended/unattended.test.sh:145`) for S14; unit 37 S17's
re-stamp rule for S1. `python tools/codebase-map/reuse_lookup.py "run a child under a bound and kill its
tree on any exception"` ranked `tree`, `run`, `run_git` and `run_arms`, name-token neighbours none of
which is a bounded runner, so the canonical block is the seam. The recall probe returned
KICK-dKeptSession-44, -56, -62, -64 and -65, minors batches closed after the units they land on, and
units 29 and 42, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the fourth
dFurnishedOrders spec audit land on the roles run-gates and unattended kits" --terms "minors batch
run_bounded_py census re-stamp ratchet VERB_OFFENDER_PIN miss needle CRLF self-containment budget
guard"`

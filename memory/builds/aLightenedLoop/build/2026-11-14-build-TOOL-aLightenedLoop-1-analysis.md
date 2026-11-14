**Serves:** research TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5

# Where a build unit's fixed overhead goes: the slowdown audit behind this build

These figures come from the dSafePassage session `c5f50d22` (about 102 units, plus 4 of dPavedRoad), <!-- PINNED 2026-11-14 -->
which covered 157 workflows and 469 agents. They were re-timed on `main` 846d51d39 on node `a` beside a
live run, so read every wall time as about ±2×. The instruments are the scripts `slow.py`, `slow2.py`
and `slow3.py`, each run as `python -B <script> <session-dir> <out>`. Their outputs are `slow.txt` and
`slow2.txt`, in that session's scratchpad on node `a`, and the auto-memory note
`slowdown-audit-2026-11-14` carries the same summary.

**Builders.** The median builder ran 17.6 min: 9.6 min before its first product edit and 5.1 min after
its last. Summed over 101 builders, the overhead is about 31 h.

## 1. The commit tail (about 17 h)

- `gen_build_index.py --write` takes 68–106 s. On an idle re-render it rewrote all 3,206 artifacts <!-- PINNED 2026-11-14 -->
  while none changed content, because `write_text` (line 296) opens every file `"wb"`. Those writes
  cost about 12 s by cProfile, and the `git status` after them about 3 s more. <!-- PINNED 2026-11-14 -->
- A cProfile of `--write` at 92 s: `plan` (line 2700) 83 s; `read_carries_coverage` (line 1990, through <!-- PINNED 2026-11-14 -->
  `check-spec-tokens.py`'s `derive_carries_coverage` at 1122 and `read_carries_specs` at 952) 35 s; <!-- PINNED 2026-11-14 -->
  `collect` (line 1107) 33 s; and 52 git spawns, about 24 s. <!-- PINNED 2026-11-14 -->
- The pre-commit hook took about 230 s on a one-line append to a ledger under <!-- PINNED 2026-11-14 -->
  `memory/builds/dPavedRoad/build/`. Check 9 ran `--check --staged` for 67 s and printed a full render. <!-- PINNED 2026-11-14 -->
  Check 29 ran `--check-coverage --staged` for 34 s to report that it graded nothing. <!-- PINNED 2026-11-14 -->
- Why check 9's staged skip did not fire: `check_index_input` (line 895) classes any path under a
  build's `spec`, `build`, `prompts` or `reviews` folder as structural (line 927), because the
  renderer reads those records' headers, bindings and filenames. So every edit there renders,
  whatever it changes.
- A builder therefore renders the index twice per commit: once by its own `--write`, and once inside
  the hook.

## 2. Idle-wake ticks (about 24.5 h of main-loop time)

- 666 tick turns averaged 132 s each and produced 795k output tokens in total. <!-- PINNED 2026-11-14 -->
- `unattended.sh --resume` ran 483 times for 370 min: a median of 12 s on its own, and about 72 s <!-- PINNED 2026-11-14 -->
  when paired with `--audit`.
- Most ticks fired while a harness-tracked Workflow was running, and that Workflow notifies the
  session itself when it finishes. Because the main loop takes one turn at a time, a tick also delays
  the handling of those notifications.
- The cadence is the conf key `KEEPALIVE_INTERVAL` (`tools/unattended/.unattended.conf.example`, cron
  `3-59/10`). It is set by the `/unattended` Skill's "schedule the idle-wake NOW" step and by the
  unattended protocol, and `verb_resume` sits near line 9335 of `unattended.sh`.

## 3. `--dispatch` inside the builder (about 19 h; partly fixed since)

- The session made 229 calls, with a median of 5.3 min. Its 50 refusals took the same 5.4 min each, <!-- PINNED 2026-11-14 -->
  and 45 calls ran past the 120 s tool default and were moved to the background. <!-- PINNED 2026-11-14 -->
- aSwiftRefusal, aSmoothedDispatch and aBatchedPacket have since landed cheap refusals first, a check
  scoped to the dispatching build's specs, and no packet history walk.
- Still open on 846d51d39: `run_spec_token_check` (line 14458) takes 62 s today. Its cache key
  (aSmoothedDispatch unit 4, S2) includes HEAD, so every pass commit invalidates it and every unit
  of a sequential run misses.
- The builder runs `--dispatch` itself, from the `DRIVER_STEPS` text in `unattended-unit.js`, so a
  refusal costs a spawned builder plus its orientation. dSafePassage units 16 and 29 each lost 5–6
  min this way.

## 4. Rework from diverged units (about 8 h of builders, plus spec rounds)

- 23 unit runs diverged and 4 more ended uncommitted, about 481 min in total. 17 of 41 units needed <!-- PINNED 2026-11-14 -->
  more than one spec-writer round, for 66 spawns. dSafePassage unit 5 took 6 dispatches and 6 spec
  rounds, about 4 h of builders, and builders ran 50–100 min before diverging.
- The causes, by run: the spec contradicts itself, about 9; the spec claims behaviour the current code
  lacks, about 5; the fix needs files outside the declared list (other specs, a manifest re-stamp,
  `memory/DECISIONS.md`), about 4; a refusal found inside the builder, about 4; the environment or
  build order, about 2.
- The builders' own reasons are the `why` fields of that session's `workflows/wf_*.json` run records.

## 5. Stop-guard liveness (about 2.7 h)

- `tools/unattended/stop-guard.js` spawns `bash unattended.sh --liveness <slug>` (`runLiveness`) on
  every Stop. The session had 1,028 Stops at an average of 9.3 s. Today the spawn takes 13 s on a live <!-- PINNED 2026-11-14 -->
  run and 5 s on an attended slug. <!-- PINNED 2026-11-14 -->

## 6. Overlap with the chain builds, checked at kickoff

- dWellOiledMachine is DEFERRED. Its units 28, 10, 21, 31 and 64 move `stop-guard.js` and the tick
  into a runtime kit or into hook packs. They share files with this build, not mechanisms, and they
  re-ground on this build once it lands.
- dTendedCadence has no overlap.
- The live dDeclaredLoop run branch has changed `unattended.sh` and the hygiene script (its units 5 and
  23), so a reconcile is expected at landing.

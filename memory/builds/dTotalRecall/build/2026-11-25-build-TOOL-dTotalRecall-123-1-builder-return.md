**Serves:** journal TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-123

# TOOL-dTotalRecall-123 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `b4d582a2d` from [2026-11-25-prompt-TOOL-dTotalRecall-123-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `b4d582a2d`.

## Why

DIVERGENCE: the design (§2 S1-S3, §4) builds as written. Two acceptance criteria can never read as stated, and two passages contradict this dispatch. Please revise all of these together.

(1) §6 AC4. Its grep `twin (difference|runs)|"twin"` over `tools/workflows/README.md` is required to print nothing. That README, in the twin-run paragraph, spells the harness line `review-twin runs=2 a=<first>-<last> ...`, which matches `twin runs`. It was already there at base `fbe06249`; it entered at `ef757de0c`, TOOL-dFairHearing-11. It documents what `tier2-review.js` renders and is outside this unit's scope. With the draft applied, that is the one line the grep still prints. §6 AC4 would have to grep e.g. `twin difference|twin runs'|"twin"`, or exempt the `review-twin runs=` line by name. (DERIVED 2026-11-25, the pass)

(2) §6 AC5, second half. `grep -l` of "this build's folder" for `Bound:** the twin runs' difference as the recall term's noise` must name "that one file". The spec itself spells that exact string inside AC5 and lives in the build folder. With the record written in scratch clone rf2, the grep named two files: `build/...-123-deviation-1021.md` and `spec/2026-10-26-spec-TOOL-dTotalRecall-123.md`. A ledger line quoting the string would be a third. §6 AC5 would have to scope the grep to `memory/builds/dTotalRecall/build/` and anchor it at `^- \*\*Bound:`.

(3) §6 AC5, first half. `deviations.py --policy report` did not return within 600 s on node a (a foreground run over rf2 holding the record hit the bound; a background run started earlier had also printed nothing). AC5 would have to be marked as the main loop's or close-owed with a cost, or name a cheaper reader. `deviation_join.py#read_record` over the record returned `malformed: []` at once. (DERIVED 2026-11-25, the pass)

(4) §4 Rollout and §2 S5, against the task and brief. Rollout says the builder lands S1 to S4, the main loop does S5 to S7, "and the unit closes on the verdict record". S5 says the main loop commits the manifest after the scorer's pass commit. The task and brief order this pass to commit the manifest too, as one pass commit, and to flip the header to CLOSED in it, before any run and so before S6, S7 and AC6 to AC8. Unit 17 met the same conflict; its builder left INPROGRESS at `30c21c834` and the main loop closed it at `cb97caf03`. §4 Rollout and S5 would have to say one of two things. Either the pass commits the manifest with the scorer and closes, the runs and verdict being a main-loop act (or another unit's) after CLOSED. Or the header stays INPROGRESS until the verdict commit, in which case the brief and task must say so and allow a manifest commit after the scorer's. (DERIVED 2026-11-25, the pass)

Minor, for the same revision: S5 gives no value for the manifest's `map` key before the runs. The key is required by `INSTANCES["map-replay"]["manifest"]`. `null` works: the instance then refuses `map None: not a source of a non-empty map`, exit 2. §2 S5 should name it.

## Summary

Nothing is committed, and no product path in the worktree was changed. The worktree holds only the main loop's staged memory/builds/dTotalRecall/RUN.md, as I found it. The brief was already recorded at 5802519c2c45.

The draft is complete and checked. It is in C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u123b/ :
- `draft.patch`: `tools/workflows/replay_scorer.py` and `tools/workflows/README.md`. `git apply --check` passes at `b4d582a2d`.
- `manifest.json`: the pre-run manifest, `dispatched` 15 per arm, `candidates` empty, `map` null. (DERIVED 2026-11-25, the pass)
- `rf2.sh`: the deviation door call with every §4 field. It wrote number 1021 in the clone. (DERIVED 2026-11-25, the pass)
- `probe.py` and `mut.py`: the probes.

Probe results (DERIVED 2026-11-25). They stand in for the `review-replay selftest` leg; no suite or gate ran:
- AC1: the two `term recall` lines read exactly as §4 says. (DERIVED 2026-11-25, the pass)
- AC2: refused with the counts named for a dropped run, two declared counts, 5 over two audits, one run, and one run too many. The complete set returns lines. (DERIVED 2026-11-25, the pass)
- AC3: the win and lose boundaries hold, and `measure_rise_noise` over the first record's six pairs reads 15.46.
- AC4: the grep prints only the unrelated `review-twin runs=` line.
- `map-verdict`, `map-experiment`, `map-noise` and `map-known`, cut out of `run_selftest`, all answer None.
- Staged breaks in scratch copies: `map-noise` reds on the range put back, on the division cut and on the exact-count refusal cut. `map-verdict` reds on the margin read alone. The formal RED-first observations are still owed to the close.

Claims checked true: the §4 table and spread (73, 46.5, 59.75, 7.73), `ARMS_DECLARED` 33, no caller of `statistics.variance`, `stdev` or `pstdev` under `tools/`, and the `cl-dClosedLoop-0228` clause text. `--suggest` admits `measure_rise_noise`, `check_map_noise_arm` and `build_map_manifest`. The deviation record is well-formed by `deviation_join.py#read_record`. (DERIVED 2026-11-25, the pass)

Not returned within its bound: `deviations.py --policy report` over C:/Temp/rf2 for AC5. Two runs were started, the second in the foreground at 600 s; both are abandoned and I will not re-run them. One scratch commit, `31fd71c72`, sits on a detached HEAD in C:/Temp/rf2. (DERIVED 2026-11-25, the pass)

Owed after re-dispatch: the commit itself, `gen_map.py --write`, the build-index render, the ledger and the gotchas checklist.

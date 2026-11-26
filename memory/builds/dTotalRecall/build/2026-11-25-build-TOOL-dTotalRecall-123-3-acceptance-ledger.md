# TOOL-dTotalRecall-123 — acceptance ledger, build pass 3

**Serves:** log TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-123

No merge bar, no self-test suite and no gate leg in this pass. The builder built S1 to S5 of spec rev-3 over base
`688a6f195cff2b4b1ac8f1d9de968d6d0731cf23`, 2026-11-26 local, in one commit, the header left `INPROGRESS` as §4 "Rollout"
has it. S6 and S7 are the main loop's. §7's legs and the RED-first observation of both `New arm:` lines are owed to the
close; the lexicon's `--measure` read its offender pin unmoved.

**Evidences:** TOOL-dTotalRecall-123
- AC1 — `check_experiment` — over the seven-item fixture the two `term recall` lines ended `noise 5.65685 at 2 run(s) per arm · loses below 10.6569` and `noise 4.16333 at 4 run(s) per arm · loses below 9.16333`; the arm `map-noise`, cut out of `run_selftest`, answered None, and in scratch copies it named the failure with the range put back and with the division by the count cut (DERIVED 2026-11-26, the probe).
- AC2 — `Refusal` — one run of four dropped read `3 parsed run(s), not the 4 the manifest declares`, two declared counts `dispatched 4, 5 over 1 audit(s)`, 5 declared over two audits `dispatched 5 over 2 audit(s)`, one run `dispatched 1 over 1 audit(s)`, and one run past the declared count `3 parsed against 2 dispatched`; the complete set returned lines, and `map-noise` named the failure with the exact-count refusal cut (DERIVED 2026-11-26, the probe).
- AC3 — `derive_map_verdict` — `map-verdict`, cut out of `run_selftest`, answered None, so the boundary set read `win` and a rise of 4, and `noise` 1 with a rise of 5, each lost `recall` alone; with the comparison reading the margin alone it named the failure; `measure_rise_noise` over the first record's six pairs read 15.46 (DERIVED 2026-11-26, the probe).
- AC4 — `grep -nE "twin difference|twin runs'|\"twin\"" tools/workflows/replay_scorer.py tools/workflows/README.md` — printed nothing, and the README's `map-replay` paragraph names `measure_rise_noise`, `NOISE_FACTOR` and the count rule (DERIVED 2026-11-26).
- AC5 — `deviation_join.py#read_record` — over deviation 1021 its `malformed` is empty, its `address` is `TOOL-dTotalRecall-17@rev-3`, its `follow` is `ask TOOL-dTotalRecall-111` and its `bound` is the `relaxes:` value of F1, and the anchored `grep` named that one file (DERIVED 2026-11-26).
- AC6 — `run.log` — OWED to the main loop at the verdict commit.
- AC7 — `python tools/workflows/replay_scorer.py --experiment <manifest>` — OWED to the main loop at the verdict commit.
- AC8 — `git log` — OWED to the main loop at the verdict commit.
- AC9 — `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dTotalRecall` — OWED to the close, on the prepared merge.
- AC10 — `python tools/workflows/replay_scorer.py --experiment <manifest>` — over the manifest this pass adds, its `candidates` empty, `map` null, both `dispatched` 15 and `known` equal to the first manifest's, it exited 2 printing `map None: not a source of a non-empty map` (DERIVED 2026-11-26).

# Acceptance ledger — TOOL-aNimbleMend-13

**Serves:** journal TOOL-aNimbleMend-13

Built against spec rev-2 in one pass commit. Each line is a probe of the changed code the builder made in the pass. No suite, gate leg, pass-leg run or bar ran in the pass. Owed to the main loop at the close: AC1, AC2, AC7 and AC9, the legs of the spec's Gates section, and the RED-first observation of the spec's two new arms, in `tools/run-gates/run-gates.test.sh` (arm 14a2) and `tools/run-gates/run-gates.evidence.test.sh` (the kit-subject arms).

**Evidences:** TOOL-aNimbleMend-13
- AC1 — `gate-pass-legs.txt` — observed by the main loop at the pass commit `cb1ee1c51`: the pass-leg run's record read `ok` on the `leg` line of each of the three list-reading legs, its `held` key read 0, and the output held no line opening `pass-legs: FINDING held`. The run took 199 s and redded 2 of 29 legs, `docs` and `drift-audit records`, neither one of the three. (PINNED, 2026-11-12)
- AC2 — `gate-pass-legs.json` — observed by the main loop after AC1's run: the criterion's command printed `29 29`. (DERIVED from the file)
- AC3 — `kit-subject kit-subject` — the criterion's command printed exactly that line.
- AC4 — `would hold it` — the criterion's command printed a list of one string holding the phrase.
- AC5 — `python tools/run-gates/pass_legs.py --check` — after `--apply`, which took the field off one row of the manifest, `--report` opened the resolver leg's line with `kit-subject`, `--check` exited 0, and `--budget` exited 0 on a last line opening `pass-budget:` that names the budget.
- AC6 — `GOVKIT_RERENDER` — the criterion's grep over the descriptor printed 1.
- AC7 — `python tools/govkit/govkit.py selfcheck` — observed by the main loop at `cb1ee1c51`: it exited 0 and no line of its output named the kit's descriptor.
- AC8 — `remove_pass_field` — the grep for `def strip` printed 0, the grep for the new name printed 2, and the diff of `.lexicon.conf` against HEAD printed nothing before the commit.
- AC9 — `over pin` — observed by the main loop at `cb1ee1c51`: the lexicon exited 0 and printed no line holding it.
- AC10 — `pass-leg-evidence.txt` — the grep for the old two-file sentence printed 0 and the grep for the evidence file's name printed 1.
- AC11 — `filtered list and not the manifest` — the three greps printed 0, 1 and 1, in the criterion's order.

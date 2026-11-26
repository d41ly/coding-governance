**Serves:** journal TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-123

# TOOL-dTotalRecall-123 build pass 3 — the builder's return

The gov-builder return for the pass dispatched at `688a6f195` from [2026-11-25-prompt-TOOL-dTotalRecall-123-build-3-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-123-build-3-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `2f8525d79`.

## Why

Spec rev-3 built as written: S1 to S5 are in one pass commit and every criterion is observed or named as owed. The header stays INPROGRESS, as spec section 4 "Rollout" and the brief say, against the task text's CLOSED; the commit records this as a `Decided:` trailer.

## Summary

Pass commit 2f8525d79 holds:
- the scorer: `measure_rise_noise`, `NOISE_FACTOR`, the declared and held run count, the arm `map-noise`, `map-verdict` on the figure `noise`, and ARMS_DECLARED 34
- the README's `map-replay` paragraph
- deviation 1021, minted through `gov_record.py new deviation`, departing from `TOOL-dTotalRecall-17@rev-3` [§4 "The terms"] (DERIVED 2026-11-25, the pass)
- the manifest memory/builds/dTotalRecall/build/2026-11-26-build-TOOL-dTotalRecall-123-map-replay-manifest.json: `candidates` empty, `map` null, both `dispatched` 15
- the ledger memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-123-3-acceptance-ledger.md, RUN.md, and the renders

Probes run (DERIVED 2026-11-26). They stand in for the `review-replay selftest` leg, which did not run:
- AC1: both `term recall` lines exact.
- AC2: a dropped run, two declared counts, an undivided count, one run and an extra run each refused; the complete set returned lines.
- AC3: boundaries held; the first record's six pairs read 15.46.
- AC4: the grep printed nothing.
- AC5: `malformed` empty; `address`, `follow` and `bound` as specified; the anchored grep named the one file.
- AC10: exit 2 naming `map None: not a source of a non-empty map`. The manifest's `known` equals the first experiment's. (DERIVED 2026-11-25, the pass)
- `map-verdict`, `map-experiment`, `map-noise` and `map-known`, cut out of `run_selftest`, each answered None. In scratch copies, `map-noise` failed with the range put back, with the division cut and with the exact-count refusal cut; `map-verdict` failed on the margin alone.
- The lexicon's `--measure` left `VERB_OFFENDER_PIN` at 1443. The commit hook's memory-hygiene (staged), codebase-map and kickoff-ratchet checks passed.
- `gotchas.py --for-diff HEAD~1..HEAD` was run and read; nothing it named needed a change.

Owed to the close: the section 7 legs, the RED-first observation of both `New arm:` lines (`map-noise`; `map-verdict` with the noise-alone set), and AC9. Owed to the main loop: S6's runs, S7's verdict commit with AC6 to AC8 and the header flip to CLOSED, and naming the cl-dClosedLoop-0228 amendment to the owner at the close. (DERIVED 2026-11-25, the pass)

No command exceeded its bound. One file was left unstaged, as found: memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-123-2-builder-return.md.

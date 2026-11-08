# Acceptance ledger — TOOL-dFairHearing-32

**Serves:** journal TOOL-dFairHearing-32

Built against spec rev-6 at pass commit `fb755fa80`, whose parent is `5c9bb5bd7`. The main loop drafted
this ledger at the close from the builder return, and from the ledgers of units 37 and 38 where a line
says so. Each observation is a scratch probe or fixture under the pass's scratch directory. No suite,
gate or bar ran in the pass. The spec's Gates section's legs and the RED-first observation of its six
`New arm:` lines are owed to the close.

AC5 was observed at the close. AC18 was not: its line says why.
AC1, AC11, AC15 and AC17 each state the half that is still owed.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-32
- AC1 — `git grep` — the tree-wide grep printed nothing. The stub-run half, the `resume:probe` prompt naming `verify-batch-<n>.json`, is the `tier2-review.test.sh` arm this commit adds, and no record observes it: it is owed to the close. At the tip `tools/workflows/tier2-review.js:1708` carries `verify-batch-<n>.json` in the `resume:probe` prompt
- AC2 — `tools/workflows/tier2-review.js` — a node probe of the prelude keyed the five `where` forms to the five `at` values the criterion names. A copy whose pattern requires the space keyed the two unspaced forms to `null`
- AC3 — `grep -n -B12` — the comment above `function deriveAddressKey` appeared within the grep's window, naming the three differences from the instrument's `loc`
- AC4 — `review_replay.py` — the python and node readers agreed on the three refs, and this commit leaves the file untouched. That diff half is superseded by unit 37's AC7, below
- AC5 — `python replay_scorer.py --selftest` — at the tip `948e4141b` it prints `replay_scorer selftest: 29/29 arms` and exits 0. A scratch copy with `ARMS_DECLARED` at 28 exited 1 printing `29 arm(s) ran against 28 declared`
- AC6 — `case_evidence` — `--experiment` over the fixture manifests exited 2 with the expected names on each refusal, and each valid control exited 0
- AC7 — `--experiment` — the planted manifests each exited 2 naming the arm, with no `Traceback`, and the valid control exited 0
- AC8 — `%TEMP%/fgc` — the pass ran the comparison over this repository, `gotchas.py --for-diff HEAD~5..HEAD` with and without `--all-ungated`, and the output was byte-identical, not over the fixture catalogue. The fixture comparison is unit 38's: its ledger's AC1 line records `%TEMP%/fgc` printing byte-identical output both ways on a `selected` decision, with a staged break that differs
- AC9 — `git rev-parse` — for both replay records, the commit that added the record has the orchestrating commit, `8ee00000a` and `3cf918a65`, as its first parent. Unit 23's `7ff570cfa` is an ancestor of both, and all six named blobs match. Unit 37's ledger, on its AC3 line, records neither record's line ending `(derived)`
- AC10 — `git for-each-ref refs/replay/` — `precondition`: it printed nothing
- AC11 — `review_pin.py` — a scratch copy with the constant set to `design-audit` printed `{"preset": "design-audit"}`. The `grep -n DESIGN_RECORD_PRESET` half is in no record: it is owed to the close. At the tip `grep -n DESIGN_RECORD_PRESET` hits `tools/workflows/tier2-review.test.sh:2590` to `:2591`
- AC12 — `attempts.py` — it printed 8 `scored` lines, and unit 30's record holds `paired 4 of 4`, so no `void after cap` pair exists. Replay 1 lists fhr1b, void, and fhr1c for run 1, and fhr2b for run 2, each under its own clone, and no run reads `not run`. The `unscored` half is `n/a: no unscored attempt`, not counted as coverage, and no attempt is red
- AC13 — `renderBlankedView` — through the blanked view neither file holds `MAX_LENSES`, and `check-verifier-fanout.js` holds one `const LENS_SLOTS` declaration. A history comment passed and a declaration failed, and the two greps printed nothing and 0
- AC14 — `Filename too long` — recorded evidence for S23, under the precondition unit 37's AC13 computes: the clone into the scratchpad exited 128 printing it, and the clone into `%TEMP%/lp` exited 0 and was removed
- AC15 — `agent-cap.js` — on a scratch layout the stale row with the pack beside the hook exited 0, where the parent hook exited 2. With the pack removed it exited 2 naming the receipt and both probe paths, and the `..` row exited 2 the same way. The `grep -c "function resolveKitDir"` half is in no record: it is owed to the close. At the tip `grep -c "function resolveKitDir"` prints 1 in `tools/hooks/agent-cap.js` and 1 in `tools/workflows/spec-audit-optin.js`
- AC16 — `resolve_kit_dir.py` — the suite's new layout block, run alone, gave the same seven answers from it and from the JS port, and a port denying on row 2 disagreed on row 2
- AC17 — `LENS_SLOTS` — over the suite's new fixture the scratch copy exited 0, and with `LENS_SLOTS` set to 6 it exited 1 naming `lens-array bound`. Its run over this repository's own tree is owed to the close
- AC18 — `scope:` — NOT OBSERVED as written. The fixture would not build: `govkit.py apply` needs the four dependent kits, then four answers, then a `[gate_runner]` in the descriptor, and it stopped at BASELINE leaving no receipt, so `update` had nothing to move. The code path prints the line at `tools/govkit/govkit.py:9638`, and `tools/govkit/selftest.py:17990` asserts a `scope: review-harness moves with` line, which this close did not run
- AC19 — `--experiment` — with `heldOut` naming a directory and then a path holding `*`, each exited 2 with the expected names and no `Traceback`. Unit 37's ledger, on its AC5 line, quotes `2 line(s)` and `0 line(s)`
- AC20 — `check_ungated` — an import probe showed the scope stopping at `.**`, where the old pattern read `tools/y` as the gate

## Supersessions

Each one is named by a hands-off bullet in this unit's spec, in `TOOL-dFairHearing-23`'s form.

- AC4's whole-file diff of `review_replay.py` — answered by `TOOL-dFairHearing-37`'s S7 and AC7, over the body of `extract_section_ref`
- AC8 — re-run by `TOOL-dFairHearing-38`'s S2 and AC1, with a staged break, as the observation of a `selected` verdict
- AC9 — graded over the values the records wrote at call time, by `TOOL-dFairHearing-37`'s S3 and AC3
- AC12's unit-15 half — read through unit 35's rule by `TOOL-dFairHearing-37`'s S2 and AC2
- AC13's absence check — widened to template interpolations by `TOOL-dFairHearing-37`'s S9 and AC9
- AC14 — computes its precondition under `TOOL-dFairHearing-37`'s S14 and AC13. Its S16 labels this ledger's AC10 and AC14 lines
- AC15 and AC16's truth table — gains rows 8 and 9 under `TOOL-dFairHearing-37`'s S13 and AC12
- AC19 — gains its valid-path control under `TOOL-dFairHearing-37`'s S5 and AC5
- AC20 — gains the mixed closing run under `TOOL-dFairHearing-37`'s S15 and AC14
- S6 — the instrument's line citation is corrected by `TOOL-dFairHearing-37`'s S17 and AC15
- S25's port against the canonical on rows 8 and 9 — left to `TOOL-dFairHearing-40`, whose ledger's AC10 line records the two agreeing

# TOOL-dWitnessedBar-91 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-91

No merge bar, no self-test suite and no gate leg ran in this pass. This unit writes records only: it touches no code file and mints no function. Its criteria were probed on node d, 2026-11-21, from base `d83669eb9`, by reading the unedited built `.githooks/pre-push`. Every line marked OWED is the main loop's at the close, after the last unit is terminal: 90 AC2's two scratch clones, S1's counts in them and S2's note in unit 90's ledger (§4 Rollout).

**Evidences:** TOOL-dWitnessedBar-91
- AC1 — `sha)` — over the unedited built hook at `d83669eb9`, `grep -c 'rec_sha="'` printed 2, the anchored `grep -c 'sha)[[:space:]]*rec_sha="'` printed 0, the `read_green_file` cut piped to `grep -o 'sha)' | wc -l` printed 1, and `grep -c 'rec_sha=""'` printed 2 (PINNED 2026-11-21); `grep -n 'sha)'` named the reader's `sha) rec_sha=$_rg_v ;;` in `.githooks/pre-push#read_green_file` and `sha) bg_sha=$_rb_v ;;` in `.githooks/pre-push#read_bar_file`, as §4 states. OWED: the three counts in each of 90 AC2's two quoted-arm clones, `rec_sha="$_rg_v"` and `rec_sha="${_rg_v}"`, against the reset count re-derived from the unedited built hook at the close.
- AC2 — `sha)[[:space:]]*rec_sha="` — OWED: the note labelled `TOOL-dWitnessedBar-91 S2`, a continuation line under the `- AC2` answer of `2026-11-19-build-TOOL-dWitnessedBar-90-1-acceptance-ledger.md`, is written at the close with S1's counts, and AC2's selector runs over that ledger then.

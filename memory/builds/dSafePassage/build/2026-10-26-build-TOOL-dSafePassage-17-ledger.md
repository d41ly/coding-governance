**Serves:** journal TOOL-dSafePassage-17

# TOOL-dSafePassage-17 — acceptance ledger

The unit as built, at spec rev-5. `read_steps` in `tools/govkit/upgrade_steps.py` admits an optional
`reverted` on an `[[upgrade]]` row, `"down-exit"` or an argv under `check_argv`, and refuses any other
value naming the file, the row and the key; `StepRow` carries it, `FROZEN_FIELDS` and `check_frozen`'s
program walk grade it as they grade `down`, and `STEP_PHASES` lets `run_step_isolated` spawn it.
`derive_down_verdict(row, image_present, down_rc)` decides move 5 of `run_reverse_walk`, the image
read before the down's spawn by the existing `read_image_paths`. `write_from_before_image` already
returned `[]` with no image, so S3 needed no code; AC5 observes it. The floor row in
`tools/govkit/steps.toml` declares `reverted = "down-exit"`. The `rollback` fixture gains the plants
`witness-only`, `node-witness` and `node-witness-refuses`, and `help/upgrade-steps.md`'s "Rolling
back" section says how a down is judged. No deviation.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass: each criterion below was
observed by the unit's own CLI over a scratch fixture or by a probe. Owed at the close: the new arm's
rows in `tools/govkit/selftest.py` (`[dSP-17 AC1]`, `[dSP-17 AC5]`, `[dSP-17 AC7]` and the three
`rollback` plant rows tagged `dSP-17`), their RED-first observation on a walk copy whose move 5 reads
the witness for every row, and the §7 legs: `govkit selftest`, `govkit refusal join`, `govkit
acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture (text IO names its
encoding)`, `lexicon naming predicates`, `policy fixtures`, `spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dSafePassage-17
- AC1 — `python tools/govkit/upgrade_steps.py list` over a scratch gov at `%TEMP%/gk17g` with `reverted = "maybe"` exited 2 printing `tools/govkit/steps.toml [[upgrade]] row 1 key reverted: 'maybe' is neither "down-exit" nor an argv`; with `reverted = "down-exit"` and with a tracked python argv it exited 0 listing the row; `["node", "x"]` and `true` each exited 2 naming `key reverted`.
- AC2 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-only` printed `rollback: fx/s2 applied by witness alone, no before-image`, then `step fx/s4 · rolled-back` through `step fx/s1 · rolled-back`, `rollback: the target's bytes equal their bytes before the walk`, and exited 0.
- AC3 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant node-witness` printed s2 applied by witness alone, all four rows `rolled-back`, and exited 0; `--plant node-witness-refuses` printed `step fx/s2 · STOPPED · down exit 1: fx: s2 down fails by its plant`, kept fx/s2 `applied` with that failure, downed no s1, and exited 1.
- AC4 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-stays` printed `step fx/s2 · STOPPED · witness still holds after down`, kept fx/s2 `('applied', 'witness still holds after down')`, and exited 1; the base plant, `down-fails` and `schema-step` still exited 0, 1 and 0 with no `rollback: FAILED`.
- AC5 — `python tools/govkit/steps/fanout_cap.py down <t>` on a fresh `git init` target at `%TEMP%/gk17t` with no `.agent-cap.conf` and no image printed `fanout-cap: down · restored nothing: no before-image, no up applied` and exited 0, and `git -C <t> status --porcelain` printed nothing.
- AC6 — `python -c "import sys, tomllib; print([r.get('reverted') for r in tomllib.load(open(sys.argv[1], 'rb'))['upgrade'] if r['id'] == 'lib/python-floor-3.15'])" "tools/govkit/steps.toml"` printed `['down-exit']`.
- AC7 — `python tools/govkit/upgrade_steps.py frozen --base <main sha>` in the scratch gov, on a branch editing a landed row's `reverted` from `"down-exit"` to an argv, exited 1 naming the id `lib/first` and the field `reverted` ("its landed ... was edited in tools/govkit/steps.toml"); the control branch with no edit exited 0, `0 problem(s)`.
- AC8 — `git grep -n -e "reverted" -e "down-exit" -- help/upgrade-steps.md` printed the "Rolling back" section's "How a down is judged" lines naming `reverted = "down-exit"`, `reverted` as a command, and `reverted check exits <rc>`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_rollback`, cut to `witness-only` and `node-witness`. Break: `derive_down_verdict` returns `(None, "witness")` for every row. RED: `FAIL [dSP-17] fixture rollback witness-only exits 0 and names rollback: fx/s2 applied by witness alone, no before-image, …` with `rollback: FAILED · s1 to s3 do not each read rolled-back`. `node-witness` and two dSP-33 S3 rows also go red. GREEN restored: FAILURES=0, 21 ok.

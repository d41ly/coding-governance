**Serves:** journal TOOL-dDeclaredLoop-32

# Builder return — TOOL-dDeclaredLoop-32, dispatch 1: rev-5's no-fall rule and promotion target redden driver-suite arms its sweep does not name

## Why

DIVERGENCE: if built as written, rev-5 turns existing arms of tools/unattended/unattended.test.sh red, and its §5 sweep neither lists those arms nor says how each stays green. The sweep says the existing --review lines read as today and that empty arguments 4 to 6 keep every three-argument answer. That holds only for the slice arms. At the driver level, two scope items change behaviour the suite already asserts.

(1) The no-fall rule for spec subjects (S3 and §4 "The targets", subject table row "a spec subject … no-fall set"; also §2 S2: spec subjects get no route-backs). The suite's fixture policy, set where it writes .governance/policy.toml, is fixed-count 7 with max-rounds 7. Under that policy a flat spec subject now reads CONVERGING instead of NON-CONVERGENT, and with no route-backs on spec subjects a spec audit can never reach NON-CONVERGENT at all. I probed the sliced rev-5 review_state: `review_state 2 2 7 "" 2 no-fall` prints CONVERGING, where today's `review_state 2 2 7` prints NON-CONVERGENT. Each of these arms records a flat second round on a spec subject, then passes `--disposition promote` or asserts NON-CONVERGENT; under rev-5 the driver refuses with "names a disposition on a round that is not a terminal exit":
- subject "F1 (fork)", the terminal-subject-as-regex arm;
- subject S1, "the exit token is written into the round's own reason", and the terminal refusal that follows it;
- subject D2, "--review exits NON-CONVERGENT on a spec audit, which folds nothing", the promote row and "the pre-existing substring the leg reads still matches";
- subject S8, "a spec exit's counts sit before the disposition".
Which way each arm is re-planted (BOUNDED, the build slug, or retired as unreachable) changes what it tests, so the decision belongs in the spec.

(2) The promotion target on every promoting exit (S4: "Every exit row that records `disposition promote` records the target in a field before it"). Eight exact-row assertions expect `… · minors N · disposition promote` with no ` · to units`: "AC8 today's row has no new field", "AC7 the old value writes the new row", "the promote is written into the converged round's reason" (C2), "the promote disposition is written into the round's own reason" (D2), "the bounded exit is written into the round's own reason" (B1), "a bounded spec exit's counts sit before the disposition" (B3), "a spec exit's counts sit before the disposition" (S8), and "the counts sit before the disposition, the field check 2 reads last" (tRun).

The spec's §5 sweep (the `review_state` and `verb_review`'s-flags rows) and §6/§7 would have to name these arms and state how each is kept green or re-planted. All other sweep claims held at a68d80da1: census 329 = 324 branches + 5 sites against ceiling 329; families 1/1, 11/11 and 36/37; check-unattended 266/266; lexicon pin 1215; 89 --review lines; 19 zero-blocker fixtures; Skill render 10755; draw/value fingerprints and usage rows unchanged by units 48/49; run_budget_draw still reads the verdict as the first line.

## Summary

I did not commit TOOL-dDeclaredLoop-32. I built rev-5 nearly in full, then stopped at the divergence above and restored every product path. The work is saved as a patch at C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/TOOL-dDeclaredLoop-32-builder.patch (19 files, +495/-103).

**What the patch holds:**
- `review_bounds.py` prints seven fields and gains a `targets` plant.
- `budget.py` gains a `target` verb.
- `unattended.sh`:
  - `review_state` takes route-backs, target and no-fall arguments.
  - `review_counts` and `review_last_reason` take a row-kind argument.
  - `run_budget_verb` is extracted from `run_budget_draw`.
  - `run_fix_pass` and `check_fix_pass_open` are new, and `--dispatch` calls the latter.
  - the round flags, `PARK_KINDS`, `VERBS_SLUG`, `VERB_REQUIRES`, the header lines and the `closing-asks` note.
- `fix-pass` added to `runlog/model.py`'s and `drift_report.py`'s copies of the park kinds; `_RUN_ROW` reads a hyphenated kind; a new `tFixPassLast` arm in `drift-audit/selftest.py`.
- Check 2 in `check-unattended.sh` changed as S6 says.
- The build harness template and its render.
- The verbs carrier template and render, the Skill template and render, `help/loop.md` with both anchors, the `budget.py#target` row in `usage.toml`, the size row raised 10755 -> 10815, the ceiling token moved 329 -> 332 with its positional row.
- Partial edits to `unattended.test.sh`: the seven-field parity arm, and the eight row assertions re-pointed to ` · to units`.

**Not done before stopping:** the new arms in the three test suites, the kickoff manifest re-stamp, the codebase-map regeneration, the acceptance ledger and the spec status flip.

**What ran (probes only, no gate, suite or bar):**
- Sliced `review_counts` and `review_state`: AC1, AC3, AC10 and AC11 printed exactly as the spec says. This stands in for the new arm planned in `unattended.test.sh`.
- `review_bounds.py --fixture --plant defaults` and `--plant targets` both held (AC12), standing in for the `loop review bounds fixtures` leg.
- `drift_report._RUN_ROW` matched the `fix-pass` row with group one `fix-pass` (AC6). The `tFixPassLast` classification read `other`, and `surfaced-park` with `_RUN_ROW` set back to `[a-z]+`. That RED/GREEN stands in for the drift-audit selftest arm.
- The three AC6 greps printed 1, 1, 1 and 0.
- `writeRound` slices of the template and the render were byte-identical, `node --check` passed on the render, and `'specTarget'` counted 1 (AC8).
- The verbs carrier greps each counted at least 1, the Skill greps counted 1, and the Skill render measured 10815 CR-stripped (AC9).
- `docs_leg.py --list` named both anchors on `help/loop.md` (AC13). Fingerprints: `budget.py#target` d06981ab, `--fix-pass` 3696cb6a.
- `check-arms.py`'s own readers measured the census at 332 after the edits; the families and check-unattended's 266 did not move.

**Worktree state left behind:**
- `memory/builds/dDeclaredLoop/RUN.md` stays staged with this unit's `--dispatch` row, written by the driver; I recorded no row of my own. `--brief` printed "already recorded, unchanged".
- I added `deviation-323` to the declared write set but did not write it.
- A probe of mine that waited on stdin went to the background and could not be stopped from here, because TaskStop is not available. It touches no file.
- `gotchas.py --for-diff` was not run, because there is no commit.

**Owed at the close once rev-6 lands:** the RED-first observation of each `New arm:` line.

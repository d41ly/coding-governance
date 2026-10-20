**Serves:** research PLAY-dClosedLoop-1

# Phase 0, dispatch 234: every command run for a plant or a red test, in order

The builder's evidence for its brief (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-deviations.md`), each
command with its exit code and the line that proves it, before and after each fix. `build/` is
`memory/builds/dClosedLoop/build/`, and a file there is named by its suffix. Every id this record quotes from a
command's output is written in the `missing:` form, so the build index joins nothing; the outputs held each one bare.
Every command ran from a tree's root, with `python -B`.

## [p0-6] The bare-id predicate and the marks

The predicate is `build/…-bare-ids.py`. The fix is commit `60d041ba5`, on `4bfca2c74`.

**1. The predicate on the unfixed tree** (`4bfca2c74`): `python -B build/…-bare-ids.py`, exit 1, 25 lines, one per
citation, on 22 lines in 7 files, the plan's count. No later record added one.

| File | Lines | Citations |
|---|---|---|
| `build/…-deviations.py` | 178, 180, 181, 183, 184, 185, 189, 191, 193, 197 | 12 |
| `build/…-asbuilt.py` | 106, 107 | 2 |
| `build/…-research-exec-instruments.md` | 7, 776, 789 | 4 |
| `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md` | 24483 | 1 |
| `build/…-execution-plan-reviews-compared.md` | 170 | 1 |
| `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-a.md` | 275, 277, 312 | 3 |
| `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-b.md` | 202, 235 | 2 |

Its first line: `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:24483: missing:PLAY-dTrueNorth-2`.

**2. The red test before the fix**, in a scratch clone at `4bfca2c74`: a minimal `memory/builds/dTrueNorth/README.md`
(front matter with `ids:` empty, the five slot headings), staged, then `python -B tools/memory-tree/gen_build_index.py
--write`: exit 0, `build-index: wrote 1540 artifact(s)`. The README's line 7 became `ids: missing:PLAY-dTrueNorth-1
missing:PLAY-dTrueNorth-2 missing:PLAY-dTrueNorth-3 missing:PLAY-dTrueNorth-4 missing:PLAY-dTrueNorth-5
missing:PLAY-dTrueNorth-6 missing:PLAY-dTrueNorth-7 missing:TOOL-dTrueNorth-1`: the generator joined eight ids.

**3. Each instrument mode before the fix**, on `4bfca2c74`, and **4. after it**, on `60d041ba5`:

| Command | Exit before | Exit after | Summary line, the same before and after |
|---|---|---|---|
| `build/…-deviations.py` | 0 | 0 | `baseline read, chain-build specs 0, members 0, records 0 · findings 0` |
| `build/…-deviations.py --fixture` | 0 | 0 | `chain-build specs 2, members 3, records 3 · findings 0 · fixture` |
| `… --fixture --plant clause` | 1 | 1 | `members 3, records 2 · findings 1 · fixture · plant clause` |
| `… --fixture --plant pass-revision` | 1 | 1 | `chain-build specs 3, members 4, records 3 · findings 1` |
| `… --fixture --plant amended` | 1 | 1 | `members 4, records 3 · findings 1 · fixture · plant amended` |
| `… --fixture --plant pin` | 1 | 1 | `members 3, records 3 · findings 1 · fixture · plant pin` |
| `… --fixture --plant approver` | 1 | 1 | `members 3, records 3 · findings 1 · fixture · plant approver` |
| `… --fixture --plant status` | 0 | 0 | `chain-build specs 3, members 3, records 3 · findings 0` |
| `build/…-asbuilt.py --check` | 0 | 0 | `asbuilt: findings 0` |
| `build/…-asbuilt.py --fixture` | 0 | 0 | `asbuilt: findings 0 · fixture` |
| `… --fixture --plant hand-edit` | 1 | 1 | `asbuilt: findings 1 · fixture · plant hand-edit` |
| `… --fixture --plant no-row` | 1 | 1 | `asbuilt: findings 1 · fixture · plant no-row` |
| `… --fixture --plant no-citation` | 1 | 1 | `asbuilt: findings 2 · fixture · plant no-citation` |

Every exit code and summary line is unchanged. A diff of the two full outputs differs in three finding lines only,
each naming its id in the `missing:` form after the fix: the `pass-revision`, `amended` and `pin` plants, whose ids are
fixture strings.

**5. The predicate after the fix**, on `60d041ba5`: exit 0, nothing printed.

**6. The red test after the fix**, in the same scratch clone reset onto `60d041ba5`, the same README staged, then
`gen_build_index.py --write`: exit 0, `wrote 1540 artifact(s)`. The README's line 7 stayed `ids:`, and its
build-index region carries no `ids` line: the generator joined none. The predicate there: exit 0, nothing printed.

**7. The predicate's plants**, in that clone, each line appended to the tracked
`build/2026-10-20-build-PLAY-dClosedLoop-1-recheck-brief-a.md` and the file restored after each run:

| Plant | Exit | Output |
|---|---|---|
| a bare id, the id missing:TOOL-dTrueNorth-1 written bare | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dTrueNorth-1` |
| the same id behind `x:` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dTrueNorth-1` |
| control: the same id in the `missing:` form | 0 | nothing |

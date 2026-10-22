# TOOL-dTrueNorth-18 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-18

No merge bar, no self-test suite and no gate leg ran in this pass. Every criterion below was observed
by the probe or CLI the spec names, over the working tree with this pass's files in it. The probes
stand in for the `build-index selftest`, `routed-commits selftest`, `memory hygiene` and `kit/dogfood
doc parity` legs, which the close runs.

The two new arms are the spec's `New arm:` lines. They need no new code in either self-test: the
generator's `test_asbuilt_view` runs every plant `asbuilt_view.run_plant_arms` holds, and the
routed-commits self-test runs every plant `deviation_join.run_plant_arms` holds, so the four as-built
plants and `malformed-supersedes` joined both by being added to each module's `PLANTS`, exit and
needle tables. Their RED-first observation and their green belong to the close, recorded here under a
`Pass: none` commit. What this pass observed instead is a scratch probe that ran each module's
`run_fixture` per plant against its exit, its needles and its liveness flag, without calling either
self-test. Under the head rule every plant held, the twelve as-built plants included. With
`resolve_clause_rows` swapped for the base rule, where the later path supplies the row,
`amends-order`, `unordered-amends` and `supersedes-stray` went red and `same-after` held, since a pair
whose texts agree is exactly the case where the base rule is already right. With it swapped for a rule
that refuses every pair, `same-after` and `amends-order` went red, which is AC3's red-when. With
`deviation_join.SUPERSEDES` widened to accept any value, `malformed-supersedes --policy refuse` exited 0.

This pass changes the render's code, so by TOOL-dTrueNorth-17 S1 it ran
`python3 tools/memory-tree/gen_build_index.py --write`, which left the view byte-identical:
deviation-1 and deviation-4 agree on `cl-dClosedLoop-0004`'s **After:**, and no record in the tree
carries `**Supersedes:**`.

**Evidences:** TOOL-dTrueNorth-18
- AC1 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant amends-order` — exit 0, findings 0; it printed "cl-dClosedLoop-0009: 2026-10-21-build-FIX-dTrueNorth-18-deviation-10 supersedes 2026-10-21-build-FIX-dTrueNorth-18-deviation-9 and supplies the row's **After:** and citation, though its path sorts first", the plant having checked that the two records reach the render in path order, `deviation-10` first, and that the row holds `deviation-10`'s **After:** and cites it.
- AC2 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant unordered-amends` — exit 1, findings 1: "unordered amends of cl-dClosedLoop-0009: 2026-10-21-build-FIX-dTrueNorth-18-deviation-10, 2026-10-21-build-FIX-dTrueNorth-18-deviation-9 give it differing **After:** texts, and no **Supersedes:** orders 2026-10-21-build-FIX-dTrueNorth-18-deviation-10, 2026-10-21-build-FIX-dTrueNorth-18-deviation-9; cl-dClosedLoop-0009 renders its baseline row", and the note that the row is the baseline's text, citing none.
- AC3 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant same-after` — exit 0, findings 0, "two amends with one **After:** cite the later path, 2026-10-21-build-FIX-dTrueNorth-18-deviation-9", which is the later path because `-deviation-10` sorts first; and on the tree after the pass `grep -c 'cl-dClosedLoop-0004.*deviation-4' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` printed 1, `asbuilt_view.py --check` printed findings 0, and `gen_build_index.py --write` left the view's bytes unchanged.
- AC4 — `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant supersedes-stray` — exit 1, findings 1: "2026-10-21-build-FIX-dTrueNorth-18-deviation-9: its **Supersedes:** names 2026-10-21-build-FIX-dTrueNorth-18-deviation-10, no amends of cl-dClosedLoop-0009, whose amends are 2026-10-21-build-FIX-dTrueNorth-18-deviation-9; cl-dClosedLoop-0009 renders its baseline row". The named record amends the eleventh clause, and its row still cites it.
- AC5 — `python3 "tools/memory-tree/deviation_join.py" --fixture --plant malformed-supersedes --policy refuse` — exit 1, records 5 (1 malformed), and the line "malformed: memory/builds/dFixA/build/2026-10-21-build-FIX-dTrueNorth-35-deviation-5.md: Supersedes deviation-9 is not one record id: **Supersedes:** names the stem <date>-build-<unit id>-deviation-<n> of another record". A probe of `read_record` accepted a bare stem and a backticked one, returning the stem, and named as malformed a value naming the record itself, a stem with trailing words, and `deviation-9`.
- AC6 — `git grep -n "Supersedes" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md tools/memory-tree/README.md "tools/memory-tree/asbuilt_view.py"` — printed lines in all four files. In both HYGIENE copies, lines 634 to 640 of the "Deviation records" paragraph name the optional field, the stem it holds, and the head rule. In the README it is line 28, the `asbuilt_view.py` row's head-rule sentence, and in `asbuilt_view.py` it is the THE HEAD paragraph at lines 45 to 53 and `resolve_clause_rows`' docstring. None of the four still says the later path supplies the row unqualified: each gives that only to a set whose texts agree.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, breaks `u18-later-path-head` and `u18-no-stray`, 3 of its 4 plant arms red; under the `routed_commits.py` selftest, which runs `deviation_join.py`'s plant arms, break `u18-supersedes-any`, the malformed-supersedes plant's 4 arm lines red, labelled under its host plant table. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.

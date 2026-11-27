# TOOL-dTotalRecall-122 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-122
**Caused-by:** TOOL-dTotalRecall-122

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`e0e9cb73b055ee5a50a5d6130d6ed2fb8c5e3d5d`, 2026-11-25 local, in one commit. §7's legs and the RED-first observation of
every `New arm:` line are owed to the close. `2026-11-25-build-TOOL-dTotalRecall-122-deviation-1018` records the one change
the spec did not state.

**Evidences:** TOOL-dTotalRecall-122
- AC1 — `python build_records.py --fixture --plant ask-door` — printed PASS with 20 cases, `foreign row` over no file and over a held one exit 2, `foreign read-back` exit 3, the foreign line kept in each; `door-header` printed PASS with 26 cases, `foreign line` exit 2; the `index-lock` cases exited 2 as they did. With the compare cut in a scratch copy the `ask-door` run failed every foreign case, and `index-lock` stood (DERIVED 2026-11-25, the three runs).
- AC2 — `python record_find.py --fixture --plant section-later-row` — the unpinned, pinned and unheld reads printed the later row's outcome and the pinned read with no tag the first row, each `exit 0`; with the pick cut to the first row the pinned and unheld reads exited 2 (DERIVED 2026-11-25).
- AC3 — `bash gov-claim.sh slug <s> --claimant <key>` — printed `refused the slug is not a letter, then letters, digits or dashes`, exit 2, for the three slugs and the remote held no claim ref; with the pre-check line cut each was refused by the grammar's words (DERIVED 2026-11-25, the probe). The `test_slug_claims` arms are owed to the close.
- AC4 — `check_experiment` — the arm `map-experiment`, cut out of `run_selftest`, answered None, so both pairs of last lines read as §4 says; with `armed` pinned True it named `verdict win` in the unarmed run's place (DERIVED 2026-11-25, the probe).
- AC5 — `python record_find.py --fixture --plant section-second-file` — printed the second file's outcome, `exit 0`; with the loop's containment cut it exited 2 (DERIVED 2026-11-25).
- AC6 — `python record_find.py --fixture --plant other-tree` — printed the other tree's text, the path line naming the record's own path and `exit 0`; the lookup cut printed an empty path and a plain `min` the earlier one; `other-tree-unpathed` printed `stands at no path the index holds`, `exit 2`, and with the refusal cut exited 0 (DERIVED 2026-11-25).
- AC7 — `unread header` — exited 2 inside the `door-header` PASS; with `read_key_fields` answering the fields without the cause in a scratch copy, that case alone failed (DERIVED 2026-11-25, the two runs).
- AC8 — `grep -nE '^ASSERTION_FLOOR|^# RAISED 1724' tools/runlog/selftest.py` — printed the raise line and 1746; `parse_floor_raise` answered 1724 and 1746; the `ast` count gave 10 and 6 (DERIVED 2026-11-25, the probe). The suite's run at the floor is owed to the close.
- AC9 — `git log -1 --format='%(trailers:key=Decided,valueonly)'` — the pass commit's message carries the three lines of §4 and S12's in its final block, and `commit_trailers.py decided` over it answered 4 decisions, each in the block, before the commit (DERIVED 2026-11-25); the read over the commit itself is in the builder's return.
- AC10 — `python tools/unattended/commit_trailers.py decided <file>` — exited 1 naming the line over a paragraph above the block and over the three commits' messages, 0 over one in the block and over one with none, 2 over no file; the three blocks hash alike; `--check-commit` in this worktree refused the first message through check 49 and admitted the second (DERIVED 2026-11-25). The suite's arms are owed to the close.
- AC11 — `check_read_call` — answered False for the eleven writing calls and True for the five reads; `map-transcript` answered None, and named the failure with `QUOTED_SPAN` a no-op, the heredoc removal cut, or either option test cut (DERIVED 2026-11-25, the probe).
- AC12 — `python tools/memory-tree/gotchas.py --check` — named no finding of the new file, the dossier's `grep` printed 1, and `row_grammar.py --check-relations 3d6c1702a` over the staged file printed no line naming it, no near match of it clearing the floor (DERIVED 2026-11-25); it names `an-allow-that-bypasses-a-judge-names-none` by a relation.
- AC13 — `awk 'length($0) > 110' tools/unattended/VERBS.template.md | grep -c 'no record events were rebuilt'` — printed 0, the `--check-commit` entry names `Decided:`, and the guide is the template's bytes (DERIVED 2026-11-25).
- AC14 — `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` — read 12224, 17614 and 3809, as the three rows hold, widened by `2026-11-25-build-TOOL-dTotalRecall-122-widen-34` and set to the measure by hand; the literals read 26 and 20 as the plants print; the floors rose 879 to 894, 4228 to 4237 and 436 to 445, by 15 and by 9 assertions read off the diff (DERIVED 2026-11-25). The observed counts are owed to the close.

# TOOL-dTrueNorth-17 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-17

No merge bar, no self-test suite and no gate leg ran in this pass. Every criterion below was observed
by the probe or CLI the spec names, over the working tree with this pass's files in it, or in a
scratch clone under `%TEMP%` where the spec says so. The probes stand in for the `build-index
selftest`, `memory hygiene` and `kit/dogfood doc parity` legs, which the close runs.

The new arm, S3's, is two arms in `test_asbuilt_view` of the generator's self-test, on the spec's
`New arm:` line: its RED-first observation and its green are the close's, recorded here under a
`Pass: none` commit. What this pass observed instead is a scratch fixture probe that rebuilt the
arm's fixture and ran the arm's steps without calling the self-test: an `amends` record committed
over a view rendered on zero records, then an edit of the fixture's own kit file staged alone.
`check_staged_render`, given that kit directory, answered render; `cmd_check` exited 1 with the view
under `build-index DRIFT` from line 5 and no `as-built VERDICT`; after `cmd_write`, the view staged,
the same pair exited 0 over a view counting 1 deviation record and citing it on the amended row. Two
plants each turned one half false: the classifier not told the fixture's kit skipped the render and
exited 0, and the `--write` left out kept the view under DRIFT, exit 1.

S2's transition was met before this unit: `TOOL-dTrueNorth-4` (`93d33f534`) landed first and
`TOOL-dTrueNorth-6` (`8c5b1e542`) second, re-rendering the view in its own commit over the records
that stood. This pass changes the render's code, so by S1 it ran
`python3 tools/memory-tree/gen_build_index.py --write`, which left the view byte-identical.

**Evidences:** TOOL-dTrueNorth-17
- AC1 — `git rev-list 271aa59d..HEAD` — a probe walked the 40 commits of the range at `a48025364`; 8 hold `tools/memory-tree/asbuilt_view.py` and touch `memory/builds/*/build/*-deviation-*.md` or `tools/memory-tree/`, from `8c5b1e542` to `a48025364`, and for each the head's `<n> deviation records` in `git show <c>:` of the view equalled the `/build/*-deviation-*.md` count of `git ls-tree -r --name-only <c> -- memory/builds`: 16, 16, 18, 18, 19, 19, 19 and 19, mismatched 0. The compare can produce a negative: at `93d33f534`, the first order-3 pass, before the generator existed and so unread, the view counted 0 and the tree held 2.
- AC2 — `grep -E 'dispatch · item [^ ]+ TOOL-dTrueNorth-(4|6) ' memory/builds/dTrueNorth/RUN.md` — printed two rows, item `a8ecf7d7` for TOOL-dTrueNorth-4 and item `b1526808` for TOOL-dTrueNorth-6; TOOL-dTrueNorth-6 landed second (`8c5b1e542` after `93d33f534`), and its row names `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, the `DESIGN_VIEW` path, among its writes.
- AC3 — `python3 tools/memory-tree/gen_build_index.py --check --staged` — in a scratch clone of `a48025364` under `%TEMP%`, no hook installed, carrying this pass's three kit files: one `amends` record, numbered 99 under dTrueNorth's `build/` folder and amending `cl-dClosedLoop-0007@b0458b78`, was committed without re-rendering, so HEAD's view counted 19 records and its tree held 20; only an edit of `tools/memory-tree/asbuilt_view.py`'s docstring was staged, and the command exited 1, printing "render owed under --staged" and the view listed under `build-index DRIFT` from line 5, with no `SKIPPED` line. After `python3 tools/memory-tree/gen_build_index.py --write` and staging the view, the same command exited 0, "build-index: clean (1582 artifact(s))", the head counting 20 deviation records and the amended row citing the record. With the docstring edit left unstaged the same command printed the `SKIPPED` line and exited 0 over the same stale HEAD, so the staged kit edit is what made it render.
- AC4 — `git grep -n -e "render" -- "tools/memory-tree/asbuilt_view.py" tools/memory-tree/README.md` — printed `tools/memory-tree/README.md:28`, the `asbuilt_view.py` row, whose rule names the render's code (`asbuilt_view.py`, `design_lib.py` and the host calls in `gen_build_index.py`) among the view's inputs and the second order-3 pass as the transition's owner, and `tools/memory-tree/asbuilt_view.py:26`, `:29`, `:35` and `:36`, the render's code among the inputs on the first two and the second order-3 pass owning the transition on the last two.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, break `u17-kit-input`, 1 of its 2 arms red, the red-while-stale arm; the other asserts the clean state after `--write`. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.

# TOOL-dTrueNorth-8 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-8

No merge bar, no self-test suite and no gate leg ran in this pass. The pass's render, one
`python3 tools/memory-tree/gen_build_index.py --write` over the tree at `72ee0dbe1`, left the view
byte-identical: the commits that landed records 1 to 21 had each re-rendered it in their own commit,
so its head already counted the 19 records the tree holds, and S2's re-render had nothing to apply.
Every criterion below was observed by the CLIs the spec names, over the working tree with this
pass's files in it, or in a scratch clone where the spec says so. The probes stand in for the
`build-index selftest`, `memory hygiene` and `kit/dogfood doc parity` legs, which the close runs.

The new arm, S3's, is three arms in `test_asbuilt_view` of the generator's self-test, on the spec's
`New arm:` line: its RED-first observation and its green are the close's, recorded here under a
`Pass: none` commit. What this pass observed instead is a scratch fixture probe that rebuilt the
arm's fixture without calling the self-test: the design record committed, the view rendered over
zero records and committed, then an `amends` record staged beside it. `check_staged_render` answered
render, `cmd_check` exited 1 with the view under `build-index DRIFT` from line 5 and no
`as-built VERDICT`, and after `cmd_write`, the view staged, `cmd_check` exited 0 over a view counting 1
deviation record and citing it on the amended row. With `cmd_write`'s view write planted out, the
same probe's fixed-point half was false, exit 1 with the view still under DRIFT.

**Evidences:** TOOL-dTrueNorth-8
- AC1 — `python3 "tools/memory-tree/asbuilt_view.py" --check` — exit 0, "as-built view: findings 0 · view at 59ff8f2ac"; and `python3 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check` — exit 0, "asbuilt: findings 0 · view at 59ff8f2ac", both against the one view file.
- AC2 — `grep -o '[0-9]* deviation records' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` — printed "19 deviation records", the head's count, and a second line " deviation records" with no digit, the empty `[0-9]*` match inside the text of the `cl-dClosedLoop-0237` row at line 248, which carries no count. `git ls-files 'memory/builds/*/build/*-deviation-*.md' | wc -l` printed 19. `grep -c 'cl-dClosedLoop-0004.*| deviation ' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` printed 1, the row citing deviation-4 of TOOL-dTrueNorth-4.
- AC3 — `python3 tools/memory-tree/gen_build_index.py --check --staged` — in a scratch clone of `72ee0dbe1` under `%TEMP%`, whose generator code this pass does not change, after `--check` printed it clean over 1582 artifacts: one `amends` record, numbered 99 under dTrueNorth's `build/` folder and amending `cl-dClosedLoop-0007@b0458b78` of dGroundRules, was staged, and the command, run with the probe's own interpreter, exited 1 printing "render owed under --staged", the view listed under `build-index DRIFT` from line 5, and no `SKIPPED` line. After `python3 tools/memory-tree/gen_build_index.py --write` and staging the view, the same command exited 0, "build-index: clean (1582 artifact(s))", the head counting 20 deviation records and the amended row citing the record. The same probe amending `cl-dClosedLoop-0001`, a clause dTrueNorth's specs carry, exited 1 after one `--write` with the view fresh and dTrueNorth's README stale: its coverage region renders from the view as it stood before the write, and a second `--write` moved it to `- stale: 1 (cl-dClosedLoop-0001)`. That one-write fixed point is `TOOL-dTrueNorth-16` S20, observed by its AC20.
- AC4 — `git grep -n -e "re-render" -- tools/memory-tree/README.md "tools/memory-tree/asbuilt_view.py"` — printed `tools/memory-tree/README.md:28`, the `asbuilt_view.py` row, whose TOOL-dTrueNorth-8 sentence names `*/build/*-deviation-*.md` and `gen_build_index.py --write`, and `tools/memory-tree/asbuilt_view.py:27` and `:28`, the glob on the first and `gen_build_index.py --write` on the second; `git grep -n -i -e "never rewritten" -e "not rewritten"` over the two homes printed nothing.

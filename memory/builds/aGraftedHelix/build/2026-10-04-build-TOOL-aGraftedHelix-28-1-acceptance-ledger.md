# Acceptance ledger — TOOL-aGraftedHelix-28

**Serves:** journal TOOL-aGraftedHelix-28

Node `a`, 2026-10-05. The build commit is `e306d99c`, over the spec's rev-2 commit `f52ee82b` and a
records commit `a99f8ce6` that re-declared the write set with `memory/LIVE.md` and the month's ledger
shard: closing the build's last open unit flips the derived build status, so the pass commit writes
both. Rev-2 was made before any code, after reading the current tree: `gotchas.py` now imports
`tree_lib.py` from its own directory, which the rev-1 evidence did not say. No merge bar and no
self-test suite ran in this pass. The checker's `--selftest` ran whole, because it is a flag. The
build-harness suite's new arms ran as a slice inside the kit dir under a name that is not a
`.test.sh`, behind the suite's prologue, with its fixture layouts under a short `%TEMP%` root; every
staged break was a scratch COPY, deleted after its run.

**Evidences:** TOOL-aGraftedHelix-28
- AC1 — `cd tools/workflows && python check_by_design_parity.py ../memory-tree` — exited 0 and printed one `by-design parity:` line: `count 0 matched and captured 0, count 12 matched and captured 12; the count-12 head behind a leading space not matched`.
- AC2 — `cd tools/workflows && python check_by_design_parity.py <scratch-dir>` — over copies of `gotchas.py` and `tree_lib.py` with `BY_DESIGN_HEAD` reworded to `by-design`, it exited 1 with two `DRIFT` lines quoting `'# by-design — 0 invariant(s) this selection touches'` and the count-12 head.
- AC2 — `render_by_design` — with the constant as shipped and the copy's renderer printing the reworded head as its own literal, it exited 1 with the same two `DRIFT` lines.
- AC2 — `invariant` — with `render_by_design` renamed out of the copy, it exited 1 with a `DRIFT` line naming the `invariant` kind; with `invariant` also taken out of the copy's `KINDS`, it exited 0 with a `SKIP` line.
- AC3 — `python <scratch-dir>/check_by_design_parity.py tools/memory-tree` — with the template copy's pattern loosened to `/^(.*)$/` it exited 1 with three `DRIFT` lines: each head's whole text captured, `which is not the count`, and the leading-space head matched.
- AC3 — `^` — with only the pattern's leading `^` taken out it exited 1 with one `DRIFT` line naming the count-12 head behind a leading space.
- AC3 — `REFUSING` — with the declaration line removed it exited 2 with `carries 0 declaration(s) of BY_DESIGN_HEAD`, and with the line doubled it exited 2 with `carries 2 declaration(s)`.
- AC4 — `cd tools/workflows && python check_by_design_parity.py --selftest` — printed `selftest: 13/13 arms` and exited 0, with the fixture root under the session scratchpad.
- AC4 — `ARMS_DECLARED` — thirteen scratch copies of the checker, each with one arm's predicate disabled, each printed `FAIL <that arm>` and exited 1, the result-count check and the `KINDS` test included.
- AC5 — `--check` — the leg printed the `by-design parity:` agreement line and `in parity — 5 rendered pair(s)` and exited 0 at the build tree.
- AC5 — `tools/memory-tree/gotchas.py` — with `BY_DESIGN_HEAD` reworded in the working tree the leg exited 1 with two `DRIFT` lines and no in-parity line.
- AC5 — `git diff --quiet -- tools/memory-tree/gotchas.py` — exited 0 after the restore, and the leg exited 0 again.
- AC6 — `DRIFT` — the slice, with the real leg, ran 23 arms green: the review-only layout's did-NOT-run line, the stub catalogue's `SKIP` at `rc=0`, the real catalogue copy's agreement at `rc=0`, the committed reworded head's `DRIFT` at `rc=1`, and the checker's `--selftest` at `rc=0`.
- AC6 — `SKIP` — with the leg's whole by-design block cut from a scratch copy of the leg, the did-NOT-run, `SKIP`, agreement, `DRIFT` and `rc=1` arms read FAIL and the two `rc=0` arms stayed green, as the spec says they must.
- AC6 — `ARMS_DECLARED` — with a scratch copy of the checker declaring 14, the `--selftest` arm read FAIL and every other arm stayed green.
- AC6 — `FLOOR_ASSERTIONS` — raised 399 to 407; the static grep counted 541 sites at the unit's parent and 549 after.
- AC7 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `a99f8ce6` it printed `epoch: review-harness · clean · 1.35`, up from `1.34`.
- AC7 — `bash tools/check-kit-versions.sh` — printed `kit-versions: clean — 16 declared carrier(s) under tools/`.
- AC7 — `git status --porcelain tools/workflows/` — printed nothing after the leg's `--render` mode ran at the build commit.
- AC8 — `python tools/codebase-map/test_codebase_map.py` — printed six `ok` lines after `gen_map.py --write`.
- AC8 — `grep -c "check_by_design_parity.py" tools/workflows/README.md memory/map/features/review-harnesses.md` — counted 1 in each file.
- AC8 — `git grep -nE "(memory-tree|workflows)/" -- "*check_by_design_parity.py"` — printed nothing and exited 1.

`python tools/lexicon/lexicon.py` read OK, and `--suggest` answered OK for each of the nine function
names in the new file, the nested `arm` among them. `bash tools/check-install-prefix.sh` read clean,
`python tools/check-spec-tokens.py` exited 0, `node tools/workflows/check-workflow-syntax.js` printed
`6 workflow script(s) parsed clean`, and `bash skills/session-kickoff/manifest-check.sh` exited 0.
Left to the main loop at VERIFYING, because only a suite observes them: the build-harness self-test
whole, at its new floor of 407, and the other legs the spec's section 7 names.

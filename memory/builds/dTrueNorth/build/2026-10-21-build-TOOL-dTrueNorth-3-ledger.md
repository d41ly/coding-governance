# TOOL-dTrueNorth-3 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-3

No merge bar, no self-test suite and no gate leg but the naming lexicon ran in this pass, save one
`check-memory-hygiene.sh --only 29` over the worktree, run before the pass settled what it would
run, which exited 0 and is not read as a verdict here. Every criterion was observed by a probe of
the changed code, each a scratch script under the run's scratchpad or the generator's own CLI: a
scratch clone of the branch under the user temp directory, short-named, with this pass's working
tree copied in and committed there with the chain READMEs, `memory/LIVE.md` and this spec put back
at HEAD, so `--write` there renders the region onto a tree that holds none; a scratch fixture
repository shaped as the generator's new selftest arm builds it, the generator's CLI run over it;
and check 6's awk read verbatim out of the engine, at HEAD and in this change, run over a padded
README. The probes stand in for the `build-index selftest` and `memory hygiene` legs and the
`memory-hygiene self-test` suite; those, with the two new arms' RED-first observation, are owed to
the close.

**Evidences:** TOOL-dTrueNorth-3
- AC1 — `git diff --stat` — after `--write` in the clone it listed the 22 chain READMEs and no other
  README, 22 being the Build column `read_design_view` reads from the view at observation, and
  `memory/LIVE.md` for the Landed-unclosed count of this unit, open in the clone and closed here.
  For each of the 22 a probe found the README equal to HEAD once the new pair and the one blank line
  before it are removed, the line before that blank being `<!-- /gen:build-index -->`.
- AC2 — `carries.py --report dTrueNorth` — a probe parsed the region of the clone's
  `memory/builds/dTrueNorth/README.md` and the instrument's report into fields: nine and nine, each
  EQUAL, the derived specs' build-relative paths read against the instrument's repo-relative ones;
  the same for dConvergedCharter. With `- carried whole: 6` hand-edited to 7 the probe printed one
  DIFFER, so it can tell them apart.
- AC3 — `over 0 spec(s)` — dConvergedCharter's region read `over 0 spec(s)`, `- uncarried: 23 (` with
  the 23 ids the instrument lists, wrapped onto one two-space continuation line, and every empty
  field as `none`; the awk `length > 300` over the region printed nothing, the widest region line of
  the 22 being 300.
- AC4 — `python tools/memory-tree/gen_build_index.py --check` — in the clone it exited 0 printing
  `build-index: clean (1581 artifact(s))`; with one byte of dTrueNorth's region edited it exited 1
  naming `memory/builds/dTrueNorth/README.md (stale — differs from a fresh render)`; with
  dGroundRules' pair deleted it exited 1 naming that README as a chain build's README with no pair
  and the `--write` that creates it.
- AC5 — `SPEC_CARRIES_CUTOFF=""` — in the clone on a tree with no pair `--write` changed no README,
  and a render probe found `design_lib` unloaded after it, where the same probe with the key set found
  it loaded; on the tree holding the 22 pairs `--write` rendered all 22 as
  `*Coverage is not read: SPEC_CARRIES_CUTOFF is blank.*` and `--check` was clean.
- AC6 — `uncarried cl-dClosedLoop-0599` — in the clone with `TOOL-dTrueNorth-1` at `INPROGRESS` and
  the row `| dTrueNorth | cl-dClosedLoop-0599 | a planted clause | baseline |` in the as-built view,
  check 29's delegate `--check-coverage` exited 1 printing that spec `is INPROGRESS while
  dTrueNorth's coverage is red: uncarried cl-dClosedLoop-0599`, and with the row out it exited 0.
  Check 29 itself over the plant, `HYGIENE check 29 FAILED`, is owed to the close in the suite arm.
- AC7 — `1 (cl-dClosedLoop-0599)` — the plant standing and every dTrueNorth spec `OPEN` or
  `CLOSED`, `--check-coverage` exited 0 and the region after `--write` read
  `- uncarried: 1 (cl-dClosedLoop-0599)`; check 29's own pass there is owed with AC6.
- AC8 — `DESIGN_VIEW` — in the clone `--check-coverage` exited 0 on the clean tree, 1 under AC6's
  plant, 0 with the one line `coverage is not read — SPEC_CARRIES_CUTOFF is blank` when the key is
  blank, and 2 printing `DESIGN_VIEW names memory/builds/dClosedLoop/build/no-such-view.md, which
  cannot be read` when the key names a missing file.
- AC9 — `BUILD_README_CAP_BYTES` — check 6's awk, read out of the engine, over a 31341-byte README of
  95 authored rows and a 30-row coverage region: HEAD's priced it at 31273 authored bytes, over the
  25600 `BUILD_README_CAP_BYTES` default, and this change's at 23746, under it. The `--only 6` run
  over the suite's padded README is owed to the close.
- AC10 — `grep -n 'check-coverage' tools/memory-tree/README.md` — printed line 361, the verb's
  paragraph; `grep -n 'gen:build-coverage'` printed lines 225 and 280 of both `memory/HYGIENE.md` and
  the template, items 6 and 9; `grep -n '^29\. ' memory/HYGIENE.md` printed line 571, check 29's
  entry. The rendered copy differs from the template only where a placeholder renders.
- AC11 — `tools/check-spec-tokens.py` — in the clone, staged alone, `--check --staged` printed
  `render owed under --staged` and no SKIPPED line, by the LIVE_LANDED_UNCLOSED branch this tree
  arms; with that key off in a probe commit, `check_staged_render` answered `(True,
  'tools/check-spec-tokens.py is a build-index input or output')` with the cutoff set and `(False,
  'nothing is staged under the memory root, the conf or the kit')` with it blank.

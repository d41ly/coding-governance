# KICK-dKeptSession-80 — acceptance ledger

**Serves:** journal KICK-dKeptSession-80

The unit took two builder passes, both on node a, 2026-11-24, in the run worktree, and neither committed.
The first resolved the main loop's in-progress `git merge --no-ff --no-commit origin/main`, first parent
`9ab869b7d`, second `525f3ab97`, merge base `8b8b1374`. The main loop committed it as `dcb75b59e`, `Pass:
none`. The second wrote this ledger and the CLOSED flip, keyed to the spec's rev-2. No merge bar, no
self-test suite and no gate leg ran in either pass. The role's hook refused the one leg command tried, the
reference render's check. A reading named "the main loop's" below was taken by the main loop and handed to
the second pass; that pass did not repeat it.

The claims the spec makes about the tree were read at `9ab869b7d` before the first edit. The 33 conflicted
files and their hunk counts match the spec's (DERIVED, `git diff --name-only --diff-filter=U` and
`grep -c '^<<<<<<<'`), and the watched-commit count reads 9 for the run's `last-body-change` and 17 for
main's (DERIVED, the spec's `git rev-list --count`).

The window's provisional commit was `3005434ee`. In it, in order, the reference render exited 0, the
regeneration exited 0 and wrote its 16 items (DERIVED, its last line), and the packet `--write` exited 0
for each of the 22 slugs (DERIVED, one call per slug). The packets were rendered four at a time after a
first serial call was stopped between writes, and `dBoundRoles`, written before the stop, then read
current. HEAD was put back on the run branch after the last one.

The first pass also read each render as a fixpoint. A scratch clone was checked out at a second provisional
commit of the fully staged index and the writers run there. The reference render and the regeneration moved
no file but `AGENTS.md` and the lock line holding its blob, which is the clone's own default branch name.
`chain-packet.py --write` over `dGroundRules`, `dIndexedDesign`, `dKeptSession` and `dLinkedLibrary` printed
`is current, nothing written` for each.

**Evidences:** KICK-dKeptSession-80
- AC1 — observed, staged: `git ls-files -u` printed nothing (the first pass). At the merge, `git grep -l -e '^<<<<<<< ' -e '^>>>>>>> ' dcb75b59e --` printed nothing (the main loop's).
- AC2 — observed at the merge, the main loop's: `git rev-parse dcb75b59e^2` printed `525f3ab9766e1c117a600cfd756593de5b46a8b6`, `git rev-parse dcb75b59e^1` printed `9ab869b7da52d47708620cdde24dfaf5949df18f`, and the `Pass: none` count printed `1`.
  The first parent is the run head the merge started from. The pass commit's trailer half, `git log
  --first-parent --format=%B dcb75b59e..HEAD` counted for this unit's trailer, is the main loop's after that commit.
- AC3 — observed at `876408728`, the main loop's: `python tools/run-gates/regen.py --check` exited 0 and `python tools/playbook/render_playbook.py --reference --check` exited 0.
  The flip and this ledger came after that reading. They move the indexes alone, which
  `gen_build_index.py --write` rendered over them.
- AC4 — observed: the `grep '^PROJECT_REGISTRY_EXTRA=' .memory-tree.conf` count printed `3`, and the two member heads' `grep -c` printed `2` (DERIVED, both re-read at `d1c26e907`).
- AC5 — observed: over `tools/govkit/registry.toml`, `grep -c` printed `3` for `presets.py`, `4` for `design_lib.py`, `5` for `legacy_ledger.py` and `5` for `coverage_join.py` (DERIVED, re-read at `d1c26e907`).
- AC6 — observed: the first `grep -c` over `tools/lib/resolve-python.test.sh` printed `9` and the second `2` (DERIVED, re-read at `d1c26e907`); `bash -n` over it exited 0 in the first pass.
- AC7 — observed: over `tools/policy/catalogue.toml`, `grep -c '^\[\[key\]\]$'` printed `277`, `grep -c '^\[\[namespace\]\]$'` printed `14` and the three names' count printed `3` (DERIVED, re-read at `d1c26e907`); `tomllib` parsed the file in the first pass.
- AC8 — observed: over `tools/policy/check_policy.py`, the `grep -c` printed `2` (DERIVED, re-read at `d1c26e907`) and `python -m py_compile tools/policy/check_policy.py` exited 0.
  Its three inline blocks equal `owned_scratch.py`'s, block by block (DERIVED, the first pass's byte probe).
- AC9 — observed, the main loop's: `python tools/chain-packet.py --check <slug>` exited 0 for each slug, `grep -c '^- repinned inside a live chain run: '` printed `2` over each packet, and `python tools/check-spec-tokens.py` exited 0, printing `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s) checked` and no row carrying `[packet]`.
  The packet checks were one serial run begun at `4022da267` and ended at `876408728`, whose only change is
  the spec's rev-2 and its records, and one more of dKeptSession over the rev-2 text. The
  second pass ran that last one again over the CLOSED flip and this ledger: `byte compare green`, exit 0.
- AC10 — observed, staged: `bash skills/session-kickoff/manifest-check.sh --staged` exited 0, printing nothing (the first pass). At the merge, the main loop's, the three greps over `memory/guides/SESSION-KICKOFF.md` printed `1`, `1` and `2`, the stamp's sha is the merge's first parent, and a plain `bash skills/session-kickoff/manifest-check.sh` printed no `MANIFEST check 9 FAILED` line.
  That plain run printed check 5 alone, the red §3 gives the close's re-stamp.

## Owed to the close

AC2's trailer half, after the pass commit, and every leg the spec's section 7 names. One red was seen in
the first pass and left, as section 3 rules: `python tools/policy/policy.py lists --check` exited 1, naming
`install.baseline`, `tests.fixture-templates` and `tests.history-verdicts`, main's three keys, `unnamed and
not listed` in `memory/project/unnamed-keys.txt`; the policy check leg will carry it. The two pass legs red
at `dcb75b59e`, `kickoff-manifest ratchet` and `govkit selfcheck`, are the close's by section 7. The spec
mints no arm, so no `New arm:` line is owed a RED-first observation.

The bug-class checklist was run over the six hand-resolved paths in the first pass. Two classes bear on
them: `a-spelling-change-strands-its-readers`, for the note renumbered from the twenty-second to the
twenty-third ordinal, which no reader parses; and `adopter-migration-sweep`, for the catalogue, where
nothing ships that main or the run did not already.

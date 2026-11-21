**Serves:** journal TOOL-dWitnessedBar-4

# TOOL-dWitnessedBar-4 — builder return 1 (run `wf_3e736891-7fe`), committed 7a2701739851d39b4e064a799de1f3589b7fa315

## Why

TOOL-dWitnessedBar-4 is built and committed as one pass commit with a `Pass: TOOL-dWitnessedBar-4` trailer, and the spec header is moved to CLOSED. Before writing anything I checked the spec against the code: the pinned blobs and line numbers matched (the runner's lines are off by one since unit 9), and the eight named readers were the ones `git grep` finds. Nothing blocked the build. Two places where my code is narrower than the spec's wording are recorded as deviation 42 (author-recorded), not treated as a divergence.

## Summary

The unit is built and committed as 7a2701739 on base 8a98c9cf. A sibling's spec commit, 875e875a, landed in this worktree during the pass and touches none of my paths.

**What changed**
- **Runner** (`tools/run-gates/run-gates.sh`): the run record's `verdict` file now carries `tree` (`-` when the run started dirty). Every run that started clean and did not move writes `<common-dir>/gate-verdict/<tree>` (full run) or `<tree>.scoped` (scoped run) in the spec's twelve keys, through a temp name and a rename. A dirty start or a moved tree writes nothing and prints why on one line.
- **Hook** (`.githooks/pre-push`): the candidates are now the pushed tree's two per-tree files, read only for the runner's own bar. One is adopted only when it reads `verdict GREEN`, passes the runner-stamp checks and `check_green_reuse`. `check_bar_base` reads the full file of the base's tree. The covered line prints the record's path.
- **Old writers deleted**: `write_bar_green` is gone from the hook, from `tools/unattended/unattended.sh` and from `tools/run-gates/post-merge.sh`.
- **`tools/push-main.sh`**: `--prepare` reads `verdict.tree` (falling back to `prepared-merge`). Under `build-tip` it pins the tip and makes no merge; either way it prints `push-main: test.merge <value> <sha8> tree <tree>`. The merge code is now its own function, `write_prepared_merge`, which `--land` also calls under `build-tip`, including on its race path.
- **`tools/loop/loop_transition.py`**: `TRANSITION_FIELDS` gains `tree`. The move `testing -> deploying` at `item.test.exit` now exits 1, naming the tree, unless that tree's full per-tree record reads GREEN.
- **Policy**: the `verdict.tree` row gains `summary` and `usage`, is drained from `unsummarised-keys.txt`, and `help/reference/policy.md` is re-rendered with its section.
- **Docs**: the run-gates README describes the record kind.
- **Housekeeping**: kickoff manifest re-stamped, `symbols.json` and the build index regenerated, acceptance ledger written.

**Checks I ran (each stands in for the gate named)**
- **AC1–AC3** (stands in for `run-gates evidence`): the runner over a one-leg scratch clone wrote full GREEN, then RED, then a `.scoped` record that left the full one alone. A dirty start wrote nothing and said so. I ran the runner through a probe script, including under `GATE_FULL=1`, before I met the hook's refusal of the runner for this role; I did not run it again after the refusal. The linked-worktree half of AC1 was refused, so it is owed.
- **AC4/AC5 and the reworked hook arms** (stands in for `pre-push self-test`): I ran an isolated copy of the suite's per-tree section on its own fixture. All 49 arms read ok. (DERIVED from the builder's probe)
- **AC7** (stands in for `push-main self-test`): new arm 42, run alone, read ok.
- **AC8** (stands in for `loop transition record`): the `record` verb exited 1 when the record was missing. `check_tree_verdict` in process gave the RED reason, `None` on GREEN, and refused `../x`.
- **AC9** (stands in for `policy check` and `help reference pages`): checked with `policy.py get`, `lists --write`, the two `grep`s and the re-render.
- **AC6**: `git grep` for `write_bar_green` prints nothing.
- **Lexicon**: every new name was accepted.
- **Bug-class checklist**: I ran it over the commit. It caught a heredoc that had turned `\t` and `\n` into raw bytes in three files; I fixed that before committing, and the commit holds no raw tabs or carriage returns.

**Owed at the close**
- Every leg in §7, plus the RED-first runs of the three `New arm:` lines: the evidence suite's AC1–3, `pre-push.test.sh`'s AC4/5, and `push-main.test.sh` arm 42.
- `.governance/policy.json` is now stale, because its mirror only renders a committed catalogue. It is a pass-leg red to fix after this commit, as with unit 9.
- The reworked covered arm in `pre-push.runlog.test.sh` (root-install stand-in on a side branch) has not been run at all.
- The unattended suite's amended arms are under the README waiver.
- New code paths that no test reaches: `check_tree_verdict`'s no-tree, bad-hash and wrong-tree refusals; `read_verdict_tree`'s fallbacks; the runner's moved-tree and could-not-write lines.
- The runner prints one new stdout line per run. That could break a suite arm that expects the runner's output byte for byte.

**Deviation 42**
- The Test-exit check verifies the tree the move names; it does not work out which tree `verdict.tree` selects.
- Because the hook now reads only the pushed tree's records, the arms that adopted an ancestor's record as a scoped base were retired (25b, BG AC18, slot AC1–3/5/6, PM AC12, TF15 AC1, T16 AC1), along with the arms over the deleted writers.

Kit version bumps are left to the lander's version minting.

**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 build pass 3 — the builder's return

The gov-builder return for the pass dispatched at `426dd9dbd` from [2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-3](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-3.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: §6 AC9's second half, and the deployer-suite change in §2 S4, cannot hold as written. The new `playbook-render` requirement installs a kit whose adopter refuses a target that carries only the `DEPLOY_FULL` answers.

What I observed: I built a fresh target with `tools/govkit/fixture_target.py#build_target` and the deployer suite's `DEPLOY_FULL`, then ran `govkit.py apply --kits memory-recall,memory-tree,playbook-render,playbook,policy`. It exits 1, not 0. recall's `query.py` and the playbook kit's `tag_index.py` do land. But govkit reports "kit 'playbook-render': its adopter exited 1", with render-playbook saying "REFUSED — CI_FILE is derived by probe `ci_file`, it returned nothing for this target". Adding `ci_file = "none"` and `gate_runner = "none"` only moves the refusal on: "COMMAND_CATALOG is an ASKED placeholder and deploy.toml supplies no value for it".

AC9's first half holds: the `memory-recall,memory-tree,playbook` apply exits 2, printing `'memory-recall' requires 'playbook-render'`, and no recall directory lands.

Same cause, second consequence: S4 has the aRF-36 block's applies and `pin_target`'s deploy line in `tools/govkit/selftest.py#main` name the closure. Every one of those applies then exits 1 on the playbook-render adopter. `pin_target`'s deploy line carries only `memory_root`, so it exits 1 too; I probed it, and it still reaches ATTRIBUTES, LAND and RENORMALIZE. `selftest.py#run` writes the receipt pin only on exit 0 (`write_receipt_pin`), so those targets lose their pin. The spec claims the target's declaration matches what it installs, and it does not account for this.

What §2 S4, §4 Files touched and §6 AC9 would have to say:
- Every target that installs the closure (AC9's second apply, and the aRF-36 and pin-block targets in `tools/govkit/selftest.py`) carries `playbook-render`'s placeholder answers. One option is the stubs `tools/govkit/matrix.py#render_deploy_tail` derives from the playbook entry's placeholder rows over `INSTALL_ANSWERS`. That would be reused or factored, and the spec would name the seam.
- Or AC9 and those arms state the exit and output they expect when `playbook-render`'s adopter refuses.

The choice between these is a fork for the spec writer, not mine.

Every other claim I probed holds at 426dd9db. Pass 2's draft applied cleanly, and the rev-5 additions (unborn-HEAD refusal, README notes) build as written.

## Summary

TOOL-dTotalRecall-21 is not committed: AC9 can't pass as the spec writes it (see `why`). I put every path I changed back. The tree is at base 426dd9db again. The only uncommitted change is the main loop's staged `memory/builds/dTotalRecall/RUN.md`, which also holds the extra `--dispatch` row my call added for `.claude/skills/memory-recall/SKILL.md`. The brief was already recorded, and `--brief` said so and changed nothing.

**Draft saved for the next pass.** It is `TOOL-dTotalRecall-21-pass3-draft.patch` in the run's scratch (`git apply --check` confirms it applies cleanly at base). Its paths are listed in `r21-pass3-paths.txt` in the same scratch directory. It is pass 2's draft plus everything that draft still owed, except the generators:
- **Unborn HEAD (S4, AC5):** `query.py` gains `UnbornHeadError`. `load_served_set` runs `git rev-parse --verify -q HEAD` (through `read_worktree_head`) before opening the index. `main` then exits 2 naming the first commit and never mentions removing the index. `check-recall.py#load_served_index` catches the new error.
- **Deployer suite:** `tools/govkit/selftest.py` gains `RECALL_CLOSURE` for the five aRF-36 and pin-block applies, and the closure is on `pin_target`'s deploy line.
- **New arms:**
  - in `tools/memory-recall/selftest.py`: `test_unborn_head_refuses`, with `SELFTEST_ARMS` 88 -> 81 and its provenance line. I also renamed `index_file_of` and `reset_and_list` to declared verbs.
  - in `tools/memory-recall/test_recall_floor.py`: the AC7 arm `test_served_set_leaves_untracked_out` with `build_served_fixture`.
- **Docs:** the README's upgrade notes name `playbook-render`, the unborn-HEAD refusal and the `apply --kits` closure. `memory/map/features/memory-recall.md` is re-pointed to the index.
- **Re-stamps:** `verbatim.json` re-stamped. `VERB_OFFENDER_PIN` 1448 -> 1435 (none arrived; 13 left, each named in its RE-MEASURED line). `SESSION-KICKOFF.md`'s `last-audit` re-stamped.
- **Deviations:** records 1003 (F5) and 1004 (F8), written by `gov_record.py new deviation --caused-by TOOL-dTotalRecall-21`.

**Still owed by the next pass:** `gen_map.py --write`, `gen_build_index.py --write`, the acceptance ledger, the spec CLOSED flip, the manifest-audit delta line in the commit message, and whatever the AC9 fix needs.

**Checks that ran, all on the draft before I put things back:**
- **Fixture repos under `%TEMP%`, through the kit's own CLI** (stands in for the `memory-recall kit selftest` arms and part of `recall floor`):
  - AC3: extracted counts were 2 cold, 0 warm, 1 after one edit, 0 after its commit, and 2 of 2 after a FAMILIES edit.
  - AC4: an untracked record is served in worktree A, not in B, and in B once merged.
  - AC5: a zeroed header gives exit 2 naming the file and its removal, and the file is still there. An unborn HEAD gives exit 2 naming the first commit, with no removal remedy and no index file created.
  - AC8: `gov_tag.py --rebuild` exits 0 twice with no `fts_` table left, and the query between extracts 4.
  - The AC7 arm's logic: check-recall's graded set holds only tracked paths, and the CLI's set holds the untracked one.
  - AC2's tail: an index file exists and there is no `recall/cache/`.
- **AC1 and AC6 greps** came back empty, with `common_git_dir` only as `T.` calls (stands in for `row-grammar selftest` and part of `memory-recall kit selftest`).
- **Naming lexicon:** `--suggest` passes every new name, and `--measure` reads 1435.
- **AC9 over `build_target` fixtures** (stands in for `govkit selftest` and `govkit refusal join`): the first half holds; the second half failed, which is the divergence.
- **Not run:** I did not repeat AC2 and AC7 against `old/` in a scratch clone. Pass 2 saw 12 of 12 questions match, and the changes since then don't touch ranking. `gotchas.py --for-diff` did not run because there is no commit.

No command timed out. Every scratch repo under `%TEMP%` (`r21p`, `r21pb`, `r21pu`, `r21g`, `r21h`, `r21pin`) was removed.

**Owed at the close, after a revised spec and a rebuilt pass:**
- the RED-first observations of both New arms: `tools/memory-recall/selftest.py` for AC3, AC4, AC5 and AC8, and `tools/memory-recall/test_recall_floor.py` for AC7;
- every leg on the spec's gates line, `govkit selftest` included.

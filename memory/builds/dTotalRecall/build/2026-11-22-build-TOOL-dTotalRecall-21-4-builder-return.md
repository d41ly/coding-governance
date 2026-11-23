**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 build pass 4 — the builder's return

The gov-builder return for the pass dispatched at `f9713282e` from [2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-4](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief-4.md), recorded whole; the pass tip is `bd6fe04f8`.

## Why

Rev-6 builds as written. Pass 3's saved draft (`TOOL-dTotalRecall-21-pass3-draft.patch` in the run's scratch) applied cleanly at base. This pass added the two parts that draft still owed. First, S11: the deploy-tail factory moved into tools/govkit/fixture_target.py. Second, S4: the deployer suite's recall closure now runs over one deploy text with stub answers, and its applies are checked at exit 0. Every claim I probed in S4, S11, AC9 and AC10 held against the tree, and AC1 to AC10 were each observed by a fixture or probe.

## Summary

TOOL-dTotalRecall-21 is committed as bd6fe04f8 on base f9713282e. The commit carries the `Pass: TOOL-dTotalRecall-21` and `Co-Authored-By: Claude Opus 5` trailers. Its spec is flipped to CLOSED, dated 2026-11-23, and the generated records table is refreshed. The commit-msg hook and the pre-commit checks passed on the second try. The first try was refused by hygiene check 23 because the AC5 ledger line led with a token the criterion does not spell; I changed it to `git init` and recommitted. `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and listed 63 bug classes. I followed up the move, retirement and long-function-local classes with git greps, and they found no stale reader of the moved factory, no surviving cache-budget key or `recall/cache` reference outside the README's removal note, and no name collision in the suite.

**What this pass built on top of pass 3's draft:**
- **S11:** `INSTALL_ANSWERS`, `derive_bullet_placeholders` and `render_deploy_tail` moved into `tools/govkit/fixture_target.py` with their bodies unchanged. The descriptor is now read from that module's own directory, and `govkit` is imported inside the functions. `tools/govkit/matrix.py` imports all three; `derive_bullet_placeholders` is kept only as a re-export with a `noqa F401`.
- **S4:** in `tools/govkit/selftest.py#main`, the pin block now starts by building `RECALL_CLOSURE` and one deploy text, `deploy_recall`: `DEPLOY_FULL`'s `gov_source` and `prefix` lines followed by `render_deploy_tail` over the closure and `INSTALL_ANSWERS`. The `incomplete`, `optin36` and `optall36` targets and both `pin_target` targets use it. New exit-0 checks cover `incomplete`, `optin36`, `u6p1` and `u6p2`.
- **Records and generators:**
  - acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-21-4-acceptance-ledger.md`;
  - the kickoff manifest's `last-audit` re-stamped, with the `manifest-audit:` delta line in the commit message;
  - `gen_map.py --write`, which changed only `symbols.json`;
  - `gen_build_index.py --write`, which rewrote `memory/backlog/TOOL.md`, the build README and the dClosedLoop as-built view. That last file needed an extra `--dispatch`, and so did `tools/govkit/matrix.py` and `.claude/skills/memory-recall/SKILL.md`; none was refused.
- `--brief` reported the brief as already recorded.

**Checks that ran** (fixtures and probes only; no gate, suite or bar ran):
- **AC1, AC6 and AC10 greps:** each printed exactly what the criterion asks. These stand in for `row-grammar selftest` and part of `memory-recall kit selftest`.
- **AC2, in a local clone under %TEMP% with the pass committed on top and the start commit's `tools/` in `old/`:** 12 of 12 questions printed the same hit lines through the new and old `query.py`. Both read 6258 records and 391118 chunks; the first run extracted 14566 blobs in 33.46 s (each DERIVED, the builder's AC2 clone). Afterwards the common dir held `gov/index-s3.db` and no `recall/cache/`. One workaround: the old kit picked up the clone's new memory-tree until I added an empty `old/.git`. This stands in for `recall floor`.
- **AC7, same clone:** the new `check-recall.py`, the old one, and the new one with `--data-dir` pointing at the index file printed identical per-id, cell and slice lines (24/24, r@5 0.9167). This stands in for `recall floor` and `recall floor arms`.
- **AC3, AC4, AC5 and AC8:** I re-ran pass 3's fixture probe through the kit's CLI and every observation held:
  - AC3: 2 blobs extracted cold, 0 warm, 1 after one edit, 0 after its commit, and 2 after a FAMILIES edit;
  - AC4: an untracked record is served from worktree A only, and from B once merged;
  - AC5: a zeroed header gives exit 2 naming the file and the file stays; an unborn HEAD gives exit 2 naming a first commit and creates no index file;
  - AC8: two `--rebuild`s exit 0 with no `fts_` table left, and the query between them extracts 4.
  
  This stands in for the `memory-recall kit selftest` arms and `tags`.
- **AC9, over `build_target` targets:**
  - the `memory-recall,memory-tree,playbook` apply exits 2 printing `'memory-recall' requires 'playbook-render'`, and no recall directory lands;
  - the closure apply exits 0 and lands `query.py`, `tag_index.py` and `install.json`;
  - over `DEPLOY_FULL`'s answers alone it exits 1 printing `kit 'playbook-render': its adopter exited 1`.
  
  The pin-block targets behaved as the suite now expects: `u6p1`, `u6p2`, `optin36` and `incomplete` exit 0, and `optall36` exits 2 naming the reserved key. This stands in for `govkit selftest` and `govkit refusal join`.
- **Naming lexicon:** `--suggest` passes both moved names, and `--measure` reads 1435, equal to the pin.

**One deviation from S4's wording:** S4 says the `plan --kits memory-recall` arm keeps "its UNMET line". On the exit-0 `incomplete` target, the receipt already satisfies the edge, so plan prints no UNMET line. The arm's actual checks (`query.py` listed, no hook) still hold, so I left it unchanged and recorded this as a `Decided:` trailer.

**Owed at the close:**
- RED-first observations of the three `New arm:` lines:
  - `tools/memory-recall/selftest.py` for AC3, AC4, AC5 and AC8;
  - `tools/memory-recall/test_recall_floor.py` for AC7;
  - `tools/govkit/selftest.py` for AC9, staged by putting `DEPLOY_FULL`'s answers back in place of `deploy_recall`.
- Every leg on section 7's gates line, `govkit acceptance matrix` included, since `matrix.py` now imports the factory.

No command timed out. The scratch repositories under %TEMP% (`r21p`, `r21pb`, `r21pu`, `r21p4`, `r21p4pin`, `r21c`) were removed.

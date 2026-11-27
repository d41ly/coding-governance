**Serves:** journal TOOL-dTotalRecall-3

# TOOL-dTotalRecall-3 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `e1ae60af8` from [2026-11-22-prompt-TOOL-dTotalRecall-3-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-3-build-brief.md), recorded whole; the pass tip is `dd15c0a8b`.

## Why

TOOL-dTotalRecall-3 is built and closed in two commits. The pass commit f8b950c13 holds the work and sets the spec to CLOSED. The follow-up dd15c0a8b adds the self-test arm for the argument refusals, because the bug-class checklist flagged refusal-branch-with-no-arm. Nothing in the spec had to change. Where I departed from it, deviation 35 records it.

## Summary

Built TOOL-dTotalRecall-3, base e1ae60af8, commits f8b950c13 (the pass, spec status CLOSED) and dd15c0a8b (adds the self-test arm for the argument refusals). Both commits end with the trailers `Pass: TOOL-dTotalRecall-3` and `Co-Authored-By: Claude Opus 5`. The brief was already recorded; `--brief` printed "unchanged".

What was built:
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/gov-claim.sh (new): the verbs `slug` and `ask` and the six functions the spec lists. It carries the resolve_python, refuse_wrong_shell, remote_ladder_sh, health_log_sh, gov_feed_sh and gov_ref_sh blocks inline, copied byte for byte. A `blk` comparison shows every block, and gov_ref_sh in all three of its other copies, equal to its canonical.
- tools/lib/gov-ref.sh: `remove_gov_ref` now refuses any ref under `refs/gov/claims/` on one `case` line. The same block was re-copied into tools/unattended/unattended.sh and tools/run-gates/post-merge.sh.
- tools/memory-tree/gen_build_index.py: `derive_mandate_key`, `read_own_claim` and `write_slug_claim` are wired into `cmd_new_build`, plus the self-test function `test_slug_claims`.
- The `claim` row in record-kinds.toml, the rewritten ids rule and the re-rendered kinds region in both HYGIENE.template.md and memory/HYGIENE.md, and the part 2p arm in resolve-python.test.sh.
- VERB_OFFENDER_PIN re-measured from 1446 to 1448. The two new offenders are `wrong_shell_at` and `refuse_wrong_shell`, from the inline refuse_wrong_shell block.
- symbols.json regenerated. The acceptance ledger and deviations 33 (supersedes 31), 34 (supersedes 32) and 35 are in memory/builds/dTotalRecall/build/.
- Extra write paths were declared through `--dispatch`. That verb refused memory/LIVE.md declared beside its generator (check 49); I re-declared without it, and LIVE.md was committed as a generated output.
- The pre-commit hook passed both times.

Checks run, all probes of this unit's own code. No gate, suite or bar ran.
- A scratch probe of gov-claim.sh over a bare remote and its clones under %TEMP%, covering AC1, AC2 (including the floor: a branch naming TOOL-dFloor-14 minted 15), AC3, AC6, AC8 and the argument refusals.
- `test_slug_claims` run on its own by a python probe that imports the module: 13 arms passed in 35 s (DERIVED, that run). This stands in for the build-index selftest leg.
- A probe sourcing gov-ref.sh and gov-feed.sh for AC5: deleting a claim ref returned 2 and the ref stayed; deleting a run ref returned 0 and it was gone. This stands in for part 2p and the python resolver leg.
- A `tomllib` read plus `record_kinds.check_row` for AC7, with no red. This stands in for the record-kinds leg.
- `cmd_new_build` in a fixture with no remote: exit 0, README written, the `local` line printed.

Owed to the close:
- Every §7 leg.
- Both `New arm:` RED-first observations: part 2p in resolve-python.test.sh, staged by deleting the refusal line; and the `gen_build_index.py --selftest` two-clone arms, staged by a copy of gov-claim.sh whose push carries no lease.
- The whole build-index selftest's time against its 350 s ceiling (tools/gate-legs.json). These arms add about 35 s (DERIVED).

Departures from the spec, recorded in deviation 35:
- When two creates race, the remote itself rejects the loser with `[remote rejected] (reference already exists)`. `write_gov_ref` reads that as not completed (rc 2), so the loser exited 2 instead of 1 `taken`. Both verbs now read again once after a write that did not complete: a ref that moved is a lost race, an unmoved ref is the refusal.
- The `slug` verb refuses the slug `asks`, which would block the whole counter subtree.
- CLAUDE_CODE_SESSION_ID is validated before it goes into the commit message.
- Each fetch uses a one-star refspec with `--prune`, so an absent ref is an empty answer rather than a failed fetch that reads as offline.
- The repository root is read before the family and grammar checks.

For the main loop:
- (a) `run_entry_claim` in unattended.sh has the same race defect: a lost create there reads as offline. It is outside this unit's scope.
- (b) Ask TOOL-dTotalRecall-29 (the shared ref writer may delete a claim ref) re-derived from DEFERRED to OPEN. S5 answers it, but the spec carries no `closes`.
- (c) The two-clone arms race two mints at a time over five rounds. The spec's three-retry bound does not hold for ten mints at once.
- (d) The lexicon declares no `sh.file` cell, so no naming convention covers the script's file name.
- Bug-class checklist: run over both commits. Acted on refusal-branch-with-no-arm (commit dd15c0a8b). The others I checked against the code (bounded-through-a-pipe, subprocess-resolves-a-different-shell, fixture-passes-by-finding-nothing, topology-sweep, heredoc) do not apply.
- Another agent's uncommitted revisions to specs 10, 11, 19, 41 and 42, and their rows in the build README, were left unstaged and are still unstaged in the tree. Every bounded command returned within its bound; nothing was skipped.

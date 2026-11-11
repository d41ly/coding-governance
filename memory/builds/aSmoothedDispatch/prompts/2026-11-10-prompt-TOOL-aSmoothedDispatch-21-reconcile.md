# Promotion brief — aSmoothedDispatch: reconcile with aSwiftRefusal on local main

**Serves:** research TOOL-aSmoothedDispatch-21

## The brief

### Goal
The owner said "Land both together" on 2026-11-10. That lands this build with aSwiftRefusal, which sits merged and unpushed on local `main` at `b904a0f91`. Both builds rewrote `--dispatch`'s spec-token check in `tools/unattended/unattended.sh`. This build moved the inline block into `run_spec_token_check`, scoped to the dispatching build's specs and cached, and called it early. aSwiftRefusal moved the inline block below condition 1, so that it runs after every cheap refusal. `git merge --no-ff main` into `branch/aSmoothedDispatch` conflicts in six files. This unit makes that merge commit with both builds' behaviour intact. The check runs once, through `run_spec_token_check`, at aSwiftRefusal's position, after every cheap refusal and before the claim read.

### Items
1. `tools/unattended/unattended.sh`: drop this build's early `run_spec_token_check "$slug" || return 1` call, the HEAD side of the one conflict hunk. Replace aSwiftRefusal's inline `if [ -n "${SPEC_TOKENS_CLI:-}" ]` … `fi` block, which follows condition 1 and now auto-merges in, with that one call. Keep aSwiftRefusal's comment paragraph ("IT RUNS LAST AMONG THE LOCAL REFUSALS (TOOL-aSwiftRefusal-1)") at the call site. No refusal message changes, and no refusal is added or lost.
2. `tools/unattended/unattended.test.sh`: both builds' arms are kept. `FLOOR_ASSERTIONS`, `FLOOR_SHARD_3` and `FLOOR_SHARD_4` carry both sides' raises, with both sides' comment lines. The sums at the merge base are 3329, 445 and 410. Recount them off the merged blocks rather than trusting those sums. Any arm of one build that the other's behaviour now answers differently is fixed in the arm's fixture, never by weakening its assertion. For example, an aSwiftRefusal ordering arm may now meet this build's scoping or cache.
3. `tools/unattended/unarmed-branches.txt`: the spec-token resolver row and every other `unattended.sh` row are keyed to the ordinals they take in the merged driver. Add one `RE-KEYED` comment naming this unit.
4. `tools/unattended/VERBS.template.md`: one paragraph that states both behaviours. It runs after every cheap refusal and before the claim read, and says why. It is scoped to the dispatching build's specs, a hit in another build's spec is noted and admitted, and the run is skipped on a cache match. Re-render `memory/guides/UNATTENDED-VERBS.md` from it with the kit's own renderer, never by hand.
5. `memory/project/readme-contract.txt`: keep both sides' rows, with this build's README beside aSwiftRefusal's and aProfiledEffort's.
6. The merge commit carries every other auto-merged file as git merged it. Re-render the generated outputs the merge stales with their generators: the build index, symbols and LIVE.

### Acceptance
The merge commit has two parents, this branch's tip and `b904a0f91`. `grep -c 'run_spec_token_check "$slug"' tools/unattended/unattended.sh` prints 1, and no inline `SPEC_TOKENS_CLI` block remains in `verb_dispatch`. The harness-arms leg, the refusal-ceiling check in memory hygiene, shell hygiene, install-prefix and docs exit 0 over the merge. Regions 2, 3 and 4 of the driver suite print no FAIL line beyond the inherited ones filed as asks 10 to 13. The main loop observes those regions at the close.

### Gates
`bash -n` on both driver files, the harness-arms leg, shell hygiene, install-prefix, docs and memory hygiene, and the unattended suite's regions 2 to 4 (main loop); then the full bar once, through the lander.

### Non-goals
Any change to what either build's refusals decide, or to their messages. The inherited reds filed as asks 10 to 13. Pushing, and the `--no-ff` merge into `main`, which are the main loop's.

# Acceptance ledger — TOOL-aTwinnedPass-11

**Serves:** journal TOOL-aTwinnedPass-11

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `43c8c6773`. The spec's forks carry their resolutions, and the build follows each:
F1 (a), the two observed spellings and no others; F2 (a), the `wf_` alternative pins its structure
and not its group lengths.

The spec's line citations are at its base `900f656d0`; at the dispatch commit the shape test of
`check_pass_branch` sits at `pass-tree.sh:120`, not `:121`. The line is the same one, so nothing
diverges.

The observations below are each criterion's own command, or the changed code run over a hand-built
fixture, run in the worktree with the change in place before the commit. No suite, gate leg or bar
ran in the pass. The role's hook refused `check-arms.py --check` as a gate leg, so that check is the
main loop's.

The fixture for AC4 and AC5 was built inside the worktree under an untracked folder, removed before
the commit: a repository with the suite's `.unattended.conf`, `.claude/worktrees/` in
`info/exclude`, a `run` branch carrying the records commit C with build tRun's run-state file, no
hook, and no fixture kit, so the merge was clean and the tool announced and skipped `regen.py`. One
script ran the calls of §4 "The arms" twice: over this pass's `pass-tree.sh`, and over the dispatch
commit's copy beside the driver.

Owed to the main loop at the close:
- the `TP11` group of `tools/workflows/unattended-build.test.sh` red, then green, under the breaks
  §7's first `New arm:` line names, with `FLOOR_ASSERTIONS` at 1039;
- the `TP11` block of `tools/unattended/pass-tree.test.sh` red, then green, under the breaks of §7's
  second `New arm:` line, including the conflicted merge of `fx-out.txt` and the README region,
  which the hand-built fixture did not carry;
- `check-arms.py --check`, showing the discovered population did not move;
- the legs of the spec's Gates section.

**Evidences:** TOOL-aTwinnedPass-11
- AC1 — `PASS_NAME` — a `node -e` probe read the `PASS_NAME`, `TREE_SHAPE` and `BRANCH_SHAPE` lines
  out of `tools/workflows/unattended-unit.js`, evaluated them and tested every value the criterion
  lists. All eight admitted values passed and all twenty-three refused values failed; the two
  backslash forms, the quote values and the newline values were built with `String.fromCharCode`, so
  the shell carried them as the intended bytes. With `PASS_NAME`'s alternation put back to
  `agent-[A-Za-z0-9]+$`, `TREE_SHAPE.source` equals the source of the dispatch commit's literal
  (`true`), so the prefix's `..` lookahead, its backslash alternative and its anchor are unchanged.
- AC2 — `run_wf` — a `node -e` stub of `agent`, evaluating the harness as `run_wf` does with
  `passBase`, `writes` and `passLegs` set, returned the `wf_` return's `branch` and `worktree`
  unchanged, and its `nextAction` carried
  ``with its working directory at `/w/.claude/worktrees/wf_0d688c69-edb-1`, before that worktree is merged back``.
  The hostile `wf_` tail, `worktree-wf_x` and `worktree-foo` each returned `""` for both fields with
  `nextAction` naming the path unusable, and the hostile return's JSON carried no
  `wf_0d688c69-edb-1`. The suite's `TP11` and `TP4` groups are owed to the main loop.
- AC3 — `grep -c` — `wf_\[0-9a-f\]` and `agent-\[A-Za-z0-9\]` each counted `1` in
  `tools/workflows/unattended-unit.js` and `1` in `tools/unattended/pass-tree.sh`. A bash probe
  testing the regex read out of `pass-tree.sh` admitted `worktree-agent-x1` and
  `worktree-wf_0d688c69-edb-1`, and refused `worktree-wf_x`, `worktree-foo`,
  `worktree-wf_0d688c69-edb`, a `;id` tail, a `$(id)` tail, a newline tail and `agent-x1`.
- AC4 — `worktree-wf_0d688c69-edb-1` — over the fixture, `--merge tRun --pass TOOL-tRun-12 --branch worktree-wf_0d688c69-edb-1 --from <C>`,
  with that branch at `<primary>/.claude/worktrees/wf_0d688c69-edb-1` holding one pass commit,
  exited 0; its stdout was `HEAD`, the merge's second parent was the pass commit, and the worktree
  and branch were gone. Over the dispatch commit's tool it exited 1 with
  `is not a branch the runtime cuts for a pass (worktree-agent-<id>)`, and both remained.
- AC5 — `where the runtime cuts that pass's worktree` — `--remove tRun --branch worktree-wf_0d688c69-edb-2`,
  held at `<primary>/.claude/worktrees/wf_0d688c69-edb-3`, exited 1 with the holder refusal naming
  both paths, and the directory and branch remained. `--remove` naming `worktree-wf_x`, held at
  `.claude/worktrees/wf_x`, exited 1 with `is not a branch the runtime cuts for a pass`, the text
  naming both spellings, and the directory remained. Over the dispatch commit's tool both exited 1
  on the shape refusal, so the holder arm's red is the staged break §7 names, owed to the main loop.
- AC6 — `wf_<run id>-<n>` — `grep` finds it in the comment above `PASS_NAME` in
  `tools/workflows/unattended-unit.js`, and in the header's section 4 and the comment above
  `check_pass_holder` in `tools/unattended/pass-tree.sh`; `grep -c 'tools/unattended'` over
  `pass-tree.sh` printed `0`. After `gen_map.py --write`,
  `git diff --quiet -- memory/map/generated/symbols.json` exited 0, and no generated output moved.

## The close

The main loop's observations at the close, on node a, 2026-11-15, at `1bf0e9f78`.

- `tools/unattended/pass-tree.test.sh`: GREEN, 169 assertions and 0 FAIL lines; RED with `pass-tree.sh` put back to `43c8c6773`, 6 FAIL lines, every one a `TP11` arm (PINNED 2026-11-15).
- `tools/workflows/unattended-build.test.sh`: GREEN, 1541 assertions and 0 FAIL lines; RED with `unattended-unit.js` put back to `43c8c6773`, 3 FAIL lines, every one a `TP11` arm (PINNED 2026-11-15).
- The per-group staged breaks of the `wf_` pattern were not staged; the closing review's round 3 filed the missing interior arms as `TOOL-aTwinnedPass-12`.

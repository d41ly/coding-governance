# TOOL-dSettledStage-1 — acceptance ledger

**Serves:** journal TOOL-dSettledStage-1

No merge bar, no self-test suite and no arm of `tools/push-main.test.sh` ran in this pass. The pass
started at 6daf04180. Each probe ran from the worktree root in Git Bash as a script under the session
scratchpad, its fixture repositories under `%TEMP%`: `probe43.sh` (arm 43's body, the two functions
cut from a named lander with arm 38's `sed -n` idiom) and `probe-land.sh` (the attended lander run
over a clone of this worktree at HEAD with a stub pre-push hook writing the allow record, as the
suite's fixtures do, the lander under probe copied in and committed first). The base lander is
`git show 12764ec2:tools/push-main.sh`.

**Evidences:** TOOL-dSettledStage-1
- AC1 — `gating + pushing` — `probe-land.sh eol` over the built lander printed `eol-dirty=1`,
  `eol-empty=1` and `clean=1`, then the lander's `gating + pushing` line, `rc=0`, `landed=1` and
  `regen-commits=0`. The same probe over the base lander printed the three liveness lines, then
  `could not commit the regenerated outputs`, `rc=1` and no `landed=1`. This is a hand-built
  fixture of the lander, not arm 42; arm 42's own RED and GREEN are owed to the close.
- AC2 — `write_merge_fold` — `probe43.sh` over the built lander printed `eol-rc=0`,
  `eol-head=same`, `real-rc=0` and `real-moved=1` after `git status --porcelain` named `f.txt`
  dirty by line endings only. Over the base lander it printed `eol-rc=0`, `real-rc=0` and
  `real-moved=1` and no `eol-head=same`: the base fold moved HEAD over the unchanged tree.
- AC3 — `grep -c 'git add -A' tools/push-main.sh` — printed 1, the line inside
  `write_staged_change`; the spec's `grep -cE` over the two caller shapes printed 4.
- AC4 — `TOOL-tFix-29` — `probe-land.sh stale` over the built lander, arm 29's stale bug-class
  index with a spec defining `TOOL-tFix-29`, printed `rc=0` and `landed=1`, and HEAD's subject was
  `regen: generated outputs onto origin/main at <sha8> for TOOL-tFix-29` with `head-pass=none`.
- AC5 — `git grep -h -E -e '--no-verify|could not commit|could not fold' 12764ec2 -- tools/push-main.sh`
  — `diff` of its output against the spec's `grep -E` over the built lander printed nothing.
- AC6 — `write_staged_change` — the spec's `sed -n` paragraph prints a sentence naming
  `write_staged_change` and saying a regeneration staging no change makes no commit.

**Also probed:** `write_staged_change` cut from the built lander answered 1 on a clean tree and 0 on
a tree whose only change is an untracked file, which it staged. `bash -n` passed over both files.
`lexicon.py --suggest write_staged_change --as sh.function` answered OK.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/push-main.test.sh` 42, covering AC1: RED with the three attended sites of the
  base 12764ec2 lander restored, GREEN once restored.
- New arm `tools/push-main.test.sh` 43, covering AC2: RED with the base 12764ec2 `write_merge_fold`
  restored, GREEN once restored.
- The gates section 7 names, the `push-main self-test` and `harness arms` among them.

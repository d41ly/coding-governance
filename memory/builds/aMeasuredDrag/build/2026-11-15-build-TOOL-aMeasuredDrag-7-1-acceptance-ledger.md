# TOOL-aMeasuredDrag-7 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-7

No merge bar and no self-test suite ran in this pass. The pass started at 5b503148. AC1, AC2 and AC4
ran in the worktree in Git Bash, before the edit and again after it, with outputs saved to the session
scratchpad as `md7-ac1-before.txt`, `md7-ac1-after.txt`, `md7-ac2-before.txt` and
`md7-ac2-after.txt`. AC1 ran as the spec's own block, saved as `md7-ac1.py`, over the `bp` fixture
folder in the scratchpad.

**Evidences:** TOOL-aMeasuredDrag-7
- AC1 — `sibling_kept True` — after the edit the block printed `budget_mb 2048.0`, `lines []` and
  `sibling_kept True`. Before it, at 5b503148, it printed `budget_mb 512.0`, one
  `evicted the least-recently-queried cache: sib` line and `sibling_kept False`. That before run is the
  red the spec names, observed on the unedited key.
- AC2 — `718d6dd8e2cc` — the one-line probe printed byte-identical output before and after the edit
  (`cmp` silent), and both open with the digest `718d6dd8e2cc`, PINNED at 5b503148.
- AC3 — `built_s` — owed to the main loop: the warm query timed twice after the pass commit.
  - before: the one cache under `<git-common-dir>/recall/cache` holds `built_s` 82.28 s, PINNED at
    5b503148 (built 2026-11-15T03:36:51Z by another worktree). This is the cost an evicted sibling
    pays. The spec's figures are 32 s and 62 s, PINNED at 6d98c39ca.
  - after: owed, the second warm run's time, at the close.
  - spawn baseline: 1.969 s per 10 runs of `/usr/bin/true`, PINNED at 5b503148. The spec's figure is
    0.31 s per 10 runs, PINNED at 6d98c39ca, so this machine was under load when sampled.
  - The cache measured 402 MB by `du -sm`, PINNED at 5b503148, as at 6d98c39ca.
- AC4 — `402 MB` — before the edit the stale grep printed `.memory-tree.conf:656` and
  `tools/memory-recall/README.md:126`; after it, it printed nothing (rc 1). `grep -n "402 MB"` prints
  one line, `:657`, carrying `6d98c39ca`. `git diff -U0 -- .memory-tree.conf` shows hunks at
  `-656,2` and `-663` only, inside the block below `REFUSAL_CEILINGS` (line 653) and above the blank
  line after the key, so neither line 653 nor line 664 moved.
- AC5 — `last-audit:` — the manifest's one changed line is `last-audit:`, stamped
  `@ 5b503148330e3bc85abf82da0bae21ca8a410e81`, the parent of this unit's commit. The staged ratchet
  leg's verdict on the commit is the pre-commit hook's.

**Owed to the close (the main loop, after every unit is terminal):**
- No new arm. Spec §6 adds none, so no RED-first observation is owed.
- AC3's after figure, as above.
- The gates in spec §6: `kickoff-manifest ratchet`, `kit/dogfood doc parity`, `recall floor`,
  `recall floor arms`, `transition-audit arms` and `straggler-guard arms`.

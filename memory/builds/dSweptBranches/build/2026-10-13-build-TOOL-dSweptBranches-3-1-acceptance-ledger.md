# Acceptance ledger — TOOL-dSweptBranches-3

**Serves:** journal TOOL-dSweptBranches-3

Built on `d48ccf0a`, inline, after unit 4. The write fixture holds one row of each verdict —
`MERGED`, `EQUIVALENT` (a cherry-picked copy), `UNMERGED-LIVE`, `IN-PROGRESS` (a build README at
`INPROGRESS`) and `UNKNOWN` (an orphan branch sharing no history) — with a worktree on the merged and
on the live branch, and both of those branches published to `upstream`. The arms run `main`
in-process, so a seam can stage a failed or busy removal, and read `WRITE_TRACE` for the order.

Two harness findings were fixed in the pass. A trace appended after each act let a manifest written
late still read first, so the trace now records each act before it runs. And the default branch is
excluded by name in two places, so a break of one guard alone is masked by the other; the staged
break removes both.

The pass also renames three helpers in unit 4's arms that the lexicon refuses: `fail_git`,
`leave_skeleton` and `spy`.

**Evidences:** TOOL-dSweptBranches-3
- AC1 — `WRITE_TRACE` — the manifest is the first entry, sits under `--git-common-dir`, and lists every branch tip and both worktree `HEAD`s; red with the manifest write removed, and with its worktree lines dropped
- AC2 — `branch_reconcile.py --write` — afterwards only `main`, `live-br`, `open-br` and `orphan-br` remain, the merged worktree is gone and the live one stays, and `upstream` still holds `merged-br`; red with `UNMERGED-LIVE` admitted to the deletable set
- AC3 — `--remote` — one push deleted exactly `merged-br` from `upstream`, `live-br` stayed, the run exited 0 and the remote `main` tip is unchanged; red with the push naming `live-br`, and with both default-branch guards removed
- AC4 — `branch_reconcile.py --write` — one staged failed removal printed `failed — worktree`, the other deletable worktree was still removed, and the exit was 1; a busy removal printed `busy — worktree` and exited 0; red with a failure aborting the run, and with busy counted as a failure

All 52 checks across the eleven arms ran green in 25 s on node d.

## Owed at the close

The `branch-reconcile selftest` leg and the spec's §7 legs run in the close's bar.

## Rev-3 — the closing review's two blockers

Folded on `0ac2418c` from the closing review, round 1
(`2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`).

- AC5 — `arm_keeps` — run from a linked worktree with the primary on `side`: a merged worktree holding a live nested worktree reads `keep (contains kept worktree …)` and survives `--write` with the nested file; the primary reads `keep (the primary worktree)`, and local and `upstream` `main` read `keep (the default branch)`, and all survive; no action carries ` · `. Red with the containment keep removed; red with the primary keep removed, where `--write` deleted the fixture's primary repository outright; red with both default-branch guards removed

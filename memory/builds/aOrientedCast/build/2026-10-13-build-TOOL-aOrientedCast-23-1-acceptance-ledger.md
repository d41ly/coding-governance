# TOOL-aOrientedCast-23 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-23

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran, from the worktree
root on the staged tree: the greps and counts each criterion names, `bash -n` over the size gate, a
CR-stripped byte count and a line count of the method's render, and `git rev-list --count` for the
kickoff manifest's check 9. The texts of §4 "The rule" and "The pointers" are built verbatim, as the
owner ratified them. Owed to the main loop at the close (M8): every leg §7 lists. §7 declares no
`New arm:`, so no RED-first observation is owed. The second pass, building rev-3, changed term 4's
one line of the limits file and nothing else, and observed AC9 by its two greps on the working tree
and its `git diff --numstat` on the pass's commit; AC1 to AC8 stand as the first pass observed them.

**Evidences:** TOOL-aOrientedCast-23
- AC1 — `WHEN A RUN MAY RAISE A ROW` — the grep printed lines 10, 16 and 27 in that order, the `WHO WRITES THIS FILE: a person or a run` sentence, the rule's title and the quoted `perfectly resolvable on your own`, all above the first row, `coding-governance-agents.template.md`, at line 48.
- AC2 — `A declared ceiling is the owner's to move unless the file declaring it states` — the count printed 1 for the template and 1 for the render, the line sitting after the `may:` sentence of M3's "What is delegated", and `grep -c "template-size-limits"` over the template printed 0.
- AC3 — `on the terms the header of` — `grep -c "OWNER decision"` printed 0, the new phrase counted 1, and `bash -n tools/check-template-size.sh` exited 0.
- AC4 — `reserve its next movement to the owner` — the `git grep -l` printed `tools/template-size-limits.txt` alone.
- AC5 — `^- TOOL-aOrientedCast-23 · ` — the count printed 1, the row sits at line 138, between `## TOOL — tooling` at 20 and `## DEPL — deployer` at 140, awk measured it at 240, under 300, and this commit leaves `memory/DECISIONS.md` alone: the main loop committed the row at a75ade2e.
- AC6 — `^KIT_MEMORY_TREE_VERSION=2.148` — the count printed 1 and the `gov:kit memory-tree@2.147` grep over tools, memory/HYGIENE.md, memory/TEMPLATE-SPEC.md and memory/guides printed nothing; the four templates and four renders carry the 2.148 marker.
- AC7 — `tr -d '\r' < memory/guides/BUILD-METHOD.md | wc -c` — it printed 29322, at most 30720, and the line count printed 362, at most 400.
- AC8 — `last-audit:` — the stamp moved from `f76d7b9c…` to `2026-10-13T12:01:29+03:00 @ a75ade2e3560155650eccb82a82d437aec0d1e5f`, the sha of this commit's parent; check 9's count since `last-body-change` was 6, under 9, so `last-body-change` stays.
- AC9 — `the run records that unit's row in memory/DECISIONS.md before or with the raise` — the anchored grep printed 1 at line 23, `grep -c "the same commit adds that unit's row"` printed 0, and `git diff --numstat HEAD~1 HEAD -- tools/template-size-limits.txt` printed 1 added and 1 deleted, one line changed each way.

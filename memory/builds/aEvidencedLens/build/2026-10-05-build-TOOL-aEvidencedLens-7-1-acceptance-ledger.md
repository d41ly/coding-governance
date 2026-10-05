# TOOL-aEvidencedLens-7 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-7

`--review` counts highs and minors at every subject's terminal exit and refuses `fold` everywhere. The
pass commit `694b7b63f` records no direct `--review` run against a scratch fixture: it rewrote the
`unattended.test.sh` arms that pinned the old spec-subject behaviour and the converged spec round of
`runlog-writer.test.sh`, and says neither suite was run. It records AC9's figure. The greps below
were re-run at `3bf1726b5`; `unattended.sh` moved after the pass in `029b0522a`, `efad4cee4` and
`94d99c6ca`, so a reading at HEAD is not a reading at the pass. AC8's floor half was re-run by
extracting check 2's awk program from `tools/unattended/check-unattended.sh` at HEAD into the scratch.

**Evidences:** TOOL-aEvidencedLens-7
- AC1 — `S9` — no arm runs the criterion's own row, `S9` at `--blockers 1 --highs 0 --minors 2` printing `BOUNDED`; the nearest arms are the `B1` and `B3` blocks of `unattended.test.sh`, which write a `BOUNDED` spec row carrying `--highs`, `--minors` and `--disposition promote`. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC2 — `--highs and --minors` — the `S9` arms for `--blockers 0 --highs 1` and `--blockers 0`, the `B3` arm for `--blockers 2 --disposition promote`, and `a refused spec-subject round wrote no row (closing review round 1, L6)` carry it. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC3 — `CONVERGING` — the `S9` arm for `--verdict BLOCKED --blockers 3 --minors 1` expects the refusal that a count is a claim about an exit that has not happened yet. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC4 — `fold is legal only at CONVERGED` — the `S9` arm for `--minors 3` with no disposition expects the `requires --disposition promote` refusal, the `C3` arm expects the converged fold refused and `a refused converged fold wrote nothing`, and the `D2` and `B1` arms `miss` that sentence. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC5 — `promote` — the `S9` arm for a zero-standing `--disposition promote` expects the refusal that it promotes nothing, and the `C1` arm writes a zero-count converged row with no disposition. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC6 — `blockers 1 · BOUNDED · highs 1 · minors 4 · disposition promote` — the `B3` arm expects that row ending, `this exit owes at least 3 new unit(s)` and the batched sentence, and `a bounded spec exit's counts sit before the disposition`. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC7 — `FOLDED into the spec` — the criterion's `grep -nE` over `tools/unattended/unattended.sh` printed nothing at HEAD (rc 1), and the same pattern counted 6 lines over `git show 694b7b63f~1:tools/unattended/unattended.sh`, so the probe can move.
- AC8 — `newids=2` — the floor half was run directly: AC6's row through check 2's awk program extracted at HEAD, with `graded=1` and `readable=1`, printed `against a floor of 3` at `newids=2` and nothing at `newids=3`. The byte-identical replay of the slug subject's `TOOL-aBatchedMinors-2` rounds is suite-only. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC9 — `FOLD_CUTOFF=` — `grep -nE` printed `FOLD_CUTOFF="2026-09-15"` at line 836 and `SPEC_COUNTS_CUTOFF="2026-10-06"` at line 846, at HEAD and at `694b7b63f`. The commit records the newest spec-subject `review · item` row across 31 refs as 2026-10-05T01:11:02Z (`aEvidencedLens-spec-set-r2`). A `git grep` over every `RUN*.md` in the `694b7b63f` tree, one ref only, found the same newest row; the cutoff is a day later.

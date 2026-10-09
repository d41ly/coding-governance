# DEPL-aFrugalTurnstile-1 — acceptance ledger

**Serves:** journal DEPL-aFrugalTurnstile-1

No merge bar, no runner and no self-test suite ran in this pass. The checks were the greps the spec
names, run over `WIRE-INTO-PROJECT.md` at `bef97330` (RED: the new item's grep counted 0 and the
table-row count was 0) and over the edited working copy (GREEN, below), plus the install-prefix
checker run directly. The close still owes every §7 leg: install-prefix, govkit runbook parity,
dead-path carriers, memory hygiene and spec tokens.

**Evidences:** DEPL-aFrugalTurnstile-1
- AC1 — `grep -n 'Optional, to land on the scoped bar' WIRE-INTO-PROJECT.md` — one hit at line 788,
  after the doc-push item at 784 and before "Also copy" at 803; the bullet carries
  `GATE_POST_MERGE=local`, `GATE_POST_MERGE=ci` and `refs/gov/bar-red`.
- AC2 — amended rev-2 — the row count grew from 0 to seven, not eight, because the `^ *\| ` pattern
  does not match the `|---|` separator; the spec's §9 rev-2 line logs it. The three
  `--hold --`, `post-merge.sh <sha>` and `relaxing any rule of your own` greps hit lines 798, 800
  and 801.
- AC3 — `bash tools/check-install-prefix.sh` — exit 0, "clean", 0 kit-path spellings; the one
  `run-gates/post-merge.sh` hit is spelled `<prefix>/run-gates/post-merge.sh`.
- AC4 — `git diff --cached -- WIRE-INTO-PROJECT.md | cat -A` — 0 added lines end in `^M$` after
  staging the 14 added lines.

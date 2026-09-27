# aShardedFloor — asks

## Asks

- TOOL-aShardedFloor-1 · filed 2026-08-21 · `run-gates evidence` was UNRUNNABLE inside a bar whose parent exports GATE_BASE, which `.githooks/pre-push` does: `rec_run` passed the ambient env into the nested runner it grades, which resolved a sha its scratch lacks, ran everything and skipped nothing, so the arm whose subject IS a skipped leg refused. Latent. FIXED: `rec_run` clears the GATE_* vars. Class `memory/gotchas/inputs-inside-the-subjects-reach.md`

## Dispositions

- CLOSED · TOOL-aShardedFloor-1 · by 381345dd4d44d47cb2332f8323119df7ecedf3c8 · `run-gates evidence` was UNRUNNABLE inside a bar whose parent exports GATE_BASE, which `.githooks/pre-push` does: `rec_run` passed the ambient env into the nested runner it grades, which resolved a sha its scratch lacks, ran everything and skipped nothing, so the arm whose subject IS a skipped leg refused. Latent. FIXED: `rec_run` clears the GATE_* vars. Class `memory/gotchas/inputs-inside-the-subjects-reach.md`

# Acceptance ledger — TOOL-dThriftyLanding-8

**Serves:** journal TOOL-dThriftyLanding-8

Built on `7f1fa5f1`. The arm is the merged-side-branch assertion in canary section 3i2. A slice holding
the canary's prologue, section 3's setup and 3i2 passed 10 assertions against this runner and failed
that one assertion against the runner at `f765eb8e`.

**Evidences:** TOOL-dThriftyLanding-8
- AC1 — `GATE ok    reads b only` — printed when notes/b.md was edited and restored on a side branch merged with `--no-ff` past the docs base; the f765eb8e runner printed `GATE skip` for it

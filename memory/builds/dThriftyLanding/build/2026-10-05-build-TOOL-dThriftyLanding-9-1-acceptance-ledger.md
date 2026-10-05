# Acceptance ledger — TOOL-dThriftyLanding-9

**Serves:** journal TOOL-dThriftyLanding-9

Built on `dd229b04`. The arm, `DOCS U9`, sits in the hook suite's DOCS block before AC4. A slice holding
the suite's prologue and that block passed against this hook and failed only `DOCS U9` against the
hook at `f765eb8e`.

**Evidences:** TOOL-dThriftyLanding-9
- AC1 — `docs-only` — absent from the decision line when src/z.sh was added and removed on a side branch merged with `--no-ff`; the f765eb8e hook printed `docs-only` for that push

# memory/map — the self-verifying codebase map

Feature dossiers whose machine claims are CI-verified against live code inventories, a
generated system map, and a git-range digest. Kit: `codebase-map/` (coding-governance);
inventories: `codebase-map/map_extractors.py`; gate: see `.codebase-map.conf` GATE_FILE.

## Layout
- `FOUNDATION.md` — shared-substrate claims (same contract as a dossier).
- `baseline.toml` — shrink-only ratchet baseline (backfill inventory; never add new keys).
- `affordance-exempt.toml` — shrink-only grace list for dossiers predating `## Reuse affordance`
  (seeded at adoption; a new dossier is never graced, a touch drops entries).
- `features/<feature>.md` — one dossier per feature: first ```toml fence = machine claims,
  then `## Constraints & why` · `## Shared seams` · `## Gaps` · `## Reuse affordance` prose.
- `generated/` — `inventories.json` (keys-only) + `MAP.md` (claimant-annotated) + `symbols.json`
  (reuse-recall index — only when the SYMBOL tier is declared in map_extractors.py); regenerate
  with `python codebase-map/gen_map.py --write`, never hand-edit.

## How to claim (quickstart)
1. You add an inventoried moving part -> the gate fails naming the key.
2. Claim it in the owning dossier's toml fence (create the dossier from any existing one).
3. Shared substrate -> claim in `FOUNDATION.md` instead.
4. Claim edits stale `generated/MAP.md` -> run `python codebase-map/gen_map.py --write`
   in the same commit (`--check` to verify).
5. Digest any range: `python tools/codebase-map/map_diff.py <base>..<head>` (`--verbose` for files).

## Rules
- Claims are exact keys, gate-enforced BOTH directions (a claim naming a dead key fails too).
- Path globs are digest-only, never gated; overlap is legal (multi-claim >= 1 owner).
- Shared mega-modules are documented in dossiers' "Shared seams" prose, never glob-claimed.
- Substantial work touching an undossiered feature creates its dossier at design time.
- New dossiers must record a reuse decision in `## Reuse affordance`: one
  `seam: <id> — reuse for <need>; extend via <point>` line per seam this feature is reused through,
  or `none — <why feature-specific>` (presence gated, content not). BEFORE building, run
  `python codebase-map/reuse_lookup.py "<behaviour>"` to find an existing seam to wire through
  instead of reinventing it (see `codebase-map/reuse-lookup.agent.md`).

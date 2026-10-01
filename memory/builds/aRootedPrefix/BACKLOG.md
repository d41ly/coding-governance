# aRootedPrefix — asks

## Asks

- TOOL-aRootedPrefix-1 · filed 2026-08-09 · unit · codebase-map hardcoded its `<root>/codebase-map/` install convention and answered from an empty corpus at any other prefix — landed on main (`map_lib.resolve_root`, kit 1.1); the record is in DECISIONS.md
- TOOL-aRootedPrefix-2 · filed 2026-08-09 · `REGEN_CMD` and the scaffolded map README spelled a kit path that does not exist at a prefixed install — closed by TOOL-aRootedPrefix-1 at rev-2 (S9); the record is in DECISIONS.md
- TOOL-aRootedPrefix-3 · filed 2026-08-09 · hygiene checks 6/7 measure RAW working-tree bytes, so an adopter without the eol=lf pin still gets a platform-dependent cap and entry budget — normalize before measuring, as `check-template-size.sh` already does

## Dispositions

- CLOSED · TOOL-aRootedPrefix-1 · by f54143f1e749bd917e9b3b77fc5369cc8c3f6da9 · codebase-map hardcoded its `<root>/codebase-map/` install convention and answered from an empty corpus at any other prefix — landed on main (`map_lib.resolve_root`, kit 1.1); the record is in DECISIONS.md
- CLOSED · TOOL-aRootedPrefix-2 · by TOOL-aRootedPrefix-1 · `REGEN_CMD` and the scaffolded map README spelled a kit path that does not exist at a prefixed install — closed by TOOL-aRootedPrefix-1 at rev-2 (S9); the record is in DECISIONS.md

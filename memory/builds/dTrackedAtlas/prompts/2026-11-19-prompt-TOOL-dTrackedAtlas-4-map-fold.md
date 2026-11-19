# Revision — dTrackedAtlas: TOOL-dTrackedAtlas-4 claims its hook in the codebase map

**Serves:** research TOOL-dTrackedAtlas-4

## The prompt

> Unit 4's second dispatch built the unit, and the pre-commit codebase-map gate refused its commit: the new `PostToolUse` hook group is a `harness-hooks` inventory key no dossier claims, and the generated inventory is stale.

## The brief

### Goal
Revise `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md` so its write set and gates carry the codebase map's claim of the hook it wires. The refusal named `test_every_inventory_key_is_claimed_or_baselined`, UNCLAIMED `harness-hooks` `PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js`, and `test_generated_artifacts_are_fresh` on `memory/map/generated/inventories.json`; `memory/map/baseline.toml` is reserved for the initial backfill. The main loop decided the claim's home: a new dossier, `memory/map/features/closed-loop-atlas.md`, because every existing dossier is scoped to one kit and `memory/map/FOUNDATION.md` holds shared substrate, which this build-folder hook is not.

### Items
1. Add the dossier to the spec: its feature name, title, status, streams, decisions (this build's unit ids), its `[claims]` with the one `harness-hooks` row and empty rows for every other claim kind, and `[paths]` globs naming this build's code files and nothing another dossier already globs. Read two existing dossiers, such as `memory/map/features/runlog.md`, and `tools/codebase-map/README.md` for the shape, the caps and what the coverage tests grade, and verify that no glob you write overlaps another dossier's.
2. Add to section 4's Files touched the dossier and every generated file `python tools/codebase-map/gen_map.py --write` rewrites when a dossier is added, after reading which files that is.
3. Add to section 7 the codebase-map legs that grade the claim and the generated files, by their names in `tools/gate-legs.json`.
4. Correct any sentence in section 3 or 4 implying the wiring touches no graded inventory.
5. Bump the rev and add one revision-log line naming this record and what moved; no other design change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades unit 4 READY; `--check-specs dTrackedAtlas TOOL-dTrackedAtlas-4` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean; every new function name the spec declares still gets an OK line from the lexicon's `--suggest`.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
No change to the hook's design; no product code and no dossier written in this pass, which the builder writes; no commit and no index render, which the main loop does.

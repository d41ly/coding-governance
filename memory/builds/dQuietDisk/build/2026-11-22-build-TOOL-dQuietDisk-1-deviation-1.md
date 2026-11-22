# TOOL-dQuietDisk-1 deviation 1 — the map's foundation dossier claims the new `history-store selftest` leg

**Serves:** deviation TOOL-dQuietDisk-1

- **Departs from:** `TOOL-dQuietDisk-1@rev-4` [Files touched]
- **Hand-off:** spec-to-code
- **Before:** the spec's Files touched, an estimate, names the store's files, the leg's `[[exempt_leg]]` row in `tools/govkit/registry.toml`, the rendered `tools/gate-legs.json`, its budget row and the kickoff manifest, and names no dossier under `memory/map/` to claim the new leg.
- **After:** the pass commit also appends `"history-store selftest"` to the `gate-legs` row of `memory/map/FOUNDATION.md`'s `[claims]` table, and the map's generated files are regenerated from it; no other claim and no other row of that file changed.
- **Cause:** builder discovery
- **Reason:** Files touched left out the map claim the new leg needs. Every gate leg must be claimed by one dossier, and the pre-commit codebase-map gate refused the third pass's commit because `history-store selftest` was claimed by none. The leg runs `tools/lib/history-store.sh`, and `tools/lib/` is gov-internal shared substrate owned by no single feature, so the foundation dossier, whose claim policy covers shared substrate, is where the claim lands (PINNED, the third pass's refused commit and the fourth dispatch's brief).
- **Evidence:** after the edit, `python tools/codebase-map/gen_map.py --write` exited 0. The regenerated `memory/map/generated/MAP.md` lists `history-store selftest` against `foundation`, and `memory/map/generated/inventories.json` lists it among the gate legs (PINNED, that run in this pass).
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** ask TOOL-dQuietDisk-1
- **Caused-by:** TOOL-dQuietDisk-1

# DEPL-dShippedRelease-78 deviation 781 — DEPL-dShippedRelease-78 S59 names its lease-epoch surface

**Serves:** deviation DEPL-dShippedRelease-78

- **Departs from:** `DEPL-dShippedRelease-78@rev-3`
- **Hand-off:** spec-revised
- **Before:** `DEPL-dShippedRelease-78`'s spec as the revision at `DEPL-dShippedRelease-78@rev-3` reads it, whose S59 "re-reads the lease epoch" of unit 15's run lease through no named surface.
- **After:** the spec at rev-4: S59 re-reads it as the sixth TAB field of TOOL-dPlacedRequest-34 S22's read-only `unattended.sh --lease status run release <E>`, the field DEPL-dShippedRelease-138 S48's `read_lease_epoch` reads for the build lease, and reads `lease — none · <tail>` as not the holder.
- **Cause:** external
- **Reason:** the 2026-11-03 parents cross-check listed the unnamed read as this build's own gap, and the owner asked on 2026-11-03 to fix it. No code has started.
- **Evidence:** the brief `memory/builds/dShippedRelease/prompts/2026-11-03-prompt-DEPL-dShippedRelease-78-lease-epoch-surface.md`, the writer's return `memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-78-lease-epoch-returns.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dShippedRelease/prompts/2026-11-03-prompt-DEPL-dShippedRelease-78-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask DEPL-dShippedRelease-32
- **Caused-by:** 2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck

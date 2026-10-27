# TOOL-dFurnishedOrders-15 deviation 151 — TOOL-dFurnishedOrders-15's spec re-grounded against dBoundRoles, dTotalRecall and dKeptSession' landed specs

**Serves:** deviation TOOL-dFurnishedOrders-15

- **Departs from:** `TOOL-dFurnishedOrders-15@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dFurnishedOrders-15`'s spec as the revision at `TOOL-dFurnishedOrders-15@rev-2` reads it, written before dBoundRoles, dTotalRecall and dKeptSession re-grounded and naming their interfaces, or the rules they now apply to every spec, from their earlier text.
- **After:** the spec at rev-3, revised for the cross-check record's row 60, as the brief `memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md` states for this spec.
- **Cause:** external
- **Reason:** dBoundRoles, dTotalRecall and dKeptSession' re-grounds (ac8ab8d5f, 794a0f5fb, ff44fb2a2) spell the catalogue-default read, the policy and sibling-kit reads, the leg declarations and the loop render differently from what this spec assumed, or apply a rule it breaks; the re-ground session was asked to re-ground this build before the dependent spec runs start, and no code has started.
- **Evidence:** `memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`, and the rev-3 line in this spec's §9.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dFurnishedOrders/prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-46-1-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dFurnishedOrders-21
- **Caused-by:** 2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck

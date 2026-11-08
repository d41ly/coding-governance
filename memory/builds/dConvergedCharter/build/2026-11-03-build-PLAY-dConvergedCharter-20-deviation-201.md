# PLAY-dConvergedCharter-20 deviation 201 — the widened exit check grades every row of the adopter register, an unregistered one passing only on an owner item

**Serves:** deviation PLAY-dConvergedCharter-20

- **Departs from:** cl-dClosedLoop-0494@eb095d63
- **Hand-off:** design-to-spec
- **Before:** the exit check widened: every registered adopter at the converged commit with no step pending, or an owner item for that adopter.
- **After:** the exit check widened: every row of the adopter register, a registered adopter at the converged release passing with no step pending or on an open owner item for that adopter, and an unregistered one passing only on an open owner item for it; an empty register is not graded.
- **Cause:** design defect
- **Reason:** no row of `tools/govkit/adopters.toml` is registered at base (DEPL-dShippedRelease-31 S2 reads `registered` only where `remote`, `branch` and `grant` are all present, and no row holds one), so the clause's population is empty until the owner acts. An exit check over an empty population either reads green over nothing, which the charter's `[gate]` rule refuses, or never reads at all. Grading every row, and asking an owner item of an unregistered one, keeps the clause's registered case as written and makes each unregistered adopter the owner's turn rather than an absence (PLAY-dConvergedCharter-20 §8 F1). The owner item is the one unit 5 raises, `adopter-unmigrated`, so no new item is minted for it.
- **Evidence:** the clause, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:40`; the register at base, `tools/govkit/adopters.toml:16-25`; scout D's row for cl-0479, `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md:13`
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dConvergedCharter's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0494@eb095d63
- **Caused-by:** PLAY-dConvergedCharter-20

# DEPL-dShippedRelease-24 deviation 241 — under `managed` the project's entries stay, so the guards sit in both tiers

**Serves:** deviation DEPL-dShippedRelease-24

- **Departs from:** `cl-dClosedLoop-0434@df3486aa` [install.guards]
- **Hand-off:** design-to-spec
- **Before:** `install.guards`: the core guards installed into the project's settings, or into managed settings where the operator opts in (NP-20)
- **After:** `install.guards`: the core guards installed into the project's settings, and also into managed settings where the operator opts in, the project's entries staying as the floor on any node whose operator has not
- **Cause:** design defect
- **Reason:** The clause reads as a choice of one home. The key is a committed value and managed settings are per-machine, so a repository setting `managed` would take the guards out of its project settings on every node, and any node whose operator has not installed the managed file would then run with no guard. `tools/hooks/README.md` calls a guard silently off the one failure mode a wiring move must avoid. Keeping the project's entries loses nothing: the harness keys hook dedup on the root and the command, so a guard in both tiers fires once, and the managed entry is what the project cannot edit, which is the gap the clause closes (DEPL-dShippedRelease-24 §8 F2).
- **Evidence:** the clause, `memory/builds/dShippedRelease/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:44`; the gap, `gap-deploy-14` at the same file's Gaps section; the wiring rule, `tools/hooks/README.md` "Migrating an installed tree"; the harness's dedup and its managed tier, read from Claude Code 2.1.292 on node d on 2026-10-30, DEPL-dShippedRelease-24 §8 F1
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value; carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0434@df3486aa
- **Caused-by:** DEPL-dShippedRelease-24
